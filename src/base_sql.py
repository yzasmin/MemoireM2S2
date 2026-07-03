"""Construction de la base SQLite `data/copilote.db` (module Bases de données SQL).

Schéma en étoile simplifié :
- dimensions : operations, communes, conjoncture
- faits      : budget (lignes analytiques), lots, ventes (événements),
               desistements (détail client)
- vues métier SQL : v_marge_operation, v_ecoulement_mensuel, v_stock_lots

Les vues sont écrites en SQL pur pour démontrer les jointures, agrégations
et fenêtres vues en cours de bases de données.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from nettoyage import RACINE, construire_tout

DB = RACINE / "data" / "copilote.db"

VUES = {
    # Marge par opération : budget vs engagé/facturé, calculée en SQL.
    "v_marge_operation": """
        CREATE VIEW v_marge_operation AS
        SELECT
            o.id_operation,
            o.libelle,
            o.agence,
            o.statut,
            o.commune_norm,
            SUM(CASE WHEN b.sens = 'R' THEN b.budget_ht  ELSE 0 END) AS recettes_budget,
            SUM(CASE WHEN b.sens = 'D' THEN b.budget_ht  ELSE 0 END) AS depenses_budget,
            SUM(CASE WHEN b.sens = 'R' THEN b.facture_ht ELSE 0 END) AS recettes_facturees,
            SUM(CASE WHEN b.sens = 'D' THEN b.engage_ht  ELSE 0 END) AS depenses_engagees,
            SUM(CASE WHEN b.sens = 'D' THEN b.facture_ht ELSE 0 END) AS depenses_facturees,
            SUM(CASE WHEN b.sens = 'R' THEN b.budget_ht  ELSE -b.budget_ht END) AS marge_budget,
            CASE WHEN SUM(CASE WHEN b.sens = 'D' THEN b.budget_ht ELSE 0 END) > 0
                 THEN SUM(CASE WHEN b.sens = 'D' THEN b.engage_ht ELSE 0 END)
                      / SUM(CASE WHEN b.sens = 'D' THEN b.budget_ht ELSE 0 END)
            END AS taux_engagement
        FROM operations o
        JOIN budget b USING (id_operation)
        GROUP BY o.id_operation
    """,
    # Rythme de réservations par opération et par mois (données répétées).
    "v_ecoulement_mensuel": """
        CREATE VIEW v_ecoulement_mensuel AS
        SELECT
            v.id_operation,
            strftime('%Y-%m', v.date_reservation) AS mois,
            COUNT(*)                               AS nb_reservations,
            SUM(v.desiste)                         AS nb_desistements,
            AVG(v.prix_vente_ttc)                  AS prix_moyen_ttc
        FROM ventes v
        WHERE v.date_reservation IS NOT NULL
        GROUP BY v.id_operation, strftime('%Y-%m', v.date_reservation)
    """,
    # État du stock par opération (photo à date d'export).
    "v_stock_lots": """
        CREATE VIEW v_stock_lots AS
        SELECT
            l.id_operation,
            COUNT(*)                                                  AS nb_lots,
            SUM(CASE WHEN l.statut_lot = 'En stock' THEN 1 ELSE 0 END) AS nb_en_stock,
            SUM(CASE WHEN l.statut_lot IN ('Vendu', 'Livré') THEN 1 ELSE 0 END) AS nb_vendus,
            AVG(l.prix_m2_ttc)                                        AS prix_m2_moyen
        FROM lots l
        WHERE l.principal_secondaire = 'Principal'
        GROUP BY l.id_operation
    """,
}


def construire_base(chemin: Path = DB) -> Path:
    tables = construire_tout()
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.unlink(missing_ok=True)
    with sqlite3.connect(chemin) as con:
        for nom, df in tables.items():
            df.to_sql(nom, con, index=False)
        cur = con.cursor()
        cur.execute("CREATE INDEX ix_budget_op ON budget(id_operation)")
        cur.execute("CREATE INDEX ix_ventes_op ON ventes(id_operation)")
        cur.execute("CREATE INDEX ix_lots_op ON lots(id_operation)")
        for sql in VUES.values():
            cur.execute(sql)
    return chemin


if __name__ == "__main__":
    p = construire_base()
    with sqlite3.connect(p) as con:
        for (nom,) in con.execute(
            "SELECT name FROM sqlite_master WHERE type IN ('table','view') ORDER BY type, name"
        ):
            n = con.execute(f'SELECT COUNT(*) FROM "{nom}"').fetchone()[0]
            print(f"{nom:25s} {n:7d} lignes")
