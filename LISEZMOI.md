# Gabarit officiel — mémoire de fin d'études

Ce dossier reprend le gabarit LaTeX fourni par les enseignants, celui déjà
utilisé pour le mémoire de mi-parcours. Son préambule, sa page de titre et sa
mise en page n'ont pas été refaits : seuls le contenu et les métadonnées ont
été remplacés.

## Compiler

Sur Overleaf : téléverser ce dossier, désigner `latex/manuscript.tex` comme
fichier principal, compiler avec pdfLaTeX. C'est la configuration d'origine du
gabarit, dans laquelle le dossier du fichier principal est ajouté au chemin de
recherche.

En local, depuis ce dossier :

    TEXINPUTS=".//:./latex//:" pdflatex latex/manuscript.tex   # trois fois

Trois passes sont nécessaires : la table des matières, les minitocs, la liste
des figures et les renvois `\ref` ne se stabilisent qu'à la troisième.

## Modifier le contenu

Les fichiers de `latex/chapters/` sont la source : ils s'éditent directement,
il n'y a pas d'étape de génération intermédiaire.

## Structure du manuscrit

| Fichier | Contenu |
|---|---|
| `chapters/abstract.tex` | Remerciements et résumé |
| `chapters/introduction.tex` | Introduction |
| `chapters/chapter_1.tex` | Contexte et enjeux, problématique, outils |
| `chapters/chapter_2.tex` | Mission 1 : la reprise des données vers SPO |
| `chapters/chapter_3.tex` | Mission 2 : le Copilote Financier |
| `chapters/chapter_4.tex` | Activités complémentaires (reporting, SSO) |
| `chapters/chapter_5.tex` | Organisation, compétences et prise de recul |
| `chapters/conclusion.tex` | Conclusion |
| `chapters/glossaire.tex` | Glossaire, en deux parties (métier / technique) |

Les figures sont numérotées d'après le chapitre où elles apparaissent
(`fig_<chapitre>_<rang>_<nom>.png`) et appelées par `\ref`, jamais par un
numéro écrit en dur : renuméroter un chapitre ne casse donc pas les renvois.
