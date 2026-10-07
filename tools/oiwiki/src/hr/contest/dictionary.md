---
title: Tablice unaprijed izračunatih odgovora
---

Preduvjet: [Dekompozicija na blokove](../ds/decompose.md).

Naivno tabličenje (打表) znači da prije natjecanja ili tijekom njega izračunamo i spremimo odgovore za sve moguće ulaze, zatim u kodu otvorimo niz, stavimo odgovore u njega i izravno ih ispisujemo.

Ovaj se trik primjenjuje samo kad raspon ulaza nije velik (npr. ulaz je jedan broj malog raspona); inače kod može biti predugačak, dovesti do MLE-a ili bi računanje tablice trajalo predugo.

???+ note "Primjer"
    Neka je $f(x)$ broj jedinica u binarnom zapisu cijelog broja $x$. Za zadani prirodan broj $n$ ($n\leq 10^9$) ispiši $\sum_{i=1}^n f^2(i)$.

Kad bismo za svaki $n$ spremili odgovor, osim mogućeg MLE-a kod bi mogao premašiti najveću dopuštenu duljinu i ne bi se preveo.

Zato optimiramo tablicu odgovora. Idejom [dekompozicije na blokove](../ds/decompose.md) odaberemo razuman korak $m$ (obično ovisno o dopuštenoj duljini koda) i za $i$-ti blok izračunamo

$$
\sum_{k=\frac{n}{m}(i-1)+1}^{\frac{ni}{m}} f^2(k)
$$

Pri ispisu odgovora koristimo ideju blokova: cijele blokove računamo iz unaprijed izračunatih vrijednosti, a nepotpune blokove grubom silom.

Općenito, u takvim zadacima pojedina se vrijednost $f(x)$ računa brzo, ali treba zbrojiti (pomnožiti ili na neki brzo spojiv način kombinirati) jako puno vrijednosti funkcije, pa nabrajanje prelazi vremensko ograničenje. Ako ne nađemo standardno rješenje, tablica po blokovima je dobar izbor.

???+ note "Napomena"
    Ako u gornjem zadatku eksponent nije fiksan, ali ima mali raspon, tablica također dolazi u obzir.

### Zadaci

[「BZOJ 3798」特殊的质数](https://hydro.ac/p/bzoj-P3798): koliko prostih brojeva iz intervala $[l,r]$ se može prikazati kao zbroj kvadrata dvaju prirodnih brojeva.

[「Luogu P1822」魔法指纹](https://www.luogu.com.cn/problem/P1822)
