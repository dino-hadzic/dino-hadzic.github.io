---
title: Gaussova eliminacija
---

## Uvod

Gaussova eliminacija (Gauss–Jordanova eliminacija) klasičan je algoritam za rješavanje sustava linearnih jednadžbi. Ima važno mjesto i vrijednost u suvremenoj matematici te je važan dio nastave linearne algebre.

Osim za rješavanje sustava linearnih jednadžbi, Gaussova eliminacija može se koristiti i za računanje determinanti, nalaženje inverzne matrice te u drugim računalnim i inženjerskim primjenama.

## Metoda eliminacije i ideja Gaussove eliminacije

### Definicija

Metoda eliminacije sastoji se u tome da se nepoznanica iz jedne jednadžbe sustava izrazi algebarskim izrazom koji sadrži drugu nepoznanicu i uvrsti u drugu jednadžbu; time se jedna nepoznanica eliminira i dobiva se rješenje. Ili se jedna jednadžba sustava pomnoži nekom konstantom i doda drugoj jednadžbi, čime se također postiže eliminacija jedne nepoznanice. Metoda eliminacije uglavnom se koristi za rješavanje sustava dviju linearnih jednadžbi s dvije nepoznanice.

### Objašnjenje

Primjer 1: metodom eliminacije riješite sustav dviju linearnih jednadžbi s dvije nepoznanice:

$$
\begin{cases}
4x+y&=100 \\
x-y&=100
\end{cases}
$$

Rješenje: zbrajanjem dviju jednadžbi sustava eliminiramo $y$ i dobivamo:

$$
5x = 200
$$

Rješavanjem dobivamo:

$$
x = 40
$$

Uvrštavanjem $x = 40$ u drugu jednadžbu sustava dobivamo:

$$
y = -60
$$

### Srž teorije metode eliminacije

Srž teorije metode eliminacije uglavnom je sljedeća:

-   zamjenom dviju jednadžbi rješenje se ne mijenja;

-   množenjem jednadžbe brojem $k$ različitim od nule rješenje se ne mijenja;

-   dodavanjem jednadžbe pomnožene brojem $k$ drugoj jednadžbi rješenje se ne mijenja.

### Ideja Gaussove eliminacije

Njemački matematičar Gauss promislio je o metodi eliminacije i analizirao je te došao do sljedećih zaključaka:

-   u metodi eliminacije u računanju sudjeluju i mijenjaju se koeficijenti uz varijable u jednadžbama;

-   same varijable ne sudjeluju u računanju i ne mijenjaju se;

-   varijable se mogu predstaviti položajem koeficijenata, pa se varijable mogu izostaviti;

-   ako se varijable u računanju pojednostavne i izostave, rješenje jednadžbi ostaje nepromijenjeno.

Na temelju tih zaključaka Gauss je predložio Gaussovu eliminaciju: najprije se proširena matrica sustava elementarnim transformacijama redaka svede na reducirani stupčasti ešelonski oblik, zatim se slobodnim nepoznanicama pridruže vrijednosti po kriteriju linearne nezavisnosti i naposljetku se zapiše opće rješenje sustava.

## Gaussova eliminacija u pet koraka

## Objašnjenje

Pridruživanje vrijednosti slobodnim nepoznanicama nakon što se proširena matrica svede na reducirani oblik u Gaussovoj eliminaciji zahtijeva poznavanje linearne zavisnosti, a u tom pridruživanju ima i elemenata ljudskog iskustva, što stvara određene teškoće pri učenju. Zato Gaussovu eliminaciju dijelimo na pet koraka i tako dobivamo metodu pet koraka, čiji je sadržaj sljedeći:

1.  proširenu matricu elementarnim transformacijama redaka svedemo na reducirani stupčasti ešelonski oblik;

2.  rekonstruiramo sustav linearnih jednadžbi;

3.  izrazimo prvu varijablu;

4.  dopunimo slobodne nepoznanice;

5.  zapišemo opće rješenje sustava.

Rad algoritma dodatno ćemo objasniti na primjeru.

## Postupak

Primjer 2: metodom pet koraka Gaussove eliminacije riješite sustav linearnih jednadžbi:

$$
\begin{cases}
2x_1+5x_3+6x_4&=9 \\
x_3+x_4&=-4 \\
2x_3+2x_4&=-8
\end{cases}
$$

### Svođenje proširene matrice (elementarnim) transformacijama redaka na reducirani stupčasti ešelonski oblik

Proširena matrica nova je matrica nastala spajanjem matrice koeficijenata sustava $A$ i stupca konstanti $b$, tj. $(A | b)$. Svođenje proširene matrice elementarnim transformacijama redaka na reducirani stupčasti ešelonski oblik upravo koristi ideju Gaussove eliminacije: varijable se izostavljaju i predstavljaju položajem svojih koeficijenata. Okomita crta u proširenoj matrici odvaja matricu koeficijenata od stupca konstanti i predstavlja znak jednakosti.

$$
\left(\begin{matrix}
2 & 0 & 5 & 6 \\
0 & 0 & 1 & 1 \\
0 & 0 & 2 & 2
\end{matrix} \middle|
\begin{matrix}
9 \\
-4 \\
-8
\end{matrix} \right)
$$

$$
\xrightarrow{r_3-2r_2}
\left(\begin{matrix}
2 & 0 & 5 & 6 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0
\end{matrix} \middle|
\begin{matrix}
9 \\
-4 \\
0
\end{matrix} \right)
$$

svedeno na stupčasti ešelonski oblik

$$
\xrightarrow{\frac{r_1}{2}}
\left(\begin{matrix}
1 & 0 & 2.5 & 3 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0
\end{matrix} \middle|
\begin{matrix}
4.5 \\
-4 \\
0
\end{matrix} \right)
$$

$$
\xrightarrow{r_1-r_2 \times 2.5}
\left(\begin{matrix}
1 & 0 & 0 & 0.5 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0
\end{matrix} \middle|
\begin{matrix}
14.5 \\
-4 \\
0
\end{matrix} \right)
$$

svedeno na reducirani oblik

### Rekonstrukcija sustava linearnih jednadžbi

$$
\begin{cases}
x_1+0.5x_4 &= 14.5\\
x_3+x_4 &= -4 \\
\end{cases}
$$

???+ note "Objašnjenje"
    Rekonstrukcija sustava linearnih jednadžbi znači da se na temelju reduciranog stupčastog ešelonskog oblika sustav ponovno zapiše u obliku linearnih jednadžbi, tj. koeficijentima na pojedinim položajima u reduciranom obliku ponovno se pridruže varijable, a okomita crta u sredini vraća se u znak jednakosti.

### Izražavanje prve varijable

$$
\begin{cases}
x_1 = -0.5x_4+14.5\notag \\
x_3 = -x_4-4\notag
\end{cases}
$$

???+ note "Objašnjenje"
    To znači da se u rekonstruiranom sustavu linearnih jednadžbi prva varijabla svake jednadžbe izrazi pomoću ostalih veličina. Primjerice, prve varijable dviju jednadžbi sustava jesu $x_1$ i $x_3$.

### Dopunjavanje slobodnih nepoznanica

$$
\begin{cases}
x_1 = -0.5x_4+14.5 \\
x_2 = x_2 \\
x_3 = -x_4-4 \\
x_4 = x_4
\end{cases}
$$

???+ note "Objašnjenje"
    U 3. koraku izražene su varijable $x_1$ i $x_3$, iz čega slijedi da preostale varijable $x_2$ i $x_4$ nisu ograničene sustavom jednadžbi; one su slobodne nepoznanice i mogu poprimiti bilo koju vrijednost. Zato rješenje dobiveno u 3. koraku treba dopuniti, i to tako da se zapiše $x_2 = x_2,x_4 = x_4$. Takav način dopunjavanja rješenja u skladu je s definicijom slobodne nepoznanice i lako ga je razumjeti: budući da su slobodne nepoznanice neograničene, mogu biti jednake samo samima sebi.

### Zapis općeg rješenja sustava

$$
\begin{aligned}
\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} &=
\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} x_2+
\begin{pmatrix} -0.5 \\ 0 \\ -1 \\ 1 \end{pmatrix} x_4 +
\begin{pmatrix} 14.5 \\ 0 \\ -4 \\ 0 \end{pmatrix} \\
&= \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} C_1+
\begin{pmatrix} -0.5 \\ 0 \\ -1 \\ 1 \end{pmatrix} C_2 +
\begin{pmatrix} 14.5 \\ 0 \\ -4 \\ 0 \end{pmatrix}
\end{aligned}
$$

pri čemu su $C_1$ i $C_2$ proizvoljne konstante.

???+ note "Objašnjenje"
    To znači da se na temelju 4. koraka rješenje zapiše kao kombinacija vektora stupaca; ujedno, budući da su $x_2$ i $x_4$ slobodne nepoznanice koje mogu poprimiti bilo koju vrijednost, na desnoj strani rješenja postavljamo ih redom na proizvoljne konstante $C_1$ i $C_2$, čime je sustav jednadžbi riješen.

## Računanje determinante

### Objašnjenje

Determinanta (determinant) kvadratne matrice $N \times N$ može se shvatiti kao orijentirani volumen geometrijskog tijela razapetog svim vektorima stupaca.

Primjerice:

$$
\begin{vmatrix}
1 & 0 \\
0 & 1 \end{vmatrix} = 1
$$

$$
\begin{vmatrix}
1 & 2 \\
2 & 1 \end{vmatrix} = -3
$$

Za determinantu vrijedi formula

$$
\operatorname{det}(A)=\sum_{\sigma \in S_{n}} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} a_{i, \sigma(i)}
$$

pri čemu je $S_n$ skup svih permutacija duljine $n$, $\sigma$ je jedna permutacija, a ako je broj inverzija permutacije $\sigma$ paran, tada je $\operatorname{sgn}(\sigma)=1$, inače je $\operatorname{sgn}(\sigma)=−1$.

Razumijevanje invarijantnosti determinante preko pojma volumena vrlo je jednostavan pristup:

-   transponiranjem matrice determinanta se ne mijenja;

-   zamjenom redaka (stupaca) matrice determinanta mijenja predznak;

-   zbrajanjem ili oduzimanjem redaka (stupaca) matrice determinanta se ne mijenja;

-   množenjem svih elemenata retka (stupca) matrice brojem $k$ determinanta se proporcionalno povećava.

Stoga nakon primjene Gaussove eliminacije na matricu dobivamo dijagonalnu matricu čija je determinanta određena umnoškom dijagonalnih elemenata. Njezin se predznak određuje brojem zamjena redaka (ako je neparan, predznak determinante treba promijeniti). Dakle, Gaussovim algoritmom možemo izračunati determinantu matrice u složenosti $O(n^3)$.

Napomena: ako u nekom trenutku u trenutačnom stupcu ne možemo naći element različit od nule, algoritam treba stati i vratiti 0.

### Implementacija

```cpp
constexpr double EPS = 1E-9;
int n;
vector<vector<double>> a(n, vector<double>(n));

double det = 1;
for (int i = 0; i < n; ++i) {
  int k = i;
  for (int j = i + 1; j < n; ++j)
    if (abs(a[j][i]) > abs(a[k][i])) k = j;
  if (abs(a[k][i]) < EPS) {
    det = 0;
    break;
  }
  swap(a[i], a[k]);
  if (i != k) det = -det;
  det *= a[i][i];
  for (int j = i + 1; j < n; ++j) a[i][j] /= a[i][i];
  for (int j = 0; j < n; ++j)
    if (j != i && abs(a[j][i]) > EPS)
      for (int k = i + 1; k < n; ++k) a[j][k] -= a[i][k] * a[j][i];
}

cout << det;
```

## Inverz matrice

Za kvadratnu matricu $A$, ako postoji kvadratna matrica $A^{-1}$ takva da je $A \times A^{-1} = A^{-1} \times A = I$, kažemo da je matrica $A$ invertibilna, a $A^{-1}$ nazivamo njezinom inverznom matricom.

Za zadanu kvadratnu matricu $A$ reda $n$ inverzna se matrica određuje ovako:

1.  konstruiramo matricu $(A, I_n)$ dimenzija $n \times 2n$;
2.  Gaussovom eliminacijom svedemo je na reducirani oblik $(I_n, A^{-1})$ i time dobivamo inverznu matricu $A^{-1}$ matrice $A$. Ako lijeva polovica konačnog reduciranog oblika nije jedinična matrica $I_n$, matrica $A$ nije invertibilna.

Dokaz ispravnosti ove metode zahtijeva dosta znanja iz linearne algebre pa ga zbog ograničenog prostora ovdje ne navodimo. Zainteresirani čitatelji mogu sami potražiti odgovarajuću literaturu.

## Rješavanje sustava XOR jednadžbi Gaussovom eliminacijom

Sustav XOR jednadžbi sustav je oblika

$$
\begin{cases}
a_{1,1}x_1 \oplus a_{1,2}x_2 \oplus \cdots \oplus a_{1,n}x_n &= b_1\\
a_{2,1}x_1 \oplus a_{2,2}x_2 \oplus \cdots \oplus a_{2,n}x_n &= b_2\\
\cdots &\cdots \\ a_{m,1}x_1 \oplus a_{m,2}x_2 \oplus \cdots \oplus a_{m,n}x_n &= b_m
\end{cases}
$$

pri čemu $\oplus$ označava „bitovni isključivi ILI” (tj. `xor`, odnosno `^` u C++-u), a svi koeficijenti/konstante u izrazu (tj. $a_{i,j}$ i $b_i$) jednaki su $0$ ili $1$.

Budući da je „XOR” komutativan i asocijativan, sustav se može rješavati postupnom eliminacijom kao u Gaussovoj eliminaciji. Valja napomenuti da pri eliminaciji koristimo „eliminaciju XOR-om”, a ne „eliminaciju zbrajanjem i oduzimanjem”, te da nije potrebno množiti ni dijeliti radi promjene koeficijenata (jer su svi koeficijenti $0$ ili $1$).

Primijetimo da je proširena matrica sustava XOR jednadžbi $01$-matrica (matrica koja sadrži samo $0$ i $1$), pa za optimizaciju možemo upotrijebiti `std::bitset` iz C++-a i smanjiti vremensku složenost na $O(\dfrac{n^2m}{\omega})$, pri čemu je $n$ broj nepoznanica, $m$ broj jednadžbi, a $\omega$ je obično $32$ (ovisi o stroju).

Referentna implementacija:

```cpp
std::bitset<1010> matrix[2010];  // matrix[1~n]: proširena matrica, na položaju 0 je konstanta

std::vector<bool> GaussElimination(
    int n, int m)  // n je broj nepoznanica, m broj jednadžbi; vraća rješenje sustava
                   // (za više rješenja / bez rješenja vraća prazan vector)
{
  for (int i = 1; i <= n; i++) {
    int cur = i;
    while (cur <= m && !matrix[cur].test(i)) cur++;
    if (cur > m) return std::vector<bool>(0);
    if (cur != i) swap(matrix[cur], matrix[i]);
    for (int j = 1; j <= m; j++)
      if (i != j && matrix[j].test(i)) matrix[j] ^= matrix[i];
  }
  std::vector<bool> ans(n + 1);
  for (int i = 1; i <= n; i++) ans[i] = matrix[i].test(0);
  return ans;
}
```

## Zadaci za vježbu

-   [Codeforces - Wizards and Bets](http://codeforces.com/contest/167/problem/E)
-   [Luogu - SDOI2010 外星千足虫 (Izvanzemaljske stonoge)](https://www.luogu.com.cn/problem/P2447)
