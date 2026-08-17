#!/usr/bin/env bash
# Rend les deux chapitres du mémoire en PDF et en DOCX à partir des sources .Rmd.
#
# Les .Rmd ne contiennent aucun bloc de code R : ils sont convertis directement
# par pandoc, ce qui donne exactement le même résultat qu'un knit sous R.
#
# Usage : bash rendu/rendre.sh
set -euo pipefail

RACINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RACINE"

COMMUN=(--from markdown
        --lua-filter=rendu/filtre_memoire.lua
        --top-level-division=chapter
        --resource-path=.)

rendre() {
  local source="$1"
  local base="${source%.Rmd}"
  echo "→ $base.pdf"
  pandoc "$source" -o "$base.pdf" "${COMMUN[@]}" \
    --template=rendu/template_memoire.tex \
    --number-sections \
    --pdf-engine=pdflatex
  echo "→ $base.docx"
  pandoc "$source" -o "$base.docx" "${COMMUN[@]}"
}

rendre chapitre_1_migration_tiers_spo.Rmd
rendre chapitre_2_copilote_financier.Rmd

echo "Rendus terminés."
