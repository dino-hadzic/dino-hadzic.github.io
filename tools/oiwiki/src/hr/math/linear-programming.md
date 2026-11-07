---
title: Osnove linearnog programiranja
---

## Uvod

Linearno programiranje (linear programming, LP) zajednički je naziv za metode proučavanja problema ekstrema linearne ciljne funkcije uz linearna ograničenja; grana je operacijskih istraživanja i ima primjene u mnogim područjima. Neki posebni slučajevi linearnog programiranja, poput problema mrežnog toka i višerobnog toka (multi-commodity flow), mogu se pojaviti u zadacima na algoritamskim natjecanjima. Na algoritamskim natjecanjima rijetko se pojavljuju zadaci koji se mogu riješiti samo algoritmima linearnog programiranja; velika većina takvih zadataka može se učinkovitije riješiti modeliranjem mrežnim tokom i sličnim metodama.

### Jednostavan primjer

Da bi se problem mogao zapisati u obliku linearnog programa, mora imati i nekoliko linearnih ograničenja i linearnu ciljnu funkciju.

Razmotrimo sljedeći primjer:

???+ example "Primjer"
    Majstor u pekarnici svaki dan može napraviti određenu količinu baozija (punjenih peciva na pari) i youtiaoa (prženih štapića od tijesta); oba su doručka vrlo omiljena među kupcima. Kako bi maksimizirao dobit, majstor želi napraviti što više doručaka, ali je u praksi ograničen raznim resursima poput sastojaka i vremena. Zato je popisao količinu sastojaka, vrijeme izrade i pripadnu dobit po porciji svakog doručka, kako prikazuje sljedeća tablica:
    
    | Doručak | Biljno ulje | Brašno | Vrijeme | Dobit |
    | :-: | :-: | :-: | :-: | :-: |
    | Baozi | $4$ | $7$ | $8$ | $5$ |
    | Youtiao | $7$ | $3$ | $6$ | $6$ |
    
    Pretpostavimo da majstor dnevno može nabaviti najviše $66$ jedinica biljnog ulja i $60$ jedinica brašna te uložiti najviše $96$ jedinica vremena izrade. Kako majstor treba rasporediti proizvodnju baozija i youtiaoa da bi dnevna dobit bila najveća?

Opišimo to matematičkim jezikom: neka su $x_1$ i $x_2$ redom količine baozija i youtiaoa koje majstor napravi. Tada se uvjet „ukupno potrebno biljno ulje ne premašuje $66$ jedinica” može zapisati kao

$$
4x_1 + 7x_2 \le 66.
$$

Slično, uvjeti „ukupno potrebno brašno ne premašuje $60$ jedinica” i „ukupno potrebno vrijeme ne premašuje $96$ jedinica” zapisuju se kao

$$
\begin{aligned}
7x_1 + 3x_2 &\le 60,\\
8x_1 + 6x_2 &\le 96.
\end{aligned}
$$

Osim toga, majstor ne može proizvesti negativan broj doručaka, pa vrijedi i uvjet

$$
x_1,x_2\ge 0.
$$

Majstor, dakle, uz ta ograničenja treba maksimizirati dobit:

$$
z = 5x_1 + 6x_2.
$$

To je tipičan problem linearnog programiranja. Njegova je ciljna funkcija linearna funkcija varijabli odlučivanja, a ograničenja čine linearne jednadžbe ili nejednadžbe u varijablama odlučivanja.

### Grafička metoda

Problemi linearnog programiranja sa samo dvije varijable odlučivanja mogu se zorno riješiti grafičkom metodom.

Promotrimo geometrijsku sliku koja odgovara problemu iz ovog odjeljka

$$
\begin{aligned}
\max_{x_1,x_2}\;& z = 5x_1 + 6x_2 \\
\text{subject to } & 4x_1 + 7x_2 \le 66,\\
& 7x_1 + 3x_2 \le 60,\\
& 8x_1 + 6x_2 \le 96,\\
& x_1,x_2\ge 0
\end{aligned}
$$

Zadnji redak ograničenja znači da se sve dopustive točke $(x_1,x_2)$ nalaze u prvom kvadrantu, a ostala tri ograničenja znače da dopustive točke moraju ležati ispod pravaca $4x_1 + 7x_2 = 66$, $7x_1 + 3x_2 = 60$ i $8x_1 + 6x_2 = 96$. Presjek tih područja (zeleno područje na slici dolje) skup je svih točaka koje dolaze u obzir:

![](images/linear-programming.svg)

Zatim treba maksimizirati vrijednost $z=5x_1+6x_2$. Shvatimo li tu jednakost kao jednadžbu pravca $5x_1+6x_2=z$, onda s promjenom $z$ dobivamo familiju paralelnih pravaca, i što je $z$ veći, pravac je bliže gornjem desnom kutu. Stoga je dovoljno pomicati pravac sve dok ne dosegne kritični položaj u kojem bi se, pomaknemo li ga još malo gore-desno, prestao sjeći s prikazanim područjem; vrijednost $z$ koja odgovara tom pravcu upravo je tražena najveća vrijednost.

Kao što slika pokazuje, to se događa u položaju označenom crvenom točkom. To je sjecište pravaca $4x_1 + 7x_2 = 66$ i $7x_1 + 3x_2 = 60$. Rješavanjem sustava jednadžbi tih dvaju pravaca dobivamo da su njegove koordinate $(6,6)$. To je jedino optimalno rješenje ovog problema. Najveća dobit majstora iznosi $z=66$.

Kad problem ima više od dvije varijable odlučivanja, grafička metoda više nije primjenjiva. Međutim, neka zapažanja iz primjera u ovom odjeljku i dalje vrijede. Svako ograničenje u obliku nejednakosti u problemu linearnog programiranja opisuje jednu „poluravninu”, a skup svih dopustivih rješenja presjek je tih „poluravnina”, pa je uvijek „konveksan poligon”. Optimalno rješenje problema uvijek se može postići u nekom „vrhu” tog „konveksnog poligona”. Koordinate tih „vrhova” mogu se dobiti rješavanjem sustava jednadžbi „rubova” tih „poluravnina”. Proširenjem tih zapažanja na višedimenzionalne prostore razvijena je učinkovita metoda za rješavanje problema linearnog programiranja – simpleks metoda. To je ujedno metoda koja se najčešće primjenjuje na algoritamskim natjecanjima.

Još jedan problem vrijedan pažnje jest to da baoziji i youtiaoi koje majstor pravi načelno nisu beskonačno djeljivi, nego bi njihov broj trebao biti cijeli. Iako to pri rješavanju ovog zadatka nismo izričito zahtijevali, konačno optimalno rješenje doista je cjelobrojno, pa odgovor ostaje dopustiv čak i ako dodamo cjelobrojno ograničenje. No za mnoge probleme optimizacije optimalno se rješenje možda ne može postići u cjelobrojnoj točki; takvi su problemi zapravo problemi cjelobrojnog programiranja, a ne obični problemi linearnog programiranja. Ta je vrsta problema kratko razmotrena na kraju ovog članka.

## Osnovni pojmovi

U ovom se odjeljku uvode osnovni pojmovi problema linearnog programiranja.

### Problem linearnog programiranja

Problem linearnog programiranja $P$ obično se sastoji od sljedeća dva dijela:

-   linearne ciljne funkcije, tj. funkcije oblika

    $$
    f(x_1,x_2,\cdots,x_n)=c_1x_1+c_2x_2+\cdots+c_nx_n
    $$

    gdje su $c_i\in\mathbf R$ konstante;

-   linearnih ograničenja, tj. ograničenja u obliku nejednakosti ili jednakosti

    $$
    g_j(x_1,x_2,\cdots,x_n)=a_{j1}x_1+a_{j2}x_2+\cdots+a_{jn}x_n \le (=,\ge) b_j
    $$

    gdje su $a_{ji},b_j\in\mathbf R$ konstante.

Problem linearnog programiranja sastoji se u tome da se uz zadovoljavanje zadanih ograničenja maksimizira ili minimizira ciljna funkcija. Rješenje $(x_1,x_2,\cdots,x_n)\in\mathbf R^n$ koje zadovoljava zadana ograničenja naziva se **dopustivo rješenje** (feasible solution); ono dopustivo rješenje pri kojem ciljna funkcija postiže ekstrem naziva se **optimalno rješenje** (optimal solution).

### Standardni oblik

Radi lakšeg opisa i daljnje obrade obično se propisuje standardni oblik problema linearnog programiranja. Različita literatura može ga propisivati različito; u ovom članku standardni oblik linearnog programa definiramo ovako:

$$
\begin{aligned}
\min_{\{x_i\}}\;& \sum_{i=1}^n c_ix_i \\
\text{subject to }& \sum_{i=1}^n a_{ji}x_i = b_j \ge 0,~j=1,\cdots,m,\\
& x_i \ge 0,~i = 1,\cdots,n.
\end{aligned}
$$

Drugim riječima, problem linearnog programiranja problem je minimizacije, sve varijable odlučivanja imaju ograničenje nenegativnosti, a osim toga sadrži samo niz ograničenja u obliku jednakosti s nenegativnom konstantom na desnoj strani. Pomoću [matrica](./linear-algebra/matrix.md) taj se problem može zapisati sažetije:

$$
\min\{c^Tx : Ax = b \ge 0,~ x\ge 0\}.
$$

Ovdje je $x=(x_i)\in\mathbf R^n$ vektor varijabli odlučivanja, a $b=(b_j)\in\mathbf R^m$ i $A=(a_{ji})\in\mathbf R^{m\times n}$ konstante koje se pojavljuju u ograničenjima. Veličina problema linearnog programiranja odnosi se na broj njegovih varijabli odlučivanja i broj njegovih ograničenja.

???+ tip "Vektorske nejednakosti"
    U ovom će se članku više puta pojavljivati vektorske nejednakosti poput $b \ge 0$. Općenito, za vektore $x,y\in\mathbf R^n$ nejednakost $x\le y$ znači $\forall i(x_i\le y_i)$, tj. usporedbu realnih brojeva po koordinatama. Ta je relacija [parcijalni uređaj](./order-theory.md#binarna-relacija) na vektorskom prostoru, što znači da postoje parovi vektora koji se ne mogu usporediti.

Odabir standardnog oblika služi samo lakšem izlaganju i nije ni po čemu poseban, jer se svaki problem linearnog programiranja može ekvivalentno zapisati u svakom od sljedećih šest oblika:

$$
\begin{aligned}
&\min\{c^Tx : Ax = b,~ x\ge 0\},\\
&\min\{c^Tx : Ax \ge b\},\\
&\min\{c^Tx : Ax \ge b,~ x\ge 0\},\\
&\max\{c^Tx : Ax = b,~ x\ge 0\}, \\
&\max\{c^Tx : Ax \le b\},\\
&\max\{c^Tx : Ax \le b,~ x\ge 0\}.\\
\end{aligned}
$$

Sljedećim se operacijama svaki problem linearnog programiranja može ekvivalentno pretvoriti u bilo koji od tih šest oblika:

1.  Dodavanjem predznaka minus, tj. zamjenom $c$ s $-c$, problem maksimizacije pretvara se u problem minimizacije i obrnuto.
2.  Dodavanjem predznaka minus, tj. zamjenom $a_j^Tx \lesseqqgtr b_j$ s $-a_j^Tx \gtreqqless -b_j$, mijenja se smjer nejednakosti u ograničenju, odnosno konstanta na desnoj strani ograničenja u obliku jednakosti postaje nenegativna.
3.  Svako ograničenje u obliku jednakosti $a_j^Tx = b_j$ može se zamijeniti dvama ograničenjima u obliku nejednakosti suprotnih smjerova, $a_j^Tx \ge b_j$ i $a_j^Tx \le b_j$.
4.  Svako ograničenje u obliku nejednakosti $a_j^Tx \le(\ge) b_j$ može se dodavanjem nenegativne dopunske varijable $s_j$ pretvoriti u ograničenje u obliku jednakosti $a_j^Tx +(-) s_j = b_j$ zajedno s pripadnim ograničenjem nenegativnosti $s_j\ge 0$.
5.  Ako neka varijabla odlučivanja $x_i$ nema ograničenje nenegativnosti, može se zamijeniti razlikom dviju nenegativnih varijabli, tj. $x_i = x^+_i - x^-_i$ uz $x^+_i,x^-_i \ge 0$.

Veličina problema linearnog programiranja dobivenog tim operacijama ne premašuje dvostruku veličinu izvornog problema, a dopustiva i optimalna rješenja tih problema lako se preslikavaju jedna u druga. Stoga se problem linearnog programiranja u općem obliku uvijek može najprije pretvoriti u standardni oblik (ili u jedan od navedenih šest oblika) pa tek onda rješavati.

??? example "Primjer"
    Promotrimo problem linearnog programiranja
    
    $$
    \begin{aligned}
    \max\;& 3x_1 - 2x_2 + x_3 \\
    \text{subject to }& 2x_1 + 3x_2 + 4x_3 \ge 1,\\
    & 3x_1 + 4x_2 \le 5,\\
    & 5x_2 - x_3 = -1, \\
    & x_1, x_2 \ge 0.
    \end{aligned}
    $$
    
    Operacijama 1, 2 i 3 može se pretvoriti u oblik $\min\{c^Tx : Ax \ge b\}$, tj.
    
    $$
    \begin{aligned}
    \min\;& -3x_1 + 2x_2 - x_3 \\
    \text{subject to }& 2x_1 + 3x_2 + 4x_3 \ge 1,\\
    & -3x_1 - 4x_2 \ge -5,\\
    & 5x_2 - x_3 \ge -1, \\
    & -5x_2 + x_3 \ge 1, \\
    & x_1 \ge 0,\\
    & x_2 \ge 0.
    \end{aligned}
    $$
    
    Operacijama 4 i 5 može se pretvoriti u oblik $\max\{c^Tx : Ax = b,~ x\ge 0\}$, tj.
    
    $$
    \begin{aligned}
    \max\;& 3x_1 - 2x_2 + x^+_3 - x^-_3 \\
    \text{subject to }& 2x_1 + 3x_2 + 4x^+_3 - 4x^-_3 - x_4 = 1,\\
    & 3x_1 + 4x_2 + x_5 = 5,\\
    & 5x_2 - x^+_3 + x^-_3 = -1, \\
    & x_1, x_2, x^+_3, x^-_3, x_4, x_5 \ge 0.
    \end{aligned}
    $$

### Dopustivo područje i rješenja problema

Skup svih dopustivih rješenja $\mathcal D\subseteq\mathbf R^n$ naziva se **dopustivo područje** (feasible region) problema linearnog programiranja $P$. Geometrijski gledano, svako ograničenje u obliku nejednakosti $a_j^T x \le b_j$ opisuje poluprostor $\{x\in\mathbf R^n:a_j^T x \le b_j\}$, a svako ograničenje u obliku jednakosti $a^T_jx = b_j$ opisuje hiperravninu $\{x\in\mathbf R^n:a_j^Tx=b_j\}$, pa je dopustivo područje nužno presjek konačno mnogo poluprostora i hiperravnina. U području optimizacije[^poly-names] takvo se geometrijsko tijelo obično naziva **poliedar** (polyhedron) u $\mathbf R^n$. Poliedar je uvijek zatvoren konveksan skup, ali ne mora biti omeđen. Omeđeni poliedar naziva se i **politop** (polytope). Politop se može shvatiti kao poopćenje poligona u ravnini na prostore više dimenzije, a poliedar ga dalje poopćuje na moguće neomeđen slučaj.

???+ example "Primjeri poliedara"
    Navodimo neke uobičajene poliedre:
    
    1.  Prazan skup $\varnothing$, koji se naziva i **nulitop** (nullitope); njegova se dimenzija po dogovoru definira kao $-1$.
    2.  **Afini potprostor** (affine subspace), tj. presjek nekoliko hiperravnina $\{x\in\mathbf R^n:Ax = b\}$. On odgovara skupu rješenja sustava linearnih jednadžbi $Ax = b$: kad sustav nema rješenja, to je prazan skup; inače se uvijek može zapisati u obliku $x_0+V$, gdje je $x_0\in\mathbf R^n$, a $V\subseteq\mathbf R^n$ linearni potprostor dimenzije $n-\operatorname{rank}A$. Posebno, i hiperravnine su afini potprostori.
    3.  **Poliedarski konus** (polyhedral cone), tj. skup svih nenegativnih linearnih kombinacija $\{\sum_i\alpha_ix_i:\alpha_i\ge 0\}$ konačno mnogo točaka $\{x_i\}$ u prostoru. To je konveksan konus s vrhom u ishodištu. Ekvivalentno, može se shvatiti kao poliedar omeđen nekoliko hiperravnina koje prolaze ishodištem, tj. $\{x\in\mathbf R^n : Ax\le 0\}$. Posebno, i poluprostori su poliedarski konusi.
    4.  Politop, tj. omeđen poliedar. Posebno, politopi dimenzije $-1$, $0$, $1$, $2$ i $3$ redom su poznati prazan skup, točka, dužina, poligon i poliedar (u uobičajenom smislu). Skup je politop ako i samo ako je konveksna ljuska $\{\sum_i\alpha_ix_i:\alpha_i\ge 0,~\sum_i\alpha_i=1\}$ konačno mnogo točaka $\{x_i\}$. Politop dimenzije $k$ konveksna je ljuska razapeta s najmanje $k+1$ točaka.
    5.  **Simpleks** (simplex), tj. politop dimenzije $k$ razapet s točno $k+1$ točaka. To je najjednostavniji politop dimenzije $k$. Posebno, simpleksi dimenzije $-1$, $0$, $1$, $2$ i $3$ redom su prazan skup, točka, dužina, trokut i tetraedar. Najjednostavniji primjer simpleksa dimenzije $k$ jest $\{x\in\mathbf R^{k+1}:x_i\ge 0,~\sum_ix_i=1\}$. Zapravo se svaki simpleks dimenzije $k$ afinom transformacijom (tj. translacijom i skaliranjem) može prevesti u taj posebni slučaj. Vrijedi napomenuti da se simpleks metoda zapravo ne izvodi na simpleksu.
    
    Svaki se poliedar može shvatiti kao [suma Minkowskog](../geometry/convex-hull.md#suma-minkowskog) jednog poliedarskog konusa i jednog politopa: prvi opisuje neomeđeni dio poliedra, a drugi oblik njegova omeđenog dijela. Taj je poliedarski konus jedinstven: poliedarski konus dobiven rastavom poliedra $\{x\in\mathbf R^n:Ax\le b\}$ nužno je $\{x\in\mathbf R^n:Ax\le 0\}$.

Rješenja linearnog programa usko su povezana sa strukturom poliedra. Za poliedar $\mathcal D\subseteq\mathbf R^n$ i vektor $c\in\mathbf R^n\setminus\{0\}$ promotrimo sljedeći problem linearnog programiranja $P$ (slučaj minimizacije razmatra se analogno):

$$
\max\{c^Tx:x\in\mathcal D\}.
$$

Geometrijski gledano, to znači pomicati hiperravninu $H:c^Tx = z$ u smjeru vektora $c$ tako da $z$ bude što veći, uz uvjet da hiperravnina $H$ i dopustivo područje $\mathcal{D}$ imaju barem jednu zajedničku točku. Postoje tri mogućnosti:

-   Dopustivo područje $\mathcal D$ prazan je skup. To znači da problem $P$ nema dopustivog rješenja, tj. neka su njegova ograničenja međusobno proturječna. Tada kažemo da je problem $P$ **nedopustiv** (infeasible), a njegova optimalna vrijednost po dogovoru iznosi $-\infty$.

-   Dopustivo područje $\mathcal D$ neprazno je, ali sadrži zraku sa smjerom $d$ za koji je $c^Td>0$, tj. postoji $x_0\in\mathbf R^n$ takav da $x_0+td\in\mathcal D$ vrijedi za sve $t\ge 0$. Budući da se hiperravnina $H$ može neograničeno pomicati u smjeru vektora $c$, a pritom skup $H\cap\mathcal D$ sadrži barem jednu točku te zrake pa je sigurno neprazan, ciljna funkcija $c^Tx = c^Tx_0 + tc^Td$ može poprimiti proizvoljno velike vrijednosti. Tada kažemo da je problem $P$ **neomeđen** (unbounded), a njegova optimalna vrijednost po dogovoru iznosi $+\infty$.

-   Dopustivo područje $\mathcal D$ neprazno je i ne sadrži nijednu takvu zraku. Tada kažemo da je problem $P$ **omeđen** (bounded). Označimo sa $z^*\in\mathbf R$ optimalnu vrijednost problema $P$. Hiperravnina $H^*:c^Tx = z^*$ nalazi se u kritičnom položaju: siječe poliedar $\mathcal D$, a $\mathcal D$ je sadržan u poluprostoru $\{x:c^Tx\le z^*\}$. Takva se hiperravnina naziva **potporna hiperravnina** (supporting hyperplane) poliedra $\mathcal D$. Skup optimalnih rješenja problema $P$ upravo je $H^*\cap\mathcal D$. Kao presjek potporne hiperravnine i poliedra, skup $H^*\cap\mathcal D$ nužno je poliedar i sadržan je u rubu poliedra $\mathcal D$. Naziva se **strana** (face) poliedra $\mathcal D$. Slikovito rečeno, poliedar je omeđen tim stranama. Osim tih strana, nastalih kao presjek potporne hiperravnine i poliedra, poliedar općenito ima još dvije strane: prazan skup i sam poliedar. Sve strane poliedra s obzirom na relaciju inkluzije skupova tvore strukturu [rešetke](../math/order-theory.md#usmjereni-skupovi-i-rešetke).

    Dimenzija strane poliedra dimenzije $d$ nužno je cijeli broj između $-1$ i $d$. Strana dimenzije $0$ (tj. točka) naziva se **vrh** (vertex) ili **kutna točka** (corner point) poliedra $\mathcal D$, strana dimenzije $1$ naziva se **brid** (edge) poliedra $\mathcal D$, a strana dimenzije $d-1$ naziva se **faceta** (facet) poliedra $\mathcal D$. Međutim, nemaju svi poliedri vrhove. Budući da je strana strane poliedra i sama strana tog poliedra, a jedino afini potprostori nemaju strogo manjih nepraznih strana, sve minimalne strane poliedra $\mathcal D$ afini su potprostori. Štoviše, minimalne strane istog poliedra imaju jednaku dimenziju; posebno, dimenzija minimalnih strana poliedra $\mathcal D=\{x\in\mathbf R^n:Ax\le b\}$ iznosi $n-\operatorname{rank}A$.

    Budući da su strane poliedra upravo skupovi rješenja omeđenih problema linearnog programiranja, treba razjasniti kako odrediti jednadžbe strana poliedra. Neka je poliedar $\mathcal D$ opisan nizom ograničenja $a_j^Tx \lesseqqgtr b_j$ i neka je $F$ jedna strana od $\mathcal D$. Ako neko ograničenje u svim točkama $x\in F$ vrijedi s jednakošću, kažemo da je to ograničenje **aktivno** (tight) na strani $F$. Točke strane $F$ očito zadovoljavaju sustav jednadžbi dobiven izjednačavanjem tih aktivnih ograničenja, a presjek afinog potprostora određenog tim sustavom i poliedra $\mathcal D$ upravo je strana $F$. Obrnuto, odaberemo li bilo koji podskup ograničenja poliedra $\mathcal D$, ta ograničenja pretvorimo u jednakosti i riješimo dobiveni sustav, presjek dobivenog afinog potprostora i poliedra jedna je strana od $\mathcal D$. Štoviše, što više aktivnih ograničenja odaberemo, to je dobivena strana (u smislu inkluzije) manja.

    Posebno, matrica koeficijenata $\begin{pmatrix}A\\ I\end{pmatrix}$ dopustivog područja $\mathcal D=\{x\in\mathbf R^n:Ax=b,~x\ge 0\}$ linearnog programa u standardnom obliku ima rang $n$, pa su njegove minimalne strane upravo njegovi vrhovi. Drugim riječima, ako je problem omeđen, njegovo se optimalno rješenje uvijek može odabrati u nekom vrhu. Štoviše, taj se vrh može dobiti odabirom $n$ linearno nezavisnih aktivnih ograničenja i rješavanjem pripadnog sustava. Upravo je to prednost standardnog oblika linearnog programa.

???+ example "Primjer"
    Na slici dolje $\mathcal D$ je dopustivo područje. Kad su koeficijenti ciljne funkcije $c_1,c_2,c_3$, dobivamo redom tri slučaja: jedinstveno optimalno rješenje, više optimalnih rješenja i neomeđen problem. U prvim dvama slučajevima odgovarajući debeli crveni puni pravac (jedna je od) potpornih hiperravnina koje odgovaraju skupu rješenja, a skupovi optimalnih rješenja redom su vrh $B$ i brid $\overline{CD}$ poliedra $\mathcal D$. U trećem slučaju dopustivo područje $\mathcal D$ sadrži zraku smjera $c_3$, pa se hiperravnina s normalom $c_3$ može neograničeno pomicati u smjeru $c_3$, te je problem neomeđen.
    
    ![](./images/lp-feasible.svg)

U ovim je razmatranjima izostavljen slučaj $c=0$. Tada problem linearnog programiranja očito ne može biti neomeđen, pa je ili sam problem nedopustiv ili je optimalna vrijednost jednaka $0$, a skup optimalnih rješenja upravo je $\mathcal D$. Takvi se posebni linearni programi nazivaju i **linearnim programima dopustivosti** (feasibility linear programming).

Vrijedi istaknuti da su problemi poput odlučivanja je li problem linearnog programiranja dopustiv ili omeđen te nalaženja dopustivog rješenja sustava nejednadžbi jednako teški kao i samo rješavanje problema linearnog programiranja[^reducible]. Primjerice, dokaz teorema o jakoj dualnosti u nastavku pokazuje da je rješavanje omeđenog problema linearnog programiranja ekvivalentno nalaženju dopustivog rješenja skupa nejednadžbi. Stoga je za zadatke poput odlučivanja ima li sustav nejednadžbi rješenje ili ima li sustav jednadžbi nenegativno rješenje najučinkovitiji način rješavanje pripadnog linearnog programa dopustivosti[^other-methods].

Osim toga, ako neko ograničenje problema linearnog programiranja nije aktivno ni na jednoj strani dopustivog područja, to je ograničenje **redundantno** (redundant). U primjeru s pekarskim majstorom s početka ovog članka ograničenje radnog vremena redundantno je ograničenje. Problem odlučivanja je li u zadanom sustavu nejednadžbi neka nejednadžba $a_j^Tx\le b_j$ redundantna može se riješiti rješavanjem problema linearnog programiranja $\max\{a_j^Tx:x\in\mathcal D\}$ i usporedbom rezultata s $b_j$.

## Uobičajeni algoritmi

Na algoritamskim natjecanjima rijetko se pojavljuju problemi koji se mogu riješiti samo algoritmima linearnog programiranja. Većina zadataka koji se mogu riješiti metodama linearnog programiranja obično se može riješiti i specijaliziranijim i učinkovitijim algoritmima poput mrežnog toka.

Uobičajeni algoritmi za rješavanje problema linearnog programiranja jesu:

-   [simpleks metoda](./simplex.md)
-   metoda elipsoida
-   metode unutarnje točke

Iako je složenost simpleks metode u najgorem slučaju eksponencijalna, a složenost metoda unutarnje točke polinomna, obje vrste algoritama izvrsno se ponašaju na većini praktičnih problema. Nasuprot tome, metoda elipsoida, iako joj je teorijska složenost polinomna, obično je spora i nije praktična.

Još nije poznato postoji li za probleme linearnog programiranja algoritam jako polinomne složenosti.

## Dualni problem

Svakom problemu linearnog programiranja odgovara dualni problem. Rješenja primarnog (izvornog) i dualnog problema usko su povezana. Dualni problem ne samo da pomaže dubljem razumijevanju strukture problema nego često može i povećati učinkovitost rješavanja primarnog problema.

Za problem linearnog programiranja $P$ (sve varijable označene malim slovima su vektori)

$$
\begin{aligned}
\min_{x_1,x_2,x_3}\;& c_1^Tx_1 + c_2^Tx_2 + c_3^Tx_3 \\
\text{subject to }& A_{11}x_1 + A_{12}x_2 + A_{13}x_3 \ge b_1,\\
& A_{21}x_1 + A_{22}x_2 + A_{23}x_3 = b_2,\\
& A_{31}x_1 + A_{32}x_2 + A_{33}x_3 \le b_3,\\
& x_1\ge 0,~ x_3\le 0,
\end{aligned}
$$

njegov dualni problem $D$ jest problem linearnog programiranja

$$
\begin{aligned}
\max_{y_1,y_2,y_3}\;&b_1^Ty_1+b_2^Ty_2+b_3^Ty_3 \\
\text{subject to }&A_{11}^Ty_1 + A_{21}^Ty_2 + A_{31}^Ty_3\le c_1,\\
&A_{12}^Ty_1 + A_{22}^Ty_2 + A_{32}^Ty_3 = c_2,\\
&A_{13}^Ty_1 + A_{23}^Ty_2 + A_{33}^Ty_3 \ge c_3,\\
&y_1\ge 0,~ y_3\le 0.
\end{aligned}
$$

Pritom su varijable odlučivanja dualnog problema $y_1,y_2,y_3$ redom Lagrangeovi multiplikatori triju vrsta ograničenja primarnog problema; obrnuto, varijable odlučivanja primarnog problema $x_1,x_2,x_3$ redom su Lagrangeovi multiplikatori triju vrsta ograničenja dualnog problema. Lako se provjeri da je dualni problem dualnog problema upravo primarni problem.

Odnos između primarnog problema $P$ i dualnog problema $D$ je sljedeći:

| Problem minimizacije | Problem maksimizacije |
| :----: | :----: |
| ograničenje „veće ili jednako” | nenegativna varijabla |
| ograničenje „manje ili jednako” | nepozitivna varijabla |
| ograničenje u obliku jednakosti | slobodna varijabla |
| nenegativna varijabla | ograničenje „manje ili jednako” |
| nepozitivna varijabla | ograničenje „veće ili jednako” |
| slobodna varijabla | ograničenje u obliku jednakosti |
| koeficijenti ciljne funkcije | konstante na desnoj strani ograničenja |
| konstante na desnoj strani ograničenja | koeficijenti ciljne funkcije |

Posebno, dualni problem linearnog programa u standardnom obliku

$$
\min\{c^Tx:Ax=b,~x\ge 0\}
$$

jest

$$
\max\{b^Ty:A^Ty\le c\}.
$$

### Princip dualnosti

Primarni i dualni problem nisu samo formalno zrcalne slike jedan drugoga, nego su im i rješenja usko povezana. To se naziva **princip dualnosti** (duality principle). Radi jednostavnosti izlaganja, pri iskazivanju i dokazivanju teorema u ovom odjeljku primarni problem uzimamo u standardnom obliku.

Najprije, **teorem o slaboj dualnosti** (weak duality theorem) kaže da maksimum dualnog problema ne premašuje minimum primarnog problema.

???+ note "Teorem o slaboj dualnosti"
    Za sve $A\in\mathbf R^{m\times n}$, $b\in\mathbf R^m$ i $c\in\mathbf R^n$ uvijek vrijedi
    
    $$
    \max\{b^Ty:A^Ty\le c\} \le \min\{c^Tx:Ax=b,~x\ge 0\}.
    $$

??? note "Dokaz"
    Ako je bilo koji od primarnog i dualnog problema nedopustiv, nejednakost je trivijalna. Pretpostavimo da su oba problema dopustiva. Tada za sve dopustive $x$ i $y$ vrijedi
    
    $$
    b^Ty = x^TA^Ty \le x^Tc.
    $$
    
    Uzimanjem ekstrema na objema stranama dobivamo da vrijedi teorem o slaboj dualnosti.

Za daljnje razmatranje odnosa između rješenja primarnog i dualnog problema potrebna je još Farkasova lema (i njezine razne inačice). Ona daje nužan i dovoljan uvjet da sustav linearnih jednadžbi ima nenegativno rješenje.

???+ note "Farkasova lema"
    Za $A\in\mathbf R^{m\times n}$ i $b\in\mathbf R^m$ vrijedi točno jedna od sljedećih dviju tvrdnji:
    
    1.  postoji $x\in\mathbf R^n$ takav da je $Ax=b$ i $x\ge 0$;
    2.  postoji $y\in\mathbf R^m$ takav da je $A^T y\ge 0$ i $b^Ty<0$.

??? note "Dokaz"
    Kad bi obje tvrdnje vrijedile istodobno, imali bismo $0\le (A^Ty)^Tx = y^T(Ax) = b^Ty<0$, što je kontradikcija. Dakle, vrijedi najviše jedna od tvrdnji. Pokažimo sada da vrijedi barem jedna. Označimo s $C=\{Ax:x\ge 0\}$ poliedarski konus razapet stupcima matrice $A$. Ako je $b\in C$, vrijedi tvrdnja 1; inače treba pokazati da vrijedi tvrdnja 2. Budući da se poliedarski konus $C$ može zapisati i kao presjek konačno mnogo poluprostora koji prolaze ishodištem, on je zatvoren konveksan skup. Kako je $b\notin C$, prema teoremu o separaciji hiperravninom postoje $y\in\mathbf R^m$ i $\alpha\in\mathbf R$ takvi da je $b^Ty<\alpha$ i $z^Ty>\alpha$ za sve $z\in C$. Budući da je $0\in C$, vrijedi $\alpha<0$, pa je $b^Ty<0$. Nadalje, budući da za sve $x\ge 0$ i $t>0$ vrijedi $t(A^Ty)^Tx>\alpha$, puštajući $t\to+\infty$ dobivamo da $(A^Ty)^Tx\ge 0$ vrijedi za sve $x\ge 0$, tj. $A^Ty\ge 0$. To je upravo tvrdnja 2.

Geometrijski gledano, tvrdnja 1 kaže da točka $b$ leži u poliedarskom konusu $C$ razapetom stupcima matrice $A$; tvrdnja 2 kaže da postoji hiperravnina $H:y^Tx = 0$ koja prolazi ishodištem i ima normalu $y$, a strogo razdvaja točku $b$ od poliedarskog konusa $C$. Farkasova lema stoga je svojevrsni [teorem o separaciji hiperravninom](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem).

Pomoću Farkasove leme dobiva se način da se na temelju dopustivosti primarnog i dualnog problema odluči je li primarni problem neomeđen.

???+ note "Korolar"
    Problem linearnog programiranja neomeđen je ako i samo ako je dopustiv, a njegov je dualni problem nedopustiv.

??? note "Dokaz"
    I dalje za primjer uzimamo primarni problem u standardnom obliku. Problem linearnog programiranja u općem obliku dovoljno je najprije pretvoriti u standardni oblik, jer pretvorbe opisane [ranije](#standardni-oblik) ne mijenjaju dopustivost ni omeđenost problema i njegova dualnog problema.
    
    S jedne strane, ako je primarni problem neomeđen, očito je dopustiv, a optimalna mu je vrijednost $-\infty$. Tada dualni problem nužno nije dopustiv, jer bi inače njegova optimalna vrijednost bila ne manja od nekog realnog broja, što proturječi teoremu o slaboj dualnosti.
    
    S druge strane, neka je primarni problem dopustiv, a dualni nedopustiv. Zapišemo li slobodnu varijablu u ograničenju $A^Ty\le c$ kao razliku dviju nenegativnih varijabli $y=y^+-y^-$ i dodamo nenegativnu dopunsku varijablu $s$, ono postaje ekvivalentno ograničenju $Mz=c$ uz $z\ge 0$, gdje je $M=(A^T,-A^T,I)$ i $z=(y^+,y^-,s)$. Budući da je $M^Td=(Ad,-Ad,d)$, primjena Farkasove leme na $M$ i $c$ pokazuje da ili postoji $y$ takav da je $A^Ty\le c$, ili postoji $d\ge 0$ takav da je $Ad=0$ i $c^Td<0$, i to točno jedno od toga. Prema pretpostavci vrijedi potonje. Uzmemo li tada bilo koje dopustivo rješenje $x_0$ primarnog problema, vrijedi $A(x_0+td)=b$ i $x_0+td\ge 0$ za sve $t\ge 0$, dok $c^T(x_0+td)=c^Tx_0+tc^Td\to-\infty~(t\to+\infty)$. To pokazuje da je primarni problem neomeđen.

Kombiniranjem teorema o slaboj dualnosti i ovog korolara, za rješenja primarnog i dualnog problema moguća su samo sljedeća četiri slučaja:

1.  primarni i dualni problem oba su nedopustiva, tj. $-\infty\le+\infty$;
2.  primarni je problem nedopustiv, a dualni neomeđen, tj. $+\infty\le+\infty$;
3.  primarni je problem neomeđen, a dualni nedopustiv, tj. $-\infty\le-\infty$;
4.  primarni i dualni problem oba su omeđena.

U četvrtom slučaju vrijedi jači zaključak: optimalne vrijednosti primarnog i dualnog problema jednake su. Objedinimo li posljednja tri slučaja, dobivamo **teorem o jakoj dualnosti** (strong duality theorem): čim je barem jedan od primarnog i dualnog problema dopustiv, njihove su optimalne vrijednosti nužno jednake.

???+ note "Teorem o jakoj dualnosti"
    Za sve $A\in\mathbf R^{m\times n}$, $b\in\mathbf R^m$ i $c\in\mathbf R^n$ vrijedi
    
    $$
    \max\{b^Ty:A^Ty\le c\} = \min\{c^Tx:Ax=b,~x\ge 0\}.
    $$
    
    čim je barem jedan od dvaju skupova neprazan.

??? note "Dokaz"
    U prethodnom razmatranju jedini slučaj u kojem optimalna vrijednost nije određena jest onaj kad su i primarni i dualni problem dopustivi. Tada promotrimo sljedeći linearni program dopustivosti $Q$:
    
    $$
    \max\{0:c^Tx \le b^Ty,~Ax=b,~x\ge 0,~A^Ty\le c\}.
    $$
    
    Ako problem $Q$ ima dopustivo rješenje $(x^*,y^*)\in\mathbf R^n\times\mathbf R^m$, onda prema teoremu o slaboj dualnosti i optimalnosti vrijedi
    
    $$
    b^Ty^* \le \max\{b^Ty:A^Ty\le c\} \le \min\{c^Tx:Ax=b,~x\ge 0\} \le c^Tx^*,
    $$
    
    no $c^Tx^*\le b^Ty^*$, pa u svim tim nejednakostima vrijedi jednakost; drugim riječima, ne samo da vrijedi jaka dualnost nego su $x^*$ i $y^*$ redom optimalna rješenja primarnog i dualnog problema.
    
    Dovoljno je stoga dokazati da je problem $Q$ dopustiv. Pretpostavimo suprotno. Po uzoru na dokaz gornjeg korolara promotrimo dualni problem $DQ$ problema $Q$:
    
    $$
    \min\{c^T\mu - b^T\lambda : ct - A^T\lambda \ge 0,~ -bt + A\mu = 0,~t\ge 0,~\mu\ge 0\}.
    $$
    
    Budući da je $(t,\lambda,\mu)=(0,0,0)$ dopustivo rješenje dualnog problema $DQ$, prema gornjem korolaru nedopustivost problema $Q$ znači da je dualni problem $DQ$ neomeđen, tj. da postoji $(t^*,\lambda^*,\mu^*)$ takav da je
    
    $$
    c^T\mu^* - b^T\lambda^* <0,~ ct^* - A^T\lambda^* \ge 0,~ -bt^* + A\mu^* = 0,~t^*\ge 0,~\mu^*\ge 0.
    $$
    
    Ako je pritom $t^*>0$, te nejednakosti zapravo kažu da je $(x,y)=(\mu^*/t^*,\lambda^*/t^*)$ dopustivo rješenje prethodnog problema, što proturječi pretpostavci. Stoga mora biti $t^*=0$. To znači
    
    $$
    c^T\mu^* < b^T\lambda^*,~ A^T\lambda^*\le 0,~ A\mu^*=0,~\mu^*\ge 0.
    $$
    
    Međutim, kako smo već pretpostavili da su primarni i dualni problem iz teorema oba dopustiva, tj. da postoji $(x_0,y_0)$ za koji vrijedi
    
    $$
    Ax_0 = b,~ x_0\ge 0,~ A^Ty_0\le c
    $$
    
    imamo
    
    $$
    0 = (A\mu^*)^Ty_0 = (A^Ty_0)^T\mu^* \le c^T\mu^* < b^T\lambda^* = x_0^TA^T\lambda^* \le 0.
    $$
    
    To je očita kontradikcija. Ta kontradikcija pokazuje da je problem $Q$ dopustiv, a time i da vrijedi jaka dualnost.

Iz dokaza teorema o jakoj dualnosti dobiva se i sljedeći korolar:

???+ note "Korolar"
    Neka dopustiva rješenja $x^*$ i $y^*$ primarnog odnosno dualnog problema zadovoljavaju jaku dualnost, tj. $c^Tx^* = b^Ty^*$. Tada su ona ujedno redom optimalna rješenja primarnog i dualnog problema.

Teorem o jakoj dualnosti pokazuje da je za dopustiv problem linearnog programiranja dovoljno riješiti njegov dualni problem da bi se dobila optimalna vrijednost primarnog problema.

### Uvjeti komplementarnosti

Kao i kod drugih problema optimizacije, uvjeti komplementarnosti dio su uvjeta optimalnosti problema linearnog programiranja. Štoviše, budući da je ciljna funkcija linearna, za probleme linearnog programiranja uvjeti komplementarnosti nužan su i dovoljan uvjet da dopustivo rješenje bude optimalno.

Uvjet **komplementarnosti** (complementary slackness) kaže da varijabla dualnog (primarnog) problema može poprimiti vrijednost različitu od nule samo kad odgovarajuće ograničenje primarnog (dualnog) problema vrijedi s jednakošću (tj. kad je ograničenje aktivno). Shvatimo li i to da varijabla poprima vrijednost različitu od nule kao jedno labavo (neaktivno) ograničenje, onda to znači da odgovarajuća varijabla i ograničenje primarnog i dualnog problema ne mogu istodobno biti labavi. Zato se taj uvjet naziva uvjetom komplementarne labavosti (komplementarnosti).

Na primjeru linearnog programa u standardnom obliku vrijedi sljedeći zaključak:

???+ note "Teorem"
    Neka su $x^*$ i $y^*$ redom dopustiva rješenja primarnog problema $\min\{c^Tx:Ax=b,~x\ge 0\}$ i dualnog problema $\max\{b^Ty:A^Ty\le c\}$. Tada vrijedi uvjet komplementarnosti, tj.
    
    $$
    (x^*)^T(A^Ty^*-c) = 0
    $$
    
    ako i samo ako su $x^*$ i $y^*$ ujedno redom optimalna rješenja primarnog i dualnog problema.

??? note "Dokaz"
    Budući da su $x^*$ i $y^*$ dopustiva rješenja, vrijedi
    
    $$
    b^Ty^* - c^Tx^* = (x^*)^T(A^T y^* - c).
    $$
    
    Stoga uvjet komplementarnosti vrijedi ako i samo ako je $b^Ty^* = c^Tx^*$. Prema korolaru teorema o jakoj dualnosti taj uvjet vrijedi ako i samo ako su $x^*$ i $y^*$ redom optimalna rješenja primarnog i dualnog problema.

Standardni je oblik možda previše poseban. Nešto općenitiji oblik tog teorema glasi:

???+ note "Teorem"
    Neka su $x^*$ i $y^*$ redom dopustiva rješenja primarnog problema $\min\{c^Tx:Ax\ge b,~x\ge 0\}$ i dualnog problema $\max\{b^Ty:A^Ty\le c,~y\ge 0\}$. Tada vrijede uvjeti komplementarnosti, tj.
    
    $$
    (x^*)^T(A^Ty^*-c) = (y^*)^T(Ax^*-b) = 0
    $$
    
    ako i samo ako su $x^*$ i $y^*$ ujedno redom optimalna rješenja primarnog i dualnog problema.

??? note "Dokaz"
    Dokaz je u osnovi isti kao gore, samo što se razlika ovaj put zapisuje kao
    
    $$
    b^Ty^* - c^Tx^* = (x^*)^T(A^T y^* - c) - (y^*)^T(Ax^*-b).
    $$

Uvjeti komplementarnosti daju jednostavan kriterij za provjeru optimalnosti dopustivog rješenja problema linearnog programiranja.

### Primarno-dualna metoda

Dualni problem može pomoći pri rješavanju primarnog problema. Pri rješavanju problema linearnog programiranja često se koristi **primarno-dualna metoda** (primal-dual method). Ona rješavanjem niza razmjerno jednostavnih pomoćnih problema postupno poboljšava rješenje dualnog problema i tako dolazi do optimalnog rješenja primarnog problema.

Za primarni problem u standardnom obliku

$$
(P)\qquad\min\{c^Tx : Ax=b\ge 0,~ x\ge 0\}
$$

i njegov dualni problem

$$
(D)\qquad\max\{b^Ty : A^Ty\le c\},
$$

u prethodnom je odjeljku pokazano da je za nalaženje njihovih optimalnih rješenja dovoljno naći par dopustivih rješenja problema $(P)$ i $(D)$ koja zadovoljavaju uvjet komplementarnosti $x^T(A^Ty-c)=0$. Razmotrimo stoga sljedeći postupak:

1.  Krenuvši od dopustivog rješenja $y$ dualnog problema $(D)$, izračunamo skup aktivnih ograničenja dualnog problema

    $$
    I = \{i : (A^Ty - c)_i = 0\}.
    $$

2.  Prema uvjetu komplementarnosti, ako postoji dopustivo rješenje $x$ problema $(P)$ takvo da $x_i>0$ vrijedi samo za $i\in I$, to znači da smo već našli par optimalnih rješenja. Zato promotrimo problem linearnog programiranja

    $$
    (RP)\qquad
    \begin{aligned}
    \min_{x,s}\;& 1^Ts \\
    \text{subject to } & Ax + s = b, \\
    & x_i \ge 0,~\forall i \in I,\\
    & x_i = 0,~\forall i \notin I,\\
    & s \ge 0.
    \end{aligned}
    $$

3.  Ako je minimum problema $(RP)$ jednak $0$, onda je $x^*$ iz optimalnog rješenja $(x^*,0)$ optimalno rješenje izvornog problema $(P)$. Inače se može naći rješenje $\bar y$ njegova dualnog problema $(DRP)$:

    $$
    (DRP)\qquad
    \begin{aligned}
    \max_{y}\;& b^Ty \\
    \text{subject to }& \sum_{j}a_{ji}y_j \le 0,~\forall i\in I,\\
    & y \le 1.
    \end{aligned}
    $$

    Prema teoremu o jakoj dualnosti vrijedi $b^T\bar y = 1^Ts^*>0$.

4.  Pomoću rješenja problema $(DRP)$ poboljšamo dopustivo rješenje dualnog problema $(D)$. Neka je $y' = y + \varepsilon \bar y$, gdje je $\varepsilon>0$; tada sigurno vrijedi $b^Ty' = b^Ty + \varepsilon b^T\bar y > b^Ty$. Stoga, dokle god je $y'$ i dalje dopustivo rješenje dualnog problema $(D)$, vrijednost $\varepsilon$ treba odabrati što većom.

    Za $i\in I$ vrijedi

    $$
    \sum_ja_{ji}y'_j = \sum_ja_{ji}y_j + \varepsilon \sum_ja_{ji}\bar y_j \le c_i,
    $$

    pa su ta ograničenja problema $(D)$ uvijek zadovoljena.

    Za preostala ograničenja, tj. za $i\notin I$, dovoljno je uzeti

    $$
    \varepsilon = \min\left\{\dfrac{c_i - \sum_{j}a_{ji}y_j}{\sum_{j}a_{ji}\bar y_j}:i\notin I,~\textstyle\sum_{j}a_{ji}\bar y_j>0\right\}
    $$

    čime se, uz očuvanje dopustivosti, rješenje dualnog problema poboljšava što je više moguće; zatim se vraćamo na korak 1 i nastavljamo iteraciju. Posebno, ako je skup u gornjem izrazu prazan, tj. $\varepsilon=+\infty$, onda je dualni problem $(D)$ neomeđen, a izvorni problem $(P)$ nedopustiv.

U tom postupku zapravo treba stvarno riješiti samo problem $(DRP)$, koji je s problemom $(RP)$ povezan teoremom o jakoj dualnosti. Problem $(DRP)$ daje smjer poboljšanja rješenja dualnog problema, a u usporedbi sa samim dualnim problemom $(D)$ problem $(DRP)$ ima jednostavniji oblik. Problem $(DRP)$ uvijek je dopustiv ($y=0$ je jedno dopustivo rješenje), a ograničenje $y\le 1$ samo je normalizacijski uvjet koji osigurava da je problem $(DRP)$ omeđen.

Na algoritamskim natjecanjima primarno-dualna metoda široko se primjenjuje na razne probleme kombinatorne optimizacije. Primjerice, [Mađarski algoritam](../graph/graph-matching/bigraph-weight-match.md#mađarski-algoritam-kuhnmunkresov-algoritam) za najveće težinsko sparivanje u bipartitnom grafu, [algoritam poništavanja ciklusa](../graph/flow/min-cost.md) i [algoritam SSP (primarno-dualni algoritam)](../graph/flow/min-cost.md#algoritam-ssp) za tok minimalne cijene, [Dijkstrin algoritam](../graph/shortest-path.md#dijkstrin-algoritam) za najkraće putove, [Ford–Fulkersonov algoritam povećanja](../graph/flow/max-flow.md#fordfulkersonovo-povećanje) za maksimalni tok itd. mogu se shvatiti kao izravne primjene primarno-dualne metode.

## Cjelobrojno programiranje

**Cjelobrojno programiranje** (integer programming) obično označava **cjelobrojno linearno programiranje** (integer linear programming, ILP). Cjelobrojni linearni program u standardnom obliku glasi:

$$
\begin{aligned}
\min_{x}\; & c^Tx \\
\text{subject to } & Ax = b \ge 0,\\
& x \ge 0,\\
& x \in \mathbf Z^n,
\end{aligned}
$$

gdje je $A\in\mathbf R^{m\times n}$, $b\in\mathbf R^m$, $c\in\mathbf R^n$. Drugim riječima, cjelobrojno linearno programiranje problem je koji nastaje kad se problemu linearnog programiranja doda ograničenje da varijable odlučivanja moraju biti cijeli brojevi.

Cjelobrojno ograničenje znatno povećava složenost problema cjelobrojnog programiranja. Mnogi problemi kombinatorne optimizacije, primjerice problem naprtnjače (knapsack), problem zadovoljivosti i brojni optimizacijski problemi iz teorije grafova, mogu se izraziti kao modeli cjelobrojnog programiranja, a za većinu tih problema dokazano je da su NP-teški.

### Totalno unimodularne matrice

Upravo se zato za mnoge velike probleme cjelobrojne optimizacije ponekad razmatra relaksacija cjelobrojnih ograničenja, pa se umjesto toga rješava problem linearnog programiranja. Općenito, optimalna vrijednost relaksiranog linearnog programa samo je donja ocjena optimalne vrijednosti izvornog cjelobrojnog programa (uz pretpostavku da je riječ o problemu minimizacije). Međutim, ako je optimalno rješenje relaksiranog linearnog programa slučajno cjelobrojno, ono je nužno i optimalno rješenje izvornog cjelobrojnog programa.

Prirodno se nameće pitanje postoje li uvjeti koji jamče da su sva optimalna rješenja problema linearnog programiranja cjelobrojna. Pojam totalno unimodularne matrice daje upravo takav uvjet.

???+ abstract "Totalno unimodularna matrica"
    Ako su determinante svih kvadratnih podmatrica matrice $A\in\mathbf R^{m\times n}$ jednake $0$ ili $\pm 1$, matrica $A$ naziva se **totalno unimodularna matrica** (totally unimodular matrix).

Posebno, svi elementi totalno unimodularne matrice jednaki su $0$ ili $\pm 1$. Pomoću pojma totalno unimodularne matrice može se iskazati sljedeći zaključak:

???+ note "Teorem"
    Za totalno unimodularnu matricu $A\in\mathbf Z^{m\times n}$, $b\in\mathbf Z^{m}$ i $c\in\mathbf Z^n$ problem linearnog programiranja i njegov dualni problem
    
    $$
    \min\{c^Tx : Ax=b,x\ge 0\} = \max\{b^Ty: A^Ty\le c\}
    $$
    
    oba imaju cjelobrojna optimalna rješenja čim su oba omeđena.

??? note "Dokaz"
    Ranije je pokazano da se skup optimalnih rješenja problema linearnog programiranja može uzeti kao jedna njegova minimalna strana, a ona je skup rješenja sustava jednadžbi dobivenog izjednačavanjem nekoliko linearno nezavisnih aktivnih ograničenja:
    
    $$
    \{x\in\mathbf R^n : a_j^Tx = b_j,~\forall j\in J\}.
    $$
    
    Označimo taj sustav s $A_Jx=b_J$ i neka je $A_J=(A_1,A_2)$, gdje je $A_1$ kvadratna matrica punog ranga s determinantom $\pm 1$. Tada je prema Cramerovu pravilu rješenje
    
    $$
    x = \begin{pmatrix}A_1^{-1}b_J \\ 0\end{pmatrix}
    $$
    
    jedno cjelobrojno rješenje na toj minimalnoj strani.

Među uobičajenim modelima iz teorije grafova matrice koeficijenata linearnih programa koji odgovaraju mrežnom toku, najkraćim putovima, bipartitnim grafovima itd. totalno su unimodularne. Stoga, čim ti problemi uključuju samo cjelobrojne parametre, njihova se optimalna rješenja mogu uzeti cjelobrojnima, bez bojazni da rješenje linearnog programa odgovara razlomljenom toku, razlomljenom sparivanju i sl. Zato se problemi [maksimalnog toka](../graph/flow/max-flow.md), [minimalnog reza](../graph/flow/min-cut.md), [toka minimalne cijene](../graph/flow/min-cost.md), [najkraćeg puta](../graph/shortest-path.md), [sustava razlika](../graph/diff-constraints.md), [najvećeg (težinskog) sparivanja i najmanjeg vršnog pokrivača u bipartitnom grafu](../graph/graph-matching/bigraph-match.md#oblik-linearnog-programa) itd. svi mogu pretvoriti u probleme linearnog programiranja i tako riješiti. Štoviše, maksimalni tok i minimalni rez, najkraći put i sustavi razlika te najveće sparivanje i najmanji vršni pokrivač u bipartitnom grafu međusobno su dualni problemi.

Osim toga, postoje i uobičajeni modeli iz teorije grafova čija su sva dopustiva rješenja upravo svi vrhovi nekog politopa čiji su vrhovi cjelobrojne točke. Stoga se vještim odabirom ograničenja može postići da rješenje odgovarajućeg problema kombinatorne optimizacije bude upravo optimalno rješenje nekog problema linearnog programiranja. Primjerice, u tu skupinu spadaju modeli poput sparivanja u općem grafu i razapinjućih stabala, pa se i problemi [najvećeg (težinskog) sparivanja u općem grafu](../graph/graph-matching/general-weight-match.md) i [minimalnog razapinjućeg stabla](../graph/mst.md) također mogu pretvoriti u probleme linearnog programiranja.

## Literatura i bilješke

-   Schrijver, Alexander. Theory of linear and integer programming. John Wiley & Sons, 1998.
-   Papadimitriou, Christos H., and Kenneth Steiglitz. Combinatorial optimization: algorithms and complexity. Courier Corporation, 1998.
-   [Duality in linear programming. Part 1—definition and construction. by adamant - Codeforces blog](https://codeforces.com/blog/entry/105049)
-   [Duality in linear programming. Part 2—in competitive programming. by adamant - Codeforces blog](https://codeforces.com/blog/entry/105789)

[^poly-names]: Različita literatura može ta dva pojma definirati različito: neki izvori omeđeni slučaj nazivaju „poliedrom”, a neomeđeni „politopom”; neki ne pretpostavljaju da su to nužno konveksni skupovi; neki „poliedrom” nazivaju politop u trodimenzionalnom prostoru. Ovaj članak koristi definicije usklađene sa Schrijver (1998), Boyd i Vandenberghe (2004) i dr.

[^reducible]: Strože rečeno, oni se međusobno mogu svesti jedan na drugi u polinomnom vremenu.

[^other-methods]: Druge metode za rješavanje sustava nejednadžbi uključuju Fourier–Motzkinovu eliminaciju, Agmon–Motzkin–Schoenbergovu relaksacijsku metodu i dr. One su izravnije, ali često nisu učinkovite.
