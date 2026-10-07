---
title: Binarno pretraživanje
---

Ova stranica kratko predstavlja binarno pretraživanje, binarno pretraživanje po odgovoru te ternarno pretraživanje, izvedeno iz metode polovljenja.

## Binarno pretraživanje

Binarno pretraživanje (binary search), poznato i kao pretraživanje polovljenjem intervala (half-interval search) ili logaritamsko pretraživanje (logarithmic search), algoritam je za pronalaženje elementa u sortiranom nizu.

### Postupak

Uzmimo kao primjer traženje broja u uzlazno sortiranom nizu.

U svakom koraku pristupamo srednjem elementu trenutnog dijela niza. Ako je srednji element upravo traženi, pretraživanje završava; ako je srednji element manji od tražene vrijednosti, svi elementi lijevo od njega nisu veći od srednjeg, pa traženi element ne može biti među njima i dovoljno je tražiti desno; ako je srednji element veći od tražene vrijednosti, analogno je dovoljno tražiti lijevo.

Konkretno, neka indeksi niza $a$ počinju od $1$, neka je duljina niza $n$ i tražimo položaj broja $x$. Neka $l,r$ označavaju da trenutno promatramo samo elemente niza s indeksom $i$ za koji vrijedi $l\le i\le r$. Na početku postavimo $l\gets1$, $r\gets n$. U svakom koraku pristupamo srednjem elementu $a_{\textit{mid}}$, gdje je $\textit{mid}=\left\lfloor\dfrac{l+r}{2}\right\rfloor$, i razlikujemo slučajeve:

-   Ako je $a_{\textit{mid}}<x$, budući da je niz uzlazan, svi brojevi s indeksom manjim ili jednakim $\textit{mid}$ sigurno su manji od $x$, pa ih ne treba pretraživati; dovoljno je pretraživati brojeve s indeksom većim od $\textit{mid}$, tj. postavimo $l\gets \textit{mid}+1$, a $r$ ostaje.
-   Ako je $a_{\textit{mid}}>x$, budući da je niz uzlazan, svi brojevi s indeksom većim ili jednakim $\textit{mid}$ sigurno su veći od $x$, pa ih ne treba pretraživati; dovoljno je pretraživati brojeve s indeksom manjim od $\textit{mid}$, tj. $l$ ostaje, a $r\gets \textit{mid}-1$.
-   Ako je $a_{\textit{mid}}=x$, pronašli smo položaj broja $x$ i algoritam završava.

Ako položaj broja $x$ nismo pronašli ni kad je promatrani raspon postao prazan, tj. $l>r$, onda $x$ nije u nizu $a$.

### Svojstva

#### Vremenska složenost

Najbolja vremenska složenost binarnog pretraživanja je $O(1)$.

Prosječna i najgora vremenska složenost binarnog pretraživanja su $O(\log n)$. Budući da algoritam u svakom koraku prepolovi interval koji pretražuje, za niz duljine $n$ obavit će najviše $O(\log n)$ usporedbi s traženim elementom.

#### Prostorna složenost

Prostorna složenost iterativne inačice binarnog pretraživanja je $O(1)$.

Prostorna složenost rekurzivne inačice (bez eliminacije repnih poziva) je $O(\log n)$.

### Implementacija

```cpp
int binary_search(int x, int l = 1, int r = n) {  // traži indeks broja x u uzlaznom nizu
  int ret = -1;                                   // ako nije pronađen, vraća -1
  while (l <= r) {
    int mid = (l + r) >> 1;  // l + r može prekoračiti raspon, vidi napomenu ispod
    if (a[mid] < x)
      l = mid + 1;
    else if (a[mid] > x)
      r = mid - 1;
    else {  // jednakost provjeravamo zadnju jer je u većini koraka element ili veći ili manji
      ret = mid;
      break;
    }
  }
  return ret;
}
```

???+ note "Napomena"
    -   Prema [optimizacijama pri prevođenju – pomak umjesto množenja](../lang/optimizations.md#移位代替乘法), ako je $s$ predznačeni broj i možete jamčiti $s\ge 0$, `s >> 1` troši manje instrukcija nego `s / 2`.
    
    -   Kad su $l$ ili $r$ vrlo veliki, $l+r$ može prekoračiti raspon tipa. Ako $r-l$ pritom ne prekoračuje raspon, `(l + r) >> 1` u kodu možete zamijeniti s `l + ((r - l) >> 1)`.

???+ warning "Upozorenje"
    Kad je $s$ negativan neparan broj, rezultati `s >> 1` i `s / 2` razlikuju se za $1$ i nisu jednaki. Razlog je što prvi zaokružuje prema minus beskonačnosti (standardizirano u C++20, prije toga ovisno o implementaciji), a drugi prema nuli. Vidi [C++ operatori nad bitovima](../lang/op.md#位操作符). Zato, ako $l + r$ može biti negativan, `(l + r) / 2` može dati $r$, što u inačici s `r = mid` dovodi do **beskonačne petlje**. Npr. za $l = -1,~r = 0$ vrijednost `(l + r) / 2` jednaka je $0$. Na tu razliku treba paziti pri implementaciji.

### bsearch

Funkcija `bsearch` binarno je pretraživanje iz standardne biblioteke jezika C, definirano u `<stdlib.h>`. U standardnoj biblioteci C++-a ta je funkcija definirana u `<cstdlib>`. `qsort` i `bsearch` jedine su dvije algoritamske funkcije u standardnoj biblioteci jezika C.

U odnosu na četiri parametra funkcije `qsort` ([STL funkcije za sortiranje](./stl-sort.md)), `bsearch` na krajnjoj lijevoj strani dodaje parametar „adresa traženog elementa”. Element se predaje preko adrese kako bi se mogla izravno upotrijebiti ista funkcija usporedbe kao za `qsort`, čime se odmah nakon sortiranja može pretraživati. Zato se tom parametru ne može izravno predati konkretna vrijednost: traženu vrijednost treba najprije spremiti u varijablu, a zatim predati adresu te varijable.

Funkcija `bsearch` tako ima ukupno pet parametara: adresu traženog elementa, adresu početka niza, broj elemenata, veličinu elementa i pravilo usporedbe. Pravilo usporedbe i dalje se zadaje funkcijom usporedbe; vidi [STL funkcije za sortiranje](./stl-sort.md).

Povratna vrijednost funkcije `bsearch` adresa je pronađenog elementa, tipa `void *`.

Napomena: `bsearch` se od `std::lower_bound` i `std::upper_bound`, koje opisujemo u nastavku, razlikuje u dvjema stvarima:

-   kad više elemenata zadovoljava uvjet, nije određeno koji se od njih vraća;
-   kad odgovarajući element nije pronađen, vraća `NULL`.

Pomoću `lower_bound` može se ostvariti gotovo ista funkcionalnost kao s `bsearch` (dovoljno je posebno obraditi slučaj kad element nije pronađen da bi bila potpuno jednaka), pa se zadaci rješivi s `bsearch` mogu izravno prepisati s `lower_bound`.

## Binarno pretraživanje po odgovoru

Binarno pretraživanje po odgovoru algoritam je koji iskorištava poopćenu uređenost odgovora na problem (obično zvanu monotonost) i, postupkom sličnim binarnom pretraživanju, brzo pronalazi odgovor.

Ako nije drukčije naglašeno, binarno pretraživanje po odgovoru obično se odnosi na cjelobrojne odgovore, tj. unaprijed znamo da je odgovor cijeli broj.

Problemi na koje se može primijeniti binarno pretraživanje po odgovoru obično su oblika „nađi najveću (najmanju) vrijednost koja zadovoljava uvjet $P$” i imaju sljedeća svojstva:

1.  za proizvoljan broj $x$ lako je provjeriti zadovoljava li $x$ uvjet;
2.  za odgovor se mogu odrediti grube donja i gornja granica, tj. mogu se odrediti $L$ i $R$ takvi da, ako odgovor $x$ postoji, nužno vrijedi $L\le x \le R$;
3.  raspon tih grubih granica je velik, pa bi provjera svih kandidata redom premašila vremensko ograničenje;
4.  uvjet $P$ ima poopćenu uređenost.

Pretpostavimo da postoji funkcija $f(x)$ takva da je $f(x)=1$ ako i samo ako $x$ zadovoljava uvjet $P$, a inače $f(x)=0$. Poopćenu uređenost uvjeta $P$ možemo definirati na sljedeći način:

-   Ako za sve $L\le i<j \le R$ vrijedi $f(i)\le f(j)$, tj. $f(x)$ je neopadajuća. Zapišemo li $f(i)$ za $i=L,\dots,R$ kao 01-niz, on ima oblik `00...011...1`. Tada binarnim pretraživanjem po odgovoru možemo naći **najmanju** vrijednost koja zadovoljava uvjet $P$.

-   Ako za sve $L \le i<j \le R$ vrijedi $f(i)\ge f(j)$, tj. $f(x)$ je nerastuća. Odgovarajući 01-niz ima oblik `11...100...0`. Tada binarnim pretraživanjem po odgovoru možemo naći **najveću** vrijednost koja zadovoljava uvjet $P$.

Drugim riječima, prva vrsta uređenosti znači: ako znamo da $x$ zadovoljava uvjet $P$, onda ga sigurno zadovoljavaju i svi brojevi veći od $x$. Binarno pretraživanje po odgovoru pronalazi $x$ koji odgovara opisu „svi brojevi manji od njega ne zadovoljavaju uvjet $P$, a on i svi veći od njega zadovoljavaju uvjet $P$”.

Druga vrsta uređenosti znači: ako znamo da $x$ zadovoljava uvjet $P$, onda ga sigurno zadovoljavaju i svi brojevi manji od $x$. Binarno pretraživanje po odgovoru pronalazi $x$ koji odgovara opisu „on i svi brojevi manji od njega zadovoljavaju uvjet $P$, a svi veći od njega ne zadovoljavaju uvjet $P$”.

### Postupak

Uzmimo kao primjer traženje najmanje vrijednosti binarnim pretraživanjem po odgovoru (algoritam tada zahtijeva da problem ima prvu gore opisanu vrstu uređenosti). Neka su grube donja i gornja granica odgovora $L$ i $R$.

Neka $l,r$ označavaju da trenutno sa sigurnošću znamo da odgovor $x$ zadovoljava $l \le x \le r$. Slično binarnom pretraživanju, na početku postavimo $l\gets L$, $r\gets R$. U svakom koraku provjeravamo zadovoljava li $\textit{mid}=\left\lfloor\dfrac{l+r}{2}\right\rfloor$ uvjet $P$ i razlikujemo slučajeve:

-   Ako $\textit{mid}$ ne zadovoljava uvjet (tj. $f(\textit{mid})$ je $0$), po uređenosti problema ni jedan broj manji ili jednak $\textit{mid}$ ne zadovoljava uvjet i ne treba ih razmatrati, pa postavimo $l\gets \textit{mid}+1$, a $r$ ostaje.
-   Ako $\textit{mid}$ zadovoljava uvjet (tj. $f(\textit{mid})$ je $1$), po uređenosti problema svi brojevi veći ili jednaki $\textit{mid}$ zadovoljavaju uvjet; no budući da tražimo najmanju vrijednost, brojeve veće od $\textit{mid}$ ne treba razmatrati i dovoljno je promatrati brojeve manje ili jednake $\textit{mid}$. Tada postavimo $r \gets \textit{mid}$, a $l$ ostaje.

Kad raspon odgovora zadovolji $l=r$ (tj. više ne vrijedi $l<r$), algoritam završava. Tada je $l$ odnosno $r$ odgovor.

Napomena: ako unutar granica odgovor ne postoji (tzv. slučaj bez rješenja), svaki upit $f(\textit{mid})$ vraća $0$, pa po završetku algoritma vrijedi $l=r=R$ i $f(l)=0$. Zato, ako treba prepoznati slučaj bez rješenja, dovoljno je dodatno provjeriti je li $f(l)$ jednako $0$.

Slično binarnom pretraživanju, algoritam u svakom koraku prepolovi interval koji pretražuje, pa je vremenska složenost $O(M \log (R-L+1))$, gdje je $M$ vremenska složenost jedne provjere zadovoljava li $\textit{mid}$ uvjet $P$.

### Implementacija

Prema gornjem opisu algoritma možemo dati sljedeću implementaciju:

```cpp
// traži najmanji cijeli broj x u [L, R] koji zadovoljava uvjet P, uz L <= R
// uvjet P mora imati prvu vrstu uređenosti, tj. f(x) je neopadajuća
// u implementaciji je obično check(x) = f(x)
// ako u intervalu nema rješenja, vraća -1
int binary_search_min(int L, int R) {
  if (L > R) return -1;
  int l = L, r = R;
  while (l < r) {
    int mid = (l + r) >> 1;
    if (check(mid))  // f(mid) = 1, uvjet P je zadovoljen
      r = mid;       // odgovor je u [l, mid]
    else
      l = mid + 1;  // odgovor je u [mid + 1, r]
  }
  // sada je l == r
  if (!check(l)) return -1;  // provjera postoji li rješenje
  return l;
}
```

Kad `-1` označava nepostojanje rješenja, treba osigurati da se ne može zamijeniti s valjanim odgovorom.

### Detalji implementacije

U rješenjima zadataka možemo naići i na drugu inačicu implementacije:

```cpp
// traži najmanji cijeli broj x u [L, R] koji zadovoljava check(x)
// check mora biti neopadajuća na [L, R]
// ako je interval prazan ili u njemu nema rješenja, vraća -1
int binary_search_min(int L, int R) {
  if (L > R) return -1;
  int l = L, r = R;
  while (l <= r) {
    int mid = (l + r) >> 1;
    if (check(mid))
      r = mid - 1;
    else
      l = mid + 1;
  }

  if (l > R) return -1;
  return l;
}
```

Obje inačice daju isti odgovor, ali održavaju različite invarijante petlje.

??? note "Zašto obje inačice pronalaze najmanju dopustivu vrijednost?"
    Pretpostavimo najprije da je $[L,R]$ neprazan i da u njemu postoji odgovor; najmanji broj koji zadovoljava uvjet $P$ označimo $\textit{ans}$. Budući da je $f$ neopadajuća, u izvornom intervalu $[L,R]$ vrijedi
    
    $$
    f(x)=0\quad (x<\textit{ans}),\qquad
    f(x)=1\quad (x\ge \textit{ans}).
    $$
    
    **Inačica s `l < r` čuva odgovor unutar zatvorenog intervala.**
    
    Invarijanta koju održava jest
    
    $$
    l\le \textit{ans}\le r.
    $$
    
    U svakom koraku uzimamo $\textit{mid}=\left\lfloor\dfrac{l+r}{2}\right\rfloor$. Ako je $f(\textit{mid})=1$, onda je $\textit{ans}\le\textit{mid}$ i postavljamo $r\gets\textit{mid}$; ako je $f(\textit{mid})=0$, onda je $\textit{ans}>\textit{mid}$ i postavljamo $l\gets\textit{mid}+1$. Obje izmjene čuvaju invarijantu.
    
    Dok je $l<r$, vrijedi $l\le\textit{mid}<r$, pa svaka iteracija strogo smanjuje interval. Po završetku petlje $l=r$, a iz invarijante slijedi $\textit{ans}=l$.
    
    **Inačica s `l <= r` isključuje već odlučeni dio; odgovor se može nalaziti neposredno iza desne granice.**
    
    Invarijanta koju održava jest: u izvornom intervalu $[L,R]$ svi $x<l$ zadovoljavaju $f(x)=0$, a svi $x>r$ zadovoljavaju $f(x)=1$. Uz pretpostavku da odgovor postoji, to znači
    
    $$
    l\le \textit{ans}\le r+1.
    $$
    
    Ako je $f(\textit{mid})=1$, svi $x\ge\textit{mid}$ u izvornom intervalu zadovoljavaju $f(x)=1$, pa možemo postaviti $r\gets\textit{mid}-1$; ako je $f(\textit{mid})=0$, svi $x\le\textit{mid}$ u izvornom intervalu zadovoljavaju $f(x)=0$, pa možemo postaviti $l\gets\textit{mid}+1$.
    
    Svaka iteracija iz intervala koji još treba pretražiti isključuje barem jedan cijeli broj, pa petlja na kraju završava.
    
    Dok se petlja izvršava, vrijedi $l\le\textit{mid}\le r$. Ako izvršimo $r\gets\textit{mid}-1$, nova desna granica zadovoljava $r\ge l-1$; ako izvršimo $l\gets\textit{mid}+1$, nova lijeva granica zadovoljava $l\le r+1$. Dakle, koju god izmjenu primijenili, nakon nje vrijedi $l\le r+1$. Petlja završava kad je $l>r$, a uz cjelobrojnost granica slijedi da tada nužno vrijedi $l=r+1$. Iz invarijante o položaju odgovora $l\le\textit{ans}\le r+1$ dobivamo $\textit{ans}=l$.
    
    Ovdje treba uočiti: interval $[l,r]$ koji još treba pretražiti ne mora uvijek sadržavati odgovor. Npr. ako u nekom koraku upravo dobijemo $\textit{mid}=\textit{ans}$, nakon $r\gets\textit{mid}-1$ vrijedi $\textit{ans}=r+1$. Odgovor tada više nije u $[l,r]$, ali i dalje zadovoljava invarijantu $l\le\textit{ans}\le r+1$, pa to ne utječe na gornji dokaz ispravnosti.
    
    **Kad rješenja nema, dvije inačice završavaju na različitim položajima.**
    
    Za inačicu s `l <= r`: ako po završetku petlje vrijedi $l\le R$, budući da lijeva granica uvijek zadovoljava $l\ge L$, $l$ je u izvornom intervalu. Iz $l=r+1$ i invarijante „svi $x>r$ u izvornom intervalu zadovoljavaju $f(x)=1$” slijedi $f(l)=1$, pa `check(l)` ne treba ponovno pozivati.
    
    Ako rješenja nema, na kraju je $l=R+1$, što je već izvan izvornog intervala pretraživanja. Budući da `check` zahtijevamo samo na $[L,R]$, najprije treba provjeriti `l > R`, a ne izravno pozvati `check(l)` da bismo utvrdili postoji li rješenje.
    
    Za inačicu s `l < r`, prisjetimo li se ranijeg opisa, ako u intervalu nema rješenja na kraju je $l=r=R$. Tada treba dodatno provjeriti je li `check(l)` jednako $0$ da bismo razlikovali je li odgovor $R$ ili rješenja nema.
    
    Ukratko, uz $L\le R$ i $f$ neopadajuću na $[L,R]$, obje inačice završavaju nakon konačno mnogo iteracija. Ako u intervalu postoji dopustiva vrijednost, obje na kraju daju $l=\textit{ans}$ i vraćaju najmanji cijeli broj u intervalu koji zadovoljava uvjet; ako rješenja nema, inačica s `l < r` to utvrđuje provjerom `check(l)` nakon petlje, a inačica s `l <= r` provjerom `l > R` nakon petlje, i obje vraćaju dogovorenu oznaku za nepostojanje rješenja. Za prazan interval $L>R$ oba koda vraćaju oznaku za nepostojanje rješenja prije ulaska u petlju. Dakle, iako dvije implementacije održavaju različite invarijante petlje i završavaju na različitim položajima, obje ispravno obavljaju traženi upit za najmanju dopustivu vrijednost i daju isti rezultat.

Ove dvije inačice pokazuju da ispravnost implementacije binarnog pretraživanja ovisi o usklađenosti značenja granica, invarijante petlje, uvjeta petlje i pravila izmjene. Samo iz toga jesu li krajevi intervala uključeni ili koristi li petlja `l < r` ili `l <= r` ne može se zaključiti je li neka inačica ispravna.

Da bismo dokazali ispravnost neke inačice, treba potvrditi:

1.  inicijalizacija zadovoljava invarijantu petlje;
2.  svaka izmjena čuva invarijantu i strogo smanjuje broj cijelih brojeva u intervalu koji još treba pretražiti, čime jamči završetak petlje;
3.  po završetku petlje iz invarijante i uvjeta zaustavljanja može se utvrditi da je povratna vrijednost upravo odgovor; ako je dopušteno nepostojanje rješenja, treba objasniti i kako se ono prepoznaje.

Pri raspravi o načinima implementacije treba posebno razlikovati „interval koji još treba pretražiti” od „intervala koji jamčeno sadrži konačan odgovor”: zbog različitih rubnih uvjeta oni nisu nužno jednaki i ne može se jednoobrazno zahtijevati da odgovor uvijek bude u intervalu koji još treba pretražiti.

U nastavku je nekoliko uobičajenih inačica. Za sve pretpostavljamo $L\le R$, da problem ima prvu vrstu uređenosti i da najmanja dopustiva vrijednost $\textit{ans}$ postoji. Položaj odgovora određen je stupcem „invarijanta o položaju odgovora”.

| Inačica                                                   | Početni $l,r$     | Uvjet petlje | $\textit{mid}$                            | Kad $f(\textit{mid})=1$ | Kad $f(\textit{mid})=0$ | Invarijanta o položaju odgovora | Na kraju | Vraća |
| --------------------------------------------------------- | ----------------- | ------------ | ----------------------------------------- | ----------------------- | ----------------------- | ------------------------------- | -------- | ----- |
| Zatvoreni interval $[l,r]$, isključuje odlučeni dio       | $l=L,\ r=R$       | $l\le r$     | $\left\lfloor\dfrac{l+r}{2}\right\rfloor$ | $r\gets\textit{mid}-1$  | $l\gets\textit{mid}+1$  | $l\le\textit{ans}\le r+1$       | $l=r+1$  | $l$   |
| Zatvoreni interval $[l,r]$, čuva odgovor                  | $l=L,\ r=R$       | $l<r$        | $\left\lfloor\dfrac{l+r}{2}\right\rfloor$ | $r\gets\textit{mid}$    | $l\gets\textit{mid}+1$  | $l\le\textit{ans}\le r$         | $l=r$    | $l$   |
| Poluotvoreni interval $[l,r)$, isključuje odlučeni dio    | $l=L,\ r=R+1$     | $l<r$        | $\left\lfloor\dfrac{l+r}{2}\right\rfloor$ | $r\gets\textit{mid}$    | $l\gets\textit{mid}+1$  | $l\le\textit{ans}\le r$         | $l=r$    | $l$   |
| Poluotvoreni interval $(l,r]$, čuva odgovor               | $l=L-1,\ r=R$     | $l+1<r$      | $\left\lfloor\dfrac{l+r}{2}\right\rfloor$ | $r\gets\textit{mid}$    | $l\gets\textit{mid}$    | $l<\textit{ans}\le r$           | $l+1=r$  | $r$   |
| Otvoreni interval $(l,r)$, održava obje granice           | $l=L-1,\ r=R+1$   | $l+1<r$      | $\left\lfloor\dfrac{l+r}{2}\right\rfloor$ | $r\gets\textit{mid}$    | $l\gets\textit{mid}$    | $l<\textit{ans}\le r$           | $l+1=r$  | $r$   |

Uz tablicu treba napomenuti još nekoliko stvari:

-   U 3. retku $[l, r)$ je interval koji još treba pretražiti, ali odgovor može biti upravo $r$.
-   4. redak čuva odgovor u $(l, r]$ i oslanja se na to da početna desna granica $R$ zadovoljava $f(R) = 1$. Dok se petlja izvršava vrijedi $r - l \ge 2$, pa je u 4. i 5. retku ispravno i zaokruživanje sredine prema gore.
-   U 5. retku $(l, r)$ označava položaje između dviju granica koje još treba provjeriti. Početni $L - 1$ možemo smatrati virtualnim graničnikom s vrijednošću 0, a $R + 1$ virtualnim graničnikom s vrijednošću 1. Petlja funkciju provjere poziva samo unutar izvornog intervala, pa vrijednosti u graničnicima nije potrebno zaista računati.
-   Ako treba obraditi slučaj bez rješenja: u 1., 3. i 5. retku to se prepoznaje po tome je li povratna vrijednost $R + 1$; u 2. retku treba provjeriti $f(l)$; u 4. retku treba najprije provjeriti $f(R)$.

### Minimizacija maksimuma i maksimizacija minimuma

Problemi minimizacije maksimuma i maksimizacije minimuma tipični su problemi na koje se može primijeniti binarno pretraživanje po odgovoru.

Uzmimo kao primjer minimizaciju maksimuma. Obično svakom rješenju odgovara skup $S$ koji treba razmotriti. Ako među svim rješenjima treba minimizirati maksimum brojeva u pripadnom skupu $S$, problem se može preoblikovati u: nađi najmanji $k$ za koji postoji rješenje sa $\max(S) \le k$.

Taj problem ima poopćenu uređenost: ako postoji rješenje sa $\max(S) \le k$, onda za $i\ge k$ to rješenje zadovoljava i $\max(S)\le i$. Dakle za $i \ge k$ postoji rješenje sa $\max(S) \le i$, što također ispunjava uvjet zadatka. Stoga se problem može riješiti binarnim pretraživanjem po odgovoru. Maksimizacija minimuma rješava se analogno.

### Binarno pretraživanje po odgovoru u STL-u

#### std::lower\_bound i std::upper\_bound

Standardna biblioteka C++-a implementira:

-   funkciju [`std::lower_bound`](https://en.cppreference.com/w/cpp/algorithm/lower_bound) koja pronalazi prvi element koji nije manji od zadane vrijednosti;
-   funkciju [`std::upper_bound`](https://en.cppreference.com/w/cpp/algorithm/upper_bound) koja pronalazi prvi element veći od zadane vrijednosti.

Obje su implementirane binarnim pretraživanjem, pa prije poziva elementi moraju biti sortirani (sortiranost se ovdje odnosi na funkciju usporedbe iz nastavka, ne nužno na matematičku uređenost) kako bi njihov problem imao poopćenu uređenost (tj. za `std::lower_bound`, ako $a_i$ nije manji od zadane vrijednosti, ni brojevi nakon $i$ nisu manji od zadane vrijednosti; za `std::upper_bound`, ako je $a_i$ veći od zadane vrijednosti, i brojevi nakon $i$ veći su od zadane vrijednosti).

`std::lower_bound` i `std::upper_bound` imaju po četiri parametra:

-   `first`: početni [iterator](../lang/csl/iterator.md) niza, pokazuje na prvi element niza;
-   `last`: završni iterator niza, pokazuje na **mjesto iza** posljednjeg elementa niza. Drugim riječima, ako je `last` dvosmjerni iterator, `--last` pokazuje na posljednji element niza;
-   `value`: zadana vrijednost;
-   `comp` (neobavezno): funkcija usporedbe, piše se kao za funkciju `sort`. Treba paziti da je `std::lower_bound` poziva u obliku `comp(element, value)`, a `std::upper_bound` u obliku `comp(value, element)`.

Obje vraćaju iterator na element koji zadovoljava uvjet, istog tipa kao predani iteratori. Dakle, ako predamo pokazivače na niz, vraća se pokazivač na odgovarajući element niza. Ako element koji zadovoljava uvjet ne postoji, vraća se `last`.

Obje su definirane u zaglavlju `<algorithm>`.

???+ note "Primjeri upotrebe"
    -   U nizu $a$ duljine $n$ s indeksima od $1$, na položajima od $l$ do $r$, pronaći prvi broj koji nije manji od $x$ i dobiti njegov indeks: `lower_bound(a+l,a+r+1,x)-a`.
    -   U nizu $a$ duljine $n$ s indeksima od $0$ pronaći prvi broj veći od $x$ (mora postojati) i dobiti njegovu vrijednost: `*upper_bound(a,a+n,x)`.
    -   U vectoru $a$ duljine $n$ pronaći prvi broj koji nije manji od $x$ i dobiti njegov indeks (indeksi vectora počinju od $0$): `lower_bound(a.begin(),a.end(),x)-a.begin()`.

???+ note "O iteratorima"
    Gornji početni i završni iterator moraju biti ForwardIterator. Pokazivači na niz te iteratori vectora, seta, mape i stringa zadovoljavaju taj zahtjev.

??? note "O vremenskoj složenosti algoritma"
    U implementaciji standardne biblioteke libstdc++ koju koristi GCC obje funkcije srednjem elementu pristupaju pomoću `std::advance`. To znači da je složenost funkcije $O(\log n)$ samo kad iterator podržava slučajni pristup (npr. predani su pokazivači na niz ili iteratori vectora). Ako slučajni pristup nije podržan (npr. set ili map), složenost funkcije jednaka je zbroju vremena pristupa srednjem elementu u svakom koraku (obično linearno). Npr. operacija poput `lower_bound(st.begin(),st.end(),val)` na setu ili mapi ima vremensku složenost $O(n)$. Tada treba koristiti člansku funkciju `st.lower_bound(val)`.

??? note "Implementacija `std::lower_bound` i `std::upper_bound` pomoću `bsearch`"
    Budući da `bsearch` vraća NULL kad element nije pronađen (vidi [bsearch](./binary.md#bsearch)), npr. pri traženju broja 3 u nizu 1, 2, 4, 5, 6, ostvariti funkcionalnost `lower_bound` pomoću `bsearch` postaje teško.
    
    Pri implementaciji `std::lower_bound` i `std::upper_bound` pomoću `bsearch` možemo iskoristiti dogovor o parametrima funkcije usporedbe: prvi parametar pokazuje na traženi element, a drugi na element niza u kojem tražimo. Dakle, dovoljno je da funkcija usporedbe može doći do adrese početka niza.
    
    ```cpp
    int A[100005];  // primjer globalnog niza
    
    // compare uspoređuje vrijednosti na koje pokazuju dva int pokazivača: *p1 > *p2 vraća pozitivan broj, jednakost
    // 0, manje vraća negativan broj
    int compare(const void*, const void*);
    
    // traži adresu prvog elementa koji nije manji od traženog elementa
    int lower(const void* p1, const void* p2) {
      int* a = (int*)p1;
      int* b = (int*)p2;
      if ((b == A || compare(a, b - 1) > 0) && compare(a, b) > 0)
        return 1;
      else if (b != A && compare(a, b - 1) <= 0)
        return -1;  // koristi oduzimanje adresa, pa tip elementa mora biti naveden
      else
        return 0;
    }
    
    // traži adresu prvog elementa većeg od traženog elementa
    int upper(const void* p1, const void* p2) {
      int* a = (int*)p1;
      int* b = (int*)p2;
      if ((b == A || compare(a, b - 1) >= 0) && compare(a, b) >= 0)
        return 1;
      else if (b != A && compare(a, b - 1) < 0)
        return -1;  // koristi oduzimanje adresa, pa tip elementa mora biti naveden
      else
        return 0;
    }
    ```
    
    Napomena: ako je odgovor položaj iza kraja (npr. traženi element veći je od svih elemenata), gornja metoda i dalje vraća `NULL`, što treba posebno obraditi.
    
    Budući da današnji OI natjecatelji rijetko pišu čisti C, a ova metoda ima ograničenu primjenu, ona nije u središtu pozornosti. Početnicima se preporučuje izravno koristiti funkcije `std::lower_bound` i `std::upper_bound` iz C++-a.

#### std::partition\_point

C++11 uvodi [`std::partition_point`](https://en.cppreference.com/w/cpp/algorithm/partition_point). Služi za brzo pronalaženje „točke particije” u već particioniranom nizu binarnim pretraživanjem po odgovoru.

`std::partition_point` ima tri parametra:

-   `first`, `last`: kao gore;
-   `p`: unarni [predikat](../lang/csl/container.md#关联式容器). To je pozivni objekt koji prima jedan argument $v$ i vraća logičku vrijednost koja kaže zadovoljava li $v$ uvjet particije.

Neka je predani niz $a$; funkcija vraća iterator na prvi element koji ne zadovoljava uvjet particije, tj. iterator na element s najmanjim indeksom $x$ za koji je $p(a_x)$ jednako `false`.

Niz mora biti particioniran, tj. mora imati drugu gore opisanu vrstu poopćene uređenosti. Drugim riječima, zapišemo li rezultate $p(v)$ za svaki element $v$ niza kao 01-niz, on ima oblik `11...100...0`, a funkcija vraća iterator na položaj prve $0$.

??? note "Odnos `std::partition_point` prema `std::lower_bound` i `std::upper_bound`"
    Zapravo su `std::lower_bound` i `std::upper_bound` posebni oblici funkcije `std::partition_point`.
    
    Definirajmo funkciju `f` kodom: `bool f(int v) { return !(val <= v); }`. Predamo li `f` kao predikat funkciji `std::partition_point`, dobivamo isti rezultat kao `std::lower_bound`. Analogno za `std::upper_bound`.

### Binarno pretraživanje po realnom odgovoru

Binarno pretraživanje po realnom odgovoru, poznato i kao binarno pretraživanje s pomičnim zarezom, inačica je binarnog pretraživanja po odgovoru u kojoj je odgovor realan broj.

Za razliku od cjelobrojnog slučaja, kod realnog odgovora obično se ne traži točan odgovor, nego realna aproksimacija koja zadovoljava zadanu preciznost.

#### Postupak

Uzmimo kao primjer traženje najmanje vrijednosti. Neka su grube donja i gornja granica odgovora $L$ i $R$. Neka $l,r$ označavaju da trenutno sa sigurnošću znamo da odgovor $x$ zadovoljava $l\le x\le r$. Na početku postavimo $l\gets L$, $r\gets R$. U svakom koraku uzimamo $\textit{mid}=\dfrac{l+r}{2}$ (pazite, ovdje je riječ o realnom računanju) i provjeravamo zadovoljava li $\textit{mid}$ uvjet $P$:

-   Ako $\textit{mid}$ zadovoljava uvjet, slično cjelobrojnom slučaju postavimo $r\gets \textit{mid}$, a $l$ ostaje.
-   Ako $\textit{mid}$ ne zadovoljava uvjet, slično cjelobrojnom slučaju postavimo $l\gets \textit{mid}$, a $r$ ostaje.

Treba uočiti da se, za razliku od cjelobrojnog slučaja, kod realnog odgovora interval ne može sužavati pomoću `mid + 1` ili `mid - 1`, jer u skupu realnih brojeva ne postoje susjedni elementi; granicu možemo samo postaviti na $\textit{mid}$ i osloniti se na to da se duljina intervala stalno prepolavlja i približava odgovoru.

Algoritam završava kad duljina intervala $r-l$ ne premašuje zadanu preciznost $\textit{eps}$ ili kad dosegne unaprijed zadani broj iteracija. Tada se $l$, $r$ ili $\dfrac{l+r}{2}$ mogu uzeti kao aproksimacija odgovora (ako se zahtijeva da konačna povratna vrijednost zadovoljava uvjet $P$, treba vratiti $r$). Za traženje najveće vrijednosti dovoljno je obrnuti smjerove u gornja dva slučaja: ako $\textit{mid}$ zadovoljava uvjet, postavimo $l\gets \textit{mid}$; inače $r\gets \textit{mid}$ (odgovarajuće, ako se zahtijeva da konačna povratna vrijednost zadovoljava uvjet $P$, treba vratiti $l$).

Koristi li se `while (r - l > eps)`, vremenska složenost binarnog pretraživanja po realnom odgovoru je $O(M \log((R-L)/\textit{eps}))$. Koristi li se fiksan broj iteracija $k$, vremenska složenost je $O(Mk)$. Ovdje je $M$ vremenska složenost jedne provjere zadovoljava li $\textit{mid}$ uvjet $P$. Zbog pogrešaka u računanju s pomičnim zarezom u praksi se obično ne provjerava izravno $l=r$, nego $r-l<\textit{eps}$, ili se petlja izvršava fiksan broj puta, npr. $60$ do $100$, kako bi se izbjegla beskonačna petlja i zajamčila preciznost.

#### Implementacija

```cpp
double binary_search_iter(double L, double R) {  // implementacija s fiksnim brojem iteracija
  double l = L, r = R;
  for (int i = 0; i < 100; ++i) {
    double mid = (l + r) / 2;
    if (check(mid))
      r = mid;
    else
      l = mid;
  }
  return r;
}

const double eps = 1e-7;  // tražena preciznost, obično 1/100 preciznosti iz zadatka ili manje

double binary_search_eps(double L, double R) {  // implementacija s eps
  double l = L, r = R;
  while (r - l > eps) {
    double mid = (l + r) / 2;
    if (check(mid))
      r = mid;
    else
      l = mid;
  }
  return r;
}
```

???+ warning "Upozorenje"
    `eps` ne smije biti prevelik, inače preciznost nije dovoljna; ne smije biti ni premalen, inače se zbog pogrešaka pomičnog zareza možda ne može dosegnuti i petlja postaje beskonačna. Ako je raspon odgovora vrlo velik ili je tražena preciznost vrlo visoka, preporučuje se fiksan broj iteracija umjesto `while (r - l > eps)`.

### Primjer zadatka

???+ note "[Luogu P1873 Sječa drveća](https://www.luogu.com.cn/problem/P1873)"
    Drvosječa Mirko treba nasjeći $M$ metara drva. To je za Mirka lak posao jer ima prekrasan novi stroj za sječu koji može oboriti šumu poput požara. No Mirku je dopušteno sjeći samo jedan red stabala.
    
    Mirkov stroj radi ovako: Mirko zada visinu $H$ (u metrima), stroj podigne golemu pilu na visinu $H$ i odreže sve dijelove stabala viših od $H$ (dijelovi stabala koji nisu viši od $H$ metara ostaju netaknuti). Mirko dobiva odrezane dijelove stabala.
    
    Npr. ako su visine stabala u redu $20,~15,~10,~17$ i Mirko podigne pilu na visinu $15$ metara, nakon rezanja preostale visine stabala bit će $15,~15,~10,~15$, a Mirko će od prvog stabla dobiti $5$ metara drva, a od četvrtog $2$ metra, ukupno $7$ metara drva.
    
    Mirko jako brine o zaštiti okoliša, pa ne želi posjeći previše drva. Upravo zato pilu postavlja što je više moguće. Vaš je zadatak pomoći Mirku da pronađe najveću cjelobrojnu visinu pile $H$ pri kojoj dobiva barem $M$ metara drva. Drugim riječima, podigne li pilu još $1$ metar, neće dobiti $M$ metara drva.

??? note "Ideja rješenja"
    Mogli bismo isprobati sve odgovore od $0$ do $10^9$, ali takav naivan pristup sigurno ne bi dobio sve bodove jer isprobavanje od $0$ do $10^9$ traje predugo. Umjesto toga možemo binarno pretraživati odgovor na intervalu $[0,~10^9]$ i provjeravati izvedivost svakog kandidata (obično greedy pristupom). **To je binarno pretraživanje po odgovoru.**

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/basic/code/binary/binary_2.cpp"
    ```
    
    Nakon čitanja gornjeg koda sigurno imate dva pitanja:
    
    1.  Zašto je interval pretraživanja poluotvoren (zatvoren slijeva, otvoren zdesna)?
    
        Jer na kraju pretraživanja izgleda ovako (na primjeru najveće dopustive vrijednosti):
    
        ![](./images/binary-final-1.svg)
    
        a zatim
    
        ![](./images/binary-final-2.svg)
    
        Za najmanju dopustivu vrijednost je upravo obrnuto.
    2.  Zašto se vraća lijeva vrijednost?
    
        Kao gore. Po završetku petlje vrijedi $l+1=r$, `check(l)` je istinito, a `check(r)` lažno, pa je $l$ najveća dopustiva vrijednost.

## Ternarno pretraživanje

### Uvod

Metoda polovljenja može se koristiti za približno nalaženje nultočke funkcije. Ako treba pronaći točku ekstrema unimodalne funkcije, obično se koristi ternarno pretraživanje (ternary search).

U ovom odjeljku koristimo sljedeći strogi dogovor o unimodalnosti: za funkciju $f(x)$ definiranu na $[l,r]$, ako postoji $x^*\in[l,r]$ takav da je $f(x)$ strogo rastuća na $[l,x^*]$ i strogo padajuća na $[x^*,r]$, kažemo da je $f(x)$ unimodalna funkcija (unimodal function). Oba intervala sadrže $x^*$, pa je $x^*$ jedinstvena točka maksimuma, a $f(x^*)$ maksimum.

??? note "Zašto točku ekstrema ne tražimo kao nultočku derivacije?"
    Prvo, unimodalnost ne jamči da je nultočka derivacije jedinstvena, a točka u kojoj je derivacija nula ne mora biti točka maksimuma. Npr.
    
    $$
    f(x)=\begin{cases}
      (x-1)^3+1,&0\le x<2,\\
      (3-x)^3+1,&2\le x\le 4.
    \end{cases}
    $$
    
    Nultočke $f'(x)$ su $x=1$ i $x=3$, a maksimum $f(x)$ postiže se u $x=2$, gdje funkcija nije derivabilna.
    
    Drugo, za neke funkcije postupak i rezultat deriviranja prilično su složeni, a funkcija se možda ni ne može zapisati u obliku $y=f(x)$.
    
    Treće, u nekim zadacima unimodalna funkcija čiji ekstrem tražimo nije jedna zasebna funkcija, nego funkcija dobivena posebnim operacijama nad više funkcija (npr. maksimum minimuma više linearnih funkcija koje nemaju potpuno jednaku monotonost). Tada derivacija može biti funkcija po dijelovima, a u nekim točkama funkcija možda nije derivabilna.

???+ warning "Napomena"
    Ternarnim pretraživanjem može se naći i maksimum unimodalne funkcije i minimum „unidolne” funkcije. Radi jednostavnosti, osim ako nije drukčije rečeno, u nastavku kao primjer uzimamo traženje maksimuma unimodalne funkcije.

### Postupak

Osnovna ideja ternarnog pretraživanja slična je metodi polovljenja, ali u svakom koraku unutar trenutnog intervala $[l,r]$ (između dviju narančastih točaka na slici) biramo dvije točke $\textit{lmid} < \textit{rmid}$ (dvije plave točke na slici). Kao na slici, ako je $f(\textit{lmid})<f(\textit{rmid})$, funkcija je na $[l,\textit{lmid})$ (crveni dio na slici) nužno rastuća, točka maksimuma (zelena točka na slici) sigurno nije u tom intervalu, pa ga možemo odbaciti; no ne možemo isključiti mogućnost da je točka maksimuma desno od $\textit{rmid}$, pa ne možemo odbaciti ništa više. I obrnuto.

![](images/ternary.svg)

Ispravnost ternarnog pretraživanja ne ovisi o konkretnom izboru $\textit{lmid}$ i $\textit{rmid}$; dovoljno je da to budu dvije različite točke unutar intervala, a obično se uzimaju dvije trećinske točke. No njihov izbor utječe na učinkovitost. U svakom se koraku odbacuje jedan od dvaju rubnih intervala, pa se mogu uzeti i dvije točke blizu sredine kako bi odbačeni interval bio veći. Uzmemo li $\textit{mid}\pm\delta$, gdje je $\delta>0$ dovoljno malen, usporedba vrijednosti funkcije odgovara određivanju predznaka približne derivacije $\dfrac{f(\textit{mid}+\delta)-f(\textit{mid}-\delta)}{2\delta}$. Budući da funkcije na algoritamskim natjecanjima obično imaju dobru glatkoću, na temelju toga možemo grubo odrediti s koje je strane $\textit{mid}$ točka ekstrema i tako postići učinkovitost blisku metodi polovljenja.

### Implementacija

Pseudokod:

$$
\begin{array}{l}
\textbf{Algorithm}\operatorname{TernarySearch}(f,l,r):\\
\textbf{Input. } \text{A unimodal function } f(x) \text{ and its domain } [l,r].  \\
\textbf{Output. } \text{The maximizer }x^*\text{, up to an error of }\varepsilon\text{, and its value } f(x^*). \\
\textbf{Method. } \\
\begin{array}{ll}
1 & \textbf{while } r - l > \varepsilon\\
2 & \qquad \textit{mid}\gets (l+r)/2\\
3 & \qquad \textit{lmid}\gets \textit{mid} - \varepsilon / 3 \\
4 & \qquad \textit{rmid}\gets \textit{mid} + \varepsilon / 3 \\
5 & \qquad \textbf{if } f(\textit{lmid}) < f(\textit{rmid}) \\
6 & \qquad \qquad l\gets \textit{lmid} \\
7 & \qquad \textbf{else } \\
8 & \qquad \qquad r\gets \textit{rmid} \\
9 & x^* \gets (l+r)/2 \\
10& \textbf{return } x^*,~ f(x^*)
\end{array}
\end{array}
$$

???+ tip "Izbor točaka podjele"
    U kodu su točke podjele $\textit{mid} \pm \varepsilon / 3$ kako bi uvijek bile između trenutnih $l$ i $r$, čime se izbjegava beskonačna petlja.

???+ info "Cjelobrojni slučaj"
    Ako je domena funkcije $f(x)$ skup cijelih brojeva, i gornje ternarno pretraživanje i metoda zlatnog reza iz nastavka trebaju završiti čim je $r-l$ vrlo malen. Za vrlo malen $r-l$ točku maksimuma treba naći izravnim prolaskom kroz sve kandidate.

### Optimizacija: metoda zlatnog reza

Ako je jedan poziv $f(x)$ skup i treba dodatno smanjiti broj poziva $f(x)$, konstanta ternarnog pretraživanja može se dodatno poboljšati metodom zlatnog reza (golden-section search). To je ujedno važan dio metode optimalnog izbora koju je predložio Hua Luogeng.

U ternarnom pretraživanju svaka iteracija zahtijeva dva poziva funkcije, a nakon jedne iteracije duljina intervala smanji se najviše na $1/2$ izvorne. To znači da za postizanje preciznosti $\varepsilon$ treba barem

$$
2\log_2\dfrac{r-l}{\varepsilon}
$$

poziva funkcije. To je najbolje što ternarno pretraživanje može postići. Odaberu li se druge točke podjele, npr. trećinske točke, broj poziva dodatno raste jer se interval nakon jedne iteracije sporije skraćuje.

Ideja poboljšanja metodom zlatnog reza jest ponovno iskoristiti već izračunatu točku podjele. Tako su, osim u prvoj iteraciji koja zahtijeva dva poziva funkcije, u svim ostalim iteracijama potreban samo jedan poziv. Neka je omjer zlatnog reza

$$
\phi = \dfrac{\sqrt{5}-1}{2} \approx 0.618.
$$

U svakoj iteraciji biraju se lijeva i desna točka zlatnog reza:

$$
m^l = \phi l +(1-\phi)r,~m^r = (1-\phi)l+\phi r.
$$

Podjela dužine točkama zlatnog reza ima samosličnu strukturu. Drugim riječima, $m^l$ je lijeva točka zlatnog reza dužine $[l,r]$, ali i desna točka zlatnog reza dužine $[l,m^r]$. Prednost takvog izbora jest da je u iteraciji $k>1$ jedna od odabranih točaka podjele uvijek već ranije izračunata, pa se prethodni rezultat može izravno iskoristiti.

![](./images/golden-section-search.svg)

Uz takav izbor točaka podjele, za postizanje preciznosti $\varepsilon$ dovoljno je

$$
1 + \log_{\phi^{-1}}\dfrac{r-l}{\varepsilon} \approx 1 + 1.44\log_2\dfrac{r-l}{\varepsilon}
$$

poziva funkcije. Asimptotski je broj poziva funkcije manji.

Pseudokod:

$$
\begin{array}{l}
\textbf{Algorithm}\operatorname{GoldenSectionSearch}(f,l,r):\\
\textbf{Input. } \text{A unimodal function } f(x) \text{ and its domain } [l,r].  \\
\textbf{Output. } \text{The maximizer }x^*\text{, up to an error of }\varepsilon\text{, and its value } f(x^*). \\
\textbf{Method. } \\
\begin{array}{ll}
1 & \textit{lmid} \gets \phi l + (1-\phi)r \\
2 & \textit{rmid} \gets (1-\phi)l + \phi r \\
3 & \textit{lval} \gets f(\textit{lmid}) \\
4 & \textit{rval} \gets f(\textit{rmid}) \\
5 & \textbf{while } r - l > \varepsilon \\
6 & \qquad \textbf{if } \textit{lval} > \textit{rval} \\
7 & \qquad \qquad r \gets \textit{rmid} \\
8 & \qquad \qquad \textit{rmid} \gets \textit{lmid} \\
9 & \qquad \qquad \textit{rval} \gets \textit{lval} \\
10& \qquad \qquad \textit{lmid} \gets \phi l + (1-\phi)r \\
11& \qquad \qquad \textit{lval} \gets f(\textit{lmid}) \\
12& \qquad \textbf{else} \\
13& \qquad \qquad l \gets \textit{lmid} \\
14& \qquad \qquad \textit{lmid} \gets \textit{rmid} \\
15& \qquad \qquad \textit{lval} \gets \textit{rval} \\
16& \qquad \qquad \textit{rmid} \gets (1-\phi)l + \phi r \\
17& \qquad \qquad \textit{rval} \gets f(\textit{rmid}) \\
18& x^* \gets (l+r)/2 \\
19& \textbf{return }x^*,~f(x^*)
\end{array}
\end{array}
$$

### Primjer zadatka

???+ note "[Luogu P3382 - Ternarno pretraživanje](https://www.luogu.com.cn/problem/P3382)"
    Zadani su polinom $N$-tog stupnja i interval $[l, r]$. Pronađite jedinstveni $x$ takav da je funkcija rastuća na $[l, x]$ i padajuća na $[x, r]$.

??? note "Ideja rješenja"
    Zadatak traži vrijednost argumenta u kojoj polinom $N$-tog stupnja postiže maksimum na $[l, r]$, pa očito možemo primijeniti ternarno pretraživanje. Implementacija u nastavku koristi dvije trećinske točke i pomiče krajeve intervala na točke koje su zaista uspoređene; kad je interval dovoljno malen, ispisuje njegovu sredinu.

??? note "Referentni kod"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/binary/binary_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/binary/binary_1.py"
        ```

### Zadaci za vježbu

-   [UVa 1476 - Error Curves](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=447&page=show_problem&problem=4222)
-   [UVa 10385 - Duathlon](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=15&page=show_problem&problem=1326)
-   [UOJ 162 - Tsinghua Training 2015, Testiranje žarulja](https://uoj.ac/problem/162)
-   [Luogu P7579 - RdOI R2, Vaganje (weigh)](https://www.luogu.com.cn/problem/P7579)

## Razlomačko programiranje

Vidi: [Razlomačko programiranje](../misc/frac-programming.md)

Razlomačko programiranje (fractional programming) obično se opisuje sljedećim problemom: svaki predmet ima dva svojstva $c_i$, $d_i$, a treba na neki način odabrati nekoliko predmeta tako da $\dfrac{\sum{c_i}}{\sum{d_i}}$ bude najveći ili najmanji.

Klasični su primjeri ciklus optimalnog omjera, razapinjuće stablo optimalnog omjera i slično.

Razlomačko programiranje može se riješiti metodom polovljenja.

## Literatura i bilješke

-   [Ternary search - Wikipedia](https://en.wikipedia.org/wiki/Ternary_search)
-   [Golden-section search - Wikipedia](https://en.wikipedia.org/wiki/Golden-section_search)
-   [Ternary search - CP Algorithms](https://cp-algorithms.com/num_methods/ternary_search.html)
