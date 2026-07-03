# Cadrage du projet — Copilote Financier Groupe Angelotti

**Mémoire M2 MIASHS — Yasmina Saoudy — 2025/2026**

## 1. Contexte

Le Groupe Angelotti est un promoteur-aménageur immobilier implanté en
Occitanie et en Provence (agences Béziers, Montpellier, Toulouse, Aix),
filiale du groupe Nexity. Son activité : acheter du foncier, concevoir des
programmes (appartements, terrains à bâtir, stationnements), les
commercialiser en VEFA, puis les livrer.

Chaque opération immobilière est une petite entreprise à part entière
(SCCV dédiée) : un budget prévisionnel est posé en amont (foncier, VRD,
construction, honoraires, commercialisation… contre recettes attendues),
puis la vie de l'opération fait dériver ce budget — appels d'offres plus
chers que prévu, rythme de vente plus lent, désistements d'acquéreurs,
remises commerciales. La direction financière pilote aujourd'hui ces dérives
avec des tableaux Excel, opération par opération, sans vision statistique
transverse.

## 2. Problème métier

Trois questions reviennent en comité d'engagement et en revue de gestion :

1. **Quelles opérations vont déraper financièrement ?** La marge budgétée
   à l'engagement est-elle tenable, et peut-on détecter tôt les opérations
   « à risque » ?
2. **À quel rythme le stock va-t-il s'écouler ?** Le rythme de réservation
   dépend du contexte macroéconomique (taux d'intérêt des crédits habitat,
   moral des ménages), de la localisation et du produit. Or 2023-2024 a
   montré la violence de ce lien : la remontée des taux de 1 % à 4 % a
   divisé la demande.
3. **À quel prix vendre chaque lot ?** Trop cher, le lot reste en stock et
   génère des frais financiers ; pas assez cher, la marge fond. Les remises
   sont aujourd'hui accordées au cas par cas, sans règle.

## 3. Objectif : le Copilote Financier

Un outil d'aide à la décision en trois axes, adossé aux données de gestion
réelles de l'entreprise :

| Axe | Question | Cible modélisée | Familles de modèles |
|---|---|---|---|
| A — Risque de marge | Quelles opérations dérapent ? | Taux de variation de la marge (budget → réalisé) ; classe de risque | Régression (OLS, Ridge), classification (logistique, SVM, Naive Bayes, arbres) |
| B — Vitesse d'écoulement | Combien de réservations par mois ? | Nombre de réservations mensuelles par opération ; délais | Modèle à effets aléatoires (panel), ARIMAX (exogènes macro), courbe logistique |
| C — Optimisation de prix | Quel prix pour quel lot ? | Prix hédonique au m² ; recommandation sous contrainte de marge | OLS hédonique, optimisation sous contrainte (Lagrange, descente de gradient) |

Un axe transverse exploite les **données textuelles** (9 688 commentaires de
vente, motifs de désistement) et le **réseau de commercialisation**
(vendeurs ↔ opérations) pour enrichir la détection de risque.

## 4. Données disponibles

Quatre exports du système de gestion (voir `docs/02_dictionnaire_donnees.md`) :

| Export | Grain | Volumétrie | Usage principal |
|---|---|---|---|
| Grille de Prix Avec Desistements | lot × dossier | 16 467 lignes, 196 opérations | Ventes, prix, dates, désistements |
| Budget & EFR | poste analytique niv. 3 | 64 788 lignes, 267 opérations | Budget vs engagé vs facturé → marge |
| A_DM_BUDGET_MONTANT_GESTION_LIVE | poste (hiérarchie 0-3) | 79 106 lignes | Contrôle de cohérence du budget |
| 06_Informations Lots | dossier désisté | 2 164 lignes | Détail client/canal des désistements |

Données externes ajoutées (sources publiques, scripts reproductibles) :

- **Taux des crédits habitat France**, mensuel 2015-2026 — BCE, série
  `MIR.M.FR.B.A2C.AM.R.A.2250.EUR.N` (`data/externe/taux_credit_habitat_france.csv`) ;
- **Confiance des ménages France**, mensuel 2015-2026 — Eurostat
  `ei_bsco_m` / BS-CSMCI (`data/externe/confiance_menages_france.csv`) ;
- **Référentiel communes** : population, département, coordonnées —
  geo.api.gouv.fr (`data/externe/communes_geo.csv`), enrichi d'une distance
  au littoral calculée.

## 5. Architecture technique

```
donnéebrut/ (4 exports Excel)          data/externe/ (BCE, Eurostat, geo.api)
        │                                       │
        └────────► src/nettoyage.py ◄───────────┘
                        │      harmonisation, typage, dédoublonnage
                        ▼
               src/base_sql.py ──► data/copilote.db (SQLite)
                                    7 tables + 3 vues SQL métier
                        │
        ┌───────────────┼───────────────────────────┐
        ▼               ▼                           ▼
  notebooks/      src/features.py            plateforme/ (Streamlit)
  00 → 06         jeux de données ML         3 pages = 3 axes + accueil
  (démarche       (marge, écoulement,        modèles entraînés (joblib)
  pas à pas)      prix hédonique)
```

- **notebooks/** : un notebook par étape de la démarche (exécutables sur
  Google Colab, une cellule d'amorçage clone le dépôt) ;
- **plateforme/** : application Streamlit qui consomme la base SQLite et
  les modèles entraînés — le « Copilote » utilisable par un contrôleur de
  gestion ;
- **journal_de_bord.md** : leçons apprises, une entrée par étape.

## 6. Démarche et correspondance avec les modules du master

| Notebook | Étape | Modules et concepts mobilisés |
|---|---|---|
| 00_exploration_donnees | EDA | Intro science des données, EDA ; distribution normale, z-score, corrélation de Pearson, entropie |
| 01_preparation_sql_spark | Ingestion, SQL, passage à l'échelle | Bases SQL ; données massives (PySpark, parallélisation) |
| 02_analyse_multidimensionnelle | Structure des opérations | Analyse multidimensionnelle : PCA (valeurs/vecteurs propres, multiplicateur de Lagrange), SVD, similarité cosinus ; classification non supervisée (k-means, CAH) |
| 03_prediction_marge | Axe A | Régression linéaire OLS (MLE, R², MSE), descente de gradient, régularisation ; classification supervisée : logistique (sigmoïde, log-loss, softmax), Naive Bayes, SVM (fonctions de décision linéaires, dual de Lagrange), arbres ; F1, KL divergence ; ReLU (perceptron multicouche) |
| 04_vitesse_ecoulement | Axe B | Données répétées (modèle à effets aléatoires sur panel opération × mois) ; données séquentielles temporelles (ARIMAX avec taux d'intérêt exogène) ; régression non linéaire (courbe logistique d'écoulement) |
| 05_optimisation_prix | Axe C | OLS hédonique, élasticité ; optimisation sous contrainte (multiplicateur de Lagrange), descente de gradient projetée |
| 06_texte_et_reseau | Axe transverse | Données séquentielles textuelles (TF-IDF, similarité cosinus, Naive Bayes, entropie) ; analyse de réseaux sociaux (graphe biparti vendeurs-opérations, centralités, communautés spectrales) |

## 7. Périmètre et limites assumées

- Les données budgétaires sont une **photo à date d'export** (pas
  d'historique de révisions) : le « taux de variation de marge » compare le
  budget initial au réalisé (engagé/facturé) à cette date. Les opérations
  trop peu avancées (taux d'engagement < 60 %) sont exclues de
  l'apprentissage supervisé de l'axe A.
- 267 opérations, dont 123 exploitables pour l'axe A (engagement ≥ 60 %,
  marge budgétée > 50 k€, recettes budgétées > 0, cf. notebook 03 §1) :
  petit échantillon,
  d'où la préférence pour des modèles simples, régularisés et validés en
  validation croisée, et une lecture prudente des intervalles.
- Les recommandations de prix (axe C) sont des aides à la décision, pas des
  prix opposables : l'élasticité est estimée sur données historiques
  agrégées.
