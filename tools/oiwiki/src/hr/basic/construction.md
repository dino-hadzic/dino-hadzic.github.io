---
title: Konstruktivni zadaci
---

Ova stranica kratko predstavlja konstruktivne zadatke.

## Uvod

Konstruktivni zadaci čest su tip zadataka na natjecanjima.

Po obliku, odgovor na zadatak često ima neku pravilnost, zbog koje se i pri brzom rastu veličine problema odgovor još može razmjerno lako dobiti.

To zahtijeva da pri rješavanju razmišljamo o tome kako rast veličine problema utječe na odgovor i može li se taj utjecaj poopćiti. Primjerice, pri osmišljavanju dinamičkog programiranja razmatramo kakav učinak ima prijelaz iz jednog stanja u sljedeće.

## Značajke

Vrlo uočljiva značajka konstruktivnih zadataka je velika sloboda: načina konstrukcije u jednom zadatku može biti mnogo, ali postoji neki razmjerno jednostavan koji zadovoljava uvjete. Čini se da to olabavljuje zahtjeve i olakšava zadatak, ali upravo zbog te slobode često nema jasnog smjera i ne znamo odakle krenuti.

Druga značajka je fleksibilan, raznolik oblik. Ne postoji opće rješenje ni recept za sve konstruktivne zadatke; teško je čak pronaći zajedničke crte u načinu razmišljanja.

## Primjeri

Slijedi nekoliko primjera koji čitatelju pomažu osjetiti ideje konstruktivnih zadataka i daju poticaj za razmišljanje. Preporučujemo da dobro promislite prije čitanja rješenja; također pozivamo sve da podijele zanimljive konstruktivne zadatke.

### Primjer 1

???+ note "[Codeforces Round #384 (Div. 2) C. Vladik and fractions](http://codeforces.com/problemset/problem/743/C)"
    Konstruiraj tri međusobno različita prirodna broja $x,y,z$ takva da za zadani $n$ vrijedi $\dfrac{1}{x}+\dfrac{1}{y}+\dfrac{1}{z}=\dfrac{2}{n}$.

??? note "Ideja rješenja"
    Način konstrukcije vidi se iz drugog primjera u zadatku.
    
    Rastavimo $\dfrac{2}{n}$ na $\dfrac{1}{n}+\dfrac{1}{n}$, a drugi član zapišimo kao $\dfrac{1}{n+1}+\dfrac{1}{n(n+1)}$. Dakle $n,n+1,n(n+1)$ je valjano rješenje. Posebno, za $n=1$ rješenja nema, jer je zbroj recipročnih vrijednosti triju različitih prirodnih brojeva najviše $1+\dfrac{1}{2}+\dfrac{1}{3}<2$.

### Primjer 2

???+ note "[Luogu P3599 Koishi Loves Construction](https://www.luogu.com.cn/problem/P3599)"
    Task1: odredi može li se, i konstruiraj, permutacija brojeva $1\dots n$ duljine $n$ čijih je $n$ prefiksnih suma međusobno različito modulo $n$.
    
    Task2: odredi može li se, i konstruiraj, permutacija brojeva $1\dots n$ duljine $n$ čijih je $n$ prefiksnih produkata međusobno različito modulo $n$.

??? note "Ideja rješenja"
    U oba zadatka za $n=1$ uzmemo permutaciju $[1]$. Dalje neka je $n>1$.
    
    Task1:
    
    Za neparan $n$ rješenje ne postoji; za paran $n$ možemo konstruirati niz oblika $n,1,n-2,3,\cdots$.
    
    Prvo, $n$ mora biti na prvom mjestu, inače bi prefiksne sume neposredno prije i poslije $n$ bile jednake modulo $n$;
    
    zatim razmotrimo kako konstruirati cijeli niz:
    
    konstruiramo niz prefiksnih suma pa iz njega izvedemo izvorni niz; razlike susjednih prefiksnih suma (uz prvi član) moraju biti međusobno različite modulo $n$, jer diferencijski niz prefiksnih suma odgovara izvornoj permutaciji.
    
    Zato pokušajmo s prefiksnim sumama koje su modulo $n$ oblika
    
    $$
    0,1,-1,2,-2,\cdots
    $$
    
    i lako se vidi da to zadovoljava sva ograničenja.
    
    Task2:
    
    Kad je $n$ složen broj različit od $4$, rješenje ne postoji; za $n=4$ posebno uzmemo $[1,3,2,4]$. Kad je $n$ prost, možemo konstruirati niz oblika $1,\dfrac{2}{1},\dfrac{3}{2},\cdots,\dfrac{n-1}{n-2},n$, gdje dijeljenje označava množenje [inverzom](../math/number-theory/inverse.md) modulo $n$ i uzimanje predstavnika iz $[1,n]$.
    
    Prvo kad rješenje postoji:
    
    za složen $n$ različit od $4$ nema rješenja. Za složen broj postoje dva manja broja $p,q$ s $p\times q \equiv 0 \pmod n$, npr. $(3\times6)\bmod 9=0$. Nakon što se pojave i $p$ i $q$, prefiksni produkt ostaje $0$, pa za složene brojeve osim $4$ nema rješenja. Posebno, $4=2\times 2$ nema takav par $p,q$, pa rješenje postoji.
    
    Kako konstruirati niz:
    
    kao u Task1, $1$ mora biti na prvom mjestu, inače bi prefiksni produkti prije i poslije $1$ bili jednaki; a $n$ mora biti na posljednjem mjestu, jer su svi prefiksni produkti nakon $n$ jednaki $0$ modulo $n$. Analizom primjera iz zadatka vidimo da u svima postoji valjano rješenje čiji su prefiksni produkti modulo $n$ redom $1,2,3,\cdots,n$, pa možemo konstruirati gore opisani niz. Preostaje dokazati da je tih $n$ brojeva međusobno različito.
    
    Ti su brojevi upravo inverzi brojeva $1 \cdots n-2$ uvećani za $1$, dakle različiti, i zadatak je riješen.

### Primjer 3

???+ note "[AtCoder Grand Contest 032 B](https://atcoder.jp/contests/agc032/tasks/agc032_b)"
    Za zadani cijeli broj $N$ konstruiraj neusmjeren graf s $N$ vrhova označenih $1\ldots N$ koji zadovoljava:
    
    -   graf je jednostavan i povezan;
    -   postoji cijeli broj $S$ takav da je za svaki vrh zbroj oznaka susjeda jednak $S$.
    
    Zajamčeno je da rješenje postoji.

??? note "Ideja rješenja"
    Analizom slučajeva $n=3,4,5$ dolazimo do ideje konstrukcije.
    
    Konstruiramo potpun $k$-partitan graf čiji svi dijelovi imaju jednak zbroj oznaka. Tada je $S$ za svaki vrh jednak i iznosi
    
    $$
    S=\dfrac{(k-1)\sum_{i=1}^{n}i}{k}.
    $$
    
    Ako je $n$ paran, sparimo vrhove s početka i kraja: $\{1,n\},\{2,n-1\}\cdots$.
    
    Ako je $n$ neparan, $n$ izdvojimo kao zasebnu grupu, a preostalih $n-1$ sparimo: $\{n\},\{1,n-1\},\{2,n-2\}\cdots$.
    
    Povezanost tako konstruiranog grafa za $n\ge 3$ lako se dokazuje i ovdje je ne raspisujemo.
    
    Zadatak je riješen.

### Primjer 4

???+ note "[BZOJ 4971 „Lydsy1708 月赛” Ruksak iz sjećanja](https://vjudge.net/problem/BZOJ-4971)"
    Nakon napornog radnog dana mali Q je zaspao. U snu se prisjetio kako je na početku fakulteta učio 0-1 ruksak; tada je kao brucoš riješio jednostavan zadatak o 0-1 ruksaku koji je glasio:
    
    Zadano je $n$ predmeta volumena $v_1,v_2,\ldots,v_n$. Izračunaj broj načina da se odabere podskup predmeta (moguće i prazan) ukupnog volumena točno $w$. Budući da odgovor može biti vrlo velik, ispiši ga modulo $P$.
    
    Zbog dugotrajnog noćnog rješavanja zadataka vidio je samo $w$ i $P$ iz ulaza primjera te izlaz $k$, ali ne i koliko predmeta ima ni kolikih volumena. Do buđenja mali Q nije vidio ni $n$ ni $v$; napiši program koji mu pomaže rekonstruirati ulaz primjera.
    
    Više testnih primjera; vrijedi $50\le w\le20000$, $1\le P\le2^{30}$, $0\le k\le\min(20000,P-1)$; treba ispisati $1\le n\le40$ predmeta s $1\le v_i\le20000$.

??? note "Ideja rješenja"
    Ovo je jedan od konstruktivnih zadataka s najvećom slobodom, pa je teško znati odakle početi.
    
    Budući da je $k<P$, možemo izravno konstruirati skup predmeta s točno $k$ načina.
    
    Jedna konstrukcija: uzmemo $i$ malih predmeta volumena $1$ i nekoliko velikih predmeta volumena $w-t$, gdje je $1\le i\le20$ i $0\le t\le i$. Budući da je $i<w$ i $w-t\ge w-20>w/2$, svaki način da se ruksak točno napuni mora sadržavati točno jedan veliki predmet.
    
    Neka je doprinos velikog predmeta volumena $w-t$ broju načina $C$; tada je $C=\dbinom{i}{t}$, a doprinosi različitih velikih predmeta se zbrajaju. I kad su volumeni jednaki, različiti predmeti broje se zasebno.
    
    Neka $f_{i,j}$ označava najmanji broj velikih predmeta uz $i$ jedinica kojim se dobiva točno $j$ načina.
    
    Za fiksni $i$ stavimo $f_{i,0}=0$, a ostala stanja na $+\infty$. Po rastućem $j$ računamo prijelaz neograničenog ruksaka:
    
    $$
    f_{i,j}=1+\min_{0\le t\le i;~C\le j}f_{i,j-C},\qquad 1\le j\le20000.
    $$
    
    Zapamtimo li $t$ koji postiže minimum, možemo rekonstruirati volumen $w-t$ svakog velikog predmeta. Računanjem za sve $0\le k\le20000$ dobivamo $\min_{1\le i\le 20}(i+f_{i,k})\le 29<40$, pa je ovaj raspon predobrade dovoljan.

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/basic/code/construction/construction_1.cpp"
    ```
