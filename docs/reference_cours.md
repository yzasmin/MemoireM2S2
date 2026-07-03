# Référence des cours M2 MIASHS — Notations et concepts par PDF

> Document de référence construit à partir de la lecture intégrale des 9 PDF du dossier `Cours/`.
> **Objectif** : pour chaque concept, recopier la **notation exacte du cours** (LaTeX fidèle) avec le
> numéro de page, afin de réutiliser le formalisme du cours dans le mémoire, et non un formalisme générique.
>
> **Convention de pagination** : pour les documents de type « polycopié » (LaTeX, EDA, régression, optim,
> regularization, course), les numéros renvoient au numéro de page **imprimé** en bas de page. Pour les
> diaporamas (arbres de décision, clustering, ARIMAX, text retrieval), les numéros renvoient au numéro de
> **slide imprimé** en bas à droite (les slides à apparition progressive partagent le même numéro).

---

## Table de correspondance rapide concepts → cours

| Concept | Cours où il est traité (principal en gras) |
|---|---|
| Gradient Descent (GD, SGD, mini-batch, momentum, Nesterov, Newton, coordinate descent) | **optim.pdf** |
| Distribution Normale | Marginal : bruit blanc gaussien implicite (SeriesTemp), priors gaussiens BayesianRidge (modèle_de_régression p. 6), processus gaussiens (modèle_de_régression p. 9). Pas de chapitre dédié. |
| Z-Score | **EDA_for_Data_Science.pdf** (cité comme outil de détection d'outliers, p. 4 et 6 ; pas de formule donnée) |
| Sigmoïde | **course.pdf** (p. 33–34, $\sigma(t)=\frac{1}{1+e^{-t}}$) |
| Corrélation de Pearson | **EDA_for_Data_Science.pdf** (p. 5, via `df.corr()` ; pas de formule mathématique donnée) |
| Similarité Cosinus | **simialrity_based_text_retrieval_slides.pdf** (slide 12) |
| Naive Bayes | **Absent.** Attention : course.pdf traite le *classifieur/prédicteur de Bayes* $h^*$ (optimal théorique), qui est un concept différent. Ne pas confondre. |
| MLE (maximum de vraisemblance) | **SeriesTemp_ARIMAX_2025.pdf** (slide 3 : maximiser la vraisemblance $\equiv$ minimiser $\sum \hat{\varepsilon}_t^2$) ; **course.pdf** (p. 35 : cross-entropy = log-vraisemblance négative) ; regularization.pdf (p. 5–6, vraisemblance dans le BMA) |
| OLS / moindres carrés | **optim.pdf** (p. 11–12), **modèle_de_régression.pdf** (p. 3) |
| F1 Score | EDA_for_Data_Science.pdf (p. 3 : `"metric": "f1"` dans la checklist métier ; pas de formule) |
| ReLU | modèle_de_régression.pdf (p. 12 : `activation="relu"` dans MLPRegressor et Keras ; pas de formule) |
| Valeurs/vecteurs propres | Implicite : optim.pdf (Hessienne (semi-)définie positive, p. 2–3, 12) ; regularization.pdf (valeurs singulières $\sigma_j$ du SVD, p. 26). Pas de chapitre dédié. |
| R² | **modèle_de_régression.pdf** (p. 3) |
| Softmax | **Absent** (seule la fonction `logsumexp` est mentionnée, regularization.pdf p. 6) |
| MSE | **modèle_de_régression.pdf** (p. 3), **coursClassif-3ArbresDecision.pdf** (slide 17), optim.pdf (p. 11) |
| Entropie | **coursClassif-3ArbresDecision.pdf** (slide 16, entropie comme critère d'impureté) ; course.pdf (cross-entropy, p. 33) |
| KL Divergence | **Absent** |
| Log Loss / perte logistique / cross-entropy | **course.pdf** (p. 32–37), optim.pdf (p. 13), regularization.pdf (p. 16) |
| SVD | **regularization.pdf** (p. 26, effet de rétrécissement de Ridge) |
| Multiplicateur de Lagrange | **Absent** (le SVR est donné sous forme contrainte, modèle_de_régression p. 8, mais sans dérivation lagrangienne) |
| SVM | **course.pdf** (p. 25–26, borne VC), optim.pdf (p. 11, perte hinge), modèle_de_régression.pdf (p. 8, SVR), course.pdf (p. 35, 37 : perte charnière) |
| Régression Linéaire | **modèle_de_régression.pdf**, **optim.pdf** (p. 11–12, 19, 33–34), SeriesTemp (régression + erreurs ARIMA) |
| PCA | **Absent** (l'ACM — analyse des correspondances multiples — est mentionnée pour variables qualitatives, coursClassif-5-Clustering slide 6) |
| Fonctions de décision linéaires | **course.pdf** (p. 24–26, hyperplans, VCdim = d+1, classifieur à marge), coursClassif-3ArbresDecision (slides 4–10, séparateurs linéaires orthogonaux aux axes) |
| ARIMA / ARIMAX / séries temporelles | **SeriesTemp_ARIMAX_2025.pdf** |
| Arbres de décision | **coursClassif-3ArbresDecision.pdf**, modèle_de_régression.pdf (p. 9–10) |
| Clustering (k-means, CAH) | **coursClassif-5-Clustering.pdf** |
| TF-IDF / recherche textuelle | **simialrity_based_text_retrieval_slides.pdf** |
| Régularisation (Ridge/Lasso) | **regularization.pdf** (partie 2), optim.pdf (p. 12–13), modèle_de_régression.pdf (p. 4) |
| EDA | **EDA_for_Data_Science.pdf** |

---

# 1. EDA_for_Data_Science.pdf

## 1.1 Identification
- **Titre** : *Exploration des Données (EDA) pour un Projet de Machine Learning*
- **Auteur** : Georf MIGUIAMA BAMBA, Janvier 2026
- **Langue** : français
- **Nature** : document méthodologique (bonnes pratiques EDA), orienté code Python (pandas/seaborn), **sans formules mathématiques** — les concepts sont opérationnalisés par du code.
- 9 pages.

## 1.2 Concepts couverts
- **EDA** (cœur du document, méthodologie complète en 13 sections).
- **Z-Score** : cité comme méthode de détection de valeurs aberrantes (« Boxplots, IQR, Z-score », p. 4 et p. 6), sans formule.
- **Corrélation (Pearson par défaut de pandas)** : p. 5, `corr = df[num_cols].corr()` + heatmap ; p. 7, corrélation à la cible `df[tmp.columns].corrwith(df[target])` triée par valeur absolue pour détecter la **fuite de cible** (target leakage).
- **F1 Score** : p. 3, apparaît dans la checklist métier : `problem = {"type": "classification", "target": "y", "metric": "f1", "constraints": [...]}` (mention, pas de formule).

## 1.3 Notations / conventions exactes
Pas de LaTeX dans ce cours ; les « notations » sont des conventions de code :
- Outliers via IQR (p. 6) :
  ```python
  Q1 = df[col].quantile(0.25) ; Q3 = df[col].quantile(0.75) ; IQR = Q3 - Q1
  mask_out = (df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)
  ```
  soit, en formule : un point est aberrant si $x < Q_1 - 1.5\,\mathrm{IQR}$ ou $x > Q_3 + 1.5\,\mathrm{IQR}$, avec $\mathrm{IQR} = Q_3 - Q_1$.
- Ratio de valeurs manquantes (p. 4) : `missing_ratio = (df.isnull().mean() * 100)`.
- Résumé univarié « robuste » (p. 4) : `describe().T` enrichi de `missing_%`, `skew`, `kurtosis`.
- Détection avancée d'anomalies (p. 6) : `IsolationForest(contamination=0.01)`, DBSCAN cité.
- Transformations de distributions asymétriques (p. 6) : `np.log1p(x)` (log) et Box-Cox (`scipy.stats.boxcox`, nécessite $x>0$).

## 1.4 Méthodologie recommandée (démarche EDA du cours, à réutiliser telle quelle)
1. **Comprendre le problème** (p. 3) : objectif métier, variables clés (cible et caractéristiques), contraintes (ex : latence, interprétabilité) — formalisé dans un dictionnaire `problem`.
2. **Chargement des données** (p. 3) : `df.head()`, `df.shape`, `df.info()`.
3. **Vérification de la qualité** (p. 3–4) : valeurs manquantes (`df.isnull().sum()`), doublons (`df.duplicated().sum()`), types (`df.dtypes`), outliers (Boxplots, IQR, Z-score), heatmap des valeurs manquantes.
4. **Analyse univariée** (p. 4) : `describe()` + histogrammes pour le numérique ; `value_counts()` + cardinalité pour le catégoriel.
5. **Analyse bivariée** (p. 5) : Numérique vs Numérique → corrélation + scatter plot ; Catégorique vs Numérique → boxplot ; Catégorique vs Catégorique → crosstab.
6. **Ingénierie des caractéristiques** (p. 5–6) : création de variables (ratios, dates → mois/jour de semaine), encodage (one-hot `pd.get_dummies(..., drop_first=True)`, label encoding — « attention : impose un ordre arbitraire »), transformations log/Box-Cox si forte asymétrie.
7. **Détection des valeurs aberrantes** (p. 6) : IQR, puis IsolationForest/DBSCAN en option.
8. **Gestion des valeurs manquantes** (p. 6–7) : (1) drop si faible proportion ; (2) imputation simple (médiane/moyenne pour numérique, mode pour catégoriel) ; (3) imputation prédictive (`KNNImputer(n_neighbors=5)`).
9. **Notions avancées souvent oubliées** (p. 7–8) — section distinctive du cours :
   - **Fuite de cible** : corrélations trop fortes à la cible (`corrwith`).
   - **Déséquilibre de classes** : `value_counts(normalize=True)`.
   - **Split train/test AVANT certaines transformations** : `train_test_split(..., test_size=0.2, random_state=42, stratify=y si y.nunique()<20)` — « Bon réflexe : split avant fit preprocessing ».
   - **Scaling et pipelines pour éviter les fuites** : `Pipeline` + `ColumnTransformer` (imputer médiane + `StandardScaler` pour numérique ; imputer mode + `OneHotEncoder(handle_unknown="ignore")` pour catégoriel), le tout fitté sur le train seulement.
10. **Vérification du dataset final** (p. 8) : shape, manquants, doublons, sauvegarde `cleaned_data.csv`.
11. **Insights et prochaines étapes** (p. 8) : synthèse, problèmes potentiels, plan (sélection de variables, choix du modèle).
12. **Conclusion** (p. 9) : une EDA doit être **structurée** (checklist + étapes reproductibles), **traçable** (résultats sauvegardés, décisions documentées), **orientée métier** (métriques, contraintes, interprétabilité), **sans fuite de données** (split/pipelines).

---

# 2. modèle_de_régression.pdf

## 2.1 Identification
- **Titre** : *Panorama des modèles de régression en Machine Learning (formules, explications, exemples, code Python)*
- **Auteur** : Georf MIGUIAMA BAMBA, 4 février 2026
- **Langue** : français
- 15 pages. Catalogue de ~30 modèles de régression avec formule + code scikit-learn.

## 2.2 Convention de notation générale (p. 3)
Le cours note les **poids $w$** (et non $\beta$ ni $\theta$), le biais $b$, la prédiction $\hat{y}$, le paramètre de régularisation $\lambda$ :

> On cherche une fonction $f : \mathbb{R}^d \to \mathbb{R}$ (ou $\mathbb{R}^m$ en multi-sorties) qui prédit $y$ à partir de $x$ en minimisant une perte sur un jeu d'entraînement $\{(x_i, y_i)\}_{i=1}^n$ :
> $$\min_{f\in\mathcal{F}} \sum_{i=1}^{n} \ell\big(y_i, f(x_i)\big) + \lambda\,\Omega(f)$$
> où $\Omega$ est une régularisation (complexité) et $\lambda \ge 0$.

## 2.3 Concepts et notations exactes

### Métriques d'évaluation (p. 3) — **MSE, RMSE, MAE, R²**
- MSE : $\frac{1}{n}\sum(y-\hat{y})^2$
- RMSE : $\sqrt{\mathrm{MSE}}$
- MAE : $\frac{1}{n}\sum|y-\hat{y}|$
- $R^2 : 1 - \frac{\sum(y-\hat{y})^2}{\sum(y-\bar{y})^2}$

### OLS / Régression linéaire (p. 3)
> **Idée :** modèle linéaire $\hat{y} = w^\top x + b$ en minimisant la MSE :
> $$\min_{w,b} \sum_{i=1}^{n} (y_i - (w^\top x_i + b))^2$$
> **Quand :** baseline, interprétable, rapide, sensible aux outliers et à la colinéarité.

### Régression polynomiale (p. 4)
Transformer $x$ en $\phi(x)$ (monômes) puis OLS/Ridge/Lasso : $\hat{y} = w^\top \phi(x)$.

### Ridge (L2) (p. 4)
$$\min_{w} \sum (y_i - w^\top x_i)^2 + \lambda \|w\|_2^2$$
« Stabilise en présence de colinéarité ; garde tous les coefficients. »

### Lasso (L1) (p. 4)
$$\min_{w} \sum (y_i - w^\top x_i)^2 + \lambda \|w\|_1$$
« Favorise la sparsité (sélection de variables), peut être instable si variables corrélées. »

### Elastic Net (L1 + L2) (p. 4)
$$\min_{w} \sum (y_i - w^\top x_i)^2 + \lambda\Big(\alpha\|w\|_1 + \tfrac{1-\alpha}{2}\|w\|_2^2\Big)$$
« Compromis Lasso/Ridge. »

### Perte de Huber — régression robuste (p. 5)
$$\ell_\delta(r) = \begin{cases} \tfrac{1}{2}r^2 & |r| \le \delta \\ \delta(|r| - \tfrac{1}{2}\delta) & |r| > \delta \end{cases}$$
« Perte quadratique près de 0, linéaire pour grandes erreurs (robuste). » Aussi : RANSAC (ajuste sur inliers), Theil-Sen.

### Régression quantile — perte pinball (p. 6)
$$\ell_\tau(r) = \max(\tau r, (\tau - 1)r)$$

### GLM (p. 7–8)
- Poisson (comptages) : $y \sim \mathrm{Poisson}(\mu), \quad \log \mu = w^\top x$
- Gamma (positif continu) : $y > 0, \quad \log\mu = w^\top x$
- Tweedie : inclut Poisson/Gamma selon `power`.

### SVR — Support Vector Regression (p. 8) — **SVM en régression**
> Epsilon-insensitive loss, kernel possible (RBF, poly...).
> $$\min \frac{1}{2}\|w\|^2 + C\sum (\xi_i + \xi_i')$$
> sous contraintes $|y_i - f(x_i)| \le \epsilon$ + slack.

### Kernel Ridge Regression (p. 8)
$$\min_{f\in\mathcal{H}} \sum (y_i - f(x_i))^2 + \lambda\|f\|_\mathcal{H}^2$$

### Processus gaussiens (p. 9)
Priors sur les fonctions $f \sim \mathcal{GP}(m(x), k(x,x'))$, « donne une moyenne et une incertitude ».

### Arbres de décision et forêts (p. 9–10)
`DecisionTreeRegressor` : « Partitionne l'espace ; minimise MSE (ou MAE) par nœud. » Puis ExtraTree, RandomForest (bagging d'arbres), ExtraTrees ; boosting : GradientBoosting, HistGradientBoosting, AdaBoost (p. 10) ; méta-modèles : Bagging, Voting, Stacking (p. 11).

### Réseaux de neurones et **ReLU** (p. 12)
`MLPRegressor(hidden_layer_sizes=(128, 64), activation="relu", alpha=1e-4, ...)` (« scaling recommandé ») et exemple Keras avec `Dense(128, activation="relu")`, `loss="mse"`, optimiseur Adam.

### GAM (p. 13)
Forme additive : $\hat{y} = \beta_0 + \sum_j f_j(x_j)$ (seule apparition de la notation $\beta_0$ dans ce cours).

### Gradient boosting moderne (p. 13–14)
XGBoost (`reg_alpha` = L1, `reg_lambda` = L2), LightGBM, CatBoost avec hyperparamètres typiques.

## 2.4 Méthodologie recommandée
- **Gabarit commun** (p. 3) : `train_test_split(X, y, test_size=0.2, random_state=42)` + fonction `report` retournant `{"RMSE", "MAE", "R2"}` — toutes les comparaisons de modèles du cours passent par ces trois métriques.
- **Standardisation systématique** : quasi tous les modèles linéaires/noyaux sont dans `make_pipeline(StandardScaler(), ...)`.
- **Aide-mémoire par familles** (p. 14) : Linéaires (OLS, Ridge, Lasso, ElasticNet, SGDRegressor, PLS) ; Robustes (Huber, RANSAC, Theil-Sen) ; Quantiles ; GLM (Poisson, Gamma, Tweedie) ; Noyaux (SVR, Kernel Ridge) ; Bayésien non-param (GP) ; Voisins (KNN) ; Arbres/Forêts ; Boosting (GBDT, HistGBDT, AdaBoost, XGBoost, LightGBM, CatBoost) ; Neural nets ; Splines/GAM ; Méta-modèles (Bagging, Voting, Stacking).
- **Remarque finale** (p. 15) : il n'existe pas de liste exhaustive finie de modèles — on compose features, pertes, régularisations, architectures.

---

# 3. optim.pdf

## 3.1 Identification
- **Titre** : *Optimisation*
- **Module** : MIASHS M1 - Semestre 1
- **Langue** : français
- 36 pages, 3 chapitres : (1) Conditions d'existence d'un minimum ; (2) Fonctions d'optimisation en Machine Learning ; (3) Algorithmes de descente de gradient.

## 3.2 Convention de notation générale
- La variable optimisée est $x \in \mathbb{R}^n$ (chap. 1) puis $x \in \mathbb{R}^d$ ou $w$ (paramètres du modèle) en ML.
- Gradient $\nabla f(x)$, **Hessienne $H_f(x)$**, minimum $x^*$, pas d'apprentissage $\alpha_k$, itérés en exposant parenthésé : $x^{(k)}$, $w^{(k)}$.
- Fonction objectif ML : moyenne de pertes par exemple $f_i$.

## 3.3 Concepts et notations exactes

### Conditions d'optimalité (chap. 1)
- **Minimum local** (Déf. 1.1, p. 1) : $f(x^*) \le f(x), \quad \forall x \in B(x^*, \varepsilon) \cap \Omega$, où $B(x^*,\varepsilon) = \{x \in \mathbb{R}^n : \|x - x^*\| < \varepsilon\}$.
- **Minimum global** (Déf. 1.2, p. 2) : $f(x^*) \le f(x), \ \forall x \in \Omega$.
- **CNO** (Théorème 1.3, p. 2) : si $x^*$ minimum local intérieur, $\nabla f(x^*) = 0$ (point critique / stationnaire).
- **CNSO** (Théorème 1.4, p. 2) : $\nabla f(x^*) = 0$ et $H_f(x^*)$ **semi-définie positive** : $v^\top H_f(x^*) v \ge 0, \ \forall v \in \mathbb{R}^n$.
- **CSSO** (Théorème 1.5, p. 3) : $\nabla f(x^*) = 0$ et $H_f(x^*)$ **définie positive** ($v^\top H_f(x^*) v > 0, \ \forall v \ne 0$) $\Rightarrow$ minimum local strict.
- **Convexité** (Déf. 1.6, p. 3) : $f(\lambda x + (1-\lambda)y) \le \lambda f(x) + (1-\lambda)f(y)$, $\forall x,y \in \Omega, \lambda \in [0,1]$.
- **Convexité et optimalité** (Théorème 1.7, p. 3) : $f$ convexe différentiable $\Rightarrow$ ($\nabla f(x^*)=0 \Rightarrow x^*$ minimum global).
- **Coercivité** (Déf. 1.11, p. 5) : $\lim_{\|x\|\to+\infty} f(x) = +\infty$ ; Théorème 1.12 (p. 6) : $f$ continue et coercive $\Rightarrow$ au moins un minimum global (preuve via ensemble de sous-niveau $S_c = \{x : f(x) \le c\}$, Heine-Borel, bornes atteintes/Weierstrass).
- **Tableau hiérarchie des conditions** (p. 6) : $\nabla f(x^*)=0$ (nécessaire, point critique) ; $H_f(x^*) \ge 0$ (nécessaire, candidat minimum) ; $H_f(x^*) > 0$ (suffisante, minimum local) ; $f$ convexe + $\nabla f(x^*)=0$ (suffisante, minimum global) ; $f$ coercive + continue (suffisante, existence minimum). Avec la mise en garde : « Attention à l'abus de notation avec la Hessienne !!! ».
- Contre-exemples clés (p. 4–5) : $f(x) = x^4 - x^2$ (min globaux sans convexité) ; $f(x)=x^3$ (point critique sans extremum) ; $f(x,y) = x^2 - x^4 - y^4$ (Hessienne SDP en $(0,0)$ mais point selle).

### Structure des objectifs ML (chap. 2, p. 7)
$$f(x) = \frac{1}{n}\sum_{i=1}^{n} f_i(x)$$
où $x \in \mathbb{R}^d$ est le **vecteur de paramètres du modèle**, $n$ le nombre d'exemples, $f_i(x)$ la perte sur l'exemple $i$.
Propriétés de conservation par somme : convexité (Thm 2.1, p. 7), différentiabilité $\nabla f(x) = \frac{1}{n}\sum \nabla f_i(x)$ (Prop 2.2, p. 8), Hessienne $H_f(x) = \frac{1}{n}\sum H_{f_i}(x)$ (Prop 2.3, p. 9), coercivité (Prop 2.4, p. 9), convexité par composition affine $f(x) = g(Mx+b)$ (Thm 2.5, p. 9).

### **SVM — perte hinge** (Exemple 2.5.2, p. 11)
$$f(w) = \sum_{i=1}^n \max(0, 1 - y_i(w^\top x_i + b))$$
convexe car $A_i(w) = y_i w^\top x_i$ est affine en $w$ et $g(t) = \max(0, 1-t)$ est convexe.

### **Moindres carrés / OLS** (Exemple 2.6, p. 11)
> Pour des données $(x_i, y_i)_{i=1}^n$, la fonction de perte est :
> $$f(w) = \frac{1}{2n}\sum_{i=1}^{n} (y_i - w^\top x_i)^2$$
> - $\nabla f(w) = -\frac{1}{n}\sum_{i=1}^n (y_i - w^\top x_i)x_i = \frac{1}{n}(X^\top X w - X^\top y)$
> - $H_f(w) = \frac{1}{n}\sum_{i=1}^n x_i x_i^\top = \frac{1}{n}X^\top X$

**Solution en forme close** (Prop. 2.6.1, p. 11–12) : si $X^\top X$ **inversible** ($\Leftrightarrow \mathrm{rang}(X) = d$),
$$w^* = (X^\top X)^{-1}X^\top y$$

### **Régularisation Ridge** (Prop. 2.6.2, p. 12)
$$f_\lambda(w) = \frac{1}{2n}\sum_{i=1}^{n}(y_i - w^\top x_i)^2 + \frac{\lambda}{2}\,\|w\|_2^2, \quad \lambda > 0$$
1. $f_\lambda$ strictement convexe ; 2. $H_{f_\lambda}(w) = \frac{1}{n}X^\top X + \lambda I_d$ définie positive ; 3. solution unique :
$$w^*_\lambda = \big(X^\top X + n\lambda I_d\big)^{-1} X^\top y$$
(noter le facteur $n$ devant $\lambda$, spécifique à la normalisation $\frac{1}{2n}$ de ce cours).

### **Régression logistique — log-perte** (Exemple 2.7, p. 13)
> Pour des données $(x_i, y_i)_{i=1}^n$ avec $y_i \in \{0,1\}$ :
> $$f(w) = \frac{1}{n}\sum_{i=1}^{n} \log(1 + \exp(-y_i w^\top x_i))$$
> Chaque $f_i$ convexe ; pas de forme fermée pour le minimum.

### Régularisation générique (Exemple 2.8, p. 13–14)
$$f(w) = \frac{1}{n}\sum_{i=1}^n \ell_i(w) + \lambda r(w)$$
- **Ridge** : $r(w) = \|w\|_2^2$ (convexe, différentiable, coercif)
- **Lasso** : $r(w) = \|w\|_1$ (convexe, non différentiable partout)

Non-convexité en deep learning (p. 14) : $f(\theta) = \frac{1}{n}\sum \ell(h_\theta(x_i), y_i)$ « généralement non convexe à cause de la composition non linéaire des couches ».
Gradient $L$-Lipschitz (p. 15) : $\|\nabla g(x) - \nabla g(y)\| \le L\,\|x-y\|, \ \forall x,y \in \mathbb{R}^d$.

### **Descente de gradient** (Algorithme 3.1, p. 16)
$$x^{(k+1)} = x^{(k)} - \alpha_k \nabla f\big(x^{(k)}\big)$$
où $\alpha_k > 0$ est le **pas d'apprentissage** (learning rate) à l'itération $k$.

- **Direction de plus forte descente** (Prop. 3.2, p. 16–17) : $d^* = \arg\min_{\|d\|=1} \nabla f(x)^\top d = -\frac{\nabla f(x)}{\|\nabla f(x)\|}$.
- **Décroissance locale** (Prop. 3.3, p. 17) : par Taylor ordre 1, $f(x - \alpha\nabla f(x)) = f(x) - \alpha\|\nabla f(x)\|^2 + o(\alpha) < f(x)$ pour $\alpha$ assez petit.
- **Choix du pas** (p. 18) : pas constant $\alpha_k = \alpha$ ; recherche linéaire $\alpha_k = \arg\min_{\alpha>0} f(x^{(k)} - \alpha\nabla f(x^{(k)}))$ ; pas décroissant $\alpha_k = \frac{\alpha_0}{k}$ ou $\alpha_k = \frac{\alpha_0}{\sqrt{k}}$.
- **Convergence cas convexe** (Théorème 3.4, p. 19) : $f$ convexe, $L$-lisse, $\alpha_k = \frac{1}{L}$ :
  $$f\big(x^{(k)}\big) - f(x^*) \le \frac{L\|x^{(0)} - x^*\|^2}{2k}$$
  convergence en $\mathcal{O}(\frac{1}{k})$ ; fortement convexe : exponentielle $\mathcal{O}\big(e^{-\mu\frac{k}{L}}\big)$.
- **GD pour moindres carrés** (Exemple 3.5, p. 19) : pour $f(w) = \frac{1}{2n}\|y - Xw\|^2$ :
  $$w^{(k+1)} = w^{(k)} - \frac{\alpha}{n}X^\top\big(Xw^{(k)} - y\big) = w^{(k)} - \frac{\alpha}{n}\sum_{i=1}^n \big(w^{(k)\top}x_i - y_i\big)x_i$$
  Coût par itération $\mathcal{O}(nd)$.

### **Momentum** (Algorithme 3.6, p. 20)
$$v^{(k+1)} = \beta v^{(k)} + \nabla f\big(x^{(k)}\big), \qquad x^{(k+1)} = x^{(k)} - \alpha v^{(k+1)}$$
$\beta \in [0,1)$ coefficient de momentum (typiquement $\beta = 0.9$). Déroulé : $v^{(k)} = \sum_{i=0}^{k-1}\beta^i \nabla f(x^{(k-1-i)})$.

### **Nesterov** (Algorithme 3.8, p. 21)
$$\tilde{x}^{(k)} = x^{(k)} + \beta\big(x^{(k)} - x^{(k-1)}\big), \qquad x^{(k+1)} = \tilde{x}^{(k)} - \alpha\nabla f\big(\tilde{x}^{(k)}\big)$$
Convergence $\mathcal{O}(\frac{1}{k^2})$ pour fonctions convexes (contre $\mathcal{O}(\frac{1}{k})$).

### **SGD** (Algorithme 3.9, p. 21)
À chaque itération $k$ : tirer $i_k \in \{1,\dots,n\}$ uniformément, puis
$$w^{(k+1)} = w^{(k)} - \alpha_k \nabla f_{i_k}\big(w^{(k)}\big)$$
- Coût $\mathcal{O}(d)$ au lieu de $\mathcal{O}(nd)$.
- **Non-biais** (Prop. 3.10, p. 22) : $E\big[\nabla f_{i_k}(w)\big] = \frac{1}{n}\sum \nabla f_i(w) = \nabla f(w)$.
- Variance : $E\big[\|\nabla f_{i_k}(w) - \nabla f(w)\|^2\big]$ ; les itérés oscillent autour du minimum.
- **Convergence SGD** (Prop. 3.11, p. 23) : convexe, $L$-lisse, $\alpha_k = \frac{\alpha}{\sqrt{k}}$ :
  $$E[f(\overline{w}_K)] - f(w^*) = \mathcal{O}\Big(\frac{1}{\sqrt{K}}\Big), \quad \overline{w}_K = \frac{1}{K}\sum_{k=1}^K w^{(k)}$$

### **Mini-batch SGD** (Algorithme 3.12, p. 23–24)
Tirer $\mathcal{B}_k \subset \{1,\dots,n\}$, $|\mathcal{B}_k| = b$ (batch size) :
$$w^{(k+1)} = w^{(k)} - \alpha_k \frac{1}{b}\sum_{i\in\mathcal{B}_k}\nabla f_i\big(w^{(k)}\big)$$
$E[\tilde\nabla f(w)] = \nabla f(w)$ (non biaisé), $\mathrm{Var}[\tilde\nabla f(w)] = \frac{\sigma^2}{b}$ avec $\sigma^2 = E[\|\nabla f_i(w) - \nabla f(w)\|^2]$. Tailles typiques $b \in \{32, 64, 128, 256\}$.

Tableau comparatif (p. 24) : GD $\mathcal{O}(nd)$/iter, convergence $\mathcal{O}(\frac1k)$ ; SGD $\mathcal{O}(d)$, $\mathcal{O}(\frac{1}{\sqrt k})$ ; Mini-batch $\mathcal{O}(bd)$, $\mathcal{O}(\frac{1}{\sqrt{bk}})$.

### Descente par coordonnées (p. 25–28)
Version cyclique (Gauss-Seidel) : $x_i^{(k+1)} \leftarrow \arg\min_{t\in\mathbb{R}} f\big(x_1^{(k+1)},\dots,x_{i-1}^{(k+1)}, t, x_{i+1}^{(k)},\dots,x_d^{(k)}\big)$ — utilise **immédiatement** les valeurs mises à jour. Convergence CD aléatoire : $E[f(x^{(k)})] - f(x^*) = \mathcal{O}(\frac{d}{k})$ (Thm 3.16, p. 27). Solution exacte possible pour le Lasso (p. 28).

### **Méthode de Newton** (p. 29–34)
Taylor ordre 2 : $f(x+v) \approx f(x) + \nabla f(x)^\top v + \frac{1}{2}v^\top H_f(x)v$ ; direction $v^* = -H_f(x)^{-1}\nabla f(x)$ ;
$$x^{(k+1)} = x^{(k)} - H_f\big(x^{(k)}\big)^{-1}\nabla f\big(x^{(k)}\big)$$
Convergence **quadratique** (Thm 3.14, p. 30) : $\|x^{(k+1)} - x^*\| \le C\,\|x^{(k)} - x^*\|^2$ (le nombre de chiffres corrects double à chaque itération, p. 31), contre convergence linéaire $\|x^{(k+1)} - x^*\| \le \rho\|x^{(k)} - x^*\|$, $\rho \in (0,1)$ pour GD (p. 32). Coût : $\mathcal{O}(d^3)$ (inversion Hessienne), stockage $\mathcal{O}(d^2)$, convergence locale seulement (p. 33). Newton sur les moindres carrés converge **en une itération** vers $w^* = (X^\top X)^{-1}X^\top y$ (p. 34).

## 3.4 Méthodes / recommandations pratiques du cours (p. 35–36)
- Récapitulatif : GD (ordre 1, $\mathcal{O}(nd)$, $\mathcal{O}(\frac1k)$) ; SGD (ordre 1, $\mathcal{O}(d)$, $\mathcal{O}(\frac{1}{\sqrt k})$) ; Momentum ($\mathcal{O}(\frac{1}{k^2})$ Nesterov) ; Newton (ordre 2, quadratique) ; BFGS / L-BFGS (quasi-Newton, super-linéaire).
- **En pratique** : petits problèmes ($d < 1000$) → Newton ou BFGS ; problèmes moyens ($d < 10^6$) → L-BFGS ; deep learning ($d > 10^6$, $n > 10^6$) → SGD/mini-batch avec momentum (Adam, etc.).
- On combine souvent : descente de gradient au début (convergence globale), Newton à la fin (vitesse quadratique) (p. 33).

---

# 4. regularization.pdf

## 4.1 Identification
- **Titre** : *Ensembles & Régularisation*
- **Module** : MIASHS M1 - Semestre 1
- **Langue** : français
- 34 pages, 2 parties : (1) Méthodes ensemblistes (p. 1–23) ; (2) Régularisation (p. 23–34).

## 4.2 Convention de notation générale
- Cadre statistique : espaces $\mathcal{X}$ (entrée), $\mathcal{Y}$ (sortie), variables aléatoires $X, Y$, mesure jointe $\mathbb{P}$, prédicteur $h : \mathcal{X}\to\mathcal{Y}$, données $S_n = \{(X_i, Y_i)\}_{i\le n} \sim \mathbb{P}^n$ (p. 1).
- **Risque empirique** (p. 1–2) : $L_n(h) = \frac{1}{n}\sum_{i=1}^n \ell(h(X_i), Y_i)$.
- Dans la partie régularisation, les paramètres sont notés $\theta$ (et non $w$) : $\hat\theta$, $\hat\theta_\lambda$, $\hat\theta_{\mathrm{Ridge}}$, etc.

## 4.3 Partie 1 — Méthodes ensemblistes : notations exactes

### Réduction de variance par agrégation (Théorème 4.1, p. 2)
Agrégation $\hat{y} = \frac{1}{m}\sum_{j=1}^m y_j(x)$. Si $\hat y_{ij} = y(x_j) + \varepsilon_{ij}$ avec bruit **centré** $\mathbb{E}[\varepsilon_{ij}] = 0$ et erreurs **indépendantes** ($\mathbb{E}[\varepsilon_j\varepsilon_k] = 0$, $j\ne k$) :
$$\mathbb{E}\Bigg[\Big(\frac{1}{m}\sum_{j=1}^m \varepsilon_j\Big)^2\Bigg] = \frac{1}{m}\mathbb{E}[\varepsilon^2]$$
« La variance est **réduite d'un facteur $m$** » — effective seulement si les modèles font des erreurs complémentaires.

### Vote majoritaire (Déf. 4.2, p. 3) et moyenne (Déf. 4.3, p. 4)
$$\hat{y}(x) = \arg\max_{c\in\mathcal{y}} \sum_{j=1}^m \mathbb{1}\big[h_j(x) = c\big] \qquad\text{(classification)}, \qquad \hat{y}(x) = \frac{1}{m}\sum_{j=1}^m h_j(x) \quad\text{(régression)}$$
Conditions de succès (p. 4) : diversité, qualité individuelle (mieux que le hasard), indépendance des erreurs.

### Bayesian Model Averaging (Déf. 4.4, p. 5)
$$p(y|x, \mathcal{D}) = \sum_{j=1}^M p\big(y|x, \mathcal{M}_j, \mathcal{D}\big)\, p\big(\mathcal{M}_j \mid \mathcal{D}\big), \qquad p\big(\mathcal{M}_j\mid\mathcal{D}\big) = \frac{p(\mathcal{D}\mid\mathcal{M}_j)\,p(\mathcal{M}_j)}{\sum_{k=1}^M p(\mathcal{D}\mid\mathcal{M}_k)\,p(\mathcal{M}_k)}$$
Implémentation en log-probabilités avec `logsumexp` (p. 6) ; **log-vraisemblance** : $\log p(\mathcal{D}\mid\mathcal{M}_j) = \sum_{i=1}^n \log p(y_i \mid x_i, \mathcal{M}_j)$.

### Bagging (p. 7–9)
- Échantillon bootstrap $S_n^*$ : $n$ tirages **avec remise** ; environ $\big(1-\frac{1}{e}\big) \approx 63.2\%$ des points présents, $\frac{1}{e}\approx 36.8\%$ absents (Déf. 4.5, p. 7).
- Algorithme 4.1 (p. 8) : pour $j = 1..M$, bootstrap $S_n^{(j)}$, modèle $h_j = \mathcal{A}(S_n^{(j)})$ ; sortie $\hat{h}(x) = \frac{1}{M}\sum_{j=1}^M h_j(x)$ (régression) ou vote majoritaire.
- Théorème 4.2 (p. 9) : modèles de variance $\sigma^2$ décorrélés $\Rightarrow$ variance baggée $\frac{\sigma^2}{M}$. Le bagging stabilise les algorithmes **instables** (arbres, réseaux), pas les stables (régression linéaire).
- **Out-of-Bag Error** (Déf. 4.6, p. 9) : estimation non biaisée de l'erreur de généralisation **sans ensemble de validation séparé**.

### Random Forest (Algorithme 4.2, p. 11)
Bagging + sélection aléatoire de $m$ features parmi $d$ à chaque nœud. **Règles empiriques** (p. 11) :
- Classification : $m = \sqrt{d}$ ; Régression : $m = \frac{d}{3}$.

### AdaBoost (Algorithme 4.3, p. 13)
Entrée $S = \{(x_i,y_i)\}_{i=1}^n$, $y_i \in \{-1,+1\}$ ; initialisation $w_i^1 = \frac{1}{n}$. Pour $t = 1..T$ :
1. Entraîner un classificateur faible $h_t$ sur $(S, w^t)$
2. Erreur pondérée : $\varepsilon_t = \sum_{i:h_t(x_i)\ne y_i} w_i^t$
3. Si $\varepsilon_t \ge \frac12$ : arrêter
4. Poids du modèle : $\alpha_t = \frac{1}{2}\log\Big(\frac{1-\varepsilon_t}{\varepsilon_t}\Big)$
5. Mise à jour : $w_i^{t+1} = \frac{w_i^t}{Z_t}e^{-\alpha_t y_i h_t(x_i)}$ ($Z_t$ constante de normalisation)

Sortie : $H(x) = \mathrm{sign}\Big(\sum_{t=1}^T \alpha_t h_t(x)\Big)$.

- **Borne sur l'erreur d'entraînement** (Théorème 4.3, p. 14) : $\mathrm{Err}_{\mathrm{train}} \le \prod_{t=1}^T 2\sqrt{\varepsilon_t(1-\varepsilon_t)} = \prod_{t=1}^T \sqrt{1 - 4\gamma_t^2}$, où $\gamma_t = \frac{1}{2} - \varepsilon_t$ est l'avantage sur le hasard → décroissance **exponentielle**.
- **Perte exponentielle** (Théorème 4.4, p. 14) : AdaBoost = descente de coordonnées sur $L_{\exp}(F) = \frac{1}{n}\sum_{i=1}^n e^{-y_i F(x_i)}$ avec $F(x) = \sum_{t=1}^T \alpha_t h_t(x)$.
- **Margin** (Déf. 4.7, p. 15) : $\mathrm{margin}_i = y_i F(x_i)$ ; AdaBoost maximise le margin minimum (p. 16).
- **Perte logistique** (comparaison, p. 16) : $L_{\mathrm{logistic}}(\mathrm{margin}) = \log(1 + e^{-\mathrm{margin}})$ — les deux convexes, l'exponentielle plus agressive donc sensible aux outliers (p. 17).

### Gradient Boosting (p. 18)
1. Modèle initial $F_0$ ; 2. à chaque étape $m$ : résidus $r_{i,m} = -\Big[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\Big]_{F = F_{m-1}}$, entraîner $h_m$ sur ces résidus, mise à jour $F_m = F_{m-1} + \nu h_m$ ($\nu$ = learning rate). XGBoost = + régularisation L1/L2 sur les feuilles, approximation d'ordre 2 (hessienne), gestion native des manquants (p. 19). Hyperparamètres critiques et plages typiques (p. 20) : `n_estimators` 100–1000, `learning_rate` 0.01–0.3, `max_depth` 3–8, `subsample` 0.8–1.0, `colsample_bytree` 0.8–1.0, `reg_alpha` (L1) 0–10, `reg_lambda` (L2) 1–10.

### Guide de choix ensembliste (p. 21–22)
- **Random Forest** : premier choix robuste/interprétable, données mixtes, importance des variables.
- **XGBoost/LightGBM** : compétitions, optimisation fine, grands jeux de données.
- **Bagging** : modèles instables, réduction de variance.
- **AdaBoost** : modèles simples (stumps), classification binaire.
- Bonnes pratiques : commencer simple (RF défaut), valider par cross-validation, diversifier les modèles de base, surveiller la complexité, exploiter l'OOB.

## 4.4 Partie 2 — Régularisation : notations exactes

### Cadre général (p. 23)
$$\hat{\theta} = \arg\min(\theta)\, L_{n(\theta)} = \arg\min(\theta)\, \frac{1}{n}\sum_{i=1}^n \ell\big(f_{\theta(x_i)}, y_i\big)$$
$$\hat{\theta}_\lambda = \arg\min(\theta)\, L_{n(\theta)} + \lambda\Omega(\theta)$$
- $\Omega(\theta)$ : terme de régularisation (pénalité de complexité) ; $\lambda \ge 0$ : paramètre de régularisation (force de la pénalité).
- $\lambda = 0$ : pas de régularisation (risque de surajustement) ; $\lambda$ petit : favorise l'ajustement ; $\lambda$ grand : favorise la simplicité (p. 24).

### Décomposition biais-variance (Théorème 5.1, p. 24)
$$\mathbb{E}\Big[\big(y - \hat{f}_\lambda(x)\big)^2\Big] = \mathrm{Biais}^2\big[\hat{f}_\lambda(x)\big] + \mathrm{Var}\big[\hat{f}_\lambda(x)\big] + \sigma^2$$
« La régularisation introduit un **biais** mais **réduit la variance**. »

### **Ridge (L2)** (Déf. 5.1, p. 24 ; solution p. 25)
Pour un modèle linéaire $f_{\theta(x)} = \theta^\top x$ :
$$\hat{\theta}_{\mathrm{Ridge}} = \arg\min(\theta)\ \|y - X\theta\|_2^2 + \lambda\,\|\theta\|_2^2, \qquad \|\theta\|_2^2 = \sum_{j=1}^p \theta_j^2$$
$$\hat{\theta}_{\mathrm{Ridge}} = \big(X^\top X + \lambda I\big)^{-1}X^\top y$$
Propriétés (p. 25) : conditionnement amélioré, inversion garantie pour $\lambda>0$, stabilité numérique (multicolinéarité), coefficients « contractés » vers zéro.

### **SVD et rétrécissement** (Prop. 5.1, p. 26)
> Soit $X = U\Sigma V^\top$ la décomposition SVD de la matrice de design. Les coefficients Ridge s'écrivent :
> $$\hat{\theta}_{\mathrm{Ridge}} = \sum_{j=1}^r \frac{\sigma_j^2}{\sigma_j^2 + \lambda}\, v_j\big(u_j^\top y\big)$$
> Les facteurs $\frac{\sigma_j^2}{\sigma_j^2+\lambda}$ montrent comment Ridge **rétrécit** plus fortement les directions associées aux petites valeurs singulières.

### **Lasso (L1)** (Déf. 5.2, p. 26)
$$\hat{\theta}_{\mathrm{Lasso}} = \arg\min(\theta)\ \|y - X\theta\|_2^2 + \lambda\,\|\theta\|_1, \qquad \|\theta\|_1 = \sum_{j=1}^p |\theta_j|$$
« L1 peut **annuler exactement** certains coefficients → **sélection de variables automatique**. » Géométrie : losange/polytope dont les coins correspondent à des coordonnées nulles (p. 27). **Lasso path** $\lambda \mapsto \hat\theta_{\mathrm{Lasso}}(\lambda)$ : linéaire par morceaux (Déf. 5.3, p. 27). Algorithme **LARS** (p. 28) : variable la plus corrélée au résidu $j^* = \arg\max_j |x_j^\top r|$, avancée équiangulaire.

### **Elastic Net** (Déf. 5.3 [sic], p. 29)
$$\hat{\theta}_{\mathrm{EN}} = \arg\min(\theta)\ \|y - X\theta\|_2^2 + \lambda_1\,\|\theta\|_1 + \lambda_2\,\|\theta\|_2^2$$
Paramétrisation alternative avec $\alpha \in [0,1]$ :
$$\hat{\theta}_{\mathrm{EN}} = \arg\min(\theta)\ \|y - X\theta\|_2^2 + \lambda\big[(1-\alpha)\|\theta\|_2^2 + \alpha\,\|\theta\|_1\big]$$
($\alpha = 0$ → Ridge, $\alpha = 1$ → Lasso). Effet de groupement, stabilité, parcimonie contrôlée (p. 30). Tableau (p. 29) : Ridge — pas de sélection, conserve tout ; Lasso — sélection arbitraire dans les groupes corrélés ; Elastic Net — sélection groupée.

### Choix de $\lambda$ par validation croisée (p. 31)
> **Procédure de sélection par CV** :
> 1. **Grille de valeurs** : définir $\Lambda = \{\lambda_1, \dots, \lambda_K\}$
> 2. Pour chaque $\lambda_k \in \Lambda$ : calculer l'erreur de validation croisée $\mathrm{CV}(\lambda_k)$
> 3. **Sélection** : $\hat{\lambda} = \arg\min_{\{\lambda_k\}} \mathrm{CV}(\lambda_k)$
> 4. **Modèle final** : réentraîner sur toutes les données avec $\hat{\lambda}$

Grilles pratiques (p. 31–32) : `np.logspace(-4, 4, 50)` pour Ridge, `np.logspace(-4, 1, 50)` pour Lasso ; `GridSearchCV(..., cv=5, scoring='neg_mean_squared_error')`.

### Weight decay = L2 en deep learning (p. 32–33)
$$L_{\mathrm{total}}(w) = L_{\mathrm{data}}(w) + \frac{\lambda}{2}\,\|w\|_2^2$$
$$w_{t+1} = w_t - \eta\nabla L_{\mathrm{data}}(w_t) - \eta\lambda w_t = (1-\eta\lambda)w_t - \eta\nabla L_{\mathrm{data}}(w_t)$$
Le terme $(1-\eta\lambda)$ provoque un **decay** des poids. Autres techniques modernes : batch normalization, dropout, LayerNorm/GroupNorm, spectral normalization ; régularisation structurée : Group Lasso, Fused Lasso, Nuclear norm (p. 33).

### Guide de choix de la régularisation (p. 33–34)
- **Ridge** : toutes les variables a priori importantes, multicolinéarité, stabilité numérique requise.
- **Lasso** : sélection automatique souhaitée, structure parcimonieuse attendue, interprétabilité.
- **Elastic Net** : groupes de variables corrélées, compromis sélection/stabilité, $p > n$.

---

# 5. coursClassif-3ArbresDecision.pdf

## 5.1 Identification
- **Titre/module** : *Apprentissage supervisé et non supervisé — II. L'apprentissage supervisé — C. Les arbres de décisions*
- **Établissement** : Université Paul Valéry Montpellier 3, M1 MIASHS
- **Langue** : français
- Diaporama, slides 1–22. Références : Azencott *Introduction au Machine Learning* ; Shalev-Shwartz & Ben-David ; Hastie, Tibshirani, Friedman (slide 22).

## 5.2 Concepts couverts
Arbres de décision (CART), critères d'impureté (**Gini, Entropie, erreur de classification**), **MSE** pour la régression, gain d'information, élagage (régularisation d'arbre), lien avec les frontières de décision linéaires par morceaux, weak learners → méthodes ensemblistes.

## 5.3 Notations exactes

### Définition (slide 2)
« On appelle **arbre de décision** un modèle de prédiction qui peut être représenté sous la forme d'un arbre. Chaque nœud de l'arbre teste une condition sur une seule variable et chacun de ses enfants correspond à une réponse possible à cette condition. Les feuilles de l'arbre correspondent à une étiquette. »

### Algorithme CART (slide 4)
« Classification and Regression Tree » : partitionnement de l'espace par approche **gloutonne, récursive et divisive**, apprend un **arbre binaire** à partir de données $(x_1, y_1), \dots, (x_n, y_n) \in \mathcal{X}\times\mathcal{Y}$. (1) chaque nœud sépare linéairement, exactement deux enfants ; (2) **une seule variable par nœud** — frontière orthogonale à l'axe pour les variables numériques ; (3) à la feuille, règle d'agrégation (vote pour classification, moyenne pour régression).

### Variable séparatrice et régions (slide 6)
La variable séparatrice $x^j$ définit deux régions $R_l$ et $R_m$ :
- **variable binaire** : $R_l(x^j) = \{x \in \mathcal{X} : x^j = 1\}$, $R_m(x^j) = \{x \in \mathcal{X} : x^j = 0\}$
- **variable qualitative nominale** (sous-ensemble $S$ de modalités, souvent $dim(S)=1$) : $R_l(x^j, S) = \{x \in \mathcal{X} : x^j \in S\}$, $R_m(x^j, S) = \{x : x^j \notin S\}$
- **variable quantitative continue** (point de séparation $s$) : $R_l(x^j, s) = \{x \in \mathcal{X} : x^j < s\}$, $R_m(x^j, s) = \{x \in \mathcal{X} : x^j \ge s\}$

Variables ordinales et discrètes : traitées par seuil ou par regroupement de modalités (slide 7).

### Règle d'agrégation (slide 13) — pour $r$ régions $R_1, \dots, R_r$
- **Classification** (étiquette majoritaire de la région) :
  $$f(x) = \sum_{j=1}^r \mathbb{1}\{x \in R_j\}\ \arg\max_{k\in\{1,\dots,C\}} \sum_{\substack{i\in\{1,\dots,n\}\\ x_i \in R_j}} \mathbb{1}\{y_i = k\}$$
- **Régression** (étiquette moyenne de la région) :
  $$f(x) = \sum_{j=1}^r \mathbb{1}\{x \in R_j\}\ \frac{1}{|R_j|}\sum_{\substack{i\in\{1,\dots,n\}\\ x_i\in R_j}} y_i$$

### Gain d'information (slide 15)
On choisit la variable séparatrice $x^j$ et le seuil de séparation *seuil* ($s$ continue ou $S$ discrète) qui maximise :
$$\mathcal{IG}(R_l, R_m) = \mathcal{I}(R) - \frac{n_l}{n}\,\mathcal{I}\big(R_l(x^j, seuil)\big) - \frac{n_m}{n}\,\mathcal{I}\big(R_m(x^j, seuil)\big)$$
avec $\mathcal{I}$ : critère d'impureté ; $n$ : nombre de points de $R$ ; $n_l, n_m$ : nombre de points dans $R_l$ et $R_m$.

### Critères d'impureté (slide 16) — $p_k$ = proportion de la classe $k$ dans la région $R$
- **Impureté de Gini** : $\mathcal{I}_G(R) = \sum_{k=1}^{C} p_k(1-p_k) = \sum_{k=1}^{C}\sum_{k'\ne k \in \{1,\dots C\}} p_k p_{k'}$
- **Entropie** : $\mathcal{I}_{\mathcal{E}}(R) = -\sum_k p_k \log_2(p_k)$ (« le but de la construction est de minimiser la quantité d'information supplémentaire nécessaire pour étiqueter correctement les exemples »)
- **Erreur de classification** : $\mathcal{I}_{EC}(R) = 1 - \max_k(p_k)$

### Partitionnement en régression (slide 17) — **MSE**
$$\mathrm{MSE}(R) = \frac{1}{n}\sum_i (y_i - \bar{y})^2$$
(« relativement à la moyenne » car la moyenne est justement la prédiction pour un nœud fixé). On minimise :
$$\frac{n_l}{n}\mathrm{MSE}(R_l) + \frac{n_r}{n}\mathrm{MSE}(R_m)$$

### Élagage / coût en complexité (slide 20)
$$C_\lambda(T) = \sum_{l=1}^{|T|} n_l\, \mathcal{I}(R_l) + \lambda|T|$$
où $|T|$ = nombre de régions de l'arbre $T$ et $\lambda > 0$ hyperparamètre contrôlant l'importance relative de l'erreur et de la complexité.

## 5.4 Méthodes recommandées
- **Sélection de l'arbre — Stratégie n°1** (slide 19) : hyperparamètres par **validation croisée** : profondeur maximale, nombre de feuilles maximal, nombre d'exemples minimal par feuille/nœud. (Arbre peu profond → sous-apprentissage ; trop profond → sur-apprentissage, slide 18.)
- **Stratégie n°2 — Élagage** (slide 20) : construire sans limite sur le train, ne garder que les branches qui améliorent la validation ; minimiser $C_\lambda(T)$.
- Avantages spécifiques (slide 3) : variables qualitatives sans représentation numérique (*apprentissage non métrique*), multiclasse natif, classes multi-modales.
- Mise en garde (slide 21) : les arbres sont des **apprenants faibles** (weak learners), peu robustes → remédier via méthodes ensemblistes (bagging, forêts aléatoires, boosting — renvoi au cours *Régularisation et optimisation*).

---

# 6. coursClassif-5-Clustering.pdf

## 6.1 Identification
- **Titre/module** : *Classification supervisée et non supervisée — Clustering*
- **Auteure** : Marine Demangeot, Université Paul Valéry Montpellier 3, M1 MIASHS, 25/09/2022
- **Langue** : français
- Diaporama, slides 1–30. S'inspire de l'ouvrage d'Azencott (slide 1).

## 6.2 Concepts couverts
Clustering (objectif, exemples), distances, homogénéité/séparabilité, indice de Davies-Bouldin, coefficient de silhouette, inertie intra/inter-classes, **classification ascendante hiérarchique (CAH)** avec liens (simple, complet, moyen, centroïdal, Ward), dendrogramme, **K-moyennes** (algorithme de Lloyd), critère du coude, K-médoïdes, évaluation d'un clustering.

## 6.3 Notations exactes

### Cadre (slide 2)
Données $x_1, \dots, x_n \in \mathcal{X}$ **sans étiquettes** ; objectif : séparer en sous-groupes homogènes appelés **clusters** : $\{x_1,\dots,x_n\} = \bigcup_{i=1}^K C_k$. « C'est une **analyse exploratoire des données**. »

### Distance (Définition, slide 4)
$d : \mathcal{X}\times\mathcal{X}\to\mathbb{R}_+$ est une *distance* si :
- $\forall x,y \in \mathcal{X}$, $d(x,y) = d(y,x)$ (**Symétrie**)
- $\forall x,y$, $d(x,y) = 0 \Leftrightarrow x = y$ (**Séparation**)
- $\forall x,y,z$, $d(x,y) \le d(x,z) + d(z,y)$ (**Inégalité triangulaire**)

### Distances quantitatives (slide 5) — $x = (x_1,\dots,x_d), y = (y_1,\dots,y_d) \in \mathbb{R}^d$
- **Euclidienne** : $d(x,y) = \|x-y\|_2 = \sqrt{\sum_{i=1}^d (x_i - y_i)^2}$ (« on la notera plus simplement $\|\cdot\|$ par la suite »)
- **Manhattan** : $d(x,y) = \|x-y\|_1 = \sum_{i=1}^d |x_i - y_i|$
- **Minkowski** : $d(x,y) = \big(\sum_{i=1}^d (x_i-y_i)^p\big)^{1/p}$
- **Chebyshev** : $d(x,y) = \max_{i\in\{1,\dots,n\}} |x_i - y_i|$
- **Mahalanobis** : $d(x,y) = \sqrt{(x-y)^\top\Sigma^{-1}(x-y)}$, $\Sigma$ : matrice de variance-covariance empirique

Variables qualitatives (slide 6) : distance du $\chi_2$, de Jaccard, de Gower ; ou stratégies de conversion (découpage en classes, one-hot, **ACM** puis coordonnées quantitatives).

### Centroïde et homogénéité (slide 8)
- **Centroïde** du cluster $C$ : $\mu_C = \frac{1}{|C|}\sum_{x\in C} x$
- **Homogénéité** (*tightness*) du cluster $C_k$ : $T_k = \frac{1}{|C_k|}\sum_{x\in C_k} d(x, \mu_k)$
- Homogénéité globale : $T = \frac{1}{K}\sum_{k=1}^K T_k$ (à **minimiser**)

### Séparabilité (slide 9)
- $S_{k\ell} = d(\mu_k, \mu_\ell)$ ; globale : $S = \frac{2}{K(K-1)}\sum_{k=1}^K\sum_{\ell=k+1}^K S_{k\ell}$ (à **maximiser**)

### Indice de Davies-Bouldin (slide 10)
$$D_k = \max_{\ell\ne k} \frac{T_k + T_\ell}{S_{k\ell}}, \qquad D = \frac{1}{K}\sum_{k=1}^K D_k$$
Objectif : trouver le clustering qui **minimise** $D$.

### Coefficient de silhouette (slide 11)
$$s_x = \frac{b(x) - a(x)}{\max((a(x), b(x)))} \in [-1, 1]$$
avec
$$a(x) = \frac{1}{|C_{k(x)}|-1}\sum_{y\in C_{k(x)}, y\ne x} d(x,y) \qquad b(x) = \min_{\ell\ne k(x)} \frac{1}{|C_\ell|}\sum_{y\in C_\ell} d(x,y)$$
($a(x)$ : distance moyenne de $x$ aux autres éléments de son cluster $C_{k(x)}$ ; $b(x)$ : plus petite valeur que pourrait prendre $a(x)$ si $x$ appartenait à un autre cluster.) Global : $s = \frac{1}{n}\sum_{i=1}^n s(x_i)$, à **maximiser**.

### Inertie intra et inter-classes (slide 12) — $\mu = \frac{1}{n}\sum_{i=1}^n x_i$, distance euclidienne
$$I = \sum_{i=1}^n \|x_i - \mu\|^2 = \underbrace{\sum_{k=1}^K \sum_{x_i\in C_k}\|x_i - \mu_k\|^2}_{I_W\ \text{(inertie intra-classes)}} + \underbrace{\sum_{k=1}^K |C_k|\,\|\mu_k - \mu\|^2}_{I_B\ \text{(inertie inter-classes)}}$$
Objectif : **maximiser $I_B$** ou de manière équivalente **minimiser $I_W$**.

### Choix d'une partition (slide 13)
$$C^* = \argmin_{K\in\{1,\dots,n\}}\ \min_{C_1,\dots,C_K} R(C_1, \dots, C_K)$$
avec $R$ = indice de Davies-Bouldin global, coefficient de silhouette global ou variance intra-classes. Nombre de partitions possibles = **nombre de Bell** $B_n = \frac{1}{e}\sum_{K\ge 1}\frac{K^n}{K!}$ ($B_{50} \ge 10^{48}$) → algorithmes itératifs.

### CAH — clustering hiérarchique (slides 15–19)
- **Agglomératif** (= **classification ascendante hiérarchique, CAH**) : chaque observation est un cluster de taille 1, on agglomère les deux clusters les plus proches ; **divisif** : inverse (slide 15).
- Distances entre clusters $C_k, C_\ell$ (slide 16) :
  - **lien simple** : $d(C_k, C_\ell) = \min_{(x,y)\in C_k\times C_\ell} d(x,y)$
  - **lien complet** : $d(C_k, C_\ell) = \max_{(x,y)\in C_k\times C_\ell} d(x,y)$
  - **lien moyen** : $d(C_k, C_\ell) = \frac{1}{|C_k|}\frac{1}{|C_\ell|}\sum_{x\in C_k}\sum_{y\in C_\ell} d(x,y)$
  - **lien centroïdal** : $d(C_k, C_\ell) = d(\mu_k, \mu_\ell)$
- **Distance de Ward** (slide 17) :
  $$d(C_k, C_\ell) = \frac{|C_k|\,|C_\ell|}{|C_k| + |C_\ell|}\,\|\mu_k - \mu_\ell\|^2$$
  Proposition : la distance de Ward correspond à la **perte d'inertie inter-classes** (= gain de variance intra-classe) lors de la fusion de $C_k$ et $C_\ell$ ; elle prend en compte les effectifs (groupes équilibrés).
- **Dendrogramme** (slide 18) : longueur de branche proportionnelle à la distance entre clusters connectés.
- Choix du nombre de clusters (slide 19) : arrêt quand distance minimale > seuil $r$ (ou $\alpha\max_{(x,y)} d(x,y)$, $\alpha<1$) ; ou évaluer les nœuds du dendrogramme avec une mesure (ex : silhouette). Complexité élevée : $O(dn^2)$ opérations par itération.

### K-moyennes (slides 20–28)
- **Objectif** (slide 20) : pour $K$ fixé, trouver la partition qui minimise l'inertie intra-classes :
  $$C^* = \arg\min_{C_1,\dots,C_K}\ \sum_{k=1}^K\sum_{x\in C_k} \|x - \mu_k\|^2$$
  Problème trop long → heuristique : **l'algorithme de Lloyd**.
- **Algorithme de Lloyd** (slide 21) :
  1. Choisir $K$ centroïdes initiaux $\mu_1, \dots, \mu_K$ aléatoirement (ou dispersés au maximum)
  2. Affecter chaque observation au centroïde le plus proche : $k(x_i) = \arg\min_{k=1,\dots,K}\|x_i - \mu_k\|^2$ (cellules de **Voronoï**)
  3. Recalculer les centroïdes : $\mu_k = \frac{1}{|C_k|}\sum_{x_i\in C_k} x_i$
  4. Répéter 2–3 jusqu'à convergence (affectations stables)
- Proposition (slide 24) : l'inertie intra-classes $\sum_{k=1}^K\sum_{x\in C_k}\|x-\mu_k\|^2$ **diminue à chaque itération** → possible minimum local → **répéter avec différentes initialisations aléatoires**.
- **Choix de $K$ — critère du coude** (slide 25) : l'inertie intra-classe décroît toujours avec $K$ ; on choisit $K$ au niveau du coude (changement de pente).
- Complexité (slide 26) : $O(ndKt)$ — linéaire en $n$, contre quadratique pour le hiérarchique. Combinaison possible : K-moyennes avec $K = \lambda n$ puis CAH sur les centroïdes.
- **Données aberrantes** (slide 27) : K-moyennes sensible aux outliers (peut servir à les détecter) ; **K-médoïdes** plus robuste (médoïde = point de la classe de dissimilarité moyenne minimale, observation la plus centrale).
- Forme des clusters (slide 28) : diagramme de Voronoï → clusters **convexes** ; astuce du noyau pour clusters non convexes.

## 6.4 Méthodes d'évaluation recommandées (slide 29)
- **Stabilité des clusters** : robustesse à plus de données, perturbations, initialisations différentes.
- **Évaluation externe** : a posteriori par un expert ; a priori avec étiquettes partielles (**indice de Rand**).
- **Évaluation interne** : indice de Davies-Bouldin global, coefficient de silhouette global (homogénéité + séparabilité).

---

# 7. course.pdf

## 7.1 Identification
- **Titre** : *Théorie de l'Apprentissage Statistique*
- **Module** : MIASHS M1 - Semestre 2
- **Langue** : français
- 47 pages : Introduction ; Prédicteurs optimaux de Bayes ; Consistance et convergence ; Inégalités de concentration et Généralisation (dont VC et Rademacher) ; Fonctions de perte calibrées ; Bibliographie (Devroye et al., Shalev-Shwartz & Ben-David, Bach, Vapnik, Boucheron et al.).

## 7.2 Convention de notation générale (p. 1–2)
- Espace d'entrée $\mathcal{X}$ (typiquement $\mathbb{R}^d$), sortie $\mathcal{Y} = \{0,1\}$ (classification binaire) puis $\{-1,+1\}$ pour la calibration (p. 37) ; couples $(X, Y)$ i.i.d. de distribution inconnue $P_{X,Y}$.
- **Risque théorique** : $L(h) = E[\ell(h(X), Y)]$ ; perte 0-1 : $\ell(y, \hat{y}) = \mathbb{1}_{\{y\ne\hat{y}\}}$, risque $= P(h(X)\ne Y)$.
- Échantillon $\mathcal{S}_n = \{(X_i, Y_i)\}_{i=1}^n$ ; **risque empirique** :
  $$R_n(h) = \frac{1}{n}\sum_{i=1}^n \ell(h(X_i), Y_i)$$
- **Principe de minimisation du risque empirique (ERM)** : $\hat{h}_n = \arg\min_{h\in\mathcal{H}} R_n(h)$, avec classe de fonctions $\mathcal{H}\subset\mathcal{Y}^\mathcal{X}$.

## 7.3 Concepts et notations exactes

### Classifieur de Bayes (Théorème 1.1, p. 3) — ⚠ ce n'est PAS Naive Bayes
> Pour la perte 0-1, le classifieur optimal en $x$ est :
> $$h^*(x) = \begin{cases} 1 \text{ si } \eta(x) \ge \frac{1}{2} \\ 0 \text{ sinon}\end{cases}$$
> où $\eta(x) = P(Y = 1 \mid X = x)$ est la probabilité a posteriori.

Risque conditionnel : $r(\hat{y}, x) = P(\hat{y}\ne Y\mid X = x)$ ; **risque de Bayes** (p. 5) :
$$R^* = R(h^*) = E_X[\min(\eta(X), 1-\eta(X))]$$
($R^* = 0$ ssi problème séparable).

### Prédicteurs optimaux en régression (Théorème 1.2, p. 5–6) — **MSE**
1. **Erreur quadratique ($L_2$)** : $\ell(y,\hat{y}) = (y-\hat{y})^2$ → prédicteur optimal = **moyenne conditionnelle** $h^*(x) = E[Y\mid X=x]$ (preuve par décomposition biais-variance conditionnelle, p. 6–7 : $E[(Y-c)^2\mid X=x] = E[(Y-m(x))^2\mid X=x] + (m(x)-c)^2$ avec $m(x)=E[Y|X=x]$).
2. **Erreur absolue ($L_1$)** : $\ell(y,\hat{y}) = |y-\hat{y}|$ → **médiane conditionnelle** (preuve p. 8 : $g'(c) = 2F_{Y|x}(c) - 1 = 0$).

### Consistance (Définition 1.2, p. 9)
- consistant en probabilité : $\forall\varepsilon>0,\ P(R(h_n) - R^* > \varepsilon)\xrightarrow{n\to+\infty} 0$
- en moyenne quadratique : $E[(R(h_n)-R^*)^2]\to 0$ ; fortement consistant : $P(\lim R(h_n) = R^*) = 1$.
- Décomposition (p. 10) :
  $$R(h_n) - R^* = \underbrace{R(h_n) - \inf_{h\in\mathcal{H}}R(h)}_{\text{terme d'estimation}} + \underbrace{\inf_{h\in\mathcal{H}}R(h) - R^*}_{\text{terme d'approximation}}$$
- **Consistance universelle de Stone (1977)** pour k-NN (Théorème 2.1, p. 10–11) : si $k(n)\to+\infty$ et $\frac{k(n)}{n}\to 0$, alors $E[R(h_n^{k\text{-NN}})]\to R^*$ pour toute $P_{X,Y}$.

### Inégalités de concentration (p. 12–20)
- **Markov** (p. 12) : $Z \ge 0$, $t>0$ : $P(Z\ge t) \le \frac{E[Z]}{t}$
- **Bienaymé-Tchebychev** (p. 13) : $P(|Z - E[Z]| \ge \varepsilon) \le \frac{\mathrm{Var}(Z)}{\varepsilon^2}$
- Application (p. 14) : $P(|R_n(h) - R(h)| \ge \varepsilon) \le \frac{R(h)(1-R(h))}{n\varepsilon^2} \le \frac{1}{4n\varepsilon^2}$ (pour $h$ fixé)
- **Cas séparable, $|\mathcal{H}|<+\infty$** (Théorème 3.1, p. 15) : si $\exists h^*\in\mathcal{H}$, $R(h^*)=0$ :
  $$P^n\big(R(\hat{h}_{\mathcal{S}_n}) > \varepsilon\big) \le |\mathcal{H}|\,e^{-n\varepsilon}, \qquad n \ge \frac{\log(\frac{|\mathcal{H}|}{\delta})}{\varepsilon}$$
  (preuve par échantillons trompeurs + union bound, p. 15–17) ; corollaire (p. 18) : avec probabilité $1-\delta$, $R(\hat{h}_{\mathcal{S}_n}) \le \frac{\log(\frac{|\mathcal{H}|}{\delta})}{n}$.
- **Hoeffding (1963)** (p. 18–19) : $Z_i \in [a_i, b_i]$ indépendantes : $P\big(\frac{1}{n}\sum(Z_i - E[Z_i]) \ge t\big) \le \exp\big(-\frac{2n^2t^2}{\sum(b_i-a_i)^2}\big)$ ; si $Z_i\in[0,1]$ : $P\big(|\frac{1}{n}\sum Z_i - E[Z_1]| \ge t\big) \le 2e^{-2nt^2}$.
- **Théorème de généralisation, cas non séparable fini** (Théorème 3.2, p. 19–20) : avec probabilité $1-\delta$, simultanément pour tout $h\in\mathcal{H}$ :
  $$|R(h) - R_{\mathcal{S}_n}(h)| \le \sqrt{\frac{\log|\mathcal{H}| + \log(\frac{2}{\delta})}{2n}}, \qquad R(\hat{h}_{\mathcal{S}_n}) \le R_{\mathcal{S}_n}(\hat{h}_{\mathcal{S}_n}) + \sqrt{\frac{\log|\mathcal{H}| + \log(\frac{2}{\delta})}{2n}}$$
  Vitesse $O(\frac{1}{\sqrt{n}})$ contre $O(\frac{1}{n})$ dans le cas séparable (p. 22).

### Théorie de Vapnik-Chervonenkis (p. 22–26) — **fonctions de décision linéaires**
- **Brisure** (p. 23) : $\mathcal{H}$ brise $C = \{x_1,\dots,x_m\}$ si $|\{(h(x_1),\dots,h(x_m)) : h\in\mathcal{H}\}| = 2^m$.
- **Dimension VC** : $\mathrm{VCdim}(\mathcal{H}) = \sup\{m\in\mathbb{N} : \exists C\subset\mathcal{X}, |C|=m, \mathcal{H} \text{ brise } C\}$.
- Exemples (p. 23–24) : seuils sur $\mathbb{R}$ → VCdim = 1 ; intervalles → VCdim = 2 ; **hyperplans de $\mathbb{R}^d$** : $\mathcal{H} = \{x\mapsto\mathbb{1}_{w^\top x\ge b}\}$ → $\mathrm{VCdim}(\mathcal{H}) = d+1$.
- **Coefficient de brisure** : $\Pi_\mathcal{H}(m) = \max_{C\subset\mathcal{X}, |C|=m} |\{(h(x_1),\dots,h(x_m)) : h\in\mathcal{H}\}|$ ; **lemme de Sauer-Shelah** (p. 24) : $\Pi_\mathcal{H}(m) \le \sum_{i=0}^d\binom{m}{i} \le \big(\frac{em}{d}\big)^d$ pour $m\ge d$.
- **Borne VC** (Théorème 3.3, p. 25) : $d = \mathrm{VCdim}(\mathcal{H})$, avec probabilité $1-\delta$ :
  $$|R(h) - R_{\mathcal{S}_n}(h)| \le \sqrt{\frac{8d\log(2e\frac{n}{d}) + 8\log(\frac{4}{\delta})}{n}}$$

### **SVM et classifieur à marge** (p. 25–26)
- Définition (p. 25) : $h_{w,b}(x) = \mathrm{sgn}(w^\top x - b)$ classe $S$ avec marge $\gamma > 0$ si $\forall i,\ Y_i(w^\top X_i - b) \ge \gamma$ ; $\mathcal{H}_\gamma$ = classifieurs linéaires de norme $\|w\|_2 = 1$ séparant avec marge $\gamma$.
- **Borne VC pour le SVM (Vapnik 1995)** (Théorème 3.4, p. 25–26) : si $\|X_i\|_2\le R$ p.s. :
  $$\mathrm{VCdim}(\mathcal{H}_\gamma) \le \Big\lfloor\frac{R^2}{\gamma^2}\Big\rfloor$$
  « la dimension VC dépend de la marge et non de la dimension ambiante ».

### Limites VC pour réseaux de neurones et double descente (p. 26–31)
$\mathrm{VCdim} = O(WL\log W)$ (Bartlett 1998) ; phénomène de **double descente** (Belkin et al. 2019) : régimes sous-paramétré $W\ll n$, seuil d'interpolation $W\approx n$, sur-paramétré $W\gg n$ (p. 28) ; régularisation implicite de SGD (marge maximale, Soudry et al. 2018) ; bornes en normes de poids (Bartlett, Foster, Telgarsky 2017) ; **complexité de Rademacher** (p. 31) : $\hat{\mathfrak{R}}_n(\mathcal{H}) = E_\sigma\big[\sup_{h\in\mathcal{H}}\frac{1}{n}\sum\sigma_i h(X_i)\big]$, borne $\sup_h|R(h) - R_{\mathcal{S}_n}(h)| \le 2\hat{\mathfrak{R}}_n(\mathcal{H}) + \sqrt{\frac{\log(2/\delta)}{2n}}$.

### **Sigmoïde, Log Loss / cross-entropy, pertes calibrées** (chap. 5, p. 32–44)
- La perte 0-1 est NP-difficile à minimiser (non convexe, gradient nul p.p.) → **perte logistique (ou cross-entropy)** (p. 32) :
  $$\frac{1}{n}\sum_{i=1}^n \log\big(1 + e^{-y_i f_\theta(x_i)}\big)$$
- **Perte logistique** (convention $y\in\{-1,+1\}$, sortie $f(x)\in\mathbb{R}$, p. 33) :
  $$\ell_{\log}(y, f(x)) = \log\big(1 + e^{-yf(x)}\big)$$
- **Cross-entropy** (convention $\tilde{y}\in\{0,1\}$, sortie $\sigma(f(x))\in(0,1)$, p. 33) :
  $$\ell_{\mathrm{CE}}(\tilde{y}, f(x)) = -\tilde{y}\log(\sigma(f(x))) - (1-\tilde{y})\log(1 - \sigma(f(x)))$$
  où $\sigma(t) = \frac{1}{1+e^{-t}}$ est la **fonction sigmoïde**.
- **Propriétés de la sigmoïde** (p. 34) : $\sigma(t) = \frac{1}{1+e^{-t}}$ et $1 - \sigma(t) = \frac{e^{-t}}{1+e^{-t}} = \frac{1}{1+e^{t}} = \sigma(-t)$ ; $\log(\sigma(t)) = -\log(1+e^{-t})$.
- **Équivalence** (p. 35) : $\ell_{\mathrm{CE}}(\tilde{y}, f(x)) = \ell_{\log}(2\tilde{y}-1, f(x)) = \log(1 + e^{-(2\tilde{y}-1)f(x)})$ sous $\tilde{y} = \frac{y+1}{2}$.
- **Interprétation MLE** (p. 35) : la cross-entropy est la **log-vraisemblance négative** du modèle probabiliste $P(Y=1\mid X=x) = \sigma(f(x))$ ; « minimiser la cross-entropy revient à maximiser la vraisemblance du modèle logistique ».
- **Marge et pertes de substitution** (p. 37) : $\ell_\varphi(f(x), y) = \varphi(yf(x))$ ; $\varphi$-risque $R_\varphi(f) = E[\varphi(Yf(X))]$ ; tableau des pertes usuelles :
  | Perte | $\varphi(t)$ | Usage |
  |---|---|---|
  | Logistique | $\log(1+e^{-t})$ | Régression logistique, deep learning |
  | Charnière | $\max(0, 1-t)$ | SVM |
  | Exponentielle | $e^{-t}$ | AdaBoost |
  | Carrée (Brier) | $(1-t)^2$ | Least-squares classification |
- **Théorème de calibration** (Bartlett, Jordan, McAuliffe 2006 ; Théorème 4.1, p. 39) : $\varphi$ convexe positive est **calibrée** ssi $\varphi$ est différentiable en 0 et $\varphi'(0) < 0$. Risque conditionnel : $C_\varphi(\alpha, \eta) = \eta\varphi(\alpha) + (1-\eta)\varphi(-\alpha)$. Vérification (p. 42) : logistique $\varphi'(0)=-\frac12<0$ ✓ ; charnière ✓ ; exponentielle $\varphi'(0)=-1$ ✓ ; carrée $\varphi'(0)=-2$ ✓.
- **Décomposition de l'erreur en 3 termes** (Théorème 4.2, p. 43) :
  $$R(h_{\hat{f}_S}) - R^* = \underbrace{R(h_{\hat{f}_S}) - R(h_{f^*})}_{A\ \text{estimation}} + \underbrace{R(h_{f^*}) - R(h_{f^{**}})}_{B\ \text{calibration}} + \underbrace{R(h_{f^{**}}) - R^*}_{C\ \text{approximation}}$$
  $C = 0$ si $\varphi$ calibrée ; $B = 0$ si $f^{**}\in\mathcal{F}$.

## 7.4 Démarche du cours
Trois axes annoncés (p. 2) : (1) le **prédicteur de Bayes** (optimal sous connaissance parfaite de $P_{X,Y}$) ; (2) la **consistance et les bornes de généralisation** ($\hat h_n \to$ optimal quand $n\to\infty$) ; (3) la **calibration des fonctions de perte** (substituer à la perte 0-1 une perte proxy convexe sans perdre les garanties théoriques).

---

# 8. SeriesTemp_ARIMAX_2025.pdf

## 8.1 Identification
- **Titre/module** : *Données séquentielles — Modèles de régression dynamique*
- **Auteure** : Marine Demangeot, Université Paul Valéry Montpellier 3, **M2 MIASHS**
- **Langue** : français (code R avec `fable`/`fpp3`)
- Diaporama, slides 1–46. Trois parties : (I) Régression avec des erreurs ARIMA ; (II) Régression harmonique dynamique ; (III) Prédicteurs retardés.

## 8.2 Convention de notation générale
- Série réponse $y_t$, prédicteurs $x_{1,t}, \dots, x_{k,t}$, coefficients $\beta_0, \beta_1, \dots, \beta_k$.
- **Opérateur retard $B$** (backshift), polynômes AR $\phi(B)$ et MA $\theta(B)$, différenciation $(1-B)^d$.
- ⚠ Distinction cruciale du cours (slide 2) : **$\eta_t$** = erreur de régression (autocorrélée, suit un ARIMA) vs **$\varepsilon_t$** = bruit blanc. « Attention de bien distinguer $\eta_t$ de $\varepsilon_t$. Seules les erreurs $\varepsilon_t$ sont assumées être des bruits blancs. »

## 8.3 Concepts et notations exactes

### Modèle de régression standard (slide 1)
$$y_t = \beta_0 + \beta_1 x_{1,t} + \cdots + \beta_k x_{k,t} + \varepsilon_t$$
« Les erreurs $\varepsilon_t$ sont supposées être des bruits blancs. Nous souhaitons maintenant que le bruit $\varepsilon_t$ puisse être autocorrélé. »

### Régression avec erreurs ARIMA — exemple ARIMA(1,1,1) (slides 1–2, 4)
$$y_t = \beta_0 + \beta_1 x_{1,t} + \cdots + \beta_k x_{k,t} + \eta_t,$$
$$(1 - \phi_1 B)(1 - B)\eta_t = (1 + \theta_1 B)\varepsilon_t$$
où $\varepsilon_t$ est un bruit blanc.

### Estimation (slide 3) — pourquoi pas les MCO ordinaires, lien **MLE**
> Si $\sum \hat{\eta}_t^{\,2}$ est minimisée (comme en régression ordinaire) :
> 1. Les coefficients estimés $\hat{\beta}_0, \dots, \hat{\beta}_k$ ne sont plus optimaux puisque de l'information a été ignorée
> 2. Les tests associés au modèle (e.g., t-tests sur les coefficients) sont incorrects
> 3. Les $p$-valeurs sont généralement trop petites (« *spurious regression* »)
>
> **Minimiser $\sum\hat{\varepsilon}_t^2$ évite ces problèmes. Maximiser la vraisemblance est équivalent à minimiser $\sum\hat{\varepsilon}_t^2$.**

### Équivalence par différenciation (slides 4–5)
Modèle avec erreurs ARIMA(1,1,1) $\equiv$ modèle avec erreurs ARIMA(1,0,1) sur les données différenciées :
$$y'_t = \beta_1 x'_{1,t} + \cdots + \beta_k x'_{k,t} + \eta'_t, \qquad (1-\phi_1 B)\eta'_t = (1+\theta_1 B)\varepsilon_t$$
où $y'_t = y_t - y_{t-1}$, $x'_{t,i} = x_{t,i} - x_{t-1,i}$ et $\eta'_t = \eta_t - \eta_{t-1}$.

Forme générale (slide 5) — données originales :
$$y_t = \beta_0 + \beta_1 x_{1,t} + \cdots + \beta_k x_{k,t} + \eta_t \quad\text{où}\quad \phi(B)(1-B)^d\eta_t = \theta(B)\varepsilon_t$$
Après différenciation de **toutes** les variables : $y'_t = \beta_1 x'_{1,t} + \cdots + \beta_k x'_{k,t} + \eta'_t$ avec $\phi(B)\eta'_t = \theta(B)\varepsilon_t$, $y'_t = (1-B)^d y_t$, $x'_{i,t} = (1-B)^d x_{i,t}$, $\eta'_t = (1-B)^d\eta_t$.

### Forme rationnelle et mise en garde (slides 6–7)
$$y'_t = \beta x'_t + \eta'_t = \beta x'_t + \frac{\theta(B)}{\phi(B)}\varepsilon'_t$$
Modèles alternatifs avec ARMA sur $y_t$ : $y_t = \beta x_t + \phi_1 y_{t-1} + \cdots + \phi_p y_{t-p} + \varepsilon_t + \theta_1\varepsilon_{t-1} - \cdots - \theta_q\varepsilon_{t-q}$, i.e. $y_t = \frac{\beta}{\phi(B)}x_t + \frac{\theta(B)}{\phi(B)}\varepsilon_t$ — mais alors « la valeur de $\beta$ ne correspond pas à l'effet sur $y_t$ lorsque $x_t$ est augmenté d'une unité » (interprétation non intuitive, slide 7).

### Procédure de modélisation (slide 8) — méthodologie clé du cours
1. Dans R, spécifier un $\mathrm{ARIMA}(p, d, q)$ pour les erreurs ; $d$ niveaux de différenciation appliqués à **toutes** les variables $(y, x_{1,t}, \dots, x_{k,t})$
2. **Vérifier que la série $\varepsilon_t$ ressemble à un bruit blanc** (ACF/PACF des résidus, test de **Ljung-Box** — slides 11–13, `ljung_box, dof, lag`)
3. **L'AICc peut être calculé pour le modèle final**
4. **Répéter la procédure pour tous les sous-ensembles de prédicteurs et sélectionner le modèle avec la plus basse valeur d'AICc**

Code R canonique (slide 10) : `fit <- us_change %>% model(ARIMA(Consumption ~ Income))` → sortie « LM w/ ARIMA(1,0,2) errors ». Résidus : `residuals(fit, type='regression')` (erreurs $\eta_t$) vs `type='innovation'` (erreurs ARIMA $\varepsilon_t$) (slides 11–12).

### Prévision (slide 15)
- Prévoir séparément la partie régression et la partie ARIMA, puis combiner.
- Certains prédicteurs sont connus à l'avance (temps, variables muettes) ; d'autres nécessitent leur propre modèle de prévision.
- ⚠ « Les intervalles de prévision ignorent l'incertitude liée à la prévision des prédicteurs. »

### Exemple électricité (slides 16–25)
Régression quadratique avec erreurs ARMA : `ARIMA(Demand ~ Temperature + I(Temperature^2) + (Day_Type=="Weekday"))` → « LM w/ ARIMA(2,1,2)(2,0,0)[7] errors » (notation saisonnière $(P,D,Q)[m]$, période 7). Variante avec `log(Demand)`, `stepwise = FALSE, order_constraint = (p+q <= 8 & P+Q <= 5)` (slide 21). Prévision avec `new_data` + scénarios.

### Régression harmonique dynamique (slides 26–36)
- Principe : **termes de Fourier + erreurs ARIMA**. Avantages (slide 26) : saisonnalité de n'importe quelle longueur ; plusieurs périodes saisonnières via des termes de Fourier de différentes fréquences ; motif saisonnier lisse contrôlé par $K$ (« une saisonnalité plus ondulée peut être gérée en augmentant $K$ ») ; dynamique court terme gérée par une simple erreur ARMA.
- Sélection de $K$ (slides 28–34) : ajuster `ARIMA(log(Turnover) ~ fourier(K = k) + PDQ(0,0,0))` pour $K = 1..6$ et **choisir $K$ minimisant l'AICc** (le cours montre AICc = −616 pour K=1 jusqu'à −918 pour K=6).
- Exemple essence hebdomadaire (slide 35) : `ARIMA(Barrels ~ fourier(K = 13) + PDQ(0,0,0))`, coefficients notés `fourier(K = 13)C1_52`, `S1_52`, etc.

### Prédicteurs retardés / fonction de transfert (slides 37–46)
> Le modèle inclut les valeurs présentes et passées de la variable explicative : $x_t, x_{t-1}, x_{t-2}, \dots$
> $$y_t = a + \gamma_0 x_t + \gamma_1 x_{t-1} + \cdots + \gamma_k x_{t-k} + \eta_t$$
> où $\eta_t$ est un processus ARIMA. **Réécriture** :
> $$y_t = a + (\gamma_0 + \gamma_1 B + \gamma_2 B^2 + \cdots + \gamma_k B^k)x_t + \eta_t = a + \gamma(B)x_t + \eta_t$$
> $\gamma(B)$ est appelé une **fonction de transfert** puisque cela décrit la manière dont un changement dans $x_t$ est transféré à $y_t$. $x$ peut influencer $y$, mais $y$ n'est pas autorisée à influencer $x$.

Exemple assurance/publicité TV (slides 39–46) : comparer les modèles à 0–3 lags **sur la même période d'ajustement** (`Quotes = c(NA,NA,NA,Quotes[4:40])`), choisir par AICc (lag 1 optimal, AICc = 59.9, slide 42) ; modèle ajusté (slide 43) :
$$y_t = 2.155 + 1.253x_t + 0.146x_{t-1} + \eta_t, \qquad \eta_t = 0.512\eta_{t-1} + \varepsilon_t + 0.917\varepsilon_{t-1} + 0.459\varepsilon_{t-2}$$
Prévision sous scénarios de dépenses publicitaires futures (TVadverts = 10, 8, 6 ; slides 44–46).

## 8.4 Critères de choix de modèle du cours
- **AICc minimal** pour : le choix des prédicteurs (slide 8), le choix de $K$ dans les termes de Fourier (slide 28), le choix du nombre de lags (slides 41–42 : comparer AIC, AICc, BIC, sigma2, log_lik dans `glance(fit)` — le cours retient l'AICc).
- **Diagnostic** : résidus d'innovation ≈ bruit blanc (ACF/PACF + Ljung-Box), `gg_tsresiduals(fit)`.

---

# 9. simialrity_based_text_retrieval_slides.pdf

## 9.1 Identification
- **Titre** : *Similarity-Based Text Retrieval — From Basics to Vector Spaces*
- **Auteur** : Bala Priya C, 29th May, 2025
- **Langue** : **anglais**
- Diaporama, slides 1–22.

## 9.2 Concepts couverts
Vector space model, représentations de texte (word count, **TF-IDF**, Word2Vec), mesures de similarité (**similarité cosinus**, distance euclidienne, similarité de Jaccard), pipeline de recherche documentaire (retrieval).

## 9.3 Notations exactes

### Vector space model (slides 2–4)
Documents → vecteurs dans un espace de grande dimension ; « Closer points = More similar documents ».

### Méthode 1 : Simple Word Count (slide 5)
Comptage brut par terme ; ex : Doc1 = [2,1,0,1,1,1,0], Doc2 = [2,0,1,1,1,0,1]. Problème (slide 6) : les mots fréquents dominent → « **Solution:** Use TF-IDF to balance frequency with rarity! »

### Méthode 2 : **TF-IDF** (slide 7) — recopier ces formules exactes
> **TF-IDF = Term Frequency × Inverse Document Frequency**
>
> Term Frequency (TF) :
> $$TF(t,d) = \frac{\text{count of term } t \text{ in document } d}{\text{total terms in document } d}$$
>
> Inverse Document Frequency (IDF) :
> $$IDF(t) = \log\left(\frac{\text{total documents}}{\text{documents containing term } t}\right)$$
>
> TF-IDF Score :
> $$\text{TF-IDF}(t,d) = TF(t,d) \times IDF(t)$$
>
> **Intuition:** Rare words get higher scores, common words get lower scores.

Exemple chiffré (slide 8) : pour « cat » dans Doc 1 (3 docs) : $TF = \frac{1}{3} = 0.33$ ; $IDF = \log(\frac{3}{2}) = 0.18$ ; TF-IDF $= 0.33\times 0.18 = 0.06$.

### Méthode 3 : Word2Vec (slides 9–10)
Motivation : « "cat" and "kitten" should be similar, but TF-IDF treats them as completely different ». Apprentissage des sens par le contexte via réseau de neurones ; « Document vector = average of all word vectors in the document ».

### **Similarité cosinus** (slide 12)
> Measures the angle between two vectors. **Formula:**
> $$\cos(\theta) = \frac{\mathbf{A}\cdot\mathbf{B}}{|\mathbf{A}|\times|\mathbf{B}|} = \frac{\sum_{i=1}^n A_i B_i}{\sqrt{\sum_{i=1}^n A_i^2} \times \sqrt{\sum_{i=1}^n B_i^2}}$$
> **Range:** $[-1, 1]$ where $1$ = identical direction, $0$ = perpendicular, $-1$ = opposite.

Exemple (slide 12) : $A = [1,2,3]$, $B = [2,4,6]$ : $\cos(\theta) = \frac{1\times2 + 2\times4 + 3\times6}{\sqrt{1^2+2^2+3^2}\times\sqrt{2^2+4^2+6^2}} = \frac{26}{\sqrt{14}\times\sqrt{56}} = 1.0$.
« **Key Insight:** Cosine similarity ignores magnitude, only cares about direction » (slide 13).

### Distance euclidienne (slide 14)
$$d(\mathbf{A}, \mathbf{B}) = \sqrt{\sum_{i=1}^n (A_i - B_i)^2}$$
Conversion en similarité : $\text{Similarity} = \frac{1}{1 + \text{distance}}$. « Euclidean distance considers both direction and magnitude » (slide 15).

### Similarité de Jaccard (slide 16)
$$J(A, B) = \frac{|A \cap B|}{|A \cup B|} = \frac{\text{intersection}}{\text{union}}$$
Range $[0,1]$ ; adaptée aux features binaires/ensembles de mots. Exemple : Doc A = {cat, sat, mat}, Doc B = {cat, dog, mat} → $J = \frac{2}{4} = 0.5$.

## 9.4 Méthodes / pipeline recommandés
- **Combinaison de référence** (slide 18) : « Most common in text retrieval: **Cosine similarity with TF-IDF or Word2Vec** ».
- **Pipeline de recherche** (slides 20–21) : 1. Convert query to vector ; 2. Calculate similarity with all documents ; 3. Rank by similarity score ; 4. Return top documents.
- **Conseils pratiques** (slide 19) : *Preprocessing* : remove stopwords, lowercase, stemming ; *Dimensionality* : 50–300 dimensions pour Word2Vec ; *Speed* : approximate nearest neighbor search pour les grands corpus ; *Evaluation* : jugements humains de similarité. Outils : scikit-learn, gensim, sentence-transformers ; Elasticsearch, Faiss, Annoy.
- **Key takeaways** (slide 22) : 3 représentations (Count — simple mais limité ; TF-IDF — équilibre fréquence/rareté ; Word2Vec — sens sémantique) ; 3 similarités (Cosine — directionnelle, la plus populaire ; Euclidean — distance ; Jaccard — ensembles) ; « Choose based on your use case and data characteristics ».

---

# Annexe A — Concepts de la liste NON couverts (ou seulement effleurés)

À savoir pour le mémoire : si l'un de ces concepts est utilisé, il faudra citer une source externe car **aucun cours ne fournit de formalisme** :

| Concept | Statut dans les cours |
|---|---|
| Distribution Normale | Jamais définie formellement. Apparitions implicites : bruit blanc (SeriesTemp), priors gaussiens de BayesianRidge et $\mathcal{GP}(m(x), k(x,x'))$ (modèle_de_régression p. 6, 9), loi de la prévision `t(N(5.1, 0.00087))` en sortie R (SeriesTemp slide 23). |
| Z-Score | Uniquement cité comme outil de détection d'outliers (EDA p. 4, 6), aucune formule $z = \frac{x-\mu}{\sigma}$ donnée. |
| Corrélation de Pearson | Uniquement via `df.corr()` / `corrwith` (EDA p. 5, 7), pas de formule. |
| Naive Bayes | Absent. Le « classifieur de Bayes » $h^*$ de course.pdf (p. 3) est le prédicteur optimal théorique, pas l'algorithme Naive Bayes. |
| F1 Score | Seulement le mot-clé `"metric": "f1"` (EDA p. 3). |
| ReLU | Seulement le paramètre `activation="relu"` (modèle_de_régression p. 12). |
| Valeurs/vecteurs propres | Pas de cours dédié ; notions voisines : (semi-)définie positive via $v^\top H_f v$ (optim p. 2–3), valeurs singulières $\sigma_j$ du SVD (regularization p. 26). |
| Softmax | Absent ($\log\sum e$ / `logsumexp` mentionné, regularization p. 6). |
| KL Divergence | Absent. |
| Multiplicateur de Lagrange | Absent (le SVR de modèle_de_régression p. 8 est donné sous forme primale contrainte sans dérivation duale). |
| PCA | Absent (ACM mentionnée pour le qualitatif, clustering slide 6 ; SVD traité côté Ridge, regularization p. 26). |

# Annexe B — Divergences de notation entre cours (à harmoniser avec précaution dans le mémoire)

- **Paramètres du modèle** : $w$ (optim.pdf, modèle_de_régression.pdf), $\theta$ (regularization.pdf partie 2, course.pdf pour $f_\theta$), $\beta$ (SeriesTemp_ARIMAX pour la régression dynamique, GAM p. 13 de modèle_de_régression). Choisir la notation du cours cité.
- **Fonction objectif** : $f(x)$ ou $f(w)$ (optim), $L_n(h)$ (regularization), $R_n(h)$ / $R_{\mathcal{S}_n}(h)$ (course.pdf), $L_{n(\theta)}$ (regularization partie 2), $\mathrm{MSE}$ (modèle_de_régression, arbres).
- **Ridge** : trois écritures selon le cours — $\min_w \sum(y_i - w^\top x_i)^2 + \lambda\|w\|_2^2$ (modèle_de_régression p. 4) ; $f_\lambda(w) = \frac{1}{2n}\sum(\cdot)^2 + \frac{\lambda}{2}\|w\|_2^2$ avec solution $(X^\top X + n\lambda I_d)^{-1}X^\top y$ (optim p. 12, facteur $n$ !) ; $\|y - X\theta\|_2^2 + \lambda\|\theta\|_2^2$ avec solution $(X^\top X + \lambda I)^{-1}X^\top y$ (regularization p. 24–25).
- **Perte logistique** : $\frac{1}{n}\sum\log(1+\exp(-y_i w^\top x_i))$ avec $y_i\in\{0,1\}$ énoncé (optim p. 13 — noter que la formule suppose implicitement $y_i\in\{-1,+1\}$) ; $\ell_{\log}(y,f(x)) = \log(1+e^{-yf(x)})$ avec $y\in\{-1,+1\}$ et équivalence cross-entropy rigoureuse (course.pdf p. 33–35, version de référence).
- **Erreurs en séries temporelles** : $\eta_t$ (erreur de régression, ARIMA) vs $\varepsilon_t$ (bruit blanc) — distinction propre à SeriesTemp_ARIMAX, à respecter absolument.
- **Nombre de clusters/modèles** : $K$ (clustering), $M$ (bagging/BMA), $m$ (agrégation naïve, nb de features RF), $T$ (itérations AdaBoost).
- **Impureté** : $\mathcal{I}$, $\mathcal{I}_G$, $\mathcal{I}_{\mathcal{E}}$, $\mathcal{I}_{EC}$ (arbres slide 15–16) ; entropie en $\log_2$.
