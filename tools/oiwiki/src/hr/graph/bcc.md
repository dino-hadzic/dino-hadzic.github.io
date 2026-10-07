---
title: Dvostruko povezane komponente
---

## Uvod

Prije čitanja obvezno se upoznajte s [osnovnim pojmovima teorije grafova](./concept.md).

Srodno štivo: [Artikulacijski vrhovi i mostovi](./cut.md)

## Definicija

Strože definicije artikulacijskih vrhova i mostova vidi u [Osnovni pojmovi teorije grafova](./concept.md).

U povezanom neusmjerenom grafu, za dva vrha $u$ i $v$, ako ih brisanje bilo kojeg brida (smije se obrisati samo jedan) ne može učiniti nepovezanima, kažemo da su $u$ i $v$ **bridno dvostruko povezani** (edge-biconnected).

U povezanom neusmjerenom grafu, za dva vrha $u$ i $v$, ako ih brisanje bilo kojeg vrha (smije se obrisati samo jedan, i to ne sami $u$ ili $v$) ne može učiniti nepovezanima, kažemo da su $u$ i $v$ **vršno dvostruko povezani** (vertex-biconnected).

Bridna dvostruka povezanost je tranzitivna: ako su $x,y$ bridno dvostruko povezani i $y,z$ bridno dvostruko povezani, onda su i $x,z$ bridno dvostruko povezani.

Vršna dvostruka povezanost **nije** tranzitivna; protuprimjer je na slici dolje: $A,B$ su vršno dvostruko povezani, $B,C$ su vršno dvostruko povezani, a $A,C$ **nisu** vršno dvostruko povezani.

![bcc-counterexample.png](./images/bcc-0.svg)

**Maksimalni** bridno dvostruko povezani podgraf neusmjerenog grafa zovemo **bridno dvostruko povezana komponenta** (edge-biconnected component, e-BCC).

**Maksimalni** vršno dvostruko povezani podgraf neusmjerenog grafa zovemo **vršno dvostruko povezana komponenta** (vertex-biconnected component, v-BCC).

## DFS razapinjuće stablo

Za povezan neusmjeren graf možemo iz proizvoljnog vrha pokrenuti DFS i dobiti DFS razapinjuće stablo izvornog grafa (s korijenom u vrhu iz kojeg smo krenuli). Bridovi tog razapinjućeg stabla zovu se **stablasti bridovi**, a bridovi koji nisu u njemu **nestablasti bridovi**.

Zbog svojstava DFS-a možemo jamčiti da je za svaki nestablasti brid jedan od njegovih krajeva predak drugoga u razapinjućem stablu.

Kôd DFS-a:

???+ note "Implementacija"
    === "C++"
        ```cpp
        void DFS(int p) {
          visited[p] = true;
          for (int to : edge[p])
            if (!visited[to]) DFS(to);
        }
        ```
    
    === "Python"
        ```python
        def DFS(p):
            visited[p] = True
            for to in edge[p]:
                if visited[to] == False:
                    DFS(to)
        ```

## Bridno dvostruko povezane komponente

???+ note "[Primjer: Luogu P8436 \[Predložak\] Bridno dvostruko povezane komponente](https://www.luogu.com.cn/problem/P8436)"
    Za graf s $n$ vrhova i $m$ neusmjerenih bridova ispiši broj bridno dvostruko povezanih komponenata i svaku od njih.

### Tarjanov algoritam 1

Traženje dvostruko povezanih komponenata Tarjanovim algoritmom slično je traženju jako povezanih komponenata; prvo pročitajte Tarjanov algoritam u [Jako povezane komponente](./scc.md).

Ideja: prvo nađemo sve mostove, a zatim DFS-om nađemo bridno dvostruko povezane komponente.

Traženje mostova vidi u dijelu o mostovima u [Artikulacijski vrhovi i mostovi](./cut.md).

Vremenska složenost $O(n+m)$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_1.cpp"
    ```

### Tarjanov algoritam 2

Prvo sažmimo važno svojstvo: u neusmjerenom grafu brid u odnosu na DFS razapinjuće stablo može biti samo stablasti ili nestablasti.

Povežimo to s metodom za jako povezane komponente: u neusmjerenom grafu, čim komponenta nema mostova, svi su njezini vrhovi u DFS razapinjućem stablu u istoj jako povezanoj komponenti.

Obratno, jako povezana komponenta u DFS razapinjućem stablu u izvornom je neusmjerenom grafu bridno dvostruko povezana komponenta.

Vidimo da je postupak traženja bridno dvostruko povezanih komponenata zapravo postupak traženja jako povezanih komponenata.

Vremenska složenost $O(n+m)$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_2.cpp"
    ```

### Algoritam s diferencijama

Slično Tarjanovu algoritmu 1, prvo nađemo sve mostove, a zatim diferencijama (difference array) nađemo bridno dvostruko povezane komponente.

Prvo napravimo DFS izvornog grafa.

![bcc-1.png](./images/bcc-1.svg)

Na slici su crni i zeleni bridovi stablasti, a crveni su nestablasti. Dvama krajevima svakog nestablastog brida jednoznačno odgovara jednostavan put u stablu sastavljen od stablastih bridova; kažemo da taj nestablasti brid **pokriva** sve bridove tog jednostavnog puta.

Na slici je svaki zeleni stablasti brid pokriven **barem** jednim nestablastim bridom, a crni stablasti bridovi nisu pokriveni **nijednim** nestablastim bridom.

Očito **nestablasti bridovi** i **zeleni stablasti bridovi** sigurno nisu mostovi, a **crni stablasti bridovi** sigurno jesu.

Razmotrimo prvo grubi pristup: za svaki nestablasti brid jedan po jedan obojimo zeleno sve stablaste bridove koje pokriva; vremenska složenost je $O(nm)$.

Optimirajmo diferencijama. Za svaki nestablasti brid na njegovu kraju manje dubine u stablu zapišemo oznaku `-1`, a na kraju veće dubine oznaku `+1`, zatim u $O(n)$ izračunamo zbroj oznaka u podstablu svakog vrha.

Za vrh $u$ zbroj oznaka u njegovu podstablu jednak je broju nestablastih bridova koji pokrivaju stablasti brid između $u$ i $fa_u$. Ako je taj zbroj $0$, stablasti brid između $u$ i $fa_u$ je **most**.

Zatim DFS-om nađemo bridno dvostruko povezane komponente.

Vremenska složenost $O(n+m)$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_4.cpp"
    ```

???+ note "[#2788. „CEOI2015 Day1” Cjevovodi](https://loj.ac/p/2788)"
    Zadan je neusmjeren graf s $N$ vrhova i $M$ bridova koji ne mora biti povezan. Svaku povezanu komponentu promatraj kao podgraf i nađi mostove u svakom podgrafu. **Na raspolaganju imaš samo 16 MB memorije.**

??? note "Rješenje"
    Glavna je osobitost zadatka da ne možeš spremiti sve bridove.
    
    Optimirajmo spremanje bridova: ako je nestablasti brid potpuno pokriven drugim nestablastim bridom, on je beskoristan.
    
    Dovoljno je to održavati DSU-om.

## Vršno dvostruko povezane komponente

???+ note "[Primjer: Luogu P8435 \[Predložak\] Vršno dvostruko povezane komponente](https://www.luogu.com.cn/problem/P8435)"
    Za graf s $n$ vrhova i $m$ neusmjerenih bridova ispiši broj vršno dvostruko povezanih komponenata i svaku od njih.

### Tarjanov algoritam

Prvo treba naučiti artikulacijske vrhove; vidi dio o artikulacijskim vrhovima u [Artikulacijski vrhovi i mostovi](./cut.md).

Prvo dva svojstva:

1.  Dvije vršno dvostruko povezane komponente imaju najviše jedan zajednički vrh, i on je nužno artikulacijski vrh.
2.  Za vršno dvostruko povezanu komponentu, njezin vrh s najmanjom vrijednošću dfn u DFS stablu nužno je artikulacijski vrh ili korijen stabla.

Prema drugom svojstvu razlikujemo slučajeve:

1.  Ako je taj vrh artikulacijski, on je nužno korijen vršno dvostruko povezane komponente, jer bi, čim bi komponenta sadržavala njegova roditelja, on i dalje bio artikulacijski.
2.  Ako je taj vrh korijen stabla:
    1.  ima dva ili više podstabla: on je artikulacijski vrh;
    2.  ima samo jedno podstablo: on je korijen vršno dvostruko povezane komponente;
    3.  nema podstabala: smatra se zasebnom vršno dvostruko povezanom komponentom.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_3.cpp"
    ```

### Algoritam s diferencijama

![bcc-2.png](./images/bcc-2.svg)

Na slici su crni bridovi stablasti, a crveni nestablasti; dvama krajevima svakog nestablastog brida jednoznačno odgovara jednostavan put u stablu sastavljen od stablastih bridova.

Promotrimo novi graf u kojem svaki vrh odgovara jednom stablastom bridu izvornog grafa (na slici plavi vrhovi). Za svaki nestablasti brid izvornog grafa plave vrhove koji odgovaraju bridovima jednostavnog puta u stablu pripadnog tom nestablastom bridu spojimo u jednu povezanu komponentu (na slici prikazano plavim bridovima).

Tada vrh **nije** artikulacijski ako i samo ako plavi vrhovi koji u novom grafu odgovaraju svim bridovima incidentnima s njim **pripadaju** istoj povezanoj komponenti.

Dva vrha **jesu** vršno dvostruko povezana ako i samo ako plavi vrhovi koji odgovaraju svim bridovima na njihovu putu u stablu izvornog grafa **pripadaju** istoj povezanoj komponenti; drugim riječima, svaka povezana komponenta plavih vrhova na slici jedna je vršno dvostruko povezana komponenta.

Povezanost plavih vrhova može se održavati metodom sličnom diferencijama kod bridno dvostruko povezanih komponenata; vremenska složenost $O(n+m)$.
