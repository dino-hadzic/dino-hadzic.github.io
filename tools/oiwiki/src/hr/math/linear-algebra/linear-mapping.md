---
title: Linearno preslikavanje
---

Proučavati linearna preslikavanja znači proučavati preslikavanja između linearnih (vektorskih) prostora.

Linearno preslikavanje može se prikazati u obliku matrice, pa se za mnoge pojmove iz teorije matrica može pronaći odgovarajući pojam kod linearnih preslikavanja.

## Linearno preslikavanje i linearni operator

Neka su $V$ i $W$ dva linearna prostora nad poljem $F$, a $T$ preslikavanje iz $V$ u $W$.

Ako za sve vektore $x$ i $y$ iz $W$ i sve skalare $k$ i $l$ iz polja $F$ vrijedi:

$$
T(kx+ly)=kTx+lTy
$$

kažemo da je $T$ linearno preslikavanje iz $V$ u $W$. Ako je $W=V$, kažemo da je $T$ linearni operator (linearna transformacija) na $V$.

Na primjer, identitet $T_e$ ostavlja prostor nepromijenjenim, a nul-operator $T_0$ preslikava prostor u nul-prostor.

Skup svih linearnih preslikavanja iz $V$ u $W$ označavamo $L(V,W)$. Skup svih linearnih operatora $L(V,V)$ označava se i $L(V)$.

### Svojstva

-   Linearno preslikavanje preslikava nul-vektor u nul-vektor.
-   Linearno preslikavanje čuva oblik linearnih operacija, tj. linearno preslikavanje linearne kombinacije jednako je linearnoj kombinaciji linearnih preslikavanja.
-   Linearno preslikavanje čuva linearnu zavisnost, tj. ako su vektori linearno zavisni prije preslikavanja, linearno su zavisni i nakon preslikavanja.

Linearno preslikavanje, međutim, ne čuva linearnu nezavisnost: vektori koji su linearno nezavisni prije preslikavanja ne moraju biti linearno nezavisni nakon njega.

## Matrični prikaz linearnog preslikavanja

Neka je dimenzija prostora $V$ jednaka $n$, neka je $\alpha_1,\cdots,\alpha_n$ baza od $V$, neka je dimenzija prostora $W$ jednaka $m$, neka je $\beta_1,\cdots,\beta_m$ baza od $W$ te neka je $T$ linearno preslikavanje iz $V$ u $W$.

Sliku svakog $\alpha$ pod preslikavanjem $T$ prikažemo pomoću vektora $\beta$:

$$
T\alpha_j=a_{1j}\beta_1+\cdots+a_{mj}\beta_m
$$

U matričnom zapisu:

$$
T(\alpha_1,\cdots,\alpha_n)=(T\alpha_1,\cdots,T\alpha_n)=(\beta_1,\cdots,\beta_m)A
$$

Matrica $A$ naziva se matrični prikaz (matrica) linearnog preslikavanja $T$ u tom paru baza.

## Jezgra i slika linearnog preslikavanja

Jezgra i slika ovdje se opisuju iz perspektive linearnog preslikavanja. Pomoću matričnog prikaza vidi se da se jezgra i slika linearnog preslikavanja podudaraju s jezgrom i slikom matrice.

Neka je $T$ linearno preslikavanje iz prostora $V$ u prostor $W$ i neka je:

$$
N(T)=\{x\in V|Tx=0\}
$$

$$
R(T)=Im(T)=\{y\in W|y=Tx,Vx\in V\}
$$

Lako se provjeri da je $N(T)$ potprostor od $V$, a $R(T)$ potprostor od $W$. Skupove $N(T)$ i $R(T)$ zovemo jezgrom i slikom od $V$; dimenziju od $N(T)$ zovemo **defektom** ili **nulitetom** od $T$, a dimenziju od $R(T)$ **rangom** od $T$.

Teorem: Neka je $T$ linearno preslikavanje iz prostora $V$ u prostor $W$ i neka je $V$ konačne dimenzije. Tada su $N(T)$ i $R(T)$ konačnodimenzionalni i vrijedi:

$$
\operatorname{dim} N(T)+\operatorname{dim} R(T)=\operatorname{dim} V
$$

Drugim riječima, defekt plus rang od $T$ jednak je dimenziji njegove domene $V$.

## Matrični prikaz linearnog operatora

Neka je dimenzija prostora $V$ jednaka $n$, neka je $\alpha_1,\cdots,\alpha_n$ baza od $V$ i neka je $T$ linearni operator na $V$. Tada vrijedi:

$$
T\alpha_j=a_{1j}\alpha_1+\cdots+a_{nj}\alpha_n
$$

U matričnom zapisu:

$$
T(\alpha_1,\cdots,\alpha_n)=(T\alpha_1,\cdots,T\alpha_n)=(\alpha_1,\cdots,\alpha_n)A
$$

Matrica $A$ naziva se matrični prikaz (matrica) linearnog operatora $T$ u toj bazi.

Zbog strukture prostora i linearnosti od $T$, operator $T$ potpuno je određen vektorima $T\alpha_1,\cdots,T\alpha_n$, pa $T$ jednoznačno određuje matricu $A$.

Teorem: Neka je dimenzija prostora $V$ jednaka $n$ i neka je $\alpha_1,\cdots,\alpha_n$ baza od $V$. Za proizvoljnu kvadratnu matricu $A$ reda $n$ postoji jedan i samo jedan linearni operator $T$ iz $V$ u $V$ takav da je matrica od $T$ upravo $A$.

Korolar: Između $L(V,V)$ i skupa svih kvadratnih matrica reda $n$ postoji bijekcija (obostrano jednoznačna korespondencija).

Na primjer: nul-operatoru odgovara nul-matrica, a identitetu jedinična matrica.

## Prostor linearnih operatora

Teorem: $L(V)$ također tvori linearni prostor. Uvedimo operacije u $L(V)$: za sve $T_1$ i $T_2$ iz $L(V)$, svaki $x$ iz $V$ i svaki $k$ iz polja $F$ neka je:

$$
(T_1+T_2)x=T_1x+T_2x
$$

$$
(kT_1)x=k(T_1x)
$$

Lako se provjeri da je $L(V)$ linearni prostor nad $F$, tzv. prostor linearnih operatora.

Za linearne operatore $T_1$ i $T_2$ iz $L(V)$ definiramo produkt $T_1T_2$ operatora $T_1$ i $T_2$ kao:

$$
(T_1T_2)x=T_2(T_1x)
$$

Može se provjeriti da je $(T_1T_2)$ također linearni operator iz $L(V)$ te da je produkt linearnih operatora asocijativan, ali ne i komutativan, slično produktu matrica.

Ako za linearni operator $T_1$ iz $L(V)$ postoji linearni operator $T_2$ iz $L(V)$ takav da za svaki vektor $x$ iz $V$ vrijedi:

$$
(T_1T_2)x=T_1(T_2x)=x
$$

kažemo da je $T_2$ inverzni operator od $T_1$ i pišemo:

$$
T_2=T_1^{-1}
$$

Pritom vrijedi:

$$
T_1T_2=T_2T_1=T_e
$$

Teorem: Neka je dimenzija prostora $V$ jednaka $n$, neka je $\alpha_1,\cdots,\alpha_n$ baza od $V$ te neka u toj bazi linearni operator $T_1$ ima matricu $A$, a $T_2$ matricu $B$. Tada:

-   linearni operator $T_1+T_2$ ima matricu $A+B$
-   množenje linearnog operatora skalarom $kT_1$ ima matricu $kA$
-   produkt linearnih operatora $T_1T_2$ ima matricu $AB$
-   inverzni operator od $T_1$, ako postoji, ima matricu $A^{-1}$

## Koordinate

Neka $n$ vektora $x$ tvori bazu $n$-dimenzionalnog prostora $V$. Za proizvoljan vektor $y$ iz $V$ zapišimo $y$ kao:

$$
y=a_1x_1+a_2x_2+\cdots+a_nx_n=(x_1,x_2,\cdots,x_n)\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}
$$

Vektor-stupac:

$$
\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}
$$

zovemo **koordinatama** vektora $y$ u bazi $x_1,x_2,\cdots,x_n$.

Vidimo da su koordinate vektor-stupac sastavljen od skalara iz polja; treba ih razlikovati od vektora u Abelovoj grupi.

## Formula za promjenu koordinata

Neka je dimenzija prostora $V$ jednaka $n$, neka je $T$ operator iz $L(V)$ i neka $T$ u bazi $\alpha_1,\cdots,\alpha_n$ ima matricu $A$. Neka je:

$$
\xi=(\alpha_1,\cdots,\alpha_n)\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}
$$

i neka vrijedi:

$$
T\xi=T(\alpha_1,\cdots,\alpha_n)\begin{pmatrix}y_1\\y_2\\\vdots\\y_n\end{pmatrix}
$$

Tada je:

$$
T\xi=T(\alpha_1,\cdots,\alpha_n)\begin{pmatrix}y_1\\y_2\\\vdots\\y_n\end{pmatrix}=(\alpha_1,\cdots,\alpha_n)A\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}
$$

Točke (vektori-stupci) prostora $V$ u biti su uvijek oblika „baza puta koordinate”. Točka $x$ prostora $V$, zadana vektorom-stupcem, sama koristi jediničnu matricu $I$ kao bazu, tj. $x=Ix$.

Samo kad je baza jedna i ista, tj. kad se baza ne mijenja, čisti linearni operator $T$ svodi se na množenje koordinata običnom matricom slijeva.

Linearni operator $T$ možemo zamisliti kao „filtar” kroz koji promatramo prostor $V$. Linearni operator $T$ djeluje na prostor $V$ i iskrivljuje prostor $V$. Nakon što stavimo filtar, položaj same točke se ne mijenja.

Ovaj teorem također pokazuje da je linearni operator $T$ na bazi od vektora-stupaca ekvivalentan množenju baze zdesna matricom prijelaza.

Stoga je, između različitih baza, veza među koordinatama množenje slijeva inverzom matrice prijelaza.

## Matrica prijelaza

Neka $n$ vektora $x$ i $n$ vektora $y$ tvore dvije baze prostora $V$. Za $1\leq i\leq n$ neka su koordinate svakog vektora $y_i$ u bazi $x_1,x_2,\cdots,x_n$ jednake:

$$
y_i=(x_1,x_2,\cdots,x_n)\begin{pmatrix}a_{1i}\\a_{2i}\\\vdots\\a_{ni}\end{pmatrix}
$$

Tada $n$ vektora $y$ poredamo u matricu na lijevoj strani jednakosti, a $n$ koordinatnih stupaca u matricu $A$ na desnoj strani:

$$
(y_1,y_2,\cdots,y_n)=(x_1,x_2,\cdots,x_n)A
$$

Matrica $A$ naziva se **matricom prijelaza** iz baze $x_1,x_2\cdots,x_n$ u bazu $y_1,y_2\cdots,y_n$, a također i matricom promjene baze.

Očito je matrica prijelaza invertibilna. Prema gornjoj jednakosti, matrica prijelaza iz baze $y_1,y_2\cdots,y_n$ u bazu $x_1,x_2\cdots,x_n$ jednaka je $A^{-1}$.

Vidimo da je matrica prijelaza matrica sastavljena od skalara iz polja, a ne matrica sastavljena od vektora iz Abelove grupe; to treba razlikovati.

Neka $n$ vektora $x$ i $n$ vektora $y$ tvore dvije baze prostora $V$. Za isti vektor $z$ prostora $V$ vrijedi:

$$
z=(x_1,x_2,\cdots,x_n)\begin{pmatrix}\xi_1\\\xi_2\\\vdots\\\xi_n\end{pmatrix}=(y_1,y_2\cdots,y_n)\begin{pmatrix}\eta_1\\\eta_2\\\vdots\\\eta_n\end{pmatrix}
$$

Uvrstimo gornju jednakost

$$
(y_1,y_2\cdots,y_n)=(x_1,x_2\cdots,x_n)A
$$

Zbog jedinstvenosti dobivamo:

$$
\begin{pmatrix}\xi_1\\\xi_2\\\vdots\\\xi_n\end{pmatrix}=A\begin{pmatrix}\eta_1\\\eta_2\\\vdots\\\eta_n\end{pmatrix}
$$

odnosno

$$
\begin{pmatrix}\eta_1\\\eta_2\\\vdots\\\eta_n\end{pmatrix}=A^{-1}\begin{pmatrix}\xi_1\\\xi_2\\\vdots\\\xi_n\end{pmatrix}
$$

To je transformacija isključivo među koordinatama; formule za promjenu koordinata u cijelosti su u polju skalara. Budući da smo gore napravili razliku, vektori linearnog prostora i Abelove grupe su „apstraktni vektori”, dok su koordinate i elementi matrice prijelaza u polju skalara i smatramo ih „konkretnim vektorima”; te dvije vrste vektora treba smatrati „različitim stvarima”.

Matrica može transformirati cijeli prostor, tj. sve koordinate; vektori-stupci $x$ kao koordinate ispunjavaju cijeli prostor.

Jedinična matrica $I$ sastoji se od jediničnih vektora. Matrica $A$ preslikava jediničnu matricu $I$ u stupce matrice $A$, tj. preslikava jedinične vektore u stupce matrice $A$. Zato se množenje matricom $A$ slijeva može shvatiti i kao takva transformacija prostora.

Množenje vektora matricom slijeva može se shvatiti i kao množenje koordinata skupom vektora slijeva. S koordinatnog stajališta to je:

$$
Iy=Xa
$$

Isti vektor-stupac $y$ u „običnom” prostoru, tj. prostoru koji predstavlja jedinična matrica $I$, ima koordinate $y$, a u novom, transformiranom prostoru njegove ćemo koordinate označiti $a$. Tako matrica $X$ nije samo baza u običnom prostoru nego i matrica prijelaza iz skupa vektora $I$ u skup vektora $X$.

Linearni operator $T$ preslikava jednu bazu u drugu bazu, pa se i koordinate preslikavaju u druge koordinate.

Ako je matrica prijelaza linearnog operatora $T$ koji preslikava bazu $\alpha$ u $\beta$ jednaka $A$, za odgovarajuće matrice baza vrijedi $\beta=\alpha A$.

Stoga je odnos koordinata upravo obrnut. Pretpostavimo da su koordinate nakon primjene linearnog operatora $T$ jednake $b$, tj. kroz filtar vidimo koordinate $b$; tada je prikaz točke u $V$ jednak $\beta b$. Vraćamo se pomoću matrice prijelaza i prikaz točke u $V$ zapišemo kao $\alpha Ab$. Sada je jasno gledište prema kojem je promjena koordinata množenje slijeva inverzom matrice prijelaza.

## Linearni operatori i sličnost matrica

Odnos linearnog operatora $T$ na prostoru $V$ prema bazi $\alpha$ prostora $V$:

Linearni operator $T$ djeluje na bazu $\alpha$ i preslikava bazu $\alpha$ u $T(\alpha)$, što odgovara množenju baze $\alpha$ zdesna matricom $A$, tj. $T(\alpha)=\alpha A$.

Sličnost matrica bavi se sljedećim pitanjem: isti linearni operator $T$ u prostoru $V$ s bazom $\beta$ opisan je matricom $B$, a u prostoru $V$ s bazom $\alpha$ matricom $A$.

Ako je matrica prijelaza $C$, tj. $\beta=\alpha C$, kakva je veza između dvaju opisa $B$ i $A$?

Budući da je riječ o istom operatoru $T$, uočavamo činjenicu da odnos preko matrice prijelaza vrijedi i prije i poslije primjene operatora, tj.:

$$
T(\beta)=T(\alpha)C=\alpha AC
$$

Linearni operator $T$ iz perspektive baze $\beta$ i dalje je množenje zdesna; baza $\beta$ prelazi u bazu $\alpha$ množenjem zdesna matricom $C$, a odnos preko matrice prijelaza $C$ ostaje očuvan prije i poslije primjene operatora:

$$
T(\beta)=\beta B=\alpha CB
$$

Time je problem riješen:

$$
B=C^{-1}AC
$$

Teorem: Neka je $T$ operator iz $L(V)$. Tada su matrice od $T$ u različitim bazama **slične**.

Za kvadratne matrice $A$ i $B$, ako postoji invertibilna matrica $C$ takva da je $B=C^{-1}AC$, kažemo da su $A$ i $B$ slične.

Sličnost matrica čuva rang, pa iz sličnosti matrica slijedi ekvivalentnost matrica. Međutim, dvije ekvivalentne matrice ne moraju biti slične.

Budući da je sličnost matrica usko vezana uz njihov oblik, sličnost matrica nema veze s ekvivalentnošću skupova vektora ni s jednakošću skupova rješenja sustava jednadžbi.

Vratimo se na početak: objašnjenje sličnosti matrica svodi se na 4 jednakosti: $\beta=\alpha C$, $T(\alpha)=\alpha A$, $T(\beta)=\beta B$, $T(\beta)=T(\alpha)C$.

## Literatura

-   [【官方双语/合集】线性代数的本质 - 系列合集 P13 09 - 基变换](https://www.bilibili.com/video/BV1Ls411b7r2) (Essence of Linear Algebra, službena dvojezična zbirka, 13. dio: „Promjena baze”)
