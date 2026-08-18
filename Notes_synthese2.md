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

## 5. Le seul passage que je dois écrire moi-même

**Résumé en une ligne.** La section 7.4.1 comporte un bloc « À compléter — projet immédiat »
de deux ou trois phrases, et c'est le seul endroit du mémoire qu'aucune source ne permet de
rédiger à ma place.

Le chapitre 7 expose le positionnement professionnel que ces deux années dessinent :
construire et fiabiliser les chaînes de données qui rendent la décision possible, puis les
outiller, à l'intersection de l'ingénierie des données, de la modélisation et du dialogue
avec les métiers. Ce que le texte ne peut pas dire à ma place, c'est mon intention concrète à
l'issue du diplôme : poursuite au sein du groupe et sur quel périmètre, recherche d'un
premier poste et dans quel type de structure, ou poursuite d'études. Le jury l'attendra.

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
