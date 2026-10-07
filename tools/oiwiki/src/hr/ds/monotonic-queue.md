---
title: Monotoni red
---

## Uvod

Prije nego što naučimo monotoni red (monotonic queue), pogledajmo jedan primjer zadatka.

???+ note "Primjer zadatka"
    [Sliding Window](http://poj.org/problem?id=2823)
    
    Zadatak u osnovi glasi: zadan je niz duljine $n$; za svakih $k$ uzastopnih brojeva ispišite njihov maksimum i minimum.

Najgrublja je ideja jednostavna: za svaki odsječak niza $i \sim i+k-1$ usporedbama element po element pronađemo maksimum (i minimum); vremenska je složenost otprilike $O(n \times k)$.

Očito se pritom obavlja mnogo suvišnog posla: osim prvih $k-1$ i zadnjih $k-1$ brojeva, svaki se broj uspoređuje $k$ puta, a $100\%$ testnih podataka u zadatku ima $n \le 1000000$, pa već za nešto veći $k$ očito dobivamo TLE.

Tu u igru ulazi monotoni red.

## Definicija

Kako mu i ime kaže, bit monotonog reda dijeli se na „monoton” i „red”.

„Monoton” se odnosi na „pravilnost” elemenata – rastući su (ili padajući).

„Red” znači da se elementi mogu obrađivati samo na čelu i na začelju reda.

P. S. „Red” u monotonom redu donekle se razlikuje od običnog reda; o tome kasnije.

## Analiza primjera

### Objašnjenje

Uz gornji pojam „monotonog reda” lako se dosjetiti optimizacije monotonim redom.

Tražimo maksimum (minimum) svakih $k$ uzastopnih brojeva; očito, kad neki broj uđe u raspon u kojem „tražimo” maksimum, ako je veći od brojeva ispred sebe (onih koji su ušli u red prije njega), onda će ti prethodni brojevi očito izaći iz reda prije njega i više nikad ne mogu biti maksimum.

Drugim riječima – kad je gornji uvjet ispunjen, prethodne brojeve možemo „izbaciti”, a zatim ovaj broj zaista dodati (push) na začelje reda.

To je kao da održavamo padajući red, što odgovara definiciji monotonog reda i smanjuje broj suvišnih usporedbi. Štoviše, budući da je održavani red unutar raspona upita i padajući, čelo reda sigurno je maksimum tog raspona, pa pri ispisu treba samo ispisati čelo reda.

Očito je da u ovakvom algoritmu svaki broj ulazi u red i izlazi iz njega najviše jednom, pa je vremenska složenost smanjena na $O(n)$.

A budući da je duljina intervala upita fiksna, vrijednost izvan prostora upita ne smije se ispisati ma koliko velika bila; zato nam treba i niz site koji pamti položaj $i$-tog elementa reda u izvornom nizu, kako bismo izbacili čelo koje je izašlo iz granica.

### Postupak

Primjerice, konstrukcija monotono rastućeg reda izgleda ovako:

Izvorni niz je:

```text
1 3 -1 -3 5 3 6 7
```

Budući da red stalno održavamo tako da ostane **rastući**, događa se sljedeće (pretpostavimo $k = 3$):

| Operacija                                                                        | Stanje reda |
| -------------------------------------------------------------------------------- | ----------- |
| 1 ulazi u red                                                                    | `{1}`       |
| 3 je veći od 1, 3 ulazi u red                                                    | `{1 3}`     |
| -1 je manji od svih elemenata u redu, pa ispraznimo red i -1 ulazi u red         | `{-1}`      |
| -3 je manji od svih elemenata u redu, pa ispraznimo red i -3 ulazi u red         | `{-3}`      |
| 5 je veći od -3, izravno ulazi u red                                             | `{-3 5}`    |
| 3 je manji od 5, 5 izlazi iz reda, 3 ulazi u red                                 | `{-3 3}`    |
| -3 je već izvan prozora, pa -3 izlazi iz reda; 6 je veći od 3, 6 ulazi u red     | `{3 6}`     |
| 7 je veći od 6, 7 ulazi u red                                                    | `{3 6 7}`   |

???+ note "Referentni kôd za primjer"
    ```cpp
    --8<-- "docs/ds/code/monotonic-queue/monotonic-queue_1.cpp"
    ```

P. S. Velika razlika između ovog „reda” i običnog reda jest to što se operacije mogu izvoditi i na začelju; u STL-u postoji slična struktura podataka, deque.

???+ note "Primjer 2 [Luogu P2698 Flowerpot S](https://www.luogu.com.cn/problem/P2698)"
    Zadane su koordinate $N$ kapi vode; $y$ je visina kapi, a $x$ mjesto na kojem pada na os $x$. Svaka kap pada brzinom od 1 jedinice duljine u sekundi. Posudu za cvijeće treba postaviti na neko mjesto na osi $x$ tako da vremenska razlika između prve kapi koju posuda uhvati i posljednje kapi koju uhvati bude barem $D$.
    Smatramo da je kap uhvaćena čim padne na os $x$ poravnata s rubom posude. Za zadane koordinate $N$ kapi i vrijednost $D$ izračunajte najmanju širinu posude $W$. $1\leq N \leq 100000 , 1 \leq D \leq 1000000, 0 \leq x,y\leq 10^6$

Nakon što sve kapi sortiramo po koordinati $x$, zadatak se svodi na pronalaženje intervala s najmanjom razlikom koordinata $x$ u kojem je razlika maksimuma i minimuma koordinata $y$ barem $D$. Vidimo da ovaj zadatak ima sličnosti s prethodnim primjerom – oba se tiču maksimuma i minimuma unutar intervala – ali ovdje veličina intervala nije fiksna, štoviše, upravo je veličina intervala traženi odgovor.

I dalje možemo pomoću dva monotona reda, jednog rastućeg i jednog padajućeg, održavati maksimum i minimum na $[L,R]$ dok se $R$ pomiče udesno; no primjećujemo da, ako je $L$ fiksan, maksimum na $[L,R]$ može samo rasti, a minimum samo padati, pa ako stavimo $f(R) = \max[L,R]-\min[L,R]$, onda je $f(R)$ rastuća funkcija od $R$, dakle $f(R)\geq D \implies f(r)\geq D,R\lt r \leq N$. To znači da je za svaki fiksni $L$ prvi $R$ udesno koji zadovoljava uvjet ujedno i optimalan odgovor.
Cijeli postupak rješavanja stoga glasi: fiksiramo $L$, pomičemo $R$ sprijeda prema natrag i s dva monotona reda održavamo ekstreme na $[L,R]$. Kad nađemo prvi $R$ koji zadovoljava uvjet, ažuriramo odgovor i pomaknemo i $L$ unatrag. Kako se $L$ pomiče, iz oba monotona reda treba pravodobno izbacivati čelo. Tako, dok $R$ ne dođe do kraja, svaki element i dalje ulazi u red i izlazi iz njega po jednom, čime je zajamčena vremenska složenost $O(n)$.

???+ note "Referentni kôd"
    ```cpp
    --8<-- "docs/ds/code/monotonic-queue/monotonic-queue_2.cpp"
    ```
