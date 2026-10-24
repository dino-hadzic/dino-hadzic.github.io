---
title: Kahanovo zbrajanje
---

## Uvod

Algoritam **Kahanova zbrajanja** (Kahan summation), poznat i kao kompenzirano zbrajanje ili zbrajanje s prijenosom, algoritam je za **smanjenje pogreške pri akumuliranju zbroja niza brojeva s pomičnim zarezom konačne preciznosti**. Postiže to uglavnom tako da u zasebnoj varijabli (obično nazvanoj $c$) akumulira pogrešku.

Algoritam je 1960-ih otkrio uglavnom William Kahan. Budući da je sličan algoritam neovisno predložio i Ivo Babuška, Kahanovo se zbrajanje naziva i Kahan–Babuškino zbrajanje.

## Pogreška zaokruživanja

U računalnim programima realne brojeve moramo približno prikazivati konačnim brojem znamenaka; većina današnjih računala za taj približni prikaz koristi brojeve s pomičnim zarezom propisane standardom [IEEE-754](https://en.wikipedia.org/wiki/IEEE_754). Broj $\frac{1}{3}$ ne možemo točno prikazati konačnim brojem znamenaka, pa se pri zapisu po IEEE-754 dio vrijednosti mora zaokružiti (odrezati, truncate). Ta je **pogreška zaokruživanja** (rounding off error) svojstvo računanja s pomičnim zarezom.

Pri zbrajanju brojeva s pomičnim zarezom vrijedi komutativnost (commutativity), ali ne i asocijativnost (associativity). Drugim riječima, $a+b = b+a$, ali $(a+b)+c \neq a+(b+c)$. Zato pri zbrajanju niza brojeva s pomičnim zarezom možemo zbrajati jedan po jedan slijeva nadesno, a možemo ih i, zadržavajući izvorni redoslijed, grupirati u parove. Drugi je postupak razmjerno sporiji i treba više memorije, a često ga koriste posebne funkcije za zbrajanje u nekim jezicima, ali daje razmjerno točniji rezultat.

Da bismo dobili točniji rezultat zbrajanja brojeva s pomičnim zarezom, trebamo algoritam Kahanova zbrajanja.

Pri računanju $S_{new}=S_{old}+a$ ($a$ je jedan broj iz niza brojeva s pomičnim zarezom) definiramo vrijednost koja je stvarno dodana u $S$ kao $a_{eff}=S_{new}-S_{old}$; ako je $a_{eff}$ veći od $a$, došlo je do zaokruživanja prema gore, a ako je $a_{eff}$ manji od $a$, došlo je do zaokruživanja prema dolje. Pogreška zaokruživanja definira se kao $E_{roundoff} = a_{eff} - a$. Vrijednost kojom se ta pogreška zaokruživanja ispravlja tada je $a-a_{eff}$, tj. negativna vrijednost od $E_{roundoff}$. Ako je $c$ varijabla koja kompenzira izgubljene niže znamenke, dobivamo $c_{new} = c_{old} + (a - a_{eff})$.

## Postupak

Algoritam Kahanova zbrajanja pogrešku akumulira u zasebnoj varijabli. Kao što pokazuje referentni kod u nastavku, $sum$ je konačni rezultat zbrajanja koji se vraća. $c$ je varijabla koja kompenzira izgubljene niže znamenke (dio koji je odbačen) i nužna je varijabla algoritma Kahanova zbrajanja.

Budući da je $sum$ velik, a $y$ malen, niže se znamenke od $y$ gube. $(t - sum)$ poništava viši dio od $y$, a oduzimanjem $y$ dobiva se negativna vrijednost (niži dio od $y$). Zato je algebarski $c$ uvijek nula. U sljedećoj iteraciji izgubljeni se niži dio pribraja u $y$.

## Implementacija

??? note "Referentni kod"
    ```cpp
    float kahanSum(vector<float> nums) {
      float sum = 0.0f;
      float c = 0.0f;
      for (auto num : nums) {
        float y = num - c;
        float t = sum + y;
        c = (t - sum) - y;
        sum = t;
      }
      return sum;
    }
    ```

## Zadaci za vježbu

U OI-ju Kahanovo zbrajanje postoji uglavnom kao pomoćni alat koji rezultatu računanja daje manju pogrešku.

???+ note "Primjer [CodeForces Contest 800 Problem A. Voltage Keepsake](https://codeforces.com/contest/800/problem/A)"
    Postoji $n$ uređaja koji se koriste istodobno. $i$-ti uređaj troši $a_{i}$ jedinica energije u sekundi. Potrošnja je kontinuirana, tj. u $\lambda$ sekundi uređaj potroši $\lambda \times a_{i}$ jedinica energije. $i$-ti uređaj trenutačno ima pohranjeno $b_{i}$ jedinica energije. Svi uređaji mogu pohraniti proizvoljnu količinu energije. Postoji jedan punjač koji se može priključiti na bilo koji pojedini uređaj. Punjač uređaju dodaje $p$ jedinica energije u sekundi. Punjenje je kontinuirano, tj. ako je uređaj priključen $\lambda$ sekundi, dobit će $\lambda \times p$ jedinica energije. Uređaj koji se puni možemo promijeniti u bilo kojem trenutku (uključujući realne trenutke; vrijeme prebacivanja zanemarujemo). Odredite koliko se najdulje uređaji mogu koristiti prije nego što energija nekog od njih padne na $0$ jedinica.

???+ note "Primjer [CodeForces Contest 504 Problem B. Misha and Permutations Summation](https://codeforces.com/problemset/problem/504/B)"
    Zbroj dviju permutacija $p$ i $q$ brojeva $0, 1, \cdots, (n - 1)$ definiran je kao $Perm((Ord(p)+Ord(q))\bmod n!)$, gdje je $Perm(x)$ $x$-ta permutacija brojeva $0, 1, \cdots, (n-1)$ u leksikografskom poretku (brojeći od nule), a $Ord(p)$ je broj permutacija koje su leksikografski manje od $p$. Na primjer, $Perm(0) = (0, 1, \cdots , n - 2, n - 1)$, $Perm(n! - 1) = (n - 1, n-2,\cdots, 1,0))$. Misha ima dvije permutacije $p$ i $q$; odredite njihov zbroj.

## Zbrajanje u programskim jezicima

Standardna biblioteka Pythona propisuje funkciju [fsum](https://docs.python.org/3/library/math.html#math.fsum) za točno zaokruženo zbrajanje, kojom se može dobiti točan zbroj vrijednosti s pomičnim zarezom iz iterabilnog objekta; gubitak preciznosti izbjegava Shewchukovim algoritmom, prateći više međuzbrojeva.

U jeziku Julia zadana implementacija funkcije [sum](https://docs.julialang.org/en/v1/base/collections/#Base.sum) jest zbrajanje u parovima, radi visoke točnosti i dobrih performansi. Istodobno funkcija vanjske biblioteke [sum\_kbn](http://www.jlhub.com/julia/manual/en/function/sum_kbn) nudi implementaciju Neumaierove varijante za slučajeve u kojima je potrebna veća točnost; vidi [KahanSummation.jl](https://github.com/JuliaMath/KahanSummation.jl).

## Literatura i bilješke

1.  [Kahan\_summation\_algorithm - Wikipedia](https://en.wikipedia.org/wiki/Kahan_summation_algorithm)
2.  [Kahan summation - Rosetta Code](https://rosettacode.org/wiki/Kahan_summation)
3.  [VK Cup Round 2 + Codeforces Round 409 Announcement](https://codeforces.com/blog/entry/51577)
4.  [Rounding off errors in Java - GeeksforGeeks](https://www.geeksforgeeks.org/rounding-off-errors-java/)
