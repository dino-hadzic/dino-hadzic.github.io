---
title: Linearna baza
---

Prisjetimo se pojma baznih vektora iz srednjoškolske stereometrije: u trodimenzionalnom euklidskom prostoru možemo pronaći skup baznih vektora $\boldsymbol{i}$, $\boldsymbol{j}$, $\boldsymbol{k}$ pomoću kojih se zatim može prikazati svaki vektor prostora. Drugim riječima, **pomoću konačno mnogo baznih vektora možemo opisati beskonačan trodimenzionalni prostor**, što dovoljno govori o važnosti baznih vektora.

Trodimenzionalni euklidski prostor poseban je [vektorski prostor](./vector-space.md), a bazni vektori trodimenzionalnog euklidskog prostora u vektorskom se prostoru poopćuju u linearnu bazu.

Primjene linearne baze u OI-ju u pravilu uključuju samo dvije vrste vektorskih prostora: $n$-dimenzionalni realni vektorski prostor $\mathbf{R}^n$ i $n$-dimenzionalni vektorski prostor nad [Booleovom domenom](https://en.wikipedia.org/wiki/Boolean_domain) $\mathbf{Z}_2^n$; detaljno ih obrađujemo u odjeljku [Primjene](#primjene). Ako vam linearna algebra nije bliska, preporučujemo da čitanje započnete od odjeljka o primjenama.

U nastavku linearnu bazu uvodimo polazeći od općeg vektorskog prostora i navodimo njezina uobičajena svojstva.

Predznanje: [vektorski prostor](./vector-space.md).

Linearna baza je baza vektorskog prostora i važan je alat za proučavanje vektorskih prostora.

## Definicija

Maksimalan linearno nezavisan podskup vektorskog prostora $V$ nazivamo **Hamelovom bazom** ili **linearnom bazom** prostora $V$, kraće **bazom**.

Dogovorno, baza vektorskog prostora $\{\theta\}$ prazan je skup.

Može se dokazati da svaki vektorski prostor ima linearnu bazu[^existence_basis]; **dimenziju** vektorskog prostora $V$ definiramo kao broj elemenata (ili kardinalnost) linearne baze i označavamo $\dim V$.

## Svojstva

1.  Za konačnodimenzionalan vektorski prostor $V$ dimenzije $n$ vrijedi:

    1.  Bilo kojih $n+1$ vektora iz $V$ linearno je zavisno.

    2.  Bilo kojih $n$ linearno nezavisnih vektora iz $V$ čini bazu prostora $V$.

    3.  Ako se svaki vektor iz $V$ može linearno izraziti pomoću skupa vektora $a_1,a_2,\dots,a_n$, onda je taj skup baza prostora $V$.

        ???+ note "Dokaz"
            Uzmimo bilo koju bazu $b_1,b_2,\dots,b_n$ prostora $V$. Prema pretpostavci, skup vektora $b_1,b_2,\dots,b_n$ može se linearno izraziti pomoću $a_1,a_2,\dots,a_n$, pa je
            
            $$
            n=\operatorname{rank}\{b_1,b_2,\dots,b_n\}\leq\operatorname{rank}\{a_1,a_2,\dots,a_n\}\leq n
            $$
            
            Stoga je $\operatorname{rank}\{a_1,a_2,\dots,a_n\}=n$

    4.  Svaki linearno nezavisan skup vektora $a_1,a_2,\dots,a_m$ iz $V$ može se dodavanjem nekih vektora nadopuniti do baze prostora $V$.

2.  (Formula za dimenziju potprostora) Neka su $V_1,V_2$ konačnodimenzionalni vektorski prostori nad $\Bbb{P}$ te neka su i $V_1+V_2$ i $V_1\cap V_2$ konačnodimenzionalni. Tada je $\dim V_1+\dim V_2=\dim(V_1+V_2)+\dim(V_1\cap V_2)$

    ???+ note "Dokaz"
        Neka je $\dim V_1=n_1$, $\dim V_2=n_2$, $\dim(V_1\cap V_2)=m$.
        
        Uzmimo bazu $a_1,a_2,\dots,a_m$ prostora $V_1\cap V_2$ i nadopunimo je do baze prostora $V_1$ odnosno $V_2$: $a_1,a_2,\dots,a_m,b_1,b_2,\dots,b_{n_1-m}$ i $a_1,a_2,\dots,a_m,c_1,c_2,\dots,c_{n_2-m}$.
        
        Preostaje samo dokazati da je skup vektora $a_1,a_2,\dots,a_m,b_1,b_2,\dots,b_{n_1-m},c_1,c_2,\dots,c_{n_2-m}$ linearno nezavisan.
        
        Neka je $\sum_{i=1}^m r_ia_i+\sum_{i=1}^{n_1-m} s_ib_i+\sum_{i=1}^{n_2-m} t_ic_i=\theta$.
        
        Tada je $\sum_{i=1}^{n_2-m} t_ic_i=-\sum_{i=1}^m r_ia_i-\sum_{i=1}^{n_1-m} s_ib_i$.
        
        Primijetimo da je lijeva strana gornje jednakosti u $V_2$, a desna u $V_1$, pa su obje strane u $V_1\cap V_2$; stoga je $\sum_{i=1}^{n_2-m} t_ic_i=\sum_{i=1}^m k_ia_i$
        
        Odatle je $t_1=t_2=\dots=t_{n_2-m}=k_1=k_2=\dots=k_m=0$, a zatim i $r_1=r_2=\dots=r_m=s_1=s_2=\dots=s_{n_1-m}=t_1=t_2=\dots=t_{n_2-m}=0$

3.  Neka su $V_1,V_2$ konačnodimenzionalni vektorski prostori nad $\Bbb{P}$ te neka su i $V_1+V_2$ i $V_1\cap V_2$ konačnodimenzionalni. Tada su sljedeće tvrdnje ekvivalentne:

    1.  $V_1+V_2=V_1\oplus V_2$.

    2.  $\dim V_1+\dim V_2=\dim(V_1+V_2)$.

    3.  Ako je $a_1,a_2,\dots,a_n$ baza prostora $V_1$, a $b_1,b_2,\dots,b_m$ baza prostora $V_2$, onda je $a_1,a_2,\dots,a_n,b_1,b_2,\dots,b_m$ baza prostora $V_1+V_2$.

    ???+ note "Napomena"
        Tvrdnje 1 i 3 mogu se poopćiti na beskonačnodimenzionalne vektorske prostore.

## Primjeri

Promotrimo baze prostora $\Bbb{R}^2$.

1.  Kao na slici

    ![](./images/basis-1.svg)

    $u,v$ čine bazu.

2.  Kao na slici

    ![](./images/basis-2.svg)

    $u,v$ čine bazu.

3.  Kao na slici

    ![](./images/basis-3.svg)

    $u,v$ ne čine bazu jer je $u=-v$.

4.  Kao na slici

    ![](./images/basis-4.svg)

    $u,v,w$ ne čine bazu jer je $u+4v+6w=\theta$.

## Ortogonalna i ortonormirana baza

Ako baza $B$ vektorskog prostora $V$ zadovoljava $\forall b,b'\in B,~(b,b')\ne 0\iff b=b'$ (tj. vektori su u parovima ortogonalni), tu bazu nazivamo **ortogonalnom bazom**.

Ako ortogonalna baza $B$ vektorskog prostora $V$ k tome zadovoljava $\forall b\in B,~|b|=\sqrt{(b,b)}=1$, tu bazu nazivamo **ortonormiranom bazom**.

Svaka baza konačnodimenzionalnog vektorskog prostora $V$ može se [Gram–Schmidtovim postupkom ortogonalizacije](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process) pretvoriti u ortogonalnu bazu.

## Primjene

Prema prethodno rečenom, pomoću linearne baze možemo:

1.  odrediti rang zadanog skupa vektora;
2.  za zadani skup vektora pronaći maksimalan linearno nezavisan podskup (ili bazu vektorskog prostora koji razapinje);
3.  u zadani skup vektora umetati nove vektore i nakon umetanja pronaći maksimalan linearno nezavisan podskup (ili bazu vektorskog prostora koji razapinje);
4.  za pronađeni maksimalan linearno nezavisan podskup (ili bazu) provjeriti može li se neki vektor linearno izraziti pomoću njega;
5.  za pronađeni maksimalan linearno nezavisan podskup (ili bazu) odrediti posebne elemente vektorskog prostora koji razapinje (npr. najveći, najmanji element itd.).

U OI-ju linearnu bazu u $n$-dimenzionalnom realnom vektorskom prostoru $\mathbf{R}^n$ obično nazivamo **realnom linearnom bazom**, a linearnu bazu u $n$-dimenzionalnom vektorskom prostoru nad Booleovom domenom $\mathbf{Z}_2^n$ **XOR linearnom bazom**.

???+ tip "Savjet"
    U $\mathbf{Z}_2$ zbrajanje je XOR (isključivo ili), a množenje je AND (i); može se dokazati da je $\mathbf{Z}_2$ polje.
    
    Može se dokazati da je algebarska struktura $(\mathbf{Z}_2^n,+,\cdot,\mathbf{Z}_2)$ vektorski prostor, pri čemu je:
    
    $$
    (a_1,\dots,a_n)+(b_1,\dots,b_n):=(a_1+b_1,\dots,a_n+b_n),
    $$
    
    $$
    k\cdot(a_1,\dots,a_n):=(ka_1,\dots,ka_n).
    $$
    
    Dakle, zbrajanje je XOR, a množenje skalarom AND.

Na primjeru XOR linearne baze: iz zadanog skupa Booleovih nizova $X=\{x_1,\dots,x_m\}$ možemo konstruirati XOR linearnu bazu $B=\{b_1,\dots,b_n\}$ sa sljedećim svojstvima:

1.  XOR svakog nepraznog podskupa od $B$ različit je od $0$;
2.  za svaki element $x$ iz $X$ u $B$ se može odabrati nekoliko elemenata čiji je XOR jednak $x$;
3.  svaki skup $B'$ koji zadovoljava prethodna dva svojstva nema manje elemenata od $B$.

Pomoću XOR linearne baze možemo:

1.  provjeriti može li se neki broj prikazati kao XOR nekog podskupa zadanog skupa brojeva;
2.  odrediti broj načina na koje se neki broj može prikazati kao XOR podskupa zadanog skupa brojeva;
3.  odrediti najveći/najmanji/$k$-ti najveći/$k$-ti najmanji XOR podskupa zadanog skupa brojeva;
4.  odrediti rang (poziciju) nekog broja među XOR-ovima podskupova zadanog skupa brojeva.

### Metode konstrukcije

Budući da između XOR linearne baze i realne linearne baze nema bitne razlike, u nastavku kao primjer uzimamo XOR linearnu bazu; za inačicu s realnom linearnom bazom kôd treba samo neznatno izmijeniti.

#### Pohlepna metoda

Svaki broj $p$ izvornog skupa zapišemo binarno i prolazimo od najvišeg bita prema najnižem; za svaki bit $x$ koji je $1$: ako $a_x$ ne postoji, postavimo $a_x \leftarrow p$ i završimo prolaz; ako postoji, postavimo $p\leftarrow p~\text{xor}~a_x$.

Za upit o najvećem $\text{xor}$-u bilo kojih nekoliko elemenata izvornog skupa dovoljno je proći linearnu bazu od najvišeg bita prema najnižem; ako se $\text{xor}$-anjem s trenutačnim $a_x$ odgovor poveća, odgovor XOR-amo s $a_x$.

Zašto to radi? Zato što pri prolasku od viših bitova prema nižima, ako smo trenutačno na $i$-tom bitu, možemo jamčiti da je $i$-ti bit odgovora $1$, a poslije više nema prilike da se $i$-ti bit promijeni.

Najmanji $\text{xor}$ bilo kojih nekoliko elemenata izvornog skupa upravo je najmanji element skupa linearne baze.

Provjera može li se neki broj dobiti kao XOR slična je umetanju: ako se broj $p$ koji umećemo na kraju XOR-anjem svede na $0$, taj se broj može dobiti kao XOR.

??? example "Kôd (Luogu P3812 [【模板】线性基 (Predložak: linearna baza)](https://www.luogu.com.cn/problem/P3812))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_1.cpp"
    ```

#### Gaussova eliminacija

Gaussova eliminacija odgovara konstrukciji linearne baze s gledišta sustava linearnih jednadžbi; ispravnost je očita.

??? example "Kôd (Luogu P3812 [【模板】线性基 (Predložak: linearna baza)](https://www.luogu.com.cn/problem/P3812))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_2.cpp"
    ```

### Svojstva

Linearna baza konstruirana pohlepnom metodom ima sljedeća svojstva:

-   Linearna baza nema podskup čiji je XOR jednak $0$.
-   Brojevi u linearnoj bazi imaju različite najviše (vodeće) bitove u binarnom zapisu.

Linearna baza konstruirana Gaussovom eliminacijom zadovoljava sljedeće svojstvo:

-   Matrica nakon Gaussove eliminacije je u reduciranom ešelonskom obliku (po retcima).

    > Ovo svojstvo obuhvaća oba svojstva linearne baze konstruirane pohlepnom metodom

    Ako vam ispravnost ovog svojstva nije jasna, pogledajte [Gaussova eliminacija](../numerical/gauss.md).

Evo jednog primjera:

```text
5
633 211 169 841 1008
```

Binarni zapis:

```text
1001111001
0011010011
0010101001
1101001001
1111110000
```

Linearna baza dobivena pohlepnom metodom:

```text
1001111001
0100110000
0011010011
0001111010
0000000000
0000010000
0000000000
0000000000
0000000000
0000000000
```

Linearna baza dobivena Gaussovom eliminacijom:

```text
1000000011
0100100000
0010101001
0001101010
0000010000
0000000000
0000000000
0000000000
0000000000
0000000000
```

To je vrlo korisno svojstvo koje nam pomaže da lakše riješimo mnoge zadatke. Na primjer: zadano je nekoliko brojeva, treba odabrati neke od njih i XOR-ati ih tako da XOR bude najveći. Ako linearnu bazu konstruiramo pohlepnom metodom, potrebno je još jednom proći pohlepno: ako je trenutačni bit od `ans` jednak `0`, XOR-anje je sigurno bolje, a ako je trenutačni bit `1`, sigurno nije bolje; ako pak linearnu bazu konstruiramo Gaussovom eliminacijom, dovoljno je izravno XOR-ati sve elemente linearne baze i ispisati rezultat.

I druge klasične zadatke (provjeru može li se broj dobiti kao XOR, pronalaženje $k$-tog najvećeg broja koji se može dobiti kao XOR itd.) linearna baza dobivena Gaussovom eliminacijom rješava lakše.

### Vremenska složenost

Neka je duljina vektora $n$, a njihov ukupan broj $m$. Tada je vremenska složenost $O(nm)$. Gaussova eliminacija ima nešto veću konstantu.

Za realnu linearnu bazu vremenska je složenost $O(n^2m)$.

### Spajanje linearnih baza

Spajanje linearnih baza izvodi se jednostavno grubom silom: elemente jedne od linearnih baza koje spajamo jedan po jedan umećemo u drugu linearnu bazu. Vremenska složenost jednog spajanja je $O(n^2)$ (XOR linearna baza) odnosno $O(n^3)$ (realna linearna baza).

### Presjek linearnih baza

Presjek linearnih baza, strogo govoreći, jest linearna baza presjeka dvaju vektorskih prostora koje te baze razapinju. U ovom odjeljku opisujemo dva algoritma. Vremenska složenost jednog računanja presjeka za oba je algoritma $O(n^2)$ (XOR linearna baza) odnosno $O(n^3)$ (realna linearna baza).

#### Naivni algoritam

Neka su linearne baze čiji presjek tražimo $\alpha$ i $\beta$. Algoritam za presjek linearnih baza dobiva se iz algoritma za spajanje grubom silom sljedećim izmjenama (na primjeru XOR linearne baze):

-   vektore $\beta_j$ linearne baze $\beta$ pokušavamo [pohlepnom metodom](#pohlepna-metoda) umetnuti u $\alpha$, a presjek linearnih baza $\gamma$ inicijaliziramo kao prazan skup;
-   pri umetanju treba za vektor koji umećemo bilježiti doprinos elemenata linearne baze $\beta$. Konkretno, održavamo novi vektor $b$, inicijaliziran na $\beta_j$; ako se vektor koji upravo umećemo XOR-a s vektorom na $x$-toj poziciji linearne baze, onda i doprinos $b$ treba XOR-ati s doprinosom $b_x$ zabilježenim na $x$-toj poziciji;
-   ako umetanje uspije i na $x$-tu poziciju linearne baze umetnemo vektor $\beta_j'$, doprinos $b_x$ zabilježen na $x$-toj poziciji postavimo na doprinos $b$ elemenata linearne baze $\beta$ u postupku kojim je dobiven $\beta_j'$;
-   ako umetanje ne uspije, doprinos $b$ elemenata linearne baze $\beta$ zabilježen tijekom postupka umetnemo u $\gamma$.

Tako dobivena linearna baza $\gamma$ traženi je presjek; dakako, ovaj algoritam istodobno računa i uniju linearnih baza.

??? note "Objašnjenje algoritma"
    Neka je spojena linearna baza $\{\alpha_1,\cdots,\alpha_m,\beta'_{j_1},\cdots,\beta'_{j_\ell}\}$, gdje je $\beta'_{j_k}$ vektor dobiven na kraju umetanja $\beta_{j_k}$. Tada je i $\{\alpha_1,\cdots,\alpha_m,\beta_{j_1},\cdots,\beta_{j_\ell}\}$ linearna baza spojenog prostora. Označimo s $\beta^+$ skup $\{\beta_{j_1},\cdots,\beta_{j_\ell}\}$; spojena se baza tada može zapisati kao $\alpha\cup\beta^+$. Štoviše, svaki vektor $c$ prostora sume može se na jedinstven način prikazati u obliku
    
    $$
    c = a\oplus b
    $$
    
    gdje je $a\in\operatorname{span}\alpha$ i $b\in\operatorname{span}\beta^+$. Član $b$ u ovom rastavu upravo je „doprinos elemenata linearne baze $\beta$” koji algoritam iz prethodnog teksta **pokušava** bilježiti. Strogo govoreći, to je samo doprinos onih vektora iz $\beta$ koji su na kraju uspješno umetnuti.
    
    Za uspješno umetanje, na kraju zabilježeni $b$ upravo je član $b$ tog rastava. Neka je $\beta_j\in\beta^+$. Na početku je $\beta_j=0\oplus\beta_j$, što je već ispravan rastav vektora $\beta_j$ u bazi $\alpha\cup\beta^+$. Kad $\beta'_j=a\oplus b$ ažuriramo u $\beta'_j\oplus c_x$, budući da je $\beta_j'\oplus c_x=(a\oplus a_x)\oplus(b\oplus b_x)$, dovoljno je $b$ ažurirati u $b\oplus b_x$ da bi rastav i dalje bio ispravan. Indukcijom slijedi da je pri konačnom umetanju $\beta'_j$ u spojenu linearnu bazu zabilježeni doprinos $b$ upravo član $b$ gornjeg rastava.
    
    Za neuspješno umetanje, vektor koji umećemo na kraju nužno postaje $0$, a tadašnji doprinos $b$ umeće se u $\gamma$. Ako ponovimo gornje razmatranje, vidjet ćemo da i dalje tijekom umetanja uvijek vrijedi $\beta_j'=a\oplus b$ uz $a\in\operatorname{span}\alpha$, samo što $b$ više ne pripada $\operatorname{span}\beta^+$. Razlog je taj što pri inicijalizaciji $\beta_j=0\oplus\beta_j$ vrijedi $\beta_j\notin\beta^+$. Osim toga, svi članovi koji se pri ažuriranju doprinosa XOR-aju pripadaju $\operatorname{span}\beta^+$. Stoga zapravo vrijedi $b\oplus\beta_j\in\operatorname{span}\beta^+$.
    
    Zašto onda umetanjem svih tih $b$ dobivenih pri neuspješnim umetanjima u $\gamma$ dobivamo linearnu bazu presjeka? Prvo, ako umetanje $\beta_j$ ne uspije, na kraju nužno dobivamo $0=a\oplus b$, gdje je $a\in\operatorname{span}\alpha$ i $b\in\operatorname{span}(\beta^+\cup\{\beta_j\})\subseteq\operatorname{span}\beta$. Stoga $b=a$ nužno leži u presjeku $\operatorname{span}\alpha\cap\operatorname{span}\beta$. Obratno, neka je $c$ bilo koji element presjeka. Budući da je $c\in\operatorname{span}\beta$, $c$ se može prikazati kao linearna kombinacija (XOR) elemenata iz $\beta$:
    
    $$
    c = \bigoplus_{\beta_j\in\beta}\lambda_j\beta_j,
    $$
    
    gdje je $\lambda_j\in\{0,1\}$. Za svaki $\beta_j\notin\beta^+$ označimo s $b_j$ pripadni doprinos umetnut u $\gamma$; tada je
    
    $$
    c\oplus\bigoplus_{\beta_j\notin\beta^+}\lambda_jb_j = \bigoplus_{\beta_j\in\beta^+}\lambda_j\beta_j+\bigoplus_{\beta_j\notin\beta^+}\lambda_j(\beta_j\oplus b_j),
    $$
    
    Primijetimo da $b_j$ i $c$ leže u presjeku, pa i lijeva strana nužno leži u presjeku te se može zapisati kao linearna kombinacija elemenata iz $\alpha$; istodobno, za svaki član desne strane ili je $\beta_j\in\beta^+$, ili je $\beta_j\notin\beta^+$ i $\beta_j\oplus b_j\in\beta^+$, pa je desna strana zapravo linearna kombinacija elemenata iz $\beta^+$. No $\alpha\cup\beta^+$ je linearno nezavisan, pa su svi koeficijenti jednaki $0$, odnosno $c=\bigoplus_{\beta_j\notin\beta^+}\lambda_jb_j\in\operatorname{span}\{b_1,\cdots,b_j\}$. Time je pokazano da doprinosi $b$ vektora koji se nisu mogli umetnuti zajedno razapinju presjek.
    
    Prema ovom objašnjenju, svrha održavanja doprinosa $b$ tijekom postupka zapravo je održavanje rastava $a\oplus b$; štoviše, pri konačnom umetanju doprinosa u $\gamma$ uvijek je $a=b$. Stoga je rezultat ispravan bez obzira na to održavamo li doprinos elemenata iz $\alpha$ ili iz $\beta$ (tj. održavamo li $a$ ili $b$). Ako želimo održavati doprinos elemenata linearne baze $\alpha$, dovoljno je izmijeniti početne vrijednosti doprinosa: svaki vektor $\alpha_i$ iz $\alpha$ na početku ima doprinos $\alpha_i$, a umetnuti $\beta_j$ ima početni doprinos $0$.

Kôd za zadatak-predložak:

??? example "Kôd (Library Checker [Intersection of $\mathbf F_2$ vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_intersect_1.cpp"
    ```

#### Zassenhausov algoritam

Drugi, ekvivalentan postupak jest Zassenhausov algoritam, koji također istodobno računa uniju i presjek dviju linearnih baza. Složenost je potpuno jednaka gore navedenoj.

Konkretni koraci:

-   inicijaliziramo praznu linearnu bazu $\gamma$ vektora duljine $2n$, čije vektore zapisujemo u obliku $(a,b)$, gdje su $a$ i $b$ duljine $n$;
-   elemente $\alpha_i$ iz $\alpha$ umećemo u $\gamma$ u obliku $(\alpha_i,\alpha_i)$;
-   elemente $\beta_j$ iz $\beta$ umećemo u $\gamma$ u obliku $(\beta_j,0)$;
-   među svim elementima $(c_k,d_k)$ različitim od nule u konačnoj linearnoj bazi $\gamma$, komponente $c_k$ onih vektora kod kojih je $c_k$ različit od nule zajedno čine linearnu bazu unije $\alpha$ i $\beta$, a komponente $d_k$ onih vektora kod kojih je $c_k$ jednak nuli zajedno čine linearnu bazu presjeka $\alpha$ i $\beta$.

Metoda konstrukcije linearne baze u algoritmu može biti [pohlepna metoda](#pohlepna-metoda) ili [Gaussova eliminacija](#gaussova-eliminacija); važno je samo da linearna baza u $\gamma$ čini matricu u ešelonskom obliku (po retcima).

Usporedimo li korake eliminacije u Zassenhausovu algoritmu s gornjim naivnim algoritmom, lako uočavamo da Zassenhausov algoritam zasnovan na pohlepnoj metodi odgovara naivnom algoritmu koji održava doprinos elemenata iz $\alpha$. Ako umjesto toga najprije umetnemo sve $(\alpha_i,0)$, a zatim sve $(\beta_j,\beta_j)$, Zassenhausov algoritam zasnovan na pohlepnoj metodi odgovara naivnom algoritmu koji održava doprinos elemenata iz $\beta$. Iz ekvivalentnosti koraka eliminacije slijedi i ispravnost Zassenhausova algoritma.

Osim toga, možemo dati i neovisan, općenitiji algebarski dokaz:

??? note "Dokaz ispravnosti"
    Neka je $V$ vektorski prostor s potprostorima $U=\operatorname{span}\alpha$ i $W=\operatorname{span}\beta$. Sam algoritam odgovara određivanju, svođenjem na ešelonski oblik, baze $\gamma$ potprostora
    
    $$
    H = \operatorname{span}(\{(\alpha_i,\alpha_i):\alpha_i\in\alpha\}\cup\{(\beta_j,0):\beta_j\in\beta\})
    $$
    
    Na kraju algoritma elemente $(c_k,d_k)$ iz $\gamma$ treba podijeliti u dvije klase prema tome je li $c_k\neq 0$, pa promotrimo projekciju $\pi:H\rightarrow V$, $\pi(a,b)=a$. Tada je $\pi(H)=U+W$ i lako se provjerava
    
    $$
    \begin{aligned}
    \ker\pi &= H\cap(\{0\}\times V) = \{0\}\times(U\times W).
    \end{aligned}
    $$
    
    Prema [teoremu o linearnim preslikavanjima](./linear-mapping.md#线性映射的核空间与像空间) vrijedi $\dim H = \dim\pi(H)+\dim\ker\pi = \dim(U+W)+\dim(U\cap W)$.
    
    Prvih nekoliko stupaca matrice u ešelonskom obliku i dalje čini matricu u ešelonskom obliku, pa je broj redaka s $c_k\neq 0$ upravo jednak rangu po retcima skupa $\alpha\cup\beta$, tj. $\dim(U+W)$; štoviše, skup komponenata $c_k$ tih redaka čini bazu prostora $U+W$. Preostalih redaka različitih od nule ima točno $\dim(U\cap W)$ i svi zadovoljavaju $c_k=0$. Za komponente $d_k$ tih redaka vrijedi $(0,d_k)\in\ker\pi$, pa je $d_k\in U\cap W$; k tome su $(0,d_k)$, kao retci matrice u ešelonskom obliku, nužno linearno nezavisni, pa su i ti $d_k$ linearno nezavisni. Sve zajedno, ti $d_k$ čine linearno nezavisan skup veličine $\dim(U\cap W)$ u presjeku $U\cap W$, pa su nužno i baza tog prostora.

Kôd za zadatak-predložak:

??? example "Kôd (Library Checker [Intersection of $\mathbf F_2$ vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_intersect_2.cpp"
    ```

Napomena: pri ispisu dovoljno je razmotriti samo vektore čijih je prvih $n$ bitova jednako nuli.

### Proširenje: prefiksna linearna baza

U ovom odjeljku razmatramo samo slučaj XOR linearne baze te pretpostavljamo da se jedan vektor može pohraniti u $O(1)$ prostora i da je složenost jedne operacije uvijek $O(1)$.

Kad je potrebno više puta odgovoriti na upit o najvećem XOR-u na intervalu, uobičajen je pristup [cat tree](../../ds/cat-tree.md) u kombinaciji s linearnom bazom, vremenske složenosti $O(nm\log m+n^2q)$, gdje je $n$ duljina vektora, $m$ duljina niza, a $q$ broj upita. Drugi mogući pristup jest prefiksna linearna baza (ili linearna baza s vremenskim oznakama), kojom se složenost može smanjiti na $O(n(m+q))$.

Prefiksna linearna baza omogućuje da za svaki prefiks niza održavamo linearne baze svih sufiksa tog prefiksa, čime se podržava upit o linearnoj bazi svakog intervala. Primijetimo da su linearne baze svih sufiksa $[j,i]$ nekog prefiksa $[1,i]$ niza međusobno ugniježđene, tj. linearna baza intervala $[j,i]$ uvijek sadrži linearnu bazu intervala $[j+1,i]$; stoga među linearnim bazama tih sufiksa ima najviše $n$ međusobno različitih, a sve linearne baze sufiksa od $[i,i]$ do $[1,i]$ uvijek se mogu dobiti postupnim dodavanjem novih vektora u prazan skup. Dakle, zahvaljujući toj monotonosti, dovoljno je svaki dodani vektor $v$ označiti najvećim indeksom $t$ na kojem se pojavljuje, pa se linearne baze svih sufiksa mogu pohraniti u $O(n)$ prostora. Štoviše, pri upitu o linearnoj bazi intervala $[j,i]$ dovoljno je u prefiksnoj linearnoj bazi na poziciji $i$ zadržati samo vektore s oznakom $t\ge j$.

Oznaku $t$ vektora $v$ nazovimo njegovom vremenskom oznakom. Vektor $v$ u linearnoj bazi uvijek se može prikazati kao XOR nekih elemenata izvornog niza, npr. $v_{i_1}\oplus v_{i_2}\oplus\cdots\oplus v_{i_k}$. Među svim takvim mogućim prikazima, najveći od najmanjih indeksa upravo je $t$, tj.

$$
t(v) = \max\{j:\exists i_1,\cdots,i_k\in[j,i]\text{ s.t. }v=v_{i_1}\oplus v_{i_2}\oplus\cdots\oplus v_{i_k}\}.
$$

Ovaj izraz samo formalnim jezikom zapisuje ono što je rečeno u prethodnom odlomku. Pouka koju nam daje jest da za održavanje vremenske oznake svakog vektora $v$ u linearnoj bazi treba samo pohlepno birati što novije vektore kojima zamjenjujemo stare.

U odnosu na gore opisanu konstrukciju linearne baze [pohlepnom metodom](#pohlepna-metoda), prefiksna linearna baza u postupku konstrukcije radi sljedeće izmjene:

-   za svaki vektor $a_x$ zadržan u linearnoj bazi čuvamo vremensku oznaku $t_x$, početno postavljenu na $0$;
-   pri dodavanju $i$-tog vektora $v$ niza i dalje prolazimo od viših bitova prema nižima, ali istodobno bilježimo trenutačno vrijeme $i$;
-   ako je $x$-ti bit vektora $v$ jedinica, uspoređujemo vremensku oznaku $t_x$ postojećeg vektora $a_x$ u linearnoj bazi s trenutačnim vremenom $i$:
    -   ako je $i>t_x$, tj. vektor koji dodajemo je noviji, postavimo $a_x$ na $v$, ažuriramo vremensku oznaku na $i$ te postupak dodavanja nastavljamo s rezultatom XOR-a starog $a_x$ i $v$, $a_x\oplus v$, uz prije zabilježeno vrijeme $t_x$;
    -   ako je $i<t_x$, tj. vektor koji dodajemo je stariji, ne ažuriramo $a_x$ ni $t_x$, nego $v$ XOR-amo s $a_x$ i nastavljamo dodavanje.

Drugim riječima, ako se trenutačni bit može prikazati novijim vektorom, izravno koristimo noviji vektor; inače zadržavamo postojeći. Pri ažuriranju vektora na poziciji $x$ ne smijemo rezultat XOR-a $a_x\oplus v$ pohraniti na poziciju $x$, jer je vremenska oznaka rezultata $a_x\oplus v$ jednaka $\min\{t(a_x)=t(v)\}=t(a_x)$, što je manje od vremenske oznake $t(v)$ vektora $v$ koji dodajemo. Iz istog razloga, ažuriranje prema gore u konstrukciji linearne baze [Gaussovom eliminacijom](#gaussova-eliminacija) može narušiti svojstvo vremenskih oznaka, pa ona više nije prikladna za konstrukciju prefiksne linearne baze.

Kôd za zadatak-predložak:

??? example "Kôd (Codeforces [1100F Ivan and Burgers](https://codeforces.com/problemset/problem/1100/F))"
    ```cpp
    --8<-- "docs/math/code/basis/prefix_basis.cpp"
    ```

Ako su upiti online, može se u $O(mn)$ prostora pohraniti prefiksna linearna baza za svaki prefiks i zatim odgovarati na upite; to se može shvatiti kao svojevrsna „perzistentna” linearna baza. Ako su potrebna svojstva linearne baze dobivene Gaussovom eliminacijom, to se može dodatno obraditi pri upitu.

### Zadaci za vježbu

-   [Luogu P3812【模板】线性基 (Predložak: linearna baza)](https://www.luogu.com.cn/problem/P3812)
-   [AcWing 3164. 线性基 (Linearna baza)](https://www.acwing.com/problem/content/description/3167)
-   [SGU 275 to xor or not xor](https://codeforces.com/problemsets/acmsguru/problem/99999/275)
-   [HDU 3949 XOR](https://acm.hdu.edu.cn/showproblem.php?pid=3949)
-   [HDU 6579 Operation](https://acm.hdu.edu.cn/showproblem.php?pid=6579)
-   [Luogu P4151 \[WC2011\] 最大 XOR 和路径 (Put s najvećim XOR-om)](https://www.luogu.com.cn/problem/P4151)
-   [Library Checker - Intersection of $\mathbf F_2$ vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces)
-   [AtCoder Grand Contest 045 A - Xor Battle](https://atcoder.jp/contests/agc045/tasks/agc045_a)
-   [Codeforces 1100F Ivan and Burgers](https://codeforces.com/problemset/problem/1100/F)
-   [Luogu P3292 \[SCOI2016\] 幸运数字 (Sretni brojevi)](https://www.luogu.com.cn/problem/P3292)

## Literatura i bilješke

1.  丘维声，高等代数（下）．清华大学出版社． (Qiu Weisheng, Viša algebra (2. dio). Tsinghua University Press.)
2.  [Basis (linear algebra) - Wikipedia](https://en.wikipedia.org/wiki/Basis_%28linear_algebra%29)
3.  [Vector Basis -- from Wolfram MathWorld](https://mathworld.wolfram.com/VectorBasis.html)
4.  [Zassenhaus algorithm - Wikipedia](https://en.wikipedia.org/wiki/Zassenhaus_algorithm)

[^existence_basis]: [Proof that every vector space has a basis](https://en.wikipedia.org/wiki/Basis_%28linear_algebra%29#Proof_that_every_vector_space_has_a_basis)
