---
title: BFS (pretraživanje)
---

## Uvod

BFS (breadth-first search, pretraživanje u širinu) osnovni je algoritam teorije grafova, vidi stranicu [BFS (teorija grafova)](../graph/bfs.md). U **algoritmima pretraživanja** taj naziv obično označava pretraživanje koje pomoću reda (queue) širi stanja razinu po razinu; ideja je ista kao kod BFS-a iz teorije grafova i osobito je prikladna za zadatke s **najkraćim putem** ili **najmanjim brojem koraka**.

## Objašnjenje

Temeljna ideja BFS-a je **širenje po razinama**: od početka se razinu po razinu pregledavaju dostupna mjesta. Duljina puta pri prvom susretu s ciljem upravo je duljina najkraćeg puta. Time su zajamčene slojevitost i optimalnost pretraživanja.

U izvođenju BFS kreće od početnog vrha i najprije posjećuje sve vrhove izravno dostupne iz početka; oni čine prvu razinu pretrage. Zatim se ti vrhovi uzimaju kao nova polazišta i redom se posjećuju njihovi susjedi, koji čine drugu razinu; i tako dalje, pretraga se širi prema van dok se ne pronađe ciljni vrh ili dok se ne obiđu svi dostupni vrhovi. Pritom se algoritam služi redom i nizom posjećenosti: novootkrivene vrhove svake razine (one koji još nisu zabilježeni u nizu posjećenosti) redom stavlja u red, čime osigurava da se vrhovi iste razine obrađuju redoslijedom posjeta, strogo slijedeći logiku „širenja po razinama”.

BFS je vrlo pogodan za brzo nalaženje **najkraćeg puta** ili **najmanjeg broja koraka**. Kad algoritam na nekoj razini prvi put naiđe na cilj, prijeđeni put (broj koraka) nužno je najkraći. Razlog je to što mehanizam „širenja po razinama” jamči da se svaki vrh posjećuje s najmanjim brojem koraka: kao da od početka tražimo duž najizravnijeg puta dok ne stignemo do cilja, bez zaobilaženja i suvišnih koraka. U takvim je zadacima BFS obično i učinkovitiji od DFS-a.

No u usporedbi s DFS-om BFS ima i nedostatke. Obično treba više memorije, nema prirodnog vraćanja (backtracking), a rezanje po dubini manje je fleksibilno nego kod DFS-a.

## Riješeni primjer

???+ example "Primjer [Luogu B3625 Put kroz labirint](https://www.luogu.com.cn/problem/B3625)"
    U matrici labirinta dimenzija $n \times m$ znak `.` označava prohodno polje, a `#` prepreku. Krećemo iz polja $(1,1)$ i u svakom se koraku možemo pomaknuti gore, dolje, lijevo ili desno. Može li se stići do cilja $(n,m)$?

??? note "Rješenje"
    U implementaciji održavamo red s koordinatama koje čekaju obradu, uz niz oznaka posjećenosti koji sprječava ponovno računanje. Kad iz nekog vrha širimo dostupne vrhove, širimo gore, dolje, lijevo i desno: u ta četiri smjera to su $(x, y + 1)$, $(x, y - 1)$, $(x + 1, y)$ i $(x - 1, y)$; u kodu se koriste nizovi smjerova. Pazite da se ne smije proširiti na polje s preprekom.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/bfs/bfs-1.cpp"
    ```

???+ example "Primjer [Luogu P1135 Čudno dizalo](https://www.luogu.com.cn/problem/P1135)"
    Zgrada ima $n$ katova i jedno dizalo. Kad je dizalo na $i$-tom katu, pomiče se gore ili dolje za točno $k_i$ katova. Ako odredišni kat nije dopušten, tj. nije između $1$ i $n$, taj se potez ne može izvesti. Pitanje: koliko najmanje puta treba pokrenuti dizalo da bi se s kata $a$ stiglo na kat $b$? Ako je to nemoguće, ispišite $-1$.

??? note "Rješenje"
    Zadatak traži najkraći put, a upravo u tome je BFS dobar. U implementaciji u redu zajedno s katom koji čeka obradu čuvamo i najkraću udaljenost od početnog kata $a$ do njega, uz niz oznaka posjećenosti koji sprječava da isti element uđemo više puta. Kad iz vrha $i$ širimo dostupne vrhove, širimo na $i + k_i$ i $i - k_i$, pazeći da ne odemo na nedopušten kat. Kad proširimo na dopušten kat koji još nismo dosegnuli, stavljamo ga u red i bilježimo da je najkraća udaljenost do njega za jedan veća od najkraće udaljenosti do trenutnog kata. Kad prvi put stignemo do vrha $b$, zabilježena najkraća udaljenost je konačan odgovor.
    
    U kodu se izravno čuva niz udaljenosti, a je li vrh već posjećen provjerava se po tome je li udaljenost još na početnoj vrijednosti (tj. $-1$).

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/bfs/bfs-2.cpp"
    ```

## Zadaci za vježbu

-   [Luogu P1443 Obilazak konja](https://www.luogu.com.cn/problem/P1443)
-   [Luogu P3956 \[NOIP 2017 Popularizacijska razina\] Šahovska ploča](https://www.luogu.com.cn/problem/P3956)
-   [Luogu P1126 Robot nosi teret](https://www.luogu.com.cn/problem/P1126)
