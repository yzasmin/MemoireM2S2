# Journal de bord — Copilote Financier Angelotti

Une entrée par étape. Chaque entrée : résumé en une ligne, puis leçons
apprises et sources mobilisées (cours + concepts).

---

## Étape 1 — Cadrage du projet

**Résumé : le Copilote Financier est cadré en trois axes (risque de marge,
vitesse d'écoulement, optimisation de prix) + un axe transverse texte/réseau,
adossés aux 4 exports de gestion et à 3 sources externes publiques.**

- La demande métier est reformulée en cibles modélisables : taux de variation
  de la marge (régression + classification), réservations mensuelles par
  opération (panel + séries temporelles), prix hédonique et recommandation
  sous contrainte (optimisation).
- Leçon : formaliser le problème AVANT de toucher aux données, comme le
  recommande la checklist « Comprendre le problème » du cours d'EDA
  (*EDA_for_Data_Science.pdf*, p. 3 : dictionnaire `problem` avec objectif,
  cible, métrique, contraintes).
- Livrables : `docs/01_cadrage_projet.md`, `docs/03_besoins_metier.md`.

## Étape 2 — Référentiel des cours

**Résumé : lecture intégrale des 9 PDF de cours et extraction des notations
exactes dans `docs/reference_cours.md`, pour utiliser le formalisme des cours
et non un formalisme générique.**

- Leçon 1 : les cours divergent entre eux sur les notations (paramètres $w$
  dans *optim.pdf*, $\theta$ dans *regularization.pdf*, $\beta$ dans
  *SeriesTemp_ARIMAX*) — chaque notebook cite le cours dont il suit la
  notation.
- Leçon 2 : certains concepts demandés (PCA, Naive Bayes, softmax, KL,
  multiplicateur de Lagrange, z-score en formule) ne sont PAS formalisés
  dans les PDF : ils seront introduits avec une source externe classique
  (Azencott, *Introduction au Machine Learning*, déjà cité par les cours
  de classification comme référence) et raccrochés aux notions voisines des
  cours (ex. PCA ↔ SVD de *regularization.pdf* p. 26 ; entropie ↔ arbres
  slide 16).
- Leçon 3 : *SeriesTemp_ARIMAX* impose une distinction stricte $\eta_t$
  (erreur de régression autocorrélée) vs $\varepsilon_t$ (bruit blanc) — à
  respecter dans l'axe B.

## Étape 3 — Exploration et nettoyage des données brutes

**Résumé : les 4 exports Excel sont compris, nettoyés et chargés dans une
base SQLite (7 tables, 3 vues SQL) par un pipeline reproductible
(`src/nettoyage.py`, `src/base_sql.py`).**

- Découverte 1 : « 06_Informations Lots » ne contient QUE les dossiers
  désistés (2 164 lignes) — c'est un export de détail des désistements, pas
  la table des lots. La table maîtresse est la Grille de Prix (16 467
  lignes lot × dossier, 196 opérations).
- Découverte 2 : « Budget & EFR » affiche 65 000 lignes rondes, ce qui
  ressemblait à une troncature d'export ; la réconciliation avec le fichier
  LIVE (79 106 lignes, hiérarchie niveaux 0-3) montre un écart médian NUL
  sur les 118 opérations jointes : le fichier est complet (64 788 postes de
  niveau 3 + 212 lignes de synthèse). Leçon : toujours réconcilier deux
  sources qui décrivent le même objet avant d'en écarter une.
- Découverte 3 : la marge est calculable par opération (Recettes −
  Dépenses, budget vs engagé/facturé) ; 144 opérations sont assez avancées
  (engagement > 30 %) pour l'apprentissage supervisé de l'axe A — petit
  échantillon assumé, qui oriente vers des modèles régularisés (cf.
  *regularization.pdf*, guide de choix p. 33-34).
- Nettoyages notables : natures de lot harmonisées (`appt`/`Appartement`,
  `stat`/`Parking extérieur` → 8 familles), doublons orthographiques de
  communes fusionnés (91 → 90), surfaces et prix à 0 convertis en
  manquants (valeurs sentinelles, cf. démarche qualité de
  *EDA_for_Data_Science.pdf* p. 3-4), retours chariot `_x000d_` purgés des
  commentaires.
- Sources : *EDA_for_Data_Science.pdf* (checklist qualité) ; module bases
  de données SQL (schéma en étoile, vues, index dans `src/base_sql.py`).

## Étape 4 — Données externes

**Résumé : trois sources publiques ajoutées par scripts reproductibles :
taux des crédits habitat France (BCE), confiance des ménages (Eurostat),
référentiel communes avec population et coordonnées (geo.api.gouv.fr).**

- Le besoin vient de l'axe B : le rythme de vente dépend du contexte macro
  (la remontée des taux 2022-2023 de 1,1 % à ~4 % coïncide avec la chute
  des réservations observée dans la grille) — ces séries seront les
  variables exogènes $x_{k,t}$ de l'ARIMAX (*SeriesTemp_ARIMAX*, slides 1-8).
- La distance au littoral est dérivée des coordonnées geo.api.gouv.fr :
  proxy simple de l'attractivité « bord de mer » du portefeuille (Canet,
  Cap d'Agde, Sérignan…).
- Leçon : préférer des séries publiques re-téléchargeables par script à des
  valeurs recopiées à la main (traçabilité exigée par la démarche EDA du
  cours : « traçable : résultats sauvegardés, décisions documentées », p. 9).
