#!/usr/bin/env bash
# Assemble et rend le mémoire de fin d'études (PDF et DOCX).
#
# Les fichiers de `memoire/` sont des sources R Markdown sans bloc de code R :
# le script les concatène dans l'ordre de leur numéro, ajoute l'en-tête YAML
# commun, puis appelle pandoc. Le résultat est identique à un knit sous R.
#
# Usage : bash rendu/rendre.sh
set -euo pipefail

RACINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RACINE"

SOURCE="memoire_M2_saoud.Rmd"

# --- assemblage -----------------------------------------------------------
cat rendu/entete.yaml > "$SOURCE"
for partie in memoire/[0-9][0-9]_*.Rmd; do
  printf '\n\n' >> "$SOURCE"
  cat "$partie" >> "$SOURCE"
done
echo "→ $SOURCE assemblé ($(grep -c '' "$SOURCE") lignes)"

COMMUN=(--from markdown
        --lua-filter=rendu/filtre_memoire.lua
        --top-level-division=chapter
        --resource-path=.)

echo "→ memoire_M2_saoud.pdf"
pandoc "$SOURCE" -o memoire_M2_saoud.pdf "${COMMUN[@]}" \
  --template=rendu/template_memoire.tex \
  --number-sections \
  --pdf-engine=pdflatex

echo "→ memoire_M2_saoud.docx"
pandoc "$SOURCE" -o memoire_M2_saoud.docx "${COMMUN[@]}" --toc --toc-depth=2

echo "Rendu terminé."
