# Priručnik za natjecateljsko programiranje (hrvatski prijevod)

Hrvatski prijevod knjige *Competitive Programmer's Handbook* autora Anttija Laaksonena.

- Izvornik: `../cphb-master/cphb-master` (https://cses.fi/book/)
- Licencija izvornika i ovog prijevoda: Creative Commons BY-NC-SA 4.0
  (https://creativecommons.org/licenses/by-nc-sa/4.0/)
- LaTeX izvor prijevoda: `book.tex` (glavna datoteka), `preface.tex`, `chapter01.tex` … `chapter30.tex`,
  `list.tex` (popis literature, ostavljen u izvornom obliku jer sadrži bibliografske podatke).

Sav LaTeX markup, matematika i programski kod preslikani su iz izvornika; preveden je samo
tekst namijenjen čitanju.

## Prevođenje u PDF

```
pdflatex book.tex   # dva do tri prolaza zbog sadržaja i indeksa
```

Potrebni su TeX Live paketi `texlive-latex-extra`, `texlive-fonts-extra`, `texlive-pictures`,
`texlive-games` (šahovski simboli) i `texlive-lang-european` (hrvatski babel).

## Web izdanje

Direktorij `../website` sadrži statičku stranicu (Astro) generiranu iz ovih `.tex` datoteka.
