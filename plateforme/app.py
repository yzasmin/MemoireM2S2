# -*- coding: utf-8 -*-
"""Copilote Financier — Groupe Angelotti.

Plateforme d'aide à la décision (Streamlit) adossée à la base
`data/copilote.db` et aux modèles construits dans les notebooks 00 à 06.

Lancement :  streamlit run plateforme/app.py
(la base et les modèles se reconstruisent automatiquement s'ils manquent :
`python src/base_sql.py` puis notebook 03 pour le modèle de risque).
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

# Palette du mémoire (src/theme_viz.py)
BLEU, VERT, AMBRE, VIOLET = "#2a78d6", "#1baf7a", "#eda100", "#4a3aa7"
ROUGE = "#e34948"

st.set_page_config(page_title="Copilote Financier — Angelotti",
                   page_icon="🏗️", layout="wide")


# ---------------------------------------------------------------- données
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
    """Modèle de l'axe A sérialisé par le notebook 03 (reconstruit sinon)."""
    chemin = MODELES / "risque_marge.joblib"
    if chemin.exists():
        return joblib.load(chemin)
    return None


@st.cache_data
def features_marge():
    """Reconstruit les variables de l'axe A (mêmes requêtes que le notebook 03)."""
    con = base()
    b = pd.read_sql("""
        SELECT id_operation, sens, poste_niv1,
               SUM(budget_ht) AS budget, SUM(engage_ht) AS engage
        FROM budget GROUP BY id_operation, sens, poste_niv1""", con)
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
        FROM operations o LEFT JOIN communes c USING (commune_norm)""", con)
    com = pd.read_sql("""
        SELECT id_operation, COUNT(*) AS nb_dossiers, AVG(desiste) AS taux_desistement,
               AVG(prix_vente_ttc) AS prix_moyen
        FROM ventes GROUP BY id_operation""", con)
    df = (df.reset_index().merge(parts.reset_index(), on="id_operation")
            .merge(ops, on="id_operation", how="left")
            .merge(com, on="id_operation", how="left"))
    df = df[df["rec_budget"] > 0]
    df["log_recettes"] = np.log(df["rec_budget"])
    df["marge_relative_budget"] = df["marge_budget"] / df["rec_budget"]
    df["taux_desistement"] = df["taux_desistement"].fillna(0)
    df["nb_dossiers"] = df["nb_dossiers"].fillna(0)
    df["littoral"] = df["littoral"].fillna(0)
    df["log_population"] = np.log(df["population"].fillna(df["population"].median()))
    return df


@st.cache_resource
def modele_hedonique():
    """Ré-entraîne le modèle hédonique du notebook 05 (rapide : ~5 000 lignes)."""
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
            USING (id_operation, numero_lot)""", con)
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
    rmse = float(np.sqrt((resid ** 2).mean()))
    stock["y_pred"] = pipe.predict(stock[num + cat])
    stock["cherte"] = stock["y"] - stock["y_pred"]
    stock["prix_hedonique_ttc"] = np.exp(stock["y_pred"]) * stock["surface"]
    return pipe, stock, rmse


@st.cache_data
def serie_intensite():
    con = base()
    v = pd.read_sql("""SELECT date_reservation, id_operation FROM ventes
                       WHERE date_reservation IS NOT NULL""", con,
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


# ------------------------------------------------------------------ pages
def page_accueil():
    st.title("🏗️ Copilote Financier — Groupe Angelotti")
    st.caption("Aide à la décision sur trois axes : risque de marge, vitesse "
               "d'écoulement, prix. Mémoire M2 MIASHS — données de gestion "
               "réelles (267 opérations, 16 467 lignes de grille, 64 788 "
               "lignes budgétaires).")
    df = features_marge()
    stock = sql("SELECT SUM(nb_en_stock) AS s FROM v_stock_lots")["s"].iloc[0]
    serie = serie_intensite().dropna(subset=["intensite"])
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Opérations suivies", f"{len(df)}")
    mures = df[df["taux_engagement"] >= 0.6]
    c2.metric("Opérations en dérive de marge",
              f"{(mures['variation_marge'] < -0.02).sum()} / {len(mures)}",
              help="Dérive committée > 2 % de la marge budgétée, "
                   "opérations engagées à plus de 60 %")
    c3.metric("Lots principaux en stock", f"{int(stock)}")
    c4.metric("Rythme actuel",
              f"{serie['intensite'].iloc[-3:].mean():.1f} résa/op/mois",
              f"taux crédit {serie['taux_credit_habitat'].iloc[-1]:.2f} %",
              delta_color="off")
    st.divider()
    st.markdown("""
| Axe | Question métier | Modèles (notebook) |
|---|---|---|
| 🅰️ **Risque marge** | Quelles opérations vont déraper ? | Régression régularisée, classification F1 (nb 03) |
| 🅱️ **Écoulement** | À quel rythme vend-on, et sous quels taux 2026 ? | Effets aléatoires, ARIMAX, sigmoïde (nb 04) |
| 🅲 **Prix** | Quel prix pour chaque lot en stock ? | Hédonique OLS, optimisation sous contrainte (nb 05) |

La démarche complète (EDA, SQL/Spark, typologie PCA, texte et réseau) est
documentée dans les notebooks 00 à 06 et le `journal_de_bord.md` du dépôt.
""")


def page_risque():
    st.title("🅰️ Risque de dérive de marge")
    df = features_marge()
    art = modele_risque()
    mures = df[(df["taux_engagement"] >= 0.6) & (df["marge_budget"].abs() > 5e4)].copy()

    if art is not None:
        X = mures[art["variables"]].to_numpy(dtype=float)
        proba = art["modele"].predict_proba(X)[:, 1]
        mures["proba_derive"] = proba
        st.caption(f"Modèle : {type(art['modele']).__name__} entraîné au "
                   f"notebook 03 (F1 validation croisée = {art['f1_cv']:.2f} ; "
                   f"seuil de dérive matérielle −2 % de la marge).")
    else:
        mures["proba_derive"] = np.nan
        st.warning("Modèle non trouvé : exécuter le notebook 03 "
                   "(`python src/nb_specs/nb03_marge.py`).")

    en_cours = mures[mures["statut"] == "En Cours"].copy()
    en_cours["derive_constatee"] = mures["variation_marge"]
    tri = en_cours.sort_values("proba_derive", ascending=False)
    st.subheader("Opérations en cours, classées par probabilité de dérive")
    tableau = tri[["libelle", "agence", "taux_engagement", "marge_relative_budget",
                   "taux_desistement", "proba_derive", "derive_constatee"]].head(20)
    st.dataframe(
        tableau.style.format({
            "taux_engagement": "{:.0%}", "marge_relative_budget": "{:+.1%}",
            "taux_desistement": "{:.0%}", "proba_derive": "{:.0%}",
            "derive_constatee": "{:+.1%}"})
        .background_gradient(subset=["proba_derive"], cmap="Reds", vmin=0, vmax=1),
        width="stretch", height=520)
    st.caption("« Dérive constatée » = dépassements déjà engagés (photo à date) ; "
               "la probabilité anticipe la dérive à partir de la structure du "
               "budget initial et des signaux commerciaux — jamais du réalisé "
               "comptable (anti-fuite, notebook 03 §1).")


def page_ecoulement():
    st.title("🅱️ Vitesse d'écoulement et scénarios de taux")
    serie = serie_intensite().dropna(subset=["intensite"])

    st.subheader("Rythme observé et conjoncture")
    c1, c2 = st.columns(2)
    with c1:
        st.line_chart(serie["intensite"].rename("réservations / opération active"),
                      color=BLEU, height=240)
    with c2:
        st.line_chart(serie[["taux_credit_habitat"]].rename(
            columns={"taux_credit_habitat": "taux crédit habitat (%)"}),
            color=VERT, height=240)

    st.subheader("Simulateur 2026 : effet d'un scénario de taux")
    st.caption("Élasticité du modèle à effets aléatoires (notebook 04, "
               "p < 10⁻¹⁵) : +1 point de taux ⇒ −19 % de réservations "
               "mensuelles. Trajectoire de référence = dernier rythme observé.")
    beta = -0.216
    taux_actuel = float(serie["taux_credit_habitat"].iloc[-1])
    scenario = st.slider("Taux des crédits habitat fin 2026 (%)", 2.0, 5.0,
                         taux_actuel, 0.1)
    base_rythme = float(serie["intensite"].iloc[-6:].mean())
    facteur = float(np.exp(beta * (scenario - taux_actuel)))
    c1, c2, c3 = st.columns(3)
    c1.metric("Taux simulé", f"{scenario:.1f} %", f"{scenario-taux_actuel:+.1f} pt")
    c2.metric("Rythme attendu", f"{base_rythme*facteur:.2f} résa/op/mois",
              f"{100*(facteur-1):+.0f} %")
    ops_actives = int(serie["operations_actives"].iloc[-1])
    c3.metric("Réservations groupe / an",
              f"{base_rythme*facteur*ops_actives*12:.0f}",
              help=f"Sur la base de {ops_actives} opérations actives")

    st.subheader("Trajectoire d'écoulement par opération (sigmoïde)")
    eco = sql("SELECT * FROM v_ecoulement_mensuel")
    libs = sql("SELECT id_operation, libelle FROM operations")
    tot = eco.groupby("id_operation")["nb_reservations"].sum()
    choix_ids = tot[tot >= 40].index
    noms = libs[libs["id_operation"].isin(choix_ids)].set_index("libelle")["id_operation"]
    nom_op = st.selectbox("Opération", sorted(noms.index))
    g = eco[eco["id_operation"] == noms[nom_op]].copy()
    g["mois"] = pd.PeriodIndex(g["mois"], freq="M")
    idx = pd.period_range(g["mois"].min(), g["mois"].max(), freq="M")
    cum = g.set_index("mois")["nb_reservations"].reindex(idx).fillna(0).cumsum()
    t = np.arange(len(cum), dtype=float)
    graphe = pd.DataFrame({"cumul observé": cum.values}, index=idx.to_timestamp())
    try:
        from scipy.optimize import curve_fit
        total = cum.iloc[-1]
        p, _ = curve_fit(lambda tt, L, k, t0: L / (1 + np.exp(-k * (tt - t0))),
                         t, cum.values, p0=[total, 0.3, len(t) / 2],
                         bounds=([0.8 * total, 0.01, 0], [1.5 * total, 3, 2 * len(t)]),
                         maxfev=20000)
        graphe["sigmoïde ajustée"] = p[0] / (1 + np.exp(-p[1] * (t - p[2])))
        delai90 = p[2] + np.log(9) / p[1]
        st.caption(f"Vitesse k = {p[1]:.2f} ; 90 % du potentiel atteint à "
                   f"{delai90:.0f} mois (voir notebook 04 §5 — fiable sur les "
                   "opérations proches de l'épuisement du stock).")
    except RuntimeError:
        st.caption("Ajustement sigmoïde non convergé (opération trop tôt dans "
                   "sa commercialisation) — cumul observé seul.")
    st.line_chart(graphe, color=[BLEU, AMBRE][: graphe.shape[1]], height=280)


def page_prix():
    st.title("🅲 Prix : diagnostic du stock et recommandations")
    pipe, stock, rmse = modele_hedonique()
    st.caption(f"Modèle hédonique du notebook 05 (R² test ≈ 0,89, erreur type "
               f"±{rmse:.0%} sur le prix). {len(stock)} appartements en stock "
               "scorés aux conditions de marché 2026.")

    def diagnostic(r):
        if r > rmse:
            return "surcoté"
        if r < -rmse:
            return "sous-coté"
        return "dans le marché"
    stock = stock.copy()
    stock["diagnostic"] = stock["cherte"].map(diagnostic)
    libs = sql("SELECT id_operation, libelle FROM operations")
    stock = stock.merge(libs, on="id_operation", how="left")

    c1, c2, c3 = st.columns(3)
    c1.metric("Dans le marché",
              int((stock["diagnostic"] == "dans le marché").sum()))
    c2.metric("Surcotés (> +1 RMSE)", int((stock["diagnostic"] == "surcoté").sum()))
    c3.metric("Sous-cotés (< −1 RMSE)", int((stock["diagnostic"] == "sous-coté").sum()))

    st.subheader("Lots en stock : prix grille vs prix de marché estimé")
    filtre = st.multiselect("Diagnostic", ["surcoté", "sous-coté", "dans le marché"],
                            default=["surcoté", "sous-coté"])
    vue = stock[stock["diagnostic"].isin(filtre)]
    tableau = (vue[["libelle", "numero_lot", "type_lot", "surface", "etage",
                    "prix_vente_ttc", "prix_hedonique_ttc", "cherte", "diagnostic"]]
               .rename(columns={"libelle": "opération",
                                "prix_hedonique_ttc": "prix marché estimé"})
               .sort_values("cherte", ascending=False))
    st.dataframe(tableau.style.format({
        "surface": "{:.0f}", "prix_vente_ttc": "{:,.0f} €",
        "prix marché estimé": "{:,.0f} €", "cherte": "{:+.0%}"}),
        width="stretch", height=420)

    st.subheader("Recommandation d'ajustement (opération avec objectif d'écoulement)")
    st.caption("Optimisation du notebook 05 §4 : maximiser le revenu attendu "
               "sous objectif de volume, bornes −10 % / +5 %. La solution "
               "analytique (multiplicateur de Lagrange, ε = −1) impose le même "
               "effort en euros sur chaque lot.")
    ops_stock = (stock.groupby(["id_operation", "libelle"]).size()
                 .rename("n").reset_index().query("n >= 5"))
    nom = st.selectbox("Opération à optimiser", sorted(ops_stock["libelle"]))
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
    accel = st.slider("Accélération d'écoulement visée (%)", 0, 10, 8) / 100
    EPS = -1.0
    from scipy.optimize import minimize
    V = S * q0 * np.exp(accel)
    resu = minimize(
        lambda d: -(p * (1 + d) * q0 * np.exp(EPS * d)).sum(),
        np.zeros(S), method="SLSQP", bounds=[(-0.10, 0.05)] * S,
        constraints=[{"type": "eq",
                      "fun": lambda d: (q0 * np.exp(EPS * d)).sum() - V}])
    if resu.success:
        reco = lots_op[["numero_lot", "type_lot", "surface",
                        "prix_vente_ttc", "diagnostic"]].copy()
        reco["ajustement"] = resu.x
        reco["prix recommandé"] = (reco["prix_vente_ttc"] * (1 + resu.x)).round(-2)
        st.dataframe(reco.sort_values("ajustement").style.format({
            "surface": "{:.0f}", "prix_vente_ttc": "{:,.0f} €",
            "prix recommandé": "{:,.0f} €", "ajustement": "{:+.1%}"}),
            width="stretch")
        R0 = float((p * q0).sum())
        R1 = float((p * (1 + resu.x) * q0 * np.exp(EPS * resu.x)).sum())
        st.caption(f"Ventes attendues à 12 mois : {S*q0:.1f} → {V:.1f} lots ; "
                   f"revenu attendu : {R0/1e6:.2f} → {R1/1e6:.2f} M€ "
                   f"({100*(R1/R0-1):+.1f} %).")
    else:
        st.warning("Objectif d'écoulement inatteignable dans les bornes "
                   "−10 %/+5 % (avec ε = −1, le volume gagne au plus ~10,5 %). "
                   "Réduire l'accélération visée.")


def page_signaux():
    st.title("🔎 Signaux faibles : texte et réseau")
    st.caption("Axe transverse du notebook 06 — recherche par similarité "
               "cosinus sur les 9 688 commentaires de vente, et profil des "
               "motifs de désistement par agence.")

    st.subheader("Moteur de recherche dans les commentaires de vente")
    requete = st.text_input("Requête", "refus de prêt banque")
    if requete.strip():
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        ventes = sql("""SELECT v.id_operation, o.libelle, v.numero_lot,
                               v.commentaire_vente, v.desiste
                        FROM ventes v JOIN operations o USING (id_operation)
                        WHERE v.commentaire_vente IS NOT NULL""")
        vec = TfidfVectorizer(lowercase=True, min_df=2)
        M = vec.fit_transform(ventes["commentaire_vente"])
        sims = cosine_similarity(vec.transform([requete.lower()]), M).ravel()
        top = np.argsort(-sims)[:8]
        resultat = ventes.iloc[top][["libelle", "numero_lot",
                                     "commentaire_vente", "desiste"]].copy()
        resultat["similarité"] = sims[top].round(2)
        st.dataframe(resultat[resultat["similarité"] > 0],
                     width="stretch", height=320)

    st.subheader("Motifs de désistement par agence")
    motifs = sql("""
        SELECT o.agence, v.motif_desistement, COUNT(*) AS n
        FROM ventes v JOIN operations o USING (id_operation)
        WHERE v.motif_desistement IS NOT NULL
        GROUP BY o.agence, v.motif_desistement""")
    pivot = (motifs.pivot(index="agence", columns="motif_desistement", values="n")
             .fillna(0))
    pivot = pivot.div(pivot.sum(axis=1), axis=0)
    st.dataframe(pivot.style.format("{:.0%}")
                 .background_gradient(cmap="Blues", axis=None),
                 width="stretch")
    st.caption("Le notebook 06 (§6) montre par divergence de Kullback-Leibler "
               "que le profil de Salon-de-Provence est un artefact de saisie "
               "(90 % « Autres motifs ») — à fiabiliser avant analyse.")


PAGES = {
    "Accueil": page_accueil,
    "🅰️ Risque marge": page_risque,
    "🅱️ Écoulement": page_ecoulement,
    "🅲 Prix": page_prix,
    "🔎 Signaux faibles": page_signaux,
}

with st.sidebar:
    st.markdown("## Copilote Financier")
    choix = st.radio("Navigation", list(PAGES), label_visibility="collapsed")
    st.markdown("---")
    st.caption("Mémoire M2 MIASHS — Groupe Angelotti (Nexity).\n\n"
               "Base : `data/copilote.db` — reconstruite depuis les exports "
               "bruts par `python src/base_sql.py`.")
PAGES[choix]()
