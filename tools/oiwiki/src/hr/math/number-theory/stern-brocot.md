---
title: Stern–Brocotovo stablo i Fareyev niz
---

## Uvod

Ovaj članak predstavlja strukturu podataka za pohranu neskrativih razlomaka i druge srodne pojmove. Oni su usko povezani s [verižnim razlomcima](./continued-fraction.md), na algoritamskim natjecanjima mogu poslužiti za rješavanje niza problema iz teorije brojeva, a mogu se pojaviti i kao skrivena pozadina nekih zadataka.

## Stern–Brocotovo stablo

Stern–Brocotovo stablo elegantna je struktura za održavanje razlomaka koja sadrži sve različite pozitivne racionalne brojeve. Tu su strukturu neovisno otkrili Moritz Stern 1858. godine i Achille Brocot 1861. godine.

### Konstrukcija

#### Konstrukcija po razinama

Stern–Brocotovo stablo može se dobiti iterativnom konstrukcijom Stern–Brocotova niza $k$-tog reda (Stern–Brocot sequence of order $k$). Stern–Brocotov niz $0$-tog reda sastoji se od dvaju jednostavnih razlomaka:

$$
\frac{0}{1},\ \frac{1}{0}.
$$

Ovdje $\dfrac{1}{0}$, strogo govoreći, nije racionalan razlomak; može se shvatiti kao neskrativi razlomak koji predstavlja $\infty$.

Ako između svakih dvaju susjednih razlomaka $\dfrac{a}{b}$ i $\dfrac{c}{d}$ Stern–Brocotova niza $k$-tog reda umetnemo njihovu medijantu (mediant)[^mediant] $\dfrac{a+c}{b+d}$, dobivamo Stern–Brocotov niz reda $k+1$. Iako sama definicija medijante dopušta skraćivanje razlomka, u konstrukciji Stern–Brocotova stabla dovoljno je jednostavno zbrojiti brojnike i nazivnike, bez brige o skraćivanju. Tako se iterativno mogu konstruirati Stern–Brocotovi nizovi svih redova. Rezultati prvih nekoliko iteracija su sljedeći:

$$
\begin{array}{ccccccccc}
&&&\dfrac{0}{1}, & \dfrac{1}{1}, & \dfrac{1}{0} &&&\\\\
&&\dfrac{0}{1}, & \dfrac{1}{2}, & \dfrac{1}{1}, & \dfrac{2}{1}, & \dfrac{1}{0} &&\\\\
\dfrac{0}{1}, & \dfrac{1}{3}, & \dfrac{1}{2}, & \dfrac{2}{3}, & \dfrac{1}{1}, & \dfrac{3}{2}, & \dfrac{2}{1}, & \dfrac{3}{1}, & \dfrac{1}{0}
\end{array}
$$

Ako razlomke dodane u svakoj iteraciji povežemo u strukturu stabla, dobivamo Stern–Brocotovo stablo, kao na slici:

![](./images/stern-brocot-tree.svg)

Stern–Brocotov niz $k$-tog reda, bez lijeve i desne krajnje točke, upravo je inorder obilazak Stern–Brocotova stabla dubine $k-1$.

#### Konstrukcija trojkama

Drugi, ekvivalentan način konstrukcije jest da se trojka

$$
\left(\dfrac{0}{1},\dfrac{1}{1},\dfrac{1}{0}\right)
$$

uzme za korijen, a svakom čvoru

$$
\left(\dfrac{a}{b},\dfrac{p}{q},\dfrac{c}{d}\right)
$$

dodaju

$$
\left(\dfrac{a}{b},\dfrac{a+p}{b+q},\dfrac{p}{q}\right),\ \left(\dfrac{p}{q},\dfrac{p+c}{q+d},\dfrac{c}{d}\right)
$$

kao lijevo odnosno desno dijete; tako se konstruira cijelo Stern–Brocotovo stablo. U trojci zapisanoj u svakom čvoru Stern–Brocotova stabla stvarno pohranjeni razlomak je srednji razlomak trojke $\dfrac{p}{q}$, dok su lijevi i desni razlomak $\dfrac{a}{b}$ i $\dfrac{c}{d}$ razlomci koji su se pojavili ranije. Štoviše, ako razmotrimo prethodnu konstrukciju, vidimo da je razlomak $\dfrac{p}{q}$ upravo dobiven umetanjem medijante razlomaka $\dfrac{a}{b}$ i $\dfrac{c}{d}$.

#### Matrični prikaz i Stern–Brocotov brojevni sustav

Konstrukcija trojkama znači da svakom čvoru Stern–Brocotova stabla odgovara matrica

$$
S = \begin{pmatrix}
b & d\\
a & c
\end{pmatrix}.
$$

Korijen Stern–Brocotova stabla je jedinična matrica $I$, a prelazak u lijevo dijete odnosno desno dijete odgovara množenju matrice trenutačnog čvora s desne strane matricom

$$
L=\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix},~
R=\begin{pmatrix}
1 & 0 \\
1 & 1
\end{pmatrix}.
$$

Razlomak koji stvarno odgovara svakom čvoru je $f(S)=\dfrac{a+c}{b+d}$. Matrica $S$ svakog čvora može se zapisati kao umnožak niza matrica $L$ i $R$, što se može shvatiti i kao niz znakova sastavljen od $L$ i $R$ koji predstavlja put od korijena do tog čvora. Time se svi pozitivni racionalni brojevi jednoznačno prikazuju takvim nizovima znakova, što se može smatrati jednim prikazom pozitivnih racionalnih brojeva, pa se stoga naziva i **Stern–Brocotov brojevni sustav** (Stern–Brocot number system).

#### Implementacija izgradnje stabla

Algoritam izgradnje stabla samo simulira gore opisani postupak. Slijedi kôd koji obavlja inorder obilazak prvih $n$ razina Stern–Brocotova stabla.

???+ example "Izgradnja stabla"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/stern-brocot/tree-build.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/stern-brocot/tree-build.py:core"
        ```

Složenost algoritma izgradnje stabla je $O(2^n)$.

### Svojstva

Sada raspravljamo o svojstvima Stern–Brocotova stabla. Ukratko, Stern–Brocotovo stablo je [binarno stablo pretraživanja](../../ds/bst.md) koje sadrži sve pozitivne neskrative racionalne razlomke; ono je ujedno [heap](../../ds/binary-heap.md) po brojnicima i po nazivnicima, kao i [Kartezijevo stablo](../../ds/cartesian-tree.md) parova (nazivnik, brojnik). Ako razmotrimo intervale koje tvore lijeva i desna krajnja točka u ranije opisanoj konstrukciji trojkama, Stern–Brocotovo stablo može se promatrati i kao [segment tree](../../ds/seg.md) nad $[0,\infty]$. Te se tvrdnje mogu izvesti iz sljedećih triju osnovnih svojstava:

#### Monotonost

U gornjoj konstrukciji razlomci su na svakoj razini strogo rastući. To se dokazuje indukcijom. Naime, ako je $\dfrac{a}{b} < \dfrac{c}{d}$, nužno vrijedi

$$
\dfrac{a}{b} < \dfrac{a+c}{b+d} < \dfrac{c}{d}.
$$

To se dobiva uklanjanjem nazivnika iz nejednakosti. Baza indukcije je $\dfrac{0}{1} < \dfrac{1}{0}$, pa monotonost očito vrijedi.

#### Neskrativost

U gornjoj konstrukciji svaki je razlomak neskrativ. Za to također treba indukcijom dokazati da u gornjoj konstrukciji svaka dva susjedna razlomka $\dfrac{a}{b}$ i $\dfrac{c}{d}$ na istoj razini zadovoljavaju jednakost

$$
bc-ad = \det\begin{pmatrix}
b & d\\
a & c
\end{pmatrix} = 1.
$$

U korijenu je jedinična matrica, pa to očito vrijedi. Pri spuštanju množimo matricama $L$ i $R$ čije su determinante jednake $1$, pa prema svojstvima [determinante](../linear-algebra/determinant.md) na sljedećoj razini jednako vrijedi

$$
\det\begin{pmatrix}b & b+d \\ a & a+c \end{pmatrix} = \det\begin{pmatrix}b+d & d \\ a+c & c\end{pmatrix} = 1.
$$

Za bazu indukcije $\dfrac{0}{1}$ i $\dfrac{1}{0}$ to je također očito. Iz toga, prema [Bézoutovu teoremu](./bezouts.md), nužno slijedi da su brojnik i nazivnik svakog razlomka relativno prosti, tj. svi su razlomci neskrativi.

#### Potpunost

Naposljetku, treba pokazati da Stern–Brocotovo stablo sadrži sve pozitivne neskrative razlomke. Budući da prva dva svojstva već pokazuju da je Stern–Brocotovo stablo binarno stablo pretraživanja, a svaki pozitivni neskrativi razlomak $\dfrac{p}{q}$ nužno leži između $\dfrac{0}{1}$ i $\dfrac{1}{0}$, prema načinu pretraživanja u binarnom stablu pretraživanja jedina mogućnost da $\dfrac{p}{q}$ nema u stablu jest da je postupak pretraživanja beskonačno dug. Dokazat ćemo da je za svaki pozitivni racionalni broj $\dfrac{p}{q}$ beskonačno dug postupak pretraživanja nemoguć.

Neka je donja granica za $\dfrac{p}{q}$ dobivena tijekom pretraživanja $\dfrac{a}{b}$, a gornja granica $\dfrac{c}{d}$. Početna vrijednost donje granice je $\dfrac{0}{1}$, početna vrijednost gornje granice je $\dfrac{1}{0}$, a zatim se granice postupno prilagođavaju prema rezultatu usporedbe $\dfrac{a+c}{b+d}$ i $\dfrac{p}{q}$. Ako je postupak pretraživanja beskonačno dug, u svakom koraku vrijedi

$$
\dfrac{a}{b} < \dfrac{p}{q} < \dfrac{c}{d},
$$

pa u beskonačno mnogo koraka nužno vrijedi

$$
bp-aq \ge 1,\ cq-dp \ge 1.
$$

Pomnožimo li te dvije nejednakosti redom s $(c+d)$ i $(a+b)$, dobivamo

$$
(c+d)(bp-aq) + (a+b)(cq-dp) \ge a+b+c+d.
$$

Pomoću ranije pokazane jednakosti $bc-ad=1$ gornji se izraz pojednostavnjuje u

$$
p+q \ge a+b+c+d.
$$

Međutim, svaki put kad pretraživanje siđe jednu razinu dublje, desna strana nejednakosti strogo raste, a lijeva ostaje ista, pa gornji uvjet ne može vrijediti u beskonačno mnogo koraka. Stoga se postupak pretraživanja zaustavlja u konačno mnogo koraka.

### Traženje razlomka

U praktičnoj primjeni Stern–Brocotova stabla često treba odrediti položaj zadanog razlomka u Stern–Brocotovu stablu.

#### Naivni algoritam

Budući da je Stern–Brocotovo stablo binarno stablo pretraživanja, dovoljno je usporediti trenutačni razlomak s traženim razlomkom da bi se odredio put od korijena do zadanog razlomka. Ako prelazak u lijevo dijete odnosno desno dijete na putu označimo s $L$ odnosno $R$, svakom putu odgovara niz znakova sastavljen od $L$ i $R$, a to je upravo ranije spomenuti prikaz racionalnog broja u Stern–Brocotovu brojevnom sustavu. Određivanje puta do nekog racionalnog broja istovjetno je određivanju prikaza tog racionalnog broja u Stern–Brocotovu brojevnom sustavu.

Implementacija naivnog algoritma traženja razlomka izgleda ovako:

???+ example "Naivno traženje razlomka"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/stern-brocot/fraction-finding-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/stern-brocot/fraction-finding-1.py:core"
        ```

Složenost algoritma je $O(p+q)$, pa na algoritamskim natjecanjima nije praktičan.

U Stern–Brocotovu brojevnom sustavu svakom pozitivnom iracionalnom broju odgovara jedinstven beskonačno dug niz znakova. Isti algoritam može se upotrijebiti za konstrukciju tog niza. Svakom prefiksu tog beskonačnog niza odgovara neki racionalni neskrativi razlomak. Poredamo li te neskrative razlomke u niz, nazivnici razlomaka u nizu strogo rastu, a limes niza je taj iracionalni broj. Stoga se Stern–Brocotovo stablo može upotrijebiti za nalaženje racionalne aproksimacije nekog iracionalnog broja s proizvoljnom točnošću. Treba, međutim, imati na umu da razlika između tog niza racionalnih brojeva i iracionalnog broja nije strogo padajuća. Za strogu teoriju racionalnih aproksimacija vidi odjeljak [Diofantske aproksimacije](./continued-fraction.md#diofantska-aproksimacija) na stranici o verižnim razlomcima. Kad se Stern–Brocotovo stablo u praksi koristi za nalaženje najbolje aproksimacije nekog realnog broja s nazivnikom koji ne prelazi zadanu granicu, na kraju treba usporediti udaljenosti lijeve i desne krajnje točke intervala od tog realnog broja.

#### Brzi algoritam

Naivni algoritam traženja razlomka nije učinkovit, ali jednostavnom optimizacijom dobiva se brzi algoritam traženja složenosti $O(\log(p+q))$. Ključ optimizacije je zajednička obrada uzastopnih $L$ odnosno $R$.

Ako traženi razlomak $\dfrac{p}{q}$ pada između $\dfrac{a}{b}$ i $\dfrac{c}{d}$, tada pri $t$ uzastopnih pomaka udesno desna granica ostaje nepomična, a lijeva se granica pomiče u $\dfrac{a+tc}{b+td}$; obrnuto, pri $t$ uzastopnih pomaka ulijevo lijeva granica ostaje nepomična, a desna se granica pomiče u $\dfrac{ta+c}{tb+d}$. Stoga se broj pomaka udesno odnosno ulijevo može odrediti izravno pomoću $\dfrac{a+tc}{b+td}<\dfrac{p}{q}$ odnosno $\dfrac{p}{q}<\dfrac{ta+c}{tb+d}$. Ovdje se uzima stroga nejednakost jer algoritam pomiče lijevu i desnu krajnju točku, a traženi se razlomak pojavljuje kao medijanta konačno dobivenih krajnjih točaka.

???+ example "Brzo traženje razlomka"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/stern-brocot/fraction-finding-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/stern-brocot/fraction-finding-2.py:core"
        ```

Ovaj algoritam traženja zahtijeva da je razlomak $\dfrac{p}{q}$ poznat. Ako ciljni razlomak nije poznat, često je pri svakom pomaku udesno ili ulijevo potrebno broj pomaka tražiti udvostručavanjem (binary lifting) ili binarnim pretraživanjem. Tada je složenost algoritma traženja razlomka $O(\log^2(p+q))$.

#### Algoritam temeljen na verižnim razlomcima

Za slučaj kad je razlomak poznat, pomoću verižnih razlomaka može se dati još jednostavniji algoritam. Bez smanjenja općenitosti pretpostavimo da je prva skupina pomaka udesno; ako nije, neka broj pomaka u prvoj skupini pomaka udesno bude nula. Krajnje točke pomičemo naizmjence udesno i ulijevo, a položaje krajnjih točaka nakon svake skupine pomaka poredamo ovako:

$$
\dfrac{p_0}{q_0},~\dfrac{p_1}{q_1},~\dfrac{p_2}{q_2},~\cdots,~\dfrac{p_{n-2}}{q_{n-2}},~\dfrac{p_{n-1}}{q_{n-1}},~\dfrac{p_n}{q_n}.
$$

Pri tome su skupine pomaka s parnim indeksom usmjerene udesno, pa bilježe položaj lijeve krajnje točke; skupine s neparnim indeksom usmjerene su ulijevo, pa bilježe položaj desne krajnje točke. Ispred tog niza krajnjih točaka dodamo još dvije krajnje točke

$$
\dfrac{p_{-2}}{q_{-2}}=\dfrac{0}{1},~\dfrac{p_{-1}}{q_{-1}}=\dfrac{1}{0}.
$$

Neka je broj pomaka u $k$-toj skupini $t_k$; prema gore dobivenoj vezi između broja pomaka i položaja krajnjih točaka vrijedi

$$
\dfrac{p_k}{q_k} = \dfrac{t_kp_{k-1}+p_{k-2}}{t_kq_{k-1}+q_{k-2}}.
$$

Prema [rekurzivnoj relaciji](./continued-fraction.md#rekurzivne-relacije) verižnih razlomaka slijedi da je krajnja točka

$$
\dfrac{p_k}{q_k} = [t_0,t_1,\cdots,t_k].
$$

Konačno dobiveni verižni razlomak je

$$
\dfrac{p}{q} = \dfrac{p_n+p_{n-1}}{q_n+q_{n-1}} = [t_0,t_1,\cdots,t_{n-1},t_n,1].
$$

Dakle, u [prikazu verižnim razlomkom](./continued-fraction.md#jednostavni-verižni-razlomci) ciljnog razlomka koji završava jedinicom, članovi ispred posljednje jedinice kodiraju put od korijena do trenutačnog čvora u Stern–Brocotovu stablu. Pri tome članovi s parnim indeksom (indeksi počinju od $0$) odgovaraju bridovima prema desnom djetetu, a članovi s neparnim indeksom bridovima prema lijevom djetetu.

Prikaz racionalnog broja verižnim razlomkom može se dobiti Euklidovim algoritmom, pa je složenost algoritma traženja razlomka temeljenog na prikazu verižnim razlomkom $O(\log\min\{p,q\})$.

???+ example "Traženje razlomka temeljeno na verižnim razlomcima"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/stern-brocot/fraction-finding-3.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/stern-brocot/fraction-finding-3.py:core"
        ```

Pomoću prikaza verižnim razlomkom jednostavno se izražavaju roditelj i djeca nekog čvora. Za čvor $[t_0,t_1,\cdots,t_n,1]$ roditelj je čvor koji u smjeru posljednjeg pomaka ima jedan pomak manje: ako je $t_n>1$, roditelj je $[t_0,t_1,\cdots,t_n - 1,1]$; inače je roditelj $[t_0,t_1,\cdots,t_{n-1},1]$. Njegova dva djeteta su redom $[t_0,t_1,\cdots,t_n+1,1]$ i $[t_0,t_1,\cdots,t_n,1,1]$; koji je od tih dvaju čvorova lijevo, a koji desno dijete, određuje se prema parnosti $n$.

## Calkin–Wilfovo stablo

Još jedna, jednostavnija struktura za pohranu pozitivnih racionalnih razlomaka je Calkin–Wilfovo stablo. Obično se prikazuje ovako:

![pic](./images/calkin-wilf-tree.svg)

Korijen stabla je $\dfrac{1}{1}$. Zatim, za čvor u kojem je razlomak $\dfrac{p}{q}$, njegovo lijevo odnosno desno dijete su $\dfrac{p}{p+q}$ odnosno $\dfrac{p+q}{q}$. Slično Stern–Brocotovu stablu, svaki je njegov razlomak neskrativ i sadrži svaki pozitivni neskrativi razlomak točno jednom.

### Veza s verižnim razlomcima

Za razliku od Stern–Brocotova stabla, Calkin–Wilfovo stablo nije binarno stablo pretraživanja, pa se ne može upotrijebiti za binarno pretraživanje racionalnih brojeva.

U Calkin–Wilfovu stablu, kad je $p>q$, roditelj razlomka $\dfrac{p}{q}$ je $\dfrac{p-q}{q}$; kad je $p<q$, roditelj je $\dfrac{p}{q-p}$. U prvom slučaju, krenuvši od $\dfrac{p}{q}$, on je desno dijete svog roditelja i možemo se neprestano penjati preko desne strane roditelja sve dok brojnik više nije veći od nazivnika; tada je u čvoru pohranjen razlomak $\dfrac{p\bmod q}{q}$, a broj pomaka u ovoj skupini je $\left\lfloor\dfrac{p}{q}\right\rfloor$. U drugom slučaju on je lijevo dijete svog roditelja i možemo se neprestano penjati preko lijeve strane roditelja sve dok nazivnik više nije veći od brojnika; tada je u čvoru pohranjen razlomak $\dfrac{p}{q\bmod p}$, a broj pomaka u ovoj skupini je $\left\lfloor\dfrac{q}{p}\right\rfloor$.

Jezikom verižnih razlomaka: neka je u trenutačnom čvoru pohranjen ostatak $s_k$ nekog verižnog razlomka; tada se penjanjem preko desne strane roditelja $\lfloor s_k\rfloor$ puta dolazi do razlomka $\dfrac{1}{s_{k+1}}$, a zatim se pomicanjem preko lijeve strane roditelja $\lfloor s_{k+1}\rfloor$ puta dolazi do razlomka $s_{k+2}$. Stoga je put od čvora $s_0=\dfrac{p}{q}$ prema gore do korijena $\dfrac{1}{1}$ kodiran verižnim razlomkom $[t_0,t_1,\cdots,t_n,1]$: izuzev posljednje $1$, članovi s parnim indeksom (indeksi počinju od $0$) označavaju broj pomaka preko desne strane roditelja, a članovi s neparnim indeksom broj pomaka preko lijeve strane roditelja.

Za čvor u kojem je razlomak $\dfrac{p}{q}=[t_0,t_1,\cdots,t_n,1]$ roditelj ima sljedeći prikaz:

1.  kad je $t_0>0$, roditelj je $\dfrac{p-q}{q}=[t_0 - 1, t_1, \cdots, t_n,1]$;
2.  kad je $t_0=0$ i $t_1>1$, roditelj je $\dfrac{p}{q-p} = [0, t_1 - 1, t_2, \cdots, t_n,1]$;
3.  kad je $t_0=0$ i $t_1=1$, roditelj je $\dfrac{p}{q-p} = [t_2, t_3, \cdots, t_n,1]$.

Obrnuto, njegova su djeca redom $\dfrac{p+q}{q}=[t_0+1,t_1,\cdots,t_n,1]$ i $\dfrac{p}{p+q}=[0,1,t_0,t_1,\cdots,t_n,1]$. Prikaz drugog djeteta verižnim razlomkom, kad je $t_0=0$, treba shvatiti kao $[0,1+t_1,t_2,\cdots,t_n,1]$.

### Veza sa Stern–Brocotovim stablom

Također u vezi s verižnim razlomcima: čvorovi na putu u Stern–Brocotovu stablu pokazuju rekurzivnu relaciju konvergenata (approximants), dok čvorovi na putu u Calkin–Wilfovu stablu pokazuju rekurzivnu relaciju ostataka. Prikaz istog razlomka verižnim razlomkom je jednoznačan, pa je kôd puta od njega do korijena u Calkin–Wilfovu stablu potpuno jednak kodu puta od korijena do njega u Stern–Brocotovu stablu. No budući da su smjerovi putova suprotni, iako su razlomci pohranjeni na istoj razini Stern–Brocotova i Calkin–Wilfova stabla jednaki, njihovi se položaji razlikuju.

Ako na oba stabla provedemo [pretraživanje u širinu](../../graph/bfs.md) i redom numeriramo čvorove, pri čemu korijen dobiva broj $1$, lijevo i desno dijete čvora s brojem $v$ su redom $2v$ i $2v+1$. Gledano u binarnom zapisu broja, izuzev početne $1$, od najviših bitova prema najnižima svaka $1$ označava pomak u desno dijete, a svaka $0$ pomak u lijevo dijete. U Calkin–Wilfovu stablu broj čvora u kojem se nalazi racionalni broj s prikazom verižnim razlomkom $[t_0,t_1,\cdots,t_n,1]$ je

$$
1\cdots \underbrace{0\cdots 0}_{t_3}\underbrace{1\cdots 1}_{t_2}\underbrace{0\cdots 0}_{t_1}\underbrace{1\cdots 1}_{t_0}.
$$

Odgovarajuće, u Stern–Brocotovu stablu broj čvora u kojem se nalazi racionalni broj s prikazom verižnim razlomkom $[t_0,t_1,\cdots,t_n,1]$ je

$$
1\underbrace{1\cdots 1}_{t_0}\underbrace{0\cdots 0}_{t_1}\underbrace{1\cdots 1}_{t_2}\underbrace{0\cdots 0}_{t_3}\cdots.
$$

Izbrišemo li početnu $1$, broj sastavljen od preostalih binarnih znamenki upravo je redni broj čvora na toj razini gledano slijeva nadesno (počevši od $0$). Ovo izvođenje pokazuje da su rasporedi razlomaka na istoj razini Stern–Brocotova i Calkin–Wilfova stabla međusobno povezani permutacijom obrnutih bitova (bit-reversal permutation), tj. permutacijom na $0\sim (2^k-1)$ dobivenom obrtanjem binarnih znamenki indeksa (dopunjenih vodećim $0$).

Upravo zato se čvorovi Stern–Brocotova stabla ponekad numeriraju prema brojevima odgovarajućih čvorova Calkin–Wilfova stabla; tako dobivena numeracija prikazana je na sljedećoj slici:

![pic](./images/stern-brocot-index.svg)

Ta se numeracija može konstruirati rekurzivno: korijen ima broj $1$; pri svakom prelasku u lijevo dijete vodeća $1$ broja zamjenjuje se s $10$, a pri prelasku u desno dijete vodeća $1$ broja zamjenjuje se s $11$. Čitanjem tog broja zdesna nalijevo dobiva se put od korijena do tog čvora.

### Sternov diatomski niz

Poredamo li sve razlomke Calkin–Wilfova stabla prema brojevima iz pretraživanja u širinu, ili sve razlomke Stern–Brocotova stabla prema numeraciji s gornje slike, dobivamo sljedeći niz:

$$
\dfrac{1}{1},~\dfrac{1}{2},~\dfrac{2}{1},~\dfrac{1}{3},~\dfrac{3}{2},~\dfrac{2}{3},~\dfrac{3}{1},~\dfrac{1}{4},~\dfrac{4}{3},~\dfrac{3}{5},~\dfrac{5}{2},\cdots.
$$

Pomoću postupka konstrukcije Calkin–Wilfova stabla može se dokazati da je u tom nizu nazivnik svakog razlomka nužno jednak brojniku sljedećeg. Izdvojimo li brojnike, dobivamo Sternov diatomski niz (Stern diatomic sequence, [OEIS A002487](https://oeis.org/A002487)), koji se naziva i Stern–Brocotov niz (Stern–Brocot sequence). Numeracija gornjeg niza počinje od $1$, a dodatno se definira da je $0$-ti član jednak $0$.

Neka je $a_n$ $n$-ti član Sternova diatomskog niza; tada on zadovoljava sljedeću rekurzivnu relaciju:

$$
\begin{aligned}
a_{2n} &= a_n,\\
a_{2n+1} &= a_n + a_{n+1}. 
\end{aligned}
$$

Baza rekurzije je $a_0=0$ i $a_1=1$. Za izračun vrijednosti $a_n$ Sternova diatomskog niza izravna primjena rekurzivne relacije ima složenost $O(\log^2n)$, što nije dobro. Bolji je pristup promatrati ga kao brojnik razlomka s brojem $n$ u Calkin–Wilfovu stablu i izračunati ga pomoću gore opisane rekurzivne relacije temeljene na verižnim razlomcima, uz složenost $O(\log n)$.

## Fareyev niz

Fareyev niz ima vrlo slična obilježja kao Stern–Brocotovo stablo. **Fareyev niz $n$-tog reda** (Farey sequence of order $n$) označavamo s $F_n$. To je niz koji nastaje poredanjem po veličini svih neskrativih razlomaka iz $[0,1]$ s nazivnikom manjim od ili jednakim $n$:

$$
\begin{array}{lllllllllllll}
F_1=\bigg\{&\dfrac{0}{1},&&&&&&&&&&\dfrac{1}{1}&\bigg\}\\\\
F_2=\bigg\{&\dfrac{0}{1},&&&&&\dfrac{1}{2},&&&&&\dfrac{1}{1}&\bigg\}\\\\
F_3=\bigg\{&\dfrac{0}{1},&&&\dfrac{1}{3},&&\dfrac{1}{2},&&\dfrac{2}{3},&&&\dfrac{1}{1}&\bigg\}\\\\
F_4=\bigg\{&\dfrac{0}{1},&&\dfrac{1}{4},&\dfrac{1}{3},&&\dfrac{1}{2},&&\dfrac{2}{3},&\dfrac{3}{4},&&\dfrac{1}{1}&\bigg\}\\\\
F_5=\bigg\{&\dfrac{0}{1},&\dfrac{1}{5},&\dfrac{1}{4},&\dfrac{1}{3},&\dfrac{2}{5},&\dfrac{1}{2},&\dfrac{3}{5},&\dfrac{2}{3},&\dfrac{3}{4},&\dfrac{4}{5},&\dfrac{1}{1}&\bigg\}
\end{array}
$$

Prema definiciji Fareyeva niza on prirodno zadovoljava monotonost, neskrativost i potpunost. Kao što je gore prikazano, razlomci koje $F_k$ dodaje u odnosu na $F_{k-1}$ uvijek su medijante susjednih razlomaka u $F_{k-1}$.

Gore opisani algoritam izgradnje Stern–Brocotova stabla jednako se može primijeniti na izgradnju Fareyeva niza. Budući da Stern–Brocotovo stablo sadrži sve neskrative razlomke, dovoljno je rubni uvjet zamijeniti ograničenjem na nazivnik da bi se dobio kôd za konstrukciju Fareyeva niza. Fareyev niz $n$-tog reda $F_n$ može se promatrati kao podniz Stern–Brocotova niza $n$-tog reda.

???+ example "Izgradnja Fareyeva niza"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/stern-brocot/farey-build.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/stern-brocot/farey-build.py:core"
        ```

Složenost izravne izgradnje Fareyeva niza je $O(|F_n|)=O(n^2)$.

### Duljina niza i traženje razlomka

Duljina Fareyeva niza može se izračunati rekurzivno. U odnosu na $F_{n-1}$, razlomci koje niz $F_n$ ima više svi imaju nazivnik $n$, a brojnik im ne prelazi $n$ i relativno je prost s $n$, pa vrijedi:

$$
\begin{aligned}
|F_n| &= |F_{n-1}| + \varphi(n) = 1 + \sum_{k=1}^n\varphi(k).
\end{aligned}
$$

Ovdje je $\varphi(n)$ [Eulerova funkcija](./euler-totient.md). Taj se izraz pomoću [linearnog sita](./sieve.md#sito-za-eulerovu-funkciju) može izračunati u $O(n)$, a pomoću [Du sita](./hyperbola.md#du-sito) složenost se može spustiti na $O(n^{2/3})$.

Češći od izravnog računanja duljine niza je slučaj kad treba odrediti redni broj nekog razlomka $r=\dfrac{p}{q}$ u nizu $F_n$. To je jednako izračunu vrijednosti

$$
1 + \sum_{k = 1}^n\sum_{i=1}^{\lfloor rk\rfloor}[i\perp k] = 1 + \sum_{d=1}^n\mu(d)\sum_{j=1}^{\lfloor n/d\rfloor}\lfloor rj\rfloor.
$$

Za dobivanje desne strane primijenjena je [Möbiusova inverzija](./mobius.md). Kombinacijom linearnog sita i nabrajanja djelitelja postiže se $O(n)$ pretprocesiranja i $O(n\log n)$ po upitu; kombinacijom Du sita i [algoritma nalik Euklidovu](./euclidean.md) postiže se $O(n^{2/3})$ pretprocesiranja i $O(\sqrt n\log n)$ po upitu.

Obrnuto, za nalaženje razlomka iz poznatog rednog broja treba binarno pretraživati po realnim brojevima iz $[0,1]$ ili [binarno pretraživati](#brzi-algoritam) u Stern–Brocotovu stablu. Prvi pristup može biti ograničen točnošću brojeva s pomičnim zarezom, a broj upita za redni broj razlomka je $O(\log V)$, gdje je $V$ raspon točnosti; drugi pristup nije ograničen točnošću brojeva s pomičnim zarezom, ali je broj upita za redni broj razlomka $O(\log^2n)$.

### Fareyevi susjedi

Ako su razlomci $\dfrac{a}{b}$ i $\dfrac{c}{d}$ susjedni u nekom Fareyevu nizu, nazivaju se **Fareyevim susjedima** (Farey neighbors), a također i Fareyevim parom (Farey pair).

Neka je $\dfrac{a}{b}<\dfrac{c}{d}$. Iz postupka konstrukcije Fareyeva niza znamo da je od dvaju susjednih razlomaka onaj kasnije dodani nužno medijanta drugog razlomka i njegova prethodnog susjeda, pa su Fareyevi susjedi susjedni i u Stern–Brocotovu nizu nekog reda; prema zaključku dokazanom u odjeljku [Neskrativost](#neskrativost) nužno vrijedi i

$$
bc-ad=1.
$$

Obrnuto, to je i dovoljan uvjet da dva neskrativa prava razlomka budu Fareyevi susjedi. Pokažimo to. Bez smanjenja općenitosti neka je $\dfrac{a}{b}$ onaj od dvaju razlomaka s većim nazivnikom; tada se oba razlomka pojavljuju u $F_b$. Neka je $\dfrac{e}{f}$ član niza $F_b$ koji se nalazi neposredno desno od $\dfrac{a}{b}$; prema već pokazanoj nužnosti vrijedi $be-af=1$. Međutim, [linearna kongruencija](./linear-equation.md) $bx-ay=1$ ima samo jedno rješenje u pozitivnim cijelim brojevima s $y\le b$, pa nužno vrijedi $(e,f)=(c,d)$.

Zapravo, budući da je sljedeći neskrativi razlomak koji će se pojaviti između njih nužno $\dfrac{a+c}{b+d}$, razlomci $\dfrac{a}{b}$ i $\dfrac{c}{d}$ susjedni su u Fareyevim nizovima od $\max\{b,d\}$-tog do $(b+d-1)$-og reda.

Odnos Fareyevih susjeda s nazivnikom koji ne prelazi $9$ prikazan je na sljedećoj slici:

![](./images/farey-diagram-ford-circle.svg)

Kružnice na slici nazivaju se [Fordove kružnice](https://en.wikipedia.org/wiki/Ford_circle): za svaki neskrativi razlomak $\dfrac{p}{q}$ iz $[0,1]$ nacrta se kružnica sa središtem $\left(\dfrac{p}{q},\dfrac{1}{2q^2}\right)$ i polumjerom $\dfrac{1}{2q^2}$. Slika pokazuje da se Fordove kružnice koje odgovaraju dvama razlomcima mogu samo dodirivati ili biti razdvojene, a dodiruju se ako i samo ako su ta dva razlomka Fareyevi susjedi. Štoviše, za bilo koje dvije kružnice na slici koje se dodiruju uvijek postoji jedinstvena treća kružnica koja dodiruje obje. Razlomak koji odgovara toj trećoj kružnici upravo je medijanta razlomaka koji odgovaraju tim dvjema kružnicama.

Da bismo provjerili da kružnice koje se dodiruju uvijek odgovaraju Fareyevim susjedima, možemo izravno izračunati udaljenost dvaju središta:

$$
\left(\dfrac{a}{b}-\dfrac{c}{d}\right)^2 + \left(\dfrac{1}{2b^2}-\dfrac{1}{2d^2}\right)^2 = \left(\dfrac{1}{2b^2}+\dfrac{1}{2d^2}\right)^2+\frac{(bc-ad)^2-1}{b^2d^2}.
$$

Budući da su dva neskrativa razlomka različita, vrijedi $|bc-ad|\ge 1$, pa se dvije kružnice mogu samo dodirivati ili biti razdvojene. Štoviše, dvije se kružnice dodiruju ako i samo ako je $|bc-ad|=1$, što je ekvivalentno tome da su ta dva razlomka Fareyevi susjedi.

Naposljetku, izračunajmo broj parova Fareyevih susjeda. Osim $\left(\dfrac{0}{1},\dfrac{1}{1}\right)$, svi ostali Fareyevi susjedi imaju različite nazivnike. Bez smanjenja općenitosti neka je $\dfrac{p}{q}$ onaj s većim nazivnikom; tada se drugi razlomak nužno može dobiti iz linearne diofantske jednadžbe u dvije nepoznanice

$$
qx-py=\pm 1
$$

Svaka od dviju jednadžbi ima točno jedno rješenje u pozitivnim cijelim brojevima koje zadovoljava $y<q$, a ona odgovaraju susjedima lijevo odnosno desno od $\dfrac{p}{q}$. Stoga svaki pravi razlomak iz $(0,1)$ ima dva Fareyeva susjeda s nazivnikom manjim od njegova; dodamo li $\dfrac{0}{1}$ i $\dfrac{1}{1}$, slijedi da niz $F_n$ ima ukupno $(2|F_n|-3)$ parova Fareyevih susjeda.

Naravno, razlomci $\dfrac{a}{b}<\dfrac{c}{d}$ nađeni u tom postupku upravo su lijevi i desni susjed razlomka $\dfrac{p}{q}$ u trenutku njegova umetanja u niz. Stoga su oni i sami Fareyevi susjedi, a $\dfrac{p}{q}$ je njihova medijanta. Neka je $\dfrac{p}{q}=[t_0,t_1,\cdots,t_n,1]$; tada su ta dva Fareyeva susjeda s manjim nazivnicima redom $[t_0,t_1,\cdots,t_n]$ i $[t_0,t_1,\cdots,t_{n-1}]$.

Za izračun ostalih Fareyevih susjeda trenutačnog razlomka $\dfrac{p}{q}$ dovoljno je [proširenim Euklidovim algoritmom](./bezouts.md#slučaj-dviju-varijabli) odrediti sva rješenja koja zadovoljavaju uvjete.

### Rekurzivna relacija

Fareyev niz ima jednostavnu rekurzivnu relaciju kojom se slijeva nadesno redom mogu izračunati svi razlomci Fareyeva niza $n$-tog reda.

Prvo, prethodna analiza pokazuje da je u $F_n$ novododani član $\dfrac{p}{n}$ uvijek medijanta dvaju susjednih razlomaka, lijevog i desnog. Zapravo ta relacija vrijedi za sve razlomke u $F_n$ (osim dviju krajnjih točaka). Neka je $\dfrac{a}{b}<\dfrac{p}{q}<\dfrac{c}{d}$; prema nužnom i dovoljnom uvjetu za Fareyeve susjede uvijek vrijedi

$$
bp-aq = 1 = cq-dp \iff \frac{p}{q} = \dfrac{a+c}{b+d}.
$$

Međutim, u općem slučaju razlomak $\dfrac{a+c}{b+d}$ možda treba skratiti.

Pomoću tog opažanja može se izgraditi sljedeća rekurzivna relacija. Neka su $\dfrac{a}{b}$ i $\dfrac{p}{q}$ poznati, a treba odrediti vrijednost trećeg razlomka $\dfrac{c}{d}$. Tada postoji $k$ takav da vrijedi

$$
a+c = kp,\ b+d=kq
$$

Budući da razlika

$$
\frac{kp-a}{kq-b} - \dfrac{p}{q} = \dfrac{bp-aq}{q(kq-b)} = \dfrac{1}{q(kq-b)}
$$

pada s rastom $k$, a neposredno uz $\dfrac{p}{q}$ treba biti onaj razlomak među svima koji zadovoljavaju $kq-b\le n$ s najmanjom tom razlikom, nužno vrijedi

$$
k = \left\lfloor\dfrac{n+b}{q}\right\rfloor.
$$

Može se provjeriti da je tako dobiveni razlomak nužno u $F_n$. Stoga brojnici i nazivnici razlomaka u $F_n$ zadovoljavaju rekurzivnu relaciju:

$$
\begin{aligned}
p_k &= \left\lfloor\frac{n + q_{k-2}}{q_{k-1}}\right\rfloor p_{k-1} - p_{k-2},\\
q_k &= \left\lfloor\frac{n + q_{k-2}}{q_{k-1}}\right\rfloor q_{k-1} - q_{k-2}.
\end{aligned}
$$

Početak rekurzije je $(p_0,q_0)=(0,1)$ i $(p_1,q_1)=(1,n)$.

## Zadaci

Zadaci kojima je gradivo ovog članka pozadina:

-   [LOJ 6685. 迷宫 (Labirint)](https://loj.ac/p/6685)
-   [UVa 10077. The Stern-Brocot Number System](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=33&page=show_problem&problem=1018)
-   [Luogu P8058. \[BalkanOI2003\] Farey 序列 (Fareyev niz)](https://www.luogu.com.cn/problem/P8058)
-   [UVa 12995. Farey Sequence](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4878)
-   [UVa 10408. Farey Sequences](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=16&page=show_problem&problem=1349)
-   [UVa 12438. Farey Polygon](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=279&page=show_problem&problem=3869)
-   [AtCoder ARC123F. Insert Addition](https://atcoder.jp/contests/arc123/tasks/arc123_f)

Zadaci u kojima treba binarno pretraživati u Stern–Brocotovu stablu:

-   [AtCoder ABC333G. Nearest Fraction](https://atcoder.jp/contests/abc333/tasks/abc333_g)
-   [SPOJ DIVCNT1 - Counting Divisors](https://www.spoj.com/problems/DIVCNT1/)
-   [SPOJ AFS3 - Amazing Factor Sequence (hard)](https://www.spoj.com/problems/AFS3/)

## Literatura i napomene

-   [Stern–Brocot tree - Wikipedia](https://en.wikipedia.org/wiki/Stern%E2%80%93Brocot_tree)
-   [Calkin–Wilf tree - Wikipedia](https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree)
-   [Farey sequence - Wikipedia](https://en.wikipedia.org/wiki/Farey_sequence)

**Dio sadržaja ove stranice preveden je prema članku [Дерево Штерна-Броко. Ряд Фарея](http://e-maxx.ru/algo/stern_brocot_farey) i njegovu engleskom prijevodu [The Stern-Brocot Tree and Farey Sequences](https://cp-algorithms.com/others/stern_brocot_tree_farey_sequences.html). Ruska je inačica pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0. Drugi dio sadržaja ove stranice preveden je prema članku [Continued fractions](https://cp-algorithms.com/algebra/continued-fractions.html), pod licencijom CC-BY-SA 4.0. Sadržaj je izmijenjen.**

[^mediant]: Kineski naziv preuzet je iz odjeljka 4.5 knjige 《具体数学》 (Concrete Mathematics, „Konkretna matematika”) u prijevodu Zhanga Mingyaoa i Zhanga Fana.
