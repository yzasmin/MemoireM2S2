# Analyse des besoins métier — Copilote Financier

## 1. Utilisateurs cibles

| Utilisateur | Rôle | Décision à instrumenter |
|---|---|---|
| Direction financière | Pilote la marge consolidée du groupe | Où concentrer l'attention en revue de gestion trimestrielle ? |
| Responsable de programmes | Pilote 5-10 opérations | Mon opération dérive-t-elle ? Sur quels postes ? |
| Direction commerciale | Fixe grilles de prix et remises | Quel rythme de vente attendre ? Quelle remise accorder sans détruire la marge ? |
| Comité d'engagement | Valide les nouvelles opérations | Le budget proposé est-il réaliste au vu des opérations comparables ? |

## 2. Besoins par axe

### Axe A — Risque de dérive de marge

**Constat chiffré** (exploration, base au 2026-06) : sur les 144 opérations
suffisamment avancées (engagement > 30 % ou achevées), la variation
médiane entre marge budgétée et marge « engagée » est fortement négative ;
les dépassements se concentrent sur quelques postes (construction, frais
financiers). L'entreprise découvre souvent la dérive au moment de la
facturation, trop tard pour agir.

**Besoins** :
- B-A1 : score de risque par opération (probabilité de dérive de marge
  au-delà d'un seuil), mis à jour à chaque export de gestion ;
- B-A2 : classement des postes budgétaires qui expliquent la dérive
  (interprétabilité exigée : coefficients, pas de boîte noire seule) ;
- B-A3 : comparaison d'une opération à ses « voisines » (profil de coûts
  similaire) pour objectiver les revues de gestion.

**Réponse du copilote** : notebook 03 (régression du taux de variation,
classification du risque, importance des variables) + notebook 02
(similarité entre opérations, typologie) + page « Risque marge » de la
plateforme.

### Axe B — Vitesse d'écoulement

**Constat chiffré** : 14 428 réservations 2016-2026 ; le rythme mensuel
groupe est passé d'environ 150/mois (2021-2022) à moins de 115/mois (2023)
en pleine remontée des taux (1,1 % → 4 %) ; 2 157 désistements dont 45 %
pour problème de financement / refus de prêt — le lien taux → demande est
au cœur du besoin.

**Besoins** :
- B-B1 : prévision du nombre de réservations par mois et par opération à
  horizon 6-12 mois, sous scénarios de taux 2026 (statu quo ~3,1 %, baisse
  à 2,5 %, remontée à 3,5 %) ;
- B-B2 : quantifier l'effet propre de l'opération (localisation, produit,
  prix) vs l'effet conjoncture — c'est exactement la décomposition
  intra/inter d'un modèle à effets aléatoires ;
- B-B3 : estimer le délai d'écoulement complet d'un programme (courbe
  cumulée) pour caler les échéanciers de trésorerie.

**Réponse du copilote** : notebook 04 (panel à effets aléatoires, ARIMAX
avec exogènes macro, courbe logistique d'écoulement) + page « Écoulement »
de la plateforme avec simulateur de scénarios de taux.

### Axe C — Optimisation des prix

**Constat chiffré** : les prix au m² varient de 1 à 3 au sein d'une même
commune ; les remises commerciales sont hétérogènes (0 à >5 % du prix) et
non corrélées au délai de vente constaté — signe d'une politique de remise
non pilotée.

**Besoins** :
- B-C1 : prix « de marché » attendu d'un lot compte tenu de ses
  caractéristiques (surface, étage, exposition, commune, produit) ;
- B-C2 : recommandation d'ajustement pour le stock restant : maximiser le
  revenu attendu sous contrainte d'écouler avant une date cible et de
  préserver la marge minimale de l'opération ;
- B-C3 : signaler les lots sur- ou sous-cotés par rapport au modèle
  (résidus extrêmes).

**Réponse du copilote** : notebook 05 (modèle hédonique, élasticité
prix-demande, optimisation sous contrainte) + page « Prix » de la
plateforme.

### Axe transverse — Signaux faibles (texte et réseau)

**Besoins** :
- B-T1 : exploiter les 9 688 commentaires libres de vente (mentions de
  refus de prêt, de remises cachées « prix hors pack », de contentieux)
  comme signal précoce de désistement ;
- B-T2 : cartographier le réseau vendeurs ↔ opérations pour identifier les
  vendeurs pivots et les dépendances commerciales.

**Réponse du copilote** : notebook 06 (TF-IDF, classification des motifs,
graphe biparti).

## 3. Exigences non fonctionnelles

- **Reproductibilité** : tout se reconstruit depuis les exports bruts par
  `python src/base_sql.py` ; les notebooks tournent sur Google Colab.
- **Interprétabilité** : chaque score affiché dans la plateforme est
  accompagné des variables qui le déterminent.
- **Confidentialité** : les données clients (noms, dates de naissance) ne
  sont jamais affichées dans la plateforme ni utilisées comme variables ;
  seules des variables agrégées (âge, département) sont dérivées.
- **Petit échantillon assumé** : validation croisée systématique, métriques
  rapportées avec leur dispersion, pas de deep learning au-delà de la
  démonstration pédagogique (ReLU).
