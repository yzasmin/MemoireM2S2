# Plan des slides — soutenance Copilote Financier

14 slides. Répartition volontaire du temps de parole : **≈ 25-30 % sur les
deux reprises de données (missions d'alternance, slides 2-3), ≈ 70-75 %
sur le Copilote Financier (slides 5-11)** — c'est la partie data science,
et c'est elle que le jury attend en profondeur. Une entrée par slide :
titre, contenu (bullets ou visuel du mémoire/repo à reprendre), et la
portion de `discours_soutenance.md` qui lui correspond. En cas de
divergence entre ce fichier et le `.pptx` généré en complément, **ce
fichier fait foi**.

**Note de calibrage :** avec l'ajout de la slide 6 (exploration des
données) et l'approfondissement de l'axe A (ACP, validation croisée), le
discours est passé de ~2 040 à ~2 240 mots, soit **16 à 17 minutes** selon
le débit plutôt que 15 — un compromis assumé entre la cible de durée
initiale et la demande de creuser davantage la méthode. À retravailler
si 15 minutes strictes redeviennent la contrainte prioritaire.

---

### Slide 1 — Titre

**Titre affiché :** Le Copilote Financier — Groupe Angelotti
**Sous-titre :** Reprise de données, reporting et aide à la décision —
Yasmina Saoud, Master MIASHS, alternance Groupe Angelotti

**Contenu visuel :** page de garde sobre — nom Angelotti, nom du master,
jury (tutrice entreprise, tutrice pédagogique, membre expert), date de
soutenance. Pas de bullet.

**Discours :** SLIDE 1.

---

### Slide 2 — Contexte Angelotti et migration des opérations

**Contenu (slide condensée — chapitre 1, à traiter vite) :**
- Groupe Angelotti — promoteur-aménageur, filiale Nexity, deux métiers
  (promotion / aménagement)
- Chaque opération = une société dédiée ; budget qui dérive au fil du
  chantier et des ventes
- **L'événement de l'année : migration de l'ERP Grimmo vers SPO**
  (changement de modèle de données, pas seulement d'outil)
- 283 opérations à recréer — automatisation via API, validation par
  paliers (3 pilotes → 12 → masse), déploiement en « coquilles vides »
- **283 opérations créées dans SPO à la fin du semestre**

**Visuel :** schéma du système d'information (Figure 1.1 du mémoire) ou
séquence d'injection (Figure 1.2), en petit format — cette slide doit
rester rapide à l'oral.

**Discours :** SLIDE 2.

---

### Slide 3 — La reprise des tiers

**Contenu (condensée mais garde le cœur méthodologique) :**
- Second semestre : reconstituer le référentiel client (« tiers » dans
  SPO) — 1 602 lignes de coordonnées issues du CRM, ~13 000 tiers déjà
  présents dans SPO
- **Trois clés d'unicité différenciées selon la nature du tiers** (couple
  / personne physique / personne morale) — calcul d'un rang plutôt qu'une
  suppression, pour rester traçable
- Résultat chiffré : 1 602 → −128 doublons internes → 1 474 uniques → −40
  déjà présents → **1 434 tiers créés** (881 couples, 462 personnes
  physiques, 91 personnes morales), **zéro doublon détecté**
- Contrainte technique résolue par API : 872 requêtes PATCH (5 lots) pour
  les coordonnées des couples, toutes exécutées sans erreur

**Visuel :** Figure 1.4 du mémoire (entonnoir 1 602 → 1 434).

**Discours :** SLIDE 3.

---

### Slide 4 — Vers le Copilote Financier

**Contenu :**
- Les deux reprises répondent à une question : la donnée est-elle bien
  arrivée ?
- Le socle reconstitué permet de se poser une question différente : que
  peut-on en tirer pour la décision ?
- **Transition vers le second projet de l'année : le Copilote Financier**

**Visuel :** slide de transition, minimaliste.

**Discours :** SLIDE 4.

---

### Slide 5 — Le Copilote Financier : contexte, données et méthode

**Contenu :**
- Constat : la direction financière suit ses dérives opération par
  opération, sur tableurs, sans vision transverse
- Trois questions : quelles opérations dérapent ? à quel rythme le stock
  s'écoule-t-il ? à quel prix vendre chaque lot ?
- Adossé à **267 opérations réelles** et **7 programmes d'analyse**
  exécutés et vérifiés un par un
- **Boîte à outils volontairement diverse** : typologie non supervisée,
  régression et classification, séries temporelles, optimisation sous
  contrainte, fouille de texte et analyse de réseau
- **Principe méthodologique affirmé à l'oral, valable sur tout le
  projet** : sur un échantillon restreint, un résultat n'est retenu que
  s'il tient en validation croisée (testé sur des données non vues à
  l'entraînement) — jamais sur sa seule performance d'ajustement

**Visuel :** tableau à 3 lignes (Axe / Question / Famille de modèles),
repris du mémoire (section 2.1.2 / `docs/01_cadrage_projet.md`).

**Discours :** SLIDE 5.

---

### Slide 6 — Exploration des données : deux leçons avant de modéliser

**Slide nouvelle (notebook 00), ajoutée à la demande explicite de couvrir
l'EDA — absente de la version précédente.**

**Contenu :**
- Distribution du prix au m² des appartements très asymétrique (quelques
  lots de standing tirent la queue) → **après log-transformation,
  quasi-normale** → oriente l'axe C à modéliser le **log-prix**
- Piège méthodologique repéré et corrigé : la corrélation brute entre
  réservations mensuelles et taux des crédits est **quasi nulle**, alors
  que le lien économique est réel — la croissance du portefeuille
  (nombre d'opérations commercialisées) maquille la relation
- Une fois rapportée au nombre d'opérations actives (intensité de vente),
  **la corrélation redevient nette et négative** — cette correction a
  directement structuré la démarche de l'axe B (panel plutôt que série
  brute)
- Leçon assumée à l'oral : toujours vérifier la sortie réelle d'une
  cellule plutôt que la conclusion attendue

**Visuel :** Figure 2.1 du mémoire (distribution du prix, brute puis
log) à côté de la Figure 2.2 (intensité de vente, effet des taux visible
une fois l'effet de portefeuille neutralisé) — les deux n'ont pas encore
été extraites en image pour le `.pptx`, à ajouter si le temps le permet
(pages du PDF à identifier comme pour les autres figures).

**Discours :** SLIDE 6.

---

### Slide 7 — Axe A : le risque de marge

**Contenu (enrichie — méthode complète, pas seulement le chiffre final) :**
- Périmètre : 123 opérations suffisamment avancées (engagement ≥ 60 %) —
  **28 % en dérive matérielle** (> 2 % de la marge budgétée)
- Régression du taux de dérive : R² test = 0,08 (résultat modeste) →
  bascule en classification « à risque / non »
- **Comparaison de six méthodes en validation croisée (métrique F1)** :
  logistique 0,283 · SVM linéaire 0,303 · SVM RBF 0,257 · arbre 0,340 ·
  **forêt aléatoire 0,306 (retenue)** · réseau de neurones (MLP) 0,913 en
  apprentissage mais **0,262 en validation — sur-apprentissage démonstratif**
- Régression Ridge en complément : rend lisibles les facteurs de dérive
  (postes techniques, marge budgétée confortable qui protège)
- **Analyse en composantes principales (ACP)** : 2 axes résument **61 %**
  de la structure des coûts, résultat vérifié par une seconde méthode de
  calcul indépendante (SVD) → fonde une typologie de 4 familles
  d'opérations, utilisée comme comparateur (« voisines » de coûts
  similaires)
- Message assumé : signal réel mais faible

**Visuel :** Figure 2.3 du mémoire (distribution de la variation de
marge) **+** petit tableau des 6 F1 par méthode, avec le duo
train/validation du MLP mis en évidence (c'est le point pédagogique fort
de cette slide pour un jury data science).

**Discours :** SLIDE 7. **Slide la plus dense en méthode — normal, c'est
elle qui montre la rigueur statistique la plus large (ACP, validation
croisée, régularisation, comparaison de modèles).**

---

### Slide 8 — Axe B : la vitesse d'écoulement

**Contenu :**
- Panel de 3 230 observations (opération × mois, 160 opérations) — modèle
  à effets aléatoires (Laird-Ware)
- **2/3 de la variance du rythme = effet propre à l'opération, 1/3 =
  conjoncture**
- **+1 point de taux de crédit ⇒ −19 % de réservations mensuelles**
  (p < 10⁻¹⁵, très significatif)
- Contrôle de robustesse par série temporelle (ARIMA) sur la série
  agrégée (114 mois) : effet du taux non identifiable isolément — lu
  comme une validation méthodologique (écarte le risque de corrélation
  fallacieuse, cf. slide 6), pas un échec
- Scénarios 2026 : détente à 2,5 % → **+6 % de rythme** ; remontée à
  3,5 % → **−3 %**
- Courbe logistique par opération : bat un ajustement linéaire sur 25/28
  opérations terminées, délai médian de 20 mois pour 90 % du potentiel

**Visuel :** Figure 2.4 du mémoire (scénarios de taux 2026, trajectoire
ARIMA combinée à l'élasticité du panel).

**Discours :** SLIDE 8. **Axe le plus solide — à assumer clairement comme
tel à l'oral.**

---

### Slide 9 — Axe C : l'optimisation des prix

**Contenu :**
- Modèle hédonique sur 5 064 appartements vendus depuis 2016 — **R² test
  = 0,886, erreur type ≈ 11 %**
- Primes hédoniques cohérentes : étage +6,0 %, logement social −62,8 %
  (prix réglementés) — voir aussi exposition sud +2,6 %, millésime
  +19-21 % (2016→2023/2026) si une question du jury s'y intéresse
- Appliqué au stock (127 appartements) : **24 lots hors marché** (16
  sous-cotés, 8 surcotés)
- Élasticité non significative en interne (p = 0,57, n = 95) → fixée
  prudemment à ε = −1, documentée plutôt que masquée
- **Optimisation sous contrainte par multiplicateur de Lagrange, vérifiée
  par un second solveur (SLSQP) — convergence à 0,006 près** : la remise
  optimale est un **montant identique en euros** sur tous les lots (donc
  un % plus fort sur les petits lots), à l'inverse de la pratique actuelle

**Visuel :** tableau des résultats clés (R², lots hors marché, règle de
remise) — c'est l'option retenue dans le `.pptx` généré, car le discours
ne nomme aucune opération précise.

**Discours :** SLIDE 9.

---

### Slide 10 — Signaux faibles : texte et réseau de vente

**Contenu :**
- 9 688 commentaires libres de vente (67 % des dossiers) : moteur de
  recherche par similarité cosinus (TF-IDF) — une requête en langage
  courant (« refus de prêt banque ») retrouve les dossiers concernés
- Prédiction du désistement par le texte : contrôle de fuite (314
  commentaires nommant déjà l'annulation, écartés) → Naive Bayes F1 =
  0,343 sur le corpus filtré, préféré à une régression logistique plus
  précise mais quasi muette (rappel 0,15) — signal d'appoint, pas
  prédicteur autonome
- Divergence de Kullback-Leibler (mesure d'écart entre distributions) :
  révèle un défaut de saisie sur une agence (90 % de motifs « autres »),
  pas un profil client
- Réseau biparti vendeurs-opérations (209 vendeurs, 711 arêtes) : deux
  pivots concentrent **51,6 % des dossiers**, avec des taux de
  désistement très contrastés (9,0 % vs 29,6 %)

**Visuel :** pas de figure extraite du mémoire pour cette slide (aucune
n'a été identifiée) — le `.pptx` utilise trois cartes chiffrées à la
place (F1 texte, concentration réseau, contraste des taux de
désistement).

**Discours :** SLIDE 10.

---

### Slide 11 — La plateforme : cinq pages pour la direction financière

**Contenu :**
- Application Streamlit, périmètre 147 opérations de promotion, 5 pages
  testées individuellement
- **Vue d'ensemble**, **Alertes marge** (10 opérations en alerte sur 68
  suffisamment engagées), **Rythme de vente** (simulateur de taux 2026),
  **Pilotage des prix** (lots hors marché + grille ajustée), **Qualité
  commerciale** (alerte de saisie par agence + recherche de dossiers
  similaires)
- Leçon de conduite de projet : première version « trop data science »
  (retour du commanditaire) → refondue en langage métier

**Visuel :** Figure 2.6 et/ou 2.7 du mémoire (captures des pages « Vue
d'ensemble » et « Alertes marge »).

**Discours :** SLIDE 11.

---

### Slide 12 — Réflexion transversale

**Contenu :**
- **« Un traducteur avant d'être un modélisateur »** : traduire une gêne
  métier en question calculable, puis un résultat statistique en
  information actionnable
- **Deux régimes de preuve, selon la nature du livrable :**
  - Réconciliation (les deux reprises) — la donnée est-elle bien arrivée ?
  - Validation statistique (Copilote Financier) — le résultat tient-il
    hors échantillon ?

**Visuel :** Figure 3.1 du mémoire (les trois régimes de preuve) — on peut
garder la figure complète telle quelle même si le discours n'évoque à
l'oral que les deux régimes les plus directement illustrés par les
projets présentés ; le troisième (recette par l'usage) reste visible sur
la figure sans être commenté verbalement, pour ne pas alourdir le texte.

**Discours :** SLIDE 12.

---

### Slide 13 — Perspectives et projet professionnel

**Contenu :**
- Entrée en master visant la modélisation prédictive stricte → sortie
  avec un projet plus large : construire et fiabiliser les chaînes de
  données qui rendent la décision possible, puis les outiller
- Cible à court terme : poste d'ingénieure données orientée aide à la
  décision, ou direction data structurée

**Visuel :** slide texte, bullets courts, pas de graphique.

**Discours :** SLIDE 13.

---

### Slide 14 — Conclusion

**Contenu :**
- Année dominée par la reconstruction d'un socle de données, avant retour
  à la modélisation statistique au second semestre
- Message final : un projet de données se joue avant le choix de
  l'algorithme
- Merci — ouverture aux questions

**Visuel :** slide de clôture sobre (« Merci — Questions »).

**Discours :** SLIDE 14.
