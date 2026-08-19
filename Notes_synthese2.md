# Notes de synthèse — mémoire de fin d'études couvrant l'année de M2

Fichier de travail de la seconde phase, celle où les deux chapitres rédigés séparément sont
devenus un mémoire complet reprenant l'année entière. Une entrée par sujet, avec un résumé
d'une ligne. Le fichier `Notes_synthese.md` reste le journal de la première phase ; il n'est
pas dupliqué ici, seules les entrées qui ont changé sont reprises.

---

## 1. La structure retenue, et pourquoi

**Résumé en une ligne.** Sept chapitres dans l'ordre chronologique des missions, encadrés par
un appareil complet de mémoire, et une lecture transversale en fin de volume pour répondre
aux exigences de l'école.

Le mémoire n'est plus un volume distinct du mi-parcours : il l'intègre. Cela impose trois
choses que la première version ne faisait pas. Le mi-parcours n'est plus cité comme un
document extérieur, mais comme les chapitres 2 et 4 du même manuscrit. Les figures ont été
renumérotées. Et la conclusion générale, qui fermait le chapitre du Copilote Financier, a
migré en fin de volume.

| Partie | Contenu | Origine |
|:---|:---|:---|
| Préambule | Remerciements, résumé, glossaire, table des matières, table des figures | Rédigé pour cette version, en reprenant la structure du mi-parcours |
| Introduction | Contexte général, thèse, annonce du plan | Rédigée, à partir de l'introduction du mi-parcours |
| Chapitre 1 | Contexte de l'alternance, métier et data | Nouveau |
| Chapitre 2 | La migration vers SPO, premier semestre | Repris du mi-parcours, chapitre 1, et développé |
| Chapitre 3 | La reprise des tiers, second semestre | Rédigé en première phase, transposé |
| Chapitre 4 | Reporting et missions SI transverses | Repris du mi-parcours, chapitre 2, et développé |
| Chapitre 5 | Le Copilote Financier | Rédigé en première phase, transposé |
| Chapitre 6 | Conduite de projet, technologies, évaluation, difficultés | Nouveau |
| Chapitre 7 | Réflexion sur le métier, perspectives, projet professionnel | Nouveau |
| Conclusion | Bilan de l'année et retour sur la thèse | Nouvelle, reprenant la conclusion du mi-parcours sans la répéter |

**L'ordre des chapitres 3 et 4 est un choix, et il mérite d'être défendu à l'oral.**
Chronologiquement, les missions filées du chapitre 4 courent sur les deux semestres et
auraient pu venir juste après le chapitre 2. Je les ai placées après la reprise des tiers
pour garder ensemble les deux chantiers de reprise, qui sont le même travail, et parce que
le chapitre 4 amène naturellement le chapitre 5 : la règle de facturation juridique, qui ne
peut être écrite nulle part et doit être recalculée à chaque affichage, est exactement le
problème que les vues SQL du Copilote Financier résolvent.

**Un écart assumé au sommaire imposé du chapitre 5.** Sa section 5.7 s'intitulait
« Conclusion du chapitre et conclusion générale » dans la version précédente. Comme trois
chapitres et une conclusion générale la suivent désormais, elle est devenue « Conclusion du
chapitre », et son contenu de clôture d'année a été déplacé dans la conclusion du mémoire.
Tout le reste du sommaire imposé est inchangé, y compris la sous-section de quatrième niveau
2.1.1.1, devenue 5.1.1.1.

---

## 2. Analyse de mon style d'écriture

**Résumé en une ligne.** L'analyse conduite en première phase reste valable et s'applique
telle quelle aux nouveaux chapitres ; elle est détaillée dans `Notes_synthese.md`, section 1,
et je n'en reprends ici que ce qui a servi de grille aux chapitres 1, 6 et 7.

Mesures de référence, établies par comptage sur les 24 pages du mi-parcours : 162 phrases
dans le corps narratif, moyenne de 23,6 mots, médiane de 22, et 17 % de phrases de moins de
15 mots.

Les huit traits que j'ai appliqués aux nouveaux chapitres :

1. **Aucune incise entre tirets cadratins.** C'est le marqueur le plus discriminant du
   mi-parcours, qui n'en compte aucune. Vérifié par comptage sur les sept chapitres.
2. **Une phrase brève de scansion tous les cinq ou six énoncés**, pour éviter le flux
   monotone.
3. **Le démonstratif anaphorique en tête de phrase** comme mode d'enchaînement dominant des
   paragraphes.
4. **Le participe présent détaché en fin de phrase**, qui remplace chez moi l'incise.
5. **« je » au féminin pour mes réalisations, « nous » pour ce qui engage l'équipe.** La
   frontière n'est pas « décision au nous, exécution au je » : le mi-parcours écrit « Nous
   avons injecté en priorité les données indispensables à la facturation ».
6. **Les listes numérotées introduites par une phrase se terminant par deux-points**, avec
   un libellé court en gras suivi de son explication.
7. **L'ouverture des sections par le problème** avant la solution, sauf dans les sections de
   bilan et de conclusion, qui ouvrent par un raccordement.
8. **La phrase de recul réflexif en fin de section**, qui généralise ce qui vient d'être
   raconté.

Deux points de vigilance identifiés en première phase et reconduits : « Par ailleurs » et
« Toutefois » en tête de phrase sont absents du mi-parcours et à proscrire ; les connecteurs
adversatifs « Néanmoins » et « Cependant » y sont rares et quasi réservés aux pages de
transition, ce qui est la règle appliquée dans tout le mémoire.

**Le risque propre à cette phase** était l'hétérogénéité entre les chapitres repris du
mi-parcours, dont la matière est déjà écrite dans mon style, et les chapitres entièrement
nouveaux. J'ai traité ce risque en écrivant les chapitres 1, 6 et 7 avec la même grille, et
en reprenant dans les chapitres 2 et 4 des formulations du mi-parcours mot pour mot lorsque
c'était possible, plutôt qu'en les paraphrasant.

---

## 3. Inventaire des figures

**Résumé en une ligne.** Vingt-et-une figures, dont huit produites pour ce mémoire, deux
captures reprises du mi-parcours, deux captures de la plateforme et neuf sorties exécutées
des notebooks du projet de Data Science.

Toutes sont dans `figures/`, toutes sont appelées et commentées dans le corps du texte, et
toutes portent une légende « Figure X.Y – Titre » placée sous la figure.

| Figure | Fichier | Origine |
|:---|:---|:---|
| 1.1 | `fig_1_1_systeme_information.png` | Produite (`src/figures_memoire.py`) |
| 1.2 | `fig_1_2_frise_missions.png` | Produite |
| 2.1 | `fig_2_1_interface_spo.png` | Capture reprise du mi-parcours, sa Figure 1.1 |
| 2.2 | `fig_2_2_directapi.png` | Capture reprise du mi-parcours, sa Figure 1.2 |
| 2.3 | `fig_2_3_sequence_injection.png` | Produite, d'après la séquence décrite dans le mi-parcours |
| 2.4 | `fig_2_4_requetage_dynamique.png` | Produite, d'après la logique GET / tri / POST du mi-parcours |
| 3.1 | `fig_3_1_chaine_traitement.png` | Produite, d'après la note de synthèse SPO |
| 3.2 | `fig_3_2_entonnoir_volumetrie.png` | Produite : 1 602 → 1 474 → 1 434 |
| 3.3 | `fig_3_3_volumetrie_fichiers_import.png` | Produite : les six fichiers d'import |
| 3.4 | `fig_3_4_repartition_natures.png` | Produite : 881 / 462 / 91 |
| 4.1 | `fig_4_1_regle_facturation.png` | Produite, d'après la règle décrite dans le mi-parcours |
| 5.1 à 5.7 | `fig_5_1_*` à `fig_5_7_*` | Sorties exécutées des notebooks du dépôt |
| 5.8 et 5.9 | `fig_5_8_*`, `fig_5_9_*` | Captures de la plateforme, extraites du brouillon |

Les huit figures produites sont régénérables par `python src/figures_memoire.py`. Aucune
valeur n'y est calculée : le script ne met en forme que des données déjà écrites dans les
sources.

**La figure DirectAPI n'apparaît qu'une fois.** Elle est présentée au chapitre 2, où elle
illustre le module d'injection, et le chapitre 3 y renvoie plutôt que de la reproduire,
puisque la capture montre justement la ressource « Tiers » sélectionnée.

---

## 4. Captures d'écran restant à ma charge

**Résumé en une ligne.** Trois captures internes que moi seule peux produire ; leur
emplacement est réservé dans le chapitre 3, qui est complet sans elles.

Chaque emplacement est signalé dans le texte par un bloc détaché commençant par « À insérer
— figure ». Il suffit d'insérer l'image, de la légender et de renuméroter les figures
suivantes du chapitre.

| À produire | Emplacement réservé | Ce que la capture doit montrer |
|:---|:---|:---|
| **Feuille `BuilderTiers`** | Fin de la section 3.3.3 | Une dizaine de lignes avec, côte à côte, les colonnes de données reprises et les colonnes calculées : les trois rangs de déduplication avec des valeurs 1 et 2 visibles, et au moins une ligne où une colonne de rapprochement affiche un code SPO du type `T00012666`. Cadrer aussi le panneau de contrôle avec ses compteurs 881 / 462 / 91 / 40. **Anonymiser les noms d'acquéreurs.** |
| **Collection Postman** | Fin de la section 3.4.2 | L'arborescence de la collection montrant les cinq lots de requêtes, et une requête PATCH ouverte sur son onglet *Body* pour qu'on lise la structure JSON Patch. Le *Runner* affichant les 872 requêtes en succès serait encore mieux. **Masquer l'adresse du serveur et les identifiants**, comme sur la Figure 2.2. |
| **Fiche tiers dans SPO** | Section 3.6, après la Figure 3.4 | Une fiche de couple créée par l'import, onglet des représentants ouvert, montrant les deux personnes et les coordonnées ajoutées par requête PATCH sur l'une d'elles. **Anonymiser.** |

Deux autres illustrations seraient utiles si elles existent, mais leur absence ne gêne pas :
une capture d'un tableau de bord MyReport au chapitre 4, et une capture de la page
« Rythme de vente » ou « Pilotage des prix » de la plateforme au chapitre 5.

---

## 5. Le passage que je dois relire et valider moi-même

**Résumé en une ligne.** La section 7.4.1 est désormais rédigée, mais son contenu est le seul
du mémoire qu'aucune source ne fonde : c'est une intention, et elle m'engage.

Le chapitre 7 expose le positionnement professionnel que ces deux années dessinent :
construire et fiabiliser les chaînes de données qui rendent la décision possible, puis les
outiller, à l'intersection de l'ingénierie des données, de la modélisation et du dialogue
avec les métiers. Ce que le texte ne pouvait pas dire à ma place, c'est mon intention
concrète à l'issue du diplôme. Le bloc « À compléter » a été remplacé par deux paragraphes :
à court terme, poursuivre dans le groupe sur le périmètre données et système d'information ;
à moyen terme, m'orienter vers un poste d'ingénieure données tourné vers l'aide à la
décision.

**Ce que j'ai à faire.** Relire ces deux paragraphes et les corriger s'ils ne correspondent
pas à ce que je veux annoncer au jury. Ils sont formulés de manière à rester vrais si le
projet évolue, mais ils restent une prise de position personnelle et non un constat.

---

## 6. Écarts et points à trancher

**Résumé en une ligne.** Les écarts relevés en première phase restent valables et sont
détaillés dans `Notes_synthese.md`, section 4 ; trois points nouveaux tiennent à la
restructuration.

1. **283 opérations au chapitre 2, 267 au chapitre 5.** Ce ne sont pas les mêmes ensembles :
   283 est le périmètre de la migration vers SPO, 267 le nombre d'opérations présentes dans
   l'export « Budget & EFR » du système de gestion, à une autre date. Le chapitre 5 le
   précise désormais par une incise. Aucune source ne relie les deux chiffres, et je n'ai
   rien ajouté pour les rapprocher.
2. **L'état d'avancement de la migration doit rester cohérent d'un chapitre à l'autre.** Le
   chapitre 2 clôt le premier semestre sur des opérations et des tranches créées, des budgets
   reportés par la stratégie des « coquilles vides » et un historique de factures non repris.
   Les chapitres 3 et 7 ainsi que la conclusion reprennent cet état sans le contredire. C'est
   le point que je vérifierais en premier si le manuscrit devait être remanié.
3. **Le mémoire de mi-parcours ne doit plus être cité comme un document extérieur.** Toutes
   les occurrences ont été converties en renvois internes. Une exception subsiste, volontaire
   et signalée comme telle : le chapitre 7 mentionne les chantiers que j'annonçais à la fin du
   premier semestre, ce qui est un renvoi à un moment du récit et non à un autre document.
4. **Confidentialité des figures 2.1, 5.8 et 5.9.** Ces trois captures montrent des données
   réelles à l'écran : noms d'opérations, agences, marges budgétées et dépassements en euros.
   Rien n'y est nominatif au sens des personnes, mais ce sont des informations de gestion du
   groupe. **À faire valider par ma tutrice en entreprise avant dépôt**, avec deux issues
   possibles : accord explicite, ou floutage des libellés d'opération et remplacement des
   montants par des ordres de grandeur. Le texte ne dépend d'aucune de ces valeurs lues à
   l'écran, l'anonymisation ne coûterait donc rien au propos.
5. **1 602 contre 1 557 : l'écart de 45 lignes n'est toujours pas expliqué.** La note de
   synthèse SPO se contredit sur ce point, sa section 1 annonçant 1 602 lignes brutes issues
   de Vadimm et sa section 3 en donnant 1 557 pour la feuille `VADIMM` et 1 602 pour la
   feuille `Builder coordonnée`. Le chapitre 3 retient 1 602 comme périmètre de travail
   constitué des deux extractions, ce qui est la lecture la plus défendable, mais **je dois
   pouvoir expliquer les 45 lignes en soutenance** : selon toute vraisemblance, des lignes de
   coordonnées présentes dans la seconde extraction et absentes de la première.
6. **« Trois tiers » d'adresse étrangère, mais deux seulement listés.** Le chapitre 3 reprend
   désormais le décompte explicite de la note de synthèse, qui écrit « Trois tiers avaient une
   adresse hors France », alors que son propre tableau de détail n'en documente que deux
   (`T_AR_0863`, Allemagne, et `T_AR_1209`, Émirats arabes unis). J'ai suivi la phrase de la
   note plutôt que son tableau, parce que c'est l'énoncé et non l'illustration. Le troisième
   cas reste à retrouver dans le fichier de travail.
7. **Le paramètre d'élasticité de l'axe C est emprunté à la littérature, sans référence.** Le
   chapitre 5 le signale comme une limite, ce qui est honnête, mais un jury peut demander
   laquelle. Il faut soit retrouver la source d'origine et l'ajouter à la bibliographie, soit
   assumer explicitement qu'il s'agit d'une valeur conventionnelle retenue par convention de
   travail et non d'un paramètre estimé sur nos données.

---

## 7. Chaîne de production du document

**Résumé en une ligne.** Onze fichiers R Markdown sans bloc de code R, assemblés par un
script et rendus par pandoc avec un gabarit LaTeX qui reproduit la mise en forme du
mi-parcours.

- Sources : `memoire/00_preambule.Rmd` à `memoire/10_bibliographie.Rmd`, dans l'ordre de
  leur numéro.
- En-tête commun : `rendu/entete.yaml`, qui porte le titre, les métadonnées de la page de
  titre et les options de sortie.
- Gabarit : `rendu/template_memoire.tex` — classe `report` 12 pt, Computer Modern, `babel`
  français, page de titre, `minitoc` pour les encadrés « Sommaire », pagination romaine puis
  arabe, légendes « Figure X.Y – Titre » sous la figure.
- Filtre : `rendu/filtre_memoire.lua` — traite les blocs `::: sommaire` et `::: transition`,
  reconstruit la numérotation hiérarchique en sortie Word, et compense le décalage du
  compteur `minitoc` provoqué par les chapitres non numérotés.
- Commande : `bash rendu/rendre.sh` assemble `memoire_M2_saoud.Rmd` puis produit le PDF et
  le DOCX.

**Un piège technique à retenir**, parce qu'il a coûté du temps et qu'il se reproduira si le
préambule change. `minitoc` compte les chapitres non numérotés lorsqu'il écrit ses fichiers
auxiliaires, mais pas lorsqu'il les relit. Avec quatre chapitres non numérotés avant le
chapitre 1, les encadrés « Sommaire » des quatre premiers chapitres sortaient vides et ceux
des chapitres 5 à 7 affichaient le sommaire des chapitres 1 à 3. La correction consiste à
émettre `\adjustmtc` après chaque chapitre non numéroté, ce que fait désormais le filtre.

---

## 8. Suite donnée à l'audit final

**Résumé en une ligne.** Un sous-agent à contexte neuf a audité le manuscrit complet et l'a
jugé « non soutenable en l'état, réparable en une passe » ; vingt-neuf remarques ont été
formulées, vingt-six ont été appliquées, trois ont été écartées pour des raisons que je note
ici afin de pouvoir les défendre.

Le rapport intégral est dans `audits/audit_4_manuscrit_complet.md`. L'essentiel de ce qui a
changé se range en quatre familles.

**Ce qui relevait du fond.** Le projet professionnel a été rédigé, la contradiction sur les
tranches commerciales a été levée, les 283 et 267 opérations ont été réconciliées par une
incise, les sur-affirmations ont été ramenées à ce que les sources établissent — « sans
aucun doublon » est devenu « sans doublon détecté par les trois clés d'unicité retenues » —
et le décompte des adresses étrangères a été aligné sur l'énoncé de la note de synthèse.

**Ce qui relevait de la langue.** Concordance des temps de la section 4.1.3, remplacement de
« la plus optimale » et de « au niveau de », diversification des connecteurs adversatifs
— il ne reste que deux « Néanmoins » dans tout le manuscrit —, définition du terme
« committée » là où il apparaît, et non plus seulement dans une légende.

**Ce qui relevait de la présentation.** Le tableau des volumes créés du chapitre 3 ne se
brise plus sur la cellule « 872 requêtes », le tableau des quatre exports du chapitre 5 tient
désormais sur une page, la Figure 2.3 n'est plus tronquée à droite, la Figure 1.1 fait
apparaître les tableurs comme la quatrième couche que le texte annonce, les sous-titres des
axes A, B et C disent ce que chaque axe traite, la table des figures est appelée dans le
sommaire général et le glossaire a été complété de DirectAPI, EFR, Grimmo et MyReport.

**Ce qui a été étoffé.** Le chapitre 2 était le plus court des cinq chapitres de mission
alors qu'il porte la mission la plus longue. Il a été développé sur deux points déjà présents
dans le mémoire de mi-parcours mais traités en une phrase : ce que recouvre l'étape de
transformation et de mapping, et ce que contient la documentation interne que j'ai rédigée.
Le développement a d'abord été trop loin, et a été repris ; voir la section 9.

**Les trois remarques écartées, et pourquoi.**

1. **Supprimer les trois blocs « À insérer — figure » du chapitre 3.** L'auditeur les juge
   incompatibles avec un manuscrit soutenable. Je les conserve parce que la consigne initiale
   était explicite : ne pas bloquer la rédaction sur des captures que moi seule peux produire,
   et signaler leur emplacement. Ces blocs sont des marqueurs de travail, à retirer au moment
   où j'insère les captures, et ils ne partiront pas au dépôt en l'état.
2. **Remanier le plan du chapitre 5**, en remontant le niveau 4 « Besoins par axe et
   exigences non fonctionnelles » d'un cran et en retirant le mot « dashboard » du titre
   5.1.2. Le sommaire de ce chapitre est celui que j'ai imposé, avec la consigne de ne pas en
   modifier l'ordre ni la numérotation, et il porte explicitement ces deux éléments. Seuls
   les sous-titres des axes A, B et C ont été allongés, ce qui ne touche ni à l'ordre ni à la
   numérotation. Si je veux appliquer la remarque, c'est une décision que je prends
   moi-même.
3. **Ajouter une référence bibliographique pour le paramètre d'élasticité de l'axe C.** Je ne
   peux pas inventer une source que le brouillon ne nomme pas. Le point est consigné en
   section 6 comme une décision qui m'appartient.

**Ce que l'audit m'a appris, au-delà des corrections.** Deux choses. La première est qu'un
défaut de mise en page se lit comme un défaut de rigueur : un tableau brisé en deux pages
fait douter du chiffre qu'il porte, alors même que le chiffre est juste. La seconde est que
les formulations absolues sont le point faible d'un mémoire technique. « Sans aucun
doublon » est invérifiable et donc attaquable ; « sans doublon détecté par les trois clés
d'unicité retenues » dit exactement ce qui a été fait, et se défend.


---

## 9. La leçon la plus importante de cette relecture

**Résumé en une ligne.** Une seconde vérification, par un relecteur à contexte neuf qui
n'avait participé ni à la rédaction ni au premier audit, a trouvé que le développement ajouté
au chapitre 2 contenait quatre affirmations qu'aucune de mes sources ne porte. Elles ont été
supprimées. C'est le point de ce dossier que je dois retenir avant tous les autres.

**Ce qui s'était passé.** En étoffant le chapitre 2, l'écriture est passée sans prévenir du
développement d'un fait établi à l'invention d'un fait vraisemblable. La frontière est plus
ténue qu'elle n'en a l'air, et voici les quatre cas, parce qu'ils sont instructifs pris
ensemble :

1. **Une anecdote datée.** « J'avais constaté que je redécouvrais deux fois la même
   contrainte, à quelques jours d'intervalle. » Aucune source ne dit cela. C'était une raison
   plausible d'avoir rédigé la documentation interne, pas une raison attestée.
2. **Une procédure inventée.** Les fichiers de mapping constitués « relevaient d'un arbitrage,
   tranché avec les services concernés puis consigné ». La note dit seulement que j'ai
   constitué ces fichiers.
3. **Une scène avec un personnage.** « La responsable concernée pouvait ouvrir la maquette,
   voir la formule et pointer la ligne fautive. » Personne n'apparaît nulle part dans les
   sources à cet endroit.
4. **Un durcissement technique.** « Un libellé de poste budgétaire, un type de tranche, une
   nature d'opération y sont des valeurs contrôlées. » Le mi-parcours parle d'une
   « nomenclature stricte », ce qui n'établit pas que ces trois champs précis soient des
   listes fermées.

Les quatre ont un trait commun : elles rendaient le texte plus vivant. C'est exactement ce
qui les rendait dangereuses, parce qu'un détail concret est plus crédible qu'une
généralité — et donc plus coûteux si le jury le vérifie.

**Ce qui a été fait.** Les quatre passages sont supprimés ou ramenés à ce que les sources
établissent. Le chapitre 2 gagne désormais environ quatre cents mots au lieu des cinq cent
cinquante annoncés dans l'entrée précédente, et l'audit demandait six à huit cents. J'assume
l'écart : mieux vaut un chapitre plus court que défendable seulement à moitié.

**La règle que j'en tire, pour la suite.** Avant d'écrire une phrase qui fait image — une
date, un nom, une réaction, un chiffre —, vérifier qu'elle figure quelque part dans une
source, et pas seulement qu'elle est vraisemblable. Si elle est vraie mais non écrite, elle
peut être dite au moment de la soutenance, où l'on répond de sa propre mémoire ; elle n'a pas
sa place dans un manuscrit qui doit être vérifiable ligne à ligne.

**Autres corrections issues de cette relecture.** Le tableau consolidé du chapitre 6
contredisait la réserve « hors budgets détaillés » posée aux chapitres 1 et 2. La
concordance des temps de la section 4.1.3 était restée incomplète sur les deux verbes que le
premier audit nommait pourtant. La description de la figure 1.1 parlait de trois boîtes là où
le schéma refait en porte quatre. La phrase sur les adresses étrangères répartissait trois
tiers entre deux pays quand la note n'en documente qu'un par pays. Le glossaire n'était plus
alphabétique après l'ajout de Grimmo et de MyReport. La référence [1] n'était appelée nulle
part ; elle l'est désormais au chapitre 7, où elle sert. Enfin, le séparateur des titres
d'axes a été ramené au deux-points employé partout ailleurs dans le mémoire.

**Ce que le relecteur a laissé passer et que j'ai vérifié moi-même** : la table des matières
n'est pas décalée, les sept encadrés « Sommaire » correspondent aux titres réels, les
volumétries se recoupent d'un chapitre à l'autre, et les vingt-et-une figures sont toutes
appelées et légendées, en PDF comme en Word.
