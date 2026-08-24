# Plan des slides — soutenance Copilote Financier

17 slides, calibrées pour **25 minutes** à l'oral. Répartition volontaire
du temps de parole : **≈ 30 % sur les deux reprises de données (missions
d'alternance, slides 2-6), ≈ 70 % sur le Copilote Financier (slides
8-14)** — c'est la partie data science, et c'est elle que le jury attend
en profondeur. Une entrée par slide : titre, contenu (bullets ou visuel du
mémoire/repo à reprendre), et la portion de `discours_soutenance.md` qui
lui correspond. En cas de divergence entre ce fichier et le `.pptx`
généré en complément, **ce fichier fait foi**.

**Calibrage actuel :** 3 220 mots utiles → 23,0 à 24,8 minutes selon le
débit (130-140 mots/minute), ratio réel 32,5 % / 67,5 %.

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

### Slide 2 — Contexte Angelotti

**Contenu :**
- Groupe Angelotti — promoteur-aménageur, filiale Nexity, deux métiers
  (promotion / aménagement)
- Chaque opération = une société dédiée ; budget posé à l'engagement, qui
  dérive au fil du chantier et des ventes (appels d'offres, rythme de
  vente, désistements, remises au cas par cas)
- Aujourd'hui : suivi opération par opération, sur tableurs, sans vision
  transverse — le constat qui motive les deux projets présentés

**Visuel :** schéma du système d'information (Figure 1.1 du mémoire).

**Discours :** SLIDE 2.

---

### Slide 3 — La migration des opérations

**Contenu :**
- L'événement de l'année : migration de l'ERP Grimmo vers SPO
  (changement de modèle de données, pas seulement d'outil)
- 283 opérations à recréer — automatisation par API + traitement manuel
  des cas hors gabarit
- Deux règles ERP non documentées, découvertes en creusant les erreurs :
  ordre d'injection strict, identifiants non stables
- Validation par paliers (3 pilotes → 12 → masse), déploiement en
  « coquilles vides »
- **283 opérations créées dans SPO à la fin du semestre**

**Visuel :** Figure 1.2 du mémoire (séquence d'injection imposée par
l'intégrité référentielle de l'ERP).

**Discours :** SLIDE 3.

---

### Slide 4 — La reprise des tiers : le problème

**Contenu :**
- Second semestre : reconstituer le référentiel client (« tiers » dans
  SPO) — 1 557 ventes + 1 602 lignes de coordonnées issues du CRM
- Le piège : une ligne = un achat, pas un client
- ~13 000 tiers déjà présents dans SPO
- Enjeu : créer chaque client une fois, sans contrôle manuel ligne à
  ligne

**Visuel :** slide texte, pas de graphique nécessaire.

**Discours :** SLIDE 4.

---

### Slide 5 — La reprise des tiers : la solution et les résultats

**Contenu :**
- **Trois clés d'unicité différenciées selon la nature du tiers** (couple
  / personne physique / personne morale) — calcul d'un rang plutôt qu'une
  suppression, pour rester traçable
- Résultat chiffré : 1 602 → −128 doublons internes → 1 474 uniques → −40
  déjà présents → **1 434 tiers créés** (881 couples, 462 personnes
  physiques, 91 personnes morales), **zéro doublon détecté**
- 872 requêtes API (5 lots) pour les coordonnées des couples, toutes
  exécutées sans erreur ; 9 cas particuliers traités à la main

**Visuel :** Figure 1.4 du mémoire (entonnoir 1 602 → 1 434) et Figure 1.5
(répartition par nature) si la place le permet.

**Discours :** SLIDE 5.

---

### Slide 6 — Ce que ces deux reprises ont en commun

**Contenu :**
- Même méthode : avancer par paliers quand le modèle cible n'est pas
  connu à l'avance ; un rejet = une information, pas une erreur
- Les deux répondent à la même question : la donnée est-elle bien
  arrivée ? → **régime de preuve de la réconciliation**
- Angle mort assumé : prouve que la donnée est arrivée, pas qu'elle est
  juste

**Visuel :** slide texte courte, transition conceptuelle vers la
réflexion de la fin (slide 15).

**Discours :** SLIDE 6.

---

### Slide 7 — Vers le Copilote Financier

**Contenu :**
- Une fois le socle reconstitué : que peut-on en tirer pour la décision ?
- **Transition vers le second projet de l'année : le Copilote Financier**

**Visuel :** slide de transition, minimaliste.

**Discours :** SLIDE 7.

---

### Slide 8 — Le Copilote Financier : contexte, données et méthode

**Contenu :**
- Trois questions : quelles opérations dérapent ? à quel rythme le stock
  s'écoule-t-il ? à quel prix vendre chaque lot ?
- Données : 4 exports du système de gestion + 3 sources externes (taux
  BCE, confiance des ménages Eurostat, référentiel communes)
- Adossé à **267 opérations réelles** et **7 programmes d'analyse**
- **Boîte à outils volontairement diverse** : typologie non supervisée,
  régression et classification, séries temporelles, optimisation sous
  contrainte, fouille de texte et analyse de réseau
- **Principe transversal affirmé à l'oral** : validation croisée
  systématique, jamais de résultat retenu sur sa seule performance
  d'ajustement

**Visuel :** tableau à 3 lignes (Axe / Question / Famille de modèles),
repris du mémoire (section 2.1.2 / `docs/01_cadrage_projet.md`).

**Discours :** SLIDE 8.

---

### Slide 9 — Exploration des données : deux leçons

**Contenu :**
- Prix au m² très asymétrique → quasi normal après log-transformation →
  l'axe C modélise le log-prix
- Piège repéré : la corrélation brute réservations / taux de crédit est
  quasi nulle — la croissance du portefeuille maquille la relation
- Corrigée par opération active, la corrélation redevient nette et
  négative — cette correction structure toute la démarche de l'axe B
- Leçon assumée à l'oral : toujours vérifier la sortie réelle plutôt que
  la conclusion attendue

**Visuel :** Figure 2.1 du mémoire (distribution du prix, brute puis log)
et Figure 2.2 (intensité de vente, effet des taux visible une fois
l'effet de portefeuille neutralisé).

**Discours :** SLIDE 9.

---

### Slide 10 — Axe A : le risque de marge

**Contenu :**
- Périmètre : 123 opérations suffisamment avancées (engagement ≥ 60 %) —
  **28 % en dérive matérielle** (> 2 % de la marge budgétée)
- Régression du taux de dérive : R² test = 0,08 → bascule en
  classification « à risque / non »
- **Comparaison de six méthodes en validation croisée (métrique F1)** :
  logistique 0,283 · SVM linéaire 0,303 · SVM RBF 0,257 · arbre 0,340 ·
  **forêt aléatoire 0,306 (retenue)** · réseau de neurones (MLP) 0,913 en
  apprentissage mais **0,262 en validation — sur-apprentissage démonstratif**
- Régression Ridge en complément (facteurs de dérive lisibles)
- **ACP** : 2 axes résument **61 %** de la structure des coûts (vérifié
  par SVD) → typologie de 4 familles d'opérations (résidentiel classique,
  aménagement foncier, promotion sur foncier allégé, aménagement lourd
  VRD) → comparateur de « voisines » ; exemple nommé : Le Parc des
  Cyclades (marge budgétée +6,5 %, voisines à +7,9 % / +11,3 %)
- Message assumé : signal réel mais faible

**Visuel :** Figure 2.3 du mémoire (distribution de la variation de
marge) + petit tableau des 6 F1 par méthode, duo train/validation du MLP
mis en évidence.

**Discours :** SLIDE 10. **Slide la plus dense en méthode.**

---

### Slide 11 — Axe B : la vitesse d'écoulement

**Contenu :**
- Panel de 3 230 observations (opération × mois, 160 opérations) — modèle
  à effets aléatoires
- **2/3 de la variance du rythme = effet propre à l'opération, 1/3 =
  conjoncture**
- **+1 point de taux de crédit ⇒ −19 % de réservations mensuelles**
  (p < 10⁻¹⁵)
- Contrôle par série temporelle (ARIMA, 114 mois) : effet non
  identifiable isolément — validation méthodologique, pas un échec
- Scénarios 2026 : détente à 2,5 % → **+6 %** ; remontée à 3,5 % → **−3 %**
- Courbe logistique par opération : bat un ajustement linéaire sur 25/28
  opérations terminées, délai médian de 20 mois pour 90 % du potentiel

**Visuel :** Figure 2.4 du mémoire (scénarios de taux 2026).

**Discours :** SLIDE 11. **Axe le plus solide — à assumer clairement
comme tel à l'oral.**

---

### Slide 12 — Axe C : l'optimisation des prix

**Contenu :**
- Modèle hédonique sur 5 064 appartements vendus depuis 2016 — **R² test
  = 0,886, erreur type ≈ 11 %**
- Primes cohérentes : étage +6,0 %, sud +2,6 %, social −62,8 %, millésime
  +19-21 % (2016→2023/2026, plateau après 2022)
- Appliqué au stock (127 appartements) : **24 lots hors marché**
- Élasticité non significative en interne (p = 0,57, n = 95) → fixée
  prudemment à ε = −1
- **Lagrange + vérification par un second solveur (SLSQP), convergence à
  0,006 près** : remise optimale **identique en euros** sur tous les lots
  — exemple nommé : opération Arpeggio (18 lots, 166-461 k€), +8 % de
  ventes visé → ajustements de −5 % à −14 % selon le lot, ≈ 23 k€
  constants

**Visuel :** tableau des résultats clés (R², lots hors marché, règle de
remise, exemple Arpeggio).

**Discours :** SLIDE 12.

---

### Slide 13 — Signaux faibles : texte et réseau de vente

**Contenu :**
- 9 688 commentaires libres de vente : moteur de recherche par
  similarité (TF-IDF sur corpus dédupliqué de 1 346 documents, 535
  termes)
- Prédiction du désistement par le texte, fuite contrôlée (314
  commentaires écartés) : Naive Bayes F1 = 0,343, préféré à une
  régression logistique quasi muette
- Divergence de Kullback-Leibler : révèle un défaut de saisie sur une
  agence (90 % de motifs « autres »)
- Réseau biparti vendeurs-opérations (209 vendeurs ≥ 3 dossiers, 98,8 %
  des dossiers couverts, 104 opérations, 711 arêtes) : deux pivots
  concentrent **51,6 % des dossiers**, désistement 9,0 % vs 29,6 %

**Visuel :** trois cartes chiffrées (F1 texte, concentration réseau,
contraste des taux de désistement) — pas de figure extraite du mémoire
pour cette slide.

**Discours :** SLIDE 13.

---

### Slide 14 — La plateforme : cinq pages pour la direction financière

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

**Discours :** SLIDE 14.

---

### Slide 15 — Réflexion transversale

**Contenu :**
- **« Un traducteur avant d'être un modélisateur »** : traduire une gêne
  métier en question calculable, puis un résultat statistique en
  information actionnable
- **Trois régimes de preuve, selon la nature du livrable :**
  - Réconciliation (les deux reprises, cf. slide 6) — la donnée est-elle
    bien arrivée ?
  - Recette par l'usage (maintien des tableaux de bord, déploiement SSO)
    — la personne s'en sert-elle, pour la bonne chose ?
  - Validation statistique (Copilote Financier) — le résultat tient-il
    hors échantillon ?
- « Documenter est un acte technique » : la note sur la séquence
  d'injection réutilisée deux mois après pour la reprise des tiers

**Visuel :** Figure 3.1 du mémoire (les trois régimes de preuve) — reprise
telle quelle, elle correspond maintenant exactement aux trois régimes
évoqués à l'oral.

**Discours :** SLIDE 15.

---

### Slide 16 — Perspectives et projet professionnel

**Contenu :**
- Entrée en master visant la modélisation prédictive stricte → sortie
  avec un projet plus large : construire et fiabiliser les chaînes de
  données qui rendent la décision possible, puis les outiller
- Trois compétences à tenir ensemble : ingénierie des données /
  modélisation proportionnée / dialogue avec les métiers
- Cible à court terme : poste d'ingénieure données orientée aide à la
  décision, ou direction data structurée

**Visuel :** slide texte, 3 bullets courts, pas de graphique.

**Discours :** SLIDE 16.

---

### Slide 17 — Conclusion

**Contenu :**
- Année dominée par la reconstruction d'un socle de données, avant retour
  à la modélisation statistique au second semestre
- Message final : un projet de données se joue avant le choix de
  l'algorithme
- Merci — ouverture aux questions

**Visuel :** slide de clôture sobre (« Merci — Questions »).

**Discours :** SLIDE 17.
