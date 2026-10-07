---
title: Eulerovi grafovi
---

Ova stranica kratko predstavlja pojam Eulerova grafa, implementaciju i primjene.

## Definicija

U ovom tekstu razmatramo samo konačne grafove.

U teoriji grafova **Eulerov put (Eulerian path)** jest put koji prolazi svakim bridom grafa točno jednom, a **Eulerov ciklus (Eulerian circuit)** jest zatvoreni put koji prolazi svakim bridom grafa točno jednom.
Ako u grafu postoji Eulerov ciklus, graf se zove **Eulerov graf (Eulerian graph)**; ako u grafu ne postoji Eulerov ciklus, ali postoji Eulerov put, graf se zove **polu-Eulerov graf (semi-Eulerian graph)**.

??? warning "Upozorenje"
    Iako se u ovoj definiciji koristi riječ „put”, strogo govoreći ovdje se radi o pojmu „staza (trail)”. Eulerov put i Eulerov ciklus smiju svaki brid upotrijebiti točno jednom, ali ne ograničavaju koliko se puta prolazi kroz vrhove.

## Svojstva

U nastavku pretpostavljamo da promatrani graf $G$ nema izoliranih vrhova. Ta pretpostavka ne umanjuje općenitost, jer za graf $G$ s izoliranim vrhovima sljedeća svojstva i dalje vrijede za graf $G'$ dobiven uklanjanjem izoliranih vrhova iz $G$.

Za povezan graf $G$ sljedeća su tri svojstva međusobno ekvivalentna:

1.  $G$ je Eulerov graf;
2.  svi vrhovi grafa $G$ imaju paran stupanj (za usmjereni graf: ulazni stupanj svakog vrha jednak je izlaznom);
3.  $G$ se može rastaviti na uniju nekoliko bridno disjunktnih ciklusa.

Dokažimo ekvivalenciju.

Ako je graf $G$ Eulerov, tada svi vrhovi grafa $G$ imaju paran stupanj: krenemo li iz bilo kojeg vrha duž Eulerova ciklusa, stupanj svakog vrha $v$ jednak je broju izlazaka iz $v$ plus broj dolazaka u $v$. Budući da je prijeđena trajektorija zatvorena, za svaki vrh $v$ broj izlazaka jednak je broju dolazaka. Dakle stupanj svakog vrha ima oblik $2k$, tj. paran je.
Posebno, za usmjerene grafove istim se dokazom dobiva da je ulazni stupanj svakog vrha jednak izlaznom.

Ako svi vrhovi grafa imaju paran stupanj (ili jednak ulazni i izlazni stupanj), tada se $G$ može rastaviti na disjunktnu uniju nekoliko bridno disjunktnih ciklusa: krenimo iz bilo kojeg vrha $u$, odaberimo bilo koji izlazni brid $(u, v)$, prijeđimo u susjedni vrh $v$ i obrišimo $(u, v)$, i tako sve dok se ne vratimo u početni vrh $u$. Može se dokazati da se taj postupak nužno vraća u $u$: kad god stignemo u novi vrh $v \neq u$, prema prethodnom svojstvu preostali stupanj tog vrha je neparan, pa nužno postoji izlazni brid i postupak ne staje u $v$. (Drugim riječima, postupak staje onda i samo onda kad se vratimo u $u$.) Kako je broj bridova grafa $G$ konačan, postupak nužno staje nakon konačno mnogo koraka, pa se na kraju nužno vraćamo u $u$ i dobivamo ciklus. Primijetimo da smo u ovom dokazu koristili samo parnost stupnjeva, a nakon pronalaska i brisanja jednog ciklusa preostali graf i dalje ima to svojstvo, pa postupak možemo ponavljati dok graf ne postane prazan, čime $G$ rastavljamo na nekoliko bridno disjunktnih ciklusa.
Štoviše, svaki se takav zatvoreni put može u vrhovima kroz koje prolazi više puta rastaviti na disjunktnu uniju jednostavnih ciklusa, pa se u gornjem svojstvu zatvoreni putovi mogu zamijeniti jednostavnim ciklusima.

Ako se povezan graf $G$ može rastaviti na disjunktnu uniju nekoliko bridno disjunktnih ciklusa, tada je $G$ Eulerov graf: iz skupa bridno disjunktnih ciklusa svaki put odaberemo dva koja imaju zajednički vrh i spojimo ih u jedan, i to ponavljamo dok više nema dvaju ciklusa sa zajedničkim vrhom.
Može se dokazati da na kraju tog postupka preostaje točno jedan ciklus. Za bilo koja dva bridno disjunktna ciklusa $P_1, P_2$: ako $P_1$ i $P_2$ imaju zajednički vrh, spajamo ih izravno u njemu; inače uzmemo bilo koji vrh $v_1$ na $P_1$ i vrh $v_2$ na $P_2$; zbog povezanosti grafa $G$ postoji put $e_1, e_2, \ldots, e_k$ koji spaja $v_1$ i $v_2$, a svaki njegov brid $e_i$ sadržan je u nekom ciklusu $C_i$, pri čemu $P_1$ i $C_1$, $C_i$ i $C_{i+1}$, te $C_k$ i $P_2$ imaju zajedničke vrhove (ili je $C_i = C_{i+1}$, što ne utječe na dokaz). U tom se slučaju $P_1$ i $P_2$ mogu spojiti preko $C_1, \ldots, C_k$. Dakle, bilo koja dva ciklusa mogu se spojiti, pa na kraju nužno ostaje jedinstveni ciklus čiji je skup bridova unija svih bridno disjunktnih ciklusa, tj. $E(G)$; taj je ciklus Eulerov ciklus u $G$, pa je $G$ Eulerov graf.

Gornja svojstva ujedno su i kriterij za prepoznavanje Eulerovih grafova. Konkretno, graf je Eulerov ako i samo ako su vrhovi nenultog stupnja međusobno (jako) povezani i svi vrhovi imaju paran stupanj (ili jednak ulazni i izlazni stupanj).

Svojstva polu-Eulerovih grafova slična su svojstvima Eulerovih: polu-Eulerov graf ima točno dva vrha neparnog stupnja i upravo su to krajevi Eulerova puta. Spajanjem tih dvaju vrhova polu-Eulerov graf postaje Eulerov. Brisanjem bilo kojeg brida Eulerova grafa dobiva se polu-Eulerov graf.
Odatle slijedi kriterij za polu-Eulerove grafove: graf je polu-Eulerov ako i samo ako su vrhovi nenultog stupnja međusobno (jako) povezani i postoje točno dva vrha neparnog stupnja. Za usmjerene grafove drugi uvjet glasi: postoje točno dva vrha $u, v$ takva da $\deg^+(u) - \deg^-(u) = 1, \deg^+(v) - \deg^-(v) = -1$, a svi ostali vrhovi imaju jednak ulazni i izlazni stupanj.

## Konstrukcija Eulerova ciklusa/puta

Ovdje opisujemo najčešće korišten Hierholzerov algoritam, čija je ključna ideja treće od gornjih svojstava Eulerovih grafova: Eulerov graf može se rastaviti na uniju nekoliko bridno disjunktnih ciklusa.
Primijetimo da je u gornjem dokazu već opisan potpun i izvediv postupak spajanja bridno disjunktnih ciklusa u Eulerov ciklus, a uz prikladne strukture podataka (npr. pohranu ciklusa u strukturi nalik na povezanu listu) implementacija nije teška.

Konkretno, algoritam najprije u grafu nađe jedan ciklus kao trenutni ciklus; zatim svaki put odabere vrh trenutnog ciklusa s preostalim stupnjem različitim od nule, iz njega nađe novi jednostavan ciklus i spoji ga s trenutnim ciklusom; to ponavlja dok svi vrhovi trenutnog ciklusa ne budu bez preostalog stupnja, a trenutni je ciklus tada Eulerov ciklus.

Algoritam radi i za usmjerene grafove. Za polu-Eulerov graf kao trenutni put uzmemo put između dvaju vrhova neparnog stupnja, zatim svaki put odaberemo vrh nenultog stupnja, nađemo jednostavan ciklus i spojimo ga s trenutnim putom; na kraju dobivamo Eulerov put.

### Implementacija

Pseudokod Hierholzerova algoritma:

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{The edges of the graph } e , \text{ where each element in } e \text{ is } (u, v) \\
2 &  \textbf{Output. } \text{The vertex of the Euler Road of the input graph}.\\
3 &  \textbf{Method. } \\
4 &  \textbf{Function } \text{Hierholzer } (v) \\
5 &  \qquad circle \gets \text{Find a Circle in } e \text{ Begin with } v \\
6 &  \qquad \textbf{if } circle=\varnothing \\
7 &  \qquad\qquad \textbf{return } v \\
8 &  \qquad e \gets e-circle \\
9 &  \qquad \textbf{for} \text{ each } v \in circle \\
10&  \qquad\qquad v \gets \text{Hierholzer}(v) \\
11&  \qquad \textbf{return } circle \\
12&  \textbf{Endfunction}\\
13&  \textbf{return } \text{Hierholzer}(\text{any vertex})
\end{array}
$$

### Analiza vremenske složenosti

Vremenska složenost Hierholzerova algoritma je $O(|E| + |V|)$.

Primijetimo da u gornjoj analizi ispravnosti traženje jednostavnog ciklusa u Eulerovu ili polu-Eulerovu grafu (ili početnog puta u polu-Eulerovu grafu) **ne zahtijeva vraćanje (backtracking)**: dovoljno je stalno ići preostalim bridovima i traženi ciklus ili put sigurno ćemo naći, pri čemu se **svaki brid posjeti samo jednom**.
Da bismo to iskoristili, bridove grafa treba pohraniti u strukturi nalik na povezanu listu, npr. listama susjedstva ili ulančanim listama bridova (linked forward star), kako bismo svaki brid odmah nakon posjeta obrisali. Koristi li se obična matrica susjedstva, svako traženje brida košta $O(|V|)$, pa je ukupna složenost $O(|V||E|)$.

???+ note "Napomena"
    Zapravo bi točna složenost ovog algoritma trebala biti $O(|E|)$, a ne $O(|V| + |E|)$, jer se algoritam može implementirati tako da ovisi samo o bridovima, a ne o vrhovima: održavanjem zajedničke povezane liste preostalih bridova iz koje se traži sljedeći ciklus.

Ako treba ispisati leksikografski najmanji Eulerov put ili ciklus, bridove treba sortirati, pa je vremenska složenost $\Theta(|E|\log |E|)$ ili $\Theta(|E|)$ (uz counting sort ili radix sort).

### Primjene

Usmjereni Eulerovi grafovi mogu se upotrijebiti za računalno dekodiranje.

Neka je zadano $m$ slova; želimo konstruirati kružni disk s $m^n$ sektora, u svaki upisati jedno slovo, tako da svakih $n$ uzastopnih pozicija na disku odgovara nizu znakova duljine $n$. Nakon punog okreta ($m^n$ koraka) dobivamo $m^n$ međusobno različitih nizova duljine $n$ nad $m$ slova.

![](images/euler1.svg)

Konstruiramo sljedeći usmjereni Eulerov graf:

Neka je $S = \{a_1, a_2, \cdots, a_m\}$; konstruiramo $D=\langle V, E\rangle$ ovako:

$V = \{a_{i_1}a_{i_2}\cdots a_{i_{n-1}} |a_i \in S, 1 \leq i \leq n - 1 \}$

$E = \{a_{j_1}a_{j_2}\cdots a_{j_{n-1}}|a_j \in S, 1 \leq j \leq n\}$

Incidenciju vrhova i bridova u $D$ definiramo ovako:

iz vrha $a_{i_1}a_{i_2}\cdots a_{i_{n-1}}$ izlazi $m$ bridova: $a_{i_1}a_{i_2}\cdots a_{i_{n-1}}a_r, r=1, 2, \cdots, m$;

brid $a_{j_1}a_{j_2}\cdots a_{j_{n-1}}$ ulazi u vrh $a_{j_2}a_{j_3}\cdots a_{j_{n}}$.

![](images/euler2.svg)

Takav je $D$ povezan i svakom je vrhu ulazni stupanj jednak izlaznom (oba su $m$), pa je $D$ usmjereni Eulerov graf.

Nađemo bilo koji Eulerov ciklus $C$ u $D$, uzmemo posljednje slovo svakog brida u $C$ i ta slova, redom kojim se bridovi pojavljuju u $C$, upišemo kružno na disk.

## Primjer zadatka

???+ note "[Luogu P2731 Jahanje uz popravak ograde](https://www.luogu.com.cn/problem/P2731)"
    Zadan je neusmjereni graf s 500 vrhova; nađi u njemu Eulerov put ili Eulerov ciklus. Ako ima više rješenja, ispiši najmanje.
    
    U ovom zadatku Eulerov put ili ciklus ne mora proći kroz sve vrhove.
    
    Broj bridova m zadovoljava $1\leq m \leq 1024$.

??? note "Ideja rješenja"
    Zadatak je izravna primjena Hierholzerova algoritma.
    
    Za spremanje odgovora može se koristiti `std::stack<int>`, jer ako nađeno nije ciklus, taj dio mora doći na kraj.
    
    Pazi: graf se ne smije pohraniti matricom susjedstva, inače se vremenska složenost pogoršava na $\Theta(nm)$. Budući da bridove treba sortirati, preporučuje se pohrana ulančanim listama bridova (forward star) ili `std::vector`. Primjer koda koristi `std::vector`.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/euler/euler_1.cpp"
    ```

## Zadaci

-   [SGU 101 Domino](https://codeforces.com/problemsets/acmsguru/problem/99999/101)

-   [POJ 1780 Code](http://poj.org/problem?id=1780)

-   [Luogu P1127 Lanac riječi](https://www.luogu.com.cn/problem/P1127)

-   [Luogu P1333 Ruiruijevi štapići](https://www.luogu.com.cn/problem/P1333)

-   [Luogu P1341 Neuređeni parovi slova](https://www.luogu.com.cn/problem/P1341)

-   [Luogu P6066 \[USACO05JAN\]Watchcow S](https://www.luogu.com.cn/problem/P6066)

-   [Luogu P6628 \[Pokrajinski izbor 2020, skup B\] Put jorgovana](https://www.luogu.com.cn/problem/P6628)

-   [Luogu P3520 \[POI 2011\] SMI-Garbage](https://www.luogu.com.cn/problem/P3520)
