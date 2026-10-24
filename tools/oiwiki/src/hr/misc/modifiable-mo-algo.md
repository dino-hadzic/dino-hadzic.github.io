---
title: Mo algoritam s izmjenama
---

Provjerite da već vladate običnim Mo algoritmom. Ako ga još ne znate, prvo pročitajte prethodnu stranicu [Običan Mo algoritam](./mo-algo.md).

## Značajke

Običan Mo algoritam ne podržava izmjene.

Možemo ga nasilu natjerati da podržava izmjene: kao u DP-u, možemo nasilu dodati jednu dimenziju, **vremensku dimenziju**, koja označava vrijeme ove operacije.

Vremenska dimenzija označava broj dosad primijenjenih izmjena.

Drugim riječima, upit $[l,r]$ pretvaramo u $[l,r,\text{time}]$.

Tada se naše koordinate mogu pomicati i po vremenskoj dimenziji, tj. $[l,r,\text{time}]$ ima jednu dimenziju više u kojoj se može pomaknuti i može prijeći u:

-   $[l-1,r,\text{time}]$
-   $[l+1,r,\text{time}]$
-   $[l,r-1,\text{time}]$
-   $[l,r+1,\text{time}]$
-   $[l,r,\text{time}-1]$
-   $[l,r,\text{time}+1]$

Takav je prijelaz također $O(1)$, ali naše sortiranje ima jedan ključ više; dovoljno je malo doraditi.

Sortiranje i prijelazi mogu se izvesti slično običnom Mo algoritmu, čime se postiže $O(n^{5/3})$.

Ovaj put sortiramo tako da je blok duljine $n^{2/3}$ i blokova je $n^{1/3}$; prvi je ključ blok u kojem se nalazi lijevi kraj, drugi ključ blok u kojem se nalazi desni kraj, a treći ključ vrijeme.

???+ note "Optimalna duljina bloka i analiza vremenske složenosti"
    Neka je duljina niza $n$, neka ima $m$ upita i $t$ izmjena.
    
    Drugi ključ sortiranja u Mo algoritmu s izmjenama indeks je bloka u kojem se nalazi desni kraj, za razliku od običnog Mo algoritma.
    
    Razmislite što bi bilo da desni kraj ne dijelimo na blokove:
    
    -   Nesortirani desni krajevi za svaki bi se upit pomicali $n$ puta.
    -   Sortirani desni krajevi donijeli bi nesortirana vremena, pa bi se za svaki upit vrijeme pomicalo $t$ puta.
    
    U oba je slučaja vremenski trošak neprihvatljiv.
    
    Analizirajmo sada vremensku složenost.
    
    Neka je duljina bloka $s$; tada ima $\dfrac{n}{s}$ blokova. Za blokove $i$ i $j$ neka $q_{i,j}$ označava broj upita čiji je lijevi kraj u bloku $i$, a desni kraj u bloku $j$.
    
    Za svaku „grupu” upita $(i,j)$ kod kojih lijevi i desni kraj ne mijenjaju blok, krajevi se pri svakom pomaku pomiču $O(s)$ puta, a vrijeme monotono raste: $O(t)$.
    
    Vrijeme promjene bloka lijevog i desnog kraja zanemarujemo.
    
    Zapisano, to je:
    
    $$
    \begin{aligned}
    &\sum_{i=1}^{n/s}\sum_{j=i+1}^{n/s}(q_{i,j}\cdot s+t)\\
    =&ms+\left(\dfrac{n}{s}\right)^2t\\
    =&ms+\dfrac{n^2t}{s^2}
    \end{aligned}
    $$
    
    Minimum tog izraza tražimo deriviranjem. Neka je $f(s)=ms+\dfrac{n^2t}{s^2}$. Tada je $f'(s)=m-\dfrac{2n^2t}{s^3}=0$.
    
    Dobivamo $s=\sqrt[3]{\dfrac{2n^2t}{m}}=\dfrac{2^{1/3}n^{2/3}t^{1/3}}{m^{1/3}}=s_0$.
    
    Dakle, kad je duljina bloka $\dfrac{n^{2/3}t^{1/3}}{m^{1/3}}$, dobiva se optimalna vremenska složenost $O\left(n^{2/3}m^{2/3}t^{1/3}\right)$.
    
    Često spominjana složenost $O\left(n^{5/3}\right)$ upravo je vremenska složenost kad se $n,m,t$ smatraju istim redom veličine.
    
    U praksi se ipak preporučuje uzeti $n^{2/3}$ za duljinu bloka.

## Primjer

???+ note "Primjer [「国家集训队」数颜色/维护队列 (Brojanje boja / održavanje reda)](https://www.luogu.com.cn/problem/P1903)"
    Sažetak zadatka: zadan je niz i M operacija dviju vrsta:
    
    1.  promijeni broj na nekom mjestu u nizu
    2.  upitaj koliko različitih brojeva ima u intervalu $[l,r]$ (više jednakih brojeva računa se kao jedan)

Lako je uočiti da bismo bez operacije 1 (izmjene) zadatak lako riješili običnim Mo algoritmom.

No zadatak sadrži i izmjene pojedinih elemenata, pa koristimo **Mo algoritam s izmjenama**.

### Postupak

Prvo razmotrimo pristup običnim Mo algoritmom:

-   Pri svakom proširenju intervala, za svaki dodani broj prebrojimo koliko se puta već pojavio; ako je prije dodavanja broj pojavljivanja te vrijednosti bio $0$, riječ je o novoj vrijednosti i odgovor se uveća za $1$. Zatim se broj pojavljivanja te vrijednosti uveća za $1$.
-   Pri svakom smanjenju intervala, za svaki izbrisani broj prebrojimo koliko se puta pojavljuje nakon brisanja; ako je nakon brisanja broj pojavljivanja te vrijednosti $0$, ta je vrijednost potpuno izbrisana iz trenutačnog intervala, tj. trenutačni interval ima jednu boju manje, pa se odgovor umanji za $1$. Zatim se broj pojavljivanja te vrijednosti umanji za $1$.

Razmotrimo sada izmjene:

-   Izmjena jednog elementa mijenja broj na nekom mjestu. Ako prelazimo s upita koji je prošao $i$ izmjena na upit koji je prošao $j$ izmjena i vrijedi $i<j$, moramo nasilu primijeniti izmjene od $(i+1)$-ve do $j$-te.
-   Ako je $j<i$, moramo nasilu poništiti izmjene od $i$-te do $(j+1)$-ve.

Kako nasilu primijeniti izmjenu? Pretpostavimo da izmjena mijenja boju na položaju $pos$, da je izvorna boja na $pos$ bila $a$, a nakon izmjene je $b$, i da je trenutačni interval Mo algoritma proširen na $[l,r]$.

-   Primjena izmjene: najprije provjerimo je li $pos$ unutar intervala $[l,r]$. Ako jest, to je isto kao da iz intervala izbrišemo boju $a$ i dodamo boju $b$, a $pos$-ti element trenutačnog niza boja promijenimo u $b$. Ako nije unutar intervala $[l,r]$, samo izravno promijenimo $pos$-ti element trenutačnog niza boja u $b$.
-   Poništavanje izmjene: isto je kao primjena izmjene koja mijenja $pos$-ti element i boju $b$ mijenja u boju $a$.

Tako je ovaj zadatak lako riješen Mo algoritmom s izmjenama!

### Implementacija

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/misc/code/modifiable-mo-algo/modifiable-mo-algo_1.cpp"
    ```
