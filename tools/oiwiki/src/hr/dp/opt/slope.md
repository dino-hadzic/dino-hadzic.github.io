---
title: Optimizacija nagibom
---

## Uvodni primjer

???+ note "[„HNOI2008” Pakiranje igračaka](https://loj.ac/problem/10188)"
    U redu je $n$ igračaka, $i$-ta igračka ima vrijednost $c_i$. Tih $n$ igračaka treba podijeliti na nekoliko segmenata. Cijena segmenta $[l,r]$ je $(r-l+\sum_{i=l}^r c_i-L)^2$, gdje je $L$ konstanta. Odredite najmanju ukupnu cijenu podjele.
    
    $1\le n\le 5\times 10^4, 1\le L, c_i\le 10^7$.

### Naivno DP rješenje

Neka $f_i$ označava najmanju cijenu podjele prvih $i$ predmeta na nekoliko segmenata.

Jednadžba prijelaza stanja: $f_i=\min_{j<i}\{f_j+(i-(j+1)+pre_i-pre_j-L)^2\}=\min_{j<i}\{f_j+(pre_i-pre_j+i-j-1-L)^2\}$.

Ovdje $pre_i$ označava zbroj prvih $i$ brojeva, tj. $\sum_{j=1}^i c_j$.

Vremenska složenost ovog pristupa je $O(n^2)$, što nije dovoljno za ovaj zadatak.

### Optimizacija

Pojednostavnimo gornju jednadžbu prijelaza stanja: neka je $s_i=pre_i+i,L'=L+1$; tada je $f_i=\min_{j<i}\{f_j+(s_i-s_j-L')^2\}$.

Prebacimo li članove koji ne ovise o $j$ van, dobivamo

$$
f_i - (s_i-L')^2=\min_{j<i}\{f_j+s_j^2 + 2s_j(L'-s_i) \} 
$$

Promotrimo eksplicitni oblik pravca $y=kx+b$ i prebacimo članove: $b=y-kx$. Informaciju koja ovisi o $j$ zapisujemo kao $y$, informaciju koja ovisi i o $i$ i o $j$ kao $kx$, a ono što minimiziramo (informaciju koja ovisi o $i$) kao $b$, odnosno odsječak na osi $y$. Konkretno, neka je

$$
\begin{aligned}
x_j&=s_j\\
y_j&=f_j+s_j^2\\
k_i&=-2(L'-s_i)\\
b_i&=f_i-(s_i-L')^2\\
\end{aligned}
$$

Tada se jednadžba prijelaza zapisuje kao $b_i = \min_{j<i}\{ y_j-k_ix_j \}$. Promatramo li $(x_j,y_j)$ kao točke u ravnini, $k_i$ je nagib pravca, a $b_i$ odsječak pravca nagiba $k_i$ koji prolazi točkom $(x_j,y_j)$. Zadatak se sveo na odabir prikladnog $j$ ($1\le j<i$) koji minimizira odsječak pravca.

![slope\_optimization](../images/optimization.svg)

Kao na slici, pravac nagiba $k_i$ translatiramo odozdo prema gore dok neka točka $(x_p,y_p)$ ne legne na njega; tada je $b_i=y_p-k_ix_p$ i $b_i$ postiže minimum. Nakon što izračunamo $f_i$, točku $(x_i,y_i)$ dodajemo u skup točaka kao novu DP odluku. Kako onda održavati skup točaka?

Lako je uočiti da točka u kojoj $b_i$ može postići minimum nužno leži na donjoj konveksnoj ljusci. Zato pri traženju $p$ ne moramo enumerirati svih $i-1$ točaka, nego samo točke na konveksnoj ljusci. U ovom zadatku $k_i$ raste s porastom $i$, pa konveksnu ljusku možemo održavati monotonim redom.

Konkretno, neka $K(a,b)$ označava nagib pravca kroz $(x_a,y_a)$ i $(x_b,y_b)$. Promotrimo red $q_l,q_{l+1},\ldots,q_r$ koji održava točke donje konveksne ljuske. Drugim riječima, za $l<i<r$ uvijek vrijedi $K(q_{i-1},q_i) < K(q_i,q_{i+1})$.

Održavamo pokazivač $e$ kojim računamo minimum $b_i$. Trebamo pronaći $e$ takav da je $K(q_{e-1},q_e)\le k_i< K(q_e,q_{e+1})$ (slučajevi $e=l$ i $e=r$ zahtijevaju posebnu provjeru); tada je $p=q_e$, tj. $q_e$ je optimalna odluka za $i$. Budući da je $k_i$ monotono rastuć, broj pomaka pokazivača $e$ je amortizirano $O(1)$.

Pri umetanju točke $(x_i,y_i)$ provjeravamo vrijedi li $K(q_{r-1},q_r)<K(q_r,i)$; ako nejednakost ne vrijedi, izbacujemo $q_r$, sve dok ne bude zadovoljena. Zatim $i$ umećemo na kraj reda $q$.

Time smo složenost DP-a optimizirali na $O(n)$.

Sažmimo algoritam za gornji ogledni zadatak optimizacije nagibom:

1.  Stavi početno stanje u red.
2.  Svaki put pravcem $f(i)$ povezanim s $i$ „presijeci” održavanu konveksnu ljusku, pronađi optimalnu odluku i ažuriraj $dp_i$.
3.  Dodaj stanje $dp_i$. Ako neko stanje (tj. točka na konveksnoj ljusci) nakon dodavanja $dp_i$ više nije na ljusci, treba ga ukloniti prije dodavanja $dp_i$.

U nastavku predstavljamo naprednije primjene optimizacije nagibom, u kojima se ona kombinira s binarnim pretraživanjem/podjelom/strukturama podataka kako bi se održavale DP jednadžbe s lošijim svojstvima (bez nekih svojstava monotonosti).

## Optimizacija DP-a binarnim pretraživanjem/CDQ-om/balansiranim stablom

Kad u točki $i$ tražimo optimalnu odluku, pravcem $f(i)$ povezanim s $i$ presijecamo održavanu konveksnu ljusku. Pogođena točka je optimalna odluka.

U gornjem primjeru nagib pravca mijenja se monotono s $i$, ali u nekim zadacima nagib nije monoton. Tada moramo održavati svaki čvor konveksne ljuske i svaki put presjeći ljusku trenutnim pravcem. Taj se postupak može izvesti binarnim pretraživanjem, jer su nagibi između susjednih točaka konveksne ljuske monotoni.

???+ note "Pakiranje igračaka, izmijenjeno"
    U redu je $n$ igračaka, $i$-ta igračka ima vrijednost $c_i$. Tih $n$ igračaka treba podijeliti na nekoliko segmenata. Cijena segmenta $[l,r]$ je $(r-l+\sum_{i=l}^r c_i-L)^2$, gdje je $L$ konstanta. Odredite najmanju ukupnu cijenu podjele.
    
    $1\le n\le 5\times 10^4,1\le L\le 10^7,-10^7\le c_i\le 10^7$.

Jedina razlika u odnosu na zadatak „Pakiranje igračaka” jest da vrijednosti igračaka mogu biti negativne. Nastavljajući prijašnju ideju, neka $f_i$ označava najmanju cijenu podjele prvih $i$ predmeta na nekoliko segmenata.

Jednadžba prijelaza stanja: $f_i=\min_{j<i}\{f_j+(pre_i-pre_j+i-j-1-L)^2\}$.

Ovdje je $pre_i = \sum_{j=1}^i c_j$.

Istom transformacijom jednadžbe dobivamo

$$
f_i - (s_i-L')^2=\min_{j<i}\{f_j+s_j^2 + 2s_j(L'-s_i) \} 
$$

No sada dva uvjeta više ne vrijede:

1.  nagib pravca više nije monoton;
2.  apscise točaka odluka koje dodajemo više nisu monotone.

I dalje razmatramo održavanje konveksne ljuske.

Pri traženju optimalne odluke, tj. pri presijecanju ljuske pravcem, umjesto traženja početka monotonog reda koristimo: binarno pretraživanje na ljusci. Binarnim pretraživanjem nalazimo brid ljuske čiji je nagib najbliži nagibu pravca i time dobivamo optimalnu odluku.

Pri dodavanju točke odluke, tj. pri dodavanju točke na ljusku, imamo dva načina održavanja.

Prvi je način izravno održavati ljusku balansiranim stablom. Tada binarno pretraživanje odluke postaje binarno pretraživanje po balansiranom stablu, a umetanje točke odluke postaje umetanje čvora u balansirano stablo uz brisanje nekoliko točaka izbačenih iz ljuske. Ideja je jednostavna, ali je implementacija zamorna.

U nastavku predstavljamo pristup temeljen na [CDQ podjeli](../../misc/cdq-divide.md).

Neka $\text{CDQ}(l,r)$ označava izračun $f_i,i\in [l,r]$. Promotrimo $\text{CDQ}(1,n)$:

-   Najprije pozovemo $\text{CDQ}(1,mid)$ i izračunamo $f_i,i\in[1,mid]$. Zatim od točaka odluka iz intervala $[1,mid]$ izgradimo konveksnu ljusku i njome ažuriramo $f_i,i\in [mid+1,n]$. Skup točaka odluka sada je fiksan, ne dodajemo točke tijekom računanja DP vrijednosti kao prije, pa $f_i$ za $i \in [mid+1,n]$ možemo najprije sortirati po nagibu pravca $k_i$ i zatim DP vrijednosti računati monotonim redom. Naravno, DP vrijednosti možemo računati i binarnim pretraživanjem na statičkoj ljusci.

-   Za svaku točku iz $[mid+1,n]$ čija optimalna odluka leži u intervalu $[1,mid]$ ovaj korak postavlja optimalni odgovor. Nakon tog koraka sve točke iz $[1,mid]$ odigrale su svoju ulogu i njihova prisutnost u ljusci više ne utječe na kasnija ažuriranja. Zato točke odluka iz tog intervala možemo jednostavno odbaciti i preostali dio desnog intervala riješiti pozivom $\text{CDQ}(mid+1,n)$.

Vremenska složenost je $O(n\log^2 n)$.

Usporedbom zadataka „Pakiranje igračaka” i „Pakiranje igračaka, izmijenjeno” možemo zaključiti sljedeće:

-   Binarno pretraživanje/CDQ/balansirano stablo i slično mogu optimizirati izračun DP jednadžbe i do neke mjere smanjiti složenost, ali ne mogu promijeniti samu jednadžbu.
-   Svojstva DP jednadžbe ovise o značajkama ulaznih podataka, ali sama DP jednadžba ovisi o matematičkom modelu zadatka.

## Sažetak

Optimizaciju nagibom treba primjenjivati fleksibilno; njezina je bit svesti optimizacijski problem na problem minimuma/maksimuma odsječka na osi u ravnini, povezan s konveksnom ljuskom. Kod jednadžbi s lošijim svojstvima ponekad je potrebno pomoći se strukturama podataka, a to ovisi o konkretnom zadatku.

## Zadaci

-   [„SDOI2016” Pohod](https://loj.ac/problem/2035)
-   [„ZJOI2007” Gradnja skladišta](https://loj.ac/problem/10189)
-   [„APIO2010” Specijalna postrojba](https://loj.ac/problem/10190)
-   [„JSOI2011” Limun](https://www.luogu.com.cn/problem/P5504)
-   [„Codeforces 311B” Cats Transport](http://codeforces.com/problemset/problem/311/B)
-   [„NOI2007” Mjenjačnica](https://loj.ac/problem/2353)
-   [„NOI2019” Put kući](https://loj.ac/problem/3156)
-   [„NOI2016” Kralj pije vodu](https://uoj.ac/problem/223)
-   [„NOI2014” Kupnja karata](https://uoj.ac/problem/7)
