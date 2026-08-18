"""Figures produites pour le mémoire de fin d'études.

Toutes les valeurs proviennent de la note de synthèse « Import des tiers vers SPO »
(juin 2026). Aucune donnée n'est recalculée ici : le script ne fait que mettre en
forme les compteurs de cette note.

Usage : python src/figures_memoire.py
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
# Figure 3.1 — La chaîne de traitement à trois étages
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

    _enregistrer(fig, "fig_3_1_chaine_traitement.png")


# --------------------------------------------------------------------------
# Figure 3.2 — L'entonnoir de la volumétrie
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

    _enregistrer(fig, "fig_3_2_entonnoir_volumetrie.png")


# --------------------------------------------------------------------------
# Figure 3.3 — Volumétrie des six fichiers d'import
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
    _enregistrer(fig, "fig_3_3_volumetrie_fichiers_import.png")


# --------------------------------------------------------------------------
# Figure 3.4 — Répartition des 1 434 tiers créés par nature
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
    _enregistrer(fig, "fig_3_4_repartition_natures.png")


# --------------------------------------------------------------------------
# Outils communs aux schémas
# --------------------------------------------------------------------------
def _boite(ax, x, y, w, h, titre, lignes, couleur, fond, taille_titre=9.6,
           taille_ligne=8.4, interligne=3.4):
    """Trace une boîte arrondie titrée, avec ses lignes de contenu."""
    ax.add_patch(
        mpatches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.0,rounding_size=1.4",
            linewidth=1.4, edgecolor=couleur, facecolor=fond,
        )
    )
    ax.text(x + w / 2, y + h - 3.2, titre, ha="center", va="center",
            fontsize=taille_titre, fontweight="bold", color=ENCRE)
    yc = y + h - 8.0
    for ligne in lignes:
        if ligne:
            ax.text(x + w / 2, yc, ligne, ha="center", va="center",
                    fontsize=taille_ligne, color=ENCRE_2)
        yc -= interligne


def _fleche(ax, x0, y0, x1, y1, texte=None, couleur=None):
    couleur = couleur or ENCRE_2
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", linewidth=1.7, color=couleur))
    if texte:
        ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 2.0, texte, ha="center",
                va="bottom", fontsize=7.8, color=ENCRE_2)


def _cadre(figsize, xmax=100, ymax=60):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    ax.axis("off")
    ax.grid(False)
    return fig, ax


# --------------------------------------------------------------------------
# Figure 1.1 — Le système d'information et la circulation de la donnée
# --------------------------------------------------------------------------
def figure_systeme_information():
    fig, ax = _cadre((11.6, 7.0), ymax=88)

    _boite(ax, 1, 55, 27, 25, "Gestion des opérations",
           ["Grimmo, l'ERP historique", "", "SPO, le nouvel ERP",
            "opérations, tranches, budgets"], BLEU, "#eef4fc")
    _boite(ax, 1, 25, 27, 25, "Relation commerciale",
           ["Vadimm, le CRM", "", "acquéreurs, réservations,",
            "désistements, coordonnées"], BLEU, "#eef4fc")
    _boite(ax, 37, 40, 24, 25, "Restitution",
           ["MyReport", "", "requêtes sur les bases",
            "et tableaux de bord"], VIOLET, "#f3f2fa")
    _boite(ax, 70, 40, 29, 25, "Usages métier",
           ["Direction financière,", "service juridique,",
            "équipes commerciales"], VERT, "#eef9f4")

    _fleche(ax, 28.5, 67, 36.5, 55)
    _fleche(ax, 28.5, 37, 36.5, 50)
    _fleche(ax, 61.5, 52.5, 69.5, 52.5)

    # La quatrième couche : les tableurs, qui comblent ce que les outils
    # ne se transmettent pas.
    _boite(ax, 1, 1, 98, 15, "Les tableurs, quatrième couche du système",
           ["Suivi des dérives budgétaires opération par opération, sur des "
            "fichiers individuels, sans vision transverse.",
            "Ils font le lien partout où les trois outils précédents ne se "
            "parlent pas."],
           JAUNE, "#fdf7e8", taille_ligne=8.4, interligne=4.2)

    for x, y0, y1 in ((14.5, 16.4, 25.0), (14.5, 50.0, 55.0),
                      (49.0, 16.4, 40.0), (84.5, 16.4, 40.0)):
        ax.plot([x, x], [y0, y1], linestyle=(0, (3, 3)), linewidth=1.3,
                color=ENCRE_2, zorder=1)

    # repères des chapitres, décalés des traits pointillés
    reperes = [(4.0, 53.0, "chapitre 2"), (4.0, 23.0, "chapitre 3"),
               (39.5, 38.0, "chapitre 4"), (72.5, 38.0, "chapitre 5")]
    for x, y, t in reperes:
        ax.text(x, y, t, ha="left", va="top", fontsize=8,
                color=ENCRE, fontweight="bold")

    ax.text(50, 86.5, "Les flèches pleines indiquent la circulation de la "
            "donnée, les traits pointillés les échanges qui passent par les "
            "tableurs ;",
            ha="center", va="center", fontsize=8, color=ENCRE_2, style="italic")
    ax.text(50, 83.0, "les repères signalent le chapitre où la mission "
            "correspondante est exposée.",
            ha="center", va="center", fontsize=8, color=ENCRE_2, style="italic")
    _enregistrer(fig, "fig_1_1_systeme_information.png")


# --------------------------------------------------------------------------
# Figure 1.2 — La frise des quatre missions
# --------------------------------------------------------------------------
def figure_frise_missions():
    missions = [
        ("Migration des opérations vers SPO", 0.0, 0.62, BLEU, "chapitre 2"),
        ("Reprise des tiers", 0.50, 0.45, VIOLET, "chapitre 3"),
        ("Reporting et missions SI transverses", 0.0, 1.0, JAUNE, "chapitre 4"),
        ("Copilote Financier", 0.55, 0.45, VERT, "chapitre 5"),
    ]
    fig, ax = plt.subplots(figsize=(10.6, 3.6))
    ax.set_xlim(0, 1.0)
    ax.set_ylim(-0.9, len(missions) - 0.3)
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.axvspan(0, 0.5, color="#f7f7f4", zorder=0)
    ax.axvline(0.5, color="#c9c8c3", linewidth=1.0, zorder=1)
    ax.text(0.25, len(missions) - 0.55, "Premier semestre", ha="center",
            fontsize=9.5, fontweight="bold", color=ENCRE)
    ax.text(0.75, len(missions) - 0.55, "Second semestre", ha="center",
            fontsize=9.5, fontweight="bold", color=ENCRE)

    for i, (nom, debut, duree, couleur, renvoi) in enumerate(missions):
        y = len(missions) - 1 - i
        ax.barh(y, duree, left=debut, height=0.42, color=couleur, zorder=3)
        ax.text(debut + 0.012, y, nom, va="center", ha="left", fontsize=9,
                color="white", fontweight="bold", zorder=4)
        ax.text(debut + duree + 0.012, y, renvoi, va="center", ha="left",
                fontsize=8, color=ENCRE_2, zorder=4)

    ax.set_yticks([])
    ax.set_xticks([])
    _enregistrer(fig, "fig_1_2_frise_missions.png")


# --------------------------------------------------------------------------
# Figure 2.3 — La séquence d'injection imposée par l'ERP
# --------------------------------------------------------------------------
def figure_sequence_injection():
    etapes = ["Opération", "Tranches\nde travaux", "Tranches\ncommerciales", "Budget"]
    fig, ax = _cadre((11.2, 3.2), ymax=40)
    largeur, ecart = 18.0, 6.0
    x = 2.5
    for i, etape in enumerate(etapes):
        ax.add_patch(mpatches.FancyBboxPatch(
            (x, 14), largeur, 18, boxstyle="round,pad=0.0,rounding_size=1.4",
            linewidth=1.5, edgecolor=BLEU, facecolor="#eef4fc"))
        ax.text(x + largeur / 2, 23, etape, ha="center", va="center",
                fontsize=10, fontweight="bold", color=ENCRE)
        ax.text(x + largeur / 2, 34.5, "%d" % (i + 1), ha="center", va="center",
                fontsize=9, color=ENCRE_2)
        if i < len(etapes) - 1:
            _fleche(ax, x + largeur + 1.0, 23, x + largeur + ecart - 1.0, 23)
        x += largeur + ecart

    ax.text(50, 6, "Toute injection qui ne respecte pas cet ordre est rejetée : "
            "le système ne trouve pas l'objet parent.",
            ha="center", va="center", fontsize=8.6, color=ENCRE_2, style="italic")
    _enregistrer(fig, "fig_2_3_sequence_injection.png")


# --------------------------------------------------------------------------
# Figure 2.4 — Le requêtage dynamique face au versionnement
# --------------------------------------------------------------------------
def figure_requetage_dynamique():
    fig, ax = _cadre((11.6, 4.4), ymax=52)
    _boite(ax, 1, 16, 28, 22, "1. Appel GET",
           ["Récupérer toutes les versions", "de budget d'une opération"],
           BLEU, "#eef4fc")
    _boite(ax, 36, 16, 28, 22, "2. Tri",
           ["Retenir l'identifiant de la", "version la plus récente,",
            "c'est-à-dire le budget actif"], VIOLET, "#f3f2fa")
    _boite(ax, 71, 16, 28, 22, "3. Appel POST",
           ["Écrire la mise à jour", "sur cet identifiant"], VERT, "#eef9f4")
    _fleche(ax, 29.5, 27, 35.5, 27)
    _fleche(ax, 64.5, 27, 70.5, 27)
    ax.text(50, 45, "L'ERP ne remplace jamais un budget : il clôture la version "
            "précédente et en crée une nouvelle, avec un nouvel identifiant.",
            ha="center", va="center", fontsize=8.6, color=ENCRE_2, style="italic")
    ax.text(50, 9, "Aucun identifiant n'étant stable, il faut le retrouver "
            "avant chaque écriture.",
            ha="center", va="center", fontsize=8.6, color=ENCRE_2, style="italic")
    _enregistrer(fig, "fig_2_4_requetage_dynamique.png")


# --------------------------------------------------------------------------
# Figure 4.1 — La règle de facturation traduite en calcul de rang
# --------------------------------------------------------------------------
def figure_regle_facturation():
    fig, ax = _cadre((11.6, 4.0), ymax=48)
    etapes = [
        ("Commandes du lot", ["telles qu'elles sont", "dans la base"], BLEU, "#eef4fc"),
        ("Tri chronologique", ["par opération", "et par lot"], BLEU, "#eef4fc"),
        ("Rang", ["1, 2, 3, ...", "attribué au calcul"], VIOLET, "#f3f2fa"),
        ("Statut", ["rang impair : Payant", "rang pair : Gratuit"], VERT, "#eef9f4"),
    ]
    largeur, ecart = 21.0, 5.0
    x = 1.0
    for i, (titre, lignes, c, f) in enumerate(etapes):
        _boite(ax, x, 12, largeur, 24, titre, lignes, c, f, taille_ligne=8.2)
        if i < len(etapes) - 1:
            _fleche(ax, x + largeur + 0.6, 24, x + largeur + ecart - 0.6, 24)
        x += largeur + ecart

    ax.text(50, 43, "Aucune de ces étapes n'est stockée : la chaîne est rejouée "
            "à chaque génération du tableau.",
            ha="center", va="center", fontsize=8.6, color=ENCRE_2, style="italic")
    ax.text(50, 5, "C'est ce qui permet de tenir la règle sans droit d'écriture "
            "sur la base ni colonne ajoutée aux fichiers sources.",
            ha="center", va="center", fontsize=8.6, color=ENCRE_2, style="italic")
    _enregistrer(fig, "fig_4_1_regle_facturation.png")


# --------------------------------------------------------------------------
# Figure 6.1 — Les trois régimes de preuve
# --------------------------------------------------------------------------
def figure_regimes_de_preuve():
    fig, ax = _cadre((11.6, 4.6), ymax=58)
    regimes = [
        (1.0, "Réconciliation", "Reprises de données",
         ["« Ce qui est arrivé", "correspond-il à ce", "qui est parti ? »", "",
          "paliers de validation,", "compteurs de contrôle,", "recoupement de deux", "sources"],
         BLEU, "#eef4fc"),
        (34.5, "Validation statistique", "Modèles",
         ["« Le résultat tient-il", "hors de l'échantillon", "d'apprentissage ? »", "",
          "échantillon test,", "référence naïve,", "contrôle des fuites"],
         VIOLET, "#f3f2fa"),
        (68.0, "Recette par l'usage", "Livrables utilisateurs",
         ["« La personne s'en sert-elle,", "et pour la bonne chose ? »", "", "",
          "validation par le service,", "test automatisé des écrans,", "retour de l'entreprise"],
         VERT, "#eef9f4"),
    ]
    for x, titre, sous_titre, lignes, c, f in regimes:
        _boite(ax, x, 8, 31, 44, titre, [sous_titre, ""] + lignes, c, f,
               taille_ligne=8.2, interligne=3.5)
    ax.text(50, 56.5, "Le régime de preuve se déduit de la nature du livrable, "
            "jamais de la méthode employée.",
            ha="center", va="center", fontsize=8.6, color=ENCRE_2, style="italic")
    _enregistrer(fig, "fig_6_1_regimes_de_preuve.png")


if __name__ == "__main__":
    figure_systeme_information()
    figure_frise_missions()
    figure_sequence_injection()
    figure_requetage_dynamique()
    figure_chaine_traitement()
    figure_entonnoir()
    figure_fichiers_import()
    figure_repartition()
    figure_regle_facturation()
    figure_regimes_de_preuve()
