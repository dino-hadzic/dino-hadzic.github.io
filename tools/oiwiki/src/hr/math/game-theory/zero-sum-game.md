---
title: Igre nulte sume
---

Preduvjeti: [Uvod u teoriju igara](./intro.md)

U ovom članku razmatramo (dvoigračke) [igre nulte sume](./intro.md#igre-nulte-i-nenulte-sume).

U igri nulte sume zbroj isplata dvaju igrača uvijek je jednak nuli, pa dobitak jedne strane nužno znači gubitak druge. Igra nulte sume može se smatrati posebnim slučajem igre konstantne sume. Obrnuto, svaka igra konstantne sume može se dodavanjem ili oduzimanjem konstante svim isplatama jedne strane ekvivalentno pretvoriti u igru nulte sume, pa je dovoljno razmatrati samo igre nulte sume.

Igre nulte sume koje se često pojavljuju u algoritamskim natjecanjima mogu se ugrubo podijeliti u dvije vrste: sekvencijalne igre nulte sume i simultane igre nulte sume.

## Sekvencijalne igre nulte sume

U sekvencijalnoj igri nulte sume dva igrača naizmjence povlače poteze dok igra ne završi.

U sekvencijalnoj igri nulte sume funkcija isplate igrača ima rekurzivnu strukturu. Pozicije igre $S$ mogu se podijeliti u tri vrste: završne pozicije $S_0$, pozicije $S_1$ u kojima potez povlači igrač $1$ i pozicije $S_2$ u kojima potez povlači igrač $2$. Pretpostavimo da je u završnoj poziciji $s\in S_0$ isplata igrača $1$ jednaka $v(s)$, pa je isplata igrača $2$ u skladu s tim $-v(s)$. Stoga, kad je na potezu igrač $2$, maksimizirati njegovu isplatu isto je što i minimizirati isplatu igrača $1$. Iz toga slijedi da, ako obje strane igraju optimalno, najveća isplata $V(s)$ koju igrač $1$ može ostvariti u poziciji $s\in S$ zadovoljava sljedeću rekurziju:

$$
V(s) = \begin{cases}
v(s), & s \in S_0,\\
\max_{t\in s} V(t), & s\in S_1,\\
\min_{t\in s} V(t), & s\in S_2.
\end{cases}
$$

Pritom $t\in s$ znači da je $t$ sljedbenik pozicije $s$. To je upravo [ideja minimaxa](../../search/alpha-beta.md#algoritam-minimax).

Pri primjeni ovog algoritma na konkretne zadatke obično se koriste sljedeći postupci:

-   Ako igra ima malo pozicija, dovoljno je algoritam izravno implementirati grubom silom.

-   Ako igra ima vrlo velik broj pozicija bez posebne strukture, može se razmotriti [Alpha–Beta odsijecanje](../../search/alpha-beta.md#alphabeta-odsijecanje) u kombinaciji s drugim algoritmima odsijecanja u pretraživanju.

-   Ako je u igri jedna pozicija često sljedbenik više pozicija, radi izbjegavanja ponovnog pretraživanja može se razmotriti memoizirano pretraživanje ili neki drugi algoritam dinamičkog programiranja.

-   Ako je konačna isplata igrača u igri zbroj isplata svih poteza prije završetka igre, modeliranje se može prikladno optimizirati. Konkretno, pretpostavimo da su pri dolasku u završnu poziciju $s\in S_0$ nizovi poteza igrača $i=1,2$ redom $\{a^{(i)}_j\}_{j=1}^{k_i}$, da je isplata potezu $a$ jednaka $w(a)$ te da je funkcija isplate igrača $1$

    $$
    v(s) = \sum_{j=1}^{k_1}w(a_j^{(1)}) - \sum_{j=1}^{k_2}w(a_j^{(2)}).
    $$

    Tada možemo definirati $\tilde V(s)$ kao najveću razliku između isplate igrača koji je na potezu i isplate njegova protivnika u dijelu igre nakon pozicije $s\in S$. Za početno stanje $s_0$ u kojem prvi potez povlači igrač $1$ vrijedi $V(s_0)=\tilde V(s_0)$, pa je za rješenje izvornog problema dovoljno izračunati $\tilde V(\cdot)$. Za $\tilde V(\cdot)$ vrijedi sljedeća rekurzija:

    $$
    \tilde V(s) = \begin{cases}
    0, & s \in S_0, \\
    \max_{t\in s} \{w(a_{s\to t}) - \tilde V(t)\}, & s\in S_1\cup S_2.
    \end{cases}
    $$

    Pritom $a_{s\to t}$ označava potez koji stanje $s$ prevodi u stanje $t$; ako takvih poteza ima više, uzima se onaj s najvećom isplatom $w(a)$.

-   Nepristrane kombinatorne igre sve su sekvencijalne igre nulte sume: dovoljno je isplatu pobjednika postaviti na $+1$, a isplatu gubitnika na $-1$. Tada je rekurzija za funkciju isplate $V(\cdot)$ zapravo upravo [lema](./impartial-game.md#graf-igre-i-stanja) kojom se određuju pobjedničke i gubitničke pozicije.

    Česta je varijanta ovakvih zadataka pitanje koliko najmanje poteza treba pobjedniku, odnosno koliko se najviše poteza gubitnik može održati. Za to je dovoljno primijetiti da, kad od završnih stanja krenemo BFS-om i prema lemi određujemo pobjedničke i gubitničke pozicije, broj sloja BFS-a u kojem je pozicija određena kao pobjednička ili gubitnička upravo je traženi broj poteza. Razlog je sljedeći: da bi pozicija bila određena kao pobjednička, dovoljno je da je jedan njezin sljedbenik gubitnička pozicija, pa ona uvijek nastaje iz gubitničkog sljedbenika s najmanjim brojem sloja; a da bi pozicija bila određena kao gubitnička, svi njezini sljedbenici moraju biti pobjedničke pozicije, pa ona uvijek nastaje iz pobjedničkog sljedbenika s najvećim brojem sloja.

    Ta se metoda jednako može poopćiti na općenite [igre na usmjerenim grafovima](./impartial-game.md#igra-na-usmjerenom-grafu).

### Primjer zadatka

???+ example "[Codeforces 794 E. Choosing Carrot](https://codeforces.com/problemset/problem/794/E)"
    Zadan je niz $\{a_i\}$ duljine $n$. Dva igrača, $1$ i $2$, naizmjence uzimaju po jedan broj s jednog od dvaju krajeva niza, sve dok u nizu ne ostane samo posljednji broj. Cilj igrača $1$ jest maksimizirati taj posljednji preostali broj, a cilj igrača $2$ minimizirati ga. Prije nego što igra službeno počne, igrač $1$ smije još povući $k$ poteza. Pretpostavimo da oba igrača tijekom cijelog postupka igraju optimalno. Za svaki $k = 0,1,2,\cdots,n-1$ odredite broj koji ostaje na kraju igre. Pritom je $1 \le n \le 3\times 10^5$.

??? note "Rješenje"
    Bez obzira na to kako obje strane uzimaju brojeve, preostali dio niza uvijek je cjelovit interval, pa se pozicija u igri može opisati samo intervalom $[l,r]$ i igračem $i=1,2$ koji je na potezu, a zadatak se može riješiti dinamičkim programiranjem. Neka je $f(l,r,i)$ broj koji ostaje na kraju igre kad je pozicija opisana s $(l,r,i)$. Iz prethodne analize slijedi da za $l < r$ ta funkcija zadovoljava jednadžbu prijelaza:
    
    $$
    \begin{aligned}
    f(l,r,1) &= \max\{f(l+1,r,2),f(l,r-1,2)\},\\
    f(l,r,2) &= \min\{f(l+1,r,1),f(l,r-1,1)\}.
    \end{aligned}
    $$
    
    Rubni je uvjet $f(l,l,1)=f(l,l,2) = a_l$. Na temelju toga vrijednosti funkcije za sve moguće pozicije mogu se izračunati u vremenu $\Theta(n^2)$. Za svaki $k$ odgovor je
    
    $$
    g(k) = \max f(l,r,1) \text{ subject to } r - l + 1 = n - k.
    $$
    
    Taj algoritam ne prolazi ograničenja iz izvornog zadatka, pa treba razmisliti o optimizaciji prijelaza. Postoji mnogo načina da se to učini; ovdje dajemo samo jedan.
    
    Promatrajmo jednadžbe prijelaza kao operacije nad cijelim nizom. Dvije jednadžbe prijelaza redom znače da iz susjednih brojeva uzimamo maksimum odnosno minimum i tako dobivamo novi niz; nazovimo ih „operacija maksimizacije” i „operacija minimizacije”. Svaka operacija skraćuje niz za jedan. Svi intervali duljine $d$ daju ukupno $(n-d+1)$ rezultata, što odgovara nizu dobivenom primjenom $(d-1)$ operacija na početni niz. Osim toga, da bismo dobili rezultat $f(l,r,1)$, posljednja operacija mora biti operacija maksimizacije. Stoga se u tim nizovima operacija dvije vrste operacija izmjenjuju, a na kraju je uvijek operacija maksimizacije.
    
    Promotrimo kako dvije uzastopne operacije mijenjaju niz. Bez smanjenja općenitosti neka se najprije izvodi operacija minimizacije, a zatim operacija maksimizacije. Tada niz $a_1,a_2,a_3$ prelazi u
    
    $$
    \max\{\min\{a_1,a_2\},\min\{a_2,a_3\}\}.
    $$
    
    Ispitamo li sve moguće odnose veličina triju brojeva $a_1,a_2,a_3$, vidimo da je taj izraz uvijek jednak $a_2$, osim u slučaju $a_1 < a_2$ i $a_2 > a_3$ (tj. kad je $a_2$ strogi lokalni maksimum). Drugim riječima, ako niz nema nijedan strogi lokalni maksimum, jedini je učinak dviju uzastopnih operacija brisanje po jednog broja s početka i s kraja niza. To očito znatno pojednostavnjuje prijelaz. Preostaje samo jedno pitanje: kako osigurati da niz nema nijedan strogi lokalni maksimum? Zapravo, dovoljno je na niz jednom primijeniti operaciju maksimizacije i strogih lokalnih maksimuma više neće biti. Zato se rezultati svih parnih brojeva operacija mogu dobiti tako da se na niz dobiven primjenom dviju operacija na početni niz redom brišu parovi brojeva s početka i s kraja, a rezultati svih neparnih brojeva operacija tako da se na niz dobiven primjenom jedne operacije na početni niz redom brišu parovi brojeva s početka i s kraja. (Slučaj nula operacija, tj. $k=n-1$, u kojem je odgovor $\max_i a_i$, treba obraditi zasebno.)
    
    Budući da je potrebno najviše $3$ puta primijeniti operaciju na cijeli niz, a za izračun odgovora zatim trebaju još samo $2$ prolaska, ukupna je vremenska složenost algoritma $\Theta(n)$.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/zero-sum-game/zero-sum-game-1.cpp"
    ```

### Zadaci za vježbu

-   [Luogu P2734 \[USACO3.3\] 游戏 A Game](https://www.luogu.com.cn/problem/P2734)
-   [Luogu P4576 \[CQOI2013\] 棋盘游戏 (Igra na ploči)](https://www.luogu.com.cn/problem/P4576)
-   [Luogu P7097 \[yLOI2020\] 牵丝戏 (Lutkarska igra)](https://www.luogu.com.cn/problem/P7097)
-   [Codeforces 388 C. Fox and Card Game](https://codeforces.com/problemset/problem/388/C)
-   [Codeforces 794 E. Choosing Carrot](https://codeforces.com/problemset/problem/794/E)
-   [Codeforces 1628 D2. Game on Sum (Hard Version)](https://codeforces.com/problemset/problem/1628/D2)
-   [Luogu P3210 \[HNOI2010\] 取石头游戏 (Igra uzimanja kamenčića)](https://www.luogu.com.cn/problem/P3210)

## Simultane igre nulte sume

U simultanoj igri nulte sume oba igrača povlače potez istodobno.

Simultane igre nulte sume obično se prikazuju matricom isplata. Pretpostavimo da je skup poteza igrača $i=1,2$ jednak $A_i$ te da su, kad igrači $i=1,2$ redom povuku poteze $a_i\in A_i$, isplate dvaju igrača redom $v(a_1,a_2)$ i $-v(a_1,a_2)$.

???+ example "Primjer"
    Promotrimo igru kamen-škare-papir. Neka pobjeda donosi $1$ bod, poraz $-1$ bod, a neriješeno $0$ bodova. Tada se isplate dvaju igrača u igri mogu prikazati kao
    
    $$
    \begin{pmatrix}
    0,0 & 1,-1 & -1,1 \\
    -1,1 & 0,0 & 1,-1 \\
    1,-1 & -1,1 & 0,0
    \end{pmatrix}.
    $$
    
    I općenite simultane igre dvaju igrača mogu se prikazati u sličnom obliku, pa se nazivaju i [bimatrične igre](https://en.wikipedia.org/wiki/Bimatrix_game) (bimatrix game). Kod igara nulte sume matrica isplata igrača $1$ i matrica isplata igrača $2$ međusobno su suprotne, pa je dovoljno promatrati samo matricu isplata igrača $1$:
    
    $$
    V = (v(a_1,a_2))_{(a_1,a_2)\in A_1\times A_2} = \begin{pmatrix}
    0 & 1 & -1 \\
    -1 & 0 & 1 \\
    1 & -1 & 0
    \end{pmatrix}.
    $$

Problem koji treba riješiti glasi: kako za zadanu matricu isplata $V = (v(a_1,a_2))_{(a_1,a_2)\in A_1\times A_2}$ odrediti optimalne strategije obaju igrača i njihove najveće isplate?

### Mješovite strategije

Za razliku od sekvencijalnih igara nulte sume, u simultanoj igri uloge dvaju igrača simetrične su. No budući da smo sekvencijalne igre nulte sume već riješili, razmotrimo sekvencijalnu inačicu simultane igre. Primjerice, pretpostavimo li da igrač $1$ povlači potez prvi, a igrač $2$ nakon njega, tada je prema prethodnoj raspravi isplata igrača $1$ na kraju igre dana s

$$
w_-=\max_{a_1\in A_1}\min_{a_2\in A_2} v(a_1,a_2)
$$

Budući da je potez igrača $1$ jednostrano vidljiv igraču $2$, to bi trebao biti najgori ishod koji igrač $1$ može postići. Simetrično, pretpostavimo li da igrač $2$ povlači potez prvi, isplata igrača $1$ dana je s

$$
w_+ = \min_{a_2\in A_2}\max_{a_1\in A_1} v(a_1,a_2)
$$

Budući da je potez igrača $2$ jednostrano vidljiv igraču $1$, to bi trebao biti najbolji ishod koji igrač $1$ može postići. Igrač $1$ trebao bi očekivati da će u stvarnoj igri ostvariti isplatu $w\in[w_-,w_+]$. Iako nejednakost $w_-\le w_+$ uvijek vrijedi (dokaz vidi u [teoremu o slaboj dualnosti](../linear-programming.md#princip-dualnosti)), jednakost ne mora vrijediti, pa se isključivo sredstvima analize sekvencijalnih igara ishod igre općenito ne može jednoznačno odrediti.

???+ example "Primjer (nastavak)"
    U igri kamen-škare-papir, ako se potezi povlače jedan za drugim, prvi igrač sigurno gubi, a drugi sigurno pobjeđuje. Prevedeno na matematički jezik, to je sljedeća nejednakost:
    
    $$
    w_- = -1 \le +1 = w_+.
    $$
    
    Ovdje $w_- = w_+$ ne vrijedi.

Gornja analiza zanemaruje ključni element simultane igre: igrač ne može točno predvidjeti protivnikov potez. Formalno, to znači da obje strane mogu primjenjivati neku slučajnu strategiju. U kontekstu sekvencijalne igre ta ideja ne pomaže, jer bez obzira na to kako prvi igrač nasumično izabere potez, drugi ga igrač uvijek može točno vidjeti i ciljano odgovoriti. No u simultanoj igri strateška neodređenost koju unosi slučajna strategija onemogućuje protivniku da se učinkovito usmjeri protiv našeg poteza.

???+ example "Primjer (nastavak)"
    U igri kamen-škare-papir, ako igrač $1$ uniformno nasumično bira jedan od triju poteza kamen, škare, papir, tada su, ovisno o potezu igrača $2$, moguće isplate igrača $1$
    
    $$
    \dfrac{1}{3}(0,1,-1)^T + \dfrac{1}{3}(-1,0,1)^T + \dfrac{1}{3}(1,-1,0)^T = (0,0,0)^T.
    $$
    
    Tada je, bez obzira na to kako igrač $2$ odabere potez, očekivana isplata igrača $1$ uvijek $0$. To je očito bolje od determinističkog odabira jednog poteza.

Time dolazimo do pojma mješovite strategije.

???+ abstract "Mješovita strategija"
    U simultanoj igri **mješovita strategija** (mixed strategy) igrača $i$, kraće **strategija**, jest funkcija $s_i:A_i\to[0,1]$ koja zadovoljava $\sum_{a_i\in A_i}s_i(a_i)=1$. Drugim riječima, strategija $s_i$ razdioba je vjerojatnosti na skupu poteza $A_i$ igrača $i$. Skup svih mješovitih strategija igrača $i$ označavamo sa $S_i=\Delta(A_i)$, pri čemu $\Delta(A_i)$ označava skup svih razdioba vjerojatnosti na $A_i$. Ako je $s_i$ degenerirana razdioba vjerojatnosti, tj. postoji $a\in A_i$ takav da je $s_i(a)=1$, strategija $s_i$ naziva se i **čista strategija** (pure strategy).

Isplata mješovite strategije očekivanje je isplata pojedinih poteza:

$$
v(s_1,s_2) = \sum_{a_1\in A_1}\sum_{a_2\in A_2}s_1(a_1)s_2(a_2)v(a_1,a_2).
$$

Promatramo li pojedini potez kao odgovarajuću čistu strategiju, skup poteza $A_i$ može se uložiti u skup (mješovitih) strategija $S_i$, a $v(s_1,s_2)$ definiran gornjim izrazom može se shvatiti kao proširenje $v(a_1,a_2)$ s $A_1\times A_2$ na $S_1\times S_2$.

### Von Neumannov teorem

Nakon uvođenja mješovitih strategija rezultati ideje maksimina i ideje minimaksa podudaraju se, pa je i ishod simultane igre nulte sume jednoznačno određen.

???+ note "Teorem (von Neumann)"
    U simultanoj igri nulte sume u kojoj su dopuštene mješovite strategije, ako obje strane igraju optimalno, najveća isplata igrača $1$ iznosi
    
    $$
    w = \max_{s_1\in S_1}\min_{s_2\in S_2} v(s_1,s_2) = \min_{s_2\in S_2}\max_{s_1\in S_1} v(s_1,s_2),
    $$
    
    a najveća isplata igrača $2$ iznosi $-w$.

??? note "Dokaz"
    Neka je $w = \max_{s_1\in S_1}\min_{s_2\in S_2} v(s_1,s_2)$. Promotrimo unutarnji problem minimizacije. Budući da je $v(s_1,s_2)=\sum_{a_2\in A_2}s_2(a_2)v(s_1,a_2)$, vrijedi $\min_{s_2\in S_2}v(s_1,s_2)=\min_{a_2\in A_2}v(s_1,a_2)$, a čista strategija koja odgovara optimalnom rješenju potonjeg problema optimalno je rješenje prvoga. Stoga je $w = \max_{s_1\in S_1}\min_{a_2\in A_2} v(s_1,a_2)$. Uvedemo li zatim pomoćnu varijablu $u$, problem se može zapisati kao
    
    $$
    w = \max_{u,s_1} u \text{ subject to }u \le \min_{a_2\in A_2} v(s_1,a_2).
    $$
    
    To je ograničenje ekvivalentno tome da $u\le v(s_1,a_2)$ vrijedi za sve $a_2\in A_2$. Naposljetku, uvrstimo li definiciju mješovite strategije $s_1$ i izraz za funkciju isplate $v(s_1,a_2)$, izvorni je problem ekvivalentan [problemu linearnog programiranja](../linear-programming.md)
    
    $$
    (P) \qquad
    \begin{aligned}
    w = \max_{u,s_1}\; & u\\
    \text{subject to }& \sum_{a_1\in A_1}s_1(a_1)v(a_1,a_2) \ge u,~\forall a_2\in A_2,\\
    & \sum_{a_1\in A_1}s_1(a_1) = 1,\\
    & s_1(a_1) \ge 0,~\forall a_1\in A_1.
    \end{aligned}
    $$
    
    Taj je problem očito dopustiv, a ciljna je funkcija ograničena, pa optimalno rješenje postoji. Prema [principu dualnosti](../linear-programming.md#princip-dualnosti) njegova je optimalna vrijednost jednaka optimalnoj vrijednosti dualnog problema:
    
    $$
    (D) \qquad
    \begin{aligned}
    w = \min_{t,s_2}\; & t\\
    \text{subject to }&\sum_{a_2\in A_2}s_2(a_2)v(a_1,a_2) \le t,~\forall a_1\in A_1,\\
    &\sum_{a_2\in A_2}s_2(a_2) = 1,\\
    &s_2(a_2)\ge 0,~\forall a_2\in A_2.
    \end{aligned}
    $$
    
    Ponovimo li prethodne korake, taj je problem ekvivalentan s $\min_{s_2\in S_2}\max_{s_1\in S_1}v(s_1,s_2)$. Time je teorem dokazan.

Optimalne strategije obiju strana čine [Nashovu ravnotežu](https://en.wikipedia.org/wiki/Nash_equilibrium) ove igre. Drugim riječima, ako obje strane odaberu optimalne strategije iz ravnoteže, nijedan igrač ne može strogo profitirati jednostranim odstupanjem od ravnotežne strategije.

### Svođenje na problem linearnog programiranja

Dokaz von Neumannova teorema ujedno pokazuje i kako se simultane igre nulte sume rješavaju. Neka su $n$ i $m$ redom brojevi poteza koje mogu povući igrači $1$ i $2$. Za zadanu matricu isplata $V\in\mathbf R^{n\times m}$ igrača $1$ može se riješiti sljedeći problem linearnog programiranja:

$$
\begin{aligned}
w = \max_{(u,s)\in\mathbf R\times\mathbf R^n}\; & u\\
\text{subject to }& V^Ts \ge u\mathbf 1,\\
& \mathbf 1^Ts = 1,\\
& s \ge 0.
\end{aligned}
$$

To je problem linearnog programiranja s $n+1$ varijablom i $m+1$ ograničenjem (ne računajući ograničenja nenegativnosti), koji se može učinkovito riješiti [simpleks metodom](../simplex.md). Budući da $u$ može biti negativan, može se najprije svim elementima matrice $V$ dodati ista konstanta $c$ tako da svi postanu pozitivni, pa se smije zahtijevati $u\ge 0$; to ne mijenja optimalnu strategiju, a dobiveni $w$ umanjen za $c$ vrijednost je izvorne igre. Optimalno rješenje $s$ koje algoritam vrati optimalna je (mješovita) strategija igrača $1$. Da bismo dobili optimalnu strategiju igrača $2$, dovoljno je iz simpleks tablice očitati dualne varijable (tj. cijene u sjeni) optimalnog rješenja tog problema.

### Zadaci za vježbu

-   [Luogu P4232 无意识之外的捉迷藏 (Skrivača izvan svijesti)](https://www.luogu.com.cn/problem/P4232)

## Literatura i bilješke

-   [Zero-sum game - Wikipedia](https://en.wikipedia.org/wiki/Zero-sum_game)
-   [Minimax theorem - Wikipedia](https://en.wikipedia.org/wiki/Minimax_theorem)
