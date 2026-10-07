---
title: Sufiksno balansirano stablo
---

## Definicija

Poredak među sufiksima određen je leksikografskim poretkom, a sufiksno balansirano stablo (suffix balanced tree) balansirano je stablo koje održava taj poredak sufiksa; drugim riječima, sufiksno balansirano stablo niza znakova $T$ uređeni je skup svih sufiksa od $T$. Jedan čvor sufiksnog balansiranog stabla odgovara jednom sufiksu izvornog niza.

Posebno, inorder obilazak sufiksnog balansiranog stabla upravo je sufiksno polje (suffix array).

## Postupak izgradnje

Za niz $T$ duljine $n$ gradimo njegovo sufiksno balansirano stablo tako da sufikse dodajemo u stablo obrnutim redoslijedom.

Označimo skup koji sufiksno balansirano stablo održava s $X$, a trenutačno dodani sufiks sa $S$; dodavanje sljedećeg sufiksa tada znači dodavanje $\texttt{c}S$ u $X$ (može se shvatiti i tako da sufiksno balansirano stablo održava niz $S$, a u sljedećem koraku ispred $S$ dodajemo znak $\texttt{c}$). Ta je operacija zapravo umetanje čvora u balansirano stablo.

Ovdje koristimo balansirano stablo s očekivanom visinom $O(\log n)$, npr. scapegoat tree ili treap.

### Pristup 1

Pri umetanju grubom silom uspoređujemo dva sufiksa i tako odlučujemo u koje podstablo idemo dalje. Tako jedno umetanje izvodi najviše $O(\log n)$ usporedbi, a jedna usporedba ima vremensku složenost najviše $O(n)$, što je ukupno $O(n\log n)$.

Umetanja ima ukupno $n$, pa vremenska složenost ovog pristupa ima gornju ogradu $O(n^2 \log n)$.

### Pristup 2

Uočimo da se $\texttt{c}S$ i $S$ razlikuju samo u znaku $\texttt{c}$ te da $S$ već pripada skupu $X$; to možemo iskoristiti za ubrzanje umetanja.

Pretpostavimo da trenutačno uspoređujemo nizove $\texttt{c}S$ i $A$, pri čemu je $A, S \in X$. Pri svakoj usporedbi najprije usporedimo prve znakove obaju nizova. Ako se prvi znakovi razlikuju, odnos među nizovima već je određen; ako su prvi znakovi jednaki, treba samo odrediti odnos nizova bez prvog znaka. A oba niza bez prvog znaka već pripadaju skupu $X$, pa ostatak usporedbe možemo obaviti operacijom balansiranog stabla za traženje ranga u $O(\log n)$. Tako jedno umetanje traje najviše $O(\log^2 n)$.

Umetanja ima ukupno $n$, pa vremenska složenost ovog pristupa ima gornju ogradu $O(n \log^2 n)$.

### Pristup 3

Prema pristupu 2, kad bismo u $O(1)$ mogli odrediti odnos dvaju čvorova balansiranog stabla, mogli bismo izgraditi sufiksno balansirano stablo u vremenu $O(n \log n)$.

Neka $val_i$ označava vrijednost čvora $i$. Ako pri izgradnji balansiranog stabla u svakom čvoru održavamo dodatnu oznaku $tag_i$ takvu da vrijedi $tag_i > tag_j \iff val_i > val_j$, tada odnos dvaju čvorova balansiranog stabla možemo odrediti u $O(1)$ usporedbom vrijednosti $tag_i$.

Neka svakom čvoru balansiranog stabla pridružimo realni interval, a korijenu interval $(0, 1)$. Za čvor $i$ označimo pridruženi realni interval s $(l, r)$; tada je $tag_i = \frac{l + r}{2}$, njegovom lijevom podstablu pridružen je realni interval $(l, tag_i)$, a desnom podstablu interval $(tag_i, r)$. Lako se dokaže da $tag_i$ zadovoljava gornji zahtjev.

Budući da koristimo balansirano stablo s očekivanom visinom $O(\log n)$, preciznost je u određenoj mjeri zajamčena. U praksi se može raditi i s većim intervalom, npr. tako da korijenu pridružimo $(0, 10^{18})$.

### Pristup 4

Zapravo možemo najprije izgraditi sufiksno polje, a zatim prema sufiksnom polju izgraditi sufiksno balansirano stablo. Usko grlo složenosti ovog pristupa jest složenost izgradnje sufiksnog polja ili složenost umetanja $n$ elemenata odjednom u odabrano balansirano stablo.

## Operacija brisanja

Pretpostavimo da je trenutačno dodani sufiks $\texttt{c}S$, a prethodno dodani sufiks $S$. Sufiksno balansirano stablo podržava i operaciju brisanja sufiksa $\texttt{c}S$ (može se shvatiti i tako da sufiksno balansirano stablo održava niz $\texttt{c}S$ i da brišemo početni znak $\texttt{c}$).

Slično umetanju, brisanje $\texttt{c}S$ obavljamo pomoću operacije brisanja čvora u balansiranom stablu.

## Prednosti sufiksnog balansiranog stabla

-   Ideja sufiksnog balansiranog stabla prilično je jasna; lakše ga je razumjeti od sufiksnog automata i drugih sufiksnih struktura, a tko zna napisati balansirano stablo, zna napisati i njega.
-   Složenost sufiksnog balansiranog stabla ne ovisi o veličini abecede.
-   Sufiksno balansirano stablo podržava brisanje jednog znaka s početka niza.
-   Ako se koristi balansirano stablo koje podržava perzistentnost, i sufiksno balansirano stablo može biti perzistentno.

## Primjeri zadataka

### [P3809 [predložak] Sufiksno sortiranje](https://www.luogu.com.cn/problem/P3809)

Zadatak-predložak za sufiksno polje: nakon izgradnje sufiksnog balansiranog stabla inorder obilaskom dobivamo sufiksno polje.

??? note "Primjer rješenja (inačica sa scapegoat treeom)"
    ```cpp
    --8<-- "docs/string/code/suffix-bst/suffix-bst_1.cpp"
    ```

### [P6164 [predložak] Sufiksno balansirano stablo](https://www.luogu.com.cn/problem/P6164)

???+ note "Zadatak"
    Zadan je početni niz znakova $s$ i $q$ operacija:
    
    1.  Na kraj trenutačnog niza dodaj nekoliko znakova.
    2.  S kraja trenutačnog niza obriši nekoliko znakova.
    3.  Upit: koliko se puta niz $t$ pojavljuje kao uzastopni podniz u trenutačnom nizu?
    
    Zadatak je **prisilno online**; ukupna promjena duljine niza i početna duljina su $\le 8 \times 10^5$, $q \le 10^5$, a ukupna duljina upita je $\le 3 \times 10^6$.

Za operacije 1 i 2: budući da sufiksno balansirano stablo lako održava umetanje i brisanje na početku, dolazimo na ideju da umetanje i brisanje na kraju pretvorimo u umetanje i brisanje na početku. Ako umjesto sufiksnog balansiranog stabla niza $s$ održavamo sufiksno balansirano stablo obrnutog niza od $s$, upravo smo postigli tu pretvorbu. Dodavanje i brisanje u balansiranom stablu su $O(\log n)$, pa je vremenska složenost dodavanja ili brisanja jednog znaka $O(\log n)$. Ako ukupan broj dodanih i obrisanih znakova označimo s $N$, ukupna vremenska složenost ovog dijela je $O(N \log n)$.

Za operaciju 3: broj pojavljivanja niza $t$ jednak je broju sufiksa kojima je $t$ prefiks, a broj sufiksa kojima je $t$ prefiks jednak je rangu njegova sljedbenika umanjenom za rang njegova prethodnika. Dodamo li iza $t$ jedan vrlo velik znak, dobivamo jednog sljedbenika od $t$. Smanjimo li posljednji znak niza $t$ za 1, dobivamo jednog prethodnika od $t$.

Sada treba pronaći rang nekog niza $t$ u sufiksnom balansiranom stablu; budući da ne možemo jamčiti da se $t$ pojavljuje u sufiksnom balansiranom stablu, svaki put nizove možemo uspoređivati samo grubom silom. Jedna usporedba ima vremensku složenost $O(|t|)$, a svaki upit izvodi najviše $O(\log n)$ usporedbi, pa je složenost jednog upita $O(|t|\log n)$. Ako zbroj duljina svih upitnih nizova označimo s $L$, ukupna vremenska složenost ovog dijela je $O(L \log n)$.

??? note "Primjer rješenja (inačica sa scapegoat treeom)"
    ```cpp
    --8<-- "docs/string/code/suffix-bst/suffix-bst_2.cpp"
    ```

## Literatura

-   Chen Lijie – „Primjena težinski balansiranih stabala i sufiksnih balansiranih stabala na informatičkim olimpijadama” (陈立杰 -《重量平衡树和后缀平衡树在信息学奥赛中的应用》)
