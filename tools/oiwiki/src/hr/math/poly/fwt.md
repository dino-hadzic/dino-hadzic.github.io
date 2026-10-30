---
title: Brza Walsh–Hadamardova transformacija
---

## Uvod

Walshova transformacija (Walsh Transform)[^note1] metoda je koja u spektralnoj analizi služi kao zamjena za diskretnu Fourierovu transformaciju i široko se primjenjuje u obradi signala. FFT radi s tipom double, dok Walshova transformacija signal rastavlja na pravokutne valove različitih frekvencija oscilacije, pa su svi koeficijenti cijeli brojevi jednake apsolutne vrijednosti; time se izbjegava množenje brojeva s pomičnim zarezom i povećava brzina računanja.

Dakle, osnovna ideja FWT-a i FFT-a trebala bi biti ista: oboje su transformacije niza. Rezultat brze Walshove transformacije niza $A$ označavamo $FWT[A]$.

Osnovna ideja FWT-a je sljedeća:

Trebamo novi niz $C$ koji se iz nizova $A$ i $B$ dobiva nekim pravilom računanja, tj. $C = A \cdot B$;

najprije unaprijed izračunamo nizove $FWT[A], FWT[B]$, zatim prema $FWT[C]=FWT[A] \cdot FWT[B]$ u vremenu $O(n)$ izračunamo $FWT[C]$, gdje je $\cdot$ množenje nizova po odgovarajućim pozicijama;

potom inverznom transformacijom dobivamo izvorni niz $C$. Vremenska složenost je $O(n \log{n})$.

U algoritamskim natjecanjima FWT je metoda za rješavanje problema konvolucije u kojima se nad indeksima provode bitovne operacije.

Formula: $C_{i} = \sum_{i=j \oplus k}A_{j} B_{k}$

(gdje je $\oplus$ neka binarna bitovna operacija)

U nastavku kao primjere uzimamo $\cup$ (bitovno ILI), $\cap$ (bitovno I) i $\oplus$ (bitovno XOR, isključivo ILI).

## Operacije FWT-a

### Operacija ILI

Ako je $k=i\cup j$, tada su pozicije na kojima $i$ u binarnom zapisu ima $1$ i pozicije na kojima $j$ ima $1$ sigurno podskup pozicija na kojima $k$ u binarnom zapisu ima $1$.

Želimo dobiti $FWT[C] = FWT[A] \cdot FWT[B]$, pa moramo konstruirati pravilo te FWT transformacije.

Prema definiciji očito možemo konstruirati $FWT[A]_i = A'_i = \sum_{i=i\cup j}A_{j}$, što znači da $j$ ima bitove $1$ samo na podskupu pozicija na kojima ih ima $i$.

Tada vrijedi:

$$
\begin{aligned}
FWT[A]_i\cdot FWT[B]_i&=\left(\sum_{i\cup j=i} A_j\right)\left(\sum_{i\cup k=i} B_k\right) \\
&=\sum_{i\cup j=i}\sum_{i\cup k=i}A_jB_k \\
&=\sum_{i\cup(j\cup k)=i}A_jB_k \\
&= FWT[C]_i
\end{aligned}
$$

Pogledajmo sada kako izračunati $FWT[A]$.

Jasno je da ne možemo enumerirati sve parove: složenost bi bila $O(n^2)$. Budući da ne možemo enumerirati sve, razmotrimo podjelu (divide and conquer).

Cijeli interval dijelimo na dva dijela; nakon podjele indeksi zapisani u binarnom obliku slijede određenu pravilnost.

Neka $A_0$ označava prvu polovicu niza $A$, a $A_1$ drugu polovicu intervala. Tada u $A_0$ najviši bit (najviši bit najvećeg indeksa niza A) iznosi $0$, pa su njegovi podskupovi upravo njegovi vlastiti podskupovi (jer je najviši bit $0$), dok je u $A_1$ najviši bit $1$, pa podskupovi koji zadovoljavaju uvjet nisu samo njegovi vlastiti, nego uključuju i podskupove s najvišim bitom $0$, tj.

$$
FWT[A] = merge(FWT[A_0], FWT[A_0] + FWT[A_1])
$$

gdje merge označava spajanje dvaju nizova kao kod nadovezivanja znakovnih nizova, a $+$ je obično zbrajanje, tj. zbrajanje odgovarajućih elemenata.

Tako podjelom spajanje obavljamo u $O(\log{n})$ razina, a pri svakom spajanju treba izvršiti jedan prolaz računanja, što znači da $FWT[A]$ dobivamo u vremenskoj složenosti $O(n\log{n})$.

Slijedi inverzija, koja je zapravo vrlo jednostavna: budući da znamo da je $A_0$ sam sebi podskup ($A_0 = FWT[A_0]$), a podskupovi od $A_1$ daju $FWT[A_0] + FWT[A_1]$, lako dobivamo rekurzivnu formulu inverzije:

$$
UFWT[A'] = merge(UFWT[A_0'], UFWT[A_1'] - UFWT[A_0'])
$$

U nastavku dajemo implementaciju. Lako se vidi da se izravna i inverzna transformacija mogu spojiti u jednu funkciju: pri izravnoj transformaciji $\text{type}=1$, pri inverznoj $\text{type}=-1$.

???+ note "Implementacija"
    ```cpp
    void Or(ll *a, ll type) {  // iterativna implementacija, manja konstanta
      for (ll x = 2; x <= n; x <<= 1) {
        ll k = x >> 1;
        for (ll i = 0; i < n; i += x) {
          for (ll j = 0; j < k; j++) {
            (a[i + j + k] += a[i + j] * type) %= P;
          }
        }
      }
    }
    ```

### Operacija I

Za operaciju I, analogno operaciji ILI, dobivamo slične zaključke

$$
FWT[A] = merge(FWT[A_0] + FWT[A_1], FWT[A_1])
$$

$$
UFWT[A'] = merge(UFWT[A_0'] - UFWT[A_1'], UFWT[A_1'])
$$

U nastavku dajemo implementaciju. Pri izravnoj transformaciji $\text{type}=1$, pri inverznoj $\text{type}=-1$.

???+ note "Implementacija"
    ```cpp
    void And(ll *a, ll type) {
      for (ll x = 2; x <= n; x <<= 1) {
        ll k = x >> 1;
        for (ll i = 0; i < n; i += x) {
          for (ll j = 0; j < k; j++) {
            (a[i + j] += a[i + j + k] * type) %= P;
          }
        }
      }
    }
    ```

### Operacija XOR

Konvolucija po XOR-u temelji se na sljedećem načelu:

Ako $x\circ y$ označava parnost broja znamenaka $1$ u $x\cap y$, tj. $x\circ y=\text{popcnt}(x\cap y)\bmod 2$, tada lako vrijedi $(x\circ y)\oplus (x\circ z)=x\circ(y\oplus z)$.

Računanje $FWT[A]$ također se lako dobiva.

Stavimo $FWT[A]_i=\sum_{i\circ j=0}A_j-\sum_{i\circ j=1}A_j$. Dokažimo ispravnost $FWT[C] = FWT[A] \cdot FWT[B]$:

$$
\begin{aligned}
FWT[A]_iFWT[B]_i&=\left(\sum_{i\circ j=0}A_j-\sum_{i\circ j=1}A_j\right)\left(\sum_{i\circ k=0}B_k-\sum_{i\circ k=1}B_k\right) \\
&=\left(\sum_{i\circ j=0}A_j\sum_{i\circ k=0}B_k+\sum_{i\circ j=1}A_j\sum_{i\circ k=1}B_k\right)-\left(\sum_{i\circ j=0}A_j\sum_{i\circ k=1}B_k+\sum_{i\circ j=1}A_j\sum_{i\circ k=0}B_k\right) \\
&=\sum_{(j\oplus k)\circ i=0}A_jB_k-\sum_{(j\oplus k)\circ i=1}A_jB_k \\
&=FWT[C]_i
\end{aligned}
$$

Pogledajmo kako brzo izračunati vrijednosti $A,B$; i dalje podjelom:

Za podniz $FWT[A_0]$, u kojem $i$ na trenutnom bitu ima $0$, pri operaciji $\circ$ rezultat se ne mijenja ni s $0$ ni s $1$ (jer je $0\cap 0=0,0\cap1=0$), pa je u $FWT[A]=\sum_{i\circ j=0}A_j-\sum_{i\circ j=1}A_j$ član $\sum_{i\circ j=1}A_j=0$.

Za podniz $A_1$, u kojem $i$ na trenutnom bitu ima $1$, pri operaciji $\circ$ rezultat s $0$ je $0$, a s $1$ je $1$ (jer je $1\cap 0=0,1\cap1=1$).

Ukupno imamo:

$$
FWT[A]=merge((FWT[A_0]+FWT[A_1])-0, FWT[A_0]-FWT[A_1])
$$

odnosno:

$$
FWT[A] = merge(FWT[A_0] + FWT[A_1], FWT[A_0] - FWT[A_1])
$$

Inverzna transformacija lako se dobiva:

$$
UFWT[A'] = merge(\frac{UFWT[A_0'] + UFWT[A_1']}{2}, \frac{UFWT[A_0'] - UFWT[A_1']}{2})
$$

Dajemo kod; pri izravnoj transformaciji $\text{type}=1$, pri inverznoj $\text{type}=\frac{1}{2}$.

???+ note "Implementacija"
    ```cpp
    void Xor(ll *a, ll type) {
      for (ll x = 2; x <= n; x <<= 1) {
        ll k = x >> 1;
        for (ll i = 0; i < n; i += x) {
          for (ll j = 0; j < k; j++) {
            (a[i + j] += a[i + j + k]) %= P;
            (a[i + j + k] = a[i + j] - a[i + j + k] * 2) %= P;
            (a[i + j] *= type) %= P;
            (a[i + j + k] *= type) %= P;
          }
        }
      }
    }
    ```

### Operacija XNOR

Analogno operaciji XOR dajemo formule:

$FWT[A]_{i} = \sum_{C_1}A_{j} - \sum_{C_2}A_{j}$ ($C_1$ označava da je $\text{popcnt}(x\cup y)\bmod 2$ jednako $0$, a $C_2$ da je $\text{popcnt}(x\cup y)\bmod 2$ jednako $1$)

$$
FWT[A] = merge(FWT[A_1] - FWT[A_0], FWT[A_1] + FWT[A_0])
$$

$$
UFWT[A'] = merge(\frac{UFWT[A_1'] - UFWT[A_0']}{2}, \frac{UFWT[A_1'] + UFWT[A_0']}{2})
$$

## FWT iz drugog kuta

Neka je $c(i,j)$ koeficijent doprinosa elementa $A_j$ vrijednosti $FWT[A]_i$. Postupak FWT transformacije možemo opisati iznova:

$$
FWT[A]_i = \sum_{j=0}^{n-1} c(i,j) A_j
$$

Budući da vrijedi:

$$
FWT[A]_i\cdot FWT[B]_i=FWT[C]_i
$$

jednostavnim dokazom dobivamo: $c(i,j)c(i,k)=c(i,j\odot k)$, gdje je $\odot$ bilo koja bitovna operacija.

Istodobno, funkcija $c$ ima još jedno važno svojstvo: može se obrađivati bit po bit.

Na primjer, pri transformaciji:

$$
FWT[A]_i = \sum_{j=0}^{n-1} c(i,j) A_j
$$

ovakvo je računanje prilično loše, pa ga rastavimo:

$$
FWT[A]_i = \sum_{j=0}^{n/2-1} c(i,j) A_j+\sum_{j=n/2}^{n-1} c(i,j) A_j
$$

Razmotrimo razliku između $i,j$ u prvom i drugom izrazu: razlikuju se samo u najvišem bitu.

Stoga vrijednosti $i,j$ bez najvišeg bita označimo $i',j'$, a $i_0$ neka bude najviši bit od $i$. Imamo:

$$
FWT[A]_i = c(i_0,0)\sum_{j=0}^{n/2-1} c(i',j') A_j+c(i_0,1)\sum_{j=n/2}^{n-1} c(i',j') A_j
$$

Ako je $i_0=0$, tada je:

$$
FWT[A]_i = c(0,0)\sum_{j=0}^{n/2-1} c(i',j') A_j+c(0,1)\sum_{j=n/2}^{n-1} c(i',j') A_j
$$

Za $i_0=1$ je:

$$
FWT[A]_i = c(1,0)\sum_{j=0}^{n/2-1} c(i',j') A_j+c(1,1)\sum_{j=n/2}^{n-1} c(i',j') A_j
$$

Drugim riječima, trebamo samo:

$$
\begin{bmatrix}
c(0,0) & c(0,1) \\
c(1,0) & c(1,1)
\end{bmatrix}
$$

četiri broja da bismo obavili transformaciju. Tu matricu nazivamo bitovnom matricom.

Ako želimo provesti inverznu transformaciju, trebamo inverz gornje bitovne matrice.

Ako je inverzna matrica $c^{-1}$, sličnim postupkom dobivamo izvorne vrijednosti:

$$
A_i = \sum_{j=0}^n c^{-1}(i,j) FWT[A]_j
$$

Inverzna matrica ne mora postojati; primjerice, ako postoji redak od $0$ ili stupac od $0$, matrica nema inverz, pa pri konstrukciji moramo biti posebno oprezni.

### Bitovno ILI

Možemo konstruirati:

$$
\begin{bmatrix}
1 & 0 \\
1 & 1
\end{bmatrix}
$$

Time je zadovoljeno $c(i,j)c(i,k)=c(i,j\cup k)$. Uočavamo da je to potpuno jednako ranije izvedenom $FWT[A]=\text{merge}(FWT[A_0], FWT[A_0]+FWT[A_1])$! Analogno, i sljedeća matrica zadovoljava taj uvjet, ali obično koristimo gornju:

$$
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix}
$$

Iako i sljedeća matrica zadovoljava $c(i,j)c(i,k)=c(i,j\cup k)$, ona ima redak od $0$ pa nema inverz, stoga nije dopuštena:

$$
\begin{bmatrix}
0 & 0 \\
1 & 1
\end{bmatrix}
$$

Ako želimo provesti inverznu transformaciju, moramo invertirati matricu; za **prvu, najgornju** matricu dobivamo:

$$
\begin{bmatrix}
1 & 0 \\
-1 & 1
\end{bmatrix}
$$

Zatim, na isti način kao pri izravnoj transformaciji, uvrstimo matricu inverzne transformacije.

### Bitovno I

Možemo konstruirati:

$$
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$

Time je zadovoljeno $c(i,j)c(i,k)=c(i,j\cap k)$.

Inverzna matrica:

$$
\begin{bmatrix}
1 & -1 \\
0 & 1
\end{bmatrix}
$$

### Bitovno XOR

Možemo konstruirati:

$$
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
$$

Time je zadovoljeno $c(i,j)c(i,k)=c(i,j\oplus k)$.

Inverzna matrica:

$$
\begin{bmatrix}
0.5 & 0.5 \\
0.5 & -0.5
\end{bmatrix}
$$

## FWT je linearna transformacija

FWT je linearna transformacija. To znači da zadovoljava:

$$
FWT[A+B]=FWT[A]+FWT[B]
$$

i:

$$
FWT[c\cdot A]=c\cdot FWT[A]
$$

## K-dimenzionalni FWT

Bitovne su operacije u biti operacije nad $n$-dimenzionalnim vektorom iz $\{0,1\}$. Operacija ILI uzima $\max$ po svakoj dimenziji, operacija I uzima $\min$ po svakoj dimenziji, a operacija XOR po svakoj dimenziji zbraja odgovarajuće komponente i zatim uzima $\bmod 2$.

Bitovne operacije imaju jedno svojstvo: svaka komponenta vektora je neovisna.

Proširimo $\{0,1\}$ na $[0,K)\cap \mathbf{Z}$, tj. na $K$-arni sustav, i pogledajmo što dobivamo.

### Operacija max

Proširimo operaciju $\cup$ na $K$-arni sustav tako da $i\cup j$ označava $\max$ po znamenkama; vrijedi:

$$
c(i,j)c(i,k)=c(i,j\cup k)
$$

Za $j=k$ gornji izraz postaje:

$$
c(i,j)c(i,j)=c(i,j)
$$

Drugim riječima, u svakom retku $1$ smije stajati samo ispred $0$; ako stoji iza, konstrukcija nije dopuštena. Malo isprobavanja daje jednu dopuštenu konstrukciju:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
1 & 1 & 1 & 0 \\
1 & 1 & 1 & 1
\end{bmatrix}
$$

Invertiranjem dobivamo:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
-1 & 1 & 0 & 0 \\
0 & -1 & 1 & 0 \\
0 & 0 & -1 & 1
\end{bmatrix}
$$

### Operacija min

Proširimo operaciju $\cap$ na $K$-arni sustav tako da $i\cap j$ označava $\min$ po znamenkama; vrijedi:

$$
c(i,j)c(i,k)=c(i,j\cap k)
$$

Za $j=k$ gornji izraz postaje:

$$
c(i,j)c(i,j)=c(i,j)
$$

Drugim riječima, u svakom retku $1$ smije stajati samo iza $0$; ako stoji ispred, konstrukcija nije dopuštena. Malo isprobavanja daje jednu dopuštenu konstrukciju:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 1 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Invertiranjem dobivamo:

$$
\begin{bmatrix}
1 & -1 & 0 & 0 \\
0 & 1 & -1 & 0 \\
0 & 0 & 1 & -1 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Prve dvije operacije rijetko se koriste; mnogo se češće koristi:

### Zbrajanje bez prijenosa

Proširimo operaciju $\oplus$ na $K$-arni sustav tako da $i\oplus j$ označava zbrajanje po znamenkama i zatim $\bmod K$; vrijedi:

$$
c(i,j)c(i,k)=c(i,j\oplus k)
$$

Konstruiramo li $c(i,j)=\omega_{K}^j$, uvjet je zadovoljen:

$$
\omega_{K}^j\omega_{K}^k=\omega_{K}^{j\oplus k}
$$

Međutim, matrica u kojoj su svi retci jednaki nema inverz, pa možemo konstruirati $c(i,j)=\omega_{K}^{(i-1)j}$.

Dobivamo sljedeću matricu:

$$
\begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & \omega_{K}^1 & \omega_{K}^2 & \cdots & \omega_{K}^{k-1} \\
1 & \omega_{K}^2 & \omega_{K}^4 & \cdots & \omega_{K}^{2(k-1)} \\
1 & \omega_{K}^3 & \omega_{K}^6 & \cdots & \omega_{K}^{3(k-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \omega_{K}^{k-1} & \omega_{K}^{2(k-1)} & \cdots & \omega_{K}^{(k-1)(k-1)}
\end{bmatrix}
$$

To je upravo [Vandermondeova matrica](https://en.wikipedia.org/wiki/Vandermonde_matrix); invertiranjem dobivamo:

$$
\frac{1}{K}\begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & \omega_{K}^{-1} & \omega_{K}^{-2} & \cdots & \omega_{K}^{-(k-1)} \\
1 & \omega_{K}^{-2} & \omega_{K}^{-4} & \cdots & \omega_{K}^{-2(k-1)} \\
1 & \omega_{K}^{-3} & \omega_{K}^{-6} & \cdots & \omega_{K}^{-3(k-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \omega_{K}^{-(k-1)} & \omega_{K}^{-2(k-1)} & \cdots & \omega_{K}^{-(k-1)(k-1)}
\end{bmatrix}
$$

Ako za modul zadan u zadatku postoji korijen jedinice, implementacija je jednostavna.

Međutim, **korijen jedinice u modularnoj aritmetici možda ne postoji**, pa razmatramo proširenje polja: umjetno definiramo $x$ koji zadovoljava $x^K=1$ i zatim izravno računamo s $x$, tako da je svaki broj polinom stupnja $k-1$ u $x$. Dovoljno je računati $\bmod {x^K-1}$. Matrica se tada može zapisati ovako:

$$
\begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & x^1 & x^2 & \cdots & x^{k-1} \\
1 & x^2 & x^4 & \cdots & x^{2(k-1)} \\
1 & x^3 & x^6 & \cdots & x^{3(k-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x^{k-1} & x^{2(k-1)} & \cdots & x^{(k-1)(k-1)}
\end{bmatrix}
$$

No tako mogu nastati djelitelji nule, tj. **jedan broj može imati više prikaza**, pa ne možemo odrediti stvarnu vrijednost broja.

Umjesto $\bmod {x^K-1}$ računamo $\bmod$ ciklotomički polinom $\Phi_{K}(x)$, u kojem $x$ ima red $k$ i koji je ireducibilan nad $\mathbb{Q}$. Stoga gornje računanje definiramo kao računanje $\bmod {\Phi_{K}(x)}$.

Preostaje još problem da $\bmod \Phi_{K}(x)$ ima veliku konstantu (jer je $\Phi$ sam polinom). Ali budući da $\Phi_{K}(x)\mid x^k-1$, tijekom računanja dovoljno je uzimati $\bmod x^k -1$, a tek na kraju $\bmod \Phi_{K}(x)$.

## Primjeri zadataka

???+ note "[CF 1103E Radix sum](https://www.luogu.com.cn/problem/CF1103E)"
    Zadan je niz $a_1,a_2,...,a_n$ duljine $n$. Za svaki $p \in [0,n-1]$ treba odrediti broj cjelobrojnih nizova $i_1,i_2,...,i_n$ koji zadovoljavaju sljedeće uvjete, modulo $2^{58}$:
    
    -   $\forall j \in [1,n] , i_j \in [1,n]$;
    -   $\sum\limits_{j=1}^n a_{i_j} = p$, pri čemu je zbrajanje definirano kao dekadsko zbrajanje bez prijenosa.
    
    $n\le10^5,a_i\le10^5$
    
    ??? note "Rješenje"
        Možemo se sjetiti DP-a: definiramo stanje $f_{i,s}$ koje znači da smo razmotrili prvih $i$ brojeva i da je trenutno stanje zbroja $s$. Budući da je FWT transformacija linearna, možemo najprije prijeći na FWT prikaz po vrijednostima, zatim ga dignuti na $n$-tu potenciju i na kraju transformirati natrag.
        
        To je trivijalno, ali u zadatku je modul $2^{58}$. Uočavamo da korijen jedinice ne postoji, pa razmatramo proširenje polja.
        
        Ciklotomički polinom ovdje je $\Phi_{10}(x)=x^4-x^3+x^2-x+1$.
        
        Međutim, pri UFWT-u treba dijeliti bazom $10$, a $10$ nema inverz modulo $2^{58}$. Zapravo, $5$ ima inverz modulo $2^{58}$: $57646075230342349$, pa preostaje još podijeliti s $2$. Neka je odgovor nakon dijeljenja s $5$ jednak $x$, a pravi odgovor $y$, tj. $2^5y\equiv x\pmod{2^{64}}$; očito vrijedi $y\equiv \frac{x}{2^5}\pmod{2^{64-5}}$, tj. $y\equiv \frac{x}{2^5}\pmod{2^{59}}$, pa je dovoljno konačni odgovor podijeliti s $2^5$. Iako nije jasno zašto je autor zadatka tražio modul $2^{58}$, dovoljno je na kraju još jednom uzeti ostatak.

???+ note "[CF103329F (XXII Opencup, Grand Prix of XiAn) The Struggle](https://codeforces.com/gym/103329/problem/F)"
    Zadana je elipsa $E$ u kojoj su koordinate svih cjelobrojnih točaka u intervalu $[1,4 \cdot 10^6]$. Treba izračunati $\sum_{(x,y) \in E} (x \oplus y)^{33}x^{-2}y^{-1} \mod 10^9+7$.
    
    ??? note "Rješenje"
        Ovo je zadatak u kojem tehnika nije izravno vidljiva; autor je dao detaljno rješenje na engleskom jeziku, vidi [ovu poveznicu](https://codeforces.com/blog/entry/96518).

## Literatura

-   [桃酱的算法笔记 (Taojiangove bilješke o algoritmima)](https://zhuanlan.zhihu.com/p/41867199)
-   [Blog korisnika ZnPdCo](https://znpdco.github.io/%E7%AE%97%E6%B3%95/2024/05/07/FWT.html)

[^note1]: [Wikipedija](https://en.wikipedia.org/wiki/Hadamard_transform)
