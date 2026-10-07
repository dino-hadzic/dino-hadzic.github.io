---
title: Scapegoat stablo
---

## Uvod

**Scapegoat stablo** (scapegoat tree, „stablo žrtvenog jarca”) težinski je balansirano stablo koje ravnotežu održava operacijom ponovne izgradnje (rebuild). Nakon umetanja i brisanja scapegoat stablo provjerava je li stablo izgubilo ravnotežu; ako jest, ciljano ponovno izgrađuje dio stabla kako bi vratilo ravnotežu.

Općenito, scapegoat stablo ne podržava operacije nad intervalima i ne može se potpuno perzistentno implementirati, ali ima prednosti jednostavne implementacije i male konstante.

## Osnovna struktura i operacije

Ključne operacije scapegoat stabla su ponovna izgradnja, umetanje i brisanje.

### Informacije u čvoru

Scapegoat stablo mora čuvati sljedeće informacije potrebne za samobalansiranje stabla:

-   informacije o strukturi stabla:
    -   `id`: broj iskorištenih čvorova;
    -   `rt`: korijen;
    -   `lc[x]`, `rc[x]`: lijevo i desno dijete;
    -   `tot[x]`: veličina podstabla s korijenom $x$ (svaki se čvor broji kao $1$)[^tot-cnt];
    -   `tot_active`: broj neizbrisanih čvorova (tj. onih s `cnt[x] != 0`) u cijelom stablu.

Kad scapegoat stablom implementiramo balansirano stablo, treba čuvati i sljedeće informacije:

-   informacije balansiranog stabla u čvoru:
    -   `val[x]`: vrijednost pohranjena u čvoru;
    -   `cnt[x]`: broj pojavljivanja vrijednosti pohranjene u čvoru (može biti $0$);
    -   `sz[x]`: zbroj brojeva pojavljivanja vrijednosti pohranjenih u podstablu s korijenom $x$.

Za održavanje informacija u čvoru možemo implementirati operaciju `push_up`:

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:push-up"
    ```

Obratite pozornost na razliku u načinu ažuriranja `tot[x]` i `sz[x]`.

### Ponovna izgradnja

Kad stablo izgubi ravnotežu, neko se podstablo mora ponovno izgraditi tako da bude što uravnoteženije. Ponovna izgradnja ima dva koraka:

-   inorder obilazak podstabla koje se ponovno izgrađuje, pri čemu sve neizbrisane čvorove spremimo u niz;
-   izgradnja stabla raspolavljanjem: srednji element uzmemo za korijen, lijevo i desno rekurzivno izgradimo podstabla i ažuriramo informacije u čvorovima.

Primjer implementacije:

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:rebuild"
    ```

Pri izgradnji treba paziti na održavanje informacija u čvorovima, uključujući i informacije u listovima.

Složenost jedne ponovne izgradnje je $\Theta(|T_x|)$, pa bi složenost bila neprihvatljiva kad bismo ponovno izgrađivali pri svakom umetanju i brisanju. Ključna je ideja scapegoat stabla upravo u izboru trenutka ponovne izgradnje, čime se postiže amortizirana složenost $O(\log n)$.

### Umetanje

Umetanje može narušiti ravnotežu stabla. Da bismo prepoznali gubitak ravnoteže, uvodimo parametar $\alpha\in(0.5,1)$; uobičajeno se bira između $0.7$ i $0.8$.

Ako dubina novoumetnutog čvora premaši $\lfloor\log_{1/\alpha}|T|\rfloor$, gdje je $|T|$ veličina stabla nakon ažuriranja, pri povratku iz rekurzije treba pronaći čvor u kojem je došlo do gubitka ravnoteže i ponovno ga izgraditi. Pritom se neuravnoteženost podstabla s korijenom $x$ prepoznaje po uvjetu

$$
\max\{|T_{\mathrm{left}(x)}|,|T_{\mathrm{right}(x)}|\} > \alpha\cdot |T_x|,
$$

gdje su $\mathrm{left}(x)$ i $\mathrm{right}(x)$ lijevo i desno dijete čvora $x$, a $|T_x|$ veličina podstabla s korijenom $x$.

Konkretni koraci umetanja su sljedeći:

-   najprije, koristeći svojstvo binarnog stabla pretraživanja, spuštamo se do mjesta za umetanu vrijednost i pritom bilježimo dubinu;
-   ako čvor već postoji, samo ažuriramo njegove informacije, inače stvaramo novi čvor;
-   vraćamo se odozdo prema gore do korijena i ažuriramo informacije u čvorovima; ako je novi čvor predubok, zabilježimo i prvi (ili bilo koji) čvor na povratnom putu čije je podstablo neuravnoteženo;
-   ako postoji neuravnoteženi čvor, ponovno izgradimo njegovo podstablo.

Primjer implementacije:

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:insert"
    ```

Primijetite da jedno umetanje izaziva najviše jednu ponovnu izgradnju. Ako nije stvoren novi čvor, ako novi čvor nije predubok ili ako je tijekom ovog povratka već obavljena ponovna izgradnja, više ne treba provjeravati neuravnoteženost. Suvišne ponovne izgradnje mogu dovesti do gubitka učinkovitosti[^insert-complexity]. Prvi neuravnoteženi čvor na povratnom putu upravo je takozvani „žrtveni jarac” (scapegoat).

### Brisanje

Brisanje je vrlo jednostavno. Strategija brisanja scapegoat stabla jest „lijeno brisanje”: kad čvor postane prazan, ne uklanjamo ga, nego ga ostavljamo za kasniju obradu.

Naravno, ako u stablu ima previše praznih čvorova, učinkovitost pristupa stablu znatno pada. Zato scapegoat stablo održava dva brojača: broj neizbrisanih čvorova u cijelom stablu i broj stvarno iskorištenih čvorova u cijelom stablu. Za odabrani prag[^threshold] $\alpha\in(0,1)$, kad omjer prvog i drugog padne ispod $\alpha$, cijelo se stablo jednom ponovno izgradi, pri čemu se uklone svi prazni čvorovi.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:remove"
    ```

### Vremenska složenost

U scapegoat stablu veličine $n$ vremenska složenost jednog pristupa čvoru je $O(\log n)$; vremenska složenost $\Theta(n)$ umetanja i brisanja također je amortizirano $O(\log n)$ po operaciji.

Ovaj odjeljak daje samo kratko obrazloženje vremenske složenosti scapegoat stabla; za detaljan dokaz pogledajte izvorni rad.

??? note "Obrazloženje vremenske složenosti scapegoat stabla"
    Zbog strategije lijenog brisanja scapegoat stablo s $n$ neizbrisanih čvorova može zauzimati $\alpha^{-1}n$ čvorova. Budući da se razlikuju samo za konstantni faktor, u ovom tekstu ne razlikujemo broj neizbrisanih čvorova i broj zauzetih čvorova scapegoat stabla, nego oboje nazivamo „veličinom stabla”.
    
    1.  **Pristup**: složenost pristupa zajamčena je time što je visina scapegoat stabla veličine $n$ uvijek $O(\log n)$.
    
        Najprije razlikujemo dva pojma:
    
        -   $\alpha$‑težinska ravnoteža: u svakom čvoru veličine podstabala lijevog i desnog djeteta ne premašuju $\alpha$ puta veličinu podstabla tog čvora;
        -   $\alpha$‑visinska ravnoteža: visina stabla ne premašuje $\lfloor\log_{1/\alpha}|T|\rfloor$, gdje je $|T|$ veličina stabla.
    
        Iz $\alpha$‑težinske ravnoteže slijedi $\alpha$‑visinska ravnoteža, jer se sa svakim povećanjem dubine za jedan veličina podstabla smanji na najviše $\alpha$ puta prijašnju; obrat ne mora vrijediti. Preciznije, nakon završetka svake operacije scapegoat stablo uvijek je $\alpha$‑visinski uravnoteženo[^hei-bal], što jamči složenost pristupa.
    
        Samo umetanje mijenja strukturu stabla, pa je dovoljno pokazati da je nakon svakog umetanja scapegoat stablo i dalje $\alpha$‑visinski uravnoteženo. Ako je novoumetnuti čvor predubok, tako da cijelo stablo više nije $\alpha$‑visinski uravnoteženo, tada pri povratku od tog čvora do korijena nužno naiđemo na barem jedan čvor, „žrtvenog jarca”, čije podstablo više nije $\alpha$‑težinski uravnoteženo. Nakon njegove ponovne izgradnje visina podstabla smanji se barem za jedan, pa novoumetnuti čvor više nije predubok.
    2.  **Umetanje**: složenost umetanja je amortizirano $O(\log n)$.
    
        Pretpostavimo da nakon nekog umetanja u čvoru $x$ dođe do ponovne izgradnje podstabla, s vremenskim troškom $\Theta(|T_x|)$. Kad je čvor $x$ tek umetnut, ili neposredno nakon prethodne ponovne izgradnje (njega samog ili nekog pretka), njegova se lijeva i desna podstabla razlikuju najviše za jedan čvor. A neposredno prije ove ponovne izgradnje u čvoru $x$ nužno vrijedi
    
        $$
        \max\{|T_{\mathrm{left}(x)}|,|T_{\mathrm{right}(x)}|\} > \alpha\cdot |T_x|.
        $$
    
        Taj uvjet jamči da je razlika veličina lijevog i desnog podstabla barem $(2\alpha-1)|T_x|$. Stoga je između tih dviju ponovnih izgradnji u podstablo $T_x$ umetnuto $\Omega(|T_x|)$ čvorova.
    
        Amortiziranom analizom dobivamo[^alternative-analysis]: ako pri svakom umetanju čvora u svakom čvoru na putu od korijena do tog čvora (prije eventualne ponovne izgradnje) povećamo potencijal za $\Theta(1)$, tada se do ponovne izgradnje podstabla u čvoru $x$ u tom čvoru nužno nakupi potencijal $\Omega(|T_x|)$, dovoljan da plati trošak $\Theta(|T_x|)$ ponovne izgradnje podstabla u $x$. Budući da je dubina stabla uvijek $O(\log n)$, potencijal dodan jednim umetanjem je $O(\log n)$; to znači da je ukupno povećanje potencijala tijekom $\Theta(n)$ umetanja $O(n\log n)$. Stoga je i ukupni trošak ponovnih izgradnji podstabala $O(n\log n)$, pa je amortizirana vremenska složenost jednog umetanja (uključujući ponovnu izgradnju) $O(\log n)$.
    
        Primijetite da analiza ne pretpostavlja da se između dviju ponovnih izgradnji u čvoru $x$ unutar podstabla $T_x$ nisu dogodile druge ponovne izgradnje. Zato, dok god ponovno izgrađujemo samo podstabla čvorova koji zadovoljavaju uvjet neuravnoteženosti, složenost ostaje ispravna.
    3.  **Brisanje**: složenost brisanja također je amortizirano $O(\log n)$.
    
        Ponovna izgradnja izazvana brisanjem dovodi do toga da cijelo stablo ne sadrži prazne čvorove. Prije nego što neko brisanje izazove ponovnu izgradnju, u cijelom stablu već ima $\Theta(n)$ praznih čvorova, što znači da je obavljeno barem $\Theta(n)$ brisanja. Budući da je složenost pronalaženja čvora pri svakom brisanju $O(\log n)$, a složenost jedne ponovne izgradnje $\Theta(n)$, stvarni vremenski trošak tih $\Theta(n)$ brisanja iznosi
    
        $$
        \Theta(n)O(\log n)+\Theta(n)
        $$
    
        . Stoga je amortizirana složenost jednog brisanja $O(\log n)$.

## Operacije balansiranog stabla

Ovaj odjeljak opisuje kako scapegoat stablom održavati multiskup.

Osim operacija opisanih u prethodnom odjeljku, ostale su operacije uobičajene operacije balansiranog stabla. Međutim, budući da u scapegoat stablu mogu postojati prazni čvorovi, i te operacije treba odgovarajuće prilagoditi.

### Upit ranga

Koristeći svojstvo binarnog stabla pretraživanja spuštamo se do položaja čvora i usput brojimo vrijednosti pohranjene lijevo od puta.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:find-rank"
    ```

### Upit vrijednosti po rangu

Spuštamo se koristeći informaciju o broju vrijednosti pohranjenih u podstablu koju čuva svaki čvor. Pazite da mogu postojati čvorovi s brojačem nula.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:find-kth"
    ```

### Upit prethodnika i sljedbenika

Dovoljno je kombinirati prethodne dvije funkcije.

???+ example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:pred-succ"
    ```

Ako ih želite implementirati izravno, pazite na obradu čvorova s brojačem nula.

### Primjer implementacije

Na kraju odjeljka dajemo primjer implementacije za ogledni zadatak [Obično balansirano stablo](https://loj.ac/p/104).

??? example "Primjer implementacije"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:full-text"
    ```

## Literatura

-   Galperin, Igal, and Ronald L. Rivest. "Scapegoat trees." Proceedings of the fourth annual ACM-SIAM Symposium on Discrete algorithms. 1993.
-   [Scapegoat Tree - Wikipedia](https://en.wikipedia.org/wiki/Scapegoat_tree)
-   [Scapegoat stablo – blog riteme](https://riteme.site/blog/2016-4-6/scapegoat.html)

[^tot-cnt]: Može se brojiti i samo neizbrisane čvorove; tada više ne treba održavati `tot_active`, nego ukupan broj zauzetih čvorova `tot_max`, a kôd se odgovarajuće prilagodi.

[^insert-complexity]: Iz analize složenosti u nastavku vidi se da ti gubici učinkovitosti znače samo veći konstantni faktor, a složenost ostaje ispravna. Budući da provjera dubine stabla može uključivati dosta logaritamskih operacija s brojevima s pomičnim zarezom, kôd koji ne provjerava dubinu nego samo neuravnoteženost na nekim podacima može biti brži.

[^threshold]: Ne mora biti isti kao parametar odabran za umetanje. Iako izvorni rad to pretpostavlja, izbor različitih parametara mijenja samo konstantu u složenosti pojedine operacije, a ukupna složenost ostaje ispravna.

[^hei-bal]: Prema definiciji iz izvornog rada $n$ označava broj neizbrisanih čvorova, pa se može jamčiti samo da visina stabla ne premašuje $\lfloor\log_{1/\alpha}n\rfloor+1$, što se naziva slabom $\alpha$‑visinskom ravnotežom. Ovdje se ne bavimo tom razlikom u konstanti.

[^alternative-analysis]: Neki tekstovi pojednostavljeno analiziraju da $\Omega(|T_x|)$ umetanja odgovara jednoj ponovnoj izgradnji, pa je amortizirana složenost $\dfrac{\Omega(|T_x|)O(\log n)+\Theta(|T_x|)}{\Omega(|T_x|)} = O(\log n)$. Takvo razmišljanje pomaže razumjeti zašto je amortizirana složenost ispravna, ali nije strogo. Naime, jedno umetanje može odgovarati ponovnim izgradnjama više predaka, pa kad se u čvoru $x$ dogodi ponovna izgradnja, nije očito da je broj čvorova u podstablu koji nisu izazvali ponovnu izgradnju $\Omega(|T_x|)$.
