# Journal — rédaction du chapitre « Copilote Financier »

Une entrée par fichier ou problème rencontré. Résumé en une ligne, puis
détail si utile. (Le journal du projet lui-même est `journal_de_bord.md`.)

## memoire/chapitre_copilote_financier.Rmd

**Résumé : chapitre rédigé selon le sommaire imposé (6 parties), chaque
chiffre tracé jusqu'à une cellule de notebook exécutée ; base de travail à
reformuler par l'auteure avant intégration au mémoire.**

- Positionnement assumé en tête de fichier (encadré « Note de
  rédaction ») : le texte est une base préparée avec assistance, pas un
  texte à faire passer pour une rédaction personnelle — l'appropriation et
  la reformulation restent à la charge de l'auteure.
- Le sommaire ne prévoit pas de section pour la typologie PCA/clustering
  (notebook 02) : intégrée en fin de 4.1 (« Exploration ») car c'est de
  l'analyse exploratoire ; aucun ajout de sous-section au sommaire.
- Chiffres sensibles revérifiés en session avant rédaction : R² test 0,077
  arrondi honnêtement à 0,08 ; F1 0,283/0,303/0,340/0,306 ; ICC 0,66 ;
  −19 % par point de taux ; R² hédonique 0,886 ; λ* = −23 015 € ; 25/28
  sigmoïdes ; KL Salon ≈ 3,0 bits ; 51,6 % de concentration vendeurs.

## memoire/figures/

**Résumé : 13 figures extraites des sorties PNG réellement enregistrées
dans les notebooks + 3 captures d'écran de la plateforme (Playwright).**

- Les figures ne sont pas régénérées pour le chapitre : elles sont
  extraites telles quelles des notebooks exécutés (traçabilité stricte
  nom de fichier → notebook/cellule, conservée dans l'historique de
  session).
- Problème : première capture de la plateforme prise pendant le
  chargement (« Running sql(...) ») → attente explicite de la fin des
  exécutions et de l'hydratation des tableaux avant capture.
- Problème : le modèle `risque_marge.joblib` (non versionné) avait disparu
  avec la réinitialisation de l'environnement → page « Vue d'ensemble »
  affichait 0 alerte au lieu de 10. Régénéré via le notebook 03 avant les
  captures définitives. Leçon : les artefacts non versionnés doivent être
  régénérables par une commande unique — c'était le cas, la doctrine a
  tenu.

## memoire/chapitre_copilote_financier.docx

**Résumé : généré par pandoc depuis le .Rmd ; 16 images intégrées, 17
titres conformes au sommaire.**

- L'environnement ne dispose pas de R : le rendu passe par pandoc
  directement (le .Rmd ne contient pas de chunk R, c'est du Markdown pur
  avec en-tête YAML), ce qui produit un .docx identique à ce qu'aurait
  donné `rmarkdown::render`.
- Avertissement pandoc bénin sur l'extension `.Rmd` (« defaulting to
  markdown ») : sans conséquence.

## Environnement

**Résumé : l'environnement Python du conteneur a été réinitialisé en cours
de session (pandas, streamlit, nbformat disparus) ; tout a été réinstallé
et les artefacts régénérés depuis les scripts du dépôt.**

- Confirmation en conditions réelles de l'exigence de reproductibilité du
  cadrage : `python src/base_sql.py` + `python src/nb_specs/nb03_marge.py`
  ont suffi à tout reconstruire.
