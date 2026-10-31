---
title: Aritmetika velikih brojeva (bignum)
---

> Verzija za one koji ne žele čitati: gotovi predložak nalazi se na kraju…

## Definicija

Računanje s velikim brojevima (aritmetika proizvoljne preciznosti, Arbitrary-Precision Arithmetic), poznato i kao računanje s velikim cijelim brojevima (bignum), koristi određene algoritamske strukture kako bi podržalo operacije nad većim cijelim brojevima (brojevima koji premašuju ugrađene cjelobrojne tipove jezika).

## Uvod

Zadaci s velikim brojevima sadrže mnogo sitnih detalja, a i implementacija ima brojne finese.

Zato ćemo danas zajedno napisati jednostavan kalkulator.

???+ note "Zadatak"
    Ulaz: izraz oblika `a <op> b`.
    
    -   `a` i `b` nenegativni su dekadski cijeli brojevi duljine najviše $1000$;
    -   `<op>` je jedan znak (`+`, `-`, `*` ili `/`) koji označava operaciju.
    -   Brojevi i operator odvojeni su jednim razmakom.
    
    Izlaz: rezultat operacije.
    
    -   Za operacije `+`, `-` i `*` ispišite jedan redak s rezultatom;
    -   Za operaciju `/` ispišite dva retka: kvocijent i ostatak.
    -   Zajamčeno je da su svi rezultati nenegativni cijeli brojevi.

## Pohrana

U uobičajenim implementacijama veliki brojevi prikazuju se stringovima, pri čemu svaki znak predstavlja jednu dekadsku znamenku. Stoga se može reći da je računanje s velikim brojevima zapravo posebna vrsta obrade stringova.

Kad se string pročita, najznačajnija znamenka nalazi se na početku stringa (na mjestu s malim indeksom). No uobičajeno je da se na mjestu s najmanjim indeksom pohrani **najmanje značajna** znamenka, tj. pohranjuje se obrnuti string. Razlog je to što se duljina broja može mijenjati, a želimo da znamenke iste težine uvijek ostanu poravnate (primjerice, da sve jedinice budu na indeksu `[0]`, sve desetice na indeksu `[1]`…); istodobno, zbrajanje, oduzimanje i množenje obično počinju od jedinica (sjetite se pisanog računanja iz osnovne škole), što sve daje dovoljno razloga za „obrnutu pohranu”.

Tog ćemo se dogovora držati u nastavku. Definiramo konstantu `LEN = 1004` kao najveću duljinu koju program može prihvatiti.

Iz toga nije teško napisati kôd za čitanje velikog broja:

```cpp
void clear(int a[]) {
  for (int i = 0; i < LEN; ++i) a[i] = 0;
}

void read(int a[]) {
  static char s[LEN + 1];
  scanf("%s", s);

  clear(a);

  int len = strlen(s);
  // kao što je rečeno, obrćemo
  for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
  // s[i] - '0' je upravo znamenka koju s[i] predstavlja
  // nekima je možda bliže to shvatiti kao ord(s[i]) - ord('0')
}
```

Ispis također ide obrnutim redoslijedom od pohrane. Budući da ne želimo ispisivati vodeće nule, ovdje od najznačajnije znamenke tražimo prvu znamenku različitu od nule i od nje počinjemo ispis; uvjet zaustavljanja je `i >= 1`, a ne `i >= 0`, jer kad je cijeli broj jednak $0$ ipak želimo ispisati jedan znak `0`.

```cpp
void print(int a[]) {
  int i;
  for (i = LEN - 1; i >= 1; --i)
    if (a[i] != 0) break;
  for (; i >= 0; --i) putchar(a[i] + '0');
  putchar('\n');
}
```

Spojimo li to, dobivamo potpun program „papagaj” koji ponavlja uneseno.

??? note "`copycat.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    int main() {
      read(a);
      print(a);
    
      return 0;
    }
    ```

## Četiri osnovne operacije

Četiri osnovne operacije razlikuju se po težini. Najjednostavnije su zbrajanje i oduzimanje velikih brojeva, zatim množenje velikog broja običnim brojem (obični `int`) i množenje dvaju velikih brojeva, a na kraju dijeljenje velikog broja velikim brojem.

Sve tražene funkcionalnosti implementirat ćemo redom.

### Zbrajanje

Zbrajanje velikih brojeva zapravo je obično pisano zbrajanje.

![](./images/plus.svg)

Dakle, počevši od najmanje značajne znamenke, zbrajamo znamenke dvaju pribrojnika na odgovarajućim mjestima i provjeravamo je li zbroj dosegnuo ili premašio $10$. Ako jest, obrađujemo prijenos: rezultat na sljedećem višem mjestu uvećamo za $1$, a rezultat na trenutačnom mjestu umanjimo za $10$.

```cpp
void add(int a[], int b[], int c[]) {
  clear(c);

  // u implementacijama velikih brojeva najveća duljina niza LEN obično je malo veća od mogućeg ulaza,
  // a zatim se posljednjih nekoliko iteracija petlje preskoči; time se uštedi dosta obrade rubnih slučajeva
  // budući da stvarni ulaz ne prelazi 1000 znamenaka, ovdje je dovoljno ići do LEN - 1 = 1003
  for (int i = 0; i < LEN - 1; ++i) {
    // zbrojimo znamenke na odgovarajućem mjestu
    c[i] += a[i] + b[i];
    if (c[i] >= 10) {
      // prijenos
      c[i + 1] += 1;
      c[i] -= 10;
    }
  }
}
```

Pokušajte to spojiti s prethodnim dijelom i dobit ćete kalkulator za zbrajanje.

??? note "`adder.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN], b[LEN], c[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    void add(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] + b[i];
        if (c[i] >= 10) {
          c[i + 1] += 1;
          c[i] -= 10;
        }
      }
    }
    
    int main() {
      read(a);
      read(b);
    
      add(a, b, c);
      print(c);
    
      return 0;
    }
    ```

### Oduzimanje

Oduzimanje velikih brojeva također je obično pisano oduzimanje.

![](./images/subtraction.svg)

Od jedinica nadalje oduzimamo znamenku po znamenku, a kad naiđemo na negativan rezultat, posuđujemo $1$ s višeg mjesta. Cjelokupna je ideja potpuno ista kao kod zbrajanja.

```cpp
void sub(int a[], int b[], int c[]) {
  clear(c);

  for (int i = 0; i < LEN - 1; ++i) {
    // oduzimamo znamenku po znamenku
    c[i] += a[i] - b[i];
    if (c[i] < 0) {
      // posudba
      c[i + 1] -= 1;
      c[i] += 10;
    }
  }
}
```

Zamijenimo li u prethodnom programu `add()` sa `sub()`, dobivamo kalkulator za oduzimanje.

??? note "`subtractor.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN], b[LEN], c[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    void sub(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] - b[i];
        if (c[i] < 0) {
          c[i + 1] -= 1;
          c[i] += 10;
        }
      }
    }
    
    int main() {
      read(a);
      read(b);
    
      sub(a, b, c);
      print(c);
    
      return 0;
    }
    ```

Probajte: unesite `1 2` – izlaz je `/9999999`. Hej, zar nam je **OI Wiki** dao pogrešan kôd…

Zapravo, gornji kôd može obraditi samo slučaj kad je umanjenik $a$ veći od ili jednak umanjitelju $b$. Slučaj kad je umanjenik manji od umanjitelja, tj. $a<b$, rješava se jednostavno.

$a-b=-(b-a)$

Da bismo izračunali $b-a$, budući da je $b>a$, možemo pozvati funkciju `sub` iz gornjeg koda kao `sub(b,a,c)`. Da bismo dobili $a-b$, dovoljno je ispred rezultata dodati znak minus.

### Množenje

#### Veliki broj – obični broj

Množenje velikih brojeva također je obično pisano… čekajte, čekajte!

Razmotrimo prvo jednostavan slučaj: jedan od faktora običan je `int`. Postoji li jednostavan način da se to obradi?

Intuitivna je ideja jednostavno pomnožiti svaku znamenku broja $a$ s $b$. Brojčano je ta metoda ispravna, ali rezultat nije u skladu s dekadskim zapisom, pa ga treba ponovno urediti u uobičajeni oblik.

Uređivanje se također provodi od jedinica nadalje, obrađujući prijenos znamenku po znamenku prema višim mjestima. No ovdje prijenos može biti vrlo velik, čak znatno veći od $9$, jer svaka znamenka nakon množenja može dosegnuti red veličine $9b$. Zato se prijenos više ne može obraditi jednostavnom operacijom $-10$, nego ga treba izračunati preko kvocijenta i ostatka pri dijeljenju s $10$. Detalji su u komentarima koda, a možete pogledati i sliku u nastavku koja prikazuje postupak množenja velikog broja $1337$ običnim brojem $42$.

![](./images/multiplication-short.png)

Naravno, upravo zbog toga ova metoda zahtijeva posebnu pozornost na raspon faktora $b$. Ako je on istog reda veličine kao $10^9$ (odnosno gornja granica odgovarajućeg cjelobrojnog tipa), množenje velikog broja običnim brojem treba koristiti s oprezom.

```cpp
void mul_short(int a[], int b, int c[]) {
  clear(c);

  for (int i = 0; i < LEN - 1; ++i) {
    // i-tu znamenku broja a izravno pomnožimo faktorom i dodamo u rezultat
    c[i] += a[i] * b;

    if (c[i] >= 10) {
      // obrada prijenosa
      // c[i] / 10, tj. kvocijent dijeljenja, postaje iznos prijenosa
      c[i + 1] += c[i] / 10;
      // a c[i] % 10, tj. ostatak dijeljenja, postaje vrijednost koja ostaje na trenutačnom mjestu
      c[i] %= 10;
    }
  }
}
```

#### Veliki broj – veliki broj

Ako su oba faktora veliki brojevi, pisano množenje ponovno dolazi do izražaja.

Prisjetimo se da svaki korak pisanog množenja zapravo računa zbroj nekoliko članova $a \times b_i \times 10^i$. Primjerice, pri računanju $1337 \times 42$ računamo $1337 \times 2 \times 10^0 + 1337 \times 4 \times 10^1$.

Stoga $b$ možemo rastaviti na njegove znamenke, od kojih je svaka običan broj, svaku od njih pomnožiti s $a$, a zatim ih pomaknuti ulijevo na odgovarajuća mjesta i zbrojiti – to je odgovor. Naravno, na kraju treba obraditi prijenos na isti način kao u prethodnom primjeru.

![](./images/multiplication-long.png)

Primijetite da se ovaj postupak ne poklapa posve s pisanim množenjem: naš algoritam u svakom koraku množenja ne radi prijenos, nego sve rezultate zadržava na odgovarajućim mjestima i tek na kraju obrađuje prijenos zajedno, ali to ne utječe na rezultat.

```cpp
void mul(int a[], int b[], int c[]) {
  clear(c);

  for (int i = 0; i < LEN - 1; ++i) {
    // ovdje izravno računamo i-tu znamenku rezultata (od najmanje značajne) i usput obrađujemo prijenos
    // i-ta iteracija u c[i] dodaje zbroj svih umnožaka a[p] * b[q] za koje je p + q = i
    // učinak je isti kao kad bismo proveli račun sa slike i na kraju zbrojili, samo je implementacija kraća
    for (int j = 0; j <= i; ++j) c[i] += a[j] * b[i - j];

    if (c[i] >= 10) {
      c[i + 1] += c[i] / 10;
      c[i] %= 10;
    }
  }
}
```

### Dijeljenje

Jedan način implementacije dijeljenja velikih brojeva pisano je dugo dijeljenje.

![](./images/division.svg)

Pisano dugo dijeljenje zapravo se može promatrati kao postupak uzastopnog oduzimanja. Primjerice, računanje desetica kvocijenta na gornjoj slici može se shvatiti ovako: od $45$ tri puta oduzmemo $12$ i rezultat postane manji od $12$, dalje se ne može oduzimati, pa je ta znamenka $3$.

Kako bismo smanjili suvišne operacije, unaprijed odredimo duljinu djeljenika $l_a$ i duljinu djelitelja $l_b$ te kvocijent računamo od indeksa $l_a - l_b$ nadalje, od viših prema nižim znamenkama. To je isto kao kad pri ručnom računanju najznačajniju znamenku prvog množenja poravnamo s najznačajnijom znamenkom djeljenika.

Referentni program implementira funkciju `greater_eq()` koja provjerava može li se od djeljenika, kojemu je indeks `last_dg` najmanje značajna znamenka, još jednom oduzeti djelitelj tako da rezultat ostane nenegativan. Zatim za svaku znamenku kvocijenta uzastopno pozivamo `greater_eq()` i, kad je uvjet ispunjen, oduzimanjem velikih brojeva oduzmemo djelitelj od ostatka, čime simuliramo postupak pisanog dijeljenja.

```cpp
// može li se od djeljenika a, kojemu je indeks last_dg najmanje značajna znamenka, još oduzeti djelitelj b tako da ostane nenegativan
// len je duljina djelitelja b, da se ne računa iznova
bool greater_eq(int a[], int b[], int last_dg, int len) {
  // preostali dio djeljenika može biti dulji od djelitelja, ali najviše za 1 znamenku, pa je ova provjera dovoljna
  if (a[last_dg + len] != 0) return true;
  // od najznačajnije do najmanje značajne znamenke, usporedba znamenku po znamenku
  for (int i = len - 1; i >= 0; --i) {
    if (a[last_dg + i] > b[i]) return true;
    if (a[last_dg + i] < b[i]) return false;
  }
  // slučaj jednakosti također je dopušten
  return true;
}

void div(int a[], int b[], int c[], int d[]) {
  clear(c);
  clear(d);

  int la, lb;
  for (la = LEN - 1; la > 0; --la)
    if (a[la - 1] != 0) break;
  for (lb = LEN - 1; lb > 0; --lb)
    if (b[lb - 1] != 0) break;
  if (lb == 0) {  // djelitelj ne smije biti nula
    puts("> <");
    return;
  }

  // c je kvocijent
  // d je preostali dio djeljenika, koji nakon završetka algoritma prirodno postaje ostatak
  for (int i = 0; i < la; ++i) d[i] = a[i];
  for (int i = la - lb; i >= 0; --i) {
    // računamo i-tu znamenku kvocijenta
    while (greater_eq(d, b, i, lb)) {
      // ako se može oduzeti, oduzmemo
      // ovaj je odsječak oduzimanje velikih brojeva
      for (int j = 0; j < lb; ++j) {
        d[i + j] -= b[j];
        if (d[i + j] < 0) {
          d[i + j + 1] -= 1;
          d[i + j] += 10;
        }
      }
      // ovu znamenku kvocijenta uvećamo za 1
      c[i] += 1;
      // vraćamo se na početak petlje i ponovno provjeravamo
    }
  }
}
```

## Uvodni dio dovršen!

Spojimo li gore opisane implementacije četiriju osnovnih operacija, dobivamo program kalkulatora spomenut na početku.

??? note "`calculator.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN], b[LEN], c[LEN], d[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    void add(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] + b[i];
        if (c[i] >= 10) {
          c[i + 1] += 1;
          c[i] -= 10;
        }
      }
    }
    
    void sub(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] - b[i];
        if (c[i] < 0) {
          c[i + 1] -= 1;
          c[i] += 10;
        }
      }
    }
    
    void mul(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        for (int j = 0; j <= i; ++j) c[i] += a[j] * b[i - j];
    
        if (c[i] >= 10) {
          c[i + 1] += c[i] / 10;
          c[i] %= 10;
        }
      }
    }
    
    bool greater_eq(int a[], int b[], int last_dg, int len) {
      if (a[last_dg + len] != 0) return true;
      for (int i = len - 1; i >= 0; --i) {
        if (a[last_dg + i] > b[i]) return true;
        if (a[last_dg + i] < b[i]) return false;
      }
      return true;
    }
    
    void div(int a[], int b[], int c[], int d[]) {
      clear(c);
      clear(d);
    
      int la, lb;
      for (la = LEN - 1; la > 0; --la)
        if (a[la - 1] != 0) break;
      for (lb = LEN - 1; lb > 0; --lb)
        if (b[lb - 1] != 0) break;
      if (lb == 0) {
        puts("> <");
        return;
      }
    
      for (int i = 0; i < la; ++i) d[i] = a[i];
      for (int i = la - lb; i >= 0; --i) {
        while (greater_eq(d, b, i, lb)) {
          for (int j = 0; j < lb; ++j) {
            d[i + j] -= b[j];
            if (d[i + j] < 0) {
              d[i + j + 1] -= 1;
              d[i + j] += 10;
            }
          }
          c[i] += 1;
        }
      }
    }
    
    int main() {
      read(a);
    
      char op[4];
      scanf("%s", op);
    
      read(b);
    
      switch (op[0]) {
        case '+':
          add(a, b, c);
          print(c);
          break;
        case '-':
          sub(a, b, c);
          print(c);
          break;
        case '*':
          mul(a, b, c);
          print(c);
          break;
        case '/':
          div(a, b, c, d);
          print(c);
          print(d);
          break;
        default:
          puts("> <");
      }
    
      return 0;
    }
    ```

## Pakiranje znamenaka

### Uvod

U običnom zbrajanju, oduzimanju i množenju velikih brojeva brojeve koji sudjeluju u operaciji rastavljamo na pojedinačne znamenke i s njima računamo.

Primjerice, pri računanju $8192\times 42$, ako slijedimo postupak množenja dvaju velikih brojeva, zapravo računamo $(8000+100+90+2)\times(40+2)$.

Kad broj ima mnogo znamenaka, i rastavljenih dijelova je mnogo, pa učinkovitost računanja s velikim brojevima opada.

Može li se to nekako optimizirati?

Primijetimo da način rastavljanja broja ne utječe na konačni rezultat, pa možemo spojiti više znamenaka u jednu cjelinu.

### Postupak

Uzmimo ponovno gornji primjer: ako rastavljamo po dvije znamenke, možemo rastaviti kao $(8100+92)\times 42$.

Takvo rastavljanje ne utječe na konačni rezultat, ali budući da je rastavljenih brojeva manje, učinkovitost računanja raste.

Gledano iz perspektive [brojevnih sustava](./numeral-sys/base.md), ovaj postupak znači da računamo u većoj bazi (gornje rastavljanje po dvije znamenke može se shvatiti kao računanje u bazi $100$), čime smanjujemo broj znamenaka koje sudjeluju u računu i povećavamo učinkovitost.

To je ideja **pakiranja znamenaka** (压位高精度, više znamenaka u jednoj ćeliji).

U nastavku dajemo kôd zbrajanja velikih brojeva s pakiranjem znamenaka kako bismo dodatno pojasnili način implementacije:

??? note "Referentna implementacija zbrajanja s pakiranjem znamenaka"
    ```cpp
    // ovdje su nizovi a, b, c brojevi u bazi p
    // pri konačnom ispisu odgovora broj treba pretvoriti u dekadski zapis
    void add(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] + b[i];
        if (c[i] >= p) {  // u običnom računanju s velikim brojevima p=10
          c[i + 1] += 1;
          c[i] -= p;
        }
      }
    }
    ```

### Učinkovito pisano dijeljenje s pakiranjem znamenaka

Kad koristimo pakiranje znamenaka, ako pri pogađanju znamenke kvocijenta i dalje koristimo gore opisanu metodu, broj pokušaja bit će vrlo velik, pa će i konstanta u složenosti biti ogromna. Primjerice, u bazi 10000 za svaku znamenku u prosjeku treba 5000 pokušaja, što je neprihvatljivo velika konstanta. Zato trebamo učinkovitiji način pogađanja kvocijenta.

Kao posrednik može poslužiti `double`. Pretpostavimo da djeljenik ima 4 znamenke, $a_4,a_3,a_2,a_1$, a djelitelj 3 znamenke, $b_3,b_2,b_1$; tada trebamo pogoditi samo jednu znamenku kvocijenta: u bazi $base$ kvocijent procjenjujemo izrazom $\dfrac{a_4 base + a_3}{b_3 + b_2 base^{-1} + (b_1+1)base^{-2}}$. Za više znamenaka, postupak za jednu znamenku jednostavno stavimo u petlju. Budući da djelitelj u procjeni sudjeluje s preciznošću od 3 znamenke, zajamčeno je da procijenjeni kvocijent q' i stvarni kvocijent q zadovoljavaju $q-1 \le q' \le q$, pa su za svaku znamenku u najgorem slučaju potrebna samo dva pokušaja. Istodobno se zahtijeva da $base^3$ bude unutar efektivne preciznosti tipa `double`, tj. $base^3 < 2^{53}$, pa se pri primjeni ove metode preporučuje ne prelaziti bazu 32768; inače zbog nedovoljne preciznosti lako nastaju odstupanja koja dovode do pogrešaka.

Osim toga, budući da je procijenjeni kvocijent uvijek manji od ili jednak stvarnome, postoji prostor za daljnju optimizaciju. U velikoj većini slučajeva za svaku znamenku kvocijent procjenjujemo samo jednom; tada pri procjeni sljedeće znamenke dobiveni kvocijent zbog pogreške prethodne znamenke može biti veći od ili jednak base, ali to nije problem – dovoljno je na kraju odjednom obraditi prijenose. Na primjer, neka je baza 10 i računamo $395081/9876$; koraci pogađanja kvocijenta su sljedeći:

1.  Prvo pogađanjem dobivamo $3950/988=3$, pa je $395081-(9876 \times 3 \times 10^1) = 98801$; u ovom se koraku pojavila pogreška, ali ne obraćamo pozornost na nju i nastavljamo sa sljedećim korakom.
2.  Za ostatak 98801 pogađanjem dobivamo $9880/988=10$, pa je $98801-(9876 \times 10 \times 10^0) = 41$, što je konačni ostatak.
3.  Zbrojimo rezultate pogađanja i obradimo prijenos: $3 \times 10^1 + 10 \times 10^0 = 40$ točan je kvocijent.

Iako metoda izgleda jednostavno, u konkretnoj se implementaciji lako upada u zamke, pa u nastavku dajemo višestruko provjerenu implementaciju bez poznatih grešaka kao referencu; detalji na koje treba obratiti pozornost napisani su u komentarima.

??? note "Referentna implementacija učinkovitog pisanog dijeljenja s pakiranjem znamenaka"
    ```cpp
    // potpuni predložak i implementacija: https://baobaobear.github.io/post/20210228-bigint1/
    // od ovog broja oduzima b pomnožen s mul i pomaknut ulijevo za offset; služi dijeljenju
    BigIntSimple &sub_mul(const BigIntSimple &b, int mul, int offset) {
      if (mul == 0) return *this;
      int borrow = 0;
      // za razliku od oduzimanja, borrow može biti vrlo velik, pa se ne može pisati kao kod oduzimanja
      for (size_t i = 0; i < b.v.size(); ++i) {
        borrow += v[i + offset] - b.v[i] * mul - BIGINT_BASE + 1;
        v[i + offset] = borrow % BIGINT_BASE + BIGINT_BASE - 1;
        borrow /= BIGINT_BASE;
      }
      // ako još ima posudbe, nastavljamo obradu
      for (size_t i = b.v.size(); borrow; ++i) {
        borrow += v[i + offset] - BIGINT_BASE + 1;
        v[i + offset] = borrow % BIGINT_BASE + BIGINT_BASE - 1;
        borrow /= BIGINT_BASE;
      }
      return *this;
    }
    
    BigIntSimple div_mod(const BigIntSimple &b, BigIntSimple &r) const {
      BigIntSimple d;
      r = *this;
      if (absless(b)) return d;
      d.v.resize(v.size() - b.v.size() + 1);
      // unaprijed izračunamo recipročnu vrijednost najznačajnije tri znamenke djelitelja + 1; ako su najznačajnije tri znamenke a3,a2,a1,
      // onda je db recipročna vrijednost od a3+a2/base+(a1+1)/base^2, a na kraju množenjem procjenjujemo svaku znamenku kvocijenta
      // ova metoda radi unutar raspona int32 kad je BIGINT_BASE<=32768
      // ali čak i s int64 upotrebljiva je samo za BIGINT_BASE<=131072 (ograničeno preciznošću tipa double)
      // može se zajamčiti da procijenjeni rezultat q' i stvarni rezultat q zadovoljavaju q'<=q<=q'+1
      // pa je za svaku znamenku u prosjeku potreban samo jedan pokušaj, a prijenosi se poslije obrade odjednom
      // ako se želi koristiti veća baza, treba promijeniti način pogađanja kvocijenta
      double t = (b.get((unsigned)b.v.size() - 2) +
                  (b.get((unsigned)b.v.size() - 3) + 1.0) / BIGINT_BASE);
      double db = 1.0 / (b.v.back() + t / BIGINT_BASE);
      for (size_t i = v.size() - 1, j = d.v.size() - 1; j <= v.size();) {
        int rm = r.get(i + 1) * BIGINT_BASE + r.get(i);
        int m = std::max((int)(db * rm), r.get(i + 1));
        r.sub_mul(b, m, j);
        d.v[j] += m;
        if (!r.get(i + 1))  // provjeravamo je li najznačajnija znamenka već 0, da izbjegnemo ekstremne slučajeve
          --i, --j;
      }
      r.trim();
      // ispravak najmanje značajne znamenke rezultata
      int carry = 0;
      while (!r.absless(b)) {
        r.subtract(b);
        ++carry;
      }
      // ispravak prijenosa na svakoj znamenki
      for (size_t i = 0; i < d.v.size(); ++i) {
        carry += d.v[i];
        d.v[i] = carry % BIGINT_BASE;
        carry /= BIGINT_BASE;
      }
      d.trim();
      d.sign = sign * b.sign;
      return d;
    }
    
    BigIntSimple operator/(const BigIntSimple &b) const {
      BigIntSimple r;
      return div_mod(b, r);
    }
    
    BigIntSimple operator%(const BigIntSimple &b) const {
      BigIntSimple r;
      div_mod(b, r);
      return r;
    }
    ```

## Karatsubino množenje

Označimo broj znamenaka velikog broja s $n$; tada pisano množenje dvaju velikih brojeva zahtijeva $O(n^2)$ vremena. U ovom odjeljku predstavljamo algoritam bolje vremenske složenosti, koji je predložio sovjetski (ruski) matematičar Anatolij Karacuba (Anatoly Karatsuba); riječ je o algoritmu tipa „podijeli pa vladaj”.

Promotrimo dva velika dekadska cijela broja $x$ i $y$, oba s $n$ znamenaka (vodeće nule su dopuštene). Odaberimo proizvoljno $0 < m < n$ i označimo

$$
\begin{aligned}
x &= x_1 \cdot 10^m + x_0, \\
y &= y_1 \cdot 10^m + y_0, \\
x \cdot y &= z_2 \cdot 10^{2m} + z_1 \cdot 10^m + z_0,
\end{aligned}
$$

gdje je $x_0, y_0, z_0, z_1 < 10^m$. Dobivamo

$$
\begin{aligned}
z_2 &= x_1 \cdot y_1, \\
z_1 &= x_1 \cdot y_0 + x_0 \cdot y_1, \\
z_0 &= x_0 \cdot y_0.
\end{aligned}
$$

Uočavamo

$$
z_1 = (x_1 + x_0) \cdot (y_1 + y_0) - z_2 - z_0,
$$

pa za izračun $z_1$ treba izračunati samo $(x_1 + x_0) \cdot (y_1 + y_0)$ i od toga oduzeti $z_0$ i $z_2$.

Gornja je formula zapravo srž Karatsubina algoritma: ona problem množenja duljine $n$ pretvara u $3$ potproblema manje duljine. Ako stavimo $m = \left\lceil \dfrac n 2 \right\rceil$ i označimo vrijeme koje Karatsubin algoritam troši na množenje dvaju $n$-znamenkastih brojeva s $T(n)$, vrijedi $T(n) = 3 \cdot T \left(\left\lceil \dfrac n 2 \right\rceil\right) + O(n)$, a iz master teorema slijedi $T(n) = \Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})$.

Cijeli se postupak može implementirati rekurzivno. Radi jasnoće, kôd u nastavku Karatsubinim algoritmom implementira množenje polinoma, a na kraju obrađuje sve prijenose.

??? note "karatsuba_mulc.cpp"
    ```cpp
    int *karatsuba_polymul(int n, int *a, int *b) {
      if (n <= 32) {
        // za male veličine računamo izravno, da izbjegnemo gubitak učinkovitosti zbog daljnje rekurzije
        int *r = new int[n * 2 + 1]();
        for (int i = 0; i <= n; ++i)
          for (int j = 0; j <= n; ++j) r[i + j] += a[i] * b[j];
        return r;
      }
    
      int m = n / 2 + 1;
      int *r = new int[m * 4 + 1]();
      int *z0, *z1, *z2;
    
      z0 = karatsuba_polymul(m - 1, a, b);
      z2 = karatsuba_polymul(n - m, a + m, b + m);
    
      // računamo z1
      // privremena izmjena, nakon računanja vraćamo
      for (int i = 0; i + m <= n; ++i) a[i] += a[i + m];
      for (int i = 0; i + m <= n; ++i) b[i] += b[i + m];
      z1 = karatsuba_polymul(m - 1, a, b);
      for (int i = 0; i + m <= n; ++i) a[i] -= a[i + m];
      for (int i = 0; i + m <= n; ++i) b[i] -= b[i + m];
      for (int i = 0; i <= (m - 1) * 2; ++i) z1[i] -= z0[i];
      for (int i = 0; i <= (n - m) * 2; ++i) z1[i] -= z2[i];
    
      // rezultat dobivamo kombiniranjem z0, z1, z2
      for (int i = 0; i <= (m - 1) * 2; ++i) r[i] += z0[i];
      for (int i = 0; i <= (m - 1) * 2; ++i) r[i + m] += z1[i];
      for (int i = 0; i <= (n - m) * 2; ++i) r[i + m * 2] += z2[i];
    
      delete[] z0;
      delete[] z1;
      delete[] z2;
      return r;
    }
    
    void karatsuba_mul(int a[], int b[], int c[]) {
      int *r = karatsuba_polymul(LEN - 1, a, b);
      memcpy(c, r, sizeof(int) * LEN);
      for (int i = 0; i < LEN - 1; ++i)
        if (c[i] >= 10) {
          c[i + 1] += c[i] / 10;
          c[i] %= 10;
        }
      delete[] r;
    }
    ```

??? note "O `new` i `delete`"
    Vidi [Memory pool](../contest/common-tricks.md#memory-pool).

No takva implementacija ima problem: u bazi $b$ svaki koeficijent polinoma može dosegnuti red veličine $n \cdot b^2$, što u implementaciji s pakiranjem znamenaka može uzrokovati prelijevanje cijelih brojeva; a ako prijenose obrađujemo tijekom množenja polinoma, rezultati $x_1 + x_0$ i $y_1 + y_0$ mogu dosegnuti $2 \cdot b^m$, tj. dobiti jednu znamenku više (ako se pak računa u obliku $x_1 - x_0$, nužno je posebno obraditi negativne brojeve). Stoga način implementacije treba odabrati prema konkretnoj primjeni.

## Učinkovito množenje velikih brojeva pomoću polinoma

Ako veličina podataka dosegne $10^{10^5}$ ili više, obično množenje velikih brojeva može prekoračiti vremensko ograničenje. U ovom odjeljku predstavljamo kako takvo množenje optimizirati pomoću polinoma.

$n$-znamenkasti dekadski cijeli broj $a$ možemo promatrati kao polinom $A=a_{0} 10^0+a_{1} 10^1+\cdots+a_{n-1} 10^{n-1}$ čiji su svi koeficijenti cijeli brojevi manji od $10$. Tako smo množenje dvaju cijelih brojeva pretvorili u množenje dvaju polinoma.

Obično množenje polinoma i dalje ima vremensku složenost $O(n^2)$, ali može se optimizirati algoritmima iz poglavlja o polinomima, kao što su [brza Fourierova transformacija](poly/fft.md) i [brza teorijsko-brojevna transformacija](poly/ntt.md); nakon optimizacije vremenska je složenost $O(n\log n)$.

## Gotova klasa

[Ovdje](https://paste.ubuntu.com/p/7VKYzpC7dn/) se nalazi gotova klasa za velike cijele brojeve, a [ovdje](https://github.com/Baobaobear/MiniBigInteger/blob/main/bigint_tiny.h) ultraminijaturna implementacija klase koja podržava dinamičku duljinu i četiri osnovne operacije.

??? note "Ovdje je još jedan predložak"
    ```cpp
    constexpr int MAXN = 9999;
    // MAXN je najveći broj u jednoj ćeliji
    constexpr int MAXSIZE = 10024;
    // MAXSIZE je broj ćelija
    constexpr int DLEN = 4;
    
    // DLEN bilježi koliko se znamenaka pakira
    struct Big {
      int a[MAXSIZE], len;
      bool flag;  // označava predznak '-'
    
      Big() {
        len = 1;
        memset(a, 0, sizeof a);
        flag = false;
      }
    
      Big(const int);
      Big(const char*);
      Big(const Big&);
      Big& operator=(const Big&);
      Big operator+(const Big&) const;
      Big operator-(const Big&) const;
      Big operator*(const Big&) const;
      Big operator/(const int&) const;
      // TODO: Big / Big;
      Big operator^(const int&) const;
      // TODO: Big ^ Big;
    
      // TODO: bitovne operacije nad Big;
    
      int operator%(const int&) const;
      // TODO: Big ^ Big;
      bool operator<(const Big&) const;
      bool operator<(const int& t) const;
      void print() const;
    };
    
    Big::Big(const int b) {
      int c, d = b;
      len = 0;
      // memset(a,0,sizeof a);
      CLR(a);
      while (d > MAXN) {
        c = d - (d / (MAXN + 1) * (MAXN + 1));
        d = d / (MAXN + 1);
        a[len++] = c;
      }
      a[len++] = d;
    }
    
    Big::Big(const char* s) {
      int t, k, index, l;
      CLR(a);
      l = strlen(s);
      len = l / DLEN;
      if (l % DLEN) ++len;
      index = 0;
      for (int i = l - 1; i >= 0; i -= DLEN) {
        t = 0;
        k = i - DLEN + 1;
        if (k < 0) k = 0;
        g(j, k, i) t = t * 10 + s[j] - '0';
        a[index++] = t;
      }
    }
    
    Big::Big(const Big& T) : len(T.len) {
      CLR(a);
      f(i, 0, len) a[i] = T.a[i];
      // TODO: preopteretiti ovdje?
    }
    
    Big& Big::operator=(const Big& T) {
      CLR(a);
      len = T.len;
      f(i, 0, len) a[i] = T.a[i];
      return *this;
    }
    
    Big Big::operator+(const Big& T) const {
      Big t(*this);
      int big = len;
      if (T.len > len) big = T.len;
      f(i, 0, big) {
        t.a[i] += T.a[i];
        if (t.a[i] > MAXN) {
          ++t.a[i + 1];
          t.a[i] -= MAXN + 1;
        }
      }
      if (t.a[big])
        t.len = big + 1;
      else
        t.len = big;
      return t;
    }
    
    Big Big::operator-(const Big& T) const {
      int big;
      bool ctf;
      Big t1, t2;
      if (*this < T) {
        t1 = T;
        t2 = *this;
        ctf = true;
      } else {
        t1 = *this;
        t2 = T;
        ctf = false;
      }
      big = t1.len;
      int j = 0;
      f(i, 0, big) {
        if (t1.a[i] < t2.a[i]) {
          j = i + 1;
          while (t1.a[j] == 0) ++j;
          --t1.a[j--];
          // WTF?
          while (j > i) t1.a[j--] += MAXN;
          t1.a[i] += MAXN + 1 - t2.a[i];
        } else
          t1.a[i] -= t2.a[i];
      }
      t1.len = big;
      while (t1.len > 1 && t1.a[t1.len - 1] == 0) {
        --t1.len;
        --big;
      }
      if (ctf) t1.a[big - 1] = -t1.a[big - 1];
      return t1;
    }
    
    Big Big::operator*(const Big& T) const {
      Big res;
      int up;
      int te, tee;
      f(i, 0, len) {
        up = 0;
        f(j, 0, T.len) {
          te = a[i] * T.a[j] + res.a[i + j] + up;
          if (te > MAXN) {
            tee = te - te / (MAXN + 1) * (MAXN + 1);
            up = te / (MAXN + 1);
            res.a[i + j] = tee;
          } else {
            up = 0;
            res.a[i + j] = te;
          }
        }
        if (up) res.a[i + T.len] = up;
      }
      res.len = len + T.len;
      while (res.len > 1 && res.a[res.len - 1] == 0) --res.len;
      return res;
    }
    
    Big Big::operator/(const int& b) const {
      Big res;
      int down = 0;
      gd(i, len - 1, 0) {
        res.a[i] = (a[i] + down * (MAXN + 1)) / b;
        down = a[i] + down * (MAXN + 1) - res.a[i] * b;
      }
      res.len = len;
      while (res.len > 1 && res.a[res.len - 1] == 0) --res.len;
      return res;
    }
    
    int Big::operator%(const int& b) const {
      int d = 0;
      gd(i, len - 1, 0) d = (d * (MAXN + 1) % b + a[i]) % b;
      return d;
    }
    
    Big Big::operator^(const int& n) const {
      Big t(*this), res(1);
      int y = n;
      while (y) {
        if (y & 1) res = res * t;
        t = t * t;
        y >>= 1;
      }
      return res;
    }
    
    bool Big::operator<(const Big& T) const {
      int ln;
      if (len < T.len) return true;
      if (len == T.len) {
        ln = len - 1;
        while (ln >= 0 && a[ln] == T.a[ln]) --ln;
        if (ln >= 0 && a[ln] < T.a[ln]) return true;
        return false;
      }
      return false;
    }
    
    bool Big::operator<(const int& t) const {
      Big tee(t);
      return *this < tee;
    }
    
    void Big::print() const {
      printf("%d", a[len - 1]);
      gd(i, len - 2, 0) { printf("%04d", a[i]); }
    }
    
    void print(const Big& s) {
      int len = s.len;
      printf("%d", s.a[len - 1]);
      gd(i, len - 2, 0) { printf("%04d", s.a[i]); }
    }
    
    char s[100024];
    ```

## Zadaci

-   [NOIP 2012 国王游戏 (Kraljeva igra)](https://loj.ac/problem/2603)
-   [SPOJ - Fast Multiplication](http://www.spoj.com/problems/MUL/en/)
-   [SPOJ - GCD2](http://www.spoj.com/problems/GCD2/)
-   [UVa - Division](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1024)
-   [UVa - Fibonacci Freeze](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=436)
-   [Codeforces - Notepad](http://codeforces.com/contest/17/problem/D)

## Literatura i poveznice

1.  [Karatsuba algorithm - Wikipedia](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
