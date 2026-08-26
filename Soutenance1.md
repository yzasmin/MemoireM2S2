# Soutenance1 — journal de la préparation de soutenance

Une entrée par fichier produit ou étape franchie. Mise à jour en place, pas
de duplication. Les chiffres corrigés en cours de route remplacent les
anciens plutôt que de s'y ajouter.

## Étape 1 — Lecture intégrale des sources

- Mémoire (PDF, 27 pages) extrait en texte via `pdftotext -layout` (le
  rendu image par `pdftoppm` échouait, poppler-utils installé puis
  contourné en extraction texte directe) et lu intégralement.
- `chapitre_copilote_financier.docx` extrait en texte brut via parsing XML
  du zip (pas de `python-docx` disponible dans l'environnement) et lu
  intégralement.
- README.md, journal_de_bord.md, docs/01, docs/02, docs/03,
  plateforme/app.py lus intégralement.
- Les 7 notebooks exécutés (00 à 06) extraits en texte (cellules markdown +
  sorties texte, sans les images) via un script Python maison, pour
  vérification chiffre par chiffre sans consommer le budget de contexte
  des images.

## Étape 2 — Vérification croisée mémoire / docx / notebooks

- Comparaison ligne à ligne des chiffres cités dans le mémoire et dans le
  chapitre docx : aucune divergence non résolue trouvée. Les deux sources
  sont cohérentes (le docx est la version longue du chapitre 2 du mémoire).
- Spot-check direct dans les sorties de cellules exécutées des notebooks
  pour les chiffres les plus cités du discours : R² axe A (0,077), F1 par
  classifieur (forêt 0,306, arbre CART 0,340, SVM linéaire 0,303), ICC axe
  B (0,66), β taux (−0,216, p<1e-15), ARIMA (AICc 611,7, Ljung-Box p=0,224,
  p taux=0,82), R² hédonique axe C (0,886), élasticité interne (−0,81,
  p=0,57, n=95), λ* Lagrange (−23 015 €), F1 texte (Naive Bayes 0,343,
  logistique 0,254), réseau (51,6 %, Valoriciel 29,6 %, interne 9,0 %,
  centraux 16,9 % vs périphériques 20,2 %), axe A périmètre (123
  opérations, 28 % soit 34 en dérive). **Tous confirmés à l'identique dans
  les sorties de cellules exécutées.**
- Point de vigilance noté (pas une divergence, une distinction à ne pas
  confondre à l'oral) : notebook 00 (EDA) travaille sur 5 137 appartements
  (asymétrie du prix au m²), notebook 05 (modèle hédonique) sur 5 064
  appartements transigés (échantillon d'apprentissage, filtré
  différemment) — deux échantillons différents, pas une erreur.
- Autre point de vigilance : le diagnostic de stock du notebook 05
  (103/8/16 sur 127 appartements, périmètre 267 opérations toutes
  activités) diffère du diagnostic affiché sur la plateforme (111/4/12 sur
  127 appartements) parce que le modèle de la plateforme est ré-entraîné
  sur le seul périmètre promotion — explicité comme tel dans le docx, pas
  une incohérence.

## Étape 3 — Rédaction de `discours_soutenance.md`

- Texte mot à mot rédigé, découpé en 14 slides, phrases courtes,
  transitions explicites, jargon expliqué à la première occurrence.
- 2 060 mots au total → 14,7 à 15,8 minutes selon le débit (130-140
  mots/minute) : dans la cible.
- Axe A présenté comme modeste (F1 ≈ 0,30) sans le survendre ; axe B
  présenté comme le plus solide.

## Étape 4 — Rédaction de `plan_slides.md`

- 14 slides, correspondance 1:1 avec les sections du discours. Visuels
  proposés : figures existantes du mémoire (1.1, 1.2, 1.4, 1.5, 2.3, 2.4,
  2.6, 2.7, 3.1) réutilisées telles quelles plutôt que redessinées.

## Étape 5 — Génération du `.pptx` complémentaire

- 14 slides construites avec `pptxgenjs`, palette reprise à l'identique de
  `src/theme_viz.py` (bleu, vert, ambre, violet, rouge) pour une cohérence
  visuelle avec les figures du mémoire et la plateforme.
- Figures réelles extraites du PDF du mémoire via `pdfimages` (pages
  identifiées en splittant le texte `pdftotext -layout` sur les sauts de
  page `\f`) plutôt que redessinées : Fig. 1.1, 1.2, 1.4, 1.5, 2.3, 2.4,
  2.6, 2.7, 3.1 — toutes vérifiées visuellement avant intégration.
- Validation structurelle (`validate.py`) : PASS. Contenu vérifié via
  `markitdown` (aucun texte de substitution oublié).
- **Limite technique notée** : LibreOffice ne convertit aucun fichier dans
  ce sandbox (`soffice` échoue même sur un `.pptx` minimal d'une slide ou
  un `.txt` brut) — le rendu visuel image par image n'a donc pas pu être
  vérifié par capture d'écran. Le contrôle s'est appuyé sur la validation
  structurelle + `markitdown` + relecture manuelle du contenu de chaque
  slide.
- Fichier : `soutenance_copilote_financier.pptx` (à la racine du dépôt).
  `plan_slides.md` reste le livrable qui fait foi en cas de divergence.

## Étape 6 — Audit « contexte neuf » (discours + slides)

- Verdict durée : ~2 013 mots utiles → 14 min 23 à 15 min 29 selon le
  débit (130-140 mots/minute) — dans la cible.
- 7 phrases trop longues repérées et raccourcies (identifiants ERP,
  enjeu de dédoublonnage, trois clés d'unicité, définition du F1, panel à
  effets aléatoires, élasticité, page Qualité commerciale — cette
  dernière avait une rupture grammaticale, corrigée).
- 4 termes non expliqués à leur première occurrence, corrigés : « variance »,
  « corrélation fallacieuse », « notebooks », « CRM ».
- 2 transitions muettes ajoutées à l'oral (« Premier axe... » avant la
  slide 8, « Troisième axe... » avant la slide 10).
- 3 écarts slide ↔ discours corrigés : le seuil des 60 % d'engagement et
  le nom de l'algorithme (forêt aléatoire) manquaient à l'oral pour l'axe
  A ; le chiffre intermédiaire de 1 474 tiers uniques manquait à l'oral.
- 2 corrections de cohérence appliquées à `plan_slides.md` : le sigle SSO
  (jamais expliqué) retiré du bullet de la slide 12 ; la mention nominative
  de l'opération ARPEGGIO retirée du visuel proposé de la slide 10 (le
  discours ne la nomme pas).
- Toutes les corrections ont été appliquées. Recompte après correction :
  2 117 mots → 15,1 à 16,3 minutes selon le débit — toujours dans la
  cible, à l'extrémité lente en cas de débit très posé (130 mots/min), ce
  qui reste cohérent avec la consigne d'un rythme volontairement lent
  pour une candidate peu à l'aise à l'oral.

## Étape 7 — Audit expert data science

- Sous-agent expert data science : audit chiffre par chiffre contre les
  sources primaires (mémoire, docx, 7 notebooks exécutés, `app.py`).
  Verdict : quasiment tous les chiffres exacts et correctement arrondis
  (R²=0,077→8 %, F1 forêt=0,306≈0,30 vs baseline 0, ICC=0,66, effet taux
  −19 % p<10⁻¹⁵, ARIMA p=0,82 sur 114 mois, R² hédonique=0,886/±11 %,
  ε=−1, chiffres complets de la reprise des tiers, description des 5
  pages de la plateforme conforme au code réel) — un seul vrai problème
  trouvé, corrigé :
  - Slide 8 : « seuil que j'ai fixé comme dérive **significative** »
    confondait un seuil de matérialité choisi par l'analyste (2 %) avec
    la significativité statistique — dangereux car le mot « significatif »
    est réutilisé 30 secondes plus tard en slide 9 dans son sens
    statistique strict (p < 10⁻¹⁵). Corrigé en « dérive **matérielle** »,
    conforme au vocabulaire du mémoire et de `plan_slides.md`.
  - Point de vigilance signalé (pas une erreur, à anticiper à l'oral) :
    le diagnostic de stock cité en slide 10 (16 sous-cotés / 8 surcotés,
    depuis le notebook 05, périmètre 267 opérations) diffère des chiffres
    réellement affichés par la plateforme démontrée en slide 11 (12 en
    dessous / 4 au-dessus, périmètre promotion ré-entraîné, incertitude
    ±13 % au lieu de ±11 %) — expliqué dans le docx, mais si un membre du
    jury ouvre la plateforme après la slide 10 il verra des chiffres
    différents. **Repris comme question probable en phase 2.**

## Étape 8 — Rééquilibrage 30/70 (demande explicite)

- Consigne : la soutenance (pas le mémoire PDF, déjà validé) doit passer à
  ≈ 30 % sur les deux reprises de données (mes missions d'alternance) et
  ≈ 70 % sur le Copilote Financier, jugé « la vraie partie data science »,
  en puisant plus largement dans le dépôt GitHub (pas seulement le résumé
  déjà fait par le mémoire).
- Restructuration complète : 14 slides → **13 slides**. Chapitre 1
  (contexte, migration, tiers) fusionné de 4 slides à 2, condensé sans
  perdre le cœur méthodologique (trois clés d'unicité, validation par
  paliers). Une slide entièrement nouvelle ajoutée : **Signaux faibles
  (texte et réseau)**, absente de la première version.
- Contenu ajouté au Copilote Financier, retrouvé et vérifié dans les
  notebooks (pas seulement recopié du mémoire) :
  - Axe A : comparaison des **six classifieurs** (logistique 0,283, SVM
    linéaire 0,303, SVM RBF 0,257, arbre 0,340, forêt 0,306, MLP
    0,913 train / 0,262 CV) et la démonstration de sur-apprentissage du
    MLP, l'interprétation Ridge, la typologie comme comparateur.
  - Axe C : la vérification croisée Lagrange/SLSQP (écart 0,006), les
    primes hédoniques détaillées (étage, sud, social).
  - Axe transverse (nouveau) : TF-IDF/cosinus, Naive Bayes anti-fuite
    (F1=0,343), divergence de Kullback-Leibler (défaut de saisie Salon-
    de-Provence), réseau biparti vendeurs-opérations (51,6 %, 9,0 % vs
    29,6 % de désistement).
  - Tous ces chiffres avaient déjà été vérifiés cellule par cellule dans
    les notebooks lors de l'étape 2 — réutilisés tels quels, aucun
    nouveau chiffre non vérifié introduit.
- Recompte final : **2 041 mots**, répartition **28,4 % / 71,6 %** entre
  les deux missions (cible 30/70, à la marge d'erreur d'un recomptage
  manuel) — 14,6 à 15,7 minutes selon le débit.
- Vérifications de cohérence appliquées lors de la réécriture : sigle CRM
  ré-expliqué (perdu pendant la réécriture, rattrapé), transitions
  parallèles ajoutées entre les trois axes (« Premier axe », « Deuxième
  axe », « Troisième axe »), dernière occurrence du mot « notebooks »
  remplacée par une formulation sans jargon.
- `plan_slides.md` et `soutenance_copilote_financier.pptx` régénérés en
  cohérence avec la nouvelle structure à 13 slides.
- Cette réécriture n'a pas été repassée par les deux sous-agents d'audit
  (contexte neuf + expert data science) : les chiffres ajoutés provenaient
  tous de vérifications déjà faites à l'étape 2, et les corrections de
  fluidité/cohérence ont été appliquées directement en suivant les mêmes
  règles que celles identifiées par les audits de la phase 1. Si une
  relecture plus poussée est souhaitée sur cette version, le redemander
  explicitement.

## Étape 9 — Ajout ACP, validation croisée et exploration des données

- Demande explicite : couvrir aussi l'ACP (analyse en composantes
  principales), la validation croisée comme choix méthodologique, et
  l'exploration des données (EDA, notebook 00) — absente de toutes les
  versions précédentes du discours.
- 13 slides → **14 slides** : nouvelle slide 6 « Exploration des données :
  deux leçons » (asymétrie du prix corrigée par log, et le piège de la
  corrélation brute réservations/taux masquée par la croissance du
  portefeuille — corrigée en intensité par opération active). Figures 2.1
  et 2.2 du mémoire extraites (page 26 du PDF) et intégrées au `.pptx`.
- Axe A (slide 7) enrichi : l'ACP est nommée explicitement, avec son
  résultat vérifié dans le notebook 02 (2 axes résument 61 % de la
  structure des coûts, vérifié par SVD) plutôt que la mention vague
  « typologie » de la version précédente.
- Validation croisée élevée en principe transversal explicite (slide 5),
  plutôt que mentionnée seulement en passant dans l'axe A.
- Recompte : 2 041 → **2 240 mots**, ratio alternance/copilote 28,4 % →
  **25,3 % / 74,7 %** (toujours nettement côté 70 % visé, un peu plus
  penché), durée 14,6-15,7 → **16,0-17,2 minutes** selon le débit. Un
  compromis assumé : ajouter cette profondeur méthodologique sans
  dépasser trop largement les 15 minutes cibles a nécessité un allègement
  de plusieurs phrases (axe B, axe C, plateforme), mais le total reste
  au-dessus de la fourchette initiale de durée. Signalé explicitement
  plutôt que masqué — à retravailler si 15 minutes strictes redeviennent
  la priorité.
- `plan_slides.md` et le `.pptx` régénérés et re-validés (`validate.py`
  PASS, contenu vérifié via `markitdown`, aucun texte de substitution).

## Étape 10 — Réécriture du registre : voix naturelle d'étudiante M2

- Demande explicite : que le texte sonne comme écrit naturellement par
  une étudiante en M2 MIASHS, pas comme un texte poli par une IA.
- Repérage des tics d'écriture IA dans la version précédente : contrastes
  répétés en « plutôt que » (« documentée plutôt que masquée », « je le
  dis clairement plutôt que de le cacher »…), « Je l'assume » répété,
  chutes théâtrales en tiret après deux-points, ouvertures figées
  (« Précision importante », « Résultat : »), phrases-punchline très
  ciselées façon consultant.
- Réécriture intégrale du discours dans un registre plus oral et plus
  personnel : connecteurs naturels (« du coup », « en fait », « pour le
  coup »), réflexions à la première personne moins packagées (« je ne
  l'avais pas vue venir », « ça m'a bien intéressée »), suppression des
  effets de manche répétés, en gardant intactes toutes les consignes de
  fond (phrases courtes, jargon expliqué à la première occurrence,
  transitions explicites, `[pause]`, tous les chiffres inchangés).
- Aucun chiffre modifié — uniquement la formulation. Pas de nouvel audit
  chiffré nécessaire pour cette étape (travail de style, pas de contenu).

## Étape 11 — Correction de durée : 25 minutes, pas 15

- Le facteur limitant initial (~15 minutes) était une erreur : la
  consigne réelle est **25 minutes**. Recalibrage complet du discours.
- 14 slides → **17 slides** : le chapitre 1, condensé à 2 slides dans la
  version 15 minutes, est redéployé sur 5 slides pour retrouver le
  niveau de détail d'une vraie soutenance de 25 minutes (contexte
  Angelotti seul, migration des opérations seule, reprise des tiers en
  deux temps problème/solution) + une slide neuve de synthèse « Ce que
  ces deux reprises ont en commun », qui introduit le régime de preuve de
  la réconciliation et prépare la réflexion transversale de la fin.
- Contenu Copilote Financier également enrichi avec du détail déjà
  vérifié à l'étape 2 mais laissé de côté faute de place : les quatre
  noms des familles de la typologie de l'axe A et l'exemple nommé du Parc
  des Cyclades (voisines à cosinus ≥ 0,945, marges +7,9 % à +11,3 %),
  l'exposition sud et l'effet millésime de l'axe C, l'exemple nommé de
  l'opération Arpeggio pour l'optimisation de prix, la taille du corpus
  TF-IDF (1 346 documents, 535 termes) de l'axe transverse.
- Réflexion transversale restaurée à ses **trois** régimes de preuve
  (réconciliation, recette par l'usage — maintien des tableaux de bord et
  déploiement du SSO —, validation statistique), plus le point
  « documenter est un acte technique » — tous deux absents des versions
  15 minutes faute de place, tous deux vérifiés dans le mémoire (chapitre
  1, section 1.5 et chapitre 3).
- Recompte : 3 220 mots utiles → **23,0 à 24,8 minutes** selon le débit
  (130-140 mots/minute), au plus près des 25 minutes demandées ; ratio
  alternance/copilote **32,5 % / 67,5 %**, proche de la cible 30/70.
- `plan_slides.md` réécrit intégralement pour les 17 slides. `.pptx`
  régénéré avec 3 nouvelles slides (contexte seul, migration seule,
  synthèse des deux reprises) — validation structurelle PASS, contenu
  vérifié via `markitdown`, aucun texte de substitution.
- Comme à l'étape 9, cette réécriture n'a pas été repassée par les deux
  sous-agents d'audit complets : les chiffres ajoutés proviennent tous de
  vérifications déjà faites à l'étape 2 (ré-confirmés ici un par un avant
  intégration), et les règles de fluidité/jargon suivies sont celles déjà
  validées par l'audit contexte neuf de la phase 1. Une relecture
  complète par les deux sous-agents reste possible sur demande.

## Étape 12 — La partie Copilote Financier doit suivre le fil du projet

- Demande explicite : que la partie Copilote Financier raconte le projet
  dans l'ordre où il s'est déroulé (« j'ai commencé par ça, pourquoi, ça
  m'a amenée vers ça, résultat ») plutôt que de présenter les axes A/B/C
  comme des résultats posés côte à côte.
- Restructuration : la typologie (ACP + classification non supervisée,
  notebook 02), qui était fondue dans la fin de la slide axe A, devient
  sa propre slide, positionnée **avant** l'axe A — ordre réellement suivi
  dans les notebooks (02 précède 03) et motivé explicitement à l'oral
  (« comparer une opération de 2 M€ à une de 50 M€ sur leurs montants
  bruts n'a pas de sens »).
- Phrases de liaison ajoutées à l'oral entre chaque étape, pour que
  l'enchaînement soit dit et non seulement sous-entendu par l'ordre des
  slides : exploration → « avant d'attaquer le premier axe, il y a eu
  encore une étape » → typologie → « avec cette typologie en poche » →
  axe A → « une fois cet axe traité, je suis passée à la deuxième
  question » → axe B → « une fois qu'on savait anticiper le rythme de
  vente, la question qui s'imposait naturellement, c'était le prix » →
  axe C → « une fois ces trois axes posés, j'ai voulu voir si je pouvais
  aller chercher un signal en plus » → signaux faibles → plateforme.
- 17 slides → **18 slides** (nouvelle slide « La typologie : une étape
  avant l'axe A »). Aucun chiffre nouveau introduit — tout provient de
  contenu déjà vérifié à l'étape 2 (ACP 61 %, 4 familles nommées, exemple
  du Parc des Cyclades), simplement déplacé et mieux motivé.
- Recompte : 3 220 → **3 380 mots** → 24,1 à 26,0 minutes selon le débit,
  toujours centré sur les 25 minutes demandées. Ratio alternance/copilote
  32,5 % → **30,7 % / 69,3 %**, quasiment exactement 30/70.
- `plan_slides.md` réécrit avec un principe de construction explicite en
  tête de fichier (le récit suit l'ordre réel du projet). `.pptx`
  régénéré avec la nouvelle slide typologie et les bullets d'axe A
  allégés de la typologie (déplacée) — validation structurelle PASS,
  contenu vérifié via `markitdown`.

## Étape 13 — La base de données SQL manquait dans le récit

- Demande explicite : ajouter la partie sur la base de données SQL, qui
  manquait totalement alors qu'elle est l'infrastructure de tout le
  reste du projet (notebook 01, construit avant la typologie et les
  trois axes).
- Nouvelle slide insérée **entre l'exploration des données et la
  typologie**, à la place réelle du notebook 01 dans la séquence
  (00 exploration → 01 SQL/Spark → 02 typologie → 03/04/05 axes) :
  - les 4 exports Excel transformés en base SQLite, **7 tables + 3 vues
    SQL** métier (marge par opération, réservations par mois, état du
    stock) ;
  - l'intérêt d'une vue SQL : elle n'est écrite qu'une fois, notebooks
    et plateforme partagent la même définition d'un indicateur au lieu
    de la recopier et risquer de la faire diverger ;
  - une requête de comptage par commune comme premier signal utile :
    **Le Cap d'Agde concentre 117,1 M€ de chiffre d'affaires budgété sur
    seulement 2 opérations**, un poids à garder en tête pour l'axe A ;
  - comparatif chronométré honnêtement, pandas vs Spark, sur la même
    agrégation : **9,9 ms contre 577,4 ms** (+ 23,9 s de démarrage de
    session Spark) — verdict que Spark est très surdimensionné à cette
    volumétrie, mais que le chemin de montée en charge existe si le
    Copilote devait un jour couvrir tout le groupe Nexity.
  - Chiffres tous déjà vérifiés à l'étape 2 contre
    `nb_extracts/01_preparation_sql_spark.txt` et
    `chapitre_copilote_financier.txt` ; aucun nouveau chiffre non
    sourcé introduit.
- 18 slides → **19 slides**. L'ajout a fait grimper le texte à 3 620
  mots (25,9 à 27,9 minutes) : plusieurs phrases resserrées ailleurs
  (axe C, clôture de l'axe C, signaux faibles, migration, et la slide
  SQL elle-même) pour revenir près de la cible sans retirer de contenu
  demandé.
- Recompte final : 3 380 → **3 544 mots** → 25,3 à 27,3 minutes selon le
  débit. Ratio alternance/copilote 30,7 % / 69,3 % → **28,3 % / 71,7 %**
  (la nouvelle slide SQL fait partie du bloc Copilote Financier).
- `plan_slides.md` réécrit intégralement pour les 19 slides, avec
  l'entrée « Slide 10 — La base de données SQL » marquée comme ajout
  explicite. `.pptx` régénéré avec la nouvelle slide (bullets + 3
  cartes chiffrées : tables/vues, Cap d'Agde, pandas vs Spark) et toutes
  les slides suivantes renumérotées — validation structurelle PASS,
  19 slides confirmées via `markitdown`, aucun texte de substitution.

## État à la fin de la phase 1

- `discours_soutenance.md`, `plan_slides.md` et
  `soutenance_copilote_financier.pptx` sont à jour avec toutes les
  corrections des deux audits, les demandes de rééquilibrage 30/70,
  d'approfondissement (ACP, validation croisée, exploration des données),
  de réécriture du registre, de recalibrage à 25 minutes, de mise en
  récit chronologique du Copilote Financier, et d'ajout de la base de
  données SQL.
- État final : **19 slides, 3 544 mots utiles → 25,3 à 27,3 minutes**
  selon le débit (130-140 mots/minute) ; répartition ≈ 28,3 % missions
  d'alternance / ≈ 71,7 % Copilote Financier. Légèrement au-dessus de
  25 minutes à débit lent, pile dans la cible à débit normal-rapide.
- **Validation explicite reçue le 26/08/2026** : passage à la phase 2
  autorisé.

## Étape 14 — Phase 2 : questions du jury (`questions_jury.md`)

- Fichier créé avec **20 questions probables du jury**, classées en six
  blocs : méthodologie générale (6), axe A (4), axe B (3), axe C (3),
  typologie/exploration (3), infrastructure SQL (1).
- Couverture demandée respectée : méthodologie de l'axe A (choix du
  modèle retenu malgré un F1 inférieur au CART, seuil de dérive
  matérielle, Ridge vs Lasso), de l'axe B (effets aléatoires vs pooled
  OLS, contradiction panel/ARIMA, choix de l'ordre ARIMA), de l'axe C
  (Lagrange vs SLSQP, élasticité non significative retenue quand même,
  lecture de la remise en euros constants), plus la méthodologie
  générale du projet (validation croisée systématique, absence de deep
  learning, confidentialité, périmètre plateforme vs notebooks, régimes
  de preuve).
- Chaque réponse est rédigée pour l'oral (registre naturel, pas de
  jargon non expliqué) et suivie d'une ligne **Source :** pointant vers
  le document exact (chapitre détaillé, notebook et cellule, ou mémoire)
  où le chiffre ou l'argument cité est vérifiable — conformément à
  l'exigence de traçabilité posée dès le départ.
- Chiffres nouveaux introduits dans cette étape (absents des slides,
  mais nécessaires pour répondre en profondeur à une question de jury),
  tous vérifiés par grep direct dans les sources déjà extraites :
  - notebook 03 : F1 forêt aléatoire 0,306 ± 0,069, score OOB 0,691,
    « modèle retenu parmi les interprétables » (pas le F1 maximum
    absolu, qui est celui du CART à 0,340) ;
  - notebook 02 : silhouette maximale 0,47 et Davies-Bouldin minimal
    0,96 pour K = 4, indice de Rand ajusté K-moyennes/CAH-Ward = 0,862 ;
  - notebook 04 : coefficient pooled OLS -0,242 contre -0,216 pour le
    modèle à effets aléatoires ; ARIMA(1,1,1)×(1,0,1,12), AICc = 611,7,
    Ljung-Box p = 0,224 ; corrélation brute r = +0,07 puis r = -0,34 /
    +0,44 après correction par opération active ;
  - notebook 05 : écart Lagrange/SLSQP = 0,0056 ; élasticité interne
    ε = -0,81, IC 95 % [-3,62 ; 1,99], p = 0,57, retenue à -1 par
    référence à la littérature (Meen 2001, DiPasquale & Wheaton 1994) ;
  - chapitre détaillé : section « Périmètre et limites » (147 opérations
    en plateforme contre 267 en notebooks, à la demande du
    commanditaire).
- Aucune vérification par sous-agent effectuée à cette étape : les
  chiffres proviennent tous d'un grep direct et vérifié dans les
  fichiers sources déjà extraits en phase 1
  (`chapitre_copilote_financier.txt`, `nb_extracts/*.txt`), pas d'une
  nouvelle extraction. Une relecture par le sous-agent
  data-science-expert reste possible sur demande avant la soutenance
  finale.

## État à la fin de la phase 2

- `questions_jury.md` livré avec 20 questions/réponses sourcées.
  `discours_soutenance.md`, `plan_slides.md` et
  `soutenance_copilote_financier.pptx` restent dans l'état validé de la
  fin de phase 1 (19 slides, 3 544 mots, 25,3 à 27,3 minutes, ratio
  28,3 % / 71,7 %).
- **En attente de retour de l'étudiante sur les réponses proposées**
  avant la soutenance ; possibilité d'audit complémentaire par les deux
  sous-agents (fresh-context sur le discours, data-science-expert sur
  les chiffres) sur simple demande.
