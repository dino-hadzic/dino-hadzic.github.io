---
title: Simpleks metoda
---

Preduvjeti: [Osnove linearnog programiranja](./linear-programming.md)

## Uvod

U algoritamskim natjecanjima simpleks metoda (simplex method) često se koristi za rješavanje problema linearnog programiranja. Međutim, budući da problemi linearnog programiranja na koje se nailazi u natjecanjima uglavnom imaju posebniju strukturu i često se mogu svesti na probleme mrežnih tokova, simpleks metoda nije u čestoj upotrebi, a ni po učinkovitosti se ne može mjeriti s algoritmima posebno osmišljenima za probleme mrežnih tokova.

## Osnovni pojmovi

Pretpostavimo da treba riješiti sljedeći problem linearnog programiranja u [standardnom obliku](./linear-programming.md#标准形式) s $n$ varijabli odlučivanja i $m+n$ ograničenja:

$$
\begin{aligned}
\min_{x}\; & z = c^Tx \\
\text{subject to }& Ax = b, \\
& x \ge 0.
\end{aligned}
$$

Bez smanjenja općenitosti pretpostavimo da sustav linearnih jednadžbi određen tih $m$ ograničenja jednakosti ima rješenje i da je $A$ punog ranga, pa je $\operatorname{rank}A = m \le n$.

### Primjer

Prije strogog opisa koraka simpleks metode, u ovom odjeljku najprije promatramo konkretan primjer radi lakšeg razumijevanja.

???+ example "Primjer"
    Promotrimo problem linearnog programiranja
    
    $$
    \begin{aligned}
    \max\; & 10 x_1 + 12 x_2 + 12 x_3 \\
    \text{subject to } & x_1 + 2 x_2 + 2x_3 \le 20, \\
    & 2x_1 + x_2 + 2x_3 \le 20, \\
    & 2x_1 + 2x_2 + x_3 \le 20,\\
    & x_1,x_2,x_3 \ge 0.
    \end{aligned}
    $$
    
    Dodavanjem dopunskih varijabli dobivamo njegov standardni oblik:
    
    $$
    \begin{aligned}
    \min\; & -10 x_1 - 12 x_2 - 12 x_3 \\
    \text{subject to } & x_1 + 2 x_2 + 2x_3 + x_4 = 20, \\
    & 2x_1 + x_2 + 2x_3 + x_5 = 20, \\
    & 2x_1 + 2x_2 + x_3 + x_6 = 20,\\
    & x_1,x_2,x_3,x_4,x_5,x_6 \ge 0.
    \end{aligned}
    $$
    
    Promotrimo ograničenja jednakosti ovog problema: ona zapravo izražavaju varijable $x_4,x_5,x_6$ pomoću varijabli $x_1,x_2,x_3$. Nakon malog preuređivanja polaznog problema dobivamo
    
    $$
    \begin{array}{rrrrrr}
    \min_{x_i\ge 0}  &  z  = &  0 &  -10x_1 &  -12x_2 &  -12x_3\;\\
    \text{subject to}& x_4 = & 20 &    -x_1 &   -2x_2 &   -2x_3, \\
                & x_5 = & 20 &   -2x_1 &    -x_2 &   -2x_3, \\
                & x_6 = & 20 &   -2x_1 &   -2x_2 &    -x_3. \\
    \end{array}
    $$
    
    Iz ovog se oblika jasno vidi da, stavimo li $x_1=x_2=x_3=0$, dobivamo jedno dopustivo rješenje polaznog problema
    
    $$
    x = (0,0,0,20,20,20)^T.
    $$
    
    Njemu pripada vrijednost $z=0$. Radi jednostavnijeg izražavanja, varijable $x_1,x_2,x_3$ koje smo postavili na nulu zovemo nebaznim varijablama, a preostale varijable $x_4,x_5,x_6$ baznim varijablama.
    
    Ovo dopustivo rješenje očito nije optimalno. Dovoljno je prikladno povećati vrijednosti $x_1,x_2,x_3$ tako da $x_4,x_5,x_6$ i dalje budu nenegativni, pa će rješenje ostati dopustivo. Štoviše, budući da su u ciljnoj funkciji koeficijenti uz $x_1,x_2,x_3$ strogo negativni, povećanje njihovih vrijednosti sigurno će smanjiti vrijednost ciljne funkcije. Možemo, primjerice, odabrati povećanje vrijednosti $x_1$. Da bismo vrijednost ciljne funkcije smanjili što je više moguće, vrijednost $x_1$ treba povećati što je više moguće. No da bi rješenje ostalo dopustivo, mora vrijediti $x_4,x_5,x_6\ge 0$. Stoga se $x_1$ može povećati najviše do
    
    $$
    \min\left\{\dfrac{20}{1},\dfrac{20}{2},\dfrac{20}{2}\right\} = 10.
    $$
    
    Dopustivo rješenje tada postaje
    
    $$
    x = (10,0,0,10,0,0)^T.
    $$
    
    Budući da je $x_1$ postao bazna varijabla, da bismo se vratili u početnu situaciju (tj. tri bazne varijable izražene pomoću tri nebazne), treba odabrati novu nebaznu varijablu. Kako su $x_5,x_6$ obje jednake nuli, bilo koju od njih možemo odabrati za nebaznu varijablu i postaviti na nulu. Odaberimo $x_5$ za nebaznu varijablu. Uvrstimo li
    
    $$
    x_1 = 10 - 0.5x_5 - 0.5x_2 - x_3
    $$
    
    u polazni problem, možemo ga prepisati kao
    
    $$
    \begin{array}{rrrrrr}
    \min_{x_i\ge 0}  &   z = &-100&   +5x_5 &   -7x_2 &   -2x_3\;\\
    \text{subject to}& x_4 = & 10 & +0.5x_5 & -1.5x_2 &    -x_3, \\
                & x_1 = & 10 & -0.5x_5 & -0.5x_2 &    -x_3, \\
                & x_6 = &  0 &    +x_5 &    -x_2 &    +x_3. \\
    \end{array}
    $$
    
    Time smo se vratili u početnu situaciju.
    
    Promotrimo dalje trenutačnu ciljnu funkciju. Koeficijent uz nebaznu varijablu $x_3$ još je uvijek negativan. Možemo razmotriti povećanje vrijednosti $x_3$. Da bi vrijedilo $x_4,x_1,x_6\ge 0$, varijabla $x_3$ može se povećati najviše do
    
    $$
    \min\left\{\dfrac{10}{1},\dfrac{10}{1}\right\} = 10.
    $$
    
    Primijetimo da je u izrazu za $x_6$ koeficijent uz $x_3$ pozitivan, pa koliko god povećavali $x_3$, $x_6$ neće postati negativan. Zato su u vitičastim zagradama ovaj put samo dva člana. Kad $x_3$ poraste do $10$, $x_1,x_4$ obje postaju nula, pa bilo koju od njih možemo odabrati za novu nebaznu varijablu. Odaberimo $x_4$. Uvrštavanjem
    
    $$
    x_3 = 10 + 0.5x_5 - 1.5x_2 - x_4
    $$
    
    u gornji problem, problem se pretvara u
    
    $$
    \begin{array}{rrrrrr}
    \min_{x_i\ge 0}  &   z = &-120&   +4x_5 &   -4x_2 &   +2x_4\;\\
    \text{subject to}& x_3 = & 10 & +0.5x_5 & -1.5x_2 &    -x_4, \\
                & x_1 = &  0 &    -x_5 &    +x_2 &    +x_4, \\
                & x_6 = & 10 & +1.5x_5 & -2.5x_2 &    -x_4. \\
    \end{array}
    $$
    
    Dovoljno je uvrstiti $x_5=x_2=x_4=0$ pa iz ovog oblika očitati da je trenutačno dopustivo rješenje
    
    $$
    x = (0,0,10,0,0,10)^T,
    $$
    
    a pripadna vrijednost $z=-120$.
    
    Ponavljamo prethodni postupak. Koeficijent uz $x_2$ je negativan, pa mu vrijednost možemo povećati; ali da bi $x_3,x_6$ ostali nenegativni, možemo ga povećati samo do
    
    $$
    \min\left\{\dfrac{10}{1.5},\dfrac{10}{2.5}\right\} = 4.
    $$
    
    Budući da se minimum u vitičastim zagradama postiže u izrazu za varijablu $x_6$, ona će postati nula kada $x_2=4$. Uvrštavanjem izraza
    
    $$
    x_2 = 4 + 0.6x_5 - 0.4x_6 - 0.4x_4
    $$
    
    u gornji problem, polazni problem možemo prepisati kao
    
    $$
    \begin{array}{rrrrrr}
    \min_{x_i\ge 0}  &   z = &-136& +1.6x_5 & +1.6x_6 & +3.6x_4\;\\
    \text{subject to}& x_3 = &  4 & -0.4x_5 & +0.6x_6 & -0.4x_4, \\
                & x_1 = &  4 & -0.4x_5 & -0.4x_6 & +0.6x_4, \\
                & x_2 = &  4 & +0.6x_5 & -0.4x_6 & -0.4x_4. \\
    \end{array}
    $$
    
    Stavimo li opet nebazne varijable $x_5,x_6,x_4$ na nulu, dobivamo trenutačno dopustivo rješenje
    
    $$
    x = (4,4,4,0,0,0)^T.
    $$
    
    Pripadna vrijednost je $z=-136$.
    
    Budući da su u ciljnoj funkciji koeficijenti uz sve nebazne varijable pozitivni, gore opisani postupak poboljšavanja ciljne funkcije ne može se nastaviti, pa je trenutačno dopustivo rješenje optimalno. Algoritam završava.

U ovom primjeru algoritam polazi od jednog dopustivog rješenja i neprestano poboljšava ciljnu funkciju sve dok daljnje poboljšanje nije moguće. To je osnovna ideja simpleks metode.

### Bazno dopustivo rješenje

Budući da je $A$ punog ranga, uvijek možemo odabrati podskup $B\subseteq\{1,2,\cdots,n\}$ veličine $m$ takav da je $A_B$ regularna kvadratna matrica. Tako $x_B$ možemo izraziti pomoću preostalih varijabli $x_N$:

$$
x_B = A_B^{-1}b - A_B^{-1}A_Nx_N.
$$

Ovdje je $N=\{1,2,\cdots,n\}\setminus B$, matrice $A_B,A_N$ su podmatrice matrice $A$ sastavljene od stupaca s indeksima $i\in B$ odnosno $i\in N$, a vektori $x_B,x_N$ su podvektori vektora $x$ sastavljeni od komponenata s indeksima $i\in B$ odnosno $i\in N$. Ako je $i\in B$, varijablu $x_i$ zovemo **baznom varijablom** (basic variable); inače $x_i$ zovemo **nebaznom varijablom** (non-basic variable). Skup svih baznih varijabli zove se **baza** (basis); u ovom članku bazu označavamo pripadnim skupom indeksa $B$.

???+ tip "„Baza”"
    Naziv „baza” može se razumjeti iz perspektive linearne algebre. Neka je $V$ linearni prostor razapet svim stupcima matrice $A$. Tada stupci koji odgovaraju bazi $B$ čine bazu prostora $V$.

Stavimo li u izrazu za bazne varijable $x_B$ da je $x_N=0$, dobivamo jedno rješenje svih ograničenja jednakosti[^notation]

$$
x = (x_B,x_N) = (A_B^{-1}b,0).
$$

Tako dobiveno rješenje zove se **bazno rješenje** (basic solution) problema linearnog programiranja. Ako ono k tomu zadovoljava i sva ograničenja nenegativnosti, tj. $x \ge 0$, onda je ono i dopustivo rješenje polaznog problema i zove se **bazno dopustivo rješenje** (basic feasible solution, BFS). Tijekom iteracija simpleks metode trenutačno rješenje mora cijelo vrijeme biti bazno dopustivo rješenje.

### Pivotiranje

Svaka iteracija simpleks metode zove se **pivotiranje** (pivoting). Gledano po rezultatu, svako pivotiranje uklanja jednu staru baznu varijablu i dodaje jednu novu, čime poboljšava vrijednost ciljne funkcije.

???+ tip "„Pivotiranje”"
    I naziv „pivotiranje” (doslovno „okretanje osi”) može se razumjeti iz perspektive linearne algebre. Kao što je gore rečeno, stupci koji odgovaraju bazi $B$ čine bazu prostora $V$, pa oni odgovaraju i koordinatnim osima prostora $V$ u prikazu u toj bazi. Stoga je pivotiranje postupak kojim se jedna koordinatna os zakreće u novi položaj.

Da bismo odredili baznu varijablu koju treba dodati, ciljnu funkciju možemo izraziti pomoću nebaznih varijabli:

$$
\begin{aligned}
c^Tx &= c^T_Bx_B + c^T_Nx_N \\
&= c_B^TA_B^{-1}b + (c_N^T - c_B^TA_B^{-1}A_N)x_N.
\end{aligned}
$$

Stavimo li $x_N=0$, dobivamo vrijednost ciljne funkcije u trenutačnom baznom dopustivom rješenju $z=c_B^TA_B^{-1}b$. Koeficijenti drugog člana izraza pokazuju kako se ciljna funkcija mijenja kad se mijenja $x_N$:

$$
\tilde c_N = \dfrac{\partial z}{\partial x_N} = c_N - A_N^T(A_B^{-1})^Tc_B.
$$

Primijetimo da je $c_B - A_B^T(A_B^{-1})^Tc_B = 0$, pa vektor

$$
\tilde c = (\tilde c_B^T,\tilde c_N^T)^T = c - A^T(A_B^{-1})^Tc_B
$$

možemo zvati **reduciranim troškom** (reduced cost) problema linearnog programiranja u baznom dopustivom rješenju $x$. Komponenta $\tilde c_i<0$ znači da povećanje vrijednosti varijable $x_i$ poboljšava ciljnu funkciju polaznog problema. Takva varijabla može biti samo nebazna, a zove se **ulazna varijabla** (entering variable) ovog pivotiranja, jer će nakon pivotiranja $x_i$ postati bazna varijabla i više neće stalno biti postavljena na nulu (iako i dalje može biti jednaka nuli).

Nakon odabira ulazne varijable treba još odabrati staru baznu varijablu koju ćemo ukloniti. Za to je dovoljno odrediti koja postojeća bazna varijabla prva postaje nula dok povećavamo $x_i$. Uvrštavanjem $x_N=(x_i,x_{N\setminus\{i\}})=(x_i,0)$ u izraz za $x_B$ dobivamo

$$
x_B = A_B^{-1}b - A_B^{-1}A_ix_i.
$$

Stoga je najveći iznos za koji se $x_i$ može povećati jednak

$$
\theta = \min\left\{\dfrac{(A_B^{-1}b)_j}{(A_B^{-1}A_i)_j}:(A_B^{-1}A_i)_j>0\right\}.
$$

Varijabla koja prva postaje nula jest bazna varijabla $x_{B_j}$ koja odgovara indeksu $j$ u kojem se postiže minimum tog izraza. Ona je ujedno „usko grlo” pri povećavanju $x_i$ – daljnje povećanje $x_i$ učinilo bi $x_{B_j}$ negativnom. Ta je varijabla **izlazna varijabla** (leaving variable) ovog pivotiranja. Postupak određivanja izlazne varijable zove se **test minimalnog omjera** (minimum ratio test).

Neka je ulazna varijabla $x_i$, a izlazna $x_{i'}$. Nakon pivotiranja bazne su varijable $x_{B\setminus\{i'\}\cup\{i\}}$, a nebazne $x_{N\setminus\{i\}\cup\{i'\}}$.

### Uvjeti zaustavljanja

Simpleks metoda je postupak koji polazi od jednog baznog dopustivog rješenja i neprestano pivotira. Rasprava o pivotiranju u prethodnom odjeljku nije potpuna: zanemarila je neke posebne slučajeve. Neki od njih odgovaraju završetku algoritma, a neki zahtijevaju dodatnu obradu.

Prvo, ulazna varijabla ne mora postojati, tj. $\tilde c\ge 0$. Tada nema načina za daljnje poboljšanje optimalne vrijednosti, što znači da je trenutačno bazno dopustivo rješenje optimalno i algoritam završava. Za strogi dokaz te tvrdnje potrebni su [uvjeti komplementarne labavosti](./linear-programming.md#互补松弛条件). Neka je $y=(A_B^{-1})^Tc_B$. Primijetimo da je tijekom cijelog algoritma $x$ uvijek dopustivo rješenje i da vrijede uvjeti komplementarne labavosti, tj.

$$
x^T(c-A^Ty) = \tilde c^Tx = \tilde c_B^Tx_B + \tilde c_N^Tx_N = 0.
$$

Stoga je dovoljno da $y$ bude dopustivo rješenje dualnog problema, tj. $A^Ty\le c$, pa da zaključimo da su $x$ i $y$ optimalna rješenja polaznog odnosno dualnog problema. Taj je uvjet upravo $\tilde c\ge 0$, tj. nepostojanje ulazne varijable.

???+ tip "„Cijena u sjeni”"
    Vektor $y=(A_B^{-1})^Tc_B$ često se zove **dualni vektor** (dual vector). Kada je bazno dopustivo rješenje koje odgovara bazi $B$ optimalno rješenje polaznog problema, vektor $y$ je optimalno rješenje dualnog problema. Stoga, rješavajući polazni problem simpleks metodom, dobivamo i optimalno rješenje dualnog problema. Budući da je vektor $y$ parcijalna derivacija trenutačne vrijednosti po konstantama ograničenja, tj.
    
    $$
    \dfrac{\partial(c^Tx)}{\partial b} = (A_B^{-1})^Tc_B = y,
    $$
    
    on se zove i **cijena u sjeni** (shadow price).

Drugo, izlazna varijabla ne mora postojati, tj. $A_B^{-1}A_i\le 0$. Tada u postupku pivotiranja nema nikakvog „uskog grla”, što znači da se ciljna funkcija može neograničeno poboljšavati povećavanjem vrijednosti $x_i$, tako da teži k $-\infty$. To znači da je zadani problem linearnog programiranja neograničen i algoritam završava.

Konačno, odabir ulazne i izlazne varijable ne mora biti jedinstven. Neprikladan način odabira može dovesti do prevelikog broja pivotiranja, pa čak i do toga da algoritam upadne u ciklus i ne završi. Obrada takvih situacija nešto je složenija i zahtijeva primjenu [pravila pivotiranja](#pravila-pivotiranja) koja sprječavaju cikliranje i smanjuju broj pivotiranja.

### Simpleks tablica

Pri konkretnoj implementaciji pivotiranja dovoljno je nakon svakog pivotiranja održavati matricu koeficijenata problema linearnog programiranja:

$$
\tilde T_B = 
\begin{pmatrix}
-z_B & \tilde c^T_N \\
x_B & A_B^{-1}A_N
\end{pmatrix}
=
\begin{pmatrix}
-c_B^TA_B^{-1}b & c_N^T - c_B^TA_B^{-1}A_N \\
A_B^{-1}b & A_B^{-1}A_N 
\end{pmatrix}.
$$

Ona odgovara problemu linearnog programiranja:

$$
\begin{array}{rrrr}
\min_{x\ge 0}    &       & c_B^TA_B^{-1}b & + \tilde c_N^Tx_N\; \\
\text{subject to}& x_B = & A_B^{-1}b      & - A_B^{-1}A_Nx_N.
\end{array}
$$

Matrica $\tilde T_B$ zove se **sažeta simpleks tablica** (condensed simplex tableau) tog problema linearnog programiranja u odnosu na bazu $B$. Gornji lijevi kut tablice $(\tilde T_B)_{00}$ jest vrijednost trenutačnog rješenja (sa suprotnim predznakom), element $(\tilde T_B)_{0i}$ u $0$-tom retku i $i$-tom stupcu jest reducirani trošak $i$-te nebazne varijable $x_{N_i}$, element $(\tilde T_B)_{j0}$ u $j$-tom retku i $0$-tom stupcu jest vrijednost $j$-te bazne varijable $x_{B_j}$, a $A_B^{-1}A_N$ su koeficijenti u izrazu kojim su bazne varijable $x_B$ izražene pomoću nebaznih varijabli $x_N$.

Lako se vidi da se sve informacije potrebne za pivotiranje mogu izravno očitati iz sažete simpleks tablice. Konkretno, jedno pivotiranje pomoću sažete simpleks tablice sastoji se od sljedećih operacija:

1.  Odaberi stupac $i=1,\cdots,n-m$ takav da je $(\tilde T_B)_{0i}<0$. Ako takav $i$ ne postoji, trenutačno je rješenje optimalno, a $-(\tilde T_B)_{00}$ je optimalna vrijednost.
2.  Odaberi redak $j=1,\cdots,m$ takav da je $(\tilde T_B)_{ji}>0$ i da je $(\tilde T_B)_{j0}/(\tilde T_B)_{ji}$ najmanji. Ako takav $j$ ne postoji, polazni je problem neograničen.
3.  Neka varijabla $x_{N_i}$ uđe u bazu, varijabla $x_{B_j}$ izađe iz baze, i ažuriraj simpleks tablicu.

Razmotrimo sada konkretno kako se simpleks tablica ažurira. Prije ažuriranja simpleks tablice, $j$-ti redak predstavlja jednakost

$$
x_{B_j} = (\tilde T_B)_{j0} - \sum_{i=1}^{n-m}(\tilde T_B)_{ji}x_{N_i}.
$$

Da bismo ažurirali simpleks tablicu, treba $x_{N_i}$ izraziti pomoću $x_{N\setminus\{N_i\}\cup\{B_j\}}$, tj.:

$$
x_{N_i} = \dfrac{(\tilde T_B)_{j0}}{(\tilde T_B)_{ji}} - \dfrac{1}{(\tilde T_B)_{ji}}x_{B_j} - \sum_{i'\neq i}\dfrac{(\tilde T_B)_{ji'}}{(\tilde T_B)_{ji}}x_{N_{i'}}.
$$

Uvrštavanjem u preostale izraze dobivamo

$$
x_{B_{j'}} = \left((\tilde T_B)_{j'0} - (\tilde T_B)_{j'i}\dfrac{(\tilde T_B)_{j0}}{(\tilde T_B)_{ji}}\right) + \dfrac{(\tilde T_B)_{j'i}}{(\tilde T_B)_{ji}}x_{B_j} - \sum_{i'\neq i}\left((\tilde T_B)_{j'i'}-(\tilde T_B)_{j'i}\dfrac{(\tilde T_B)_{ji'}}{(\tilde T_B)_{ji}}\right)x_{N_{i'}}.
$$

Za $0$-ti redak vrijedi slično, samo lijeva strana jednakosti postaje $-z_B$. Iako izrazi izgledaju složeno, u implementaciji su potrebna samo dva koraka:

1.  Ažuriraj $j$-ti redak: neka je $\alpha=(\tilde T_B)_{ji}$, postavi broj u $i$-tom stupcu na $1$, a zatim sve brojeve u retku podijeli s $\alpha$;
2.  Ažuriraj retke $j'\neq j$: neka je $\beta=(\tilde T_B)_{j'i}$, postavi broj u $i$-tom stupcu na $0$, a zatim od svih brojeva u retku oduzmi $\beta$ puta brojeve $j$-tog retka.

???+ tip "„Simpleks tablica”"
    **Simpleks tablica** (simplex tableau) jest matrica
    
    $$
    T_B = 
    \begin{pmatrix}
    -z_B & \tilde c^T \\
    x_B & A_B^{-1}A 
    \end{pmatrix}
    =
    \begin{pmatrix}
    -c_B^TA_B^{-1}b & c^T - c_B^TA_B^{-1}A \\
    A_B^{-1}b & A_B^{-1}A 
    \end{pmatrix}.
    $$
    
    U odnosu na sažetu simpleks tablicu ima $m$ stupaca više, koji odgovaraju $m$ baznih varijabli; pritom je stupac koji odgovara $j$-toj baznoj varijabli uvijek $e_j$, tj. taj vektor ima vrijednost $1$ samo u $j$-tom retku, a u ostalim je retcima $0$. Budući da ti stupci ne nose dodatne informacije, pri implementaciji simpleks metode često se izostavljaju, čime se dobiva sažeta simpleks tablica.
    
    Pomoću simpleks tablice lakše je razumjeti korake njezina ažuriranja. Naime, sve simpleks tablice $T_B$ mogu se dobiti množenjem iste matrice $T_0$ slijeva regularnom matricom $L_B$ koja ovisi o bazi, tj.
    
    $$
    T_B=
    \begin{pmatrix}
    -c_B^TA_B^{-1}b & c^T - c_B^TA_B^{-1}A \\
    A_B^{-1}b & A_B^{-1}A 
    \end{pmatrix}
    =
    \begin{pmatrix}
    1 & -c_B^TA_B^{-1} \\
    O & A_B^{-1}
    \end{pmatrix}
    \begin{pmatrix}
    0 & c^T \\
    b & A 
    \end{pmatrix}=L_BT_0,
    $$
    
    pa se te simpleks tablice i $T_0$ mogu prevoditi jedna u drugu konačnim brojem [elementarnih transformacija redaka](./linear-algebra/elementary-operations.md). Zato je pri ažuriranju simpleks tablice dovoljno provesti elementarne transformacije redaka tako da stupac koji odgovara ulaznoj varijabli postane $e_j$. Prenesemo li potrebne operacije na sažetu simpleks tablicu, dobivamo upravo gore navedene korake.

Referentna implementacija ažuriranja sažete simpleks tablice:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/simplex/simplex_0.cpp:pivot"
    ```

Iz te implementacije vidi se da je vremenska složenost jednog ažuriranja simpleks tablice $O(mn)$. Kad kasnije budemo raspravljali o [pravilima pivotiranja](#pravila-pivotiranja), pokazat ćemo da ni složenost određivanja izlazne i ulazne varijable ne premašuje $O(mn)$, pa je vremenska složenost jednog pivotiranja $O(mn)$.

Radi lakšeg razumijevanja ovdje navodimo detaljne korake računanja sažetom simpleks tablicom za ranije prikazani primjer.

???+ example "Primjer (nastavak)"
    Na početku sažeta simpleks tablica izgleda ovako:
    
    $$
    \begin{array}{|l|c|ccc|}
    \hline
        &    & x_1 & x_2 & x_3 \\
    \hline
        & 0  & -10 & -12 & -12 \\
    \hline
    x_4= & 20 &   1 & 2   &   2 \\
    x_5= & 20 &   2 & 1   &   2 \\
    x_6= & 20 &   2 & 2   &   1 \\
    \hline
    \end{array}
    $$
    
    Prema reduciranim troškovima u $0$-tom retku, u bazu mogu ući $x_1,x_2,x_3$. Neka uđe $x_1$. Zatim prema testu minimalnog omjera iz baze mogu izaći $x_5,x_6$. Neka izađe $x_5$. Sažeta simpleks tablica ažurira se ovako:
    
    $$
    \begin{array}{|l|c|ccc|}
    \hline
        &    & x_5 & x_2 & x_3 \\
    \hline
        &100 & 5   & -7  & -2  \\
    \hline
    x_4= & 10 &-0.5 & 1.5 &   1 \\
    x_1= & 10 & 0.5 & 0.5 &   1 \\
    x_6= &  0 & -1  & 1   &  -1 \\
    \hline
    \end{array}
    $$
    
    Prema reduciranim troškovima u $0$-tom retku, u bazu mogu ući $x_2,x_3$. Neka uđe $x_3$. Zatim prema testu minimalnog omjera iz baze mogu izaći $x_4,x_1$. Neka izađe $x_4$. Sažeta simpleks tablica ažurira se ovako:
    
    $$
    \begin{array}{|l|c|ccc|}
    \hline
        &    & x_5 & x_2 & x_4 \\
    \hline
        &120 & 4   & -4  & 2   \\
    \hline
    x_3= & 10 &-0.5 & 1.5 &  1  \\
    x_1= &  0 &  1  & -1  & -1  \\
    x_6= & 10 & -1.5& 2.5 &  1  \\
    \hline
    \end{array}
    $$
    
    Prema reduciranim troškovima u $0$-tom retku, u bazu može ući samo $x_2$. Neka uđe $x_2$. Zatim prema testu minimalnog omjera iz baze može izaći samo $x_6$. Neka izađe $x_6$. Pomoću opisanih elementarnih transformacija redaka simpleks tablica ažurira se ovako:
    
    $$
    \begin{array}{|l|c|ccc|}
    \hline
        &    & x_5 & x_6  & x_4 \\
    \hline
        &136 & 1.6 & 1.6 & 3.6 \\
    \hline
    x_3= & 4  & 0.4 &-0.6 & 0.4 \\
    x_1= &  4 & 0.4 & 0.4 &-0.6 \\
    x_2= &  4 & -0.6& 0.4 & 0.4 \\
    \hline
    \end{array}
    $$
    
    Prema reduciranim troškovima u $0$-tom retku, ulazna varijabla ne postoji. Stoga je trenutačno rješenje
    
    $$
    x=(4,4,4,0,0,0)^T
    $$
    
    optimalno, a optimalna vrijednost (problema minimizacije) je $-136$.

Osim implementacije simpleks metode pomoću simpleks tablice, može se koristiti i revidirana simpleks metoda (revised simplex method), koja dodatno poboljšava vremensku i prostornu složenost algoritma te složenost jednog ažuriranja smanjuje na $O(m^2)$; osobito je učinkovita kad je $m\ll n$ ili kad je $A$ rijetka matrica.

## Geometrijska pozadina

U ovom odjeljku predstavljamo geometrijsku pozadinu simpleks metode.

[Analiza](./linear-programming.md#可行域与问题的解) dopustivog područja problema linearnog programiranja

$$
\mathcal D = \{x\in\mathbf R^n : Ax = b,~ x\ge 0\}
$$

pokazuje:

-   Optimalno rješenje problema linearnog programiranja (ako postoji) uvijek se može odabrati kao vrh dopustivog područja $\mathcal D$. Rješavanje problema linearnog programiranja tako se svodi na pronalaženje, među svim vršnim rješenjima, onoga s najboljom vrijednošću ciljne funkcije.
-   Koordinate svakog vrha mogu se dobiti rješavanjem sustava koji čini $n$ aktivnih (tijesnih) ograničenja. Kod ograničenja u standardnom obliku svih $m$ ograničenja jednakosti sigurno je aktivno, a preostalih $n-m$ ograničenja može se birati samo među ograničenjima nenegativnosti. Odabir tih ograničenja nenegativnosti kao aktivnih znači postavljanje odgovarajućih varijabli odlučivanja $x_N$ na $0$; sustav $Ax = b$ pritom se svodi na sustav linearnih jednadžbi $A_Bx_B = b$ u preostalih $m$ varijabli odlučivanja $x_B$. Čim je $A_B$ regularna, možemo riješiti $x_B = A_B^{-1}b$. Time dobivamo rješenje $(x_B,x_N)=(A_B^{-1}b,0)$; ako je $x_B\ge 0$, to su koordinate jednog vrha od $\mathcal D$.

Lako se vidi da se pojam vršnog rješenja podudara s ranije definiranim baznim dopustivim rješenjem. Stoga je dovoljno među svim baznim dopustivim rješenjima pronaći najbolje da bismo dobili optimalno rješenje polaznog problema. Iako to znatno pojednostavljuje problem, broj vrhova dopustivog područja može biti eksponencijalan, pa iscrpno pretraživanje nije realno.

Da bismo riješili tu poteškoću, možemo se kretati duž [bridova](./linear-programming.md#可行域与问题的解) dopustivog područja, s jednog vrha na njemu susjedni vrh. Budući da susjedni vrhovi nužno leže na istom bridu, oni zadovoljavaju barem $n-1$ zajedničkih aktivnih ograničenja. Drugim riječima, aktivna ograničenja susjednih vrhova mogu se i moraju razlikovati u točno jednom. Stoga, za bazno dopustivo rješenje $x$, dovoljno je jednu njegovu baznu varijablu zamijeniti nebaznom pa dobiti **susjedno** (adjacent) bazno dopustivo rješenje $x'$. To je upravo pivotiranje.

Dakle, postupak u kojem simpleks metoda polazi od jednog baznog dopustivog rješenja i neprestanim pivotiranjem poboljšava ciljnu funkciju zapravo je postupak u kojem se na pripadnom dopustivom području polazi od jednog vrha i neprestano prelazi na susjedne vrhove, poboljšavajući ciljnu funkciju.

???+ example "Primjer (nastavak)"
    U primjeru iz ovog članka dopustivo je područje trodimenzionalni poliedar s pet vrhova, prikazan na sljedećoj slici:
    
    ![](./images/simplex-geo.svg)
    
    Opisani postupak rješavanja, geometrijski gledano, odgovara sljedećem putu po vrhovima poliedra:
    
    $$
    (0,0,0) \rightarrow (10,0,0) \rightarrow (0,0,10) \rightarrow (4,4,4).
    $$

## Detalji implementacije

Pomoću simpleks tablice već možemo riješiti mnoge probleme linearnog programiranja. Ipak, za najopćenitiji slučaj u simpleks metodi ostaje još mnogo detalja vrijednih dublje rasprave.

### Kanonski oblik

[Postupak](./linear-programming.md#标准形式) pretvaranja problema linearnog programiranja iz općeg oblika u standardni već je obrađen. No da bi rješavanje simpleks metodom bilo jednostavno, treba još osigurati da matrica koeficijenata $A$ bude punog ranga. Iako je izvedivo najprije prijeći na standardni oblik pa zatim ukloniti linearno zavisna ograničenja, radi jednostavnijeg rješavanja obično se primjenjuje sljedeća strategija:

1.  Problem linearnog programiranja pretvori se u **oblik s nejednakostima** (inequality form), tj. oblik $\min\{c^Tx : Ax \le b,~ x \ge 0\}$;
2.  Dodavanjem dopunskih varijabli $s$ problem se pretvori u standardni oblik: $\min\{c^Tx : Ax + s = b,~ x\ge 0,~ s \ge 0\}$.

Prednost je toga što je matrica koeficijenata $(A,I)$ konačno dobivenog standardnog oblika uvijek punog ranga i uvijek postoji (ne nužno dopustivo) bazno rješenje $(x,s)=(0,b)$. Taj se posebni standardni oblik zove i **kanonski oblik** (slack form).

### Početno bazno dopustivo rješenje

Prethodno opisana simpleks metoda uvijek pretpostavlja da je poznato jedno bazno dopustivo rješenje. Ponekad je bazno dopustivo rješenje lako pronaći. Na primjer, ako je u gornjem kanonskom obliku $b\ge 0$, onda je $(x,s)=(0,b)$ bazno dopustivo rješenje. To je situacija na koju smo naišli u ranijem numeričkom primjeru.

U općem slučaju može se primijeniti **metoda dviju faza** (two-phase method). U metodi dviju faza simpleks metoda se provodi dvaput. U prvoj fazi rješava se problem dopustivosti linearnog programiranja i dobiva jedno bazno dopustivo rješenje polaznog problema. U drugoj fazi, polazeći od tog baznog dopustivog rješenja, simpleks metodom se rješava polazni problem.

Pretpostavimo da imamo problem u standardnom obliku $\min\{c^Tx : Ax = b \ge 0,~ x\ge 0\}$. U prvoj fazi treba riješiti problem

$$
\min\{1^Tx_a : Ax + x_a = b,~ x\ge 0,~ x_a\ge 0\}.
$$

To je u biti problem dopustivosti linearnog programiranja, u kojem se novododane varijable $x_a$ zovu i **umjetne varijable** (artificial variable). On sigurno ima bazno dopustivo rješenje $(x,x_a)=(0,b)$, pa se može izravno riješiti simpleks metodom. Ako je optimalna vrijednost tog problema strogo veća od $0$, onda ne postoji $x\ge 0$ takav da je $Ax=b$, tj. polazni je problem nedopustiv. Ako je optimalna vrijednost tog problema jednaka $0$, onda umjetne varijable u njegovu optimalnom rješenju mogu biti samo nula. Ako su neke umjetne varijable još uvijek bazne, može ih se izbaciti iz baze s nekoliko pivotiranja. Konačno, kad su sve umjetne varijable nebazne, bazno rješenje dobiveno u prvoj fazi može poslužiti kao početno bazno dopustivo rješenje druge faze.

???+ note "Implementacija prve faze bez eksplicitnog uvođenja umjetnih varijabli"
    Pri implementaciji prve faze nije nužno eksplicitno uvoditi umjetne varijable. Za proizvoljno odabranu početnu bazu $B$ vrijedi
    
    $$
    x_B + A_B^{-1}A_Nx_N = A_B^{-1}b.
    $$
    
    Ako je $(A_B^{-1}b)_j\ge 0$, umjetnu varijablu nije potrebno uvoditi; inače treba dodatno uvesti umjetnu varijablu $x^{-}_{B_j}$, tj.
    
    $$
    x_{B_j} - x^-_{B_j} + (A_B^{-1}A_N)_{(j)}x_N = (A_B^{-1}b)_j.
    $$
    
    Označimo skup indeksa $L:=\{j:(A_B^{-1}b)_j<0\}$. Tada se sve simpleks tablice prve faze dobivaju iz sljedeće simpleks tablice konačnim brojem elementarnih transformacija redaka:
    
    $$
    \begin{array}{|r|c|cccc|}
    \hline
                    &                       & x_N                      & x_{B_{\sim L}} & x_{B_L}  &x_{B_{L}}^- \\  
    \hline
                    & 0                     & 0^T                      & 0^T            & 0^T      & 1^T        \\
    \hline
    x_{B_{\sim L}}=  & (A_B^{-1}b)_{\sim L}  & (A_B^{-1}A_N)_{(\sim L)} & I              &  O       &  O         \\
    x_{B_{L}}^-=     & (A_B^{-1}b)_L         & (A_B^{-1}A_N)_{(L)}      & O              &  I       & -I         \\
    \hline
    \end{array}
    $$
    
    Slično kao što se simpleks tablica sažima u sažetu simpleks tablicu, i ovu možemo prikladno pojednostavniti (retke $x_{B_{L}}^-$ pomnožimo slijeva s $1^T$ i dodamo $0$-tom retku, a zatim izostavimo posljednja tri stupca):
    
    $$
    \begin{array}{|r|c|cccc|}
    \hline
                    &                      & x_N                      \\  
    \hline
                    & 1^T(A_B^{-1}b)_L     & 1^T(A_B^{-1}A_N)_{(L)}   \\
    \hline
    x_{B_{\sim L}}= & (A_B^{-1}b)_{\sim L} & (A_B^{-1}A_N)_{(\sim L)} \\
    -x_{B_{L}}=     & (A_B^{-1}b)_L        & (A_B^{-1}A_N)_{(L)}      \\
    \hline
    \end{array}
    $$
    
    To se uglavnom podudara s običnom sažetom simpleks tablicom, samo što su varijable u posljednjem retku označene predznakom minus, koji pokazuje da taj redak još sadrži umjetnu varijablu, tj. da je izvorna dopunska varijabla još uvijek nedopustiva. Pomoću te tablice postupak pivotiranja teče ovako:
    
    1.  Ako je $L=\varnothing$, algoritam završava.
    2.  Inače, prema uvjetu da je reducirani trošak u $0$-tom retku negativan odaberi ulaznu varijablu $x_{N_i}$. Ako takva ne postoji, polazni je problem nedopustiv i algoritam završava.
    3.  Zatim prema $i$-tom stupcu odaberi izlaznu varijablu $x_{B_j}$. I dalje se koristi test minimalnog omjera, ali se zahtijeva da trenutačno dopustive varijable ostanu dopustive, a trenutačno nedopustive nedopustive, tj. bira se
    
        $$
        \arg\min_{j}\left\{\dfrac{(\tilde T_B)_{j0}}{(\tilde T_B)_{ji}}:(j\notin L\land(\tilde T_B)_{ji}>0)\lor(j\in L\land(\tilde T_B)_{ji}<0)\right\}
        $$
    
        kao redak izlazne varijable. Ako postoji više takvih izlaznih varijabli, prednost ima nedopustiva izlazna varijabla.
    4.  Neka $x_{N_i}$ uđe u bazu, $x_{B_j}$ izađe iz baze, i ažuriraj simpleks tablicu.
    5.  Ako je $j\in L$, ukloni $j$ iz $L$ (tj. ukloni oznaku minus s tog retka) i uvećaj $(\tilde T_B)_{0i}$ za jedan.
    
    Stupci umjetnih varijabli mogu se izostaviti zato što su, dok su one još bazne, njihovi stupci jednaki $e_j$ pa ih nije potrebno bilježiti, a kad više nisu bazne, nikad više neće ući u bazu, pa ih također nije potrebno bilježiti. Kad umjetna varijabla izlazi iz baze, treba je zamijeniti odgovarajućom neumjetnom varijablom; upravo je to svrha posljednjeg koraka gornjeg postupka.
    
    Referentna implementacija:
    
    ??? example "Referentna implementacija"
        ```cpp
        --8<-- "docs/math/code/simplex/simplex_0.cpp:initialize"
        ```
    
    Prije početka prve faze dodaje se dodatni redak za ciljnu funkciju prve faze. Pri pivotiranju pivotira se cijela tablica, uključujući ciljnu funkciju druge faze. Tako se po završetku prve faze i ciljna funkcija druge faze već odgovarajuće ažurira, pa se simpleks metoda druge faze može odmah započeti.

Metoda dviju faza može se provesti i jednom primjenom simpleks metode. Dovoljno je uzeti dovoljno velik pozitivan broj $M$ i izravno riješiti problem

$$
\min\{c^Tx + M1^Tx_a : Ax + x_a = b,~ x\ge 0,~ x_a\ge 0\}
$$

da bismo dobili optimalno rješenje polaznog problema. U implementaciji se $M$ ne pridružuje konkretna brojčana vrijednost, nego se s njim računa kao s nepoznatim dovoljno velikim pozitivnim brojem. Ta se metoda zove **metoda velikog $M$** (big $M$ method).

???+ warning "Stvarna učinkovitost naivnog algoritma je eksponencijalna"
    Budući da kanonski oblik uvijek ima početno bazno rješenje, samo što ono ne mora biti dopustivo, jednostavna ideja za traženje početnog baznog dopustivog rješenja jest sljedeća: polazeći od nedopustivog baznog rješenja, opetovano pivotiranjem izbacujemo nedopustive bazne varijable iz baze, a u bazu uvodimo nebaznu varijablu čiji stupac u odgovarajućem retku također sadrži negativan broj, sve dok sve bazne varijable ne postanu nenegativne. Referentna implementacija:
    
    ??? example "Referentna implementacija"
        ```cpp
        --8<-- "docs/math/code/simplex/simplex_2.cpp:initialize"
        ```
    
    Iako je to jednostavno, u usporedbi s metodom dviju faza ovaj pristup nema ciljnu funkciju koja opisuje stupanj nedopustivosti trenutačne baze, pa mu nedostaje jasan smjer poboljšanja. Praktična testiranja pokazuju da, dok metoda dviju faza ili metoda velikog $M$ obično trebaju $O(m)$ pivotiranja, ovaj naivni algoritam obično treba $O(2^m)$ pivotiranja te pri većim $n,m$ lako upada u ciklus. Iako je konstanta u broju pivotiranja naivnog algoritma vrlo mala, on je primjenjiv samo za $n,m<50$.

### Pravila pivotiranja

Ako se pri pivotiranju pojavi više mogućih ulaznih ili izlaznih varijabli, potrebno je **pravilo pivotiranja** (pivot rule) kojim se odlučuje koja će varijabla ući u bazu odnosno izaći iz nje. Pomoću simpleks tablice sva pravila o kojima se raspravlja u ovom odjeljku mogu pronaći ulaznu i izlaznu varijablu u vremenu $O(mn)$, pa vremenska složenost jednog pivotiranja ostaje $O(mn)$.

Odabir ulazne varijable često određuje broj pivotiranja prije završetka algoritma. Uobičajena pravila su:

-   odabrati prvu pronađenu ulaznu varijablu;
-   odabrati ulaznu varijablu s najmanjim indeksom (dio Blandova pravila);
-   odabrati ulaznu varijablu s najvećom apsolutnom vrijednošću reduciranog troška (tj. $|\tilde c_i|$) (Dantzigovo pravilo);
-   odabrati ulaznu varijablu s najvećim poboljšanjem ciljne funkcije u jednom pivotiranju (tj. $|\tilde c_i|\theta_i$);
-   odabrati ulaznu varijablu koja odgovara najstrmijem bridu, tj. onu s najvećim poboljšanjem ciljne funkcije po jediničnoj duljini pomaka duž brida (tj. $|\tilde c_i|/\sqrt{1+\|A_B^{-1}A_i\|^2}$);
-   odabrati ulaznu varijablu nasumično.

U praksi je najučinkovitije pravilo najstrmijeg brida[^steepest-edge]. Općenito se smatra da se prikladnim pravilom pivotiranja optimalno rješenje većine problema dobiva u otprilike $2m$ pivotiranja. Međutim, za sva trenutačno poznata pravila pivotiranja postoje posebno konstruirani primjeri[^klee-minty] koji broj pivotiranja tjeraju na eksponencijalan. Upravo je to razlog zašto je simpleks metoda u praksi iznimno učinkovita, a teorijska složenost u najgorem slučaju eksponencijalna.

Odabir izlazne varijable često određuje hoće li algoritam upasti u ciklus. Ako više baza odgovara istom baznom dopustivom rješenju (tj. degenerirani slučaj), algoritam može beskonačno kružiti među tim bazama. Takve situacije nisu česte, pa mnoge implementacije simpleks metode ne propisuju pravilo odabira izlazne varijable. Dva su uobičajena pravila za izbjegavanje cikliranja:

-   Blandovo pravilo: uvijek odaberi ulaznu i izlaznu varijablu s najmanjim indeksom.
-   Leksikografsko pravilo: uvijek odaberi izlaznu varijablu $x_{B_j}$ koja odgovara retku $j$ za koji je $(A_B^{-1}A_i)_j>0$ i

    $$
    \left(\dfrac{(A_B^{-1}b)_j}{(A_B^{-1}A_i)_j},\dfrac{(A_B^{-1})_{j1}}{(A_B^{-1}A_i)_j},\cdots,\dfrac{(A_B^{-1})_{jm}}{(A_B^{-1}A_i)_j}\right)
    $$

    leksikografski najmanji. Odabir ulazne varijable nije bitan.

    Primijetimo: ako je problem linearnog programiranja u kanonskom obliku, sve te veličine mogu se izravno očitati iz simpleks tablice $T_B$ ranije opisanog oblika; inače, nakon što se pronađe početno bazno rješenje (ne nužno dopustivo), kao koeficijenti od $A_B^{-1}$ mogu se uzeti koeficijenti u stupcima koji odgovaraju baznim varijablama te početne baze (u fiksnom redoslijedu).

Blandovo pravilo vrlo je neučinkovito jer samo pravilo bira ulaznu i izlaznu varijablu na isti način, što lako dovodi do toga da ista varijabla opetovano ulazi u bazu i izlazi iz nje. Leksikografsko je pravilo razmjerno praktičnije. Ono odgovara maloj perturbaciji parametara problema linearnog programiranja[^lexico], zbog koje ne postoje degenerirana bazna dopustiva rješenja, pa ni mogućnost cikliranja.

## Referentna implementacija

U ovom odjeljku dajemo referentnu implementaciju simpleks metode dviju faza temeljenu na sažetoj simpleks tablici.

??? example "[Luogu P13337【模板】线性规划 (Predložak: linearno programiranje)](https://www.luogu.com.cn/problem/P13337)"
    ```cpp
    --8<-- "docs/math/code/simplex/simplex_0.cpp:full-text"
    ```

## Primjeri zadataka

???+ example "[「NOI2008」志愿者招募 (Zapošljavanje volontera)](https://www.luogu.com.cn/problem/P3980)"
    Za aktivnost koja traje ukupno $n$ dana treba zaposliti volontere, pri čemu je $i$-tog dana potrebno barem $b_i$ volontera. Postoji $m$ vrsta volontera, pri čemu volonteri $j$-te vrste mogu raditi u neprekinutom intervalu dana $[l_j,r_j]$, a jedinični trošak njihova zapošljavanja je $c_j$. Odredite optimalan plan zapošljavanja tako da trošak zapošljavanja volontera bude najmanji.

??? note "Rješenje"
    Neka se zaposli $x_j$ volontera $j$-te vrste. Tada možemo postaviti problem linearnog programiranja
    
    $$
    \begin{align*}
    \min_{x}\; & \sum_{j=1}^mc_jx_j \\
    \text{subject to }& \sum_{j=1}^m a_{ij}x_j \ge b_i,~i=1,\cdots,n,\\
    & x_j\ge 0,~j=1,\cdots,m.
    \end{align*}
    $$
    
    Pritom su koeficijenti
    
    $$
    a_{ij} = 
    \begin{cases}
    1,& l_j\le i\le r_j,\\
    0,& \text{otherwise.}
    \end{cases}
    $$
    
    Polazni problem nema očito početno dopustivo rješenje. Zato promotrimo njegov [dualni problem](./linear-programming.md#对偶问题):
    
    $$
    \begin{align*}
    \max_{y}\; & \sum_{i=1}^n b_iy_i \\
    \text{subject to } & \sum_{i=1}^na_{ij}y_i \le c_j,~j=1,\cdots,m,\\
    & y_i\ge 0,~i=1,\cdots,n.
    \end{align*}
    $$
    
    Dodavanjem dopunskih varijabli lako dobivamo početno dopustivo rješenje, pa prvu fazu možemo preskočiti i problem izravno riješiti simpleks metodom. Prema teoremu dualnosti dobiveno je rješenje ujedno rješenje polaznog problema.
    
    ```cpp
    --8<-- "docs/math/code/simplex/simplex_1.cpp"
    ```

## Zadaci za vježbu

-   [Luogu P13337【模板】线性规划 (Predložak: linearno programiranje)](https://www.luogu.com.cn/problem/P13337)
-   [UOJ#179. 线性规划 (Linearno programiranje)](https://uoj.ac/problem/179)
-   [Luogu P4232 无意识之外的捉迷藏 (Skrivač izvan nesvjesnog)](https://www.luogu.com.cn/problem/P4232)
-   [Codeforces 1430 G. Yet Another DAG Problem](https://codeforces.com/problemset/problem/1430/G)
-   [AtCoder Beginner Contest 231 H - Minimum Coloring](https://atcoder.jp/contests/abc231/tasks/abc231_h)

## Literatura

-   [线性规划之单纯形法【超详解 + 图解】(Simpleks metoda u linearnom programiranju – vrlo detaljno objašnjenje s ilustracijama)](https://www.cnblogs.com/ECJTUACM-873284962/p/7097864.html)
-   [Radovi kineske nacionalne trening-ekipe 2016.](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2016%E8%AE%BA%E6%96%87%E9%9B%86.pdf)
-   Introduction to Algorithms (算法导论)
-   Matoušek, Jiří, and Bernd Gärtner. Understanding and using linear programming. Vol. 1. Berlin: Springer, 2007.
-   Inayatullah, Syed, Nasir Touheed, and Muhammad Imtiaz. "A streamlined artificial variable free version of simplex method." PloS one 10, no. 3 (2015): e0116156.
-   Floudas, Christodoulos A., and Panos M. Pardalos, eds. Encyclopedia of optimization. Springer Science & Business Media, 2008.

[^notation]: Načelno, budući da su svi vektori po dogovoru stupčani, $(x_B,x_N)$ bi trebalo pisati kao $(x_B^T,x_N^T)^T$. No radi jednostavnosti zapisa, u ovom se članku svi takvi slučajevi pišu izravno kao $(x_B,x_N)$, s izostavljenim znakom transponiranja.

[^steepest-edge]: Za rezultate testiranja vidi Forrest, John J., and Donald Goldfarb. "Steepest-edge simplex algorithms for linear programming." Mathematical programming 57, no. 1 (1992): 341-374.

[^klee-minty]: Klasičan protuprimjer može se naći u Klee, Victor, and George J. Minty. "How good is the simplex algorithm." Inequalities 3, no. 3 (1972): 159-175.

[^lexico]: Detaljno objašnjenje može se naći u [ovim bilješkama s predavanja](https://misha.fish/archive/docs/3272-fall-2022/lecture8.pdf).
