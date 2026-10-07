---
title: DP na stablu
---

DP na stablu (tree DP) jest DP koji se izvodi na stablu. Zbog prirođene rekurzivne strukture stabla DP na stablu obično se izvodi rekurzivno.

## Osnove

Opći postupak DP-a na stablu predstavit ćemo na sljedećem zadatku.

???+ note "Primjer [Luogu P1352 Zabava bez šefa](https://www.luogu.com.cn/problem/P1352)"
    Neko sveučilište ima $n$ zaposlenika označenih brojevima $1 \sim N$. Među njima postoji odnos podređenosti, tj. njihovi odnosi čine stablo s rektorom u korijenu, a roditeljski čvor je izravni šef djeteta. Priprema se godišnja zabava; svaki pozvani zaposlenik povećava indeks veselja za $a_i$, no ako na zabavu dođe izravni šef nekog zaposlenika, taj zaposlenik ni u kojem slučaju ne želi doći. Napišite program koji određuje koje zaposlenike pozvati da indeks veselja bude najveći i ispisuje taj najveći indeks veselja.

Neka $f(i,0/1)$ označava optimalno rješenje za podstablo s korijenom $i$ (druga dimenzija 0 znači da $i$ ne dolazi na zabavu, a 1 da $i$ dolazi).

Za svako stanje postoje dvije odluke (u nastavku je $x$ dijete čvora $i$):

-   Ako šef ne dolazi, podređeni mogu, ali ne moraju doći; tada je $f(i,0) = \sum\max \{f(x,1),f(x,0)\}$;
-   Ako šef dolazi, nijedan podređeni ne dolazi; tada je $f(i,1) = \sum{f(x,0)} + a_i$.

Optimalno rješenje trenutnog čvora možemo ažurirati DFS-om, pri povratku na prethodnu razinu.

```cpp
--8<-- "docs/dp/code/tree/tree_1.cpp"
```

Stanje DP-a na stablu obično je optimalno rješenje za trenutni čvor. DFS-om najprije obiđemo sva optimalna rješenja podstabala, zatim ih prenesemo roditelju i izvedemo prijelaz; vrijednost u korijenu na kraju je traženo optimalno rješenje.

### Zadaci za vježbu

-   [HDU 2196 Computer](https://acm.hdu.edu.cn/showproblem.php?pid=2196)

-   [POJ 1463 Strategic game](http://poj.org/problem?id=1463)

-   [\[POI2014\]FAR-FarmCraft](https://www.luogu.com.cn/problem/P3574)

## Ruksak na stablu

Problem ruksaka na stablu, jednostavno rečeno, spoj je problema ruksaka i DP-a na stablu.

???+ note "Primjer [Luogu P2014 CTSC1997 Odabir kolegija](https://www.luogu.com.cn/problem/P2014)"
    Postoji $n$ kolegija; $i$-ti kolegij nosi $a_i$ bodova. Svaki kolegij ima nula ili jedan preduvjetni kolegij; kolegij s preduvjetom može se upisati tek nakon što se položi preduvjet.
    
    Student želi upisati $m$ kolegija. Koliko najviše bodova može skupiti?
    
    $n,m \leq 300$

Svojstvo da svaki kolegij ima najviše jedan preduvjet slično je svojstvu da u korijenskom stablu svaki čvor ima najviše jednog roditelja.

Stoga se nameće ideja da prema tom svojstvu izgradimo stablo; tako svi kolegiji čine šumu. Radi jednostavnosti dodamo novi kolegij s $0$ bodova (označimo ga brojem $0$) kao preduvjet svih kolegija koji nemaju preduvjet; tako šuma postaje stablo s korijenom u kolegiju $0$.

Neka $f(u,i,j)$ označava najveći broj bodova u podstablu s korijenom $u$ ako je obiđeno prvih $i$ podstabala čvora $u$ i odabrano je $j$ kolegija.

Prijelaz spaja obilježja DP-a na stablu i [DP-a za ruksak](./knapsack/basic.md): prolazimo po svakom djetetu $v$ čvora $u$ i istodobno po broju kolegija odabranih u podstablu s korijenom $v$, pa rezultat podstabla spajamo u $u$.

Neka je $s_x$ broj djece čvora $x$, a $\textit{siz}_x$ veličina podstabla s korijenom $x$; jednadžba prijelaza stanja glasi:

$$
f(u,i,j)=\max_{v,k \leq j,k \leq \textit{siz}_v} f(u,i-1,j-k)+f(v,s_v,k)
$$

Obratite pažnju na ograničenja u gornjoj jednadžbi prijelaza: ona osiguravaju da se besmislena stanja ne posjećuju.

Druga dimenzija $f$ lako se uklanja tehnikom kotrljajućeg niza; pritom treba paziti da se $j$ prolazi silazno.

Može se dokazati da je vremenska složenost ovog postupka $O(nm)$[^note1].

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/tree/tree_2.cpp"
    ```

### Zadaci za vježbu

-   [„CTSC1997” Odabir kolegija](https://www.luogu.com.cn/problem/P2014)

-   [„JSOI2018” Infiltracija](https://loj.ac/problem/2546)

-   [„SDOI2017” Stablo jabuke](https://loj.ac/problem/2268)

-   [„Codeforces Round 875 Div. 1” Problem D. Mex Tree](https://codeforces.com/contest/1830/problem/D)

## DP s promjenom korijena

DP s promjenom korijena (rerooting DP) u DP-u na stablu naziva se i dvostrukim prolaskom; korijen obično nije zadan, a promjena korijena utječe na neke vrijednosti, primjerice na zbroj dubina djece ili na zbroj težina vrhova.

Obično su potrebna dva DFS-a: prvi DFS unaprijed računa podatke poput dubine i zbroja težina, a u drugom se DFS-u izvodi dinamičko programiranje s promjenom korijena.

Upoznat ćemo se s tim gradivom kroz nekoliko primjera.

???+ note "Primjer [\[POI2008\]STA-Station](https://www.luogu.com.cn/problem/P3478)"
    Zadano je stablo s $n$ čvorova. Odredi čvor takav da je, kad se on uzme za korijen, zbroj dubina svih čvorova najveći.

Neka je $u$ trenutni čvor, a $v$ njegovo dijete. Najprije $s_i$ označava broj čvorova u podstablu s korijenom $i$; vrijedi $s_u=1+\sum s_v$. Očito je za računanje svih $s_i$ potreban jedan DFS; taj je DFS priprema, njime za svaki čvor dobivamo ukupan broj čvorova u njegovu podstablu.

Promotrimo prijelaz stanja; tu se očituje „promjena korijena”. Neka je $f_u$ zbroj dubina svih čvorova kad je $u$ korijen.

$f_v\leftarrow f_u$ predstavlja promjenu korijena, tj. prijelaz od korijena $u$ na korijen $v$. Očito se pri promjeni korijena s $u$ na $v$ mijenjaju dubine čvorova u njegovu podstablu. Konkretno:

-   dubina svih čvorova u podstablu čvora $v$ smanjuje se za jedan, pa se ukupni zbroj dubina smanjuje za $s_v$;

-   dubina svih čvorova izvan podstabla čvora $v$ povećava se za jedan, pa se ukupni zbroj dubina povećava za $n-s_v$;

Iz tih dvaju uvjeta izvodi se jednadžba prijelaza stanja $f_v = f_u - s_v + n - s_v=f_u + n - 2 \times s_v$.

U drugom DFS-u obilazimo cijelo stablo i izvodimo prijelaz $f_v=f_u + n - 2 \times s_v$, čime dobivamo zbroj dubina za svaki čvor uzet kao korijen. Na kraju jednim prolaskom po zbrojevima dubina svih korijena dobivamo odgovor.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/tree/tree_3.cpp"
    ```

### Zadaci za vježbu

-   [Atcoder Educational DP Contest, Problem V, Subtree](https://atcoder.jp/contests/dp/tasks/dp_v)

-   [Educational Codeforces Round 67, Problem E, Tree Painting](https://codeforces.com/contest/1187/problem/E)

-   [POJ 3585 Accumulation Degree](http://poj.org/problem?id=3585)

-   [\[USACO10MAR\]Great Cow Gathering G](https://www.luogu.com.cn/problem/P2986)

-   [CodeForce 708C Centroids](http://codeforces.com/problemset/problem/708/C)

## Literatura i bilješke

[^note1]: [Dokaz složenosti DP-a tipa spajanja podstabala ruksakom – CSDN blog LYD729](https://blog.csdn.net/lyd_7_29/article/details/79854245)
