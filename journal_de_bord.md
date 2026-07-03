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
  Dépenses, budget vs engagé/facturé) ; le périmètre d'apprentissage de
  l'axe A, arrêté au notebook 03, compte **123 opérations** (engagement
  ≥ 60 %, marge budgétée > 50 k€, recettes budgétées > 0) — petit
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

## Étape 5 — Notebook 00 : exploration des données (EDA)

**Résumé : EDA menée en suivant pas à pas la checklist du cours (problème →
qualité → univarié → bivarié → catégoriel → temporel → manquants →
anti-fuite → synthèse), avec une leçon de méthode sur les corrélations en
niveaux.**

- Le prix au m² est log-normal en bonne approximation (diagramme
  quantile-quantile avant/après log) : l'axe C modélisera le log-prix.
  Sources : *EDA_for_Data_Science* p. 6 (transformation log), z-score et
  IQR (p. 4, 6) ; distribution normale introduite avec source externe (les
  PDF ne la formalisent pas, cf. Annexe A de `docs/reference_cours.md`).
- Piège déjoué : la corrélation de Pearson brute réservations ↔ taux
  d'intérêt est nulle (+0,07) alors que le lien économique existe — effet
  de la croissance du portefeuille (non-stationnarité). Sur l'intensité
  (réservations par opération active), r = −0,34 avec le taux et +0,44
  avec la confiance des ménages. J'avais d'abord écrit la conclusion
  attendue avant de vérifier la sortie : le chiffre réel m'a contredit,
  le notebook documente désormais le piège. Leçon : toujours confronter
  chaque commentaire à la cellule exécutée. Source : mise en garde
  *spurious regression* de *SeriesTemp_ARIMAX* slide 3.
- Anti-fuite : `depenses_engagees` entre dans la définition de la cible de
  l'axe A → exclue des variables explicatives (convention `corrwith` du
  cours EDA p. 7).

## Étape 6 — Notebook 01 : SQL et passage à l'échelle Spark

**Résumé : la couche d'ingestion est démontrée en SQL pur (jointures,
agrégats, vues, fonction fenêtre) puis en PySpark, avec une conclusion
honnête sur la volumétrie.**

- Les modules SQL et données massives n'ont pas de PDF dans `Cours/` : le
  notebook le signale et suit la terminologie standard (Codd ; Dean &
  Ghemawat pour MapReduce ; Zaharia pour Spark).
- Contrôle croisé Spark ↔ SQLite à l'euro près (dépenses 1 561,8 M€,
  recettes 1 754,8 M€ par les deux moteurs).
- Leçon d'échelle : sur 64 788 lignes, Spark est ~28× plus lent que pandas
  (démarrage de session 27 s, conversion 6 s, overhead JVM) — le passage à
  l'échelle est une assurance pour les volumétries futures (groupe Nexity
  entier), pas un gain immédiat. Un étudiant qui vend Spark comme
  accélérateur sur 25 Mo se trompe de problème.

## Étape 7 — Notebook 02 : analyse multidimensionnelle et typologie

**Résumé : PCA écrite à la main (covariance → valeurs/vecteurs propres),
vérifiée par SVD, puis typologie des opérations en 4 types par K-moyennes
(Lloyd maison = sklearn) et CAH de Ward.**

- La dérivation PCA (maximiser $v^\top\Sigma v$ sous $\|v\|=1$) introduit
  le multiplicateur de Lagrange avec source externe (Azencott) — la PCA est
  absente des PDF ; le pont avec le cours est fait par le SVD de
  *regularization.pdf* p. 26 (vérification numérique : valeurs propres de
  la covariance = $\sigma_j^2/(n-1)$ à 1,8·10⁻¹⁵ près).
- K choisi en arbitrant les critères internes du cours de clustering
  (coude, silhouette slide 11, Davies-Bouldin slide 10) contre la lecture
  métier : K=2 optimal numériquement mais redécouvre la ligne
  promotion/aménagement ; K=4 retenu pour sa valeur d'usage. Accord
  K-moyennes/CAH : indice de Rand ajusté 0,86 (évaluation slide 29).
- La similarité cosinus (formule exacte du cours de text retrieval slide
  12) fournit le comparateur d'opérations demandé par le besoin B-A3.

## Étape 8 — Notebook 03 : axe A, prédiction de la dérive de marge

**Résumé : cible « dérive committée » définie sans fuite (max(engagé,
budget) par poste), régression OLS/Ridge/Lasso puis classification du
risque (logistique, SVM, arbres, forêt, softmax, MLP) comparées au F1.**

- Deux pièges de rang rencontrés et documentés dans le notebook : les
  parts de postes somment à 1 (colinéarité parfaite avec le biais → poste
  de référence retiré, condition rang(X)=d de la Prop. 2.6.1 d'optim.pdf)
  et un poste quasi constant donnait une colonne standardisée nulle.
- La descente de gradient maison converge vers la forme close avec le pas
  1/L du théorème 3.4 (L = plus grande valeur propre de la Hessienne — les
  valeurs propres servent aussi en optimisation). La logistique sans
  pénalité voit ses poids diverger sur directions quasi séparantes alors
  que la log-perte converge : argument concret pour la régularisation L2.
- Résultats honnêtes : R² test ≈ 0,08 (la structure budgétaire initiale
  prédispose, elle ne détermine pas) ; F1 ≈ 0,30-0,34 contre 0 en baseline ;
  le MLP ReLU sur-ajuste comme prévu (F1 train 0,91 vs CV 0,26) — illustre
  la borne VC de course.pdf sur petit n. Trois visages du MLE dans un même
  notebook : OLS gaussien, cross-entropy logistique, log-perte softmax.

## Étape 9 — Notebook 04 : axe B, vitesse d'écoulement

**Résumé : modèle à effets aléatoires sur le panel opération × mois
(effet causal du taux), ARIMAX selon la procédure du cours (constat
d'inidentifiabilité honnête), et sigmoïde d'écoulement.**

- Panel de 3 230 observations (mois à zéro réintroduits — sans eux le
  rythme est surestimé). ICC = 0,66 ; +1 point de taux ⇒ −19 % de
  réservations (p < 10⁻¹⁵) ; le pooled OLS surestime l'effet.
- Leçon majeure : sur la série agrégée (114 mois), une fois les erreurs
  ARIMA modélisées (procédure slide 8 : résidus blancs via Ljung-Box PUIS
  AICc), le coefficient du taux devient indiscernable de zéro — variation
  trop lente pour 114 points. Décision : scénarios 2026 = trajectoire
  ARIMA × élasticité du panel (esprit fonction de transfert, slides
  37-46). Détente à 2,5 % : +6 % de rythme en moyenne ; remontée à
  3,5 % : −3 %.
- La sigmoïde (curve_fit) bat l'ajustement linéaire sur 25/28 opérations
  terminées ; L inidentifiable en début de commercialisation (constat
  vérifié) — délai médian à 90 % du potentiel ≈ 20 mois.

## Étape 10 — Notebook 05 : axe C, prix hédonique et optimisation

**Résumé : modèle hédonique (R² test 0,886), diagnostic du stock,
élasticité sourcée, et optimisation sous contrainte résolue analytiquement
(Lagrange) puis numériquement (gradient projeté ≈ SLSQP).**

- Primes hédoniques cohérentes : étage, Sud, −63 % pour le social
  (réglementé), effet millésime +19 % entre 2016 et 2023 — les prix du
  neuf n'ont pas baissé avec les taux, c'est le volume qui s'est ajusté.
- Élasticité interne −0,81 mais non significative (p = 0,57) : ε = −1
  retenu, bas de fourchette de la littérature (Meen 2001 ; DiPasquale &
  Wheaton 1994), compatible avec notre estimation. Documenté plutôt que
  masqué.
- Résultat d'optimisation non trivial : à ε = −1, la condition du premier
  ordre du lagrangien donne p_j·δ_j = λ — remise optimale identique en
  EUROS sur tous les lots (λ* = −23 k€ sur ARPEGGIO), donc % plus fort sur
  les petits lots ; les bornes −10 % remplacent la condition intérieure
  (KKT) sur 2 lots. Gradient projeté et SLSQP concordent à 0,006 près.
- Premier cas d'application mal posé (opération à écoulement rapide,
  cible de volume infaisable dans les bornes) : détecté à l'exécution,
  q0 réestimé par le taux d'écoulement des 12 derniers mois. Leçon :
  l'optimiseur doit être appliqué là où le problème métier se pose.

## Étape 11 — Notebook 06 : signaux faibles (texte et réseau)

**Résumé : TF-IDF et cosinus aux formules exactes du cours, Naive Bayes
anti-fuite sur les commentaires (F1 0,34 vs 0 en baseline), KL divergence
comme détecteur de qualité de saisie, graphe vendeurs-opérations.**

- Fuite évitée : 314 commentaires mentionnent explicitement le
  désistement (98,4 % de désistés) → retirés du corpus d'apprentissage
  avec les mots directement révélateurs.
- La KL divergence désigne Salon-de-Provence comme profil de motifs le
  plus atypique (3,0 bits vs < 0,3) — en réalité un défaut de saisie
  (90 % « Autres motifs ») : la divergence sert de détecteur de qualité de
  données avant d'être un signal commercial. Erreur corrigée en relecture :
  ma première lecture citait des chiffres non conformes à la sortie
  exécutée (entropie 0,56 au lieu de 0,47 ; motif dominant de Toulouse mal
  attribué) — reprise après vérification systématique sorties ↔ texte.
- Réseau : 2 vendeurs (dont la force de vente interne) concentrent 51,6 %
  des dossiers attribués — dépendance commerciale à surveiller. Module
  sans PDF dans le dépôt : formalisme standard (Newman) signalé.

## Étape 12 — Plateforme Streamlit

**Résumé : application en 5 pages branchée sur la base SQLite et les
modèles des notebooks, chaque page vérifiée sans exception via AppTest.**

- Choix d'architecture : les modèles rapides (hédonique) sont ré-entraînés
  au démarrage avec cache, le classifieur de risque est sérialisé par le
  notebook 03 (joblib) — tout est régénérable depuis les exports bruts.
- Les pages reprennent les conventions des notebooks (mêmes définitions
  SQL, même anti-fuite, élasticité du panel) : une seule source de vérité
  par indicateur.
- Confidentialité respectée : aucune donnée nominative de client affichée.

## Étape 13 — Audit final en contexte neuf

**Résumé : un auditeur indépendant a tout re-vérifié par exécution (base,
notebooks, couverture de la consigne, plateforme) ; verdict PASS, avec 4
incohérences texte ↔ sortie et un chiffre non traçable, tous corrigés.**

- PASS confirmés : base conforme au dictionnaire (comptages exacts), 7
  notebooks sans erreur et 100 % des cellules exécutées, les 24 concepts
  et 9 modules couverts, les 5 pages de la plateforme sans exception.
- Corrections issues de l'audit : (1) nb06 — les vendeurs centraux
  désistent en réalité MOINS que les périphériques (16,9 % vs 20,2 %), le
  texte disait l'inverse ; (2) nb06 — précision de la logistique 0,72 (et
  non 0,63) ; (3) nb05 — 95 opérations (et non 92), ε = −0,81, p = 0,57 ;
  (4) nb00 — motif dominant 42 % (et non ≈ 45 %) ; (5) le « 144 opérations
  exploitables » du cadrage, invérifiable, remplacé partout par le
  périmètre traçable du notebook 03 (123 opérations : engagement ≥ 60 %,
  marge > 50 k€, recettes > 0).
- Leçon d'humilité : ma « vérification systématique sorties ↔ texte »
  avait laissé passer ces cas — une relecture par un regard neuf qui
  ré-exécute tout n'est pas un luxe, c'est une étape de la démarche.

## Étape 14 — Refonte métier de la plateforme (retour du commanditaire)

**Résumé : la plateforme est refondue pour la direction financière —
langage métier sans jargon statistique, design professionnel, et périmètre
restreint aux 147 opérations de promotion (aménagement exclu).**

- Retour utilisateur : la première version était « trop data science »
  pour ses destinataires. Leçon de conduite de projet : l'outil de
  restitution ne s'adresse pas au jury du mémoire mais au métier — les
  métriques de validation (F1, R²) restent dans les notebooks, l'écran ne
  montre que des décisions possibles (« niveau d'alerte », « prix de
  marché estimé », « sensibilité de la demande au coût du crédit »).
- Périmètre : l'activité aménagement (120 opérations) est exclue de tous
  les indicateurs de la plateforme (`operations.activite = 'Promotion'`) ;
  les notebooks conservent les 267 opérations car la distinction
  promotion/aménagement y est un résultat d'analyse (typologie du
  notebook 02). Le modèle de risque, entraîné toutes activités, ne score à
  l'écran que les lignes promotion.
- Pages : Vue d'ensemble (5 indicateurs, top 5 des opérations à examiner),
  Alertes marge (68 opérations en cours : 10 alerte / 2 à surveiller / 56
  conformes, détail des postes en dépassement en euros), Rythme de vente
  (simulateur de taux 2026 en phrases claires), Pilotage des prix (127
  appartements évalués : 111 dans le marché, 4 au-dessus, 12 en dessous ;
  grille recommandée lot par lot), Qualité commerciale.
- Vérification : les 5 pages passent AppTest sans exception ; contrôle
  indépendant du filtre (147 opérations affichées) et de l'absence de
  jargon à l'écran.
