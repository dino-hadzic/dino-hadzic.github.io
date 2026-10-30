---
title: Algoritam nalik Euklidovu
---

## Uvod

Algoritam nalik Euklidovu (类欧几里得算法, engl. Euclidean-like algorithm) predstavio je Hong Huadun 2016. godine u sklopu razmjene iskustava sudionika zimskog kampa (冬令营). Često se koristi za rješavanje problema sumiranja nizova (s indeksom $i$) oblika

$$
\left\lfloor\dfrac{ai+b}{c}\right\rfloor
$$

Glavna mu je ideja iskoristiti rekurzivnu strukturu samih razlomaka kako bi se problem sveo na problem manje veličine i riješio rekurzivno. Budući da je rekurzivna struktura razlomaka u izravnoj [vezi](./continued-fraction.md#连分数表示的求法) s [Euklidovim algoritmom](./gcd.md#欧几里得算法), ova se metoda sumiranja naziva i algoritmom nalik Euklidovu.

Budući da [verižni razlomci](./continued-fraction.md) i [Stern–Brocotovo stablo](./stern-brocot.md) također opisuju rekurzivnu strukturu razlomaka, problemi koji se mogu riješiti algoritmom nalik Euklidovu obično se mogu riješiti i tim metodama. U usporedbi s njima, algoritam nalik Euklidovu obično je lakše razumjeti, a i implementacija mu je sažetija.

## Algoritam nalik Euklidovu

Najjednostavniji je primjer problem sumiranja:

$$
f(a,b,c,n)=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,
$$

gdje su $a,b,c,n$ pozitivni cijeli brojevi.

### Algebarski pristup

Najprije, uzimanjem $a,b$ modulo $c$ problem se može pojednostavniti i svesti na slučaj $0\le a,b<c$:

$$
\begin{aligned}
f(a,b,c,n)&=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor\\
&=\sum_{i=0}^n\left\lfloor
\frac{\left(\left\lfloor\frac{a}{c}\right\rfloor c+(a\bmod c)\right)i+\left(\left\lfloor\frac{b}{c}\right\rfloor c+(b\bmod c)\right)}{c}\right\rfloor\\
&=\sum_{i=0}^n\left(\left\lfloor\frac{a}{c}\right\rfloor i+\left\lfloor\frac{b}{c}\right\rfloor+\left\lfloor\frac{\left(a\bmod c\right)i+\left(b\bmod c\right)}{c}
\right\rfloor\right)\\
&=\frac{n(n+1)}{2}\left\lfloor\frac{a}{c}\right\rfloor
+(n+1)\left\lfloor\frac{b}{c}\right\rfloor+f(a\bmod c,b\bmod c,c,n).
\end{aligned}
$$

Razmotrimo sada preoblikovani problem. Neka je

$$
m = \left\lfloor \frac{an+b}{c} \right\rfloor.
$$

Tada se izvorni problem može zapisati kao dvostruka suma:

$$
\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor
=\sum_{i=0}^n\sum_{j=0}^{m-1}\left[j<\left\lfloor \frac{ai+b}{c} \right\rfloor\right].
$$

Zamijenimo redoslijed sumiranja; za to je za svaki $j$ potrebno izračunati raspon vrijednosti $i$ koje zadovoljavaju uvjet. U tu svrhu preoblikujemo uvjet:

$$
\begin{aligned}
&j<\left\lfloor \frac{ai+b}{c} \right\rfloor = \left\lceil \frac{ai+b+1}{c} \right\rceil-1\\
&\iff j + 1 < \left\lceil \frac{ai+b+1}{c} \right\rceil
\iff j+1< \frac{ai+b+1}{c} \\
&\iff \dfrac{cj+c-b-1}{a} < i
\iff \left\lfloor\dfrac{cj+c-b-1}{a}\right\rfloor < i.
\end{aligned}
$$

U preoblikovanju smo više puta iskoristili svojstva [funkcija zaokruživanja](./basic.md#取整函数) (najveće cijelo i najmanje cijelo). Uvrstimo li preoblikovani uvjet, izvorni se izraz može zapisati kao:

$$
\begin{aligned}
f(a,b,c,n)&=\sum_{j=0}^{m-1}
\sum_{i=0}^n\left[i>\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\
&=\sum_{j=0}^{m-1}\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\
&=nm-f\left(c,c-b-1,a,m-1\right).
\end{aligned}
$$

Neka je $(a',b',c',n')=(c,c-b-1,a,m-1)$; time smo se vratili na već razmotreni slučaj $a'>c'$.

Spojimo li ova dva koraka, vidimo da se tijekom postupka $(a,c)$ neprestano uzimaju modulo pa zamjenjuju mjesta, sve dok ne bude $a=0$. To nalikuje uzastopnom dijeljenju s ostatkom (Euklidovu algoritmu) primijenjenom na $(a,c)$, po čemu je algoritam nalik Euklidovu i dobio ime. Njegova je vremenska složenost $O(\log\min\{a,c\})$.

Tijekom računanja može se dogoditi $m=0$; tada se u unutarnjoj rekurziji pojavljuje $n=-1$. To ne utječe na konačni rezultat. Međutim, ako algoritam odmah prekinemo kad se pojavi $m=0$, vremenska se složenost algoritma može poboljšati na $O(\log\min\{a,c,n\})$.

??? note "Objašnjenje složenosti"
    Koristeći sličnost ovog algoritma s Euklidovim algoritmom, lako je pokazati da mu je vremenska složenost $O(\log\min\{a,c\})$. Stoga je dovoljno pokazati da je, ako algoritam prekinemo pri $m=0$, njegova vremenska složenost također $O(\log n)$.
    
    Neka je $m=\lfloor(an+b)/c\rfloor$ te označimo $S=mn$, $k=m/n$; oni redom odgovaraju površini rešetke točaka i nagibu pravca u geometrijskoj interpretaciji (vidi sljedeći odjeljak). Za dovoljno velik $n$ približno vrijedi $k\doteq a/c$.
    
    Promotrimo kako se $S$ i $k$ mijenjaju tijekom algoritma. U prvom koraku, uzimanju modula, $n$ ostaje nepromijenjen, $k$ se približno mijenja iz $a/c$ u $(a\bmod c)/c$, što odgovara promjeni nagiba iz $k$ u $k-\lfloor k\rfloor$, a $S$ se približno množi s $(k-\lfloor k\rfloor)/k$. U drugom koraku, zamjeni koordinatnih osi, $S$ ostaje približno nepromijenjen, a $k$ prelazi u svoju recipročnu vrijednost. Dakle, ako nakon ta dva koraka par $(k,S)$ prijeđe u $(k',S')$, vrijedi $k'=(k-\lfloor k\rfloor)^{-1}$ i $S'=\dfrac{k-\lfloor k\rfloor}{k}S\le (k-\lfloor k\rfloor)S$, jer je od druge runde nadalje na početku svake runde uvijek $k\ge 1$.
    
    Budući da je $1\le\lfloor k'\rfloor\le k'<\lfloor k'\rfloor+1$, nakon dviju rundi rekurzije $S$ se množi najviše s
    
    $$
    (k'-\lfloor k'\rfloor)(k-\lfloor k\rfloor) = 1-\dfrac{\lfloor k'\rfloor}{k'} < 1-\dfrac{\lfloor k'\rfloor}{\lfloor k'\rfloor+1} = \dfrac{1}{\lfloor k'\rfloor+1}\le \dfrac{1}{2}.
    $$
    
    Stoga algoritam nužno završava nakon najviše $O(\log S)$ rundi. Budući da od druge runde nadalje $S$ na početku svake runde nikad ne premašuje $S$ s kraja uzimanja modula u prethodnoj rundi, a potonji je približno $kn^2$ uz $k<1$, vrijedi $O(\log S)\subseteq O(\log n)$. Time je gornja tvrdnja dokazana.

Referentna implementacija zadatka-predloška:

??? example "Implementacija zadatka-predloška ([Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear))"
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-0.cpp:full-text"
    ```

### Geometrijska interpretacija

Ovaj se algoritam može razumjeti i s geometrijskog stajališta. Problemi koje algoritam nalik Euklidovu može riješiti uglavnom su problemi prebrojavanja cjelobrojnih točaka ispod pravca.

Kao što prikazuje krajnji lijevi dio slike u nastavku, ta suma odgovara broju točaka rešetke ispod pravca

$$
y = \dfrac{ax+b}{c}
$$

i iznad osi $x$ (ne uključujući os $x$) čija se apscisa nalazi u $[0,n]$.

![](./images/euclidean-1.svg)

Najprije uklonimo cjelobrojne dijelove nagiba i odsječka. Taj korak odgovara zasebnom prebrojavanju plavih točaka u srednjem dijelu gornje slike. Kad su nagib i odsječak cijeli brojevi, plave točke nužno tvore trapezni raspored, tj. točke rešetke u različitim stupcima tvore aritmetički niz, pa se njihov broj lako izračuna. Nakon što uklonimo te točke, broj preostalih točaka rešetke jednak je broju crvenih točaka u krajnjem desnom dijelu gornje slike. Problem se time sveo na slučaj u kojem su nagib i odsječak manji od jedan. Budući da je visina trapeza $n+1$, a duljine dviju osnovica redom $\lfloor b/c\rfloor$ i $(\lfloor a/c\rfloor n+\lfloor b/c\rfloor)$, prema formuli za površinu trapeza ovaj se korak može sažeti formulom

$$
f(a,b,c,n) = f(a\bmod c,b\bmod c,c,n) + \dfrac{1}{2}(n+1)\left(\left\lfloor\dfrac{b}{c}\right\rfloor+\left(\left\lfloor\dfrac{a}{c}\right\rfloor n+\left\lfloor\dfrac{b}{c}\right\rfloor\right)\right).
$$

Zatim zamijenimo koordinatne osi. Kao što prikazuje krajnji lijevi dio slike u nastavku, crvene i plave točke zajedno tvore pravokutnu rešetku točaka širine $n$ i visine $m=\lfloor(an+b)/c\rfloor$. Da bismo izračunali broj crvenih točaka, dovoljno je izračunati broj plavih točaka i oduzeti ga od broja točaka pravokutne rešetke. Nakon zamjene osi plava rešetka iz lijevog dijela slike postaje crvena rešetka ispod nekog pravca. Štoviše, nakon zamjene nagib je veći od jedan, pa smo se vratili na već obrađeni slučaj.

![](./images/euclidean-2.svg)

Ključno je kako izračunati jednadžbu pravca iznad nove crvene rešetke. Zamjenom koordinatnih osi u krajnjem lijevom dijelu gornje slike dobivamo njezin srednji dio. Pravac iznad crvene rešetke nakon zamjene (puna crta u srednjem dijelu) ne odgovara pravcu prije zamjene (punoj crti u krajnjem lijevom dijelu), nego je rezultat pomicanja pravca prije zamjene malo ulijevo i prema gore (isprekidana crta u krajnjem lijevom dijelu). Razlog je taj što bismo izravnom zamjenom osi na pravcu (punoj crti u krajnjem lijevom dijelu) dobili isprekidanu crtu u srednjem dijelu, no po definiciji točke rešetke ispod njega uključuju i točke koje leže točno na pravcu, što bi dovelo do dvostrukog brojanja točaka na pravcu. Da bismo to izbjegli, pravac $y=(cx-b)/a$, dobiven zamjenom osi na pravcu $y=(ax+b)/c$, treba pomaknuti malo prema dolje u pravac $y=(cx-b-1)/a$, tako da rešetka ispod njega bude upravo plava rešetka prije zamjene.

Treba riješiti još jedan detalj. Odsječak pravca u srednjem dijelu gornje slike negativan je, što znači da se još nismo vratili u početnu situaciju. Da bi odsječak ponovno postao nenegativan, dovoljno je pravac (punu crtu u srednjem dijelu) pomaknuti za jednu jedinicu ulijevo. Pritom ne gubimo nijednu točku rešetke, jer u plavoj rešetki prije zamjene nema točaka s ordinatom nula, pa nakon zamjene nema točaka s apscisom nula. Na kraju jednadžba pravca postaje $y=(cx+c-b-1)/a$; istodobno gornja granica apscisa rešetke prelazi iz $m$ u $m-1$. Ovaj se korak može sažeti formulom

$$
f(a,b,c,n) = mn - f(c,c-b-1,a,m-1).
$$

Ovaj rekurzivni algoritam funkcionira ponajprije iz dvaju razloga:

-   Prvo, nagibu pravca neprestano se uzima razlomljeni dio pa zatim recipročna vrijednost, što je ekvivalentno računanju [razvoja u verižni razlomak](./continued-fraction.md#连分数表示的求法) nagiba pravca $k=a/c$. Budući da je duljina razvoja racionalnog razlomka u verižni razlomak $O(\log\min\{a,c\})$, ovaj postupak nužno završava nakon $O(\log\min\{a,c\})$ koraka;
-   Drugo, budući da je pri svakoj zamjeni koordinatnih osi nagib pravca manji od jedan, intuitivno bi trebalo vrijediti $m<n$, odnosno nakon svake takve runde iteracije raspon apscisa neprestano se smanjuje. Strogom analizom u ranijem izračunu složenosti pokazano je da se nakon svake dvije runde iteracije $S=mn$ smanji barem na polovinu, pa ovaj postupak nužno završava nakon $O(\log n)$ koraka.

Zato je složenost algoritma nalik Euklidovu, kad je nagib racionalan, $O(\log\min\{a,c,n\})$.

Sličnom geometrijskom interpretacijom algoritam nalik Euklidovu može se poopćiti na slučaj iracionalnog nagiba; detaljna analiza nalazi se u primjeru zadatka u nastavku.

### Primjeri zadataka

???+ example "[【模板】类欧几里得算法 (Predložak: algoritam nalik Euklidovu)](https://www.luogu.com.cn/problem/P5170)"
    Više upita. Zadani su pozitivni cijeli brojevi $a,b,c,n$; izračunajte
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    g(a,b,c,n) &= \sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    h(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2.
    \end{aligned}
    $$

??? note "Rješenje 1"
    Slično izvodu za $f$ mogu se dobiti rekurzivni izrazi za $g,h$.
    
    Najprije, uzimanjem modula problem svodimo na slučaj $0\le a,b<c$:
    
    $$
    \begin{aligned}
    g(a,b,c,n)
    &=g(a\bmod c,b\bmod c,c,n)+\left\lfloor\frac{a}{c}\right\rfloor\frac{n(n+1)(2n+1)}{6}+\left\lfloor\frac{b}{c}\right\rfloor\frac{n(n+1)}{2}, \\
    h(a,b,c,n)&=h(a\bmod c,b\bmod c,c,n)\\
    &\quad+2\left\lfloor\frac{b}{c}\right\rfloor f(a\bmod c,b\bmod c,c,n)
    +2\left\lfloor\frac{a}{c}\right\rfloor g(a\bmod c,b\bmod c,c,n)\\
    &\quad+\left\lfloor\frac{a}{c}\right\rfloor^2\frac{n(n+1)(2n+1)}{6}+\left\lfloor\frac{b}{c}\right\rfloor^2(n+1)
    +\left\lfloor\frac{a}{c}\right\rfloor\left\lfloor\frac{b}{c}\right\rfloor n(n+1).
    \end{aligned}
    $$
    
    Zatim zamjenom redoslijeda sumiranja problem dalje preoblikujemo. Jednako kao prije, neka je
    
    $$
    m = \left\lfloor \frac{an+b}{c} \right\rfloor.
    $$
    
    Tada za sumu $g$ vrijedi
    
    $$
    \begin{aligned}
    g(a,b,c,n)&=\sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor\\
    &=\sum_{i=0}^n \sum_{j=0}^{m-1}i
    \left[j<\left\lfloor\frac{ai+b}{c}\right\rfloor\right] \\
    &=\sum_{j=0}^{m-1}\sum_{i=0}^n i\left[i>\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\
    &=\sum_{j=0}^{m-1}\dfrac{1}{2}\left(\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor+n+1\right)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\
    &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor^2\\
    &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}f(c,c-b-1,a,m-1) - \dfrac{1}{2}h(c,c-b-1,a,m-1).
    \end{aligned}
    $$
    
    Za sumu $h$ vrijedi
    
    $$
    \begin{aligned}
    h(a,b,c,n)&=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2\\
    &=\sum_{i=0}^n\sum_{j=0}^{m-1}(2j+1)\left[j<\left\lfloor\frac{ai+b}{c}\right\rfloor\right]\\
    &=\sum_{j=0}^{m-1}\sum_{i=0}^n(2j+1)\left[i>\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\
    &=\sum_{j=0}^{m-1}(2j+1)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\
    &=nm^2 - \sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - 2\sum_{j=0}^{m-1}j\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\\
    &=nm^2 - f(c,c-b-1,a,m-1) - 2g(c,c-b-1,a,m-1).
    \end{aligned}
    $$
    
    S geometrijskog stajališta ove nelinearne sume odgovaraju pridruživanju odgovarajuće težine $w(i,j)$ svakoj točki $(i,j)$ u području. Osim tih težina, ostatak postupka računanja potpuno je isti. Za izbor težina općenito vrijedi
    
    $$
    \sum_{i=0}^ni^r\left\lfloor \frac{ai+b}{c} \right\rfloor^s = \sum_{i=0}^n\sum_{j=0}^{m-1} i^r\left((j+1)^s-j^s\right)\left[j<\left\lfloor\frac{ai+b}{c}\right\rfloor\right].
    $$
    
    Još je jedna osobitost ovog zadatka da se $g$ i $h$ pri rekurzivnom računanju međusobno isprepliću. Stoga je potrebno $(f,g,h)$ rekurzivno računati zajedno kao trojku.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-1.cpp"
    ```

???+ example "[\[清华集训 2014\] Sum (Tsinghua trening 2014)](https://www.luogu.com.cn/problem/P5172)"
    Više upita. Zadani su pozitivni cijeli brojevi $n$ i $r$; izračunajte
    
    $$
    \sum_{d=1}^n(-1)^{\lfloor d\sqrt{r}\rfloor}.
    $$

??? note "Rješenje 1"
    Ako je $r$ potpun kvadrat, onda je suma jednaka $n$ kad je $\sqrt{r}$ paran; inače suma, ovisno o parnosti $n$, naizmjence poprima vrijednosti $0$ i $-1$. U nastavku razmatramo slučaj kad $r$ nije potpun kvadrat.
    
    Da bismo primijenili algoritam nalik Euklidovu, najprije sumu preoblikujemo u poznati oblik:
    
    $$
    \begin{aligned}
    \sum_{d=1}^n(-1)^{\lfloor d\sqrt{r}\rfloor} &= \sum_{d=1}^n\left(1 - 2(\lfloor d\sqrt{r}\rfloor\bmod 2)\right)\\
    &= n - 2\sum_{d=1}^n\left(\lfloor d\sqrt{r}\rfloor - 2\left\lfloor\dfrac{\lfloor d\sqrt{r}\rfloor}{2}\right\rfloor\right) \\
    &= n - 2\sum_{d=1}^n\lfloor d\sqrt{r}\rfloor + 4 \sum_{d=1}^n\left\lfloor\dfrac{d\sqrt{r}}{2}\right\rfloor\\
    &= n - 2f(1,0,1,n) + 4f(1,0,2,n).
    \end{aligned}
    $$
    
    Pritom funkcija $f$ ima oblik
    
    $$
    f(a,b,c,n) = \sum_{i=1}^n\left\lfloor\dfrac{a\sqrt{r}+b}{c}i\right\rfloor.
    $$
    
    Za razliku od algoritma u glavnom tekstu, ovdje nagib više nije racionalan. Neka je nagib
    
    $$
    k = \dfrac{a\sqrt{r}+b}{c}.
    $$
    
    Opet razlikujemo dva slučaja. Ako je $k\ge 1$, onda je
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=1}^n \lfloor ki\rfloor = \sum_{i=1}^n \lfloor(k-\lfloor k\rfloor)i\rfloor + \lfloor k\rfloor \sum_{i=1}^ni\\
    &= \lfloor k\rfloor\dfrac{n(n+1)}{2} + f(a,b-c\lfloor k\rfloor,c,n).
    \end{aligned}
    $$
    
    Problem se svodi na slučaj nagiba manjeg od jedan. Ako je $k<1$, neka je $m=\lfloor nk\rfloor$; tada je
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=1}^n \lfloor ki\rfloor = \sum_{i=1}^n\sum_{j=1}^m[j\le\lfloor ki\rfloor]\\
    &= \sum_{j=1}^m\sum_{i=1}^n[i>\lfloor k^{-1}j\rfloor] = nm - \sum_{j=1}^m\sum_{i=1}^n[i\le\lfloor k^{-1}j\rfloor].
    \end{aligned}
    $$
    
    Uvjet pri zamjeni $i$ i $j$ u ovom je izvodu jednostavniji nego u glavnom tekstu zato što na pravcu $y=kx$ nema točaka rešetke osim ishodišta. Ključno je sumu nakon zamjene zapisati u obliku $f(a,b,c,n)$, što znači da $a',b',c'$ moraju zadovoljavati
    
    $$
    k^{-1} = \dfrac{a'\sqrt{r}+b'}{c'}.
    $$
    
    To nije teško: dovoljno je racionalizirati nazivnik, čime dobivamo
    
    $$
    k^{-1} = \dfrac{c}{a\sqrt{r}+b} = \dfrac{ca\sqrt{r}-cb}{a^2r-b^2}.
    $$
    
    Dakle,
    
    $$
    a'=ca,~b'=-cb,~c'=a^2r-b^2.
    $$
    
    To pokazuje da je
    
    $$
    f(a,b,c,n) = nm - f(ca,-cb,a^2r-b^2,m).
    $$
    
    Da bismo izbjegli cjelobrojno prelijevanje (overflow), potrebno je svaki put $a,b,c$ podijeliti njihovim najvećim zajedničkim djeliteljem. Budući da se ovaj postupak računanja u potpunosti podudara s računanjem verižnog razlomka od $k$, prema [teoriji verižnih razlomaka](./continued-fraction.md#二次无理数), ako osiguramo $\gcd(a,b,c)=1$, oni tijekom računanja nužno ostaju unutar raspona cjelobrojnog tipa. Osim toga, iako se $(a,b,c,n)$ ne prelijeva, pri ograničenjima ovog zadatka $f(a,b,c,n)$ može premašiti raspon $64$-bitnih cijelih brojeva; dovoljno je dopustiti prirodno prelijevanje bez dodatne obrade, jer je konačni rezultat sigurno u $[-n,n]$.
    
    Iako nagib nikad ne postaje nula, složenost algoritma i dalje je $O(\log n)$, što se lako vidi iz ranijeg razmatranja složenosti algoritma.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-2.cpp"
    ```

???+ example "[Fraction](https://www.luogu.com.cn/problem/P5179)"
    Zadani su pozitivni cijeli brojevi $a,b,c,d$. Među svim neskrativim razlomcima $p/q$ koji zadovoljavaju $a/b<p/q<c/d$ pronađite onaj s leksikografski najmanjim $(q,p)$.

??? note "Rješenje"
    Ovaj je zadatak ujedno klasična primjena [Stern–Brocotova stabla](./stern-brocot.md); odgovarajuće rješenje može se naći [ovdje](./continued-fraction.md#连分数的树). Budući da ovisi samo o rekurzivnoj strukturi razlomaka, može se riješiti i metodom sličnom Euklidovu algoritmu, pa se može smatrati i primjenom algoritma nalik Euklidovu.
    
    Ako između $a/b$ i $c/d$ (bez krajeva) postoji barem jedan prirodan broj, možemo izravno uzeti $(q,p)=(1,\lfloor a/b\rfloor+1)$. Inače nužno vrijedi
    
    $$
    \left\lfloor\dfrac{a}{b}\right\rfloor \le \dfrac{a}{b} <\dfrac{p}{q} <\dfrac{c}{d}\le\left\lfloor\dfrac{a}{b}\right\rfloor+1.
    $$
    
    Iz ove nejednakosti vidimo da je cjelobrojni dio od $p/q$ određen kao $\lfloor a/b\rfloor$; izravno ga uklonimo, a zatim uzmemo recipročnu vrijednost cijelog izraza kako bismo odredili njegov razlomljeni dio. To je upravo [osnovna metoda](./continued-fraction.md#连分数表示的求法) određivanja verižnog razlomka od $p/q$. Ako je konačni odgovor $p/q$, vremenska je složenost algoritma $O(\log\min\{p,q\})$.
    
    Ovdje postoji jedan detalj: je li leksikografski najmanji razlomak dobiven nakon uzimanja recipročne vrijednosti ujedno leksikografski najmanji razlomak prije uzimanja recipročne vrijednosti. Drugim riječima, je li među razlomcima $p/q$ koji zadovoljavaju $a/b<p/q<c/d$ onaj s leksikografski najmanjim $(q,p)$ ujedno i onaj s leksikografski najmanjim $(p,q)$. Pretpostavimo suprotno: neka $p/q$ ima leksikografski najmanji $(q,p)$, ali $r/s\neq p/q$ ima leksikografski najmanji $(r,s)$. Tada nužno vrijedi $r<p$ i $q<s$. No to znači da je
    
    $$
    \dfrac{a}{b} < \dfrac{r}{s} < \dfrac{r}{q} < \dfrac{p}{q} < \dfrac{c}{d}.
    $$
    
    Dakle, $r/q$ strogo je manji od trenutačnog rješenja u oba leksikografska uređaja. To je u suprotnosti s pretpostavkom. Stoga je gornji algoritam ispravan.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-3.cpp"
    ```

## Univerzalni Euklidov algoritam

Izvodi algoritma nalik Euklidovu iz prethodnog odjeljka obično su prilično zamorni, a sume koje se njime mogu riješiti uglavnom su one koje se mogu svesti na problem (težinskog) prebrojavanja cjelobrojnih točaka ispod pravca. U ovom odjeljku razmatramo općenitiju metodu koja dodatno apstrahira gornji postupak i time omogućuje rješavanje više problema. Zato se ta metoda naziva i univerzalnim Euklidovim algoritmom (万能欧几里得算法, engl. universal Euclidean algorithm). I ona za rješavanje problema koristi rekurzivnu strukturu razlomaka, ali se način svođenja problema donekle razlikuje od algoritma nalik Euklidovu.

I dalje razmatramo najklasičniji problem sumiranja:

$$
f(a,b,c,n)=\sum_{i=1}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,
$$

gdje su $a,b,c,n$ pozitivni cijeli brojevi.

### Preoblikovanje problema

Neka je dužina s parametrima $(a,b,c,n)$ zadana s

$$
y = \frac{ax+b}{c},~0< x\le n.
$$

Za tu dužinu možemo na sljedeći način definirati niz znakova $S$ sastavljen od $U$ i $R$, koji nazivamo i **niz operacija**:

-   niz se sastoji od točno $n$ znakova $R$ i $m=\lfloor(an+b)/c\rfloor$ znakova $U$;
-   broj znakova $U$ ispred $i$-tog znaka $R$ jednak je točno $\lfloor(ai+b)/c\rfloor$, gdje je $i=1,\cdots,n$.

Geometrijski, to otprilike odgovara sljedećem: krenemo od ishodišta i svaki put kad udesno prijeđemo okomitu liniju mreže zapišemo $R$, a svaki put kad prema gore prijeđemo vodoravnu liniju mreže zapišemo $U$. Kao na sljedećoj slici:

![](./images/euclidean-universal.svg)

Dakako, pri takvoj definiciji treba razmotriti niz posebnih slučajeva:

-   pri prolasku kroz cjelobrojnu točku (tj. istodobnom prijelazu prema gore i udesno) najprije se zapisuje $U$, a zatim $R$;
-   na početku niza, osim broja prijelaza linija mreže prema gore na intervalu $(0,1]$, treba dodati još $\lfloor b/c\rfloor$ znakova $U$;
-   na kraju niza ne smije biti dodatnih znakova $U$.

Ako je nešto u geometrijskom opisu nejasno, za lakše razumijevanje može se pogledati gornja algebarska definicija. Geometrijski opis pomaže u razumijevanju tijeka algoritma u nastavku.

Osnovna je ideja univerzalnog Euklidova algoritma da se $U$ i $R$ u nizu operacija shvate kao elementi nekog [monoida](../algebra/basic.md#群), cijeli niz operacija kao umnožak elemenata monoida, a konačni je odgovor problema povezan s tim umnoškom.

Primjerice, u ovom zadatku možemo definirati vektor stanja $v = (1,y,\sum y)$ koji predstavlja trenutačno stanje nakon što smo od ishodišta prešli određeni broj linija mreže prema gore i udesno. Prva je komponenta konstanta, druga je ordinata $y$, a treća je tražena suma. Na početku je $v=(1,0,0)$. Svaki prijelaz linije mreže prema gore povećava ordinatu za jedan, što odgovara množenju vektora stanja zdesna matricom

$$
U = \begin{pmatrix}1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}.
$$

Svaki prijelaz linije mreže udesno dodaje sumi trenutačnu ordinatu, što odgovara množenju vektora stanja zdesna matricom

$$
R = \begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1\end{pmatrix}.
$$

Stoga je konačno stanje umnožak $(1,0,0)S$, gdje $S$ shvaćamo kao umnožak gornjih matrica. Traženi odgovor treća je komponenta konačnog stanja.

Osim definiranja elemenata monoida kao matrica, možemo ih definirati i kao doprinos dijela niza operacija konačnom rezultatu, a umnožak operacija kao spajanje doprinosa dvaju dijelova niza operacija.

U ovom zadatku doprinos svakog dijela niza operacija možemo definirati kao $(x,y,\sum y)$. Da bismo te oznake strogo objasnili, komponente možemo promatrati kao funkcije niza operacija, tj. za niz operacija $S$ njegov se doprinos može zapisati kao $(x(S),y(S),(\sum y)(S))$. Pritom $x(S)$ i $y(S)$ redom odgovaraju broju znakova $R$ i $U$ u nizu operacija $S$, odnosno broju prijelaza linija mreže udesno i prema gore na toj dužini. Znak sumiranja u posljednjoj komponenti općenito se definira ovako: za funkciju $f(S)$ na nizovima operacija definiramo $(\sum f)(S)$, zapisano i kao $\sum_S f$, kao sljedeći izraz:

$$
\sum_S f := \sum\{f(S_{[1,r]}):S_r=R\}.
$$

Pritom je $S_r$ $r$-ti znak niza $S$, a $S_{[1,r]}$ prefiks od $S$ sastavljen od prvih $r$ znakova. Drugim riječima, taj se znak sumiranja može shvatiti kao sumiranje po svim prefiksima niza operacija $S$ koji završavaju znakom $R$. Primjerice, vrijedi

$$
\sum_S 1 = x,~ \sum_S x = \dfrac{1}{2}x(x+1).
$$

Kao daljnji primjer, $\sum y$ zbroj je, po svakom prijelazu linije mreže udesno, broja dotadašnjih prijelaza linija mreže prema gore. Za cijeli niz operacija vrijednosti $y$ na svim prefiksima koji završavaju znakom $R$ upravo su vrijednosti $\lfloor(ai+b)/c\rfloor$ za $i=1,\cdots,n$. Stoga je $\sum y$ izračunat za cijeli niz operacija upravo tražena veličina u ovom zadatku.

Dvije su operacije redom $U=(0,1,0)$ i $R=(1,0,0)$. Nadalje, umnožak dvaju elemenata $(x_1,y_1,s_1)$ i $(x_2,y_2,s_2)$ možemo definirati kao

$$
(x_1,y_1,s_1)\cdot (x_2,y_2,s_2) = (x_1+x_2,y_1+y_2,s_1+s_2+x_2y_1).
$$

Pritom se rezultat spajanja doprinosa u posljednjoj komponenti dobiva sljedećim računom:

$$
\sum_{S_1+S_2}y = \sum_{S_1}y + \sum_{S_2}(y+y_1) = \sum_{S_1}y + \sum_{S_2}y + y_1\sum_{S_2}1 = s_1+s_2+x_2y_1.
$$

Lako se provjerava da je ovo množenje asocijativno i da je neutralni element $(0,0,0)$, pa ti elementi s tim množenjem tvore monoid. Traženi odgovor treća je komponenta umnoška.

Obje metode daju točan rezultat. Međutim, budući da čuva mnogo suvišnih informacija, matrični račun ima veliku konstantu, pa je druga metoda praktičnija pri rješavanju stvarnih problema.

### Tijek algoritma

Za razliku od algoritma nalik Euklidovu, koji problem svodi u cjelini, univerzalni Euklidov algoritam svodi problem spajanjem tih operacija u skupinama. Označimo umnožak operacija koje odgovaraju nizu znakova s

$$
F(a,b,c,n,U,R).
$$

Postupak svođenja glasi:

-   Kad je $b\ge c$, na početku niza operacija nalazi se $\lfloor b/c\rfloor$ znakova $U$; izravno izračunamo njihov umnožak i uklonimo te znakove $U$ iz niza operacija. Tada je broj znakova $U$ ispred $i$-tog znaka $R$ jednak

    $$
    \left\lfloor\dfrac{ai+b}{c}\right\rfloor - \left\lfloor\dfrac{b}{c}\right\rfloor = \left\lfloor\dfrac{ai+(b\bmod c)}{c}\right\rfloor.
    $$

    Dakle, to odgovara promjeni parametara dužine iz $(a,b,c,n)$ u $(a,b\bmod c,c,n)$. Stoga u ovom slučaju vrijedi

    $$
    F(a,b,c,n,U,R) = U^{\lfloor b/c\rfloor}F(a,b\bmod c,c,n,U,R).
    $$

-   Kad je $a\ge c$, ispred svakog znaka $R$ u nizu operacija nalazi se barem $\lfloor a/c\rfloor$ znakova $U$, koje možemo spojiti s $R$. Drugim riječima, $R$ možemo zamijeniti s $U^{\lfloor a/c\rfloor}R$. U spojenom nizu broj znakova $U$ ispred $i$-tog znaka $R$ jednak je

    $$
    \left\lfloor\dfrac{ai+b}{c}\right\rfloor - \left\lfloor\dfrac{a}{c}\right\rfloor i = \left\lfloor\dfrac{(a\bmod c)i+b}{c}\right\rfloor.
    $$

    Dakle, to odgovara promjeni parametara dužine iz $(a,b,c,n)$ u $(a\bmod c,b,c,n)$. Stoga u ovom slučaju vrijedi

    $$
    F(a,b,c,n,U,R) = F(a\bmod c,b,c,n,U,U^{\lfloor a/c\rfloor}R).
    $$

-   U preostalom slučaju treba zamijeniti koordinatne osi, što je u osnovi zamjena $U$ i $R$, samo što parametre dužine nakon zamjene treba pažljivo izračunati. Iz definicije niza operacija slijedi da treba odrediti koeficijente $(a',b',c',n')$ takve da je u nizu operacija prije transformacije broj znakova $R$ ispred $j$-tog znaka $U$ točno $\lfloor(a'j+b')/c'\rfloor$ i da ukupno ima $n'$ znakova $U$. Po definiciji je

    $$
    n'=\left\lfloor\dfrac{an+b}{c}\right\rfloor = m,
    $$

    a broj znakova $R$ ispred $j$-tog znaka $U$ jednak je najvećem $i$ za koji je

    $$
    \begin{aligned}
    \left\lfloor\dfrac{ai+b}{c}\right\rfloor < j 
    &\iff \dfrac{ai+b}{c} < j \iff i < \dfrac{cj-b}{a} \\
    &\iff i < \left\lceil\dfrac{cj-b}{a}\right\rceil = \left\lfloor\dfrac{cj-b - 1}{a}\right\rfloor + 1.
    \end{aligned}
    $$

    Dakle, $i = \lfloor(cj-b-1)/a\rfloor$. Ovaj je izvod sličan ranijem izvodu algoritma nalik Euklidovu i također koristi svojstva funkcija najvećeg i najmanjeg cijelog.

    Treba riješiti dva detalja:

    -   Član odsječka $-(b+1)/a$ negativan je. Uočimo da pomak dužine za jednu jedinicu ulijevo vraća odsječak u nenegativan, jer uvijek vrijedi $(c-b-1)/a\ge 0$. Stoga možemo izdvojiti prvi dio $R^{\lfloor(c-b-1)/a\rfloor}U$ niza prije zamjene i zamijeniti $U$ i $R$ samo u ostatku niza operacija;
    -   Nakon zamjene $U$ i $R$ na kraju ostaju suvišni znakovi $U$. Stoga prije zamjene $U$ i $R$ najprije treba izdvojiti posljednji blok znakova $R$ i zamijeniti $U$ i $R$ samo u ostatku niza operacija. Broj znakova $R$ u tom bloku jednak je $n-\lfloor(cm-b-1)/a\rfloor$.

    Nakon uklanjanja nekoliko znakova s početka i kraja, broj znakova $R$ ispred $j$-tog znaka $U$ postaje:

    $$
    \left\lfloor\dfrac{c(j+1)-b-1}{a}\right\rfloor - \left\lfloor\dfrac{c-b-1}{a}\right\rfloor = \left\lfloor\dfrac{cj+(c-b-1)\bmod a}{a}\right\rfloor.
    $$

    Prisjetimo se da je broj znakova $U$ u nizu prije zamjene $m = \lfloor(an+b)/c\rfloor$. Gornji pomak za jednu jedinicu ulijevo zahtijeva da prije zamjene postoji barem jedan znak $U$, tj. $m>0$. Prema tom uvjetu razlikujemo dva slučaja:

    -   Za $m>0$, nakon obrade gornjih dviju točaka, niz operacija sa zamijenjenim $U$ i $R$ upravo je valjani niz koji odgovara dužini s parametrima $(c,(c-b-1)\bmod a,a,m-1)$. Stoga vrijedi

        $$
        F(a,b,c,n,U,R) = R^{\lfloor(c-b-1)/a\rfloor}UF(c,(c-b-1)\bmod a,a,m-1,R,U)R^{n-\lfloor(cm-b-1)/a\rfloor}.
        $$

    -   Posebno, za $m=0$ niz operacija prije zamjene sadrži samo $n$ znakova $R$; zamjena nije potrebna i možemo izravno vratiti

        $$
        F(a,b,c,n,U,R) = R^n.
        $$

        Za razliku od algoritma nalik Euklidovu, ovaj poseban slučaj univerzalnog Euklidova algoritma treba obraditi zasebno; inače bi se zbog pojave negativnih potencija račun pokvario.

Na temelju ovih razmatranja problem se može riješiti rekurzivno.

Pretpostavimo da je vremenska složenost jednog množenja elemenata monoida $O(1)$. Tada, ako se sve potencije tih elemenata tijekom računanja računaju [brzim potenciranjem](../binary-exponentiation.md), konačna je složenost algoritma $O(\log\max\{a,c\}+\log(b/c))$[^complexity].

??? note "Objašnjenje složenosti"
    U usporedbi s (nalik) Euklidovim algoritmom, univerzalni Euklidov algoritam dodaje samo korake brzog potenciranja. Složenost ostatka postupka računanja slična je algoritmu nalik Euklidovu i već je pokazano da iznosi $O(\log\min\{a,c,n\})$. Sada treba izračunati ukupnu složenost tih brzih potenciranja.
    
    Osim u prvoj rundi iteracije, uvijek je $b<c$, pa svaka od tih rundi uključuje tri brza potenciranja, ukupne složenosti:
    
    $$
    O\left(\log\left\lfloor\dfrac{a}{c}\right\rfloor+\log\left\lfloor\dfrac{c-b_1-1}{a_1}\right\rfloor+\log\left(n-\left\lfloor\dfrac{cm-b_1-1}{a_1}\right\rfloor\right)\right),
    $$
    
    pri čemu je $a_1=a\bmod c$, $b_1=b\bmod c$ i $m=\lfloor(a_1n+b_1)/c\rfloor$. Za posljednja dva člana redom vrijede ocjene:
    
    $$
    \begin{aligned}
    \dfrac{c-b_1-1}{a_1} &\le \dfrac{c}{a_1},\\
    n-\left\lfloor\dfrac{cm-b_1-1}{a_1}\right\rfloor &\le n - \dfrac{cm-b_1-1}{a_1} + 1 \\
    &\le n - \dfrac{c((a_1n+b_1)/c-1)-b_1-1}{a_1} +1 \\
    &= \dfrac{c+1}{a_1}+1.
    \end{aligned}
    $$
    
    Stoga je složenost obaju članova $O(\log(c/a_1))$.
    
    U svakoj rundi iteracije parametri dužine prelaze iz $(a,\cdot,c,\cdot)$ u $(c,\cdot,a\bmod c,\cdot)$, a ukupna vremenska složenost te runde iznosi
    
    $$
    O\left(\log\dfrac{a}{c}+\log\dfrac{c}{a\bmod c}\right).
    $$
    
    Po svim rundama rekurzije ti se članovi teleskopski pokrate, pa je konačna ukupna složenost $O(\log a+\log c)=O(\log\max\{a,c\})$.
    
    Naposljetku, dodamo li složenost $O(\log(b/c))$ brzog potenciranja $U^{\lfloor b/c\rfloor}$ u prvoj rundi iteracije, dobivamo ukupnu složenost $O(\log\max\{a,c\}+\log(b/c))$.

Tijek univerzalnog Euklidova algoritma može se zapisati kao jedinstveni predložak; pri rješavanju konkretnog problema dovoljno je promijeniti implementaciju tipa predloška `T`.

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-4.cpp:euclidean"
    ```

Univerzalnim Euklidovim algoritmom dobivamo sljedeću implementaciju zadatka-predloška:

??? example "Implementacija zadatka-predloška ([Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear))"
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-4.cpp:full-text"
    ```

### Primjeri zadataka

???+ example "[【模板】类欧几里得算法 (Predložak: algoritam nalik Euklidovu)](https://www.luogu.com.cn/problem/P5170)"
    Više upita. Zadani su pozitivni cijeli brojevi $a,b,c,n$; izračunajte
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    g(a,b,c,n) &= \sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    h(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2.
    \end{aligned}
    $$

??? note "Rješenje 2"
    Da bismo primijenili predložak univerzalnog Euklidova algoritma, najprije izdvojimo član $i=0$ i razmotrimo ga zasebno. Ostatak možemo shvatiti kao računanje $\sum y,\sum xy,\sum y^2$ za dužinu s parametrima $(a,b,c,n)$. Kao što je rečeno u glavnom tekstu, postoje dva načina pretvaranja niza operacija u elemente monoida.
    
    **Matrični račun**: vektor stanja definiramo kao $(1,x,y,xy,y^2,\sum y,\sum xy,\sum y^2)$. Početno je stanje $(1,0,0,0,0,0,0,0)$, a dvije su operacije redom
    
    $$
    U =
    \begin{pmatrix}
    1 & 0 & 1 & 0 & 1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 2 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 
    \end{pmatrix},~
    R = 
    \begin{pmatrix}
    1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 1 & 0 & 1 & 1 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 
    \end{pmatrix}.
    $$
    
    Konačni su odgovor posljednje tri komponente vektora dobivenog množenjem početnog stanja zdesna umnoškom ovih matrica operacija.
    
    Ovaj pristup ima golemu konstantu i ne prolazi ovaj zadatak; detalji su ovdje navedeni samo kao pomoć razumijevanju.
    
    **Spajanje doprinosa**: doprinos dijela niza operacija definiramo kao $(x,y,\sum y,\sum xy,\sum y^2)$. Dvije su operacije redom
    
    $$
    U = (0,1,0,0,0),~ R = (1,0,0,0,0).
    $$
    
    Pri spajanju doprinosa vrijedi
    
    $$
    \begin{aligned}
    \sum_{S_1+S_2} y 
    &= \sum_{S_1}y + \sum_{S_2}(y+y_1) = \sum_{S_1}y + \sum_{S_2}y + x_2y_1,\\
    \sum_{S_1+S_2} xy
    &= \sum_{S_1}xy + \sum_{S_2}(x+x_1)(y+y_1) \\
    &= \sum_{S_1}xy + \sum_{S_2}xy + x_1\sum_{S_2}y + y_1\sum_{S_2}x + x_1y_1\sum_{S_2}1\\
    &= \sum_{S_1}xy + \sum_{S_2}xy + x_1\sum_{S_2}y + \dfrac{1}{2}x_2(x_2+1)y_1 + x_1x_2y_1,\\
    \sum_{S_1+S_2}y^2
    &= \sum_{S_1}y^2 + \sum_{S_2}(y+y_1)^2 \\
    &= \sum_{S_1}y^2 + \sum_{S_2}y^2 + 2y_1\sum_{S_2}y + y_1^2\sum_{S_2}1  \\
    &= \sum_{S_1}y^2 + \sum_{S_2}y^2 + 2y_1\sum_{S_2}y + x_2y_1^2.
    \end{aligned}
    $$
    
    To pokazuje da množenje operacija treba definirati kao
    
    $$
    \begin{aligned}
    &(x_1,y_1,s_1,t_1,u_1)\cdot(x_2,y_2,s_2,t_2,u_2)\\
    &= (x_1+x_2,y_1+y_2,s_1+s_2+x_2y_1,\\
    &\qquad t_1+t_2+x_1s_2+(1/2)x_2(x_2+1)y_1+x_1x_2y_1,\\
    &\qquad u_1+u_2+2y_1s_2+x_2y_1^2).
    \end{aligned}
    $$
    
    Iako je izravna provjera prilično zamorna, gore definirani vektori doprinosa s tim množenjem doista tvore monoid, s neutralnim elementom $(0,0,0,0,0)$.
    
    U općem slučaju vrijedi
    
    $$
    \begin{aligned}
    \sum_{S_1+S_2}x^ry^s &= \sum_{S_1}x^ry^s + \sum_{S_2}(x+x_1)^r(y+y_1)^s \\
    &= \sum_{S_1}x^ry^s + \sum_{i=0}^r\sum_{j=0}^s\binom{r}{i}\binom{s}{j}x_1^{r-i}y_1^{s-j}\sum_{S_2}x^iy^j.
    \end{aligned}
    $$
    
    Dok god održavamo doprinose svih nižih potencija, možemo izračunati i sume općeg oblika.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-5.cpp"
    ```

???+ example "[\[清华集训 2014\] Sum (Tsinghua trening 2014)](https://www.luogu.com.cn/problem/P5172)"
    Više upita. Zadani su pozitivni cijeli brojevi $n$ i $r$; izračunajte
    
    $$
    \sum_{d=1}^n(-1)^{\lfloor d\sqrt{r}\rfloor}.
    $$

??? note "Rješenje 2"
    Najprije zasebno obradimo slučaj kad je $r$ potpun kvadrat, potpuno jednako kao prije, pa ga ovdje izostavljamo. Razmatramo samo slučaj kad $r$ nije potpun kvadrat.
    
    Postoji mnogo načina primjene univerzalnog Euklidova algoritma na ovaj zadatak. Primjerice, svakoj operaciji možemo pridružiti linearnu transformaciju:
    
    $$
    U(x) = -x,~ R(x) = x + 1.
    $$
    
    Množenje operacija definiramo kao kompoziciju linearnih transformacija. Tada je konačni odgovor vrijednost u $x=0$ funkcije dobivene kompozicijom transformacija koje odgovaraju nizu operacija.
    
    Također možemo svakom dijelu niza operacija definirati njegov doprinos. Doprinos možemo definirati kao $((-1)^y,\sum(-1)^y)$. Tada za dvije operacije uzimamo redom
    
    $$
    U = (-1,0),~ R = (1,1).
    $$
    
    Spajanje doprinosa definiramo kao
    
    $$
    (u_1,v_1)\cdot(u_2,v_2) = (u_1u_2,v_1+u_1v_2).
    $$
    
    Lako se provjerava da s tim množenjem sve operacije tvore monoid, s neutralnim elementom $(1,0)$. Konačni je odgovor druga komponenta umnoška svih elemenata.
    
    Ove su dvije metode ekvivalentne, jer ako linearnu transformaciju zapišemo kao $f(x)=ux+v$, promjena koeficijenata pri kompoziciji linearnih transformacija upravo je gore definirano množenje operacija. Drugim riječima, ta su dva monoida izomorfna.
    
    U ovom su zadatku parametri dužine $(k,n)$, gdje je $k\in\mathbf R$ nagib pravca. Neka je umnožak koji odgovara nizu operacija $F(k,n,U,R)$. Tada imamo sljedeći rekurzivni algoritam:
    
    -   Ako je $k\ge 1$, ispred svakog znaka $R$ u nizu operacija nalazi se barem $\lfloor k\rfloor$ znakova $U$, pa vrijedi
    
        $$
        F(k,n,U,R) = F(k-\lfloor k\rfloor,n,U,U^{\lfloor k\rfloor} R).
        $$
    -   Ako je $k<1$, zamijenimo $U$ i $R$ u nizu operacija i odbacimo znakove $U$ na kraju (tj. znakove $R$ prije zamjene); označimo li $m=\lfloor kn\rfloor$, vrijedi
    
        $$
        F(k,n,U,R) = F(k^{-1},m,R,U)R^{n-\lfloor k^{-1}m\rfloor}.
        $$
    
    Iteracija $k$ u algoritmu zapravo je računanje razvoja $\sqrt{r}$ u verižni razlomak. Za to se može primijeniti [PQa algoritam](./pell-equation.md#pqa-算法). Postupak računanja verižnog razlomka i iteracija univerzalnog Euklidova algoritma mogu se provoditi istodobno.
    
    Kao i u slučaju algoritma nalik Euklidovu, složenost algoritma i dalje je $O(\log n)$.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-6.cpp"
    ```

## Zadaci za vježbu

Zadaci-predlošci:

-   [Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)
-   [Luogu P5170【模板】类欧几里得算法 (Predložak: algoritam nalik Euklidovu)](https://www.luogu.com.cn/problem/P5170)
-   [Luogu P5171 Earthquake](https://www.luogu.com.cn/problem/P5171)
-   [Luogu P5172 \[清华集训 2014\] Sum (Tsinghua trening 2014)](https://www.luogu.com.cn/problem/P5172)
-   [Luogu P4132 \[BJOI2012\] 算不出的等式 (Neizračunljiva jednakost)](https://www.luogu.com.cn/problem/P4132)
-   [LOJ 138. 类欧几里得算法 (Algoritam nalik Euklidovu)](https://loj.ac/p/138)
-   [LOJ 6440. 万能欧几里得 (Univerzalni Euklidov algoritam)](https://loj.ac/p/6440)
-   [Luogu P5179 Fraction](https://www.luogu.com.cn/problem/P5179)
-   [Codeforces 1182 F. Maximum Sine](https://codeforces.com/problemset/problem/1182/F)

Zadaci s primjenom:

-   [Luogu P4433 \[COCI 2009/2010 #1\] ALADIN](https://www.luogu.com.cn/problem/P4433)
-   [AtCoder Beginner Contest 372 G - Ax + By < C](https://atcoder.jp/contests/abc372/tasks/abc372_g)
-   [AtCoder Beginner Contest 313 G - Redistribution of Piles](https://atcoder.jp/contests/abc313/tasks/abc313_g)
-   [AtCoder Beginner Contest 283 Ex - Popcount Sum](https://atcoder.jp/contests/abc283/tasks/abc283_h)
-   [Codeforces 1098 E. Fedya the Potter](https://codeforces.com/problemset/problem/1098/E)
-   [Codeforces 868 G. El Toll Caves](https://codeforces.com/problemset/problem/868/G)

## Literatura i bilješke

[^complexity]: U problemima koji se obično razmatraju $b$ je istog reda veličine kao $a$, pa se član $O(\log(b/c))$ može zanemariti. Štoviše, ako se prije poziva univerzalnog Euklidova algoritma najprije provede jedna runda uzimanja modula iz algoritma nalik Euklidovu kako bi se uklonio utjecaj $b$, složenost tog brzog potenciranja može se izbjeći. Razlog je zapravo taj što je u uobičajenim problemima početni oblik $U$ prilično poseban, pa njegove potencije imaju jednostavniji oblik i ne treba ih računati brzim potenciranjem. Primjerice, u primjeru iz glavnog teksta rezultat $U^{\lfloor b/c\rfloor}$ dobiva se tako da se onaj $1$ u $U$ koji nije na dijagonali zamijeni s $\lfloor b/c\rfloor$, bez računanja brzim potenciranjem.
