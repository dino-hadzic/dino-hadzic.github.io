---
title: Heavy-light dekompozicija (dekompozicija stabla na lance)
---

## Uvod

Dekompozicija stabla na lance služi za rastavljanje stabla na niz lanaca radi održavanja informacija o putevima u stablu.

Konkretno, cijelo se stablo rastavi na niz lanaca, čime se složi u linearnu strukturu, a zatim se informacije održavaju drugim strukturama podataka.

**Dekompozicija stabla na lance** (tree chain decomposition) ima više oblika, npr. **heavy-light dekompoziciju** (heavy path decomposition), **dekompoziciju na duge lance** (long-path decomposition) i dekompoziciju koja se koristi u Link/cut Treeu (ponekad zvanu „dekompozicija na stvarne lance”). U većini slučajeva (ako nije posebno naglašeno) „dekompozicija na lance” znači „heavy-light dekompozicija”.

Heavy-light dekompozicija može bilo koji put u stablu podijeliti na najviše $O(\log n)$ uzastopnih lanaca, pri čemu su dubine čvorova na svakom lancu međusobno različite (tj. lanac ide odozdo prema gore, a LCA svih čvorova lanca jedan je njegov kraj).

Heavy-light dekompozicija ujedno jamči da su DFS indeksi čvorova svakog dobivenog lanca uzastopni, pa se informacije o putevima u stablu mogu zgodno održavati strukturama podataka za nizove (npr. segment treeom). Primjerice:

1.  Izmjena vrijednosti svih čvorova **na putu između dvaju čvorova stabla**.
2.  Upit **zbroja/ekstrema/drugih informacija (koje se u nizu mogu održavati strukturom podataka i lako spajati)** težina čvorova **na putu između dvaju čvorova stabla**.

Osim za održavanje informacija o putevima u kombinaciji sa strukturama podataka, dekompozicija na lance može se koristiti i za računanje LCA u $O(\log n)$ (s malom konstantom). U nekim se zadacima njezina svojstva mogu iskoristiti i na fleksibilnije načine.

## Heavy-light dekompozicija

Uvedimo nekoliko definicija:

**Teško dijete** (heavy child) čvora jest ono njegovo dijete čije je podstablo najveće. Ako takvih ima više, uzmemo bilo koje. Ako čvor nema djece, nema ni teško dijete.

**Laka djeca** (light children) sva su ostala djeca.

Brid od čvora do njegova teškog djeteta je **teški brid** (heavy edge).

Bridovi do ostale, lake djece su **laki bridovi** (light edges).

Niz nadovezanih teških bridova čini **teški lanac** (heavy chain).

Ako i osamljene čvorove smatramo teškim lancima, cijelo je stablo rastavljeno na niz teških lanaca.

Kao na slici:

![HLD](./images/hld.png)

## Implementacija

Implementacija dekompozicije sastoji se od dva DFS prolaza. Pseudokod je sljedeći:

Prvi DFS za svaki čvor bilježi roditelja ($\textit{father}$), dubinu ($\textit{depth}$), veličinu podstabla ($\textit{size}$) i teško dijete ($\textit{hson}$).

$$
\begin{array}{l}
\text{TREE-BUILD }(u,\textit{dep}) \\
\begin{array}{ll}
1 & u.\textit{hson}\gets 0 \\
2 & u.\textit{hson}.\textit{size}\gets 0 \\
3 & u.\textit{depth}\gets \textit{dep} \\
4 & u.\textit{size}\gets 1 \\
5 & \textbf{for }\text{each son }v\text{ of }u \\
6 & \qquad u.\textit{size}\gets u.\textit{size} + \text{TREE-BUILD }(v,\textit{dep}+1) \\
7 & \qquad v.\textit{father}\gets u \\
8 & \qquad \textbf{if }v.\textit{size}> u.\textit{hson}.\textit{size} \\
9 & \qquad \qquad u.\textit{hson}\gets v \\
10 & \textbf{return } u.\textit{size}
\end{array}
\end{array}
$$

Drugi DFS bilježi vrh lanca kojem čvor pripada ($\textit{top}$, treba ga inicijalizirati na sam čvor), DFS indeks pri obilasku s prednošću teških bridova ($\textit{dfn}$) i indeks čvora koji odgovara DFS indeksu ($\textit{rank}$).

$$
\begin{array}{l}
\text{TREE-DECOMPOSITION }(u,\textit{top}) \\
\begin{array}{ll}
1 & u.\textit{top}\gets \textit{top} \\
2 & \textit{tot}\gets \textit{tot}+1\\
3 & u.\textit{dfn}\gets \textit{tot} \\
4 & \textit{rank}(\textit{tot})\gets u \\
5 & \textbf{if }u.\textit{hson}\text{ is not }0 \\
6 & \qquad \text{TREE-DECOMPOSITION }(u.\textit{hson},\textit{top}) \\
7 & \qquad \textbf{for }\text{each son }v\text{ of }u \\
8 & \qquad \qquad \textbf{if }v\text{ is not }u.\textit{hson} \\
9 & \qquad \qquad \qquad \text{TREE-DECOMPOSITION }(v,v) 
\end{array}
\end{array}
$$

Slijedi implementacija u kodu.

Najprije nekoliko definicija:

-   $\operatorname{fa}(x)$ označava roditelja čvora $x$ u stablu.
-   $\operatorname{dep}(x)$ označava dubinu čvora $x$ u stablu.
-   $\operatorname{siz}(x)$ označava broj čvorova u podstablu čvora $x$.
-   $\operatorname{son}(x)$ označava **teško dijete** čvora $x$.
-   $\operatorname{top}(x)$ označava vršni čvor (najmanje dubine) **teškog lanca** kojem $x$ pripada.
-   $\operatorname{dfn}(x)$ označava **DFS indeks** čvora $x$, ujedno njegov indeks u segment treeu.
-   $\operatorname{rnk}(x)$ označava indeks čvora koji odgovara DFS indeksu; vrijedi $\operatorname{rnk}(\operatorname{dfn}(x))=x$.

Te vrijednosti predobradimo dvama DFS prolazima: prvi DFS računa $\operatorname{fa}(x)$, $\operatorname{dep}(x)$, $\operatorname{siz}(x)$, $\operatorname{son}(x)$, a drugi DFS računa $\operatorname{top}(x)$, $\operatorname{dfn}(x)$, $\operatorname{rnk}(x)$.

```cpp
void dfs1(int u, int f) {
  fa[u] = f, dep[u] = dep[f] + 1, siz[u] = 1;
  for (auto v : G[u]) {
    if (v == f) continue;
    dfs1(v, u);
    siz[u] += siz[v];
    if (siz[v] > siz[son[u]]) son[u] = v;
  }
}

void dfs2(int u, int ftop) {
  top[u] = ftop, dfn[u] = ++idx, rnk[idx] = u;
  if (son[u]) dfs2(son[u], ftop);
  for (auto v : G[u])
    if (v != son[u] && v != fa[u]) dfs2(v, v);
}
```

## Svojstva heavy-light dekompozicije

**Svaki čvor stabla pripada točno jednom teškom lancu**.

Početni čvor teškog lanca sigurno nije teško dijete (jer je početak teškog lanca ili korijen ili lako dijete svog roditelja).

Svi teški lanci zajedno **potpuno rastavljaju** cijelo stablo.

Pri dekompoziciji **obilazimo s prednošću teških bridova**, pa su u konačnom DFS poretku stabla DFS indeksi unutar teškog lanca uzastopni. Niz sortiran po DFN upravo su lanci dobiveni dekompozicijom.

DFS indeksi unutar jednog podstabla su uzastopni.

Uočavamo da se, kad prema dolje prijeđemo preko **lakog brida**, veličina podstabla u kojem se nalazimo barem prepolovi.

Stoga za bilo koji put u stablu, rastavimo li ga na dva silaska od [LCA](./lca.md) na obje strane, svaki silazak prelazi najviše $O(\log n)$ lakih bridova, pa se svaki put u stablu može rastaviti na najviše $O(\log n)$ teških lanaca.

??? info "Kako argumentirano srušiti HLD"
    U pravilu je $O(\log n)$ HLD-a s nepunom konstantom teško srušiti; ako se želi, može se samo izgraditi binarno stablo male dubine.
    
    Stoga možemo razmotriti kompromis.
    
    Izgradimo binarno stablo sa $\sqrt{n}$ čvorova. Svaki brid od čvora do njegova djeteta zamijenimo lancem duljine $\sqrt{n}$.
    
    Tako broj prijelaza između lakih i teških lanaca za slučajne upite možemo dovesti na prosječno $\frac{\log n}{2}$, uz dubinu $O(\sqrt{n} \log n)$.
    
    Dodamo li još nekoliko slučajnih listova, čini se da bi se HLD mogao srušiti. No zbog male konstante HLD-a to možda ipak neće uspjeti.

## Česte primjene

### Održavanje na putu

Računanje zbroja težina na putu između dvaju čvorova stabla pomoću heavy-light dekompozicije; pseudokod je sljedeći:

$$
\begin{array}{l}
\text{TREE-PATH-SUM }(u,v) \\
\begin{array}{ll}
1 & \textit{tot}\gets 0 \\
2 & \textbf{while }u.\textit{top}\text{ is not }v.\textit{top} \\
3 & \qquad \textbf{if }u.\textit{top}.\textit{depth}< v.\textit{top}.\textit{depth} \\
4 & \qquad \qquad \text{SWAP}(u, v) \\
5 & \qquad \textit{tot}\gets \textit{tot} + \text{sum of values between }u\text{ and }u.\textit{top} \\
6 & \qquad u\gets u.\textit{top}.\textit{father} \\
7 & \textit{tot}\gets \textit{tot} + \text{sum of values between }u\text{ and }v \\
8 & \textbf{return } \textit{tot} 
\end{array}
\end{array}
$$

DFS indeksi na lancu su uzastopni, pa se mogu održavati segment treeom ili Fenwick treeom.

Svaki put biramo lanac veće dubine i skačemo prema gore, dok oba čvora ne budu na istom lancu.

Ista struktura skakanja po lancima primjenjiva je za održavanje i brojanje drugih informacija na putu.

### Održavanje podstabla

Ponekad se traži održavanje informacija na podstablu, primjerice povećanje težine svih čvorova podstabla s korijenom $x$ za $v$.

Pri DFS obilasku DFS indeksi čvorova unutar podstabla su uzastopni.

Za svaki čvor zabilježimo bottom, čvor na kraju uzastopnog intervala njegova podstabla.

Tako se informacija o podstablu pretvara u informaciju o uzastopnom intervalu.

### Računanje LCA

Neprestano skačemo prema gore po teškim lancima; kad dođemo na isti teški lanac, čvor manje dubine je LCA.

Pri skakanju prema gore prvo skačemo s onim čvorom čiji vrh teškog lanca ima veću dubinu.

Primjer koda:

```cpp
int lca(int u, int v) {
  while (top[u] != top[v]) {
    if (dep[top[u]] > dep[top[v]])
      u = fa[top[u]];
    else
      v = fa[top[v]];
  }
  return dep[u] > dep[v] ? v : u;
}
```

### Promjena korijena

Razmotrimo novu vrstu problema: osim osnovnih operacija koje heavy-light dekompozicija podržava, dodana je operacija promjene korijena.

Budući da su informacije koje održava dekompozicija statične, dinamičke izmjene nisu podržane. Istodobno, nemoguće je nakon svake promjene korijena ponovno raditi predobradu; složenost bi bila prevelika. Stoga treba što bolje iskoristiti prethodno dobivene informacije za obradu promjene korijena.

Za izmjene i upite na putu: budući da je jednostavni put između dvaju čvorova stabla jedinstven, ništa se ne mijenja i obrada je ista kao inače.

Za izmjene i upite na podstablu opća je ideja preslikati podstablo nakon promjene korijena na izvorno podstablo. Za to treba razlikovati slučajeve prema međusobnom položaju korijena operiranog podstabla, korijena cijelog stabla nakon promjene korijena i izvornog korijena stabla. Detalji su u [primjeru zadatka „LOJ 139. Dekompozicija stabla na lance” u nastavku](#primjeri-zadataka).

## Primjeri zadataka

Na primjerima pokazujemo kako se primjenjuje heavy-light dekompozicija. Najprije jedan šablonski zadatak.

???+ example "[„ZJOI2008” Statistika stabla](https://loj.ac/problem/10138)"
    Na statičnom stablu s $n$ čvorova s težinama izvršite ukupno $q$ operacija triju vrsta:
    
    1.  izmijenite težinu pojedinog čvora;
    2.  upitajte najveću težinu na putu od $u$ do $v$;
    3.  upitajte zbroj težina na putu od $u$ do $v$.
    
    Vrijedi $1\le n\le 30000$, $0\le q\le 200000$.

??? note "Rješenje"
    Prema tekstu zadatka i gore opisanim svojstvima, segment tree treba podržavati tri operacije:
    
    1.  izmjenu u točki;
    2.  upit maksimuma na intervalu;
    3.  upit zbroja na intervalu.
    
    Izmjena u točki lako se implementira.
    
    Budući da su DFS indeksi podstabla uzastopni (bez obzira na dekompoziciju), za izmjenu podstabla nekog čvora dovoljno je izmijeniti taj uzastopni interval DFS indeksa.
    
    Pitanje je kako izmijeniti/upitati put između dvaju čvorova.
    
    Prisjetimo se kako smo **binary liftingom računali LCA**. Najprije smo **dva čvora doveli na istu visinu, a zatim ih zajedno pomicali prema gore**. Istu ideju možemo primijeniti i na heavy-light dekompoziciju.
    
    Tijekom skakanja prema gore: ako je trenutačni čvor na teškom lancu, skačemo na vrh tog lanca; ako nije na teškom lancu, skačemo za jedan čvor prema gore. Tako dok dva čvora ne postanu jednaka. Usput ažuriramo/upitamo informacije intervala.
    
    Za svaki upit prolazimo najviše $O(\log n)$ teških lanaca, a složenost segment treea na svakom lancu je $O(\log n)$, pa je ukupna vremenska složenost $O(n\log n+q\log^2 n)$. U praksi broj teških lanaca teško doseže $O(\log n)$ (može se zasititi potpunim binarnim stablom), pa dekompozicija u pravilu ima malu konstantu.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_1.cpp"
    ```

Zatim šablonski zadatak s heavy-light dekompozicijom i operacijom promjene korijena.

???+ example "[LOJ 139. Dekompozicija stabla na lance](https://loj.ac/p/139)"
    Zadano je stablo s $n$ čvorova (početni korijen je $1$); treba podržati sljedećih $m$ operacija:
    
    -   promjena korijena: čvor $u$ postaje novi korijen stabla;
    -   izmjena težina čvorova na putu: težine svih čvorova na putu između čvorova $u$ i $v$ (uključujući ta dva čvora) povećaju se za $w$;
    -   izmjena težina čvorova u podstablu: težine svih čvorova u podstablu s korijenom $u$ povećaju se za $w$;
    -   upit puta: zbroj težina svih čvorova na putu između čvorova $u$ i $v$ (uključujući ta dva čvora);
    -   upit podstabla: zbroj težina svih čvorova u podstablu s korijenom $u$.
    
    $1 \le n,m \le 10^5$.

??? note "Rješenje"
    Najprije pokrenemo DFS s korijenom $1$ i predobradimo informacije potrebne za heavy-light dekompoziciju. Radi jednostavnosti, stablo s korijenom $1$ zovemo „izvorno stablo”, a stablo nakon nekoliko promjena korijena „trenutačno stablo”. Tijekom operacija održavamo $\textit{root}$, korijen trenutačnog stabla. Budući da segment tree pohranjuje informacije u DFS poretku izvornog stabla, pri svakom upitu i izmjeni operacije na trenutačnom stablu treba pretvoriti u operacije na izvornom stablu.
    
    Za promjenu korijena jednostavno postavimo $\textit{root}\gets u$. Za operacije na putu, budući da promjena korijena ne utječe na put, odgovarajuću operaciju izvedemo izravno na izvornom stablu.
    
    Glavno je pitanje operacija na podstablu. Razlikujemo slučajeve prema međusobnom položaju $u$ i $\textit{root}$:
    
    -   $u = \textit{root}$: najposebniji slučaj, operacija se odnosi na cijelo stablo. Dovoljno je postaviti oznaku na korijen segment treea ili upitati odgovor u korijenu.
    -   $u$ je predak od $\textit{root}$ u izvornom stablu, tj. $u$ leži na jednostavnom putu od $1$ do $\textit{root}$.
    
        To je slučaj koji najviše zaslužuje pozornost. Definiramo $v$ kao čvor najmanje dubine, osim $u$, na jednostavnom putu od $u$ do $\textit{root}$ u izvornom stablu; uočavamo da je dio izvornog stabla izvan $v$ i njegova podstabla upravo $u$ i njegovo podstablo u trenutačnom stablu.
    
        Razmotrimo kako učinkovito pronaći $v$. Najprije postavimo $v\gets\textit{root}$, a zatim skačemo prema gore po teškim lancima dok ne bude $\operatorname{dep}(\operatorname{top}(v))\le\operatorname{dep}(u)+1$.
    
        -   Ako je $\operatorname{dep}(\operatorname{top}(v))=\operatorname{dep}(u)+1$, postavimo $v\gets\operatorname{top}(v)$. Tada je $v$ lako dijete od $u$.
        -   Ako je $\operatorname{dep}(\operatorname{top}(v))<\operatorname{dep}(u)+1$, tj. $\operatorname{dep}(\operatorname{top}(v))\le \operatorname{dep}(u)$, to znači da su $u,v$ na istom teškom lancu. Prema svojstvu da su DFS indeksi na istom teškom lancu uzastopni, traženi $v$ nužno zadovoljava $\operatorname{dfn}(v)=\operatorname{dfn}(u)+1$. Stoga možemo postaviti $v\gets\operatorname{rnk}(\operatorname{dfn}(u)+1)$.
    
        Primijetimo da se ta dva slučaja mogu spojiti: nakon skakanja možemo izravno postaviti
    
        $$
        v\gets\operatorname{rnk}(\operatorname{dfn}(\operatorname{top}(v))+\operatorname{dep}(u)+1-\operatorname{dep}(\operatorname{top}(v))).
        $$
    
        Lako se provjeri da je $v$ dobiven tim izrazom jednak $v$ dobivenom razlikovanjem slučajeva. Primjer implementacije koristi upravo taj izraz.
    
        Budući da podstablo od $v$ pokriva interval $[\operatorname{dfn}(v),\operatorname{dfn}(v)+\operatorname{siz}(v))$, dovoljno je operaciju izvesti na $[1,\operatorname{dfn}(v))\cup[\operatorname{dfn}(v)+\operatorname{siz}(v),n]$.
    -   Ostali slučajevi. Uočavamo da promjena korijena ne utječe na podstablo od $u$, pa ga održavamo na uobičajen način.
    
    Složenost je ista kao kod pristupa bez promjene korijena, $O(n\log^2 n)$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_4.cpp"
    ```

Na kraju jedan interaktivni zadatak, ujedno netradicionalna primjena dekompozicije.

???+ example "[Nauuo and Binary Tree](https://loj.ac/problem/6669)"
    Zadano je binarno stablo s korijenom $1$; smijete upitati udaljenost između bilo koja dva čvora, a treba odrediti roditelja svakog čvora.
    
    Broj čvorova ne premašuje $3000$, a smijete postaviti najviše $30000$ upita.

??? note "Rješenje"
    Najprije s $n-1$ upita možemo odrediti dubinu svakog čvora.
    
    Zatim roditelje određujemo po rastućoj dubini, tako da su pri određivanju roditelja nekog čvora svi njegovi preci već poznati.
    
    Prije određivanja roditelja nekog čvora napravimo heavy-light dekompoziciju poznatog dijela stabla.
    
    Pretpostavimo da u podstablu $u$ trebamo pronaći položaj čvora $k$; možemo upitati udaljenost između $k$ i donjeg kraja teškog lanca kojem pripada $u$, čime dalje određujemo položaj $k$; vidi sliku:
    
    ![](./images/hld2.png)
    
    Crvena isprekidana crta je teški lanac, $d$ je rezultat upita, tj. $\textit{dis}(k, \textit{bot}(u))$, a dubina od $v$ je $(\textit{dep}(k)+\textit{dep}(\textit{bot}(u))-d)/2$.
    
    Tada, ako $v$ ima samo jedno dijete, roditelj od $k$ je $v$; inače rekurzivno tražimo roditelja od $k$ u podstablu od $w$.
    
    Vremenska složenost $O(n^2)$, složenost broja upita $O(n\log n)$.
    
    Konkretno, neka je $T(n)$ broj upita potreban u najgorem slučaju da se u stablu veličine $n$ pronađe položaj novog čvora; dobivamo:
    
    $$
    T(n)\le
    \begin{cases}
    0&n=1\\
    T\left(\left\lfloor\frac{n-1}2\right\rfloor\right)+1&n\ge2
    \end{cases}
    $$
    
    $2999+\sum_{i=1}^{2999}T(i)\le 29940$; zapravo se ta gornja granica može dostići konstruiranim podacima, no uz malo slučajnog poremećaja (npr. korištenjem nestabilnog algoritma sortiranja pri sortiranju po dubini) broj upita teško premašuje $21000$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_2.cpp"
    ```

## Dekompozicija na duge lance

Dekompozicija na duge lance (long-path decomposition) u biti je samo drugi način dekompozicije na lance.

**Teško dijete** (heavy child) čvora jest ono njegovo dijete čije podstablo ima najveću dubinu. Ako takvih ima više, uzmemo bilo koje. Ako čvor nema djece, nema ni teško dijete.

**Laka djeca** sva su ostala djeca.

Brid od čvora do njegova teškog djeteta je **teški brid**.

Bridovi do ostale, lake djece su **laki bridovi**.

Niz nadovezanih teških bridova čini **teški lanac**.

Ako i osamljene čvorove smatramo teškim lancima, cijelo je stablo rastavljeno na niz teških lanaca.

Kao na slici (ova se dekompozicija može shvatiti i kao heavy-light dekompozicija i kao dekompozicija na duge lance):

![HLD](./images/hld.png)

Implementacija dekompozicije na duge lance slična je heavy-light dekompoziciji pa je ovdje nećemo razrađivati.

### Česte primjene

Najprije uočimo da je kod dekompozicije na duge lance broj prijelaza preko lakih bridova na putu od čvora do korijena reda $\sqrt{n}$.

??? info "Kako konstruirati podatke koji maksimiziraju broj prijelaza između lakih i teških bridova"
    Možemo konstruirati ovakvo binarno stablo T:
    
    Neka je parametar konstruiranog binarnog stabla $D$.
    
    Ako je $D \neq 0$, u lijevom djetetu konstruiramo binarno stablo s parametrom $D-1$, a u desnom djetetu lanac duljine $2D-1$.
    
    Ako je $D = 0$, konstruiramo samo jedan osamljeni list i završavamo poziv.
    
    Takva konstrukcija jamči da su svi bridovi na putu od osamljenog lista do korijena laki, a potreban je broj čvorova reda $D^2$.
    
    Dovoljno je uzeti $D=\sqrt{n}$.

#### Optimizacija DP-a dekompozicijom na duge lance

U pravilu DP koji se može optimizirati dekompozicijom na duge lance ima jednu dimenziju stanja koja je dimenzija dubine.

Možemo razmotriti optimizaciju DP-a na stablu dekompozicijom na duge lance.

Konkretno, stanje svakog čvora izravno nasljeđujemo od njegova teškog djeteta, a DP stanja lake djece spajamo „na silu”.

???+ example "[Codeforces 1009 F. Dominant Indices](http://codeforces.com/contest/1009/problem/F)"
    Zadano je korijensko stablo s $n$ vrhova, s korijenom u vrhu $1$.
    
    Niz dubina vrha $x$ definiran je kao beskonačan niz $[d_{x, 0}, d_{x, 1}, d_{x, 2}, \dots]$, gdje $d_{x, i}$ označava broj vrhova $y$ koji zadovoljavaju sljedeća dva uvjeta:
    
    -   $x$ je predak od $y$;
    -   jednostavni put od $x$ do $y$ prolazi točno $i$ bridova.
    
    Dominantni indeks (dominant index) niza dubina vrha $x$ (kraće: dominantni indeks vrha $x$) definiran je kao indeks $j$ za koji vrijedi:
    
    -   za sve $k < j$ vrijedi $d_{x, k} < d_{x, j}$;
    -   za sve $k > j$ vrijedi $d_{x, k} \le d_{x, j}$.
    
    Izračunajte dominantni indeks svakog vrha stabla.

??? note "Rješenje"
    Neka $f_{i,j}$ označava broj čvorova u podstablu i na udaljenosti j od i.
    
    Izravan grubi prijelaz ima vremensku složenost $O(n^2)$
    
    Razmotrimo da pri svakom prijelazu izravno naslijedimo DP polje i odgovor teškog djeteta, a zatim ih na toj osnovi ažuriramo.
    
    Najprije na početak DP polja teškog djeteta trebamo umetnuti element 1, koji predstavlja trenutačni čvor.
    
    Zatim DP polja sve lake djece na silu spojimo s DP poljem trenutačnog čvora.
    
    Uočimo da je duljina DP polja lakog djeteta jednaka duljini teškog lanca kojem lako dijete pripada, a zbroj duljina svih teških lanaca je $n$.
    
    Drugim riječima, ukupna vremenska složenost grubog spajanja lake djece je $O(n)$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_3.cpp"
    ```

Napomena: u pravilu se memorija za DP polje dodjeljuje odjednom za cijeli teški lanac, a različiti čvorovi na lancu imaju različite pokazivače na početni položaj.

Duljinu DP polja možemo izračunati prema najdubljem čvoru podstabla.

Naravno, tehnika optimizacije DP-a dekompozicijom na duge lance ima mnogo varijanti, uključujući, ali ne ograničavajući se na lijene oznake itd. Ovdje ih nećemo razrađivati.

Vidi [blog korisnika 租酥雨](https://www.cnblogs.com/zhoushuyu/p/9468669.html).

#### Traženje k-tog pretka dekompozicijom na duge lance

Dakle, upit: čvor do kojeg dolazimo skočimo li iz nekog čvora $k$ puta prema roditelju.

Najprije pretpostavimo da smo već predobradili $2^i$-te pretke svakog čvora.

Pretpostavimo sada da smo pronašli $2^i$-tog pretka upitanog čvora takvog da je $2^i \le k < 2^{i+1}$.

Odredimo čvorove teškog lanca kojem on pripada i popišemo ih u tablicu po dubini. Neka je duljina teškog lanca $d$.

Istodobno u predobradi za vrh svakog teškog lanca pronađemo njegove pretke od $1.$ do $d.$ i također ih stavimo u tablicu.

Prema svojstvu dekompozicije na duge lance, $k-2^i \le 2^i \leq d$, odnosno $k$-tog pretka tog čvora možemo u $O(1)$ očitati iz tablice tog teškog lanca.

Predobrada zahtijeva binary lifting za $2^i$-te pretke te predobradu tablice za svaki teški lanac.

Složenost predobrade $O(n\log n)$, složenost upita $O(1)$.

## Zadaci za vježbu

-   [„Luogu P3379” 【模板】Najniži zajednički predak (LCA)](https://www.luogu.com.cn/problem/P3379) (računanje LCA dekompozicijom ne treba strukturu podataka, dobro za vježbu)
-   [„JLOI2014” Vjeveričin novi dom](https://loj.ac/problem/2236) (može i razlikama na stablu)
-   [„HAOI2015” Operacije na stablu](https://loj.ac/problem/2125)
-   [„Luogu P3384” 【模板】Heavy-light dekompozicija / dekompozicija na lance](https://www.luogu.com.cn/problem/P3384)
-   [„Luogu P1505” \[Nacionalni kamp\] Putovanje](https://www.luogu.com.cn/problem/P1505)
-   [„NOI2015” Upravitelj paketa](https://uoj.ac/problem/128)
-   [„SDOI2011” Bojenje](https://www.luogu.com.cn/problem/P2486)
-   [„SDOI2014” Putovanje](https://hydro.ac/p/bzoj-P3531)
-   [„Luogu P3979” Daleka zemlja](https://www.luogu.com.cn/problem/P3979)
-   [„POI2014” Hotel, pojačana inačica](https://hydro.ac/p/bzoj-P4543) (optimizacija DP-a dekompozicijom na duge lance)
-   [Strategija](https://hydro.ac/p/bzoj-P3252) (optimizacija greedyja dekompozicijom na duge lance)
