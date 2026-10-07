---
title: Osnove dinamičkog programiranja
---

Ova stranica uglavnom predstavlja osnovnu ideju dinamičkog programiranja te način osmišljavanja stanja i jednadžbi prijelaza stanja, kako bi početnici stekli prvi uvid u dinamičko programiranje.

Ostale stranice ovog poglavlja predstavljaju načine izgradnje modela dinamičkog programiranja za razne vrste problema te neke tehnike optimizacije dinamičkog programiranja.

## Uvod

???+ note "[\[IOI1994\] Brojčani trokut](https://www.luogu.com.cn/problem/P1216)"
    Zadan je brojčani trokut s $r$ redaka ($r \leq 1000$). Treba pronaći put od vrha do bilo kojeg mjesta u donjem retku takav da je zbroj brojeva na putu najveći. U svakom koraku može se prijeći na broj dolje lijevo ili dolje desno od trenutnog.
    
    ```plain
            7 
          3   8 
        8   1   0 
      2   7   4   4 
    4   5   2   6   5 
    ```
    
    U gornjem primjeru optimalni je put $7 \to 3 \to 8 \to 7 \to 5$.

Najjednostavnija i najgrublja ideja je isprobati sve putove. Budući da je broj putova reda $O(2^r)$, takav pristup nije prihvatljiv.

Uočimo sljedeću činjenicu: svaka odluka na optimalnom putu također je optimalna.

Uzmimo za primjer optimalni put iz zadatka i promotrimo samo prva četiri koraka $7 \to 3 \to 8 \to 7$: ne postoji put od vrha do $2$. broja u $4$. retku s većim zbrojem.

A za svaku točku sljedeća odluka ima samo dvije mogućnosti: dolje lijevo ili dolje desno (ako postoji). Zato je dovoljno zapamtiti najveći zbroj u trenutnoj točki i tim najvećim zbrojem izvesti sljedeću odluku, ažurirajući najveće zbrojeve sljedećih točaka.

Takav pristup ima još jednu prednost: uspješno smo smanjili veličinu problema, rastavivši jedan problem na više manjih problema. Da bismo dobili optimalno rješenje od vrha do $r$-tog retka, dovoljno je znati informacije o optimalnom rješenju od vrha do $(r-1)$-og retka.

Ostaje još jedan problem: potproblemi se uvelike preklapaju, pa se isti potproblem može posjetiti više puta i učinkovitost je i dalje niska. Rješenje je spremiti rješenje svakog potproblema i memoizacijom ograničiti redoslijed posjećivanja, tako da se svaki potproblem posjeti samo jednom.

To su neke osnovne ideje dinamičkog programiranja. U nastavku ćemo sustavnije predstaviti ideju dinamičkog programiranja.

## Načela dinamičkog programiranja

Problem rješiv dinamičkim programiranjem mora zadovoljavati tri uvjeta: optimalnu podstrukturu, odsutnost naknadnog utjecaja (bez posljedica) i preklapanje potproblema.

### Optimalna podstruktura

Problem s optimalnom podstrukturom možda je pogodan i za rješavanje greedy metodom.

Pazite da razmotrimo sve potprobleme koji se koriste u optimalnom rješenju.

1.  Dokažite da je prvi sastavni dio optimalnog rješenja problema donošenje jednog izbora;
2.  za zadani problem, među mogućim prvim izborima, pretpostavite da već znate koji izbor vodi do optimalnog rješenja. Ne zanima vas kako se taj izbor konkretno dobiva; samo pretpostavite da ga znate;
3.  za dani izbor koji vodi do optimalnog rješenja odredite koje potprobleme taj izbor stvara i kako najbolje opisati prostor potproblema;
4.  dokažite da je rješenje svakog potproblema, kao sastavni dio optimalnog rješenja izvornog problema, samo po sebi optimalno rješenje tog potproblema. Metoda je dokaz kontradikcijom: pretpostavimo da rješenje nekog potproblema nije njegovo optimalno rješenje; tada bismo u rješenju izvornog problema mogli zamijeniti to neoptimalno rješenje optimalnim rješenjem potproblema i dobiti bolje rješenje izvornog problema, što proturječi pretpostavci da je rješenje izvornog problema optimalno.

Prostor potproblema treba držati što jednostavnijim i proširivati ga samo kad je nužno.

Razlike u optimalnoj podstrukturi očituju se u dva aspekta:

1.  koliko potproblema uključuje optimalno rješenje izvornog problema;
2.  koliko izbora treba razmotriti pri određivanju koje potprobleme optimalno rješenje koristi.

U grafu potproblema svaki vrh odgovara jednom potproblemu, a izbori koje treba razmotriti odgovaraju bridovima koji vode u vrhove potproblema.

### Bez naknadnog utjecaja

Na već riješene potprobleme ne utječu kasnije odluke.

### Preklapanje potproblema

Ako postoji mnogo preklapajućih potproblema, možemo utrošiti memoriju da spremimo rješenja tih potproblema i tako izbjegnemo ponovno rješavanje istih potproblema, čime se povećava učinkovitost.

### Osnovni pristup

Problem rješiv dinamičkim programiranjem obično se rješava na sljedeći način:

1.  Izvorni problem podijelimo na nekoliko **faza**; svaka faza odgovara nekoliko potproblema, čije značajke izdvojimo (zovemo ih **stanja**);
2.  pronađemo moguće **odluke** za svako stanje, odnosno načine prijelaza među stanjima (matematičkim jezikom: **jednadžbu prijelaza stanja**);
3.  redom rješavamo probleme svake faze.

Shvatimo li to u terminima teorije grafova, gradimo [usmjereni aciklički graf](../graph/dag.md) u kojem svako stanje odgovara čvoru grafa, a odluke odgovaraju bridovima među čvorovima. Tako se problem pretvara u traženje najduljeg (najkraćeg) puta u DAG-u (vidi [DP na DAG-u](./dag.md)).

## Najdulji zajednički podniz

???+ note "Problem najduljeg zajedničkog podniza"
    Zadan je niz $A$ duljine $n$ i niz $B$ duljine $m$ ($n,m \leq 5000$). Treba pronaći najdulji niz koji je podniz i od $A$ i od $B$.

Definiciju podniza možete pogledati u [podniz](../string/basic.md). Kratak primjer: zajednički podnizovi stringova `abcde` i `acde` su `a`, `c`, `d`, `e`, `ac`, `ad`, `ae`, `cd`, `ce`, `de`, `acd`, `ade`, `ace`, `cde`, `acde`, a duljina najduljeg zajedničkog podniza je 4.

Neka $f(i,j)$ označava duljinu najduljeg zajedničkog podniza kad se promatra samo prvih $i$ elemenata niza $A$ i prvih $j$ elemenata niza $B$; traženje te duljine je **potproblem**. $f(i,j)$ je ono što zovemo **stanjem**, a $f(n,m)$ je konačno stanje koje treba dosegnuti, tj. traženi rezultat.

Za svako $f(i,j)$ postoje tri odluke: ako je $A_i=B_j$, može se dodati na kraj zajedničkog podniza; druge su dvije odluke preskočiti $A_i$ odnosno $B_j$. Jednadžba prijelaza stanja glasi:

$$
f(i,j)=\begin{cases}f(i-1,j-1)+1&A_i=B_j\\\max(f(i-1,j),f(i,j-1))&A_i\ne B_j\end{cases}
$$

Za bolje razumijevanje postupka LCS-a možete pogledati [interaktivnu LCS stranicu na SourceForgeu](http://lcs-demo.sourceforge.net/).

???+ example "Primjer implementacije"
    === "C++"
        ```cpp
        --8<-- "docs/dp/code/basic/lcs.cpp:core"
        ```
    
    === "Python"
        ```cpp
        --8<-- "docs/dp/code/basic/lcs.py:core"
        ```

Vremenska složenost ovog pristupa je $O(nm)$.

Osim toga, za ovaj problem postoji i algoritam složenosti $O\left(\dfrac{nm}{w}\right)$[^ref1]. Zainteresirani ga mogu istražiti sami.

## Najdulji nepadajući podniz

???+ note "Problem najduljeg nepadajućeg podniza"
    Zadan je niz $a$ duljine $n$ ($n \leq 5000$). Treba pronaći najdulji podniz od $a$ takav da svaki sljedeći element nije manji od prethodnog.

### Algoritam 1

Neka $f(i)$ označava duljinu najduljeg nepadajućeg podniza koji završava s $a_i$; traži se $\max_{1 \leq i \leq n} f(i)$.

Pri računanju $f(i)$ pokušavamo $a_i$ nadovezati na druge najdulje nepadajuće podnizove i tako ažurirati odgovor. Tako dobivamo jednadžbu prijelaza stanja: $f(i)=\max_{1 \leq j < i,~a_j \leq a_i} (f(j)+1)$.

???+ example "Primjer implementacije"
    === "C++"
        ```cpp
        --8<-- "docs/dp/code/basic/lis-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/dp/code/basic/lis-1.py:core"
        ```

Lako se vidi da je vremenska složenost ovog algoritma $O(n^2)$.

### Algoritam 2

Kad se raspon $n$ proširi na $n \leq 10^5$, prvi pristup više nije dovoljno brz; u nastavku dajemo pristup složenosti $O(n \log n)$.

Promotrimo prije definirano stanje $(i, l)$: označava da je najdulji nepadajući podniz koji završava $i$-tim elementom duljine $l$. Za razliku od dosadašnjeg pristupa obrade stanja po fiksnom $i$, ovdje izravno provjeravamo je li $(i, l)$ valjano:

-   Početno stanje $(1,1)$ sigurno je valjano.
-   Za bilo koje $(i, l)$: ako postoji $j < i$ takav da je $(j, l-1)$ valjano i ujedno $a_j \le a_i$, onda je $(i, l)$ valjano.

Na kraju je dovoljno među valjanim stanjima pronaći $(i,l)$ s najvećim $l$ i dobili smo duljinu najduljeg nepadajućeg podniza.

Neka je izvorni niz $a_1, \cdots, a_n$. Definiramo niz $d$ u kojem $x$-ti element označava najmanju vrijednost posljednjeg elementa nepadajućeg podniza duljine $x$. Početno je niz prazan. Neka $i$ prolazi od $1$ do $n$ i redom računamo duljinu najduljeg nepadajućeg podniza prvih $i$ elemenata. Za trenutni element $a_i$:

-   Ako je $a_i$ veći ili jednak posljednjem elementu niza $d$, element $a_i$ izravno dodajemo na kraj niza $d$.
    -   Objašnjenje: ako je $a_i$ veći ili jednak posljednjem elementu trenutno najduljeg podniza, postoji nepadajući podniz na koji se $a_i$ može nadovezati. Ne dodati ga narušilo bi optimalnost.
-   Ako je $a_i$ strogo manji od posljednjeg elementa niza $d$, pronađemo **prvi** element veći od njega i zamijenimo ga s $a_i$.
    -   Objašnjenje: kad bismo ga dodali na kraj, narušili bismo monotonost niza $d$; zamjena jamči da je posljednji element za svaku duljinu što manji, čime se kasnijim elementima ostavlja više mogućnosti.
    -   Optimizacija: budući da je $d$ monotono neopadajući, binarnim pretraživanjem izravno nalazimo mjesto umetanja, čime se ukupna složenost smanjuje na $O(n\log n)$ umjesto $O(n^2)$ grubim pretraživanjem.

Ako treba ispisati i sam najdulji nepadajući podniz, možemo dodatno održavati niz $d'_x$ koji označava položaj najmanjeg posljednjeg elementa među nepadajućim podnizovima duljine $x$ (ako ih je više, bilo koji). Konkretno, pri umetanju elementa $a_i$ u $d_x$ ujedno postavimo $d'_x$ na $i$. Istodobno treba zapisati optimalnog prethodnika $p_i$ od $i$ kao $d'_{x-1}$. Na kraju, iz bilo kojeg stanja najveće duljine, praćenjem prethodnika $p_i$ unatrag dobivamo cijeli podniz.

???+ example "Primjer implementacije"
    === "C++"
        ```cpp
        --8<-- "docs/dp/code/basic/lis-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/dp/code/basic/lis-2.py:core"
        ```

Vremenska složenost ovog algoritma je $O(n\log n)$. Vremenska složenost ispisa odgovora je $O(\textit{ans})$.

???+ tip "Napomena"
    Za problem najduljeg **rastućeg** podniza slično možemo definirati $d_i$ kao najmanju vrijednost posljednjeg elementa među svim najduljim rastućim podnizovima duljine $i$.
    
    Treba pripaziti da u 2. koraku, ako je $a_i \leq d_{len}$, budući da susjedni elementi najduljeg rastućeg podniza ne smiju biti jednaki, u nizu $d$ treba pronaći **prvi** element **koji nije manji od** $a_i$ i zamijeniti ga s $a_i$.
    
    U implementaciji (npr. u C++-u) treba funkciju `upper_bound` zamijeniti s `lower_bound`.

## Literatura i bilješke

-   [Detaljno objašnjenje algoritma nlogn za najdulji nepadajući podniz – lvmememe – cnblogs (kineski)](https://www.cnblogs.com/itlqs/p/5743114.html)

[^ref1]: [Najdulji zajednički podniz pomoću bitovnih operacija – -Wallace- – cnblogs (kineski)](https://www.cnblogs.com/-Wallace-/p/bit-lcs.html)
