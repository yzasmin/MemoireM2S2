"""Nettoyage des exports bruts du Groupe Angelotti.

Transforme les 4 exports Excel de `donnéebrut/` en tables propres et typées,
prêtes à être chargées dans la base SQLite (voir `src/base_sql.py`).

Choix de nettoyage documentés dans docs/02_dictionnaire_donnees.md et
journal_de_bord.md :
- « Budget & EFR » = détail analytique niveau 3 (64 788 lignes) + 212 lignes
  de synthèse sans sens Dépenses/Recettes, réconcilié à l'euro près avec
  A_DM_BUDGET_MONTANT_GESTION_LIVE (écart médian nul sur 118 opérations).
- « 06_Informations Lots » ne contient QUE les dossiers désistés : c'est un
  export de détail des désistements (2 164 lignes), pas la table des lots.
- La table maîtresse lot × dossier est « Grille de Prix Avec Desistements ».
- Les libellés de nature de lot sont hétérogènes (appt/Appartement,
  stat/Parking extérieur…) : harmonisés via NATURE_LOT_MAP.
- Les communes en doublon orthographique (LATOUR BAS ELNE / LATOUR-BAS-ELNE,
  SAINTES MARIES…) sont normalisées via le référentiel geo.api.gouv.fr.
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

RACINE = Path(__file__).resolve().parent.parent
BRUT = RACINE / "donnéebrut"
EXTERNE = RACINE / "data" / "externe"
INTERIM = RACINE / "data" / "interim"

FICHIERS = {
    "grille": BRUT / "Grille de Prix Avec Desistements.xlsx",
    "lots_desistes": BRUT / "06_Informations Lots.xlsx",
    "budget_efr": BRUT / "Budget & EFR.xlsx",
    "budget_live": BRUT / "A_DM_BUDGET_MONTANT_GESTION_LIVE.xlsx",
}

# Harmonisation des natures de lot observées dans la grille de prix.
NATURE_LOT_MAP = {
    "appartement": "Appartement",
    "appt": "Appartement",
    "villa": "Maison",
    "maison": "Maison",
    "terrain à batir": "Terrain",
    "terrain à bâtir": "Terrain",
    "terrain brut": "Terrain",
    "parking extérieur": "Stationnement",
    "parking sous sol": "Stationnement",
    "parking": "Stationnement",
    "stat": "Stationnement",
    "stat (couv)": "Stationnement",
    "garage": "Stationnement",
    "box": "Stationnement",
    "local commercial": "Local",
    "local": "Local",
    "bureau": "Local",
    "cave": "Annexe",
    "annexe": "Annexe",
    "jardin": "Annexe",
    "macro lot": "Macro-lot",
}


def _normalise_texte(s: str) -> str:
    """Majuscules sans accent, espaces et tirets uniformisés (clé de jointure)."""
    if pd.isna(s):
        return s
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode()
    s = re.sub(r"[-']", " ", s.upper())
    s = re.sub(r"\bST\b", "SAINT", s)
    s = re.sub(r"\bSTE\b", "SAINTE", s)
    return re.sub(r"\s+", " ", s).strip()


def _lire(source: str) -> pd.DataFrame:
    """Lit un export brut, avec cache pickle pour éviter de relire l'Excel."""
    cache = INTERIM / f"{source}_raw.pkl"
    if cache.exists():
        return pd.read_pickle(cache)
    df = pd.read_excel(FICHIERS[source])
    INTERIM.mkdir(parents=True, exist_ok=True)
    df.to_pickle(cache)
    return df


def table_operations() -> pd.DataFrame:
    """Référentiel des 267 opérations (une ligne par opération).

    La source la plus complète est Budget & EFR (267 opérations, contre 196
    dans la grille de prix : les opérations en étude n'ont pas encore de
    grille).
    """
    b = _lire("budget_efr")
    colonnes = {
        "ID Operation": "id_operation",
        "Code Operation": "code_operation",
        "Code Operation old": "code_operation_gr",
        "Lib Operation": "libelle",
        "Activite Operation": "activite",
        "Agence Operation": "agence",
        "Statut Operation": "statut",
        "Type Operation": "type_operation",
        "Commune Operation": "commune",
        "Code Postal Operation": "code_postal",
        "Lib Societe": "societe",
        "Forme Juridique Societe": "forme_juridique",
    }
    ops = (
        b[list(colonnes)]
        .rename(columns=colonnes)
        .drop_duplicates(subset="id_operation")
        .reset_index(drop=True)
    )
    ops["commune_norm"] = ops["commune"].map(_normalise_texte)
    ops["agence"] = ops["agence"].str.replace("PROMOTION / ", "", regex=False)
    return ops


def table_budget() -> pd.DataFrame:
    """Lignes budgétaires analytiques (niveau 3) : budget vs engagé vs facturé.

    On écarte les 212 lignes de synthèse sans sens Dépenses/Recettes : la
    marge se recalcule proprement comme Recettes - Dépenses.
    """
    b = _lire("budget_efr")
    colonnes = {
        "ID Operation": "id_operation",
        "Depenses / Recettes": "sens",
        "Lib Poste Niv 1": "poste_niv1",
        "Lib Poste Niv 2": "poste_niv2",
        "Lib Poste Niv 3": "poste_niv3",
        "Budget HT": "budget_ht",
        "Pre Engage HT": "pre_engage_ht",
        "Engage HT": "engage_ht",
        "Facture HT": "facture_ht",
        "Regle HT": "regle_ht",
    }
    bud = b[list(colonnes)].rename(columns=colonnes)
    bud = bud.dropna(subset=["sens"]).copy()
    bud["sens"] = bud["sens"].map({"Dépenses": "D", "Recettes": "R"})
    for c in ["budget_ht", "pre_engage_ht", "engage_ht", "facture_ht", "regle_ht"]:
        bud[c] = pd.to_numeric(bud[c], errors="coerce").fillna(0.0)
    return bud.reset_index(drop=True)


def table_lots_ventes() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Sépare la grille de prix en deux tables :

    - `lots`   : une ligne par lot physique (attributs + prix grille) ;
    - `ventes` : une ligne par dossier commercial (réservation, désistement,
      vente, livraison), c'est la table des événements séquentiels.
    """
    g = _lire("grille")

    id_lot = ["ID Operation", "Numero Lot"]
    attributs = {
        "ID Operation": "id_operation",
        "Numero Lot": "numero_lot",
        "Nature Lot": "nature_lot_source",
        "Type Lot": "type_lot",
        "Type Produit": "type_produit",
        "Type Ouvrage": "type_ouvrage",
        "Lot Principal / Secondaire": "principal_secondaire",
        "Surface Lot": "surface",
        "(SHAB) Surface Habitable Lot": "surface_habitable",
        "Surface Terrain Lot": "surface_terrain",
        "Surface Balcon Lot": "surface_balcon",
        "Surface Terrasse Lot": "surface_terrasse",
        "Exposition Lot": "exposition",
        "Etage Lot": "etage",
        "Statut Lot": "statut_lot",
        "Lot Prix Budget TTC": "prix_budget_ttc",
        "Lot Prix Lancement TTC": "prix_lancement_ttc",
        "Lot Prix Vente Commercial TTC": "prix_vente_ttc",
        "Lot Remise Commercial TTC": "remise_ttc",
        "Lot Taux TVA": "taux_tva",
    }
    # Un lot peut apparaître sur plusieurs dossiers (désistement puis
    # revente) : on garde la ligne du dossier le plus récent pour l'état
    # du lot, les événements restent tous dans `ventes`.
    ordre_statut = pd.CategoricalDtype(
        ["Désisté", "Résolution de vente", "En stock", "Réservé", "Vendu", "Livré"],
        ordered=True,
    )
    g2 = g.copy()
    g2["_statut_ord"] = g2["Statut Lot"].astype(ordre_statut)
    lots = (
        g2.sort_values(["_statut_ord", "Date Reservation"])
        .drop_duplicates(subset=id_lot, keep="last")[list(attributs)]
        .rename(columns=attributs)
        .reset_index(drop=True)
    )
    nettoye = lots["nature_lot_source"].str.strip().str.lower()
    lots["nature_lot"] = nettoye.map(NATURE_LOT_MAP).fillna("Autre")
    for c in ["surface", "surface_habitable", "prix_vente_ttc", "prix_budget_ttc"]:
        lots[c] = pd.to_numeric(lots[c], errors="coerce")
    lots.loc[lots["surface"] <= 0, "surface"] = np.nan
    lots.loc[lots["prix_vente_ttc"] <= 0, "prix_vente_ttc"] = np.nan
    lots["prix_m2_ttc"] = lots["prix_vente_ttc"] / lots["surface"]

    evenements = {
        "ID Operation": "id_operation",
        "Numero Lot": "numero_lot",
        "Code Dossier": "code_dossier",
        "Statut Lot": "statut_dossier",
        "Date Reservation": "date_reservation",
        "Date Desistement": "date_desistement",
        "Date Vente": "date_vente",
        "Date Vente Contractuelle": "date_vente_contractuelle",
        "Date Livraison Lot": "date_livraison",
        "Date Accord Pret": "date_accord_pret",
        "Date Demande Pret": "date_demande_pret",
        "Motif Desistement": "motif_desistement",
        "Commentaire Vente": "commentaire_vente",
        "Origine Contact Client": "origine_contact",
        "Nom Vendeur": "nom_vendeur",
        "Vendeur Interne / Externe": "vendeur_interne_externe",
        "Type Tiers Acquereur": "type_acquereur",
        "Qualite Acquereur": "qualite_acquereur",
        "Code Postal Client 1": "code_postal_client",
        "Lot Prix Vente Commercial TTC": "prix_vente_ttc",
    }
    ventes = g[list(evenements)].rename(columns=evenements)
    ventes = ventes.dropna(subset=["code_dossier"]).copy()
    for c in [c for c in ventes.columns if c.startswith("date_")]:
        ventes[c] = pd.to_datetime(ventes[c], errors="coerce")
    ventes["desiste"] = ventes["date_desistement"].notna().astype(int)
    ventes["delai_resa_vente_j"] = (
        ventes["date_vente"] - ventes["date_reservation"]
    ).dt.days
    ventes["commentaire_vente"] = (
        ventes["commentaire_vente"].astype("string").str.replace("_x000d_", " ", regex=False)
    )
    return lots, ventes.reset_index(drop=True)


def table_desistements() -> pd.DataFrame:
    """Détail client/canal des 2 164 dossiers désistés (export 06)."""
    d = _lire("lots_desistes")
    colonnes = {
        "ID Operation": "id_operation",
        "LOT_NUMERO": "numero_lot",
        "ID_DOSSIER": "id_dossier",
        "Statut Lot": "statut",
        "Motif Desistement": "motif_desistement",
        "Canal Vente": "canal_vente",
        "Vendeur Interne / Externe": "vendeur_interne_externe",
        "Taux Commission Lot": "taux_commission",
        "Montant Commission Lot": "montant_commission",
        "Commentaire Vente": "commentaire_vente",
        "Qualite Acquereur": "qualite_acquereur",
        "Nationalite Client 1": "nationalite_client",
        "Code Postal Client 1": "code_postal_client",
        "Date Naissance Client 1": "date_naissance_client",
        "Date Reservation": "date_reservation",
        "Date Desistement": "date_desistement",
    }
    des = d[list(colonnes)].rename(columns=colonnes)
    for c in ["date_reservation", "date_desistement", "date_naissance_client"]:
        des[c] = pd.to_datetime(des[c], errors="coerce")
    des["age_client"] = (
        (des["date_reservation"] - des["date_naissance_client"]).dt.days / 365.25
    ).round(1)
    des.loc[(des["age_client"] < 18) | (des["age_client"] > 100), "age_client"] = np.nan
    des["delai_resa_desist_j"] = (
        des["date_desistement"] - des["date_reservation"]
    ).dt.days
    des["commentaire_vente"] = (
        des["commentaire_vente"].astype("string").str.replace("_x000d_", " ", regex=False)
    )
    des["canal_vente"] = des["canal_vente"].replace("VIDE", pd.NA)
    return des.reset_index(drop=True)


def table_communes() -> pd.DataFrame:
    """Référentiel communes enrichi (geo.api.gouv.fr) + distance au littoral."""
    cm = pd.read_csv(EXTERNE / "communes_geo.csv", dtype={"code_insee": "string", "departement": "string"})
    cm["commune_norm"] = cm["commune_source"].map(_normalise_texte)
    # Proxy littoral : distance au point côtier le plus proche du golfe du
    # Lion (approximation suffisante pour un effet « bord de mer »).
    cote = np.array(
        [[3.05, 43.26], [3.51, 43.28], [4.13, 43.53], [3.00, 42.86], [4.85, 43.40], [5.05, 43.33]]
    )
    def dist_cote(row):
        if pd.isna(row["longitude"]):
            return np.nan
        d = np.sqrt(
            ((cote[:, 0] - row["longitude"]) * 73.0) ** 2
            + ((cote[:, 1] - row["latitude"]) * 111.0) ** 2
        )
        return round(float(d.min()), 1)
    cm["dist_littoral_km"] = cm.apply(dist_cote, axis=1)
    cm["littoral"] = (cm["dist_littoral_km"] < 10).astype(int)
    # Une ligne par commune normalisée (doublons orthographiques fusionnés)
    return cm.sort_values("population", ascending=False).drop_duplicates("commune_norm")


def table_conjoncture() -> pd.DataFrame:
    """Série mensuelle : taux crédit habitat (BCE) + confiance ménages (Eurostat)."""
    taux = pd.read_csv(EXTERNE / "taux_credit_habitat_france.csv")
    conf = pd.read_csv(EXTERNE / "confiance_menages_france.csv")
    conj = taux[["mois", "taux_credit_habitat"]].merge(
        conf[["mois", "confiance_menages"]], on="mois", how="outer"
    ).sort_values("mois").reset_index(drop=True)
    # Le taux BCE est publié avec ~2 mois de retard : on prolonge la série
    # par la dernière valeur connue (hypothèse documentée au journal).
    conj["taux_credit_habitat"] = conj["taux_credit_habitat"].ffill()
    return conj


def construire_tout() -> dict[str, pd.DataFrame]:
    """Exécute tout le nettoyage et renvoie le dictionnaire des tables propres."""
    lots, ventes = table_lots_ventes()
    tables = {
        "operations": table_operations(),
        "budget": table_budget(),
        "lots": lots,
        "ventes": ventes,
        "desistements": table_desistements(),
        "communes": table_communes(),
        "conjoncture": table_conjoncture(),
    }
    return tables


if __name__ == "__main__":
    for nom, df in construire_tout().items():
        print(f"{nom:15s} {df.shape[0]:6d} lignes x {df.shape[1]:3d} colonnes")
