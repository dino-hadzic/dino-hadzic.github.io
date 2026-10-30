---
title: Mali Fermatov teorem & Eulerov teorem
---

U ovom se članku razmatraju mali Fermatov teorem, Eulerov teorem i njegovo proširenje. Ti teoremi rješavaju problem računanja potencija s proizvoljno velikim eksponentom po proizvoljnom modulu.

## Mali Fermatov teorem

**Mali Fermatov teorem** (Fermat's little theorem) jedan je od najosnovnijih teorema teorije brojeva. On je ujedno i teorijska podloga [Fermatova testa prostosti](./prime.md#fermat-素性测试).

???+ note "Mali Fermatov teorem"
    Neka je $p$ prost broj. Za svaki cijeli broj $a$ takav da $p\nmid a$ vrijedi $a^{p-1}\equiv 1\pmod p$.

???+ note "Teorem"
    Neka je $p$ prost broj. Za svaki cijeli broj $a$ vrijedi $a^{p}\equiv a\pmod p$.

Ove su dvije kongruencije ekvivalentne kad $p\nmid a$; a kad $p\mid a$, kongruencija $a^p\equiv 0\equiv a\pmod p$ vrijedi trivijalno. Stoga su ove dvije tvrdnje ekvivalentne. Obje se tvrdnje često nazivaju malim Fermatovim teoremom.

??? note "Prvi dokaz"
    Neka je $p$ prost broj i $p\nmid a$. Najprije dokazujemo: za $i=1,2,\cdots,p-1$ ostatci $ia \bmod p$ međusobno su različiti. Dokaz provodimo kontradikcijom. Kad bi postojali $1\le i < j < p$ takvi da
    
    $$
    ia \bmod p = ja \bmod p \iff (j-i)a\equiv 0.\pmod p
    $$
    
    No ni $(j-i)$ ni $a$ nisu višekratnici od $p$, što je očita kontradikcija.
    
    Drugim riječima, ti ostatci čine permutaciju skupa $\{1,2,\cdots,p-1\}$. Stoga vrijedi
    
    $$
    \prod_{i=1}^{p-1}i = \prod_{i=1}^{p-1}(ia\bmod p) \equiv \prod_{i=1}^{p-1}ia = a^{p-1}\prod_{i=1}^{p-1}i.\pmod p
    $$
    
    To znači
    
    $$
    (a^{p-1}-1)\prod_{i=1}^{p-1}i \equiv 0. \pmod{p}
    $$
    
    Dakle, lijeva je strana jednakosti višekratnik od $p$, ali nijedan od $i=1,2,\cdots, p-1$ nije višekratnik od $p$, pa mora biti $p\mid (a^{p-1}-1)$, odnosno vrijedi mali Fermatov teorem.

??? note "Drugi dokaz"
    Uočimo da druga formulacija malog Fermatova teorema vrijedi za sve $a\in\mathbf N$, pa možemo razmotriti matematičku indukciju. Slučaj negativnih cijelih brojeva lako se svodi na slučaj nenegativnih.
    
    Baza indukcije je $0^p\equiv 0\pmod p$, što očito vrijedi. Pretpostavimo da tvrdnja vrijedi za $a\in\mathbf N$; treba dokazati da vrijedi i za $a+1$. Prema binomnom teoremu
    
    $$
    (a+1)^p=a^p+\binom{p}{1}a^{p-1}+\binom{p}{2}a^{p-2}+\cdots +\binom{p}{p-1}a+1.
    $$
    
    Osim prvog i posljednjeg člana, u izrazu za binomni koeficijent $\dbinom{p}{k} = \dfrac{p!}{k!(p-k)!}$ broj $p$ dijeli brojnik, a ne dijeli nazivnik, pa su ti koeficijenti za $k\neq 0,p$ višekratnici od $p$. Stoga vrijedi
    
    $$
    (a+1)^p \equiv a^p + 1\equiv a + 1. \pmod{p}
    $$
    
    Pritom je u drugom koraku primijenjena pretpostavka indukcije. Dakle, po matematičkoj indukciji mali Fermatov teorem vrijedi.

Obrat malog Fermatova teorema ne vrijedi. Čak i ako za sve $a$ relativno proste s $n$ vrijedi $a^{n-1}\equiv 1\pmod n$, $n$ ne mora biti prost. Više o tome u odjeljku [Fermatov test prostosti](./prime.md#fermat-素性测试).

## Eulerov teorem

**Eulerov teorem** (Euler's theorem) poopćuje mali Fermatov teorem na slučaj općeg modula, ali i dalje zahtijeva da baza i modul budu relativno prosti.

???+ note "Eulerov teorem"
    Za cijeli broj $m>0$ i cijeli broj $a$ takve da je $\gcd(a,m)=1$ vrijedi $a^{\varphi(m)}\equiv 1\pmod{m}$, gdje je $\varphi(\cdot)$ [Eulerova funkcija](./euler-totient.md).

??? note "Dokaz"
    Slično kao u prvom dokazu malog Fermatova teorema, opet uzimamo niz brojeva relativno prostih s $m$ i zatim provodimo odgovarajuće operacije. Promotrimo skup
    
    $$
    R = \{r\in\mathbf N : 0 < r < m,~\gcd(r,m)=1\}.
    $$
    
    To je [reducirani sustav ostataka](./basic.md#同余类与剩余系) modulo $m$. Prema definiciji Eulerove funkcije vrijedi $|R|=\varphi(m)$. Slično kao gore, množenje tih brojeva s $a$ odgovara permutaciji tog skupa:
    
    $$
    R = \{ar\bmod m: r\in R\}.
    $$
    
    Naime, lako se provjeri da je $\gcd(ar,m)=1$ te da različitim $r_1,r_2\in R$ odgovaraju različiti $ar_1\bmod m$ i $ar_2\bmod m$. Stoga vrijedi
    
    $$
    \prod_{r\in R}r \equiv \prod_{r\in R}ar = a^{\varphi(m)}\prod_{r\in R}r. \pmod{m}
    $$
    
    Ponavljajući prethodni argument i kratimo $\prod_{r\in R}r$, dobivamo $a^{\varphi(m)}\equiv 1\pmod m$.

Za prost broj $p$ vrijedi $\varphi(p)=p-1$, pa je mali Fermatov teorem poseban slučaj Eulerova teorema. Osim toga, eksponent $\varphi(m)$ u Eulerovu teoremu općenito nije najmanji eksponent za koji ta kongruencija vrijedi. Može se poboljšati na $\lambda(m)$, gdje je $\lambda(\cdot)$ [Carmichaelova funkcija](./primitive-root.md#carmichael-函数). Za algebarsku pozadinu srodnih rezultata vidi odjeljak [Multiplikativna grupa klasa ostataka cijelih brojeva](../algebra/ring-theory.md#应用整数同余类的乘法群).

## Prošireni Eulerov teorem

Prošireni Eulerov teorem[^ex-euler] dodatno poopćuje rezultat na slučaj kad baza i modul nisu relativno prosti. Time u potpunosti rješava problem računanja potencija proizvoljne baze po proizvoljnom modulu: svodi ih na slučaj eksponenta manjeg od $2\varphi(m)$, pa se mogu izračunati [brzim potenciranjem](../binary-exponentiation.md) u vremenu $O(\log\varphi(m))$.

???+ note "Prošireni Eulerov teorem"
    Za svaki pozitivni cijeli broj $m$, cijeli broj $a$ i nenegativni cijeli broj $k$ vrijedi
    
    $$
    a^k \equiv \begin{cases}
    a^{k \bmod \varphi(m)},                &\gcd(a,m) =  1,                   \\
    a^k,                                   &\gcd(a,m)\ne 1, k <   \varphi(m), \\
    a^{(k \bmod \varphi(m)) + \varphi(m)}, &\gcd(a,m)\ne 1, k \ge \varphi(m).
    \end{cases} \pmod m
    $$

Drugi slučaj kaže da, ako je $k < \varphi(m)$, nema potrebe dalje smanjivati eksponent, nego se izravno primjenjuje brzo potenciranje; a najveća razlika između trećeg i prvog slučaja jest treba li, nakon smanjenja eksponenta uzimanjem ostatka, dodati još član $\varphi(m)$. Dakako, ispravno je i prvi slučaj spojiti s drugim i trećim.

### Intuitivno razumijevanje

Prije strogog dokaza teorema možemo najprije intuitivno razumjeti njegovo značenje.

![fermat1](./images/fermat.svg)

Promotrimo kako se ostatak $a^k\bmod m$ mijenja kako $k$ raste. Budući da ostatak nužno leži u intervalu $[0,m)$, a vrijednosti $k$ ima beskonačno mnogo, promatrajmo $a^k\bmod m \mapsto a^{k+1}\bmod m$ kao usmjerene bridove između čvorova-ostataka. Tada nužno nastaje ciklus kao na slici.

Prošireni Eulerov teorem kaže da ti ciklusi mogu biti čisti ciklusi (prvi slučaj) ili miješani ciklusi (drugi i treći slučaj). U čistom ciklusu nijedan čvor nema dva prethodnika, dok se u miješanom ciklusu takva situacija pojavljuje. Stoga je u općem slučaju dovoljno odrediti duljinu ciklusa i duljinu puta prije ulaska u ciklus pa pomoću tog svojstva smanjiti eksponent.

### Strogi dokaz

U ovom odjeljku dajemo strogi dokaz proširenog Eulerova teorema.

??? note "Dokaz"
    Najprije pokazujemo da postoji $k_0\in\mathbf N$ takav da su cijeli broj $a$ i $m':=\dfrac{m}{\gcd(a^{k_0},m)}$ relativno prosti. U tu svrhu neka je $\nu_p(n)$ eksponent prostog broja $p$ u rastavu cijelog broja $n$ na proste faktore; tada bez smanjenja općenitosti možemo uzeti
    
    $$
    k_0 = \max\left\{\left\lceil\dfrac{\nu_p(m)}{\nu_p(a)}\right\rceil : \nu_p(a)>0\right\}.
    $$
    
    Budući da su eksponenti svih prostih faktora zajedničkih brojevima $m$ i $a$ već sadržani u $a^{k_0}$, broj $a$ relativno je prost s preostalim faktorom $m'=\dfrac{m}{\gcd(a^{k_0},m)}$ broja $m$.
    
    Nadalje, za $k\ge k_0$ promotrimo kongruenciju
    
    $$
    b\equiv a^k. \pmod m
    $$
    
    Budući da $\gcd(a^{k_0},m)=\gcd(a^k,m)\mid b$, dijeljenjem obiju strana (uključujući modul) s $\gcd(a^{k_0},m)$ dobivamo
    
    $$
    \dfrac{b}{\gcd(a^{k_0},m)} \equiv \dfrac{a^{k_0}}{\gcd(a^{k_0},m)}\cdot a^{k-k_0}. \pmod{m'}
    $$
    
    Sada, budući da je $a$ relativno prost s modulom $m'$, možemo izravno primijeniti Eulerov teorem i dobiti
    
    $$
    \dfrac{b}{\gcd(a^{k_0},m)} \equiv \dfrac{a^{k_0}}{\gcd(a^{k_0},m)}\cdot a^{(k-k_0)\bmod\varphi(m')}. \pmod{m'}
    $$
    
    Stoga, množeći natrag faktorom $\gcd(a^{k_0},m)$, dobivamo
    
    $$
    b \equiv a^{k_0}\cdot a^{(k-k_0)\bmod\varphi(m')} = a^{k_0 + (k-k_0)\bmod\varphi(m')}. \pmod{m}
    $$
    
    Time smo dobili oblik proširenog Eulerova teorema. Formula kaže da je duljina ciklusa $\varphi(m')$, a duljina puta prije ulaska u ciklus $k_0$.
    
    Ovdje dobiveni parametri stroži su od onih u proširenom Eulerovu teoremu, ali ih je razmjerno teško izračunati. Može se pokazati da se ti parametri mogu olabaviti do onih iz proširenog Eulerova teorema. Prvo, prema [formuli za Eulerovu funkciju](./euler-totient.md), budući da $m'\mid m$, vrijedi $\varphi(m')\mid\varphi(m)$. Dakle, i $\varphi(m)$ je duljina ciklusa. Drugo, i $k_0$ se može olabaviti do $\varphi(m)$. Naime, za sve $m\in\mathbf N_+$ i svaki $p\mid m$ vrijedi
    
    $$
    \begin{aligned}
    \varphi(m) &\ge \varphi(p^{\nu_p(m)}) = (p-1)p^{\nu_p(m)-1} \ge p^{\nu_p(m)-1} \\
    &= (1+(p-1))^{\nu_p(m)-1} \ge 1 + (p-1)(\nu_p(m)-1) \\
    &\ge 1 + (\nu_p(m)-1) = \nu_p(m).
    \end{aligned}
    $$
    
    Pritom nejednakost u drugom retku koristi binomni razvoj, zadržavajući samo konstantni i linearni član. Stoga vrijedi
    
    $$
    k_0 \le \max\{\nu_p(m):p\in\mathbf P\}\le \varphi(m).
    $$
    
    Time je tvrdnja u potpunosti dokazana.

## Primjer zadatka

U ovom odjeljku na jednom primjeru pokazujemo klasičnu primjenu proširenog Eulerova teorema: računanje potencijskog tornja po proizvoljnom modulu. **Potencijski toranj** (power tower) izraz je oblika $A\uparrow(B\uparrow(C\uparrow(D\uparrow\cdots)))$, gdje je $\uparrow$ Knuthova strelica, a $A,B,C,D,\cdots$ niz nenegativnih cijelih brojeva.

???+ example "[Library Checker - Tetration Mod](https://judge.yosupo.jp/problem/tetration_mod)"
    Zadano je $T$ testnih primjera. U svakom su zadani $A,B,M$; treba izračunati $(A\uparrow\uparrow B)\bmod M$. Pritom $A\uparrow\uparrow B$ označava potencijski toranj sastavljen od $B$ brojeva $A$. Formalno, definiramo
    
    $$
    A \uparrow\uparrow B =
    \begin{cases}
    1 , & B = 0,\\
    A\uparrow(A\uparrow\uparrow(B-1)), & B > 0.
    \end{cases}
    $$
    
    Dogovorno je $0^0=1$.

??? note "Rješenje"
    Koristeći definiciju $A\uparrow\uparrow B$, dovoljno je računati rekurzivno. Da bismo izračunali $(A\uparrow\uparrow B)\bmod M$, samo primijenimo prošireni Eulerov teorem i izračunamo $(A\uparrow\uparrow(B-1))\bmod\varphi(M)$. Budući da $\varphi(\varphi(n)) \le n/2$ vrijedi za sve $n\ge 2$, rekurzija sigurno završava u $O(\log M)$ koraka. Budući da primjenjujemo prošireni Eulerov teorem, moramo razlikovati je li trenutačni rezultat strogo manji od trenutačnog modula. Za to je dovoljno pri uzimanju ostatka napraviti još jednu provjeru. Osim toga, treba paziti na obradu rubnih slučajeva.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/fermat/tetration.cpp"
    ```

??? warning "Dokaz ispravnosti trika s uzimanjem ostatka"
    Ova implementacija umjesto uzimanja ostatka koristi
    
    $$
    r_m(v) = \begin{cases} v\bmod m, &\text{if }v < m, \\ v \bmod m + m, &\text{if }v \ge m\end{cases}
    $$
    
    što je ekvivalentno istodobnom bilježenju informacije o ostatku $v\bmod m$ i informacije o prekoračenju $v \ge m$. Prošireni Eulerov teorem jamči samo da, kad su i informacija o ostatku i informacija o prekoračenju eksponenta točne, potenciranje daje točnu informaciju o ostatku; točnost informacije o prekoračenju, međutim, ne može se jamčiti. Na primjer, pri računanju $r_6(2^4)$ eksponent treba uzeti modulo $\varphi(6)=2$, a $r_2(4)=2$ (tj. ostatak je $0$ i došlo je do prekoračenja), pa nakon potenciranja dobivamo $r_6(2^2) = 4$; u usporedbi s točnim odgovorom $r_6(2^4) = 10$, ostatak modulo $6$ je točan, ali je informacija o prekoračenju izgubljena. Ipak, može se dokazati da je, iako se informacija o prekoračenju može izgubiti, informacija o ostatku uvijek točna. Stoga je i algoritam potenciranja zasnovan na ovom triku s uzimanjem ostatka uvijek ispravan.
    
    Promotrimo iterativni tijek algoritma. Pretpostavimo da se, vraćajući se od najunutarnjije razine prema vanjskim funkcijama, prva pogreška u informaciji o prekoračenju dogodi pri računanju $r_m(a^k)$. Kad je $k<\varphi(m)$, eksponent je točan i pogreška se ne može dogoditi, pa neka je $k\ge\varphi(m)$; tada je $k\ge k\bmod\varphi(m)+\varphi(m)$, tj. uzimanje ostatka može eksponent samo podcijeniti, informacija o prekoračenju ne može nastati ni iz čega, pa je jedina mogućnost pogreške da je prekoračenje trebalo biti zabilježeno, a nije, tj.
    
    $$
    a^{k\bmod\varphi(m)+\varphi(m)} < m \le a^{k}.
    $$
    
    Ta nejednakost može vrijediti samo za $a \ge 2$, pa izraz na lijevoj strani nije manji od $2^{\varphi(m)}$. No $2^{\varphi(m)} < m$ događa se samo za $m = 6$.[^phi-ineq] Uvrštavanjem u gornju nejednakost dobivamo $a^{k\bmod 2 + 2} < 6 \le a^{k}$. U izrazu na lijevoj strani, ako je $k$ paran, eksponent je $2$, pa je $a = 2$ i $k \ge 4$; ako je $k$ neparan, eksponent je $3$ i rješenja nema. Ukupno, gubitak informacije o prekoračenju događa se samo kad je $m=6,~a=2$ i $k\ge 4$ paran.
    
    Sada pokazujemo da gubitak informacije o prekoračenju u ovom slučaju ne utječe na daljnji račun. Promatramo samo netrivijalni slučaj $a_i\ge 2$ (za $a_i\le 1$ vrijednost potencije ne prelazi $1$ i prekoračenja nema). Modul unutarnje razine je $6$, pa modul $m_1$ nakon vraćanja za jednu razinu zadovoljava $\varphi(m_1)=6$ i može biti samo jedan od $7,9,14,18$. Pri vraćanju na tu razinu treba izračunati $r_{m_1}(a_1^{k_1})$, pri čemu bi $k_1$ trebao biti $10$, a zapravo je $4$. No za sve $a_1$ i te $m_1$ vrijedi $a_1^{4}\equiv a_1^{10}\pmod {m_1}$. Da bismo to pokazali, uočimo da je u gornjem [dokazu](#strogi-dokaz) proširenog Eulerova teorema već dobiveno: za svaki $a$ i $m$ duljina $k_0$ puta prije ulaska ostatka $a^k\bmod m$ u ciklus ne prelazi $\nu_+(m):=\max\{\nu_p(m) : p\mid m\}$, a duljina ciklusa dijeli $\varphi(m)$. Budući da je $\nu_+(m_1)\le 2$, $k_1=4$ već je u ciklusu, a od $10$ se razlikuje za $\varphi(m_1)=6$, pa gornja kongruencija uvijek vrijedi. Dakle, informacija o ostatku je točna. Pogledajmo sada informaciju o prekoračenju. Budući da je prava vrijednost unutarnje razine $2^k\ge 16>10$, vrijedi $a_1^{2^k}\ge a_1^{10}\ge m_1$, pa bi ova razina uvijek trebala označiti prekoračenje. No ova razina vraća samo je li $a_1^4$ prekoračio; jedina mogućnost pogreške jest $a_1^4<m_1$, tj. jedino $a_1=2,~m_1=18$. U ostalim je slučajevima informacija o prekoračenju već točno označena i daljnje je vraćanje prirodno ispravno. A za $a_1=2,~m_1=18$ trebalo bi vratiti $34$, a zapravo se vraća $16$, pa treba vratiti se još jednu razinu; tada $m_2$ može biti samo jedan od $19,27,38,54$. Tada uvijek vrijedi $\nu_+(m_2)\le 3 < 16$ i $34-16=\varphi(m_2)$, pa je informacija o ostatku točna; a $a_2^{16}\ge m_2$ vrijedi uvijek, pa je i informacija o prekoračenju točna. Dakle, rezultat je tada točan, a i daljnje je vraćanje nužno ispravno.
    
    Budući da moduli po razinama strogo padaju, $m=6$ pojavljuje se najviše jednom. Ukupno, pri računanju višerazinskih potencija ovim trikom s uzimanjem ostatka informacija o ostatku na svakoj je razini točna, a informacija o prekoračenju pogrešna je na najviše dvije razine. Primijetimo da u dokazu nismo pretpostavili da su baze potenciranja na svim razinama jednake, pa zaključak vrijedi i za slučaj različitih baza.

## Zadaci za vježbu

-   [Luogu P5091【模板】扩展欧拉定理 (Predložak: prošireni Eulerov teorem)](https://www.luogu.com.cn/problem/P5091)
-   [Codeforces 906 D. Power Tower](https://codeforces.com/problemset/problem/906/D)
-   [Luogu P3747 \[六省联考 2017\] 相逢是问候 (Susret je pozdrav)](https://www.luogu.com.cn/problem/P3747)
-   [Luogu P4139 上帝与集合的正确用法 (Bog i ispravna uporaba skupova)](https://www.luogu.com.cn/problem/P4139)
-   [Luogu P3934 \[Ynoi Easy Round 2016\] 炸脖龙 I (Jabberwocky I)](https://www.luogu.com.cn/problem/P3934)
-   [Luogu P6736「Wdsr-2」白泽教育 (Obrazovanje kod Bai Zea)](https://www.luogu.com.cn/problem/P6736)

## Literatura i bilješke

-   [Fermat's little theorem - Wikipedia](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
-   [Euler's theorem - Wikipedia](https://en.wikipedia.org/wiki/Euler%27s_theorem)
-   Hardy, Godfrey Harold, and Edward Maitland Wright. An introduction to the theory of numbers. Oxford university press, 1979.

[^ex-euler]: Taj se naziv pojavljuje uglavnom u krugovima natjecateljskog programiranja i nije općeprihvaćeni naziv tog rezultata.

[^phi-ineq]: Prema članku Kendall, R. and Osborn, R. (1965) Two Simple Lower Bounds for the Euler ϕ-Function. Texas Journal of Science, 17, 324-326, za $m > 6$ uvijek vrijedi $\varphi(m)\ge\sqrt{m}$. Izravnim računom vidi se da za $m\ge 16$ uvijek vrijedi $\sqrt{m}\ge\log_2m$. Stoga nejednakost $\varphi(m)\ge\log_2m$ vrijedi za sve $m\ge 16$. Preostali se slučajevi provjere pojedinačno.
