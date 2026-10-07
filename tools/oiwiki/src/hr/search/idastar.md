---
title: IDA*
---

Preduvjeti: [Algoritam A\*](./astar.md), [iterativno produbljivanje](./iterative.md)

Ova stranica kratko predstavlja algoritam IDA\*. IDA\* je algoritam A\* koji koristi iterativno produbljivanje (iterative deepening).

## Postupak

Algoritam IDA\* inačica je pretraživanja s iterativnim produbljivanjem. Iterativno produbljivanje u svakom DFS-u ograničava dubinu pretraživanja, dok IDA\* ograničava cijenu puta u jednom DFS-u.

U jednoj iteraciji algoritam iz početnog vrha $s$ pokreće DFS, bilježi stvarnu cijenu $g(x)$ dolaska do trenutnog vrha $x$ i za odsijecanje (pruning) koristi procjenu $h(x)$ najmanje cijene od $x$ do cilja. Ako procjena ukupne cijene puta do cilja duž trenutnog puta

$$
f(x) = g(x) + h(x)
$$

prelazi prag $C$, pretraživanje te grane se prekida.

Prag $C$ dinamički se mijenja između iteracija. Početni prag je procjena ukupne cijene početnog vrha $h(s)$. U jednoj iteraciji, svaki put kad se pretraživanje prekine zbog prelaska praga, bilježi se najmanja procjena ukupne cijene među svim još neposjećenim sljedbenicima. Nakon završetka iteracije prag se postavlja na tu najmanju vrijednost i kreće sljedeći krug pretraživanja.

## Svojstva

Budući da se koristi ista strategija odsijecanja kao u algoritmu A\*, rasprava o svojstvima algoritma A\* vrijedi i za IDA\*.

U usporedbi s algoritmom A\*, IDA\* ima sljedeće prednosti:

-   Nije potrebno provjeravati duplikate ni sortirati, što pogoduje dubinskom odsijecanju.
-   Manji su zahtjevi za memorijom. Svaka je iteracija pretraživanje u dubinu, ali s ograničenjem cijene puta; DFS smanjuje potrošnju memorije.

Ima i nedostatak:

-   Ponovljeno pretraživanje. Čak i kad se dvije uzastopne iteracije malo razlikuju, pri svakom popuštanju ograničenja pretraživanje kreće ispočetka.

## Implementacija

Neka je $h$ prikladna heuristička funkcija (funkcija procjene), a $s$ početni vrh pretraživanja. Cjelovit tijek algoritma izgleda otprilike ovako:

$$
\begin{array}{l}
\textbf{Algorithm. }\textrm{IdaStar}():\\
\textbf{Output. }\text{The shortest path, }\textit{path}\text{, and its cost, }C\text{, if a path exists,}\\
\quad \text{and }\textrm{NOT}\_\textrm{FOUND}\text{, otherwise.}\\
\textbf{Method.}\\
\begin{array}{ll}
1  & C \gets h(s) \\
2  & path \gets [s] \\
3  & \textbf{while }\text{true}\\
4  & \quad t \gets \textrm{Search}(\textit{path},0,C)\\
5  & \quad \textbf{if } t=\text{FOUND}\textbf{ then return }(\textit{path},C) \\
6  & \quad \textbf{if } t=\infty\textbf{ then return }\textrm{NOT}\_\textrm{FOUND} \\
7  & \quad C \gets t
\end{array}\\
\\
\textbf{Sub-Algorithm. }\textrm{Search}(\textit{path},g,C):\\
\textbf{Input. }\text{The current path, }\textit{path}\text{, its cost, }g\text{, and search limit }C.\\
\textbf{Output. }\text{FOUND, if the target node has been reached; }\infty\text{, if all}\\
\quad \text{reachable nodes have been explored; otherwise, the minimum}\\
\quad \text{total cost, }t\text{, among nodes not yet explored.}\\
\textbf{Method.}\\
\begin{array}{ll}
1  & \textit{node} \gets \text{the last element in }\textit{path}\\
2  & f \gets g + h(\textit{node}) \\
3  & \textbf{if } f > C \textbf{ then return } f \\
4  & \textbf{if }\textit{node}\text{ is the target }\textbf{then return }\text{FOUND}\\
5  & \textit{min} \gets \infty \\
6  & \textbf{for }\text{each }\textit{child}\text{ of }\textit{node }\textbf{do}\\
7  & \quad \textbf{if }\textit{child}\text{ not in }\textit{path}\textbf{ then}\\
8  & \quad \quad \text{append }\textit{child}\text{ to }\textit{path}\\
9  & \quad \quad t \gets \text{Search}(\textit{path}, g + \text{Cost}(\textit{node},\textit{child}), C)\\
10 & \quad \quad \textbf{if }t = \text{FOUND}\textbf{ then return }\text{FOUND}\\
11 & \quad \quad \textbf{if }t < \textit{min}\textbf{ then }\textit{min}\gets t\\
12 & \quad \quad \text{remove the last element of }\textit{path}\\
13 & \textbf{return }\textit{min}
\end{array}
\end{array}
$$

## Primjer

???+ example "[Egipatski razlomci](https://www.luogu.com.cn/problem/P1763)"
    U starom Egiptu svaki se racionalni broj zapisivao kao zbroj međusobno različitih jediničnih razlomaka (tj. razlomaka $1/a$, $a\in\mathbf{N}_+$). Na primjer, $\dfrac{2}{3}=\dfrac{1}{2}+\dfrac{1}{6}$, ali nije dopušteno $\dfrac{2}{3}=\dfrac{1}{3}+\dfrac{1}{3}$ jer se među pribrojnicima ne smiju pojaviti jednaki jedinični razlomci.
    
    Razlomak $\dfrac{a}{b}$ može se prikazati na mnogo načina. Dogovorimo se: od dvaju prikaza istog razlomka bolji je onaj s manje pribrojnika; ako je broj pribrojnika jednak, bolji je onaj čiji je najmanji razlomak veći. Na primjer, $\dfrac{19}{45}=\dfrac{1}{5}+\dfrac{1}{6}+\dfrac{1}{18}$ najbolji je prikaz.
    
    Zadani su cijeli brojevi $a,b$ ($0<a<b<1000$); napišite program koji računa najbolji prikaz.

??? note "Ideja rješenja"
    Zadatak se u teoriji može riješiti backtrackingom, ali bi stablo rješenja bilo zaista „strašno”: ne samo da dubina nema očitu gornju granicu, nego je i izbor pribrojnika u teoriji beskonačan. Drugim riječima, pretraživanjem u širinu ne bismo uspjeli proširiti ni jednu razinu, jer je svaka razina beskonačna.
    
    Rješenje je iterativno produbljivanje: redom od manjih prema većima nabrajamo gornju granicu dubine $C$ i u svakom pretraživanju razmatramo samo vrhove dubine najviše $C$. Tako ćemo, ako je dubina rješenja konačna, rješenje sigurno pronaći u konačnom vremenu.
    
    Gornja granica dubine $C$ može poslužiti i za odsijecanje. Proširujemo u poretku rastućih nazivnika; ako smo na razini $i$, zbroj prvih $i$ razlomaka je $\dfrac{c}{d}$, a $i$-ti razlomak je $\dfrac{1}{e}$, onda je potrebno još najmanje
    
    $$
    h = \left(\dfrac{a}{b}-\dfrac{c}{d}\right)/\left(\dfrac{1}{e+1}\right)
    $$
    
    razlomaka da bi zbroj dosegnuo $\dfrac{a}{b}$. Na primjer, ako smo trenutno došli do $\dfrac{19}{45}=\dfrac{1}{5}+\dfrac{1}{100}+\cdots$, svaki sljedeći razlomak iznosi najviše $\dfrac{1}{101}$, pa je potrebno još najmanje $\left({\dfrac{19}{45}-\dfrac{1}{5}}\right)/\left({\dfrac{1}{101}}\right)=23$ pribrojnika da bi zbroj dosegnuo $\dfrac{19}{45}$; zato prvih $22$ iteracija to podstablo uopće neće razmatrati. Ključno je ovo: možemo procijeniti koliko je još najmanje koraka potrebno do rješenja.
    
    Uočite da riječ „najmanje” znači da je procjena „optimistična”. Kao i u algoritmu A\*, dobra funkcija procjene mora biti „optimistična”, tj. ne smije precijeniti stvarnu cijenu. Zamijenimo li ograničenje dubine $g\le C$ iz iterativnog produbljivanja strožim ograničenjem $g + h \le C$, dobivamo algoritam IDA\* o kojem govori ova stranica. Budući da je cijena puta u ovom tekstu upravo njegova duljina, IDA\* također ograničava duljinu puta, samo joj dodaje procjenu koliko je još koraka potrebno. U općenitijim zadacima, ovisno o tome koja se cijena minimizira, mogu se smisliti i druge funkcije procjene.
    
    U implementaciji IDA\* dodatno optimiziramo odsijecanjem:
    
    1.  Pri proširivanju vrha sljedeći nazivnik koji razmatramo iznosi najmanje $\left(\dfrac{a}{b}-\dfrac{c}{d}\right)^{-1}$, pa time možemo poboljšati početnu točku nabrajanja $e$.
    2.  Ograničenje cijene puta u IDA\* može se preoblikovati u
    
        $$
        e \le \left(\dfrac{a}{b}-\dfrac{c}{d}\right)^{-1}(C-g) - 1.
        $$
    
        Zato ne treba nabrajati sve sljedeće nazivnike i provjeravati ih jedan po jedan; dovoljno je nabrajati do te gornje granice.
    3.  Kad pretraživanje dođe do posljednja dva razlomka, izvedivost provjerimo izravno kvadratnom jednadžbom umjesto da nastavljamo pretraživati. Konkretno, da bismo našli $e<x<y\le E_\text{max}$ takve da
    
        $$
        \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{p}{q} := \dfrac{a}{b}-\dfrac{c}{d},
        $$
    
        dovoljno je riješiti sustav kvadratnih jednadžbi s dvije nepoznanice
    
        $$
        \begin{cases}
        x + y = kp,\\
        xy = kq
        \end{cases}
        $$
    
        pri čemu je $k\in\mathbf N_+$. Iz teorije kvadratnih jednadžbi znamo da sustav samo kad je
    
        $$
        \Delta = k^2p^2-4kq > 0 \iff k > \dfrac{4q}{p^2}
        $$
    
        ima dva različita realna rješenja
    
        $$
        x = \dfrac{kp - \sqrt{\Delta}}{2},~ y = \dfrac{kp + \sqrt{\Delta}}{2}.
        $$
    
        Zato možemo izravno nabrajati sve moguće $k$ i provjeravati postoji li takav par cjelobrojnih rješenja. Pri nabrajanju $k$ gornju granicu određuje uvjet $y < E_\text{max}$.
    4.  Svaki put kad nađemo rješenje, gornju granicu nazivnika $M_e$ postavimo na najveći nazivnik u trenutnom rješenju umanjen za jedan.
    
    Osim toga, implementacija izravno pamti vrijednosti $\dfrac{a}{b}-\dfrac{c}{d}$ i $C-g$: brojnik i nazivnik prve čuvaju se u varijablama `a` i `b`, a druga u varijabli `d`.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/search/code/idastar/idastar_1.cpp"
    ```

## Zadaci za vježbu

-   [UVa 1343 The Rotation Game](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4089)
