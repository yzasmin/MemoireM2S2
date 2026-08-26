# Explications complémentaires

Sept points que tu as demandé à revoir, expliqués simplement mais avec
assez de détail pour que tu puisses reformuler avec tes propres mots
devant le jury. Les sections « Axe B » et « Axe C » sont pensées comme un
mini script de présentation : tu peux les relire juste avant la
soutenance pour reconstruire le fil du raisonnement, pas juste retenir
des chiffres isolés.

---

## 1. Le référentiel des communes du portefeuille : qu'est-ce qu'il y a dedans ?

C'est un petit tableau de 90 lignes, une ligne par commune où le groupe a
au moins une opération. Pour chaque commune, il contient :

- **la population** de la commune,
- **le département**,
- **les coordonnées géographiques** (latitude/longitude),
- **une distance au littoral**, que tu as calculée toi-même à partir de
  ces coordonnées, via un service public en ligne (geo.api.gouv.fr).

Ce tableau ne vient pas du système de gestion interne d'Angelotti : c'est
une donnée externe que tu es allée chercher toi-même, comme le taux des
crédits (BCE) ou la confiance des ménages (Eurostat). Elle sert de table
de référence : chaque opération est reliée à sa commune (par un nom de
commune normalisé — 91 orthographes différentes ramenées à 90 communes
uniques, parce que « LATOUR BAS ELNE » et « LATOUR-BAS-ELNE » désignaient
la même ville dans les exports), et par cette relation, l'opération
« hérite » des informations de sa commune.

**À quoi ça sert concrètement ?** Dans l'axe C (les prix), tu construis un
modèle qui explique le prix d'un logement par ses caractéristiques. Le
fait qu'un lot soit proche de la mer ou non (l'« indicateur littoral »,
calculé à partir de la distance au littoral de sa commune) est une de ces
caractéristiques : un appartement à 500 mètres de la plage ne se vend pas
au même prix qu'un appartement à 40 kilomètres, même avec la même
surface. Sans ce référentiel de communes, tu n'aurais pas pu construire
cette variable.

**Comment le présenter simplement au jury si on te pose la question :**
« J'ai enrichi mes données internes avec un référentiel externe des 90
communes du portefeuille — population, localisation, et une distance au
littoral que j'ai calculée moi-même — pour pouvoir intégrer la proximité
de la mer comme variable dans mon modèle de prix. »

---

## 2. Que veut dire « rapporté au nombre d'opérations actives » ?

C'est l'idée centrale de la deuxième leçon de l'exploration des données,
et elle mérite d'être bien comprise parce qu'elle structure tout l'axe B.

**Le problème de départ.** Tu regardes, mois par mois, le nombre total de
réservations faites sur l'ensemble du portefeuille. Ce nombre dépend de
deux choses en même temps : est-ce que la demande est forte ce mois-là
(ce qui t'intéresse), et combien d'opérations sont en cours de
commercialisation ce mois-là (ce qui n'a rien à voir avec la demande).
Le nombre d'opérations en vente a doublé entre le début et la fin de la
période étudiée. Donc même si la demande par programme s'effondre, le
total de réservations peut rester stable ou même augmenter, simplement
parce qu'il y a deux fois plus d'opérations qui vendent en même temps.
Regarder le total brut, c'est comme comparer le chiffre d'affaires total
d'une chaîne de magasins d'une année sur l'autre sans tenir compte du
fait qu'elle a ouvert deux fois plus de magasins entre-temps : le total
peut monter alors que chaque magasin, individuellement, vend moins.

**La correction.** Pour chaque mois, tu comptes combien d'opérations
étaient « actives » — c'est-à-dire en cours de commercialisation, entre
leur première et leur dernière vente enregistrée. Puis tu calcules :

```
intensité de vente du mois = (total des réservations ce mois) / (nombre d'opérations actives ce mois)
```

C'est une moyenne : combien de réservations, en moyenne, une opération
fait ce mois-là. Ça neutralise l'effet du nombre d'opérations, et ça
permet de comparer des mois entre eux sur une base équitable, qu'il y ait
10 ou 25 opérations en vente.

**Le résultat, avec les chiffres.** Sur le volume brut, la corrélation
entre réservations et taux de crédit était de +0,07 (quasiment nulle,
et même du mauvais signe). Une fois passé à l'intensité (réservations par
opération active), la corrélation devient -0,34 avec le taux de crédit,
et +0,44 avec la confiance des ménages — des liens nets, dans le sens
attendu économiquement.

**Comment le présenter simplement au jury :**
« Le total brut de réservations était pollué par la croissance du
portefeuille : plus d'opérations en vente en fin de période, donc plus
de réservations, même si chaque opération individuellement vendait
moins. En divisant le nombre de réservations du mois par le nombre
d'opérations actives ce mois-là, j'obtiens une intensité de vente par
opération, comparable d'un mois à l'autre — et c'est là que le lien
avec le taux de crédit apparaît vraiment. »

---

## 3. Le dendrogramme de la classification des opérations

**Rappel du contexte.** Après l'ACP (qui résume la structure des coûts
en deux axes), tu regroupes les opérations en familles similaires par
deux méthodes différentes : les k-moyennes (vue dans l'explication
précédente) et une classification ascendante hiérarchique (CAH), dont le
résultat se visualise par un dendrogramme.

**Comment lire un dendrogramme, en général.** C'est un arbre à l'envers.
En bas, chaque feuille est une opération individuelle. L'algorithme
commence par considérer que chaque opération est son propre groupe, puis
il fusionne, étape par étape, les deux groupes les plus proches l'un de
l'autre — un peu comme un tournoi où on rapproche à chaque tour les deux
équipes les plus semblables. Chaque fusion est représentée par une
branche horizontale, et la **hauteur** à laquelle deux branches se
rejoignent indique à quel point les deux groupes fusionnés étaient
différents : plus la fusion se fait haut, plus les deux groupes étaient
éloignés l'un de l'autre. En remontant tout en haut, tout finit par
fusionner en un seul groupe géant — ce qui n'a pas d'intérêt en soi, mais
permet de choisir où « couper » l'arbre pour décider du nombre de
groupes qu'on veut garder.

**La distance utilisée : Ward.** Il existe plusieurs façons de mesurer
la « distance » entre deux groupes pendant la construction de l'arbre.
Tu utilises la distance de Ward, qui a une propriété élégante : à chaque
fusion, elle choisit les deux groupes qui, une fois réunis, font perdre
le moins possible d'homogénéité interne à l'ensemble. C'est cohérent
avec l'objectif des k-moyennes (minimiser la dispersion à l'intérieur de
chaque groupe), ce qui rend les deux méthodes comparables.

**Ce que montre ton dendrogramme précisément.** Sur tes 223 opérations,
la toute première scission — tout en haut de l'arbre, donc la plus
importante — sépare déjà la promotion immobilière de l'aménagement
foncier : c'est la même opposition que celle que révélait le premier axe
de l'ACP. Ensuite, chaque branche se subdivise à nouveau, jusqu'à ce que
tu coupes l'arbre à une hauteur choisie pour obtenir exactement 4
groupes.

**La vérification de robustesse.** Tu compares ensuite ces 4 groupes
avec ceux obtenus par les k-moyennes (une méthode complètement
différente : elle ne construit pas d'arbre, elle réaffecte directement
chaque opération au groupe le plus proche, plusieurs fois de suite). Le
tableau croisé montre que les deux méthodes s'accordent fortement — par
exemple, 114 des 116 opérations du groupe « aménagement foncier » selon
les k-moyennes tombent dans le même groupe CAH — avec un indice de Rand
ajusté de 0,862. Les rares désaccords concernent des opérations
« frontières », entre deux familles, que la CAH, qui ne peut jamais
revenir sur une fusion déjà faite, classe parfois différemment des
k-moyennes.

**Comment le présenter simplement au jury :**
« Le dendrogramme construit les groupes par fusions successives, des
opérations individuelles vers des familles de plus en plus larges. La
toute première séparation, la plus significative, oppose déjà promotion
et aménagement foncier — cohérent avec ce que montrait l'ACP. En coupant
l'arbre à 4 groupes et en comparant avec une méthode complètement
différente, les k-moyennes, j'obtiens un accord de 0,862 sur l'indice de
Rand ajusté : la typologie ne dépend pas de la méthode choisie, elle est
stable. »

---

## 4. Tous les modèles de l'axe A, un par un

L'axe A a deux volets : d'abord une régression (prédire l'ampleur de la
dérive), puis une classification (prédire si l'opération est « à
risque » ou non). Voici chaque modèle utilisé, dans l'ordre où tu les
présentes.

### Volet régression

**OLS (moindres carrés ordinaires).** C'est la régression la plus
classique : on cherche la droite (ou l'hyperplan, avec plusieurs
variables) qui minimise la somme des écarts au carré entre les valeurs
prédites et les valeurs réelles. Tu l'as d'abord résolue par une formule
mathématique directe (forme close), puis retrouvée avec un algorithme
itératif que tu as codé toi-même, la descente de gradient (voir plus
bas), pour vérifier que les deux donnent le même résultat. Résultat :
R² de test = 0,077, ce qui veut dire que la structure budgétaire de
départ n'explique que 7,7 % de la variation de la dérive observée d'une
opération à l'autre — un chiffre faible, qui montre que prédire
l'ampleur exacte de la dérive avec ces seules variables est difficile.

**Descente de gradient.** Ce n'est pas un modèle différent, c'est une
autre façon de résoudre le même problème que l'OLS : au lieu d'utiliser
la formule mathématique directe, on part d'une solution au hasard et on
l'améliore petit à petit, en se déplaçant dans la direction qui réduit le
plus l'erreur (comme descendre une pente en suivant la direction la plus
raide). Tu as vérifié qu'après 400 étapes, ton résultat codé à la main
est très proche (à 0,145 près) de la solution exacte obtenue par la
formule — une preuve que ton algorithme fonctionne correctement.

**Ridge.** Une version de l'OLS qui ajoute une pénalité sur la taille des
coefficients, pour éviter qu'un coefficient devienne démesurément grand à
cause du bruit dans les données. Le paramètre de pénalité est choisi par
validation croisée. Le R² ne s'améliore pas par rapport à l'OLS simple
(logique, puisque la moitié de l'échantillon a une variation nulle, donc
il n'y a pas grand-chose à « stabiliser »), mais l'intérêt est ailleurs :
en travaillant sur des variables standardisées (ramenées à une échelle
comparable), les coefficients du Ridge deviennent directement lisibles
comme des facteurs explicatifs — le poids des postes techniques
(foncier, VRD, construction), et l'effet protecteur d'une marge budgétée
confortable.

**Lasso.** Le même principe que Ridge, mais avec une pénalité qui peut
mettre certains coefficients strictement à zéro, ce qui revient à
éliminer certaines variables. Testé pour comparaison, il n'améliore pas
non plus le R², et tu as préféré garder le Ridge parce qu'il conserve
toutes les variables visibles dans l'explication.

### Volet classification

**Régression logistique.** Le modèle de classification le plus simple :
elle prédit une probabilité (entre 0 et 1) qu'une opération soit « à
risque », à partir d'une combinaison linéaire des variables, transformée
par une fonction en forme de S (la sigmoïde) qui ramène le résultat entre
0 et 1. Elle est dite « équilibrée » (class_weight balanced) parce que
tu as ajusté son fonctionnement pour compenser le fait qu'il y a
beaucoup moins d'opérations à risque que d'opérations saines dans tes
données — sinon, le modèle aurait tendance à toujours prédire « saine »,
la classe majoritaire, pour maximiser son score brut. F1 en validation
croisée : 0,283.

**SVM linéaire (machine à vecteurs de support).** Une autre façon de
tracer une frontière entre les deux classes, qui cherche à maximiser la
« marge » — la distance entre la frontière et les points les plus
proches de chaque classe, pour être la plus robuste possible face à de
nouvelles données. F1 : 0,303, très proche de la régression logistique.

**SVM à noyau RBF.** La même idée que le SVM linéaire, mais avec une
frontière qui peut être courbe plutôt que droite, pour capturer des
relations plus complexes entre les variables. F1 : 0,257, légèrement en
dessous du SVM linéaire — un signe que la relation entre les variables et
le risque est plutôt simple (linéaire), pas besoin d'une frontière
compliquée.

**Arbre de décision (CART).** Il découpe l'espace des variables par une
suite de questions oui/non successives (par exemple : « la marge
budgétée est-elle inférieure à X ? », puis « le poste foncier dépasse-t-il
Y % ? »), jusqu'à obtenir des petits groupes homogènes. Sa profondeur (le
nombre de questions posées avant de s'arrêter) est choisie par
validation croisée, pour éviter qu'il pose trop de questions et
sur-apprenne le bruit. F1 : 0,340, le meilleur score de la comparaison —
mais un arbre seul reste instable (voir l'explication détaillée dans
`explications_questions_jury.md`, question 7).

**Forêt aléatoire.** Elle construit 500 arbres de décision différents
(chacun entraîné sur un tirage aléatoire des opérations et des
variables), puis fait voter tous ces arbres pour donner la décision
finale. F1 : 0,306 ± 0,069, avec un score « out-of-bag » de 0,691 (une
façon de tester chaque arbre sur les données qu'il n'a pas vues, propre
aux forêts). C'est ce modèle-là que tu retiens pour la plateforme, avec
le Ridge comme complément explicatif.

**MLP (perceptron multicouche, un petit réseau de neurones).** Un modèle
avec 16 neurones organisés en une couche cachée, capable d'apprendre des
relations beaucoup plus complexes que les modèles précédents — mais qui a
besoin de beaucoup de données pour le faire correctement. F1 sur
l'entraînement : 0,913 ; F1 en validation croisée : 0,262. L'écart énorme
entre les deux est la preuve du sur-apprentissage : le modèle a appris
par cœur les particularités de ses données d'entraînement plutôt que la
vraie tendance.

**Baseline (référence naïve).** Un modèle qui prédit toujours « saine »,
quelle que soit l'opération. F1 = 0 (puisqu'il ne détecte jamais aucun
cas à risque). Sert de point de comparaison minimal : n'importe quel
modèle utile doit faire mieux que ça.

---

## 5. Axe B — la vitesse d'écoulement, en clair pour la présentation

**Le problème métier.** La direction financière veut savoir à quel
rythme le stock de logements va se vendre — c'est important pour
anticiper la trésorerie et pour ajuster la stratégie commerciale.

**Étape 1 : l'exploration révèle un piège.** Tu regardes d'abord si les
réservations mensuelles du groupe sont liées au taux des crédits
immobiliers. La corrélation brute est quasiment nulle (+0,07). Mais tu
comprends que ce n'est pas parce qu'il n'y a pas de lien : c'est parce
que le nombre d'opérations en vente a doublé sur la période, ce qui
gonfle le volume total même quand chaque programme vend moins. Une fois
corrigé (réservations divisées par le nombre d'opérations actives, voir
l'explication du point 2 ci-dessus), le lien apparaît clairement :
-0,34 avec le taux de crédit, +0,44 avec la confiance des ménages. Cette
découverte est le point de départ de toute la méthode de l'axe B :
travailler sur des données bien construites, pas sur le volume brut.

**Étape 2 : le modèle à effets aléatoires (l'outil principal).** Tu
construis un panel — un tableau avec une ligne par opération et par
mois, plus de 3 200 lignes au total — et tu utilises un modèle à effets
aléatoires. L'idée : chaque opération a sa propre « personnalité de
vente » (son emplacement, son produit, son prix la rendent plus ou moins
attractive dans l'absolu), qui reste plus ou moins stable dans le temps ;
et en plus de ça, il y a des variations d'un mois à l'autre liées à la
conjoncture économique (le taux de crédit, la confiance des ménages). Le
modèle sépare mathématiquement ces deux sources de variation. Résultat
principal : le coefficient de corrélation intraclasse est de 0,66,
c'est-à-dire que deux tiers de la variance du rythme de vente
s'expliquent par le programme lui-même, et un tiers par la conjoncture.
Et l'effet du taux de crédit est très net : chaque point de taux en plus
fait baisser les réservations mensuelles d'environ 19 %, un résultat
statistiquement très solide. Pourquoi ce modèle plutôt qu'une régression
simple ? Parce qu'une régression simple, qui traite chaque ligne comme
indépendante, confond l'effet du taux avec l'effet du changement de
composition du portefeuille au fil du temps, et surestime l'effet du
taux (-0,242 au lieu de -0,216).

**Étape 3 : vérifier autrement, avec un modèle de série temporelle.** Tu
ne t'arrêtes pas là : tu veux vérifier si cet effet du taux se retrouve
aussi en regardant l'évolution du groupe dans le temps, sur une seule
série agrégée (114 mois). Tu ajustes un modèle ARIMA (voir
`explications_questions_jury.md`, question 13, pour le détail de la
méthode de choix). Résultat surprenant : sur cette série agrégée, l'effet
du taux devient statistiquement indiscernable de zéro. Ce n'est pas une
contradiction qui remet en cause le résultat précédent : c'est que 114
points mensuels, sur une seule série, ne suffisent pas à isoler un effet
aussi lent que celui du taux d'intérêt. C'est même plutôt rassurant, car
ça écarte l'hypothèse que ton résultat du panel serait une coïncidence
statistique plutôt qu'un vrai effet.

**Étape 4 : combiner les deux résultats en scénarios utiles.** Tu
utilises alors les deux modèles ensemble, chacun pour ce qu'il fait le
mieux : l'ARIMA donne la trajectoire réaliste dans le temps (avec la
saisonnalité), et le panel donne l'ampleur précise de l'effet du taux.
Concrètement, ça permet de simuler des scénarios : une détente des taux à
2,5 % en 2026 redonnerait 6 % de rythme de vente en plus par rapport à la
situation actuelle, et une remontée à 3,5 % en retirerait 3 %.

**Étape 5 : un résultat complémentaire, à l'échelle d'un programme.**
En plus de ces analyses à l'échelle du groupe, tu ajustes, pour chaque
opération individuelle, une courbe en forme de S sur ses réservations
cumulées dans le temps (le rythme de vente typique d'un programme
immobilier : lent au début, rapide au milieu, qui ralentit à la fin
quand il ne reste que les moins bons lots). Cette courbe explique mieux
les données qu'une simple droite sur 25 des 28 opérations terminées, et
donne un repère utile : un délai médian de 20 mois pour vendre 90 % du
potentiel d'un programme.

**Comment résumer l'axe B en une minute devant le jury :**
« Sur l'axe B, j'ai d'abord découvert que la corrélation brute entre
réservations et taux de crédit était trompeuse à cause de la croissance
du portefeuille — corrigée, elle devient nette. J'ai ensuite construit un
panel avec un modèle à effets aléatoires, qui sépare l'effet propre à
chaque programme de l'effet de la conjoncture : deux tiers contre un
tiers, avec un effet du taux de crédit de -19 % par point. Pour vérifier
que ce résultat n'était pas un artefact, je l'ai comparé à un modèle de
série temporelle sur la série agrégée, où l'effet du taux disparaît —
logique, avec seulement 114 points sur une seule série, on ne peut pas
isoler un effet aussi lent. J'ai donc combiné les deux modèles pour
produire des scénarios de taux exploitables, en plus d'une courbe de
vente typique par programme, utile pour la trésorerie. »

---

## 6. Axe C — l'optimisation des prix, en clair pour la présentation

**Le problème métier.** La direction financière veut savoir à quel prix
vendre chaque lot restant, et si les remises commerciales actuelles, qui
se décident au cas par cas, sont bien calibrées.

**Étape 1 : le modèle hédonique — comprendre ce qui fait le prix.** L'idée
d'un modèle hédonique, c'est de considérer que le prix d'un logement est
la somme de plusieurs caractéristiques valorisées séparément : la
surface, l'étage, l'exposition, la proximité de la mer, s'il s'agit de
logement social réglementé, l'année de vente, etc. Tu construis une
régression (une variante de l'OLS) sur plus de 5 000 appartements vendus
depuis 2016, avec le logarithme du prix comme cible (rappel de la
première leçon de l'exploration : le prix brut est trop asymétrique, le
log le rend exploitable). Ce modèle explique 88,6 % de la variance du
prix — un très bon score, avec une erreur moyenne d'environ 11 %.

**Étape 2 : lire les résultats, poste par poste.** Chaque coefficient du
modèle a un sens concret : un étage de plus vaut environ 6 % de prix en
plus ; le logement social, dont les prix sont réglementés par l'État,
coûte 63 % de moins qu'un logement libre équivalent ; il y a un effet
« millésime », les prix ayant augmenté d'environ 19 % entre 2016 et
2023, avec un plateau après 2022 — ce qui confirme, en écho à l'axe B,
que face à la remontée des taux, les promoteurs ont plutôt ajusté leur
volume de ventes que baissé leurs prix affichés.

**Étape 3 : détecter les lots mal positionnés.** Une fois le modèle
construit, tu l'appliques au stock actuel : pour chaque lot invendu, tu
compares son prix affiché (le prix « grille ») au prix que le modèle
prédirait compte tenu de ses caractéristiques. Un écart important dans
un sens ou dans l'autre signale un lot potentiellement mal positionné :
sur 127 appartements en stock, 24 sont identifiés comme hors marché
(sous-cotés ou surcotés), une piste concrète pour ajuster la grille de
prix.

**Étape 4 : le vrai défi, recommander une remise optimale.** Ici, tu as
besoin d'une information supplémentaire : l'élasticité-prix, c'est-à-dire
de combien la demande augmente quand on baisse le prix de 1 %. Ton
estimation interne (-0,81) n'est pas statistiquement fiable (p = 0,57,
avec un intervalle de confiance très large), donc tu ne l'utilises pas
telle quelle : tu retiens une élasticité de -1, compatible avec ton
estimation et avec les valeurs habituelles trouvées dans la littérature
scientifique sur le logement neuf (entre -1 et -2). C'est un choix
documenté, pas une approximation cachée.

**Étape 5 : résoudre le problème d'optimisation.** Tu veux trouver, pour
chaque lot, la remise qui maximise le chiffre d'affaires total, tout en
respectant un objectif de volume de ventes fixé (par exemple, accélérer
les ventes de 8 %). C'est un problème d'optimisation sous contrainte, que
tu résous avec la méthode du multiplicateur de Lagrange (voir
`explications_questions_jury.md`, question 14, pour le détail), puis
vérifié avec un second algorithme numérique indépendant (SLSQP) : les
deux méthodes tombent sur quasiment la même réponse (écart de 0,0056),
ce qui confirme que le calcul est juste.

**Étape 6 : un résultat contre-intuitif.** Avec une élasticité de -1, la
solution mathématique du problème donne une remise identique en euros
sur tous les lots — pas un pourcentage identique. Or un même montant en
euros représente un pourcentage plus fort sur un petit lot que sur un
grand. Sur l'opération test Arpeggio, viser 8 % d'accélération des
ventes donne un montant constant d'environ 23 000 euros, ce qui se
traduit par des remises de -5 % à -14 % selon le prix du lot — l'inverse
de la pratique actuelle, où les remises sont décidées au cas par cas
sans logique systématique.

**Comment résumer l'axe C en une minute devant le jury :**
« Sur l'axe C, j'ai construit un modèle hédonique qui explique 88,6 % de
la variance du prix à partir des caractéristiques du logement — étage,
exposition, proximité de la mer, logement social, année de vente. Il me
sert à deux choses : détecter les lots mal positionnés dans le stock
actuel, 24 sur 127, et surtout recommander une remise optimale. Pour ça,
il me fallait une élasticité-prix ; la mienne, estimée en interne,
n'était pas significative, donc j'ai retenu une valeur de la littérature
scientifique, en le disant explicitement. J'ai résolu le problème
d'optimisation par un multiplicateur de Lagrange, vérifié par un second
algorithme indépendant, et le résultat est contre-intuitif : la remise
optimale est un montant identique en euros sur tous les lots, donc un
pourcentage plus fort sur les petits lots — l'inverse de ce qui se
pratique aujourd'hui au cas par cas. »

---

## 7. Le diagramme de la leçon 2 de l'exploration des données

C'est le graphique intitulé « Intensité de vente par programme —
l'effet 2023 apparaît » (Figure 2.2 du mémoire), utilisé sur la slide 9
du discours et de la plateforme.

**Ce qu'il montre.** En abscisse, le temps, de 2017 à la fin de la
période étudiée. En ordonnée, l'intensité de vente : le nombre de
réservations par opération active, mois par mois (exactement le calcul
expliqué au point 2 ci-dessus). Deux courbes sont tracées : la valeur
mensuelle brute, qui zigzague beaucoup d'un mois à l'autre (les
réservations ne sont jamais parfaitement régulières), et une moyenne
mobile sur 6 mois, qui lisse ces zigzags pour faire apparaître la
tendance de fond.

**Pourquoi ce graphique existe.** Il vient juste après avoir montré que
la corrélation brute (sur le volume total, non corrigé) ne révélait
rien. Ce graphique, lui, montre l'intensité déjà corrigée — et c'est sur
cette version qu'on voit apparaître clairement un decrochage à partir de
2022-2023 : la moyenne mobile baisse nettement à ce moment-là, ce qui
coïncide avec la remontée des taux de crédit immobilier sur la même
période. C'est la preuve visuelle, avant même le calcul de corrélation,
que le ralentissement du marché n'est pas une impression, mais un vrai
changement de tendance dans les données une fois qu'on regarde la bonne
variable.

**Comment le présenter simplement au jury :**
« Ce graphique montre l'intensité de vente corrigée, mois par mois, avec
une moyenne mobile pour lisser le bruit. On y voit un décrochage net à
partir de 2022-2023, qui coïncide avec la remontée des taux — c'est ce
signal visuel qui m'a confirmé que la correction par le nombre
d'opérations actives faisait apparaître un vrai phénomène, pas un
artefact statistique. »
