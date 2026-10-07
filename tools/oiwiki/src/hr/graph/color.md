---
title: Bojenje grafova
---

## Bojenje vrhova

(Razmatramo neusmjerene grafove bez petlji.)

Bojimo vrhove neusmjerenog grafa tako da susjedni vrhovi ne budu iste boje. Ako je G $k$-obojiv, ali nije $(k-1)$-obojiv, kažemo da je k kromatski broj grafa G i označavamo ga s $\chi(G)$.

Za svaki graf G vrijedi $\chi(G) \leq \Delta(G) + 1$, gdje je $\Delta(G)$ najveći stupanj.

### Brooksov teorem

Ako povezan graf nije ni potpun graf ni neparan ciklus, tada je $\chi(G) \leq \Delta(G)$.

#### Dokaz

???+ note "Dokaz"
    Neka je $|V(G)|=n$; dokazujemo matematičkom indukcijom.
    
    Najprije, za $n\leq 3$ tvrdnja očito vrijedi.
    
    Pretpostavimo da tvrdnja vrijedi za $n-1$; sada ćemo tvrdnju postupno pojačavati.
    
    Dovoljno je promatrati $\Delta(G)$-regularne grafove, jer se neregularan graf može shvatiti kao regularan graf iz kojeg su uklonjeni neki bridovi, a taj postupak ne utječe na zaključak.
    
    Za bilo koji regularan graf G koji nije ni potpun ni neparan ciklus uzmimo bilo koji njegov vrh v i promotrimo podgraf $H:=G-v$; po pretpostavci indukcije $\chi(H)\leq\Delta(H)=\Delta(G)$, pa preostaje dokazati da umetanje v u H ne mijenja zaključak.
    
    Neka je $\Delta:=\Delta(G)$, neka su $\Delta$ boja kojima je obojen H redom $c_1,c_2,\dots,c_{\Delta}$, a $\Delta$ susjeda vrha v neka su $v_1,v_1,\dots,v_{\Delta}$. Smijemo pretpostaviti da su boje tih susjeda vrha v međusobno različite; inače je tvrdnja dokazana.
    
    Neka svi vrhovi grafa H obojeni bojom $c_i$ ili $c_j$ zajedno sa svim bridovima među njima tvore podgraf $H_{i,j}$. Smijemo pretpostaviti da su bilo koja 2 različita vrha $v_i$, $v_j$ u istoj komponenti povezanosti grafa $H_{i,j}$; kad bi bili u dvjema komponentama, mogli bismo zamijeniti boje svih vrhova jedne od njih, pa bi $v_i$, $v_j$ bili iste boje.
    
    > Zamjena boja ovdje znači: ako su u grafu samo dvije boje a i b, sve vrhove izvorno obojene bojom a obojimo bojom b, a sve vrhove izvorno obojene bojom b obojimo bojom a.
    
    Označimo tu komponentu povezanosti s $C_{i,j}$; tada $C_{i,j}$ može biti samo put od $v_i$ do $v_j$. Naime, stupanj vrha $v_i$ u H je $\Delta-1$, pa su boje susjeda vrha $v_i$ u H nužno međusobno različite (inače bismo $v_i$ mogli prebojiti drugom bojom, pa bi se njegova boja poklopila s bojom nekog drugog susjeda vrha v), stoga $v_i$ u $C_{i,j}$ ima točno 1 susjeda; isto vrijedi za $v_j$. Uzmimo zatim u $C_{i,j}$ put od $v_i$ do $v_j$ i nazovimo ga P; ako je $C_{i,j}\ne P$, bojimo vrhove redom duž P i neka je u prvi vrh stupnja većeg od 2 na koji naiđemo; susjedi vrha u koriste najviše $\Delta-2$ boja, pa u možemo prebojiti i time $v_i$, $v_j$ učiniti nepovezanima.
    
    Zatim lako vidimo da za bilo koja 3 različita vrha $v_i$, $v_j$, $v_k$ vrijedi $V(C_{i,j})\cap V(C_{j,k})=\{v_j\}$.
    
    Time je pojačavanje tvrdnje završeno.
    
    Ostatak je jednostavan. Najprije, ako su susjedi vrha v međusobno susjedni, tvrdnja je dokazana. Neka, bez smanjenja općenitosti, $v_1$, $v_2$ nisu susjedni; uzmimo u $C_{1,2}$ susjeda w vrha $v_1$ i zamijenimo boje u $C_{1,3}$. U novom grafu vrijedi $w\in V(C_{1,2})\cap V(C_{2,3})$, što je kontradikcija.
    
    Time je dokaz tvrdnje završen.

### Welsh–Powellov algoritam

Welsh–Powellov algoritam pohlepni je algoritam za traženje bojenja kad **broj boja nije ograničen**.

Za neusmjereni graf G bez petlji neka $V(G):=\{v_1,v_2,\dots,v_n\}$ zadovoljava

$\deg(v_i)\geq\deg(v_{i+1}),~\forall 1\leq i\leq n-1$

Broj boja nakon bojenja Welsh–Powellovim algoritmom najviše je $\max_{i=1}^n\min\{\deg(v_i)+1,i\}$, a vremenska složenost algoritma je $O\left(n\max_{i=1}^n\min\{\deg(v_i)+1,i\}\right)=O(n^2)$.

#### Postupak

1.  Trenutno neobojene vrhove poredaj silazno po stupnju.
2.  Prvi vrh oboji još neiskorištenom bojom.
3.  Redom prolazi sljedeće vrhove; ako trenutni vrh **nije susjedan** nijednom vrhu **iste** boje kao prvi vrh, oboji ga bojom prvog vrha.
4.  Ako još ima neobojenih vrhova, vrati se na korak 1, inače završi.

Primjer:

![Original](images/color1.png)

(Napravljeno pomoću [Graph Editora](https://csacademy.com/app/graph_editor/).)

Najprije vrhove sortiramo silazno po stupnju i dobivamo:

| Redni broj              | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  | 10 | 11 | 12 | 13 |
| ----------------------- | - | - | - | - | - | - | - | - | -- | -- | -- | -- | -- |
| Oznaka vrha             | 4 | 5 | 0 | 2 | 9 | 1 | 3 | 6 | 10 | 12 | 7  | 8  | 11 |
| Stupanj                 | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 3  | 3  | 2  | 2  | 1  |
| $\min\{\deg(v_i)+1,i\}$ | 1 | 2 | 3 | 4 | 5 | 4 | 4 | 4 | 4  | 4  | 3  | 3  | 2  |

Dakle, Welsh–Powellov algoritam koristi najviše 5 boja.

Osim toga, graf ima podgraf $C_3$, pa je kromatski broj sigurno barem 3.

-   Prvo bojenje:

    ![Colored 1](images/color2.png)

    Bojimo vrhove `4 9 3 11`.
-   Drugo bojenje:

    ![Colored 2](images/color3.png)

    Bojimo vrhove `5 2 6 7 8`.
-   Treće bojenje:

    ![Colored 3](images/color4.png)

    Bojimo vrhove `0 1 10 12`.

#### Dokaz

???+ note "Dokaz"
    Za neusmjereni graf G bez petlji neka $V(G):=\{v_1,v_2,\dots,v_n\}$ zadovoljava
    
    $\deg(v_i)\geq\deg(v_{i+1}),~\forall 1\leq i\leq n-1$
    
    Neka je $V_0=\varnothing$; iz $V(G)\setminus\bigcup_{i=0}^{m-1} V_i$ uzimamo podskup $V_m$ čiji elementi zadovoljavaju
    
    1.  $v_{k_m}\in V_m$, gdje je $k_m=\min\{k:v_k\notin\bigcup_{i=0}^{m-1} V_i\}$
    2.  Ako je
    
        $\{v_{i_{m,1}},v_{i_{m,2}},\dots,v_{i_{m,l_m}}\}\subset V_m,~i_{m,1}<i_{m,2}<\dots<i_{m,l_m}$
    
        tada $v_j\in V_m$ ako i samo ako
    
        1.  $j>i_{m,l_m}$
        2.  $v_j$ nije susjedan nijednom od $v_{i_{m,1}},v_{i_{m,2}},\dots,v_{i_{m,l_m}}$
    
    Očito, obojimo li vrhove iz $V_i$ i-tom bojom, to je bojenje upravo ono koje daje Welsh–Powellov algoritam, i očito vrijedi
    
    -   $V_1\neq\varnothing$
    -   $V_i\cap V_j=\varnothing\iff i\neq j$
    -   $\exists \alpha(G)\in\Bbb{N}^*,\forall i>\alpha(G),~s.t.~ V_i=\varnothing$
    
    Treba samo dokazati:
    
    $\bigcup_{i=1}^{\alpha(G)} V_i=V(G)$
    
    pri čemu
    
    $\chi(G)\leq\alpha(G)\leq\max_{i=1}^n\min\{\deg(v_i)+1,i\}$
    
    Lijeva nejednakost očito vrijedi; promotrimo desnu.
    
    Najprije lako zaključujemo:
    
    ako $v\notin\bigcup_{i=1}^mV_i$, tada je v susjedan barem jednom vrhu iz svakog od $V_1,V_2,\dots,V_m$, pa je $\deg(v)\geq m$
    
    odakle slijedi
    
    $v_j\in\bigcup_{i=1}^{\deg(v_j)+1}V_i$
    
    S druge strane, iz načina konstrukcije niza $\{V_i\}$ lako vidimo
    
    $v_j\in\bigcup_{i=1}^j V_i$
    
    Spajanjem obiju relacija tvrdnja je dokazana.

## Bojenje bridova

Bojimo bridove neusmjerenog grafa tako da susjedni bridovi budu različitih boja. Ako je G k-bridno obojiv, ali nije $(k-1)$-bridno obojiv, kažemo da je k bridni kromatski broj grafa G i označavamo ga s $\chi'(G)$.

### Vizingov teorem

Ako je G jednostavan graf, tada je $\Delta(G) \leq \chi'(G) \leq \Delta(G) + 1$

Ako je G bipartitan graf, tada je $\chi'(G)=\Delta(G)$

Za neparan $n$ ($n \neq 1$) vrijedi $\chi'(K_n)=n$; za paran $n$ vrijedi $\chi'(K_n)=n-1$

### Konstruktivni dokaz Vizingova teorema za bipartitne grafove

???+ note "Dokaz"
    Bridove u bipartitni graf dodajemo redom.
    
    Kad pokušavamo dodati brid $(x,y)$, za $x$ i $y$ tražimo još neiskorištenu boju s najmanjim brojem; neka su to redom $l_x$ i $l_y$.
    
    Ako je $l_x=l_y$, tom bridu izravno dodijelimo boju $l_x$.
    
    Inače neka je $l_x<l_y$; pokušavamo bridu boje $l_x$ koji izlazi iz vrha $y$ promijeniti boju u $l_y$.
    
    Postupak promjene može se približno shvatiti kao konačan, jedinstveno određen augmentirajući put koji kreće iz $y$ i redom prolazi bridovima boja $l_x,l_y,\cdots$.
    
    Budući da je augmentirajući put konačan, svim bridovima na njemu možemo zamijeniti boje, tj. one boje $l_x$ prebojiti u $l_y$, a one boje $l_y$ u $l_x$.
    
    Po svojstvu bipartitnih grafova vrh $x$ ne može biti na augmentirajućem putu, jer bi to bilo u suprotnosti s time da je $l_x$ najmanja neiskorištena boja.
    
    Zato nakon augmentacije bridu koji spaja $x$ i $y$ izravno dodijelimo boju $l_x$.
    
    Ukupna vremenska složenost konstrukcije je $O(nm)$.

???+ note "Primjer koda [UVa10615 Rooks](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=18&page=show_problem&problem=1556)"
    ```cpp
    --8<-- "docs/graph/code/color/color_1.cpp"
    ```

??? note "Vrlo netrivijalan primjer [UOJ 444 Bipartitni graf](https://uoj.ac/problem/444)"
    Ovaj je zadatak autor sastavio 2018. za prvi krug domaćih zadaća kineskog reprezentativnog kampa.
    
    Najprije uočavamo da je donja granica odgovora broj vrhova čiji stupanj nije višekratnik od k.
    
    Konstrukcija koja postiže donju granicu je razdvajanje vrhova bipartitnog grafa.
    
    Ako je $degree \bmod k \neq 0$, vrh razdvajamo na $degree/k$ vrhova stupnja k i jedan vrh stupnja $degree \bmod k$.
    
    Ako je $degree \bmod k = 0$, vrh razdvajamo na $degree/k$ vrhova stupnja k.
    
    Razdvojeni vrhovi u izvornom grafu imaju isto značenje, tj. uz poštovanje ograničenja stupnja kraj brida može se spojiti s bilo kojim od razdvojenih vrhova.
    
    Po Vizingovu teoremu očito možemo konstruirati k-bojenje tog grafa.
    
    Dio s brisanjem bridova nema mnogo veze s Vizingovim teoremom pa ga ovdje ne razrađujemo.
    
    Zainteresirani čitatelji mogu pročitati autorovo tadašnje rješenje.

## Kromatski polinom

$P(G,k)$ označava ukupan broj različitih k-bojenja grafa G.

$P(K_n, k) = k(k-1)\cdots(k-n+1)$

$P(N_n, k) = k^n$

U neusmjerenom grafu G bez petlji:

1.  ako $e=(v_i, v_j) \notin E(G)$, tada $P(G, k) = P(G \cup e, k)+P(G\setminus e, k)$
2.  ako $e=(v_i, v_j) \in E(G)$, tada $P(G,k)=P(G-e,k)-P(G\setminus e,k)$

Teorem: neka je $V_1$ vršni separator grafa G, $G[V_1]$ potpun podgraf grafa G reda $|V_1|$, a $G-V_1$ neka ima $p(p \geq 2)$ komponenata povezanosti; tada:

$P(G,k)=\frac{\Pi_{i=1}^{p}{(P(H_i, k))}}{P(G[V_1], k)^{p-1}}$

gdje je $H_i=G[V_1 \cup V(G_i)]$

## Literatura

1.  [Graph coloring - Wikipedia](https://en.wikipedia.org/wiki/Graph_coloring)
2.  Welsh, D. J. A.; Powell, M. B. (1967), "[An upper bound for the chromatic number of a graph and its application to timetabling problems](https://doi.org/10.1093%2Fcomjnl%2F10.1.85)", The Computer Journal, 10 (1): 85–86
