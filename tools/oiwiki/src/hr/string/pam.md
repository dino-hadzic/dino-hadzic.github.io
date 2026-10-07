---
title: Palindromsko stablo
---

## Definicija

Palindromsko stablo (EER Tree, palindromic tree, također poznato kao palindromski automat) učinkovita je struktura podataka za pohranu svih palindromskih podstringova stringa. Prvi su ga objavili Mikhail Rubinchik i Arseny M. Shur 2015. godine. Nadahnuto je strukturama za sufikse stringova poput sufiksnog stabla te omogućuje jednostavno i učinkovito rješavanje niza problema s palindromima.

## Struktura

Palindromsko stablo otprilike izgleda ovako:

![](./images/pam1.png)

Poput drugih automata, palindromsko stablo sastoji se od prijelaznih bridova i sufiksnih veza (pokazivača fail), a svaki čvor može predstavljati palindromski podstring.

Palindromi mogu imati neparnu ili parnu duljinu. Kao u Manacherovu algoritmu, mogli bismo umetnuti znak izvan abecede, primjerice '#', kao separator da sve duljine palindroma postanu neparne, ali to je nespretno. Postoji li bolji način?

Naravno da postoji. Izgradimo dva stabla: čvorovi jednog predstavljaju palindromske podstringove neparne duljine, a čvorovi drugog palindromske podstringove parne duljine.

Kao u drugim automatima, pokazivač fail čvora pokazuje na čvor koji predstavlja najdulji palindromski sufiks njegova palindroma. No prijelazni brid ne dodaje znak samo na kraj: on dodaje jednak znak na oba kraja izvornog palindroma (što je prirodno jer pohranjeni string mora ostati palindrom).

U svakom čvoru održavamo i duljinu len njegova palindromskog podstringa. Taj podatak omogućuje jednostavnu izgradnju palindromskog stabla.

## Izgradnja

Palindromsko stablo ima dva početna stanja koja predstavljaju palindrome duljina $-1,0$, a zovemo ih neparnim i parnim korijenom. Ne predstavljaju stvarne stringove, nego služe samo kao početna stanja, slično korijenima drugih automata.

Pokazivač fail parnog korijena pokazuje na neparni korijen. Pokazivač fail neparnog korijena nije nam važan jer u neparnom korijenu podudaranje ne može izostati (sljedeći prijelaz vodi u stanje duljine $1$, odnosno jedan znak, koji je uvijek palindromski podstring).

Kao i sufiksni automat, palindromsko stablo gradimo inkrementalno.

Pretpostavimo da smo izgradili stablo za prvih $p-1$ znakova, a sada dodajemo znak s pozicije $p$ izvornog stringa.

Krećemo od čvora najduljeg palindromskog podstringa koji završava prethodnim znakom. Slijedimo pokazivače fail dok ne dođemo do čvora za koji vrijedi $s_{p}=s_{p-len-1}$, odnosno znak ispred njegova palindroma jednak je znaku koji dodajemo.

Slijedi slika iz izvornog rada:

![](./images/pam2.png)

Slijedeći pokazivače fail pronalazimo čvor za A. Dodavanjem `X` na oba kraja dobivamo trenutačni palindrom, `XAX`. Očito je to čvor stabla za najdulji palindromski podstring koji završava na $p$. (Ovdje se vidi prednost čvora duljine $-1$: ako se nijedan `X` ne podudara, uvjet postaje $s_p=s_p$ na istoj poziciji i prirodno dobivamo čvor za znak `X`.) Ako taj čvor ne postoji, stvorimo ga.

Zatim izračunamo pokazivač fail novog čvora. Postupak je sličan: krećući od `A`, slijedimo pokazivače fail da pronađemo `XBX`, najdulji palindromski sufiks stringa `XAX`, i postavimo pokazivač fail na njegov čvor.

Taj čvor ne treba stvarati. Prvih $len_B$ i posljednjih $len_B$ znakova stringa `A` jednaki su i čine `B`. Prema simetriji palindroma, prvih $len_B$ znakova s obje strane okruženo je znakom `X`; zadnji je znak zadan kao `X`. Zato čvor `XBX` sigurno već postoji.

Ako za fail ne pronađemo podudaranje, povežemo ga s čvorom duljine $0$. To je ispravno jer je on sufiks svakog čvora.

## Dokaz linearnog broja stanja

### Teorem

String $s$ ima najviše $|s|$ različitih palindromskih podstringova.

### Dokaz

Koristimo matematičku indukciju.

-   Ako je $|s| =1$, $s$ ima jedan znak i samo jedan podstring, koji je palindrom. Tvrdnja stoga vrijedi.

-   Ako je $|s| >1$, neka je $t=sc$, gdje je $t$ string dobiven iz stringa $s$ dodavanjem znaka $c$ na kraj, i pretpostavimo da tvrdnja vrijedi za $s$. Promotrimo palindromske podstringove koji završavaju posljednjim znakom $c$, s lijevim krajevima poredanima rastuće kao $l_1,l_2,\dots,l_k$. Budući da je $t[l_1..|t|]$ palindrom, za svaku poziciju $l_1 \le p \le |t|$ vrijedi $t[p..|t|]=t[l_1..l_1+|t|-p]$. Zato se za $1 < i \le k$ podstring $t[l_i..|t|]$ već pojavio u $t[1..|t|-1]$. Dodavanje jednog znaka stoga povećava broj različitih palindromskih podstringova najviše za $1$.

Teorem slijedi matematičkom indukcijom.

Zato palindromsko stablo ima $O(|s|)$ stanja. Svako stanje predstavlja točno jedan različit palindromski podstring, pa je stanje iz kojeg dolazi prijelaz u njega jedinstveno. Zbog toga je i ukupan broj prijelaza $O(|s|)$.

## Dokaz ispravnosti

Na prethodnoj slici dodajemo trenutačni znak `X`. Prema dokazu linearnog broja stanja dovoljno je pronaći najdulji palindromski sufiks koji sadrži posljednji `X`, odnosno `XAX`. Zatim pronalazimo njegov najdulji palindromski sufiks `XBX` i stvaramo sufiksnu vezu. Stanje za `XBX` već postoji u stablu. Palindromski sufiksi koji sadrže posljednji znak jesu `XAX`, sam `XBX` i svi preci njegova stanja u stablu fail veza.

Pri izgradnji palindromskog stabla stringa $s$ neka je $n=|s|$. Očito sve operacije osim slijeđenja pokazivača fail ukupno traju $O(n)$.

Pri dodavanju znaka svaki skok pokazivačem fail mijenja dubinu trenutačnog čvora u stablu fail veza za $-1$ u odnosu na prethodni korak. Povezivanje fail veze povećava dubinu samo za 1 (osim kad je fail $0$, odnosno podudaranje postoji tek na $-1$: tada u odnosu na $-1$ dubina raste za $+2$).

Budući da dodajemo samo $n$ znakova, dubina se povećava samo $n$ puta, pa ima najviše $2n$ skokova pokazivačem fail.

Zato je vremenska složenost izgradnje palindromskog stabla stringa $s$ jednaka $O(|s|)$.

## Primjene

### Broj različitih palindromskih podstringova

Iz dokaza linearnog broja stanja slijedi da je broj različitih palindromskih podstringova stringa jednak broju stanja njegova palindromskog stabla, bez neparnog i parnog korijena.

### Broj pojavljivanja palindromskih podstringova

Izgradimo palindromsko stablo i brojimo pojavljivanja slično kao u sufiksnom automatu.

Tijekom izgradnje čvorovi se već umeću topološkim redoslijedom. Zato je dovoljno proći svim stanjima obrnutim redoslijedom i broj pojavljivanja svakog stanja dodati broju pojavljivanja stanja na koje pokazuje njegov fail.

Primjer: [APIO2014: Palindromi](https://www.luogu.com.cn/problem/P3649)

Vrijednost podstringa stringa $s$ definiramo kao umnožak njegova broja pojavljivanja u $s$ i njegove duljine. Za zadani string $s$ pronađite najveću vrijednost među svim palindromskim podstringovima.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/string/code/pam/pam_1.cpp"
    ```

### Minimalna palindromska faktorizacija

> Zadan je string $s(1\le |s| \le 10^5)$. Pronađite najmanji $k$ za koji postoje stringovi $s_1,s_2,\dots,s_k$ takvi da je svaki $s_i(1\le i \le k)$ palindrom, a spajanjem $s_1,s_2, \dots ,s_k$ redom dobivamo $s$.

Razmotrimo dinamičko programiranje. Neka $dp[i]$ označava najmanji broj dijelova faktorizacije prefiksa stringa $s$ duljine $i$. Za prijelaz prolazimo svim palindromima koji završavaju na $i$-tom znaku:

$$
dp[i]=1+\min_{ s[j+1..i] \text{ je palindrom} } dp[j]
$$

String može imati $O(n^2)$ palindromskih podstringova, pa ovaj algoritam traje $O(n^2)$, što je neprihvatljivo. Za optimizaciju prijelaza dokazujemo sljedeće leme.

Za string $s$ njegov prefiks duljine $i$ označavamo s $pre(s,i)$, a sufiks duljine $i$ sa $suf(s,i)$.

Period: ako je $0< p \le |s|$ i vrijedi $\forall 1 \le i \le |s|-p,s[i]=s[i+p]$, onda $p$ zovemo periodom stringa $s$.

Rub (border): ako je $0 \le r < |s|$ i vrijedi $pre(s,r)=suf(s,r)$, onda $pre(s,r)$ zovemo rubom stringa $s$.

Veza perioda i rubova: $t$ je rub stringa $s$ ako i samo ako je $|s|-|t|$ period stringa $s$.

???+ note "Dokaz"
    Ako je $t$ rub stringa $s$, tada je $pre(s,|t|)=suf(s,|t|)$, pa vrijedi $\forall 1\le i \le |t|, s[i]=s[|s|-|t|+i]$. Zato je $|s|-|t|$ period stringa $s$.
    
    Ako je $|s|-|t|$ period stringa $s$, tada vrijedi $\forall 1 \le i \le |s|-(|s|-|t|)=|t|,s[i]=s[|s|-|t|+i]$. Zato je $pre(s,|t|)=suf(s,|t|)$, pa je $t$ rub stringa $s$.

#### Lema 1

Neka je $t$ sufiks palindroma $s$. Tada je $t$ rub stringa $s$ ako i samo ako je $t$ palindrom.

???+ note "Dokaz"
    Za $1 \le i \le |t|$, budući da su $s$ i $t$ palindromi, vrijedi $s[i]=s[|s|-i+1]=s[|s|-|t|+i]$. Zato je $t$ rub stringa $s$.
    
    Za $1 \le i \le |t|$, budući da je $t$ rub stringa $s$, vrijedi $s[i]=s[|s|-|t|+i]$. Budući da je $s$ palindrom, vrijedi $s[i]=s[|s|-i+1]$. Zato je $s[|s|-i+1]=s[|s|-|t|+i]$, pa je $t$ palindrom.

Na sljedećoj slici pozicije jednake boje sadrže jednake znakove.

![](./images/pam3.png)

#### Lema 2

Neka je $t$ rub stringa $s$ i vrijedi $|s|\le 2|t|$. Tada je $s$ palindrom ako i samo ako je $t$ palindrom.

???+ note "Dokaz"
    Ako je $s$ palindrom, iz leme $1$ slijedi da je i $t$ palindrom.
    
    Ako je $t$ palindrom, budući da je $t$ rub stringa $s$, vrijedi $\forall 1 \le i \le |t|, s[i]=s[|s|-|t|+i]=s[|s|-i+1]$. Budući da je $|s| \le 2|t|$, i $s$ je palindrom.

#### Lema 3

Ako je $t$ rub palindroma $s$, tada je $|s|-|t|$ period stringa $s$. Nadalje, $|s|-|t|$ najmanji je period stringa $s$ ako i samo ako je $t$ najdulji pravi palindromski sufiks stringa $s$.

#### Lema 4

Neka je $x$ palindrom, $y$ najdulji pravi palindromski sufiks stringa $x$, a $z$ najdulji pravi palindromski sufiks stringa $y$. Neka su $u,v$ stringovi za koje vrijedi $x=uy,y=vz$. Tada vrijede sljedeća tri svojstva:

1.  $|u| \ge |v|$;

2.  Ako je $|u| > |v|$, tada je $|u| > |z|$;

3.  Ako je $|u| = |v|$, tada je $u=v$.

![](./images/pam4.png)

???+ note "Dokaz"
    1.  Prema lemi $3$, $|u|=|x|-|y|$ najmanji je period stringa $x$, a $|v|=|y|-|z|$ najmanji period stringa $y$. Pretpostavimo suprotno, $|u| < |v|$. Budući da je $y$ sufiks stringa $x$, $u$ je period i stringa $x$ i stringa $y$, što proturječi činjenici da je $|v|$ najmanji period stringa $y$. Zato je $|u| \ge |v|$.
    2.  Budući da je $y$ rub stringa $x$, $v$ je prefiks stringa $x$. Neka string $w$ zadovoljava $x=vw$ (kao na slici), pri čemu je $z$ rub stringa $w$. Pretpostavimo suprotno, $|u| \le |z|$. Tada je $|zu| \le 2|z|$, pa je prema lemi $2$ string $w$ palindrom. Prema lemi $1$, $w$ je rub stringa $x$. Budući da je $|u| > |v|$, vrijedi $|w| > |y|$, što je proturječje. Zato je $|u| > |z|$.
    3.  Oba stringa $u,v$ prefiksi su stringa $x$ i vrijedi $|u|=|v|$, pa je $u=v$.
    
    ![](./images/pam5.png)

#### Korolar

Nakon što sve palindromske sufikse stringa $s$ poredamo po duljini, njihove duljine možemo podijeliti u $\log |s|$ aritmetičkih nizova.

???+ note "Dokaz"
    Neka su duljine svih palindromskih sufiksa stringa $s$, poredane rastuće, $l_1,l_2,\dots,l_k$. Za svaki $2 \le i \le k-1$, ako vrijedi $l_{i}-l_{i-1}=l_{i+1}-l_{i}$, tada $l_{i-1},l_{i},l_{i+1}$ čine aritmetički niz. Inače je $l_{i}-l_{i-1}\neq l_{i+1}-l_{i}$. Prema lemi $4$ vrijedi $l_{i+1}-l_{i}>l_{i}-l_{i-1}$ i $l_{i+1}-l_{i}>l_{i-1}$, pa je $l_{i+1}>2l_{i-1}$. Dakle, kad se razlike duljina dvaju susjednih parova promijene, najveća je duljina više nego dvostruka u odnosu na najmanju. Udvostručenje se može dogoditi samo $O(\log |s|)$ puta, pa se duljine palindromskih sufiksa stringa $s$ mogu podijeliti u $\log |s|$ aritmetičkih nizova.

Korolar se može dokazati i slabom lemom o periodičnosti: sve rubove najduljeg palindromskog sufiksa stringa $s$ razvrstamo prema duljini $x$, gdje je $x \in [2^0,2^1),[2^1,2^2),\dots,[2^k,n)$, te promatramo najdulji rub u svakoj od tih $\log |s|$ skupina. Detaljne dokaze donose Jin Ce u „Odabranim temama iz algoritama za stringove” i Chen Sunli u radu za nacionalni tim kandidata za IOI 2019. „Algoritmi za upite o periodima podstringova i njihove primjene”.

S tim zaključkom sada možemo optimizirati prijelaze za $dp$.

#### Optimizacija

U svakom čvoru $u$ palindromskog stabla održavamo još dvije vrijednosti, $diff[u]$ i $slink[u]$. Vrijednost $diff[u]$ razlika je duljina palindroma koje predstavljaju čvorovi $u$ i $fail[u]$, odnosno $len[u]-len[fail[u]]$. Vrijednost $slink[u]$ dobivamo tako da od $u$ slijedimo pokazivače fail do prvog čvora $v$ za koji je $diff[v] \neq diff[u]$, odnosno čvora najmanje duljine u aritmetičkom nizu kojem pripada $u$.

Prema prethodno dokazanom zaključku, slijeđenje pokazivača $slink$ prema gore zahtijeva samo $O(\log |s|)$ skokova za svaki dodani znak. Zato zbroj vrijednosti $dp$ svih palindroma predstavljenih jednim aritmetičkim nizom (u izvornom problemu $\min$) možemo pohraniti u čvoru najduljeg palindroma tog niza.

Neka $g[v]$ za aritmetički niz kojem pripada $v$ označava zbroj njegovih vrijednosti $dp$, pri čemu je $v$ njegov najdulji čvor. Tada je $g[v]=\sum_{slink[x]=slink[v]} dp[i-len[x]]$, gdje je $i$ trenutačni indeks.

Razmotrimo kako ažurirati polja $g$ i $dp$. Na sljedećoj slici pretpostavimo da obrađujemo $i$-ti znak, kojem u palindromskom stablu odgovara čvor $x$. Vrijednost $g[x]$ zbroj je vrijednosti $dp$ na trima narančastim pozicijama (najkraći palindrom $slink[x]$ pripada sljedećem aritmetičkom nizu). Prethodno pojavljivanje $fail[x]$ nalazi se na $i-diff[x]$ (završava na $i-diff[x]$), a $g[fail[x]]$ sadrži vrijednosti $dp$ na plavim pozicijama. Zato je $g[x]$ jednak $g[fail[x]]$ uvećanom za vrijednost $dp$ na jednoj dodatnoj poziciji, $i-(len[slink[x]]+diff[x])$. Na kraju s $g[x]$ ažuriramo $dp[i]$ i time dovršavamo doprinos tog aritmetičkog niza. Nastavljamo skakati na $slink[x]$ i ponavljamo postupak. Implementacija se nalazi u kodu primjera.

![](./images/pam6.png)

Na kraju, ispravnost se oslanja na sljedeću činjenicu: ako $x$ i $fail[x]$ pripadaju istom aritmetičkom nizu, prethodno pojavljivanje $fail[x]$ nalazi se na $i-diff[x]$.

???+ note "Dokaz"
    Prema lemi $1$, $fail[x]$ je rub stringa $x$, pa se pojavljuje na $i-diff[x]$.
    
    Pretpostavimo da se $fail[x]$ pojavljuje u intervalu $(i-diff[x],i)$ na poziciji $j$. Budući da $x$ i $fail[x]$ pripadaju istom aritmetičkom nizu, vrijedi $2|fail[x]| \ge x$. Dodatno pojavljivanje $fail[x]$ preklapa se s pojavljivanjem na $i-diff[x]$ stringa $fail[x]$. Preklapanje označimo s $w$ i neka string $u$ zadovoljava $uw=fail[x]$. Slično kao u lemi $1$ možemo dokazati da je $w$ palindrom i da je prefiks stringa $x$, $s[i-len[x]+1..j]=uwu$, također palindrom. To proturječi činjenici da je $fail[x]$ najdulji palindromski prefiks (sufiks) stringa $x$.

Primjer: [Codeforces 932G Palindrome Partition](https://codeforces.com/problemset/problem/932/G)

Zadan je string $s$. Podijelite $s$ na $t_1, t_2, \dots, t_k$, pri čemu je $k$ paran i vrijedi $t_i=t_{k-i+1}$. Prebrojite takve podjele.

??? note "Rješenje"
    Konstruiramo $t= s[0]s[n - 1]s[1]s[n - 2]s[2]s[n - 3] \dots s[n / 2 - 1]s[n / 2]$. Problem je ekvivalentan brojanju faktorizacija stringa $t$ na palindrome parne duljine. Prethodne prijelaze zamijenimo zbrajanjem i polje $dp$ ažuriramo samo na parnim pozicijama. Vremenska složenost jest $O(n \log n)$, a prostorna $O(n)$.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/string/code/pam/pam_2.cpp"
    ```

## Primjeri zadataka

-   [Najdulji dvostruki palindrom](https://www.luogu.com.cn/problem/P4555)

-   [Proba navijačica](https://www.luogu.com.cn/problem/P1659)

-   [SHOI2011: Dvostruki palindrom](https://www.luogu.com.cn/problem/P4287)

-   [HDU 5421 Victor and String](https://acm.hdu.edu.cn/showproblem.php?pid=5421)

-   [CodeChef Palindromeness](https://www.codechef.com/LTIME23/problems/PALPROB)

## Povezani izvori

-   [EERTREE: An Efficient Data Structure for Processing Palindromes in Strings](https://arxiv.org/pdf/1506.04862)

-   [Palindromic tree](http://adilet.org/blog/palindromic-tree/)

-   Weng Wentao, „Palindromska stabla i njihove primjene”, zbornik radova nacionalnog tima kandidata za IOI 2017.

-   Chen Sunli, „Algoritmi za upite o periodima podstringova i njihove primjene”, zbornik radova nacionalnog tima kandidata za IOI 2019.

-   Jin Ce, „Odabrane teme iz algoritama za stringove”.

-   [A bit more about palindromes](https://codeforces.com/blog/entry/19193)

-   [A Subquadratic Algorithm for Minimum Palindromic Factorization](https://arxiv.org/pdf/1403.2431.pdf)
