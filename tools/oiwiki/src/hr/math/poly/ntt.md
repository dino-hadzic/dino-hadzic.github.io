---
title: Brza teorijsko-brojevna transformacija
---

## Uvod

**Teorijsko-brojevna transformacija** (number-theoretic transform, NTT) implementacija je diskretne Fourierove transformacije (DFT) na teorijsko-brojevnoj osnovi; **brza teorijsko-brojevna transformacija** (fast number-theoretic transform, FNTT) implementacija je [brze Fourierove transformacije](./fft.md) (FFT) na teorijsko-brojevnoj osnovi.

**Teorijsko-brojevna transformacija** brz je algoritam za računanje konvolucije (convolution). Među najčešće korištene algoritme spada i već spomenuta brza Fourierova transformacija. Međutim, brza Fourierova transformacija ima neke implementacijske nedostatke: primjerice, vektor podataka mora se pomnožiti matricom s kompleksnim koeficijentima, a realni i imaginarni dio svakog kompleksnog koeficijenta vrijednosti su funkcija sinus i kosinus, pa je većina koeficijenata zapisana u pomičnom zarezu; drugim riječima, moraju se izvoditi kompleksne operacije, i to u pomičnom zarezu, zbog čega je količina računanja veća, a i pogreška nastala računanjem u pomičnom zarezu veća je.

NTT rješava slučaj množenja polinoma s modulom; može se reći da je donekle ograničena modulom, a i brojevi su veći. Trenutačno je najčešći modul 998244353.

## Predznanje

Za učenje teorijsko-brojevne transformacije potrebno je predznanje: diskretna Fourierova transformacija, generirane podgrupe, [primitivni korijen](../number-theory/primitive-root.md), diskretni logaritam. Ta se znanja mogu naučiti na odgovarajućim stranicama pa ih ovdje ne ponavljamo.

## Definicija

### Teorijsko-brojevna transformacija

U matematici je NTT diskretna Fourierova transformacija (DFT) nad proizvoljnim [prstenom](../algebra/basic.md#环). U slučaju konačnog polja obično se naziva teorijsko-brojevnom transformacijom (NTT).

**Teorijsko-brojevna transformacija** (NTT) dobiva se prenošenjem diskretne Fourierove transformacije u $F={\mathbb {Z}/p}$, cijele brojeve modulo prost broj $p$. To je **konačno polje**, i čim $n$ dijeli $p-1$, postoji primitivni $n$-ti korijen jedinice, pa imamo $p=\xi n+1$ za neki pozitivan cijeli broj $ξ$. Konkretno, za prost broj $p=qn+1, (n=2^m)$ primitivni korijen $g$ zadovoljava $g^{qn} \equiv 1 \pmod p$; promatramo li $g_n=g^q\pmod p$ kao ekvivalent od $\omega_n$, on zadovoljava slična svojstva, npr. $g_n^n \equiv 1 \pmod p, g_n^{n/2} \equiv -1 \pmod p$.

Budući da je ovdje riječ o teorijsko-brojevnoj transformaciji, $N$ (da bismo ga razlikovali od $n$ u FFT-u, ovdašnji $n$ zovemo $N$) može biti veći od $n$ u FFT-u, ali dovoljno je $\frac{qN}{n}$ promatrati kao ovdašnji $q$ i problem veličine je izbjegnut.

Uobičajeni su:

$$
p = 167772161 = 5 \times 2^{25}+1, g=3
$$

$$
p = 469762049 = 7 \times 2^{26}+1, g=3
$$

$$
p = 754974721 = 3^2 \times 5 \times 2^{24}+1, g=11
$$

$$
p = 998244353 = 7 \times 17 \times 2^{23}+1, g=3
$$

$$
p = 1004535809 = 479 \times 2^{21}+1, g=3
$$

Riječ je upravo o ekvivalentu $\mathrm{e}^{2\pi \mathrm{i} n}$ za $g^{qn}$.

Kad iteracija dođe do duljine $l$, vrijedi $g_l = g^{\frac{p-1}{l}}$, odnosno $\omega_n = g_l = g_N^{\frac{N}{l}} = g_N^{\frac{p-1}{l}}$.

## Brza teorijsko-brojevna transformacija

**Brza teorijsko-brojevna transformacija** (FNTT) brz je algoritam koji nastaje dodavanjem postupka „podijeli pa vladaj” teorijsko-brojevnoj transformaciji (NTT).

Postupak podjele koji koristi brza teorijsko-brojevna transformacija potpuno je jednak onom koji koristi brza Fourierova transformacija. To znači da je dovoljno jednostavno izmijeniti kod brze Fourierove transformacije da bi se dobio kod brze teorijsko-brojevne transformacije.

Pojam NTT koji se često spominje na algoritamskim natjecanjima zapravo se najčešće odnosi na brzu teorijsko-brojevnu transformaciju; obično se podrazumijeva da „teorijsko-brojevna transformacija” znači „brza teorijsko-brojevna transformacija”.

Logika te kratice slična je onoj kod brze Fourierove transformacije. Zapravo se pojam „brza Fourierova transformacija” (FFT) odnosi na „brzu diskretnu Fourierovu transformaciju” (FDFT), ali budući da se „brza” može odnositi samo na diskretnu, štoviše samo na poseban slučaj u kojem je red primitivnog korijena jedinice potencija broja $2$, a ne može na kontinuiranu, riječ „diskretna” se izostavlja, FDFT postaje FFT, tj. FFT se uvijek odnosi na poseban diskretni slučaj.

Teorijsko-brojevna transformacija, odnosno brza teorijsko-brojevna transformacija, operacija je koja se izvodi modulo neki broj; kontinuirani slučaj ne postoji, uvijek je diskretna, pa naravno nema potrebe spominjati riječ „diskretna”.

U području algoritama operacije bez ubrzanja nemaju smisla. Pojam DFT uveden je kod brze Fourierove transformacije zato što DFT ima i druge konkretne primjene u obradi signala i obradi slika, a ujedno je DFT načelo, odnosno predznanje, za FFT.

Kad ne dovodi do zabune, NTT se često koristi kao oznaka za FNTT. Da u daljnjem izlaganju ne bi došlo do zabune, u nastavku su pojmovi NTT i FNTT razdvojeni.

Konkretan odnos DFT-a, FFT-a, NTT-a i FNTT-a jest:

-   Dodavanjem postupka podjele DFT-u i NTT-u dobivaju se FFT i FNTT. Postupak i načelo podjele mogu se vidjeti u članku o brzoj Fourierovoj transformaciji.

-   Zamjenom kompleksnog zbrajanja i kompleksnog množenja u DFT-u i FFT-u zbrajanjem i množenjem modulo $p$, pri čemu se veličine obično ograničavaju na raspon od $0$ do $p-1$, te zamjenom primitivnog korijena jedinice primitivnim korijenom jedinice istog reda modulo $p$, gdje je red potencija broja $2$, dobivaju se NTT i FNTT.

Budući da zamijenjene operacije uključuju samo zbrajanje i množenje, DFT, FFT, NTT i FNTT imaju isto načelo; svi se izvode nad prstenom koji ima zbrajanje i množenje, bez strožeg uvjeta polja da mora biti definirano i dijeljenje.

Zapravo, čim postoji primitivni korijen, tj. generator u smislu teorije grupa, NTT ili FNTT za taj modul može se provesti. Budući da su moduli $1$, $2$ i $4$ premali da bi imali praktično značenje, za neparan prost broj $p$ i pozitivan cijeli broj $\alpha$ dovoljno je zadati primitivni korijen $g$ za module $p^\alpha$ i $2p^\alpha$ te se na isti način NTT ili FNTT i dalje može provesti.

## Predložak

??? example "[Library Checker - Convolution](https://judge.yosupo.jp/problem/convolution_mod)"
    ```cpp
    --8<-- "docs/math/code/poly/ntt/ntt_1.cpp"
    ```

## Literatura i daljnje čitanje

1.  [FWT（快速沃尔什变换）零基础详解 qaq（ACM/OI）(Detaljno objašnjenje FWT-a (brze Walsh–Hadamardove transformacije) od nule (ACM/OI))](https://zhuanlan.zhihu.com/p/41867199)
2.  [FFT（快速傅里叶变换）0 基础详解！附 NTT（ACM/OI）(Detaljno objašnjenje FFT-a (brze Fourierove transformacije) od nule, s dodatkom o NTT-u (ACM/OI))](https://zhuanlan.zhihu.com/p/40505277)
3.  [Number-theoretic transform(NTT) - Wikipedia](https://en.wikipedia.org/wiki/Discrete_Fourier_transform_%28general%29#Number-theoretic_transform)
4.  [Tutorial on FFT/NTT—The tough made simple. (Part 1)](https://codeforces.com/blog/entry/43499)
5.  [NTT 模板 - BlackJack\_ CSDN 博客 (Predložak NTT-a – blog BlackJack\_ na CSDN-u)](https://blog.csdn.net/blackjack_/article/details/79346433)
