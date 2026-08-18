# Notes de synthèse — rédaction des chapitres 1 et 2 du mémoire de fin d'études

Fichier de travail. Une entrée par sujet, avec un résumé d'une ligne. Mis à jour au fil de
la rédaction, jamais dupliqué. La section 1 a été corrigée après une relecture du mémoire
de mi-parcours faite en contexte neuf : les affirmations qui se sont révélées fausses ont
été supprimées, pas conservées.

---

## 1. Analyse de mon style d'écriture (source : mémoire de mi-parcours)

**Résumé en une ligne.** Phrases de longueur moyenne scandées par des phrases brèves,
enchaînement des paragraphes par démonstratif anaphorique, « je » pour mes réalisations et
« nous » pour ce qui est partagé, participes présents détachés à la place des incises, et
une phrase de recul réflexif pour fermer la plupart des sections.

Analyse conduite sur les 24 pages du mémoire de mi-parcours (`Memoire_d_alternance_mi-parcourM2.pdf`),
avant toute rédaction, puis vérifiée par comptage sur le texte extrait. Mesure de
référence : 162 phrases dans le corps narratif, moyenne 23,6 mots, médiane 22.

### 1.1 Longueur et rythme des phrases

- Médiane de 22 mots. Seulement 6 % des phrases dépassent 40 mots.
- **17 % des phrases font moins de 15 mots**, et ce sont elles qui donnent le rythme :
  « Ces ID système n'étaient visibles nulle part dans l'interface utilisateur. » (p. 13),
  « C'est tout l'enjeu du système décisionnel. » (p. 15), « Ce changement d'environnement
  ne sera pas anodin. » (p. 21). La consigne d'écriture retenue est donc : médiane autour
  de 22 mots, avec une phrase brève de scansion tous les cinq ou six énoncés.
- **Aucune incise entre tirets cadratins dans tout le mémoire de mi-parcours.** Vérifié par
  comptage : les 5 tirets cadratins du document sont tous en tête de puce, aucun en incise.
  C'est le marqueur le plus discriminant, et c'est exactement ce que le brouillon du
  chapitre 2 faisait en abondance.
- Ponctuation dominante : la virgule et les deux-points. Les deux-points annoncent soit une
  énumération, soit une précision : « vise un objectif critique : récupérer l'intégralité
  des opérations immobilières actives » (p. 10).

### 1.2 Connecteurs logiques réellement employés

Relevés par comptage, et non d'après une impression de lecture :

- **« Concrètement, »** — le connecteur signature, 4 occurrences en tête de phrase, toujours
  pour passer du principe à sa mise en œuvre (p. 11, 13, 13, 18).
- **« Face à … »** en tête de phrase pour introduire une contrainte, 3 occurrences : « Face
  à cette volumétrie conséquente » (p. 10), « Face à ce manque de clarté initial » (p. 12),
  « Face aux complexités techniques inhérentes » (p. 13).
- **« Au-delà de … »** pour élargir, 3 occurrences (p. 12, 18, 19).
- « En effet, » — 2 occurrences seulement (p. 7, p. 17). À employer avec parcimonie.
- « Enfin » — 4 occurrences ; « De plus » — 2.
- **Le stock adversatif est très pauvre et localisé** : « Néanmoins » 1 fois et
  « Cependant » 1 fois, les deux dans le même paragraphe de transition (p. 15), plus « bien
  que » 2 fois. C'est un usage quasi réservé aux pages de transition et au bilan.
- **À proscrire** : « Par ailleurs » (0 occurrence dans le mi-parcours) et « Toutefois »
  en tête de phrase (0 occurrence ; l'unique emploi est intra-phrase, p. 21). Les employer
  marquerait immédiatement le texte comme étranger. Les quatre occurrences que j'avais
  écrites dans mes premiers jets ont été supprimées.

### 1.3 Première personne

- **« je » (accordé au féminin) pour ce que j'ai fait moi-même**, 24 occurrences de
  « j'ai » : « Ma première tâche a consisté à » (p. 10), « J'ai été confrontée à deux
  difficultés structurelles majeures » (p. 12), « j'ai pris l'initiative de rédiger une
  documentation interne » (p. 12), « Mon rôle a été de construire l'intégralité du
  pipeline » (p. 11), « Cette contrainte forte m'a obligée à intégrer des vérifications
  programmatiques » (p. 13).
- **« nous » pour l'acte partagé ou l'appartenance au groupe**, 9 occurrences de « nous
  avons ». Attention : la frontière n'est **pas** « décision au nous, exécution au je ».
  Le mi-parcours écrit « Nous avons injecté en priorité les données indispensables à la
  facturation » (p. 13) et « nous avons d'abord migré 3 opérations pilotes, puis un lot de
  12 » (p. 12), dans la même phrase que « j'ai appliqué une méthode de validation
  itérative ». Le « nous » marque le fait que l'action engage l'équipe, quelle que soit sa
  nature.

### 1.4 Listes : deux formes distinctes

- Toutes les listes sont introduites par une phrase qui se termine par deux-points (4 cas
  sur 4).
- **Liste de phases d'un pipeline** : libellé court, deux-points, puis explication.
  « 1. Extraction (Extract) : J'ai utilisé MyReport Builder pour… » (p. 11), « 1. Appel
  GET : Interrogation de l'API pour récupérer… » (p. 13).
- **Liste d'un ordre d'exécution** : syntagmes nominaux nus, sans glose. « 1. Création de
  l'Opération (le conteneur principal). 2. Création des Tranches de Travaux. » (p. 12).
- Les listes à tirets sont réservées à ce qui n'est pas une procédure technique.

### 1.5 Explicitation des termes techniques : une règle plus étroite qu'il n'y paraît

L'explicitation n'est **pas** systématique, contrairement à ce que je croyais d'abord. Le
mémoire de mi-parcours n'explicite jamais ERP (12 occurrences), API (9), CRM (2) ni SQL.
La règle réellement suivie est la suivante :

- **Vocabulaire d'infrastructure et de SI** : glosé une fois, dans le sens forme longue →
  sigle. « les identifiants uniques (ID) » (p. 12), « la Gestion Électronique des Documents
  (GED) » (p. 13), « le déploiement du SSO (Single Sign-On) » (p. 18).
- **Vocabulaire data et développement** : jamais glosé, laissé brut, non italique, souvent
  capitalisé — *Data Science*, *Machine Learning*, *reporting*, *versioning*, *mapping*,
  *endpoints*, et les verbes SQL ou HTTP en capitales.
- **Vocabulaire immobilier** : renvoyé au glossaire, pas expliqué dans le corps.
- Deux gloses seulement vont dans l'autre sens, sigle → explication : « les différents
  endpoints (points de terminaison) » (p. 10) et « des formules de recherche avancées
  (RechercheX) » (p. 11).

**Décision assumée sur les guillemets.** Le mémoire de mi-parcours est incohérent : 5
mises entre guillemets français contre 13 entre guillemets droits, et « coquilles vides »
change de forme d'un chapitre à l'autre. J'ai normalisé les deux nouveaux chapitres aux
guillemets français, qui sont la norme typographique du français académique, plutôt que
d'imiter une irrégularité.

### 1.6 Ouverture de section par le problème

Vrai du chapitre technique, pas du reste. Le chapitre 1 du mi-parcours ouvre
systématiquement par la contrainte avant la solution : « Le périmètre de la migration
concernait un volume de 283 opérations immobilières. Face à cette volumétrie conséquente,
une saisie manuelle intégrale aurait représenté un risque d'erreur humaine trop élevé […].
Nous avons donc opté pour une stratégie hybride » (p. 10). Les chapitres de missions filées
et de bilan ouvrent en revanche par un **raccordement** à ce qui précède : « Dans la
continuité de ma première année d'alternance… » (p. 17), « Au-delà de l'exploitation des
données… » (p. 18).

Comme mes deux nouveaux chapitres sont l'un et l'autre techniques, j'ai appliqué partout
l'ouverture par le problème, sauf dans les sections de bilan et de conclusion.

### 1.7 Phrase de recul réflexif en fin de section

Présente à la fin de 7 sous-sections sur 11. Elle généralise ce qui vient d'être raconté et
en tire un enseignement de méthode :

- « Cette adaptation témoigne d'une gestion de projet agile, capable d'ajuster sa
  méthodologie pour répondre aux réalités du terrain. » (p. 14)
- « Cette approche permet de répondre au besoin métier sans altérer la structure des
  données sources, garantissant ainsi l'intégrité du système tout en offrant la flexibilité
  demandée. » (p. 17)
- « Cette expérience m'a permis de mieux appréhender les problématiques de gestion de parc
  informatique et de gouvernance des accès, des aspects souvent invisibles mais cruciaux
  pour la cohérence du Système d'Information. » (p. 18)

### 1.8 Les procédés syntaxiques qui font vraiment ma signature

Ce sont eux, plus que les connecteurs, qui rendent le texte reconnaissable. Je les avais
d'abord sous-estimés.

1. **Le démonstratif anaphorique en tête de phrase**, procédé dominant : 36 phrases sur
   162, soit 22 %, commencent par *Ce / Cette / Ces / Cet* + un substantif qui reprend ce
   qui précède. « Ce projet ne s'est pas résumé à un simple transfert de données » (p. 12),
   « Cette spécificité a rendu l'automatisation particulièrement délicate » (p. 13),
   « Ce report, bien que frustrant de prime abord » (p. 21). C'est ainsi que presque tous
   les paragraphes s'enchaînent.
2. **Le participe présent détaché en fin de phrase**, 19 occurrences : « garantissant ainsi
   l'intégrité du système » (p. 17), « transformant mon rôle de Data Scientist en Data
   Engineer opérationnel » (p. 21), « laissant temporairement de côté les données
   historiques plus complexes » (p. 13). **C'est ce procédé qui remplace, chez moi,
   l'incise entre tirets.**
3. **Le gérondif de moyen**, 9 occurrences en `en + -ant` et 4 en `tout en + -ant` : « en
   m'appuyant sur l'utilisation intensive d'API » (p. 3), « en analysant les codes d'erreur
   renvoyés par l'API » (p. 12), « tout en assurant la maintenance évolutive des reportings
   existants » (p. 22).
4. **La structure de réfutation « ne … pas X, mais Y »**, 4 occurrences, toujours à un
   moment clé : « Ce projet ne s'est pas résumé à un simple transfert de données, mais a
   nécessité une véritable rétro-ingénierie des processus de l'ERP » (p. 12), « La
   complexité de cette demande ne réside pas dans la donnée brute, mais dans l'application
   d'une règle de gestion spécifique » (p. 17).
5. **Le paragraphe à étiquette**, pseudo-liste rédigée : un syntagme nominal en gras, deux
   points, puis un paragraphe entier. « **L'intégration à l'infrastructure Nexity :** Une
   nouvelle mission structurante… » (p. 21-22). Repris tel quel en section 1.5 du
   chapitre 1.
6. **Le « Il » impersonnel en tête de phrase**, 8 occurrences : « Il est apparu qu'il
   fallait respecter une séquence de création immuable » (p. 12), « Il était donc
   indispensable de finaliser d'abord l'architecture des données » (p. 21).
7. **Le binaire annoncé** : « l'enjeu était double : simplifier l'expérience utilisateur…
   et renforcer la sécurité » (p. 18), « deux phases techniques distinctes », « deux
   difficultés structurelles majeures ».
8. **L'énumération ouverte close par des points de suspension collés**, jamais « etc. » :
   « (Opérations, Tranches, Budgets...) » (p. 10), « (code opération, libellé...) » (p. 13).
9. **Les objets métier de l'ERP capitalisés en cours de phrase** : Opérations, Tranches de
   Travaux, Tranches Commerciales, Budget.

### 1.9 Temps verbaux

Répartition rigide, à respecter : passé composé narratif pour les réalisations, imparfait
pour la contrainte subie (« il était indispensable », « il fallait respecter », « se
soldait par un échec »), présent pour la mission en cours, futur simple pour les
perspectives (« je présenterai », « Il faudra avancer »). Aucun passé simple, aucun présent
de narration.

### 1.10 Traitement des chiffres

Volumétries et cardinaux de données en chiffres (« 283 opérations immobilières », « 3
opérations pilotes, puis un lot de 12 »), mais **dénombrements rhétoriques en toutes
lettres** : « deux phases techniques distinctes », « trois étapes clés », « trois axes
principaux ». Séparateur de milliers par espace insécable dans mes nouveaux chapitres, qui
en contiennent beaucoup plus que le mi-parcours.

### 1.11 Conventions structurelles reprises

1. Encadré **« Sommaire »** en ouverture de chapitre (p. 9, 16, 20).
2. Paragraphe de cadrage non numéroté juste après le sommaire (« Ce chapitre détaille… »,
   p. 10).
3. Numérotation hiérarchique (1.1, 1.1.1) ; le chapitre 2 descend à un quatrième niveau
   (2.1.1.1) parce que le sommaire imposé le demande.
4. Titre de chapitre séparé par un demi-cadratin, jamais par deux-points : « La migration
   vers SPO – Enjeux d'industrialisation et défis techniques » (p. 9). Les deux-points sont
   réservés aux titres de section.
5. **Page de transition en clôture de chapitre**, avec une structure interne fixe : bilan
   de ce qui a été fait, puis restriction introduite par *Néanmoins* ou *Cependant*, puis
   annonce explicite du chapitre suivant (p. 15, p. 19). J'ai repris cette structure à la
   lettre en fin de chapitre 1.
6. Légende sous la figure au format « Figure X.Y – Titre », appel dans le texte par le
   numéro (« est présentée en Figure 1.2 », p. 11). Le mi-parcours comporte un second appel
   fautif, « dans la figure 1 » (p. 10) ; je n'ai pas reproduit cette faute.
7. Aucun appel bibliographique dans le corps, aucune note de bas de page, aucun tableau
   hors glossaire dans le mi-parcours. Mes deux chapitres ajoutent des tableaux, parce que
   le contenu l'impose, mais s'abstiennent de notes et d'appels bibliographiques.

### 1.12 Les deux écueils du brouillon du chapitre 2, et ce que j'en ai fait

| Écueil du brouillon | Traitement dans la réécriture |
|:---|:---|
| Phrases longues empilant les incises entre tirets cadratins | Découpées en deux ou trois phrases ; les incises deviennent des subordonnées, des participes présents détachés ou des phrases autonomes. Aucun tiret cadratin d'incise ne subsiste. |
| Ton essayiste et affirmatif qui tranche (« Il faut le dire simplement », « C'est la section la plus solide du projet ») | Reformulé en description justifiée et nuancée, la réserve étant énoncée à sa place plutôt que balayée. |

---

## 2. Inventaire des figures

**Résumé en une ligne.** Neuf figures pour le chapitre 2, toutes reprises du brouillon
(sept extraites des notebooks du dépôt, deux du PDF) ; cinq figures pour le chapitre 1,
dont quatre produites pour l'occasion et une reprise du mémoire de mi-parcours.

Toutes les figures sont dans `figures/`. Toutes sont appelées et commentées dans le corps
du texte, avec la légende « Figure X.Y – Titre » placée sous la figure.

### 2.1 Chapitre 1 — cinq figures

| Figure | Fichier | Origine | Section |
|:---|:---|:---|:---|
| 1.1 | `fig_1_1_chaine_traitement.png` | Produite (`src/figures_chapitre1.py`) à partir des compteurs de la note de synthèse | 1.2.1 |
| 1.2 | `fig_1_2_directapi_tiers.png` | Reprise du mémoire de mi-parcours (sa Figure 1.2), ressource « Tiers » | 1.2.2 |
| 1.3 | `fig_1_3_entonnoir_volumetrie.png` | Produite : 1 602 → 1 474 → 1 434 | 1.3.2 |
| 1.4 | `fig_1_4_volumetrie_fichiers_import.png` | Produite : volumétrie des six feuilles de sortie | 1.3.3 |
| 1.5 | `fig_1_5_repartition_natures.png` | Produite : 881 couples / 462 PP / 91 PM | 1.6 |

La reprise de la figure DirectAPI du mémoire de mi-parcours se justifie doublement : la
capture montre la ressource « Tiers » sélectionnée, et énumère à l'écran les emplacements
de fichiers (tiers, RIB, représentants, adresses, courriels, sites web, téléphones, rôles)
qui correspondent exactement au découpage en feuilles de sortie du fichier de travail. Elle
illustre donc le modèle de données, pas seulement l'outil.

Les quatre figures produites sont régénérables par `python src/figures_chapitre1.py`.
Aucune valeur n'y est calculée : le script ne met en forme que les compteurs de la note de
synthèse.

### 2.2 Chapitre 2 — neuf figures

Les sept premières ont été extraites des sorties exécutées des notebooks du dépôt, source
d'origine préférée à l'extraction depuis le PDF. Leur résolution est identique à celle des
images embarquées dans le brouillon, ce qui confirme qu'il s'agit bien des mêmes fichiers.

| Figure | Fichier | Source dans le dépôt |
|:---|:---|:---|
| 2.1 | `fig_2_1_prix_m2_log.png` | `notebooks/00_exploration_donnees.ipynb`, cellule 12 |
| 2.2 | `fig_2_2_intensite_vente.png` | `notebooks/00_exploration_donnees.ipynb`, cellule 24 |
| 2.3 | `fig_2_3_distribution_variation_marge.png` | `notebooks/03_prediction_marge.ipynb`, cellule 4 |
| 2.4 | `fig_2_4_scenarios_taux_2026.png` | `notebooks/04_vitesse_ecoulement.ipynb`, cellule 14 |
| 2.5 | `fig_2_5_courbes_logistiques.png` | `notebooks/04_vitesse_ecoulement.ipynb`, cellule 18 |
| 2.6 | `fig_2_6_effet_millesime.png` | `notebooks/05_optimisation_prix.ipynb`, cellule 6 |
| 2.7 | `fig_2_7_stock_prix_marche.png` | `notebooks/05_optimisation_prix.ipynb`, cellule 9 |
| 2.8 | `fig_2_8_plateforme_vue_ensemble.png` | Capture de la plateforme, extraite du brouillon PDF (page 10) |
| 2.9 | `fig_2_9_plateforme_alertes_marge.png` | Capture de la plateforme, extraite du brouillon PDF (page 11) |

---

## 3. Captures d'écran restant à ma charge (chapitre 1)

**Résumé en une ligne.** Trois captures internes que moi seule peux produire ; leur
emplacement est déjà réservé dans le texte du chapitre, qui est complet sans elles.

Le chapitre a été rédigé intégralement sans attendre ces captures. Chaque emplacement est
signalé dans le fichier `.Rmd` par un paragraphe en gras entre crochets, précédé et suivi
du texte qui les commentera. Il suffit d'insérer l'image, de la légender et de renuméroter
les figures suivantes.

| À produire | Emplacement réservé | Ce que la capture doit montrer |
|:---|:---|:---|
| **Feuille `BuilderTiers`** | Fin de la section 1.3.3 | Une dizaine de lignes avec, côte à côte, les colonnes de données reprises (A à Q) et les colonnes calculées : les trois rangs de déduplication R, S, T avec des valeurs 1 et 2 visibles, et au moins une ligne où la colonne AE, AF ou AG affiche un code SPO du type `T00012666`. Cadrer aussi le panneau de contrôle en haut à droite (lignes 1 à 15) avec ses compteurs 881 / 462 / 91 / 40. **Anonymiser les noms d'acquéreurs.** |
| **Collection Postman** | Fin de la section 1.4.2 | L'arborescence de la collection montrant les cinq lots de requêtes, et une requête PATCH ouverte sur l'onglet *Body* pour qu'on lise la structure JSON Patch (`op`, `path`, `value`). Le *Runner* affichant les 872 requêtes toutes en succès serait encore mieux. **Masquer l'adresse du serveur et les identifiants**, comme cela a été fait sur la figure DirectAPI du mémoire de mi-parcours. |
| **Fiche tiers dans SPO** | Section 1.6, après la Figure 1.5 | Une fiche de couple créée par l'import, avec l'onglet des représentants ouvert : on doit y voir les deux personnes du couple et, sur au moins l'une d'elles, le courriel et le téléphone ajoutés par PATCH. C'est la preuve visuelle que la chaîne complète a fonctionné. **Anonymiser.** |

---

## 4. Écarts, imprécisions et points à trancher dans les sources

**Résumé en une ligne.** Onze écarts relevés entre le brouillon, la note de synthèse et le
dépôt ; dans tous les cas j'ai gardé la version du brouillon ou de la note dans le texte du
chapitre, et je consigne ici ce qu'il faudrait vérifier.

### 4.1 Dans la note de synthèse SPO (chapitre 1)

1. **« Trois tiers avaient une adresse hors France » mais le tableau n'en liste que deux**
   (`T_AR_0863` ROLIN et `T_AR_1209` ABU DHABI). Le chapitre décrit donc le traitement sans
   avancer de décompte, pour ne pas trancher à la place de la source.
2. **Le total des lignes sources ne se recoupe pas, et la note se contredit.** Sa section 1
   annonce « Lignes brutes issues de VADIMM : 1 602 », tandis que sa section 3 donne 1 557
   lignes à la feuille `VADIMM` et 1 602 à la feuille `Builder coordonnée`. Le chapitre
   contenait d'abord la même contradiction ; il présente désormais 1 602 comme le
   **périmètre de travail** constitué des deux extractions, en donnant les deux comptes.
   L'écart de 45 lignes entre les deux feuilles reste à expliquer dans la note d'origine.
3. **881 couples créés mais 872 requêtes PATCH.** L'écart de neuf n'est expliqué nulle part
   dans la note. Le chapitre n'affirme pas une requête par couple, il se contente du
   décompte de la note, mais un jury peut poser la question : il faut préparer la réponse
   (vraisemblablement les couples sans courriel ni téléphone renseignés).
4. **Les 40 exclusions ne sont pas ventilées** entre les trois formules de rapprochement
   (personnes morales, personnes physiques, couples). Le chapitre reste au total.
5. **Le prénom « Sarah »**, cité dans la note pour la validation des doublons à adresses
   divergentes, n'a pas été repris : je ne connais pas son rôle exact et un mémoire n'est
   pas le lieu de nommer une collègue sans son accord. Le chapitre écrit « nous avons
   tranché », ce qui reste fidèle au fait qu'il s'agit d'un arbitrage à deux.
6. **La note interdit quatre manipulations du fichier, pas trois** : modifier une feuille de
   sortie, modifier les colonnes calculées R à AC, insérer une ligne, trier la feuille pivot.
   Le chapitre les énumère désormais toutes les quatre.
7. **Le mémoire de mi-parcours ne dit pas que les budgets ont été migrés au premier
   semestre**, au contraire : la stratégie des « coquilles vides » les laissait de côté et sa
   conclusion annonce la reprise des historiques budgétaires comme un chantier à venir. Le
   chapitre 1 ne mentionne donc plus que les opérations et leurs tranches.

### 4.2 Entre le brouillon du chapitre 2 et le dépôt

Ces points ont été relevés lors d'un contrôle croisé du brouillon avec les sorties
réellement exécutées des notebooks. **Aucun n'a été corrigé dans le chapitre** : le
brouillon fait foi, conformément à la consigne. Ils sont à arbitrer avant la soutenance,
parce qu'un jury peut les relever.

| Affirmation du brouillon, conservée dans le chapitre | Ce que dit le dépôt |
|:---|:---|
| « 45 % des 2 157 désistements ont pour motif un problème de financement ou un refus de prêt » | Le recalcul donne 1 030 motifs de la famille financement sur 1 963 motifs renseignés, soit 52,5 % des motifs renseignés ou 47,8 % des 2 157 désistements. Le 45 % vient de `docs/03_besoins_metier.md`, et `journal_de_bord.md` (étape 13) avait déjà signalé la valeur comme fausse. **Formulation plus sûre : « plus de la moitié des désistements dont le motif est renseigné ».** |
| « Quatre classifieurs classiques ont été confrontés » | `notebooks/03_prediction_marge.ipynb` en compare six plus une référence : arbre CART 0,340, forêt 0,306, séparateur à vaste marge linéaire 0,303, régression logistique 0,283, réseau de neurones 0,262, séparateur à noyau 0,257. |
| « un F1 de l'ordre de 0,30 à 0,34 » | La borne basse est optimiste : la régression logistique, citée parmi les quatre, est à 0,283. Fourchette exacte des quatre modèles nommés : 0,28 à 0,34. |
| « prime d'étage (+6 %) » | Le coefficient vaut +5,9 % **par écart-type de la variable étage**, soit environ 1,4 étage, et non par niveau. |
| « un référentiel des 90 communes d'implantation » | La table compte bien 90 communes, mais les 267 opérations couvrent 120 communes normalisées : 234 opérations sur 267 se rattachent au référentiel, soit 87,6 %. |
| « la frontière entre les deux activités ressort d'elle-même dès l'analyse exploratoire » | Ce résultat ne vient pas du notebook d'exploration mais du notebook d'analyse multidimensionnelle, que le brouillon ne présente pas. L'affirmation reste vraie, mais elle n'est pas sourcée par ce que le chapitre expose. |
| « 10 en alerte et 2 à surveiller » | Ces comptages viennent du modèle sérialisé `plateforme/modeles/risque_marge.joblib`, exclu du dépôt par `.gitignore`. Seule trace écrite : `journal_de_bord.md`. Les autres chiffres de la Vue d'ensemble (147, 68, 421, 4,8 et 3,11 %) sont, eux, reproductibles. |
| « Chaque page a été vérifiée par le cadre de test de Streamlit » | Aucun fichier de test n'est versionné dans le dépôt. L'affirmation est plausible mais non reproductible en l'état ; la formuler à la première personne serait plus honnête. |
| « plus d'un tiers des opérations (36,6 %) n'a aucun dépassement engagé » | **Ici c'est le brouillon qui a raison** : 45 opérations sur 123 font exactement 36,6 %. Le dépôt se trompe en trois endroits en écrivant « la moitié des opérations ». |
| « médiane proche de vingt mois » | **Le brouillon a raison** (19,9 mois). Une cellule markdown du notebook dit « de l'ordre de deux à trois ans » et se contredit. |
| « aucune donnée nominative de client affichée ni modélisée » | Exact pour les clients. Le dépôt affiche en revanche des **noms de vendeurs**, dont certains sont des personnes physiques. La formulation du brouillon reste juste telle qu'elle est écrite. |
| Périmètre de l'axe A : « engagées à au moins 60 %, de marge budgétée supérieure à 50 k€ » | Le filtre exécuté ajoute un troisième critère, recettes budgétées strictement positives, qui écarte 6 opérations. |
| « 3,1 % mi-2026 » | La série de la Banque centrale européenne n'est publiée que jusqu'en avril 2026 dans le dépôt ; les valeurs de mai et juin sont un report de la dernière valeur connue. |
| Diagnostic du stock : « 103 dans le marché, 8 au-dessus, 16 en dessous » | Conforme au notebook. **Mais la plateforme affiche 111 / 4 / 12**, parce qu'elle ajuste le modèle sur tout le corpus et utilise une bande de ±13,1 % au lieu de ±11,1 %. Si une capture de la page « Pilotage des prix » est ajoutée un jour, les deux chiffrages se contrediront à l'écran. |

### 4.3 Vérifications qui, elles, sont conformes

Le contrôle croisé a confirmé sans écart : 267 opérations ; 32 Mo d'exports (32,1 Mo
mesurés) ; 16 467 / 65 000 / 79 106 / 2 164 lignes ; 64 788 + 212 = 65 000 ; 118 opérations
jointes ; 91 orthographes pour 90 communes ; asymétrie 19,2 puis 0,39 ; corrélations +0,07,
-0,34 et +0,44 ; 1 561,8 M€ et 1 754,8 M€ ; rapport Spark 58 après 23,9 s de démarrage, 9
Mo, 28 antérieurement ; 123 opérations, seuil 2 %, R² 0,077, 27,6 % au-delà du seuil, deux
cas extrêmes ; 3 230 observations sur 160 opérations, ICC 0,66, coefficient -0,216, p très
inférieure à 10^-15^ ; 114 mois et p-valeur 0,820 ; 28 opérations terminées dont 25 mieux
ajustées ; +6 % et -3 % ; 5 064 appartements, R² test 0,886, erreur type 11,1 %, décote
62,8 %, effet millésime +19,0 % ; 127 lots en stock ; élasticité interne -0,81 non
significative sur 95 opérations ; 23 015 € de remise, 18 appartements, 6,8 → 7,4 lots,
-0,3 % ; 9 688 commentaires ; 90 motifs sur 100 en « Autres motifs » à Salon-de-Provence ;
51,6 %, 9,0 % et 29,6 % ; F1 0,343 ; 147 opérations, 68 en cours, 421 lots, 4,77
réservations, taux 3,11 % ; trajectoire du taux 1,10 % → 3,60 % → 3,11 % ; rythme groupe
150,0 en 2021 puis 113,4 en 2023.

Les noms employés dans le chapitre sont ceux du dépôt : les cinq pages `Vue d'ensemble`,
`Alertes marge`, `Rythme de vente`, `Pilotage des prix`, `Qualité commerciale`, et les
trois vues `v_marge_operation`, `v_ecoulement_mensuel`, `v_stock_lots`, dont les
descriptions du brouillon correspondent exactement et dans le même ordre.

---

## 5. Éléments du dépôt non repris dans les chapitres

**Résumé en une ligne.** Le dépôt contient beaucoup plus que ce que le brouillon raconte ;
rien de ce qui suit n'a été ajouté au texte, et c'est à moi de décider si quelque chose
mérite d'y entrer.

### 5.1 Le plus notable : un notebook entier absent du brouillon

`notebooks/02_analyse_multidimensionnelle.ipynb` n'est évoqué nulle part dans le brouillon,
alors qu'il répond au besoin « comparer une opération à ses semblables » annoncé dans l'axe
A. Il contient :

- une analyse en composantes principales sur les profils de coûts de 223 opérations et 9
  postes, avec 61 % de variance sur les deux premiers axes, et un cercle des corrélations
  qui oppose la construction au foncier et aux VRD ;
- un **comparateur d'opérations par similarité cosinus**, qui remonte pour une opération
  donnée ses voisines les plus proches avec leurs marges ;
- une classification en 4 types nommés (résidentiel classique, aménagement foncier,
  promotion sur foncier allégé, aménagement lourd), validée par des variables non utilisées
  pour la construire, avec l'arbitrage explicite « les critères statistiques disent 2
  groupes, le métier en impose 4 » ;
- la justification quantitative de la frontière promotion / aménagement que le chapitre
  invoque en 2.6 sans la sourcer.

C'est le seul ajout qui me paraît vraiment discutable : il comblerait un besoin annoncé et
sourcerait une affirmation de la conclusion. **À décider.**

### 5.2 Résultats existants mais non repris

- **Le coût des désistements en euros.** La table des désistements porte un taux et un
  montant de commission par dossier. Le chapitre affirme que « chaque commission versée sur
  un dossier qui n'aboutit pas est une dépense sans recette » sans jamais chiffrer ce coût,
  alors que la donnée existe.
- **Les modèles écartés de l'axe A** : Ridge et Lasso donnent un R² test négatif, le Lasso
  annulant tous les coefficients ; un séparateur à noyau et un réseau de neurones font
  moins bien que l'arbre. Le brouillon n'en dit rien, alors qu'il avoue une faiblesse
  symétrique sur l'axe C.
- **La variante softmax à trois classes**, qui est la brique produisant les trois niveaux
  d'alerte affichés par la plateforme.
- **Les importances de variables de la forêt** (part du foncier, marge relative au budget,
  part des VRD), qui répondent à la question « quels postes expliquent la dérive ».
- **Les deux coefficients qui prouvent l'affirmation « la régression naïve surestime »** :
  -0,2421 en régression groupée contre -0,2159 en modèle mixte.
- **La table des dix spécifications ARIMAX testées**, qui montre que la procédure a écarté
  des modèles meilleurs au critère AICc mais aux résidus non blancs.
- **Les scénarios de taux en fin d'horizon** : +14 % au douzième mois en cas de détente et
  -8 % en cas de remontée, plus parlants pour un directeur financier que les moyennes.
- **Les coefficients hédoniques non cités** : littoral, exposition sud chiffrée, et surtout
  l'élasticité-taille de -3,1 % qui crédibilise le modèle.
- **Le double contrôle numérique de l'optimisation des prix**, montée de gradient projetée
  contre méthode SLSQP, avec un écart maximal négligeable.
- **Le détail de l'anti-fuite sur le texte** : 314 commentaires mentionnant explicitement le
  désistement ont été retirés, et la régression logistique fait moins bien que le
  classifieur naïf sur cette tâche.
- **L'entropie et la divergence de Kullback-Leibler par agence**, qui sont la méthode ayant
  fait ressortir l'anomalie de saisie de Salon-de-Provence, et qui signalent aussi une
  sur-représentation de la rétractation à Toulouse.
- **L'analyse de réseau complète** : graphe biparti, communautés, centralités, et le
  résultat contre-intuitif selon lequel les vendeurs centraux se désistent moins que les
  périphériques.
- **Le mécanisme de génération des notebooks** : chaque notebook est produit et ré-exécuté
  de bout en bout par un script Python. C'est le vrai fondement de la reproductibilité
  revendiquée dans le chapitre, et il est actuellement invisible.
- **L'audit final en contexte neuf** consigné dans `journal_de_bord.md`, avec ré-exécution
  intégrale par un tiers, quatre incohérences corrigées et un chiffre non traçable
  supprimé. Ce serait un excellent paragraphe de démarche qualité.
- La distance au littoral est un **proxy maison** (distance minimale à six points du golfe
  du Lion, seuil à 10 km), et non une donnée publiée.

### 5.3 Incohérences internes au dépôt, sans effet sur les chapitres

- `docs/01_cadrage_projet.md` est obsolète : mon nom y est mal orthographié, il cite un
  fichier source qui n'existe pas, annonce une plateforme à trois pages et une liste
  d'agences incomplète.
- `journal_de_bord.md` conserve les valeurs Spark d'une exécution antérieure (28×, 25 Mo)
  qui ne correspondent plus aux sorties des notebooks.
- Deux cellules du notebook de l'axe A mentionnent 129 opérations là où l'échantillon
  exécuté en compte 123.
- `docs/03_besoins_metier.md` et une cellule du notebook de l'axe A désignent encore les
  pages de la plateforme sous leurs anciens noms.

---

## 6. Chaîne de production des documents

**Résumé en une ligne.** Les deux chapitres sont écrits en R Markdown sans bloc de code R et
rendus par pandoc, avec un gabarit LaTeX qui reproduit la mise en forme du mémoire de
mi-parcours.

- Sources : `chapitre_1_migration_tiers_spo.Rmd`, `chapitre_2_copilote_financier.Rmd`.
- Gabarit : `rendu/template_memoire.tex` — classe `report` 12 pt, Computer Modern, `babel`
  français, `minitoc` pour l'encadré « Sommaire », légendes « Figure X.Y – Titre » sous la
  figure, images bornées à la largeur du texte avec conservation des proportions.
- Filtre : `rendu/filtre_memoire.lua` — traite les blocs `::: sommaire` et
  `::: transition`, et reconstruit la numérotation hiérarchique en sortie Word, pandoc ne
  sachant pas y décaler le compteur de chapitre.
- Commande : `bash rendu/rendre.sh` produit les quatre fichiers `.pdf` et `.docx`.
- Le décalage de chapitre est porté par la métadonnée `chapoffset` du fichier `.Rmd` :
  `0` pour le chapitre 1, `1` pour le chapitre 2.
- Les `.Rmd` ne contiennent aucun bloc de code R, donc un `knit` sous R donne exactement le
  même résultat que l'appel pandoc direct. Les figures sont des fichiers PNG déjà produits,
  ce qui évite de refaire tourner l'analyse à chaque rendu.
