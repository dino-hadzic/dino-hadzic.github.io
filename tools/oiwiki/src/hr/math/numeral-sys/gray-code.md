---
title: Grayev kod
---

Grayev kod (Gray code) binarni je brojevni sustav u kojem se dva susjedna broja razlikuju u samo jednom bitu. Na primjer, niz Grayevih kodova $3$-bitnih binarnih brojeva glasi

$$
000,001,011,010,110,111,101,100
$$

Napomena: indekse niza brojimo od $0$, tj. $G(0)=000,G(4)=110$.

Grayev kod predložio je Frank Gray iz Bell Labsa 1940-ih, a patentiran je 1953.

## Konstrukcija Grayeva koda (transformacija)

Postoji mnogo načina konstrukcije Grayeva koda. Najprije predstavljamo ručnu konstrukciju, a zatim dajemo kôd za konstrukciju i dokaz ispravnosti.

### Ručna konstrukcija

$k$-bitni Grayev kod može se konstruirati na sljedeći način. Krenemo od Grayeva koda sa svim znamenkama $0$ i primjenjujemo sljedeću strategiju:

1.  invertiramo najniži bit i dobijemo sljedeći Grayev kod (na primjer $000\to 001$);
2.  invertiramo bit lijevo od najdesnije $1$ i dobijemo sljedeći Grayev kod (na primjer $001\to 011$);

Naizmjeničnom primjenom ovih strategija $2^{k-1}$ puta dobivamo niz $k$-bitnih Grayevih kodova.

### Zrcalna konstrukcija

$k$-bitni Grayev kod brzo se dobiva iz $k-1$-bitnoga tako da ga zrcalimo odozgo prema dolje i dodamo novi bit, kao na slici:

$$
\begin{matrix}
k=1\\
0\\ 1\\\\\\\\\\\\\\
\end{matrix}
\to \begin{matrix}\\
\color{Red}0\\\color{Red}1\\\color{Blue}1\\\color{Blue}0\\\\\\\\\\
\end{matrix}
\to \begin{matrix}
k=2\\
{\color{Red}0}0\\{\color{Red}0}1\\{\color{Blue}1}1\\{\color{Blue}1}0\\\\\\\\\\
\end{matrix}
\to \begin{matrix}\\
\color{Red}00\\\color{Red}01\\\color{Red}11\\\color{Red}10\\\color{Blue}10\\\color{Blue}11\\\color{Blue}01\\\color{Blue}00
\end{matrix}
\to \begin{matrix}
k=3\\
{\color{Red}0}00\\{\color{Red}0}01\\{\color{Red}0}11\\{\color{Red}0}10\\{\color{Blue}1}10\\{\color{Blue}1}11\\{\color{Blue}1}01\\{\color{Blue}1}00
\end{matrix}
$$

### Način izračuna

Promotrimo binarni zapis broja $n$ i $G(n)$. Može se uočiti da je $i$-ti bit od $G(n)$ jednak $1$ točno onda kad je $i$-ti bit od $n$ jednak $1$, a $i+1$-vi bit jednak $0$, ili je $i$-ti bit jednak $0$, a $i+1$-vi bit jednak $1$. Stoga to možemo shvatiti kao operaciju XOR, tj.

$$
G(n)=n\oplus \left\lfloor\frac{n}{2}\right\rfloor
$$

```cpp
int g(int n) { return n ^ (n >> 1); }
```

### Dokaz ispravnosti

Dokažimo sada da se u nizu Grayevih kodova dobivenih gornjom formulom dva susjedna Grayeva koda razlikuju u točno jednom bitu.

Promotrimo razliku između $n$ i $n+1$. Dodati $1$ broju $n$ znači invertirati sve uzastopne $1$ na kraju binarnog zapisa broja $n$, a zatim najnižu $0$ pretvoriti u $1$. Bitove brojeva $n$ i $n+1$ zapišimo ovako:

$$
\begin{aligned}
(n)_2 &= \cdots0\underbrace{11\cdots11}_{k\text{ znamenaka}}\\
(n+1)_2 &= \cdots1\underbrace{00\cdots00}_{k\text{ znamenaka}}
\end{aligned}
$$

Dakle, pri računanju $g(n)$ i $g(n+1)$ zadnjih $k$ bitova poprima oblik $\displaystyle\underbrace{100\cdots00}_{k\text{ znamenaka}}$, a $k+1$-vi bit je različit, jer su $n$ i $n+1$ jednaki u svim bitovima osim zadnjih $k+1$. Stoga se $k+1$-vi bit u oba slučaja XOR-a s $1$ ili u oba slučaja s $0$. U oba je slučaja $k+1$-vi bit različit. Na bitovima izvan zadnjih $k+1$ provodi se ista operacija XOR, pa je rezultat isti.

Time je dokaz završen.

## Konstrukcija izvornog broja iz Grayeva koda (inverzna transformacija)

Razmotrimo sada inverznu transformaciju Grayeva koda: zadan je Grayev kod $g$, a treba pronaći izvorni broj $n$. Prolazimo od najvišeg bita binarnog zapisa prema najnižem (najniži bit ima indeks $1$, tj. to je bit jedinica; najviši bit ima indeks $k$). Tada je odnos između $i$-tog bita broja $n$ i $i$-tog bita $g_i$ koda $g$ sljedeći:

$$
\begin{aligned}
n_k &= g_k \\
n_{k-1} &= g_{k-1} \oplus n_k &&= g_k \oplus g_{k-1} \\
n_{k-2} &= g_{k-2} \oplus n_{k-1} &&= g_k \oplus g_{k-1} \oplus g_{k-2} \\
n_{k-3} &= g_{k-3} \oplus n_{k-2} &&= g_k \oplus g_{k-1} \oplus g_{k-2} \oplus g_{k-3} \\
&\vdots\\
n_{k-i} &=\displaystyle\bigoplus_{j=0}^ig_{k-j}
\end{aligned}
$$

```cpp
int rev_g(int g) {
  int n = 0;
  for (; g; g >>= 1) n ^= g;
  return n;
}
```

## Praktične primjene

Grayev kod ima nekoliko vrlo korisnih primjena, od kojih su neke neočekivane:

-   Niz Grayevih kodova $k$-bitnih binarnih brojeva može se promatrati kao Hamiltonov ciklus po vrhovima hiperkocke u $k$-dimenzionalnom prostoru (kvadrata u dvije dimenzije, jediničnog vektora u jednoj), pri čemu svaki bit Grayeva koda predstavlja koordinatu jedne dimenzije.

-   Grayev kod koristi se za smanjivanje pogrešaka u prijenosu signala digitalno-analognih pretvarača (npr. senzora), jer se svaki put mijenja samo jedan bit.

-   Grayev kod može se iskoristiti za rješavanje problema Hanojskih tornjeva.

    Neka je broj diskova $n$. Krećemo od $n$-bitnog Grayeva koda $G(0)$ sa svim znamenkama $0$ i redom prelazimo na sljedeći Grayev kod (s $G(i)$ na $G(i+1)$). $i$-ti bit trenutačnog Grayeva koda predstavlja $i$-ti disk po veličini od najmanjega.

    Budući da se svaki put mijenja samo jedan bit, kad se promijeni $i$-ti bit, pomičemo $i$-ti disk. Pri pomicanju diskova svaki disk osim najmanjega ima samo jedan mogući izbor kamo ga staviti. Pri pomicanju prvog diska uvijek imamo dva izbora. Stoga je naša strategija sljedeća:

    ako je $n$ neparan, put pomicanja diska je $f\to t\to r\to f\to t\to r\to\cdots$, gdje je $f$ početni štap, $t$ štap na koji na kraju stavljamo sve diskove, a $r$ srednji štap;

    ako je $n$ paran: $f \to r \to t \to f \to r \to t \to \cdots$

-   Grayev kod primjenjuje se i u teoriji genetskih algoritama.

## Zadaci

-   [CSP S2 2019 D1T1](https://www.luogu.com.cn/problem/P5657) težina: lako

-   [SGU #249 Matrix](http://codeforces.com/problemsets/acmsguru/problem/99999/249) težina: srednje

> Ova je stranica dijelom prevedena iz članka [Код Грея](http://e-maxx.ru/algo/gray_code) i njegova engleskog prijevoda [Gray code](https://cp-algorithms.com/algebra/gray-code.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.
