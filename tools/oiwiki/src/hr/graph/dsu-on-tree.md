---
title: DSU on tree (heurističko spajanje na stablu)
---

## Uvod

Što je heuristički algoritam?

Heuristički algoritam je optimizacija nekog algoritma temeljena na ljudskom iskustvu i intuiciji.

Primjerice, najčešći je primjer heurističko spajanje u union-find strukturi; kôd izgleda ovako:

```cpp
void merge(int x, int y) {
  int xx = find(x), yy = find(y);
  if (size[xx] < size[yy]) swap(xx, yy);
  fa[yy] = xx;
  size[xx] += size[yy];
}
```

Ovdje za dva skupa različite veličine manji skup spajamo u veći, a ne veći u manji.

Zašto? Veličinu skupa možemo (u normalnim okolnostima) smatrati visinom skupa, a spajanje skupa manje visine u skup veće visine očito pomaže pri traženju roditelja.

Da stablo manje visine postane podstablo stabla veće visine – ta se optimizacija može nazvati algoritmom heurističkog spajanja.

## Sadržaj algoritma

Heurističko spajanje na stablu (dsu on tree) algoritam je koji za neke offline probleme na stablima može biti brži ili jednako brz kao većina algoritama, a lakši je za razumijevanje i implementaciju.

Razmotrimo sljedeći zadatak: [Brojanje boja na stablu](https://www.luogu.com.cn/problem/U41492).

???+ note "Uvodni zadatak"
    Zadano je stablo s $n$ čvorova i korijenom $1$; boja čvora $u$ je $c_u$. Za svaki čvor $u$ treba odgovoriti koliko se različitih boja pojavljuje u podstablu s korijenom $u$.
    
    $n\le 2\times 10^5$.

![dsu-on-tree-1.png](./images/dsu-on-tree-1.svg)

Takvi se zadaci uglavnom rješavaju mnoštvom struktura podataka (ugniježđene strukture i sl.); ako je dopušten offline pristup, postoji li jednostavniji način?

## Postupak

Budući da je dopušten offline pristup, razmotrimo predobradu nakon koje odgovore ispisujemo u $O(1)$.

Izravna gruba predobrada ima složenost $O(n^2)$: za svaki čvor napravimo jedan obilazak, svaki je obilazak očito reda $n$, a čvorova ima $n$, pa je složenost $O(n^2)$.

Uočavamo da se odgovor za svaki čvor dobiva iz njegova podstabla i njega samog; iskoristimo to svojstvo.

Najprije možemo predobradom izračunati veličinu podstabla svakog čvora i njegovo teško dijete; teško dijete je, kao i kod heavy-light dekompozicije, dijete s najvećim podstablom, a to se očito može napraviti u $O(n)$.

Neka $cnt_i$ označava broj pojavljivanja boje $i$, a $ans_u$ odgovor za čvor $u$.

Čvor $u$ obrađujemo sljedećim koracima:

1.  Najprije obiđemo laku (ne-tešku) djecu čvora $u$ i izračunamo njihove odgovore, ali **ne zadržavamo njihov utjecaj na polje $cnt$**;
2.  Obiđemo teško dijete i **zadržimo njegov utjecaj na polje $cnt$**;
3.  Ponovno obiđemo čvorove podstabala lake djece čvora $u$ i dodamo njihove doprinose kako bismo dobili odgovor za $u$.

![dsu-on-tree-2.png](./images/dsu-on-tree-2.svg)

Gornja slika prikazuje primjer.

Tako za jedan čvor jednom obilazimo teško podstablo, a dvaput laka podstabla, što je očito najisplativije.

Provođenjem tog postupka dobivamo odgovore za sva podstabla tog čvora.

Zašto ne spojimo prvi i treći korak? Zato što se polje $cnt$ ne može umnožavati; inače bi memorija bila prevelika, a trebamo ostati u prostoru $O(n)$.

Očito, ako se čvor $u$ obilazi $x$ puta, njegovo se teško dijete obilazi $x$ puta, a laka djeca (ako ih ima) $2x$ puta.

Pazite da se $cnt$ nakon svakog obilaska, osim za teško dijete, mora poništiti.

## Dokaz

Kao kod heavy-light dekompozicije definiramo teške i lake bridove (brid prema teškom djetetu je težak, ostali su laki). Definicije teškog djeteta i teškog brida vidljive su na slici u nastavku; za stablo s $n$ čvorova:

Broj lakih bridova od korijena do bilo kojeg čvora stabla ne premašuje $\log n$. Neka od korijena do tog čvora ima $x$ lakih bridova, a veličina podstabla tog čvora je $y$. Očito je veličina podstabla djeteta na kraju lakog brida manja od polovine roditeljeve (inače brid ne bi bio lak), pa je $y<n/2^x$, dakle očito $n>2^x$, pa $x<\log n$.

Nadalje, ako je čvor teško dijete svog roditelja, njegovo je podstablo najveće među braćom, pa svi roditelji na teškim bridovima duž puta od tog čvora do korijena pri računanju odgovora neće obilaziti taj čvor. Stoga je broj obilazaka čvora jednak broju lakih bridova na putu od njega do korijena $+1$ (ono $+1$ jer se i sam mora obići). Dakle, čvor se obilazi $=\log n+1$ puta, pa je ukupna vremenska složenost $O(n(\log n+1))=O(n\log n)$, a ispis odgovora košta $O(m)$.

![dsu-on-tree-3.png](./images/dsu-on-tree-3.svg)

*Podebljani bridovi na slici su teški bridovi, a djeca na koja pokazuju teški bridovi su teška djeca*

## Optimizacija

U dokazu je spomenuto da dsu on tree ubrzava spajanje koristeći pojmove lakog i teškog djeteta iz heavy-light dekompozicije. Kad je već tako, možemo izravno iskoristiti dfs poredak dobiven heavy-light dekompozicijom, pretvoriti rekurziju u iteraciju i dodatno smanjiti konstantu dsu on tree.

Sam dfs poredak ima sljedeće svojstvo: podstablo čvora u dfs poretku je uvijek neprekinuto. Stoga polje dfs poretka možemo obilaziti unatrag. Tako je zajamčeno da su, kad dođemo do nekog čvora, svi ostali čvorovi njegova podstabla već obrađeni.

Dfs poredak dobiven heavy-light dekompozicijom ima i sljedeće lijepo svojstvo: teški lanac u dfs poretku je uvijek neprekinut. Stoga, kad čvorove obilazimo unatrag po dfs poretku, za čvor na vrhu teškog lanca sljedeći čvor koji obilazimo sigurno nije njegov roditelj, pa njegov utjecaj treba poništiti; inače, za čvor koji nije na vrhu teškog lanca, prethodno obiđeni čvor je ili njegovo teško dijete ili čvor druge grane čiji je utjecaj već poništen, pa njegov utjecaj možemo izravno naslijediti. Na toj osnovi dfs poretkom brzo zbrojimo utjecaj sve lake djece i zabilježimo odgovor.

Gornji postupak zove se nerekurzivna/iterativna implementacija dsu on tree (ili implementacija dsu on tree dfs poretkom). U odnosu na izvornu rekurzivnu implementaciju smanjuje vremenski i prostorni trošak rekurzivnih poziva i donosi nezanemarivo smanjenje konstante, **a osobito pri obradi stabala s mnogo lančastih dijelova ima znatnu prednost u potrošnji stoga.**

## Implementacija

??? example "Primjer implementacije"
    === "Rekurzivna implementacija"
        ```cpp
        --8<-- "docs/graph/code/dsu-on-tree/dsu-on-tree_1.cpp"
        ```
    
    === "Nerekurzivna implementacija"
        ```cpp
        --8<-- "docs/graph/code/dsu-on-tree/dsu-on-tree_2.cpp"
        ```

## Primjene

1.  Zadaci u kojima je autorovo službeno rješenje dsu on tree

    Npr. [CF741D](http://codeforces.com/problemset/problem/741/D). Zadano je stablo u kojem je vrijednost svakog čvora slovo od 'a' do 'v'; u svakom upitu treba u nekom podstablu naći put takav da se znakovi na njemu nakon preslagivanja mogu složiti u palindrom.

    Budući da palindrom nastaje preslagivanjem, znak koji se pojavi dvaput kao da se nije pojavio; drugim riječima, na tom putu **najviše jedan znak smije imati neparan broj pojavljivanja**.

    Uobičajeni pristup je dfs iz svakog čvora, pri čemu u svakom čvoru nasilno prolazimo sva slova i tražimo puteve kod kojih xor s trenutačnom vrijednošću ima više od 1 jedinice, pa uzimamo najdulji; to je $O(n^2\log n)$, a s dsu on tree može se optimizirati na $O(n\log^2n)$. Za konkretan postupak vidi dodatnu literaturu u nastavku.

2.  Zadaci koje se može „na silu” riješiti dsu-om

    Mogu se pokupiti parcijalni bodovi nekih zadataka s ugniježđenim strukturama (bez operacija izmjene), a složenost dsu-a bolja je od $O(n\sqrt{m})$ Mo-ova algoritma na stablu.

## Zadaci za vježbu

[CF600E Lomsat gelral](http://codeforces.com/problemset/problem/600/E)

Sažetak zadatka: čvorovi stabla imaju boje; boja dominira podstablom ako i samo ako se nijedna druga boja u tom podstablu ne pojavljuje češće od nje. Za svako podstablo odredite zbroj svih boja koje njime dominiraju.

[UOJ284 Sretna igrajuća kokoš](https://uoj.ac/problem/284)

[CF1709E XOR Tree](https://codeforces.com/contest/1709/problem/E)

## Literatura / dodatno čitanje

[dsu on tree kako ga predstavlja autor CF741D](http://codeforces.com/blog/entry/44351)

[Rješenje istog autora](http://codeforces.com/blog/entry/48871)
