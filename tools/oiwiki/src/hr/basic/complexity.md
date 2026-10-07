---
title: Složenost
---

Vremenska i prostorna složenost važna su mjerila učinkovitosti algoritma.

## Broj osnovnih operacija

Isti algoritam na različitim računalima radi različitom brzinom, a stvarnu brzinu izvođenja teško je teorijski izračunati i nezgodno je mjeriti; zato obično ne promatramo stvarno vrijeme izvođenja, nego broj osnovnih operacija koje algoritam mora obaviti.

Na običnom računalu zbrajanje, oduzimanje, množenje, dijeljenje, pristup varijabli (osnovnog tipa, i dalje u tekstu) i pridruživanje vrijednosti varijabli mogu se smatrati osnovnim operacijama.

Brojanje ili procjena osnovnih operacija može služiti kao mjerilo vremena izvođenja algoritma.

## Vremenska složenost

### Definicija

Pri mjerenju brzine algoritma nužno treba uzeti u obzir veličinu podataka. Veličina podataka obično znači broj brojeva u ulazu, broj vrhova i bridova grafa u ulazu i slično. Općenito, što su podaci veći, algoritam radi dulje. U natjecateljskom programiranju pri ocjeni učinkovitosti algoritma najvažnije nije vrijeme na nekoj konkretnoj veličini podataka, nego trend rasta vremena s veličinom podataka – **vremenska složenost**.

### Uvod

Glavni razlozi zašto promatramo trend rasta vremena s veličinom podataka:

1.  Suvremena računala izvode stotine milijuna i više osnovnih operacija u sekundi, pa su podaci koje obrađujemo obično veliki. Ako algoritmu A na podacima veličine $n$ treba $100n$, a algoritmu B $n^2$, za $n$ manji od $100$ algoritam B je brži, ali u jednoj sekundi algoritam A obradi podatke veličine nekoliko milijuna, a B samo nekoliko desetaka tisuća. Kad je dopušteno dulje izvođenje, utjecaj vremenske složenosti na veličinu obradivih podataka postaje još izraženiji i daleko veći od razlike vremena na istoj veličini podataka;
2.  Vrijeme izvođenja izražavamo brojem osnovnih operacija, a stvarno trajanje pojedinih osnovnih operacija razlikuje se – zbrajanje i oduzimanje puno su brži od dijeljenja. Računanjem vremenske složenosti i zanemarivanjem razlika između osnovnih operacija te razlike između jedne i deset osnovnih operacija uklanjamo utjecaj različitog trajanja operacija.

Naravno, vrijeme izvođenja ne ovisi samo o veličini ulaza nego i o njegovu sadržaju. Zato se vremenska složenost dijeli na nekoliko vrsta, npr.:

1.  najgora vremenska složenost – složenost koja odgovara ulazu koji za svaku veličinu traje najdulje. U natjecateljskom programiranju ulaz može biti bilo koji unutar zadanih ograničenja, pa da bi algoritam prošao sve podatke u tom rasponu obično promatramo najgoru složenost;
2.  prosječna (očekivana) vremenska složenost – očekivanje vremena izvođenja uz pretpostavku da su svi ulazi jednako vjerojatni.

„Trend rasta vremena s veličinom podataka” nejasan je pojam, pa za formalni zapis vremenske složenosti koristimo **asimptotske oznake** opisane u nastavku.

## Definicija asimptotskih oznaka

Asimptotske oznake standardni su opis reda funkcije. Jednostavno rečeno, zanemaruju dijelove funkcije koji rastu sporije i koeficijente članova (u analizi složenosti koeficijenti se obično zovu „konstante”), a zadržavaju važan dio koji pokazuje trend rasta funkcije.

Jednostavno pravilo za pamćenje: s jednakošću (nestrogo) velika slova, bez jednakosti (strogo) mala; jednako je $\Theta$, manje je $O$, veće je $\Omega$. Veliko $O$ i malo $o$ izvorno su grčko slovo omikron, ali zbog istog oblika mogu se shvatiti i kao latinično veliko $O$ i malo $o$.

U engleskom korijeni „-micro-” i „-mega-” označavaju $10^{-6}$ (milijunti dio) i $10^{6}$ (milijun), ali i „malo” i „veliko”. Malo i veliko također su uobičajena značenja grčkih slova omikron i omega.

### Oznaka veliko Θ

Za funkcije $f(n)$ i $g(n)$ vrijedi $f(n)=\Theta(g(n))$ ako i samo ako $\exists c_1,c_2,n_0>0$ takvi da $\forall n \ge n_0, 0\le c_1\cdot g(n)\le f(n) \le c_2\cdot g(n)$.

Drugim riječima, ako je $f(n)=\Theta(g(n))$, postoje dva pozitivna broja $c_1, c_2$ takva da je $f(n)$ stisnuta između $c_1\cdot g(n)$ i $c_2\cdot g(n)$.

Primjerice, $3n^2+5n-3=\Theta(n^2)$; ovdje $c_1, c_2, n_0$ mogu biti $2, 4, 100$. Također $n\sqrt {n} + n{\log^5 n} + m{\log m} +nm=\Theta(n\sqrt {n} + m{\log m} + nm)$, jer je $\log^5 n=o(\sqrt n)$, pa postoji dovoljno velik $n_0$ za koji izostavljeni član ne prelazi $n\sqrt n$.

### Oznaka veliko O

Oznaka $\Theta$ daje i gornju i donju ogradu funkcije; ako znamo samo asimptotsku gornju ogradu, a ne i donju, koristimo oznaku $O$. $f(n)=O(g(n))$ ako i samo ako $\exists c,n_0>0$ takvi da $\forall n \ge n_0,0\le f(n)\le c\cdot g(n)$.

Pri proučavanju vremenske složenosti obično se koristi oznaka $O$, jer nas obično zanima gornja ograda vremena programa, a ne donja.

Treba napomenuti da se „gornja” i „donja ograda” ovdje odnose na trend funkcije, a ne na algoritam. Gornja ograda vremena algoritma odgovara „najgoroj vremenskoj složenosti”, a ne oznaci veliko $O$. Zato je najgoru složenost potpuno ispravno pisati oznakom $\Theta$; može se čak reći da je $\Theta$ preciznija od $O$. Glavni razlozi uporabe $O$ su: prvo, katkad možemo dokazati samo gornju ogradu složenosti, a ne i donju (obično kod složenijih algoritama i analiza); drugo, $O$ je na računalu jednostavnije utipkati.

### Oznaka veliko Ω

Slično, oznakom $\Omega$ opisujemo asimptotsku donju ogradu funkcije. $f(n)=\Omega(g(n))$ ako i samo ako $\exists c,n_0>0$ takvi da $\forall n \ge n_0,0\le c\cdot g(n)\le f(n)$.

### Oznaka malo o

Ako oznaka $O$ odgovara znaku „manje ili jednako”, oznaka $o$ odgovara znaku „manje”.

Malo $o$ široko se koristi u matematičkoj analizi: Taylorov razvoj funkcije u točki ima Peanov ostatak, a malo $o$ označava strogo manje, čime se provodi asimptotska analiza ekvivalentnih infinitezimala.

$f(n)=o(g(n))$ ako i samo ako za svaki zadani pozitivni $c$ postoji $n_0$ takav da $\forall n \ge n_0,0\le f(n)< c\cdot g(n)$.

### Oznaka malo ω

Ako oznaka $\Omega$ odgovara znaku „veće ili jednako”, oznaka $\omega$ odgovara znaku „veće”.

$f(n)=\omega(g(n))$ ako i samo ako za svaki zadani pozitivni $c$ postoji $n_0$ takav da $\forall n \ge n_0,0\le c\cdot g(n)< f(n)$.

![](images/order.svg)

### Uobičajena svojstva

-   $f(n) = \Theta(g(n))\iff f(n)=O(g(n))\land f(n)=\Omega(g(n))$.
-   $f_1(n) + f_2(n) = O(\max(f_1(n), f_2(n)))$.
-   $f_1(n) \times f_2(n) = O(f_1(n) \times f_2(n))$.
-   $\forall a>1, \log_a{n} = O(\log_2 n)$. Iz formule za promjenu baze slijedi da za fiksnu realnu bazu $a>1$ sve logaritamske funkcije imaju isti rast, pa se baza logaritma u asimptotskoj složenosti obično ne piše.

## Jednostavni primjeri računanja vremenske složenosti

### Petlja `for`

=== "C++"
    ```cpp
    int n, m;
    std::cin >> n >> m;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        for (int k = 0; k < m; ++k) {
          std::cout << "hello world\n";
        }
      }
    }
    ```

=== "Python"
    ```python
    n = int(input())
    m = int(input())
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, m):
                print("hello world")
    ```

=== "Java"
    ```java
    int n, m;
    n = input.nextInt();
    m = input.nextInt();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                System.out.println("hello world");
            }
        }
    }
    ```

Ako veličinom podataka smatramo vrijednosti $n$ i $m$ iz ulaza, vremenska složenost gornjeg koda je $\Theta(n^2m)$.

### DFS

Pri [DFS-u](../graph/dfs.md) na [povezanom grafu](../graph/concept.md#连通) s $n$ vrhova i $m$ bridova pohranjenom listama susjedstva svaki se vrh i brid posjećuje konstantan broj puta, pa je složenost $\Theta(n+m)$.

## Što je konstanta

Kad izvodimo neki broj operacija, kako odlučiti utječe li taj broj na vremensku složenost? Primjerice:

=== "C++"
    ```cpp
    constexpr int N = 100000;
    for (int i = 0; i < N; ++i) {
      std::cout << "hello world\n";
    }
    ```

=== "Python"
    ```python
    N = 100000
    for i in range(0, N):
        print("hello world")
    ```

=== "Java"
    ```java
    final int N = 100000;
    for (int i = 0; i < N; ++i) {
        System.out.println("hello world");
    }
    ```

Ako se $N$ ne smatra veličinom ulaza, vremenska složenost ovog koda je $O(1)$.

Pri računanju vremenske složenosti vrlo je važno koje se varijable smatraju veličinom ulaza; sve veličine neovisne o veličini ulaza smatraju se konstantama i pri računanju složenosti tretiraju kao $1$.

Napomena: u teorijskim raspravama o vremenskoj složenosti osnovna je pretpostavka da „algoritam može riješiti problem bilo koje veličine” (u praksi, naravno, zbog ograničenog vremena i memorije prevelike probleme ne možemo riješiti). Zato mogućnost da se problem ograničene veličine riješi u konstantnom vremenu (npr. unaprijed izračunati odgovor za svaki mogući ulaz u zadanom rasponu) ne čini složenost algoritma $O(1)$.

## Glavni teorem

Glavni teorem (master theorem) omogućuje brzo određivanje složenosti rekurzivnih algoritama. Neka su $a\ge1$, $b>1$ konstante, $f$ nenegativna i $T(1)=\Theta(1)$. Radi jednostavnosti dodatno pretpostavimo $n=b^L$, gdje je $L$ nenegativan cijeli broj. Rekurzivna relacija glasi:

$$
T(n) = a T\left(\frac{n}{b}\right)+f(n),\qquad \forall n=b^L,\ L\ge1.
$$

Tada

$$
T(n) = \begin{cases}
    \Theta(n^{\log_b a}), & f(n) = O(n^{\log_b (a)-\epsilon}),\epsilon > 0, \\
    \Theta(f(n)), & f(n) = \Omega(n^{\log_b (a)+\epsilon}),\epsilon\ge 0, \\
    \Theta(n^{\log_b a}\log^{k+1} n), & f(n)=\Theta(n^{\log_b a}\log^k n),k\ge 0.
    \end{cases}
$$

Napomena: u drugom slučaju mora biti ispunjen i uvjet regularnosti (regularity condition): postoji konstanta $0<c<1$ takva da za dovoljno velike $n$ vrijedi $a f(n/b) \leq c f(n)$.

Ideja dokaza: problem veličine $n$ rastavi se na $a$ problema veličine $n/b$, koji se zatim redom spajaju do najviše razine. Svako spajanje potproblema stoji $f(n)$ vremena.

??? note "Dokaz"
    Prema gore navedenoj ideji, dokaz teče ovako:
    
    Na razini $0$ (najvišoj) spajanje potproblema stoji $f(n)$.
    
    Na razini $1$ (potproblemi iz prve podjele) ima $a$ potproblema, a spajanje svakog stoji $f\left(\dfrac{n}{b}\right)$, pa spajanje ukupno stoji $a f\left(\dfrac{n}{b}\right)$.
    
    Nastavljajući razinu po razinu dobivamo sljedeće rekurzivno stablo:
    
    ![](./images/master-theorem-proof.svg)
    
    Stablo završava na razini $L=\log_b n$ i ima $a^L=n^{\log_b a}$ listova. Unutarnje razine označene su $0,\ldots,L-1$, pa je $T(n) = \Theta(n^{\log_b a}) + g(n)$, gdje je $g(n) = \sum_{j = 0}^{L-1} a^{j} f(n / b^{j})$.
    
    Prvi slučaj: $f(n) = O(n^{\log_b a-\epsilon})$, pa je $g(n) = O(n^{\log_b a})$.
    
    Drugi slučaj: trošak korijena je $T(n)=\Omega(f(n))$. Po uvjetu regularnosti, dok su potproblemi dovoljno veliki ukupni trošak razine $j$ iznosi najviše $c^j f(n)$, pa je zbroj troškova tih razina $O(f(n))$. Preostali konstantan broj donjih razina i listovi stoje ukupno $O(n^{\log_b a})=O(f(n))$, pa je $T(n)=\Theta(f(n))$.
    
    Treći slučaj: neka je $p=\log_b a$. Za dovoljno velike potprobleme ukupni trošak razine $j$ je $\Theta(n^p(L-j)^k)$, gdje je $k\ge0$ fiksna konstanta. Uzmimo fiksni $r_0\ge1$ takav da $b^{r_0}$ doseže tu veličinu; iz $\sum_{r=r_0}^L r^k=\Theta(L^{k+1})$ slijedi da je ukupni trošak tih razina $\Theta(n^p\log^{k+1}n)$. Preostale donje razine i listovi stoje ukupno $O(n^p)$, i zbrajanjem dobivamo tvrdnju.

Nekoliko primjera uporabe glavnog teorema:

1.  $T(n) = 2T\left(\dfrac{n}{2}\right) + 1$: tada je $a=2, b=2, {\log_2 2} = 1$, $\epsilon$ može biti iz $(0, 1]$, vrijedi prvi slučaj, pa je $T(n) = \Theta(n)$;

2.  $T(n) = T\left(\dfrac{n}{2}\right) + n$: tada je $a=1, b=2, {\log_2 1} = 0$, $\epsilon$ može biti iz $(0, 1]$, vrijedi drugi slučaj, pa je $T(n) = \Theta(n)$;

3.  $T(n) = T\left(\dfrac{n}{2}\right) + {\log n}$: tada je $a=1, b=2, {\log_2 1}=0$, $k$ može biti $1$, vrijedi treći slučaj, pa je $T(n) = \Theta(\log^2 n)$;

4.  $T(n) = T\left(\dfrac{n}{2}\right) + 1$: tada je $a=1, b=2, {\log_2 1} = 0$, $k$ može biti $0$, vrijedi treći slučaj, pa je $T(n) = \Theta(\log n)$.

## Amortizirana složenost

Više na stranici [Amortizirana analiza](./amortized-analysis.md).

## Prostorna složenost

Slično, trend rasta memorije koju algoritam koristi s veličinom ulaza mjeri se **prostornom složenošću**.

## Računska složenost

Ovaj je članak složenost predstavio iz perspektive analize algoritama; zainteresirani mogu dublje zaviriti u [računsku složenost](../misc/cc-basic.md).
