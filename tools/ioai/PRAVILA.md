# IOAI kurikulum – pravila za pisanje lekcija

Lekcije se pišu u `tools/ioai/content/<oblast>/<slug>.html` (slugovi su u `manifest.json`),
a `python3 tools/ioai/build.py` iz njih generira `IOAI/`. **Uzorna lekcija:**
`content/strojno-ucenje/01-linearna-regresija.html` – drži se njezina opsega, tona i strukture.

## Jezik i ton
* Sve na **hrvatskom** (ijekavica, hrvatski navodnici „…”, decimalni zarez u tekstu `0{,}2`, točka u kodu).
  Engleski stručni termin daj u zagradi pri prvom spominjanju: *gubitak (engl. loss)*. Nakon toga koristi
  hrvatski termin, a široko prihvaćene engleske riječi (overfitting, batch, dropout, embedding, fine-tuning)
  smiju ostati uz hrvatsko objašnjenje.
* Ton kao u Matematici: precizno, bez praznih fraza, obraćanje čitatelju u 2. osobi jednine („pokušaj”, „primijeti”).
* Ne izmišljaj činjenice o IOAI-ju (datumi, zadaci, rezultati). Zadaci „u stilu IOAI” moraju biti jasno označeni
  kao simulacije, ne kao službeni tekstovi natjecanja.
* Ne stavljaj datume ni verzije biblioteka u tekst osim ako su bitni.

## Struktura datoteke (blokovi `@@ ime`)
```
@@ meta        naslov = …, podnaslov = …, oznake = pojam1, pojam2, … (5–7 oznaka, smiju imati $…$)
@@ ciljevi     3–4 <li> („U ovoj lekciji”)
@@ teorija     pojmovi, formule, intuicija; <h3> podnaslovi; kratice <definicija>, <teorem>, <dokaz>, <napomena>
@@ primjeri    3 riješena primjera <primjer> … <rjesenje> … s kodom KORAK PO KORAK (<b>Korak 1: …</b>)
@@ zadaci      8–9 zadataka <zadatak tezina="0..4">: 3 zagrijavanja (0), zatim 1,1,2,2,3,(3); svaki s <rjesenje>,
               teži s <naputak>; rješenja sadrže kod kad je zadatak računalni
@@ sazetak     <ul> s 4–6 <li>
@@ literatura  2–4 <li> (knjige, službena dokumentacija, tečajevi) – samo stvarni, provjereni izvori
```
Kratice i pravila generatora: vidi docstring u `tools/matematika/build.py` (kratice se ne smiju gnijezditi;
`<zadatak>` sadrži `<naputak>` pa `<rjesenje>`). Opseg lekcije: 12–20 KB teksta.

## Matematika
* MathJax: `$…$` i `$$…$$`. **Unutar formule nikad `<` ni `>`** – koristi `\lt`, `\gt`, `\le`, `\ge`
  (generator inače prekida s greškom). Nema praznog retka unutar formule.
* Vektori i matrice: $w\in\mathbb R^d$, $X\in\mathbb R^{n\times d}$, transponiranje $X^\top$.

## Kod
* Sav kod je **Python 3** u `<kod jezik="python">…</kod>` (sirovi tekst, bez HTML escapeanja: `<`, `&` pišu se
  normalno). Ispis programa ide odmah iza bloka u `<izlaz>…</izlaz>`.
* **Svaki blok mora biti pokrenut**: `python3 tools/ioai/provjeri_kod.py content/<oblast>/<slug>.html`
  izvršava blokove lekcije redom u istom procesu (kao ćelije bilježnice – varijable iz primjera smiju se
  koristiti u zadacima, pazi na nazive) i uspoređuje ispis s `<izlaz>`. Tijek rada: napiši kod s praznim
  `<izlaz>\n</izlaz>`, pokreni `--upisi` da se ispisi popune, pročitaj ih i uskladi tekst s brojevima.
* Blok koji se ne može pokrenuti (`pip install`, pseudokod, kod koji zahtijeva GPU ili velik download)
  označi `<kod jezik="python" pokreni="ne">`; nedeterministički ispis označi `<izlaz provjera="ne">`.
  Takvih blokova neka bude što manje – natjecatelj mora moći sve pokrenuti na CPU-u u par minuta.
* Determinizam: `np.random.default_rng(0)`, `torch.manual_seed(0)`, `random_state=…`. Ispis zaokružuj
  (`round`, `%.3f`) da ne ovisi o zadnjoj decimali.
* Podaci: samo skupovi ugrađeni u biblioteke bez downloada (`sklearn.datasets.load_*`, `make_*`) ili sintetički
  podaci generirani u kodu. Ako je nužan download (torchvision MNIST, Hugging Face modeli), kod neka bude
  cjelovit, ali označen `pokreni="ne"` uz tekstualno objašnjenje očekivanog ispisa.
* Slike: Matplotlib s `matplotlib.use("Agg")`, spremanje u datoteku (`fig.savefig("ime.png")`); slike se
  ne commitaju – opiši riječima što se na njima vidi.
* Biblioteke: numpy, pandas, matplotlib, scikit-learn, torch (CPU: `pip3 install torch --index-url
  https://download.pytorch.org/whl/cpu`), torchvision, po potrebi transformers. Ne koristi TensorFlow/Keras.
* Stil koda: imena varijabli i komentari na hrvatskom gdje je prirodno, kratki redovi (≤ 100 znakova),
  bez `input()`, bez beskonačnih petlji, trajanje bloka ≤ 1 min na CPU-u.

## Provjera prije commita
```
python3 tools/ioai/provjeri_kod.py tools/ioai/content/<oblast>/<slug>.html   # sav kod radi i ispisi odgovaraju
python3 tools/ioai/build.py                                                 # generator prolazi bez greške
```
Commitaj **samo** `tools/ioai/content/**` (generirani `IOAI/` ne, taj se generira centralno).
