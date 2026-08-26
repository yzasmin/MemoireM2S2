# Questions probables du jury — réponses préparées

19 questions, classées par thème : méthodologie générale, axe A, axe B,
axe C, typologie/exploration, infrastructure. Chaque réponse est écrite
pour être dite à l'oral (pas lue), et suivie d'une ligne **Source :** qui
pointe vers le document exact où le chiffre ou l'argument est vérifiable
— mémoire, chapitre détaillé, ou notebook. Rien ici n'est inventé pour
« boucher un trou » : si une question ouvre sur un point réellement non
traité par le projet, la réponse le dit franchement plutôt que d'improviser
un chiffre.

---

## Méthodologie générale

### 1. Pourquoi la validation croisée partout, et pas un simple découpage entraînement/test ?

Parce que l'échantillon est petit — 267 opérations au total, et seulement
123 exploitables pour l'axe A une fois les filtres de maturité appliqués.
Sur un échantillon pareil, un seul découpage entraînement/test dépend
beaucoup du hasard : selon les lignes qui tombent d'un côté ou de l'autre,
le score peut bouger fortement sans que le modèle ait vraiment changé. La
validation croisée à 5 plis, stratifiée pour respecter le déséquilibre des
classes, moyenne le résultat sur cinq découpages différents et donne un
score plus stable, avec son écart-type — c'est ce qui apparaît par exemple
pour la forêt aléatoire de l'axe A, F1 = 0,306 ± 0,069. Je m'en suis fixé
comme règle non négociable dès le cadrage du projet : je ne retiens un
résultat que s'il tient en validation croisée, jamais sur sa seule
performance d'ajustement.

**Source :** chapitre détaillé, exigences non fonctionnelles (« un petit
échantillon assumé : validation croisée systématique... ») ; notebook 03,
`StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`.

### 2. Pourquoi si peu de deep learning dans un projet de 2026 ?

Parce que le deep learning a besoin de volume pour donner quelque chose de
fiable, et je n'en avais pas. Je l'ai quand même testé, sur l'axe A, avec
un perceptron multicouche à 16 neurones : F1 de 0,91 sur l'entraînement,
mais 0,26 en validation croisée. C'est exactement la signature du
sur-apprentissage qu'on nous enseigne en théorie de la généralisation à
petit échantillon, et je l'ai obtenue en vrai, sur mes propres données.
Plutôt que de forcer une méthode inadaptée à la taille de l'échantillon,
j'ai choisi des modèles plus simples et régularisés — logistique, Ridge,
forêt aléatoire — qui généralisent mieux quand on a peu de lignes. Le MLP
reste dans le mémoire comme démonstration pédagogique du phénomène, pas
comme candidat sérieux pour la plateforme.

**Source :** chapitre détaillé, notebook 03 (comparaison des six
méthodes, écart train/CV du MLP) ; exigences non fonctionnelles du
projet (« pas de deep learning au-delà d'une démonstration
pédagogique »).

### 3. Comment gérez-vous la confidentialité des données clients dans ce projet ?

C'est une contrainte que je me suis fixée dès le départ, avant même de
commencer à modéliser : aucune donnée nominative — nom, date de
naissance — n'est affichée ni utilisée comme variable dans un modèle,
que ce soit dans les notebooks ou sur la plateforme. Ce qui entre dans
les modèles, ce sont des variables agrégées ou dérivées — un montant, un
délai, une catégorie de motif — jamais un identifiant direct de personne.
C'est particulièrement vrai pour la reprise des tiers, où je manipule
des milliers de coordonnées d'acquéreurs : le travail de dédoublonnage
se fait sur des clés calculées, pas sur l'affichage brut des données
personnelles.

**Source :** chapitre détaillé, exigences non fonctionnelles du projet
(« confidentialité : aucune donnée nominative de client... n'est
affichée ni utilisée comme variable »).

### 4. Vous dites que vous avez été « traductrice avant modélisatrice ». Concrètement, ça veut dire quoi ?

Ça veut dire que la partie la plus difficile n'était pas d'appliquer une
méthode statistique, c'était de transformer une gêne métier, souvent
formulée de façon assez floue — « on n'arrive pas à voir venir les
dérapages », « on ne sait pas à quel rythme le stock va se vendre » — en
une question qu'on peut vraiment calculer : quelle variable cible,
quelle définition d'un dérapage, sur quel périmètre d'opérations. Et
ensuite, dans l'autre sens : traduire un résultat statistique, un F1 de
0,30 par exemple, en quelque chose qu'un directeur financier peut
utiliser pour décider. C'est ce qui m'a poussée à reconstruire la
plateforme en langage métier après le retour du commanditaire, qui
trouvait la première version — pleine de F1 et de R² — trop technique
pour ses équipes.

**Source :** chapitre détaillé, section plateforme (retour du
commanditaire sur le vocabulaire statistique) ; discours de soutenance,
slide 16 et 17.

### 5. Pourquoi la plateforme ne couvre-t-elle que 147 opérations quand les notebooks en analysent 267 ?

C'est un choix assumé, pas un oubli. Les notebooks travaillent sur les
267 opérations, promotion et aménagement foncier confondus, parce que
c'est le périmètre complet et que la typologie du notebook 02, par
exemple, a justement besoin des deux métiers pour faire apparaître ses
quatre familles. Mais la plateforme, elle, se limite aux 147 opérations
de promotion, à la demande directe du commanditaire, pour que l'outil
reste lisible pour ses utilisateurs sur leur usage métier principal.
L'aménagement foncier est donc modélisé et analysé dans le mémoire, mais
pas encore piloté à l'écran — c'est un prolongement naturel que je cite
dans mes perspectives.

**Source :** chapitre détaillé, section « Périmètre et limites »
(« le périmètre de la plateforme... est volontairement plus étroit que
celui des notebooks »).

### 6. Vous parlez de trois régimes de preuve différents. Pouvez-vous détailler ?

Oui. J'ai identifié, en prenant du recul sur mon année, trois façons
différentes de prouver qu'un livrable est correct, et l'erreur
méthodologique serait de les confondre. Une reprise de données — comme
la migration des opérations ou la reprise des tiers — se prouve par
réconciliation : est-ce que la donnée est bien arrivée, au bon endroit,
sans doublon ni perte ? Un tableau de bord ou un outil comme le SSO se
prouve par l'usage : est-ce que la personne s'en sert vraiment, et pour
la bonne chose ? Et un modèle statistique se prouve par la validation :
est-ce que le résultat tient en dehors de l'échantillon qui a servi à
le construire, en validation croisée. Le point important, c'est que ces
trois régimes ont chacun un angle mort différent : une réconciliation
prouve que la donnée est arrivée, pas qu'elle est juste ; un modèle
validé peut très bien ne jamais être utilisé si personne ne s'en sert.

**Source :** mémoire, chapitre de réflexion transversale (section sur
les régimes de preuve) ; discours de soutenance, slide 17.

---

## Axe A — le risque de marge

### 7. Vous retenez la forêt aléatoire avec un F1 de 0,306, alors que l'arbre CART fait mieux, 0,340. Pourquoi ne pas garder le meilleur score ?

Bonne remarque, et c'est un choix que j'ai fait consciemment. Le modèle
final n'a pas été choisi en prenant simplement le F1 maximum toutes
méthodes confondues : je l'ai choisi parmi les modèles interprétables,
la régression logistique et la forêt aléatoire, parce que sur la
plateforme, ce qui compte autant que le score, c'est de pouvoir
expliquer pourquoi une opération est signalée à risque. Un arbre CART
unique, même avec sa profondeur choisie en validation croisée, reste
une seule partition assez instable — sa frontière de décision peut
changer beaucoup si on change légèrement l'échantillon d'apprentissage.
La forêt aléatoire agrège 500 arbres et donne un score out-of-bag de
0,691, plus une mesure d'importance des variables directement
exploitable pour l'explication. Le CART reste dans le mémoire comme
point de comparaison, mais je ne l'ai pas retenu pour la plateforme.

**Source :** notebook 03, cellule 29 (« Modèle retenu pour la
plateforme : le meilleur F1 en CV parmi les modèles interprétables »,
score OOB = 0,691) ; chapitre détaillé, tableau comparatif des six
méthodes.

### 8. Un F1 entre 0,26 et 0,34, c'est vraiment utilisable en pratique par la direction financière ?

Je suis directe là-dessus : ce n'est pas un oracle, c'est un signal réel
mais faible. Je le dis explicitement dans le mémoire plutôt que de le
maquiller. Ce qui rend le résultat utilisable quand même, c'est qu'il
bat largement une référence naïve — 0 pour un modèle qui prédirait
toujours « opération saine » — et qu'il est accompagné, sur la
plateforme, du modèle Ridge explicatif : la personne qui consulte
l'alerte voit aussi les facteurs qui la justifient, le poids des postes
techniques ou une marge budgétée confortable qui protège. C'est pensé
comme un signal d'alerte à recouper avec le jugement métier, pas comme
une prédiction à suivre les yeux fermés. Sur 68 opérations suffisamment
avancées, la page Alertes marge en signale 10.

**Source :** chapitre détaillé, section axe A (comparaison des six
méthodes, F1 = 0 pour la baseline) ; discours de soutenance, slide 12 et
16 (page Alertes marge).

### 9. Comment avez-vous choisi le seuil de -2 % pour définir une opération « à risque » ?

Ce seuil définit ce que j'appelle la dérive matérielle : une opération
est classée « à risque » si sa variation de marge dépasse -2 % par
rapport au budget engagé. C'est un choix de seuil métier plutôt qu'un
optimum statistique trouvé automatiquement — il correspond à l'ordre de
grandeur d'un dépassement jugé significatif par la direction financière,
en dessous duquel on considère que l'écart relève de l'aléa normal de
chantier. Sur les 123 opérations suffisamment avancées pour être
apprises, ce seuil classe 28 % d'entre elles comme en dérive matérielle,
ce qui donne un déséquilibre de classes suffisant pour justifier
l'usage du F1 plutôt que la simple exactitude comme métrique.

**Source :** chapitre détaillé, section axe A (« à risque si la dérive
dépasse -2 % de la marge budgétée ») ; notebook 03.

### 10. Pourquoi la régularisation Ridge plutôt que Lasso pour la régression ?

J'ai en fait testé les deux, avec le paramètre de régularisation choisi
par validation croisée à cinq plis dans les deux cas, et aucun des deux
n'améliore le R² de test par rapport à l'OLS simple — ce qui n'est pas
surprenant puisque la moitié de l'échantillon est à variation nulle,
donc il n'y a pas grand-chose à régulariser côté prédiction pure.
L'intérêt du Ridge, dans mon cas, n'est pas là : c'est qu'il rend
lisibles, sur des variables standardisées donc comparables entre elles,
les facteurs structurels de la dérive. Le Lasso aurait pu mettre
certains coefficients strictement à zéro, ce qui est utile pour
sélectionner des variables, mais ici je voulais garder tous les postes
budgétaires visibles dans l'explication plutôt que d'en éliminer
certains — d'où le choix du Ridge pour la version explicative retenue.

**Source :** chapitre détaillé, section axe A (« la régularisation
Ridge... et Lasso n'améliorent pas ce chiffre »).

---

## Axe B — la vitesse d'écoulement

### 11. Pourquoi un modèle à effets aléatoires plutôt qu'une régression simple (pooled OLS) sur le panel ?

Parce qu'ignorer la structure du panel, c'est-à-dire le fait que chaque
opération apparaît plusieurs fois dans les données, un mois après
l'autre, fausse l'estimation de l'effet qui m'intéressait. Le modèle
pooled OLS, qui traite chaque ligne comme indépendante, surestime
l'effet du taux de crédit : -0,242 contre -0,216 avec le modèle à effets
aléatoires. La raison, c'est qu'il confond deux choses : l'effet
conjoncturel du taux, et l'effet de composition du portefeuille dans le
temps — le fait que certaines opérations, avec leurs propres
caractéristiques, entrent et sortent du portefeuille au fil du temps. Le
modèle à effets aléatoires sépare ce qui revient à l'opération
elle-même de ce qui revient à la conjoncture, avec un coefficient de
corrélation intraclasse de 0,66 : deux tiers de la variance du rythme de
vente tiennent au programme, un tiers à la conjoncture.

**Source :** chapitre détaillé, section axe B (« le modèle pooled OLS...
surestime cet effet »), formalisme de Laird-Ware, notebook 04.

### 12. Le modèle en panel trouve un effet du taux très significatif, mais l'ARIMA sur la série agrégée dit le contraire. Lequel croire ?

Les deux, en fait, parce qu'ils ne répondent pas exactement à la même
question, et je les ai combinés plutôt que de choisir l'un contre
l'autre. Le panel a l'avantage du volume — plus de 3 200 observations —
et identifie très proprement l'effet du taux, très significatif
statistiquement. Mais quand je regarde la série agrégée du groupe dans
le temps, avec un modèle ARIMA plus exigeant sur la dynamique
temporelle, l'effet du taux devient indiscernable de zéro sur cent
quatorze mois. Ce n'est pas une contradiction qui invalide le premier
résultat, c'est plutôt rassurant : ça écarte le risque que l'effet trouvé
dans le panel vienne d'une corrélation fallacieuse, un lien qui
semblerait réel sans en être un — la mise en garde classique contre la
spurious regression en séries temporelles. J'ai donc combiné les deux :
la trajectoire de référence vient de l'ARIMA, et l'ampleur de l'effet du
taux vient du panel, plus solidement identifié sur ce point précis.

**Source :** chapitre détaillé, section axe B (« Cent quatorze points
mensuels ne suffisent pas à séparer l'effet du taux... spurious
regression ») ; notebook 04.

### 13. Comment avez-vous choisi l'ordre du modèle ARIMA ?

En suivant une procédure standard plutôt qu'en le fixant à l'œil : je
spécifie d'abord l'ARIMA des erreurs, je vérifie que les résidus
ressemblent à un bruit blanc avec un test de Ljung-Box, et parmi les
modèles dont les résidus passent ce test, je retiens celui qui minimise
l'AICc, un critère qui pénalise la complexité excessive. Le modèle
retenu est un ARIMA saisonnier d'ordre (1,1,1) sur la partie non
saisonnière et (1,0,1,12) sur la partie saisonnière, avec un AICc de
611,7 et un test de Ljung-Box qui ne rejette pas l'hypothèse de bruit
blanc des résidus, p = 0,224.

**Source :** chapitre détaillé, section axe B (« ARIMA(1,1,1)×(1,0,1,12)
saisonnier, AICc = 611,7, Ljung-Box p = 0,224 »).

---

## Axe C — l'optimisation des prix

### 14. Pourquoi résoudre le problème d'optimisation avec un multiplicateur de Lagrange plutôt qu'un solveur générique directement ?

J'ai en fait fait les deux, volontairement, pour me vérifier moi-même.
Le multiplicateur de Lagrange donne une solution en forme fermée : il
traduit la contrainte de volume de ventes visé en un prix fictif, le
multiplicateur, à partir duquel on calcule directement la remise
optimale sur chaque lot. C'est élégant et ça donne une lecture
économique claire. Mais pour être sûre que je n'avais pas fait d'erreur
de calcul ou une simplification abusive, j'ai recalculé la même solution
avec un solveur numérique générique, SLSQP, sur le problème complet.
L'écart maximal entre les deux méthodes est de 0,0056, ce qui confirme
que la solution analytique est correcte.

**Source :** notebook 05, section « Vérification : SLSQP sur le problème
complet » (« Écart max |δ_gradient − δ_SLSQP| = 0,0056 »).

### 15. Votre estimation interne de l'élasticité prix-demande n'est pas significative (p = 0,57). Pourquoi utiliser une élasticité de -1 quand même ?

Parce que j'ai fait un choix documenté plutôt que d'improviser un
chiffre pour combler le trou. Mon estimation interne, sur 95 opérations,
donne une élasticité de -0,81, avec le bon signe mais un intervalle de
confiance très large et une p-value de 0,57 : ce n'est statistiquement
pas fiable, 95 opérations ne suffisent pas pour l'identifier
proprement. Plutôt que de présenter ce -0,81 comme un chiffre solide, je
le dis franchement et je retiens -1 à la place : une valeur compatible
avec mon estimation ponctuelle, et cohérente avec la littérature sur la
demande de logements neufs, où les élasticités-prix usuelles se situent
entre -1 et -2. C'est un choix prudent, plutôt bas dans cette
fourchette, et je le documente comme tel plutôt que de le présenter
comme un résultat empirique de mon travail.

**Source :** notebook 05, cellule 11-12 (« n = 95 opérations ; ε estimé
= -0.81... p = 0.57 »), référence à Meen (2001) et DiPasquale & Wheaton
(1994).

### 16. Pourquoi la remise optimale est-elle un montant identique en euros, et pas un pourcentage identique, sur tous les lots ?

C'est exactement le résultat mathématique de l'optimisation sous
contrainte avec cette forme de demande, et c'est ce qui m'a surprise en
le voyant sortir. La condition d'optimalité, une fois qu'on résout le
système avec le multiplicateur de Lagrange, se simplifie en une égalité
entre le prix du lot fois un facteur lié à l'élasticité, et le
multiplicateur — ce qui, pour l'élasticité retenue de -1, revient à dire
que la remise en euros est la même pour tous les lots. Mécaniquement, un
montant identique en euros représente un pourcentage plus fort sur un
petit lot que sur un grand. C'est l'inverse de ce qui se pratique
aujourd'hui, où les remises sont décidées au cas par cas. Sur
l'opération test Arpeggio, viser 8 % d'accélération des ventes donne un
montant constant d'environ 23 000 euros, soit des ajustements
individuels allant de -5 % à -14 % selon le prix du lot.

**Source :** notebook 05, section 4a (« condition p_j δ_j = λ (ε = −1) »)
et section démonstration Arpeggio ; chapitre détaillé, section axe C.

---

## Typologie et exploration des données

### 17. Pourquoi construire une typologie par ACP et classification plutôt que de travailler directement sur les données brutes des opérations ?

Parce que comparer deux opérations sur leurs montants bruts n'a pas de
sens : une opération de 2 millions d'euros et une de 50 millions ne sont
pas comparables en valeur absolue, c'est la structure de leur budget qui
dit ce qu'elles sont vraiment. J'ai donc construit une matrice de
profils de coûts — la part de chaque poste de dépense dans le budget
total, standardisée — puis appliqué une ACP pour résumer cette
structure : deux composantes en résument 61 % de la variance, vérifié
par une seconde méthode de calcul indépendante, la SVD, qui confirme la
décomposition à 1,8 fois 10 puissance -15 près, donc quasiment
parfaitement. Cette typologie sert ensuite de comparateur direct dans
l'axe A : situer une opération à risque parmi ses semblables plutôt que
parmi l'ensemble du portefeuille.

**Source :** chapitre détaillé, section typologie (« une ACP écrite à la
main... la vérification par SVD confirme cette décomposition à
1,8 × 10⁻¹⁵ près ») ; notebook 02.

### 18. Comment avez-vous choisi le nombre de familles, quatre, dans la classification non supervisée ?

Pas au hasard, et pas seulement à l'œil sur le dendrogramme. J'ai comparé
plusieurs valeurs de K avec trois critères convergents : le critère du
coude sur l'inertie intra-classe, le coefficient de silhouette, maximal
à 0,47 pour K = 4, et l'indice de Davies-Bouldin, minimal à 0,96
toujours pour K = 4. Les trois critères pointent vers la même valeur.
Et pour vérifier que ce résultat n'est pas un artefact de la méthode des
k-moyennes en particulier, je l'ai comparé à une classification
hiérarchique par distance de Ward, une méthode complètement différente
dans sa logique : l'indice de Rand ajusté entre les deux partitions est
de 0,862, ce qui traduit un accord fort entre deux méthodes
indépendantes sur les mêmes quatre familles.

**Source :** notebook 02, section « Choisir K : coude, silhouette,
Davies-Bouldin » (silhouette maximale 0,47, Davies-Bouldin minimal 0,96)
et section CAH-Ward (« Indice de Rand ajusté K-moyennes / CAH : 0,862 »).

### 19. Vous dites avoir découvert une « fausse piste » pendant l'exploration des données, sur la corrélation entre réservations et taux de crédit. Comment l'avez-vous détectée, et pas juste acceptée ?

En vérifiant vraiment la sortie de mon code plutôt qu'en me fiant à ce
que j'attendais d'y trouver. J'avais initialement une intuition, presque
rédigé la conclusion attendue : le lien entre taux de crédit et
réservations devait être négatif et net, puisque c'est un lien
économique connu sur ce marché. Mais la corrélation de Pearson brute sur
les réservations mensuelles du groupe donnait r = +0,07, quasiment nulle,
et positive en plus. En creusant, j'ai compris que le nombre
d'opérations commercialisées avait doublé sur la période observée : ça
gonflait mécaniquement le volume de réservations, même quand la demande
par programme individuel s'effondrait, et ça maquillait complètement la
relation macroéconomique. C'est exactement le type de piège que le cours
de séries temporelles appelle la spurious regression. Une fois
l'intensité de vente calculée par opération active plutôt qu'en volume
brut, la corrélation redevient nette : r = -0,34 avec le taux de crédit,
r = +0,44 avec la confiance des ménages. Cette correction a directement
structuré toute la démarche de l'axe B, qui travaille sur l'intensité et
non sur le volume brut.

**Source :** chapitre détaillé, section analyse bivariée temporelle
(« la corrélation de Pearson brute... r = +0,07... En neutralisant
l'effet de portefeuille... r = -0,34... r = +0,44 »).

---

## Infrastructure

### 20. Pourquoi avoir construit une base SQL plutôt que de travailler directement sur les fichiers Excel avec pandas ?

Parce que les quatre exports Excel, tels quels, n'étaient pas
interrogeables facilement, et parce que plusieurs indicateurs — la
marge par opération, les réservations par mois, l'état du stock — sont
utilisés à la fois par plusieurs notebooks et par la plateforme. Sans
base commune, j'aurais dû recalculer ces indicateurs à chaque fois,
avec le risque réel qu'une définition dérive d'un endroit à l'autre. En
les encapsulant dans des vues SQL, écrites une seule fois, je garantis
que les notebooks et la plateforme utilisent exactement la même
définition. J'en ai aussi profité pour tester la montée en charge avec
Spark : sur le volume actuel, pandas répond en 9,9 millisecondes contre
577,4 pour Spark, plus 23,9 secondes de démarrage de session — Spark est
largement surdimensionné ici, mais l'exercice prouve que le chemin de
montée en charge existe si le Copilote devait un jour couvrir tout le
groupe Nexity, pas seulement Angelotti.

**Source :** notebook 01 (chronométrage pandas vs Spark) ; chapitre
détaillé, section architecture technique (7 tables + 3 vues SQL).
