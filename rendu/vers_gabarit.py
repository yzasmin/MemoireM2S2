#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verse le contenu R Markdown du mémoire dans le gabarit LaTeX officiel.

Le gabarit (dossier gabarit/latex) est celui fourni par les enseignants et
utilisé pour le mémoire de mi-parcours : son préambule, sa page de titre et
sa mise en page ne sont pas modifiés. Seuls les fichiers de contenu du
dossier chapters/ sont régénérés à partir des sources memoire/*.Rmd.
"""
import io, os, re, shutil, subprocess, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(RACINE, 'memoire')
DST = os.path.join(RACINE, 'gabarit', 'latex')
CHAP = os.path.join(DST, 'chapters')
FIGS = os.path.join(DST, 'figures')


def pandoc(markdown, chapitre=True):
    """Convertit un fragment markdown en LaTeX."""
    cmd = ['pandoc', '--from', 'markdown', '--to', 'latex', '--wrap=preserve']
    if chapitre:
        cmd += ['--top-level-division=chapter']
    r = subprocess.run(cmd, input=markdown, capture_output=True, text=True)
    if r.returncode:
        sys.exit('pandoc : ' + r.stderr)
    return r.stdout


def nettoyer(tex):
    """Adapte la sortie pandoc aux conventions du gabarit."""
    # Les figures cherchent leur place au fil du texte : en placement fixe,
    # dix-neuf figures laisseraient autant de demi-pages blanches.
    tex = tex.replace(r'\begin{figure}', r'\begin{figure}[!htbp]')
    # graphicspath se charge du dossier : on ne garde que le nom de fichier.
    tex = re.sub(r'\\includegraphics(\[[^\]]*\])?\{figures/([^}]+)\}',
                 lambda m: r'\includegraphics%s{%s}' % (m.group(1) or '', m.group(2)), tex)
    # Largeurs : pandoc écrit \pandocbounded, absent du gabarit.
    tex = re.sub(r'\\pandocbounded\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', r'\1', tex)
    # pandoc ajoute height=\textheight : sans keepaspectratio, la figure est
    # étirée sur toute la hauteur de la page. On ne garde que la largeur.
    tex = tex.replace(r',height=\textheight', '')
    # Les macros que pandoc suppose définies par son propre gabarit.
    tex = tex.replace(r'\tightlist', '')
    return tex


def decouper(chemin):
    """Renvoie (titre, corps) d'un fichier .Rmd, sommaire retiré."""
    s = io.open(chemin, encoding='utf-8').read()
    m = re.match(r'#\s+(.+?)\n', s)
    titre = m.group(1).strip() if m else ''
    # « # Introduction {-} » : l'attribut de non-numérotation n'est pas du titre.
    titre = re.sub(r'\s*\{[.#-][^}]*\}\s*$', '', titre).strip()
    corps = s[m.end():] if m else s
    corps = re.sub(r'::: sommaire\n.*?\n:::\n', '', corps, flags=re.S)
    corps = re.sub(r'```\{=latex\}\n.*?\n```\n', '', corps, flags=re.S)
    return titre, corps.strip()


def ecrire(nom, contenu):
    io.open(os.path.join(CHAP, nom), 'w', encoding='utf-8').write(contenu)
    print('  chapters/%s' % nom)


def chapitre(nom, source, numerote=True):
    titre, corps = decouper(os.path.join(SRC, source))
    tete = '%% !TEX root = manuscript.tex\n\n'
    if numerote:
        tete += '\\chapter{%s}\n\\minitoc\n\\newpage\n\n' % titre
    else:
        tete += '\\chapter*{%s}\n\n' % titre
    ecrire(nom, tete + nettoyer(pandoc(corps, chapitre=True)))


def preambule():
    """Remerciements + résumé d'une part, glossaire de l'autre."""
    s = io.open(os.path.join(SRC, '00_preambule.Rmd'), encoding='utf-8').read()
    s = re.sub(r'```\{=latex\}\n.*?\n```\n', '', s, flags=re.S)
    parts = re.split(r'^# (.+?) \{-\}$', s, flags=re.M)[1:]
    sections = dict(zip(parts[0::2], parts[1::2]))

    abstract = ('%% !TEX root = manuscript.tex\n\n\\section*{Remerciements}\n'
                + nettoyer(pandoc(sections['Remerciements'].strip(), chapitre=False))
                + '\n\\clearpage\n\\section*{Résumé}\n'
                + nettoyer(pandoc(sections['Résumé'].strip(), chapitre=False)))
    ecrire('abstract.tex', abstract)

    # Le glossaire du gabarit est un tabular, pas un tableau pandoc.
    lignes = []
    for l in sections['Glossaire'].strip().split('\n'):
        l = l.strip()
        if not l.startswith('|') or set(l) <= set('|:- '):
            continue
        cells = [c.strip() for c in l.strip('|').split('|')]
        if len(cells) != 2 or cells[0] == 'Terme':
            continue
        terme, defi = (nettoyer(pandoc(c, chapitre=False)).strip() for c in cells)
        terme = re.sub(r'^\\.*?\{|\}$', '', terme) if terme.startswith('\\') else terme
        lignes.append('\\textbf{%s} & %s \\\\' % (terme, defi))
    glossaire = ('%% !TEX root = manuscript.tex\n\\section*{Glossaire}\n\\vspace{1em}\n'
                 '\\begin{longtable}{p{4cm} p{11cm}}\n'
                 '\\textbf{Terme} & \\textbf{Définition} \\\\\n\\hline\n\\endhead\n'
                 + '\n'.join(lignes) + '\n\\end{longtable}\n')
    ecrire('glossaire.tex', glossaire)


def figures():
    os.makedirs(FIGS, exist_ok=True)
    for f in os.listdir(FIGS):
        if f.startswith('fig_') or f.endswith(('.png', '.jpg')):
            os.remove(os.path.join(FIGS, f))
    n = 0
    for f in sorted(os.listdir(os.path.join(RACINE, 'figures'))):
        if f.endswith('.png'):
            shutil.copy2(os.path.join(RACINE, 'figures', f), os.path.join(FIGS, f))
            n += 1
    print('  figures/ : %d fichiers' % n)


if __name__ == '__main__':
    print('Contenu versé dans le gabarit officiel :')
    preambule()
    chapitre('introduction.tex', '01_introduction.Rmd', numerote=False)
    chapitre('chapter_1.tex', '02_reprise_donnees.Rmd')
    chapitre('chapter_2.tex', '03_reporting_si.Rmd')
    chapitre('chapter_3.tex', '04_copilote_financier.Rmd')
    chapitre('chapter_4.tex', '05_reflexion_projet.Rmd')
    chapitre('conclusion.tex', '06_conclusion.Rmd', numerote=False)
    figures()

    # Le PDF final se compile depuis gabarit/, comme sur Overleaf : le dossier
    # du fichier principal est ajouté au chemin de recherche.
    print('\nCompilation :')
    env = dict(os.environ, TEXINPUTS='.//:./latex//:')
    for _ in range(3):
        subprocess.run(['pdflatex', '-interaction=nonstopmode', 'latex/manuscript.tex'],
                       cwd=os.path.join(RACINE, 'gabarit'), env=env,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.copy2(os.path.join(RACINE, 'gabarit', 'manuscript.pdf'),
                 os.path.join(RACINE, 'memoire_M2_saoud.pdf'))
    print('  gabarit/manuscript.pdf -> memoire_M2_saoud.pdf')
