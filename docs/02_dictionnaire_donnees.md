# Dictionnaire des données — Copilote Financier

Ce document décrit les tables **propres** de la base `data/copilote.db`,
produites par `src/nettoyage.py` + `src/base_sql.py` à partir des 4 exports
bruts de `donnéebrut/` et des données externes de `data/externe/`.

## Constats sur les données brutes (issus de l'exploration)

1. **« 06_Informations Lots » n'est pas la table des lots** : les 2 164
   lignes sont toutes des dossiers *désistés* (2 157 « Désisté » + 7
   « Résolution de vente »). C'est un export de détail des désistements,
   avec des informations client absentes ailleurs (nationalité, date de
   naissance, canal de vente, commission).
2. **« Budget & EFR » n'est pas tronqué** malgré ses 65 000 lignes rondes :
   64 788 lignes de postes analytiques de niveau 3 + 212 lignes de synthèse
   sans sens Dépenses/Recettes (marge, intérêts…). La réconciliation avec
   `A_DM_BUDGET_MONTANT_GESTION_LIVE` (hiérarchie niveaux 0-3) donne un
   écart médian **nul** sur les 118 opérations jointes par `GR_xxx` : les
   deux fichiers décrivent le même budget ; on garde Budget & EFR (libellés
   de postes hiérarchisés) et on écarte le LIVE (redondant).
3. **La grille de prix est au grain lot × dossier** : un lot désisté puis
   revendu apparaît plusieurs fois. D'où la séparation en une table `lots`
   (état physique, dossier le plus récent) et une table `ventes`
   (événements).
4. **Libellés hétérogènes** : natures de lot (`appt` / `Appartement`,
   `stat` / `Parking extérieur`…) harmonisées en 8 familles ; communes en
   double orthographe (`LATOUR BAS ELNE` / `LATOUR-BAS-ELNE`) normalisées
   (91 orthographes → 90 communes).
5. **Valeurs sentinelles** : surfaces et prix à 0 pour les stationnements et
   lots non déployés → convertis en manquants (`NULL`) plutôt que traités
   comme des zéros réels ; retours chariot Excel `_x000d_` nettoyés dans les
   commentaires.

## Clés de jointure

- `id_operation` relie toutes les tables internes (196 opérations dans la
  grille ⊂ 267 dans le budget ; les opérations « En étude » n'ont pas encore
  de grille de prix).
- `operations.commune_norm` → `communes.commune_norm` (nom normalisé sans
  accents ni tirets).
- `strftime('%Y-%m', ventes.date_reservation)` → `conjoncture.mois`.

## Vues SQL métier (définies dans `src/base_sql.py`)

- `v_marge_operation` : recettes/dépenses budgétées vs engagées/facturées et
  taux d'engagement par opération — socle de l'axe A.
- `v_ecoulement_mensuel` : réservations et désistements par opération × mois
  — socle de l'axe B (panel de données répétées).
- `v_stock_lots` : photo du stock par opération — socle de l'axe C.

## Table `operations` — 267 lignes

Référentiel des opérations immobilières (une ligne = une opération / SCCV). Source : Budget & EFR.

| Colonne | Type | % manquant | Exemple |
|---|---|---|---|
| `id_operation` | int64 | 0 % | 30 |
| `code_operation` | str | 0 % | 104 |
| `code_operation_gr` | str | 1 % | GR_104 |
| `libelle` | str | 0 % | PARC DU VALLON |
| `activite` | str | 0 % | Promotion |
| `agence` | str | 0 % | Agence Toulouse  |
| `statut` | str | 0 % | Archivé |
| `type_operation` | str | 0 % | Promotion neuf |
| `commune` | str | 0 % | TOULOUSE |
| `code_postal` | int64 | 0 % | 31000 |
| `societe` | str | 1 % | PARC DU VALLON |
| `forme_juridique` | str | 1 % | SCCV |
| `commune_norm` | str | 0 % | TOULOUSE |

## Table `budget` — 64788 lignes

Lignes budgétaires analytiques de niveau 3 (une ligne = un poste de coût ou de recette d'une opération). Source : Budget & EFR, hors 212 lignes de synthèse.

| Colonne | Type | % manquant | Exemple |
|---|---|---|---|
| `id_operation` | int64 | 0 % | 30 |
| `sens` | str | 0 % | D |
| `poste_niv1` | str | 0 % | COMMERCIALISATION |
| `poste_niv2` | str | 0 % | Aides à la vente |
| `poste_niv3` | str | 0 % | Autres frais offerts |
| `budget_ht` | float64 | 0 % | 0.0 |
| `pre_engage_ht` | float64 | 0 % | 0.0 |
| `engage_ht` | float64 | 0 % | 0.0 |
| `facture_ht` | float64 | 0 % | 0.0 |
| `regle_ht` | float64 | 0 % | 0.0 |

## Table `lots` — 14123 lignes

Lots physiques avec attributs et prix (une ligne = un lot, état au dossier le plus récent). Source : Grille de Prix.

| Colonne | Type | % manquant | Exemple |
|---|---|---|---|
| `id_operation` | int64 | 0 % | 29 |
| `numero_lot` | str | 0 % | 2-0001 |
| `nature_lot_source` | str | 0 % | Appartement |
| `type_lot` | str | 0 % | 2 Pièces |
| `type_produit` | str | 0 % | SOCIAL |
| `type_ouvrage` | str | 0 % | Collectif social |
| `principal_secondaire` | str | 0 % | Principal |
| `surface` | float64 | 39 % | 42.0 |
| `surface_habitable` | float64 | 0 % | 42.0 |
| `surface_terrain` | float64 | 0 % | 0.0 |
| `surface_balcon` | float64 | 0 % | 0.0 |
| `surface_terrasse` | float64 | 0 % | 0.0 |
| `exposition` | str | 79 % | S |
| `etage` | str | 17 % | 0 |
| `statut_lot` | str | 0 % | Désisté |
| `prix_budget_ttc` | float64 | 0 % | 102522.0 |
| `prix_lancement_ttc` | float64 | 0 % | 0.0 |
| `prix_vente_ttc` | float64 | 13 % | 1999172.25 |
| `remise_ttc` | float64 | 14 % | 0.0 |
| `taux_tva` | float64 | 0 % | 0.055 |
| `nature_lot` | str | 0 % | Appartement |
| `prix_m2_ttc` | float64 | 39 % | 47599.33928571428 |

## Table `ventes` — 14428 lignes

Événements commerciaux (une ligne = un dossier de réservation, désisté ou non). Source : Grille de Prix, lignes avec dossier.

| Colonne | Type | % manquant | Exemple |
|---|---|---|---|
| `id_operation` | int64 | 0 % | 37 |
| `numero_lot` | str | 0 % | A08 |
| `code_dossier` | str | 0 % | GR_2219 |
| `statut_dossier` | str | 0 % | Livré |
| `date_reservation` | str | 0 % | 2019-03-25 00:00:00 |
| `date_desistement` | str | 85 % | 2022-11-30 00:00:00 |
| `date_vente` | str | 19 % | 2019-09-02 00:00:00 |
| `date_vente_contractuelle` | str | 24 % | 2019-12-30 00:00:00 |
| `date_livraison` | str | 36 % | 2021-06-10 00:00:00 |
| `date_accord_pret` | object | 100 % |  |
| `date_demande_pret` | str | 100 % | 2024-02-15 00:00:00 |
| `motif_desistement` | str | 86 % | Rétractation dans les 10 jours |
| `commentaire_vente` | str | 33 % | 10 Lots + 10 Pkg en PLUS |
| `origine_contact` | str | 99 % | Autres origines |
| `nom_vendeur` | str | 22 % | FASTRE Guillaume |
| `vendeur_interne_externe` | str | 38 % | Vendeur interne |
| `type_acquereur` | str | 13 % | tiers physique |
| `qualite_acquereur` | str | 5 % | Accédant |
| `code_postal_client` | str | 59 % | 30121 |
| `prix_vente_ttc` | float64 | 0 % | 10000.0 |
| `desiste` | int64 | 0 % | 0 |
| `delai_resa_vente_j` | float64 | 19 % | 161.0 |

## Table `desistements` — 2164 lignes

Détail client / canal / commission des dossiers désistés. Source : 06_Informations Lots.

| Colonne | Type | % manquant | Exemple |
|---|---|---|---|
| `id_operation` | int64 | 0 % | 62 |
| `numero_lot` | str | 0 % | 317 |
| `id_dossier` | str | 0 % | GR_3938 |
| `statut` | str | 0 % | Désisté |
| `motif_desistement` | str | 9 % | Rétractation dans les 10 jours |
| `canal_vente` | str | 6 % | VA |
| `vendeur_interne_externe` | str | 84 % | Vendeur interne |
| `taux_commission` | float64 | 5 % | 0.0682470784641068 |
| `montant_commission` | float64 | 5 % | 45862.0367278798 |
| `commentaire_vente` | str | 31 % | FRAIS DE NOTAIRE OFFERTS - Plis SRU non retir |
| `qualite_acquereur` | str | 1 % | Client investisseur |
| `nationalite_client` | str | 12 % | FRANCE |
| `code_postal_client` | str | 13 % | 79000 |
| `date_naissance_client` | str | 96 % | 1982-11-27 00:00:00 |
| `date_reservation` | str | 0 % | 2022-07-25 00:00:00 |
| `date_desistement` | str | 0 % | 2022-11-30 00:00:00 |
| `age_client` | float64 | 96 % | 41.7 |
| `delai_resa_desist_j` | float64 | 0 % | 128.0 |

## Table `communes` — 90 lignes

Référentiel des communes des opérations : population, coordonnées, distance au littoral. Source : geo.api.gouv.fr.

| Colonne | Type | % manquant | Exemple |
|---|---|---|---|
| `commune_source` | str | 0 % | TOULOUSE |
| `nom_insee` | str | 0 % | Toulouse |
| `code_insee` | str | 0 % | 31555 |
| `departement` | str | 0 % | 31 |
| `population` | float64 | 0 % | 514819.0 |
| `longitude` | float64 | 0 % | 1.4328 |
| `latitude` | float64 | 0 % | 43.6007 |
| `commune_norm` | str | 0 % | TOULOUSE |
| `dist_littoral_km` | float64 | 0 % | 124.0 |
| `littoral` | int64 | 0 % | 0 |

## Table `conjoncture` — 138 lignes

Séries macroéconomiques mensuelles : taux crédit habitat (BCE) et confiance des ménages (Eurostat).

| Colonne | Type | % manquant | Exemple |
|---|---|---|---|
| `mois` | str | 0 % | 2015-01 |
| `taux_credit_habitat` | float64 | 0 % | 2.55 |
| `confiance_menages` | float64 | 0 % | -13.6 |
