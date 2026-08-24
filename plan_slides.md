# Plan des slides — soutenance Copilote Financier

14 slides. Une entrée par slide : titre, contenu (bullets ou visuel du
mémoire à reprendre), et la portion de `discours_soutenance.md` qui lui
correspond. En cas de divergence entre ce fichier et un `.pptx` généré en
complément, **ce fichier fait foi**.

---

### Slide 1 — Titre

**Titre affiché :** Le Copilote Financier — Groupe Angelotti
**Sous-titre :** Reprise de données, reporting et aide à la décision —
Yasmina Saoud, Master MIASHS, alternance Groupe Angelotti

**Contenu visuel :** page de garde sobre — logo/nom Angelotti, nom du
master, jury (tutrice entreprise, tutrice pédagogique, membre expert),
date de soutenance. Pas de bullet.

**Discours :** SLIDE 1.

---

### Slide 2 — Contexte Angelotti et enjeu de l'année

**Contenu :**
- Groupe Angelotti — promoteur-aménageur, Occitanie + PACA, filiale Nexity
- Deux métiers : promotion (construire et vendre) / aménagement (viabiliser
  du foncier)
- Chaque opération = une société dédiée ; budget posé à l'engagement, puis
  dérive au fil du chantier et des ventes
- **L'événement de l'année : migration de l'ERP Grimmo vers SPO**
  (changement de modèle de données, pas seulement d'outil)

**Visuel :** reprendre le schéma du système d'information (Figure 1.1 du
mémoire — outils du SI et circulation de la donnée), version simplifiée.

**Discours :** SLIDE 2.

---

### Slide 3 — La migration des opérations

**Contenu :**
- 283 opérations immobilières à recréer dans SPO — saisie manuelle exclue
- Méthode : automatisation via API pour le volume, traitement manuel pour
  les cas hors gabarit
- Deux règles ERP non documentées, découvertes en creusant les erreurs :
  - ordre d'injection strict (opération → tranches travaux → tranches
    commerciales → budget)
  - identifiants non stables (toujours interroger la version la plus
    récente)
- Stratégie de déploiement en « coquilles vides » (structure d'abord,
  détail budgétaire ensuite) pour ne pas interrompre la facturation
- **Fin de semestre : 283 opérations créées dans SPO**

**Visuel :** Figure 1.2 du mémoire (séquence d'injection imposée par
l'intégrité référentielle de l'ERP).

**Discours :** SLIDE 3.

---

### Slide 4 — La reprise des tiers : le problème du doublon

**Contenu :**
- Second semestre : reconstituer le référentiel client (« tiers » dans SPO)
- Matière première : 1 557 lignes de ventes + **1 602 lignes de
  coordonnées** (CRM Vadimm)
- Le piège : une ligne = un achat, pas un client (un client fidèle apparaît
  plusieurs fois)
- SPO n'était pas vide : ~13 000 tiers déjà présents
- **Enjeu : créer chaque client une fois et une seule, sans contrôle
  manuel ligne à ligne**

**Visuel :** aucun graphique nécessaire — slide texte, appuyé par la
formulation du problème.

**Discours :** SLIDE 4.

---

### Slide 5 — La reprise des tiers : la solution et les résultats

**Contenu :**
- Fichier de travail piloté par formules : la décision d'importer une
  ligne est calculée, pas prise au cas par cas
- **Trois clés d'unicité différenciées selon la nature du tiers** (couple /
  personne physique / personne morale) — le cœur méthodologique du travail
- Résultat chiffré : 1 602 lignes → −128 doublons internes → 1 474
  uniques → −40 déjà présents dans SPO → **1 434 tiers créés**
- Répartition : 881 couples, 462 personnes physiques, 91 personnes morales
- **Zéro doublon détecté par les trois clés retenues**
- Contrainte technique résolue par API : 872 requêtes PATCH pour les
  coordonnées des couples, toutes exécutées sans erreur

**Visuel :** Figure 1.4 du mémoire (entonnoir 1 602 → 1 434) ; Figure 1.5
en appui si la place le permet (répartition des 1 434 tiers par nature).

**Discours :** SLIDE 5.

---

### Slide 6 — Vers le Copilote Financier

**Contenu :**
- Les deux reprises répondent à une question : la donnée est-elle bien
  arrivée ?
- Le socle reconstitué permet de se poser une question différente : que
  peut-on en tirer pour la décision ?
- **Transition vers le second projet de l'année : le Copilote Financier**

**Visuel :** slide de transition, minimaliste (une phrase, pas de bullet
dense).

**Discours :** SLIDE 6.

---

### Slide 7 — Le Copilote Financier : contexte et trois axes

**Contenu :**
- Constat : la direction financière suit ses dérives opération par
  opération, sur tableurs, sans vision transverse
- Trois questions récurrentes en comité d'engagement :
  - Quelles opérations dérapent ? → **Axe A**
  - À quel rythme le stock s'écoule-t-il ? → **Axe B**
  - À quel prix vendre chaque lot ? → **Axe C**
- Adossé à 267 opérations réelles et 7 notebooks exécutés

**Visuel :** tableau à 3 lignes (Axe / Question / Famille de modèles),
repris du mémoire (tableau section 2.1.2 / docs/01_cadrage_projet.md).

**Discours :** SLIDE 7.

---

### Slide 8 — Axe A : le risque de marge

**Contenu :**
- Périmètre : 123 opérations suffisamment avancées (engagement ≥ 60 %)
- **28 % dépassent déjà leur budget de plus de 2 %** (seuil de dérive
  matérielle) ; 2 cas extrêmes dépassent 50 % de la marge budgétée
- Régression du taux de dérive : R² test = 0,08 (résultat modeste)
- Bascule en classification « à risque / non » — métrique F1 (équilibre
  détection / fausses alertes, imposée par le déséquilibre des classes)
- **F1 ≈ 0,30 (forêt aléatoire retenue) contre 0 pour la référence
  naïve**
- Message assumé : signal réel mais faible — la structure budgétaire
  prédispose, elle ne détermine pas

**Visuel :** Figure 2.3 du mémoire (distribution de la variation de marge
« committée », seuil de dérive à −2 %).

**Discours :** SLIDE 8.

---

### Slide 9 — Axe B : la vitesse d'écoulement

**Contenu :**
- Panel de 3 230 observations (opération × mois, 160 opérations)
- Modèle à effets aléatoires : **2/3 de la variance = effet propre à
  l'opération, 1/3 = conjoncture** (ICC = 0,66)
- **+1 point de taux de crédit ⇒ −19 % de réservations mensuelles**
  (p < 10⁻¹⁵, très significatif)
- Contrôle de robustesse par série temporelle (ARIMA) sur la série
  agrégée : effet du taux non identifiable isolément (p = 0,82) — lu comme
  une validation méthodologique (pas de corrélation fallacieuse), pas un
  échec
- Scénarios 2026 (combinant trajectoire ARIMA + élasticité du panel) :
  détente à 2,5 % → **+6 % de rythme** ; remontée à 3,5 % → **−3 %**

**Visuel :** Figure 2.4 du mémoire (prévision d'intensité de vente à douze
mois sous trois scénarios de taux, intervalle à 80 %).

**Discours :** SLIDE 9. **Axe le plus solide — à assumer clairement comme
tel à l'oral.**

---

### Slide 10 — Axe C : l'optimisation des prix

**Contenu :**
- Modèle hédonique (prix = somme de caractéristiques valorisées
  séparément) sur 5 064 appartements vendus depuis 2016
- **R² test = 0,886, erreur type ≈ 11 %**
- Appliqué au stock (127 appartements) : 24 lots hors marché (16
  sous-cotés, 8 surcotés)
- Élasticité prix-demande non significative en interne (p = 0,57 sur 95
  opérations) → retenue à ε = −1, valeur prudente issue de la littérature,
  documentée plutôt que masquée
- **Résultat contre-intuitif : la remise optimale est un montant identique
  en euros sur tous les lots, donc un % plus fort sur les petits lots** —
  à l'inverse de la pratique actuelle au cas par cas

**Visuel :** tableau des 3 résultats clés (R², lots hors marché, règle de
remise) — c'est l'option retenue dans le `.pptx` généré, car le discours
ne nomme aucune opération précise. Variante possible : schéma avant/après
remise sur l'opération d'application (Arpeggio, 18 lots) — mais alors
nommer aussi l'opération dans le discours pour que la slide et l'oral se
correspondent.

**Discours :** SLIDE 10.

---

### Slide 11 — La plateforme : cinq pages pour la direction financière

**Contenu :**
- Application Streamlit, périmètre 147 opérations de promotion, 5 pages
  testées individuellement
- **Vue d'ensemble** : 147 opérations suivies, 421 lots en stock, rythme
  récent
- **Alertes marge** : 68 opérations en cours suffisamment engagées → 10 en
  alerte
- **Rythme de vente** : simulateur — un curseur de taux 2026 donne le
  rythme attendu
- **Pilotage des prix** : lots hors marché + grille ajustée recommandée
- **Qualité commerciale** : alerte sur une agence (90 % de désistements
  mal catégorisés = défaut de saisie) + recherche de dossiers similaires
- Leçon de conduite de projet : première version « trop data science »
  (retour du commanditaire) → refondue en langage métier, sans jargon
  statistique à l'écran

**Visuel :** Figure 2.6 et/ou 2.7 du mémoire (captures des pages « Vue
d'ensemble » et « Alertes marge »).

**Discours :** SLIDE 11.

---

### Slide 12 — Réflexion transversale

**Contenu :**
- **« Un traducteur avant d'être un modélisateur »** : traduire une gêne
  métier en question calculable, puis un résultat statistique en
  information actionnable
- **Trois régimes de preuve, selon la nature du livrable :**
  - Réconciliation (les deux reprises) — la donnée est-elle bien arrivée ?
  - Recette par l'usage (maintien des tableaux de bord, accès utilisateurs)
    — la personne s'en sert-elle ?
  - Validation statistique (Copilote Financier) — le résultat tient-il
    hors échantillon ?

**Visuel :** Figure 3.1 du mémoire (les trois régimes de preuve selon la
nature du livrable) — reprendre le schéma tel quel, c'est la synthèse
visuelle du mémoire.

**Discours :** SLIDE 12.

---

### Slide 13 — Perspectives et projet professionnel

**Contenu :**
- Entrée en master visant la modélisation prédictive stricte → sortie avec
  un projet plus large : construire et fiabiliser les chaînes de données
  qui rendent la décision possible, puis les outiller
- Trois compétences à tenir ensemble : ingénierie des données / modélisation
  proportionnée / dialogue avec les métiers
- Cible à court terme : poste d'ingénieure données orientée aide à la
  décision, ou direction data structurée

**Visuel :** slide texte, 3 bullets courts, pas de graphique.

**Discours :** SLIDE 13.

---

### Slide 14 — Conclusion

**Contenu :**
- Année dominée par la reconstruction d'un socle de données, avant retour
  à la modélisation statistique au second semestre
- Message final : un projet de données se joue avant le choix de
  l'algorithme — quand on décide ce qu'est un client, une marge, ou ce que
  contient vraiment un fichier
- Structurer et modéliser une donnée : deux moments du même travail
- Merci — ouverture aux questions

**Visuel :** slide de clôture sobre (« Merci — Questions »).

**Discours :** SLIDE 14.
