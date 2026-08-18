# Audit 1 — Chapitre 1 « La migration des tiers vers SPO »

*Réalisé par un relecteur à contexte neuf, sans historique de rédaction, confronté à la
consigne, à la note de synthèse SPO et au mémoire de mi-parcours. Ce rapport est reproduit
tel qu'il a été rendu ; la suite qui lui a été donnée figure en tête.*

## Suite donnée (rédigé après coup)

**Appliqué intégralement :**

- les deux défauts bloquants : la contradiction de volumétrie 1 602 / 1 557, et
  l'affirmation que les budgets avaient été migrés au premier semestre ;
- les onze affirmations non rattachables à la note de synthèse, retirées ou ramenées au
  texte de la note ;
- la comparaison illogique sur les 283 opérations ;
- le commentaire de la Figure 1.2, aligné sur ce que la capture montre réellement ;
- le décompte des manipulations interdites, porté de trois à quatre ;
- les cinq passages au ton tranchant ;
- la phrase de recul réflexif manquante en fin de 1.3.3 ;
- la glose fautive d'ADV et le développement de SPO à sa première occurrence ;
- l'ensemble des corrections de langue et de typographie, dont les espaces insécables.

**Non appliqué, et pourquoi :**

- *Déplacement de l'emplacement de capture n° 1* : la mention du panneau de contrôle a été
  retirée de la consigne en place plutôt que de déplacer la capture, qui illustre bien les
  trois mécanismes là où elle est. Le détail du panneau reste dans `Notes_synthese.md`.
- *Références croisées automatiques pour les numéros de figures* : les numéros restent
  écrits en clair, comme dans le mémoire de mi-parcours. `Notes_synthese.md` signale les
  occurrences à reprendre lors de l'insertion des trois captures.
- *Écart 881 couples / 872 requêtes PATCH* : aucune explication n'existe dans la note de
  synthèse. Rien n'a été inventé ; l'écart est consigné dans `Notes_synthese.md` avec la
  réponse à préparer pour la soutenance.

---

## 1. Verdict

Chapitre solide, conforme au sommaire imposé, fidèle dans l'ensemble à la note de synthèse
et au registre du mi-parcours ; les nombres et l'arithmétique sont exacts. Deux défauts
bloquants pour une soutenance : une **contradiction interne sur la volumétrie source
(1 602 vs 1 557)** visible à la fois dans le texte et entre deux figures, et l'affirmation
que **les budgets ont été migrés au premier semestre**, que le mi-parcours et le chapitre
lui-même démentent. S'y ajoutent une dizaine d'ajouts non rattachables à la note et
quelques formulations trop tranchantes à ramener au ton explicatif.

## 2. Contrôle de périmètre

Aucune trace du projet de data science du dépôt dans le corps du chapitre : le contrôle est
propre sur ce point. Sont rattachés à la note de synthèse : l'énoncé de l'enjeu ; tous les
compteurs (1 602, 1 557, 13 000, 553, 469, 538, 1 871, 1 434, 881, 462, 91, 40, 200, 872,
60 000) ; les trois clés d'unicité et la règle du rang 1 ; l'exclusion par les colonnes
AE/AF/AG et le code `T00012666` ; la numérotation séquentielle par destination ; les
contraintes de format (CSV UTF-8, ASCII, ligne d'en-tête unique, lots de 200 homogènes) ;
la procédure de rejeu ; les 872 requêtes JSON Patch en cinq lots ; les cas particuliers ;
les interdits d'usage et les quatre pièges Excel. La règle interdisant les tableaux de
procédure pas-à-pas est **respectée** : seule la logique est conservée.

Ajouts relevés comme non rattachables : « un prescripteur ou un fournisseur » ; le détail
des saisies manuelles à l'origine des 13 000 tiers ; la justification empirique des clés
S et T ; « qu'aucune documentation ne mentionnait » et « par rejets successifs » ; « produit
un fichier lu comme une colonne unique » ; la troisième option consistant à demander une
évolution à l'éditeur ; la finalité prêtée au découpage en cinq lots ; l'antériorité
d'usage de Postman ; « il a effectivement révélé plusieurs anomalies que rien d'autre
n'aurait signalées » ; « 283 opérations traitées » ; « notre système historique ».

## 3. Respect du sommaire

Conforme à la lettre. Les six sections et les sept sous-sections reprennent mot pour mot
les intitulés imposés, dans l'ordre et aux bons niveaux ; 1.5 et 1.6 sont bien sans
sous-section. L'encadré « Sommaire » d'ouverture reproduit fidèlement cette table. La
conclusion de chapitre et l'ouverture figurent bien en clôture, dans cet ordre.

## 4. Fidélité stylistique

Socle conforme : aucune incise entre tirets cadratins dans la prose, listes numérotées
systématiquement introduites par deux-points, enchaînement par démonstratif anaphorique,
accords féminins tenus, répartition « je » / « nous » cohérente avec la note.

Écarts relevés : ton tranchant sur cinq passages (« Ces trois mécanismes sont l'apport
méthodologique de ce travail », « Ce sont trois compétences d'ingénierie des données, et
non de saisie », « bien plus que la précédente reprise », « c'est ce qui compte pour la
suite ») ; deux adversatifs consécutifs en clôture ; généralisation assertive sur les
homonymes ; redondance de l'auto-qualification méthodologique ; absence de recul réflexif
en fin de 1.3.3 ; « ASCII pur » non explicité ; SPO jamais développé ; glose fautive d'ADV,
qui désigne le dossier de vente et non la personne (glossaire du mi-parcours, p. iv).

Temps verbaux conformes au mi-parcours : passé composé pour l'action, imparfait pour l'état
du système, présent pour le dispositif et le recul. Phrases brèves de scansion présentes et
bien dosées.

## 5. Figures

Numérotation conforme à l'ordre d'apparition (1.1 à 1.5) ; chaque figure est appelée
nommément **et** commentée dans le paragraphe qui la précède.

- **Figure 1.1** : conforme à la note (sections 3 et 4).
- **Figure 1.2** : la capture montre **huit** emplacements de fichiers — dont les RIB et les
  sites web — là où le texte en énumérait six. Le masquage du serveur et des identifiants
  est correct.
- **Figure 1.3** : 1 602 → −128 → 1 474 → −40 → 1 434, strictement conforme au texte.
- **Figure 1.4** : 1 871 / 1 434 / 1 434 / 553 / 538 / 469, conforme.
- **Figure 1.5** : 881 (61,4 %), 462 (32,2 %), 91 (6,3 %) ; le « plus de six tiers sur dix »
  du texte est exact.

Les trois emplacements de capture sont formatés à l'identique et immédiatement
identifiables. Réserve : la capture `BuilderTiers` demandait de montrer le panneau de
contrôle, introduit deux cents lignes plus loin.

## 6. Exactitude factuelle

Tous les nombres confrontés à la note sont exacts. Cohérence arithmétique vérifiée :
1 602 − 128 = 1 474 ; 1 474 − 40 = 1 434 ; 881 + 462 + 91 = 1 434. Cohérence supplémentaire
exacte et non signalée par le chapitre : 462 + 91 = 553, ce qui confirme la règle
« personnes physiques et morales seulement » pour les adresses.

Anomalies : la contradiction 1 602 / 1 557, importée telle quelle d'une incohérence interne
à la note ; l'écart entre 881 couples et 872 requêtes PATCH, non expliqué par la source ;
le décompte de trois manipulations interdites là où la note en liste quatre ; le libellé de
la colonne « Volume » du tableau de bilan pour la ligne PATCH.

## 7. Langue et typographie

Séparateurs de milliers en espace ordinaire, donc sécables. « explique que … se soit fait »
au lieu de l'indicatif. « de manière à ce que » à remplacer par « de sorte que ».
Répétition « coordonnées / coordonnées ». « produire » au lieu de « porter ». Antécédent
flottant sur « celles dont le courriel est renseigné ». Possessif inadapté sur « mes 1 602
lignes ». Anglicisme « matching » dans un emplacement de capture. Guillemets, espaces avant
les ponctuations doubles et accords : corrects, aucune faute relevée.

## 8. Défauts par ordre de gravité

1. **Contradiction sur la volumétrie source** — bloquant.
2. **Les budgets présentés comme migrés au premier semestre** — bloquant.
3. **Ajouts non rattachables à retirer** (onze occurrences).
4. **« 283 opérations traitées » et comparaison de volumétrie illogique.**
5. **Figure 1.2 : le texte ne dit pas ce que l'image montre.**
6. **Sous-décompte des interdits d'usage** (trois au lieu de quatre).
7. **Passages au ton tranchant** (cinq occurrences).
8. **Fin de 1.3.3 sans phrase de recul réflexif.**
9. **Emplacement de capture n° 1 mal calé.**
10. **Ouverture vers le chapitre 2 à vérifier** contre le chapitre 2 effectivement rédigé.
11. **Glose fautive d'ADV et acronyme SPO jamais développé.**
12. **Langue et typographie** (huit points).
