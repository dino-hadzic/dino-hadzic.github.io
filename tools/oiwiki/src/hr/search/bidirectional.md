---
title: Dvosmjerno pretraživanje
---

Ova stranica kratko predstavlja dva algoritma dvosmjernog pretraživanja: „istodobno dvosmjerno pretraživanje” i „meet in the middle”.

## Istodobno dvosmjerno pretraživanje

### Definicija

Osnovna je ideja istodobnog dvosmjernog pretraživanja da se [BFS](./bfs.md) ili [DFS](./dfs.md) pokrene istodobno iz početnog i iz ciljnog stanja u grafu stanja.

Ako se dva kraja pretrage sretnu, možemo smatrati da smo pronašli dopustivo rješenje.

### Postupak

Koraci dvosmjernog BFS-a:

```text
stavi početni i ciljni vrh u red q
označi početni vrh s 1
označi ciljni vrh s 2
while (red q nije prazan)
{
  iz q.front() proširi s novih vrhova
  
  ako je novoprošireni vrh već označen drugim brojem
    onda su se dva kraja pretrage sudarila
    onda petlja završava
  
  ako je s novih vrhova prošireno iz početnog vrha
    onda tih s vrhova označi s 1 i stavi ih u red q 
  
  ako je s novih vrhova prošireno iz ciljnog vrha
    onda tih s vrhova označi s 2 i stavi ih u red q
}
```

### Riješeni primjer

???+ note "Primjer [Slagalica s osam pločica](https://www.luogu.com.cn/problem/P1379)"
    Na ploči $3\times 3$ nalazi se osam pločica, a na svakoj je jedan od brojeva od $1$ do $8$. Na ploči je jedno prazno polje, označeno s $0$. Pločica susjedna praznom polju može se pomaknuti na njega. Zadatak je: za zadani početni raspored (početno stanje) i ciljni raspored (radi jednostavnosti neka je ciljno stanje $123804765$) pronaći niz poteza s najmanjim brojem koraka koji početni raspored pretvara u ciljni.

??? note "Ideja rješenja"
    Lako se dosjetiti grubog BFS-a, a u ovom zadatku ni on ne prekoračuje vremensko ograničenje. Ovdje ga ipak uzimamo kao primjer istodobnog dvosmjernog pretraživanja. Možemo pokrenuti dva BFS-a, jedan unaprijed iz početnog stanja i jedan unatrag iz ciljnog stanja, i naizmjence ih izvoditi; veličina stabla pretrage znatno se smanjuje. Kad jedan BFS dođe do stanja koje je drugi BFS već pronašao, dobili smo odgovor.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/bidirectional/bidirectional_1.cpp"
    ```

## Meet in the middle

???+ warning "Upozorenje"
    U ovom odjeljku nije riječ o [**binarnom pretraživanju**](../basic/binary.md) (na kineskom se binarno pretraživanje ponekad također naziva „pretraživanje raspolavljanjem”).

### Uvod

Algoritam meet in the middle nema ustaljen kineski naziv; uobičajeni su prijevodi „pretraživanje raspolavljanjem”, „dvosmjerno pretraživanje” ili „susret na pola puta”.

Prikladan je kad su ulazni podaci mali, ali ne toliko mali da bi se izravno moglo primijeniti grubo pretraživanje.

### Postupak

Glavna je ideja algoritma meet in the middle da se cijela pretraga podijeli na dvije polovice, svaka se pretraži zasebno, a na kraju se rezultati obiju polovica spoje.

### Svojstva

Složenost grubog pretraživanja često je eksponencijalna, a prelaskom na meet in the middle eksponent se može prepoloviti, tj. složenost pada s $O(a^b)$ na $O(a^{b/2})$.

### Riješeni primjer

???+ note "Primjer [„USACO09NOV” Svjetla (Lights)](https://www.luogu.com.cn/problem/P2962)"
    Zadano je $n$ svjetala; svako je povezano s nekoliko drugih svjetala i svako ima prekidač. Pritisak na prekidač nekog svjetla mijenja stanje tog svjetla i svih svjetala povezanih s njim. Na početku su sva svjetla ugašena, a treba ih sva upaliti. Odredite najmanji broj pritisaka na prekidače.
    
    $1\le n\le 35$.

??? note "Ideja rješenja"
    Ako bismo stanja paljenja i gašenja tražili grubim DFS-om, vremenska bi složenost bila $O(2^{n})$, što očito prekoračuje ograničenje. No s meet in the middle složenost se može spustiti na $O(n2^{n/2})$. Meet in the middle znači da najprije pretražimo polovicu stanja, tj. nađemo stanja dostiživa samo prekidačima s brojevima od $1$ do $\mathrm{mid}$, a zatim stanja dostiživa samo drugom polovicom prekidača. Ako su upaljena svjetla iz prve i druge polovice komplementarna, spajanjem tih dviju polovica dobivamo način da se upale sva svjetla. U implementaciji se stanja prve polovice i najmanji broj pritisaka za svako od njih spreme u `map`; pri pretrazi druge polovice za svaki pronađeni način spajamo ga s komplementarnim načinom iz prve polovice i ažuriramo odgovor.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/bidirectional/bidirectional_2.cpp"
    ```

## Vanjske poveznice

-   [What is meet in the middle algorithm w.r.t. competitive programming? - Quora](https://www.quora.com/What-is-meet-in-the-middle-algorithm-w-r-t-competitive-programming)
-   [Meet in the Middle Algorithm - YouTube](https://www.youtube.com/watch?v=57SUNQL4JFA)
