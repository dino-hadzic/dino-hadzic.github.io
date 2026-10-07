---
title: Virtualno stablo
---

## Uvod

???+ note "[„SDOI2011” Rat iscrpljivanja](https://www.luogu.com.cn/problem/P2495)"
    U jednom ratu bojište se sastoji od $n$ otoka i $n-1$ mostova, pri čemu je zajamčeno da između svaka dva otoka postoji točno jedan put. Naša je vojska izvidjela da je neprijateljski stožer na otoku s brojem $1$ i da neprijatelj više nema dovoljno energije za nastavak borbe; pobjeda je blizu. Poznato je da na drugih $k$ otoka ima obilje energije; kako neprijatelj ne bi došao do energije, zadatak je naše vojske srušiti neke mostove tako da neprijatelj ne može doći ni do jednog energetski bogatog otoka. Budući da se mostovi razlikuju materijalom i konstrukcijom, rušenje različitih mostova ima različitu cijenu, a naša vojska želi postići cilj uz najmanju ukupnu cijenu.
    
    Izvidnica je otkrila i da neprijatelj ima tajanstveni stroj. Čak i nakon što mu odsiječemo svu energiju, on može upotrijebiti taj stroj. Učinak stroja nije samo popravak svih mostova koje smo srušili, nego i nova slučajna raspodjela resursa (uz jamstvo da resursi neće biti na otoku broj $1$). No izvidnica je otkrila i da se stroj može upotrijebiti samo $m$ puta, pa je dovoljno izvršiti svaki zadatak zasebno.
    
    Za sve podatke vrijedi $2\le n\le 2.5\times 10^5,1\le m\le 5\times 10^5,\sum k_i\le 5\times 10^5,1\le k_i\le n-1$.

### Naivni pristup

Za gornji zadatak lako uočavamo: ako je broj čvorova stabla mali, možemo izravno pokrenuti DP.

Najprije čvorove odabrane u nekom upitu nazovimo **„ključnim čvorovima”**.

Neka $Dp(i)$ označava **najmanju cijenu** da $i$ ne bude povezan ni s jednim ključnim čvorom u svom podstablu.

Neka $w(a,b)$ označava težinu brida između $a$ i $b$.

Tada za svako dijete $v$ čvora $i$:

-   ako $v$ nije ključni čvor: $Dp(i)=Dp(i) + \min \{Dp(v),w(i,v)\}$;
-   ako $v$ jest ključni čvor: $Dp(i)=Dp(i) + w(i,v)$.

Odlično, tako dobivamo kôd složenosti $O(nq)$.

Zvuči zanimljivo.

### Optimizirani pristup

Lako uočavamo da je zapravo mnogo čvorova beskorisno. Uzmimo za primjer sliku:

![vtree-1](images/vtree-tree.svg)

Ako su odabrani ključni čvorovi:

![vtree-2](images/vtree-key-vertex.svg)

Na slici su samo dva crvena čvora **ključni čvorovi**, a svi ostali su „neključni čvorovi”.

Za ovaj zadatak dovoljno je osigurati da crveni čvorovi ne mogu doći do čvora $1$.

Promatranjem golim okom zaključujemo: desno podstablo čvora $1$ (iako podstabala može biti više, ovdje su samo dva pa ćemo ga privremeno tako zvati) nema nijedan crveni čvor, **pa nema potrebe raditi DP po njemu**.

Pogledamo li uvjete zadatka, ukupan broj crvenih (ključnih) čvorova istog je reda kao $n$, odnosno u jednom su upitu crveni čvorovi vrlo rijetki u odnosu na cijelo stablo; bilo bi lijepo kad bi složenost ovisila o ukupnom broju crvenih čvorova.

Stoga trebamo **sažeti informacije, cijelo veliko stablo sažeti u malo stablo**.

## Virtualno stablo (Virtual Tree)

Time dolazimo do pojma **„virtualnog stabla”**.

Pogledajmo najprije intuitivno kako virtualno stablo izgleda.

Na slikama u nastavku crveni su čvorovi odabrani ključni čvorovi. Crveni i crni čvorovi su čvorovi virtualnog stabla. Crni bridovi su bridovi virtualnog stabla.

![vtree-3](images/vtree-vtree1.svg)

![vtree-4](images/vtree-vtree2.svg)

![vtree-5](images/vtree-vtree3.svg)

![vtree-6](images/vtree-vtree4.svg)

Budući da i LCA bilo koja dva ključna čvora nosi važne informacije, treba sačuvati i njihove LCA-ove; stoga virtualno stablo ne sadrži nužno samo ključne čvorove.

Lako se vidi da se odnosi predak–potomak u virtualnom stablu ne mijenjaju. (Dakle, ne može se dogoditi nešto čudno poput toga da je $a$ izvorno bio predak od $b$, a poslije $a$ postane potomak od $b$.)

No ne možemo LCA-ove nabrajati grubo u $O(k^2)$, pa se lako dosjetimo: najprije ključne čvorove sortiramo po DFS poretku, a zatim za svaka dva susjedna ključna čvora (susjedna znači da im se indeksi u sortiranom nizu razlikuju za 1) izračunamo LCA i dodamo ga u virtualno stablo.

Sada je ključno pitanje kako konstruirati virtualno stablo.

Prije nego što predložimo postupak, utvrdimo jednu činjenicu: u virtualno stablo možemo po volji dodavati čvorove, dok god se odnosi predak–potomak ne mijenjaju.

Drugim riječima, kad bismo htjeli, mogli bismo sve čvorove izvornog stabla dodati u virtualno stablo i ne bismo dobili WA (iako bismo dobili TLE).

Stoga radi jednostavnosti možemo najprije dodati čvor $1$ u virtualno stablo, a to ne utječe na odgovor.

### Prvi postupak konstrukcije: dvostruko sortiranje + spajanje preko LCA

Budući da LCA više čvorova može biti isti čvor, ne smijemo ga više puta dodati u virtualno stablo.

Vrlo intuitivan postupak je:

-   sortiramo ključne čvorove po DFS poretku;
-   prođemo niz, za svaka dva susjedna ključna čvora izračunamo LCA i uklonimo duplikate;
-   zatim izgradimo stablo prema odnosima predak–potomak u izvornom stablu.

Konkretno, u **nizu ključnih čvorova** nabrajamo **svaka dva susjedna elementa**, računamo njihov LCA i dodajemo ga u niz $A$.

Zbog svojstava DFS poretka niz $A$ tada već sadrži **sve čvorove virtualnog stabla**, ali možda s ponavljanjima.

Zato niz $A$ **sortiramo uzlazno po DFS poretku i uklonimo duplikate**.

Na kraju u nizu $A$ nabrajamo **susjedne** parove **indeksa čvorova** $x,y$, izračunamo njihov LCA i spojimo $\operatorname{LCA}(x,y),y$; time je virtualno stablo izgrađeno.

Zašto spajanje $\operatorname{LCA}(x,y)$ i $y$ ne ispušta ništa i ne udvostručuje ništa?

??? note "Dokaz"
    Ako je $x$ predak od $y$, $x$ se izravno spaja s $y$. Budući da DFS poredak jamči da su DFS indeksi od $x$ i $y$ susjedni, na putu od $x$ do $y$ nema ključnih čvorova.
    
    Ako $x$ nije predak od $y$, uzmemo $\operatorname{LCA}(x,y)$ kao pretka od $y$; prema prethodnom slučaju može se dokazati i da na putu od $\operatorname{LCA}(x,y)$ do $y$ nema ključnih čvorova.
    
    Stoga spajanje $\operatorname{LCA}(x,y)$ i $y$ ništa ne ispušta niti udvostručuje.
    
    Osim toga, smeta li što prvi čvor nije spojen ni s jednim čvorom? Budući da je prvi čvor sigurno korijen stabla, ne smeta, pa je ukupan broj bridova $m-1$.

Budući da su potrebna barem dva stvarna čvora da bi se „prizvao” jedan virtualni čvor, plus jedan korijenski čvor, broj čvorova virtualnog stabla najviše je dvostruki broj stvarnih čvorova.

Vremenska složenost $O(m\log n)$, gdje je $m$ broj ključnih čvorova, a $n$ ukupan broj čvorova.

#### Implementacija

```cpp
int dfn[MAXN];
int h[MAXN], m, a[MAXN], len;  // pohrana ključnih čvorova

bool cmp(int x, int y) {
  return dfn[x] < dfn[y];  // sortiranje po dfs poretku
}

void build_virtual_tree() {
  sort(h + 1, h + m + 1, cmp);  // sortiraj ključne čvorove po dfs poretku
  for (int i = 1; i < m; ++i) {
    a[++len] = h[i];
    a[++len] = lca(h[i], h[i + 1]);  // umetni lca
  }
  a[++len] = h[m];
  sort(a + 1, a + len + 1, cmp);  // sortiraj sve čvorove virtualnog stabla po dfs poretku
  len = unique(a + 1, a + len + 1) - a - 1;  // ukloni duplikate
  for (int i = 1, lc; i < len; ++i) {
    lc = lca(a[i], a[i + 1]);
    conn(lc, a[i + 1]);  // spoji bridom; ako postoje težine, težina je distance(lc,a[i+1])
  }
}
```

To je zapravo dovoljno za konstrukciju virtualnog stabla.

### Drugi postupak konstrukcije: monotoni stog

Kako konstruirati virtualno stablo monotonim stogom?

Najprije razjasnimo cilj: monotonim stogom održavamo jedan lanac virtualnog stabla.

Drugim riječima, dva susjedna čvora u stogu susjedna su i u virtualnom stablu, a stog je od dna prema vrhu monotono rastući (misli se da DFS indeksi čvorova u stogu monotono rastu); jednostavno rečeno, roditelj nekog čvora je čvor ispod njega u stogu.

Najprije u stog dodamo čvor $1$.

Zatim ključne čvorove dodajemo po rastućem DFS poretku.

Ako je LCA trenutačnog čvora i vrha stoga upravo vrh stoga, oni su na istom lancu. Stoga trenutačni čvor jednostavno stavimo na stog.

![vtree-7](./images/vtree-add1.svg)

Ako LCA trenutačnog čvora i vrha stoga nije vrh stoga:

![vtree-8](./images/vtree-add2.svg)

Tada je lanac koji monotoni stog trenutačno održava:

![vtree-9](./images/vtree-add3.svg)

a trebamo lanac pretvoriti u:

![vtree-10](./images/vtree-add4.svg)

Dakle, čvorove označene isprekidanom linijom skinemo sa stoga; prije skidanja ne zaboravimo spojiti ih bridom s njihovim roditeljem u virtualnom stablu.

![vtree-11](./images/vtree-add5.svg)

Ako nakon skidanja vrh stoga nije LCA, LCA stavimo na stog.

Zatim stavimo na stog trenutačni čvor.

Slijedi konkretan primjer. Pretpostavimo da za čvorove 4, 6 i 7 sljedećeg stabla gradimo virtualno stablo:

![vtree-12](./images/vtree-construction1.svg)

Koraci su sljedeći:

-   Sortiramo 3 ključna čvora $6,4,7$ po DFS poretku i dobijemo niz $[4,6,7]$.
-   Stavimo $1$ na stog.

![vtree-13](./images/vtree-construction2.svg)

Crveni čvorovi označavaju čvorove u stogu, a tirkizni čvorove skinute sa stoga.

-   Uzmemo prvi element niza kao trenutačni čvor, dakle $4$. Uzmemo vrh stoga, $1$. Izračunamo LCA od $1$ i $4$: $LCA(1,4)=1$.
-   Vidimo da je $LCA(1,4)=$ vrh stoga, dakle na istom su lancu virtualnog stabla, pa trenutačni čvor $4$ jednostavno stavimo na stog; stog je sada $4,1$.

![vtree-14](./images/vtree-construction3.svg)

-   Uzmemo drugi element niza kao trenutačni čvor, $6$. Uzmemo vrh stoga, $4$. Izračunamo LCA od $6$ i $4$: $LCA(6,4)=1$.
-   Vidimo da je $LCA(6,4)\neq$ vrh stoga, ulazimo u fazu provjere.
-   Faza provjere: DFS indeks vrha stoga $4$ veći je od $LCA(6,4)$, ali DFS indeks drugog najvećeg čvora (onog ispod vrha stoga) $1$ jednak je LCA-u (jednaki DFS indeksi zapravo znače jednake čvorove), što znači da je LCA već na stogu; zato izravno spojimo brid $1\to4$, odnosno brid od LCA-a do vrha stoga. I skinemo $4$ sa stoga.

![vtree-15](./images/vtree-construction4.svg)

-   Nakon faze provjere stavimo $6$ na stog; stog je sada $6,1$.

![vtree-16](./images/vtree-construction5.svg)

-   Uzmemo treći element niza kao trenutačni čvor, $7$. Uzmemo vrh stoga, $6$. Izračunamo LCA od $7$ i $6$: $LCA(7,6)=3$.
-   Vidimo da je $LCA(7,6)\neq$ vrh stoga, ulazimo u fazu provjere.
-   Faza provjere: DFS indeks vrha stoga $6$ veći je od $LCA(7,6)$, ali DFS indeks drugog najvećeg čvora (onog ispod vrha stoga) $1$ manji je od LCA-a, što znači da LCA još nije bio na stogu; zato izravno spojimo brid $3\to6$, odnosno brid od LCA-a do vrha stoga. Skinemo $6$ sa stoga i stavimo $LCA(6,7)$ na stog.
-   Nakon faze provjere stavimo $7$ na stog; stog je sada $1,3,7$.

![vtree-17](./images/vtree-construction6.svg)

-   Sva 3 čvora niza već su bila na stogu, izlazimo iz petlje.
-   U stogu su još 3 čvora: $1,3,7$; očito su na istom lancu, pa ih izravno spojimo bridovima $1\to3$ i $3\to7$.
-   Virtualno stablo je izgrađeno!

![vtree-18](./images/vtree-construction7.svg)

Uklonimo li zatim čvorove koji nikad nisu bili na stogu (netirkizne čvorove), odgovarajuće virtualno stablo izgleda ovako:

![vtree-19](./images/vtree-construction8.svg)

Ima mnogo detalja; primjerice, ako virtualno stablo pohranjujemo listom susjedstva, listu treba isprazniti. No pražnjenje cijele liste susjedstva vrlo je sporo, pa **ispraznimo listu susjedstva elementa u trenutku kad element koji nikad nije bio na stogu prvi put stavljamo na stog**.

Vremenska složenost također je $O(m\log n)$ (zbog sortiranja), gdje je $m$ broj ključnih čvorova, a $n$ ukupan broj čvorova.

#### Implementacija

C++ kôd za konstrukciju virtualnog stabla izgleda otprilike ovako:

???+ note "Implementacija"
    ```cpp
    bool cmp(const int x, const int y) { return id[x] < id[y]; }
    
    void build() {
      sort(h + 1, h + k + 1, cmp);
      sta[top = 1] = 1, g.sz = 0, g.head[1] = -1;
      // čvor 1 na stog, isprazni listu susjedstva čvora 1, postavi broj bridova liste na 0
      for (int i = 1, l; i <= k; ++i)
        if (h[i] != 1) {
          // ako je čvor 1 ključni čvor, ne dodaj ga ponovno
          l = lca(h[i], sta[top]);
          // izračunaj LCA trenutačnog čvora i vrha stoga
          if (l != sta[top]) {
            // ako se LCA razlikuje od vrha stoga, trenutačni čvor nije na lancu koji stog trenutačno čuva
            while (id[l] < id[sta[top - 1]])
              // dok je Dfs indeks drugog najvećeg čvora veći od Dfs indeksa LCA-a
              g.push(sta[top - 1], sta[top]), top--;
            // spoji i skini lanac koji se ne preklapa s lancem trenutačnog čvora
            if (id[l] > id[sta[top - 1]])
              // ako LCA nije jednak drugom najvećem čvoru (ovdje se „veće” ne razlikuje od „različito”)
              g.head[l] = -1, g.push(l, sta[top]), sta[top] = l;
            // LCA je prvi put na stogu: isprazni mu listu susjedstva, spoji brid, skini vrh stoga i stavi LCA
            // na stog
            else
              g.push(l, sta[top--]);
            // LCA je upravo drugi najveći čvor, samo skini vrh stoga
          }
          g.head[h[i]] = -1, sta[++top] = h[i];
          // trenutačni čvor sigurno je prvi put na stogu: isprazni listu susjedstva i stavi ga na stog
        }
      for (int i = 1; i < top; ++i)
        g.push(sta[i], sta[i + 1]);  // spoji preostali posljednji lanac
      return;
    }
    ```

Tako smo naučili graditi virtualno stablo!

Za zadatak Rat iscrpljivanja dovoljno je na virtualnom stablu pokrenuti DP s početka; virtualnim stablom smo zapravo izbacili beskorisne neključne čvorove! I dalje promatramo svu djecu $v$ čvora $i$:

-   ako $v$ nije ključni čvor: $Dp(i)=Dp(i) + \min \{Dp(v),w(i,v)\}$
-   ako $v$ jest ključni čvor: $Dp(i)=Dp(i) + w(i,v)$

I tako je zadatak lako riješen.

## Preporučeni zadaci

-   [„SDOI2011” Rat iscrpljivanja](https://www.luogu.com.cn/problem/P2495)
-   [„HEOI2014” Veliki projekt](https://www.luogu.com.cn/problem/P4103)
-   [CF613D Kingdom and its Cities](http://codeforces.com/contest/613/problem/D/)
-   [„HNOI2014” Svjetsko stablo](https://www.luogu.com.cn/problem/P3233)
