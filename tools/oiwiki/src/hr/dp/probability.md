---
title: DP s vjerojatnostima
---

## Uvod

DP s vjerojatnostima (probability DP) služi za rješavanje problema s vjerojatnostima i očekivanjima; preporučujemo da se najprije upoznate sa sadržajem stranice [Vjerojatnost i očekivanje](../math/probability/exp-var.md). U pravilu se problemi s vjerojatnostima rješavaju petljom unaprijed, a problemi s očekivanjima petljom unatrag. Ako definirana jednadžba prijelaza stanja ima naknadni utjecaj (nije bez posljedica), potrebna je još i [Gaussova eliminacija](../math/numerical/gauss.md). DP s vjerojatnostima ispituje se i u kombinaciji s drugim gradivom, npr. sa [sažimanjem stanja](./state.md) ili s DP prijelazima na stablu.

## DP za vjerojatnost

Ovakvi se zadaci rješavaju računanjem unaprijed, tj. od početnog stanja prema rezultatu. Kao i u običnom DP-u, najteže je opisati jednadžbu prijelaza stanja; samo je zadatak zamotan u teoriju vjerojatnosti.

### Primjer

???+ example "[Codeforces 148D Bag of mice](https://codeforces.com/problemset/problem/148/D)"
    U vreći je $w$ bijelih i $b$ crnih miševa; princeza i zmaj naizmjence vade miševe iz vreće. Tko prvi izvuče bijelog miša, pobjeđuje; ako u vreći više nema miševa i nitko nije izvukao bijelog, pobjeđuje zmaj. Princeza svaki put izvuče jednog miša, a nakon što zmaj izvuče jednog miša, još jedan miš pobjegne iz vreće. Izvučeni i odbjegli miševi slučajni su. Princeza vuče prva. Kolika je vjerojatnost da princeza pobijedi?

??? note "Rješenje"
    Neka je $f_{i,j}$ vjerojatnost da princeza pobijedi ako je, kad je ona na potezu, u vreći $i$ bijelih i $j$ crnih miševa. Rubni uvjeti: $f_{0,j}=0$ jer bez bijelih miševa pobjeđuje zmaj, a $f_{i,0}=1$ jer je svaki izvučeni miš bijel pa princeza pobjeđuje.
    Promotrimo prijelaze za $f_{i,j}$:
    
    -   Princeza izvuče bijelog miša i pobjeđuje. Vjerojatnost je $\dfrac{i}{i+j}$.
    -   Princeza izvuče crnog, zmaj izvuče bijelog i zmaj pobjeđuje. Vjerojatnost je $\dfrac{j}{i+j}\cdot\dfrac{i}{i+j-1}$.
    -   Princeza izvuče crnog, zmaj izvuče crnog, pobjegne crni; prelazimo u $f_{i,j-3}$. Vjerojatnost je $\dfrac{j}{i+j}\cdot\dfrac{j-1}{i+j-1}\cdot\dfrac{j-2}{i+j-2}$.
    -   Princeza izvuče crnog, zmaj izvuče crnog, pobjegne bijeli; prelazimo u $f_{i-1,j-2}$. Vjerojatnost je $\dfrac{j}{i+j}\cdot\dfrac{j-1}{i+j-1}\cdot\dfrac{i}{i+j-2}$.
    
    Budući da računamo vjerojatnost princezine pobjede, drugi slučaj ne ulazi u račun. Treba još osigurati da su posljednja dva slučaja valjana, pa provjeravamo veličine $i,j$: za treći slučaj trebaju barem 3 crna miša, a za četvrti 1 bijeli i 2 crna.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_1.cpp"
    ```

### Zadaci za vježbu

-   [POJ3071 Football](http://poj.org/problem?id=3071)
-   [CodeForces 768D Jon and Orbs](https://codeforces.com/problemset/problem/768/D)

## DP za očekivanje

### Primjer

???+ example "[POJ2096 Collecting Bugs](http://poj.org/problem?id=2096)"
    Program ima $s$ podsustava i u njemu se može pojaviti $n$ vrsta bugova. Netko svaki dan pronađe jedan bug; taj bug pripada nekoj vrsti i nekom podsustavu. Vjerojatnost da bug pripada određenom podsustavu je $\dfrac{1}{s}$, a da pripada određenoj vrsti $\dfrac{1}{n}$. Odredi očekivani broj dana dok se ne pronađe svih $n$ vrsta bugova i bug u svakom od $s$ podsustava.

??? note "Rješenje"
    Neka je $f_{i,j}$ očekivani broj dana do ciljnog stanja ako je već pronađeno $i$ vrsta bugova i bugovi u $j$ podsustava. Ciljno je stanje pronaći $n$ vrsta bugova i bugove u $s$ podsustava. Dakle $f_{n,s}=0$, jer je cilj već postignut i nisu potrebni daljnji dani; rekurziju stoga pokrećemo od ciljnog stanja, a odgovor je $f_{0,0}$.
    
    Promotrimo prijelaze stanja za $f_{i,j}$:
    
    -   $f_{i,j}$: pronađeni bug pripada jednoj od već pronađenih $i$ vrsta i jednom od $j$ podsustava; vjerojatnost je $p_1=\dfrac{i}{n}\cdot\dfrac{j}{s}$.
    -   $f_{i,j+1}$: pronađeni bug pripada jednoj od već pronađenih $i$ vrsta, ali ne i već pronađenom podsustavu; vjerojatnost je $p_2=\dfrac{i}{n}\cdot(1-\dfrac{j}{s})$.
    -   $f_{i+1,j}$: pronađeni bug ne pripada već pronađenoj vrsti, ali pripada jednom od $j$ podsustava; vjerojatnost je $p_3=(1-\dfrac{i}{n})\cdot\dfrac{j}{s}$.
    -   $f_{i+1,j+1}$: pronađeni bug ne pripada ni već pronađenoj vrsti ni već pronađenom podsustavu; vjerojatnost je $p_4=(1-\dfrac{i}{n})\cdot(1-\dfrac{j}{s})$.
    
    Iz linearnosti očekivanja dobivamo jednadžbu prijelaza stanja:
    
    $$
    \begin{aligned}
    f_{i,j} &= p_1\cdot f_{i,j}+p_2\cdot f_{i,j+1}+p_3\cdot f_{i+1,j}+p_4\cdot f_{i+1,j+1} + 1\\
    &= \dfrac{p_2\cdot f_{i,j+1}+p_3\cdot f_{i+1,j}+p_4\cdot f_{i+1,j+1}+1}{1-p_1}
    \end{aligned}
    $$

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_2.cpp"
    ```

???+ example "[„NOIP2016” Promjena učionice](http://uoj.ac/problem/262)"
    Niuniu ima nastavu u $n$ vremenskih odsječaka; u $i$-tom odsječku nastava je u učionici $c_i$, a može zatražiti premještaj u učionicu $d_i$; zahtjev se odobrava s vjerojatnošću $p_i$, a zatražiti se može premještaj za najviše $m$ sati. Nakon nastave u $i$-tom odsječku treba otići do učionice $i+1$-og odsječka. Zadan je graf s $v$ učionica i $e$ putova; kretanje troši snagu. Za koje sate zatražiti premještaj da bi očekivani ukupni utrošak snage na kretanje među učionicama bio najmanji, tj. odredi najmanji očekivani ukupni put.

??? note "Rješenje"
    Za ovaj neusmjereni povezani graf najprije Floydovim algoritmom izračunamo najkraće putove, što olakšava kasnije prijelaze stanja. Jedan korak kretanja je jedna faza (prelazak iz $i$-tog u $i+1$-i odsječak je jedan korak); u svakom koraku s vjerojatnošću $p_i$ stižemo u $d_i$ (ali među svim $d_i$ smijemo odabrati samo $m$), a s vjerojatnošću $1-p_i$ u $c_i$. Tražimo najmanji očekivani ukupni put nakon $n$ faza.
    
    Definiramo $f_{i,j,0/1}$ kao najmanji očekivani ukupni put ako smo u $i$-tom odsječku, uključujući ovaj odsječak iskoristili $j$ zahtjeva za promjenu, a u ovom odsječku učionicu mijenjamo (1) ili ne mijenjamo (0). Odgovor je $\min \{f_{n,i,0},f_{n,i,1}\} ,i\in[0,m]$. Pazite na rubne uvjete $f_{1,0,0}=f_{1,1,1}=0$.
    
    Promotrimo prijelaze stanja za $f_{i,j,0/1}$:
    
    -   Ako u ovoj fazi ne mijenjamo, tj. $f_{i,j,0}$. Možda smo došli iz stanja u kojem prethodno nismo mijenjali; tada je to $f_{i-1,j,0}+w_{c_{i-1},c_{i}}$. Možda smo došli iz stanja u kojem smo prethodno mijenjali; analizom pomoću uvjetne i potpune vjerojatnosti dobivamo $f_{i-1,j,1}+w_{d_{i-1},c_{i}}\cdot p_{i-1}+w_{c_{i-1},c_{i}}\cdot (1-p_{i-1})$. Jednadžba prijelaza stanja glasi:
    
    $$
    \begin{aligned}
    f_{i,j,0}=min(f_{i-1,j,0}+w_{c_{i-1},c_{i}},f_{i-1,j,1}+w_{d_{i-1},c_{i}}\cdot p_{i-1}+w_{c_{i-1},c_{i}}\cdot (1-p_{i-1}))
    \end{aligned}
    $$
    
    -   Ako u ovoj fazi mijenjamo, tj. $f_{i,j,1}$. Slično, možemo doći iz stanja u kojem prethodno nismo mijenjali ili iz stanja u kojem smo mijenjali. Kad ne mijenjamo, množimo s $(1-p_i)$, a kad mijenjamo, s $p_i$; dovoljno je proći sve moguće slučajeve i izračunati ih. Ovdje ne nabrajamo sve slučajeve prijelaza; vjerujemo da se nakon prethodnog primjera ovi prijelazi lako ispisuju.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_3.cpp"
    ```

Usporedbom tih dvaju problema vidimo da kod DP-a za očekivanje to tražimo li konkretnu vrijednost ili rješavamo optimizacijski problem donekle utječe na način prijelaza u jednadžbi; no i DP za vjerojatnost i DP za očekivanje neodvojivi su od znanja o vjerojatnosti i od koraka postavljanja i pojednostavljivanja formula, a detalji na koje treba misliti pri pisanju jednadžbe prijelaza također su slični.

### Zadaci za vježbu

-   [HDU3853 LOOPS](https://acm.hdu.edu.cn/showproblem.php?pid=3853)
-   [HDU4035 Maze](https://acm.hdu.edu.cn/showproblem.php?pid=4035)
-   [„SCOI2008” Bonus razina](https://www.luogu.com.cn/problem/P2473)

## DP s naknadnim utjecajem

### Primjer

???+ example "[CodeForces 24D Broken robot](https://codeforces.com/problemset/problem/24/D)"
    Zadana je matrica $n \times m$. Robot je na početku u retku $x$ i stupcu $y$; u svakom koraku s jednakom vjerojatnošću bira ostati na mjestu, pomaknuti se lijevo, desno ili dolje. Ako je robot na rubu, ne izlazi iz područja. Odredi očekivani broj koraka dok robot ne dođe do posljednjeg retka.

??? note "Rješenje"
    Za $m=1$ robot s vjerojatnošću $\dfrac{1}{2}$ ostaje na mjestu, a s vjerojatnošću $\dfrac{1}{2}$ pomiče se za jedno polje dolje; odgovor je $2\cdot (n-x)$.
    Neka je $f_{i,j}$ očekivani broj koraka da robot iz retka i i stupca j dođe do retka $n$; završno stanje je $f_{n,j}=0$.
    Budući da robot s jednakom vjerojatnošću bira ostati, pomaknuti se lijevo, desno ili dolje, prijelazi stanja za $f_{i,j}$ su:
    
    -   $f_{i,1}=\dfrac{1}{3}\cdot(f_{i+1,1}+f_{i,2}+f_{i,1})+1$
    -   $f_{i,j}=\dfrac{1}{4}\cdot(f_{i,j}+f_{i,j-1}+f_{i,j+1}+f_{i+1,j})+1$
    -   $f_{i,m}=\dfrac{1}{3}\cdot(f_{i,m}+f_{i,m-1}+f_{i+1,m})+1$
    
    Među redcima moguće je samo kretanje prema dolje, pa nema naknadnog utjecaja. Među stupcima moguće je kretanje lijevo i desno, pri čemu mogu nastati ciklusi, pa svojstvo odsutnosti naknadnog utjecaja ne vrijedi.
    Preuređivanjem jednadžbi dobivamo:
    
    -   $2f_{i,1}-f_{i,2}=3+f_{i+1,1}$
    -   $3f_{i,j}-f_{i,j-1}-f_{i,j+1}=4+f_{i+1,j}$
    -   $2f_{i,m}-f_{i,m-1}=3+f_{i+1,m}$
    
    Budući da rekurzija ide unatrag, svaki je $f_{i+1,j}$ poznat.
    Budući da ima $m$ stupaca, desna je strana vektor-stupac s $m$ redaka, a lijeva je strana matrica s $m$ redaka i $m$ stupaca. S proširenom matricom dobivamo matricu $m$ redaka i $m+1$ stupaca, a odgovor zatim nalazimo [Gaussovom eliminacijom](../math/numerical/gauss.md).

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_4.cpp"
    ```

### Zadaci za vježbu

-   [HDU 4418 Time Travel](https://acm.hdu.edu.cn/showproblem.php?pid=4418)
-   [„HNOI2013” Šetnja](https://loj.ac/problem/2383)

## Literatura

[kuangbin: Pregled DP-a s vjerojatnostima](https://www.cnblogs.com/kuangbin/archive/2012/10/02/2710606.html)
