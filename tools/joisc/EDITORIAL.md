# JOISC: potpuni prijevod editoriala (format `@@ editorial`)

Cilj: stranica `prijevodi/joisc/<godina>/<slug>-editorial.html` je **potpun, vjeran prijevod
službene japanske prezentacije rješenja** (`*-review.pdf`) na hrvatski — tekst *i* skice —
podzadatak po podzadatak, bez preskakanja na puno rješenje. Primjer: `content/2026/festival.html`.

## Datoteka sadržaja `tools/joisc/content/<godina>/<slug>.html`

```
@@ meta
naslov = Hrvatski naslov
engleski = English title
oznake = 3–6 kratkih oznaka odvojenih zarezom (tehnike), npr. stablo, HLD, segmentno stablo
autor_analize = Ime autora prezentacije (s naslovnog slajda; japanska imena u Hepburn latinici)

@@ zadatak
(postojeći prevedeni tekst zadatka — ne dirati)

@@ editorial
(cijeli prijevod)
```

Blokovi `rjesenje`, `trener` i `analiza` se brišu: zadatak s blokom `editorial` nema trenerski
mod, a tab „Rješenje (editorial) →“ vodi na članak. Generiranje: `python3 tools/joisc/build.py <godina>`
(ruši se s porukom ako je nešto krivo — to je namjerno).

## Pravila prijevoda

1. **Sve sa slajda, istim redoslijedom.** Svaka rečenica, formula, lema, napomena, tablica i
   komentar sa svakog slajda prevodi se. Ništa se ne sažima i ne „prepričava”. Naslovni slajd
   → jedna rečenica (autor, dan). Slajdovi s raspodjelom bodova (得点分布) → kratka tablica/lista.
2. **Struktura:** `<h2>` po podzadatku (ili grupi podzadataka kako ih slajdovi grupiraju) s
   `<span class="bodovi">N</span>` (zbroj bodova te grupe) i `<span class="slajd-ref">slajdovi a–b</span>`;
   `<h3>` za podnaslove slajdova. Uvodni dio „Pregled zadatka” prije prvog podzadatka.
3. **Matematika** u MathJaxu: `$...$` u retku, `\[...\]` za istaknute formule. Oznake iz
   slajdova se zadržavaju ($x^\top_v$, $\mathrm{kth}$ …), ne izmišljaju se nove.
4. **Tvrdnje i dokazi:** `<div class="tvrdnja"><p><strong>Lema 1.</strong> …</p></div>`,
   dokaz `<p class="dokaz"><em>(Dokaz.)</em> …</p>`.
5. **`<dodatak>`** (sivi okvir „Dopuna (nije u izvorniku)”): sve čega u izvorniku *nema* — ispunjeni
   „dokaz izostavljen”, prešućeni rubni slučaj, formula koju slajd samo spominje. Dopuna mora biti
   **točna i sam je izvedi**; ako nisi siguran, napiši to u izvještaju umjesto da nagađaš.
   Opcionalno `<dodatak naslov="…">`. Sadržaj prijevoda se **nikad** ne stavlja u dodatak.
6. **`<info naslov="…">…</info>`** = gumb (i) s karticom. Samo za *veće* pozadinske pojmove
   (HLD, centroid dekompozicija, Li Chao, FFT, …), ne za jednu rečenicu — nju napiši u tekstu.
   Unutra samo `<p>`, `<b>`, `<i>`, `<code>`, `<br>`, matematika; **bez** `<ul>/<ol>/<div>`.
   Kartica se piše unutar `<p>` odmah iza pojma: `… <b>HLD</b><info naslov="HLD">…</info> …`.
7. **Skice:** svaki crtež sa slajda precrtava se kao inline SVG s **prevedenim oznakama**
   (ne slike slajdova). Jedan crtež → `<skica sirina="420px">SVG<natpis>…</natpis></skica>`.
   Crtež koji se **mijenja kroz više uzastopnih slajdova** (animacija koraka) →
   `<okviri naslov="…" vrsta="koraci"><okvir>SVG<natpis>…</natpis></okvir>…</okviri>` — jedan okvir po
   slajdu, natpis = prijevod teksta tog slajda. Koristi zajedničke klase: `cvor`, `cvor-istaknut`,
   `cvor-plavi`, `cvor-zeleni`, `cvor-sivi`, `brid`, `brid-tezak`, `brid-lak`, `brid-istaknut`,
   `oznaka-cvora`, `oznaka-brida`, `tekst`, `tekst-mali`, `tekst-naglasen`.
   **Tekst mora stati u `viewBox`**: build to provjerava procjenom širine (0,6 em po znaku) i ruši se;
   kraći natpisi, više `<text>` redaka ili širi viewBox. Svaki `<svg>` ima `viewBox` i `role="img"`.
8. **Kod na slajdovima** (i kad je slika) prepisuje se u `<pre><code>…</code></pre>` (HTML-escape `<`, `>`, `&`),
   komentari prevedeni, kod nepromijenjen.
9. **Tekst koji je na slajdu slika** (nema ga u ekstrahiranom tekstu) čita se s renderiranog slajda
   (`pymupdf`: `page.get_pixmap(dpi=150)`) i prevodi jednako.
10. Na kraju `<div class="rezime"><h2>Sažetak</h2><ul>…</ul></div>` (3–5 točaka).

## Terminologija (HR)

点火 → paljenje; 頂点/辺 → vrh/brid; 根付き木 → ukorijenjeno stablo; 部分木 → podstablo;
小課題 → podzadatak; 満点 → puni bodovi; 愚直 → izravno (naivno) rješenje; 計算量 → složenost;
セグメント木 → segmentno stablo; 遅延評価 → lijena propagacija; 二分探索 → binarno pretraživanje;
累積和 → prefiksne sume; 貪欲 → pohlepni algoritam; 動的計画法/DP → dinamičko programiranje (DP);
重軽分解 → heavy-light dekompozicija (HLD); 重心分解 → centroid dekompozicija; 全方位木DP → re-rooting DP;
多重集合 → multiskup; 単調 → monoton; 補題 → lema; 系 → korolar; 考察 → zapažanje; 証明略 → (dokaz izostavljen → napiši ga u `<dodatak>`);
クエリ → upit; 更新 → ažuriranje; 区間 → interval; 一点更新 → ažuriranje u točki; 想定解 → službeno (očekivano) rješenje;
bitset → bitset; 平方分割 → sqrt-dekompozicija; 期待値 → očekivanje; mod 998244353 → ostaci modulo 998244353.

## Provjera prije predaje

- `python3 tools/joisc/build.py <godina>` prolazi bez greške.
- Usporedba slajd-po-slajd: za svaki slajd postoji odgovarajući tekst (ništa izostavljeno, ništa dodano bez `<dodatak>`).
- Vizualna provjera u pregledniku (desktop 1280 px i mobitel 390 px): nema vodoravnog klizanja, skice i (i) kartice se otvaraju,
  tekst u SVG-u unutar okvira. Lokalno: `python3 -m http.server 8765` u korijenu repozitorija.
- Committa se **samo** `tools/joisc/content/<godina>/<slug>.html`; generirane stranice u `prijevodi/` ne (generiraju se centralno).
