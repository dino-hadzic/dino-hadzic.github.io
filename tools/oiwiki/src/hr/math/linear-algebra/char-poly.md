---
title: Karakteristični polinom
---

U dijelu o svojstvenim vrijednostima proučavaju se samo kvadratne matrice, tj. linearni operator koji odgovara matrici $A$ preslikava $n$ vektora u $n$ vektora.

Budući da u praktičnim problemima često treba razmatrati uzastopnu, ponovljenu primjenu iste transformacije, opis „linearni operator koji odgovara matrici $A$ preslikava jediničnu matricu $I$ u $A$” bio bi vrlo apstraktan. Tada je najbolje potražiti „fiksne točke”, tj. dijelove koji se pri transformaciji ne mijenjaju.

No u stvarnosti linearni operator koji odgovara matrici $A$ vrlo vjerojatno nema fiksnih točaka, pa tražimo nešto slabije: dijelove koji ostaju kolinearni ili se mijenjaju na sličan jednostavan način.

## Svojstvene vrijednosti i svojstveni vektori

Pod djelovanjem linearnog operatora koji odgovara matrici $A$ neki vektori ne mijenjaju smjer, nego se samo rastežu ili skraćuju.

Neka je $V$ linearni prostor nad $F$, a $T$ linearni operator na $V$. Ako postoje $\lambda$ iz $F$ i **nenul vektor** $\xi$ iz $V$ takvi da:

$$
T\xi=\lambda\xi
$$

kažemo da je $\lambda$ **svojstvena vrijednost** od $T$, a $\xi$ **svojstveni vektor od $T$ koji pripada svojstvenoj vrijednosti $\lambda$**.

Svojstveni vektor ostaje na istom pravcu: pod djelovanjem linearnog operatora ne mijenja smjer (sažimanje u nulu također smatramo očuvanjem smjera). Svojstveni vektor nije jedinstven; svi vektori kolinearni sa svojstvenim vektorom također su svojstveni vektori, ali se dogovorno nul-vektor ne smatra svojstvenim vektorom, a vektor koji ima smjer prirodno je nenul vektor. Svojstvena vrijednost svojstvenog vektora upravo je faktor njegova rastezanja.

U praktičnim primjenama za svojstvene vektore s istom svojstvenom vrijednošću obično se kao predstavnik svih njih odabere jedna baza.

Neka je $\alpha_1,\alpha_2,\cdots,\alpha_n$ baza od $V$ i neka $T$ u toj bazi ima matricu $A$, tj.:

$$
T(\alpha_1,\alpha_2,\cdots,\alpha_n)=(\alpha_1,\alpha_2,\cdots,\alpha_n)A
$$

Neka je $\lambda_0$ svojstvena vrijednost od $T$, $\xi$ svojstveni vektor od $T$ koji pripada svojstvenoj vrijednosti $\lambda_0$, i neka nenul vektor $X$ zadovoljava:

$$
\xi=(\alpha_1,\alpha_2,\cdots,\alpha_n)X
$$

Tada imamo:

$$
T\xi=\lambda_0\xi
$$

$$
T(\alpha_1,\alpha_2,\cdots,\alpha_n)X=\lambda_0(\alpha_1,\alpha_2,\cdots,\alpha_n)X
$$

$$
(\alpha_1,\alpha_2,\cdots,\alpha_n)AX=\lambda_0(\alpha_1,\alpha_2,\cdots,\alpha_n)X
$$

$$
AX=\lambda_0X
$$

$$
(A-\lambda_0I)X=0
$$

pa je i odgovarajuća determinanta jednaka $0$.

## Karakteristični polinom

Promotrimo matricu $A$ dimenzija $n\times n$, gdje je $n\geq 0\land n\in\mathbb{Z}$. Neka je $\lambda$ parametar; matrica $\lambda I-A$ zove se **karakteristična matrica** od $A$.

Determinanta karakteristične matrice zove se **karakteristični polinom** od $A$; razvija se u polinom stupnja $n$ čiji su korijeni svojstvene vrijednosti od $A$, a označava se $p_A(\lambda)$:

$$
p_A(\lambda)=\det(\lambda I_n-A)=\begin{vmatrix}
\lambda-a_{11} & -a_{12} &  \cdots & -a_{1n} \\
-a_{21} & \lambda-a_{22} &  \cdots & -a_{2n} \\
\vdots & \vdots &  & \vdots  \\
-a_{n1} & -a_{n2} &  \cdots & \lambda-a_{nn} \\
\end{vmatrix}
$$

gdje je $I_n$ jedinična matrica dimenzija $n\times n$. Negdje se definira $p_A(\lambda)=\det(A-\lambda I_n)$, što se od naše definicije razlikuje samo za predznak $(-1)^n$; no uz ovu definiciju $p_A(\lambda)$ sigurno je normirani polinom (s vodećim koeficijentom 1), dok je uz onu drugu normiran samo kad je $n$ paran. Treba napomenuti da je determinanta matrice dimenzija $0\times 0$ dobro definirana i jednaka $1$.

Nenul vektor rješenja $X$ sustava $(\lambda_0 I-A)X=0$ zove se svojstveni vektor od $A$ koji pripada $\lambda_0$.

Linearni operator $T$ ima svojstvenu vrijednost $\lambda_0$ ako i samo ako matrica $A$ ima svojstvenu vrijednost $\lambda_0$.

Linearni operator $T$ ima svojstveni vektor $\xi$ ako i samo ako matrica $A$ ima svojstveni vektor $X$, pri čemu je:

$$
\xi=(\alpha_1,\cdots,\alpha_n)X
$$

Prema osnovnom teoremu algebre karakteristični polinom može se faktorizirati kao:

$$
f(\lambda)=|\lambda I-A|={(\lambda-\lambda_1)}^{d_1}\cdots{(\lambda-\lambda_m)}^{d_m}
$$

Broj $d_i$ zove se **algebarska kratnost** svojstvene vrijednosti $\lambda_i$. Zbroj svih algebarskih kratnosti jednak je dimenziji prostora $n$.

### Određivanje svih svojstvenih vrijednosti i svojstvenih vektora matrice

Postupak se sastoji od sljedećih koraka:

-   Izračunamo determinantu $|\lambda I-A|$.
-   Odredimo sve korijene polinoma $f(\lambda)=|\lambda I-A|$ u polju $F$; to su svojstvene vrijednosti od $A$.
-   Za svaku svojstvenu vrijednost $\lambda$ od $A$ riješimo homogeni linearni sustav $(\lambda I-A)X=0$ i odredimo jedan njegov fundamentalni skup rješenja $X_1,\cdots,X_t$; tada su svi svojstveni vektori od $A$ koji pripadaju $\lambda$ oblika:

$$
k_1X_1+k_2X_2+\cdots+k_tX_t
$$

gdje $k_i$ u tom izrazu nisu svi jednaki nuli.

-   Svojstveni vektori linearnog operatora $T$ koji pripadaju $\lambda$ jesu:

$$
\xi_i=(\alpha_1,\cdots,\alpha_n)X_i
$$

Stoga su svi svojstveni vektori koji pripadaju $\lambda$ oblika:

$$
k_1\xi_1+k_2\xi_2+\cdots+k_t\xi_t
$$

gdje $k_i$ u tom izrazu nisu svi jednaki nuli.

Postojanje svojstvenih vrijednosti i svojstvenih vektora ovisi o polju nad kojim je $V$.

## Transformacija sličnosti

### Uvod

Ako je matrica $A$ dimenzija $n\times n$ gornjotrokutasta, npr.

$$
A=
\begin{bmatrix}
a_{1,1}&a_{1,2}&\cdots &a_{1,n}\\
&a_{2,2}&\cdots &a_{2,n}\\
&&\ddots &\vdots \\
&&&a_{n,n}
\end{bmatrix}
$$

onda se

$$
\begin{aligned}
p_A(x)&=\det(xI_n-A)\\
&=
\begin{bmatrix}
x-a_{1,1}&-a_{1,2}&\cdots &-a_{1,n}\\
&x-a_{2,2}&\cdots &-a_{2,n}\\
&&\ddots &\vdots \\
&&&x-a_{n,n}
\end{bmatrix}
\\
&=\prod_{i=1}^n(x-a_{i,i})
\end{aligned}
$$

lako izračuna; slično je i za donjotrokutaste matrice. Ako $A$ ne pripada ni jednoj od tih dviju vrsta matrica, treba primijeniti transformaciju sličnosti kako bi matrica poprimila oblik iz kojeg se karakteristični polinom lako računa.

### Definicija

Za matrice $A$ i $B$ dimenzija $n\times n$, ako postoji invertibilna matrica $P$ dimenzija $n\times n$ takva da je

$$
B=P^{-1}AP
$$

kažemo da su matrice $A$ i $B$ slične, a transformaciju $A\mapsto P^{-1}AP$ zovemo transformacijom sličnosti. Pritom $A$ i $P^{-1}AP$ imaju isti karakteristični polinom.

Promotrimo

$$
\begin{aligned}
\det(xI_n-P^{-1}AP)&=\det(xP^{-1}I_nP-P^{-1}AP)\\
&=\det(P^{-1}xI_nP-P^{-1}AP)\\
&=\det(P^{-1})\cdot \det(P)\cdot \det(xI_n-A)\\
&=\det(xI_n-A)\\
&=p_A(x)
\end{aligned}
$$

čime je tvrdnja dokazana; za $A\mapsto PAP^{-1}$ vrijedi isto. Osim toga, $p_A(0)=(-1)^n\cdot \det(A)$, jer je $p_A(0)=\det(-1\cdot I_nA)=\det(-1\cdot I_n)\cdot \det(A)$, pa je $\det(A)=\det(P^{-1}AP)$.

Teorem: Slične matrice imaju isti karakteristični polinom i iste svojstvene vrijednosti; obrat ne vrijedi.

Teorem pokazuje da karakteristični polinom matrice linearnog operatora ne ovisi o izboru baze, nego je izravno određen linearnim operatorom, pa ga možemo zvati karakterističnim polinomom linearnog operatora.

Karakteristični polinom $f(\lambda)=|\lambda I-A|$ matrice $A$ normirani je polinom. Prema Vièteovim formulama njegov koeficijent stupnja $n-1$ jednak je:

$$
-(\lambda_1+\cdots+\lambda_n)=-(a_{11}+\cdots+a_{nn})=-tr A
$$

gdje se $tr A$ zove trag od $A$ i jednak je zbroju elemenata na glavnoj dijagonali od $A$.

Prema Vièteovim formulama slobodni član karakterističnog polinoma jednak je:

$$
{(-1)}^n|A|={(-1)}^n(\lambda_1\cdots\lambda_n)
$$

Teorem: Slične matrice imaju isti trag.

### Formula zamjene

Teorem: Bez obzira na to jesu li matrice $A$ i $B$ kvadratne, ako se produkt može izračunati, trag matrice $AB$ jednak je tragu matrice $BA$.

Jedan je način dokaza izravno raspisivanje, čime je dokaz gotov. Drugi način dokaza koristi formulu zamjene.

Teorem: Neka je $A$ matrica s $m$ redaka i $n$ stupaca, a $B$ matrica s $n$ redaka i $m$ stupaca. Tada vrijedi:

$$
\lambda^n|\lambda I_m-AB|=\lambda^m|\lambda I_n-BA|
$$

Formula pokazuje da $AB$ i $BA$ imaju iste nenul svojstvene vrijednosti.

### Schurova lema

Svaka matrica $A$ reda $n$ slična je nekoj gornjotrokutastoj matrici, tj. postoji matrica $P$ punog ranga takva da je $P^{-1}AP$ gornjotrokutasta, a elementi na njezinoj glavnoj dijagonali sve su svojstvene vrijednosti od $A$.

Korolar: Neka su $\lambda_1,\cdots,\lambda_n$ svih $n$ svojstvenih vrijednosti od $A$, a $\phi(x)$ proizvoljan polinom. Tada su $n$ svojstvenih vrijednosti matričnog polinoma $\phi(A)$:

$$
\phi(\lambda_1),\cdots,\phi(\lambda_n)
$$

Posebno, svojstvene vrijednosti od $kA$ jesu $k\lambda_1,\cdots,k\lambda_n$, a svojstvene vrijednosti od $A^m$ jesu ${\lambda_1}^m,\cdots,{\lambda_n}^m$.

### Transformacija sličnosti Gaussovom eliminacijom

Na matrici $B$ dimenzija $n\times n$ može se provesti Gaussova eliminacija, čije su osnovne operacije elementarne transformacije redaka.

Ako nakon primjene takve operacije na matricu (množenje elementarnom matricom slijeva) matricu još pomnožimo zdesna inverzom te elementarne matrice, dobivamo transformaciju sličnosti; množenje slijeva je transformacija redaka, a lako se vidi da je množenje zdesna transformacija stupaca.

Ako matricu transformacijom sličnosti možemo svesti na gornjotrokutasti ili donjotrokutasti oblik, lako ćemo izračunati njezin karakteristični polinom. No ako na elemente na glavnoj dijagonali primijenimo transformaciju $A\mapsto T_{ij}(k)AT_{ij}(-k)$, onda nakon što smo s $A\mapsto T_{ij}(k)A$ poništili element u $i$-tom retku i $j$-tom stupcu, množenje zdesna s $T_{ij}(-k)$, tj. dodavanje $-k$ puta $i$-tog stupca od $A$ $j$-tom stupcu, može učiniti da prethodno poništeni element više nije nula, pa matricu možda ne možemo svesti na gornjotrokutasti ili donjotrokutasti oblik.

U nastavku ćemo pokazati da se karakteristični polinom i dalje lako dobiva iz matrice koju dobijemo primjenom transformacija na elemente na poddijagonali.

### Gornja Hessenbergova matrica

Za $n\gt 2$ matricu oblika

$$
H=
\begin{bmatrix}
\alpha_{1}&h_{12}&\dots&\dots&h_{1n}\\
\beta_{2}&\alpha_{2}&h_{23}&\dots &\vdots \\
&\ddots &\ddots & \ddots &\vdots \\
& &\ddots &\ddots & h_{(n-1)n}\\
&&& \beta_{n}& \alpha_{n}
\end{bmatrix}
$$

zovemo gornjom Hessenbergovom matricom, gdje $\beta$ označava poddijagonalu.

Transformacijama sličnosti poništimo elemente ispod poddijagonale i dobivamo gornju Hessenbergovu matricu, a karakteristični polinom gornje Hessenbergove matrice dimenzija $n\times n$ može se izračunati u vremenu $O(n^3)$.

Označimo s $H_i$ matricu koja zadržava samo prvih $i$ redaka i prvih $i$ stupaca od $H$ te neka je $p_i(x)=\det(xI_i-H_i)$. Tada je

$$
H_0=
\begin{bmatrix}
\end{bmatrix},\quad
p_0(x)=1
$$

$$
H_1=
\begin{bmatrix}
\alpha_1
\end{bmatrix},\quad
p_1(x)=\det(x I_1-H_1)=x -\alpha_1
$$

$$
H_2=
\begin{bmatrix}
\alpha_1&h_{12}\\
\beta_2&\alpha_2
\end{bmatrix},\quad
p_2(x)=\det(xI_2-H_2)=(x-\alpha_2)p_1(x)-\beta_2h_{12}p_0(x)
$$

Pri računanju determinante obično biramo razvoj po minorama duž retka ili stupca s najviše nula; minora je matrica koja ostaje nakon brisanja retka i stupca trenutačno odabranog elementa. Ovdje biramo razvoj po posljednjem retku i dobivamo

$$
\begin{aligned}
p_3(x)&=
\det(xI_3-H_3)\\
&=\begin{vmatrix}
x-\alpha_1&-h_{12}&-h_{13}\\
-\beta_2&x-\alpha_2&-h_{23}\\
&-\beta_3&x-\alpha_3
\end{vmatrix}\\
&=(x-\alpha_3)\cdot (-1)^{3+3}p_2(x)-\beta_3\cdot (-1)^{3+2}
\begin{vmatrix}
x-\alpha_1&-h_{13}\\
-\beta_2&-h_{23}
\end{vmatrix}\\
&=(x-\alpha_3)p_2(x)-\beta_3(h_{23}p_1(x)+\beta_2h_{13}p_0(x))
\end{aligned}
$$

Promatranjem i indukcijom, za $2\leq i\leq n$ vrijedi

$$
p_i(x)=(x-\alpha_i)p_{i-1}(x)-
\sum_{m=1}^{i-1}h_{i-m,i}
\left(
\prod_{j=i-m+1}^{i}\beta_j
\right)
p_{i-m-1}(x)
$$

Time je cijeli algoritam dovršen; obično se zove Hessenbergov algoritam.

## Cayley–Hamiltonov teorem

Za proizvoljnu matricu $A$ reda $n$ s karakterističnim polinomom $f(\lambda)=|\lambda I-A|$ nužno vrijedi $f(A)=0$.

Za linearni operator $T$ vrijedi analogan rezultat: ako je $f(\lambda)$ karakteristični polinom od $T$, onda je $f(T)$ nul-operator.

Iz ovog teorema slijedi da za svaku matricu $A$ postoji polinom koji je poništava.

## Minimalni polinom

Neka je $V$ $n$-dimenzionalni vektorski prostor. Budući da matrica koja odgovara linearnom operatoru ima $n^2$ elemenata, svi linearni operatori tvore $n^2$-dimenzionalni linearni prostor.

Za konkretan linearni operator $T$, od primjene $0$ puta do primjene $n$ puta, ukupno imamo $n^2+1$ linearnih operatora, pa njihove matrice sigurno moraju biti linearno zavisne. Stoga postoji nenul polinom $f$ takav da je $f(T)$ nul-operator; kažemo da operator $T$ zadovoljava polinom $f$. Među svim polinomima $f$ koje $T$ zadovoljava postoji onaj najmanjeg stupnja.

Normirani polinom najmanjeg stupnja koji poništava matricu $A$ zove se minimalni polinom od $A$ i označava se $m_A(\lambda)$.

Prema Euklidovu algoritmu za polinome minimalni polinom je jedinstven i dijeli svaki polinom koji poništava $A$. Posebno, minimalni polinom dijeli karakteristični polinom.

Teorem: Ne računajući kratnosti, karakteristični polinom $f(\lambda)$ i minimalni polinom $m_A(\lambda)$ matrice $A$ imaju iste korijene.

Teorem: Svojstveni vektori matrice $A$ koji pripadaju različitim svojstvenim vrijednostima linearno su nezavisni.

## Primjene

U informatici obično promatramo matrice nad $(\mathbb{Z}/m\mathbb{Z})^{n\times n}$, gdje je $m$ najčešće prost broj; tada je provođenje gornje transformacije sličnosti jednostavno. Kad je $m$ složen broj, možemo postupiti metodom nalik Euklidovu algoritmu.

??? note "Implementacija"
    ```cpp
    #include <cassert>
    #include <iostream>
    #include <random>
    #include <vector>
    
    using Matrix = std::vector<std::vector<int>>;
    using i64 = int64_t;
    
    Matrix to_upper_Hessenberg(const Matrix &M, int mod) {
      Matrix H(M);
      int n = H.size();
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if ((H[i][j] %= mod) < 0) H[i][j] += mod;
        }
      }
      for (int i = 0; i < n - 1; ++i) {
        int pivot = i + 1;
        for (; pivot < n; ++pivot) {
          if (H[pivot][i] != 0) break;
        }
        if (pivot == n) continue;
        if (pivot != i + 1) {
          for (int j = i; j < n; ++j) std::swap(H[i + 1][j], H[pivot][j]);
          for (int j = 0; j < n; ++j) std::swap(H[j][i + 1], H[j][pivot]);
        }
        for (int j = i + 2; j < n; ++j) {
          for (;;) {
            if (H[j][i] == 0) break;
            if (H[i + 1][i] == 0) {
              for (int k = i; k < n; ++k) std::swap(H[i + 1][k], H[j][k]);
              for (int k = 0; k < n; ++k) std::swap(H[k][i + 1], H[k][j]);
              break;
            }
            if (H[j][i] >= H[i + 1][i]) {
              int q = H[j][i] / H[i + 1][i], mq = mod - q;
              for (int k = i; k < n; ++k)
                H[j][k] = (H[j][k] + i64(mq) * H[i + 1][k]) % mod;
              for (int k = 0; k < n; ++k)
                H[k][i + 1] = (H[k][i + 1] + i64(q) * H[k][j]) % mod;
            } else {
              int q = H[i + 1][i] / H[j][i], mq = mod - q;
              for (int k = i; k < n; ++k)
                H[i + 1][k] = (H[i + 1][k] + i64(mq) * H[j][k]) % mod;
              for (int k = 0; k < n; ++k)
                H[k][j] = (H[k][j] + i64(q) * H[k][i + 1]) % mod;
            }
          }
        }
      }
      return H;
    }
    
    std::vector<int> get_charpoly(const Matrix &M, int mod) {
      Matrix H(to_upper_Hessenberg(M, mod));
      int n = H.size();
      std::vector<std::vector<int>> p(n + 1);
      p[0] = {1 % mod};
      for (int i = 1; i <= n; ++i) {
        const std::vector<int> &pi_1 = p[i - 1];
        std::vector<int> &pi = p[i];
        pi.resize(i + 1, 0);
        int v = mod - H[i - 1][i - 1];
        if (v == mod) v -= mod;
        for (int j = 0; j < i; ++j) {
          pi[j] = (pi[j] + i64(v) * pi_1[j]) % mod;
          if ((pi[j + 1] += pi_1[j]) >= mod) pi[j + 1] -= mod;
        }
        int t = 1;
        for (int j = 1; j < i; ++j) {
          t = i64(t) * H[i - j][i - j - 1] % mod;
          int prod = i64(t) * H[i - j - 1][i - 1] % mod;
          if (prod == 0) continue;
          prod = mod - prod;
          for (int k = 0; k <= i - j - 1; ++k)
            pi[k] = (pi[k] + i64(prod) * p[i - j - 1][k]) % mod;
        }
      }
      return p[n];
    }
    
    bool verify(const Matrix &M, const std::vector<int> &charpoly, int mod) {
      if (mod == 1) return true;
      int n = M.size();
      std::vector<int> randvec(n), sum(n, 0);
      std::mt19937 gen(std::random_device{}());
      std::uniform_int_distribution<int> dis(1, mod - 1);
      for (int i = 0; i < n; ++i) randvec[i] = dis(gen);
      for (int i = 0; i <= n; ++i) {
        int v = charpoly[i];
        for (int j = 0; j < n; ++j) sum[j] = (sum[j] + i64(v) * randvec[j]) % mod;
        std::vector<int> prod(n, 0);
        for (int j = 0; j < n; ++j) {
          for (int k = 0; k < n; ++k) {
            prod[j] = (prod[j] + i64(M[j][k]) * randvec[k]) % mod;
          }
        }
        randvec.swap(prod);
      }
      for (int i = 0; i < n; ++i)
        if (sum[i] != 0) return false;
      return true;
    }
    
    int main() {
      std::ios::sync_with_stdio(false);
      std::cin.tie(nullptr);
      int n, mod;
      std::cin >> n >> mod;
      Matrix M(n, std::vector<int>(n));
      for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) std::cin >> M[i][j];
      std::vector<int> charpoly(get_charpoly(M, mod));
      for (int i = 0; i <= n; ++i) std::cout << charpoly[i] << ' ';
      assert(verify(M, charpoly, mod));
      return 0;
    }
    ```

Gornji Hessenbergov algoritam nije numerički stabilan, pa matrice nad $\mathbb{R}^{n\times n}$ prije njegove primjene treba prilagoditi drugim algoritmima ili umjesto njega koristiti neki drugi, numerički stabilan algoritam.

Karakteristični polinom možemo povezati s homogenom linearnom rekurzijom s konstantnim koeficijentima, a u kombinaciji s Cayley–Hamiltonovim teoremom i računanjem ostatka polinoma možemo ubrzati neke algoritme za potenciranje matrica nad poljem.

Cayley–Hamiltonov teorem kaže da je

$$
\begin{aligned}
p_A(A)&=A^n+c_1A^{n-1}+\cdots +c_{n-1}A+c_nI\\
&=O
\end{aligned}
$$

gdje je $O$ nul-matrica dimenzija $n\times n$, $A\in\mathbb{C}^{n\times n}$, a $p_A(x)=x^n+\sum_{i=1}^nc_ix^{n-i}\in\mathbb{C}[x]$ karakteristični polinom od $A$.

Ako želimo izračunati $A^K$ za veliki $K$, možemo izračunati $f(x)=x^K\bmod{p_A(x)}$ i iskoristiti $f(A)=A^K$.

Očito je $\deg(f(x))\lt n$. Neka je $f(x)=\sum_{i=0}^{n-1}f_ix^i$ i $n=km$. Tada je

$$
\begin{aligned}
f_{km-1}x^{km-1}+\cdots +f_1x+f_0&=(\cdots (f_{km-1}x^{k-1}+\cdots +f_{k(m-1)})x^k\\
&+f_{k(m-1)-1}x^{k-1}+\cdots +f_{k(m-2)})x^k\\
&+\cdots\\
&+f_{k-1}x^{k-1}+\cdots +f_1x+f_0
\end{aligned}
$$

Uzmemo li $k=\sqrt{n}$, vidimo da je za računanje $f(A)$ potrebno otprilike $O(\sqrt{n})$ množenja matrice matricom.

## Literatura

-   Rizwana Rehman, Ilse C.F. Ipsen.[La Budde’s Method for Computing Characteristic Polynomials](https://ipsen.math.ncsu.edu/ps/charpoly3.pdf).
-   Marshall Law.[Computing Characteristic Polynomials of Matrices of Structured Polynomials](http://summit.sfu.ca/system/files/iritems1/17301/etd10125_.pdf).
-   Mike Paterson.[On the Number of Nonscalar Multiplications Necessary to Evaluate Polynomials](https://epubs.siam.org/doi/10.1137/0202007).
