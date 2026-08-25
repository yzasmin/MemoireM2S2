# Discours de soutenance — texte mot à mot

Calibré pour **25 minutes** à l'oral (~130-140 mots/minute). Les
indications `[pause]` marquent un silence court, volontaire. Une entrée =
une slide de `plan_slides.md` : le découpage est identique dans les deux
fichiers.

**Répartition volontaire : environ 30 % du temps sur les deux reprises de
données (mes missions d'alternance), 70 % sur le Copilote Financier — le
projet de data science proprement dit.**

---

## SLIDE 1 — Titre

Bonjour à toutes et à tous. Je m'appelle Yasmina Saoud, je suis en deuxième
année de Master MIASHS, en alternance au sein du groupe Angelotti.

Mon année a été marquée par deux gros chantiers : une reprise de données
vers un nouvel ERP, puis un projet de data science, le Copilote Financier.
Je vais passer assez vite sur le premier pour consacrer l'essentiel de mon
temps au second, parce que c'est vraiment là qu'il y a de la statistique.
[pause]

Je commence par le contexte.

## SLIDE 2 — Contexte Angelotti

Le groupe Angelotti est un promoteur-aménageur immobilier, filiale de
Nexity. Il a deux métiers assez différents : la promotion, qui construit
et vend des logements neufs, et l'aménagement, qui viabilise des terrains
à bâtir pour les revendre en lots. [pause]

Chaque opération immobilière est portée par une société dédiée. Un budget
est posé au moment où l'opération démarre — foncier, construction,
honoraires, commercialisation — en face des recettes attendues. Et
ensuite, la vie de l'opération le fait dériver petit à petit : des appels
d'offres plus chers que prévu, un rythme de vente plus lent qu'anticipé,
des désistements d'acquéreurs, des remises commerciales données au cas
par cas. Aujourd'hui, cette dérive est suivie opération par opération,
dans des tableurs Excel, sans vision statistique transverse sur
l'ensemble du portefeuille. C'est ce constat qui a motivé les deux
projets que je vais vous présenter.

## SLIDE 3 — La migration des opérations

Cette année, il y a eu un événement qui a occupé tout mon premier
semestre : le remplacement de l'ERP historique, Grimmo, par un nouveau
système, SPO. [pause] Un ERP, c'est le logiciel qui centralise la gestion
d'une entreprise. Et changer d'ERP, ce n'est pas juste changer d'outil,
c'est changer complètement de modèle de données.

Il fallait recréer 283 opérations dans SPO, à une échelle où la saisie
manuelle n'était pas possible. On a choisi une stratégie hybride :
injection automatisée des gros volumes via les interfaces de
programmation de l'éditeur, et traitement manuel des cas trop
particuliers pour rentrer dans un gabarit. [pause]

En analysant les erreurs renvoyées par le système, j'ai découvert deux
règles qui n'étaient documentées nulle part. La première, c'est un ordre
d'injection strict entre opération, tranches et budget. La seconde,
c'est que les identifiants ne sont jamais stables, ils changent à chaque
mise à jour. J'ai dû construire un système qui va toujours chercher la
version la plus récente avant d'agir.

Le processus a été sécurisé par une validation par paliers : trois
opérations pilotes, puis un lot de douze, avant la migration de masse.
Et comme les utilisateurs devaient pouvoir facturer dès le basculement,
on a déployé la structure d'abord, le détail budgétaire ensuite — la
stratégie des « coquilles vides ». À la fin du semestre, les 283
opérations existaient dans SPO.

## SLIDE 4 — La reprise des tiers : le problème

Au second semestre, je me suis occupée de reconstituer le référentiel
client — ce que SPO appelle un « tiers ». Ma matière première, c'était
deux extractions du CRM, le logiciel qui gère la relation commerciale :
une de 1 557 ventes, et une de 1 602 lignes de coordonnées d'acquéreurs.
[pause]

Le problème, c'est qu'une ligne de cette extraction ne décrit pas un
client, elle décrit une vente. Un acquéreur qui a acheté trois lots
apparaît trois fois, et rien dans le fichier ne le signale. Et en plus,
SPO n'était pas vide : il y avait déjà environ 13 000 tiers dedans, créés
par saisie ou par d'autres canaux.

L'enjeu tenait en une phrase : créer chaque client une fois, et une
seule, sans avoir à vérifier ça ligne par ligne à la main sur un volume
pareil.

## SLIDE 5 — La reprise des tiers : la solution et les résultats

J'ai construit un fichier de travail entièrement piloté par formules. Le
cœur du dispositif, ce sont trois clés d'unicité différentes selon le
type de client — un couple, une personne seule, ou une société — parce
qu'on ne prouve pas qu'il s'agit de la même personne de la même manière
dans les trois cas. Chaque clé calcule un rang plutôt que de supprimer
une ligne : rien n'est effacé, tout reste vérifiable. [pause]

Sur les 1 602 lignes de départ, 128 étaient des doublons internes, ce qui
laisse 1 474 lignes uniques. 40 autres existaient déjà dans SPO. Au
final, 1 434 tiers ont été créés — 881 couples, 462 personnes seules,
91 sociétés — sans aucun doublon détecté par ces trois clés.

Une contrainte technique m'a aussi obligée à sortir du simple fichier
d'import : les coordonnées de contact des couples ne passent pas par un
fichier plat dans SPO. J'ai donc construit 872 requêtes automatiques vers
l'interface de programmation, organisées en cinq lots, et les 872 sont
passées sans erreur. Il restait neuf cas trop particuliers pour la chaîne
automatique — des adresses à l'étranger, des natures mal renseignées,
deux doublons avec des adresses différentes — que j'ai traités à la
main.

## SLIDE 6 — Ce que ces deux reprises ont en commun

Ces deux chantiers ont suivi la même méthode, sans que je l'aie vraiment
choisie au départ : on ne peut pas spécifier complètement une reprise
dont on ne connaît pas encore les règles d'acceptation. Du coup, on
avance par paliers, et chaque rejet devient une information sur le
système cible plutôt qu'une simple erreur à corriger. [pause]

Et surtout, ces deux missions répondent à la même question : est-ce que
la donnée est bien arrivée ? C'est ce que j'appelle, dans mon mémoire, le
régime de preuve de la réconciliation — j'y reviendrai à la fin. Il a un
angle mort qu'il faut assumer : ça prouve qu'une donnée est arrivée, pas
qu'elle est juste. Si une clé d'unicité avait été mal choisie dès le
départ, l'erreur serait passée sans être vue.

## SLIDE 7 — Vers le Copilote Financier

Une fois le socle de données reconstitué, on peut se poser une question
différente : qu'est-ce qu'on peut en tirer pour la décision ? [pause]
C'est le second projet de mon année, le Copilote Financier, construit sur
les données réelles de gestion du groupe pour sa direction financière.

## SLIDE 8 — Le Copilote Financier : contexte, données et méthode

La direction financière suivait ses dérives opération par opération, sur
des tableurs, sans vision d'ensemble. Trois questions reviennent tout le
temps en comité d'engagement : quelles opérations dérapent ? à quel
rythme le stock se vend-il ? à quel prix vendre chaque lot ? [pause]

Le point de départ, ce sont quatre exports du système de gestion — une
grille de prix avec les désistements, un export budgétaire poste par
poste, un export de contrôle, un détail des désistements — plus trois
sources externes que je suis allée chercher moi-même : le taux des
crédits à l'habitat publié par la Banque centrale européenne, la
confiance des ménages publiée par Eurostat, et un référentiel des
communes du portefeuille.

J'ai construit un axe pour chacune des trois questions, sur 267
opérations réelles, avec sept programmes d'analyse que j'ai exécutés et
vérifiés un par un. La méthode change volontairement d'un axe à l'autre :
typologie non supervisée, régression et classification, séries
temporelles, optimisation sous contrainte, fouille de texte et analyse de
réseau. [pause] Et sur un échantillon aussi petit, j'ai gardé une règle
tout le long : je ne retiens un résultat que s'il tient en validation
croisée, c'est-à-dire testé sur des données qu'il n'a pas vues à
l'entraînement, jamais sur sa seule performance d'ajustement.

## SLIDE 9 — Exploration des données : deux leçons avant de modéliser

Avant de me lancer dans la modélisation, l'exploration des données m'a
appris deux choses qui ont orienté toute la suite.

D'abord, le prix au mètre carré des appartements est très asymétrique :
quelques lots de standing tirent la distribution vers le haut. [pause]
Une fois passé au logarithme, cette asymétrie devient presque nulle.
C'est ce constat qui m'a fait modéliser le logarithme du prix, et pas le
prix brut, dans l'axe C.

La deuxième leçon, je ne l'avais pas vue venir. La corrélation brute
entre les réservations mensuelles et le taux des crédits était presque
nulle, alors que je savais que ce lien existait vraiment sur ce marché.
En creusant, j'ai compris pourquoi : le nombre d'opérations
commercialisées avait beaucoup augmenté sur la période, et ça brouillait
la relation. Une fois rapportée au nombre d'opérations actives, la
corrélation redevient nette et négative. J'en ai tiré une leçon simple :
toujours vérifier ce que dit vraiment la sortie, pas ce qu'on s'attend à
y trouver. Ça a directement guidé ma démarche pour l'axe B. [pause]

Ces deux leçons en poche, j'ai pu passer à la suite. Mais avant ça, il
fallait que je m'assure d'avoir une base solide sur laquelle m'appuyer.

## SLIDE 10 — La base de données SQL

Les quatre exports Excel, tels quels, n'étaient pas interrogeables
facilement. Je les ai transformés en une base de données SQLite, avec
sept tables et trois vues SQL qui encapsulent les calculs partagés : la
marge par opération, les réservations par mois, l'état du stock. [pause]
L'intérêt d'une vue, c'est qu'elle n'est écrite qu'une seule fois : les
notebooks et la plateforme utilisent tous la même définition, au lieu de
la recopier et risquer de la faire diverger un jour.

Une requête toute simple, un comptage par commune, m'a d'ailleurs donné
un premier signal utile : Le Cap d'Agde concentre à lui seul 117 millions
d'euros de chiffre d'affaires budgété sur seulement deux opérations, un
poids à garder en tête pour l'axe A. [pause]

J'ai aussi voulu vérifier comment cette couche passerait à l'échelle avec
Spark, si le volume grossissait un jour. En chronométrant honnêtement la
même agrégation en pandas et en Spark sur nos données, le verdict est
sans appel : pandas répond en 10 millisecondes, Spark en 577, sans même
compter les 24 secondes de démarrage de sa session. Sur ce volume, Spark
est largement surdimensionné — mais la démonstration prouve que le
chemin de montée en charge existe, si le Copilote devait un jour couvrir
tout le groupe Nexity.

Cette base solidement posée, j'ai pu commencer à construire les trois
axes. Mais avant de m'attaquer au premier, il y a eu encore une étape.

## SLIDE 11 — La typologie : une étape avant l'axe A

En regardant les 267 opérations, je me suis vite heurtée à un problème :
comparer une opération de 2 millions d'euros et une de 50 millions sur
leurs montants bruts, ça n'a pas de sens. C'est la structure de leur
budget qui dit vraiment ce qu'elles sont. [pause]

J'ai donc construit une typologie, en commençant par une analyse en
composantes principales, une méthode qui résume la structure des coûts
en quelques axes : deux axes en résument 61 %, et j'ai vérifié ce
résultat par une seconde méthode de calcul indépendante. En croisant ça
avec une classification non supervisée, j'ai obtenu quatre familles
d'opérations assez nettes : le résidentiel classique, l'aménagement
foncier, la promotion sur foncier allégé, et l'aménagement lourd en VRD.
[pause]

Sur une opération du portefeuille, Le Parc des Cyclades, dont la marge
budgétée était de 6,5 %, ses cinq voisines les plus proches dans cette
typologie affichent des marges entre 7,9 % et 11,3 % — un référentiel
concret. Cette typologie, je m'en suis resservie directement dans l'axe
A, pour situer chaque opération à risque parmi ses semblables.

## SLIDE 12 — Axe A : le risque de marge

Avec cette typologie en poche, j'ai pu m'attaquer à la première vraie
question : le risque de marge. Sur 123 opérations suffisamment avancées,
28 % dépassent déjà leur budget de plus de 2 %, un seuil que j'ai fixé
comme dérive matérielle.

J'ai d'abord essayé une régression directe sur l'ampleur de la dérive :
elle n'explique que 8 % de la variance observée, c'est-à-dire des écarts
d'une opération à l'autre. [pause] Le résultat n'était pas satisfaisant,
donc je suis passée en classification : prédire une classe, « à risque »
ou non. J'ai comparé six méthodes en validation croisée sur la métrique
F1, qui équilibre la détection des cas à risque et les fausses alertes.
Les résultats se tiennent dans un mouchoir de poche, entre 0,26 et 0,34,
sauf un cas qui m'a bien intéressée : un réseau de neurones atteint un F1
de 0,91 sur les données d'entraînement, mais retombe à 0,26 en
validation. C'est exactement la signature du sur-apprentissage sur un
petit échantillon. J'ai finalement gardé une forêt aléatoire, F1 ≈ 0,30
contre 0 pour une référence naïve. [pause]

En complément, une régression Ridge rend les facteurs de dérive
lisibles : les postes techniques pèsent, une marge budgétée confortable
protège. Ce n'est pas un oracle, mais un signal réel, même s'il reste
faible. Une fois cet axe traité, je suis passée à la deuxième question
du cahier des charges : le rythme de vente.

## SLIDE 13 — Axe B : la vitesse d'écoulement

Deuxième axe, la vitesse d'écoulement. C'est celui dont je suis la plus
fière. J'ai construit un panel de plus de 3 200 observations, une ligne
par opération et par mois, et j'ai utilisé un modèle à effets aléatoires.
Il sépare ce qui revient à chaque programme de ce qui revient à la
conjoncture économique.

Ça donne deux choses : les deux tiers de la variance du rythme de vente
tiennent au programme lui-même, un tiers tient à la conjoncture. [pause]
Et l'effet du taux des crédits immobiliers est net : chaque point de
taux en plus fait baisser les réservations mensuelles d'environ 19 %, un
résultat très significatif statistiquement.

J'ai voulu vérifier cet effet autrement, en le testant sur la série
agrégée du groupe dans le temps, avec un modèle de série temporelle plus
exigeant. Et là, l'effet du taux devient indiscernable de zéro. Cent
quatorze mois, ce n'est pas assez pour l'isoler sur une seule série
globale. Ce n'est pas un échec, c'est plutôt rassurant : ça écarte le
risque que mon premier résultat vienne d'une corrélation fallacieuse, un
lien qui semblerait réel sans en être un. [pause] J'ai donc combiné les
deux modèles : la trajectoire vient de la série temporelle, et l'ampleur
de l'effet du taux vient du panel. Avec ça, une détente des taux à 2,5 %
en 2026 redonnerait 6 % de rythme de vente, et une remontée à 3,5 % en
retirerait 3 %.

À l'échelle d'un programme, j'ai aussi ajusté une courbe en S sur les
réservations cumulées. Elle bat un simple ajustement linéaire sur 25 des
28 opérations terminées, avec un délai médian de 20 mois pour vendre 90 %
du potentiel — un repère utile pour la trésorerie.

## SLIDE 14 — Axe C : l'optimisation des prix

Une fois qu'on savait anticiper le rythme de vente, la question qui
s'imposait naturellement, c'était le prix. Troisième axe, les prix : j'ai
construit un modèle dit hédonique : le prix
d'un logement comme somme de caractéristiques valorisées séparément. Sur
plus de 5 000 appartements vendus depuis 2016, il explique 88,6 % de la
variance du prix, avec une erreur d'environ 11 %.

Les primes retrouvées sont plutôt cohérentes : un étage de plus vaut
environ 6 %, et le logement social, dont les prix sont réglementés,
coûte 63 % de moins. [pause] Il y a aussi un effet millésime : les prix
ont augmenté d'environ 19 % entre 2016 et 2023, avec un plateau après
2022. Les prix du neuf n'ont pas baissé avec la remontée des taux, c'est
plutôt le volume de ventes qui s'est ajusté, comme on l'a vu dans l'axe
B.

Appliqué au stock, ce modèle signale 24 lots sur 127 qui sont hors
marché.

La partie qui m'a le plus intéressée, c'est la recommandation de remise.
J'ai dû fixer la sensibilité de la demande au prix, ce qu'on appelle
l'élasticité, parce que mon estimation interne n'était pas assez précise
pour être fiable. Pour résoudre le problème d'optimisation, j'ai utilisé
la méthode du multiplicateur de Lagrange, une technique qui trouve le
meilleur compromis sous contrainte, puis j'ai vérifié la solution avec un
second algorithme indépendant : les deux convergent à moins d'un centième
près. [pause] Et le résultat est plutôt surprenant : la remise optimale,
c'est un montant identique en euros sur tous les lots, donc un
pourcentage plus fort sur les petits lots. Sur une opération test,
Arpeggio, viser 8 % d'accélération des ventes donne des ajustements
individuels de -5 % à -14 % selon le prix du lot, pour un même montant
constant d'environ 23 000 euros. C'est l'inverse de ce qui se fait
aujourd'hui, au cas par cas.

## SLIDE 15 — Signaux faibles : texte et réseau de vente

Une fois ces trois axes posés, j'ai voulu voir si je pouvais aller
chercher un signal en plus, là où personne ne regardait : dans le texte
et dans le réseau commercial. C'est l'axe transverse, qui exploite ce que
les champs structurés ne captent pas : 9 688 commentaires libres de
vente, et le réseau des vendeurs.

Sur le texte, j'ai construit un moteur de recherche par similarité, avec
une méthode qu'on appelle TF-IDF : elle pondère chaque mot selon sa
fréquence et sa rareté dans le corpus. Une requête comme « refus de prêt
banque » retrouve directement les dossiers concernés. [pause]

J'ai aussi essayé de prédire le désistement à partir du commentaire seul,
avec un contrôle de fuite serré — j'ai écarté les 314 commentaires qui
nomment déjà l'annulation. Sur ce qui reste, un modèle probabiliste
simple atteint un F1 de 0,34, mieux qu'une régression logistique qui est
plus précise mais presque muette. Le signal est là, mais il reste un
appoint, pas un prédicteur autonome.

Sur les motifs de désistement, une mesure d'écart entre distributions m'a
montré qu'une agence a un profil vraiment atypique : 90 % de ses
désistements sont classés en « autres motifs ». En creusant, j'ai compris
que ce n'est pas un comportement client, c'est un défaut de saisie — une
recommandation opérationnelle très concrète pour le coup. [pause]

Enfin, j'ai construit le réseau des vendeurs et des opérations : 209
vendeurs avec au moins trois dossiers, ce qui couvre 98,8 % des dossiers
attribués, reliés à 104 opérations par 711 liens. Deux acteurs — le
réseau de vente interne, et un prescripteur externe — portent à eux deux
51,6 % des dossiers attribués, avec des taux de désistement très
différents, 9 % pour l'un, 30 % pour l'autre. C'est une dépendance
commerciale à surveiller.

## SLIDE 16 — La plateforme : cinq pages pour la direction financière

Tout ce travail, du risque de marge au réseau de vente, se retrouve dans
une application que la direction financière utilise elle-même, cinq
pages testées une par une.

Vue d'ensemble donne la situation du portefeuille en un coup d'œil.
Alertes marge classe les opérations en cours par niveau de risque — sur
68 opérations suffisamment avancées, 10 sont en alerte. [pause]

Rythme de vente transforme mon modèle en simulateur : un curseur sur le
taux de crédit 2026 donne directement le rythme attendu. Pilotage des
prix affiche les lots hors marché et propose une grille ajustée. Qualité
commerciale signale l'agence au défaut de saisie que j'ai trouvé plus
tôt, et permet de retrouver des dossiers similaires par une recherche en
langage courant.

Un point que je voudrais souligner : la première version de la
plateforme parlait le vocabulaire des statistiques — F1, R²,
coefficients. Le commanditaire me l'a dit franchement : c'était trop
technique pour ses utilisateurs. Je l'ai reconstruite en langage métier,
et cette leçon compte autant à mes yeux que les résultats eux-mêmes.

## SLIDE 17 — Réflexion transversale

Je termine sur ce que cette année a changé dans l'idée que je me faisais
de ce métier.

Je pensais que j'allais surtout être une modélisatrice. En réalité, j'ai
été avant tout une traductrice, dans les deux sens : traduire une gêne
métier en question calculable, puis traduire un résultat statistique en
information sur laquelle on peut décider. [pause]

Deuxième chose que j'ai comprise : une reprise de données, un tableau de
bord, et un modèle statistique ne se prouvent pas de la même façon. Une
reprise se prouve par réconciliation — est-ce que la donnée est bien
arrivée ? En marge des deux reprises, j'ai aussi maintenu les tableaux de
bord existants et participé au déploiement du SSO, l'authentification
unique, sur deux périmètres du groupe. Ces missions-là se prouvent
autrement, par l'usage : est-ce que la personne s'en sert, et pour la
bonne chose ? Et un modèle se prouve par la validation statistique :
est-ce que le résultat tient en dehors de l'échantillon qui a servi à le
construire ? Confondre ces régimes de preuve, ce serait la vraie erreur
méthodologique. [pause]

Une dernière chose que j'ai apprise : documenter, ce n'est pas une
formalité qui vient après le travail, c'est un vrai acte technique. La
note que j'avais écrite sur la séquence d'injection de SPO m'a resservi
deux mois plus tard pour la reprise des tiers, presque telle quelle.

## SLIDE 18 — Perspectives et projet professionnel

J'ai commencé ce master en visant la modélisation prédictive au sens
strict. J'en sors avec un projet un peu plus large : construire et
fiabiliser les chaînes de données qui rendent une décision possible, puis
les mettre en forme jusqu'à l'écran. [pause]

Ça veut dire tenir ensemble trois compétences : l'ingénierie des données,
sur laquelle j'ai le plus progressé cette année ; une modélisation
proportionnée à la donnée réellement disponible ; et le dialogue avec les
métiers, qui décide au final si un livrable sert vraiment à quelque
chose.

À court terme, je vise un poste d'ingénieure données orientée aide à la
décision, où je pourrais continuer à tenir toute cette chaîne, ou une
direction data plus structurée, où je travaillerais enfin à plusieurs sur
un même sujet.

## SLIDE 19 — Conclusion

Pour conclure, cette année a été dominée par la reconstruction d'un socle
de données, avant de revenir, au second semestre, à la modélisation
statistique.

Un projet de données ne se joue pas au moment de choisir un algorithme.
Ça se joue avant, quand on décide ce qu'est un client, ce qu'est une
marge. Structurer une donnée et la modéliser, ce ne sont pas deux métiers
séparés : ce sont deux moments du même travail. [pause]

Je vous remercie de votre attention, et je suis prête à répondre à vos
questions.
