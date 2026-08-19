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

## Régénérer le contenu depuis les sources

Les fichiers de `latex/chapters/` ne se modifient pas à la main : ils sont
produits à partir des sources R Markdown de `memoire/`. Depuis la racine du
dépôt :

    python3 rendu/vers_gabarit.py

Le script convertit chaque source, recopie les figures, compile trois fois et
dépose le résultat à la racine sous `memoire_M2_saoud.pdf`.

## Ce qui a été modifié dans le gabarit

- `manuscript.tex` : titre, auteur et date ; `\graphicspath` élargi pour que
  les figures soient trouvées quel que soit le dossier de compilation ; corps
  du document réécrit pour appeler les quatre nouveaux chapitres ;
  bibliographie remplacée par les six références appelées dans le texte.
- `front_page.tex` : intitulé « Mémoire de fin d'études », titre et sous-titre
  du mémoire, mois de soutenance, résumé et mots-clés à jour. Les espacements
  ont été resserrés et le logo Angelotti ramené à la hauteur des deux autres
  pour que la page tienne en une seule.
- `chapters/` et `figures/` : contenu du mi-parcours remplacé.

Le préambule LaTeX — classe, marges, interligne, paquets — est celui d'origine.
