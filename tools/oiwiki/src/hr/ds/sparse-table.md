---
title: ST tablica
---

## Definicija

![Shema ST tablice](images/st.svg)

ST tablica (Sparse Table, rijetka tablica) struktura je podataka za rješavanje **problema s ponovljivim doprinosom**.

???+ note "Što je problem s ponovljivim doprinosom?"
    **Problem s ponovljivim doprinosom** (idempotentna operacija) jest intervalni upit za operaciju $\operatorname{opt}$ koja zadovoljava $x\operatorname{opt} x=x$. Primjerice, za maksimum vrijedi $\max(x,x)=x$, a za gcd vrijedi $\operatorname{gcd}(x,x)=x$, pa su RMQ i intervalni GCD problemi s ponovljivim doprinosom. Zbroj na intervalu nema to svojstvo: ako se pri računanju zbroja intervala predobrađeni intervali preklapaju, preklopljeni se dio zbroji dvaput, što ne želimo. Osim toga, $\operatorname{opt}$ mora biti i asocijativna da bi se mogla rješavati ST tablicom.

???+ note "Što je RMQ?"
    RMQ je kratica za engleski Range Maximum/Minimum Query i označava maksimum (minimum) na intervalu. Postoji mnogo načina rješavanja problema RMQ; vidi [poglavlje o RMQ-u](../topic/rmq.md).

## Uvod

???+ example "[Luogu P3865【模板】ST 表 & RMQ 问题](https://www.luogu.com.cn/problem/P3865)"
    Zadano je $n$ ($1\le n\le 10^5$) cijelih brojeva i $m$ ($1\le m\le 2\times 10^6$) upita; za svaki upit treba odgovoriti koliki je maksimum na intervalu $[l,r]$.

Razmotrimo grubo rješenje. Za svaki upit prođemo interval $[l,r]$ i nađemo maksimum.

Očito će taj algoritam premašiti vremensko ograničenje.

## ST tablica

ST tablica temelji se na ideji [binary liftinga](../basic/binary-lifting.md); omogućuje predobradu u $\Theta(n\log n)$ i odgovor na svaki upit u $\Theta(1)$. Ne podržava izmjene.

Na temelju ideje binary liftinga razmislimo kako izračunati maksimum na intervalu. Vidimo da, ako slijedimo uobičajeni postupak binary liftinga i svaki put skačemo $2^i$ koraka, složenost upita ostaje $\Theta(\log n)$, što nije bolje od segment treea, a korak predobrade čak je sporiji od segment treea.

Primjećujemo da je $\max(x,x)=x$, tj. maksimum na intervalu problem je sa svojstvom „ponovljivog doprinosa”. Čak i ako se predobrađeni intervali kojima računamo preklapaju, odgovor je ispravan dok god je njihova unija upravo traženi interval.

Ako to ručno simuliramo, vidimo da upitni interval možemo pokriti s najviše dva predobrađena intervala, tj. vremenska složenost upita može se spustiti na $\Theta(1)$, što je vrlo učinkovito u zadacima s velikim brojem upita.

Konkretna implementacija:

Neka $f(i,j)$ označava maksimum na intervalu $[i,i+2^j-1]$.

Očito je $f(i,0)=a_i$.

Prema definiciji, druga dimenzija odgovara „skoku od $2^j-1$ koraka” u binary liftingu; slijedeći tu ideju, zapisujemo prijelaz stanja: $f(i,j)=\max(f(i,j-1),f(i+2^{j-1},j-1))$.

![](./images/st-preprocess-lift.svg)

To je bio dio s predobradom. Upit se može jednostavno izvesti ovako:

Za svaki upit $[l,r]$ podijelimo ga na dva dijela: $[l,l+2^s-1]$ i $[r-2^s+1,r]$, gdje je $s=\left\lfloor\log_2(r-l+1)\right\rfloor$. Maksimum rezultata tih dvaju dijelova je odgovor.

![Postupak upita u ST tablici](./images/st-query.svg)

Prema gornjem razmatranju o „problemima s ponovljivim doprinosom”, budući da je maksimum „problem s ponovljivim doprinosom”, preklapanje ne utječe na maksimum intervala. A kako ta dva intervala potpuno pokrivaju $[l,r]$, odgovor je zajamčeno ispravan.

???+ example "[Luogu P3865【模板】ST 表 & RMQ 问题](https://www.luogu.com.cn/problem/P3865) – referentna implementacija"
    === "C stil"
        ```cpp
        --8<-- "docs/ds/code/sparse-table/sparse-table_1.cpp"
        ```
    
    === "C++ stil"
        ```cpp
        --8<-- "docs/ds/code/sparse-table/sparse-table_2.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/sparse-table/sparse-table_1.py"
        ```

## Napomene

1.  Ulaznih i izlaznih podataka obično je mnogo, pa se preporučuje uključiti optimizaciju ulaza i izlaza.

2.  Pri predobradi ST tablice obično treba napraviti niz čija je jedna dimenzija veličine $\log n$, a druga veličine $n$; tada dimenziju veličine $\log n$ treba staviti kao prvu, radi bolje lokalnosti priručne memorije (cache).

3.  Ne isplati se svaki put iznova računati logaritam pomoću [std::log](https://en.cppreference.com/w/cpp/numeric/math/log); preporučuje se računati ga ugrađenim funkcijama poput `__builtin_clz` ili `__lg`. Ako te ugrađene funkcije nisu dostupne, vrijednosti logaritma mogu se i predobraditi. Predobrada izgleda ovako:

$$
\begin{cases}
\texttt{Logn}[1] \gets 0, \\
\texttt{Logn}\left[i\right] \gets \texttt{Logn}\left[\frac{i}{2}\right] + 1.
\end{cases}
$$

## ST tablica za druge informacije

Osim RMQ-a postoje i drugi „problemi s ponovljivim doprinosom”. Primjerice „bitovni AND na intervalu”, „bitovni OR na intervalu” i „GCD na intervalu” – sve to ST tablica rješava učinkovito.

Treba napomenuti da za „GCD na intervalu” složenost upita ST tablicom nije bolja od segment treea (uz raspon vrijednosti $w$, složenost upita ST tablicom je $\Theta(\log w)$, a segment treeom $\Theta(\log n+\log w)$, pri čemu je raspon vrijednosti obično veći od $n$), ali ni složenost predobrade ST tablice nije lošija od segment treea, a programerski je ST tablica mnogo jednostavnija od segment treea.

Ako analiziramo, „problemi s ponovljivim doprinosom” obično u sebi nose nekakvu komponentu nalik RMQ-u. Primjerice, „bitovni AND na intervalu” jest minimum po svakom bitu, a „GCD na intervalu” jest minimum eksponenta svakog prostog faktora.

## Sažetak

ST tablica dobro održava intervalne informacije s „ponovljivim doprinosom” (koje ujedno moraju biti asocijativne), ima nisku vremensku složenost i vrlo malo koda u usporedbi s drugim algoritmima. Međutim, informacije koje ST tablica može održavati vrlo su ograničene, teško se proširuje i ne podržava izmjene.

## Zadaci za vježbu

-   [„SCOI2007” 降雨量](https://loj.ac/p/2279)

-   [\[USACO07JAN\] Balanced Lineup](https://www.luogu.com.cn/problem/P2880)

## Dodatak: analiza vremenske složenosti ST tablice za GCD na intervalu

Tijekom izvođenja algoritma može proći $\Theta(\log n)$ iteracija. Svaka iteracija može rekurzivno pozivati funkciju GCD; uz raspon vrijednosti $w$, vremenska složenost funkcije GCD najviše je $\Omega(\log w)$, pa se čini da je ukupna složenost $O(n\log n\log w)$.

Međutim, u postupku GCD-a svaka rekurzija (osim posljednje) barem prepolovi neki broj u nizu, a brojevi u nizu mogu se prepoloviti najviše $\log_2 (w^n)=\Theta(n\log w)$ puta, pa se rekurzivni dio GCD-a izvodi najviše $O(n\log w)$ puta. Kad se tome doda $\Theta(n\log n)$ za petlje (i posljednju razinu rekurzije), konačna je složenost $O(n(\log w+\log n))$; budući da se mogu konstruirati podaci na kojima je složenost $\Omega(n(\log w+\log n))$, konačna je složenost $\Theta(n(\log w+\log n))$.

Složenost upita lako se analizira: u najgorem slučaju, kad svaki upit pita za najgori par brojeva, složenost je $\Theta(\log w)$. Stoga je složenost ST tablice za „GCD na intervalu” $\Theta(n(\log n+\log w))$ za predobradu i $\Theta(\log w)$ po upitu.

Odgovarajuće operacije segment treea imaju predobradu $\Theta(n\log w)$ i upit $\Theta(\log n+\log w)$.

Ovo nije strog matematički dokaz; stroži dokaz slijedi:

??? note "Stroži dokaz"
    Za razumijevanje ovog odjeljka možda je potrebno znanje o „metodi potencijala” iz poglavlja [Vremenska složenost](../basic/complexity.md).
    
    Najprije analizirajmo složenost predobrade:
    
    Neka je „promatrani niz” niz trenutne razine petlje pri predobradi ST tablice. Primjerice, niz nulte razine je izvorni niz, a niz prve razine je niz nulte razine nakon jedne iteracije, tj. `st[1..n][1]`; označimo ga s $A$.
    
    Funkciju potencijala definiramo kao logaritam po bazi dva umnoška svih brojeva u „promatranom nizu”, tj. $\Phi(A)=\log_2\left(\prod\limits_{i=1}^n A_i\right)$.
    
    U jednoj iteraciji utrošeno vrijeme jednako je zbroju vremena petlje i vremena GCD-a. Pritom vrijeme GCD-a varira: najkraće može biti samo dvije ili čak jedna rekurzija, a najdulje $O(\log w)$ rekurzija. No u postupku GCD-a, osim prve i posljednje razine, svaka rekurzija barem prepolovi neki rezultat u „promatranom nizu”. Dakle, $\Phi(A)$ se smanji barem za $1$, pa se vrijeme te razine rekurzije može amortizirati funkcijom potencijala.
    
    Istodobno vidimo da je početna vrijednost $\Phi(A)$ najviše $\log_2 (w^n)=\Theta(n\log w)$, a $\Phi(A)$ ne raste. Stoga je složenost predobrade ST tablice $O(n(\log w+\log n))$.
