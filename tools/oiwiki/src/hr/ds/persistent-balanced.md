---
title: Perzistentno balansirano stablo
---

## Perzistentni treap bez rotacija

### Preduvjeti

**Perzistentno balansirano stablo koje se često koristi na informatičkim natjecanjima** obično je **perzistentni treap bez rotacija**, pa preporučujemo da prvo proučite [**treap bez rotacija**](./treap.md).

### Ideja i postupak

Treap bez rotacija možemo učiniti perzistentnim kopiranjem čvorova na putu tijekom operacija **Merge** i **Split** (obično kopiramo u operaciji **Split** kako ne bismo utjecali na prethodne verzije).

Kod treapa s rotacijama, osim čvorova na putu, treba kopirati i čvorove na koje utječu rotacije (ako je čvor već kopiran u trenutačnoj operaciji, ne treba ga ponovno kopirati). Jedna rotacija obično utječe samo na dva čvora, pa se vremenska složenost ne povećava.

Ta se metoda obično naziva kopiranjem puta (path copying).

„Sve podržane operacije mogu se izvesti pomoću **Merge Split Newnode Build**.” Operacija **Build** služi samo za izgradnju i ovdje je ne trebamo razmatrati, dok je **Newnode** (stvaranje novog čvora) alat za postizanje perzistentnosti.

Promotrimo **Merge** i **Split**: obje operacije idu odozgo prema dolje!

Zato ih možemo učiniti perzistentnima **po uzoru na perzistentni segment tree**.

### Uvođenje perzistentnosti

**Učiniti strukturu perzistentnom** znači **strukturi podataka** omogućiti čuvanje povijesnih podataka kako bismo poslije mogli pristupiti prethodnim verzijama.

U **perzistentnom segment treeju** pri stvaranju svake nove verzije kopiramo **put duž kojeg izvodimo izmjene**.

Za perzistentni treap (verziju koja se trenutačno često koristi na kineskim informatičkim natjecanjima) postupak je sljedeći:

Nakon što kopiranjem čvora $X_{a}$ (verzije $a$ čvora $X$) stvorimo novu verziju $X_{a+1}$ (verziju $a+1$ čvora $X$):

-   Ako podatke nekog djeteta $Y$ ne treba mijenjati, pokazivač čvora $X_{a+1}$ može izravno pokazivati na $Y_{a}$ (verziju $a$ čvora $Y$).
-   Inače, ako treba promijeniti $Y$, pri **rekurzivnom silasku** **stvaramo** novi čvor $Y_{a+1}$ (verziju $a+1$ čvora $Y$) za **pohranu novih podataka**, a pokazivač čvora $X_{a+1}$ usmjeravamo na $Y_{a+1}$ (verziju $a+1$ čvora $Y$).

### Perzistentna implementacija

Potrebno nam je:

-   Niz elemenata tipa `struct` za podatke **svakog čvora** (obično nazvan `tree`); naravno, oni koji pišu **implementaciju s pokazivačima** mogu izostaviti taj niz.

-   **Niz korijena** koji čuva *korijen stabla* za svaku verziju. Svaki upit nad verzijom počinje od **čvora pohranjenog u nizu korijena**.

-   `split()` za razdvajanje: **razdvaja jedno stablo na dva stabla**.

-   `merge()` za spajanje: **spaja dva stabla prema nasumičnim prioritetima**.

-   `newNode()` za stvaranje novog čvora.

-   `build()` za izgradnju stabla.

#### Split

Pri **razdvajanju** svaki put **stvaramo nove čvorove** koji pokazuju na razdvojene putove. Korijene dvaju dobivenih stabala pohranjujemo u `std::pair`.

`split(x,k)` vraća `std::pair`.

Prvih $k$ elemenata stabla s korijenom $_x$ stavlja u **jedno stablo**, a preostali čvorovi tvore drugo stablo. Vraća korijene tih dvaju stabala (first je korijen prvog, a second korijen drugog stabla).

-   Ako za **lijevo podstablo** čvora $x$ vrijedi $key \geq k$, **rekurzivno ulazimo izravno u lijevo podstablo**, pa drugo stablo dobiveno njegovim razdvajanjem spajamo s **desnim podstablom** trenutačnog čvora $x$.
-   Inače rekurzivno obrađujemo **desno podstablo**.

```cpp
static std::pair<int, int> _split(int _x, int k) {
  if (_x == 0)
    return std::make_pair(0, 0);
  else {
    int _vs = ++_cnt;  // Stvori novi čvor (ključna ideja perzistentnosti)
    _trp[_vs] = _trp[_x];
    std::pair<int, int> _y;
    if (_trp[_vs].key <= k) {
      _y = _split(_trp[_vs].leaf[1], k);
      _trp[_vs].leaf[1] = _y.first;
      _y.first = _vs;
    } else {
      _y = _split(_trp[_vs].leaf[0], k);
      _trp[_vs].leaf[0] = _y.second;
      _y.second = _vs;
    }
    _trp[_vs]._update();
    return _y;
  }
}
```

#### Merge

`merge(x,y)` vraća korijen spojenog stabla.

I ova je operacija rekurzivna. Ako je **nasumični prioritet čvora x** > **nasumični prioritet čvora y**, pozivamo `merge(x_{rc},y)`, a inače `merge(x,y_{lc})`.

```cpp
static int _merge(int _x, int _y) {
  if (_x == 0 || _y == 0)
    return _x ^ _y;
  else {
    if (_trp[_x].fix < _trp[_y].fix) {
      _trp[_x].leaf[1] = _merge(_trp[_x].leaf[1], _y);
      _trp[_x]._update();
      return _x;
    } else {
      _trp[_y].leaf[0] = _merge(_x, _trp[_y].leaf[0]);
      _trp[_y]._update();
      return _y;
    }
  }
}
```

## Perzistentni WBLT

### Preduvjeti

Perzistentni WBLT nastaje izmjenom WBLT-a, pa prvo proučite [WBLT](./wblt.md).

### Ideja i postupak

Koristimo **kopiranje puta**: kopiramo čvorove **izmijenjene** tijekom operacije, a prethodni čvorovi moraju ostati netaknuti.

### Obrada lijenih oznaka

Za obradu lijenih oznaka razmotrimo sljedeće: u perzistentnom WBLT-u čvor može imati više roditelja, ali samo $0$ ili $2$ djece. Operacija pushdown prosljeđuje lijene oznake i utječe samo na djecu. Izvođenje pushdowna nad čvorom samo po sebi nije problem; problem su njegova djeca, koja mogu imati i druge roditelje. Prosljeđivanje oznake djetetu može u verziju drugog roditelja dodati oznaku koja joj ne pripada, što je pogrešno, osim ako dijete ima samo jednog roditelja. Zato pri pushdownu trebamo kopirati djecu i oznake primijeniti na nove kopije.

### Implementacija kopiranja puta

Za kopiranje puta možemo definirati funkciju refresh koja prima referencu na čvor $p$, kopira čvor $p$ u novi čvor i ponovno dodjeljuje $p$. Pravilo je sljedeće: ako će se čvor mijenjati ili će se promijeniti koja su mu djeca (ne samo podaci u njegovoj djeci), pozovemo refresh; inače to nije potrebno.

Za upite koji ne mijenjaju podatke refresh nije potreban osim pri pushdownu. Ako osiguramo kopiranje puta u svim operacijama, redoslijed poziva pushdown i refresh nije važan.

### Mala optimizacija perzistentnog WBLT-a

Moguća je sljedeća optimizacija. Pushdown kopira dva čvora; jedna je mogućnost trajno zadržavanje oznaka. No, kao što smo rekli, djecu koja imaju samo jednog roditelja ne treba kopirati. To svojstvo možemo iskoristiti da smanjimo nepotrebno kopiranje čvorova.

Za svaki čvor bilježimo broj roditelja, označen s $use$ (smatramo da korijen svake verzije ima jednog roditelja). Pri svakom refreshu, ako je $use\leq 1$, ne treba kopirati čvor. Inače stvaramo novi čvor i smanjujemo $use$ za $1$, što predstavlja roditelja koji je prešao na kopiju tog djeteta. Roditelj zatim može slobodno mijenjati novi čvor bez utjecaja na druge verzije. Nadalje, pri kopiranju čvora s djecom povećavamo $use$ svakog djeteta za $1$; pri spajanju dvaju podstabala vraćeni čvor također se broji kao roditelj u vrijednosti $use$ svoje djece; pri brisanju čvora oba djeteta gube jednog roditelja. Time se mogu uštedjeti vrijeme i memorija.

### Implementacija

??? note "Potpuni kod (perzistentno balansirano stablo za nizove)"
    ```cpp
    --8<-- "docs/ds/code/persistent-balanced/persistent-wblt.cpp"
    ```

## Primjer zadatka

???+ note "[Luogu P3835 [Predložak] Perzistentno balansirano stablo](https://www.luogu.com.cn/problem/P3835)"
    Implementirajte strukturu podataka koja podržava sljedeće operacije (u početku je prazna):
    
    1.  Umetanje broja $x$.
    2.  Brisanje broja $x$ (ako postoji više jednakih brojeva, izbrišite samo jedan; ako ne postoji, zanemarite operaciju).
    3.  Upit za rang broja $x$ (rang je broj elemenata manjih od tog broja + 1).
    4.  Upit za broj ranga $x$.
    5.  Pronalaženje prethodnika broja $x$ (najvećeg broja manjeg od $x$; ako ne postoji, ispišite $-2\,147\,483\,647$).
    6.  Pronalaženje sljedbenika broja $x$ (najmanjeg broja većeg od $x$; ako ne postoji, ispišite $2\,147\,483\,647$).
    
    Sve operacije polaze od neke prethodne verzije i stvaraju novu verziju (operacije 3, 4, 5 i 6 ostavljaju izvorno stanje nepromijenjenim). Broj svake verzije jednak je rednom broju operacije. Početna verzija posebno ima broj 0.

To je perzistentna verzija zadatka **Obično balansirano stablo**, s jednakim vrstama operacija.

Razlika je samo u upotrebi perzistentnih operacija merge i split.

## Preporučeni zadaci za vježbu

1.  [Luogu P3919: Perzistentni niz (predložak)](https://www.luogu.com.cn/problem/P3919)

2.  [Codeforces 702F: T-shirt](http://codeforces.com/problemset/problem/702/F)

3.  [Luogu P5055: Perzistentno balansirano stablo za nizove](https://www.luogu.com.cn/problem/P5055)

4.  [Luogu P5350: Niz](https://www.luogu.com.cn/problem/P5350)
