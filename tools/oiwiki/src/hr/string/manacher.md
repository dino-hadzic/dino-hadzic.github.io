---
title: Manacher
---

## Opis

Zadana je duljina $n$ i string $s$ te duljine. Pronađite sve parove $(i, j)$ za koje je podstring $s[i \dots j]$ palindrom. Ako vrijedi $t = t_{\text{rev}}$, onda je $t$ palindrom ($t_{\text{rev}}$ je obrnuti string $t$).

## Objašnjenje

Očito u najgorem slučaju može biti $O(n^2)$ palindroma, pa se na prvi pogled čini da za ovaj problem ne postoji linearan algoritam.

Međutim, informacije o palindromima možemo zapisati **sažetije**: za svaku poziciju $i = 0 \dots n - 1$ pronađemo vrijednosti $d_1[i]$ i $d_2[i]$. One redom predstavljaju broj palindroma neparne i parne duljine sa središtem na poziciji $i$. Ekvivalentno, to su polumjeri najduljih palindroma sa središtem na $i$ (oba polumjera $d_1[i]$, $d_2[i]$ broje znakove od pozicije $i$ do krajnje desne pozicije palindroma, uključivo).

Primjerice, string $s = \mathtt{abababc}$ ima tri palindroma neparne duljine sa središtem na $s[3] = b$. Polumjer najduljeg jest $3$, odnosno $d_1[3] = 3$:

$$
a\ \overbrace{b\ a\ \underset{s_3}{b}\ a\ b}^{d_1[3]=3}\ c
$$

String $s = \mathtt{cbaabd}$ ima dva palindroma parne duljine sa središtem na $s[3] = a$. Polumjer najduljeg jest $2$, odnosno $d_2[3] = 2$:

$$
c\ \overbrace{b\ a\ \underset{s_3}{a}\ b}^{d_2[3]=2}\ d
$$

Ključna je ideja da, ako na nekoj poziciji $i$ imamo središte palindroma duljine $l$, tada na $i$ imamo i središta palindroma duljina $l - 2$, $l - 4$ i tako dalje. Zato su dva polja $d_1[i]$ i $d_2[i]$ dovoljna za opis svih palindromskih podstringova stringa.

Iznenađujuće, postoji prilično jednostavan linearan algoritam za izračun tih dvaju „polja palindroma” $d_1[]$ i $d_2[]$. U ovom ga članku detaljno opisujemo.

## Pristupi rješavanju

Problem se može riješiti na više načina: hashiranje stringova daje rješenje u vremenu $O(n \log n)$, a sufiksno polje i brzi LCA daju rješenje u vremenu $O(n)$.

No ovdje opisani algoritam **znatno** je jednostavniji i ima manje konstante i u vremenskoj i u prostornoj složenosti. Predložio ga je **Glenn K. Manacher** 1975. godine.

## Naivni algoritam

Kako bismo izbjegli kasnije nejasnoće, objasnimo što podrazumijevamo pod „naivnim algoritmom”.

Za svako središte $i$ algoritam uspoređuje par odgovarajućih znakova i pokušava povećati odgovor za $1$ dokle god je to moguće.

Ovaj je algoritam spor: za izračun odgovora potrebno mu je $O(n^2)$ vremena.

Slijedi implementacija naivnog algoritma:

???+ note "Implementacija"
    === "C++"
        ```cpp
        vector<int> d1(n), d2(n);
        for (int i = 0; i < n; i++) {
          d1[i] = 1;
          while (0 <= i - d1[i] && i + d1[i] < n && s[i - d1[i]] == s[i + d1[i]]) {
            d1[i]++;
          }
        
          d2[i] = 0;
          while (0 <= i - d2[i] - 1 && i + d2[i] < n &&
                 s[i - d2[i] - 1] == s[i + d2[i]]) {
            d2[i]++;
          }
        }
        ```
    
    === "Python"
        ```python
        d1 = [0] * n
        d2 = [0] * n
        for i in range(0, n):
            d1[i] = 1
            while 0 <= i - d1[i] and i + d1[i] < n and s[i - d1[i]] == s[i + d1[i]]:
                d1[i] += 1
        
            d2[i] = 0
            while 0 <= i - d2[i] - 1 and i + d2[i] < n and s[i - d2[i] - 1] == s[i + d2[i]]:
                d2[i] += 1
        ```

## Manacherov algoritam

Ovdje opisujemo samo pronalaženje svih palindromskih podstringova neparne duljine, odnosno računanje $d_1[]$. Za pronalaženje svih palindromskih podstringova parne duljine (računanje polja $d_2[]$) potrebne su samo male izmjene algoritma za neparne duljine.

Za učinkovit izračun održavamo **granice $[l, r]$** dosad pronađenog palindromskog podstringa koji doseže najdalje udesno (palindroma s najvećim $r$, gdje su $l$ i $r$ pozicije njegove lijeve i desne granice). Na početku postavimo $l = 0$ i $r = -1$ (*-1* ovdje nije indeks koji se broji od kraja; može biti bilo koji negativan broj i služi samo jednostavnijoj inicijalizaciji petlje).

### Postupak

Pretpostavimo da sada želimo za sljedeći $i$ izračunati $d_1[i]$, a sve prethodne vrijednosti polja $d_1[]$ već su izračunate. Postupamo ovako:

-   Ako je $i$ izvan trenutačnog palindromskog podstringa, odnosno $i > r$, primijenimo naivni algoritam.

    Nastavljamo povećavati $d_1[i]$ i u svakom koraku provjeravamo je li trenutačni podstring $[i - d_1[i] \dots i + d_1[i]]$ palindrom ($d_1[i]$ ovdje i dalje označava polumjer). Zaustavljamo se na prvom paru različitih znakova ili na granici stringa $s$. U oba je slučaja $d_1[i]$ izračunat. Nakon toga ne zaboravimo ažurirati $(l, r)$.

-   Sada razmotrimo $i \le r$. Pokušavamo iskoristiti već izračunate vrijednosti polja $d_1[]$. Najprije unutar palindroma $(l, r)$ zrcalimo poziciju $i$ i dobijemo $j = l + (r - i)$. Promotrimo $d_1[j]$. Budući da je $j$ simetričan poziciji $i$, **gotovo uvijek** možemo postaviti $d_1[i] = d_1[j]$. Ideja je prikazana u nastavku (zamislimo da palindrom sa središtem na $j$ „kopiramo” na poziciju sa središtem na $i$):

    $$
    \ldots\
    \overbrace{
        s_l\ \ldots\
        \underbrace{
            s_{j-d_1[j]+1}\ \ldots\ s_j\ \ldots\ s_{j+d_1[j]-1}
        }_\text{palindrome}\
        \ldots\
        \underbrace{
            s_{i-d_1[j]+1}\ \ldots\ s_i\ \ldots\ s_{i+d_1[j]-1}
        }_\text{palindrome}\
        \ldots\ s_r
    }^\text{palindrome}\
    \ldots
    $$

    Međutim, postoji **nezgodan slučaj** koji moramo ispravno obraditi: „unutarnji” palindrom doseže granicu „vanjskog”, odnosno $j - d_1[j] + 1 \le l$ (ekvivalentno, $i + d_1[j] - 1 \ge r$). Izvan „vanjskog” palindroma simetrija nije zajamčena, pa ne bi bilo ispravno jednostavno postaviti $d_1[i] = d_1[j]$: nemamo dovoljno informacija da bismo tvrdili da palindrom na $i$ ima jednaku duljinu.

    Kako bismo taj slučaj ispravno obradili, „skratimo” palindrom postavljanjem $d_1[i] = r - i + 1$. Zatim pokrenemo naivni algoritam i povećamo $d_1[i]$ koliko god možemo.

    Taj je slučaj prikazan u nastavku (palindrom sa središtem na $j$ skraćen je kako bi stao unutar „vanjskog” palindroma):

    $$
    \ldots\
    \overbrace{
        \underbrace{
            s_l\ \ldots\ s_j\ \ldots\ s_{j+(j-l)}
        }_\text{palindrome}\
        \ldots\
        \underbrace{
            s_{i-(r-i)}\ \ldots\ s_i\ \ldots\ s_r
        }_\text{palindrome}
    }^\text{palindrome}\
    \underbrace{
        \ldots \ldots \ldots \ldots \ldots
    }_\text{try moving here}
    $$

    Prikaz pokazuje da, iako palindrom sa središtem na $j$ može biti dulji i izlaziti izvan „vanjskog” palindroma, na poziciji $i$ možemo iskoristiti samo dio potpuno sadržan u „vanjskom” palindromu. Ipak, odgovor na $i$ može biti veći, pa zatim pokrenemo naivni algoritam i pokušamo proširiti palindrom izvan „vanjskog”, u područje označeno s „try moving here”.

Na kraju još jednom podsjećamo da nakon izračuna svakog $d_1[i]$ treba ažurirati vrijednosti $(l, r)$.

Ponovimo: algoritam za računanje polja palindroma parne duljine $d_2[]$ vrlo je sličan prethodnom algoritmu za polje palindroma neparne duljine $d_1[]$.

## Složenost Manacherova algoritma

Budući da pri računanju odgovora za pojedinu poziciju koristimo naivni algoritam, na prvi pogled nije očito da je vremenska složenost linearna.

No pažljivija analiza pokazuje da je složenost linearna. Napomenimo da je [algoritam za računanje Z-funkcije](./z-func.md) sličan i također ima linearnu vremensku složenost.

Naime, svaka iteracija naivnog algoritma povećava $r$ za $1$, a $r$ se tijekom algoritma nikad ne smanjuje. Iz tih opažanja slijedi da naivni algoritam ukupno ima $O(n)$ iteracija.

Ostatak Manacherova algoritma očito je također linearan, pa ukupna složenost iznosi $O(n)$.

## Implementacija Manacherova algoritma

### Zasebna obrada slučajeva

Za računanje $d_1[]$ koristimo sljedeći kôd:

=== "C++"
    ```cpp
    vector<int> d1(n);
    for (int i = 0, l = 0, r = -1; i < n; i++) {
      int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
      while (0 <= i - k && i + k < n && s[i - k] == s[i + k]) {
        k++;
      }
      d1[i] = k--;
      if (i + k > r) {
        l = i - k;
        r = i + k;
      }
    }
    ```

=== "Python"
    ```python
    d1 = [0] * n
    l, r = 0, -1
    for i in range(0, n):
        k = 1 if i > r else min(d1[l + r - i], r - i + 1)
        while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
            k += 1
        d1[i] = k
        k -= 1
        if i + k > r:
            l = i - k
            r = i + k
    ```

Kôd za računanje $d_2[]$ vrlo je sličan, uz male razlike u aritmetičkim izrazima:

=== "C++"
    ```cpp
    vector<int> d2(n);
    for (int i = 0, l = 0, r = -1; i < n; i++) {
      int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
      while (0 <= i - k - 1 && i + k < n && s[i - k - 1] == s[i + k]) {
        k++;
      }
      d2[i] = k--;
      if (i + k > r) {
        l = i - k - 1;
        r = i + k;
      }
    }
    ```

=== "Python"
    ```python
    d2 = [0] * n
    l, r = 0, -1
    for i in range(0, n):
        k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
        while 0 <= i - k - 1 and i + k < n and s[i - k - 1] == s[i + k]:
            k += 1
        d2[i] = k
        k -= 1
        if i + k > r:
            l = i - k - 1
            r = i + k
    ```

### Objedinjena obrada

Iako smo u objašnjenju i prethodnim implementacijama zasebno računali $d_1[]$ i $d_2[]$, jednim trikom oba izračuna možemo svesti na računanje $d_1[]$.

Za zadanu duljinu $n$ i string $s$ te duljine, u svaku od $n + 1$ praznina umetnemo separator $\#$ te dobijemo duljinu $2n + 1$ za novi string $s'$. Primjerice, za $s = \mathtt{abababc}$ dobivamo $s' = \mathtt{\#a\#b\#a\#b\#a\#b\#c\#}$.

Svaki $\#$ između slova predstavlja odgovarajuću „prazninu” u $s$. Znakovi $\#$ na oba kraja služe jednostavnijoj implementaciji.

Nakon obrade stringa $s'$ i računanja polja $d_1[]$, na bilo kojoj poziciji $i$ najdulji palindromski podstring opisan s $d_1[i]$ mora završavati znakom $\#$ (kad bi završavao slovom, znakovi $\#$ s obje strane omogućili bi još jedno proširenje). Zato maksimalnom palindromu u $s$ sa središtem na slovu i duljinom $m + 1$ u $s'$ odgovara maksimalni palindrom sa središtem na istom slovu i duljinom $2m + 3$. Maksimalnom palindromu u $s$ sa središtem u praznini i duljinom $m$ u $s'$ odgovara maksimalni palindrom sa središtem na odgovarajućem $\#$ i duljinom $2m + 1$ (u oba je slučaja $m$ paran, ali to ne utječe na zaključak). Iz tih opažanja i malo računanja slijedi da u $s'$ vrijednost $d_1[i]$ predstavlja **ukupnu duljinu uvećanu za jedan** maksimalnog palindromskog podstringa sa središtem na odgovarajućoj poziciji u $s$.

Time je uspostavljena veza između stringa $s'$ i njegova polja $d_1[]$ te stringa $s$ i njegovih polja $d_1[]$ i $d_2[]$.

Budući da se objedinjenom obradom za $s'$ zapravo računa $d_1[]$, nakon konstrukcije stringa $s'$ kôd je jednak onome za računanje $d_1[]$ iz prethodnog odjeljka.

## Zadaci za vježbu

-   [UVa #11475 "Extend to Palindrome"](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2470)
-   [Nacionalni pripremni tim: Najdulji dvostruki palindrom](https://www.luogu.com.cn/problem/P4555)
-   [CF1326D2. Labyrinth](https://codeforces.com/contest/1326/problem/D2)

**Ova je stranica uglavnom prevedena iz objave [Нахождение всех подпалиндромов](http://e-maxx.ru/algo/palindromes_count) i njezina engleskog prijevoda [Finding all sub-palindromes in $O(N)$](https://cp-algorithms.com/string/manacher.html). Ruska inačica ima licencu Public Domain + Leave a Link, a engleska CC-BY-SA 4.0.**
