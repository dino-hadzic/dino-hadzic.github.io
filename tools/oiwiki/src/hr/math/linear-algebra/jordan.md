---
title: Jordanova normalna forma
---

## Jordanova dekompozicija

Neka je $T$ linearni operator na $n$-dimenzionalnom prostoru $V$. Ako je minimalni polinom operatora $T$

$$
m_A(\lambda)={(\lambda-\lambda_1)}^{r_1}{(\lambda-\lambda_2)}^{r_2}\cdots{(\lambda-\lambda_k)}^{r_k}
$$

tada se prema primarnoj dekompoziciji prostor $V$ može rastaviti na direktnu sumu potprostora:

$$
V=V_1\oplus V_2\oplus\cdots\oplus V_k
$$

gdje je $V_i=N\left({(A-\lambda_i I)}^{r_i}\right)$, pri čemu je $A$ matrica koja odgovara operatoru $T$; svi su ti potprostori invarijantni s obzirom na $T$.

Neka je operator $T_i$ projekcija prostora $V$ na potprostor $V_i$, tj. konstruiramo polinome $u_i(T)$ takve da vrijedi:

-   $$
    T_i=u_i(T)\frac{m_A(T)}{{(T-\lambda_i T_e)}^{r_i}}
    $$
-   $$
    T_1+T_2+\cdots+T_k=T_e
    $$

gdje $T_e$ označava identični operator na prostoru $V$. Tada vrijede svojstva:

-   Restrikcija operatora $T_i$ na prostor $V_i$, ${T_i|}_{V_i}$, identični je operator prostora $V_i$.
-   Ako je $i$ različit od $j$, restrikcija operatora $T_i$ na prostor $V_j$, ${T_i|}_{V_j}$, nul-operator je prostora $V_j$.

Dakle, operator $T_i$ svaki vektor $\xi$ prostora $V$ preslikava u njegovu komponentu $\xi_i$ u prostoru $V_i$.

Konstruiramo operator:

$$
T_D=\lambda_1 T_1+\lambda_2 T_2+\cdots+\lambda_k T_k
$$

Budući da je svaki operator $T_i$ polinom u operatoru $T$, i operator $T_D$ je polinom u operatoru $T$, pa je svaki potprostor $V_i$ invarijantan s obzirom na operator $T_D$.

Iz gornjih jednakosti slijedi da je restrikcija operatora $T_D$ na potprostor $V_i$, ${T_D|}_{V_i}$, homotetija potprostora $V_i$ s koeficijentom $\lambda_i$. Stoga se operator $T_D$ može dijagonalizirati.

Konstruiramo:

$$
T_N=T-T_D
$$

Tada je i operator $T_N$ polinom u operatoru $T$, pa je svaki potprostor $V_i$ invarijantan s obzirom na operator $T_N$. Za proizvoljni vektor $\xi_i$ potprostora $V_i$ vrijedi:

$$
{T_N}^{r_i}(\xi_i)={T-T_D}^{r_i}(\xi_i)={T-\lambda_i T_i}^{r_i}(\xi_i)=0
$$

Neka je $r$ maksimum svih $r_i$; tada za proizvoljni vektor $\xi$ prostora $V$ $r$-ta potencija operatora $T_N$ preslikava vektor $\xi$ u nul-vektor. Stoga je operator $T_N$ nilpotentan operator.

Tako se svaki operator $T$ na prostoru $V$ može zapisati kao:

$$
T=T_D+T_N
$$

gdje se $T_D$ može dijagonalizirati, a $T_N$ je nilpotentan operator. Budući da su $T_D$ i $T_N$ polinomi u operatoru $T$, njihov je produkt komutativan:

$$
T_DT_N=T_NT_D
$$

Teorem: Neka su $T_1$ i $T_2$ dva dijagonalizabilna operatora na prostoru $V$ i neka je $T_1T_2=T_2T_1$. Tada postoji baza u kojoj su matrice operatora $T_1$ i $T_2$ s obzirom na tu istu bazu dijagonalnog oblika.

Teorem: Neka je $T$ linearni operator na $n$-dimenzionalnom prostoru $V$. Tada postoje dijagonalizabilan operator $T_D$ i nilpotentan operator $T_N$ takvi da vrijedi:

-   $$
    T=T_D+T_N
    $$
-   $$
    T_DT_N=T_NT_D
    $$

Oba su polinomi u operatoru $T$ i jednoznačno su određeni operatorom $T$.

Taj teorem daje rastav operatora $T$ koji se naziva Jordanova dekompozicija operatora $T$; $T_D$ se naziva dijagonalizabilni dio operatora $T$, a $T_N$ nilpotentni dio operatora $T$.

Analogno postoji Jordanova dekompozicija matrice:

Teorem: Neka je $A$ matrica reda $n$. Tada postoje dijagonalizabilna matrica $D$ i nilpotentna matrica $N$ takve da vrijedi:

-   $$
    A=D+N
    $$
-   $$
    DN=ND
    $$

Obje su polinomi u matrici $A$ i jednoznačno su određene matricom $A$.

Taj teorem daje rastav matrice $A$ koji se naziva Jordanova dekompozicija matrice $A$; $D$ se naziva dijagonalizabilni dio matrice $A$, a $N$ nilpotentni dio matrice $A$.

## Lambda-matrice

Dio koji sada uvodimo odnosi se na općenitije matrice koje sadrže varijabilni parametar $\lambda$, a ne samo tablice brojeva. Ovo je razmatranje nešto šire od razmatranja matrica sastavljenih isključivo od brojeva.

Za $\lambda$-matrice polje koje odgovara pripadnom prostoru postaje polje racionalnih funkcija u jednoj varijabli $\lambda$.

Matrica čiji su elementi polinomi u $\lambda$ naziva se $\lambda$-matrica i označava se $A(\lambda)$.

Budući da polje polinoma sadrži brojevno polje, brojevne su matrice poseban slučaj $\lambda$-matrica; karakteristična matrica $\lambda I-A$ brojevne matrice $A$ jedna je vrsta $\lambda$-matrice.

### Elementarne transformacije lambda-matrica

Za $\lambda$-matrice također se mogu definirati zbrajanje i oduzimanje, množenje, elementarne transformacije i rang. Za kvadratne $\lambda$-matrice također se mogu definirati determinanta, minori i algebarski komplementi.

Za $\lambda$-matrice elementarne transformacije uglavnom su iste kao za brojevne matrice; samo se transformacija dodavanja višekratnika mijenja u (ovdje na primjeru transformacija redaka):

-   Pomnoži neki redak polinomom $\varphi(\lambda)$ u $\lambda$ i dodaj ga drugom retku.

Uočimo da se transformacija množenja ne mijenja. To je zato što transformacija dodavanja višekratnika ne mijenja determinantu, dok je transformacija množenja mijenja. Da bi se očuvala svojstva ranga nad poljem polinoma, determinanta se smije mijenjati samo unutar brojevnog polja.

Pripadne elementarne matrice mijenjaju se na odgovarajući način.

Lako se vidi da su determinante svih triju vrsta elementarnih matrica konstante različite od nule, pa su sve one punog ranga. Stoga množenje njima slijeva ili zdesna ne mijenja rang $\lambda$-matrice.

Ako se $A(\lambda)$ konačnim brojem elementarnih transformacija može prevesti u $B(\lambda)$, kažemo da su $A(\lambda)$ i $B(\lambda)$ ekvivalentne.

Ako su $\lambda$-matrice ekvivalentne, imaju isti rang. Obrat ne vrijedi, po čemu se razlikuju od brojevnih matrica.

## Smithova normalna forma

Teorem: Neka je rang $\lambda$-matrice jednak $r$. Tada je $A(\lambda)$ sigurno ekvivalentna matrici:

$$
\begin{pmatrix}
D(\lambda) & 0\\
0 & 0\\
\end{pmatrix}
$$

gdje je:

$$
D(\lambda)=\begin{pmatrix}
d_1(\lambda) &  & \\
 & \ddots & \\
 &  & d_r(\lambda)\\
\end{pmatrix}
$$

Svaki $d_i(\lambda)$ normirani je polinom (s vodećim koeficijentom $1$), a svaka dva susjedna polinoma u odnosu su djeljivosti $d_i(\lambda)|d_{i+1}(\lambda)$.

Ta se normalna forma naziva Smithova normalna forma, a $d_i(\lambda)$ nazivaju se invarijantni faktori.

Konkretan postupak za nalaženje Smithove normalne forme jest eliminacija od gornjeg lijevog kuta prema donjem desnom: u svakom je koraku element u gornjem lijevom kutu najveći zajednički djelitelj svih preostalih polinoma dolje desno, a pomoću elementa u gornjem lijevom kutu cijeli se taj redak i stupac eliminiraju u $0$.

Teorem: Uvjet da su $A(\lambda)$ i $B(\lambda)$ ekvivalentne ekvivalentan je uvjetu da $A(\lambda)$ i $B(\lambda)$ imaju potpuno iste invarijantne faktore.

### Elementarni djelitelji

Prema osnovnom teoremu algebre, neka je rastav invarijantnih faktora $d_1(\lambda),d_2(\lambda),\cdots,d_m(\lambda)$ matrice $A(\lambda)$:

$$
d_i(\lambda)={(\lambda-\lambda_1)}^{e_{i1}}{(\lambda-\lambda_2)}^{e_{i2}}\cdots{(\lambda-\lambda_S)}^{e_{iS}}
$$

gdje su $\lambda_1,\cdots,\lambda_S$ međusobno različiti. Budući da je:

$$
d_i(\lambda)|d_{i+1}(\lambda)
$$

eksponenti $e_{1j},e_{2j},\cdots,e_{mj}$ su rastući, a svi eksponenti posljednjeg člana $d_m(\lambda)$ različiti su od nule.

Svi faktori u gornjem izrazu s eksponentom većim od nule zajednički se nazivaju elementarni djelitelji matrice $A(\lambda)$.

Uočimo da se elementarni djelitelji broje s kratnošću. Ako se za neki $j$ eksponent $e_{ij}$ pojavljuje više puta, i pripadni elementarni djelitelj ${(\lambda-\lambda_j)}^{e_{ij}}$ mora se pojaviti odgovarajući broj puta.

Prethodni teorem kaže da je ekvivalentnost matrica $A(\lambda)$ i $B(\lambda)$ ekvivalentna tome da imaju potpuno iste invarijantne faktore. Ako su invarijantni faktori potpuno isti, naravno da su i elementarni djelitelji potpuno isti, ali obrat ne vrijedi. Zapravo vrijedi sljedeći rezultat:

Teorem: Da $A(\lambda)$ i $B(\lambda)$ imaju potpuno iste invarijantne faktore ekvivalentno je tome da imaju potpuno iste elementarne djelitelje i isti rang.

Stoga „potpuno isti elementarni djelitelji i isti rang” također postaje kriterij za ekvivalentnost $\lambda$-matrica.

Pri elementarnim transformacijama možemo također najprije $A(\lambda)$ prevesti u dijagonalnu matricu, zatim odrediti elementarne djelitelje i rang, a potom invarijantne faktore i tako dobiti normalnu formu. Vrijedi rezultat:

Teorem: Neka je $A(\lambda)$ ekvivalentna dijagonalnoj matrici:

$$
\operatorname{diag}\{f_1(\lambda),f_2(\lambda),\cdots,f_r(\lambda),0,\cdots,0\}
$$

Tada potencije svih linearnih faktora ${(\lambda-\lambda_j)}^{e_{ij}}$ polinoma $f_1(\lambda),f_2(\lambda),\cdots,f_r(\lambda)$ čine elementarne djelitelje matrice $A(\lambda)$.

Konkretan postupak konstrukcije invarijantnih faktora iz elementarnih djelitelja i ranga jest sljedeći: najprije elementarne djelitelje razvrstamo prema faktorima i složimo u tablicu; istovrsne faktore poredamo po padajućim potencijama u isti redak, a najviše potencije svih vrsta faktora stavimo u isti stupac; broj stupaca dopunimo jedinicama $1$ do ranga $r$; tada produkt svakog stupca čini jedan invarijantni faktor.

### Primjena na karakteristične matrice

Ako su $A$ i $B$ brojevne matrice, njihove su karakteristične matrice $\lambda$-matrice. Vrijedi rezultat:

Teorem: Uvjet da su brojevne matrice $A$ i $B$ slične ekvivalentan je uvjetu da su karakteristične matrice $\lambda I-A$ i $\lambda I-B$ ekvivalentne.

Budući da karakteristična matrica $\lambda I-A$ sadrži $n$ varijabli $\lambda$ samo na glavnoj dijagonali, njezin je rang $n$. Prema gornjem zaključivanju rangovi karakterističnih matrica brojevnih matrica istog tipa uvijek su jednaki, pa vrijedi ekvivalencija:

Brojevne matrice $A$ i $B$ slične su ako i samo ako karakteristične matrice $\lambda I-A$ i $\lambda I-B$ imaju potpuno iste elementarne djelitelje.

Za karakterističnu matricu $\lambda I-A$ elementarne transformacije čuvaju ekvivalentnost, pa ne mijenjaju rang.

Promotrimo li tri vrste elementarnih transformacija, budući da jedina izmijenjena transformacija, dodavanje višekratnika, ne mijenja determinantu, sve tri vrste elementarnih transformacija zapravo mijenjaju polinom koji je rezultat determinante samo za konstantni faktor, pa ne mijenjaju faktorizaciju ni stupanj polinoma koji je rezultat determinante.

Stoga je determinanta karakteristične matrice $\lambda I-A$ polinom stupnja $n$; nakon što se elementarnim transformacijama prevede u Smithovu normalnu formu, budući da je rang $n$, determinanta je upravo produkt svih invarijantnih faktora na glavnoj dijagonali, a jednaka je i produktu svih elementarnih djelitelja. Stoga je zbroj stupnjeva svih elementarnih djelitelja karakteristične matrice $\lambda I-A$ jednak $n$.

## Jordanova normalna forma

Matrica

$$
\begin{pmatrix}
\lambda & 1 & 0 & \cdots & 0 & 0\\
0 & \lambda & 1 & \cdots & 0 & 0\\
0 & 0 & \lambda & \cdots & 0 & 0\\
\vdots & \vdots & \vdots &  & \vdots & \vdots\\
0 & 0 & 0 & \cdots & \lambda & 1\\
0 & 0 & 0 & \cdots & 0 & \lambda\\
\end{pmatrix}
$$

čiji su svi elementi na glavnoj dijagonali $\lambda$, svi elementi neposredno iznad glavne dijagonale $1$, a svi ostali $0$, naziva se Jordanova matrica koja pripada $\lambda$, ili Jordanov blok.

Očito je nilpotentna Jordanova matrica poseban slučaj Jordanove matrice, naime slučaj kad je $\lambda$ jednak $0$.

Teorem: Neka je $T$ operator na $n$-dimenzionalnom prostoru $V$ i neka su $\lambda_1,\cdots,\lambda_k$ sve međusobno različite svojstvene vrijednosti operatora $T$. Tada postoji baza takva da matrica operatora $T$ s obzirom na tu bazu ima oblik:

$$
\begin{pmatrix}
B_1 &  &  & 0\\
 & B_2 &  & \\
 &  & \ddots & \\
0 &  &  & B_k\\
\end{pmatrix}
$$

gdje je

$$
B_i=\begin{pmatrix}
J_{i1} &  &  & 0\\
 & J_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & J_{is_i}\\
\end{pmatrix}
$$

pri čemu su $J_{i1},\cdots,J_{is_i}$ Jordanovi blokovi koji pripadaju $\lambda_i$.

Naime, najprije prema minimalnom polinomu:

$$
m_A(\lambda)={(\lambda-\lambda_1)}^{r_1}{(\lambda-\lambda_2)}^{r_2}\cdots{(\lambda-\lambda_k)}^{r_k}
$$

imamo primarnu dekompoziciju:

$$
V=V_1\oplus V_2\oplus\cdots\oplus V_k
$$

gdje je:

$$
V_i=N\left({(A-\lambda_i I)}^{r_i}\right)
$$

pri čemu je $A$ matrica koja odgovara operatoru $T$.

Neka je operator $S_i$ restrikcija ${T|}_{V_i}$ operatora $T$ na $V_i$; sada pokušavamo za svaki $S_i$ provesti Jordanovu dekompoziciju.

Označimo s $T_e$ identični operator na $V$. Za razliku od Jordanove dekompozicije iz prethodnog teksta, označimo s $T_i$ nilpotentni dio Jordanove dekompozicije operatora $S_i$:

$$
S_i=\lambda_i T_e+T_i
$$

Tada je $T_i$ nilpotentan operator potprostora $V_i$, a zapravo je i restrikcija ${(T-\lambda_i T_e)|}_{V_i}$ operatora $T-\lambda_i T_e$ na $V_i$.

Potprostor $V_i$ može se rastaviti na direktnu sumu cikličkih potprostora nilpotentnog operatora $T_i$:

$$
V_i=W_{i1}\oplus W_{i2}\oplus\cdots\oplus W_{is_i}
$$

U svakom cikličkom potprostoru $W_{ij}$ uzmemo cikličku bazu i poredamo je obrnutim redoslijedom; tako sastavimo bazu prostora $V_i$, pa matrica operatora $T_i$ s obzirom na tu bazu ima oblik:

$$
N_i=\begin{pmatrix}
N_{i1} &  &  & 0\\
 & N_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & N_{is_i}\\
\end{pmatrix}
$$

Svi $N_{ij}$ su nilpotentni Jordanovi blokovi. Tada je za gore odabranu bazu prostora $V_i$ matrica koja odgovara operatoru $S_i$:

$$
B_i=\begin{pmatrix}
\lambda_i &  &  & 0\\
 & \lambda_i &  & \\
 &  & \ddots & \\
0 &  &  & \lambda_i\\
\end{pmatrix}+\begin{pmatrix}
N_{i1} &  &  & 0\\
 & N_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & N_{is_i}\\
\end{pmatrix}=\begin{pmatrix}
J_{i1} &  &  & 0\\
 & J_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & J_{is_i}\\
\end{pmatrix}
$$

Ovdje su $J_{i1},J_{i2},\cdots,J_{is_i}$ Jordanovi blokovi koji pripadaju $\lambda_i$.

Za svaki potprostor $V_i$ na opisani način odaberemo bazu i od njih sastavimo bazu prostora $V$; tada matrica operatora $T$ s obzirom na tu bazu ima upravo oblik koji propisuje teorem.

Matrica reda $n$ oblika:

$$
\begin{pmatrix}
J_1 &  &  & 0\\
 & J_2 &  & \\
 &  & \ddots & \\
0 &  &  & J_m\\
\end{pmatrix}
$$

u kojoj je svaki $J_i$ Jordanov blok, naziva se Jordanova normalna forma.

Teorem: Svaka matrica $A$ reda $n$ slična je nekoj Jordanovoj normalnoj formi. Osim do na redoslijed Jordanovih blokova, Jordanova normalna forma slična matrici $A$ jednoznačno je određena matricom $A$.

Uočimo da je u gore konstruiranoj matrici $B_i$ prvi član višekratnik jedinične matrice, pa naravno komutira s drugim članom. Stoga je prvi član upravo dijagonalizabilni dio Jordanove dekompozicije matrice $B_i$, a drugi član nilpotentni dio Jordanove dekompozicije matrice $B_i$.

U Jordanovoj normalnoj formi koja odgovara nekoj matrici dijagonalna matrica sastavljena od elemenata na glavnoj dijagonali dijagonalizabilni je dio te Jordanove normalne forme, a zamjenom elemenata na glavnoj dijagonali nulama $0$ dobiva se nilpotentni dio te Jordanove normalne forme.

Teorem: U Jordanovoj normalnoj formi matrice $A$ svaki Jordanov blok:

$$
J_i=\begin{pmatrix}
\lambda_i & 1 &  &  & \\
 & \lambda_i & 1 &  & \\
 &  & \ddots & \ddots & \\
 &  &  & \ddots & 1\\
 &  &  &  & \lambda_i\\
\end{pmatrix}
$$

odgovara jednom elementarnom djelitelju ${(\lambda-\lambda_i)}^{n_i}$ karakteristične matrice $\lambda I-A$; svi elementarni djelitelji karakteristične matrice $\lambda I-A$ odgovaraju svim Jordanovim blokovima u Jordanovoj normalnoj formi matrice $A$.

Naime, matrica $A$ slična je svojoj Jordanovoj normalnoj formi, pa su i njihove karakteristične matrice ekvivalentne; to se vidi prevođenjem karakteristične matrice Jordanove normalne forme u Smithovu normalnu formu.

Prema tom teoremu, pomoću elementarnih djelitelja karakteristične matrice $\lambda I-A$ može se zapisati Jordanova normalna forma matrice $A$.

Jedna je posljedica da je matrica $A$ dijagonalizabilna ako i samo ako su svi elementarni djelitelji karakteristične matrice $\lambda I-A$ linearni (prvog stupnja).

## Frobeniusov teorem

Gore je pokazano da je rang Smithove normalne forme karakteristične matrice reda $n$ jednak $n$.

Teorem: Neka je Smithova normalna forma karakteristične matrice $\lambda I-A$ matrice $A$:

$$
\operatorname{diag}\{d_1(\lambda),d_2(\lambda),\cdots,d_n(\lambda)\}
$$

Tada je posljednji invarijantni faktor $d_n(\lambda)$ upravo minimalni polinom $m_A(\lambda)$ matrice $A$.

Korolar: Ekvivalentni uvjeti za dijagonalizabilnost matrice $A$ jesu:

-   Minimalni polinom $m_A(\lambda)$ nema višestrukih korijena.
-   Invarijantni faktori karakteristične matrice $\lambda I-A$ nemaju višestrukih korijena.
-   Svi elementarni djelitelji karakteristične matrice $\lambda I-A$ linearni su (prvog stupnja).
