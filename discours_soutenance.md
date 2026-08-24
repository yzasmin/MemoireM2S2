# Discours de soutenance — texte mot à mot

Calibré pour 15 minutes à l'oral (~130-140 mots/minute). Les indications
`[pause]` marquent un silence court, volontaire. Une entrée = une slide de
`plan_slides.md` : le découpage est identique dans les deux fichiers.

---

## SLIDE 1 — Titre

Bonjour à toutes et à tous. Je m'appelle Yasmina Saoud, je suis en deuxième
année de Master MIASHS, en alternance au sein du groupe Angelotti.

Mon mémoire couvre deux missions. La première, une reprise de données vers
un nouvel ERP. La seconde, un projet de data science : le Copilote
Financier. [pause]

Je vais d'abord vous présenter le contexte, puis les deux reprises de
données, puis le Copilote Financier et ses résultats, avant de conclure sur
ce que cette année m'a appris du métier. Commençons par le contexte.

## SLIDE 2 — Contexte Angelotti et enjeu de l'année

Le groupe Angelotti est un promoteur-aménageur immobilier, implanté en
Occitanie et en région PACA, filiale du groupe Nexity. Deux métiers : la
promotion, qui construit et vend des logements neufs, et l'aménagement, qui
viabilise des terrains à bâtir.

Chaque opération immobilière est portée par une société dédiée. Un budget
est posé au démarrage, puis la vie de l'opération le fait dériver : appels
d'offres plus chers que prévu, ventes plus lentes, désistements de clients.

Cette année a été dominée par un seul événement : le remplacement de l'ERP
historique, Grimmo, par un nouveau système, SPO. [pause] Un ERP, c'est le
logiciel qui centralise toute la gestion d'une entreprise. Changer d'ERP,
ce n'est pas changer d'outil : c'est changer de modèle de données. Les
objets ne portent plus les mêmes noms, ne s'articulent plus de la même
façon. C'est ce chantier qui a structuré tout mon premier semestre.

## SLIDE 3 — La migration des opérations

283 opérations immobilières devaient être recréées dans SPO. Une saisie
manuelle était exclue à cette échelle.

Nous avons automatisé l'essentiel via les interfaces de programmation de
l'éditeur, et j'ai traité à la main les seuls cas trop particuliers pour un
gabarit automatique. [pause]

Deux règles de SPO n'étaient documentées nulle part, et je les ai
découvertes en analysant les erreurs renvoyées par le système. La première :
un ordre d'injection strict — l'opération, puis ses tranches de travaux,
puis ses tranches commerciales, puis son budget. La seconde : les
identifiants ne sont jamais stables. Ils changent à chaque mise à jour.
J'ai donc dû toujours aller chercher la version la plus récente avant
d'agir.

Les utilisateurs devaient pouvoir facturer dès le basculement. Nous avons
donc déployé des « coquilles vides » : la structure d'abord, le détail
budgétaire ensuite. À la fin du semestre, les 283 opérations existaient
dans SPO. C'est ce socle qui a permis d'attaquer la seconde reprise.

## SLIDE 4 — La reprise des tiers : le problème du doublon

Au second semestre, j'ai reconstitué le référentiel client. Dans SPO, un
client s'appelle un « tiers ».

Ma matière première : deux extractions du CRM — le logiciel qui gère la
relation commerciale —, l'une de 1 557 ventes, l'autre de 1 602 lignes de
coordonnées d'acquéreurs. [pause] Le piège : une ligne ne décrit pas un
client, elle décrit un achat. Un client fidèle qui a acheté trois lots
apparaît trois fois. Et SPO n'était pas vide : environ 13 000 tiers y
existaient déjà.

L'enjeu tenait donc en une phrase : créer chaque client une fois, et une
seule fois, sans le vérifier ligne par ligne à la main. À ce volume, cela
aurait pris trop de temps et généré trop d'erreurs.

## SLIDE 5 — La reprise des tiers : la solution et les résultats

J'ai construit un fichier de travail entièrement piloté par formules, qui
calcule la décision d'importer chaque ligne plutôt que de la laisser à
mon jugement.

Le cœur du dispositif, ce sont trois clés d'unicité différentes selon la
nature du client : couple, personne seule, ou société. On ne prouve pas
qu'il s'agit de la même personne de la même façon dans les trois cas.
[pause]

Le résultat : sur 1 602 lignes de départ, 128 étaient des doublons
internes, ce qui laisse 1 474 lignes uniques. 40 autres existaient déjà
dans SPO. 1 434 tiers ont finalement été créés —
881 couples, 462 personnes seules, 91 sociétés — sans aucun doublon détecté
par ces trois clés.

Une contrainte technique m'a obligée à sortir du simple fichier d'import :
les coordonnées de contact des couples ne peuvent pas passer par un fichier
plat. J'ai donc construit 872 requêtes automatiques vers l'interface de
programmation de SPO, et les 872 sont passées sans erreur.

## SLIDE 6 — Vers le Copilote Financier

Ces deux reprises ont reconstruit le socle de données du groupe. Elles
répondent à une question simple : est-ce que la donnée est bien arrivée ?

Le second semestre m'a permis de me poser une question différente : que
peut-on maintenant en tirer ? [pause] C'est le second projet de mon année,
le Copilote Financier, un outil d'aide à la décision pour la direction
financière, construit sur les données réelles de gestion du groupe.

## SLIDE 7 — Le Copilote Financier : contexte et trois axes

La direction financière suivait ses dérives opération par opération, dans
des tableurs, sans vision d'ensemble. Trois questions revenaient sans
cesse. Quelles opérations dérapent financièrement ? À quel rythme le stock
va-t-il se vendre ? À quel prix vendre chaque lot ?

J'ai construit un axe pour chacune. [pause] L'axe A prédit le risque de
dérive de marge. L'axe B prévoit le rythme de réservation, notamment sous
l'effet des taux d'intérêt. L'axe C recommande des ajustements de prix.
Le tout est adossé à 267 opérations réelles et sept programmes d'analyse
— des notebooks — exécutés, que j'ai vérifiés un par un.

Je vais maintenant vous donner les résultats de chaque axe, avec la même
honnêteté que dans le mémoire : ils ne se valent pas tous.

## SLIDE 8 — Axe A : le risque de marge

Premier axe, le risque de marge. Sur 123 opérations suffisamment avancées
— au moins 60 % d'engagement — 28 % dépassent déjà leur budget de plus de
2 %, un seuil que j'ai fixé comme dérive matérielle. Deux cas extrêmes
dépassent la moitié de leur marge budgétée.

J'ai d'abord tenté une régression, pour prédire directement l'ampleur de la
dérive : elle n'explique que 8 % de la variance observée — c'est-à-dire des
écarts de dérive d'une opération à l'autre. [pause] Le résultat est
modeste, donc j'ai changé d'angle : plutôt que prédire un montant, prédire
une classe, « à risque » ou non. En classification, la métrique adaptée à
un problème déséquilibré s'appelle le F1. C'est une moyenne entre deux
choses : la capacité à détecter les cas à risque, et la capacité à ne pas
se tromper quand on en signale un. Avec une forêt aléatoire, j'obtiens un
F1 d'environ 0,30, contre 0 pour un modèle qui ne détecterait jamais rien.

Je l'assume : ce n'est pas un oracle, c'est un signal réel mais faible. La
structure initiale du budget prédispose à la dérive, elle ne la
détermine pas — l'aléa de chantier, lui, n'est pas dans mes données.

## SLIDE 9 — Axe B : la vitesse d'écoulement

C'est l'axe le plus solide de mon travail. J'ai construit un panel de plus
de 3 200 observations, une ligne par opération et par mois. J'ai utilisé un
modèle à effets aléatoires. Il sépare ce qui revient à chaque programme de
ce qui revient à la conjoncture économique.

Résultat : deux tiers de la variance du rythme de vente tiennent au
programme lui-même — son emplacement, son prix. Un tiers tient à la
conjoncture. [pause] Et l'effet du taux des crédits immobiliers est net :
chaque point de taux en plus fait baisser les réservations mensuelles
d'environ 19 %, un résultat très significatif statistiquement.

J'ai aussi testé cet effet sur la série agrégée du groupe dans le temps,
avec un modèle de série temporelle plus exigeant. Là, l'effet du taux
devient indiscernable de zéro. Je ne le cache pas : cent quatorze mois ne
suffisent pas à l'isoler sur une série globale. Mais c'est une bonne
nouvelle méthodologique : cela écarte le risque que mon premier résultat
soit une corrélation fallacieuse — un lien qui semblerait réel sans en
être un. J'ai donc combiné les deux modèles :
la trajectoire vient de la série temporelle, l'ampleur de l'effet du taux
vient du panel. Sous ce scénario, une détente des taux à 2,5 % en 2026
redonnerait 6 % de rythme de vente ; une remontée à 3,5 % en retirerait 3 %.

## SLIDE 10 — Axe C : l'optimisation des prix

Troisième axe, les prix. J'ai construit un modèle dit hédonique : le prix
d'un logement comme somme de caractéristiques valorisées séparément —
surface, étage, exposition, commune, année. Sur plus de 5 000 appartements vendus depuis
2016, ce modèle explique 88,6 % de la variance du prix, avec une erreur
d'environ 11 %.

Appliqué au stock actuel, il signale 24 lots sur 127 hors marché : 16
sous-cotés, 8 surcotés. [pause]

La partie la plus intéressante, c'est la recommandation de remise. J'ai dû
fixer la sensibilité de la demande au prix, ce qu'on appelle l'élasticité.
Mon estimation interne n'était pas assez précise pour être fiable — je le
dis clairement plutôt que de le cacher. J'ai retenu une valeur
prudente, cohérente avec la littérature du secteur. En résolvant le
problème d'optimisation qui en découle, un résultat contre-intuitif
apparaît : la remise optimale n'est pas un pourcentage identique sur tous
les lots, c'est un montant en euros identique. Concrètement, cela veut dire
un pourcentage de remise plus fort sur les petits lots — l'inverse de ce
qui se pratique aujourd'hui au cas par cas.

## SLIDE 11 — La plateforme : cinq pages pour la direction financière

Ce travail ne reste pas dans des notebooks : il alimente une application
que la direction financière utilise elle-même, cinq pages, testées une par
une.

Vue d'ensemble donne la situation du portefeuille en un coup d'œil : 147
opérations de promotion suivies, 421 lots en stock, le rythme de vente
récent. Alertes marge classe les opérations en cours par niveau de risque
— sur 68 opérations suffisamment avancées, 10 sont en alerte. [pause]

Rythme de vente transforme mon modèle en simulateur : un curseur sur le
taux de crédit 2026 donne directement le rythme attendu. Pilotage des
prix affiche les lots hors marché et propose une grille ajustée. Qualité
commerciale signale un problème que j'ai découvert par les données : une
agence enregistre 90 % de ses désistements sous « autres motifs » — un
défaut de saisie plutôt qu'un vrai profil de clientèle. Cette page permet
aussi de retrouver des dossiers similaires par une recherche en langage
courant.

Une précision importante : la première version de cette plateforme
parlait le langage des notebooks, F1, R², coefficients. Le commanditaire
me l'a clairement signalé : trop technique pour ses utilisateurs. Je l'ai
reconstruite en langage métier. Cette leçon compte autant que les
résultats eux-mêmes.

## SLIDE 12 — Réflexion transversale

Je termine sur ce que cette année a changé dans l'idée que je me faisais de
ce métier.

Je m'attendais à être d'abord une modélisatrice : recevoir une donnée et une
question, choisir une méthode, livrer un modèle. En réalité, sur mes quatre
missions, une seule y ressemble vraiment. [pause] J'ai surtout été une
traductrice, dans les deux sens : traduire une gêne exprimée par un service
en question calculable, puis traduire un résultat statistique en
information sur laquelle quelqu'un peut agir.

Deuxième leçon : une reprise de données, un tableau de bord et un modèle
statistique ne se prouvent pas de la même façon. Une reprise se prouve par
réconciliation — la donnée est-elle bien arrivée ? Un reporting se prouve
par l'usage — la personne s'en sert-elle vraiment ? Un modèle se prouve par
la validation statistique — le résultat tient-il en dehors de l'échantillon
qui a servi à le construire ? Confondre ces trois régimes de preuve, c'est
le risque méthodologique que j'ai appris à éviter cette année.

## SLIDE 13 — Perspectives et projet professionnel

J'ai commencé ce master en visant la modélisation prédictive au sens
strict. J'en sors avec un projet plus large : construire et fiabiliser les
chaînes de données qui rendent une décision possible, puis les outiller
jusqu'à l'écran.

Cela suppose de tenir ensemble trois compétences : l'ingénierie des
données, sur laquelle j'ai le plus progressé cette année ; une modélisation
proportionnée à la donnée réellement disponible ; et le dialogue avec les
métiers, qui décide si un livrable sert vraiment. [pause]

À court terme, je vise un poste d'ingénieure données orientée aide à la
décision, où je pourrai continuer à tenir toute cette chaîne, ou une
direction data structurée où je travaillerai enfin à plusieurs sur un même
chantier.

## SLIDE 14 — Conclusion

Cette année a été dominée par la reconstruction d'un socle de données,
avant de revenir, au second semestre, à la modélisation statistique.

Un projet de données ne se joue pas au moment de choisir un algorithme. Il
se joue avant, quand on décide ce qu'est un client, ce qu'est une marge, ou
ce que contient vraiment un fichier dont le nom annonce autre chose.
Structurer une donnée et la modéliser ne sont pas deux métiers séparés :
ce sont deux moments du même travail, et c'est le premier qui décide de ce
que le second peut en tirer. [pause]

Je vous remercie de votre attention, et je suis prête à répondre à vos
questions.
