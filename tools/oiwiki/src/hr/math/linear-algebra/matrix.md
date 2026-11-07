---
title: Matrice
---

Ovaj članak uvodi vrlo važan pojam linearne algebre – matricu (matrix). Uglavnom se bavi svojstvima matrica, operacijama s njima te nekim primjenama množenja matrica.

## Vektori i matrice

U linearnoj algebri vektori se dijele na vektore-stupce i vektore-retke.

???+ warning "Upozorenje"
    Na Tajvanu su prijevodi pojmova „列” i „行” upravo obrnuti od onih u kontinentalnoj Kini. Na **OI Wikiju** slijedi se praksa kontinentalne Kine: „列” se prevodi kao stupac (column), a „行” kao redak (row).

Glavni predmet proučavanja linearne algebre jesu vektori-stupci; dogovorno se vektori-stupci označavaju podebljanim malim slovima. U linearnoj algebri, gdje se koristi velik broj vektora i matrica, pri pisanju rukom oznaka vektora (strelica) iznad slova može se izostaviti ako to ne dovodi do zabune.

Vektori su također posebne matrice. Želimo li zapisati vektor-redak, u gornjem desnom kutu podebljanog malog slova pišemo oznaku transponiranja. Vektor-redak u linearnoj algebri obično predstavlja jednadžbu.

## Uvod

Matrice su uvedene zbog sustava linearnih jednadžbi. Slično kao i vektori, matrice utjelovljuju ideju „pakiranja” podataka koji se zatim obrađuju zajedno.

Primjerice, sustav linearnih jednadžbi:

$$
\begin{equation}
    \begin{cases}
        7x_1+8x_2+9x_3=13 \\
        4x_1+5x_2+6x_3=12 \\
        x_1+2x_2+3x_3=11
    \end{cases}
\end{equation}
$$

Matrice se obično označavaju oblim ili uglatim zagradama. Izdvojimo li gornje koeficijente, sustav možemo zapisati u obliku množenja matrica:

$$
\begin{equation}
    \begin{pmatrix}
        7 & 8 & 9 \\
        4 & 5 & 6 \\
        1 & 2 & 3
    \end{pmatrix}\begin{pmatrix}
        x_1 \\ x_2 \\ x_3
    \end{pmatrix}=\begin{pmatrix}
      13 \\ 12 \\ 11
    \end{pmatrix}
\end{equation}
$$

Skraćeno:

$$
Ax=b
$$

Dakle, vektor-stupac nepoznanica x množimo slijeva matricom A i dobivamo vektor-stupac b. Taj se izraz može smatrati osnovnim oblikom linearne algebre.

Glavni računski model koji linearna algebra proučava jest skalarni (unutarnji) produkt. Skalarni je produkt postupak u kojem se najprije množi, a zatim zbraja: vektor-redak množi se slijeva s vektorom-stupcem i rezultat je broj.

Množenje matrica proširenje je skalarnog produkta. Množenje matrica ekvivalentno je tome da iz lijeve matrice izdvojimo redak, iz desne stupac, izračunamo njihov skalarni produkt i tako dobijemo odgovarajući element matrice rezultata; mnemonik glasi „lijevo redak, desno stupac”.

Kad je predmet proučavanja vektor-stupac s desne strane, množenje matrica odgovara množenju vektora-stupca slijeva. S gledišta množenja slijeva, matrica je transformacija vektora-stupaca: svaki vektor-stupac desne matrice u umnošku transformira se i daje odgovarajući vektor-stupac matrice rezultata.

Matrica može transformirati jedan vektor-stupac, može „zapakirano” transformirati skup vektora-stupaca, a može transformirati i cijeli prostor, tj. sve vektore-stupce. Kad se matrica promatra kao transformacija cijelog prostora, ona se odvaja od samog prostora i postaje čista transformacija.

## Definicija

Za matricu $A$ glavnu dijagonalu čine elementi $A_{i,i}$.

Jedinična matrica obično se označava s $I$; na glavnoj dijagonali ima jedinice, a na ostalim mjestima nule.

### Matrice istog tipa

Dvije matrice s jednakim brojem redaka i jednakim brojem stupaca nazivaju se matricama istog tipa.

### Kvadratna matrica

Matrica kojoj je broj redaka jednak broju stupaca naziva se kvadratnom matricom. Kvadratna matrica posebna je vrsta matrice. Uobičajeni izraz „matrica $n$-tog reda” zapravo označava kvadratnu matricu $n$-tog reda. Kvadratne matrice istog reda matrice su istog tipa.

Pri proučavanju sustava jednadžbi, skupova vektora i ranga matrice koriste se opće matrice. Pri proučavanju svojstvenih vrijednosti i svojstvenih vektora te kvadratnih formi koriste se kvadratne matrice.

#### Glavna dijagonala

Elementi kvadratne matrice kojima je indeks retka jednak indeksu stupca čine glavnu dijagonalu.

#### Simetrična matrica

Ako su elementi kvadratne matrice simetrični s obzirom na glavnu dijagonalu, tj. ako je za sve $i$ i $j$ element u $i$-tom retku i $j$-tom stupcu jednak elementu u $j$-tom retku i $i$-tom stupcu, kvadratna matrica naziva se simetričnom matricom.

#### Dijagonalna matrica

Kvadratna matrica kojoj su svi elementi izvan glavne dijagonale jednaki $0$ naziva se dijagonalnom matricom i obično se zapisuje kao:

$$
\operatorname{diag}\{\lambda_1,\cdots,\lambda_n\}
$$

gdje su $\lambda_1,\cdots,\lambda_n$ elementi na glavnoj dijagonali.

Dijagonalna matrica je simetrična matrica.

Ako su svi elementi dijagonalne matrice jednaki $1$, ona se naziva jediničnom matricom i označava s $I$. Kad god je množenje izvedivo, bez obzira na oblik, svaka matrica pomnožena jediničnom matricom ostaje nepromijenjena.

#### Trokutasta matrica

Ako su svi elementi kvadratne matrice ispod glavne dijagonale (dolje lijevo) jednaki $0$, matrica se naziva gornjom trokutastom matricom. Ako su svi elementi iznad glavne dijagonale (gore desno) jednaki $0$, matrica se naziva donjom trokutastom matricom.

Umnožak dviju gornjih (donjih) trokutastih matrica opet je gornja (donja) trokutasta matrica. Ako su svi dijagonalni elementi različiti od $0$, gornja (donja) trokutasta matrica je invertibilna, a njezin je inverz također gornja (donja) trokutasta matrica.

#### Jedinična trokutasta matrica

Ako su svi dijagonalni elementi gornje trokutaste matrice $A$ jednaki $1$, kažemo da je $A$ jedinična gornja trokutasta matrica. Ako su svi dijagonalni elementi donje trokutaste matrice $A$ jednaki $1$, kažemo da je $A$ jedinična donja trokutasta matrica.

Umnožak dviju jediničnih gornjih (donjih) trokutastih matrica opet je jedinična gornja (donja) trokutasta matrica, a i inverz jedinične gornje (donje) trokutaste matrice jedinična je gornja (donja) trokutasta matrica.

## Operacije

### Linearne operacije s matricama

Linearne operacije s matricama jesu zbrajanje, oduzimanje i množenje skalarom; sve se izvode element po element. Zbrajati i oduzimati mogu se samo matrice istog tipa.

### Transponiranje matrice

Transponiranje matrice označava se tako da se u gornjem desnom kutu matrice napiše oznaka transponiranja „T”; ono znači da matrici zamjenjujemo retke i stupce.

Simetrična matrica transponiranjem ostaje nepromijenjena.

### Množenje matrica

Množenje matrica poopćenje je skalarnog produkta vektora.

Umnožak matrica ima smisla samo kad je broj stupaca prve matrice jednak broju redaka druge.

Neka je $A$ matrica tipa $P \times M$, $B$ matrica tipa $M \times Q$, a $C$ umnožak matrica $A$ i $B$;

tada se element u $i$-tom retku i $j$-tom stupcu matrice $C$ može zapisati kao:

$$
C_{i,j} = \sum_{k=1}^MA_{i,k}B_{k,j}
$$

Pri množenju matrica broj u $i$-tom retku i $j$-tom stupcu rezultata $C$ dobiva se tako da se $M$ brojeva $i$-tog retka matrice $A$ i $M$ brojeva $j$-tog stupca matrice $B$ **pomnože pa zbroje**. To **množenje pa zbrajanje** upravo je skalarni produkt vektora. Broj u $i$-tom retku i $j$-tom stupcu matrice umnoška upravo je skalarni produkt $i$-tog vektora-retka množitelja $A$ i $j$-tog vektora-stupca množitelja $B$; mnemonik glasi **lijevo redak, desno stupac**.

Vektori koje proučava linearna algebra većinom su vektori-stupci; prema ovakvoj definiciji množenja matrica često se proučava operacija množenja slijeva, tj. množenje vektora-stupca matricom slijeva, a ujedno se ovdje vidi i ideja „paketne obrade”: istodobno se obrađuje mnogo skalarnih produkata vektora.

Množenje matrica zadovoljava asocijativnost, ali ne zadovoljava komutativnost u općem slučaju.

Koristeći asocijativnost, množenje matrica može se optimizirati idejom [brzog potenciranja](../binary-exponentiation.md).

Na natjecanjima se, budući da se linearne rekurzije mogu zapisati u obliku množenja matrica, brzo potenciranje matrica također često koristi za računanje pojedinog člana linearno rekurzivnog niza.

#### Optimizacija

Prije svega, za razmjerno male matrice može se razmotriti ručno odmotavanje petlji radi smanjenja konstante.

Petlje se mogu preurediti kako bi se poboljšala prostorna lokalnost; takva optimizacija ne mijenja vremensku složenost množenja matrica, ali daje poboljšanje na razini konstante.

```cpp
// Na primjeru referentnog koda iz nastavka
mat operator*(const mat& T) const {
  mat res;
  for (int i = 0; i < sz; ++i)
    for (int j = 0; j < sz; ++j)
      for (int k = 0; k < sz; ++k) {
        res.a[i][j] += mul(a[i][k], T.a[k][j]);
        res.a[i][j] %= MOD;
      }
  return res;
}

// lošije je od
mat operator*(const mat& T) const {
  mat res;
  int r;
  for (int i = 0; i < sz; ++i)
    for (int k = 0; k < sz; ++k) {
      r = a[i][k];
      for (int j = 0; j < sz; ++j)
        res.a[i][j] += T.a[k][j] * r, res.a[i][j] %= MOD;
    }
  return res;
}
```

### Inverz kvadratne matrice

Inverzna matrica $P$ kvadratne matrice $A$ matrica je za koju vrijedi $A \times P = I$.

Inverzna matrica ne mora postojati. Ako postoji, može se izračunati [Gaussovom eliminacijom](../numerical/gauss.md).

### Determinanta kvadratne matrice

Determinanta je operacija nad kvadratnim matricama.

## Referentni kôd

Općenito, matrica se može simulirati dvodimenzionalnim poljem.

```cpp
struct mat {
  LL a[sz][sz];

  mat() { memset(a, 0, sizeof a); }

  mat operator-(const mat& T) const {
    mat res;
    for (int i = 0; i < sz; ++i)
      for (int j = 0; j < sz; ++j) {
        res.a[i][j] = (a[i][j] - T.a[i][j]) % MOD;
      }
    return res;
  }

  mat operator+(const mat& T) const {
    mat res;
    for (int i = 0; i < sz; ++i)
      for (int j = 0; j < sz; ++j) {
        res.a[i][j] = (a[i][j] + T.a[i][j]) % MOD;
      }
    return res;
  }

  mat operator*(const mat& T) const {
    mat res;
    int r;
    for (int i = 0; i < sz; ++i)
      for (int k = 0; k < sz; ++k) {
        r = a[i][k];
        for (int j = 0; j < sz; ++j)
          res.a[i][j] += T.a[k][j] * r, res.a[i][j] %= MOD;
      }
    return res;
  }

  mat operator^(LL x) const {
    mat res, bas;
    for (int i = 0; i < sz; ++i) res.a[i][i] = 1;
    for (int i = 0; i < sz; ++i)
      for (int j = 0; j < sz; ++j) bas.a[i][j] = a[i][j] % MOD;
    while (x) {
      if (x & 1) res = res * bas;
      bas = bas * bas;
      x >>= 1;
    }
    return res;
  }
};
```

## Dva pogleda na sustav linearnih jednadžbi

Matricu A, odnosno transformaciju A, možemo promatrati na dva načina.

Prvi pogled: po retcima, promatramo svaki redak matrice A. Tako A shvaćamo kao sustav jednadžbi, iz čega proizlazi rješavanje jednadžbi metodom eliminacije.

Drugi pogled: po stupcima, promatramo svaki stupac matrice A. Sama matrica A sastavljena je od vektora-stupaca. Tada transformaciju A promatramo kao skup vektora-stupaca, a x su nepoznati koeficijenti; pitamo se može li se taj skup vektora-stupaca iz A, uz prikladne nepoznanice, složiti u vektor-stupac b.

Primjerice, primjer s početka članka postaje:

$$
\begin{equation}
    \begin{pmatrix}
        7 \\ 4 \\ 1
    \end{pmatrix}x_1+\begin{pmatrix}
        8 \\ 5 \\ 2
    \end{pmatrix}x_2+\begin{pmatrix}
        9 \\ 6 \\ 3
    \end{pmatrix}x_3=\begin{pmatrix}
      13 \\ 12 \\ 11
    \end{pmatrix}
\end{equation}
$$

Rješavanje sustava svodi se na pitanje možemo li podešavanjem triju koeficijenata x od zadanih triju baznih vektora složiti vektor rezultata.

Pogled po stupcima noviji je od pogleda po retcima. Iz perspektive stupaca mogu se proučavati linearna nezavisnost i linearna zavisnost.

## Primjene množenja matrica

### Ubrzavanje rekurzija matricama

Uzmimo za primjer [Fibonaccijev niz (Fibonacci sequence)](../combinatorics/fibonacci.md). U Fibonaccijevu nizu vrijedi $F_1 = F_2 = 1$, $F_i = F_{i - 1} + F_{i - 2}(i \geq 3)$.

Ako zadatak traži vrijednost $n$-tog člana Fibonaccijeva niza, najjednostavnije ga je izračunati izravno rekurzijom. No ako $n$ doseže red veličine $10^{18}$, rekurzija više ne dolazi u obzir; tada možemo razmotriti ubrzavanje rekurzije matricama.

Prema [matričnom obliku rekurzivne formule](../combinatorics/fibonacci.md#matrični-oblik) Fibonaccijeva niza:

$$
\begin{bmatrix}
  F_{n-1} & F_{n-2}
\end{bmatrix} \begin{bmatrix}
  1 & 1 \\
  1 & 0
\end{bmatrix} = \begin{bmatrix}
  F_n & F_{n-1}
\end{bmatrix}
$$

Definirajmo početnu matricu $\text{ans} = \begin{bmatrix}F_2 & F_1\end{bmatrix} = \begin{bmatrix}1 & 1\end{bmatrix}, \text{base} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$. Tada je $F_n$ jednak elementu u prvom retku i prvom stupcu matrice $\text{ans} \text{base}^{n-2}$, odnosno elementu u prvom retku i prvom stupcu matrice $\begin{bmatrix}1 & 1\end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{n-2}$.

???+ warning "Napomena"
    Množenje matrica nije komutativno, pa se nipošto ne smije pisati „element u prvom retku i prvom stupcu matrice $\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{n-2} \begin{bmatrix}1 & 1\end{bmatrix}$”. Osim toga, za $n \leq 2$ dovoljno je izravno ispisati $1$, bez brzog potenciranja matrica.

Zašto množimo potencijom $n-2$, a ne potencijom $n$ matrice $\text{base}$? Zato što se $F_1, F_2$ mogu dobiti bez ikakva množenja matrica. Drugim riječima, već nakon jednog množenja dobivamo $F_3$. Ako još uvijek nije jasno zašto je eksponent $n-2$, preporučujemo da to izračunate rukom.

Slijedi primjer koda (ključni dio) koji računa $n$-ti član Fibonaccijeva niza modulo $10^9+7$.

```cpp
constexpr int mod = 1000000007;

struct Matrix {
  int a[3][3];

  Matrix() { memset(a, 0, sizeof a); }

  Matrix operator*(const Matrix &b) const {
    Matrix res;
    for (int i = 1; i <= 2; ++i)
      for (int j = 1; j <= 2; ++j)
        for (int k = 1; k <= 2; ++k)
          res.a[i][j] = (res.a[i][j] + a[i][k] * b.a[k][j]) % mod;
    return res;
  }
} ans, base;

void init() {
  base.a[1][1] = base.a[1][2] = base.a[2][1] = 1;
  ans.a[1][1] = ans.a[1][2] = 1;
}

void qpow(int b) {
  while (b) {
    if (b & 1) ans = ans * base;
    base = base * base;
    b >>= 1;
  }
}

int main() {
  int n = read();
  if (n <= 2) return puts("1"), 0;
  init();
  qpow(n - 2);
  println(ans.a[1][1] % mod);
}
```

Evo nešto složenijeg primjera.

$$
\begin{gathered}
f_{1} = f_{2} = 0\\
f_{n} = 7f_{n-1}+6f_{n-2}+5n+4\times 3^n
\end{gathered}
$$

Primjećujemo da $f_n$ ovisi o $f_{n-1}, f_{n-2}, n$, pa pokušavamo konstruirati matricu koja opisuje stanje.

No ako matrica sadrži samo ta tri elementa $\begin{bmatrix}f_n& f_{n-1}& n\end{bmatrix}$, teško je konstruirati jednadžbu prijelaza, jer se potenciranje i $+1$ ne mogu opisati matricom.

Zato konstruiramo veću matricu.

$$
\begin{bmatrix}f_n& f_{n-1}& n& 3^n & 1\end{bmatrix}
$$

Želimo konstruirati matricu rekurzije koja prelazi u

$$
\begin{bmatrix}
f_{n+1}& f_{n}& n+1& 3^{n+1} & 1
\end{bmatrix}
$$

Matrica prijelaza glasi

$$
\begin{bmatrix}
7 & 1 & 0 & 0 & 0\\
6 & 0 & 0 & 0 & 0\\
5 & 0 & 1 & 0 & 0\\
12 & 0 & 0 & 3 & 0\\
5 & 0 & 1 & 0 & 1
\end{bmatrix}
$$

### Izražavanje izmjena matricama

???+ note "[「THUSCH 2017」大魔法师 (Veliki čarobnjak)](https://loj.ac/p/2980)"
    Veliki čarobnjak mali L izradio je $n$ čarobnih kristalnih kugli; svaka kugla ima vrijednosti energije triju svojstava: vode, vatre i zemlje. Mali L poredao je tih $n$ kugli na tlu u red, sprijeda prema natrag, i započeo današnju čarobnjačku predstavu.
    
    S $A_i,\ B_i,\ C_i$ označavamo redom energiju vode, vatre i zemlje $i$-te kugle gledano sprijeda (indeksi počinju od $1$).
    
    Mali L planira izvesti $m$ čarolija. Svaki put odabire interval $[l, r]$ i zatim izvodi jednu od sljedećih $7$ vrsta čarolija, podijeljenih u $3$ skupine:
    
    1.  Pobuđivanje čarobne moći: energija **određenog svojstva** svake kugle u intervalu eksplodira i time pojačava energiju drugog **određenog svojstva**. Konkretno, postoje tri moguća oblika:
    
        -   element vatre pobuđuje energiju vode: $A_i = A_i + B_i$.
        -   element zemlje pobuđuje energiju vatre: $B_i = B_i + C_i$.
        -   element vode pobuđuje energiju zemlje: $C_i = C_i + A_i$.
    
            **Valja napomenuti da pojačavanje energije jednog svojstva ne mijenja energiju drugog svojstva; primjerice, $A_i = A_i + B_i$ ne povećava niti smanjuje $B_i$.**
    2.  Pojačavanje čarobne moći: mali L zamahne štapom i potroši $v$ bodova vlastite magije kako bi promijenio energiju **određenog svojstva** svake kugle u intervalu. Konkretno, postoje tri moguća oblika:
    
        -   energija vatre pojačava se za konstantu: $A_i = A_i + v$.
        -   energija vode pojačava se množenjem: $B_i=B_i \cdot v$.
        -   energija zemlje apsorbira se i stapa: $C_i = v$.
    3.  Oslobađanje čarobne moći: mali L skuplja energiju svih kugli u intervalu, stapa ih u novu kristalnu kuglu i daruje je gledateljima. Energija svakog svojstva nastale kugle jednaka je algebarskom zbroju odgovarajućih energija svih kugli u intervalu. **Valja napomenuti da oslobađanje čarobne moći zapravo ne mijenja energiju kugli u intervalu.**
    
    Vrijedi spomenuti da su kugle koje mali L izrađuje i stapa načinjene od posebno naručenih kristala iz tvornice OI, pa te kugle imaju prag energije $998244353$. Kad energija nekog svojstva kugle postane veća ili jednaka tom pragu, energija se automatski uzima modulo prag, čime se sprječava eksplozija kugle.
    
    Mali W, (jedini) gledatelj malog L, pratio je cijelu predstavu i primio svaku kuglu koju je mali L tijekom predstave stopio. Mali W želi znati koliko iznose energije triju svojstava tih kugli.

Budući da za matrice vrijede asocijativnost i distributivnost, izmjena u jednoj točki prirodno se poopćuje na interval: nakon što izvedemo matrice, dovoljno je segment treeom održavati umnožak matrica na intervalu.

U nastavku navodimo nekoliko primjera.

Prijelaz za $A_i = A_i + v$

$$
\begin{bmatrix}
A & B & C & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
v & 0 & 0 & 1\\
\end{bmatrix}=
\begin{bmatrix}
A+v & B & C & 1\\
\end{bmatrix}
$$

Prijelaz za $B_i=B_i \cdot v$

$$
\begin{bmatrix}
A & B & C & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & v & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{bmatrix}=
\begin{bmatrix}
A & B \cdot v & C & 1\\
\end{bmatrix}
$$

???+ note "[「LibreOJ 6208」树上询问 (Upiti na stablu)](https://loj.ac/p/6208)"
    Zadano je stablo s $n$ čvorova, korijen je čvor $1$. Svaki čvor ima dvije težine $k_i, t_i$, obje početno $0$.
    
    Zadane su tri vrste operacija:
    
    1.  operacija $\operatorname{Add}( x , d )$: svim čvorovima na putu od $x$ do korijena $k_i\leftarrow k_i + d$
    2.  operacija $\operatorname{Mul}( x , d )$: svim čvorovima na putu od $x$ do korijena $t_i\leftarrow t_i + d \times k_i$
    3.  operacija $\operatorname{Query}( x )$: upit za težinu $t_x$ čvora $x$
    
        $n,~m \leq 100000, ~-10 \leq d \leq 10$

Ako razmišljamo izravno, nije lako smisliti kako spuštati operacije i održavati podatke. No matricama se to lako izražava.

$$
\begin{aligned}
\begin{bmatrix}k & t & 1 \end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
d & 0 & 1
\end{bmatrix}
&=
\begin{bmatrix}k+d & t & 1 \end{bmatrix}\\
\begin{bmatrix}k & t & 1 \end{bmatrix}
\begin{bmatrix}
1 & d & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
&=
\begin{bmatrix}k & t+d \times k & 1 \end{bmatrix}
\end{aligned}
$$

### Prebrojavanje putova zadane duljine

???+ note "Opis problema"
    Zadan je usmjereni graf s $n$ vrhova u kojem svaki brid ima težinu $1$, te cijeli broj $k$. Za svaki par vrhova $(u,v)$ treba odrediti broj putova duljine $k$ od $u$ do $v$ (ne nužno jednostavnih, tj. vrhovi i bridovi na putu smiju se ponavljati).

Usmjereni graf prikazujemo matricom susjedstva $G$ (za svaki brid $(u\to v)$ grafa stavimo $G[u,v]=1$, a ostali su elementi $0$; ako postoje višestruki bridovi, $G[u,v]$ je broj višestrukih bridova). Algoritam u nastavku radi i kad graf ima petlje.

Očito ta matrica susjedstva odgovara odgovoru za $k=1$.

Pretpostavimo da znamo matricu brojeva putova duljine $k$, označimo je $C_k$, i želimo izračunati $C_{k+1}$. Očito vrijedi DP prijelaz

$$
C_{k+1}[i,j] = \sum_{p = 1}^{n} C_k[i,p] \cdot G[p,j]
$$

To možemo shvatiti kao množenje matrica, pa se gornji prijelaz može opisati kao

$$
C_{k+1} = C_k \cdot G
$$

Raspišemo li tu rekurziju, dobivamo

$$
C_k = \underbrace{G \cdot G \cdots G}_{k \text{ puta}} = G^k
$$

Za računanje te potencije matrice možemo primijeniti ideju brzog potenciranja (binarnog potenciranja) i rezultat dobiti u složenosti $O(n^3 \log k)$.

### Najkraći put zadane duljine

???+ note "Opis problema"
    Zadan je težinski usmjereni graf s $n$ vrhova i cijeli broj $k$. Za svaki par vrhova $(u,v)$ treba pronaći duljinu najkraćeg puta od $u$ do $v$ koji sadrži točno $k$ bridova. (Put ne mora biti jednostavan, tj. vrhovi i bridovi na putu smiju se ponavljati.)

Opet konstruiramo matricu susjedstva $G$ tog grafa, gdje $G[i,j]$ označava težinu brida od $i$ do $j$. Ako između vrhova $i,j$ nema brida, onda je $G[i,j]=\infty$. (Kod višestrukih bridova uzimamo najmanju težinu.)

Očito gornja matrica odgovara odgovoru na problem za $k=1$. Opet pretpostavimo da znamo odgovor za $k$, označimo ga matricom $L_k$. Sada želimo odgovor za $k+1$. Očito vrijedi prijelaz

$$
L_{k+1}[i,j] = \min_{1\le p \le n} \left\{L_k[i,p] + G[p,j]\right\}
$$

Zapravo ovo možemo usporediti s množenjem matrica: primjećujemo da gornji prijelaz samo zamjenjuje zbrajanje umnožaka u množenju matrica zbrajanjem pa uzimanjem minimuma, pa tu operaciju definiramo kao $\odot$, tj.

$$
A \odot B = C~~\Longleftrightarrow~~C[i,j]=\min_{1\le p \le n}\left\{A[i,p] + B[p,j]\right\}
$$

Tako dobivamo

$$
L_{k+1} = L_k \odot G
$$

Raspisivanjem rekurzije dobivamo

$$
L_k = \underbrace{G \odot \ldots \odot G}_{k\text{ puta}} = G^{\odot k}
$$

Gornji izraz i dalje možemo računati brzim potenciranjem matrica, jer je operacija očito asocijativna. Vremenska složenost je $O(n^3 \log k)$.

### Prebrojavanje putova / najkraći put ograničene duljine

Gornji algoritmi primjenjivi su samo kad je broj bridova fiksan. Međutim, algoritam možemo poboljšati tako da rješava i slučaj kad je broj bridova manji ili jednak $k$. Konkretno, promotrimo sljedeći problem:

???+ note "Opis problema"
    Zadan je usmjereni graf s $n$ vrhova čiji bridovi imaju težinu $1$, te cijeli broj $k$. Za svaki par vrhova $(u,v)$ treba pronaći broj putova od $u$ do $v$ duljine manje ili jednake $k$ (ne nužno jednostavnih, tj. vrhovi i bridovi na putu smiju se ponavljati).

Za svaki vrh $v$ uvodimo pomoćni vrh $v'$ koji bilježi odgovor te u graf dodajemo bridove $(v,v')$ i $(v',v')$. Tada je za par vrhova $(u,v)$ broj putova od $u$ do $v$ s najviše $k$ bridova jednak broju putova od $u$ do $v'$ s točno $k+1$ bridova, jer svakom putu s $m(m \le k)$ bridova $(p_0=u)\to p_1\to p_2 \to \dots \to p_{m-1} \to (p_m=v)$ obostrano jednoznačno odgovara put s $k+1$ bridova $(p_0=u)\to p_1 \to p_2 \to \dots \to p_{m-1} \to (p_m=v) \to v'  \to \dots \to v'$.

Za najkraći put s najviše $k$ bridova dovoljno je svakom vrhu dodati petlju težine $0$.

## Zadaci za vježbu

-   [Luogu P1962 斐波那契数列 (Fibonaccijev niz)](https://www.luogu.com.cn/problem/P1962), upravo gornji primjer; isti zadatak kao POJ3070
-   [Luogu P1349 广义斐波那契数列 (Poopćeni Fibonaccijev niz)](https://www.luogu.com.cn/problem/P1349), matricu $\text{base}$ treba malo izmijeniti
-   [Luogu P1939【模板】矩阵加速（数列）(Predložak: ubrzavanje nizova matricama)](https://www.luogu.com.cn/problem/P1939), matrica $\text{base}$ postaje matrica $3 \times 3$, a izvod je sličan gornjemu.

**Dio ove stranice preveden je iz članka [Кратчайшие пути фиксированной длины, количества путей фиксированной длины](http://e-maxx.ru/algo/fixed_length_paths) i njegova engleskog prijevoda [Number of paths of fixed length/Shortest paths of fixed length](https://cp-algorithms.com/graph/fixed_length_paths.html). Ruska je inačica pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0.**
