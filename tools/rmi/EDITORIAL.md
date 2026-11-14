# RMI: prijevod zadatka i analiza rješenja (format `@@ editorial`)

Cilj: za svaki zadatak RMI-a dvije stranice — `prijevodi/rmi/<godina>/<slug>.html` (potpun prijevod teksta
zadatka) i `<slug>-editorial.html` (**potpuna, jasna analiza rješenja podzadatak po podzadatak**).
RMI **nema pisani editorial**: analiza se piše prema službenim rješenjima iz paketa zadatka
(`solutions/*.cpp`, `scoring.txt`) i prema AC predajama natjecatelja na QOJ-u. Sve što tvrdiš mora biti
**točno i provjereno** (kod pokrenut na službenim testovima iz paketa).

Format sadržaja i komponente su **isti kao za JOISC** — pročitaj `tools/joisc/EDITORIAL.md` (komponente
`<info>`, `<dodatak>`, `<skica>`, `<okviri>`, klase SVG-a, provjera granica teksta, MathJax, sažetak).
Razlike za RMI su dolje.

## Datoteka `tools/rmi/content/<godina>/<slug>.html`

```
@@ meta
naslov = Hrvatski naslov
engleski = English title
oznake = 3–6 kratkih oznaka (tehnike), odvojenih zarezom
izvori = kratak popis izvora analize, npr. službeno rješenje (squirrel-official.cpp), AC predaje korisnika X, Y

@@ zadatak
(potpun prijevod službenog engleskog teksta: priča, formalni zadatak, implementacija/potpisi funkcija,
ograničenja, tablica podzadataka, primjeri s objašnjenjima; slike iz PDF-a precrtane kao <skica>)

@@ editorial
(analiza)
```

Generiranje: `python3 tools/rmi/build.py <godina>` (ruši se s porukom ako je nešto krivo — namjerno).

## Pravila za `@@ zadatak`

1. Prevodi se **sve** iz službenog PDF-a (engleska verzija; ako je nema, rumunjska), istim redoslijedom,
   uključujući potpise funkcija (`<pre><code>`), napomene o grader-u i sve primjere (ulaz/izlaz u `<pre>`,
   objašnjenja prevedena). Tablica podzadataka kao HTML `<table>` (#, bodovi, ograničenja).
2. Slike u tekstu (stablo iz primjera, matrica …) precrtavaju se kao `<skica>` s prevedenim oznakama.
3. Matematika u MathJaxu; imena funkcija i varijabli iz koda ostaju u `<code>`.

## Pravila za `@@ editorial`

1. **Struktura:** „Pregled zadatka” (što se traži, ključno zapažanje bez rješenja), zatim `<h2>` po
   podzadatku (ili grupi podzadataka koji dijele ideju) **redom iz `scoring.txt`**, s
   `<span class="bodovi">N</span>`. Svaki podzadatak dobiva: ideju, zašto radi (tvrdnja + dokaz u
   `<div class="tvrdnja">` / `<p class="dokaz">`), složenost, i po potrebi kratki pseudokod ili isječak C++-a.
   Puno rješenje je zadnje; ne preskače se na njega.
2. **Ne prepričavaj kod** — objašnjavaj ideju; kod daj samo za ključne dijelove (do ~40 redaka po isječku),
   HTML-escapean, s hrvatskim komentarima.
3. **Istina iznad svega.** Svaku tvrdnju o složenosti i točnosti provjeri: službeno rješenje i barem jedan
   AC kod s QOJ-a pokreni na službenim testovima (`tests.zip`, grader iz paketa). Ako AC kodovi koriste
   drugačiji pristup od službenog, opiši **oba** (službeni prvo, zatim `<h3>Drugi pristup: …</h3>`). Ako
   nešto ne možeš dokazati, ne piši ga kao činjenicu — napiši u izvještaju.
4. `<dodatak>` se **ne koristi** (cijela analiza je autorska). `<info naslov="…">` samo za veće pozadinske
   pojmove (HLD, centroid, FFT/NTT, Dinic, …). Skice (`<skica>`) za primjere i konstrukcije; animacija
   koraka algoritma na konkretnom primjeru → `<okviri vrsta="koraci">`.
5. Na kraju `<div class="rezime"><h2>Sažetak</h2><ul>…</ul></div>` (3–5 točaka) i
   `<h2>Izvori</h2>` s popisom: službena rješenja iz paketa (imena datoteka) i AC predaje (QOJ korisnik, ID predaje).

## Terminologija (HR)

subtask → podzadatak; constraints → ograničenja; interactive → interaktivni zadatak; grader → grader (ocjenjivač);
query → upit; expected value → očekivanje; connected component → komponenta povezanosti; tree → stablo;
path → put; suffix automaton → sufiksni automat; suffix array → sufiksno polje; convolution → konvolucija;
binary search → binarno pretraživanje; prefix sums → prefiksne sume; greedy → pohlepni algoritam;
DP → dinamičko programiranje; bitmask → bitmaska; modular inverse → modularni inverz; mod 998244353 → ostaci modulo 998244353.

## Provjera prije predaje

- `python3 tools/rmi/build.py <godina>` prolazi bez greške.
- Vizualna provjera (desktop 1280 px i mobitel 390 px): nema vodoravnog klizanja, (i) kartice i skice rade,
  MathJax bez grešaka. Lokalno: `python3 -m http.server 8765` u korijenu repozitorija →
  `http://localhost:8765/prijevodi/rmi/<godina>/<slug>-editorial.html`.
- Committa se **samo** `tools/rmi/content/<godina>/<slug>.html` (generirane stranice se rade centralno).
