---
title: Determinanta
---

Determinanta je operacija nad kvadratnim matricama. Za kvadratnu matricu $A$ s $\det A$ označavamo determinantu matrice $A$.

Ovaj članak uvodi tri definicije determinante. Može se dokazati da su definicije iz ovog članka ekvivalentne.

## Definicija pomoću permutacija

Preduvjeti: [permutacije](../permutation.md), [broj inverzija](../permutation.md#broj-inverzija).

Za ručno računanje determinanti nižeg reda može se koristiti ova metoda; njezina je vremenska složenost reda faktorijela.

Oznakom $\pi(j_1j_2\cdots j_n)$ označavamo broj inverzija permutacije $j_1j_2\cdots j_n$, a $S_n$ je skup svih permutacija duljine $n$. Zapis:

$$
\begin{aligned}
\det A &= \begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots &  & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nn}\\
\end{vmatrix} \\
&= \sum_{(j_1j_2\cdots j_n) \in S_n} (-1)^{\pi(j_1j_2\cdots j_n)} a_{1 j_1} a_{2 j_2}\dots a_{n j_n}
\end{aligned}
$$

označava determinantu $n$-tog reda, koja je algebarski zbroj $n!$ članova; ti su članovi svi mogući umnošci $a_{1j_1}a_{2j_2}\cdots a_{nj_n}$ od $n$ elemenata kvadratne matrice $A$ uzetih iz različitih redaka i različitih stupaca.

Predznak ispred člana $a_{1j_1}a_{2j_2}\cdots a_{nj_n}$ jest ${(-1)}^{\pi(j_1j_2\cdots j_n)}$; drugim riječima, kad je $j_1j_2\cdots j_n$ parna permutacija, predznak je pozitivan, a kad je $j_1j_2\cdots j_n$ neparna permutacija, predznak je negativan.

Pravilo dijagonala za determinante drugog i trećeg reda zapravo je primjena definicije pomoću permutacija. Iz istog se razloga pravilo dijagonala više ne može primijeniti na determinante četvrtog i višeg reda. Posebno, determinanta prvog reda jednaka je samom elementu.

Teorem: iz determinante $n$-tog reda uzmimo elemente iz redaka $i_1,i_2,\cdots,i_n$ i stupaca $j_1,j_2,\cdots,j_n$ i pomnožimo ih

$$
a_{i_1j_1}a_{i_2j_2}\cdots a_{i_nj_n}
$$

gdje su $i_1,i_2,\cdots,i_n$ i $j_1,j_2,\cdots,j_n$ permutacije $n$ brojeva $1,2,\cdots,n$. Tada je predznak tog člana u determinanti ${(-1)}^{s+t}$, gdje je

$$
s=\pi(i_1i_2\cdots i_n)
$$

$$
t=\pi(j_1j_2\cdots j_n)
$$

Teorem: determinanta je jednaka determinanti transponirane matrice.

Teorem: neka se svi elementi $i$-tog retka determinante $\det A$ mogu zapisati kao zbroj dvaju članova:

$$
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
\vdots & \vdots &  & \vdots\\
b_{i1}+c_{i1} & b_{i2}+c_{i2} & \cdots & b_{in}+c_{in}\\
\vdots & \vdots &  & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nn}\\
\end{vmatrix}
$$

Tada je ta determinanta jednaka zbroju dviju determinanti $\det A_1$ i $\det A_2$, gdje je $i$-ti redak matrice $A_1$ jednak $b_{i1},b_{i2},\cdots,b_{in}$, $i$-ti redak matrice $A_2$ jednak $c_{i1},c_{i2},\cdots,c_{in}$, a svi ostali retci matrica $A_1$ i $A_2$ jednaki su onima u $A$. Isto svojstvo vrijedi i za stupce.

## Induktivna definicija

Ova metoda samo opisuje jedno algebarsko svojstvo determinante; njezina je vremenska složenost također reda faktorijela i nije prikladna za računanje.

### Algebarski komplement

U determinanti $n$-tog reda $\det A$ odaberimo bilo kojih $k$ redaka i $k$ stupaca matrice $A$. Matrica $k$-tog reda sastavljena od elemenata na sjecištima tih redaka i stupaca naziva se podmatricom $k$-tog reda, a njezina determinanta minorom $k$-tog reda.

Za determinantu $n$-tog reda $\det A$ podmatrica $M_{ij}$ pridružena elementu $a_{ij}$ jest podmatrica reda $n-1$ koja preostaje kad se iz izvorne matrice $A$ izbrišu redak i stupac u kojima se nalazi $a_{ij}$; njezina determinanta $\det M_{ij}$ naziva se minorom.

Za determinantu $n$-tog reda $\det A$, minora $\det M_{ij}$ elementa $a_{ij}$ pomnožena predznakom ${(-1)}^{i+j}$ naziva se algebarskim komplementom (kofaktorom) elementa $a_{ij}$ i označava simbolom $A_{ij}$.

Iz definicije pomoću permutacija iz prethodnog odjeljka može se izvesti zaključak:

Teorem: ako su u determinanti $n$-tog reda $\det A$ svi elementi $i$-tog retka ili $j$-tog stupca osim $a_{ij}$ jednaki $0$, tada je ta determinanta jednaka umnošku elementa $a_{ij}$ i njegova algebarskog komplementa $A_{ij}$.

### Razvoj determinante

Budući da se determinanta transponiranjem kvadratne matrice ne mijenja, dovoljno je opisati samo jedno od razvoja po retku odnosno po stupcu.

Determinanta $\det A$ definira se kao zbroj umnožaka svih elemenata bilo kojeg njezina retka (ili stupca) s njihovim pripadnim algebarskim komplementima.

Drugim riječima, determinanta se može rekurzivno definirati razvojem po retku (ili po stupcu):

$$
\begin{aligned}
\det A &= a_{i1}A_{i1}+a_{i2}A_{i2}+\cdots+a_{in}A_{in} \\
&= \sum_{j = 1}^{n} a_{ij}A_{ij} \\
&= \sum_{j = 1}^{n} (-1)^{i + j} a_{ij} \det M_{ij}
\end{aligned}
$$

$$
\begin{aligned}
\det A &= a_{1j}A_{1j}+a_{2j}A_{2j}+\cdots+a_{nj}A_{nj} \\
&= \sum_{i = 1}^{n} a_{ij}A_{ij} \\
&= \sum_{i = 1}^{n} (-1)^{i + j} a_{ij} \det M_{ij}
\end{aligned}
$$

Rekurzija završava determinantom matrice prvog reda, koja je jednaka jedinom elementu te matrice.

Odatle slijedi zaključak:

Teorem: zbroj umnožaka elemenata nekog retka (ili stupca) determinante $\det A$ s algebarskim komplementima odgovarajućih elemenata drugog retka (ili drugog stupca) jednak je $0$.

Drugim riječima, za $i\neq j$ vrijedi:

$$
a_{i1}A_{j1}+a_{i2}A_{j2}+\cdots+a_{in}A_{jn}=0
$$

$$
a_{1i}A_{1j}+a_{2i}A_{2j}+\cdots+a_{ni}A_{nj}=0
$$

## Aksiomatska definicija

Aksiomatska definicija kaže da operacija koja zadovoljava određena svojstva može biti jedino determinanta.

Preduvjeti: [elementarne transformacije](./elementary-operations.md).

Označimo s $D_i(k)$ [matricu množenja](./elementary-operations.md#matrica-množenja), s $P_{ij}$ [matricu zamjene](./elementary-operations.md#matrica-zamjene), a s $T_{ij}(k)$ [matricu dodavanja](./elementary-operations.md#matrica-dodavanja).

Operacija $\det$ na matrici $A$ $n$-tog reda naziva se determinantom ako zadovoljava sljedeća četiri svojstva:

-   Pomnožimo li sve elemente nekog retka ili stupca determinante istim brojem $k$, to je isto kao da determinantu pomnožimo s $k$.

    $$
    \det(D_i(k)A) = \det(AD_i(k)) = k \det A
    $$

-   Zamijenimo li dva retka ili dva stupca determinante, determinanta mijenja predznak.

    $$
    \det(P_{ij}A) = \det(AP_{ij}) = -\det A
    $$

-   Pomnožimo li elemente nekog retka ili stupca determinante istim brojem i dodamo ih odgovarajućim elementima drugog retka ili stupca, determinanta se ne mijenja.

    $$
    \det(T_{ij}(k)A) = \det(AT_{ij}(k))= \det A
    $$

-   Determinanta jedinične matrice jednaka je $1$.

    $$
    \det I = 1
    $$

Pomoću svojstava determinante vezanih uz elementarne transformacije mogu se ručno lako računati determinante višeg reda. [Računanje determinante Gaussovom eliminacijom](../numerical/gauss.md#行列式计算) također koristi ta svojstva, uz vremensku složenost $O(n^3)$.

Iz gornjih svojstava slijedi i nekoliko posljedica:

-   Zajednički faktor nekog retka ili stupca determinante može se izlučiti ispred znaka determinante.
-   Ako su svi elementi nekog retka ili stupca determinante jednaki $0$, determinanta je jednaka $0$.
-   Ako su odgovarajući elementi dvaju redaka ili dvaju stupaca determinante proporcionalni, determinanta je jednaka $0$.
-   Ako su dva retka ili dva stupca determinante potpuno jednaka, determinanta je jednaka $0$.

Te se posljedice vrlo često koriste pri ručnom računanju determinanti.
