# Copilote Financier — Groupe Angelotti

**Mémoire de fin d'études M2 MIASHS — Yasmina Saoudy**

Outil d'aide à la décision pour un promoteur-aménageur immobilier (Groupe
Angelotti, filiale Nexity), construit sur les données de gestion réelles de
l'entreprise. Trois axes :

- **A. Risque de marge** — détecter les opérations dont la marge dérive par
  rapport au budget d'engagement ;
- **B. Vitesse d'écoulement** — prédire le rythme de réservation en fonction
  de l'économie (taux 2026, confiance des ménages) et de la localisation ;
- **C. Optimisation des prix** — recommander des ajustements de prix du
  stock sous contrainte d'écoulement.

## Arborescence

```
donnéebrut/            4 exports Excel du système de gestion (point de départ)
Cours/                 9 PDF de cours (le formalisme utilisé partout)
data/externe/          taux BCE, confiance Eurostat, communes geo.api.gouv.fr
src/
  nettoyage.py         exports bruts -> 7 tables propres
  base_sql.py          -> data/copilote.db (SQLite, schéma en étoile, 3 vues SQL)
  theme_viz.py         thème graphique commun (palette validée)
  nb_outils.py         générateur/exécuteur de notebooks
  nb_specs/            source de chaque notebook (reproductible)
notebooks/             7 notebooks EXÉCUTÉS, une étape de la démarche chacun
plateforme/app.py      application Streamlit (le « Copilote » utilisable)
docs/                  cadrage, dictionnaire de données, besoins métier,
                       référence des notations des cours
journal_de_bord.md     leçons apprises, une entrée par étape
```

## Les notebooks (exécutables sur Google Colab)

Chaque notebook s'ouvre dans Colab (la première cellule clone le dépôt et
reconstruit la base) ou en local. Ils sont commités **avec leurs sorties
exécutées** : chaque chiffre commenté correspond à une cellule réellement
exécutée.

| Notebook | Étape | Concepts et modules mobilisés |
|---|---|---|
| `00_exploration_donnees` | EDA | checklist EDA du cours, distribution normale, z-score, IQR, corrélation de Pearson, entropie, anti-fuite |
| `01_preparation_sql_spark` | Ingestion | SQL (jointures, vues, fenêtres), PySpark (paresse, MapReduce, comparaison honnête avec pandas) |
| `02_analyse_multidimensionnelle` | Typologie | PCA à la main (valeurs/vecteurs propres, Lagrange), SVD, similarité cosinus, K-moyennes (Lloyd), CAH de Ward, silhouette, Davies-Bouldin |
| `03_prediction_marge` | Axe A | OLS (forme close + MLE), descente de gradient (pas 1/L), Ridge/Lasso (CV), sigmoïde/log-perte, SVM (charnière, marge, VC), arbres (Gini/entropie), forêt (OOB), softmax, ReLU, F1 |
| `04_vitesse_ecoulement` | Axe B | modèle à effets aléatoires (panel, ICC), ARIMAX (η_t vs ε_t, Ljung-Box, AICc), scénarios de taux 2026, régression non linéaire (sigmoïde d'écoulement) |
| `05_optimisation_prix` | Axe C | modèle hédonique OLS (R² test 0,89), élasticité, multiplicateur de Lagrange (solution analytique), montée de gradient projetée vs SLSQP |
| `06_texte_et_reseau` | Transverse | TF-IDF (formules du cours), moteur cosinus, Naive Bayes (anti-fuite), entropie, KL divergence, graphe biparti vendeurs-opérations |

Régénérer un notebook : `python src/nb_specs/nbXX_*.py` (le script construit
et ré-exécute le notebook de bout en bout).

## Tout lancer depuis Google Colab (poste sans droits d'installation)

Le dépôt étant privé, il faut un **token GitHub en lecture seule** :
github.com → *Settings* → *Developer settings* → *Fine-grained personal
access tokens* → *Generate new token* → limiter au dépôt `MemoireM2S2`,
permission *Contents : Read-only*. Ensuite :

- **Notebooks 00-06** : sur [colab.research.google.com](https://colab.research.google.com),
  onglet *GitHub*, coche « dépôts privés » et autorise ton compte, choisis
  `yzasmin/MemoireM2S2` et la branche `claude/copilote-financier-angelotti-72c614`,
  puis ouvre n'importe quel notebook. Sa première cellule clone le dépôt
  (colle le token quand il est demandé) et reconstruit la base.
- **Plateforme Streamlit** : ouvre `notebooks/99_lancer_plateforme_colab.ipynb`
  de la même façon et exécute ses 3 cellules — la dernière affiche une URL
  publique temporaire vers l'application. Ne partage pas cette URL (données
  internes) et arrête la session Colab après usage.

## Reproduire de zéro

```bash
pip install -r requirements.txt
python src/base_sql.py                 # exports bruts + externes -> copilote.db
python src/nb_specs/nb00_exploration.py   # (idem pour 01..06)
streamlit run plateforme/app.py        # la plateforme
```

Java ≥ 17 est requis pour la partie PySpark du notebook 01.

## Résultats clés (tous vérifiés dans les notebooks)

- **Axe A** : 123 opérations mûres ; 28 % en dérive matérielle (> 2 % de la
  marge) ; classification F1 ≈ 0,30-0,34 (baseline 0) — système d'alerte
  précoce, honnêtement partiel (R² test 0,08 : la structure budgétaire
  prédispose, l'aléa de chantier décide).
- **Axe B** : +1 point de taux d'intérêt ⇒ **−19 % de réservations
  mensuelles** (panel à effets aléatoires, p < 10⁻¹⁵, ICC 0,66) ; scénarios
  2026 : détente à 2,5 % ⇒ +6 % de rythme, remontée à 3,5 % ⇒ −3 %.
- **Axe C** : prix hédonique R² test 0,886 ; à élasticité −1, la remise
  optimale sous contrainte d'écoulement est **uniforme en euros**
  (multiplicateur de Lagrange λ* ≈ −23 k€ sur l'opération test) ; 24 lots
  du stock signalés hors marché (±1 RMSE).
- **Transverse** : Naive Bayes sur commentaires F1 0,34 (fuite contrôlée) ;
  la KL divergence révèle un défaut de saisie d'agence (90 % de motifs
  « Autres ») ; 2 vendeurs concentrent 52 % des dossiers.
