---
title: Catalanovi brojevi
---

## Uvod

Catalanovi brojevi često se pojavljuju u raznim problemima prebrojavanja. Belgijski matematičar Eugène Charles Catalan otkrio je ovaj niz 1958. proučavajući problem prebrojavanja nizova zagrada, pa je niz po njemu i dobio ime. Minggatu, matematičar iz dinastije Qing, otkrio je ovaj niz već 1730-ih godina.

Catalanovi brojevi zadovoljavaju sljedeću rekurzivnu relaciju:

$$
C_n = \begin{cases}
1, & n = 0, \\
\sum_{i=0}^{n-1} C_{i}C_{n-1-i}, & n > 0.
\end{cases}\tag{1}
$$

Prvih nekoliko članova niza ([OEIS: A000108](https://oeis.org/A000108), indeksi počinju od $0$):

$$
1,1,2,5,14,42,132,429,1430,\ldots
$$

## Primjene

Rekurzivna relacija Catalanovih brojeva $C_n$ ima prirodnu rekurzivnu strukturu: problem prebrojavanja $C_n$ veličine $n$ može se, prolaskom po točki razdvajanja, rastaviti na dva potproblema veličina $i$ i $(n-1-i)$. Zbog te se rekurzivne relacije Catalanovi brojevi pojavljuju u mnogim problemima sa sličnom rekurzivnom strukturom.

-   **Prebrojavanje putova**: zadana je kvadratna mreža veličine $n\times n$ s donjim lijevim kutom $(0, 0)$ i gornjim desnim kutom $(n, n)$. Krećemo iz donjeg lijevog kuta, u svakom koraku smijemo ići samo za jednu jedinicu udesno ili prema gore, i ne smijemo prijeći iznad dijagonale $y=x$ (smijemo je dodirnuti). Ukupan broj putova do gornjeg desnog kuta jest $C_n$.

    ??? note "Dokaz"
        Neka je broj načina $T_n$. Promotrimo slučaj $n \ge 2$. Neka je točka u kojoj put **prvi put** dođe na dijagonalu $y=x$ točka $(k,k)~(k \in [1,n])$. Promotrimo putove od $(0,0)$ do $(k,k)$ čije međutočke, osim početka i kraja, **ne prolaze dijagonalom (ne smiju je dodirnuti)**.
        
        ![catalan2](./images/catalan-2.svg)
        
        Kao što prikazuje slika, prvi je korak takvih putova nužno udesno, od $(0,0)$ do $(1,0)$, a posljednji je korak nužno prema gore, od $(k,k-1)$ do $(k,k)$. Stoga su ti putovi upravo putovi od $(1,0)$ do $(k,k-1)$ koji ne prelaze pravac $y=x-1$, pa ih ima $T_{k-1}$. Istodobno, broj dopuštenih putova od $(k,k)$ do $(n,n)$ jest $T_{n-k}$. Prema principu umnoška, broj putova koji prvi put dodirnu dijagonalu u $(k,k)$ jest $T_{k-1} T_{n-k}$. Prolaskom po svim mogućnostima za $k$ ukupan broj dopuštenih putova iznosi
        
        $$
        T_n = \sum_{k=1}^n T_{k-1}T_{n-k}.
        $$
        
        Supstitucijom $k=i+1$ vidi se da je to upravo rekurzivna relacija Catalanovih brojeva. Iz $T_0=1$ slijedi $T_n = C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Prebrojavanje tetiva u kružnici koje se ne sijeku**: na kružnici je $2n$ točaka. Broj načina da se te točke spoje u parove tako da se dobivenih $n$ dužina međusobno ne sijeku jest $C_n$.

    ??? note "Dokaz"
        Označimo broj načina za $2n$ točaka s $T_n$. Numerirajmo $2n$ točaka u smjeru kazaljke na satu brojevima $1,2,\ldots,2n$. Budući da se tetive međusobno ne sijeku, točka $1$ može se spojiti samo s točkom parnog broja; inače se neparan broj točaka između njih ne bi mogao upariti bez presijecanja spojnice tih dviju točaka. Ako spojimo $1$ i $2k~(k\in[1,n])$, s lijeve je strane $2k-2$ točaka, a s desne $2n-2k$ točaka, pa je prema principu umnoška broj takvih načina $T_{k-1}T_{n-k}$. Stoga, prolaskom po $k$, vrijedi $T_n = \sum_{k=1}^n T_{k-1} T_{n-k}$. Uz $k=i+1$ dobivamo rekurzivnu relaciju Catalanovih brojeva. Iz $T_0=1$ slijedi $T_n=C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Prebrojavanje triangulacija**: broj načina da se konveksni $(n+2)$-terokut podijeli na trokute dijagonalama koje se ne sijeku jest $C_n$.

    ??? note "Dokaz"
        Neka je broj triangulacija $(n+2)$-terokuta $T_n$. Najprije odaberimo stranicu $(1,n+2)$ kao osnovicu; ona nužno pripada nekom trokutu, a treći vrh tog trokuta označimo $k~(k\in[2,n+1])$. Tako se izvorni konveksni mnogokut raspada na tri dijela:
        
        -   trokut $(1,k,n+2)$;
        -   $k$-terokut s vrhovima $1\sim k$;
        -   $(n+3-k)$-terokut s vrhovima $k\sim (n+2)$.
        
        Posljednja su dva dijela potproblemi, pa vrijedi rekurzivna relacija
        
        $$
        T_n = \sum_{k=2}^{n+1} T_{k-2}T_{n+1-k}.
        $$
        
        Uz $k=i+2$ dobivamo rekurzivnu relaciju Catalanovih brojeva. Iz $T_0=T_1=1$ slijedi $T_n=C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Prebrojavanje binarnih stabala**: broj različitih oblika binarnih stabala s $n$ čvorova jest $C_n$. Ekvivalentno, broj različitih oblika punih binarnih stabala s $n$ unutarnjih čvorova (koji nisu listovi) jest $C_{n}$.

    ??? note "Dokaz"
        Označimo broj binarnih stabala s $n$ čvorova s $T_n$. Uzmimo bilo koji korijen i prođimo po veličinama lijevog i desnog podstabla. Ako je veličina lijevog podstabla $i\in[0,n-1]$, veličina desnog podstabla je $(n-1-i)$. Lijevo i desno podstablo oba su potproblemi, pa vrijedi rekurzivna relacija
        
        $$
        T_n = \sum_{i=0}^{n-1}T_iT_{n-1-i}.
        $$
        
        To je upravo rekurzivna relacija Catalanovih brojeva. Iz $T_0=T_1=1$ slijedi $T_n=C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Prebrojavanje nizova zagrada**: broj ispravnih nizova zagrada sastavljenih od $n$ parova zagrada jest $C_n$.

    ??? note "Dokaz"
        Povežimo to s problemom prebrojavanja putova. Lijevu zagradu promatramo kao korak prema gore, a desnu kao korak udesno. Niz zagrada ispravan je ako na svakoj poziciji broj lijevih zagrada nije manji od broja desnih. To odgovara uvjetu u problemu prebrojavanja putova da u svakom trenutku broj koraka prema gore nije manji od broja koraka udesno. Stoga postoji bijekcija između ispravnih nizova zagrada i dopuštenih putova. Broj ispravnih nizova zagrada također je $C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Prebrojavanje redoslijeda skidanja sa stoga**: redoslijed stavljanja na (neograničeni) stog je $1,2,3, \ldots ,n$. Broj ispravnih redoslijeda skidanja sa stoga jest $C_n$.

    ??? note "Dokaz"
        Povežimo to s problemom prebrojavanja nizova zagrada. Stavljanje na stog promatramo kao lijevu zagradu, a skidanje sa stoga kao desnu. U svakom trenutku broj stavljanja na stog nije manji od broja skidanja. Stoga postoji bijekcija između ispravnih redoslijeda skidanja sa stoga i ispravnih nizova zagrada. Broj ispravnih redoslijeda skidanja također je $C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Prebrojavanje nizova**: među nizovima $a_1,a_2, \ldots ,a_{2n}$ sastavljenima od $n$ jedinica $+1$ i $n$ jedinica $-1$, broj onih čije parcijalne sume zadovoljavaju $a_1+a_2+ \ldots +a_k \geq 0~(k=1,2,3, \ldots ,2n)$ jest $C_n$.

    ??? note "Dokaz"
        Povežimo to s problemom prebrojavanja nizova zagrada. $+1$ promatramo kao lijevu zagradu, a $-1$ kao desnu. U svakom trenutku broj članova $+1$ nije manji od broja članova $-1$. Stoga postoji bijekcija između dopuštenih nizova i ispravnih nizova zagrada. Broj dopuštenih nizova također je $C_n$.

Iako se ova rekurzivna relacija široko primjenjuje, njezino je izravno računanje prilično složeno, pa treba potražiti jednostavnije formule.

## Uobičajeni oblici

Catalanovi brojevi imaju sljedeće uobičajene izraze:

$$
C_n = \frac{1}{n+1}\binom{2n}{n} = \dfrac{(2n)!}{n!(n+1)!},~ n\ge 0. \tag{2}
$$

$$
C_n = \binom{2n}{n} - \binom{2n}{n+1},~n \ge 0. \tag{3}
$$

$$
C_n = \frac{(4n-2)}{n+1}C_{n-1},~ n > 0,~ C_0 = 1. \tag{4}
$$

Svi se ovi oblici Catalanovih brojeva mogu učinkovito računati: prva dva svode ih na računanje faktorijela i binomnih koeficijenata, a treći daje rekurzivnu formulu za računanje redom.

Za ova tri uobičajena oblika u ovom članku dajemo dva načina dokazivanja.

### Algebarsko izvođenje

Algebarsko izvođenje gornjih izraza za Catalanove brojeve ima dva koraka. Najprije provjeravamo da su ta tri oblika međusobno ekvivalentna.

??? note "Dokaz ekvivalencije izraza $(2)\sim(4)$"
    Dovoljno je dokazati da se izraz $(3)$ može prevesti u oblik s faktorijelima iz izraza $(2)$:
    
    $$
    \begin{aligned}
    C_n &= \binom{2n}{n} - \binom{2n}{n+1} \\
    &= \frac{(2n)!}{n!n!} - \frac{(2n)!}{(n-1)!(n+1)!} \\
    &= \frac{(2n)!}{n!n!}\left(1 - \frac{n!}{(n-1)!(n+1)}\right) \\
    &= \frac{(2n)!}{n!n!}\left(1- \frac{n}{n+1}\right) \\
    &= \dfrac{(2n)!}{n!(n+1)!}.
    \end{aligned}
    $$
    
    Također, i izraz $(4)$ može se prevesti u oblik s faktorijelima iz izraza $(2)$:
    
    $$
    C_n = \prod_{i=1}^n\frac{(4i-2)}{i+1} = \prod_{i=1}^n\frac{2i(2i-1)}{i(i+1)} = \dfrac{(2n)!}{n!(n+1)!}.
    $$
    
    Dakle, ta su tri izraza međusobno ekvivalentna.

Zatim provjeravamo da su ti oblici doista rješenja rekurzivne formule Catalanovih brojeva. U tu svrhu metodom funkcija izvodnica izravno rješavamo rekurzivnu formulu $(1)$.

??? note "Rješavanje rekurzivne formule $(1)$ metodom funkcija izvodnica"
    Promotrimo običnu funkciju izvodnicu Catalanovih brojeva $C(x)=\sum_{n=0}^{\infty}C_nx^n$. Budući da rekurzivna relacija Catalanovih brojeva vrlo nalikuje obliku konvolucije, pokušajmo pomoću konvolucije sastaviti jednadžbu za $C(x)$:
    
    $$
    \begin{aligned}
    C(x)&=\sum_{n=0}^{\infty}C_nx^n\\
    &=1+\sum_{n=1}^{\infty}\left(\sum_{i=0}^{n-1}C_iC_{n-i-1}\right)x^{n}\\
    &=1+x\sum_{n=1}^{\infty}\sum_{i=0}^{n-1}C_ix^iC_{n-i-1}x^{n-i-1}\\
    &=1+x\sum_{i=0}^{\infty}C_ix^i\sum_{j=0}^{\infty}C_jx^j\\
    &=1+xC^2(x).
    \end{aligned}
    $$
    
    Pritom je u pretposljednjoj jednakosti zamijenjen redoslijed sumiranja i stavljeno $j=n-1-i$. Odatle rješavanjem dobivamo:
    
    $$
    C(x)=\dfrac{1\pm \sqrt{1-4x}}{2x} = \frac{2}{1\mp \sqrt{1-4x}}.
    $$
    
    Iz početnog uvjeta $C_0=1$ slijedi $C(0)=1$. Uvrštavanjem se vidi da je jedino moguće rješenje
    
    $$
    C(x) = \dfrac{1- \sqrt{1-4x}}{2x}.
    $$
    
    Zatim to treba razviti u red potencija. Prema [razvoju u red potencija](../poly/intro.md#uobičajeni-razvoji-u-red-potencija) funkcije $(1+x)^a$ vrijedi:
    
    $$
    \sqrt{1-4x} = \sum_{n=0}^{\infty} \dfrac{\left(\frac{1}{2}\right)_{-n}}{n!}(-4x)^n,
    $$
    
    gdje je $\left(\dfrac{1}{2}\right)_{-n}$ padajuća faktorijelna potencija:
    
    $$
    \begin{aligned}
    \left(\frac{1}{2}\right)_{-n} &= \prod_{k=0}^{n-1}\left(\dfrac{1}{2}-k\right) = \dfrac{1}{2^n}\prod_{k=1}^{n-1}(1-2k) = \dfrac{(-1)^{n-1}}{2^n}\prod_{k=1}^{n-1}(2k-1)\\
    &= \dfrac{(-1)^{n-1}}{2^{2n-1}}\prod_{k=1}^{n-1}\dfrac{(2k-1)2k}{k} = \dfrac{(-1)^{n-1}}{2^{2n-1}}\dfrac{(2n-2)!}{(n-1)!}.
    \end{aligned}
    $$
    
    Uvrštavanjem u izraz za $C(x)$ dobivamo
    
    $$
    \begin{aligned}
    C(x) &= \dfrac{1}{2x}\left(1-\sum_{n=0}^{\infty} \dfrac{\left(\frac{1}{2}\right)_{-n}}{n!}(-4x)^n\right)\\
    &= -\dfrac{1}{2x}\sum_{n=1}^\infty \dfrac{(-4x)^n}{n!}\left(\frac{1}{2}\right)_{-n} \\
    &= -\dfrac{1}{2x}\sum_{n=1}^\infty \dfrac{(-4x)^n}{n!}\dfrac{(-1)^{n-1}}{2^{2n-1}}\dfrac{(2n-2)!}{(n-1)!} \\
    &= \sum_{n=1}^{\infty}\dfrac{(2n-2)!}{(n-1)!n!}x^{n-1}\\
    &= \sum_{n=0}^{\infty}\dfrac{(2n)!}{n!(n+1)!}x^n.
    \end{aligned}
    $$
    
    Time smo dobili izraz $(2)$ za $C_n$.

### Kombinatorno značenje

Budući da Catalanovi brojevi imaju jasno kombinatorno značenje, ti se oblici mogu dokazati i isključivo metodama kombinatornog prebrojavanja. U ovom odjeljku za svaki od triju izraza dajemo po jedan kombinatorni dokaz.

??? note "Dokaz izraza $(2)$"
    Promotrimo problem prebrojavanja nizova. Za proizvoljan niz $\{a_i\}_{i=1}^{2n}$ sastavljen od $\pm 1$ definirajmo njegove parcijalne sume $S_i = \sum_{j=1}^{i}a_i$ i definirajmo njegov **višak** (exceedance) kao broj indeksa za koje je $S_i < 0$ i $a_i = -1$. Višak jednak $0$ ekvivalentan je tome da je niz dopušten; višak poprima vrijednosti iz $[0,n]$, dakle ukupno $(n+1)$ mogućih vrijednosti. Treba dokazati da je broj nizova s različitim vrijednostima viška zapravo jednak.
    
    U tu svrhu konstruiramo preslikavanje $f$ s nizova viška $e > 0$ na nizove viška $(e-1)$. Za niz $\{a_i\}$ viška $e > 0$ neka je $k$ najmanji indeks za koji vrijedi $S_i = 0$ i $a_i = +1$. Zamijenimo li dijelove niza lijevo i desno od $a_k$, dobivamo sljedeći niz $\{a'_i\}$:
    
    $$
    a_{k+1},a_{k+2},\cdots,a_{2n},a_k,a_{1},a_{2},\cdots,a_{k-1}.
    $$
    
    Budući da se niz parcijalnih suma koji odgovara dijelu izvornog niza desno od $a_k$ zamjenom ne mijenja, ne mijenja se ni njegov doprinos višku. Dijelu izvornog niza lijevo od $a_k$ parcijalne se sume nakon zamjene sve povećaju za $1$, pa se njegov doprinos višku smanjuje, i to točno za broj indeksa u dijelu izvornog niza lijevo od $a_k$ za koje je $S_i=-1$ i $a_i=-1$. Budući da izbor $a_k$ jamči da postoji točno jedan takav indeks, višak niza $\{a'_i\}$ jednak je $(e-1)$. Drugim riječima, preslikavanje $f$ smanjuje višak niza za točno $1$.
    
    Preslikavanje $f$ je invertibilno. Primijetimo da je u nizu $\{a'_i\}$ pozicija koja odgovara $a_k$ upravo najveći indeks za koji vrijedi $S'_k=+1$ i $a'_i = +1$. To je zato što su nakon zamjene te parcijalne sume točno za $1$ veće od odgovarajućih parcijalnih suma prije zamjene, pa sadašnja parcijalna suma $+1$ odgovara parcijalnoj sumi $0$ prije zamjene. No prema izboru $k$, u tom dijelu (tj. u dijelu izvornog niza lijevo od $a_k$) prije zamjene nema indeksa za koji vrijedi $S_i = 0$ i $a_i = +1$.
    
    Time preslikavanje $f$ čini bijekciju između nizova viška $e>0$ i nizova viška $(e-1)$. To pokazuje da je broj nizova s različitim vrijednostima viška zapravo jednak. Budući da je ukupan broj nizova $\dbinom{2n}{n}$, broj dopuštenih nizova (tj. nizova viška $0$) jednak je
    
    $$
    C_n = \dfrac{1}{n+1}\dbinom{2n}{n}.
    $$
    
    Time je dokazan izraz $(2)$ za Catalanove brojeve.

??? note "Dokaz izraza $(3)$"
    Promotrimo problem prebrojavanja putova. To je tipičan problem prebrojavanja rešetkastih putova koji se može riješiti principom refleksije. Konkretno, u ovom problemu od ukupnog broja putova oduzimamo broj nedopuštenih putova. Ukupno treba napraviti $2n$ koraka, od kojih je $n$ udesno, pa je ukupan broj putova $\dbinom{2n}{n}$. Put je nedopušten ako i samo ako dodiruje pravac $y = x+1$. Za svaki nedopušteni put možemo pronaći mjesto na kojem prvi put dodiruje pravac $y = x+1$ i dio puta nakon tog mjesta zrcaliti s obzirom na pravac $y=x+1$. Tada se vidi da nedopušteni put od $(0,0)$ do $(n,n)$ postaje put od $(0,0)$ do $(n-1,n+1)$.
    
    ![catalan1](./images/catalan-1.svg)
    
    Budući da put od $(0,0)$ do $(n-1,n+1)$ nužno prelazi pravac $y = x+1$, svaki takav put odgovara jednom nedopuštenom putu od $(0,0)$ do $(n,n)$. Analogno računanju ukupnog broja putova, ukupan broj nedopuštenih putova jest $\dbinom{2n}{n+1}$. Stoga je ukupan broj dopuštenih putova
    
    $$
    C_n = \binom{2n}{n} - \binom{2n}{n+1}.
    $$
    
    To je upravo izraz $(3)$ za Catalanove brojeve.

??? note "Dokaz izraza $(4)$"
    Promotrimo problem prebrojavanja triangulacija. Neka je $P$ konveksni $(n+2)$-terokut i fiksirajmo jednu njegovu stranicu kao osnovicu. Za svaku triangulaciju mnogokuta $P$ možemo odabrati jedan njezin brid koji nije osnovica (uključujući bridove dodane triangulacijom), označiti ga i orijentirati. Ukupno postoji $(4n+2)C_n$ takvih triangulacija s oznakom. Neka je nadalje $Q$ konveksni $(n+3)$-terokut i opet fiksirajmo jednu njegovu stranicu kao osnovicu. Za mnogokut $Q$ možemo odabrati jednu stranicu koja nije osnovica, označiti je, a zatim napraviti triangulaciju. Ukupno postoji $(n+2)C_{n+1}$ takvih oznaka s triangulacijom.
    
    ![](./images/catalan-triangulation.svg)
    
    Kao što prikazuje slika, između rezultata tih dviju skupina operacija postoji očita bijekcija. Za jedan rezultat triangulacije i označavanja mnogokuta $P$ možemo označeni brid proširiti u trokut tako da krajnju točku na koju pokazuje orijentacija proširimo u novu stranicu i tu novu stranicu označimo, čime dobivamo jedan rezultat označavanja i triangulacije mnogokuta $Q$; za jedan rezultat označavanja i triangulacije mnogokuta $Q$ možemo označenu stranicu sažeti u jednu točku, a dijagonalu dobivenu sažimanjem označiti i orijentirati prema vrhu dobivenom sažimanjem, čime dobivamo jedan rezultat triangulacije i označavanja mnogokuta $P$. Stoga
    
    $$
    (4n+2)C_n = (n+2)C_{n+1}.
    $$
    
    Malim sređivanjem i uz $C_0=1$ dobivamo izraz $(4)$ za Catalanove brojeve.

## Primjer zadatka

???+ example "[Luogu P1044 栈 (Stog)](https://www.luogu.com.cn/problem/P1044)"
    Redoslijed stavljanja na stog je $1,2,\ldots ,n$. Odredite ukupan broj svih mogućih redoslijeda skidanja sa stoga.

??? note "Referentni kôd"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/combinatorics/catalan/catalan_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/combinatorics/catalan/catalan_1.py"
        ```

## Zadaci za vježbu

-   [Luogu P2532 \[AHOI2012\] 树屋阶梯 (Stube do kućice na drvetu)](https://www.luogu.com.cn/problem/P2532)
-   [Luogu P1641 \[SCOI2010\] 生成字符串 (Generiranje niza znakova)](https://www.luogu.com.cn/problem/P1641)
-   [Luogu P3200 \[HNOI2009\] 有趣的数列 (Zanimljiv niz)](https://www.luogu.com.cn/problem/P3200)
-   [AtCoder Beginner Contest 205 E - White and Black Balls](https://atcoder.jp/contests/abc205/tasks/abc205_e)
-   [AtCoder Regular Contest 145 C - Split and Maximize](https://www.luogu.com.cn/problem/AT_arc145_c)
-   [Luogu P5014 水の三角（修改版）(Vodeni trokut, izmijenjena inačica)](https://www.luogu.com.cn/problem/P5014)
-   [Luogu P3978 \[TJOI2015\] 概率论 (Teorija vjerojatnosti)](https://www.luogu.com.cn/problem/P3978)

## Literatura i bilješke

-   [Catalan number - Wikipedia](https://en.wikipedia.org/wiki/Catalan_number)
