---
title: Optimizacija monotonim redom/monotonim stogom
---

## Uvod

Preduvjeti: [monotoni red](../../ds/monotonic-queue.md), [monotoni stog](../../ds/monotonic-stack.md).

Monotoni red (monotonic queue) uglavnom služi za održavanje minimuma/maksimuma intervala čiji se oba kraja pomiču monotono nepadajuće, dok monotoni stog (monotonic stack) uglavnom služi za pronalaženje prvog prethodnog/sljedećeg elementa većeg/manjeg od trenutne vrijednosti.

???+ note "Napomena"
    -   Za minimum održavamo **strogo rastući/nepadajući** monotoni red/stog, i obrnuto.
    -   Pri održavanju strogo rastućeg/padajućeg niza uspoređujemo s **manje ili jednako/veće ili jednako**, a pri održavanju nepadajućeg/nerastućeg s **manje/veće**.

## Koraci optimizacije monotonim redom

-   Dodavanje potrebnih elemenata: u monotoni red dodajemo elemente sve dok trenutni element ne dosegne desni rub traženog intervala; time osiguravamo da su svi potrebni elementi u monotonom redu.
-   Izbacivanje početka reda izvan granica: monotoni red zapravo održava minimum/maksimum svih dosad umetnutih elemenata, a mi obično želimo minimum/maksimum intervala. Zato izbacujemo elemente izvan lijevog ruba kako bi svi elementi u monotonom redu bili unutar traženog intervala.
-   Dohvat minimuma/maksimuma: odgovor je jednostavno element na početku reda.

## Koraci optimizacije monotonim stogom

-   Izbacivanje nevaljanog vrha stoga: usporedbom trenutnog elementa s vrhom stoga izbacujemo vrhove koji narušavaju svojstvo monotonog stoga. Na primjer, u strogo rastućem stogu (vrh je najveći, održava se minimum) izbacujemo sve elemente stoga koji su veći ili jednaki trenutnom.
-   Dodavanje trenutnog elementa: trenutni element jednostavno stavimo na stog.

## Ograničeni ruksak s monotonim redom

???+ note "Opis zadatka"
    Imate $n$ predmeta; $i$-ti predmet ima težinu $w_i$, vrijednost $v_i$ i dostupan je u $k_i$ komada. Imate ruksak nosivosti $W$ i u njega trebate staviti predmete što veće ukupne vrijednosti, a da ne premašite nosivost. Odredite najveću vrijednost.

Ako niste upoznati s DP-om za ruksak, najprije pročitajte [DP za ruksak](../knapsack/basic.md). Neka $f_{i,j}$ označava najveću vrijednost koja se može postići s prvih $i$ predmeta u ruksaku nosivosti $j$. Naivna jednadžba prijelaza je

$$
f_{i,j}=\max_{k=0}^{k_i}(f_{i-1,j-k\times w_i}+v_i\times k)
$$

uz vremensku složenost $O(W\sum k_i)$.

Razmotrimo kako optimizirati prijelaz za $f_i$. Radi jednostavnosti zapisa neka je $g_{x,y}=f_{i,x\times w_i+y},g'_{x,y}=f_{i-1,x\times w_i+y}$, gdje je $0\le y \lt w_i$; tada se jednadžba prijelaza može zapisati kao:

$$
g_{x,y}=\max_{k=0}^{k_i}(g'_{x-k,y}+v_i\times k)
$$

Neka je $G_{x,y}=g'_{x,y}-v_i\times x$. Tada se jednadžba može zapisati kao:

$$
g_{x,y}=\max_{k=0}^{k_i}(G_{x-k,y})+v_i\times x
$$

Time smo dobili klasičan oblik pogodan za optimizaciju monotonim redom. $G_{x,y}$ se računa u $O(1)$, pa za fiksni $y$ sve $g_{x,y}$ možemo izračunati u vremenu $O\left( \left\lfloor \dfrac{W}{w_i} \right\rfloor \right)$. Stoga je složenost izračuna svih $g_{x,y}$ jednaka $O\left( \left\lfloor \dfrac{W}{w_i} \right\rfloor \right)\times O(w_i)=O(W)$. Tako se ukupna složenost prijelaza smanjuje na $O(nW)$.

U implementaciji najprije moramo enumerirati $y$, jer samo tako pri enumeraciji $x$ možemo iskoristiti monotoni red; u monotonom redu pohranjujemo $x-k$, a ne $k$, pa pripadni $G_{x-k,y}$ dohvaćamo izrazom `f[last][q.front() * w[i] + y] - q.front() * v[i]`. Lako je uočiti da je $x-k\in [x - k_i,x]$, pa pri enumeraciji $x$ iz reda moramo ukloniti elemente koji nisu u tom rasponu.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/opt/monotonic-queue-stack/monotonic-queue-stack_2.cpp"
    ```

## Zadaci

???+ note "Primjer [CF372C Watching Fireworks is Fun](http://codeforces.com/problemset/problem/372/C)"
    Sažetak zadatka: u gradu je $n$ položaja i treba ispaliti $m$ vatrometa. Vrijeme ispaljivanja $i$-tog vatrometa označimo s $t_i$, a položaj s $a_i$. Ako se u trenutku ispaljivanja vatrometa nalazite na položaju $x$, dobivate $b_i-|a_i-x|$ bodova sreće.
    
    Na početku možete biti na bilo kojem položaju, a u jednoj jedinici vremena možete se pomaknuti za najviše $d$ jedinica udaljenosti. Trebate maksimizirati ukupan broj bodova sreće.

Neka $f_{i,j}$ označava najveći broj bodova sreće koji se može postići ako ste pri ispaljivanju $i$-tog vatrometa na položaju $j$.

Napišimo jednadžbu prijelaza stanja: $f_{i,j}=\max\{f_{i-1,k}+b_i-|a_i-j|\}$, gdje je $j-(t_{i}-t_{i-1})\times d\le k\le j+(t_{i}-t_{i-1})\times d$.

Pokušajmo je preoblikovati:

Budući da se unutar $\max$ pojavljuje konstanta $b_i$, možemo je izvući van.

$f_{i,j}=\max\{f_{i-1,k}+b_i-|a_i-j|\}=\max\{f_{i-1,k}-|a_i-j|\}+b_i$

Ako su $i$ i $j$ fiksirani, određena je i vrijednost $|a_i-j|$, pa i taj dio možemo izvući van.

Na kraju izraz postaje:

$$
f_{i,j}=\max\{f_{i-1,k}-|a_i-j|\}+b_i=\max\{f_{i-1,k}\}-|a_i-j|+b_i
$$

Razmotrimo sada optimizaciju monotonim redom. Budući da $\max$ u konačnom izrazu ovisi samo o maksimumu jednog neprekinutog segmenta prethodnog stanja, pri računanju stanja za novi $i$ dovoljno je od prethodnog $f_{i-1}$ izgraditi monotoni red i održavati ga tako da vrijednost $\max\{f_{i-1,k}\}$ dobivamo u amortiziranom vremenu $O(1)$, a zatim po formuli izračunati $f_{i,j}$.

Ukupna vremenska složenost je $O(nm)$.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/opt/monotonic-queue-stack/monotonic-queue-stack_1.cpp"
    ```

-   [„Luogu P1886” Klizni prozor](https://loj.ac/problem/10175)
-   [„NOI2005” Veličanstveni valcer](https://www.luogu.com.cn/problem/P2254)
-   [„SCOI2010” Trgovanje dionicama](https://loj.ac/problem/10183)
