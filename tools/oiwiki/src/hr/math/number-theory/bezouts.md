---
title: Bézoutov teorem i linearne diofantske jednadžbe
---

Bézoutov teorem otkriva duboku vezu između najvećeg zajedničkog djelitelja i cjelobrojnih linearnih kombinacija te je jedan od najosnovnijih i najvažnijih rezultata teorije brojeva. Na temelju njega u ovom tekstu dalje razmatramo rješavanje linearnih diofantskih jednadžbi.

## Bézoutov teorem

**Bézoutov teorem** (Bézout's lemma), poznat i kao Bézoutova lema ili Bézoutov identitet (Bézout's identity), daje nužan i dovoljan uvjet da se cijeli broj može prikazati kao linearna kombinacija dvaju cijelih brojeva s cjelobrojnim koeficijentima.

???+ note "Bézoutov teorem"
    Neka su $a,b$ cijeli brojevi koji nisu oba jednaki nuli. Tada za sve cijele brojeve $x,y$ vrijedi $\gcd(a,b)\mid ax+by$; štoviše, postoje cijeli brojevi $x,y$ takvi da vrijedi $ax+by=\gcd(a,b)$.

??? note "Dokaz"
    Označimo $d=\gcd(a,b)$. Budući da $d\mid a,b$, postoje cijeli brojevi $u,v$ takvi da je $a=du,~b=dv$. Stoga uvijek vrijedi
    
    $$
    ax + by = d(ux+vy).
    $$
    
    To pokazuje da $d\mid ax+by$.
    
    Obratno, treba pokazati da postoje $x,y$ za koje jednakost vrijedi. Budući da je $\gcd(a,b)=\gcd(-a,b)=\gcd(a,-b)$, bez smanjenja općenitosti pretpostavimo da su $a,b$ nenegativni. Ako je jedan od $a,b$ jednak $0$, neka je to $b=0$; tada je njihov najveći zajednički djelitelj $d=a$ i očito $(x,y)=(1,0)$ zadovoljava jednakost. Zatim razmotrimo slučaj kad su $a,b$ oba različita od nule; tada su $a,b$ pozitivni.
    
    Promotrimo tijek Euklidova algoritma:
    
    $$
    \begin{aligned}
    a   &= q_1b   + r_1, && 0\le r_1 < b,\\
    b   &= q_2r_1 + r_2, && 0\le r_2 < r_1,\\
    r_1 &= q_3r_2 + r_3, && 0\le r_3 < r_2,\\
        & \cdots \\
    r_{n-3} &= q_{n-1}r_{n-2} + r_{n-1}, && 0\le r_{n-1} < r_{n-2},\\
    r_{n-2} &= q_nr_{n-1} + r_n,         && 0\le r_n     < r_{n-1},\\
    r_{n-1} &= q_{n+1}r_n.
    \end{aligned}
    $$
    
    Budući da je najveći zajednički djelitelj $d$, u posljednjem koraku Euklidova algoritma nužno je $r_n=d$. Stoga se pretposljednja jednakost može zapisati kao
    
    $$
    d = r_n = r_{n-2} - q_nr_{n-1}.
    $$
    
    Iz pretpretposljednje jednakosti izrazimo
    
    $$
    r_{n-1} = r_{n-3} - q_{n-1}r_{n-2}
    $$
    
    i uvrstimo u prethodni izraz, čime eliminiramo $r_{n-1}$:
    
    $$
    \begin{aligned}
    d &= r_{n-2} - q_n(r_{n-3} - q_{n-1}r_{n-2}) \\
    &= (1 + q_nq_{n-1})r_{n-2} - q_nr_{n-3}.
    \end{aligned}
    $$
    
    Slično redom eliminiramo sve $r_{n-2},r_{n-3},\cdots,r_2,r_1$ i na kraju dobivamo
    
    $$
    d = xa + yb.
    $$
    
    Time je dokazano da postoje $x,y$ za koje vrijedi $ax+by=d$. Prema prethodnoj analizi, time je dokazana i izvorna tvrdnja.

Ovdje je dokaz egzistencije konstruktivan: ujedno daje i način izračuna tih koeficijenata. Taj je način izračuna upravo [prošireni Euklidov algoritam](./gcd.md#prošireni-euklidov-algoritam).

Promotrimo li poseban slučaj Bézoutova teorema kad je $\gcd(a,b)=1$, dobivamo sljedeću posljedicu:

???+ note "Posljedica"
    Cijeli brojevi $a,b$ relativno su prosti ako i samo ako postoje cijeli brojevi $x,y$ takvi da vrijedi $ax+by=1$.

### Slučaj više cijelih brojeva

Bézoutov teorem može se poopćiti na slučaj više cijelih brojeva.

???+ note "Teorem"
    Neka su $a_1,a_2,\cdots,a_n$ cijeli brojevi koji nisu svi jednaki nuli. Tada za sve cijele brojeve $x_1,x_2,\cdots,x_n$ vrijedi $\gcd(a_1,a_2,\cdots,a_n)\mid a_1x_1+a_2x_2+\cdots+a_nx_n$; štoviše, postoje cijeli brojevi $x_1,x_2,\cdots,x_n$ takvi da vrijedi $\gcd(a_1,a_2,\cdots,a_n)=a_1x_1+a_2x_2+\cdots+a_nx_n$.

??? note "Dokaz"
    Dovoljno je iskoristiti $\gcd(a_1,a_2,\cdots,a_n)=\gcd(\gcd(a_1,a_2,\cdots,a_{n-1}),a_n)$ i provesti indukciju po $n$.

### Primjer zadatka

???+ example "[Codeforces 510 D. Fox And Jumping](https://codeforces.com/problemset/problem/510/D)"
    Zadano je $n\le 300$ kartica, svaka s vrijednostima $l_i$ i $c_i$. Na beskonačno dugoj vrpci možete platiti $c_i$ novca za kupnju kartice $i$, nakon čega smijete proizvoljno mnogo puta skočiti $l_i$ jedinica ulijevo ili udesno. Pitanje je koliko najmanje novca treba potrošiti da biste mogli skočiti na svaki položaj na vrpci. Ako to nije moguće, ispišite $-1$.

??? note "Rješenje"
    Analizirajući zadatak, uočavamo da, želimo li doskočiti na svako polje, odabrani brojevi $l_{i_1}, \cdots, l_{i_k}$ moraju se nekoliko puta zbrajanjem ili oduzimanjem moći kombinirati u apsolutnu vrijednost $1$. Drugim riječima, postoje cijeli brojevi $x_1, \cdots, x_k$ takvi da je $l_{i_1} x_1 + \cdots + l_{i_k} x_k = 1$. Prema Bézoutovu teoremu za više cijelih brojeva, to je ekvivalentno odabiru nekoliko brojeva iz niza $l_1, \cdots, l_n$ čiji je najveći zajednički djelitelj $1$, uz zahtjev da zbroj cijena bude minimalan.
    
    **Rješenje 1**: minimalni zbroj cijena promatramo kao problem najkraćeg puta koji se može riješiti Dijkstrinim algoritmom. U vrhovima grafa pohranjena je trenutačna vrijednost najvećeg zajedničkog djelitelja. Početni je vrh grafa $0$, a ciljni vrh $1$. U svakom koraku iz trenutačnog vrha $x$ bridom duljine $c_i$ prelazimo u vrh $\gcd(x,l_i)$. Vremenska složenost ovog algoritma jest $O(n^2\log n)$.
    
    **Rješenje 2**: iz niza $l_1, \cdots, l_n$ biramo nekoliko brojeva čiji je najveći zajednički djelitelj $1$ uz minimalan zbroj cijena, što podsjeća na 0-1 problem naprtnjače.
    
    Neka $f_{i, j}$ označava minimalnu cijenu uz razmatranje prvih $i$ brojeva i najveći zajednički djelitelj $j$; tada imamo prijelaz:
    
    $$
    f_{i, j} = \min\left\{f_{i - 1, j},~\min_{\gcd(k, l_i) = j}\{f_{i - 1, k} + c_i\}\right\}.
    $$
    
    Nakon DP-a ukupna je konačna cijena $f_{n, 1}$.
    
    Kao i kod običnog 0-1 problema naprtnjače, može se optimizirati kružnim poljem (rolling array) i ukloniti prva dimenzija. Osim toga, najveći zajednički djelitelji $j$ koje može dati 300 brojeva vrlo su rijetki, pa se mogu pohraniti u hash-tablici.
    
    Zapravo, graf izgrađen u rješenju 1 upravo je graf prijelaza stanja dinamičkog programiranja u rješenju 2; rješenje 2 odgovara traženju najkraćeg puta u usmjerenom acikličkom grafu dinamičkim programiranjem, pa su rješenja 1 i 2 ekvivalentna. No rješenje 2 ne treba pohraniti cijeli graf, a vremenska složenost DP-a iznosi $O(n + m)$ (gdje je $m$ broj bridova grafa prijelaza stanja), što je manje nego kod Dijkstrina algoritma; zato je rješenje 2 bolje i vremenski i prostorno.

## Linearne diofantske jednadžbe

**Linearna diofantska jednadžba** (linear Diophantine equation) jest diofantska jednadžba oblika

$$
a_1x_1 + a_2x_2 + \cdots + a_nx_n = b
$$

gdje su $a_1,a_2,\cdots,a_n$ cijeli brojevi. Cilj je ovog odjeljka pronaći sva njezina cjelobrojna rješenja.

### Slučaj dviju varijabli

Najprije razmotrimo linearnu diofantsku jednadžbu s dvije nepoznanice:

$$
a_1x_1 + a_2x_2 = b.
$$

Bézoutov teorem kaže da ova jednadžba ima rješenje ako i samo ako

$$
d = \gcd(a_1,a_2) \mid b.
$$

Pretpostavimo u nastavku da je taj uvjet ispunjen. Proširenim Euklidovim algoritmom možemo pronaći jedno cjelobrojno rješenje $(x_1^*,x_2^*)$ jednadžbe $a_1x_1 + a_2x_2 = d$. Iz njega dobivamo jedno partikularno rješenje izvorne jednadžbe

$$
(x_1^\circ,x_2^\circ) = \left(\frac{b}{d}x_1^*,\frac{b}{d}x_2^*\right).
$$

Da bismo dobili sva rješenja, oduzmimo od izvorne jednadžbe identitet $a_1x_1^\circ+a_2x_2^\circ = b$; dobivamo

$$
a_1(x_1 - x_1^\circ) + a_2(x_2 - x_2^\circ) = 0.
$$

To je homogena linearna diofantska jednadžba u $(x_1-x_1^\circ,x_2-x_2^\circ)$ čije je opće rješenje

$$
(x_1-x_1^\circ,x_2-x_2^\circ) = \left(t\dfrac{a_2}{d},-t\dfrac{a_1}{d}\right).\quad(t\in\mathbf Z)
$$

Stoga je opće rješenje izvorne jednadžbe

$$
(x_1,x_2) = \left(x_1^\circ + t\dfrac{a_2}{d},x_2^\circ - t\dfrac{a_1}{d}\right).\quad(t\in\mathbf Z)
$$

To je niz jednako razmaknutih cjelobrojnih točaka na pravcu $a_1x_1+a_2x_2 = b$.

### Slučaj više varijabli

Kad je riješen slučaj dviju varijabli, slučaj više varijabli lako se rješava. Za linearnu diofantsku jednadžbu s $n$ nepoznanica

$$
a_1x_1 + a_2x_2 + \cdots + a_nx_n = b,\quad (n>2)
$$

prema Bézoutovu teoremu jednadžba ima rješenje ako i samo ako

$$
\gcd(a_1,a_2,\cdots,a_n) \mid b.
$$

Slično slučaju dviju varijabli, opće rješenje linearne diofantske jednadžbe s više varijabli također se može zapisati u obliku

$$
(x_1^\circ,x_2^\circ,\cdots,x_n^\circ) + \sum_{k=1}^{n-1} t_k(x_1^{(k)},x_2^{(k)},\cdots,x_n^{(k)})
$$

gdje je $x^\circ$ jedno partikularno rješenje, a $x^{(k)}$ su $(n-1)$ linearno nezavisnih rješenja pripadne homogene jednadžbe.

Konkretan oblik općeg rješenja može se dobiti svođenjem jednadžbe s $n$ nepoznanica na jednadžbu s $(n-1)$ nepoznanica. Označimo $d_1 = \gcd(a_1,a_2)$; tada su, prema Bézoutovu teoremu, sve vrijednosti $a_1x_1+a_2x_2$ upravo svi višekratnici broja $d_1$. Stoga najprije možemo riješiti linearnu diofantsku jednadžbu s $(n-1)$ nepoznanica:

$$
d_1y_1 + a_3x_3 + a_4x_4 + \cdots + a_nx_n = b.
$$

Neka je njezino dobiveno opće rješenje

$$
\begin{aligned}
y_1 &= y_1^\circ + \sum_{k=2}^{n-1}t_ky_1^{(k)}, \\
x_i &= x_i^\circ + \sum_{k=2}^{n-1}t_kx_i^{(k)},\quad i=3,\cdots,n.
\end{aligned}
$$

Neka je $(x_1^*,x_2^*)$ jedno partikularno rješenje jednadžbe $a_1x_1+a_2x_2=d_1$; tada je, prema raspravi iz prethodnog odjeljka, opće rješenje linearne diofantske jednadžbe $a_1x_1+a_2x_2=d_1y_1$ u nepoznanicama $x_1,x_2$ jednako

$$
x_1 = x_1^*y_1 + t_1\dfrac{a_2}{d_1},~x_2 = x_2^*y_1 - t_1\dfrac{a_1}{d_1}.
$$

Uvrštavanjem izraza za $y_1$ dobivamo opće rješenje izvorne jednadžbe

$$
\begin{aligned}
x_1 &= x_1^*y_1^\circ + t_1\dfrac{a_2}{d_1} + \sum_{k=2}^{n-1}t_kx_1^*y_1^{(k)}, \\
x_2 &= x_2^*y_1^\circ - t_1\dfrac{a_1}{d_1} + \sum_{k=2}^{n-1}t_kx_2^*y_1^{(k)}, \\
x_i &= x_i^\circ + \sum_{k=2}^{n-1}t_kx_i^{(k)},\quad i=3,\cdots,n.
\end{aligned}
$$

## Frobeniusov problem novčića

Bézoutov teorem daje nužan i dovoljan uvjet da se cijeli broj može linearno izraziti pomoću nekoliko cijelih brojeva. S tim je usko povezan **Frobeniusov problem novčića** (Frobenius coin problem):

-   Ako novčići imaju nekoliko cjelobrojnih vrijednosti $a_1,a_2,\cdots,a_n$ i vrijedi $\gcd(a_1,a_2,\cdots,a_n)=1$, koji je najveći cijeli broj koji se ne može složiti od tih novčića?

I ovdje se pitamo kada se cijeli broj $k$ može prikazati u obliku $a_1x_1+a_2x_2+\cdots+a_nx_n$; u Bézoutovu teoremu $x_i$ smiju biti bilo koji cijeli brojevi, dok u Frobeniusovu problemu novčića $x_i$ smiju biti samo prirodni brojevi (uključujući nulu).

Slučaj s jednom vrstom novčića trivijalan je, jer tada mora biti $a_1=1$ i svi se prirodni brojevi mogu njime prikazati. Slučaj $n>2$ pak je presložen, pa u ovom odjeljku razmatramo samo slučaj $n=2$.

### Sylvesterov teorem

Godine 1882. Sylvester je u potpunosti riješio Frobeniusov problem novčića za $n = 2$:

???+ note "Teorem (Sylvester)"
    Za relativno proste prirodne brojeve $a_1,a_2$ najveći cijeli broj koji se ne može zapisati u obliku $a_1x_1+a_2x_2~(x_1,x_2\in\mathbf N)$ jest $C = a_1a_2 - a_1 - a_2$. Štoviše, za svaki $k\in\mathbf Z$ točno jedan od cijelih brojeva $k$ i $C-k$ može se zapisati u tom obliku.

Radi jednostavnosti izražavanja, cijele brojeve koji se mogu zapisati u obliku $a_1x_1+a_2x_2~(x_1,x_2\in\mathbf N)$ nazivamo **prikazivima**.

??? note "Dokaz 1"
    Budući da su $a_1,a_2$ relativno prosti, za svaki cijeli broj $k$ jednadžba $a_1x_1+a_2x_2=k$ sigurno ima rješenje, a opće je rješenje
    
    $$
    (x_1,x_2) = (x_1^\circ + ta_2, x_2^\circ - ta_1).\quad(t\in\mathbf Z)
    $$
    
    Uzmimo za $t$ kvocijent pri dijeljenju s ostatkom broja $x_2^\circ$ brojem $a_1$; tada je ostatak $x_2 = x_2^\circ-ta_1$ između $0$ i $a_1-1$. Promotrimo tako dobiveno rješenje $(x_1,x_2)$. Budući da je $x_2$ najmanja nenegativna cjelobrojna vrijednost koju može poprimiti, $k$ je prikaziv ako i samo ako je $x_1\ge 0$.
    
    **Prvi korak**: dokazujemo da su svi cijeli brojevi veći od $C$ prikazivi.
    
    Kad je $k > C$, vrijedi
    
    $$
    a_1x_1 = k - a_2x_2 > C - a_2(a_1-1) = -a_1.
    $$
    
    Stoga je $x_1 > -1$, tj. $x_1\ge 0$. To znači da je $(x_1,x_2)$ rješenje u prirodnim brojevima. Tada se $k$ može zapisati u traženom obliku.
    
    **Drugi korak**: dokazujemo da $C$ nije prikaziv. Slijedi da je $C$ najveći neprikazivi cijeli broj te da $k$ i $C-k$ nisu oba prikaziva.
    
    Dokaz kontradikcijom. Pretpostavimo da je $C$ prikaziv, tj. da postoje $x_1,x_2\in\mathbf N$ takvi da je $a_1x_1+a_2x_2=C$. Uvrštavanjem izraza za $C$ dobivamo
    
    $$
    a_1a_2 = a_1(x_1+1) + a_2(x_2+1).
    $$
    
    Stoga $a_2\mid (x_1+1)$ i $a_1\mid (x_2+1)$. Budući da su $x_1+1,x_2+1$ pozitivni, vrijedi
    
    $$
    a_1a_2 \ge a_1a_2 + a_2a_1 = 2a_1a_2.
    $$
    
    Kontradikcija. Dakle, $C$ nije prikaziv. Zajedno s prvim korakom, on je najveći neprikazivi cijeli broj.
    
    Kad bi $k$ i $C-k$ oba bili prikazivi, zbrajanjem koeficijenata iz prikaza brojeva $k$ i $C-k$ dobili bismo koeficijente prikaza broja $C$, što je u suprotnosti s neprikazivošću broja $C$; stoga je najviše jedan od $k$ i $C-k$ prikaziv.
    
    **Treći korak**: dokazujemo da je, ako $k$ nije prikaziv, $C-k$ sigurno prikaziv.
    
    Neka je $(x_1,x_2)$ gore opisano cjelobrojno rješenje jednadžbe $a_1x_1+a_2x_2=k$. Već smo pokazali da je neprikazivost broja $k$ ekvivalentna uvjetu $x_1<0$. Stoga vrijedi
    
    $$
    C - k = a_1a_2 - a_1 - a_2 - a_1x_1 - a_2x_2 = a_1(-1-x_1) + a_2(a_1-1-x_2).
    $$
    
    Ovdje su $-1-x_1$ i $a_1-1-x_2$ nenegativni cijeli brojevi, pa je $C-k$ prikaziv.

??? note "Dokaz 2"
    Ovdje dokazujemo samo da je $C=a_1a_2-a_1-a_2$ najveći neprikazivi cijeli broj; ostatak dokaza sličan je dokazu 1.
    
    Promotrimo, modulo $a_2$, najmanji prikazivi prirodni broj u svakoj klasi ostataka. Budući da se različiti prirodni brojevi iz iste klase ostataka mogu jedan u drugi pretvoriti dodavanjem ili oduzimanjem nekoliko $a_2$, pri razmatranju najmanjeg prikazivog broja dovoljno je uzeti u obzir samo mogućnost dodavanja ili oduzimanja $a_1$. Budući da su $a_1$ i $a_2$ relativno prosti, najmanji prikazivi prirodni brojevi u pojedinim klasama ostataka upravo su višekratnici broja $a_1$
    
    $$
    0,~a_1,~2a_1,~\cdots,~(a_2-1)a_1.
    $$
    
    Stoga je najveći neprikazivi broj
    
    $$
    \max_{0\le i < a_2} ia_1 - a_2 = (a_2-1)a_1 - a_2 = C.
    $$

### Geometrijsko značenje

Promatrajmo jednadžbu $a_1x_1 + a_2x_2 = k$ kao pravac. Tada je $k$ prikaziv ako i samo ako taj pravac u prvom kvadrantu (uključujući koordinatne osi) prolazi kroz barem jednu cjelobrojnu točku. Kad je $k < a_1a_2$, taj pravac u prvom kvadrantu prolazi kroz najviše jednu cjelobrojnu točku. Stoga je za $0\le k < a_1a_2$ cijeli broj $k$ prikaziv ako i samo ako taj pravac u prvom kvadrantu prolazi kroz točno jednu cjelobrojnu točku.

Prema tome, za $k < a_1a_2$ broj prikazivih prirodnih brojeva manjih ili jednakih $k$ točno je jednak broju cjelobrojnih točaka u prvom kvadrantu ispod pravca $a_1x_1 + a_2x_2 = k$ (uključujući točke na rubu). Taj je broj jednak

$$
\sum_{i=0}^{\lfloor k / a_1 \rfloor} \left(\left\lfloor\dfrac{k-ia_1}{a_2}\right\rfloor+1\right).
$$

To je klasični problem cjelobrojnih točaka ispod pravca, koji se [algoritmom nalik Euklidovu](./euclidean.md#algoritam-nalik-euklidovu) može riješiti u vremenu $O(\log\min\{a_1,a_2,k\})$.

### Zadatci

-   [Luogu P3951 NOIP2017 提高组 小凯的疑惑/蓝桥杯 2013 省 买不到的数目 (NOIP 2017, napredna skupina, Xiao Kaijeva nedoumica / Lanqiao Cup 2013, pokrajinsko natjecanje, Iznos koji se ne može platiti)](https://www.luogu.com.cn/problem/P3951)
