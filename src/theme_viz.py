"""Thème graphique commun à tous les notebooks et à la plateforme.

Palette catégorielle validée (bande de luminance, chroma, séparation CVD)
avec le validateur du guide interne de dataviz ; ordre FIXE, jamais recyclé.
Le rouge est réservé aux alertes (statut), pas aux séries ordinaires.
"""

import matplotlib as mpl

#: Ordre fixe des séries catégorielles.
SERIES = ["#2a78d6", "#1baf7a", "#eda100", "#4a3aa7"]
#: Couleurs de statut (réservées : bon / vigilance / risque).
STATUT = {"bon": "#008300", "vigilance": "#c98500", "risque": "#e34948"}
#: Séquentiel : un seul ton (bleu), clair → foncé.
CMAP_SEQ = "Blues"
#: Divergent : deux tons + milieu neutre.
CMAP_DIV = "RdBu_r"
ENCRE = "#1a1a19"
ENCRE_2 = "#52514e"


def appliquer():
    """Applique le thème à matplotlib (grille discrète, encre douce)."""
    mpl.rcParams.update({
        "axes.prop_cycle": mpl.cycler(color=SERIES),
        "axes.edgecolor": ENCRE_2,
        "axes.labelcolor": ENCRE,
        "axes.titlecolor": ENCRE,
        "axes.titlesize": 11,
        "axes.titleweight": "bold",
        "axes.grid": True,
        "grid.color": "#e5e4df",
        "grid.linewidth": 0.6,
        "axes.axisbelow": True,
        "xtick.color": ENCRE_2,
        "ytick.color": ENCRE_2,
        "text.color": ENCRE,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "font.size": 10,
        "figure.dpi": 110,
        "lines.linewidth": 2.0,
    })
