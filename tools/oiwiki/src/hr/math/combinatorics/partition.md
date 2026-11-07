---
title: Particijski brojevi
---

Particija (rastav): zapis prirodnog broja $n$ kao zbroja nerastućih pozitivnih cijelih brojeva.

$$
n=r_1+r_2+\ldots+r_k \quad r_1 \ge r_2 \ge \ldots \ge r_k \ge 1
$$

Svaki pozitivan cijeli broj u tom zbroju naziva se dijelom.

Particijski broj: $p_n$. Broj načina na koje se prirodan broj $n$ može rastaviti.

Particijski brojevi počevši od $0$:

| n     | 0 | 1 | 2 | 3 | 4 | 5 | 6  | 7  | 8  |
| ----- | - | - | - | - | - | - | -- | -- | -- |
| $p_n$ | 1 | 1 | 2 | 3 | 5 | 7 | 11 | 15 | 22 |

## Particije na k dijelova

Broj particija broja $n$ na točno $k$ dijelova nazivamo brojem particija na $k$ dijelova i označavamo ga $p(n,k)$.

Očito je broj particija na $k$ dijelova $p(n,k)$ ujedno i broj rješenja sljedeće jednadžbe:

$$
n-k=y_1+y_2+\ldots+y_k\quad y_1\ge y_2\ge\ldots\ge y_k\ge 0
$$

Ako je u toj jednadžbi točno $j$ dijelova različito od 0, postoji točno $p(n-k,j)$ rješenja. Stoga vrijedi:

$$
p(n,k)=\sum_{j=0}^k p(n-k,j)
$$

Oduzimanjem dviju susjednih suma dobivamo:

$$
p(n,k)=p(n-1,k-1)+p(n-k,k)
$$

Prikažemo li to tablicom, broj u svakoj ćeliji jednak je zbroju broja gore lijevo i broja koji se nalazi onoliko ćelija iznad koliko iznosi indeks stupca.

| k        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| -------- | - | - | - | - | - | - | - | - | - |
| $p(0,k)$ | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $p(1,k)$ | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $p(2,k)$ | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| $p(3,k)$ | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| $p(4,k)$ | 0 | 1 | 2 | 1 | 1 | 0 | 0 | 0 | 0 |
| $p(5,k)$ | 0 | 1 | 2 | 2 | 1 | 1 | 0 | 0 | 0 |
| $p(6,k)$ | 0 | 1 | 3 | 3 | 2 | 1 | 1 | 0 | 0 |
| $p(7,k)$ | 0 | 1 | 3 | 4 | 3 | 2 | 1 | 1 | 0 |
| $p(8,k)$ | 0 | 1 | 4 | 5 | 5 | 3 | 2 | 1 | 1 |

### Primjer zadatka

???+ note "Računanje broja particija na k dijelova"
    Izračunajte broj particija na $k$ dijelova $p(n,k)$. Više testnih primjera; $n$ je najviše $10000$, $k$ najviše $1000$, rezultat se računa modulo $1000007$.
    
    Promatrajući tablicu i rekurziju, ažuriranje po stupcima povoljnije je za pohranu. Program nije teško napisati:
    
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    int p[10005][1005]; /*broj načina da se prirodan broj n rastavi na k dijelova*/
    
    int main() {
      int n, k;
      while (~scanf("%d%d", &n, &k)) {
        memset(p, 0, sizeof(p));
        p[0][0] = 1;
        int i;
        for (i = 1; i <= n; ++i) {
          int j;
          for (j = 1; j <= k; ++j) {
            if (i - j >= 0) /*p[i-j][j]: svi dijelovi veći od 1*/
            {
              p[i][j] = (p[i - j][j] + p[i - 1][j - 1]) %
                        1000007; /*p[i-1][j-1]: barem jedan dio jednak 1.*/
            }
          }
        }
        printf("%d\n", p[n][k]);
      }
    }
    ```

### Funkcija izvodnica

Iz formule za zbroj geometrijskog niza imamo:

$$
\frac{1}{1-x^k}=1+x^k+x^{2k}+x^{3k}+\ldots
$$

$$
1+p_1 x+p_2 x^2+p_3 x^3+\ldots=\frac{1}{1-x}  \frac{1}{1-x^2}  \frac{1}{1-x^3}\ldots
$$

Za particije na $k$ dijelova funkcija izvodnica malo je složenija. Konkretno glasi:

$$
\sum_{n,k=0}^\infty {p(n,k) x^n y^k }=\frac{1}{1-xy}  \frac{1}{1-x^2 y}  \frac{1}{1-x^3 y}\ldots
$$

### Ferrersov dijagram

Ferrersov dijagram: svaki dio particije prikazujemo retkom točaka. Broj točaka u retku jednak je veličini tog dijela.

Prema definiciji particije, retci Ferrersova dijagrama poredani su u padajućem redoslijedu. Najdulji je redak na vrhu.

Na primjer, Ferrersov dijagram particije $12=5+4+2+1$.

![](./images/ferrers.jpg)

Zrcalimo li Ferrersov dijagram preko dijagonale, dobiveni novi Ferrersov dijagram nazivamo konjugiranim dijagramom izvornoga, a novu particiju konjugiranom particijom izvorne. Očito je konjugiranost simetrična relacija.

Na primjer, konjugirana particija gornje particije $12=5+4+2+1$ jest particija $12=4+3+2+2+1$.

Broj particija s najvećim dijelom $k$: broj particija prirodnog broja $n$ čiji je najveći dio $k$.

Iz definicije konjugiranosti slijedi očit zaključak:

Broj particija s najvećim dijelom $k$ jednak je broju particija na $k$ dijelova; oba iznose $p(n,k)$.

## Particije na različite dijelove

Broj particija na različite dijelove: $pd_n$. Broj načina na koje se prirodan broj $n$ može rastaviti na međusobno različite dijelove. (Different)

| n      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| ------ | - | - | - | - | - | - | - | - | - |
| $pd_n$ | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 5 | 6 |

Slično definiramo broj particija na $k$ različitih dijelova $pd(n,k)$, koji predstavlja particije na različite dijelove s najviše $k$ dijelova i jednak je broju rješenja ove jednadžbe:

$$
n=r_1+r_2+\ldots+r_k\quad r_1>r_2>\ldots>r_k\ge 1
$$

Potpuno kao gore, to je ujedno i broj rješenja ove jednadžbe:

$$
n-k=y_1+y_2+\ldots+y_k\quad y_1>y_2>\ldots>y_k\ge 0
$$

Razlika u odnosu na prethodni slučaj jest to da zbog različitosti dijelova u novoj jednadžbi najviše jedan dio može biti nula. Zaključak ostaje nepromijenjen: ako je točno $j$ dijelova različito od $0$, postoji točno $pd(n-k,j)$ rješenja, pri čemu $j$ može biti samo $k$ ili $k-1$. Stoga izravno dobivamo rekurziju:

$$
pd(n,k)=pd(n-k,k-1)+pd(n-k,k)
$$

Slično kao kod binomnih koeficijenata, prikažemo li to tablicom, broj u svakoj ćeliji jednak je zbroju broja koji se u prethodnom stupcu nalazi onoliko ćelija iznad koliko iznosi indeks stupca i broja koji se u istom stupcu nalazi onoliko ćelija iznad koliko iznosi indeks stupca.

| k         | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --------- | - | - | - | - | - | - | - | - | - |
| $pd(0,k)$ | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(1,k)$ | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(2,k)$ | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(3,k)$ | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(4,k)$ | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(5,k)$ | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(6,k)$ | 0 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| $pd(7,k)$ | 0 | 1 | 3 | 1 | 0 | 0 | 0 | 0 | 0 |
| $pd(8,k)$ | 0 | 1 | 3 | 2 | 0 | 0 | 0 | 0 | 0 |

### Primjer zadatka

???+ note "Računanje broja particija na različite dijelove"
    Izračunajte broj particija na različite dijelove $pd_n$. Više testnih primjera; $n$ je najviše $50000$, rezultat se računa modulo $1000007$.
    
    Promatrajući tablicu i rekurziju, ažuriranje po stupcima povoljnije je za pohranu. U kodu je druga dimenzija sažeta radi uštede prostora; čuvaju se samo dva susjedna stupca.
    
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    int pd[50005][2]; /*broj načina da se prirodan broj n rastavi na k različitih dijelova*/
    
    int main() {
      int n;
      while (~scanf("%d", &n)) {
        memset(pd, 0, sizeof(pd));
        pd[0][0] = 1;
        int ans = 0;
        int j;
        for (j = 1; j < 350; ++j) {
          int i;
          for (i = 0; i < 350; ++i) {
            pd[i][j & 1] = 0; /*pd[i][j] ovisi samo o pd[][j] i pd[][j-1]*/
          }
          for (i = 0; i <= n; ++i) {
            if (i - j >= 0) /*pd[i-j][j]: svi dijelovi veći od 1*/
            {
              pd[i][j & 1] = (pd[i - j][j & 1] + pd[i - j][(j - 1) & 1]) %
                             1000007; /*pd[i-j][j-1]: barem jedan dio jednak 1.*/
            }
          }
          ans = (ans + pd[n][j & 1]) % 1000007;
        }
        printf("%d\n", ans);
      }
    }
    ```

### Particije na neparne dijelove

Broj particija na neparne dijelove: $po_n$. Broj načina na koje se prirodan broj $n$ može rastaviti na dijelove koji su svi neparni. (Odd)

Vrijedi očita jednakost:

$$
\prod_{i=1}^\infty (1+x^i ) =\frac{\prod_{i=1}^\infty (1-x^{2i} ) }{\prod_{i=1}^\infty (1-x^i ) }=\prod_{i=1}^\infty \frac{1}{1-x^{2i-1} }
$$

Krajnje lijevo je funkcija izvodnica broja particija na različite dijelove, a krajnje desno funkcija izvodnica broja particija na neparne dijelove. Njihovi odgovarajući koeficijenti jednaki su, pa je broj particija na neparne dijelove jednak broju particija na različite dijelove:

$$
po_n=pd_n
$$

No očito broj particija na $k$ neparnih dijelova i broj particija na $k$ različitih dijelova nisu isti pojam, pa ih ovdje ne navodimo.

Uvedimo još dva pojma:

Broj particija na paran broj različitih dijelova: $pde_n$. Broj particija prirodnog broja $n$ na različite dijelove kojih je paran broj. (Even)

Broj particija na neparan broj različitih dijelova: $pdo_n$. Broj particija prirodnog broja $n$ na različite dijelove kojih je neparan broj. (Odd)

Stoga vrijedi:

$$
pd_n=pde_n+pdo_n
$$

Postoje i odgovarajući pojmovi za $k$ dijelova. Budući da su presloženi, ne navodimo ih.

## Teorem o peterokutnim brojevima

Promotrimo zasebno nazivnik funkcije izvodnice particijskih brojeva:

$$
\prod_{i=1}^\infty (1-x^i ) 
$$

Razvijemo li taj dio, možemo se dosjetiti particija na različite dijelove, pri čemu je bitna parnost broja dijelova takve particije.

Konkretno, particije na paran broj različitih dijelova u razvoju se broje pozitivno, a particije na neparan broj različitih dijelova negativno. Stoga je koeficijent svakog člana razvoja razlika tih dvaju brojeva, tj.:

$$
\sum_{i=0}^\infty ({pde}_n-{pdo}_n ) x^n =\prod_{i=1}^\infty (1-x^i ) 
$$

Sada pokazujemo da su u većini slučajeva ta dva broja jednaka, pa je koeficijent u razvoju $0$; samo na nekoliko mjesta ta se dva broja razlikuju za $1$ ili $-1$.

Ovdje se možemo poslužiti konstrukcijom bijekcije.

Nacrtajmo Ferrersov dijagram svake particije na različite dijelove. Posljednji redak nazivamo dnom dijagrama, a broj točaka na dnu označavamo $b$ (Bottom); najdulju dužinu pod kutom od $45$ stupnjeva koja spaja posljednju točku najgornjeg retka s nekom točkom dijagrama nazivamo kosinom dijagrama, a broj točaka na kosini označavamo $s$ (Slide).

![](./images/bottom_slide.jpg)

Da bismo konstruirali bijekciju između particija na paran i particija na neparan broj različitih dijelova, trebamo definirati transformaciju koja, uz očuvanje različitosti dijelova, mijenja broj redaka za $1$:

Transformacija A: kad je $b$ manje ili jednako $s$, dno premještamo udesno tako da postane nova kosina.

Transformacija B: kad je $b$ veće od $s$, kosinu premještamo dolje tako da postane novo dno.

Za većinu $n$ i bilo koju particiju na različite dijelove točno je jedna od ovih dviju transformacija izvediva, čime je konstruirana bijekcija između particija na paran i particija na neparan broj različitih dijelova. Brojevi particija dviju vrsta između kojih je konstruirana bijekcija jednaki su, pa je koeficijent $n$-tog člana razvoja tada $0$.

No za neke $n$ postoji točno jedna particija na različite dijelove na kojoj se navedene transformacije ne mogu izvesti.

-   Slučaj 1: kad je $b=s$ i dno i kosina imaju zajedničku točku, transformacija A ne može se izvesti. Tada je

$$
n=s+(s+1)+\ldots+(s+s-1)=\frac{s(3s-1)}{2}
$$

$n$-ti član razvoja ovisi o parnosti broja dijelova particije i iznosi $(-1)^s x^n$.

-   Slučaj 2: kad je $b=s+1$ i dno i kosina imaju zajedničku točku, transformacija B ne može se izvesti. Tada je

$$
n=(s+1)+(s+2)+\ldots+(s+s)=\frac{s(3s+1)}{2}
$$

$n$-ti član razvoja iznosi $(-1)^s x^n$.

Zamijenimo li u gornjem izrazu $s$ sa $-s$, dobivamo $n=\frac{s(3s-1)}{2}$, gdje je $s$ negativan cijeli broj, a $n$-ti član razvoja i dalje je $(-1)^s x^n$.

Budući da se ova dva slučaja ne mogu pojaviti za isti $n$ istodobno, možemo spojiti oba uvjeta i dobiti uvjet koji $n$ mora zadovoljavati:

$$
\exists k\in\mathbb{Z},n=\frac{k(3k-1)}{2}
$$

Time smo dokazali:

$$
(1-x)(1-x^2 )(1-x^3 )\ldots=\sum_{k=-\infty}^{+\infty} (-1)^k x^{\frac{k(3k-1)}{2}} =\ldots+x^{26}-x^{15}+x^7-x^2+1-x+x^5-x^{12}+x^{22}-\ldots
$$

Prisjetimo se: ovaj je izraz recipročna vrijednost funkcije izvodnice particijskih brojeva, pa je njegov umnožak s funkcijom izvodnicom particijskih brojeva jednak $1$. Sređivanjem i usporedbom koeficijenata s obje strane dobivamo rekurziju za niz particijskih brojeva.

$$
(1+p_1 x+p_2 x^2+p_3 x^3+\ldots)(1-x-x^2+x^5+x^7-x^{12}-x^{15}+x^{22}+x^{26}-\ldots)=1
$$

$$
p_n=p_{n-1}+p_{n-2}-p_{n-5}-p_{n-7}+\ldots
$$

Ova rekurzija ima beskonačno mnogo članova, ali ako dogovorno uzmemo da je particijski broj negativnog broja $0$ (particijski broj broja $0$ već je definiran kao $1$), svodi se na konačno mnogo članova.

### Primjer zadatka

???+ note "Računanje particijskih brojeva"
    Izračunajte particijski broj $p_n$. Više testnih primjera; $n$ je najviše $50000$, rezultat se računa modulo $1000007$.
    
    Koristimo metodu teorema o peterokutnim brojevima. Kod:
    
    ```cpp
    #include <cstdio>
    
    long long a[100010];
    long long p[50005];
    
    int main() {
      p[0] = 1;
      p[1] = 1;
      p[2] = 2;
      int i;
      for (i = 1; i < 50005;
           i++) /*koeficijenti rekurzije 1,2,5,7,12,15,22,26...i*(3*i-1)/2,i*(3*i+1)/2*/
      {
        a[2 * i] = i * (i * 3 - 1) / 2; /*peterokutni brojevi su 1,5,12,22...i*(3*i-1)/2*/
        a[2 * i + 1] = i * (i * 3 + 1) / 2;
      }
      for (
          i = 3; i < 50005;
          i++) /*p[n]=p[n-1]+p[n-2]-p[n-5]-p[n-7]+p[12]+p[15]-...+p[n-i*[3i-1]/2]+p[n-i*[3i+1]/2]*/
      {
        p[i] = 0;
        int j;
        for (j = 2; a[j] <= i; j++) /*može biti negativno, pa u izrazu dodajemo 1000007*/
        {
          if (j & 2) {
            p[i] = (p[i] + p[i - a[j]] + 1000007) % 1000007;
          } else {
            p[i] = (p[i] - p[i - a[j]] + 1000007) % 1000007;
          }
        }
      }
      int n;
      while (~scanf("%d", &n)) {
        printf("%lld\n", p[n]);
      }
    }
    ```
