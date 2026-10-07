---
title: Splay stablo
---

Ova stranica kratko predstavlja kako Splay stablom održavati binarno stablo pretraživanja.

## Definicija

**Splay stablo** (engl. *splay tree*, „rastezljivo stablo”) balansirano je binarno stablo pretraživanja koje **operacijom splay (rastezanja)** neprestano rotira neki čvor do korijena tako da cijelo stablo i dalje zadovoljava svojstvo binarnog stabla pretraživanja, a umetanje, pretraživanje i brisanje obavlja u amortiziranom vremenu $O(\log n)$.[^degen]

Splay stablo izumili su Daniel Sleator i Robert Tarjan 1985. godine.

## Osnovna struktura i operacije

Ovaj odjeljak obrađuje osnovnu strukturu Splay stabla i njegove ključne operacije, među kojima je najvažnija operacija splay.

Splay stablo je binarno stablo pretraživanja, tj. svaki čvor u stablu zadovoljava svojstvo: vrijednost bilo kojeg čvora lijevog podstabla $<$ vrijednost tog čvora $<$ vrijednost bilo kojeg čvora desnog podstabla.

### Održavane informacije

U ovom tekstu Splay stablo implementiramo poljima koja simuliraju pokazivače; treba održavati sljedeće informacije:

|   rt  |    id   | fa\[i] | ch\[i]\[0/1] | val\[i] | cnt\[i] | sz\[i] |
| :---: | :-----: | :----: | :----------: | :-----: | :-----: | :----: |
| broj korijena | broj iskorištenih čvorova |   roditelj   |    brojevi lijevog i desnog djeteta    |   vrijednost čvora  |  broj pojavljivanja vrijednosti |  veličina podstabla  |

Pri inicijalizaciji sve informacije postavimo na nulu.

### Pomoćne operacije

Najprije nekoliko jednostavnih pomoćnih operacija:

-   `dir(x)`: određuje je li čvor $x$ lijevo ili desno dijete svojeg roditelja;
-   `push_up(x)`: nakon promjene položaja čvora ažurira informacije čvora $x$ prema informacijama njegove djece.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:aux"
    ```

### Rotacije

Da bi Splay stablo ostalo uravnoteženo, potrebne su rotacije. Rotacija pomiče neki čvor za jedno mjesto prema gore.

Rotacija mora jamčiti:

-   inorder obilazak cijelog Splay stabla ostaje nepromijenjen (ne smije se narušiti svojstvo binarnog stabla pretraživanja);
-   informacije koje održavaju zahvaćeni čvorovi ostaju ispravne i valjane;
-   `rt` mora pokazivati na korijen nakon rotacije.

U Splay stablu postoje dvije vrste rotacija: lijeva i desna.

![](./images/splay-rotate.svg)

Promatrajući sliku vidimo da je, želimo li rotacijom pomaknuti čvor $x$ (čvor $1$ pri lijevoj i čvor $2$ pri desnoj rotaciji) prema gore, smjer rotacije jednoznačno određen time je li taj čvor lijevo ili desno dijete svojeg roditelja. Stoga je pri implementaciji rotacije dovoljno proslijediti samo čvor $x$ koji treba pomaknuti gore.

Konkretni koraci rotacije: (neka je čvor koji treba pomaknuti gore $x$, na primjeru desne rotacije)

1.  Najprije zabilježimo roditelja $y$ čvora $x$ i roditelja $z$ čvora $y$ (može biti prazan) te zabilježimo je li $x$ lijevo ili desno dijete čvora $y$;
2.  Redom, odozdo prema gore u stablu nakon rotacije, postavimo lijevo dijete čvora $y$ na desno dijete čvora $x$, desno dijete čvora $x$ na $y$ i, ako $z$ nije prazan, dijete čvora $z$ na $x$;
3.  Istim redoslijedom postavimo roditelja trenutačnog lijevog djeteta čvora $y$ (ako postoji) na $y$, roditelja čvora $y$ na $x$ i roditelja čvora $x$ na $z$;
4.  Odozdo prema gore održavamo informacije čvorova.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:rotate"
    ```

Pri implementaciji svih funkcija treba paziti da se ne mijenjaju informacije čvora $0$.

### Operacija splay

Splay stablo zahtijeva da se nakon svakog pristupa čvoru $x$ taj čvor obvezno rotira do korijena. Ta se operacija naziva i operacija splay (rastezanje).

Neka je upravo posjećeni čvor $x$. Operacija splay sastoji se od niza **splay koraka** nad $x$. Nakon svakog splay koraka $x$ je bliže korijenu. Neka je $p$ roditelj čvora $x$. Postoje tri vrste splay koraka:

1.  **zig**: izvodi se kad je $p$ korijen. Splay stablo rotira oko brida između $x$ i $p$. **Zig** služi za rješavanje parnosti dubine i izvodi se samo kao posljednji korak operacije splay, i to samo kad je $x$ na početku operacije splay bio na neparnoj dubini.

    ![splay-zig](./images/splay-zig.svg)

    Dakle, $x$ izravno rotiramo udesno ili ulijevo (slike 1, 2).

    ![Slika 1](./images/splay-rotate1.svg)![Slika 2](./images/splay-rotate2.svg)

2.  **zig-zig**: izvodi se kad $p$ nije korijen te su $x$ i $p$ oba desna ili oba lijeva djeca. Primjer na slici prikazuje slučaj kad su $x$ i $p$ oba lijeva djeca. Splay stablo najprije rotira oko brida koji spaja $p$ s njegovim roditeljem $g$, a zatim oko brida koji spaja $x$ i $p$.

    ![splay-zig-zig](./images/splay-zig-zig.svg)

    Dakle, najprije $p$ rotiramo udesno ili ulijevo, a zatim $x$ rotiramo udesno ili ulijevo (slike 3, 4).

    ![Slika 3](./images/splay-rotate3.svg)![Slika 4](./images/splay-rotate4.svg)

3.  **zig-zag**: izvodi se kad $p$ nije korijen te je jedan od $x$ i $p$ desno, a drugi lijevo dijete. Splay stablo najprije rotira oko brida između $p$ i $x$, a zatim oko novonastalog brida između $x$ i $g$ nakon rotacije.

    ![splay-zig-zag](./images/splay-zig-zag.svg)

    Dakle, $x$ najprije rotiramo ulijevo pa udesno ili najprije udesno pa ulijevo (slike 5, 6).

    ![Slika 5](./images/splay-rotate5.svg)![Slika 6](./images/splay-rotate6.svg)

???+ tip "Savjet"
    Čitatelju preporučujemo da sam simulira svih $6$ slučajeva rotacije kako bi razumio osnovnu ideju operacije splay.

Usporedbom triju vrsta splay koraka vidimo da je za odabir koraka ključno provjeriti je li $x$ dijete korijena te jesu li $x$ i njegov roditelj na istoj strani svojih roditelja.

Ovdje dana implementacija dopušta zadavanje proizvoljnog korijena $z$ i pomiče bilo koji čvor $x$ iz njegova podstabla na mjesto čvora $z$:

1.  Najprije zabilježimo roditelja $w$ korijena $z$, pa pomoću `fa[x] == w` možemo provjeriti je li $x$ već na mjestu korijena;
2.  Zabilježimo trenutačnog roditelja $y$ čvora $x$; ako su $y$ i $w$ jednaki, $x$ je već stigao do korijena;
3.  Inače pomoću `fa[y] == w` provjerimo je li $y$ korijen. Ako jest, izravno napravimo zig i rotiramo $x$; ako nije, pomoću `dir(x) == dir(y)` odlučimo između zig-zig i zig-zag: prvi najprije rotira $y$ pa $x$, a drugi dvaput rotira $x$.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:splay"
    ```

Operacija splay ključna je operacija Splay stabla i ključni korak koji jamči njegovu vremensku složenost. Obvezno nakon svakog silaznog pristupa čvoru napravite jednu operaciju splay.

Osim toga, operacija splay odozdo prema gore ažurira informacije svih čvorova na putu od trenutačnog čvora $x$ do korijena $z$. Upravo zato možemo izmijeniti čvor koji nije korijen i zatim ga operacijom splay pomaknuti do korijena kako bismo ažurirali informacije cijelog stabla.

### Vremenska složenost

Složenost $m$ operacija splay nad Splay stablom veličine $n$ je $O((m+n)\log n)$, a amortizirana složenost jedne operacije je $O(\log n)$.

??? note "Dokaz složenosti metodom potencijala"
    Za to je dovoljno analizirati složenost triju operacija: **zig**, **zig-zig** i **zig-zag**. U tu svrhu koristimo **metodu potencijala**, kojom proučavanjem promjena potencijala izvodimo amortiziranu složenost operacija. Pretpostavimo da je nad Splay stablom s $n$ čvorova izvedeno $m$ operacija splay; analizu provodimo na sljedeći način:
    
    **Definicije**:
    
    1.  **Potencijal pojedinog čvora**: $w(x) = \log(\text{size}(x))$, gdje $\text{size}(x)$ označava veličinu podstabla s korijenom u čvoru $x$.
    2.  **Potencijal cijelog stabla**: $\varphi = \sum w(x)$, tj. zbroj potencijala svih čvorova u stablu; početni potencijal zadovoljava $\varphi_0 \leq n \log n$.
    3.  **Amortizirani trošak $i$-te operacije**: $c_i = t_i + \varphi_i - \varphi_{i-1}$, gdje je $t_i$ stvarni trošak operacije, a $\varphi_i$ i $\varphi_{i-1}$ potencijali nakon i prije operacije.
    
    **Svojstva**:
    
    1.  Ako je $p$ roditelj čvora $x$, vrijedi $w(p) \geq w(x)$, tj. potencijal roditelja nije manji od potencijala djeteta.
    
    2.  Budući da se veličina podstabla korijena prije i poslije operacije ne mijenja, potencijal korijena tijekom operacije ostaje nepromijenjen.
    
    3.  Ako je $\text{size}(p)\ge\text{size}(x)+\text{size}(y)$, vrijedi $2w(p) - w(x) - w(y) \geq 2$.
    
    ??? note "Dokaz svojstva 3"
        Prema nejednakosti između aritmetičke i geometrijske sredine vrijedi
        
        $$
        \begin{aligned}
        2w(p) - w(x) - w(y) 
        &= \log\dfrac{\text{size}(p)^2}{\text{size}(x)\cdot\text{size}(y)} \\
        &\ge \log\dfrac{\left(\text{size}(x)+\text{size}(y)\right)^2}{\text{size}(x)\cdot\text{size}(y)} \\
        &\ge \log 4 \\
        &= 2.
        \end{aligned}
        $$
    
    Zatim analizu potencijala provodimo redom za operacije **zig**, **zig-zig** i **zig-zag**. Neka su potencijali čvora $x$ prije i poslije operacije $w(x)$ i $w'(x)$. Oznake čvorova iste su kao [gore](#operacija-splay).
    
    **zig**: prema svojstvima 1 i 2 vrijedi $w(p) = w'(x)$ i $w'(x) \geq w'(p)$. Stoga je amortizirani trošak
    
    $$
    \begin{aligned}
    c_i &= 1 + w'(x) + w'(p) - w(x) - w(p)\\
    &= 1 + w'(p) - w(x)\\
    &\leq 1 + w'(x) - w(x).
    \end{aligned}
    $$
    
    **zig-zig**: prema svojstvima 1 i 2 vrijedi $w(g) = w'(x)$, $w'(x) \geq w'(p)$ i $w(x) \leq w(p)$. Budući da je
    
    $$
    \begin{aligned}
    \text{size}'(x) 
    &= 3 + \text{size}(A) + \text{size}(B) + \text{size}(C) + \text{size}(D) \\
    &> (1 + \text{size}(A) + \text{size}(B)) + (1 + \text{size}(C) + \text{size}(D)) \\
    &= \text{size}(x) + \text{size}'(g),
    \end{aligned}
    $$
    
    prema svojstvu 3 dobivamo
    
    $$
    2 w'(x) - w(x) - w'(g) \geq 2.
    $$
    
    Stoga je amortizirani trošak
    
    $$
    \begin{aligned}
    c_i &= 2 + w'(x) + w'(p) + w'(g) - w(x) - w(p) - w(g) \\
    &= 2 + w'(p) + w'(g) - w(x) - w(p) \\
    &\le (2 w'(x) - w(x) - w'(g)) + w'(p) + w'(g) - w(x) - w(p) \\
    &= 2(w'(x)-w(x)) + w'(p) - w(p) \\
    &\le 3(w'(x)-w(x)).
    \end{aligned}
    $$
    
    **zig-zag**: prema svojstvima 1 i 2 vrijedi $w(g) = w'(x)$ i $w(p) \geq w(x)$. Budući da je $\text{size}'(x)>\text{size}'(p)+\text{size}'(g)$, prema svojstvu 3 dobivamo
    
    $$
    2 \cdot w'(x) - w'(g) - w'(p) \geq 2.
    $$
    
    Stoga je amortizirani trošak
    
    $$
    \begin{aligned}
    c_i &= 2 + w'(x) + w'(p) + w'(g) - w(x) - w(p) - w(g) \\
    &= 2 + w'(p) + w'(g) - w(x) - w(p) \\
    &\le (2w'(x) - w'(g) - w'(p)) + w'(p) + w'(g) - w(x) - w(p) \\
    &= 2w'(x) - w(x) - w(p) \\
    &\le 2(w'(x) - w(x)).
    \end{aligned}
    $$
    
    **Jedna operacija splay**:
    
    Neka je $w^{(j)}(x)=(w^{(j-1)})'(x)$ i $w^{(0)}(x)=w(x)$. Pretpostavimo da se jedna operacija splay sastoji od ukupno $k$ splay koraka i da na kraju pomiče čvor $x_{1}$ do korijena. To se nužno odvija kroz nekoliko operacija **zig-zig** i **zig-zag** te najviše jednu operaciju **zig**; amortizirani trošak prvih dviju vrsta ne premašuje $3(w'(x)-w(x))$, a amortizirani trošak posljednje ne premašuje $3(w'(x) - w(x))+1$, pa ukupni amortizirani trošak ne premašuje
    
    $$
    3(w^{(k)}(x_1) - w^{(0)}(x_1)) + 1 \le 3\log n + 1.
    $$
    
    Stoga je amortizirana složenost jedne operacije splay $O(\log n)$. Prema tome, i vremenska složenost operacija umetanja, upita, brisanja i sličnih koje se temelje na operaciji splay iznosi amortizirano $O(\log n)$.
    
    **Zaključak**:
    
    Nakon $m$ operacija splay stvarni je trošak
    
    $$
    \begin{aligned}
    \sum_{i=1}^m t_i &= \sum_{i=1}^m \left(c_i + \varphi_{i-1} - \varphi_i \right) \\
    &= \sum_{i=1}^m c_i + \varphi_0 - \varphi_m \\
    &\le m(3\log n+1) + n\log n.
    \end{aligned}
    $$
    
    Stoga je stvarna vremenska složenost $m$ operacija splay $O((m+n)\log n)$.

??? info "Zašto operacija ponovnog balansiranja Splay stabla postiže amortiziranu složenost $O(\log n)$?"
    Naivna ideja ponovnog balansiranja jest uzastopno rotirati čvor prema gore dok ne postane korijen. Problem je te naivne ideje što je kod lančastog stabla, u kojem su sva djeca lijeva (desna), to jednako uzastopnom izvođenju operacije **zig**, pa se konstanta $1$ iz amortizirane složenosti operacije **zig** stalno gomila i konačna amortizirana složenost doseže razinu $O(n)$. Dizajn operacije ponovnog balansiranja Splay stabla izbjegava gomilanje konstante u slučaju uzastopnih **zig** koraka, tako da se u jednoj potpunoj operaciji splay izvodi najviše jedna samostalna operacija **zig**, čime se optimira vremenska složenost.

## Operacije balansiranog stabla

Ovaj odjeljak obrađuje uobičajene operacije balansiranog stabla implementirane Splay stablom. Među njima su važnije pretraživanje elementa po vrijednosti ili rangu: one pronalaze određeni element i pomiču ga do korijena radi daljnje obrade.

Kao primjer, u ovom ćemo odjeljku obraditi implementaciju oglednog zadatka [Obično balansirano stablo](https://loj.ac/problem/104).

### Pretraživanje po vrijednosti

Kao u binarnom stablu pretraživanja, po vrijednosti $v$ možemo naći odgovarajući čvor: dovoljno je uspoređivati traženu vrijednost $v$ s vrijednošću trenutačnog čvora, a kad ga nađemo, pomaknuti taj element do korijena.

Treba paziti da često odgovarajući čvor u stablu ne postoji. Za taj slučaj bilježimo posljednji posjećeni čvor (tj. $y$ u implementaciji) i pomičemo $y$ do korijena. Tada je vrijednost pohranjena u čvoru $y$ nužno ili najveća među svim elementima manjima od $v$ (tj. prethodnik od $v$) ili najmanja među svim elementima većima od $v$ (tj. sljedbenik od $v$). Razlog je to što postupak pretraživanja jamči da lijevo podstablo uvijek sadrži vrijednosti manje od $v$, a desno podstablo vrijednosti veće od $v$.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find"
    ```

Ta implementacija dopušta zadavanje bilo kojeg čvora $z$ kao korijena i pretražuje po vrijednosti unutar njegova podstabla.

### Pristup po rangu

Budući da se bilježi veličina podstabla, Splay stablo omogućuje i pristup elementu po rangu, tj. pronalaženje $k$-tog najmanjeg elementa u stablu.

Neka je $k$ preostali rang; konkretni koraci su:

-   ako lijevo podstablo nije prazno i preostali rang $k$ nije veći od veličine lijevog podstabla, tražimo u lijevom podstablu;
-   inače, ako $k$ nije veći od zbroja veličine lijevog podstabla i broja pojavljivanja vrijednosti korijena, tražen je upravo korijen;
-   inače od $k$ oduzmemo zbroj veličine lijevog podstabla i broja pojavljivanja vrijednosti korijena te nastavimo tražiti u desnom podstablu;
-   konačno pronađeni element pomaknemo do korijena.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:loc"
    ```

Ta implementacija zahtijeva da rang $k$ ne premašuje veličinu stabla s korijenom $z$.

Operacija $4$ u oglednom zadatku traži vraćanje vrijednosti po rangu: dovoljno je izravno pozvati tu metodu i vratiti vrijednost.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-kth"
    ```

### Spajanje

Ponekad treba spojiti dva Splay stabla.

Neka su korijeni dvaju stabala $x$ i $y$. Da bi rezultat i dalje bio binarno stablo pretraživanja, mora vrijediti da je najveća vrijednost u stablu $x$ manja od najmanje vrijednosti u stablu $y$. Taj je uvjet obično ispunjen, jer su dva stabla najčešće nastala razdvajanjem većeg podstabla.

Spajanje ide ovako:

-   ako je jedno od $x$ i $y$ ili oba prazno stablo, izravno vratimo korijen nepraznog stabla ili prazno stablo;
-   inače pozivom `loc(y, 1)` pomaknemo najmanju vrijednost stabla $y$ do korijena $y$, zatim njegovo lijevo dijete (koje je tada nužno prazno) postavimo na $x$, ažuriramo informacije čvora i vratimo čvor $y$.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:merge"
    ```

Razdvajanje je slično. Stoga Splay stablo može oponašati pristup [Treapa bez rotacija](./treap.md#treap-bez-rotacija) za razne operacije, uključujući operacije nad intervalima. [Kasnije](#operacije-nad-nizom) ćemo predstaviti način obrade operacija nad intervalima koji je više u duhu Splay stabla.

### Umetanje

Umetanje je razmjerno složen postupak. Konkretni koraci: (neka je umetana vrijednost $v$)

-   slično pretraživanju po vrijednosti, prema $v$ silazimo do čvora koji pohranjuje $v$ ili do praznog čvora, usput bilježeći roditelja $y$;
-   ako čvor $x$ koji pohranjuje $v$ postoji, izravno ažuriramo informacije, inače stvorimo novi čvor $x$;
-   napravimo operaciju splay i posljednji čvor $x$ pomaknemo do korijena.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:insert"
    ```

Ta implementacija dopušta izravno umetanje vrijednosti u prazno stablo. Ako ne želite obrađivati prazno stablo, možete unaprijed umetnuti lažne (dummy) čvorove.

### Brisanje

Brisanje je također razmjerno složena operacija. Konkretni koraci: (neka je brisana vrijednost $v$)

-   najprije po vrijednosti $v$ nađemo čvor koji je pohranjuje i pomaknemo ga do korijena;
-   ako takav čvor ne postoji, izravno se vratimo (operacija splay već je obavljena u prethodnom koraku);
-   inače ažuriramo informacije čvora;
-   ako broj pojavljivanja vrijednosti korijena padne na nulu, taj čvor brišemo, tj. spojimo lijevo i desno podstablo u novi korijen; pazite da prije spajanja roditelje korijena obaju podstabala treba postaviti na prazno.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:remove"
    ```

### Upit ranga

Izravno pristupimo čvoru po vrijednosti $v$ (i pomaknemo ga do korijena), a zatim vratimo odgovarajući rang.

Pazite: kad $v$ ne postoji, odnos između korijena koji vraća metoda `find(rt, v)` i $v$ nije određen, pa ga treba zasebno razmotriti.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-rank"
    ```

### Upit prethodnika

Prethodnik je definiran kao najveći broj manji od $v$. Konkretni koraci:

-   pristupimo čvoru po vrijednosti $v$ (i pomaknemo ga do korijena);
-   ako je vrijednost korijena manja od $v$, ona je nužno najveća takva, pa je izravno vratimo;
-   inače u lijevom podstablu nađemo najveću vrijednost i pomaknemo je do korijena.

Posljednji korak jednak je izravnom pozivu `loc(ch[rt][0], sz[ch[rt][0]])`, samo bez nepotrebnih provjera.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-prev"
    ```

Ta implementacija dopušta da prethodnik ne postoji; tada vraća $-1$.

### Upit sljedbenika

Sljedbenik je definiran kao najmanji broj veći od $v$. Način upita sličan je upitu prethodnika, samo što najveću vrijednost lijevog podstabla zamjenjujemo najmanjom vrijednošću desnog podstabla, tj. pozivamo `loc(ch[rt][1], 1)`.

???+ example "Implementacija"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-next"
    ```

### Primjer implementacije

Na kraju odjeljka dajemo primjer implementacije oglednog zadatka [Obično balansirano stablo](https://loj.ac/problem/104).

??? example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:full-text"
    ```

## Operacije nad nizom

Splay stablo može se primijeniti i na nizove, za održavanje informacija o intervalima. U usporedbi sa segmentnim stablom Splay stablo ima veću konstantu, ali podržava složenije operacije nad nizom, poput okretanja intervala. Gore je spomenuto da Splay stablo također podržava razdvajanje i spajanje, pa može oponašati [Treap bez rotacija](./treap.md#treap-bez-rotacija) za operacije nad intervalima; o tome ovdje nećemo dalje raspravljati. Ovaj odjeljak uglavnom obrađuje implementaciju operacija nad intervalima temeljenu na operaciji splay.

Splay stablo izgrađeno od niza ima sljedeća svojstva:

-   inorder obilazak Splay stabla odgovara obilasku izvornog niza slijeva nadesno;
-   čvor Splay stabla predstavlja element izvornog niza;
-   podstablo Splay stabla predstavlja interval izvornog niza.

Zahvaljujući operaciji splay možemo brzo izdvojiti Splay podstablo koje predstavlja neki interval.

Kao primjer, u ovom ćemo odjeljku obraditi implementaciju oglednog zadatka [Umjetničko balansirano stablo](https://loj.ac/problem/105).

### Izgradnja stabla iz niza

Prije operacija treba iz zadanog niza izgraditi Splay stablo. Zbog svojstava Splay stabla dovoljno je izravno izgraditi lanac koji ima samo lijevu djecu. Vremenska složenost je $O(n)$.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:build"
    ```

Završna operacija splay odozdo prema gore ažurira informacije čvorova. Radi lakših operacija nad intervalima u nastavku, s lijeve i desne strane niza dodana su dva čvora stražara (sentinela).

### Okretanje intervala

Na primjeru okretanja intervala može se razumjeti način izvođenja operacija nad intervalima: (neka je interval $[L,R]$)

-   najprije čvor $L-1$ pomaknemo do korijena, a zatim u njegovu desnom podstablu čvor $R+1$ pomaknemo do korijena desnog podstabla;
-   tada, neka je $x$ lijevo dijete desnog djeteta korijena; podstablo s korijenom $x$ odgovara upravo intervalu $[L,R]$;
-   u čvoru $x$ obavimo operaciju nad intervalom $[L,R]$ i postavimo lijenu oznaku;
-   u čvoru $x$ jednom spustimo oznaku, a zatim operacijom splay pomaknemo $x$ do korijena.

Operacija potrebna u prvom koraku upravo je „pristup po rangu” iz prethodnih operacija balansiranog stabla, jer je indeks elementa upravo njegov rang. Budući da uključuje upravljanje lijenim oznakama, njezina se implementacija malo razlikuje od gornje.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:reverse"
    ```

Operacija splay u posljednjem koraku nije tu radi jamstva složenosti, nego radi ažuriranja informacija čvorova. Budući da operacija splay uključuje lijevo i desno dijete čvora $x$, prethodno treba jednom spustiti oznaku u čvoru $x$. Naravno, samo kod okretanja intervala okretanje podintervala ne utječe na pretke, pa je ispravno i izostaviti taj korak. Ovdje su ta dva retka zadržana kako bi se prikazao postupak u općem slučaju.

### Upravljanje lijenim oznakama

Najprije trebamo pomoćne funkcije `lazy_reverse(x)` i `push_down(x)`. Prva zamjenjuje lijevo i desno dijete i ažurira lijenu oznaku; druga spušta oznaku.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:push-down"
    ```

Zatim je dovoljno spuštati oznake pri silaznom prolasku kroz čvorove. Operacije koje traži ogledni zadatak razmjerno su jednostavne; samo pretraživanje po rangu (tj. `loc`) uključuje silazni pristup čvorovima. Pazite: oznaku treba spustiti **prije** svakog pristupa funkcije novom čvoru.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:push-down-lazy"
    ```

Budući da su pri silaznom pristupu čvorovima već uklonjene sve lijene oznake na prijeđenom putu, pri pomicanju čvora operacijom splay više nije potrebno obrađivati lijene oznake. Međutim, s čvorom nad kojim se obavlja operacija nad intervalom treba postupati oprezno: on se također nalazi na putu operacije splay, ali je tek obrađen pa može imati još nespuštenu oznaku, koju treba najprije spustiti pa tek onda napraviti operaciju splay, kao što je gore učinjeno.

### Primjer implementacije

Na kraju odjeljka dajemo primjer implementacije oglednog zadatka [Umjetničko balansirano stablo](https://loj.ac/problem/105).

??? example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:full-text"
    ```

## Zadaci

Ovi su zadaci čisto održavanje binarnog stabla pretraživanja Splay stablom:

-   [„Predložak” Obično balansirano stablo](https://loj.ac/problem/104)
-   [„Predložak” Umjetničko balansirano stablo](https://loj.ac/problem/105)
-   [„HNOI2002” Statistika prometa](https://loj.ac/problem/10143)
-   [„HNOI2004” Sklonište za kućne ljubimce](https://loj.ac/problem/10144)

Splay stablo pojavljuje se i u složenijim primjenama:

-   [„Cerc2007” Robotic sort](https://www.luogu.com.cn/problem/P4402)
-   [„HNOI2011” Popravak zagrada / „JSOI2011” Niz zagrada](https://www.luogu.com.cn/problem/P3215)
-   [Dvostruko balansirano stablo (stablo nad stablom)](https://loj.ac/problem/106)
-   [BZOJ 2827 Ptice nestaju s tisuću planina](https://hydro.ac/p/bzoj-P2827)
-   [„Lydsy1706 mjesečno natjecanje” Upit k-te najmanje vrijednosti](https://hydro.ac/p/bzoj-P4923)
-   [POJ3580 SuperMemo](http://poj.org/problem?id=3580)

## Literatura i napomene

Dio sadržaja ovog teksta preuzet je s algoritamskog bloga algocode, uz posebnu zahvalu!

[^degen]: Splay stablo jamči samo amortiziranu složenost $O(\log n)$. Ne održava uvjet ravnoteže poput AVL stabla ili crveno-crnog stabla, pa se nakon niza operacija može čak degenerirati u lanac. Stoga je najgora složenost jedne operacije $O(n)$.
