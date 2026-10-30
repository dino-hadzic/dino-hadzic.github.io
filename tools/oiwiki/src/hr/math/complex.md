---
title: Kompleksni brojevi
---

Ako ste već učili o kompleksnim brojevima, preskočite ovu stranicu.

Za učenje o kompleksnim brojevima potrebno je nešto osnova o vektorima; ako o vektorima još niste učili, pogledajte [stranicu o vektorima](../math/linear-algebra/vector.md).

## Kompleksni brojevi

### Uvod

???+ note "Napomena"
    Način uvođenja koji slijedi preuzet je iz kineskog srednjoškolskog udžbenika matematike (人教版 A 版必修二, izdanje People's Education Press, inačica A, obvezni svezak 2).

Gledano s gledišta jednadžbi, pitanje može li se iz negativnog realnog broja vaditi drugi korijen zapravo je pitanje ima li jednadžba $x^2+a=0 (a>0)$ rješenje, što se svodi na pitanje ima li jednadžba $x^2+1=0$ rješenje.

Ako se osvrnemo na dosadašnja proširenja skupova brojeva, vidimo da je svako proširenje bilo usko povezano sa stvarnom potrebom. Primjerice, da bi se riješio problem mjerenja dijagonale kvadrata, kao i problem da jednadžba poput $x^2-2=0$ nema rješenja u skupu racionalnih brojeva, skup racionalnih brojeva proširen je na skup realnih brojeva. Nakon proširenja, zbrajanje i množenje definirani u skupu realnih brojeva usklađeni su sa zbrajanjem i množenjem koji su prije bili definirani u skupu racionalnih brojeva, a zbrajanje i množenje zadovoljavaju komutativnost i asocijativnost te je množenje distributivno prema zbrajanju.

Slijedeći tu ideju, da bismo riješili problem da jednadžba poput $x^2+1=0$ nema rješenja u sustavu realnih brojeva, zamislimo da uvodimo novi broj $\mathrm{i}$ takav da je $x=\mathrm{i}$ rješenje jednadžbe $x^2+1=0$, tj. takav da je $\mathrm{i}^2=-1$.

Razmislimo: dodamo li novouvedeni broj $\mathrm{i}$ skupu realnih brojeva, želimo da se broj $\mathrm{i}$ i realni brojevi i dalje mogu zbrajati i množiti kao realni brojevi, te da zbrajanje i množenje zadovoljavaju komutativnost i asocijativnost, a množenje distributivnost prema zbrajanju. Od kojih se brojeva onda sastoji novi sustav brojeva dobiven proširenjem sustava realnih brojeva?

Prema gornjoj zamisli, umnožak realnog broja $b$ i $\mathrm{i}$ zapisujemo $b\mathrm{i}$, a zbroj realnog broja $a$ i $b\mathrm{i}$ zapisujemo $a+b\mathrm{i}$. Uočimo da se svi realni brojevi, kao i $\mathrm{i}$, mogu zapisati u obliku $a+b\mathrm{i}(a,b\in \mathbf{R})$, pa su svi ti brojevi u proširenom novom skupu brojeva.

### Definicija

Brojeve oblika $a+b\mathrm{i}$, gdje je $a,b\in \mathbf{R}$, zovemo **kompleksni brojevi**; pritom se $\mathrm{i}$ zove **imaginarna jedinica**, a skup svih kompleksnih brojeva zove se **skup kompleksnih brojeva** i označava $\mathbf{C}$.

Kompleksni brojevi obično se označavaju sa $z$, tj. $z=a+b\mathrm{i}$. Taj se oblik zove **algebarski oblik kompleksnog broja**. Pritom se $a$ zove **realni dio** kompleksnog broja $z$ i označava $\operatorname{Re}(z)$, a $b$ **imaginarni dio** kompleksnog broja $z$ i označava $\operatorname{Im}(z)$. Ako nije drukčije rečeno, uvijek je $a,b\in \mathbf{R}$.

Kompleksni broj $z$ je realan ako i samo ako je $b=0$; ako je $b\not = 0$, on je imaginaran, a ako je $a=0$ i $b\not = 0$, on je čisto imaginaran.

Odnos čisto imaginarnih, imaginarnih, realnih i kompleksnih brojeva prikazan je na slici.

![](./images/complex-relation.svg)

## Svojstva i operacije

### Geometrijsko značenje

Znamo da se brojevi oblika $a+b\mathrm{i}$ zovu kompleksni brojevi, dali smo definiciju i podjelu, a sada možemo istražiti i dublja svojstva.

Sve realne brojeve smjestili smo na brojevni pravac i otkrili da točke brojevnog pravca odgovaraju realnim brojevima jedan na jedan. Razmotrimo može li se tako postupiti i s kompleksnim brojevima.

Najprije definiramo **jednakost kompleksnih brojeva**: dva kompleksna broja $z_1=a+b\mathrm{i},z_2=c+d\mathrm{i}$ jednaka su ako i samo ako je $a=c$ i $b=d$.

Ta je definicija sasvim prirodna i ovdje je nećemo dodatno objašnjavati.

Drugim riječima, kompleksni broj $z=a+b\mathrm{i}$ možemo prikazati jedinstvenim uređenim parom realnih brojeva $(a,b)$. Tako, prisjetimo li se pravokutnog koordinatnog sustava, otkrivamo da **skup kompleksnih brojeva odgovara jedan na jedan skupu točaka pravokutnog koordinatnog sustava**. Dobro, pronašli smo jedno geometrijsko značenje kompleksnih brojeva.

Taj pravokutni koordinatni sustav tada više nije običan, jer njegove točke imaju posebno značenje – predstavljaju kompleksni broj; zato takav pravokutni koordinatni sustav zovemo **kompleksna ravnina**, os $x$ zovemo **realna os**, a os $y$ **imaginarna os**. Dalje kažemo: **skup kompleksnih brojeva odgovara jedan na jedan skupu svih točaka kompleksne ravnine**.

Prisjetimo se znanja o vektorima u ravnini: koordinatni zapis vektora također je uređeni par realnih brojeva $(a,b)$. Očito, kompleksni broj $z=a+b\mathrm{i}$ odgovara točki $Z(a,b)$ kompleksne ravnine, pa odgovara i vektoru $\overrightarrow{OZ}=(a,b)$ u ravnini; tako smo pronašli još jedno geometrijsko značenje kompleksnih brojeva: **skup kompleksnih brojeva odgovara jedan na jedan skupu vektora u kompleksnoj ravnini (realnom broju $0$ odgovara nul-vektor)**.

Prenoseći znanje o vektorima na kompleksne brojeve, definiramo **modul kompleksnog broja** kao modul (duljinu) vektora koji odgovara tom kompleksnom broju. Modul kompleksnog broja $z=a+b\mathrm{i}$ je $|z|=\sqrt{a^2+b^2}$.

Radi jednostavnosti kompleksni broj $z=a+b\mathrm{i}$ često zovemo točkom $Z$ ili vektorom $\overrightarrow {OZ}$ i dogovorno jednaki vektori predstavljaju isti kompleksni broj.

Iz znanja o vektorima također vidimo da se imaginarni brojevi ne mogu uspoređivati po veličini (dok realni mogu).

### Zbrajanje i oduzimanje

Za kompleksne brojeve $z_1=a+b\mathrm{i},z_2=c+d\mathrm{i}$ zbrajanje definiramo ovako:

$$
z_1+z_2=(a+c)+(b+d)\mathrm{i}
$$

Očito je zbroj dvaju kompleksnih brojeva opet kompleksan broj.

Usporedimo li sa zbrajanjem vektora, vidimo da zbrajanje kompleksnih brojeva slijedi pravilo zbrajanja vektora, što također potvrđuje ispravnost geometrijskog značenja kompleksnih brojeva.

Isto se tako može provjeriti da zbrajanje kompleksnih brojeva zadovoljava **komutativnost** i **asocijativnost**, tj.:

$$
\begin{aligned}
z_1+z_2&=z_2+z_1\\
(z_1+z_2)+z_3&=z_1+(z_2+z_3)
\end{aligned}
$$

Oduzimanje je inverzna operacija zbrajanja, pa pravilo oduzimanja možemo izvesti iz pravila zbrajanja i definicije jednakosti kompleksnih brojeva:

$$
z_1-z_2=(a-c)+(b-d)\mathrm{i}
$$

To se također slaže s oduzimanjem vektora.

### Množenje, dijeljenje i konjugiranje

Za kompleksne brojeve $z_1=a+b\mathrm{i},z_2=c+d\mathrm{i}$ množenje definiramo ovako:

$$
\begin{aligned}
z_1z_2&=(a+b\mathrm{i})(c+d\mathrm{i})\\
&=ac+bc\mathrm{i}+ad\mathrm{i}+bd\mathrm{i}^2\\
&=(ac-bd)+(bc+ad)\mathrm{i}
\end{aligned}
$$

Vidimo da je množenje dvaju kompleksnih brojeva slično množenju dvaju polinoma: dovoljno je $\mathrm{i}^2$ zamijeniti s $-1$ te zasebno sabrati realne i imaginarne dijelove.

Množenje kompleksnih brojeva po obliku je slično vektorskom produktu vektora.

Lako se vidi da množenje kompleksnih brojeva zadovoljava **komutativnost**, **asocijativnost** i **distributivnost prema zbrajanju**, tj.:

-   $z_1z_2=z_2z_1$
-   $(z_1z_2)z_3=z_1(z_2z_3)$
-   $z_1(z_2+z_3)=z_1z_2+z_1z_3$

Budući da vrijede ti zakoni, uočavamo da **formule za množenje iz polja realnih brojeva jednako vrijede i u polju kompleksnih brojeva**.

Dijeljenje je inverzna operacija množenja; izvedimo ga:

$$
\begin{aligned}
\frac{a+b\mathrm{i}}{c+d\mathrm{i}}&=\frac{(a+b\mathrm{i})(c-d\mathrm{i})}{(c+d\mathrm{i})(c-d\mathrm{i})}\\
&=\frac{ac+bd}{c^2+d^2}+\frac{bc-ad}{c^2+d^2}\mathrm{i} &(c+d\mathrm{i}\not =0)
\end{aligned}
$$

Budući da za vektore ne postoji dijeljenje, ovdje ne razmatramo vezu s vektorima.

Da bismo nazivnik učinili realnim, pomnožili smo s $c-d\mathrm{i}$; taj je izraz vrlo značajan.

Za kompleksni broj $z=a+b\mathrm{i}$ broj $a-b\mathrm{i}$ zovemo **konjugirano kompleksni broj** broja $z$ i obično ga označavamo $\bar z$. Uočavamo da su dva međusobno konjugirana kompleksna broja **simetrična s obzirom na realnu os**.

Za kompleksne brojeve $z,w$ konjugiranje ima sljedeća svojstva:

-   $z\cdot\bar{z}=|z|^2$
-   $\overline{\overline{z}}=z$
-   $\operatorname{Re}(z)=\dfrac{z+\bar{z}}{2}$, $\operatorname{Im}(z)=\dfrac{z-\bar{z}}{2}$
-   $\overline{z\pm w}=\bar{z}\pm\bar{w}$
-   $\overline{zw}=\bar{z}\bar{w}$
-   $\overline{z/w}=\bar{z}/\bar{w}$

### Argument i glavna vrijednost argumenta

Ako realnu jedinicu $1$ uzmemo za pozitivan vodoravni smjer, a imaginarnu jedinicu $\mathrm{i}$ za pozitivan okomiti smjer, dobivamo kompleksnu ravninu gledanu kroz pravokutne koordinate.

Položaj kompleksnog broja $z$ može se odrediti i pomoću polarnih koordinata $(r, \theta)$. Već smo spomenuli da je $r$ modul kompleksnog broja $z$.

Kut $\theta$ između pozitivnog smjera realne osi i vektora koji odgovara **nenul** kompleksnom broju $z=x+\mathrm{i}y$ zadovoljava relaciju:

$$
\tan \theta=\frac{y}{x}
$$

i zove se **argument** kompleksnog broja $z$; označava se:

$$
\theta= \arg z
$$

Svaki **nenul** kompleksni broj $z$ ima beskonačno mnogo argumenata, pa je $\arg z$ zapravo skup. Zapisom s velikim početnim slovom, $\operatorname{Arg} z$, označava se **jedna određena vrijednost** koja zadovoljava uvjet:

$$
-\pi<\operatorname{Arg} z \le \pi
$$

$\operatorname{Arg} z$ zove se **glavna vrijednost argumenta** ili **glavni argument**. Argument se dobiva iz glavne vrijednosti argumenta dodavanjem cjelobrojnog višekratnika (koji može biti nula ili negativan) od $2k\pi$, tj. $\arg z = \{\operatorname{Arg} z + 2k\pi \mid k\in \mathbf Z\}$.

Treba uočiti da zbroj dviju glavnih vrijednosti argumenta ne mora opet biti glavna vrijednost argumenta, dok je zbroj dvaju argumenata uvijek valjan argument.

Lik koji u kompleksnoj ravnini čine kompleksni brojevi modula manjeg od $1$ zovemo **jedinični krug**. Kompleksne brojeve modula jednakog $1$ zovemo **jedinični kompleksni brojevi**, a lik koji u kompleksnoj ravnini čine svi jedinični kompleksni brojevi zovemo **jedinična kružnica**. Kad ne može doći do zabune, jedinična kružnica katkad se također kraće zove jedinični krug.

Gledano kroz polarne koordinate, množenje i dijeljenje kompleksnih brojeva postaju vrlo jednostavni. Pri množenju kompleksnih brojeva moduli se množe, a argumenti zbrajaju. Pri dijeljenju kompleksnih brojeva moduli se dijele, a argumenti oduzimaju.

### Eulerova formula

???+ note "Eulerova formula (Euler's formula)[^ref1]"
    Za svaki realni broj $x$ vrijedi
    
    $$
    \mathrm{e}^{\mathrm{i}x}=\cos x+\mathrm{i}\sin x
    $$
    
    Nakon što dodatno definiramo [kompleksnu eksponencijalnu funkciju i kompleksne trigonometrijske funkcije](#eksponencijalna-funkcija-i-trigonometrijske-funkcije), formula se može proširiti na sve kompleksne brojeve.

### Eksponencijalna funkcija i trigonometrijske funkcije

Za kompleksni broj $z=x+\mathrm{i}y$ funkcija $f(z)=\mathrm{e}^x(\cos y+\mathrm{i}\sin y)$ zadovoljava $f(z_1+z_2)=f(z_1)f(z_2)$. Time je dana definicija **kompleksne eksponencijalne funkcije**:

$$
\exp z=\mathrm{e}^x(\cos y+\mathrm{i}\sin y)
$$

Na skupu realnih brojeva kompleksna eksponencijalna funkcija potpuno se podudara s realnom eksponencijalnom funkcijom. U kompleksnoj ravnini ima sljedeća svojstva:

-   Modul je uvijek pozitivan: $|\exp z|=\exp x>0$.
-   Argument: $\arg(\exp z)=\{y + 2k\pi \mid k\in\mathbf Z\}$.
-   Adicijski teorem: $\exp (z_1+z_2)=\exp (z_1)\exp (z_2)$.
-   Periodičnost: $\exp z$ je periodična funkcija s osnovnim periodom $2\pi \mathrm{i}$. Ako je svaki period funkcije $f(z)$ cjelobrojni višekratnik nekog perioda, taj se period zove **osnovni period**.

**Kompleksne trigonometrijske funkcije** (kraće i samo **trigonometrijske funkcije**) definiraju se ovako:

$$
\cos z=\frac{\exp (\mathrm{i}z)+\exp (-\mathrm{i}z)}{2}
$$

$$
\sin z=\frac{\exp (\mathrm{i}z)-\exp (-\mathrm{i}z)}{2\mathrm{i}}
$$

Ako uzmemo $z\in\mathbf{R}$, iz [Eulerove formule](#eulerova-formula) slijedi:

$$
\cos z=\operatorname{Re}\left(\mathrm{e}^{\mathrm{i}z}\right)
$$

$$
\sin z=\operatorname{Im}\left(\mathrm{e}^{\mathrm{i}z}\right)
$$

Na skupu realnih brojeva kompleksne trigonometrijske funkcije potpuno se podudaraju s realnim trigonometrijskim funkcijama. U kompleksnoj ravnini imaju sljedeća svojstva:

-   Parnost: sinus je neparna funkcija, a kosinus parna.
-   Trigonometrijski identiteti: uobičajeni trigonometrijski identiteti i dalje vrijede, npr. zbroj kvadrata jednak je $1$, formule za sinus i kosinus zbroja i razlike kutova itd.
-   Periodičnost: sinus i kosinus imaju osnovni period $2\pi$.
-   Nultočke: sve nultočke realnog sinusa i kosinusa čine sve nultočke kompleksnog sinusa i kosinusa. Ovo proširenje ne uvodi nove nultočke.
-   Neograničenost modula: modul kompleksnog sinusa i kosinusa može biti veći od bilo kojeg zadanog pozitivnog broja; više nije ograničen na $1$ kao kod realnog sinusa i kosinusa.

## Tri oblika kompleksnog broja

Gledajući kroz pravokutni i kroz polarni koordinatni sustav, kompleksni broj možemo zapisati u tri oblika.

**Algebarski oblik** kompleksnog broja služi za prikaz proizvoljnog kompleksnog broja.

$$
z=x+y\mathrm{i}
$$

Algebarski oblik prikladan je za računanje četiriju osnovnih operacija s kompleksnim brojevima: zbrajanja, oduzimanja, množenja i dijeljenja.

**Trigonometrijski oblik** i **eksponencijalni oblik** kompleksnog broja služe za prikaz nenul kompleksnih brojeva.

$$
z=r(\cos \theta +\mathrm{i}\sin \theta)=r \exp (\mathrm{i}\theta)
$$

Ta su dva oblika prikladnija za računanje množenja i dijeljenja kompleksnih brojeva te operacija koje slijede. Ako se koristimo samo funkcijama poznatima iz srednje škole, možemo upotrijebiti trigonometrijski oblik. Ako smo uveli kompleksnu eksponencijalnu funkciju, prikladnije je pisati ekvivalentan eksponencijalni oblik.

## Korijeni jedinice

Promotrimo rješenja jednadžbe $x^n=1$ u kompleksnim brojevima. Očito takvih rješenja ima $n$ i svih tih $n$ rješenja zovemo **$n$-ti (kompleksni) korijeni jedinice** ($n$-th root of unity). Iz znanja o kompleksnoj ravnini slijedi da $n$-ti korijeni jedinice dijele jediničnu kružnicu na $n$ jednakih dijelova.

Neka je $\omega_n=\exp\dfrac{2\pi \mathrm{i}}{n}$ (tj. jedinični kompleksni broj s argumentom $2\pi/n$); tada se skup rješenja jednadžbe $x^n=1$ zapisuje $\{\omega_n^k\mid k=0,1\cdots,n-1\}$, pri čemu je

$$
w_n^k = \exp\dfrac{2\pi k \mathrm{i}}{n} = \cos\dfrac{2\pi k}{n} + \mathrm{i}\sin\dfrac{2\pi k}{n}.
$$

Ako nije drukčije rečeno, pod $n$-tim korijenom jedinice u općenitom se tekstu misli na prvo rješenje počevši od $1$ u smjeru suprotnom od kazaljke na satu, tj. na gornji $\omega_n$; sva ostala rješenja mogu se prikazati potencijama od $\omega_n$.

???+ tip "Zašto se pod $n$-tim korijenom jedinice obično misli upravo na prvi?"
    Uglavnom radi praktičnosti u primjenama. Svi $n$-ti korijeni jedinice mogu se prikazati kao potencije prvog $n$-tog korijena jedinice $\omega_n$; štoviše, za svaki $k < n$ kompleksni broj $\omega_n$ nije $k$-ti korijen jedinice.

### Primitivni korijeni jedinice

Zapravo, među $n$-tim korijenima jedinice $\omega_n$ nije jedini koji ima takvo svojstvo. Elemente skupa

$$
\{\omega_n^k\mid 0\le k<n,~\gcd(n,k)=1\}
$$

zovemo **primitivni $n$-ti korijeni jedinice** ($n$-th primitive root of unity). Iz gornjeg izraza slijedi da primitivnih $n$-tih korijena jedinice ima ukupno $\varphi(n)$, gdje je $\varphi(n)$ [Eulerova funkcija](./number-theory/euler-totient.md).

Svaki primitivni korijen jedinice $\omega$ ima isto svojstvo kao gornji $\omega_n$: za svaki $0<k<n$ $k$-ta potencija od $\omega$ nije $1$, tj. $\omega$ nije $k$-ti korijen jedinice. Zato se pomoću bilo kojeg primitivnog korijena jedinice mogu generirati svi korijeni jedinice.

Da bismo razumjeli strukturu primitivnih $n$-tih korijena jedinice, trebamo sljedeće svojstvo korijena jedinice:

???+ note "Svojstvo"
    Za cijele brojeve $n$ i $k$ neka je $d=\gcd(n,k)$; tada je $\omega_n^k = \omega_{n/d}^{k/d}$.

??? note "Dokaz"
    Izravnim računom dobivamo
    
    $$
    w_n^k = \exp\dfrac{2\pi k\mathrm{i}}{n} = \exp\dfrac{2\pi (k/d)\mathrm{i}}{n/d} = \omega_{n/d}^{k/d}.
    $$

To znači da je, kad god je $\gcd(n,k)\neq 1$, $\omega_n^k$ nužno (primitivni) korijen jedinice reda $\dfrac{n}{\gcd(n,k)}$. Zato korijen jedinice $\omega_n^k$ koji ima gore opisano svojstvo nužno zadovoljava $\gcd(n,k)=1$. Upravo je to razlog zašto primitivni korijeni jedinice imaju gornju definiciju.

Osim toga, kao jednostavna posljedica ove analize vrijedi:

???+ note "Teorem"
    Kad $k$ prolazi svim djeliteljima od $n$, svi primitivni $k$-ti korijeni jedinice čine upravo jednu particiju skupa $n$-tih korijena jedinice. Štoviše, za $\ell\perp n$ preslikavanje $x\mapsto x^\ell$ daje bijekciju skupa $n$-tih korijena jedinice na sebe koja čuva tu particiju: primitivne korijene jedinice reda $k\mid n$ i dalje preslikava u primitivne $k$-te korijene jedinice.

Iako postoji mnogo izbora primitivnog korijena jedinice, prvi korijen $\omega_n$ ima najjednostavniji oblik, pa se u algoritamskim natjecanjima ipak najčešće koristi $\omega_n$. U nekim situacijama, radi veće učinkovitosti računanja, umjesto $\omega_n$ iz polja kompleksnih brojeva može se razmotriti i [primitivni korijen jedinice](./number-theory/residue.md#单位根) modulo neki modul.

## Kompleksni brojevi u programskim jezicima

### Kompleksni brojevi u C-u

Standard C99 uvodi zaglavlje `<complex.h>`.

Zaglavlje `<complex.h>` pruža tri tipa: `double complex`, `float complex` i `long double complex`.

Aritmetički operatori '+', '-', '\*' i '/' mogu se primjenjivati na proizvoljnu kombinaciju brojeva s pomičnim zarezom i kompleksnih brojeva. Ako je jedan od operanada izraza kompleksan, rezultat je kompleksan.

Zaglavlje `<complex.h>` pruža imaginarnu jedinicu `I`; kad je to zaglavlje uključeno, veliko slovo `I` ne može se koristiti kao ime varijable.

Za pojedini kompleksni broj `<complex.h>` pruža nekoliko operacija: funkcija `creal` izdvaja realni dio, `cimag` izdvaja imaginarni dio, `cabs` računa modul, a `carg` računa glavnu vrijednost argumenta.

Sve funkcije dolaze u tri inačice ovisno o tipu. Primjerice, funkcija `creal` postoji kao `creal`, `crealf` i `creall`, za tipove `double`, `float` odnosno `long double`. Inačica bez sufiksa obrađuje tip `double`. Sve funkcije u nastavku slijede isto pravilo i to više nećemo posebno naglašavati.

Povratne vrijednosti tih funkcija obični su brojevi s pomičnim zarezom. Običan broj s pomičnim zarezom može se izravno pridružiti kompleksnom broju, ali kompleksni broj ne može se izravno pridružiti broju s pomičnim zarezom; umjesto toga treba koristiti gornje operacije izdvajanja.

Funkcija `conj` računa konjugirano kompleksni broj; povratna vrijednost je kompleksan broj.

Funkcija `cexp` računa kompleksnu eksponencijalnu funkciju, `clog` glavnu vrijednost logaritma, `csin` sinus, `ccos` kosinus, a `ctan` tangens.

Funkcija `cpow` računa potenciju, `csqrt` drugi korijen, `casin` arkus sinus, `cacos` arkus kosinus, a `catan` arkus tangens. Sve te funkcije računaju glavne vrijednosti višeznačnih funkcija.

### Kompleksni brojevi u C++-u

Zaglavlje `<ctype.h>` iz C-a u C++-u postaje `<cctype>` i gotovo sva zaglavlja slijede to pravilo imenovanja.

Međutim, `<complex.h>` ga ne slijedi: C++ nema zaglavlje `<ccomplex>`. Kompleksni brojevi u C++-u nalaze se izravno u `<complex>`, a sadržaj je potpuno različit od onoga u C-u.

Zanimljivo. Razlog je taj što je `<complex>` postojao već u prvoj inačici C++-a, C++98, dok ga je jezik C dobio tek u C99.

U C++-u kompleksni se tipovi definiraju kao `complex<float>`, `complex<double>` i `complex<long double>`. Zbog polimorfizma objektno orijentiranog programiranja imena funkcija u nastavku jedinstvena su, bez sufiksa f ili l.

Objekt kompleksnog broja ima članske funkcije `real` i `imag` za pristup realnom i imaginarnom dijelu.

Za objekt kompleksnog broja postoje i nečlanske funkcije `real`, `imag`, `abs` i `arg`, koje vraćaju realni dio, imaginarni dio, modul i argument.

Postoje i nečlanske funkcije `norm`, kvadrat modula, te `conj`, konjugirano kompleksni broj.

Postoje i nečlanske funkcije `exp`, `log` (glavna vrijednost logaritma s bazom $\mathrm{e}$), `log10` (glavna vrijednost logaritma s bazom 10, ne postoji u C-u), `pow`, `sqrt`, `sin`, `cos` i `tan`, s istim značenjem kao u C-u.

Od C++14 nadalje definirani su [operatori literala `std::literals::complex_literals::""if, ""i, ""il`](https://en.cppreference.com/w/cpp/numeric/complex/operator%2522%2522i.html). Primjerice, `100if`, `100i` i `100il` vraćaju redom `std::complex<float>{0.0f, 100.0f}`, `std::complex<double>{0.0, 100.0}` i `std::complex<long double>{0.0l, 100.0l}`. To nam omogućuje da deklaraciju kompleksnog broja zgodno zapišemo kao `auto z = 4.0 + 3i`.

## Literatura i poveznice

-   [Complex number - Wikipedia](https://en.wikipedia.org/wiki/Complex_number)
-   [Euler's formula - Wikipedia](https://en.wikipedia.org/wiki/Euler's_formula)
-   [Complex number arithmetic - cppreference.com](https://en.cppreference.com/w/c/numeric/complex)
-   [std::complex - cppreference.com](https://en.cppreference.com/w/cpp/numeric/complex)

[^ref1]: Više o Eulerovoj formuli možete pronaći u dva videa: [欧拉公式与初等群论 (Eulerova formula i elementarna teorija grupa)](https://www.bilibili.com/video/BV1fx41187tZ) i [微分方程概论 - 第五章：在 3.14 分钟内理解 $\mathrm{e}^{\mathrm{i}\pi}$ (Uvod u diferencijalne jednadžbe – 5. poglavlje: razumjeti $\mathrm{e}^{\mathrm{i}\pi}$ u 3.14 minute)](https://www.bilibili.com/video/BV1G4411D7kZ).
