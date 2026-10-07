---
title: Uvod u sufiksno polje
---

## Dogovori

Za definicije vezane uz stringove pogledajte [Osnove stringova](./basic.md).

Indeksi stringa počinju od $1$.

Duljina stringa $s$ je $n$.

„Sufiks $i$” označava sufiks koji počinje $i$-tim znakom; pri pohrani sufiks $s[i\dots n]$ stringa $s$ predstavljamo brojem $i$.

## Što je sufiksno polje?

Sufiksno polje (Suffix Array) povezano je uglavnom s dva polja: $sa$ i $rk$.

Pritom $sa[i]$ označava indeks $i$-tog najmanjeg sufiksa nakon sortiranja svih sufiksa; to je samo sufiksno polje, a u nastavku ga zovemo i poljem indeksa $sa$;

$rk[i]$ označava rang sufiksa $i$; to je važno pomoćno polje, a u nastavku ga zovemo i poljem rangova $rk$.

Ta dva polja zadovoljavaju svojstvo $sa[rk[i]]=rk[sa[i]]=i$.

### Objašnjenje

Primjer sufiksnog polja:

[![](./images/sa1.png)][2]

## Kako izračunati sufiksno polje?

### Pristup O(n^2logn)

Vjerujemo da se ovog pristupa svatko može sjetiti sam: polje koje sadrži sve sufikse sortiramo pomoću `sort`. Budući da sortiranje obavlja $O(n\log n)$ usporedbi stringova, a svaka usporedba stringova zahtijeva $O(n)$ usporedbi znakova, vremenska je složenost ovog sortiranja $O(n^2\log n)$.

### Pristup O(nlog^2n)

Ovaj se pristup oslanja na ideju udvostručavanja (doubling).

Najprije sortiramo sve podstringove stringa $s$ duljine $1$, tj. pojedinačne znakove, i dobijemo sortirano polje indeksa $sa_1$ i polje rangova $rk_1$.

Postupak udvostručavanja:

1.  Rangove dvaju podstringova duljine $1$, tj. $rk_1[i]$ i $rk_1[i+1]$, upotrijebimo kao prvi i drugi ključ sortiranja; time možemo sortirati sve podstringove stringa $s$ duljine $2$: $\{s[i\dots \min(i+1, n)]\ |\ i \in [1,\ n]\}$ i dobiti $sa_2$ i $rk_2$;

2.  zatim rangove dvaju podstringova duljine $2$, tj. $rk_2[i]$ i $rk_2[i+2]$, upotrijebimo kao prvi i drugi ključ sortiranja; time možemo sortirati sve podstringove stringa $s$ duljine $4$: $\{s[i\dots \min(i+3, n)]\ |\ i \in [1,\ n]\}$ i dobiti $sa_4$ i $rk_4$;

3.  tako udvostručavamo dalje: rangove podstringova duljine $w/2$, tj. $rk_{w/2}[i]$ i $rk_{w/2}[i+w/2]$, upotrijebimo kao prvi i drugi ključ sortiranja, čime sortiramo sve podstringove stringa $s$ duljine $w$, $s[i\dots \min(i+w-1,\ n)]$, i dobivamo $sa_w$ i $rk_w$. Pritom, slično pravilima leksikografskog uređaja, kad je $i+w>n$, $rk_w[i+w]$ smatramo beskonačno malim;

4.  $rk_w[i]$ je rang podstringa $s[i\dots i + w - 1]$, pa je za $w \geqslant n$ dobiveno polje indeksa $sa_w$ upravo traženo sufiksno polje.

#### Postupak

Shema sortiranja udvostručavanjem:

[![](./images/sa2.png)][2]

Očito postupak udvostručavanja ima $O(\log n)$ koraka, a sortiranje podstringova pomoću `sort` u svakom koraku stoji $O(n\log n)$, pri čemu svaka usporedba podstringova troši $2$ usporedbe znakova;

osim toga, u svakom koraku udvostručavanja nakon `sort` imamo još i ažuriranje $rk$ vremenske složenosti $O(n)$, no ono je zanemarivo u odnosu na $O(n\log n)$;

stoga je vremenska složenost ovog algoritma $O(n\log^2n)$.

??? note "Implementacija"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    
    using namespace std;
    
    constexpr int N = 1000010;
    
    char s[N];
    int n, w, sa[N], rk[N << 1], oldrk[N << 1];
    
    // Da pristup rk[i+w] ne bi izašao izvan granica polja, polje je dvostruke veličine.
    // Naravno, moglo bi se prije pristupa provjeravati izlazi li se izvan granica, ali dvostruko polje je jednostavnije.
    
    int main() {
      int i, p;
    
      scanf("%s", s + 1);
      n = strlen(s + 1);
      for (i = 1; i <= n; ++i) sa[i] = i, rk[i] = s[i];
    
      for (w = 1; w < n; w <<= 1) {
        sort(sa + 1, sa + n + 1, [](int x, int y) {
          return rk[x] == rk[y] ? rk[x + w] < rk[y + w] : rk[x] < rk[y];
        });  // ovdje koristimo lambdu
        memcpy(oldrk, rk, sizeof(rk));
        // budući da se pri računanju rk stari rk prepisuje, najprije ga kopiramo
        // ako su dva podstringa jednaka, njihovi rk moraju biti jednaki, pa uklanjamo duplikate
        for (p = 0, i = 1; i <= n; ++i) {
          if (oldrk[sa[i]] == oldrk[sa[i - 1]] &&
              oldrk[sa[i] + w] == oldrk[sa[i - 1] + w]) {
            rk[sa[i]] = p;
          } else {
            rk[sa[i]] = ++p;
          }
        }
      }
    
      for (i = 1; i <= n; ++i) printf("%d ", sa[i]);
    
      return 0;
    }
    ```

### Pristup O(nlogn)

U upravo opisanom pristupu $O(n\log^2n)$ jedno sortiranje stoji $O(n\log n)$; ako bismo sortirali u $O(n)$, sufiksno polje mogli bismo izračunati u $O(n\log n)$.

Predznanje: [Counting sort](../basic/counting-sort.md), [Radix sort](../basic/radix-sort.md).

Budući da su ključevi sortiranja pri računanju sufiksnog polja rangovi, čiji je raspon vrijednosti $O(n)$, i da se radi o sortiranju po dva ključa, radix sortom možemo optimirati sortiranje na $O(n)$.

??? note "Implementacija"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    
    using namespace std;
    
    constexpr int N = 1000010;
    
    char s[N];
    int n, sa[N], rk[N << 1], oldrk[N << 1], id[N], cnt[N];
    
    int main() {
      int i, m, p, w;
    
      scanf("%s", s + 1);
      n = strlen(s + 1);
      m = 127;
      for (i = 1; i <= n; ++i) ++cnt[rk[i] = s[i]];
      for (i = 1; i <= m; ++i) cnt[i] += cnt[i - 1];
      for (i = n; i >= 1; --i) sa[cnt[rk[i]]--] = i;
      memcpy(oldrk + 1, rk + 1, n * sizeof(int));
      for (p = 0, i = 1; i <= n; ++i) {
        if (oldrk[sa[i]] == oldrk[sa[i - 1]]) {
          rk[sa[i]] = p;
        } else {
          rk[sa[i]] = ++p;
        }
      }
    
      for (w = 1; w < n; w <<= 1, m = n) {
        // counting sort po drugom ključu: id[i] + w
        memset(cnt, 0, sizeof(cnt));
        memcpy(id + 1, sa + 1,
               n * sizeof(int));  // id čuva kopiju sa, što je zapravo oldsa
        for (i = 1; i <= n; ++i) ++cnt[rk[id[i] + w]];
        for (i = 1; i <= m; ++i) cnt[i] += cnt[i - 1];
        for (i = n; i >= 1; --i) sa[cnt[rk[id[i] + w]]--] = id[i];
    
        // counting sort po prvom ključu: id[i]
        memset(cnt, 0, sizeof(cnt));
        memcpy(id + 1, sa + 1, n * sizeof(int));
        for (i = 1; i <= n; ++i) ++cnt[rk[id[i]]];
        for (i = 1; i <= m; ++i) cnt[i] += cnt[i - 1];
        for (i = n; i >= 1; --i) sa[cnt[rk[id[i]]]--] = id[i];
    
        memcpy(oldrk + 1, rk + 1, n * sizeof(int));
        for (p = 0, i = 1; i <= n; ++i) {
          if (oldrk[sa[i]] == oldrk[sa[i - 1]] &&
              oldrk[sa[i] + w] == oldrk[sa[i - 1] + w]) {
            rk[sa[i]] = p;
          } else {
            rk[sa[i]] = ++p;
          }
        }
      }
    
      for (i = 1; i <= n; ++i) printf("%d ", sa[i]);
    
      return 0;
    }
    ```

### Neke optimizacije konstante

Ako gornji kôd predate na [LOJ #111: Sufiksno sortiranje](https://loj.ac/problem/111):

![](./images/sa3.png)

To je zato što gornji kôd doista ima veliku konstantu.

#### Drugi ključ ne treba counting sort

Razmislimo o biti sortiranja po drugom ključu: zapravo samo stavljamo one $sa[i]$ koji izlaze izvan stringa (tj. $sa[i] + w > n$) na početak polja $sa$, a ostale redom u izvornom poretku:

```cpp
int cur = 0;
for (int i = n - w + 1; i <= n; i++) id[++cur] = i;
for (int i = 1; i <= n; i++)
  if (sa[i] > w) id[++cur] = sa[i] - w;
```

#### Optimizacija raspona vrijednosti counting sorta

Nakon svakog ažuriranja $rk$ izračunali smo $p$; taj je $p$ upravo raspon vrijednosti od $rk$, pa raspon postavimo na njega.

#### Ako su svi rangovi različiti, sufiksno polje možemo izravno generirati

Promotrimo novo polje $rk$: ako je njegov raspon vrijednosti $[1,n]$, svi su rangovi različiti i više ne treba sortirati.

??? note "Implementacija"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    
    using namespace std;
    
    constexpr int N = 1000010;
    
    char s[N];
    int n;
    int m, p, rk[N * 2], oldrk[N], sa[N * 2], id[N], cnt[N];
    
    int main() {
      scanf("%s", s + 1);
      n = strlen(s + 1);
      m = 128;
    
      for (int i = 1; i <= n; i++) cnt[rk[i] = s[i]]++;
      for (int i = 1; i <= m; i++) cnt[i] += cnt[i - 1];
      for (int i = n; i >= 1; i--) sa[cnt[rk[i]]--] = i;
    
      for (int w = 1;; w <<= 1, m = p) {  // m = p je optimizacija raspona vrijednosti
        int cur = 0;
        for (int i = n - w + 1; i <= n; i++) id[++cur] = i;
        for (int i = 1; i <= n; i++)
          if (sa[i] > w) id[++cur] = sa[i] - w;
    
        memset(cnt, 0, sizeof(cnt));
        for (int i = 1; i <= n; i++) cnt[rk[i]]++;
        for (int i = 1; i <= m; i++) cnt[i] += cnt[i - 1];
        for (int i = n; i >= 1; i--) sa[cnt[rk[id[i]]]--] = id[i];
    
        p = 0;
        memcpy(oldrk, rk, sizeof(oldrk));
        for (int i = 1; i <= n; i++) {
          if (oldrk[sa[i]] == oldrk[sa[i - 1]] &&
              oldrk[sa[i] + w] == oldrk[sa[i - 1] + w])
            rk[sa[i]] = p;
          else
            rk[sa[i]] = ++p;
        }
    
        if (p == n) break;  // za p = n više ne treba sortirati
      }
    
      for (int i = 1; i <= n; i++) printf("%d ", sa[i]);
    
      return 0;
    }
    ```

### Pristup O(n)

U uobičajenim zadacima računanje sufiksnog polja udvostručavanjem s malom konstantom sasvim je dovoljno; i ostali dijelovi rješenja često imaju složenost $O(n\log n)$, pa udvostručavanje nije usko grlo.

No ako naiđete na posebne zadatke, zadatke sa strogim vremenskim ograničenjem ili želite još kraće vrijeme izvođenja, trebate naučiti metode računanja sufiksnog polja u $O(n)$.

#### SA-IS

Pogledajte [Inducirano sortiranje i algoritam SA-IS](https://riteme.site/blog/2016-6-19/sais.html); vrijedna je i [stranica s komentarima](https://github.com/riteme/riteme.github.io/issues/28).

#### DC3

Pogledajte [\[2009\] Sufiksno polje – moćan alat za obradu stringova, Luo Suiqian][2].

## Primjene sufiksnog polja

### Pronalaženje najmanjeg cikličkog pomaka

Kopiranjem stringa $S$ u $SS$ problem se svodi na sufiksno sortiranje.

Primjer: [„JSOI2007” Šifriranje znakova](https://www.luogu.com.cn/problem/P4051).

### Traženje podstringa u stringu

Zadatak je online tražiti uzorak $S$ u tekstu $T$. Online znači da tekst $T$ znamo unaprijed, a uzorak $S$ saznajemo tek pri upitu. Možemo najprije izgraditi sufiksno polje od $T$, a zatim tražiti podstring $S$. Ako se podstring $S$ pojavljuje u $T$, nužno je prefiks nekih sufiksa od $T$. Budući da smo sve sufikse već sortirali, to možemo postići binarnim pretraživanjem $S$ u polju $p$. Usporedba podstringa $S$ s trenutnim sufiksom ima složenost $O(|S|)$, pa je složenost traženja podstringa $O(|S|\log |T|)$. Uočimo: ako se podstring pojavljuje u $T$ više puta, sva su pojavljivanja susjedna u polju $p$. Stoga broj pojavljivanja možemo pronaći još jednim binarnim pretraživanjem, a lako je ispisati i poziciju svakog pojavljivanja.

### Uzimanje znakova s početka i kraja stringa uz minimalni leksikografski poredak

Primjer: [„USACO07DEC” Best Cow Line](https://www.luogu.com.cn/problem/P2870).

Zadatak: zadan je string; svaki put uzimamo jedan znak s početka ili kraja i slažemo novi string. Koji je od svih stringova koje tako možemo složiti leksikografski najmanji?

??? note "Rješenje"
    Naivni pristup u najgorem slučaju u $O(n)$ odlučuje treba li uzeti s početka ili s kraja (tj. uspoređuje string dobiven uzimanjem s početka s obratom stringa dobivenog uzimanjem s kraja); dovoljno je optimirati samo tu odluku.
    
    Budući da treba uspoređivati unutar skupa sufiksa izvornog stringa i sufiksa obrnutog stringa, obrnuti string možemo nadovezati na izvorni, a između umetnuti znak koji se ne pojavljuje (npr. `#`; u kodu se može izravno upotrijebiti prazni znak), izračunati sufiksno polje i tu odluku donijeti u $O(1)$.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/string/code/sa/sa_1.cpp"
    ```

## Polje height

### LCP (najdulji zajednički prefiks)

LCP dvaju stringova $S$ i $T$ najveći je $x$ ($x\le \min(|S|, |T|)$) takav da je $S_i=T_i\ (\forall\ 1\le i\le x)$.

U nastavku $lcp(i,j)$ označava (duljinu) najduljeg zajedničkog prefiksa sufiksa $i$ i sufiksa $j$.

### Definicija polja height

$height[i]=lcp(sa[i],sa[i-1])$, tj. najdulji zajednički prefiks $i$-tog sufiksa po rangu i sufiksa neposredno ispred njega.

$height[1]$ možemo smatrati $0$.

### Lema potrebna za računanje polja height u O(n)

$height[rk[i]]\ge height[rk[i-1]]-1$

???+ note "Dokaz"
    Kad je $height[rk[i-1]]\le1$, nejednakost očito vrijedi (desna je strana manja ili jednaka $0$).
    
    Kad je $height[rk[i-1]]>1$:
    
    po definiciji $height$ vrijedi $lcp(sa[rk[i-1]], sa[rk[i-1]-1]) = height[rk[i-1]] > 1$.
    
    Budući da sufiks $i-1$ i sufiks $sa[rk[i-1]-1]$ imaju najdulji zajednički prefiks duljine $height[rk[i-1]]$,
    
    označimo taj najdulji zajednički prefiks s $aA$. (Pritom je $a$ jedan znak, a $A$ neprazan string duljine $height[rk[i-1]]-1$.)
    
    Tada sufiks $i-1$ možemo zapisati kao $aAD$, a sufiks $sa[rk[i-1]-1]$ kao $aAB$. ($B < D$, $B$ može biti prazan, $D$ je neprazan.)
    
    Nadalje, sufiks $i$ možemo zapisati kao $AD$, a postoji i sufiks ($sa[rk[i-1]-1]+1$) $AB$.
    
    Budući da je sufiks $sa[rk[i]-1]$ po rangu točno za jedno mjesto manji od sufiksa $sa[rk[i]]$, tj. sufiksa $i$, a $AB < AD$,
    
    vrijedi $AB \leqslant$ sufiks $sa[rk[i]-1] < AD$, pa sufiks $i$ i sufiks $sa[rk[i]-1]$ očito imaju zajednički prefiks $A$.
    
    Iz toga slijedi da je $lcp(i,sa[rk[i]-1])$ barem $height[rk[i-1]]-1$, tj. $height[rk[i]]\ge height[rk[i-1]]-1$.

### Implementacija računanja polja height u O(n)

Dovoljno je računati izravno koristeći gornju lemu:

```cpp
for (i = 1, k = 0; i <= n; ++i) {
  if (rk[i] == 0) continue;
  if (k) --k;
  while (s[i + k] == s[sa[rk[i] - 1] + k]) ++k;
  height[rk[i]] = k;
}
```

$k$ ne premašuje $n$ i smanjuje se najviše $n$ puta, pa se povećava najviše $2n$ puta; ukupna je složenost $O(n)$.

## Primjene polja height

### Najdulji zajednički prefiks dvaju podstringova

$lcp(sa[i],sa[j])=\min\{height[i+1..j]\}$

Intuitivno: ako je $height$ cijelo vrijeme veći od nekog broja, prvih toliko znakova nikad se nije promijenilo; obrnuto, budući da su sufiksi već sortirani, nije moguće da se nakon promjene vrate na staro.

Strogi dokaz vidi u [\[2004\] Sufiksno polje, Xu Zhilei][1].

S ovim teoremom računanje najduljeg zajedničkog prefiksa dvaju podstringova svodi se na [problem RMQ](../topic/rmq.md).

### Usporedba dvaju podstringova istog stringa

Pretpostavimo da treba usporediti $A=S[a..b]$ i $B=S[c..d]$.

Ako je $lcp(a, c)\ge\min(|A|, |B|)$, onda $A<B\iff |A|<|B|$.

Inače $A<B\iff rk[a]< rk[c]$.

### Broj različitih podstringova

Podstring je prefiks nekog sufiksa, pa možemo proći sve sufikse, izračunati ukupan broj prefiksa i oduzeti ponavljanja.

„Ukupan broj prefiksa” zapravo je broj podstringova, $n(n+1)/2$.

Ako sufikse obilazimo u redoslijedu sufiksnog sortiranja, novi podstringovi koje svaki put dodajemo prefiksi su koji preostaju nakon LCP-a s prethodnim sufiksom. Ti su prefiksi sigurno novi, inače bi bilo narušeno svojstvo $lcp(sa[i],sa[j])=\min\{height[i+1..j]\}$. Novi su samo ti prefiksi, jer je dio LCP-a izbrojen pri obilasku prethodnog sufiksa.

Odgovor je stoga:

$\frac{n(n+1)}{2}-\sum\limits_{i=2}^nheight[i]$

### Najveća duljina podstringa koji se pojavljuje barem k puta

Primjer: [„USACO06DEC” Milk Patterns](https://www.luogu.com.cn/problem/P2852).

??? note "Rješenje"
    Pojavljivanje barem $k$ puta znači da nakon sufiksnog sortiranja barem $k$ uzastopnih sufiksa ima taj podstring kao zajednički prefiks.
    
    Stoga je odgovor maksimum minimuma svakih $k-1$ susjednih vrijednosti $height$.
    
    To se može riješiti monotonim redom u $O(n)$, ali i drugi su pristupi dovoljni za AC.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/string/code/sa/sa_2.cpp"
    ```

### Pojavljuje li se neki string u tekstu barem dvaput bez preklapanja

Možemo binarno pretraživati duljinu ciljnog stringa $|s|$, podijeliti polje $h$ na segmente uzastopnih LCP-ova većih ili jednakih $|s|$ i pomoću RMQ-a za svaki segment pronaći najveći i najmanji indeks koji se u njemu pojavljuje; ako udaljenost tih dvaju indeksa zadovoljava uvjet, sigurno postoji string duljine $|s|$ koji se pojavljuje dvaput bez preklapanja.

### Više uzastopnih jednakih podstringova

Možemo iterirati po duljini ponavljajućeg stringa $|s|$, podijeliti cijeli string na blokove po $|s|$ i za početke dvaju susjednih blokova postaviti upite LCP i LCS; detalje vidi u [\[2009\] Sufiksno polje – moćan alat za obradu stringova][2].

Primjer: [„NOI2016” Izvrsna podjela](https://loj.ac/p/2083).

### U kombinaciji s unijom-pronalaženjem (DSU)

Neki zadaci traže da sufiksno polje podijelite na segmente u kojima su uzastopne duljine LCP-a veće ili jednake nekoj vrijednosti, tj. da polje $h$ podijelite na segmente čiji je minimum veći ili jednak nekoj vrijednosti, i da za svaki segment izračunate odgovor. Ako ima više upita, možemo ih obraditi offline. Uočavamo da je, kako zadana vrijednost monotono pada, broj segmenata koji zadovoljavaju uvjet sve manji, a novi segmenti nastaju spajanjem dvaju ili više starih; dijelovi novog segmenta koji nisu u starim segmentima imaju $h$ jednak upravo toj vrijednosti. Dovoljno je održavati strukturu unija-pronalaženje, svaki put spojiti dva susjedna segmenta i održavati statistiku.

Klasičan zadatak: [„NOI2015” Degustacija vina](https://uoj.ac/problem/131)

### U kombinaciji sa segment tree-om

Neki zadaci traže prvih nekoliko brojeva koji zadovoljavaju uvjet, a ti se brojevi nalaze unutar jednog intervala sufiksnog sortiranja. Tada možemo svojstvom merge sorta spajati informacije dvaju čvorova, a segment tree-om održavati i dohvaćati odgovor za interval.

### U kombinaciji s monotonim stogom

Primjer: [„AHOI2013” Razlika](https://loj.ac/problem/2377)

??? note "Rješenje"
    Prva dva pribrojnika lako se obrađuju: iznose $n(n-1)(n+1)/2$ (svaki se sufiks pojavljuje $n-1$ puta, a ukupna duljina sufiksa je $n(n+1)/2$); ključan je posljednji član, tj. LCP svih parova sufiksa.
    
    Znamo da je $lcp(i,j)=k$ ekvivalentno s $\min\{height[i+1..j]\}=k$. Stoga $lcp(i,j)$ možemo pripisati kao doprinos odgovoru pozicije $\min\{x|i+1\le x\le j, height[x]=lcp(i,j)\}$.
    
    Razmotrimo kojih je sufiksa LCP doprinos svake pozicije odgovoru: zapravo biramo jedan sufiks među uzastopnim sufiksima ulijevo od nje s $height$ većim od njezinog i jedan među uzastopnim sufiksima udesno s $height$ ne manjim od njezinog. To se može izračunati [monotonim stogom](../ds/monotonic-stack.md).
    
    Dio s monotonim stogom sličan je zadatku [Luogu P2659 Lijepi niz](https://www.luogu.com.cn/problem/P2659) i [metodi visećih linija](../misc/hoverline.md).

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/string/code/sa/sa_3.cpp"
    ```

Sličan zadatak: [„HAOI2016” Pronađi jednake znakove](https://loj.ac/problem/2064).

## Zadaci

-   [UVa 760 - DNA Sequencing](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=701)
-   [UVa 1223 - Editor](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3664)
-   [Codechef - Tandem](https://www.codechef.com/problems/TANDEM)
-   [Codechef - Substrings and Repetitions](https://www.codechef.com/problems/ANUSAR)
-   [Codechef - Entangled Strings](https://www.codechef.com/problems/TANGLED)
-   [Codeforces - Martian Strings](http://codeforces.com/problemset/problem/149/E)
-   [Codeforces - Little Elephant and Strings](http://codeforces.com/problemset/problem/204/E)
-   [SPOJ - Ada and Terramorphing](http://www.spoj.com/problems/ADAPHOTO/)
-   [SPOJ - Ada and Substring](http://www.spoj.com/problems/ADASTRNG/)
-   [UVa - 1227 - The longest constant gene](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3668)
-   [SPOJ - Longest Common Substring](http://www.spoj.com/problems/LCS/en/)
-   [UVa 11512 - GATTACA](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2507)
-   [QOJ 11240 - Suffixes and Palindromes](https://qoj.ac/problem/11240)
-   [GYM - Por Costel and the Censorship Committee](http://codeforces.com/gym/100923/problem/D)
-   [UVa 1254 - Top 10](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3695)
-   [UVa 12191 - File Recover](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3343)
-   [UVa 12206 - Stammering Aliens](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3358)
-   [Codechef - Jarvis and LCP](https://www.codechef.com/problems/INSQ16F)
-   [Luogu P8617 - Ponavljajući uzorak](https://www.luogu.com.cn/problem/P8617)
-   [UVa 11107 - Life Forms](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2048)
-   [UVa 12974 - Exquisite Strings](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4853)
-   [UVa 10526 - Intellectual Property](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1467)
-   [UVa 12338 - Anti-Rhyme Pairs](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3760)
-   [DevSkills Reconstructing Blue Print of Life](https://devskill.com/CodingProblems/ViewProblem/328)
-   [UVa 12191 - File Recover](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3343)
-   [SPOJ - Suffix Array](http://www.spoj.com/problems/SARRAY/)
-   [Gym 102470J - Stammering Aliens](https://codeforces.com/gym/102470/problem/J)
-   [SPOJ - LCS2](http://www.spoj.com/problems/LCS2/)
-   [Codeforces - Fake News (hard)](http://codeforces.com/contest/802/problem/I)
-   [SPOJ - Longest Commong Substring](http://www.spoj.com/problems/LONGCS/)
-   [SPOJ - Lexicographical Substring Search](http://www.spoj.com/problems/SUBLEX/)
-   [Codeforces - Forbidden Indices](http://codeforces.com/contest/873/problem/F)
-   [Codeforces - Tricky and Clever Password](http://codeforces.com/contest/30/problem/E)
-   [Gym 101470B - Circle of digits](https://codeforces.com/gym/101470/problem/B)

## Literatura

Ova stranica (dio uveden u [4070a9b](https://github.com/OI-wiki/OI-wiki/pull/950/commits/4070a9b3db8576db16c74d3ec33806ad10476eef)) uglavnom je prevedena iz članka [Суффиксный массив](http://e-maxx.ru/algo/suffix_array) i njegova engleskog prijevoda [Suffix Array](https://cp-algorithms.com/string/suffix-array.html). Ruska je verzija pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.

Radovi:

1.  [\[2004\] Sufiksno polje, Xu Zhilei][1]

2.  [\[2009\] Sufiksno polje – moćan alat za obradu stringova, Luo Suiqian][2]

[1]: https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2004%E8%AE%BA%E6%96%87%E9%9B%86/%E8%AE%B8%E6%99%BA%E7%A3%8A--%E5%90%8E%E7%BC%80%E6%95%B0%E7%BB%84.pdf "[2004] Sufiksno polje, Xu Zhilei"

[2]: https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2009%E8%AE%BA%E6%96%87%E9%9B%86/11.%E7%BD%97%E7%A9%97%E9%AA%9E%E3%80%8A%E5%90%8E%E7%BC%80%E6%95%B0%E7%BB%84%E2%80%94%E2%80%94%E5%A4%84%E7%90%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%9C%89%E5%8A%9B%E5%B7%A5%E5%85%B7%E3%80%8B/%E5%90%8E%E7%BC%80%E6%95%B0%E7%BB%84%E2%80%94%E2%80%94%E5%A4%84%E7%90%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%9C%89%E5%8A%9B%E5%B7%A5%E5%85%B7.pdf "[2009] Sufiksno polje – moćan alat za obradu stringova, Luo Suiqian"
