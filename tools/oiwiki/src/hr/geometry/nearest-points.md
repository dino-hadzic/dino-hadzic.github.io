---
title: Najbliži par točaka u ravnini
---

## Uvod

Zadano je $n$ točaka u ravnini; treba pronaći par točaka s najmanjom euklidskom udaljenošću.

U nastavku predstavljamo algoritam podijeli pa vladaj (divide and conquer) vremenske složenosti $O(n\log n)$ koji rješava taj problem. Algoritam je 1975. godine predložio [Franco P. Preparata](https://en.wikipedia.org/wiki/Franco_P._Preparata), a Preparata i [Michael Ian Shamos](https://en.wikipedia.org/wiki/Michael_Ian_Shamos) dokazali su da je algoritam optimalan u modelu stabla odlučivanja.

## Postupak

Kao i kod uobičajenih algoritama podijeli pa vladaj, skup od $n$ točaka dijelimo na dva jednako velika skupa $S_1, S_2$ i rekurzivno nastavljamo. No nailazimo na poteškoću: kako spojiti rezultate? Odnosno, kako pronaći najbliži par točaka u kojem je jedna točka u $S_1$, a druga u $S_2$? Pretpostavimo zasad da operacija spajanja ima vremensku složenost $O(n)$; tada je ukupna složenost algoritma $T(n) = 2T(\frac{n}{2}) + O(n) = O(n\log n)$.

Najprije sve točke sortiramo tako da je $x_i$ prvi ključ, a $y_i$ drugi ključ, te s točkom $p_m (m = \lfloor \frac{n}{2} \rfloor)$ kao granicom skup točaka dijelimo na $A_1,A_2$:

$$
\begin{aligned}
A_1 &= \{p_i \ \big | \ i = 0 \ldots m \}\\
A_2 &= \{p_i \ \big | \ i = m + 1 \ldots n-1 \}
\end{aligned}
$$

i rekurzivno nastavljamo te pronalazimo najbliži par točaka unutar svakog od dvaju skupova; neka su te udaljenosti $h_1,h_2$, a manju od njih označimo s $h$.

Sad slijedi spajanje! Pokušavamo pronaći par točaka od kojih jedna pripada skupu $A_1$, druga skupu $A_2$, a njihova je udaljenost manja od $h$. Zato sve točke čija se x-koordinata od $x_m$ razlikuje za manje od $h$ stavljamo u skup $B$:

$$
B = \{ p_i \ \big | \ \lvert x_i - x_m \rvert < h \}
$$

Pogledajmo sliku: pravac $m$ dijeli točke na dva dijela. Lijevo od $m$ je skup točaka $A_1$, a desno skup točaka $A_2$.

Zatim prema pravilu $B = \{ p_i \ \big | \ \lvert x_i - x_m \rvert < h \}$ dobivamo skup točaka $B$ koji čine zelene točke.![nearest-points1](./images/nearest-points1.png)

Za svaku točku $p_i$ iz $B$ trenutačni nam je cilj pronaći točku koja je također u $B$ i čija je udaljenost do nje manja od $h$. Da dvije točke ne bismo razmatrali međusobno dvaput, razmatramo samo one točke čija je y-koordinata manja od $y_i$. Očito za valjanu točku $p_j$ vrijednost $y_i - y_j$ mora biti manja od $h$. Tako dobivamo skup $C(p_i)$:

$$
C(p_i) = \{ p_j\ \big |\ p_j \in B,\ y_i - h < y_j \le y_i \}
$$

Odaberemo točku $p_i$ u skupu točaka $B$ i prema pravilu $C(p_i) = \{ p_j\ \big |\ p_j \in B,\ y_i - h < y_j \le y_i \}$ dobivamo skup točaka $C$ koji čine žute točke unutar crvenog pravokutnika.

![nearest-points2](./images/nearest-points2.png)

Ako točke iz $B$ sortiramo po $y_i$, skup $C(p_i)$ vrlo se lako dobiva: to je nekoliko uzastopnih točaka neposredno uz $p_i$.

Time dobivamo korake spajanja:

1.  Izgradimo skup $B$.
2.  Sortiramo točke iz $B$ po $y_i$. Uobičajeno je to $O(n\log n)$, ali promjenom strategije možemo to optimirati na $O(n)$ (objašnjeno u nastavku).
3.  Za svaku $p_i \in B$ razmatramo $p_j \in C(p_i)$; za svaki par $(p_i,p_j)$ izračunamo udaljenost i ažuriramo odgovor (najbliži par točaka u skupu koji trenutačno obrađujemo).

Primijetite da smo gore spomenuli dva sortiranja. Budući da se koordinate točaka cijelo vrijeme ne mijenjaju, prvo sortiranje možemo obaviti samo jednom, prije početka podjele. Neka svaki rekurzivni poziv vrati trenutačni skup točaka sortiran po $y_i$; za drugo sortiranje viša razina samo spoji (merge) dva zasebno sortirana skupa točaka iz niže razine.

Čini se da algoritam još uvijek nije dovoljno dobar: $|C(p_i)|$ bit će reda veličine $O(n)$, pa ukupna složenost ne bi bila točna. No nije tako — njegova je najveća veličina $7$, a evo dokaza:

## Dokaz složenosti

Već znamo da su y-koordinate svih točaka iz $C(p_i)$ u rasponu $(y_i-h,y_i]$ te da su x-koordinate svih točaka iz $C(p_i)$, kao i same točke $p_i$, u rasponu $(x_m-h,x_m+h)$. To čini pravokutnik dimenzija $2h \times h$.

Taj pravokutnik razdvojimo na dva kvadrata $h \times h$. Ne računajući $p_i$, točke u jednom kvadratu čine $C(p_i) \cap A_1$, a u drugom $C(p_i) \cap A_2$, pri čemu je udaljenost između bilo kojih dviju točaka unutar istog kvadrata veća od $h$. (Jer potječu iz iste niže razine rekurzije.)

Kvadrat $h \times h$ razdvojimo na četiri mala kvadrata $\frac{h}{2} \times \frac{h}{2}$. Vidimo da u svakom malom kvadratu može biti najviše $1$ točka: najveća udaljenost dviju točaka u tom malom kvadratu jednaka je duljini njegove dijagonale, tj. $\frac{h}{\sqrt 2}$, što je manje od $h$.

![nearest-points3](./images/nearest-points3.png)

Stoga u svakom kvadratu ima najviše $4$ točke, u pravokutniku najviše $8$ točaka, a kad izuzmemo samu $p_i$, $\max(C(p_i))=7$.

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/geometry/code/nearest-points/nearest-points_1.cpp"
    ```

## Poopćenje: trokut najmanjeg opsega u ravnini

Gornji se algoritam na zanimljiv način poopćuje na sljedeći problem: među zadanim točkama odabrati tri točke tako da zbroj njihovih međusobnih udaljenosti bude najmanji.

Algoritam uglavnom ostaje isti: svaki put pokušavamo pronaći trokut opsega manjeg od trenutačnog odgovora $d$, sve točke čija se x-koordinata od $x_m$ razlikuje za manje od $\frac{d}{2}$ stavljamo u skup $B$ i pokušavamo ažurirati odgovor. (Najdulja stranica trokuta opsega $d$ manja je od $\frac{d}{2}$.)

## Algoritam bez podjele pa vladanja

Zapravo, osim gore opisanog algoritma podijeli pa vladaj, postoji i drugi algoritam, bez podjele pa vladanja, iste vremenske složenosti $O(n \log n)$.

Možemo se poslužiti uobičajenom idejom pri obradi nizova: za svaki element u odgovor dodamo doprinos njega i svih elemenata lijevo od njega. Ista se ideja može primijeniti i na problem najbližeg para točaka u ravnini.

Konkretno, sve točke sortiramo tako da je $x_i$ prvi ključ, a $y_i$ drugi ključ, te izgradimo multiset s ključem $y_i$. Za svaku poziciju $i$ izvodimo sljedeće operacije:

1.  Iz skupa brišemo sve točke za koje vrijedi $x_i - x_j \ge d$. One više ne mogu pridonijeti odgovoru.
2.  Za sve točke u skupu za koje vrijedi $\lvert y_i - y_j \rvert < d$ izračunamo njihovu udaljenost do $p_i$.
3.  Ubacimo $p_i$ u skup.

Budući da se svaka točka ubacuje i briše najviše jednom, vremenska složenost ubacivanja i brisanja točaka je $O(n \log n)$, a dokaz vremenske složenosti dijela koji računa odgovor sličan je dokazu vremenske složenosti algoritma podijeli pa vladaj; čitatelj ga može sam pokušati provesti.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/geometry/code/nearest-points/nearest-points_2.cpp"
    ```

## Pristup s očekivanim linearnim vremenom

Zapravo, osim gore navedenih pristupa vremenske složenosti $O(n \log n)$, postoji i algoritam **očekivane** složenosti $O(n)$.

Najprije točke [nasumično promiješamo](../misc/random.md#shuffle); održavat ćemo odgovor za prefiks skupa točaka. Promotrimo kako iz prvih $i - 1$ točaka dobiti odgovor za $i$-tu točku.

Neka je $s$ udaljenost najbližeg para među prvih $i - 1$ točaka. Ravninu podijelimo na mrežu ćelija sa stranicom $s$ i za svaku ćeliju pohranimo točke u njoj (pomoću [hash tablice](../ds/hash.md)), a zatim provjerimo sve točke u devet ćelija oko ćelije u kojoj se nalazi $i$-ta točka i ažuriramo odgovor. Primijetite da je broj točaka koje treba provjeriti $O(1)$, jer je udaljenost najbližeg para među prvih $i - 1$ točaka $s$, pa svaka ćelija sadrži najviše $4$ točke.

Ako se pritom odgovor promijeni, ponovno izgradimo mrežu; inače je ne izgrađujemo ponovno. Među prvih $i$ točaka vjerojatnost da najbliži par sadrži $i$ iznosi $O\left(\frac{1}{i}\right)$, a cijena ponovne izgradnje mreže je $O(i)$, pa je očekivana cijena za $i$-tu točku $O(1)$. Stoga je za $n$ točaka očekivana složenost algoritma $O(n)$.

## Zadaci za vježbu

-   [UVa 10245 "The Closest Pair Problem"\[težina: niska\]](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1186)
-   [SPOJ #8725 CLOPPAIR "Closest Point Pair"\[težina: niska\]](https://www.spoj.com/problems/CLOPPAIR/)
-   [CODEFORCES Team Olympiad Saratov - 2011 "Minimum amount"\[težina: srednja\]](http://codeforces.com/contest/120/problem/J)
-   [SPOJ #7029 CLOSEST "Closest Triple"\[težina: srednja\]](https://www.spoj.com/problems/CLOSEST/)
-   [Google Code Jam 2009 Final "Min Perimeter"\[težina: srednja\]](https://github.com/google/coding-competitions-archive/blob/main/codejam/2009/world_finals/min_perimeter/statement.pdf)

## Literatura i dodatno štivo

**Dio ove stranice o algoritmu podijeli pa vladaj uglavnom je preveden iz članka [Нахождение пары ближайших точек](http://e-maxx.ru/algo/nearest_points) i njegova engleskog prijevoda [Finding the nearest pair of points](https://github.com/e-maxx-eng/e-maxx-eng/blob/master/src/geometry/nearest_points.md). Ruska je inačica pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0.**

[Zhihu kolumna: Računalna geometrija – problem najbližeg para točaka](https://zhuanlan.zhihu.com/p/74905629)
