# -*- coding: utf-8 -*-
"""Copilote Financier — Groupe Angelotti, Direction Financière.

Application d'aide à la décision (Streamlit) destinée aux contrôleurs de
gestion et à la direction : synthèse du portefeuille de promotion, alertes
de marge, rythme de vente, pilotage des prix et qualité commerciale.

Périmètre : opérations de PROMOTION uniquement (l'aménagement est exclu de
tous les indicateurs). Données : `data/copilote.db` ; score d'alerte :
`plateforme/modeles/risque_marge.joblib` (construit au notebook 03).

Lancement :  streamlit run plateforme/app.py
"""

import sqlite3
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import streamlit as st

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "src"))

DB = RACINE / "data" / "copilote.db"
MODELES = RACINE / "plateforme" / "modeles"

# Palette du mémoire (src/theme_viz.py) — rouge réservé aux alertes.
BLEU, VERT, AMBRE, VIOLET = "#2a78d6", "#1baf7a", "#eda100", "#4a3aa7"
ROUGE = "#e34948"
ENCRE, ENCRE_2 = "#1a1a19", "#52514e"

st.set_page_config(page_title="Copilote Financier — Angelotti",
                   page_icon="🏗️", layout="wide")

# ------------------------------------------------------------------ style
CSS = """
<style>
.bandeau {
    background: linear-gradient(120deg, #17395f 0%, #2a78d6 100%);
    color: #ffffff; padding: 1.05rem 1.5rem; border-radius: 12px;
    margin-bottom: 1.1rem; display: flex; flex-wrap: wrap;
    justify-content: space-between; align-items: baseline; gap: .4rem;
}
.bandeau .titre { font-size: 1.4rem; font-weight: 700; letter-spacing: .2px; }
.bandeau .sous  { font-size: .92rem; opacity: .88; }
[data-testid="stMetric"] {
    background: #ffffff; border: 1px solid #e3e7ee; border-radius: 10px;
    padding: .85rem 1.05rem; box-shadow: 0 1px 4px rgba(23, 57, 95, .08);
}
[data-testid="stMetricLabel"] { color: #52514e; }
[data-testid="stSidebar"] { background: #f6f8fb; }
.decision {
    border-left: 4px solid #2a78d6; background: #f2f7fd;
    padding: .65rem 1rem; border-radius: 0 8px 8px 0;
    color: #2f3e4d; margin: 0 0 1.1rem 0; font-size: .96rem;
}
.resultat {
    background: #f0f8f4; border: 1px solid #cfe8da; border-radius: 8px;
    padding: .8rem 1.05rem; margin: .35rem 0 .9rem 0; color: #1a1a19;
}
.pied {
    color: #8a8984; font-size: .78rem; border-top: 1px solid #e5e4df;
    padding-top: .6rem; margin-top: 2.4rem;
}
h1, h2, h3 { color: #1a1a19; }
thead tr th { background: #f6f8fb !important; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

FIN = " "  # espace fine insécable des formats français


def fr(x, dec: int = 0) -> str:
    """Nombre au format français : 12 345,6 (espace insécable, virgule)."""
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "—"
    s = f"{x:,.{dec}f}".replace(",", FIN).replace(".", ",")
    return s


def eur(x) -> str:
    """Montant lisible en k€ / M€ français."""
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "—"
    a = abs(x)
    if a >= 1e6:
        return fr(x / 1e6, 1) + FIN + "M€"
    if a >= 1e3:
        return fr(x / 1e3, 0) + FIN + "k€"
    return fr(x, 0) + FIN + "€"


def pct(x, dec: int = 1, signe: bool = False) -> str:
    """Pourcentage français à partir d'une fraction (0,124 → « 12,4 % »)."""
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "—"
    s = f"{100 * x:+.{dec}f}" if signe else f"{100 * x:.{dec}f}"
    return s.replace(".", ",") + FIN + "%"


# ---------------------------------------------------------------- données
# Toutes les requêtes sont restreintes aux opérations de PROMOTION
# (operations.activite = 'Promotion') : l'aménagement est hors périmètre.

@st.cache_resource
def base():
    if not DB.exists():
        import base_sql
        base_sql.construire_base()
    return sqlite3.connect(DB, check_same_thread=False)


@st.cache_data
def sql(q: str) -> pd.DataFrame:
    return pd.read_sql(q, base())


@st.cache_resource
def modele_risque():
    """Score d'alerte de marge sérialisé par le notebook 03."""
    chemin = MODELES / "risque_marge.joblib"
    if chemin.exists():
        return joblib.load(chemin)
    return None


@st.cache_data
def features_marge():
    """Indicateurs budgétaires par opération de promotion (mêmes règles de
    calcul que le notebook 03 ; seul le périmètre est restreint)."""
    con = base()
    b = pd.read_sql("""
        SELECT b.id_operation, b.sens, b.poste_niv1,
               SUM(b.budget_ht) AS budget, SUM(b.engage_ht) AS engage
        FROM budget b JOIN operations o USING (id_operation)
        WHERE o.activite = 'Promotion'
        GROUP BY b.id_operation, b.sens, b.poste_niv1""", con)
    dep = b.query("sens == 'D'").copy()
    dep["terminaison"] = dep[["budget", "engage"]].max(axis=1)
    agg = dep.groupby("id_operation").agg(
        dep_budget=("budget", "sum"), dep_engage=("engage", "sum"),
        dep_terminaison=("terminaison", "sum"))
    rec = b.query("sens == 'R'").groupby("id_operation")["budget"].sum().rename("rec_budget")
    df = agg.join(rec, how="inner")
    df["taux_engagement"] = df["dep_engage"] / df["dep_budget"]
    df["marge_budget"] = df["rec_budget"] - df["dep_budget"]
    df["marge_terminaison"] = df["rec_budget"] - df["dep_terminaison"]
    df["variation_marge"] = ((df["marge_terminaison"] - df["marge_budget"])
                             / df["marge_budget"].abs())
    parts = dep.pivot_table(index="id_operation", columns="poste_niv1",
                            values="budget", aggfunc="sum").fillna(0)
    parts = parts.div(parts.sum(axis=1), axis=0)
    parts.columns = ["part_" + c.lower().replace(" ", "_").replace("/", "_")
                     for c in parts.columns]
    ops = pd.read_sql("""
        SELECT o.id_operation, o.libelle, o.agence, o.statut,
               c.population, c.littoral
        FROM operations o LEFT JOIN communes c USING (commune_norm)
        WHERE o.activite = 'Promotion'""", con)
    com = pd.read_sql("""
        SELECT id_operation, COUNT(*) AS nb_dossiers, AVG(desiste) AS taux_desistement,
               AVG(prix_vente_ttc) AS prix_moyen
        FROM ventes GROUP BY id_operation""", con)
    df = (df.reset_index().merge(parts.reset_index(), on="id_operation")
            .merge(ops, on="id_operation", how="inner")
            .merge(com, on="id_operation", how="left"))
    df = df[df["rec_budget"] > 0]
    df["log_recettes"] = np.log(df["rec_budget"])
    df["marge_relative_budget"] = df["marge_budget"] / df["rec_budget"]
    df["taux_desistement"] = df["taux_desistement"].fillna(0)
    df["nb_dossiers"] = df["nb_dossiers"].fillna(0)
    df["littoral"] = df["littoral"].fillna(0)
    df["log_population"] = np.log(df["population"].fillna(df["population"].median()))
    df["agence"] = df["agence"].str.strip()
    return df


def operations_en_cours_scorees():
    """Opérations de promotion en cours, suffisamment avancées, avec leur
    niveau d'alerte (🟢 / 🟠 / 🔴) issu du score du notebook 03."""
    df = features_marge()
    mures = df[(df["taux_engagement"] >= 0.6) & (df["marge_budget"].abs() > 5e4)].copy()
    art = modele_risque()
    if art is not None:
        X = mures[art["variables"]].to_numpy(dtype=float)
        mures["proba_derive"] = art["modele"].predict_proba(X)[:, 1]
    else:
        mures["proba_derive"] = np.nan

    def niveau(p):
        if not np.isfinite(p):
            return "—"
        if p > 0.65:
            return "🔴 Alerte"
        if p >= 0.35:
            return "🟠 À surveiller"
        return "🟢 Conforme"

    mures["niveau_alerte"] = mures["proba_derive"].map(niveau)
    mures["depassements_engages"] = (mures["dep_terminaison"] - mures["dep_budget"]).clip(lower=0)
    en_cours = mures[mures["statut"] == "En Cours"].copy()
    return en_cours.sort_values("proba_derive", ascending=False), art is not None


@st.cache_resource
def modele_hedonique():
    """Prix de marché estimé des appartements (ventes comparables du groupe :
    surface, étage, exposition, commune, période). Périmètre promotion."""
    from sklearn.compose import ColumnTransformer
    from sklearn.linear_model import LinearRegression
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    con = base()
    lots = pd.read_sql("""
        SELECT l.*, o.agence, c.littoral, c.population, v.date_reservation
        FROM lots l JOIN operations o USING (id_operation)
        LEFT JOIN communes c ON o.commune_norm = c.commune_norm
        LEFT JOIN (SELECT id_operation, numero_lot,
                          MAX(date_reservation) AS date_reservation
                   FROM ventes GROUP BY id_operation, numero_lot) v
            USING (id_operation, numero_lot)
        WHERE o.activite = 'Promotion'""", con)
    ap = lots[(lots["nature_lot"] == "Appartement")
              & (lots["prix_m2_ttc"] > 500) & (lots["surface"] > 10)].copy()
    ap["y"] = np.log(ap["prix_m2_ttc"])
    ap["log_surface"] = np.log(ap["surface"])
    ap["expo"] = ap["exposition"].fillna("Inconnue").map(
        lambda e: "Sud" if "S" in str(e) else
                  ("Nord" if "N" in str(e) else
                   ("Est-Ouest" if e in ("E", "O") else "Inconnue")))
    ap["etage_n"] = pd.to_numeric(ap["etage"], errors="coerce").clip(0, 6).fillna(-1)
    ap["littoral"] = ap["littoral"].fillna(0)
    ap["log_pop"] = np.log(ap["population"].fillna(ap["population"].median()))
    ap["annee"] = pd.to_datetime(ap["date_reservation"]).dt.year
    train = ap[ap["annee"].notna()].copy()
    train["annee"] = train["annee"].astype(int).astype(str)
    stock = ap[ap["statut_lot"] == "En stock"].copy()
    stock["annee"] = "2026"
    num = ["log_surface", "etage_n", "littoral", "log_pop"]
    cat = ["expo", "type_produit", "agence", "annee"]
    pipe = Pipeline([
        ("prep", ColumnTransformer([
            ("num", StandardScaler(), num),
            ("cat", OneHotEncoder(handle_unknown="ignore", drop="first"), cat)])),
        ("ols", LinearRegression())]).fit(train[num + cat], train["y"])
    resid = train["y"] - pipe.predict(train[num + cat])
    incertitude = float(np.sqrt((resid ** 2).mean()))  # erreur type sur le prix
    stock["y_pred"] = pipe.predict(stock[num + cat])
    stock["ecart_marche"] = stock["y"] - stock["y_pred"]
    stock["prix_marche_ttc"] = np.exp(stock["y_pred"]) * stock["surface"]
    return pipe, stock, incertitude


@st.cache_data
def serie_intensite():
    """Réservations mensuelles par opération de promotion active,
    rapprochées des taux de crédit habitat."""
    con = base()
    v = pd.read_sql("""SELECT v.date_reservation, v.id_operation
                       FROM ventes v JOIN operations o USING (id_operation)
                       WHERE v.date_reservation IS NOT NULL
                         AND o.activite = 'Promotion'""", con,
                    parse_dates=["date_reservation"])
    m = v.assign(mois=v["date_reservation"].dt.to_period("M"))
    resa = m.groupby("mois").size()
    bornes = m.groupby("id_operation")["mois"].agg(["min", "max"])
    actifs = pd.Series({p: int(((bornes["min"] <= p) & (bornes["max"] >= p)).sum())
                        for p in resa.index})
    df = pd.DataFrame({"reservations": resa, "operations_actives": actifs,
                       "intensite": resa / actifs})
    df.index = df.index.to_timestamp()
    conj = pd.read_sql("SELECT * FROM conjoncture", con)
    conj["mois"] = pd.to_datetime(conj["mois"])
    return df.join(conj.set_index("mois"), how="left")


# --------------------------------------------------------------- gabarits
def entete():
    st.markdown(
        '<div class="bandeau"><span class="titre">🏗️ Copilote Financier</span>'
        '<span class="sous">Groupe Angelotti — Direction Financière · '
        'périmètre promotion immobilière</span></div>',
        unsafe_allow_html=True)


def phrase_decision(texte: str):
    st.markdown(f'<div class="decision">{texte}</div>', unsafe_allow_html=True)


def pied_de_page():
    st.markdown(
        '<div class="pied">Données de gestion au 30/06/2026 — usage interne. '
        'Méthodologie détaillée dans les notebooks du mémoire.</div>',
        unsafe_allow_html=True)


def tableau_alertes(df: pd.DataFrame, hauteur: int = 480):
    """Tableau standard des opérations avec badge et barre d'engagement."""
    vue = pd.DataFrame({
        "Opération": df["libelle"],
        "Agence": df["agence"],
        "Niveau d'alerte": df["niveau_alerte"],
        "Taux d'engagement": df["taux_engagement"].clip(0, 1),
        "Marge budgétée": df["marge_budget"].map(eur),
        "Dépassements engagés": df["depassements_engages"].map(eur),
        "Impact sur la marge": df["variation_marge"].map(lambda v: pct(v, 1, signe=True)),
    })
    st.dataframe(
        vue, hide_index=True, width="stretch", height=hauteur,
        column_config={
            "Taux d'engagement": st.column_config.ProgressColumn(
                "Taux d'engagement", min_value=0.0, max_value=1.0,
                format="percent",
                help="Part des dépenses budgétées déjà engagées "
                     "(commandes signées) — plafonné à 100 %."),
            "Niveau d'alerte": st.column_config.TextColumn(
                "Niveau d'alerte",
                help="🟢 Conforme : pas de dérive attendue · 🟠 À surveiller : "
                     "risque intermédiaire · 🔴 Alerte : forte présomption de "
                     "dérive de marge."),
        })


# ------------------------------------------------------------------ pages
def page_vue_ensemble():
    st.header("Vue d'ensemble")
    phrase_decision(
        "L'essentiel pour décider en revue de gestion : où en est le "
        "portefeuille de promotion, quelles opérations demandent une action "
        "immédiate, et à quel rythme le marché absorbe nos programmes.")

    nb_total = int(sql("""SELECT COUNT(*) AS n FROM operations
                          WHERE activite = 'Promotion'""")["n"].iloc[0])
    stock = sql("""SELECT SUM(v.nb_en_stock) AS s FROM v_stock_lots v
                   JOIN operations o USING (id_operation)
                   WHERE o.activite = 'Promotion'""")["s"].iloc[0]
    serie = serie_intensite().dropna(subset=["intensite"])
    en_cours, modele_ok = operations_en_cours_scorees()
    nb_alerte = int((en_cours["niveau_alerte"] == "🔴 Alerte").sum())
    nb_surv = int((en_cours["niveau_alerte"] == "🟠 À surveiller").sum())
    rythme = float(serie["intensite"].iloc[-3:].mean())
    taux = float(serie["taux_credit_habitat"].iloc[-1])

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Opérations suivies", fr(nb_total),
              help="Opérations de promotion immobilière du groupe "
                   "(l'aménagement est hors périmètre de cette application).")
    c2.metric("Opérations en alerte", f"🔴 {nb_alerte}",
              f"+ {nb_surv} à surveiller", delta_color="off",
              help="Opérations en cours, engagées à plus de 60 %, où une "
                   "dérive de marge est fortement présumée d'après la "
                   "structure du budget et les signaux commerciaux.")
    c3.metric("Lots principaux en stock", fr(int(stock)),
              help="Logements et lots principaux restant à vendre sur les "
                   "programmes de promotion.")
    c4.metric("Rythme de vente récent", f"{fr(rythme, 1)} résa/mois",
              help="Réservations mensuelles moyennes par opération en cours "
                   "de commercialisation (trois derniers mois).")
    c5.metric("Taux crédit habitat", pct(taux / 100, 2),
              help="Taux moyen des crédits à l'habitat (source BCE), "
                   "principal moteur de la demande.")

    st.subheader("Opérations à examiner en priorité")
    top5 = en_cours.head(5)
    tableau_alertes(top5, hauteur=215)
    st.caption("Détail complet et postes en dépassement : page « Alertes marge ».")

    st.subheader("Rythme de vente et taux de crédit")
    g1, g2 = st.columns(2)
    with g1:
        st.line_chart(serie["intensite"].rename("Réservations par opération et par mois"),
                      color=BLEU, height=230)
    with g2:
        st.line_chart(serie["taux_credit_habitat"].rename("Taux crédit habitat (%)"),
                      color=VERT, height=230)
    il_y_a_un_an = serie.index[-1] - pd.DateOffset(years=1)
    ryt_n1 = float(serie.loc[:il_y_a_un_an, "intensite"].iloc[-3:].mean())
    taux_n1 = float(serie.loc[:il_y_a_un_an, "taux_credit_habitat"].iloc[-1])
    sens_taux = "en baisse" if taux < taux_n1 else "en hausse"
    sens_ryt = "mieux orienté" if rythme > ryt_n1 else "en retrait"
    st.markdown(
        f"**Contexte marché** — Les taux de crédit s'établissent à "
        f"{pct(taux / 100, 2)} ({sens_taux} de "
        f"{pct(abs(taux - taux_n1) / 100, 2)} sur un an) ; le rythme de vente "
        f"du trimestre, {fr(rythme, 1)} réservations par mois et par "
        f"opération, est {sens_ryt} par rapport à la même période de l'an "
        f"dernier ({fr(ryt_n1, 1)}).")
    if not modele_ok:
        st.warning("Le score d'alerte n'est pas disponible : exécuter le "
                   "notebook 03 pour le reconstruire.")


def page_alertes():
    st.header("Alertes marge")
    phrase_decision(
        "Décider quelles opérations examiner en priorité en revue de "
        "gestion : chaque opération en cours reçoit un niveau d'alerte, avec "
        "le détail des postes de coûts déjà en dépassement.")

    en_cours, modele_ok = operations_en_cours_scorees()
    if not modele_ok:
        st.warning("Le score d'alerte n'est pas disponible (modèle absent) : "
                   "seuls les dépassements déjà engagés sont affichés.")
    c1, c2, c3 = st.columns(3)
    c1.metric("🔴 Alerte", int((en_cours["niveau_alerte"] == "🔴 Alerte").sum()),
              help="Forte présomption de dérive de marge : à examiner en priorité.")
    c2.metric("🟠 À surveiller",
              int((en_cours["niveau_alerte"] == "🟠 À surveiller").sum()),
              help="Risque intermédiaire : à garder sous revue.")
    c3.metric("🟢 Conforme", int((en_cours["niveau_alerte"] == "🟢 Conforme").sum()),
              help="Pas de dérive de marge attendue à ce stade.")

    st.subheader("Opérations en cours, classées par niveau d'alerte")
    tableau_alertes(en_cours)
    st.caption(
        "Périmètre : opérations de promotion en cours, engagées à plus de "
        "60 %. Le niveau d'alerte anticipe la dérive à partir de la structure "
        "du budget initial et des signaux commerciaux ; « dépassements "
        "engagés » = surcoûts déjà actés dans les commandes, en euros.")

    st.subheader("Détail d'une opération")
    noms = en_cours.set_index("libelle")["id_operation"]
    nom = st.selectbox("Opération à examiner", list(noms.index))
    op = en_cours[en_cours["libelle"] == nom].iloc[0]
    d1, d2, d3, d4 = st.columns(4)
    d1.metric("Niveau d'alerte", op["niveau_alerte"])
    d2.metric("Marge budgétée", eur(op["marge_budget"]),
              help="Recettes budgétées moins dépenses budgétées.")
    d3.metric("Dépassements engagés", eur(op["depassements_engages"]),
              pct(op["variation_marge"], 1, signe=True) + " de marge",
              delta_color="inverse" if op["depassements_engages"] > 0 else "off",
              help="Surcoûts déjà actés : montants engagés au-delà du budget, "
                   "tous postes confondus.")
    d4.metric("Taux d'engagement", pct(op["taux_engagement"], 0),
              help="Part des dépenses budgétées déjà engagées.")

    postes = sql(f"""
        SELECT poste_niv1 AS famille, poste_niv2 AS poste,
               SUM(budget_ht) AS budget, SUM(engage_ht) AS engage
        FROM budget
        WHERE sens = 'D' AND id_operation = {int(op['id_operation'])}
        GROUP BY poste_niv1, poste_niv2
        HAVING SUM(engage_ht) > SUM(budget_ht)
        ORDER BY SUM(engage_ht) - SUM(budget_ht) DESC""")
    if len(postes):
        st.markdown("**Principaux postes en dépassement**")
        detail = pd.DataFrame({
            "Famille de coûts": postes["famille"].str.capitalize(),
            "Poste": postes["poste"],
            "Budget": postes["budget"].map(eur),
            "Engagé": postes["engage"].map(eur),
            "Dépassement": (postes["engage"] - postes["budget"]).map(eur),
        })
        st.dataframe(detail, hide_index=True, width="stretch",
                     height=min(420, 40 + 35 * len(detail)))
    else:
        st.success("Aucun poste engagé au-delà de son budget à ce jour "
                   "sur cette opération.")


def page_rythme():
    st.header("Rythme de vente")
    phrase_decision(
        "Décider des hypothèses de commercialisation 2026 : combien de "
        "réservations attendre selon l'évolution des taux de crédit, et "
        "quand chaque programme sera écoulé.")
    serie = serie_intensite().dropna(subset=["intensite"])

    st.subheader("Scénario de taux 2026")
    st.caption(
        "Sensibilité de la demande au coût du crédit, mesurée sur dix ans "
        "d'historique du groupe : une hausse de 1 point des taux réduit les "
        "réservations d'environ 19 % ; une baisse produit l'effet inverse.")
    beta = -0.216
    taux_actuel = float(serie["taux_credit_habitat"].iloc[-1])
    scenario = st.slider("Taux des crédits habitat fin 2026 (%)", 2.0, 5.0,
                         taux_actuel, 0.1)
    base_rythme = float(serie["intensite"].iloc[-6:].mean())
    facteur = float(np.exp(beta * (scenario - taux_actuel)))
    ops_actives = int(serie["operations_actives"].iloc[-1])
    rythme_attendu = base_rythme * facteur
    st.markdown(
        f'<div class="resultat">Si les taux passent à '
        f'<b>{pct(scenario / 100, 1)}</b>, le rythme attendu est de '
        f'<b>{fr(rythme_attendu, 1)} réservations par mois</b> et par '
        f'opération, soit <b>{pct(facteur - 1, 1, signe=True)}</b> par '
        f'rapport à aujourd\'hui — environ '
        f'<b>{fr(rythme_attendu * ops_actives * 12)}</b> réservations sur un '
        f'an pour les {ops_actives} opérations en cours de '
        f'commercialisation.</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Taux simulé", pct(scenario / 100, 1),
              f"{fr(scenario - taux_actuel, 1)} pt vs aujourd'hui",
              delta_color="off")
    c2.metric("Rythme attendu", f"{fr(rythme_attendu, 1)} résa/mois",
              pct(facteur - 1, 1, signe=True),
              help="Réservations mensuelles attendues par opération en cours "
                   "de commercialisation.")
    c3.metric("Réservations groupe sur un an",
              fr(rythme_attendu * ops_actives * 12),
              help=f"Sur la base des {ops_actives} opérations actuellement "
                   "en cours de commercialisation.")

    st.subheader("Historique : rythme de vente et taux de crédit")
    g1, g2 = st.columns(2)
    with g1:
        st.line_chart(serie["intensite"].rename("Réservations par opération et par mois"),
                      color=BLEU, height=240)
    with g2:
        st.line_chart(serie["taux_credit_habitat"].rename("Taux crédit habitat (%)"),
                      color=VERT, height=240)

    st.subheader("Trajectoire de vente d'un programme et délai d'écoulement")
    eco = sql("""SELECT e.* FROM v_ecoulement_mensuel e
                 JOIN operations o USING (id_operation)
                 WHERE o.activite = 'Promotion'""")
    libs = sql("""SELECT id_operation, libelle FROM operations
                  WHERE activite = 'Promotion'""")
    tot = eco.groupby("id_operation")["nb_reservations"].sum()
    choix_ids = tot[tot >= 40].index
    noms = libs[libs["id_operation"].isin(choix_ids)].set_index("libelle")["id_operation"]
    nom_op = st.selectbox("Programme", sorted(noms.index))
    g = eco[eco["id_operation"] == noms[nom_op]].copy()
    g["mois"] = pd.PeriodIndex(g["mois"], freq="M")
    idx = pd.period_range(g["mois"].min(), g["mois"].max(), freq="M")
    cum = g.set_index("mois")["nb_reservations"].reindex(idx).fillna(0).cumsum()
    t = np.arange(len(cum), dtype=float)
    graphe = pd.DataFrame({"Réservations cumulées": cum.values},
                          index=idx.to_timestamp())
    try:
        from scipy.optimize import curve_fit
        total = cum.iloc[-1]
        p, _ = curve_fit(lambda tt, L, k, t0: L / (1 + np.exp(-k * (tt - t0))),
                         t, cum.values, p0=[total, 0.3, len(t) / 2],
                         bounds=([0.8 * total, 0.01, 0], [1.5 * total, 3, 2 * len(t)]),
                         maxfev=20000)
        graphe["Trajectoire estimée"] = p[0] / (1 + np.exp(-p[1] * (t - p[2])))
        delai90 = p[2] + np.log(9) / p[1]
        st.caption(f"Estimation du délai d'écoulement : 90 % du programme "
                   f"vendu environ {fr(delai90)} mois après l'ouverture des "
                   "ventes. Estimation fiable surtout sur les programmes "
                   "proches de l'épuisement du stock.")
    except RuntimeError:
        st.caption("Programme trop tôt dans sa commercialisation pour "
                   "estimer un délai d'écoulement fiable — courbe observée "
                   "seule.")
    st.line_chart(graphe, color=[BLEU, AMBRE][: graphe.shape[1]], height=280)


def page_prix():
    st.header("Pilotage des prix")
    phrase_decision(
        "Décider des ajustements de grille : repérer les lots vendus "
        "au-dessus ou en dessous du marché, puis simuler une baisse ciblée "
        "pour atteindre un objectif de ventes sans sacrifier le chiffre "
        "d'affaires.")
    pipe, stock, incertitude = modele_hedonique()
    st.caption(
        f"Prix de marché estimé à partir des ventes comparables du groupe "
        f"(surface, étage, exposition, commune, période), aux conditions "
        f"2026. L'estimation comporte une marge d'incertitude d'environ "
        f"±{pct(incertitude, 0)} : au-delà de cette fourchette, le lot est "
        f"considéré hors marché. {fr(len(stock))} appartements en stock "
        "évalués.")

    def position(r):
        if r > incertitude:
            return "🟠 Au-dessus du marché"
        if r < -incertitude:
            return "🔵 En dessous du marché"
        return "🟢 Dans le marché"
    stock = stock.copy()
    stock["position"] = stock["ecart_marche"].map(position)
    libs = sql("""SELECT id_operation, libelle FROM operations
                  WHERE activite = 'Promotion'""")
    stock = stock.merge(libs, on="id_operation", how="inner")

    c1, c2, c3 = st.columns(3)
    c1.metric("🟢 Dans le marché",
              int((stock["position"] == "🟢 Dans le marché").sum()),
              help="Prix grille cohérent avec les ventes comparables du groupe.")
    c2.metric("🟠 Au-dessus du marché",
              int((stock["position"] == "🟠 Au-dessus du marché").sum()),
              help="Prix grille supérieur au prix de marché estimé : risque "
                   "de mévente, candidats à un ajustement.")
    c3.metric("🔵 En dessous du marché",
              int((stock["position"] == "🔵 En dessous du marché").sum()),
              help="Prix grille inférieur au prix de marché estimé : marge de "
                   "revalorisation possible.")

    st.subheader("Stock : prix grille et écart au marché")
    choix = st.multiselect(
        "Position par rapport au marché",
        ["🟠 Au-dessus du marché", "🔵 En dessous du marché", "🟢 Dans le marché"],
        default=["🟠 Au-dessus du marché", "🔵 En dessous du marché"])
    vue = stock[stock["position"].isin(choix)].sort_values("ecart_marche",
                                                           ascending=False)
    tableau = pd.DataFrame({
        "Opération": vue["libelle"],
        "Lot": vue["numero_lot"],
        "Type": vue["type_lot"],
        "Surface (m²)": vue["surface"].map(lambda s: fr(s, 0)),
        "Étage": vue["etage"].fillna("—"),
        "Prix grille": vue["prix_vente_ttc"].map(eur),
        "Prix de marché estimé": vue["prix_marche_ttc"].map(eur),
        "Écart au marché": vue["ecart_marche"].map(lambda v: pct(v, 1, signe=True)),
        "Position": vue["position"],
    })
    st.dataframe(tableau, hide_index=True, width="stretch", height=420)

    st.subheader("Simulateur d'ajustement de grille")
    st.caption(
        "Choisissez un programme et un objectif d'accélération des ventes : "
        "le simulateur propose un prix par lot qui atteint l'objectif en "
        "préservant au mieux le chiffre d'affaires. Règle de gestion : "
        "baisse maximale de 10 % et hausse maximale de 5 % par lot. "
        "Sensibilité de la demande au prix : une baisse de prix de 1 % "
        "accélère les ventes d'environ 1 %.")
    ops_stock = (stock.groupby(["id_operation", "libelle"]).size()
                 .rename("n").reset_index().query("n >= 5"))
    nom = st.selectbox("Programme à ajuster", sorted(ops_stock["libelle"]))
    id_op = int(ops_stock.set_index("libelle").loc[nom, "id_operation"])
    lots_op = stock[stock["id_operation"] == id_op]
    p = lots_op["prix_vente_ttc"].to_numpy(dtype=float)
    S = len(p)
    ventes_12m = sql(f"""
        SELECT COUNT(*) AS n FROM ventes v
        JOIN lots l USING (id_operation, numero_lot)
        WHERE v.id_operation = {id_op} AND l.nature_lot = 'Appartement'
          AND v.date_reservation >= date('now', '-12 months')""")["n"].iloc[0]
    q0 = float(np.clip(ventes_12m / max(ventes_12m + S, 1), 0.05, 0.95))
    accel = st.slider("Objectif d'accélération des ventes (%)", 0, 10, 8,
                      help="Hausse visée du nombre de lots vendus sur les "
                           "douze prochains mois, obtenue par l'ajustement "
                           "des prix.") / 100
    EPS = -1.0  # sensibilité de la demande au prix : −1 % de prix ≈ +1 % de ventes
    from scipy.optimize import minimize
    V = S * q0 * np.exp(accel)
    resu = minimize(
        lambda d: -(p * (1 + d) * q0 * np.exp(EPS * d)).sum(),
        np.zeros(S), method="SLSQP", bounds=[(-0.10, 0.05)] * S,
        constraints=[{"type": "eq",
                      "fun": lambda d: (q0 * np.exp(EPS * d)).sum() - V}])
    if resu.success:
        reco = pd.DataFrame({
            "Lot": lots_op["numero_lot"].values,
            "Type": lots_op["type_lot"].values,
            "Surface (m²)": [fr(s, 0) for s in lots_op["surface"]],
            "Position": lots_op["position"].values,
            "Prix actuel": [eur(v) for v in lots_op["prix_vente_ttc"]],
            "Prix recommandé": [eur(round(v * (1 + a), -2))
                                for v, a in zip(lots_op["prix_vente_ttc"], resu.x)],
            "Ajustement": [pct(a, 1, signe=True) for a in resu.x],
            "_tri": resu.x,
        }).sort_values("_tri").drop(columns="_tri")
        st.dataframe(reco, hide_index=True, width="stretch",
                     height=min(420, 40 + 35 * len(reco)))
        R0 = float((p * q0).sum())
        R1 = float((p * (1 + resu.x) * q0 * np.exp(EPS * resu.x)).sum())
        st.markdown(
            f'<div class="resultat">Avec cette grille ajustée : ventes '
            f'attendues sur douze mois <b>{fr(S * q0, 1)} → {fr(V, 1)} lots'
            f'</b> ; chiffre d\'affaires attendu <b>{eur(R0)} → {eur(R1)}</b> '
            f'({pct(R1 / R0 - 1, 1, signe=True)}).</div>',
            unsafe_allow_html=True)
    else:
        st.warning("Cet objectif d'accélération n'est pas atteignable avec "
                   "des baisses limitées à 10 % par lot. Réduisez l'objectif "
                   "visé.")


def page_qualite():
    st.header("Qualité commerciale")
    phrase_decision(
        "Décider où fiabiliser la saisie commerciale et objectiver les "
        "motifs de désistement, agence par agence ; retrouver rapidement des "
        "dossiers comparables à une situation donnée.")

    st.subheader("Motifs de désistement par agence")
    motifs = sql("""
        SELECT o.agence, v.motif_desistement, COUNT(*) AS n
        FROM ventes v JOIN operations o USING (id_operation)
        WHERE v.motif_desistement IS NOT NULL AND o.activite = 'Promotion'
        GROUP BY o.agence, v.motif_desistement""")
    motifs["agence"] = motifs["agence"].str.strip()
    pivot = (motifs.pivot(index="agence", columns="motif_desistement", values="n")
             .fillna(0))
    pivot = pivot.div(pivot.sum(axis=1), axis=0)
    pivot = pivot[pivot.sum().sort_values(ascending=False).index]
    pivot.index.name = "Agence"
    st.dataframe(pivot.style.format(lambda v: pct(v, 0))
                 .background_gradient(cmap="Blues", axis=None),
                 width="stretch")
    part_autres = float(pivot.loc[
        pivot.index.str.contains("Salon"), "Autres motifs"].max()) \
        if "Autres motifs" in pivot.columns else float("nan")
    st.warning(
        f"**Qualité de saisie — Salon-de-Provence** : "
        f"{pct(part_autres, 0)} des désistements de cette agence sont "
        "enregistrés sous « Autres motifs », contre moins de 5 % ailleurs. "
        "Il s'agit d'un défaut de saisie dans l'outil commercial, pas d'un "
        "vrai profil de clientèle : à fiabiliser avant toute conclusion sur "
        "cette agence.")
    st.caption("Lecture : part de chaque motif dans les désistements de "
               "l'agence. Le financement (refus de prêt) et la rétractation "
               "dans les 10 jours dominent partout ailleurs.")

    st.subheader("Rechercher des dossiers similaires")
    st.caption("Retrouvez les dossiers de vente dont le commentaire évoque "
               "une situation donnée (refus de prêt, remise, contentieux…), "
               "pour documenter un cas ou préparer une revue d'agence.")
    requete = st.text_input("Situation recherchée", "refus de prêt banque")
    if requete.strip():
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        ventes = sql("""SELECT v.id_operation, o.libelle, v.numero_lot,
                               v.commentaire_vente, v.desiste
                        FROM ventes v JOIN operations o USING (id_operation)
                        WHERE v.commentaire_vente IS NOT NULL
                          AND o.activite = 'Promotion'""")
        vec = TfidfVectorizer(lowercase=True, min_df=2)
        M = vec.fit_transform(ventes["commentaire_vente"])
        sims = cosine_similarity(vec.transform([requete.lower()]), M).ravel()
        top = np.argsort(-sims)[:8]
        top = [i for i in top if sims[i] > 0]
        if top:
            resultat = pd.DataFrame({
                "Opération": ventes.iloc[top]["libelle"].values,
                "Lot": ventes.iloc[top]["numero_lot"].values,
                "Commentaire du dossier": ventes.iloc[top]["commentaire_vente"].values,
                "Dossier désisté": ["Oui" if d else "Non"
                                    for d in ventes.iloc[top]["desiste"]],
            })
            st.dataframe(resultat, hide_index=True, width="stretch",
                         height=min(320, 40 + 35 * len(resultat)))
        else:
            st.info("Aucun dossier ne correspond à cette recherche.")


PAGES = {
    "Vue d'ensemble": page_vue_ensemble,
    "Alertes marge": page_alertes,
    "Rythme de vente": page_rythme,
    "Pilotage des prix": page_prix,
    "Qualité commerciale": page_qualite,
}

with st.sidebar:
    st.markdown("## 🏗️ Copilote Financier")
    st.caption("Groupe Angelotti — Direction Financière")
    choix = st.radio("Navigation", list(PAGES), label_visibility="collapsed")
    st.markdown("---")
    st.caption("Périmètre : opérations de promotion immobilière "
               "(147 opérations). Données de gestion au 30/06/2026.")

entete()
PAGES[choix]()
pied_de_page()
