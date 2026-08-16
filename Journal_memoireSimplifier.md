# Journal — simplification du chapitre « Copilote Financier »

Une entrée par fichier ou problème. Résumé en une ligne, puis détail.

## Audit préalable (data scientist senior, contexte neuf)

**Résumé : l'audit confirme le diagnostic du commanditaire — environ 60 %
du volume des notebooks relève de la démonstration académique — et
identifie le cœur pragmatique à raconter.**

- Verdicts par notebook : nb00 utile (deux résultats cœur : log-normalité
  des prix, piège de la corrélation brute) ; nb01 : la base SQL est le
  vrai livrable, Spark = test d'échelle à conclusion négative en trois
  phrases ; nb02 : démonstration académique sauf le comparateur de
  voisines ; nb03 : cœur pour la cible et le tableau des dépassements en
  euros (SQL pur), tournoi de 8 modèles indiscernable à n = 123 ; nb04 :
  le meilleur notebook (panel −19 %/point, ICC 0,66), ARIMAX réduit à un
  garde-fou ; nb05 : hédonique et diagnostic en détail, Lagrangien =
  élégance (une phrase) ; nb06 : trois chiffres métier, Naive Bayes en
  une phrase de limite.
- Angle éditorial retenu : « un petit jeu de données bien compris vaut
  mieux qu'un gros appareillage », avec les conclusions négatives du
  projet (Spark 58×, ARIMAX non identifiable, MLP sur-ajusté, élasticité
  non significative) présentées comme des résultats, pas des modules.
- Liste des 10 chiffres à savoir défendre à l'oral, reprise dans le
  chapitre.

## memoire/chapitre_copilote_financier.Rmd (version simplifiée)

**Résumé : le chapitre est réécrit en suivant l'audit — même sommaire
strict, ~40 % plus court, hiérarchie inversée (le cœur décisionnel en
détail, l'appareillage académique en une phrase quand il est mentionné).**

- Coupes principales par rapport à la version précédente : PCA/SVD/CAH et
  leurs figures (le comparateur et la frontière promotion/aménagement
  restent en une mention), descente de gradient et vérifications de forme
  close, dérivation lagrangienne détaillée (le résultat « remise uniforme
  en euros » est conservé, la preuve renvoyée aux notebooks), softmax et
  MLP (une phrase de contrôle du sur-ajustement), KL/entropie/centralités
  (les trois constats métier restent, les méthodes disparaissent),
  procédure ARIMAX détaillée (réduite au paragraphe garde-fou).
- Figures : 9 au lieu de 16 — suppression des figures d'appareillage
  (plan factoriel, dendrogramme, coefficients Ridge, convergence du
  gradient, KL, réseau) ; conservation des figures de décision
  (distributions, intensité, variation de marge, scénarios, écoulement,
  millésime, stock, deux pages de la plateforme).
- Section 4.2 imposée par le sommaire alors que Spark est jugé
  académique : traitée honnêtement — la base SQL comme livrable, Spark en
  trois phrases avec le chiffre mesuré (58×, en signalant qu'une
  exécution antérieure donnait 28× : conclusion robuste, chronométrage
  variable).
- Aucun trou par rapport au sommaire : toutes les sections correspondent
  à du travail réellement présent sur main.

## Livrables PDF et DOCX

**Résumé : .docx via pandoc (comme la version précédente) et .pdf via
pandoc + pdflatex (texlive minimal installé dans l'environnement).**

## Vérification finale en contexte neuf

**Résumé : PASS sur les 5 points (sommaire strict, ~45 chiffres tous
conformes, pertinence éditoriale, 9 figures, rendus .docx et .pdf), avec
une réserve documentaire levée ci-dessous.**

- Seule réserve : « 118 opérations jointes, écart médian nul » (la
  réconciliation Budget & EFR / LIVE) n'était tracé dans aucune cellule
  exécutée — le vérificateur, avec d'autres clés de jointure, obtenait 80
  ou 173. La clé correcte est l'ancien code d'opération (`GR_xxx`) :
  `Code Operation old` côté Budget & EFR contre `BUDGET_CODE_OPERATION`
  côté LIVE, en comparant la somme des dépenses budgétées HT (niveau 0
  « Dépenses » côté LIVE). Ré-exécuté ce jour :
  **118 opérations jointes, écart relatif médian 0,0, 118/118 sous 1 %.**
  À savoir refaire à l'oral :

  ```python
  efr = budget_efr[budget_efr["Depenses / Recettes"] == "Dépenses"] \
        .groupby("Code Operation old")["Budget HT"].sum()
  liv = live[(live.BUDGET_NIVEAU == 0)
             & (live.BUDGET_LIBELLE_POSTE == "Dépenses")] \
        .groupby("BUDGET_CODE_OPERATION")["BUDGET_MONTANT_HT"].sum()
  cmp = pd.concat([efr, liv], axis=1, keys=["efr", "live"]).dropna()
  # -> 118 lignes ; (efr - live).abs() : médiane nulle
  ```
- Autre point utile pour l'oral, confirmé par le vérificateur : les
  chiffres de la plateforme (147 / 68 / 10 / 2 / 421 / 4,8 / 3,11 %) sont
  reproduits indépendamment depuis la base et le modèle sérialisé — ils ne
  sont pas seulement lus sur la capture d'écran.
