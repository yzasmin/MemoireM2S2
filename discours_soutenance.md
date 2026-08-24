# Discours de soutenance — texte mot à mot

Calibré pour 15 minutes à l'oral (~130-140 mots/minute). Les indications
`[pause]` marquent un silence court, volontaire. Une entrée = une slide de
`plan_slides.md` : le découpage est identique dans les deux fichiers.

**Répartition volontaire : environ 30 % du temps sur les deux reprises de
données (mes missions d'alternance), 70 % sur le Copilote Financier — le
projet de data science proprement dit.**

---

## SLIDE 1 — Titre

Bonjour à toutes et à tous. Je m'appelle Yasmina Saoud, je suis en deuxième
année de Master MIASHS, en alternance au sein du groupe Angelotti.

Mon année a été dominée par deux chantiers : une reprise de données vers
un nouvel ERP, puis un projet de data science, le Copilote Financier.
Je vais présenter le premier rapidement, pour consacrer l'essentiel de mon
temps au second — c'est là qu'est la vraie matière statistique. [pause]

Commençons par le contexte.

## SLIDE 2 — Contexte Angelotti et migration des opérations

Le groupe Angelotti est un promoteur-aménageur immobilier, filiale de
Nexity. Deux métiers : la promotion, qui construit et vend des logements
neufs, et l'aménagement, qui viabilise des terrains à bâtir. Chaque
opération est portée par une société dédiée, avec un budget qui dérive au
fil du chantier et des ventes.

Cette année, un seul événement a structuré mon premier semestre : le
remplacement de l'ERP historique, Grimmo, par un nouveau système, SPO.
[pause] Un ERP, c'est le logiciel qui centralise la gestion d'une
entreprise. Changer d'ERP, ce n'est pas changer d'outil : c'est changer de
modèle de données. 283 opérations devaient y être recréées, à une échelle
qui excluait la saisie manuelle. J'ai automatisé l'essentiel via des
interfaces de programmation, en découvrant au passage deux règles non
documentées, en analysant les erreurs renvoyées par le système — un ordre
d'injection strict, et des identifiants qui changent à chaque mise à jour.
Le processus a été sécurisé par une validation par paliers : trois
opérations pilotes, puis un lot de douze, avant la migration de masse,
pour que les erreurs restent lisibles. Pour ne pas interrompre la
facturation, nous avons déployé la structure d'abord, le détail
budgétaire ensuite. À la fin du semestre, les 283 opérations existaient
dans SPO.

## SLIDE 3 — La reprise des tiers

Au second semestre, j'ai reconstitué le référentiel client — ce que SPO
appelle un « tiers ». Matière première : 1 602 lignes de coordonnées
d'acquéreurs, issues du CRM, le logiciel qui gère la relation commerciale.
Le piège : une ligne décrit un achat, pas un
client, donc un client fidèle apparaît plusieurs fois. Et SPO n'était pas
vide : environ 13 000 tiers y existaient déjà. [pause]

L'enjeu tenait en une phrase : créer chaque client une fois, sans le
vérifier à la main. J'ai construit un fichier piloté par formules, dont le
cœur est trois clés d'unicité différentes selon le type de client — un
couple, une personne seule, ou une société — parce qu'on ne prouve pas
l'identité de la même façon dans les trois cas. Chaque clé calcule un
rang plutôt que de supprimer une ligne : rien n'est effacé, tout reste
vérifiable, et je peux toujours dire pourquoi une ligne n'a pas été
importée. [pause]

Résultat : sur 1 602 lignes, 128 étaient des doublons internes, ce qui
laisse 1 474 lignes uniques ; 40 autres existaient déjà dans SPO. 1 434
tiers ont finalement été créés — 881 couples, 462 personnes seules, 91
sociétés — sans aucun doublon détecté. Une contrainte technique m'a
obligée à sortir du simple fichier d'import : les coordonnées de contact
des couples ne peuvent pas passer par un fichier plat dans SPO. J'ai donc
construit 872 requêtes automatiques vers l'interface de programmation de
SPO, organisées en cinq lots, et les 872 sont passées sans erreur.

## SLIDE 4 — Vers le Copilote Financier

Ces deux reprises répondent à une question : la donnée est-elle bien
arrivée ? Le socle reconstitué permet de se poser une question différente :
que peut-on en tirer pour la décision ? [pause] C'est le second projet de
mon année, le Copilote Financier, construit sur les données réelles de
gestion du groupe pour sa direction financière.

## SLIDE 5 — Le Copilote Financier : contexte, données et méthode

La direction financière suivait ses dérives opération par opération, sur
tableurs, sans vision d'ensemble. Trois questions structurent le projet :
quelles opérations dérapent ? À quel rythme le stock se vend-il ? À quel
prix vendre chaque lot ? [pause]

J'ai construit un axe pour chacune, sur 267 opérations réelles et sept
programmes d'analyse exécutés et vérifiés un par un. La méthode change
volontairement d'un axe à l'autre : typologie non supervisée, régression
et classification, séries temporelles, optimisation sous contrainte,
fouille de texte et analyse de réseau. [pause] Sur un échantillon aussi
restreint, une règle traverse tout le projet : je ne retiens un résultat
que s'il tient en validation croisée — c'est-à-dire testé sur des données
qu'il n'a pas vues à l'entraînement — jamais sur sa seule performance
d'ajustement. Je vous donne maintenant les résultats, avec la même
honnêteté que dans le mémoire : ils ne se valent pas tous.

## SLIDE 6 — Exploration des données : deux leçons avant de modéliser

Avant de modéliser, l'exploration des données a produit deux résultats qui
ont orienté toute la suite.

Le prix au mètre carré des appartements est très asymétrique : quelques
lots de standing tirent la distribution vers le haut. [pause] Après
passage au logarithme, cette asymétrie devient quasi nulle — c'est ce
constat qui a orienté l'axe C à modéliser le logarithme du prix plutôt que
le prix brut.

La deuxième leçon, je ne l'ai pas vue venir. La corrélation brute entre
les réservations mensuelles et le taux des crédits était presque nulle,
alors que je savais ce lien réel sur ce marché. En creusant, la cause
était ailleurs : le nombre d'opérations commercialisées avait fortement
augmenté sur la période, ce qui maquillait la relation. Rapportée au
nombre d'opérations actives, la corrélation redevient nette et négative.
Cette leçon — toujours vérifier la sortie réelle plutôt que la conclusion
attendue — a directement structuré la démarche de l'axe B.

## SLIDE 7 — Axe A : le risque de marge

Premier axe. Sur 123 opérations suffisamment avancées, 28 % dépassent déjà
leur budget de plus de 2 %, un seuil que j'ai fixé comme dérive
matérielle.

Une régression directe de l'ampleur de la dérive n'explique que 8 % de la
variance observée — c'est-à-dire des écarts d'une opération à l'autre.
[pause] J'ai donc basculé en classification : prédire une classe, « à
risque » ou non. J'ai comparé six méthodes en validation croisée sur la
métrique F1, qui équilibre détection des cas à risque et fausses alertes.
Les résultats se tiennent en un mouchoir de poche, entre 0,26 et 0,34,
sauf un cas instructif : un réseau de neurones atteint un F1 de 0,91 sur
les données d'entraînement, mais retombe à 0,26 en validation — la
signature exacte du sur-apprentissage sur un petit échantillon. J'ai
retenu une forêt aléatoire, F1 ≈ 0,30 contre 0 pour une référence naïve.

En complément, une régression Ridge rend les facteurs de dérive lisibles :
les postes techniques pèsent, une marge budgétée confortable protège. Et
une analyse en composantes principales — une méthode qui résume la
structure des coûts en quelques axes — montre que deux axes en résument
61 %, résultat vérifié par une seconde méthode de calcul indépendante.
Elle fonde une typologie de quatre familles d'opérations, qui permet de
comparer chaque opération à ses « voisines » les plus proches. Je
l'assume : ce n'est pas un oracle, c'est un signal réel mais faible.

## SLIDE 8 — Axe B : la vitesse d'écoulement

Deuxième axe, la vitesse d'écoulement — c'est l'axe le plus solide de mon
travail. J'ai construit un panel de plus
de 3 200 observations, une ligne par opération et par mois. J'ai utilisé
un modèle à effets aléatoires. Il sépare ce qui revient à chaque programme
de ce qui revient à la conjoncture économique.

Résultat : deux tiers de la variance du rythme de vente tiennent au
programme lui-même. Un tiers tient à la conjoncture. [pause] Et l'effet du
taux des crédits immobiliers est net : chaque point de taux en plus fait
baisser les réservations mensuelles d'environ 19 %, un résultat très
significatif statistiquement.

J'ai aussi testé cet effet sur la série agrégée du groupe dans le temps,
avec un modèle de série temporelle plus exigeant. Là, l'effet du taux
devient indiscernable de zéro. Cent quatorze mois ne suffisent pas à
l'isoler sur une série globale. C'est une bonne nouvelle méthodologique :
cela écarte le risque que mon premier résultat soit une corrélation
fallacieuse — un lien qui semblerait réel sans en être un. J'ai donc
combiné les deux modèles : la trajectoire vient de la série temporelle,
l'ampleur de l'effet du taux vient du panel. Sous ce scénario, une
détente des taux à 2,5 % en 2026 redonnerait 6 % de rythme de vente ; une
remontée à 3,5 % en retirerait 3 %.

À l'échelle d'un programme, une courbe en S ajustée sur les réservations
cumulées bat un ajustement linéaire sur 25 des 28 opérations terminées :
délai médian de 20 mois pour vendre 90 % du potentiel, un repère utile à
la trésorerie.

## SLIDE 9 — Axe C : l'optimisation des prix

Troisième axe, les prix. J'ai construit un modèle dit hédonique : le prix
d'un logement comme somme de caractéristiques valorisées séparément. Sur
plus de 5 000 appartements vendus depuis 2016, il explique 88,6 % de la
variance du prix, avec une erreur d'environ 11 %. Les primes retrouvées
sont cohérentes : un étage de plus vaut environ 6 %, le logement social,
aux prix réglementés, coûte 63 % de moins. [pause]

Appliqué au stock, ce modèle signale 24 lots sur 127 hors marché.

La partie la plus intéressante, c'est la recommandation de remise. J'ai dû
fixer la sensibilité de la demande au prix, ce qu'on appelle l'élasticité,
car mon estimation interne n'était pas assez précise pour être fiable. En
résolvant le problème d'optimisation par la méthode du multiplicateur de
Lagrange — une technique qui trouve le meilleur compromis sous contrainte
— puis en vérifiant la solution par un second algorithme indépendant, les
deux convergent à moins d'un centième près. Le résultat est
contre-intuitif : la remise optimale est un montant identique en euros
sur tous les lots, donc un pourcentage plus fort sur les petits lots — à
l'inverse de la pratique actuelle au cas par cas.

## SLIDE 10 — Signaux faibles : texte et réseau de vente

Un axe transverse exploite ce que les champs structurés ne captent pas :
9 688 commentaires libres de vente, et le réseau des vendeurs.

Sur le texte, j'ai construit un moteur de recherche par similarité : une
requête comme « refus de prêt banque » retrouve directement les dossiers
concernés. [pause] J'ai aussi tenté de prédire le désistement à partir du
seul commentaire, avec un contrôle de fuite serré — j'ai écarté les 314
commentaires qui nomment déjà l'annulation. Sur le corpus restant, un
modèle probabiliste simple atteint un F1 de 0,34, mieux qu'une régression
logistique plus précise mais presque muette. Le signal existe, mais reste
un appoint, pas un prédicteur autonome.

Sur les motifs de désistement, une mesure d'écart entre distributions a
révélé qu'une agence a un profil très atypique : 90 % de ses désistements
sont classés « autres motifs ». Ce n'est pas un comportement client, c'est
un défaut de saisie — une vraie recommandation opérationnelle.

Enfin, le réseau des vendeurs et des opérations montre une concentration
forte : deux acteurs portent 51,6 % des dossiers attribués, avec des taux
de désistement très différents, 9 % pour l'un, 30 % pour l'autre — une
dépendance commerciale à surveiller.

## SLIDE 11 — La plateforme : cinq pages pour la direction financière

Tout ce travail, du risque de marge au réseau de vente, alimente une
application que la direction financière utilise elle-même, cinq pages
testées une par une.

Vue d'ensemble donne la situation du portefeuille en un coup d'œil.
Alertes marge classe les opérations en cours par niveau de risque — sur
68 opérations suffisamment avancées, 10 sont en alerte. [pause]

Rythme de vente transforme mon modèle en simulateur : un curseur sur le
taux de crédit 2026 donne directement le rythme attendu. Pilotage des
prix affiche les lots hors marché et propose une grille ajustée. Qualité
commerciale signale l'agence au défaut de saisie identifié plus tôt, et
permet de retrouver des dossiers similaires par une recherche en langage
courant.

Précision importante : la première version parlait le vocabulaire des
statistiques — F1, R², coefficients — trop technique pour ses
utilisateurs, m'a dit le commanditaire. Je l'ai reconstruite en langage
métier, une leçon qui compte autant que les résultats eux-mêmes.

## SLIDE 12 — Réflexion transversale

Je termine sur ce que cette année a changé dans l'idée que je me faisais
de ce métier.

Je m'attendais à être d'abord une modélisatrice. En réalité, j'ai surtout
été une traductrice, dans les deux sens : traduire une gêne métier en
question calculable, puis un résultat statistique en information sur
laquelle décider. [pause]

Deuxième leçon : une reprise de données et un modèle statistique ne se
prouvent pas de la même façon. Une reprise se prouve par réconciliation —
la donnée est-elle bien arrivée ? Un modèle se prouve par la validation
statistique — le résultat tient-il en dehors de l'échantillon qui a servi
à le construire ? Confondre ces deux régimes de preuve serait la vraie
erreur méthodologique.

## SLIDE 13 — Perspectives et projet professionnel

J'ai commencé ce master en visant la modélisation prédictive au sens
strict. J'en sors avec un projet plus large : construire et fiabiliser
les chaînes de données qui rendent une décision possible, puis les
outiller jusqu'à l'écran. [pause]

À court terme, je vise un poste d'ingénieure données orientée aide à la
décision, où je pourrai continuer à tenir toute cette chaîne, ou une
direction data structurée où je travaillerai enfin à plusieurs sur un même
chantier.

## SLIDE 14 — Conclusion

Pour conclure : cette année a été dominée par la reconstruction d'un
socle de données, avant de revenir, au second semestre, à la
modélisation statistique.

Un projet de données ne se joue pas au moment de choisir un algorithme. Il
se joue avant, quand on décide ce qu'est un client, ce qu'est une marge.
Structurer une donnée et la modéliser ne sont pas deux métiers séparés :
ce sont deux moments du même travail. [pause]

Je vous remercie de votre attention, et je suis prête à répondre à vos
questions.
