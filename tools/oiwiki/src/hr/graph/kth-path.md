---
title: k-ti najkraći put
---

Preduvjeti: [Dijkstrin algoritam](./shortest-path.md#dijkstrin-algoritam), [A\* algoritam](../search/astar.md), [perzistentni spojivi heap](../ds/persistent-heap.md)

## Opis problema

Zadan je usmjereni graf s $n$ vrhova i $m$ bridova; odredite duljinu $k$-tog najkraćeg među svim različitim putovima od $s$ do $t$.

???+ info "„Put”"
    „Put” u ovom članku smije više puta proći istim bridom ili istim vrhom, pa bi strogi naziv bio „[šetnja](./concept.md#putevi)” (walk), a ne „put”. Problem o kojem govorimo strogo je, dakle, problem **$k$-te najkraće šetnje** ($k$ shortest walk). No, prema uvriježenoj praksi, u članku i dalje rabimo naziv „put”, a put koji se ne siječe sam sa sobom zovemo „jednostavni put”.

## A\* algoritam

A\* je algoritam pretraživanja. Svakom trenutnom stanju $x$ pridružuje funkciju procjene $f(x)=g(x)+h(x)$, gdje je $g(x)$ stvarna cijena dolaska iz početnog stanja u trenutno stanje, a $h(x)$ procijenjena cijena najboljeg puta iz trenutnog stanja do ciljnog stanja. Pri pretraživanju svaki put uzimamo stanje $x$ s najboljim $f(x)$ i proširujemo sva njegova sljedeća stanja. Tu vrijednost možemo održavati **prioritetnim redom**.

Pri rješavanju problema $k$-tog najkraćeg puta neka $h(x)$ bude duljina najkraćeg puta od trenutnog vrha do ciljnog vrha $t$. Tu vrijednost za svaki vrh možemo predizračunati pokretanjem najkraćeg puta iz jednog izvora od vrha $t$ na obrnutom grafu. Za svako stanje pamtimo dvije vrijednosti: trenutni vrh $x$ i već prijeđenu udaljenost $g(x)$; takvo stanje označimo $(x,g(x))$. Na početku u prioritetni red stavimo početno stanje $(s,0)$. Svaki put uzimamo stanje s najmanjom funkcijom procjene $f(x)=g(x)+h(x)$, prolazimo sve izlazne bridove vrha $x$ tog stanja i odgovarajuća sljedeća stanja stavljamo u prioritetni red. Kad neki vrh $k$-ti put izađe iz reda, $g(x)$ tog stanja duljina je $k$-tog najkraćeg puta od početnog vrha $s$ do tog vrha.

Ovaj se postupak pretraživanja može optimizirati. Budući da trebamo samo $k$-ti najkraći put od početnog do ciljnog vrha, kad neki vrh izađe iz reda $k$ puta, stanjima tog vrha koja kasnije izlaze iz reda ne trebamo proširivati sljedeća stanja. Ta stanja ne utječu na konačni odgovor, jer je pri prethodnih $k$ vađenja tog vrha već nastalo $k$ valjanih putova do tog vrha, što je dovoljno za konstrukciju prvih $k$ najkraćih putova do ciljnog vrha.

Budući da se svaki vrh proširuje najviše $k$ puta, svaki brid ulazi u prioritetni red najviše $k$ puta, pa je vremenska složenost algoritma $O(km\log km)$, a prostorna $O(km)$. U odnosu na izravno pretraživanje, A\* odsijeca prema ciljnom vrhu $t$, ali to popravlja samo konstantu, a ne asimptotsku složenost. Iako složenost algoritma iz ovog odjeljka nije sjajna, on u istoj složenosti nalazi prvih $k$ najkraćih putova od početnog vrha $s$ do svakog vrha (u stablu najkraćih putova s korijenom $t$).

### Implementacija

??? example "Referentna implementacija za zadatak-predložak [Library Checker - K-Shortest Walk](https://judge.yosupo.jp/problem/k_shortest_walk)"
    ```cpp
    --8<-- "docs/graph/code/k-shortest-walk/k-shortest-walk-1.cpp"
    ```

## Pristup s perzistentnim spojivim heapom

Prethodni algoritam zapravo nalazi $k$ najkraćih putova do svih vrhova. Ako želimo samo $k$ najkraćih putova do zadanog ciljnog vrha $t$, može se brže. Ovaj odjeljak daje pristup složenosti $O(m\log m+k\log k)$ zasnovan na perzistentnom spojivom heapu.

### Stablo najkraćih putova i bočni bridovi

Usko grlo prethodnog algoritma jest to što se odgovor ažurira tek pri dolasku u ciljni vrh $t$. No različiti putovi mogu se vrlo malo razlikovati. Primjerice, drugi najkraći put može se od najkraćeg razlikovati samo tako da kod jednog brida zaobiđe jedan vrh više, dok su ostali dijelovi puta jednaki; prethodni algoritam ipak možda mora iznova pretražiti sve te jednake bridove da bi našao drugi najkraći put. Budući da je bitan samo dio koji zaobilazi, za prvih $k$ najkraćih putova dovoljno je razmotriti $k$ najjeftinijih načina zaobilaženja. To nas dovodi do pojma stabla najkraćih putova.

Na obrnutom grafu pokrenemo najkraći put iz jednog izvora od ciljnog vrha $t$, zapamtimo duljinu najkraćeg puta $h(x)$ od svakog vrha $x$ do $t$ te prvi brid $f_x$ na najkraćem putu iz vrha $x$; ako ima više optimalnih izbora, uzmemo onaj koji je Dijkstrin algoritam zapisao pri relaksaciji. Svi ti bridovi $f_x$ i njihovi krajevi čine stablo, a jednostavni put od svakog vrha $x$ stabla do korijena $t$ jedan je najkraći put od $x$ do $t$. To je **stablo najkraćih putova** $T$.

Kad imamo stablo najkraćih putova $T$, za svaki brid koji nije u $T$ možemo izračunati koliko puta on produljuje. Za brid $e=(u,v)\notin T$ težine $w$ definiramo novi brid, i dalje od $u$ prema $v$, s cijenom $\Delta(e)=w + h(v) - h(u)$. Takve bridove s težinama $\Delta(e)$ u članku slikovito zovemo **bočni bridovi** (sidetrack), a težinu $\Delta(e)$ cijenom skretanja. Zbog $h(u)\le w+h(v)$ cijena skretanja uvijek je nenegativna. Ako krajevi nekog brida nisu oba u stablu najkraćih putova $T$, taj brid ne utječe na račun $k$-tog najkraćeg puta do vrha $t$ i možemo ga jednostavno izbrisati.

Na slici dolje lijevo je usmjereni graf $G$, a desno njegovo stablo najkraćih putova $T$ (debeli bridovi) i odgovarajući bočni bridovi (tanki bridovi):

![](./images/k-shortest-path-1.svg)

Neka je $P$ niz bridova kojima prolazi put od $s$ do $t$; uklanjanjem iz $P$ bridova koji su u $T$ dobivamo $P'$. Tada za bridove $P'$ poredane redom svaka dva susjedna brida $e_1=(u_1,v_1)$ i $e_2=(u_2,v_2)$ sigurno zadovoljavaju

-   Uvjet $(*)$: početak drugoga $u_2$ predak je (uključujući i sam vrh) kraja prvoga $v_1$ u stablu najkraćih putova $T$. Za prvi brid dogovorno uzimamo da je „kraj prethodnoga” jednak $s$.

To vrijedi jer su u izvornom putu $P$ vrhovi $v_1$ i $u_2$ povezani nizom stablastih bridova iz $T$. Obratno, za svaki niz bridova $P'$ koji zadovoljava uvjet $(*)$ postoji točno jedan put $P$ u grafu $G$ koji mu odgovara, jer je jednostavni put između $v_1$ i $u_2$ u stablu najkraćih putova $T$ jedinstven. Time smo pokazali da su putovi $P$ u izvornom grafu u bijekciji s nizovima bočnih bridova $P'$ koji zadovoljavaju uvjet $(*)$. Štoviše, duljina puta $P$ jednaka je zbroju duljine najkraćeg puta $h(s)$ i tih cijena skretanja:

$$
h(s)+\sum_{e\in P'}\Delta(e).
$$

Ova razmatranja pokazuju da se zadatak nalaženja $k$-tog najkraćeg puta pretvara u zadatak nalaženja niza bočnih bridova $P'$ koji zadovoljava uvjet $(*)$ i ima $k$-tu najmanju cijenu.

Za obradu uvjeta $(*)$, umjesto da pri svakom upitu tražimo pretke u stablu najkraćih putova, bolje je skup bočnih bridova svakog vrha izravno spustiti na njegove potomke u stablu najkraćih putova. To odgovara gradnji ovakvog grafa $G'$:

![](./images/k-shortest-path-2.svg)

U tom se grafu uvjet $(*)$ pretvara u zahtjev da se bridovi u $P'$ nastavljaju jedan na drugi, tj. da je $P'$ put u grafu $G'$. Problem se dalje pretvara u nalaženje puta $k$-te najmanje duljine iz $s$ **do bilo kojeg vrha** u tom grafu. Za razliku od izvornog problema $k$-tog najkraćeg puta, ovdje se više ne zahtijeva da put završi u ciljnom vrhu $t$.

Pretvoreni problem lako se rješava. Krenemo iz početnog vrha $s$ i prioritetnim redom proširujemo putove po duljini od manje prema većoj (isti vrh može izaći iz reda više puta). Svaki put kad iz prioritetnog reda uzmemo vrh, pronašli smo jedan put u grafu $G'$, koji odgovara jednom putu do ciljnog vrha $t$ u grafu $G$.

### Optimizacija perzistentnim spojivim heapom

Ideja algoritma sada je jasna. No naivna implementacija ima preveliku složenost. Budući da u grafu $G'$ broj bridova u jednom vrhu može biti $\Theta(m)$, pri svakom proširenju vrha možda moramo u prioritetni red staviti skup bridova veličine $\Theta(m)$. Zapravo nije potrebno staviti sve bridove u prioritetni red: od stavljenih bridova često samo najkraći mogu kasnije izaći iz reda. Dakle, cijeli skup bridova jednog vrha možemo staviti u prioritetni red kao jednu jedinicu pohrane; dovoljno je da brzo možemo pristupiti najkraćem bridu skupa.

To nas potiče da skup bridova jednog vrha pohranimo u min-heap. U prioritetni red tada stavljamo samo te heapove, a njihova je cijena cijena puta koji odgovara bridu na vrhu heapa. Pri svakom vađenju iz prioritetnog reda iz heapa na vrhu reda ujedno izvadimo brid s vrha heapa. Zatim heap bez vrha vratimo u prioritetni red, a u prioritetni red stavimo i heap skupa bočnih bridova kraja izvađenog brida.

Pohrana skupa bridova u heap rješava i problem spuštanja skupova bridova niz stablo najkraćih putova. Spuštanje skupa bridova odgovara spajanju skupa bridova trenutnog vrha u skup njegova djeteta, pa heap mora podržavati spajanje; pri spajanju u dijete ne smijemo uništiti skup bridova trenutnog vrha, pa heap mora biti i perzistentan. To je upravo perzistentni spojivi heap.

Tako dobivamo cijeli postupak algoritma:

1.  Iz ciljnog vrha $t$ pokrenemo najkraći put iz jednog izvora i odredimo stablo najkraćih putova.
2.  Za svaki vrh stabla najkraćih putova izgradimo odgovarajući skup bočnih bridova i pohranimo ga u perzistentni spojivi heap.
3.  Duž bridova stabla najkraćih putova, od ciljnog vrha $t$ odozgo prema dolje (npr. u BFS poretku), heap svakog vrha spojimo u heap njegova djeteta.
4.  Zabilježimo duljinu najkraćeg puta $h(s)$ kao prvi odgovor, zatim iz početnog vrha $s$ stavimo heap tog vrha u prioritetni red.
5.  Izvadimo heap s vrha reda, zabilježimo odgovor, zatim heap bez vrha vratimo u prioritetni red, a u prioritetni red stavimo i heap kraja brida s vrha heapa.

Perzistentni spojivi heap obično se implementira lijevo nagnutim stablom (leftist tree) ili nasumičnim heapom. Tada se i posljednji korak može dodatno optimizirati. Unutarnja struktura tih heapova binarno je stablo. Nakon vađenja vrha heapa izvorno bi trebalo spojiti lijevo i desno dijete i vrh spojenog heapa staviti u prioritetni red; no u ovom algoritmu spajanje možemo preskočiti i heapove oba djeteta zasebno staviti u prioritetni red. Tako štedimo $O(\log m)$ po jednom spajanju. Budući da se nakon vađenja heapa s vrha reda u prioritetni red stavlja najviše tri nova heapa, veličina prioritetnog reda je $O(k)$. Time se složenost jednog upita smanjuje na $O(\log k)$, a ukupna složenost upita je $O(k\log k)$.

Budući da su gradnja stabla najkraćih putova i gradnja perzistentnog spojivog heapa složenosti $O(m\log m)$, ukupna je vremenska složenost algoritma $O(m\log m+k\log k)$.

### Implementacija

??? example "Referentna implementacija za zadatak-predložak [Library Checker - K-Shortest Walk](https://judge.yosupo.jp/problem/k_shortest_walk)"
    ```cpp
    --8<-- "docs/graph/code/k-shortest-walk/k-shortest-walk-2.cpp"
    ```

## Zadaci

-   [„SDOI2010” 魔法猪学院](https://www.luogu.com.cn/problem/P2483)

## Literatura i napomene

-   [\[Tutorial\] k shortest paths and Eppstein's algorithm by meooow - Codeforces](https://codeforces.com/blog/entry/102085)
