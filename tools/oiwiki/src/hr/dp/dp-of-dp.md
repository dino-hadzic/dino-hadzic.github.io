---
title: DP unutar DP-a
---

## Uvod

Ovaj članak predstavlja ideju „DP-a unutar DP-a” (DP of DP) i na dvama primjerima pokazuje kako se primjenjuje na konkretne probleme.

## Ideja

Takozvani „DP unutar DP-a” zapravo je metoda u kojoj se, tijekom dinamičkog programiranja, postupak rješavanja nekog potproblema (obično neki DP) apstrahira u automat (DFA), a zatim se na temelju tog automata osmišljava još jedna razina novog DP-a.

Ta se tehnika uglavnom primjenjuje na klasu problema **prebrojavanja nizova**, **vjerojatnosti** ili **očekivanja**. Tipičan problem ima sljedeću strukturu:

-   Zadani su skup znakova $\Sigma$ i skup $A\subseteq\Sigma^n$ „valjanih nizova” duljine $n$ nad njim. Ovisno o skupu znakova, nizovi mogu biti binarni nizovi, nizovi znamenki, nizovi stanja itd.
-   Za svaki konkretan niz $s\in\Sigma^n$ dinamičkim se programiranjem može provjeriti je li valjan (tj. $s\in A$), izračunati njegova težina ili neka povezana vrijednost.
-   Na kraju želimo izračunati broj svih nizova iz skupa $A$, njihovu ukupnu težinu, očekivanje itd.

Tada nabrajanje svih nizova nije izvedivo. Zato postupak „provjere je li niz valjan” (tj. unutarnji DP) apstrahiramo u [deterministički konačni automat](../misc/fsm.md#确定性有限状态自动机) (DFA). Općenito, za fiksni niz $s\in\Sigma^n$ funkcija stanja unutarnjeg DP-a može se zapisati kao $g(i,x;s)$, tj. vrijednost neke veličine kad je obrađen prefiks niza $s$ duljine $i$, a ostale komponente stanja su $x$. Odgovarajuća jednadžba prijelaza stanja unutarnjeg DP-a glasi

$$
g(i,\cdot;s) = G(g(i-1,\cdot;s),s_i).
$$

Drugim riječima, funkcija $g(i,\cdot;s)$ jednoznačno je određena prethodnom funkcijom $g(i-1,\cdot;s)$ i trenutnim znakom $s_i$. Ako funkciju $g(i,\cdot;s)$ promatramo kao jedno stanje automata, jednadžba prijelaza stanja unutarnjeg DP-a zadaje jedan prijelaz automata. Stoga automat $(Q,\Sigma,\delta,q_0,F)$ koji odgovara unutarnjem DP-u ima sljedeću strukturu:

-   skup stanja $Q$ skup je svih funkcija $g(i,\cdot;s)$ za sve moguće $s\in\Sigma^n$ i $i=0,1,\cdots,n$;
-   funkcija prijelaza $\delta:Q\times\Sigma\to Q$ upravo je $G$ iz jednadžbe prijelaza stanja unutarnjeg DP-a;
-   početno stanje $q_0$ obično je očito: to je početno stanje unutarnjeg DP-a;
-   skup prihvatljivih stanja $F$ odgovara svim valjanim nizovima $s\in A$.

Sama funkcija $g(i,\cdot;s)$ može biti prilično složena, pa je pri rješavanju konkretnih problema obično potrebno [sažimanje stanja](./state.md) ili kombiniranje s tehnikom minimizacije DFA kako bi se smanjio prostor stanja. To je i glavni razlog zašto DP unutar DP-a, u odnosu na DP grubom silom, znatno smanjuje vremensku i prostornu složenost.

Nakon što unutarnji DP apstrahiramo u DFA, na tom DFA možemo osmisliti novi DP za rješavanje izvornog problema, tj. vanjski DP. Radi jednostavnosti opisa uzmimo kao primjer jednostavan problem prebrojavanja. Funkcija stanja vanjskog DP-a definira se kao $f(i,q)$, tj. broj prefiksa duljine $i$ koji dovode u stanje $q\in Q$ automata. Njegova jednadžba prijelaza stanja glasi

$$
f(i,q) = \sum_{c\in\Sigma}\sum_{q'\in Q:\delta(q',c)=q} f(i-1,q').
$$

Početna je vrijednost, naravno, $f(0,q_0)=1$, a konačni se odgovor obično jednostavno računa iz $\{f(n,q):q\in F\}$. Vanjski DP zapravo je poseban slučaj [DP-a na DAG-u](./dag.md).

## Primjeri

Sljedeća dva primjera detaljno pokazuju opći postupak DP-a unutar DP-a.

### Primjer 1

???+ example "[Hero meet devil](https://www.luogu.com.cn/problem/P10614)"
    Zadan je niz znakova $S$ nad skupom znakova `ACGT`, pri čemu je $|S|\le 15$. Za svaki $0\leq i \leq |S|$ odredi koliko ima nizova $T$ duljine $m$ nad skupom znakova `ACGT` čija je duljina najduljeg zajedničkog podniza sa $S$ jednaka $i$.

??? note "Rješenje"
    Prvo što nam dolazi na um jest DP: neka $f_{i,j}$ označava broj nizova $T$ duljine $i$ čiji najdulji zajednički podniz sa $S$ ima duljinu $j$. No tako se ne može izvesti prijelaz; glavni je problem to što ne znamo kojim znakovima odgovara taj najdulji zajednički podniz.
    
    Promotrimo naivni postupak računanja najduljeg zajedničkog podniza. Neka $g_{i,j}$ označava duljinu najduljeg zajedničkog podniza prvih $i$ znakova niza $T$ i prvih $j$ znakova niza $S$; tada je
    
    $$
    g_{i,j} = \max\{g_{i-1,j},g_{i,j-1},g_{i-1,j-1}+[T_i=S_j]\}.
    $$
    
    Uočavamo da je za zadano $i$ dovoljno pamtiti vrijednosti jednodimenzionalnog niza $g_i$ da bismo točno održavali stanje najduljeg zajedničkog podniza niza $S$ i prvih $i$ znakova niza $T$. Budući da je duljina $S$ samo $15$, ta je ideja izvediva.
    
    Stoga iznova definiramo stanje: $f_{i,x}$ označava broj nizova $T$ duljine $i$ za koje DP niz u odnosu na $S$ (tj. $g_i$) ima stanje $x$. Na prvi pogled ovaj DP ima mnogo stanja, no uočavamo da je $g_{i,j}-g_{i,j-1}\in\{0,1\}$, pa možemo održavati niz razlika od $g_i$; broj stanja tada je $2^{|S|}$.
    
    Razmotrimo sada prijelaz. Lako se vidi da, ako znamo niz $g_i$ i znak $T_{i+1}$, naivnim LCS prijelazom (tj. gornjom DP jednadžbom) možemo izračunati $g_{i+1}$. Tako naivni LCS postaje unutarnji DP koji pomaže prijelazu $f$.
    
    Dakle, prolazimo po $T_{i+1}$, računamo stanje $x'$ u koje $x$ prelazi i $f_{i+1,x'}$ uvećavamo za $f_{i,x}$; time je prijelaz stanja vanjskog DP-a gotov. Na kraju, neka $\textit{ans}_i$ označava odgovor za duljinu LCS-a $i$; prolazimo po svim stanjima $x$ i $\textit{ans}_{\operatorname{popcount}(x)}$ uvećavamo za $f_{m,x}$.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/dp-of-dp/dp-of-dp_1.cpp"
    ```

### Primjer 2

???+ example "[\[ZJOI2019\] Mahjong](https://loj.ac/p/3042)"
    Pretpostavimo da pločice za mahjong imaju $n$ vrijednosti i da od svake vrijednosti postoje $4$ pločice. Definiramo skupinu (mentsu) kao tri pločice susjednih vrijednosti $i,i+1,i+2$ (niz) ili tri pločice iste vrijednosti $i,i,i$ (tris), a par kao dvije pločice iste vrijednosti $i,i$. Niz pločica za mahjong je pobjednički ako i samo ako se (promatran kao multiskup) može rastaviti na četiri skupine i jedan par, ili na sedam različitih parova. Zadano je početnih $13$ pločica; preostalih $4n-13$ pločica slučajno se jednoliko izmiješa i zatim se redom vuku. Koliki je očekivani broj pločica koje treba izvući da bi postojao pobjednički podniz? Odgovor treba dati modulo $998244353$.

??? note "Rješenje"
    Najprije, za ruku pločica važan je samo broj pločica svake vrijednosti, a ne njihov redoslijed. Stoga svaki prefiks bilo koje ruke možemo pretvoriti u niz duljine $n$ s vrijednostima $0\sim 4$ na svakom mjestu. Na početku je broj pločica $i$-te vrijednosti $a_i$, što ograničava $i$-ti broj $x_i$ u nizu na cijele brojeve iz $[a_i,4]$. Napomena: pretvoreni niz ne uzima u obzir redoslijed vučenja, dok niz pločica u zadatku redoslijed uzima u obzir.
    
    Neka $X$ označava najmanji broj vučenja nakon kojeg se može pobijediti. Izravno računanje očekivanja $\mathbf E[X]$ prilično je teško, pa razmotrimo sljedeću pretvorbu. Neka $h_i$ označava broj načina da se iz preostalih pločica odabere $i$ (različite pločice iste vrijednosti smatraju se različitima) tako da ruka **nije pobjednička**. Budući da u odgovarajućem nizu pločica tih $i$ pločica nužno stoji ispred preostalih $(4n-13-i)$ pločica, ali je redoslijed tih $i$ pločica i redoslijed preostalih $(4n-13-i)$ pločica proizvoljan, broj nizova pločica u kojima se nakon prvih $i$ izvučenih pločica ne može pobijediti jest
    
    $$
    h_i\cdot i!(4n-13-i)!.
    $$
    
    Budući da je ukupan broj nizova pločica $(4n-13)!$, vjerojatnost da se nakon prvih $i$ izvučenih pločica ne može pobijediti jest
    
    $$
    \mathbf P[X>i] = \dfrac{h_i\cdot i!(4n-13-i)!}{(4n-13)!}.
    $$
    
    Formulom zbroja repova dobivamo traženo očekivanje
    
    $$
    \mathbf E[X] = \sum_{i=0}^\infty\mathbf P[X>i] = 1 + \sum_{i=1}^{4n-13}\dfrac{h_i\cdot i!(4n-13-i)!}{(4n-13)!}.
    $$
    
    Time se problem sveo na računanje $h_i$. Rješavamo ga metodom DP-a unutar DP-a.
    
    Najprije promotrimo unutarnji DP, tj. dinamičko programiranje kojim provjeravamo odgovara li (pretvoreni) niz pobjedničkoj ruci. Slučaj sedam parova lakši je, pa se usredotočimo na prvi oblik pobjede. Neka $g_{0/1,i,j,k}$ označava najveći broj skupina nakon obrade prvih $i$ vrijednosti, ako je preostalo $j$ grupa $(i-1,i)$ i $k$ pločica $i$, te ako par ne postoji/postoji (tj. $0/1$). Ako DP za neki niz na kraju u $g_{1,n}$ sadrži broj veći ili jednak $4$, taj je niz pobjednički.
    
    Prijelaz stanja ovog DP-a prilično je složen. Razmotrit ćemo ga u dva koraka. Prvi korak: prijelaz $g_{0/1,i}$. To znači: ako trenutnoj ruci dodajemo $x_i$ pločica vrijednosti $i$, ali ne stvaramo novi par, kako se mijenja broj skupina. Očito, ako nakon dodavanja $x_i$ pločica vrijednosti $i$ želimo dobiti $\ell$ nizova, $j$ grupa $(i-1,i)$ i $k$ pojedinačnih pločica $i$, prijelaz treba doći iz $(g_{0/1,i-1})_{\ell,j}$ (taj izbor u najvećoj mjeri izbjegava rasipanje), a preostale pločice $(x_i-\ell-j-k)$ koristimo za što više trisova. Prolaskom po svim mogućnostima dobivamo sljedeću jednadžbu prijelaza:
    
    $$
    \tilde G(g_{0/1,i-1}, x_i)_{j,k} = \max\left\{(g_{0/1,i-1})_{\ell,j} + \ell + \left\lfloor\dfrac{x_i-\ell-j-k}{3}\right\rfloor:\ell+j+k\le x_i\right\}.
    $$
    
    Drugi korak: razmotrimo slučaj u kojem treba sastaviti par. Pri dodavanju $x_i$ pločica vrijednosti $i$ postoje tri prijelaza:
    
    -   iz $g_{0,i-1}$ dodavanjem $x_i$ pločica prelazimo u $g_{0,i}$;
    -   iz $g_{1,i-1}$ dodavanjem $x_i$ pločica prelazimo u $g_{1,i}$;
    -   ako je $x_i\ge 2$, iz $g_{0,i-1}$ dodavanjem $x_i-2$ pločica prelazimo u $g_{1,i}$.
    
    Time smo dobili sve prijelaze iz $g_{i-1}$ dodavanjem $x_i$ pločica u $g_i$.
    
    Nakon što smo riješili prijelaz stanja unutarnjeg DP-a, možemo izgraditi **automat za pobjedničku ruku**. Prijelazi automata upravo su prijelazi gornjeg unutarnjeg DP-a; još treba razmotriti kako prikazati svako stanje automata. Svako stanje odgovara jednoj mogućoj vrijednosti $g_i$. Ona ima tri dimenzije $(0/1,j,k)$. Budući da se $(i-1,i)$ i $i$ sačuvani u dimenzijama $j$ i $k$ koriste za buduće nizove, a tri jednaka niza uvijek se mogu preslagati u tri trisa, dovoljno je razmatrati potrebu za najviše $2$ jednaka niza, pa od svakog oblika treba čuvati najviše $2$, tj. $j,k\in\{0,1,2\}$. Stoga se $g_i$ može prikazati nizom $2\times 3\times 3$. Osim toga, radi održavanja pobjedničkog oblika sa sedam parova, svakom stanju treba dodati i brojač koji označava najveći broj parova koji se trenutno mogu sastaviti.
    
    Vrijednosti elemenata niza $g_i$ u načelu su iz $\{-\infty\}\cup\mathbf N$, ali budući da je broj skupina veći ili jednak $4$ uvijek pobjeda, svaki element možemo ograničiti na vrijednosti do $4$. Budući da pobjednički niz ostaje pobjednički dodavanjem bilo kojih pločica, idejom minimizacije DFA sva pobjednička stanja možemo sažeti u jedno stanje. Stoga za nepobjednička stanja svako mjesto u $g_1$ poprima vrijednosti iz $\{-\infty\}\cup\{0,1,2,3\}$, a svako mjesto u $g_0$ iz $\{-\infty\}\cup\{0,1,2,3,4\}$. U implementaciji se $-\infty$ prikazuje kao $-1$.
    
    Unatoč tome, svih je mogućih stanja i dalje vrlo mnogo, ukupno $1+7\times 5^9\times 6^9$. Njihovo nabrajanje nije realno. Zapravo se velika većina tih mogućnosti nikad ne pojavljuje u automatu za pobjedničku ruku. Da bismo izbjegli razmatranje stanja koja se zapravo ne pojavljuju, možemo idejom BFS-a od početnog stanja korak po korak širiti stanja, zaustavljajući se u pobjedničkom stanju. Tako dobiveni automat ima $N = 2092$ stanja.
    
    Na kraju promotrimo kako raditi DP na automatu za pobjedničku ruku (tj. vanjski DP). Neka $f_{i,j,k}$ označava broj načina da nakon obrade prvih $i$ vrijednosti, s ukupno $j$ izvučenih pločica, dođemo u stanje $k$ automata. Pri prijelazu prolazimo po broju izvučenih pločica $0\leq t\leq 4-a_i$, gdje je $a_i$ broj pločica vrijednosti $i$ među početnih $13$, prethodni broj načina množimo s brojem načina odabira $t$ od $4-a_i$ pločica, $\dbinom{4-a_i}{t}$, i zbrajamo. Formalno:
    
    $$
    f_{i,j+t,k'} \gets f_{i,j+t,k'} + \dbinom{4-a_i}{t}f_{i-1,j,k}.
    $$
    
    Ovdje je $k'=\delta(k,a_i+t)$ stanje u koje dolazimo dodavanjem $a_i+t$ pločica u stanje $k$ automata. Nakon završetka vanjskog DP-a možemo izračunati broj načina da nakon $i$ izvučenih pločica još nema pobjede, tj.
    
    $$
    h_i=\sum_{k\notin F} f_{n,i,k},
    $$
    
    gdje je $F$ skup pobjedničkih stanja. Uvrštavanjem u prije navedeni izraz dobivamo traženo očekivanje.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/dp-of-dp/dp-of-dp_2.cpp"
    ```

## Zadaci za vježbu

-   [CF979E Kuro and Topological Parity](https://codeforces.com/problemset/problem/979/E)
-   [\[TJOI2018\] Dan otvorenih vrata](https://loj.ac/p/2575)
-   [\[NOI2022\] Uklanjanje kamenja](https://loj.ac/p/3848)
