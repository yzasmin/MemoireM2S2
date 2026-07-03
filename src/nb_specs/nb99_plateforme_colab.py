# -*- coding: utf-8 -*-
"""Spécification du notebook 99 — lancer la plateforme Streamlit depuis Google Colab.

Ce notebook n'est PAS exécuté à la construction (il démarre un serveur et un
tunnel réseau) : il est généré sans sorties, prêt à être ouvert dans Colab.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nb_outils import AMORCAGE, construire

C = []

C.append(("md", r"""
# 🏗️ Lancer le Copilote Financier depuis Google Colab

Ce notebook démarre la **plateforme Streamlit** dans Colab et l'expose via
un tunnel temporaire — utile quand le poste de travail ne permet aucune
installation locale.

**Mode d'emploi (3 cellules à exécuter dans l'ordre) :**

1. La cellule d'amorçage clone le dépôt (colle ton token GitHub en lecture
   seule quand il t'est demandé — création : github.com → *Settings* →
   *Developer settings* → *Fine-grained tokens* → dépôt `MemoireM2S2`
   seul, permission *Contents : Read-only*) et reconstruit la base ;
2. La cellule suivante installe Streamlit et entraîne le modèle de risque ;
3. La dernière lance l'application et affiche l'**URL publique** à ouvrir
   dans un nouvel onglet.

⚠️ **Confidentialité** : l'URL du tunnel est aléatoire et meurt avec la
session Colab, mais toute personne qui l'obtient peut voir l'application
(données de gestion internes). Ne la partage pas, et arrête la session
(Exécution → Gérer les sessions → Arrêter) quand tu as terminé.
"""))

C.append(("code", AMORCAGE))

C.append(("code", r'''
# Dépendances de la plateforme + modèle de risque (produit par le notebook 03)
import importlib.util, pathlib, subprocess, sys

for module, paquet in [("streamlit", "streamlit"), ("joblib", "joblib")]:
    if importlib.util.find_spec(module) is None:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", paquet], check=True)

modele = racine / "plateforme" / "modeles" / "risque_marge.joblib"
if not modele.exists():
    print("Modèle de risque absent : exécution du notebook 03 (2-3 minutes)…")
    subprocess.run([sys.executable, str(racine / "src" / "nb_specs" / "nb03_marge.py")],
                   check=True, cwd=racine)
print("Prêt. Modèle :", modele.exists())
'''))

C.append(("code", r'''
# Démarre Streamlit en arrière-plan puis ouvre un tunnel Cloudflare (sans compte)
import subprocess, time, re, urllib.request, pathlib

app = racine / "plateforme" / "app.py"
serveur = subprocess.Popen(
    [sys.executable, "-m", "streamlit", "run", str(app),
     "--server.headless", "true", "--server.port", "8501",
     "--browser.gatherUsageStats", "false"],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=racine)
time.sleep(8)

cf = pathlib.Path("/tmp/cloudflared")
if not cf.exists():
    urllib.request.urlretrieve(
        "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64",
        cf)
    cf.chmod(0o755)

tunnel = subprocess.Popen([str(cf), "tunnel", "--url", "http://localhost:8501"],
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
url = None
for _ in range(60):
    ligne = tunnel.stdout.readline()
    m = re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", ligne)
    if m:
        url = m.group(0)
        break
print("=" * 60)
print("✅ Plateforme en ligne — ouvre cette adresse dans un onglet :")
print(url or "URL non trouvée : ré-exécute cette cellule")
print("=" * 60)
print("(Laisse cette cellule et la session Colab tourner tant que tu utilises l'application.)")
'''))

if __name__ == "__main__":
    construire("99_lancer_plateforme_colab", C, executer=False)
