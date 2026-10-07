---
title: Prebrojavanje ciklusa
---

## Prebrojavanje običnih ciklusa

???+ note "[Primjer 1: Codeforces Beta Round 11 D. A Simple Task](https://codeforces.com/problemset/problem/11/D)"
    Zadan je jednostavan graf; odredi broj jednostavnih ciklusa u njemu. Jednostavan ciklus je ciklus bez ponovljenih vrhova ili bridova.
    
    Broj vrhova $1\leq n\leq 19$.

??? note "Ideja rješenja"
    Koristimo DP nad bitmaskama (state-compression DP). Neka $f(s,i)$ označava broj putova kojima je skup dosad posjećenih vrhova $s$, trenutno se nalazimo u vrhu $i$, a prvi je vrh puta **vrh s najmanjim indeksom** u skupu $s$.
    
    Za stanje $f(s,i)$ prolazimo po sljedećem vrhu $u$. Ako je $u$ u skupu $s$ i ima najmanji indeks u njemu (tj. to je početni vrh), odgovoru $A$ dodamo $f(s,i)$. Ako $u$ nije u $s$, dodamo $f(s,i)$ na $f(s\cup\{u\},u)$.
    
    Tako se prebroje i ciklusi duljine dva (tj. bridovi), a svaki se ciklus duljine veće od dva prebroji dvaput (jer se iz fiksnog početnog vrha može krenuti u dva smjera), pa je odgovor $\dfrac{A-m}2$, gdje je $m$ broj bridova. Vremenska složenost je $O(2^nm)$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_1.cpp"
    ```

## Prebrojavanje trokuta

**Trokut** (ciklus duljine tri) u jednostavnom grafu $G$ jest neuređena trojka $(u,\ v,\ w)$ takva da postoje tri brida koji spajaju $(u,\ v)$, $(v,\ w)$ i $(w,\ u)$. **Problem prebrojavanja trokuta** traži da se izračuna broj svih trokuta u grafu.

Najprije usmjerimo sve bridove. Dogovorimo da brid ide od vrha manjeg stupnja prema vrhu većeg stupnja, a pri jednakom stupnju od vrha manjeg indeksa prema vrhu većeg indeksa. Tada je graf usmjeren aciklički graf (DAG).

??? note "Dokaz da graf nema ciklusa"
    Pretpostavimo suprotno, da postoji ciklus. Tada su stupnjevi vrhova duž ciklusa sve veći, pa bi za zatvaranje ciklusa svi stupnjevi morali biti jednaki; no indeksi su nužno različiti – kontradikcija.
    
    Dakle nakon usmjeravanja graf sigurno nema ciklusa.
    
    Zapravo, prema gornjem pravilu usmjeravanja može se konstruirati [parcijalni uređaj](../math/order-theory.md#二元关系), pa je graf konstruiran po tom pravilu (tj. [Hasseov dijagram](../math/order-theory.md#偏序集的可视化表示hasse-图) tog parcijalnog uređaja) nužno DAG.

Prolazimo po $u$ i po vrhovima $v$ na koje $u$ pokazuje, zatim po vrhovima $w$ na koje pokazuje $v$, i provjerimo je li $u$ spojen s $w$.

Vremenska složenost ovog algoritma je $O(m\sqrt m)$.

???+ note "Dokaz vremenske složenosti"
    Usmjeravanje prolazi po svim bridovima, složenost $O(n+m)$.
    
    Za svaki par $(v,\ w)$ broj mogućih $u$ ne premašuje ulazni stupanj $d^-(v)$ vrha $v$.
    
    Ako je $d^-(v)\leq\sqrt m$, budući da vrhova $w$ ima najviše $n$, taj dio ima složenost $O(n\sqrt m)$.
    
    Ako je $d^-(v) > \sqrt m$, kako $v$ pokazuje na $w$, vrijedi $d(v) \leq d(w)$, pa je $d(w) > \sqrt m$; no ukupno ima samo $m$ bridova, pa takvih $w$ ima najviše $\sqrt m$ i složenost je $O(m\sqrt m)$.
    
    Ukupna vremenska složenost je $O(n+m+n\sqrt m+m\sqrt m)=O(m\sqrt m)$.
    
    Zapravo, i ako pri usmjeravanju bridove usmjerimo od vrha većeg stupnja prema vrhu manjeg stupnja, složenost je i dalje ispravna: dovoljno je zamijeniti uloge vrhova $u,\ w$ i gornji dokaz i dalje vrijedi.

???+ note "Primjer koda ([Luogu P1989 Prebrojavanje trokuta u neusmjerenom grafu](https://www.luogu.com.cn/problem/P1989))"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_2.cpp"
    ```

### Primjer 2

???+ note "[HDU 6184 Counting Stars](https://acm.hdu.edu.cn/showproblem.php?pid=6184)"
    Zadan je neusmjereni graf s $n$ vrhova i $m$ bridova; odredi koliko se puta u njemu pojavljuje sljedeći oblik.
    
    ![](./images/rings-count1.svg)
    
    $2\leq n\leq 10^5$, $1\leq m\leq\min\left\{2\times 10^5,\ \dfrac{n(n-1)}2\right\}$.

??? note "Ideja rješenja"
    Ovaj oblik čine dva trokuta koja dijele jedan brid. Zato najprije pokrenemo prebrojavanje trokuta i za svaki brid prebrojimo trokute koji ga sadrže; zatim prolazimo po zajedničkom bridu – ako taj brid sadrži $x$ trokuta, doprinos odgovoru je $\dbinom x2$.
    
    Vremenska složenost je $O(m\sqrt m)$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_3.cpp"
    ```

## Prebrojavanje četverokuta

Slično, **četverokut** (ciklus duljine četiri) čine četiri vrha $a,\ b,\ c,\ d$ takva da su $(a,\ b)$, $(b,\ c)$, $(c,\ d)$ i $(d,\ a)$ svi spojeni bridom.

Najprije sortiramo vrhove: vrhovi manjeg stupnja idu naprijed, a većeg stupnja natrag.

Prolazimo po vrhu $a$ koji je u poretku posljednji; tada za svaki vrh $c$ koji je u poretku ispred $a$ trebamo odrediti koliko vrhova $b$ ispred $a$ u poretku zadovoljava da postoje bridovi $(a,\ b)$ i $(b,\ c)$. Zatim bilo koja dva od tih $b$ tvore četverokut. Za brojanje $b$-ova dovoljno je jednom proći po $b$ i $c$.

Primijetimo da je složenost našeg prolaza u biti jednaka složenosti prebrojavanja trokuta, pa je vremenska složenost također $O(m\sqrt m)$ (uz pretpostavku da su $n,\ m$ istog reda veličine).

Vrijedi napomenuti da $(a,\ b,\ c,\ d)$ i $(a,\ c,\ b,\ d)$ mogu biti dva različita četverokuta.

Osim toga, vrhovi jednakog stupnja imat će različit položaj u poretku, a treba paziti i na provjeru $a\neq c$.

???+ note "Primjer koda ([LibreOJ P191 Prebrojavanje četverokuta u neusmjerenom grafu](https://loj.ac/p/191))"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_4.cpp"
    ```

### Primjer 3

???+ note "[Gym 102028L Connected Subgraphs](https://codeforces.com/gym/102028/problem/L)"
    Zadan je neusmjereni graf s $n$ vrhova i $m$ bridova; odredi broj načina da se odaberu četiri brida čiji je inducirani podgraf povezan.
    
    $4\leq n\leq 10^5$, $4\leq m\leq 2\times 10^5$.

??? note "Ideja rješenja"
    Lako je slučajeve podijeliti u pet vrsta: zvijezda, četverokut, trokut s jednim dodatnim bridom iz jednog vrha, lanac od četiri vrha s dodatnim bridom iz jednog od srednjih vrhova, te lanac od pet vrhova.
    
    Zvijezde brojimo izravno po stupnjevima vrhova, binomnim koeficijentima. Četverokute izravno dobivamo gornjim algoritmom. Za dio s trokutima dovoljno je proći po trokutima $(u,\ v,\ w)$; doprinos odgovoru je $[d(u)-2]+[d(v)-2]+[d(w)-2]$.
    
    Promotrimo četvrti slučaj. Prolazimo po vrhu $x$ stupnja $2$, a zatim po njemu susjednom vrhu $y$ kao vrhu stupnja $3$. Doprinos odgovoru je $[d(x)-1]\cdot\dbinom{d(y)-1}2$. No susjedi vrha $y$ mogu se poklopiti sa susjedima vrha $x$, a tada je oblik ekvivalentan trećem slučaju. Svaki tako višak prebrojani treći slučaj prebroji se dvaput (jer postoje dva vrha stupnja $3$), pa treba oduzeti dvostruki broj trećih slučajeva.
    
    Za posljednji slučaj najprije prolazimo po srednjem vrhu $x$; lako se vidi da je doprinos odgovoru
    
    $$
    \sum_{y\in son_x}\sum_{z\in son_x}[d(y)-1]\cdot[d(z)-1].
    $$
    
    I ovdje ima viška prebrojanog. Neka je $s$ susjed vrha $y$, a $t$ susjed vrha $z$; razmislimo li, višak čine sljedeći slučajevi:
    
    1.  $y$ i $t$ se poklapaju, a $s$ i $z$ ne – ekvivalentno trećem slučaju;
    2.  $s$ i $z$ se poklapaju, a $y$ i $t$ ne – također ekvivalentno trećem slučaju;
    3.  i $y$ s $t$ i $s$ sa $z$ se poklapaju – ekvivalentno trokutu;
    4.  $s$ i $t$ se poklapaju – ekvivalentno četverokutu (drugi slučaj).
    
    Budući da dva vrha stupnja $2$ u trećem slučaju, uzeta kao $x$, odgovaraju upravo viškovima 1 i 2, treba dodatno oduzeti dvostruki broj trećih slučajeva. Kod trokuta sva tri vrha mogu biti $x$, pa je prebrojan $3$ puta viška. Jednako tako četverokut je prebrojan $4$ puta viška.
    
    Time smo dobili algoritam za sve slučajeve, vremenske složenosti $O(n+m\sqrt m)$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_5.cpp"
    ```

## Zadaci

[Luogu P3547 \[POI2013\] CEN-Price List](https://www.luogu.com.cn/problem/P3547)

[CodeForces 985G Team Players](https://codeforces.com/contest/985/problem/G) (formula uključivanja-isključivanja)
