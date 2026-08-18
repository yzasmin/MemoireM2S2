"""Figures du chapitre 1 du mémoire de fin d'études (migration des tiers vers SPO).

Toutes les valeurs proviennent de la note de synthèse « Import des tiers vers SPO »
(juin 2026). Aucune donnée n'est recalculée ici : le script ne fait que mettre en
forme les compteurs de cette note.

Usage : python src/figures_chapitre1.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import theme_viz

theme_viz.appliquer()

SORTIE = Path(__file__).resolve().parent.parent / "figures"
SORTIE.mkdir(exist_ok=True)

BLEU, VERT, JAUNE, VIOLET = theme_viz.SERIES
ENCRE, ENCRE_2 = theme_viz.ENCRE, theme_viz.ENCRE_2
DPI = 220


def _enregistrer(fig, nom):
    chemin = SORTIE / nom
    fig.savefig(chemin, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"{chemin.name}")


# --------------------------------------------------------------------------
# Figure 1.1 — La chaîne de traitement à trois étages
# --------------------------------------------------------------------------
def figure_chaine_traitement():
    """Schéma des trois étages du fichier de travail (sources, pivot, sorties)."""
    interligne = 3.2          # hauteur d'une ligne de texte, en unités de l'axe
    marge_haut = 8.0          # place réservée au titre du bloc
    marge_bas = 2.6

    # (gauche, droite, gras) ; une entrée vide insère une respiration.
    etages = [
        (1.0, 27.0, BLEU, "#eef4fc", "Étage 1 — Les sources",
         [("VADIMM", "1 557", True),
          ("lignes de ventes reprises du CRM", None, False),
          ("", None, False),
          ("Builder coordonnée", "1 602", True),
          ("lignes d'adresses, courriels, téléphones", None, False),
          ("", None, False),
          ("SPO", "13 000", True),
          ("tiers déjà créés dans l'ERP", None, False)]),
        (36.0, 26.0, VIOLET, "#f3f2fa", "Étage 2 — La feuille pivot",
         [("BuilderTiers", None, True),
          ("", None, False),
          ("colonnes A à Q", "données reprises", False),
          ("colonnes R à T", "rangs d'unicité", False),
          ("colonnes V à AC", "n° séquentiels", False),
          ("colonnes AE à AG", "matching SPO", False),
          ("", None, False),
          ("environ 60 000 cellules de formules", None, False)]),
        (69.0, 30.0, VERT, "#eef9f4", "Étage 3 — Les feuilles de sortie",
         [("tiers DirectApi", "1 434", False),
          ("tier Adresse", "553", False),
          ("tiers Courriels", "469", False),
          ("tiers Phone", "538", False),
          ("tiers Representant", "1 871", False),
          ("tiers Role", "1 434", False),
          ("", None, False),
          ("exportées en CSV, injectées dans SPO", None, False)]),
    ]

    hauteur = marge_haut + marge_bas + interligne * max(len(e[5]) for e in etages)
    fig, ax = plt.subplots(figsize=(11.6, 4.6))
    ax.set_xlim(0, 100)
    ax.set_ylim(-2, hauteur + 2)
    ax.axis("off")
    ax.grid(False)

    for x, largeur, couleur, fond, titre, lignes in etages:
        ax.add_patch(
            mpatches.FancyBboxPatch(
                (x, 0), largeur, hauteur,
                boxstyle="round,pad=0.0,rounding_size=1.4",
                linewidth=1.4, edgecolor=couleur, facecolor=fond,
            )
        )
        ax.text(x + largeur / 2, hauteur - 3.2, titre, ha="center", va="center",
                fontsize=9.6, fontweight="bold", color=ENCRE)
        y = hauteur - marge_haut
        for gauche, droite, gras in lignes:
            if gauche:
                ax.text(x + 2.0, y, gauche, ha="left", va="center", fontsize=8.4,
                        color=ENCRE if gras else ENCRE_2,
                        fontweight="bold" if gras else "normal")
                if droite:
                    ax.text(x + largeur - 2.0, y, droite, ha="right", va="center",
                            fontsize=8.4, color=ENCRE_2)
            y -= interligne

    for x0, x1 in [(28.6, 35.2), (62.6, 68.2)]:
        ax.annotate("", xy=(x1, hauteur / 2), xytext=(x0, hauteur / 2),
                    arrowprops=dict(arrowstyle="-|>", linewidth=1.7, color=ENCRE_2))

    _enregistrer(fig, "fig_1_1_chaine_traitement.png")


# --------------------------------------------------------------------------
# Figure 1.3 — L'entonnoir de la volumétrie
# --------------------------------------------------------------------------
def figure_entonnoir():
    etapes = [
        ("Lignes brutes du périmètre de départ", 1602, BLEU),
        ("Tiers uniques après déduplication", 1474, VIOLET),
        ("Tiers créés dans SPO", 1434, VERT),
    ]
    fig, ax = plt.subplots(figsize=(9.6, 3.9))
    y = [2, 1, 0]
    for (libelle, valeur, couleur), yi in zip(etapes, y):
        ax.barh(yi, valeur, height=0.52, color=couleur, zorder=3)
        ax.text(valeur + 22, yi, f"{valeur:,}".replace(",", " "),
                va="center", ha="left", fontsize=11, fontweight="bold", color=ENCRE)

    ax.set_yticks(y)
    ax.set_yticklabels([e[0] for e in etapes], fontsize=9.5)
    ax.set_xlim(0, 1750)
    ax.set_ylim(-0.55, 2.65)
    ax.set_xlabel("nombre de lignes")
    ax.set_title("Du périmètre de départ aux tiers créés dans SPO")
    ax.grid(axis="y", visible=False)

    # Les écarts sont écrits dans l'espace laissé libre entre deux barres.
    for y_texte, valeur, texte in [
        (1.5, 1474, "− 128 doublons internes, écartés par les clés d'unicité"),
        (0.5, 1434, "− 40 tiers déjà présents dans SPO, exclus par le rapprochement"),
    ]:
        ax.annotate(texte, xy=(valeur, y_texte + 0.28), xytext=(valeur - 30, y_texte),
                    ha="right", va="center", fontsize=8.6, color=ENCRE_2,
                    arrowprops=dict(arrowstyle="-", linewidth=0.8, color="#b9b8b3",
                                    shrinkA=2, shrinkB=2))

    _enregistrer(fig, "fig_1_3_entonnoir_volumetrie.png")


# --------------------------------------------------------------------------
# Figure 1.4 — Volumétrie des six fichiers d'import
# --------------------------------------------------------------------------
def figure_fichiers_import():
    fichiers = [
        ("tiers Representant", 1871, "2 personnes par couple + gérant des PM"),
        ("tiers DirectApi", 1434, "1 ligne par tiers créé"),
        ("tiers Role", 1434, "rôle « Client » pour chaque tiers"),
        ("tier Adresse", 553, "PP et PM seulement"),
        ("tiers Phone", 538, "PP et PM avec téléphone"),
        ("tiers Courriels", 469, "PP et PM avec courriel"),
    ]
    fig, ax = plt.subplots(figsize=(10.2, 4.3))
    y = list(range(len(fichiers)))[::-1]
    for (nom, valeur, note), yi in zip(fichiers, y):
        couleur = VERT if valeur >= 1434 else BLEU
        ax.barh(yi, valeur, height=0.55, color=couleur, zorder=3)
        ax.text(valeur + 25, yi + 0.10, f"{valeur:,}".replace(",", " "),
                va="center", ha="left", fontsize=10, fontweight="bold", color=ENCRE)
        ax.text(valeur + 25, yi - 0.24, note, va="center", ha="left",
                fontsize=8, color=ENCRE_2)

    ax.set_yticks(y)
    ax.set_yticklabels([f[0] for f in fichiers], fontsize=9.5)
    ax.set_xlim(0, 2650)
    ax.set_xlabel("nombre de lignes générées")
    ax.set_title("Les six fichiers d'import produits par la feuille pivot")
    ax.grid(axis="y", visible=False)
    _enregistrer(fig, "fig_1_4_volumetrie_fichiers_import.png")


# --------------------------------------------------------------------------
# Figure 1.5 — Répartition des 1 434 tiers créés par nature
# --------------------------------------------------------------------------
def figure_repartition():
    natures = [("Couples", 881, BLEU), ("Personnes physiques", 462, VIOLET),
               ("Personnes morales", 91, VERT)]
    total = sum(n[1] for n in natures)
    fig, ax = plt.subplots(figsize=(9.6, 2.6))

    gauche = 0
    for libelle, valeur, couleur in natures:
        ax.barh(0, valeur, left=gauche, height=0.45, color=couleur, zorder=3)
        part = 100 * valeur / total
        if part > 8:
            ax.text(gauche + valeur / 2, 0, f"{valeur}\n{part:.1f} %".replace(".", ","),
                    ha="center", va="center", fontsize=10, fontweight="bold", color="white")
        else:
            ax.text(gauche + valeur / 2, -0.38, f"{valeur}  ({part:.1f} %)".replace(".", ","),
                    ha="center", va="center", fontsize=9, color=ENCRE)
        gauche += valeur

    ax.set_xlim(0, total)
    ax.set_ylim(-0.62, 0.55)
    ax.set_yticks([])
    ax.set_xlabel("nombre de tiers")
    ax.set_title("Répartition des 1 434 tiers créés selon leur nature")
    ax.grid(visible=False)
    ax.spines["left"].set_visible(False)
    ax.legend(handles=[mpatches.Patch(color=c, label=l) for l, _, c in natures],
              loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=3,
              frameon=False, fontsize=9)
    _enregistrer(fig, "fig_1_5_repartition_natures.png")


if __name__ == "__main__":
    figure_chaine_traitement()
    figure_entonnoir()
    figure_fichiers_import()
    figure_repartition()
