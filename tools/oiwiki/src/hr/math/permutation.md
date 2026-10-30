---
title: Permutacije
---

Permutacije i razmještaji (arrangements) pojmovi su koji se vrlo često pojavljuju u raznim vrstama zadataka.

???+ warning "Ovaj članak ne govori o broju varijacija"
    Tema ovog članka potpune su permutacije, a ne broj varijacija (razmještaja) iz kombinatorike. Za sadržaj o broju varijacija pogledajte [Kombinatorika](./combinatorics/combination.md).

???+ info "Dogovor"
    Ako nije drukčije rečeno, u ovom se članku uvijek govori o konačnim skupovima.

## Definicija

Bijekcija (tj. obostrano jednoznačno preslikavanje) $\sigma$ skupa $X$ na samog sebe naziva se **permutacija** (permutation) skupa $X$. Ako na skupu $X$ postoji i relacija [totalnog uređaja](./order-theory.md#二元关系), tada se njegova permutacija često naziva i **(potpuni) razmještaj** (arrangement). Taj totalni uređaj naziva se prirodnim poretkom na skupu.

??? info "„Permutacija” i „razmještaj”"
    U kineskom kontekstu „permutacija” (置换) obično označava promjenu redoslijeda elemenata, a „razmještaj” (排列) obično označava slaganje elemenata u niz. Kad među elementima postoji prirodan poredak, ta su dva pojma jedno te isto: „razmještaj” se može shvatiti kao rezultat „permutacije”, a u odnosu na prirodan poredak elemenata redoslijed elemenata u „razmještaju” određuje „permutaciju”. Budući da se u ovom članku pri uporabi riječi „razmještaj” uvijek pretpostavlja da na skupu postoji prirodan poredak, ta se dva pojma u ovom članku ne razlikuju posebno.
    
    Naravno, i elementi bez prirodnog poretka mogu se „razmještati”. Takvi se „razmještaji” često pojavljuju u zadacima kombinatornog prebrojavanja. To je izvan opsega ovog članka.

Neka je veličina skupa $X$ jednaka $n$; tada je broj svih permutacija skupa $X$ jednak $n!$. Posebno, $0!=1$, tj. na praznom skupu postoji točno jedna permutacija – prazna permutacija.

???+ info "Oznake"
    Permutacije se bave odnosima pridruživanja među elementima, a ne time što su elementi konkretno. Zato se, kad govorimo o skupu veličine $n$, obično pretpostavlja da je riječ o skupu $\{1,2,\cdots,n\}$; kad je na skupu potreban prirodan poredak, obično se pretpostavlja prirodan poredak na prirodnim brojevima.

## Načini zapisa

Permutacije se mogu zapisati na više načina. Ovdje ćemo različite načine zapisa permutacija raspraviti na primjeru sljedeće permutacije.

$$
\sigma(1) = 2,\
\sigma(2) = 6,\
\sigma(3) = 5,\
\sigma(4) = 4,\
\sigma(5) = 3,\
\sigma(6) = 1.
$$

### Dvoredni zapis

Permutacija skupa $X=\{x_1,x_2,\cdots,x_n\}$ može se zapisati kao

$$
\sigma=\begin{pmatrix}x_1&x_2&\cdots&x_n\\
x_{p_1}&x_{p_2}&\cdots&x_{p_n}
\end{pmatrix}.
$$

To znači da permutacija $\sigma$ element $x_i$ preslikava u $x_{p_i}$. Ovdje, naravno, mora vrijediti $X=\{x_{p_1},x_{p_2},\cdots,x_{p_n}\}$. U dvorednom zapisu permutacije redoslijed pojavljivanja elemenata u prvom retku nije važan; važno je pridruživanje između dvaju redaka.

Primjerice, prethodni se primjer u dvorednom zapisu može napisati kao

$$
\sigma=
\begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 \\
2 & 6 & 5 & 4 & 3 & 1
\end{pmatrix},
$$

a može se, naravno, napisati i kao

$$
\sigma=
\begin{pmatrix}
6 & 5 & 4 & 3 & 2 & 1 \\
1 & 3 & 4 & 5 & 6 & 2
\end{pmatrix}.
$$

### Jednoredni zapis

Često na skupu $X$ postoji prirodan poredak. Ako se u dvorednom zapisu prvi redak podrazumijevano piše u prirodnom poretku i izostavi, permutacija se može zapisati kao

$$
\sigma=\sigma(1)\sigma(2)\cdots\sigma(n).
$$

To više nalikuje pojmu razmještaja u prirodnom jeziku. Zato se ta uređena n-torka ponekad naziva i „razmještaj”.

Prethodni se primjer u jednorednom zapisu može napisati kao

$$
\sigma=265431.
$$

Takav se jednoredni zapis često koristi za uspoređivanje različitih razmještaja.

### Zapis ciklusima

Postoji još kompaktniji način zapisa permutacija, koji se naziva zapisom permutacije ciklusima. On permutaciju prikazuje kao produkt niza disjunktnih ciklusa. U nastavku opisujemo korake kojima se zadana permutacija zapisuje ciklusima.

Za zadanu permutaciju $\sigma$ zapis ciklusima dobiva se sljedećim koracima:

1.  Ako u $X$ još postoji element koji nije zapisan, napišemo lijevu zagradu i zapišemo bilo koji takav element;
2.  Kad je posljednji zapisani element $x$,
    -   ako je $\sigma(x)$ već prije zapisan, napišemo desnu zagradu i vratimo se na korak 1;
    -   ako $\sigma(x)$ još nije zapisan, zapišemo $\sigma(x)$ i nastavimo s korakom 2;
3.  Ponavljamo gornje korake dok svi elementi skupa $X$ ne budu zapisani.

Unutar svakog para zagrada nalazi se jedan ciklus. Broj elemenata u zagradama naziva se duljinom pripadnog ciklusa. U praksi se ciklusi duljine jedan često izostavljaju.

Prethodni se primjer zapisom ciklusima može napisati kao

$$
\sigma=(126)(35)(4)=(126)(35).
$$

U identičnom preslikavanju svi ciklusi imaju duljinu jedan; ono se često zapisuje kao $(1)$, a ne izostavlja se u cijelosti.

## Kompozicija

Kompozicija permutacija kompozicija je preslikavanja. Kompozicija permutacija često se naziva i množenjem permutacija.

Za zadane dvije permutacije

$$
\sigma=\begin{pmatrix}x_1&x_2&\cdots&x_n\\ x_{p_1}&x_{p_2}&\cdots&x_{p_n}\end{pmatrix},\ \pi=\begin{pmatrix}x_{p_1}&x_{p_2}&\cdots&x_{p_n}\\ x_{q_1}&x_{q_2}&\cdots&x_{q_n}\end{pmatrix},
$$

njihov je produkt $\pi\circ\sigma$ jednak

$$
\pi\circ\sigma=\begin{pmatrix}x_1&x_2&\cdots&x_n\\
x_{q_1}&x_{q_2}&\cdots&x_{q_n}\end{pmatrix}.
$$

Jednostavno rečeno, najprije se primijeni preslikavanje $\sigma$, a zatim preslikavanje $\pi$. Uočite da se u gornjem dvorednom zapisu redoslijed drugog retka unutarnjeg preslikavanja $\sigma$ podudara s redoslijedom prvog retka vanjskog preslikavanja $\pi$.

Budući da su permutacije $\sigma$ i $\pi$ u biti dva preslikavanja, vrijedi $(\pi\circ\sigma)(x)=\pi(\sigma(x))$. Redoslijed računanja kompozicije permutacija ide zdesna nalijevo. Množenje permutacija nije komutativno, pa računanje u pogrešnom redoslijedu može dovesti do pogrešnog rezultata.

Uzastopna višestruka kompozicija iste permutacije naziva se potencijom permutacije i može se ubrzano izračunati [brzim potenciranjem](./binary-exponentiation.md#多次置换).

### Inverzna permutacija

Budući da je permutacija bijekcija, permutacija uvijek ima pripadnu inverznu permutaciju.

Za zadanu permutaciju

$$
\sigma=\begin{pmatrix}x_1&x_2&\cdots&x_n\\ x_{p_1}&x_{p_2}&\cdots&x_{p_n}\end{pmatrix},
$$

njezina je inverzna permutacija

$$
\sigma^{-1}=\begin{pmatrix}x_{p_1}&x_{p_2}&\cdots&x_{p_n}\\x_1&x_2&\cdots&x_n\end{pmatrix}.
$$

U zapisu ciklusima dovoljno je invertirati svaki ciklus da bi se dobio inverz izvorne permutacije; a da bi se invertirao ciklus, dovoljno je obrnuti redoslijed zapisivanja elemenata. Primjerice, zapis ciklusima inverzne permutacije permutacije $\sigma$ iz gornjeg primjera jest

$$
\sigma^{-1} = (621)(53) = (162)(35).
$$

Za zadani razmještaj brojeva $1\sim n$, on i niz sastavljen od položaja svakog elementa u tom razmještaju međusobno su inverzni razmještaji.

## Ciklusi

**Ciklus** (cycle) sam je po sebi posebna permutacija. Svojstvo je ciklusa da se iz bilo koje točke $x$ ciklusa uzastopnom primjenom permutacije $\sigma$ može doći do bilo koje točke $y$ ciklusa. Ciklus duljine $k$ naziva se i **$k$‑ciklus** ($k$-cycle). Uzastopnom primjenom $k$‑ciklusa $k$ puta dobiva se identično preslikavanje, tj. svaki se element vraća na svoj početni položaj.

Zapis permutacije ciklusima može se shvatiti kao zapisivanje permutacije u obliku produkta tih posebnih permutacija (tj. ciklusa), pa se zapis permutacije ciklusima može smatrati i **rastavom permutacije na cikluse** (cycle decomposition). Za svaku je permutaciju način rastava na produkt ciklusa, ne gledajući redoslijed, jedinstven. Ciklusi se mogu shvatiti kao osnovne jedinice od kojih se grade permutacije.

Rastav permutacije na cikluse ima jasno geometrijsko značenje. Ako svaki uređeni par $(x,\sigma(x))$ permutacije skupa $X$ shvatimo kao brid usmjerenog grafa s vrhovima iz $X$, ti su ciklusi upravo ciklusi (zatvoreni putovi) u tom grafu. Ako se permutacija $\sigma$ može rastaviti na $m$ ciklusa, to znači da pripadni usmjereni graf ima ukupno $m$ ciklusa (uključujući petlje). Ti su ciklusi, naravno, međusobno disjunktni.

### Fiksne točke

Elementi $1$‑ciklusa **fiksne** su **točke** (fixed point) permutacije. Za permutaciju $\sigma$ skupa $X$ skup fiksnih točaka permutacije $\sigma$ obično se označava $X^\sigma$, tj. $X^\sigma=\{x\in X:\sigma(x)=x\}$.

### Transpozicije

$2$‑ciklus naziva se i **transpozicija** (transposition). Drugim riječima, transpozicija je permutacija koja zamjenjuje položaje samo jednog para elemenata. Njezin je zapis ciklusima $(x_ix_j)$, što znači da zamjenjuje položaje elemenata $x_i$ i $x_j$.

Svaka se permutacija može zapisati kao produkt niza transpozicija. To je isto što i reći da se razmještaj u bilo kojem redoslijedu nizom operacija zamjene dvaju elemenata može vratiti u zadani uzlazni redoslijed. Upravo to rade algoritmi sortiranja temeljeni na zamjenama.

Štoviše, ispravnost [algoritma bubble sort](../basic/bubble-sort.md) zapravo pokazuje da se svaka permutacija može zapisati kao produkt niza susjednih transpozicija. **Susjedna transpozicija** (adjacent transposition) ovdje je transpozicija koja zamjenjuje samo susjedne elemente.

## Svojstva

U primjenama često treba obratiti pozornost na svojstva pojedine permutacije.

### Parnost

Način rastava ciklusa na transpozicije nije jedinstven. Primjerice,

$$
(123)=(13)(12)=(12)(23)=(12)(13)(12)(13).
$$

Međutim, kad se permutacija rastavlja na niz transpozicija, parnost broja potrebnih transpozicija je fiksna. Parnost broja transpozicija u rastavu permutacije naziva se i **parnošću** (parity) permutacije.

Permutacija koja se može rastaviti na produkt parnog broja transpozicija naziva se parnom permutacijom, a permutacija koja se može rastaviti na produkt neparnog broja transpozicija naziva se neparnom permutacijom. Za $n\ge2$ među permutacijama $n$ elemenata broj je neparnih i parnih permutacija jednak.

### Predznak

Prema parnosti permutacije može se definirati i **predznak** (sign) permutacije, koji se označava $\operatorname{sgn}\sigma$. Predznak parne permutacije definira se kao $+1$, a predznak neparne permutacije kao $-1$.

Predznak produkta permutacija jednak je produktu njihovih predznaka, tj.

$$
\operatorname{sgn}(\pi\circ\sigma)=\operatorname{sgn}
\pi\cdot\operatorname{sgn}\sigma.
$$

Drugim riječima, kompozicija dviju permutacija iste parnosti parna je permutacija, a kompozicija dviju permutacija različite parnosti neparna je permutacija. Taj je zaključak očit iz perspektive rastava na transpozicije.

Posebno, jedna transpozicija nužno mijenja parnost permutacije. To upravo objašnjava zašto je, iako način rastava na transpozicije nije jedinstven, parnost broja potrebnih transpozicija određena.

Predznak permutacije pojavljuje se u [Leibnizovoj formuli za determinantu](./linear-algebra/determinant.md#全排列方法定义).

### Red permutacije

**Red** (order) permutacije najmanji je pozitivan cijeli broj $a$ koji zadovoljava sljedeći uvjet: nakon $a$ ponavljanja te permutacije svi se elementi vraćaju na svoje početne položaje. Dakle

$$
\operatorname{ord}\sigma=\min\{a\in\mathbf N_+:\sigma^a=(1)\}.
$$

Na konačnom skupu red je svake permutacije konačan. To znači da se, krenuvši od početnog redoslijeda, uzastopnim miješanjem zadanog niza prema fiksnom obrascu razmještaj u konačnom vremenu uvijek može vratiti u početno stanje.

### Tip permutacije

Rastavimo li permutaciju $n$ elemenata na cikluse, **tip** (cycle type) permutacije multiskup je duljina ciklusa u tom rastavu. Duljine tih ciklusa čine jednu particiju broja $n$ na cijele brojeve. Ako u dobivenom rastavu ima ukupno $\alpha_k$ ciklusa duljine $k$, tip permutacije često se zapisuje kao

$$
1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n},
$$

a ti eksponenti zadovoljavaju $\sum_{k=1}^nk\alpha_k=n$.

Za zadani tip permutacije broj različitih permutacija jednak je

$$
\frac{n!}{1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}\alpha_1!\alpha_2!\cdots\alpha_n!}.
$$

??? note "Analiza"
    To je zato što se svaki razmještaj brojeva $1\sim n$ prema tipu permutacije može podijeliti na odgovarajući rastav na cikluse. No redoslijed ciklusa jednake duljine ne utječe na permutaciju, pa ukupan broj treba podijeliti s $\prod_k\alpha_k!$. Osim toga, unutar jednog ciklusa riječ je zapravo o kružnom razmještaju, pa ni izbor početne točke ne utječe na permutaciju, zbog čega treba podijeliti s $\prod_kk^{\alpha_k}$. Tako se dobiva gornja formula.

Ako je zadan samo broj ciklusa $k$ na koje se permutacija rastavlja, broj različitih permutacija jednak je [Stirlingovu broju prve vrste](./combinatorics/stirling.md#第一类斯特林数stirling-number) $\begin{bmatrix}n\\ k\end{bmatrix}$. Broj različitih tipova jednak je [broju particija](./combinatorics/partition.md) $p_n$ broja $n$.

Iz tipa permutacije lako se određuju svojstva poput reda i parnosti permutacije.

Budući da je red $k$‑ciklusa jednak $k$, a različiti su ciklusi međusobno disjunktni, red permutacije $\sigma$ jednak je

$$
\operatorname{lcm}\{k:\alpha_k>0\}.
$$

Slično, budući da je parnost $k$‑ciklusa suprotna parnosti broja $k$, parnost permutacije $\sigma$ jednaka je parnosti broja

$$
\sum_k(k-1)\alpha_k=\sum_{k}k\alpha_k-\sum_{k}\alpha_k=n-c(\sigma)
$$

Ovdje je $c(\sigma)$ broj ciklusa (uključujući $1$‑cikluse, tj. fiksne točke).

Tip permutacije ima važnu ulogu u [Pólyinu prebrojavanju](./combinatorics/polya.md).

## O razmještajima

Ako skup $X$ sam ima prirodan poredak, permutacija $\sigma$ često se naziva razmještajem i zapisuje jednorednim zapisom

$$
\sigma(1)\sigma(2)\cdots\sigma(n)
$$

Pazite da to ne pomiješate s ciklusima.

### Broj inverzija

Ako u razmještaju neki veći broj stoji ispred nekog manjeg broja, kažemo da ta dva broja čine **inverziju** (inversion) ili obrnuti poredak. Uspoređivanje se ovdje provodi prema prirodnom poretku.

Ukupan broj inverzija koje se pojavljuju u razmještaju naziva se **brojem inverzija** tog razmještaja. Broj inverzija razmještaja najmanji je broj susjednih transpozicija potreban da se razmještaj vrati u uzlazno sortirani niz. Stoga se parnost broja inverzija razmještaja podudara s parnošću pripadne permutacije. To može poslužiti kao ekvivalentna definicija parnosti permutacije.

Za računanje broja inverzija može se upotrijebiti [merge sort](../basic/merge-sort.md#inverzije) ili [Fenwick tree](../ds/fenwick.md#globalne-inverzije-globalni-dvodimenzionalni-parcijalni-poredak); vremenska je složenost obaju $O(n\log n)$. Objašnjenja obaju algoritama nalaze se u odgovarajućim poglavljima; ovdje dajemo njihove referentne implementacije.

??? example "Referentna implementacija"
    === "Merge sort"
        ```cpp
        --8<-- "docs/math/code/permutation/inversion_2.cpp"
        ```
    
    === "Fenwick tree"
        ```cpp
        --8<-- "docs/math/code/permutation/inversion_1.cpp"
        ```

### Poredak

Razmještaji se mogu uspoređivati. Budući da je svaki jednoredni zapis string, poredak razmještaja [leksikografski](../string/basic.md#leksikografski-poredak) je poredak tih stringova.

U zaglavlju `<algorithm>` standardne biblioteke C++-a mogu se upotrijebiti `prev_permutation` i `next_permutation` za pronalaženje prethodnog odnosno sljedećeg razmještaja trenutačnog razmještaja u leksikografskom poretku.

### Rang

Ako razmještaje $n$ elemenata ispišemo u leksikografskom poretku od najmanjeg do najvećeg, položaj nekog razmještaja u tom nizu njegov je rang. On uspostavlja bijekciju između razmještaja i pozitivnih cijelih brojeva i često se koristi za sažimanje stanja u zadacima vezanima za razmještaje.

U kineskoj natjecateljskoj zajednici taj se rang često naziva „Cantorovim razvojem” razmještaja, ali taj naziv nije sasvim precizan. Preciznije rečeno, **Cantorov razvoj** (Cantor expansion) ranga razmještaja odgovara **Lehmerovu kodu** (Lehmer code) tog razmještaja.

??? info "O „Cantorovu razvoju”"
    Kao što ime sugerira, Cantorov razvoj metoda je razvoja prirodnog broja u niz. Može se shvatiti kao posebna vrsta brojevnog sustava, koja se naziva i [faktorijelni brojevni sustav](./numeral-sys/base.md#混合基数进制). U tom sustavu različita mjesta imaju različite baze (radix). Primjerice, dekadski broj $463_{10}$ u faktorijelnom se sustavu može zapisati kao
    
    $$
    463_{10}=341010_{!}.
    $$
    
    To znači sljedeće
    
    $$
    463=3\times 5!+4\times 4!+1\times 3!+0\times 2!+1\times 1!+0\times 0!.
    $$
    
    Cantor je proučavao ovakve sustave s miješanim bazama, pa se zapis prirodnog broja znamenkama u tom sustavu često naziva i Cantorovim razvojem prirodnog broja.

??? example "Primjer"
    Čitatelji koji nisu upoznati s načinom računanja ranga mogu kroz ovaj jednostavan primjer shvatiti osnovnu ideju algoritma u nastavku.
    
    Izračunati rang razmještaja $\sigma=452631$ znači izračunati koliko je razmještaja leksikografski manjih od $\sigma$ i dodati jedan. Ideja je ovdje slična [DP-u po znamenkama](../dp/number.md): raspravljamo mjesto po mjestu.
    
    -   Izbor $1$. mjesta mora biti manji nego u $\sigma$, pa može biti samo iz $\{1,2,3\}$, a preostalih $5$ mjesta može se birati proizvoljno; ukupno $3\times 5!$ mogućih razmještaja;
    -   Ako i na $1$. mjestu izaberemo $4$, izbor $2$. mjesta mora biti manji nego u $\sigma$, pa može biti samo iz $\{1,2,3\}$ (ovdje je $4$ već izabrano), a preostala $4$ mjesta mogu se birati proizvoljno; ukupno $3\times 4!$ mogućih razmještaja;
    -   Slično, kad se izbor prvih $2$ mjesta podudara sa $\sigma$, izbor $3$. mjesta mora biti manji nego u $\sigma$, pa može biti samo iz $\{1\}$, a preostala $3$ mjesta mogu se birati proizvoljno; ukupno $1\times 3!$ mogućih razmještaja;
    -   Kad se izbor prvih $3$ mjesta podudara sa $\sigma$, izbor $4$. mjesta mora biti manji nego u $\sigma$, pa može biti samo iz $\{1,3\}$, a preostala $2$ mjesta mogu se birati proizvoljno; ukupno $2\times 2!$ mogućih razmještaja;
    -   Kad se izbor prvih $4$ mjesta podudara sa $\sigma$, izbor $5$. mjesta mora biti manji nego u $\sigma$, pa može biti samo iz $\{1\}$, a preostalo $1$ mjesto može se birati proizvoljno; ukupno $1\times 1!$ mogućih razmještaja;
    -   Kad se izbor prvih $5$ mjesta podudara sa $\sigma$, izborom $6$. mjesta ne može se dobiti razmještaj manji od $\sigma$, pa je ukupno $0\times 0!$ mogućih razmještaja.
    
    Stoga je rang razmještaja $\sigma$ jednak
    
    $$
    1+3\times 5!+3\times 4!+1\times 3!+2\times 2!+1\times 1!+0\times 0!=444.
    $$
    
    Za različite razmještaje ključno je odrediti koeficijente ispred faktorijela. Zapravo, ti su koeficijenti upravo broj elemenata koji stoje iza tog mjesta, a manji su od elementa na tom mjestu.

Iz primjera vidimo da se algoritam za računanje ranga zadanog razmještaja može podijeliti u dva koraka:

1.  Zadani razmještaj duljine $n$ pretvorimo u njegov Lehmerov kod, tj. niz $L_\sigma$ duljine $n$ čiji je $i$-ti član

    $$
    L_\sigma(i)=\#\{j>i:\sigma(j)<\sigma(i)\},
    $$

    dakle broj elemenata u razmještaju koji stoje iza $i$-tog mjesta, a manji su od $\sigma(i)$. On je jednak rangu zadanog elementa među još neiskorištenim elementima (umanjenom za jedan).

2.  Lehmerov kod shvatimo kao Cantorov razvoj prirodnog broja, izračunamo taj prirodni broj i dodamo jedan. Drugim riječima, konačni je rang jednak

    $$
    \operatorname{rank}\sigma=1+L_\sigma(1)(n-1)!+L_\sigma(2)(n-2)!+\cdots+L_\sigma(n)0!.
    $$

Za rješavanje obratnog problema, tj. određivanje razmještaja iz zadanog ranga, dovoljno je gornji postupak provesti obrnutim redom. Zbroj brojeva u Lehmerovu kodu dobivenom u tom postupku upravo je broj inverzija razmještaja.

Pri programskoj implementaciji ključno je moći brzo izračunati „rang zadanog elementa među još neiskorištenim elementima” (pri računanju ranga) i „element zadanog ranga među još neiskorištenim elementima” (pri računanju razmještaja); sve se to može održavati strukturama podataka poput [Fenwick treeja](../ds/fenwick.md) ili [segment treeja](../ds/seg.md). Vremenska složenost obiju operacija (izravne i obratne) jest $O(n\log n)$.

??? example "Referentna implementacija"
    === "Rang zadanog razmještaja"
        ```cpp
        --8<-- "docs/math/code/permutation/perm_rank.cpp"
        ```
    
    === "Razmještaj zadanog ranga"
        ```cpp
        --8<-- "docs/math/code/permutation/rank_perm.cpp"
        ```

## Literatura i napomene

-   [Permutation - Wikipedia](https://en.wikipedia.org/wiki/Permutation)
-   [Lehmer code - Wikipedia](https://en.wikipedia.org/wiki/Lehmer_code)
-   [Factorial number system - Wikipedia](https://en.wikipedia.org/wiki/Factorial_number_system)
