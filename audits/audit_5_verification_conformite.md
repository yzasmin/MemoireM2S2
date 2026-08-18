<!--
Vérification de conformité produite par un second sous-agent à contexte neuf, qui n'avait
participé ni à la rédaction ni à l'audit 4. Sa mission n'était pas de refaire un audit, mais
de vérifier remarque par remarque que la suite annoncée dans `audit_4_manuscrit_complet.md`
avait réellement été appliquée, puis de contrôler le périmètre, les régressions et le style.
Le rapport intégral n'est pas reproduit ici ; ce fichier en consigne le verdict et la suite.
-->

# Vérification de conformité de l'audit 4 — verdict et suite

## Verdict du relecteur

Vingt-deux remarques sur vingt-neuf réellement appliquées et vérifiables dans le PDF. Trois
écarts déclarés jugés recevables et correctement consignés. **Cinq remarques annoncées comme
appliquées ne l'étaient que partiellement**, et surtout : **quatre phrases du chapitre 2
énonçaient des faits qu'aucune source ne porte**, dont une anecdote entièrement inventée.

Ce dernier point est le seul grave, parce qu'il contrevient à la règle de périmètre posée dès
la commande : le périmètre de ce que dit le mémoire est fixé par les sources, pas par ce qui
est plausible.

## Suite donnée

### Le dépassement de périmètre du chapitre 2 — corrigé

| Passage | Ce que disait le manuscrit | Ce que disent les sources | Suite |
|:---|:---|:---|:---|
| Raison d'avoir rédigé la documentation interne | « j'avais constaté que je redécouvrais deux fois la même contrainte, à quelques jours d'intervalle » | rien | **Supprimé**, remplacé par « les règles que les codes d'erreur m'avaient révélées n'existaient nulle part ailleurs que dans mes notes de test » |
| Fichiers de mapping | « relevait alors d'un arbitrage, tranché avec les services concernés puis consigné » | « des fichiers de mapping que j'ai constitués » | **Supprimé** ; ne subsiste que la distinction entre tables extraites de SPO et fichiers constitués |
| Usage de la maquette | « la responsable concernée pouvait ouvrir la maquette, voir la formule et pointer la ligne fautive » | rien | **Supprimé** |
| Valeurs contrôlées | « un libellé de poste budgétaire, un type de tranche, une nature d'opération y sont des valeurs contrôlées » | « la nomenclature stricte de SPO » | **Reformulé** : « doit correspondre à une valeur que le nouveau système reconnaît » |
| Documentation de l'éditeur | « elle n'était pas documentée du tout » (contredisant « pas explicite » une page plus loin) | « pas explicite dans la documentation technique » | **Aligné** sur la source |
| Écart 283 / 267, chapitre 5 | « la migration portant sur les dossiers actifs à reprendre » | rien | **Supprimé** ; ne subsiste que ce qui est établi : deux extractions, deux dates, un critère de budget analytique |

Le chapitre 2 gagne désormais environ quatre cents mots au lieu des cinq cent cinquante
mesurés avant correction. L'audit 4 en demandait six à huit cents. L'écart est assumé : les
sources ne portent pas de quoi écrire davantage sans recommencer la même faute.

### Les autres corrections appliquées

- **Tableau consolidé du chapitre 6** : « Opérations créées dans SPO, hors budgets détaillés
  | 283 », qui contredisait jusque-là la réserve posée aux chapitres 1 et 2.
- **Concordance des temps de la section 4.1.3** : les deux verbes que l'audit 4 nommait
  explicitement, « doit » et « attribue », sont passés à l'imparfait ; seul l'énoncé de la
  règle reste au présent, et le texte le signale.
- **Description de la figure 1.1** : elle comptait trois boîtes en haut du schéma, qui en
  porte quatre, et trois traits pointillés, qui sont quatre.
- **Adresses étrangères** : « dont un en Allemagne et un aux Émirats arabes unis », le pays du
  troisième tiers n'étant pas documenté.
- **Écart 1 557 / 1 602** : signalé dans le corps du chapitre 3, avec la justification de la
  retenue du plus large des deux totaux et une hypothèse annoncée comme telle.
- **Répétition d'attaque** en section 3.5 : « Trois autres tiers étaient renseignés… ».
- **Glossaire** : ordre alphabétique rétabli après l'ajout de Grimmo et de MyReport, et entrée
  *Dashboard* ajoutée, puisque le titre 5.1.2 conserve le mot.
- **Référence [1]**, appelée nulle part, l'est désormais au chapitre 7. La référence [2] est
  retitrée pour correspondre à l'URL qu'elle porte. Les six références sont appelées.
- **Séparateur des titres d'axes** ramené au deux-points employé partout ailleurs.
- **Reformatage** des vingt-et-un paragraphes de prose restés hors du gabarit de 96 colonnes.

### Ce qui n'a pas été suivi

**La déclaration incomplète de D7.** Le relecteur a raison : le tableau de suite de l'audit 4
ramenait D7 à deux objets alors que la remarque en portait sept. Les quatre autres — titre du
chapitre, titres 5.4 et 5.5, suppression de la section numérotée 5.7 — relèvent du même motif
que le volet déclaré écarté : ce sommaire est celui que l'autrice a imposé, avec la consigne
de ne pas en modifier l'ordre ni la numérotation. Ils sont donc écartés eux aussi, et le sont
désormais explicitement.

**Le style essayiste des ajouts.** Le relecteur signale, à juste titre, que « Mapper un champ
n'est pas le renommer » et la maxime finale sur les contraintes techniques écrites relèvent
d'un registre sentencieux. La maxime a disparu avec la réécriture du passage. La formule
d'attaque, elle, a été supprimée dans le même mouvement. Le chapitre 2 revient ainsi au
registre descriptif du mi-parcours.

### Ce qui reste, et qui n'appartient qu'à l'autrice

Les trois encadrés « À insérer — figure » du chapitre 3, et la confidentialité des figures
2.1, 5.8 et 5.9. Ces deux points figuraient dans la colonne « appliquée » du tableau de
l'audit 4 alors qu'ils n'ont produit aucune modification du document, ce qui était trompeur
et que le relecteur a relevé. Ils sont des décisions, pas des corrections : voir les sections
4 et 6 de `Notes_synthese2.md`.

### État du manuscrit après cette passe

74 pages, 7 chapitres, 21 figures toutes appelées et légendées en PDF comme en Word, 6
références toutes appelées, aucun encadré éditorial hors des trois emplacements de figures
réservés. Médianes de longueur de phrase par chapitre entre 17 et 23,5 mots contre 22 pour le
mémoire de mi-parcours, aucune incise entre tirets cadratins dans la prose.
