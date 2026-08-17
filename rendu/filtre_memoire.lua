-- Filtre pandoc des chapitres du mémoire.
--
-- Deux blocs de division sont traités :
--   ::: sommaire     -> encadré « Sommaire » en ouverture de chapitre.
--                       En PDF, le sommaire est produit par minitoc : le
--                       contenu rédigé à la main est remplacé par \minitoc.
--                       Dans les autres formats (docx), il est conservé tel
--                       quel puisqu'il n'y a pas d'équivalent automatique.
--   ::: transition   -> page de clôture de chapitre : saut de page, pas de
--                       titre de section.

-- En sortie Word, pandoc ne sait pas décaler le compteur de chapitre : la
-- numérotation hiérarchique (2, 2.1, 2.1.1) est donc reconstruite ici à
-- partir de la métadonnée « chapoffset ». En sortie LaTeX, c'est la classe
-- report qui numérote, et ce bloc reste inactif.

local function raw_tex(s)
  return pandoc.RawBlock('latex', s)
end

local function numeroter_pour_word(doc)
  local decalage = 0
  if doc.meta.chapoffset then
    decalage = tonumber(pandoc.utils.stringify(doc.meta.chapoffset)) or 0
  end
  local compteurs = { 0, 0, 0, 0, 0 }

  return doc:walk({
    Header = function(el)
      if el.classes:includes('unnumbered') then return nil end
      compteurs[el.level] = compteurs[el.level] + 1
      for n = el.level + 1, #compteurs do compteurs[n] = 0 end
      local morceaux = {}
      for n = 1, el.level do
        local valeur = compteurs[n]
        if n == 1 then valeur = valeur + decalage end
        table.insert(morceaux, tostring(valeur))
      end
      local etiquette = table.concat(morceaux, '.')
      table.insert(el.content, 1, pandoc.Space())
      table.insert(el.content, 1, pandoc.Str(etiquette))
      return el
    end,
  })
end

function Pandoc(doc)
  if FORMAT:match('docx') then
    return numeroter_pour_word(doc)
  end
  return doc
end

function Div(el)
  if el.classes:includes('sommaire') then
    if FORMAT:match('latex') then
      return { raw_tex('\\minitoc\\vspace{1em}') }
    end
    return el
  end

  if el.classes:includes('transition') then
    if FORMAT:match('latex') then
      local blocs = { raw_tex('\\clearpage') }
      for _, b in ipairs(el.content) do table.insert(blocs, b) end
      return blocs
    end
    if FORMAT:match('docx') then
      local saut = pandoc.RawBlock('openxml',
        '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
      local blocs = { saut }
      for _, b in ipairs(el.content) do table.insert(blocs, b) end
      return blocs
    end
    return el
  end

  return el
end
