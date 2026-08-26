# Comprendre chaque réponse — le concept avant le « pourquoi »

Ce fichier accompagne `questions_jury.md`. Il ne remplace pas les réponses
préparées : il les explique, question par question, pour que tu comprennes
la notion elle-même et pas seulement la phrase à dire. L'idée, c'est que si
le jury reformule la question autrement, ou pose une sous-question, tu
puisses répondre avec le concept en tête plutôt qu'avec une phrase apprise
par cœur.

Pour chaque question : **le concept, en clair** (l'idée générale, avec une
image si possible), puis **pourquoi ce choix dans ton projet** (comment le
concept général s'applique à ton cas précis).

---

## Méthodologie générale

### 1. La validation croisée

**Le concept, en clair.** Quand tu construis un modèle, tu veux savoir
s'il marche bien sur des données qu'il n'a jamais vues — pas seulement sur
celles qui ont servi à le construire, sinon tu mesures sa capacité à
« apprendre par cœur », pas sa capacité à généraliser. La méthode la plus
simple, c'est de couper les données en deux : une partie pour entraîner
le modèle, une partie pour le tester. Le problème, sur un petit
échantillon, c'est que ce découpage est un tirage au sort : selon les
lignes qui tombent côté test, le score peut changer beaucoup, sans que le
modèle lui-même ait changé. La validation croisée résout ça en répétant
l'opération plusieurs fois avec des découpages différents, puis en
moyennant. Avec 5 plis (5-fold), tu coupes les données en 5 morceaux, tu
entraînes 5 fois en gardant à chaque fois un morceau différent pour le
test, et tu obtiens 5 scores dont tu peux calculer la moyenne et
l'écart-type. « Stratifiée » veut juste dire qu'on s'assure que chaque
morceau contient à peu près la même proportion de cas « à risque » et de
cas « sains », pour ne pas tomber par malchance sur un pli qui n'en
contient aucun.

**Pourquoi ce choix dans ton projet.** Avec seulement 123 opérations
exploitables pour l'axe A, un seul découpage entraînement/test aurait
donné un score qui dépend beaucoup du hasard du tirage. La validation
croisée à 5 plis te donne un score plus fiable (0,306 ± 0,069 pour la
forêt aléatoire, par exemple) : la moyenne te dit la performance
attendue, et l'écart-type te dit à quel point ce chiffre est stable. Tu
l'as posée comme règle non négociable dès le départ, précisément parce
que ton échantillon est petit et qu'un score sur un seul découpage
t'aurait trompée.

### 2. Le sur-apprentissage et pourquoi peu de deep learning

**Le concept, en clair.** Un modèle « sur-apprend » (overfitting) quand il
devient tellement flexible qu'il colle non seulement à la vraie tendance
des données, mais aussi au bruit — les particularités propres à cet
échantillon précis, qui ne se reproduiront pas ailleurs. Le symptôme
classique : un score excellent sur les données d'entraînement, et un
score qui s'effondre sur des données nouvelles (donc en validation
croisée). Plus un modèle a de paramètres à ajuster par rapport au nombre
d'exemples dont il dispose, plus le risque de sur-apprentissage est
grand. Un réseau de neurones (deep learning) a énormément de paramètres :
il lui faut énormément de données pour ne pas sur-apprendre.

**Pourquoi ce choix dans ton projet.** Tu l'as vérifié en vrai, pas juste
en théorie : ton perceptron multicouche (MLP) obtient un F1 de 0,913 sur
l'entraînement, contre 0,262 en validation croisée. L'écart énorme entre
les deux, c'est la preuve directe du sur-apprentissage. Avec 123
opérations, un modèle à beaucoup de paramètres n'a simplement pas assez
d'exemples pour apprendre la vraie tendance plutôt que le bruit. C'est
pour ça que tu as privilégié des modèles plus simples (régression
logistique, Ridge, forêt aléatoire) : ils ont moins de paramètres, donc
ils généralisent mieux avec peu de données.

### 3. La confidentialité des données

**Le concept, en clair.** Une donnée « nominative » identifie directement
une personne (nom, date de naissance, adresse précise). Une donnée
« agrégée » ou « dérivée » résume un ensemble d'informations sans exposer
l'identité — par exemple, un délai moyen, un montant, une catégorie.
Utiliser uniquement des données agrégées comme variables d'un modèle,
c'est une pratique de protection de la vie privée : le modèle apprend des
régularités statistiques, pas des identités.

**Pourquoi ce choix dans ton projet.** Tu manipules des milliers de
coordonnées d'acquéreurs dans la reprise des tiers, et des commentaires
de vente potentiellement très personnels dans l'axe transverse. Le
principe que tu as posé — jamais de nom ou de date de naissance affiché
ou utilisé comme variable — n'est pas une contrainte technique du
modèle, c'est un principe éthique et réglementaire que tu as intégré dès
la conception, pas ajouté après coup.

### 4. Traductrice avant modélisatrice

**Le concept, en clair.** Ce n'est pas une notion statistique, c'est une
observation sur le métier de data scientist : la partie la plus difficile
n'est presque jamais le calcul lui-même (une fois qu'on sait quelle
méthode utiliser, l'appliquer est relativement mécanique). La partie
difficile, c'est de transformer un problème flou, exprimé en langage
métier (« on n'arrive pas à voir venir les dérapages »), en une question
qu'on peut vraiment calculer (quelle variable cible, quel seuil, quel
périmètre de données) — puis de refaire le chemin inverse : transformer
un résultat chiffré en information utilisable par quelqu'un qui n'est pas
statisticien.

**Pourquoi ce choix dans ton projet.** Le retour du commanditaire sur la
première version de la plateforme (trop de F1, de R², de coefficients)
est l'illustration concrète de cette idée : un résultat statistiquement
juste mais mal traduit ne sert à rien. Tu as dû reformuler tes résultats
en langage métier pour qu'ils deviennent réellement utilisables.

### 5. Le périmètre plateforme plus étroit que les notebooks

**Le concept, en clair.** Ce n'est pas une notion statistique non plus :
c'est un compromis classique entre exhaustivité scientifique (analyser
tout ce qu'on peut, pour la compréhension complète du phénomène) et
utilisabilité opérationnelle (livrer un outil que les utilisateurs
comprennent et utilisent vraiment). Un outil trop large ou trop
hétérogène peut devenir illisible pour son usage principal.

**Pourquoi ce choix dans ton projet.** Les notebooks couvrent les 267
opérations (promotion et aménagement foncier), parce que la recherche a
besoin du périmètre complet — la typologie, par exemple, a besoin des
deux métiers pour faire émerger ses 4 familles. Mais le commanditaire a
demandé que la plateforme se limite aux 147 opérations de promotion, son
usage principal, pour que l'outil reste simple à lire. C'est un choix
métier, pas une limite technique : tu pourrais étendre la plateforme à
l'aménagement plus tard.

### 6. Les trois régimes de preuve

**Le concept, en clair.** L'idée, c'est que « prouver que quelque chose
est correct » ne veut pas dire la même chose selon le type de livrable.
Tu identifies trois régimes différents :
- **Réconciliation** (pour une reprise de données) : on compare deux
  sources et on vérifie qu'elles concordent — la preuve porte sur
  l'arrivée de la donnée, pas sur son exactitude intrinsèque.
- **Usage** (pour un outil ou un tableau de bord) : on vérifie que les
  gens s'en servent, et pour la bonne chose — la preuve porte sur
  l'adoption, pas sur un calcul.
- **Validation statistique** (pour un modèle) : on vérifie que le
  résultat tient sur des données que le modèle n'a pas vues — la preuve
  porte sur la généralisation.

Chacun de ces régimes a un angle mort : une réconciliation peut valider
une donnée fausse si elle est fausse des deux côtés de la même manière ;
un modèle validé statistiquement peut ne jamais être utilisé.

**Pourquoi ce choix dans ton projet.** C'est une prise de recul sur les
trois types de travaux de ton année (les deux reprises, les tableaux de
bord et le SSO, le Copilote) : chacun demande une preuve différente, et
confondre les trois serait une erreur méthodologique — par exemple juger
un modèle statistique seulement à l'usage qu'on en fait, sans jamais
vérifier sa validité sur des données nouvelles.

---

## Axe A — le risque de marge

### 7. Pourquoi la forêt aléatoire plutôt que le CART qui a un meilleur score

**Le concept, en clair.** Un arbre de décision (CART) découpe l'espace
des variables par une suite de questions oui/non (« la marge budgétée
est-elle inférieure à X ? »), jusqu'à obtenir des groupes homogènes. C'est
facile à lire, mais un arbre unique est **instable** : si tu changes
légèrement les données d'entraînement, l'arbre peut choisir des
questions très différentes dès le début, ce qui change toute sa
structure. Une **forêt aléatoire** construit des centaines d'arbres
légèrement différents (chacun sur un sous-échantillon aléatoire des
données et des variables), puis fait voter tous ces arbres ensemble. Le
vote moyenne les instabilités individuelles : la forêt est presque
toujours plus stable et plus fiable qu'un arbre seul, même quand un
arbre isolé obtient parfois un meilleur score sur un découpage précis.
Le score « out-of-bag » (OOB) est une astuce propre aux forêts : comme
chaque arbre n'utilise qu'une partie des données, on peut tester chaque
arbre sur les données qu'il n'a pas vues, sans avoir besoin d'un
découpage séparé.

**Pourquoi ce choix dans ton projet.** Le CART obtient un F1 de 0,340,
supérieur à la forêt (0,306), mais uniquement sur ce découpage précis en
validation croisée — un chiffre qui peut bouger si on refait le tirage.
Tu as choisi de sélectionner le modèle final parmi les méthodes
interprétables (logistique et forêt), et pas simplement le score maximum
toutes méthodes confondues, parce que sur la plateforme, ce qui compte,
c'est autant la fiabilité et l'explicabilité (la forêt donne un score
OOB de 0,691 et une liste de variables importantes) que le score brut.

### 8. Pourquoi un F1 aussi bas (0,26 à 0,34) reste utilisable

**Le concept, en clair.** Le F1-score combine deux choses : la précision
(parmi les opérations que le modèle signale comme « à risque », combien
le sont vraiment ?) et le rappel (parmi les opérations vraiment à
risque, combien le modèle en détecte ?). C'est une métrique adaptée
quand les classes sont déséquilibrées (ici, 28 % à risque contre 72 %
saines), parce que l'exactitude simple (le pourcentage de bonnes
réponses) serait trompeuse — un modèle qui prédit toujours « saine »
aurait 72 % d'exactitude sans être utile. Un F1 de 0,30 n'est pas
excellent, mais il faut le comparer à la référence : un modèle qui ne
détecte jamais rien a un F1 de 0.

**Pourquoi ce choix dans ton projet.** Tu ne présentes pas ce résultat
comme une prédiction fiable à 100 %, mais comme un signal d'alerte à
recouper avec le jugement humain — d'où l'importance d'accompagner
l'alerte du modèle Ridge explicatif, qui montre pourquoi une opération
est signalée. C'est une position honnête : le signal existe (il bat
largement 0), mais il reste faible.

### 9. Le seuil de -2 % pour la dérive matérielle

**Le concept, en clair.** Un seuil de classification transforme une
variable continue (ici, l'écart de marge en pourcentage) en catégorie
(« à risque » ou « saine »). Ce seuil peut être choisi de deux façons :
soit statistiquement (par exemple, en optimisant un critère mathématique
sur les données), soit par un jugement métier (une valeur qui a du sens
pour les utilisateurs, indépendamment des données). Les deux approches
sont légitimes, mais elles ne se justifient pas de la même manière face
au jury.

**Pourquoi ce choix dans ton projet.** Ton seuil de -2 % est un choix
métier : c'est l'ordre de grandeur d'un dépassement jugé significatif par
la direction financière, en dessous duquel l'écart est considéré comme
un aléa normal de chantier. Ce n'est pas un défaut de rigueur de ne pas
l'avoir optimisé statistiquement — c'est cohérent avec l'objectif :
produire une alerte que les utilisateurs comprennent et acceptent.

### 10. Ridge plutôt que Lasso

**Le concept, en clair.** La régularisation, c'est une technique qui
pénalise les modèles trop complexes pour les empêcher de sur-apprendre
(voir question 2). Ridge et Lasso pénalisent tous les deux la taille des
coefficients d'une régression, mais différemment : Ridge réduit tous les
coefficients progressivement vers zéro sans jamais les annuler
complètement ; Lasso peut mettre certains coefficients strictement à
zéro, ce qui revient à éliminer certaines variables du modèle. Lasso est
donc utile quand tu veux sélectionner automatiquement les variables les
plus importantes ; Ridge est préférable quand tu veux garder toutes les
variables visibles, avec des coefficients comparables entre elles.

**Pourquoi ce choix dans ton projet.** Ni Ridge ni Lasso n'améliorent le
R² de test par rapport à l'OLS simple (attendu, la moitié de
l'échantillon étant à variation nulle). Mais l'intérêt du Ridge n'est
pas la prédiction, c'est la lisibilité : sur des variables standardisées
(donc comparables), il te donne une lecture claire de tous les facteurs
de dérive — le poids des postes techniques, l'effet protecteur d'une
marge confortable. Le Lasso aurait pu supprimer certaines variables, ce
qui aurait cassé cette lecture d'ensemble.

---

## Axe B — la vitesse d'écoulement

### 11. Le modèle à effets aléatoires plutôt qu'un pooled OLS

**Le concept, en clair.** Un « panel », c'est un jeu de données où
chaque unité (ici, une opération) est observée plusieurs fois dans le
temps (chaque mois). Le pooled OLS traite chaque ligne (opération ×
mois) comme totalement indépendante des autres, ce qui ignore que
plusieurs lignes viennent de la même opération et se ressemblent donc
entre elles. Un modèle à effets aléatoires corrige ça : il sépare la part
de variation qui vient de l'opération elle-même (ses caractéristiques
propres, stables dans le temps) de la part qui vient du moment observé
(la conjoncture). Le coefficient de corrélation intraclasse (ICC) mesure
la proportion de variance totale qui vient de l'opération elle-même,
plutôt que du temps.

**Pourquoi ce choix dans ton projet.** Ignorer la structure du panel
biaise l'estimation : le pooled OLS surestime l'effet du taux de crédit
(-0,242) par rapport au modèle à effets aléatoires (-0,216), parce qu'il
confond l'effet réel de la conjoncture avec l'effet de composition du
portefeuille (le fait que les opérations qui entrent et sortent du
portefeuille au fil du temps ne sont pas les mêmes). L'ICC de 0,66 te
dit une chose utile en soi : deux tiers du rythme de vente s'expliquent
par le programme lui-même, un tiers par la conjoncture.

### 12. La contradiction entre le panel et l'ARIMA — la « spurious regression »

**Le concept, en clair.** Une « spurious regression » (corrélation
fallacieuse) se produit quand deux séries temporelles semblent liées
statistiquement sans qu'il y ait de vrai lien causal — souvent parce que
les deux évoluent dans le temps pour des raisons indépendantes (une
tendance commune, par exemple), ce qui crée une corrélation artificielle.
C'est un piège classique en séries temporelles : plus une série a de
points, plus on peut distinguer un vrai effet répété d'une coïncidence
de tendances.

**Pourquoi ce choix dans ton projet.** Le panel, avec plus de 3 200
observations, identifie un effet du taux très significatif. Mais sur la
série agrégée du groupe (une seule série, 114 points mensuels), l'effet
disparaît une fois qu'on modélise correctement la dynamique temporelle
avec l'ARIMA. Ce n'est pas une contradiction qui invalide le panel :
c'est que 114 mois sur une seule série ne suffisent pas à isoler un
effet lent, alors que le panel a plus de puissance statistique grâce à
son volume. Tu combines donc les deux : l'ARIMA pour la trajectoire
réaliste, le panel pour la taille de l'effet du taux.

### 13. Comment on choisit l'ordre d'un modèle ARIMA

**Le concept, en clair.** ARIMA veut dire AutoRegressive Integrated
Moving Average : un modèle qui décrit une série temporelle par sa propre
histoire récente (la partie AR), une différenciation pour la rendre
stable (la partie I, pour Integrated), et les erreurs passées (la partie
MA). Le « (1,1,1)×(1,0,1,12) » décrit ces trois composantes pour la
partie non saisonnière et pour la partie saisonnière (le « 12 » indique
un cycle de 12 mois). Choisir ces chiffres à l'œil serait arbitraire : la
procédure standard consiste à tester plusieurs combinaisons, à ne garder
que celles dont les résidus (l'écart entre le modèle et les données
réelles) ressemblent à du bruit blanc — c'est-à-dire n'ont plus de
structure prévisible, ce qui se vérifie avec un test de Ljung-Box — puis,
parmi les modèles qui passent ce test, à choisir celui qui minimise
l'AICc, un critère qui pénalise les modèles inutilement complexes.

**Pourquoi ce choix dans ton projet.** Tu as suivi exactement cette
procédure plutôt que de choisir un ordre au hasard : le modèle retenu a
un AICc de 611,7 et un test de Ljung-Box qui ne rejette pas
l'hypothèse de bruit blanc (p = 0,224), ce qui veut dire que le modèle
capture bien la structure de la série sans laisser de motif prévisible
dans les résidus.

---

## Axe C — l'optimisation des prix

### 14. Le multiplicateur de Lagrange vérifié par SLSQP

**Le concept, en clair.** Un problème d'optimisation sous contrainte,
c'est chercher la meilleure solution (ici, les remises qui maximisent le
chiffre d'affaires) tout en respectant une règle fixe (ici, atteindre un
objectif de volume de ventes). Le multiplicateur de Lagrange est une
technique mathématique classique pour résoudre ce genre de problème : il
transforme la contrainte en un terme ajouté à l'objectif, pondéré par un
nombre (le multiplicateur), qu'on peut interpréter comme le « prix » de
la contrainte — combien ça coûterait de la relâcher un peu. Dans les cas
simples, cette méthode donne une formule explicite (une solution en
forme fermée). SLSQP est un algorithme numérique générique, qui résout le
même type de problème par itérations successives, sans passer par une
formule. Utiliser les deux méthodes sur le même problème et vérifier
qu'elles donnent la même réponse, c'est une façon de se contrôler
soi-même : si tu as fait une erreur de calcul dans la formule de
Lagrange, le solveur générique donnerait un résultat différent.

**Pourquoi ce choix dans ton projet.** L'écart entre les deux méthodes
est de 0,0056 — quasiment nul — ce qui confirme que ta formule
analytique par Lagrange est correcte. C'est une démarche de vérification
croisée, pas juste une méthode « plus rigoureuse » qu'une autre : les
deux se confirment mutuellement.

### 15. Une élasticité non significative, retenue quand même

**Le concept, en clair.** Une p-value mesure la probabilité d'observer un
résultat au moins aussi extrême que celui obtenu, si en réalité il n'y
avait aucun effet. Une p-value élevée (ici 0,57) veut dire qu'on ne peut
pas distinguer statistiquement ton estimation d'un simple hasard — pas
qu'elle est fausse, mais qu'on n'a pas assez de données pour être sûr de
sa valeur précise. Un intervalle de confiance très large (ici, de -3,62
à +1,99) illustre la même incertitude : la vraie valeur pourrait être
n'importe où dans cette fourchette très étendue, y compris avec un signe
différent. Face à ça, deux options honnêtes : soit présenter la valeur
brute avec toute son incertitude, soit remplacer par une valeur externe
mieux établie (issue de la littérature scientifique), en le disant
clairement.

**Pourquoi ce choix dans ton projet.** Tu as choisi la seconde option :
plutôt que d'utiliser ton -0,81 non significatif comme s'il était fiable,
tu retiens -1, une valeur cohérente avec ton estimation (même signe,
dans la fourchette de l'intervalle de confiance) et avec des références
publiées sur le marché du logement neuf. C'est un choix documenté et
assumé, pas une approximation cachée.

### 16. Pourquoi la remise optimale est un montant constant en euros

**Le concept, en clair.** L'élasticité-prix mesure de combien la demande
change quand le prix change (en pourcentage). Une élasticité de -1 veut
dire qu'une baisse de prix de 1 % entraîne une hausse de la demande de
1 % — un cas particulier mathématiquement intéressant, où les deux
effets se compensent d'une façon précise. Quand tu résous le problème
d'optimisation sous cette hypothèse précise, la condition mathématique
qui définit la meilleure solution se simplifie, et il se trouve qu'elle
implique une remise identique en valeur absolue (en euros) pour tous les
lots, plutôt qu'un pourcentage identique. Ce n'est pas un choix arbitraire
que tu as fait : c'est ce que la mathématique du problème impose, une
fois l'élasticité fixée à -1.

**Pourquoi ce choix dans ton projet.** Ce résultat a une conséquence
concrète et contre-intuitive : un montant identique en euros représente
un pourcentage plus fort sur un petit lot que sur un grand, ce qui est
l'inverse de la pratique actuelle (remises décidées au cas par cas). Tu
peux illustrer ça avec Arpeggio : viser 8 % d'accélération des ventes
donne un montant constant d'environ 23 000 euros, mais des pourcentages
de remise qui varient de -5 % à -14 % selon le prix du lot.

---

## Typologie et exploration des données

### 17. L'ACP pour construire une typologie

**Le concept, en clair.** L'analyse en composantes principales (ACP)
est une méthode qui résume beaucoup de variables corrélées entre elles
en un petit nombre de nouvelles variables (les composantes), qui captent
le maximum de variation possible dans les données d'origine. L'idée,
c'est que si neuf postes de dépense varient souvent ensemble (une
opération qui dépense plus en foncier dépense aussi typiquement plus en
VRD, par exemple), on peut résumer l'essentiel de cette information en
seulement deux ou trois axes, plus faciles à interpréter et à comparer.
La vérification par SVD (décomposition en valeurs singulières) est une
autre façon de calculer mathématiquement le même résultat, par une voie
de calcul différente : si les deux méthodes tombent sur la même réponse,
c'est une preuve solide qu'il n'y a pas d'erreur de calcul.

**Pourquoi ce choix dans ton projet.** Comparer deux opérations sur leurs
montants bruts n'a pas de sens (2 millions contre 50 millions), mais
comparer la *structure* de leur budget, oui. L'ACP te permet de résumer
cette structure en deux axes qui expliquent 61 % de la variance, avec
une vérification par SVD qui confirme le calcul à une précision
quasi parfaite. C'est cette typologie qui sert ensuite de comparateur
dans l'axe A.

### 18. Choisir le nombre de familles (K = 4)

**Le concept, en clair.** Une classification non supervisée (clustering)
regroupe des individus similaires sans savoir à l'avance combien de
groupes il devrait y avoir : il faut donc choisir ce nombre, K, avec des
critères objectifs plutôt qu'au hasard. Plusieurs critères existent : le
critère du coude regarde comment l'homogénéité interne des groupes
s'améliore quand on augmente K, et cherche le point où l'amélioration
ralentit nettement ; le coefficient de silhouette mesure, pour chaque
point, s'il est bien plus proche de son propre groupe que des autres
(plus il est élevé, mieux c'est) ; l'indice de Davies-Bouldin mesure la
séparation entre groupes (plus il est bas, mieux c'est). Utiliser
plusieurs critères qui convergent vers le même K rend le choix plus
robuste qu'un seul critère isolé. Enfin, comparer deux méthodes de
clustering complètement différentes (k-moyennes et classification
hiérarchique par distance de Ward) avec l'indice de Rand ajusté — qui
mesure l'accord entre deux partitions — permet de vérifier que le
résultat n'est pas un artefact d'une méthode en particulier.

**Pourquoi ce choix dans ton projet.** Tes trois critères (coude,
silhouette maximale à 0,47, Davies-Bouldin minimal à 0,96) convergent
tous vers K = 4, et la comparaison avec la CAH-Ward donne un indice de
Rand ajusté de 0,862 — un accord fort entre deux méthodes de nature
différente. C'est cette convergence de plusieurs preuves indépendantes
qui rend ta typologie en quatre familles solide, pas le résultat d'un
seul critère qu'on aurait pu forcer à donner le chiffre qu'on voulait.

### 19. La corrélation fallacieuse détectée dans l'exploration

**Le concept, en clair.** Ce cas est un exemple concret de la spurious
regression déjà mentionnée en question 12, mais version corrélation
simple plutôt que régression. Deux séries qui évoluent dans le temps
peuvent sembler corrélées (ou, ici, non corrélées) juste à cause d'une
troisième force qui les affecte toutes les deux — ici, la croissance du
nombre d'opérations commercialisées. La leçon méthodologique, c'est que
la corrélation brute mesurée sur des volumes cumulés peut masquer une
vraie relation, alors qu'une variable correctement normalisée (rapportée
au nombre d'opérations actives, donc une intensité plutôt qu'un volume)
révèle la relation réelle.

**Pourquoi ce choix dans ton projet.** Tu avais une intuition (le lien
entre taux de crédit et réservations devait être négatif), et la donnée
brute t'a d'abord contredite (r = +0,07, quasi nul). Plutôt que
d'ignorer ce résultat surprenant ou de forcer une conclusion attendue,
tu as creusé, trouvé l'explication (le doublement du nombre
d'opérations commercialisées), corrigé la variable, et retrouvé un lien
net et cohérent (r = -0,34 avec le taux, +0,44 avec la confiance des
ménages). Cette démarche — vérifier vraiment ce que dit la donnée plutôt
que ce qu'on attend d'y trouver — a ensuite structuré toute la méthode de
l'axe B (travailler sur l'intensité, pas sur le volume brut).

---

## Infrastructure

### 20. La base SQL plutôt que pandas seul, et le comparatif avec Spark

**Le concept, en clair.** Une base de données relationnelle organise
l'information en tables reliées entre elles, interrogeables par des
requêtes (SQL). Une « vue » SQL est une requête enregistrée, qu'on peut
réutiliser comme si c'était une table : l'intérêt, c'est qu'un même
calcul (par exemple, « la marge par opération ») n'est écrit qu'une
seule fois, dans la définition de la vue, et tous les programmes qui en
ont besoin utilisent cette même définition — au lieu de recopier le
calcul à chaque endroit, avec le risque qu'une copie diverge des autres
avec le temps. Spark est un outil de calcul distribué, conçu pour traiter
des volumes de données trop gros pour tenir en mémoire sur une seule
machine, en répartissant le travail sur plusieurs machines. Il a un coût
fixe de démarrage (lancer la coordination entre machines) qui n'est
rentable que si le volume de données est assez grand pour justifier
cette répartition.

**Pourquoi ce choix dans ton projet.** La base SQL garantit que les
notebooks et la plateforme calculent toujours les indicateurs de la même
façon — un vrai bénéfice de fiabilité, indépendant du volume de données.
Le test Spark, lui, sert à répondre à une question différente : est-ce
que l'architecture tiendrait si le volume grossissait beaucoup (par
exemple à l'échelle de tout le groupe Nexity) ? Le résultat (pandas à
9,9 ms contre Spark à 577,4 ms, plus 23,9 secondes de démarrage) montre
que sur ton volume actuel, le coût fixe de Spark n'est pas rentable —
mais l'exercice prouve que la voie de montée en charge existe si le
besoin se présentait un jour.
