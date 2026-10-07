---
title: Operacije intervalnog min/max i povijesni ekstremi intervala
---

Ovaj članak objašnjava problem održavanja povijesnih ekstrema intervala segment treeom, koji je Ji Ruyi (吉老师) opisao u [radu kineske nacionalne pripremne ekipe 2016.](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2016%E8%AE%BA%E6%96%87%E9%9B%86.pdf).

## Intervalni ekstremi

Općenito govoreći, operacija intervalnog ekstrema znači da se svi brojevi u intervalu $[l,r]$ zamijene svojim $\max$ ili $\min$ s $x$, tj. $a_i=\max(a_i,x)$ ili $a_i=\min(a_i,x)$.

???+ note "[HDU5306 Gorgeous Sequence](https://acm.hdu.edu.cn/showproblem.php?pid=5306)"
    Održavaj niz $a$ i izvodi sljedeće operacije:
    
    1.  `0 l r t` $\forall l\le i\le r,~ a_i=\min(a_i,t)$.
    2.  `1 l r` ispiši $\max\limits_{i=l}^r a_i$.
    3.  `2 l r` ispiši $\sum\limits_{i=l}^r a_i$.
    
    Više testnih primjera; vrijedi $T\le 100,~\sum n,\sum m\le 10^6$.

Intervalno uzimanje $\min$ znači da se mijenjaju samo brojevi veći od $t$. Dakle, objekt te operacije više nije cijeli interval, nego „brojevi u intervalu veći od $t$”. Odatle ideja: svaki čvor održava maksimum intervala $Max$, drugi najveći element $Se$, zbroj intervala $Sum$ i broj maksimuma $Cnt$. Promotrimo sada operaciju uzimanja $\min$ s $t$ na intervalu.

1.  Ako je $Max\le t$, $t$ očito nema učinka; odmah se vraćamo.
2.  Ako je $Se<t < Max$, $t$ mijenja upravo maksimum trenutnog intervala. Zato zbroju intervala dodamo $Cnt(t-Max)$, zatim $Max$ postavimo na $t$ i postavimo oznaku.
3.  Ako je $t\le Se$, ne znamo koliko je brojeva zahvaćeno izmjenom. Strategija je tada: silom (brute force) rekurzivno siđemo i izvedemo operaciju, a zatim informacije prenesemo prema gore.

Kolika je složenost tog algoritma? Analizom potencijala dobiva se složenost $O(m\log n)$. Detaljna analiza nalazi se u radu.

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_1.cpp"
```

???+ note "[BZOJ4695 最假女选手](https://loj.ac/p/6565)"
    Održavaj niz $a$ i izvodi sljedeće operacije:
    
    1.  `1 l r x` $\forall l\le i\le r,~ a_i=a_i+x$.
    2.  `2 l r x` $\forall l\le i\le r,~ a_i=\max(a_i,x)$.
    3.  `3 l r x` $\forall l\le i\le r,~ a_i=\min(a_i,x)$.
    4.  `4 l r` ispiši $\sum\limits_{i=l}^r a_i$.
    5.  `5 l r` ispiši $\max\limits_{i=l}^r a_i$.
    6.  `6 l r` ispiši $\min\limits_{i=l}^r a_i$.
    
    $n,m\le 5\times 10^5,~|a_i|\le 10^8$. Za sve operacije tipa $1$ vrijedi $|x|\le 10^3$, za ostale $|x|\le10^8$.

Istom metodom održavamo maksimum, drugi najveći, broj maksimuma, minimum, drugi najmanji, broj minimuma i zbroj intervala. Osim tih informacija trebamo održavati i oznake za intervalni $\max$, intervalni $\min$ i intervalno zbrajanje. U odnosu na prethodni zadatak, tu se pojavljuje pitanje redoslijeda spuštanja oznaka. Koristimo ovu strategiju:

1.  Oznaka intervalnog zbrajanja ima najviši prioritet, a ostale dvije oznake su ravnopravne.
2.  Kad čvoru dodajemo oznaku zbrajanja $v$, osim što s $v$ ažuriramo pomoćne informacije i oznaku intervalnog zbrajanja trenutnog čvora, s tim $v$ ažuriramo i oznake intervalnog $\max$ i intervalnog $\min$.
3.  Kad na čvoru uzimamo $\min$ s $v$ (zanemarujemo postupak pretraživanja silom i pretpostavljamo da oznaka zadovoljava uvjet za postavljanje), osim ažuriranja pomoćnih informacija uspoređujemo $v$ s oznakom intervalnog $\max$. Ako je $v$ manji od oznake intervalnog $\max$, svi će brojevi na kraju postati $v$, pa i oznaku intervalnog $\max$ postavimo na $v$. Inače ništa.
4.  Intervalno uzimanje $\max$ s $v$ je analogno.

Pri održavanju informacija, kad interval ima samo jedan ili dva broja, skupovi se mogu preklapati – npr. isti broj može biti i maksimum i drugi najmanji – što treba posebno obraditi.

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_2.cpp"
```

Ji Ruyi je dokazao da je složenost ovog algoritma $O(m\log^2 n)$.

???+ note "Mzl loves segment tree"
    Dva niza $A,B$; na početku su svi brojevi u $B$ jednaki $0$. Operacije koje treba održavati:
    
    1.  intervalno uzimanje $\min$ na $A$;
    2.  intervalno uzimanje $\max$ na $A$;
    3.  intervalno zbrajanje na $A$;
    4.  upit za zbroj intervala u $B$.
    
    Nakon svake operacije, ako se vrijednost $A_i$ promijenila, $B_i$ se uveća za $1$. $n,m\le 3\times 10^5$.

Prvo promotrimo najjednostavniju operaciju – intervalno zbrajanje. Čim je $x\neq 0$, mijenjaju se svi brojevi u intervalu, pa je dovoljno na $B$ izvesti jedno intervalno zbrajanje.

Kod operacija intervalnog ekstrema uočavamo da postavljanje i spuštanje oznaka jedan-na-jedan odgovara nizu $B$. U biti, brojeve niza dijelimo u tri klase: maksimumi, minimumi i ne-ekstremi, i svaku održavamo zasebno (samo što konkretne skupove ekstrema ne gradimo eksplicitno, ali to ne smeta operacijama održavanja). Stoga pri postavljanju oznake usput ažuriramo informaciju u $B$ (pazite: ne postavljamo oznaku na $B$, nego ažuriramo informaciju!). Pri upitu pretražujemo $A$, a pri spuštanju oznaka usput ažuriramo informaciju u $B$. Kad nađemo tražene čvorove, vratimo informaciju iz $B$. Ta operacija u biti prepušta informaciju o ekstremima nizu $B$ na održavanje. Također i dalje treba obraditi preklapanje skupova.

???+ note "[CTSN loves segment tree](https://www.luogu.com.cn/problem/U180387)"
    Održavaj dva niza $a,b$ i izvodi sljedeće operacije:
    
    1.  `1 l r x` $\forall l\le i\le r,~ a_i=\min(a_i,x)$.
    2.  `2 l r x` $\forall l\le i\le r,~ b_i=\min(b_i,x)$.
    3.  `3 l r x` $\forall l\le i\le r,~ a_i=a_i+x$.
    4.  `4 l r x` $\forall l\le i\le r,~ b_i=b_i+x$.
    5.  `5 l r` ispiši $\max\limits_{i=l}^r (a_i+b_i)$.
    
    $n,m\le 3\times 10^5,~|a_i|,|b_i|,|x|\le 10^9$.

Kandidate za odgovor $A_i+B_i$ u intervalu $[l,r]$ dijelimo u četiri klase: ni $A_i$ ni $B_i$ nisu intervalni maksimumi nizova $A,B$; $A_i$ je intervalni maksimum niza $A$, ali $B_i$ nije intervalni maksimum niza $B$; $A_i$ nije intervalni maksimum niza $A$, ali $B_i$ je intervalni maksimum niza $B$; i $A_i$ i $B_i$ su intervalni maksimumi nizova $A,B$. Označimo ih redom $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$. Osim toga normalno održavamo intervalni maksimum i drugi najveći element nizova $A,B$. Obrada maksimuma i drugog najvećeg elementa od $A,B$ pri spuštanju oznaka intervalnog zbrajanja i $\min$ oznaka ista je kao u prethodna dva primjera. Oznaka $\min$ na $A$ utječe na $C_{1,1}$ i $C_{1,0}$, oznaka na $B$ utječe na $C_{1,1}$ i $C_{0,1}$. Zbrajanje na $A,B$ utječe na sve: $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$. Treba paziti samo na granične slučajeve kad $C_{0,0},C_{1,0},C_{0,1}$ ne postoje (npr. u intervalu $[i,i]$ postoje samo maksimumi od $A,B$ i $C_{1,1}$).

Zatim treba razmotriti kako pri pushupu održavati $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$. Nakon što ažuriramo maksimume od $A,B$, razmatramo jesu li maksimumi od $A,B$ u lijevom i desnom djetetu jednaki maksimumima od $A,B$ u trenutnom čvoru. Objašnjavamo na primjeru lijevog djeteta; desno se obrađuje analogno:

-   Kad su maksimumi od $A$ i $B$ u lijevom djetetu oba jednaki maksimumima od $A,B$ u trenutnom čvoru, $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ lijevog djeteta doprinose redom $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ trenutnog čvora.
-   Kad je maksimum od $A$ u lijevom djetetu jednak maksimumu od $A$ u trenutnom čvoru, ali maksimum od $B$ nije, $C_{1,0},C_{1,1}$ lijevog djeteta doprinose $C_{1,0}$ tog čvora, a $C_{0,0},C_{0,1}$ doprinose $C_{0,0}$ tog čvora.
-   Kad maksimum od $A$ u lijevom djetetu nije jednak maksimumu od $A$ u trenutnom čvoru, ali maksimum od $B$ jest, $C_{0,1},C_{1,1}$ lijevog djeteta doprinose $C_{0,1}$ tog čvora, a $C_{0,0},C_{1,0}$ doprinose $C_{0,0}$ tog čvora.
-   Kad ni maksimum od $A$ ni maksimum od $B$ u lijevom djetetu nisu jednaki maksimumima od $A,B$ u trenutnom čvoru, $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ lijevog djeteta doprinose samo $C_{0,0}$ tog čvora.

Rezultat upita nad intervalom je $\max(C_{0,0},C_{1,0},C_{0,1},C_{1,1})$.

Budući da treba istodobno održavati intervalni $\min$ i intervalno zbrajanje, složenost je i dalje $O(m\log^2 n)$.

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_4.cpp"
```

### Sažetak

U ovom smo poglavlju dali četiri primjera zadataka, u kojima smo redom objasnili održavanje osnovnih operacija intervalnog ekstrema, obradu prioriteta više oznaka, ideju klasifikacije skupova brojeva i održavanje više klasa. U biti, temeljna ideja obrade intervalnih ekstrema je klasificirano održavanje informacija o skupovima brojeva i njihovo učinkovito spajanje. U sljedećem poglavlju bavimo se problemima povijesnih ekstrema intervala.

## Problemi povijesnih ekstrema

### Povijesni ekstremi nisu perzistentnost

Napomena: problemi povijesnih ekstrema iz ovog poglavlja razlikuju se od tzv. perzistentnih struktura podataka. Tu posebnu klasu problema zovemo problemima povijesnih ekstrema. Dijele se u tri vrste.

#### Povijesni maksimum

Jednostavno rečeno, povijesni maksimum nekog položaja najveća je vrijednost koja se ikad pojavila na tom položaju. Formalno, definiramo pomoćni niz $B$, na početku jednak $A$. Nakon svake operacije na $A$ nad cijelim nizom uzimamo $\max$:

$$
\forall i\in[1,n],\ B_i=\max(B_i,A_i)
$$

Tada $B_i$ zovemo povijesnim maksimumom tog položaja.

#### Povijesni minimum

Definicija je slična povijesnom maksimumu: nakon svake operacije na $A$ nad cijelim nizom uzimamo $\min$. Tada $B_i$ zovemo povijesnim minimumom tog položaja.

#### Zbroj povijesnih verzija

Pomoćni niz $B$ na početku je sav $0$. Nakon svake operacije cijeli niz $A$ pribrajamo nizu $B$:

$$
\forall i\in[1,n], \ B_i=B_i+A_i
$$

$B_i$ zovemo zbrojem povijesnih verzija na položaju $i$.

U nastavku probleme povijesnih ekstrema dijelimo u četiri klase.

### Problemi rješivi oznakama

???+ note "[CPU 监控](https://www.luogu.com.cn/problem/P4314)"
    Nizovi $A,B$ na početku su jednaki:
    
    1.  intervalno pridruživanje $x$ na $A$;
    2.  intervalno zbrajanje $x$ na $A$;
    3.  upit za intervalni $\max$ od $A$;
    4.  upit za intervalni $\max$ od $B$.
    
    Nakon svake operacije izvodimo ažuriranje $\forall i\in [1,n],\ B_i=\max(B_i,A_i)$. $n,m\le 10^5$.

Zanemarimo najprije operaciju 1. Tada postoji samo intervalno zbrajanje; održavamo oznaku $Add$ koja označava vrijednost dodanu trenutnom intervalu, i ta oznaka rješava problem intervalnog $\max$. Zatim promotrimo povijesni intervalni $\max$. Definiramo oznaku $Pre$ sa značenjem: povijesni maksimum oznake $Add$ tijekom životnog ciklusa te oznake.

Ta je definicija možda nejasna, pa prvo objasnimo životni ciklus oznake. Oznaka prolazi ovaj proces:

1.  stvorena je u čvoru $u$;
2.  dok čvor $u$ prima nove oznake, spaja se s njima (misli se na oznake iste vrste);
3.  oznaka čvora $u$ spušta se u djecu od $u$, a oznaka u $u$ se briše.

Životnim ciklusom oznake čvora $u$ smatramo razdoblje od koraka 1 do (ne uključujući) korak 3. Kad se dvije oznake spoje u jednu, spajaju se i njihovi životni ciklusi (tj. početak ciklusa je ranije vrijeme stvaranja). Ekvivalentno: to je razdoblje od trenutka kad je oznaka tog čvora zadnji put spuštena do trenutnog trenutka.

Zašto definiramo životni ciklus? Pomoću tog pojma možemo dokazati: tijekom životnog ciklusa oznake čvora njegova se djeca uopće ne mijenjaju i ostaju u stanju prije početka tog ciklusa. Razlog je jednostavan: u tom razdoblju oznake nisu spuštane.

Stoga možemo jamčiti da se povijesni maksimum oznake $Add$ tijekom životnog ciklusa trenutne oznake može prenijeti na oznake i informacije djece, jer se oznake i informacije djece u tom razdoblju nisu mijenjale. Dakle, kad oznaku od $u$ spuštamo u dijete $s$, lako se vidi da vrijedi

$$
Pre_s=\max(Pre_s,Pre_u+Add_s),Add_s=Add_u+Add_s
$$

Ažuriranje informacija je analogno – ažuriramo odgovarajućom oznakom.

Sada promotrimo operaciju 1.

Intervalno pridruživanje sve brojeve pretvara u isti broj. Nakon toga, bez obzira na intervalno zbrajanje ili pridruživanje, svi brojevi u intervalu i dalje su jednaki (osim ako završimo životni ciklus trenutne oznake spuštanjem). Zato sve oznake nakon prvog intervalnog pridruživanja možemo smatrati oznakama pridruživanja. Drugim riječima, životni ciklus oznake grubo se dijeli na dvije faze:

1.  spajanje više oznaka zbrajanja, bez primljene oznake pridruživanja;
2.  oznaka pridruživanja, bez oznaka zbrajanja (oznake zbrajanja pretvaraju se u oznake pridruživanja).

Zato oznaku Pre tog čvora razdvajamo na $(P_1,P_2)$: $P_1$ je najveća oznaka zbrajanja u prvoj fazi, a $P_2$ najveća oznaka pridruživanja u drugoj fazi. Sličnom metodom možemo spuštati oznake i ažurirati informacije. Vremenska složenost je $O(m\log n)$ (u ovom zadatku nema operacija intervalnog uzimanja ekstrema s $x$!).

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_3.cpp"
```
