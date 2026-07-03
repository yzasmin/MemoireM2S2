"""Outillage de construction et d'exécution des notebooks du mémoire.

Chaque notebook du dossier `notebooks/` est généré par un script
`src/nb_specs/nbXX_*.py` qui déclare une liste de cellules ("md" ou "code").
Cela garantit des notebooks reproductibles, versionnables et ré-exécutés de
bout en bout avant chaque commit (les sorties enregistrées sont réelles).
"""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbclient import NotebookClient

RACINE = Path(__file__).resolve().parent.parent
NOTEBOOKS = RACINE / "notebooks"

#: Cellule d'amorçage commune : fonctionne en local (dépôt déjà présent)
#: comme sur Google Colab (clonage du dépôt + installation des dépendances).
AMORCAGE = '''\
# --- Amorçage : exécution locale ou Google Colab ---
import pathlib, subprocess, sys

racine = pathlib.Path.cwd()
while not (racine / "src" / "nettoyage.py").exists() and racine != racine.parent:
    racine = racine.parent
if not (racine / "src" / "nettoyage.py").exists():  # environnement Colab vierge
    subprocess.run(["git", "clone", "-b", "claude/copilote-financier-angelotti-72c614",
                    "https://github.com/yzasmin/MemoireM2S2.git"], check=True)
    racine = pathlib.Path.cwd() / "MemoireM2S2"
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-r",
                    str(racine / "requirements.txt")], check=True)

sys.path.insert(0, str(racine / "src"))
import base_sql

if not base_sql.DB.exists():  # reconstruit data/copilote.db depuis donnéebrut/
    base_sql.construire_base()
DB = base_sql.DB
print("Base prête :", DB)
'''


def construire(nom: str, cellules: list[tuple[str, str]], executer: bool = True) -> Path:
    """Construit `notebooks/<nom>.ipynb` puis l'exécute de bout en bout."""
    nb = nbformat.v4.new_notebook()
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    nb.metadata["language_info"] = {"name": "python"}
    for genre, source in cellules:
        if genre == "md":
            nb.cells.append(nbformat.v4.new_markdown_cell(source))
        else:
            nb.cells.append(nbformat.v4.new_code_cell(source))
    NOTEBOOKS.mkdir(exist_ok=True)
    chemin = NOTEBOOKS / f"{nom}.ipynb"
    if executer:
        client = NotebookClient(
            nb, timeout=1800, kernel_name="python3",
            resources={"metadata": {"path": str(RACINE)}},
        )
        client.execute()
    nbformat.write(nb, chemin)
    print(f"Notebook écrit : {chemin} ({len(nb.cells)} cellules)")
    return chemin
