---
title: Centroid stabla
---

Ovaj članak predstavlja pojam centroida stabla i njegova osnovna svojstva.

## Definicija

Ako nakon uklanjanja nekog čvora $v$ iz stabla $T$ svaka komponenta povezanosti dobivenog grafa $T\setminus\{v\}$ ima veličinu koja ne premašuje polovinu broja čvorova izvornog stabla, čvor $v$ nazivamo **centroidom** (centroid) cijelog stabla. Veličina najveće komponente povezanosti dobivene uklanjanjem nekog čvora naziva se i **težinom** (weight) tog čvora. S tim pojmom definicija centroida glasi: čvor čija težina ne premašuje polovinu broja čvorova stabla.

???+ info "„Podstablo”"
    Ovaj se članak može istodobno baviti nekorijenskim stablima, korijenskim stablima i stablima dobivenima promjenom korijena korijenskog stabla u nekorijenski čvor. Da bismo izbjegli zabunu, nekorijensko stablo označavat ćemo s $T$, a korijensko stablo s korijenom $v$ s $T^{(v)}$. „Podstablo” u ovom članku uvijek znači stablo koje u **korijenskom stablu** čine neki čvor i svi njegovi potomci. U korijenskom stablu $T^{(v)}$ podstablo koje odgovara čvoru $u$ označavamo $T^{(v)}_u$. Tako definirano podstablo, naravno, uključuje i cijelo stablo. Ako želimo izričito isključiti cijelo stablo, govorit ćemo o „pravom podstablu”.
    
    „Podstablo” nekorijenskog stabla obično označava neki njegov povezani podgraf. Pri raspravi o centroidu neki autori riječju „podstablo” označavaju maksimalni povezani podgraf koji ne sadrži neki čvor ili jednu od dviju komponenata povezanosti dobivenih uklanjanjem nekog brida. Lako se provjeri da su skupovi „podstabala” definiranih na ta dva načina jednaki i da ne uključuju cijelo stablo. Budući da se taj skup ne podudara sa skupom podstabala korijenskog stabla, u ovom ćemo članku izbjegavati pojam „podstabla” za nekorijenska stabla.
    
    Pri stvarnom računanju centroida ili rješavanju nekih zadataka obično postoji zadani korijen. Tada među komponentama povezanosti dobivenima uklanjanjem nekorijenskog čvora $v$, osim podstabala koja odgovaraju djeci tog čvora, postoji i jedno podstablo „prema gore”. Ako je roditelj čvora $v$ čvor $u$, to je podstablo „prema gore” upravo $T_u^{(v)}$. Kad u ovom članku spominjemo takav podgraf, izričito ćemo ga zvati podstablom „prema gore”. Ako nije drukčije naznačeno, podstabla koja spominjemo ne uključuju takva podstabla „prema gore”.

Uočimo da su dobivene komponente povezanosti također nekorijenska stabla. Uklanjanjem centroida stablo se raspada na više stabala veličine najviše polovine izvornog. To svojstvo centroida omogućuje primjenu ideje „podijeli pa vladaj” na stablima. To je [centroid decomposition](./tree-divide.md#centroidna-dekompozicija), koja se naziva i dekompozicijom stabla po centroidima.

## Svojstva

U ovom odjeljku raspravljamo o svojstvima centroida. Najprije, centroid stabla ima sljedeće ekvivalentne definicije:

???+ note "Ekvivalentne definicije"
    Čvor $v$ stabla $T$ njegov je centroid ako i samo ako vrijedi bilo koji od sljedećih uvjeta:
    
    === "Inačica za nekorijensko stablo"
        1.  Nakon uklanjanja čvora $v$ iz stabla, svaka komponenta povezanosti dobivenog grafa $T\setminus\{v\}$ ima veličinu koja ne premašuje polovinu broja čvorova izvornog stabla.
        2.  Među veličinama najveće komponente povezanosti dobivene uklanjanjem pojedinog čvora, vrijednost dobivena uklanjanjem čvora $v$ je najmanja.
        3.  Među zbrojevima udaljenosti svih čvorova stabla do pojedinog čvora, zbroj udaljenosti do čvora $v$ je najmanji.
    
    === "Inačica za korijensko stablo"
        1.  Kad je stablo ukorijenjeno u čvoru $v$, veličina svakog pravog podstabla ne premašuje polovinu broja čvorova izvornog stabla.
        2.  Među veličinama najvećeg pravog podstabla kad je stablo ukorijenjeno u pojedinom čvoru, vrijednost dobivena s korijenom $v$ je najmanja.
        3.  Među zbrojevima dubina svih čvorova kad je stablo ukorijenjeno u pojedinom čvoru, zbroj dubina s korijenom $v$ je najmanji.

??? note "Dokaz"
    Najprije uvedimo oznake. Formulacije za korijensko i nekorijensko stablo očito su ekvivalentne. Definiramo $W(x)=\max_{u\sim x}|T_u^{(x)}|$, gdje $u\sim x$ znači da su $u$ i $x$ susjedni. Definiramo $S(x)=\sum_{u\in T}d(u,x)$, gdje je $d(u,x)$ udaljenost između čvorova $u$ i $x$. Tada definicija 1 odgovara zahtjevu $W(v)\le |T|/2$, definicija 2 zahtjevu $v\in\arg\min_{x\in T}W(x)$, a definicija 3 zahtjevu $v\in\arg\min_{x\in T}S(x)$. Treba dokazati da su ta tri uvjeta ekvivalentna.
    
    Shvatimo $S(x)$ kao zbroj dubina čvorova kad je korijen $x$ i promotrimo kako se mijenja kad korijen iz čvora $v$ premjestimo u susjedni čvor $u$. Uočimo da su nakon uklanjanja brida $(v,u)$ iz stabla dvije dobivene komponente povezanosti upravo podstabla $T_v^{(u)}$ i $T_u^{(v)}$. Pri promjeni korijena dubina svakog čvora u podstablu $T_v^{(u)}$ poveća se za $1$, a dubina svakog čvora u podstablu $T_u^{(v)}$ smanji se za $1$, pa je promjena zbroja dubina
    
    $$
    \Delta S_{v\to u} = S(u) - S(v) = |T_v^{(u)}| - |T_u^{(v)}| = |T| - 2|T_u^{(v)}|.
    $$
    
    Stoga uvjet definicije 1 odgovara zahtjevu da $\Delta S_{v\to u}\ge 0$ vrijedi za sve susjede $u$ čvora $v$, odnosno da je $v$ lokalni minimum funkcije $S(\cdot)$.
    
    Pretpostavimo sada da je $v$ (neka) točka globalnog minimuma funkcije $S(\cdot)$ (tj. definicija 3); ona nužno postoji i sigurno je lokalni minimum. Promotrimo korijensko stablo $T^{(v)}$ s korijenom $v$. Neka je $u\neq v$ nekorijenski čvor, i neka je na usmjerenom putu od $v$ do $u$ čvor koji slijedi nakon $v$ označen $y$ (može biti i sam $u$), a čvor koji prethodi $u$ označen $x$ (može biti i sam $v$). Budući da je $T_u^{(x)}\subseteq T_y^{(v)}$, vrijedi
    
    $$
    2|T_x^{(u)}| = 2|T| - 2|T_u^{(x)}| \ge 2|T| - 2|T_y^{(v)}| \ge |T|.
    $$
    
    Pritom posljednji korak koristi činjenicu da je $v$ lokalni minimum funkcije $S(\cdot)$. Sada postoje dva slučaja:
    
    -   Postoji čvor $u$ za koji vrijedi $2|T_x^{(u)}|=|T|$. Tada prema gornjoj nejednakosti nužno vrijedi $(x,u)=(v,y)$ i $|T_v^{(u)}|=|T_{u}^{(v)}| = |T|/2$. Drugim riječima, čvor $u$ za koji vrijedi jednakost nužno je susjed čvora $v$; a kako je zbroj veličina podstabala koja odgovaraju svim susjedima čvora $v$ jednak $|T|-1<|T|$, takav čvor $u$ može biti samo jedan. Tada za sve ostale čvorove $u'\neq u,v$ nužno postoji $x'\sim u'$ takav da vrijedi $|T_{x'}^{(u')}| > |T|/2$. Skup čvorova koji zadovoljavaju uvjet 1 je $\{v,u\}$.
    
        Uočimo da je pri uklanjanju bilo kojeg čvora zbroj veličina dobivenih komponenata povezanosti uvijek $|T|-1$, pa čim je neka komponenta veličine barem $|T|/2$, ona je nužno najveća. Stoga je u ovom slučaju $W(v)=W(u)=|T|/2$, a za sve $u'\neq u,v$ vrijedi $W(u') > |T|/2$. Dakle, skup čvorova koji zadovoljavaju uvjet 2 je $\arg\min W(\cdot) = \{v,u\}$.
    
        Nadalje, budući da je $\Delta S_{v\to u} = 0$, vrijedi $S(v)=S(u)$. Kako je $v$ točka globalnog minimuma, i $u$ je točka globalnog minimuma. A za $u'\neq u,v$ postoji $x'\sim u'$ takav da je $|T_{x'}^{(u')}| > |T|/2$, što krši uvjet koji lokalni minimum mora zadovoljavati, pa $u'$ sigurno nije ni globalni minimum. Dakle, skup čvorova koji zadovoljavaju uvjet 3 je $\arg\min S(\cdot) = \{v,u\}$.
    -   Ne postoji čvor $u$ za koji vrijedi $2|T_x^{(u)}|=|T|$. Tada za sve čvorove $u\neq v$ postoji čvor $x\sim u$ takav da je $|T_x^{(u)}| > |T|/2$. Ponavljanjem prethodne analize dobivamo da za sve čvorove $u\neq v$ vrijedi $W(u) > |T|/2$ i da $u$ nije lokalni minimum funkcije $S(\cdot)$. Dakle, jedini čvor koji zadovoljava uvjet 1 je $v$ i $\arg\min W(\cdot)=\arg\min S(\cdot) = \{v\}$.
    
    U oba su slučaja skupovi koji zadovoljavaju tri uvjeta jednaki. Time je dokazano da su tri definicije ekvivalentne.

Osim tih ekvivalentnih definicija, centroid stabla ima i sljedeća uobičajena svojstva:

???+ note "Svojstva"
    1.  Ako centroid stabla nije jedinstven, onda su točno dva. Ta su dva centroida susjedna. Štoviše, uklanjanjem brida između njih stablo se raspada na dvije komponente povezanosti jednake veličine.
    2.  Dodamo li stablu list ili ga uklonimo, centroid se pomiče za najviše jedan brid.
    3.  Spojimo li dva stabla jednim bridom u novo stablo, centroid novog stabla leži na putu koji spaja centroide dvaju izvornih stabala.
    4.  Centroid korijenskog stabla uvijek leži na teškom lancu koji sadrži korijen. Centroid stabla uvijek je predak centroida podstabla koje odgovara teškom djetetu korijena.

??? note "Dokaz"
    Svojstvo 1 slijedi iz dokaza ekvivalentnih definicija centroida.
    
    Za svojstvo 2 dovoljno je razmotriti dodavanje lista. To se dalje dijeli na dva slučaja:
    
    -   Stablo $T$ ima samo jedan centroid $v$. Neka je $x$ novododani list i neka je u novom stablu, u grafu $T\cup\{x\}\setminus\{v\}$ dobivenom uklanjanjem čvora $v$, komponenta povezanosti koja sadrži $x$ jednaka $B\cup\{x\}$. Kako je $v$ jedini centroid stabla $T$, vrijedi $2|B| < |T|$, odnosno $2|B|+1\le |T|$. Slijedi
    
        $$
        2|B\cup\{x\}| = 2(|B|+1) \le |T| + 1 = |T\cup\{x\}|.
        $$
    
        Dakle, $v$ je i dalje centroid novog stabla $T\cup\{x\}$. Čak i ako centroid novog stabla nije jedinstven, on je nužno susjed čvora $v$. Stoga se centroid pomiče za najviše jedan brid.
    -   Stablo $T$ ima dva centroida $u,v$. Tada su dvije komponente povezanosti $T_u^{(v)}$ i $T_v^{(u)}$ dobivene uklanjanjem $(u,v)$ jednake veličine, obje $|T|/2$. Bez smanjenja općenitosti neka je novododani list $x$ spojen na komponentu $T_v^{(u)}$ koja sadrži $v$. Tada, budući da je
    
        $$
        |T_v^{(u)}\cup\{x\}| = |T|/2 + 1 > (|T|+1)/2 = |T\cup\{x\}|/2,
        $$
    
        $u$ više nije centroid novog stabla. S druge strane, nakon uklanjanja $v$ i dalje postoji komponenta povezanosti $T_u^{(v)}$ veličine $|T|/2$, a zbroj veličina ostalih komponenata je
    
        $$
        |T\cup\{x\}| - 1 - |T_u^{(v)}| = |T|/2 \le |T_u^{(v)}|,
        $$
    
        pa je $v$ i dalje centroid novog stabla. Kako je broj čvorova novog stabla neparan, centroid je nužno jedinstven. Dakle, i ovdje se centroid pomiče za najviše jedan brid.
    
    Sažimajući analizu obaju slučajeva, vidimo da centroid novog stabla uvijek leži na putu između centroida starog stabla i novododanog lista.
    
    Svojstvo 3 može se pokazati indukcijom. Neka je pri spajanju $T$ i $T'$ novododani brid $(x,y)$, pri čemu $x\in T,y\in T'$. Bez smanjenja općenitosti neka je (jedan) centroid novog stabla u $T$. Promotrimo postupak u kojem, počevši od stabla $T$, čvorove stabla $T'$ jedan po jedan dodajemo kao listove. Fiksirajmo jedan centroid $c$ stabla $T$. Indukcijom se može dokazati da (jedan) centroid stabla uvijek leži na putu koji spaja $c$ i čvor $x$. Baza indukcije je očita. Pretpostavimo da tvrdnja vrijedi do nekog trenutka i neka je tada centroid $v$. Iz analize svojstva 2 znamo da centroid novog stabla nužno leži na putu između novododanog čvora i trenutačnog centroida $v$, a kako se ne pomiče izvan stabla $T$, dovoljno je promatrati zajednički dio tog puta i stabla $T$, tj. put između trenutačnog centroida $v$ i čvora $x$. Prema pretpostavci indukcije $v$ leži na putu između $c$ i čvora $x$, pa i centroid novog stabla nužno leži na putu između $c$ i čvora $x$. Po indukciji tvrdnja vrijedi.
    
    Svojstvo 4 slijedi kombiniranjem sa [svojstvima heavy-light dekompozicije](./hld.md#svojstva-heavy-light-dekompozicije). Neka je (jedan) centroid stabla $T$ čvor $v$. Ako je $v$ korijen, tvrdnja očito vrijedi. Neka je dalje $v$ nekorijenski čvor, a $u$ njegov roditelj. Budući da je $|T_u^{(v)}| \le |T|/2$, veličina podstabla u kojem je $v$ iznosi barem $|T|/2$. No čim put od njega do korijena prijeđe preko jednog lakog brida, veličina podstabla u kojem se nalazi bit će strogo manja od $|T|/2$, kontradikcija. Stoga on nužno leži na teškom lancu koji sadrži korijen. Nadalje, prema definiciji teškog lanca, teški lanac koji sadrži korijen podstabla koje odgovara teškom djetetu korijena dio je teškog lanca koji sadrži korijen izvornog stabla; a prema svojstvu 3, nakon što podstablu teškog djeteta dodamo korijen i podstabla sve njegove lake djece, položaj centroida pomiče se duž puta između trenutačnog centroida i korijena, pa je novi centroid nužno predak starog centroida (uključujući i njega samog).

## Postupak

Prema ekvivalentnim definicijama centroida postoje dva načina da se u vremenu $O(n)$ odrede svi centroidi stabla, gdje je $n$ veličina stabla.

### DFS s računanjem veličina podstabala

DFS-om izračunamo veličinu svakog podstabla. Za svaki čvor zabilježimo veličine podstabala koja odgovaraju svoj njegovoj djeci, a veličinu podstabla „prema gore” dobijemo oduzimanjem veličine trenutačnog podstabla od ukupnog broja čvorova; zatim prema definiciji pronađemo centroid.

??? example "Primjer implementacije"
    ```cpp
    --8<-- "docs/graph/code/tree-centroid/tree-centroid-2.cpp:core"
    ```

### Rerooting DP s računanjem zbroja dubina

Rerooting DP-om (DP-om s promjenom korijena) možemo za svaki čvor kao korijen izračunati zbroj dubina svih čvorova (tj. zbroj udaljenosti do trenutačnog korijena). Prema definiciji dovoljno je pronaći čvor za koji je taj zbroj dubina najmanji.

??? example "Primjer implementacije"
    ```cpp
    --8<-- "docs/graph/code/tree-centroid/tree-centroid-3.cpp:core"
    ```

## Primjer zadatka

???+ example "[Codeforces Round 359 (Div. 1) B. Kay and Snowflake](https://codeforces.com/problemset/problem/685/B)"
    Zadano je korijensko stablo; odredite centroid svakog podstabla.

??? note "Ideja rješenja"
    Prema svojstvu 4, za podstablo s korijenom $u$ centroid nužno leži na putu od centroida podstabla s korijenom u teškom djetetu čvora $u$ do čvora $u$.
    
    Slično gore opisanoj metodi traženja centroida DFS-om, za svako podstablo s korijenom $u$ najprije odredimo centroid podstabla njegova teškog djeteta (centroid lista je on sam), a zatim od tog centroida idemo prema gore i provjeravamo jesu li čvorovi na putu centroid; ako nijedan čvor na putu nije centroid, onda je centroid sam $u$.
    
    Budući da se centroidi podstabala na istom teškom lancu pomiču samo prema gore duž lanca, ukupan broj provjera prema gore na svakom teškom lancu istog je reda kao duljina lanca, pa se centroidi svih podstabala mogu odrediti u vremenu $O(n)$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/tree-centroid/tree-centroid-1.cpp"
    ```

## Zadaci za vježbu

-   [Gym 101649G Godfather](https://codeforces.com/gym/101649/problem/G)
-   [POJ 1655 Balancing Act](http://poj.org/problem?id=1655)
-   [Luogu P1364 Smještaj bolnice](https://www.luogu.com.cn/problem/P1364)
-   [Codeforces 1406C Link Cut Centroids](https://codeforces.com/contest/1406/problem/C)
-   [Codeforces 708C Centroids](https://codeforces.com/problemset/problem/708/C)

## Literatura

-   [Neka svojstva „centroida” stabla i njegovo dinamičko održavanje – fanhq666](https://web.archive.org/web/20181122041458/http://fanhq666.blog.163.com/blog/static/81943426201172472943638) ([prijenos na cnblogs](https://www.cnblogs.com/qlky/p/5781081.html))
-   [Promjer stabla, centroid stabla i centroid decomposition – cyendra](https://www.cnblogs.com/zinthos/p/3899075.html)
-   [Svojstva centroida stabla i njihovi dokazi – suxxsfe](https://www.cnblogs.com/suxxsfe/p/13543253.html)
-   „Rječnik informatičke olimpijade” (信息学奥林匹克辞典), odjeljak 2.4.7.11, 1. Centroid stabla
