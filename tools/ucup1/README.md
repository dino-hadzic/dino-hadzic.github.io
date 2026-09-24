# Prijevodi 1st Universal Cup – alati

Stranice u `prijevodi/ucup/1st/stageN/` generiraju se iz `content/stageN.py`; ništa se u njima ne uređuje ručno.

```
python3 gen.py 19            # (re)generira stage19/*.html + stage19/index.html i ispisuje upozorenja
python3 inject_stats.py      # osvježi kartice na prijevodi/ucup/1st/index.html iz content/stage_stats.json
python3 stress/stress.py stage19/A -n 300 --big 3   # lokalna provjera rješenja
```

## Polja zadatka (`content/stageN.py`)

| polje | sadržaj |
|---|---|
| `statement` | prijevod teksta zadatka (HTML, MathJax `$…$`) |
| `hints` | 2–3 naputka, svaki u vlastitom spoileru |
| `coach` | trenerski način: popis `(pitanje, odgovor)`; pitanje mora završavati s `?` – retoričko pitanje koje vodi do ideje, odgovor objašnjava *zašto* ta ideja slijedi |
| `tips` | opći savjeti/prečaci (2–4 stavke, `<li>` sadržaj) koji vrijede i izvan ovog zadatka |
| `solution` | sažeto rješenje (prijevod službenog ili izvedeno iz AC predaja) |
| `detailed` | detaljno rješenje: svaki korak objašnjen, dokazi tvrdnji, rubni slučajevi, složenost; prikazuje se samo uz prekidač „Detaljno rješenje” |
| `verified` | kratak opis lokalne provjere koda (ispis `stress.py` je dobar predložak) |
| `code` | (neobvezno) put do koda; zadano `solutions/stageN/<slovo>/sol.cpp` |

Polja stagea: `no_editorial` (organizatori nisu objavili editorial), `community` (rješenja izvedena iz prihvaćenih predaja – na stranici se ispisuje napomena da nisu službena).

## Kod rješenja (`solutions/stageN/<slovo>/`)

* `sol.cpp` – rješenje koje se prikazuje (C++17, čitljivo, komentari na hrvatskom)
* `brute.cpp` ili `brute.py` – očito točan spori algoritam za male ulaze
* `gen.py <seed> small|big` – generator slučajnog testa
* `check.py <ulaz> <očekivano|-> <dobiveno>` – samo za zadatke s više točnih odgovora
* `samples/K.in`, `samples/K.out` – službeni primjeri

`gen.py` odbija generirati stranicu s poljem `detailed` ako nema `sol.cpp`, `verified` ili `tips`, ili ako neko pitanje trenerskog načina ne završava s `?`.

## QOJ (`qoj/`)

`qoj/login.py` i `qoj/fetch_ac.py` čitaju prihvaćene predaje s qoj.ac preko već prijavljenog Chromea (CDP). Račun je isključivo za čitanje: ništa se ne predaje. Preuzeti kod ne ide u repozitorij.
