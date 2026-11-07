---
title: Dijagonalizacija
---

## Svojstveni potprostor

Svi svojstveni vektori matrice $A$ koji pripadaju svojstvenoj vrijednosti $\lambda_0$, zajedno s nul-vektorom, tvore linearni prostor koji zovemo svojstvenim potprostorom matrice $A$ i označavamo $E(\lambda_0)$. To je prostor rješenja homogenog linearnog sustava:

$$
(\lambda_0 I-A)X=0
$$

tj. skup svih rješenja tog sustava.

Za svojstveni potprostor $E(\lambda_i)=N(\lambda_i I-A)$ iz teorema o rangu i defektu slijedi:

$$
r(\lambda_i I-A)+\operatorname{dim} N(\lambda_i I-A)=n
$$

Stoga je dimenzija svojstvenog potprostora $E(\lambda_i)$ jednaka:

$$
\operatorname{dim} E(\lambda_i)=n-r(\lambda_i I-A)
$$

Ona se zove i **geometrijska kratnost** od $\lambda_i$.

## Invarijantni potprostor

Pri proučavanju linearnog operatora $T$ često želimo odabrati bazu prostora $V$ u kojoj matrica linearnog operatora $T$ ima što jednostavniji oblik.

Neka je $V$ linearni prostor nad poljem $F$, $W$ potprostor od $V$, a $T$ linearni operator na $V$. Ako za svaki vektor $x$ iz $W$ i $T(x)$ leži u $W$ (kažemo i da je potprostor invarijantan ili stabilan pod operatorom), kažemo da je $W$ invarijantni potprostor od $T$.

Da je prostor invarijantan pod operatorom ne znači da koordinate doista ostaju „nepromijenjene”; moguće je da se provodi, primjerice, rastezanje ili neka druga deformacija, samo što rezultat i dalje ostaje u tom prostoru.

-   Svaki potprostor linearnog prostora $V$ invarijantni je potprostor množenja skalarom.
-   Za svaki linearni operator $T$ na $V$, prostor $V$ i nul-potprostor invarijantni su potprostori od $T$; zovemo ih trivijalnim invarijantnim potprostorima.
-   Presjek i zbroj invarijantnih potprostora također su invarijantni potprostori.

Neka je $W$ invarijantni potprostor linearnog operatora $T$. Promatramo li samo djelovanje operatora $T$ na invarijantnom potprostoru $W$, dobivamo linearni operator na samom potprostoru $W$; zovemo ga restrikcijom operatora $T$ na potprostor $W$ i označavamo ${T|}_W$.

Za svaki linearni operator $T$ na $V$, slika $R(T)$ i jezgra $N(T)$ invarijantni su potprostori od $T$. Značenje tih dvaju slučajeva jest da se prostor $V$ pod operatorom sažima u sebe (slika) ili sažima u $0$ (jezgra).

Za svaki linearni operator $T$ na $V$, svojstveni potprostori od $T$ invarijantni su potprostori od $T$.

## Primarna dekompozicija

Prema osnovnom teoremu algebre minimalni polinom može se faktorizirati kao:

$$
m_A(\lambda)={(\lambda-\lambda_1)}^{r_1}\cdots{(\lambda-\lambda_S)}^{r_S}
$$

Uvrstimo li u minimalni polinom umjesto varijable $\lambda$ matricu $A$, jezgre pojedinih faktora tvore niz invarijantnih potprostora matrice $A$:

$$
W_i=N({(\lambda_i I-A)}^{r_i})
$$

Teorem: Dimenzija tog invarijantnog potprostora $W_i$ jednaka je upravo algebarskoj kratnosti svojstvene vrijednosti $\lambda_i$.

Podsjetimo se: algebarska kratnost je stupanj odgovarajućeg faktora karakterističnog polinoma, a geometrijska kratnost je dimenzija svojstvenog potprostora $E(\lambda_i)=N(\lambda_i I-A)$. Taj invarijantni potprostor $W_i$ i svojstveni potprostor $E(\lambda_i)$ oba su jezgre matrica, a te dvije matrice odnose se kao matrica i njezina $r_i$-ta potencija iz minimalnog polinoma. Drugim riječima, dimenzija svojstvenog potprostora je geometrijska kratnost, a „svojstveni potprostor” nakon podizanja na $r_i$-tu potenciju iz minimalnog polinoma postaje „invarijantni potprostor” čija dimenzija doseže algebarsku kratnost iz karakterističnog polinoma.

Taj je teorem zapravo korolar sljedećeg teorema o primarnoj dekompoziciji.

Označimo s $T$ linearni operator koji odgovara matrici $A$, a s $T_i={T|}_{W_i}$ njegovu restrikciju na svaki potprostor $W_i$. Tada je minimalni polinom od $T_i$ jednak $(x-\lambda_i)^{r_i}$.

Teorem: Neka je $V$ linearni prostor nad poljem $F$, a $T$ linearni operator na $V$. Tada se prostor $V$ može primarno dekomponirati u odnosu na linearni operator $T$, tj. rastaviti na direktnu sumu nekoliko invarijantnih potprostora $W_i$.

$$
V=W_1\oplus W_2\oplus\cdots\oplus W_S
$$

To znači da je matrica od $T$ u nekoj bazi blok-dijagonalna (kvazidijagonalna):

$$
\operatorname{diag}\{A_1,A_2,\cdots,A_S\}
$$

gdje je $A_i$ matrica od $T_i$ u odgovarajućoj bazi.

Teorem pokazuje da se invarijantnim potprostorima može pojednostavniti matrica linearnog operatora.

## Dijagonalizabilne matrice

Ako je kvadratna matrica $A$ reda $n$ slična nekoj dijagonalnoj matrici, kažemo da je $A$ dijagonalizabilna matrica ili da je jednostavna (semisimple) matrica.

-   Zbroj, produkt i inverz dijagonalnih matrica, ako postoje, opet su dijagonalne matrice, a elementi na dijagonali upravo su njihove svojstvene vrijednosti.
-   Matrica linearnog operatora $T$ dijagonalizabilna je ako i samo ako je matrica od $T$ u nekoj bazi dijagonalna.

Teorem: Neka su $\lambda_1,\cdots,\lambda_m$ sve međusobno različite svojstvene vrijednosti matrice $A$. Tada su sljedeće tvrdnje ekvivalentne:

-   Matrica $A$ je dijagonalizabilna.
-   Matrica $A$ ima $n$ linearno nezavisnih svojstvenih vektora.
-   Vrijedi sljedeća formula:

$$
\operatorname{dim} E(\lambda_1)+\cdots+\operatorname{dim} E(\lambda_m)=n
$$

Već smo spomenuli da se stupanj svojstvene vrijednosti u faktorizaciji karakterističnog polinoma zove algebarska kratnost, a dimenzija svojstvenog potprostora geometrijska kratnost. Ovaj teorem pokazuje i da je matrica $A$ dijagonalizabilna ako i samo ako je za svaku svojstvenu vrijednost $\lambda$ od $A$ algebarska kratnost jednaka geometrijskoj kratnosti.

Korolar: Ako kvadratna matrica $A$ reda $n$ ima točno $n$ međusobno različitih svojstvenih vrijednosti, onda je nužno dijagonalizabilna. Obrat ne mora vrijediti.

Teorem: Matrica $A$ dijagonalizabilna je ako i samo ako minimalni polinom od $A$ nema višestrukih korijena.

Sličnost matrica također čuva odnose linearne zavisnosti među svojstvenim vektorima.

Svojstveni vektori sasvim lako mogu biti nerealni, a sasvim je moguće i da se ne može naći $n$ linearno nezavisnih svojstvenih vektora.

Za višestruku svojstvenu vrijednost svojstveni vektori razapinju prostor. Da bismo opisali taj prostor, iz njega treba odabrati predstavnike. Obično se biraju linearno nezavisni predstavnici, a broj predstavnika jednak je dimenziji prostora.

Pri odabiru predstavnika često ih ortogonaliziramo i normiramo. Na kraju dobivamo skup ortonormiranih predstavnika.

Svojstveni vektori ne moraju biti ortogonalni; svojstvene vektore različitih svojstvenih vrijednosti možda nije moguće ortogonalizirati. Zato se ortogonalizacija može provesti samo na svojstvenim vektorima višestruke svojstvene vrijednosti. Normirati se, međutim, može svaki svojstveni vektor.

## Nilpotentne matrice

Neka je $T$ linearni operator na prostoru $V$. Ako postoji prirodan broj $r$ takav da je $T^r$ nul-operator, kažemo da je $T$ nilpotentan operator na prostoru $V$.

Matrica koja za neki prirodan broj $r$ zadovoljava uvjet $N^r=0$ zove se nilpotentna matrica.

Obično se dodatno može pretpostaviti da je $r$ najmanji prirodan broj za koji je $T^r$ nul-operator; tada je minimalni polinom od $T$ jednak $x^r$. Stoga postoji vektor $\xi_0$ takav da:

-   $$
    T^r(\xi_0)=0
    $$
-   $$
    T^{r-1}(\xi_0)\neq 0
    $$

### Ciklički potprostor

Teorem: Neka je $T$ linearni operator na prostoru $V$, a $\xi$ vektor iz prostora $V$. Ako postoji prirodan broj $s$ takav da:

-   $$
    T^s(\xi)=0
    $$
-   $$
    T^{s-1}(\xi)\neq 0
    $$

onda su vektori $\xi,T(\xi),\cdots,T^{s-1}(\xi)$ linearno nezavisni.

Na temelju tog teorema možemo dati definiciju:

Neka je $T$ linearni operator na prostoru $V$, a $W$ potprostor od $V$. Ako postoje vektor $\xi_0$ i prirodan broj $r$ takvi da:

-   vektori $\xi_0,T(\xi_0),\cdots,T^{r-1}(\xi_0)$ tvore bazu od $W$,
-   vrijedi jednakost:

    $$
    T^r(\xi_0)=0
    $$

onda potprostor $W$ zovemo cikličkim potprostorom u odnosu na $T$, kraće $T$-cikličkim potprostorom. Pritom $\xi_0$ zovemo generirajućim vektorom cikličkog potprostora $W$, a vektore $\xi_0,T(\xi_0),\cdots,T^{r-1}(\xi_0)$ cikličkom bazom od $W$.

Očito je $T$-ciklički potprostor $W$ invarijantan pod $T$, a za svaki vektor $\xi$ iz cikličkog potprostora $W$ vrijedi $T^r(\xi)=0$, gdje je $r$ dimenzija cikličkog potprostora.

### Nilpotentni Jordanov blok

Ako je prostor $W$ ciklički potprostor operatora $T$, onda je restrikcija ${T|}_W$ operatora $T$ na $W$ nilpotentan operator na $W$, a matrica od ${T|}_W$ u obrnuto poredanoj cikličkoj bazi $T^{r-1}(\xi_0),T^{r-2}(\xi_0),\cdots,\xi_0$ od $W$ gornjotrokutasta je matrica reda $r$ sljedećeg oblika:

$$
N_r=\begin{pmatrix}
0 & 1 & 0 & \cdots & 0 & 0\\
0 & 0 & 1 & \cdots & 0 & 0\\
0 & 0 & 0 & \cdots & 0 & 0\\
\vdots & \vdots & \vdots &   & \vdots& \vdots\\
0 & 0 & 0 & \cdots & 0 & 1\\
0 & 0 & 0 & \cdots & 0 & 0\\
\end{pmatrix}
$$

Matrica $N_r$ zove se nilpotentna Jordanova matrica reda $r$ ili nilpotentni Jordanov blok reda $r$.

Neka je $T$ nilpotentan operator na $n$-dimenzionalnom prostoru $V$. Jednoznačno određen niz prirodnih brojeva $r_1\geq\cdots\geq r_S$ koji se pojavljuje u rastavu prostora $V$ na $T$-cikličke potprostore zovemo invarijantnim eksponentima (indeksima) od $T$.

Za nilpotentnu matricu $A$ reda $n$, $A$ je slična matrici $N$ gornjeg oblika i također jednoznačno određuje niz prirodnih brojeva $r_1\geq\cdots\geq r_S$, koji zovemo invarijantnim eksponentima matrice $A$.

Iako nilpotentna matrica ne može biti slična dijagonalnoj matrici, slična je takvom standardnom obliku. Jordanova normalna forma objedinjuje dijagonalizaciju sličnošću i standardni oblik nilpotentnih matrica te daje standardni oblik koji se za opću matricu može postići transformacijom sličnosti.

### Neki teoremi

1.  Neka je $T$ nilpotentan operator na prostoru $V$, a

    $$
    h(x)=a_0+a_1x+\cdots+a_mx^m
    $$

    polinom. Tada linearni operator $h(T)$ ima inverz ako i samo ako je $a_0\neq 0$. Kad je $h(T)$ invertibilan, inverz od $h(T)$ također je polinom u $T$.

2.  Neka je $T$ nilpotentan operator na prostoru $V$, $W$ $r$-dimenzionalni $T$-ciklički potprostor, a $\xi$ vektor iz $W$. Ako postoji cijeli broj $k$ takav da je

    $$
    T^{r-k}(\xi)=0
    $$

    onda postoji vektor $\eta$ iz $W$ takav da je

    $$
    \xi=T^k(\eta)
    $$

3.  Neka je $T$ nilpotentan operator na $n$-dimenzionalnom prostoru $V$, $x^r$ minimalni polinom od $T$, a $W_1$ $r$-dimenzionalni $T$-ciklički potprostor. Tada postoji komplement $W_2$ potprostora $W_1$ takav da je:

    $$
    V=W_1\oplus W_2
    $$

    i $W_2$ je također invarijantan pod $T$.

4.  Neka je $T$ nilpotentan operator na $n$-dimenzionalnom prostoru $V$. Tada se $V$ može rastaviti na direktnu sumu $T$-cikličkih potprostora:

    $$
    V=W_1\oplus W_2\oplus\cdots\oplus W_S
    $$

5.  Svaka nilpotentna matrica reda $n$ slična je matrici oblika:

    $$
    N=\begin{pmatrix}
    N_{r_1} &   &   & 0\\
      & N_{r_2} &   &  \\
      &   & \cdots &  \\
    0 &   &   & N_{r_S}\\
    \end{pmatrix}
    $$

    gdje je svaki $N_{r_i}$ nilpotentni Jordanov blok reda $r_i$.

6.  Ako dogovorimo da se $T$-ciklički potprostori $W_i$ poredaju po dimenzijama $r_i$ silazno, $r_1\geq\cdots\geq r_S$, onda je rastav prostora $V$ na $T$-cikličke potprostore jednoznačno određen operatorom $T$.
