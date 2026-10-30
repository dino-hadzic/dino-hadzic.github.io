---
title: Pellova jednadžba
---

Preduvjeti: [Verižni razlomci](./continued-fraction.md), [Kvadratna polja](./quadratic.md)

## Uvod

U ovom članku razmatramo rješavanje (poopćene) Pellove jednadžbe. Poopćena Pellova jednadžba je diofantska jednadžba po $x$ i $y$ oblika

$$
x^2-Dy^2=N,
$$

gdje je $D$ pozitivan cijeli broj koji nije potpun kvadrat[^not-square], a $N$ je cijeli broj različit od nule. Pellova jednadžba u užem smislu odnosi se na poseban slučaj $N=1$ ili $N=\pm 1$, a ponekad obuhvaća i slučaj $N=\pm 4$. Poopćena Pellova jednadžba usko je povezana s traženjem kvadratnih cijelih brojeva norme $N$ u prstenu realnih kvadratnih cijelih brojeva, a slučajevi koji se obično nazivaju Pellovom jednadžbom (u užem smislu) mogu se shvatiti kao traženje jedinica u prstenu realnih kvadratnih cijelih brojeva.

Kad se u ovom članku spominje Pellova jednadžba, misli se upravo na slučaj $N=1$. Slučaj $N=-1$ naziva se u skladu s time negativna Pellova jednadžba[^neg-pell] (negative Pell's equation).

## Struktura rješenja

Cjelobrojna rješenja $(x,y)$ poopćene Pellove jednadžbe usko su povezana s kvadratnim cijelim brojem $x+y\sqrt{D}$, pa se u literaturi rješenja Pellove jednadžbe često zapisuju u obliku $x+y\sqrt{D}$. Budući da je norma kvadratnog cijelog broja

$$
N(x+y\sqrt{D}) = x^2-Dy^2,
$$

poopćena Pellova jednadžba otprilike odgovara traženju kvadratnih cijelih brojeva norme $N$. Ipak, između tih dvaju pojmova postoji suptilna razlika. Kad su $x$ i $y$ oba cijeli brojevi, $x+y\sqrt{D}$ je sigurno kvadratni cijeli broj; obratno, kvadratni cijeli broj ne zahtijeva nužno da $x$ i $y$ budu cijeli brojevi — u slučaju $D\equiv 1\pmod 4$, $x$ i $y$ mogu istodobno biti i polucijeli brojevi[^half-int].

Ta je razlika osobito važna pri traženju fundamentalne jedinice. Naime, jedinice u prstenu kvadratnih cijelih brojeva su kvadratni cijeli brojevi norme $\pm 1$. Za $D\equiv 2,3\pmod 4$, da bismo našli takve jedinice, dovoljno je riješiti poopćenu Pellovu jednadžbu za $N=\pm 1$; no za $D\equiv 1\pmod 4$ treba razmotriti i slučaj $N=\pm 4$. Postupak traženja jedinica razmatra se [u nastavku](#slučaj-norme-4).

Da bismo razumjeli strukturu rješenja poopćene Pellove jednadžbe, krećemo od [Brahmaguptina identiteta](https://en.wikipedia.org/wiki/Brahmagupta%27s_identity):

$$
(x_1^2-Dy_1^2)(x_2^2-Dy_2^2)=(x_1x_2+Dy_1y_2)^2-D(x_1y_2+x_2y_1)^2.
$$

On odgovara činjenici da norma kvadratnih cijelih brojeva čuva množenje, tj.

$$
\begin{aligned}
N\left(x_1+y_1\sqrt{D}\right)N\left(x_2+y_2\sqrt{D}\right) &= N\left((x_1+y_1\sqrt{D})(x_2+y_2\sqrt{D})\right) \\
&= N\left((x_1x_2+Dy_1y_2)+(x_1y_2+x_2y_1)\sqrt{D}\right).
\end{aligned}
$$

Pomoću tog identiteta iz cjelobrojnih rješenja jednadžbe $x^2-Dy^2=N_1$ i jednadžbe $x^2-Dy^2=N_2$ možemo složiti cjelobrojno rješenje jednadžbe $x^2-Dy^2=N_1N_2$. Naravno, gledano iz perspektive kvadratnih cijelih brojeva, slaganje rješenja upravo je množenje kvadratnih cijelih brojeva, što pokazuje koliko je praktično zapisivati rješenja Pellove jednadžbe u obliku kvadratnog cijelog broja. Posebno, uzmemo li $N_1=N$ i $N_2=1$, vidimo da iz jednog poznatog rješenja jednadžbe $x^2-Dy^2=N$ i svih rješenja pripadne Pellove jednadžbe $x^2-Dy^2=1$ možemo dobiti još rješenja jednadžbe $x^2-Dy^2=N$. Naravno, tim postupkom ne moramo nužno dobiti sva rješenja. No to barem pokazuje da je razumijevanje strukture rješenja Pellove jednadžbe važno za razumijevanje strukture rješenja poopćene Pellove jednadžbe.

### Pellova jednadžba

Geometrijsko značenje jednadžbe $x^2-Dy^2=1$ jest hiperbola kojoj je realna os na osi $x$, a imaginarna os na osi $y$. Svakoj točki hiperbole jednoznačno odgovara jedna vrijednost $x+y\sqrt{D}$ različita od nule: lijeva grana hiperbole odgovara negativnim vrijednostima $x+y\sqrt{D}$, a desna pozitivnima. Štoviše, na svakoj grani vrijednosti $x+y\sqrt{D}$ strogo rastu kako se po hiperboli krećemo odozdo prema gore. Vrijednost kvadratnog cijelog broja tako daje rješenjima Pellove jednadžbe prirodan uređaj.

Hiperbola je simetrična i s obzirom na os $x$ i s obzirom na os $y$, pa je pri razmatranju rješenja Pellove jednadžbe dovoljno promatrati samo dio u prvom kvadrantu; ostala rješenja dobivaju se simetrijom. To odgovara promatranju samo rješenja s $x+y\sqrt{D}>1$. Ako jednadžba osim $(\pm 1,0)$ ima i netrivijalna rješenja, onda u prvom kvadrantu sigurno postoji rješenje $(x_1,y_1)$ s najmanjom vrijednošću $x+y\sqrt{D}$; to je ujedno cjelobrojna točka u prvom kvadrantu (bez koordinatnih osi) s najmanjom apscisom i ordinatom, i naziva se fundamentalno rješenje (fundamental solution) Pellove jednadžbe[^fundamental-solution]. Prema prethodnom razmatranju, svi parovi cijelih brojeva $(x_k,y_k)$ za koje je $x_k+y_k\sqrt{D}=(x_1+y_1\sqrt{D})^k$ rješenja su Pellove jednadžbe i svi leže u prvom kvadrantu. Obratno, to su zaista sva rješenja Pellove jednadžbe u prvom kvadrantu. Iskoristimo li još simetriju, dobivamo sljedeći zaključak:

???+ note "Teorem"
    Neka je $(x_1,y_1)$ fundamentalno rješenje Pellove jednadžbe $x^2-Dy^2=1$. Tada je skup svih njezinih rješenja
    
    $$
    \{(x,y):x+y\sqrt{D}=\pm(x_1+y_1\sqrt{D})^k,k\in\mathbf Z\}.
    $$

??? note "Dokaz"
    Najprije dokazujemo da u prvom kvadrantu nema drugih rješenja. Pretpostavimo suprotno, da postoji neko drugo rješenje $x+y\sqrt{D}$ i da za neki $k\ge 0$ vrijedi
    
    $$
    x_k+y_k\sqrt{D}< x+y\sqrt{D}< x_{k+1}+y_{k+1}\sqrt{D}.
    $$
    
    Geometrijski to znači da cjelobrojna točka $(x,y)$ pada na hiperbolu između $(x_k,y_k)$ i $(x_{k+1},y_{k+1})$ (bez krajnjih točaka). Pomnožimo li nejednakost s $x_k-y_k\sqrt{D}=(x_k+y_k\sqrt{D})^{-1}$, dobivamo
    
    $$
    1< (x+y\sqrt{D})(x_k-y_k\sqrt{D})=(xx_k-Dyy_k)+(x_ky-xy_k)\sqrt{D} < x_1+y_1\sqrt{D}.
    $$
    
    Prema već spomenutoj monotonosti, ta nejednakost znači da je $(xx_k-Dyy_k,x_ky-xy_k)$ cjelobrojna točka koja leži između $(1,0)$ i $(x_1,y_1)$. To je u suprotnosti s izborom $(x_1,y_1)$.
    
    Pri proširenju rješenja iz prvog kvadranta na cijelu ravninu, uzimanje suprotnog eksponenta $k$ (tj. recipročne vrijednosti cijelog izraza) odgovara simetriji s obzirom na os $x$, a uzimanje suprotne vrijednosti cijelog izraza odgovara simetriji s obzirom na ishodište. Dodamo li još trivijalno rješenje za $k=0$, dobivamo sva rješenja Pellove jednadžbe.

Dosadašnje razmatranje samo je pretpostavljalo postojanje fundamentalnog rješenja. Sada treba pokazati da Pellova jednadžba uvijek ima netrivijalno rješenje.

???+ note "Teorem"
    Pellova jednadžba $x^2-Dy^2=1$ uvijek ima cjelobrojno rješenje različito od $(\pm 1,0)$.

??? note "Dokaz"
    Najprije, [Dirichletov teorem](./continued-fraction.md#用渐近分数逼近实数) pokazuje da postoji beskonačno mnogo parova pozitivnih cijelih brojeva $(x,y)$ za koje vrijedi
    
    $$
    \left|\dfrac{x}{y}-\sqrt{D}\right| \le \dfrac{1}{y^2}
    $$
    
    a svi oni zadovoljavaju nejednakost
    
    $$
    |x^2-Dy^2|=y^2\left|\dfrac{x}{y}-\sqrt{D}\right|\left|\dfrac{x}{y}+\sqrt{D}\right| \le \dfrac{1}{y^2}+2\sqrt{D}<1+2\sqrt{D}.
    $$
    
    Stoga nužno postoji cijeli broj $m\in(-1-2\sqrt{D},1+2\sqrt{D})$ takav da beskonačno mnogo parova $(x,y)$ zadovoljava $x^2-Dy^2 = m$. Razvrstamo li te parove $(x,y)$ prema ostatcima modulo $m$, zaključujemo da za neki par cijelih brojeva $(x_0,y_0)$ sigurno postoji beskonačno mnogo parova $(x,y)$ za koje vrijedi $x\equiv x_0\pmod m$ i $y\equiv y_0\pmod m$. Odaberemo li bilo koja dva različita para $(x_1,y_1)$ i $(x_2,y_2)$ koja zadovoljavaju te uvjete, vrijedi
    
    $$
    \dfrac{x_1+y_1\sqrt{D}}{x_2+y_2\sqrt{D}}=\dfrac{x_1x_2-Dy_1y_2}{m}+\dfrac{x_2y_1-x_1y_2}{m}\sqrt{D}.
    $$
    
    Budući da prema kongruencijama vrijedi
    
    $$
    \begin{aligned}
    x_1x_2-Dy_1y_2 &\equiv x_0^2-Dy_0^2 = m \equiv 0 \pmod{|m|},\\
    x_2y_1-x_1y_2 &\equiv x_0y_0-x_0y_0 = 0 \pmod{|m|},
    \end{aligned}
    $$
    
    to znači da je desna strana gornje jednakosti cjelobrojno rješenje. Štoviše, budući da je $(x_1,y_1)\neq(x_2,y_2)$, ono nije trivijalno. Time je pokazano da Pellova jednadžba zaista ima netrivijalno rješenje.

Naravno, dokaz u ovom odjeljku nije konstruktivan; kad u nastavku budemo razmatrali metodu rješavanja Pellove jednadžbe, rješenje Pellove jednadžbe izravno ćemo konstruirati pomoću konvergenti verižnog razlomka, čime ćemo dobiti još jedan dokaz da Pellova jednadžba ima netrivijalno rješenje. Osim toga, iako se struktura rješenja Pellove jednadžbe dobivena u ovom odjeljku podudara sa strukturom jedinica prstena realnih kvadratnih cijelih brojeva, za slučaj $D\equiv 1\pmod 4$ ovaj odjeljak nije u potpunosti riješio pitanje strukture jedinica pripadnog prstena kvadratnih cijelih brojeva; o tome će još biti riječi u nastavku.

### Poopćena Pellova jednadžba

Graf poopćene Pellove jednadžbe $x^2-Dy^2=N$ također je hiperbola u ravnini, također s osima $x$ i $y$ kao osima simetrije. Već smo istaknuli da se neka rješenja jednadžbe $x^2-Dy^2=N$ mogu razlikovati samo za faktor koji je rješenje Pellove jednadžbe, što znači da rješenja jednadžbe $x^2-Dy^2=N$ možemo podijeliti u klase ekvivalencije. Za dva rješenja $(x_1,y_1)$ i $(x_2,y_2)$ jednadžbe $x^2-Dy^2=N$ ako postoji rješenje $(u,v)$ Pellove jednadžbe takvo da vrijedi $x_2+y_2\sqrt{D}=(x_1+y_1\sqrt{D})(u+v\sqrt{D})$, kažemo da su rješenja $(x_1,y_1)$ i $(x_2,y_2)$ ekvivalentna. Nužan i dovoljan uvjet da dva rješenja budu ekvivalentna jest

$$
N\mid (x_1x_2-Dy_1y_2),\ N\mid (x_2y_1-x_1y_2).
$$

Budući da je rješenja Pellove jednadžbe razmjerno lako naći, prirodna je zamisao u svakoj od navedenih klasa ekvivalencije naći po jedno rješenje. Čim znamo ta rješenja, pomoću rješenja pripadne Pellove jednadžbe možemo dobiti sva tražena rješenja poopćene Pellove jednadžbe. Zbog simetrije u svakoj klasi ekvivalencije rješenja poopćene Pellove jednadžbe postoji rješenje s nenegativnom, ali što manjom ordinatom $y$: ako je takvo rješenje jedinstveno, nazivamo ga fundamentalnim rješenjem te klase ekvivalencije; inače ta klasa nužno ima dva rješenja s nenegativnim i najmanjim $y$, i to simetrična s obzirom na os $y$, pa tada kao fundamentalno rješenje biramo ono s $x>0$. Prema tome, riješiti poopćenu Pellovu jednadžbu $x^2-Dy^2=N$ znači naći skup $U$ njezinih fundamentalnih rješenja. Ako je $(r,s)$ fundamentalno rješenje pripadne Pellove jednadžbe, skup svih rješenja poopćene Pellove jednadžbe je

$$
\{(x,y):x+y\sqrt{D}=\pm(r+s\sqrt{D})^k(u+v\sqrt{D}),k\in\mathbf Z,u+v\sqrt{D}\in U\}.
$$

Fundamentalnih rješenja poopćene Pellove jednadžbe nužno ima konačno mnogo. Naime, iz gornjeg izraza za opće rješenje vidi se da apsolutna vrijednost $|u+v\sqrt{D}|$ nužno leži između $r-s\sqrt{D}$ i $r+s\sqrt{D}$. U literaturi navedenoj na kraju članka dane su strože ocjene raspona koordinata fundamentalnih rješenja. Naravno, za razliku od Pellove jednadžbe, poopćena Pellova jednadžba ne mora imati rješenja.

Da bismo iz jednog rješenja $(u,v)$ poopćene Pellove jednadžbe i fundamentalnog rješenja $(r,s)$ Pellove jednadžbe dobili sva rješenja iz iste klase ekvivalencije, osim slaganja rješenja možemo iskoristiti i sljedeću rekurziju

$$
x_{k} = 2rx_{k-1} - x_{k-2},\ y_{k} = 2ry_{k-1} - y_{k-2},
$$

gdje je $x_k+y_k\sqrt{D}=(r+s\sqrt{D})^k(u+v\sqrt{D})$. Naime, i $x_k$ i $y_k$ mogu se za neki par realnih brojeva $(A,B)$ zapisati u obliku $A(r+s\sqrt{D})^k+B(r-s\sqrt{D})^k$, a prema Vièteovim formulama $r\pm s\sqrt{D}$ dva su realna korijena jednadžbe $x^2-2rx+1=0$, pa $x_k$ i $y_k$ zadovoljavaju gornju linearnu rekurziju drugog reda s konstantnim koeficijentima. U usporedbi sa slaganjem rješenja ta rekurzija zahtijeva manje množenja.

## Metode rješavanja

I Pellova i poopćena Pellova jednadžba mogu se rješavati pomoću verižnih razlomaka.

### PQa algoritam

Svi algoritmi u ovom članku temelje se na PQa algoritmu, kojim se može izračunati razvoj određene kvadratne iracionalnosti u verižni razlomak.

Neka cijeli brojevi $P_0,Q_0,D$ zadovoljavaju $Q_0\neq 0$, $D>0$ i nije potpun kvadrat, te $P_0^2\equiv D\pmod{Q_0}$. Tada se razvoj kvadratne iracionalnosti

$$
\omega=\dfrac{P_0+\sqrt{D}}{Q_0}
$$

u verižni razlomak $[a_0,a_1,\cdots]$ može dobiti sljedećim [rekurzivnim formulama](./continued-fraction.md#二次无理数):

$$
a_k = \left\lfloor\dfrac{P_k+\sqrt{D}}{Q_k}\right\rfloor,\ P_{k+1} = a_kQ_k - P_k,\ Q_{k+1} = \dfrac{D-P_{k+1}^2}{Q_k}.
$$

Nadalje, brojnik $A_k$ i nazivnik $B_k$ $k$-te konvergente od $\omega$ dani su sljedećim [rekurzivnim formulama](./continued-fraction.md#递推关系):

$$
A_k = a_kA_{k-1} + A_{k-2},\ B_k = a_kB_{k-1} + B_{k-2}
$$

uz $A_{-1} = 1$, $A_{-2}=0$, $B_{-1}=0$, $B_{-2}=1$.

Točnost tih formula već je dokazana u članku o verižnim razlomcima. Ondje je također objašnjeno da je kvadratna iracionalnost [periodički verižni razlomak](./continued-fraction.md#二次无理数), pa trojke $(P_k,Q_k,a_k)$ na kraju ulaze u ciklus i algoritam uvijek završava u konačno mnogo koraka. Neka je najmanja duljina perioda $\ell$, a najraniji početak perioda na položaju $k_0$; tada se razvoj kvadratne iracionalnosti u verižni razlomak može zapisati kao

$$
\omega=[a_0,\cdots,a_{k_0-1},\overline{a_{k_0},\cdots,a_{k_0+\ell-1}}].
$$

Da bismo PQa algoritmom riješili Pellovu jednadžbu, trebamo sljedeći rezultat:

???+ note "Teorem"
    Nastavljamo s gornjim oznakama. Neka je $G_k=Q_0A_k-P_0B_k$. Tada par cijelih brojeva $(G_{k-1},B_{k-1})$ zadovoljava relaciju
    
    $$
    G_{k-1}^2-DB_{k-1}^2=(-1)^{k}Q_0Q_{k},
    $$
    
    a njihov najveći zajednički djelitelj $\gcd(G_{k-1},B_{k-1})$ dijeli $Q_{k}$.

??? note "Dokaz"
    Neka je u razvoju $\omega$ u verižni razlomak $k$-ti ostatak (potpuni kvocijent) $\omega_{k}$, tj.
    
    $$
    \omega = [a_0,a_1,\cdots,a_{k-1},\omega_k] = \dfrac{\omega_k A_{k-1}+A_{k-2}}{\omega_k B_{k-1}+B_{k-2}}.
    $$
    
    Uvrstimo li $\omega=(P_0+\sqrt{D})/Q_0$ i $\omega_k=(P_k+\sqrt{D})/Q_k$ u gornju jednakost, dobivamo
    
    $$
    \dfrac{P_0+\sqrt{D}}{Q_0} = \dfrac{(P_k+\sqrt{D})A_{k-1}+Q_kA_{k-2}}{(P_k+\sqrt{D})B_{k-1}+Q_kB_{k-2}}.
    $$
    
    Uklonimo li nazivnike s obiju strana i usporedimo koeficijente racionalnog i iracionalnog dijela, a zatim uvrstimo izraz za $G_k$, dobivamo sljedeće jednakosti:
    
    $$
    \begin{aligned}
    G_{k-1} &= P_kB_{k-1} + Q_kB_{k-2},\\
    DB_{k-1} &= P_kG_{k-1} + Q_kG_{k-2}.
    \end{aligned}
    $$
    
    Stoga, pomnožimo li prvu jednakost s $G_{k-1}$ i oduzmemo drugu pomnoženu s $B_{k-1}$, dobivamo
    
    $$
    \begin{aligned}
    G_{k-1}^2-DB_{k-1}^2 &= (B_{k-2}G_{k-1}-B_{k-1}G_{k-2})Q_k \\
    &= (A_{k-1}B_{k-2}-B_{k-1}A_{k-2})Q_0Q_k \\
    &= (-1)^kQ_0Q_k.
    \end{aligned}
    $$
    
    U posljednjem koraku iskorištena je [formula za razliku](./continued-fraction.md#误差估计) konvergenti. Time je dokazana prva tvrdnja.
    
    Da bismo dokazali drugu tvrdnju, uvrstimo izraz za $G_k$ u prvu tvrdnju:
    
    $$
    (Q_0A_{k-1}-P_0B_{k-1})^2 - DB_{k-1}^2 = (-1)^kQ_0Q_k.
    $$
    
    Stoga, koristeći $Q_0\mid(P_0^2-D)$, imamo
    
    $$
    Q_0A_{k-1}^2 +\left(\dfrac{P_0^2-D}{Q_0}B_{k-1}- 2P_0A_{k-1}\right)B_{k-1} = (-1)^kQ_k.
    $$
    
    Dakle, $\gcd(G_{k-1},B_{k-1}) = \gcd(Q_0A_{k-1},B_{k-1})$ dijeli $Q_k$.

Taj rezultat daje način traženja rješenja jednadžbe $x^2-Dy^2=N$. Ako prikladno odaberemo $Q_0>0$ i za $P_0$ odaberemo rješenje kongruencije $P_0^2\equiv D\pmod{Q_0}$, onda izvođenjem PQa algoritma na $(P_0+\sqrt{D})/Q_0$ sve dok ne nađemo $(-1)^kQ_0Q_{k}=N$ dobivamo da je $(G_{k-1},B_{k-1})$ rješenje polazne jednadžbe. Štoviše, ako je $Q_k=\pm 1$, tako dobiveno rješenje sigurno je primitivno, tj. $G_{k-1}$ i $B_{k-1}$ sigurno su relativno prosti.

Ta je zamisao srž rješavanja Pellove i poopćene Pellove jednadžbe. Nakon što smo je razumjeli, u nastavku se bavimo pojedinostima algoritma i dokazujemo da se sva rješenja mogu dobiti na taj način.

### Pellova jednadžba

Da bismo riješili Pellovu jednadžbu $x^2-Dy^2=1$, dovoljno je izvesti PQa algoritam za $(P_0,Q_0,D)=(0,1,D)$ sve dok se ne pojavi $(-1)^kQ_k=1$; tada je $(A_{k-1},B_{k-1})$ rješenje Pellove jednadžbe (jer je $G_{k-1}$ u tom slučaju upravo $A_{k-1}$). Naravno, za Pellovu jednadžbu taj postupak možemo opisati i preciznije.

Prvo, rješenje se sigurno pojavljuje na kraju perioda. Gornji postupak odgovara razvoju $\sqrt{D}$ u verižni razlomak. Za njega već imamo [rezultat](./continued-fraction.md#纯循环连分数):

$$
\sqrt{D} = [\lfloor\sqrt{D}\rfloor,\overline{a_1,\cdots,a_{\ell-1},2\lfloor\sqrt{D}\rfloor}].
$$

Ovdje je duljina perioda $\ell$, a period počinje od $1$. člana (indeksi počinju od $0$). Štoviše, njegov $\ell$-ti ostatak jednak je $\lfloor\sqrt{D}\rfloor+\sqrt{D}$, što znači da je $Q_{\ell}=1$. Stoga, ako je $\ell$ paran, $(A_{\ell-1},B_{\ell-1})$ je netrivijalno rješenje Pellove jednadžbe; ako je $\ell$ neparan, $(A_{2\ell-1},B_{2\ell-1})$ je netrivijalno rješenje Pellove jednadžbe.

Sljedeće treba pokazati da je upravo dobiveno rješenje sigurno fundamentalno rješenje. Taj se zaključak temelji na dvama razlozima: prvo, razlomci $x/y$ koji odgovaraju svim pozitivnim cjelobrojnim rješenjima $(x,y)$ Pellove jednadžbe pojavljuju se među konvergentama od $\sqrt{D}$, što jamči da je $(x,y)$ nužno neki $(A_k,B_k)$ iz tijeka PQa algoritma; drugo, osim na kraju perioda, $Q_k=1$ ne pojavljuje se ni na jednom drugom mjestu, a budući da rekurzija za $A_k$ i $B_k$ jamči da oni rastu s porastom indeksa, najmanje pozitivno cjelobrojno rješenje (tj. fundamentalno rješenje) nužno se pojavljuje na upravo navedenom mjestu. Ta dva razloga slijede redom iz sljedećih dvaju teorema:

???+ note "Teorem"
    Neka jednadžba $x^2-Dy^2=N$ ima pozitivno cjelobrojno rješenje $(x,y)$. Ako je $|N|<\sqrt{D}$, onda je $\dfrac{x}{y}$ sigurno jednak nekoj konvergenti od $\sqrt{D}$.

??? note "Dokaz"
    Kad je $N>0$, iz $x^2-Dy^2>0$ slijedi $x>y\sqrt{D}$. Stoga vrijedi
    
    $$
    \left|\dfrac{x}{y}-\sqrt{D}\right| = \dfrac{N}{y(x+y\sqrt{D})}<\dfrac{N}{2y^2\sqrt{D}}<\dfrac{1}{2y^2}.
    $$
    
    Prema [Legendreovu kriteriju](./continued-fraction.md#渐近分数的判定), $\dfrac{x}{y}$ je konvergenta od $\sqrt{D}$.
    
    Kad je $N<0$, $x>y\sqrt{D}$ više ne vrijedi. Zato umjesto toga promatramo rješenja jednadžbe $y^2-\dfrac{1}{D}x^2=-\dfrac{N}{D}$. Budući da je $\dfrac{|N|}{D}<\sqrt{\dfrac{1}{D}}$, gornje rasuđivanje i dalje vrijedi. To znači da je $\dfrac{y}{x}$ konvergenta od $\dfrac{1}{\sqrt{D}}$. Prema [teoremu o recipročnoj vrijednosti](./continued-fraction.md#递推关系), $\dfrac{x}{y}$ je također konvergenta od $\sqrt{D}$.

???+ note "Teorem"
    Tijekom izvođenja gornjeg PQa algoritma za $(P_0,Q_0,D)=(0,1,D)$, iz $Q_k=1$ nužno slijedi $\ell\mid k$.

??? note "Dokaz"
    U razvoju $\sqrt{D}$ u verižni razlomak svi su ostatci osim $0$. ostatka [čisto periodički verižni razlomci](./continued-fraction.md#纯循环连分数). Neka je $Q_k=1$. Prema Galoisovu rezultatu, ostatak $\omega_k=P_k+\sqrt{D}>1$ nužno ima konjugat $-1<P_k-\sqrt{D}<0$, što znači da je $P_k=\lfloor\sqrt{D}\rfloor$. Stoga je ostatak $\omega_k$ jednak $\omega_\ell$. No ponavljanje ostatka znači periodičnost verižnog razlomka, pa ako $k$ nije višekratnik od $\ell$, dolazimo u proturječje s time da je $\ell$ najmanji pozitivni period. Dakle, nužno je $\ell\mid k$.

Objedinimo li razmatranja u ovom odjeljku, zaključujemo: dovoljno je razviti $\sqrt{D}$ u verižni razlomak, tj. izvesti PQa algoritam s početkom $(P_0,Q_0,D)=(0,1,D)$, i kad prvi put dobijemo $Q_\ell=1$, stigli smo do kraja prvog perioda. Tada je, ako je $\ell$ paran, $(A_{\ell-1},B_{\ell-1})$ fundamentalno rješenje Pellove jednadžbe; inače je fundamentalno rješenje Pellove jednadžbe $(A_{2\ell-1},B_{2\ell-1})$. Za slučaj neparne duljine perioda $\ell$ nije potrebno nastavljati PQa algoritam do dvostrukog perioda; uskoro ćemo pokazati da je $A_{2\ell-1}+B_{2\ell-1}\sqrt{D}=(A_{\ell-1}+B_{\ell-1}\sqrt{D})^2$, pa se fundamentalno rješenje Pellove jednadžbe može izračunati izravno iz $(A_{\ell-1},B_{\ell-1})$. Sva ostala rješenja Pellove jednadžbe mogu se izračunati iz fundamentalnog rješenja Pellove jednadžbe.

??? example "Primjeri"
    1.  Riješimo jednadžbu $x^2-14y^2=1$.
    
        Rezultat izvođenja PQa algoritma za $(P_0,Q_0,D)=(0,1,14)$ je sljedeći (crveno je označen prvi period):
    
        | $k$ | $P$ | $Q$ |        $a$       |  $A$  |  $B$ |  $G$  | $G^2-DB^2$ |
        | :-: | :-: | :-: | :--------------: | :---: | :--: | :---: | :--------: |
        | $0$ | $0$ | $1$ |        $3$       |  $3$  |  $1$ |  $3$  |    $-5$    |
        | $1$ | $3$ | $5$ | $\color{red}{1}$ |  $4$  |  $1$ |  $4$  |     $2$    |
        | $2$ | $2$ | $2$ | $\color{red}{2}$ |  $11$ |  $3$ |  $11$ |    $-5$    |
        | $3$ | $2$ | $5$ | $\color{red}{1}$ |  $15$ |  $4$ |  $15$ |     $1$    |
        | $4$ | $3$ | $1$ | $\color{red}{6}$ | $101$ | $27$ | $101$ |    $-5$    |
        | $5$ | $3$ | $5$ |        $1$       | $116$ | $31$ | $116$ |     $2$    |
    
        Duljina perioda $\ell=4$ je parna. Najmanje pozitivno cjelobrojno rješenje jednadžbe je $(G_3,B_3)=(15,4)$.
    2.  Riješimo jednadžbu $x^2-41y^2=1$.
    
        Rezultat izvođenja PQa algoritma za $(P_0,Q_0,D)=(0,1,41)$ je sljedeći (crveno je označen prvi period):
    
        | $k$ | $P$ | $Q$ |        $a$        |   $A$   |   $B$  |   $G$   | $G^2-DB^2$ |
        | :-: | :-: | :-: | :---------------: | :-----: | :----: | :-----: | :--------: |
        | $0$ | $0$ | $1$ |        $6$        |   $6$   |   $1$  |   $6$   |    $-5$    |
        | $1$ | $6$ | $5$ |  $\color{red}{2}$ |   $13$  |   $2$  |   $13$  |     $5$    |
        | $2$ | $4$ | $5$ |  $\color{red}{2}$ |   $32$  |   $5$  |   $32$  |    $-1$    |
        | $3$ | $6$ | $1$ | $\color{red}{12}$ |  $397$  |  $62$  |  $397$  |     $5$    |
        | $4$ | $6$ | $5$ |        $2$        |  $826$  |  $129$ |  $826$  |    $-5$    |
        | $5$ | $4$ | $5$ |        $2$        |  $2049$ |  $320$ |  $2049$ |     $1$    |
        | $6$ | $6$ | $1$ |        $12$       | $25414$ | $3969$ | $25414$ |    $-5$    |
        | $7$ | $6$ | $5$ |        $2$        | $52877$ | $8258$ | $52877$ |     $5$    |
    
        Duljina perioda $\ell=3$ je neparna. Najmanje pozitivno cjelobrojno rješenje jednadžbe je $(G_5,B_5)=(2049,320)$. Ono se može izračunati i iz $(G_2,B_2)=(32,5)$:
    
        $$
        (32+5\sqrt{41})^2=2049+320\sqrt{41}.
        $$

### Negativna Pellova jednadžba

Prema razmatranju iz prethodnog odjeljka, rješenja negativne Pellove jednadžbe također nužno odgovaraju konvergentama od $\sqrt{D}$ i mogu se pojaviti samo ondje gdje je $(-1)^kQ_k=-1$. To se može dogoditi samo na kraju perioda. Stoga negativna Pellova jednadžba ima rješenje ako i samo ako je duljina perioda $\ell$ neparna. Kad rješenje postoji, $(A_{\ell-1},B_{\ell-1})$ je fundamentalno rješenje negativne Pellove jednadžbe. Postupak rješavanja isti je kao u prethodnom odjeljku.

Rasuđivanjem sličnim ranijem dokazu o strukturi rješenja Pellove jednadžbe može se dokazati sljedeći rezultat:

???+ note "Teorem"
    Neka jednadžba $x^2-Dy^2=-1$ ima rješenje i neka je njezino fundamentalno rješenje $(x_1,y_1)$. Tada sva cjelobrojna rješenja jednadžbe $x^2-Dy^2=\pm 1$ pripadaju skupu
    
    $$
    \{(x,y):x+y\sqrt{D}=\pm(x_1+y_1\sqrt{D})^k,k\in\mathbf Z\}.
    $$
    
    Posebno, cjelobrojno rješenje $(x_2,y_2)$ koje zadovoljava $x_2+y_2\sqrt{D}=(x_1+y_1\sqrt{D})^2$ upravo je fundamentalno rješenje jednadžbe $x^2-Dy^2=1$.

??? note "Dokaz"
    Zbog simetrije dovoljno je promatrati pozitivna cjelobrojna rješenja, tj. slučaj $x+y\sqrt{D}>1$. No budući da je $x^2-Dy^2=\pm 1$ par hiperbola, $x+y\sqrt{D}$ se ne može bijektivno pridružiti parovima $(x,y)$. Da bismo riješili tu poteškoću, najprije dokazujemo da je gore navedeni $(x_2,y_2)$ fundamentalno rješenje jednadžbe $x^2-Dy^2=1$.
    
    Očito je $(x_2,y_2)$ rješenje jednadžbe $x^2-Dy^2=1$. Ako je $(z,w)$ fundamentalno rješenje jednadžbe $x^2-Dy^2=1$, nužno vrijedi $1<z+w\sqrt{D}\le x_2+y_2\sqrt{D}$. Ako u desnoj nejednakosti ne vrijedi jednakost, dijeljenjem nejednakosti s $x_1+y_1\sqrt{D}$ dobivamo $-x_1+y_1\sqrt{D}<(z+w\sqrt{D})(-x_1+y_1\sqrt{D})<x_1+y_1\sqrt{D}$. Raspišemo li izraz u sredini te nejednakosti, dobivamo oblik $x'+y'\sqrt{D}$, čija je norma $-1$ i $(x',y')$ je također cjelobrojno rješenje. Uzmemo li recipročne vrijednosti u toj nejednakosti, vidimo da i $-x'+y'\sqrt{D}$ pada između $-x_1+y_1\sqrt{D}$ i $x_1+y_1\sqrt{D}$. Kvadratni cijeli brojevi $\pm x'+y'\sqrt{D}$ međusobno su recipročni, pa je jedan od njih nužno veći od $1$. No između $1$ i $x_1+y_1\sqrt{D}$ ne bi se smio pojaviti nijedan drugi kvadratni cijeli broj norme $-1$, što je u suprotnosti s minimalnošću $x_1+y_1\sqrt{D}$. Dakle, nužno vrijedi $x_2+y_2\sqrt{D}=z+w\sqrt{D}$, tj. $(x_2,y_2)$ je fundamentalno rješenje jednadžbe $x^2-Dy^2=1$.
    
    Na temelju toga, ako bi se pojavilo rješenje $(x,y)$ jednadžbe $x^2-Dy^2=\pm 1$ koje ne odgovara nijednom $(x_1+y_1\sqrt{D})^k$, nužno bi postojao $k$ takav da je $(x_1+y_1\sqrt{D})^{2k}<x+y\sqrt{D}<(x_1+y_1\sqrt{D})^{2k+2}$; uklanjanjem faktora $(x_1+y_1\sqrt{D})^{2k+1}$ dobivamo da postoji kvadratni cijeli broj $x'+y'\sqrt{D}\neq 1$ norme $\pm 1$ koji leži između $-x_1+y_1\sqrt{D}$ i $x_1+y_1\sqrt{D}$. Ponovimo li rasuđivanje s recipročnim vrijednostima iz prethodnog odlomka, to je u suprotnosti s minimalnošću $x_1+y_1\sqrt{D}$. Time je polazna tvrdnja dokazana.

Budući da je $(A_{\ell-1},B_{\ell-1})$ najmanje pozitivno cjelobrojno rješenje negativne Pellove jednadžbe, a sva pozitivna cjelobrojna rješenja jednadžbe $x^2-Dy^2=\pm 1$ pojavljuju se u skupu

$$
\{(x,y):x+y\sqrt{D}=(A_{\ell-1}+B_{\ell-1}\sqrt{D})^k,k\in\mathbf N_+\}
$$

i budući da ta pozitivna cjelobrojna rješenja nužno odgovaraju konvergentama od $\sqrt{D}$ na kraju perioda (na mjestu neposredno prije njega), a brojnici i nazivnici konvergenti strogo rastu, za sve $k\in\mathbf N_+$ uvijek vrijedi

$$
(A_{\ell-1}+B_{\ell-1}\sqrt{D})^k = A_{k\ell-1}+B_{k\ell-1}\sqrt{D}.
$$

Među svim tim pozitivnim cjelobrojnim rješenjima, ona s neparnim $k$ rješenja su negativne Pellove jednadžbe, a ona s parnim $k$ rješenja su Pellove jednadžbe; ona se pojavljuju naizmjence.

Da bismo utvrdili ima li negativna Pellova jednadžba rješenje, treba izračunati duljinu perioda razvoja $\sqrt{D}$ u verižni razlomak, što nije lako izračunati, pa bismo željeli naći jednostavniji kriterij. No trenutačno ne postoji kriterij s jednostavnim i lako izračunljivim uvjetima[^solubility-neg-pell]. Ovdje navodimo samo jedan jednostavan rezultat.

???+ note "Teorem"
    Ako jednadžba $x^2-Dy^2=-1$ ima rješenje, onda $4$ ne dijeli $D$ i $D$ nema prostih faktora oblika $4k+3$. Obratno, ako je $D=2$ ili je $D$ prost broj oblika $4k+1$, jednadžba sigurno ima rješenje.

??? note "Dokaz"
    Najprije, ako negativna Pellova jednadžba ima rješenje, to znači da je $-1$ kvadratni ostatak modulo $D$, pa je $-1$ kvadratni ostatak i modulo svaki djelitelj $d$ od $D$; stoga je $d\neq 4$ i $d$ nije prost broj oblika $4k+3$. Obratno, jednadžba $x^2-2y^2=-1$ ima netrivijalno rješenje $(1,1)$. Preostaje slučaj kad je $D$ prost broj oblika $4k+1$.
    
    Neka je $D$ prost broj oblika $4k+1$; treba dokazati da jednadžba $x^2-Dy^2=-1$ ima rješenje. Zamisao je krenuti od fundamentalnog rješenja $(u,v)$ Pellove jednadžbe $x^2-Dy^2=1$ i konstruirati rješenje $(\alpha,\beta)$ jednadžbe $x^2-Dy^2=-1$. Ako je $u$ paran, uzimanjem obiju strana jednakosti $u^2-Dv^2=1$ modulo $4$ dobivamo $v^2\equiv -1\pmod 4$, ali $-1$ nije kvadratni ostatak modulo $4$. To proturječje pokazuje da je $u$ neparan. Promotrimo jednakost $Dv^2=u^2-1=(u+1)(u-1)$. Budući da je $u$ neparan, $\gcd(u+1,u-1)=\gcd(u+1,2)=2$. Na temelju te činjenice, raspodijelimo li faktore od $Dv^2$ na $u+1$ i $u-1$, jedan od njih nužno je $2\alpha^2$, a drugi $2D\beta^2$, gdje su $\alpha$ i $\beta$ relativno prosti pozitivni cijeli brojevi i $v=2\alpha\beta$. Uvrstimo li $u=\alpha^2+D\beta^2$ i $v=2\alpha\beta$ u $u^2-Dv^2=1$, dobivamo $\alpha^2-D\beta^2=\pm 1$. Budući da je $(u,v)$ fundamentalno rješenje Pellove jednadžbe, a $(\alpha,\beta)$ je par pozitivnih cijelih brojeva manji od $(u,v)$, desna strana te jednakosti ne može biti $+1$, pa može biti samo $-1$. Time je dokazano da jednadžba $x^2-Dy^2=-1$ ima rješenje $(\alpha,\beta)$.

Ako je $D$ složen, to što nema prostih faktora oblika $4k+3$ i što nema kvadratnih faktora ne jamči da jednadžba $x^2-Dy^2=-1$ ima rješenje; primjerice, $x^2-34y^2=-1$ nema rješenja.

??? example "Primjer"
    Iz rezultata izračuna u gornjem primjeru vidi se da jednadžba $x^2-14y^2=-1$ nema rješenja, a najmanje pozitivno cjelobrojno rješenje jednadžbe $x^2-41y^2=-1$ je $(G_2,B_2)=(32,5)$.

### Slučaj norme ±4

Sada razmatramo rješenja jednadžbe $x^2-Dy^2=\pm 4$. Ovdje ponašanje rješenja ovisi o vrijednosti $D\bmod 4$.

Neki su slučajevi laki. Ako je $D\equiv 0\pmod 4$, onda je $x$ paran, pa je $(x/2,y)$ rješenje jednadžbe $u^2-(D/4)v^2=\pm 1$. U ostalim slučajevima $x,y$ nužno su oba neparna ili oba parna. Ako su $x,y$ oba neparna, uzimanjem obiju strana jednadžbe modulo $4$ dobivamo $D\equiv 1\pmod 4$. Stoga, ako je $D\equiv 2,3\pmod 4$, $x,y$ mogu biti samo oba parna, pa je $(x/2,y/2)$ rješenje jednadžbe $u^2-Dv^2=\pm 1$. Prema tome, osim u slučaju $D\equiv 1\pmod 4$, rješenja jednadžbe $x^2-Dy^2=\pm 4$ mogu se dobiti iz rješenja pripadne (negativne) Pellove jednadžbe.

Sada razmatramo slučaj $D\equiv 1\pmod 4$, koji se ne može jednostavno svesti na već riješene slučajeve. Da bismo našli fundamentalno rješenje, možemo primijeniti PQa algoritam na $(P_0,Q_0,D)=(1,2,D)$; kad prvi put dobijemo $Q_\ell=2$, stigli smo do kraja prvog perioda. Ako je duljina perioda $\ell$ parna, $(G_{\ell-1},B_{\ell-1})$ je fundamentalno rješenje jednadžbe $x^2-Dy^2=4$; inače je $(G_{\ell-1},B_{\ell-1})$ fundamentalno rješenje jednadžbe $x^2-Dy^2=-4$. Polazeći od $(G_{\ell-1},B_{\ell-1})$ možemo dobiti sva rješenja jednadžbe $x^2-Dy^2=\pm 4$:

$$
\left\{(x,y):\dfrac{x+y\sqrt{D}}{2}=\pm\left(\dfrac{G_{\ell-1}+B_{\ell-1}\sqrt{D}}{2}\right)^k,k\in\mathbf Z\right\}.
$$

Ako je duljina perioda $\ell$ parna, sva su to rješenja jednadžbe $x^2-Dy^2=4$; inače je za neparan $k$ $(x,y)$ rješenje jednadžbe $x^2-Dy^2=-4$, a za paran $k$ $(x,y)$ je rješenje jednadžbe $x^2-Dy^2=4$.

Točnost tog algoritma oslanja se na sljedeće činjenice:

???+ note "Teorem"
    Neka jednadžba $x^2-Dy^2=\pm 4$ ima pozitivno cjelobrojno rješenje $(x,y)$. Ako je $D\equiv 1\pmod 4$, onda je $\dfrac{(x+y)/2}{y}$ sigurno konvergenta od $\dfrac{1+\sqrt{D}}{2}$.

??? note "Dokaz"
    Najprije uočimo da $x,y$ u tom slučaju nužno imaju istu parnost, pa je $(x+y)/2$ cijeli broj. Ako je $(x,y)$ rješenje jednadžbe $x^2-Dy^2=4$, onda je $x>y\sqrt{D}>2y$, pa je
    
    $$
    \left|\dfrac{(x+y)/2}{y}-\dfrac{1+\sqrt{D}}{2}\right| = \dfrac{2}{y(x+y\sqrt{D})}<\dfrac{1}{2y^2}.
    $$
    
    Prema [Legendreovu kriteriju](./continued-fraction.md#渐近分数的判定), $\dfrac{(x+y)/2}{y}$ je konvergenta od $\dfrac{1+\sqrt{D}}{2}$.
    
    Ako je $(x,y)$ rješenje jednadžbe $x^2-Dy^2=-4$, da bismo dobili gornju nejednakost, dovoljno je dokazati $4y<x+y\sqrt{D}$. To vrijedi barem u svim slučajevima osim $D=5,13$. Za slučaj $D=5,13$, uvrstimo li $x=\sqrt{Dy^2-4}$ u tu nejednakost, vidimo da je ona ekvivalentna s $2(\sqrt{D}-2)y^2>1$. Osim za $(D,y)=(5,1)$, ta nejednakost vrijedi za sve $D=5,13$ i pozitivne cijele brojeve $y$. Preostaje provjeriti slučaj $(D,y)=(5,1)$; tada je rješenje jednadžbe $x^2-5y^2=-4$ jednako $(x,y)=(1,1)$, a treba provjeriti da je $\dfrac{1}{1}$ konvergenta od $\dfrac{1+\sqrt{5}}{2}=[\overline{1}]$, što očito vrijedi.

???+ note "Teorem"
    Neka je $D$ pozitivan cijeli broj koji nije potpun kvadrat. Razvoj kvadratne iracionalnosti $\omega=\dfrac{1+\sqrt{D}}{2}$ u verižni razlomak ima oblik
    
    $$
    \omega = [\lfloor\omega\rfloor,\overline{a_1,\cdots,a_{\ell-1},2\lfloor\omega\rfloor-1}],
    $$
    
    gdje je $\ell$ duljina perioda, a $a_k=a_{\ell-k}$ vrijedi za svaki $1\le k<\ell$.

??? note "Dokaz"
    Budući da je $\lfloor\omega\rfloor-1+\omega>1$, a njegov konjugat jednak je $\lfloor\omega\rfloor - \omega$ i leži između $-1$ i $0$, prema [Galoisovu rezultatu](./continued-fraction.md#纯循环连分数) $\lfloor\omega\rfloor-1+\omega$ je čisto periodički verižni razlomak i može se zapisati kao
    
    $$
    \lfloor\omega\rfloor-1+\omega = [\overline{2\lfloor\omega\rfloor-1,a_1,\cdots,a_{\ell-1}}].
    $$
    
    A Galoisov rezultat o recipročnoj vrijednosti negativnog konjugata kaže
    
    $$
    \dfrac{1}{\omega-\lfloor\omega\rfloor} = [\overline{a_{\ell-1},\cdots,a_1,2\lfloor\omega\rfloor-1}].
    $$
    
    Stoga, prema definiciji verižnog razlomka, imamo
    
    $$
    \lfloor\omega\rfloor-1+\omega = 2\lfloor\omega\rfloor-1 + \dfrac{1}{\dfrac{1}{\omega-\lfloor\omega\rfloor}} = [2\lfloor\omega\rfloor-1,\overline{a_{\ell-1},\cdots,a_1,2\lfloor\omega\rfloor-1}].
    $$
    
    Jedinstvenost razvoja u verižni razlomak pokazuje da $a_k=a_{\ell-k}$ vrijedi za sve $1\le k<\ell$, pa vrijedi i razvoj koji je trebalo dokazati.

???+ note "Teorem"
    Neka je $D\equiv 1\pmod 4$. Tijekom izvođenja gornjeg PQa algoritma za $(P_0,Q_0,D)=(1,2,D)$, iz $Q_k=2$ nužno slijedi $\ell\mid k$.

??? note "Dokaz"
    U razvoju $\dfrac{1+\sqrt{D}}{2}$ u verižni razlomak svi su ostatci osim $0$. ostatka [čisto periodički verižni razlomci](./continued-fraction.md#纯循环连分数). Neka je $Q_k=2$. Prema Galoisovu rezultatu, konjugat ostatka $\omega_k=\dfrac{P_k+\sqrt{D}}{2}$ nužno zadovoljava $-1<\dfrac{P_k-\sqrt{D}}{2}<0$, tj. $\sqrt{D}-2<P_k<\sqrt{D}$. Budući da u PQa algoritmu uvijek vrijedi $Q_k\mid P_k^2-D$ (vidi [dokaz točnosti algoritma](./continued-fraction.md#二次无理数)), $P_k$ je sigurno neparan, što znači da je vrijednost $P_k$ jedinstvena, tj. $P_k=P_0+2(\lfloor\omega\rfloor-1)$, odnosno ostatak $\omega_k=\omega_\ell$. No ponavljanje ostatka znači periodičnost verižnog razlomka, pa ako $k$ nije višekratnik od $\ell$, dolazimo u proturječje s time da je $\ell$ najmanji pozitivni period. Dakle, nužno je $\ell\mid k$.

???+ note "Teorem"
    Neka je $(x_1,y_1)$ najmanje pozitivno cjelobrojno rješenje jednadžbe $x^2-Dy^2=\pm 4$. Tada je skup svih njezinih rješenja
    
    $$
    \left\{(x,y):\dfrac{x+y\sqrt{D}}{2}=\pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^k,k\in\mathbf Z\right\}.
    $$

??? note "Dokaz"
    Zbog simetrije dovoljno je promatrati pozitivna cjelobrojna rješenja $(x,y)$. Ovdje treba dokazati samo da su parovi realnih brojeva $(x,y)$ iz tog skupa zaista cjelobrojna rješenja jednadžbe $x^2-Dy^2=\pm 4$. Za ostalo je dovoljno ponoviti dokaz o strukturi rješenja jednadžbe $x^2-Dy^2=\pm 1$.
    
    Zapravo treba dokazati da je za bilo koja dva cjelobrojna rješenja $(x_1,y_1)$ i $(x_2,y_2)$ jednadžbe $x^2-Dy^2=\pm 4$ par pozitivnih realnih brojeva $(x_3,y_3)$ definiran s
    
    $$
    \dfrac{x_3+y_3\sqrt{D}}{2} = \dfrac{x_1+y_1\sqrt{D}}{2}\dfrac{x_2+y_2\sqrt{D}}{2}.
    $$
    
    također cjelobrojno rješenje. Raspišemo li desnu stranu i usporedimo koeficijente racionalnog i iracionalnog člana, dobivamo
    
    $$
    x_3=\dfrac{x_1x_2+Dy_1y_2}{2},\ y_3=\dfrac{x_1y_2+x_2y_1}{2}.
    $$
    
    Budući da za $i=1,2$ vrijedi $x_i\equiv x_i^2\equiv Dy_i^2\equiv Dy_i\pmod 2$, imamo
    
    $$
    \begin{aligned}
    2x_3 &= x_1x_2+Dy_1y_2 \equiv D^2y_1y_2+Dy_1y_2=D(D+1)y_1y_2 \equiv 0 \pmod 2,\\
    2y_3 &= x_1y_2+x_2y_1 \equiv Dy_1y_2+Dy_2y_1 = 2Dy_1y_2 \equiv 0 \pmod 2.
    \end{aligned}
    $$
    
    To pokazuje da su $x_3$ i $y_3$ cijeli brojevi. Iskoristimo li još svojstvo da norma čuva množenje, zaključujemo da je $(x_3,y_3)$ rješenje jednadžbe $x^2-Dy^2=\pm 4$.

Objedinimo li te činjenice i ponovimo rasuđivanje iz prethodnih odjeljaka, možemo dokazati točnost gornjeg algoritma za rješavanje jednadžbe $x^2-Dy^2=\pm 4$. Ti rezultati pokazuju da jednadžba $x^2-Dy^2=\pm 4$ ima jednostavnu strukturu rješenja sličnu onoj jednadžbe $x^2-Dy^2=\pm 1$: sva se njezina rješenja mogu izraziti pomoću njezina najmanjeg pozitivnog cjelobrojnog rješenja, bez rješavanja drugih jednadžbi.

Zapravo se sva rješenja jednadžbe $x^2-Dy^2=\pm 1$ mogu naći među rješenjima jednadžbe $x^2-Dy^2=\pm 4$, pa je s tog gledišta jednadžba $x^2-Dy^2=\pm 4$ temeljnija. Očito je $(x,y)$ rješenje jednadžbe $x^2-Dy^2=\pm 1$ ako i samo ako je $(2x,2y)$ rješenje jednadžbe $x^2-Dy^2=\pm 4$. Ranija analiza pokazala je da su za $D\equiv 2,3\pmod 4$ sva rješenja jednadžbe $x^2-Dy^2=\pm 4$ nužno oba parna, pa odgovaraju rješenjima jednadžbe $x^2-Dy^2=\pm 1$.

Kad je $D\equiv 0\pmod 4$, u rješenju $(x,y)$ jednadžbe $x^2-Dy^2=\pm 4$ $x$ je sigurno paran, ali $y$ može biti neparan. Ako je u najmanjem pozitivnom cjelobrojnom rješenju $(x_1,y_1)$ jednadžbe $x^2-Dy^2=\pm 4$ $y_1$ paran, onda je i u svim rješenjima $y$ sigurno paran i tada ta cjelobrojna rješenja bijektivno odgovaraju cjelobrojnim rješenjima jednadžbe $x^2-Dy^2=\pm 1$; no ako je u najmanjem cjelobrojnom rješenju $(x_1,y_1)$ $y_1$ neparan, onda se parnost od $y_k$ podudara s parnošću od $k$ i naizmjence se mijenja, pa rješenju jednadžbe $x^2-Dy^2=\pm 1$ odgovara samo kad je $k$ paran. Ako je u najmanjem pozitivnom cjelobrojnom rješenju jednadžbe $x^2-Dy^2=\pm 4$ $y_1$ neparan, a norma od $x_1+y_1\sqrt{D}$ je $-4$, onda za takav $D$ jednadžba $x^2-Dy^2=-4$ ima rješenje, ali jednadžba $x^2-Dy^2=-1$ nema.

Kad je $D\equiv 1\pmod 4$, rješenje $(x,y)$ jednadžbe $x^2-Dy^2=\pm 4$ može biti i oba neparna i oba parna. Ako je najmanje pozitivno cjelobrojno rješenje $(x_1,y_1)$ već oba parna, onda su i sva njezina cjelobrojna rješenja sigurno oba parna, pa uvijek odgovaraju cjelobrojnim rješenjima jednadžbe $x^2-Dy^2=\pm 1$. Ako je najmanje pozitivno cjelobrojno rješenje $(x_1,y_1)$ oba neparna, vrijedi sljedeći rezultat:

???+ note "Teorem"
    Neka je $(x_1,y_1)$ najmanje pozitivno cjelobrojno rješenje jednadžbe $x^2-Dy^2=\pm 4$. Ako su $x_1$ i $y_1$ oba neparna, onda je $D\equiv 5\pmod 8$, a cjelobrojno rješenje $(x,y)$ te jednadžbe oba su parna ako i samo ako je
    
    $$
    \dfrac{x+y\sqrt{D}}{2} = \pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3k},k\in\mathbf Z.
    $$

??? note "Dokaz"
    Uzimanjem obiju strana jednakosti $x_1^2-Dy_1^2=\pm 4$ modulo $8$ dobivamo $D\equiv 5\pmod 8$. Da bismo dokazali drugu tvrdnju, najprije dokazujemo da su $(x_3,y_3)$ oba parna; budući da je
    
    $$
    \dfrac{x_3+y_3\sqrt{D}}{2} = \left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3} = \dfrac{x_1^3+3Dx_1y_1^2}{8}+\dfrac{3x_1^2y_1+Dy_1^3}{8}\sqrt{D},
    $$
    
    dovoljno je dokazati da je desna strana cjelobrojna. Budući da kvadrat neparnog broja daje ostatak $1$ modulo $8$, imamo
    
    $$
    \begin{aligned}
    &x_1^3+3Dx_1y_1^2 = x_1(x_1^2+3Dy_1^2) \equiv x_1(1+3\times 5\times 1) = 16x_1 = 0 \pmod 8,\\
    &3x_1^2y_1+Dy_1^3 = y_1(3x_1^2+Dy_1^2) \equiv y_1(3\times 1+5\times 1) = 8y_1 = 0 \pmod 8.
    \end{aligned}
    $$
    
    To pokazuje da su $x_3,y_3$ oba parna. Nadalje, za sve $k\in\mathbf Z$ vrijedi
    
    $$
    \dfrac{x+y\sqrt{D}}{2} = \pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3k} = \pm\left(\dfrac{x_3+y_3\sqrt{D}}{2}\right)^k \in \mathbf Z[\sqrt{D}],
    $$
    
    pa su tada $(x,y)$ oba parna. Obratno, za $r=1,2$ uvijek vrijedi
    
    $$
    \pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3k+r} = \pm\left(\dfrac{x_3+y_3\sqrt{D}}{2}\right)^k\left(\dfrac{x_r+y_r\sqrt{D}}{2}\right).
    $$
    
    Da bismo dokazali da pripadni $(x,y)$ nisu cijeli brojevi, dovoljno je dokazati da taj izraz nije cjelobrojan, tj. da drugi faktor u umnošku na desnoj strani nije cjelobrojan. Za $r=1$ to je upravo pretpostavka; za $r=2$, budući da je
    
    $$
    \dfrac{x_2+y_2\sqrt{D}}{2} = \left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^2 = \dfrac{x_1^2+Dy_1^2}{4} + \dfrac{x_1y_1}{2}\sqrt{D},
    $$
    
    a $x_1^2+Dy_1^2\equiv 1+1\times 1=2\pmod 4$ i $x_1y_1\equiv 1\pmod 2$, ni taj izraz nije cjelobrojan. Time je dokazano da su pripadna rješenja oba parna samo kad je eksponent višekratnik od $3$.

Drugim riječima, od svaka tri rješenja jednadžbe $x^2-Dy^2=\pm 4$ jedno je oba parno i ono odgovara cjelobrojnom rješenju jednadžbe $x^2-Dy^2=\pm 1$. To također pokazuje da za $D\equiv 1\pmod 4$ jednadžba $x^2-Dy^2=-4$ ima rješenje ako i samo ako jednadžba $x^2-Dy^2=-1$ ima rješenje.

Dosadašnje razmatranje već je dovoljno za izračun fundamentalne jedinice prstena realnih kvadratnih cijelih brojeva. Neka je $D$ pozitivan cijeli broj bez kvadratnih faktora. Za slučaj $D\equiv 2,3\pmod 4$ dovoljno je naći najmanje pozitivno cjelobrojno rješenje jednadžbe $x^2-Dy^2=\pm 1$; a za slučaj $D\equiv 1\pmod 4$ dovoljno je naći najmanje pozitivno cjelobrojno rješenje jednadžbe $x^2-Dy^2=\pm 4$. Kad dobijemo najmanje pozitivno cjelobrojno rješenje $(x,y)$, za $D\equiv 2,3\pmod 4$ fundamentalna jedinica je $\pm x\pm y\sqrt{D}$; za $D\equiv 1\pmod 4$ fundamentalna jedinica je $\dfrac{\pm x\pm y\sqrt{D}}{2}$.

??? example "Primjeri"
    1.  Riješimo jednadžbu $x^2-14y^2=\pm 4$.
    
        Iz izračuna u ranijem primjeru vidi se da je najmanje pozitivno cjelobrojno rješenje jednadžbe $x^2-14y^2=4$ jednako $(30,8)$, a jednadžba $x^2-14y^2=-4$ nema rješenja.
    2.  Riješimo jednadžbu $x^2-41y^2=\pm 4$.
    
        Rezultat izvođenja PQa algoritma za $(P_0,Q_0,D)=(1,2,41)$ je sljedeći (crveno je označen prvi period):
    
        |  $k$ | $P$ | $Q$ |        $a$       |   $A$   |   $B$  |   $G$   | $G^2-DB^2$ |
        | :--: | :-: | :-: | :--------------: | :-----: | :----: | :-----: | :--------: |
        |  $0$ | $1$ | $2$ |        $3$       |   $3$   |   $1$  |   $5$   |    $-16$   |
        |  $1$ | $5$ | $8$ | $\color{red}{1}$ |   $4$   |   $1$  |   $7$   |     $8$    |
        |  $2$ | $3$ | $4$ | $\color{red}{2}$ |   $11$  |   $3$  |   $19$  |    $-8$    |
        |  $3$ | $5$ | $4$ | $\color{red}{2}$ |   $26$  |   $7$  |   $45$  |    $16$    |
        |  $4$ | $3$ | $8$ | $\color{red}{1}$ |   $37$  |  $10$  |   $64$  |    $-4$    |
        |  $5$ | $5$ | $2$ | $\color{red}{5}$ |  $211$  |  $57$  |  $365$  |    $16$    |
        |  $6$ | $5$ | $8$ |        $1$       |  $248$  |  $67$  |  $429$  |    $-8$    |
        |  $7$ | $3$ | $4$ |        $2$       |  $707$  |  $191$ |  $1223$ |     $8$    |
        |  $8$ | $5$ | $4$ |        $2$       |  $1662$ |  $449$ |  $2875$ |    $-16$   |
        |  $9$ | $3$ | $8$ |        $1$       |  $2369$ |  $640$ |  $4098$ |     $4$    |
        | $10$ | $5$ | $2$ |        $5$       | $13507$ | $3649$ | $23365$ |    $-16$   |
        | $11$ | $5$ | $8$ |        $1$       | $15876$ | $4289$ | $27463$ |     $8$    |
    
        Duljina perioda $\ell=5$ je neparna. Najmanje pozitivno cjelobrojno rješenje jednadžbe $x^2-41y^2=-4$ je $(G_4,B_4)=(64,10)$, a najmanje pozitivno cjelobrojno rješenje jednadžbe $x^2-41y^2=4$ je $(G_9,B_9)=(4098,640)$. Među njima vrijedi sljedeća veza:
    
        $$
        \dfrac{4098+640\sqrt{41}}{2} = \left(\dfrac{64+10\sqrt{41}}{2}\right)^2.
        $$
    
        Naravno, budući da je $D\equiv 1\pmod 8$, prema ranijem rezultatu najmanja pozitivna cjelobrojna rješenja jednadžbe $x^2-41y^2=\pm 4$ sigurno su oba parna i uvijek su $2$ puta veća od najmanjih pozitivnih cjelobrojnih rješenja jednadžbe $x^2-41y^2=\pm 1$, pa se mogu dobiti i izravno iz ranijeg primjera.
    3.  Riješimo jednadžbu $x^2-13y^2=\pm 4$.
    
        Rezultat izvođenja PQa algoritma za $(P_0,Q_0,D)=(1,2,13)$ je sljedeći (crveno je označen prvi period):
    
        | $k$ | $P$ | $Q$ |        $a$       |  $A$ |  $B$ |  $G$  | $G^2-DB^2$ |
        | :-: | :-: | :-: | :--------------: | :--: | :--: | :---: | :--------: |
        | $0$ | $1$ | $2$ |        $2$       |  $2$ |  $1$ |  $3$  |    $-4$    |
        | $1$ | $3$ | $2$ | $\color{red}{3}$ |  $7$ |  $3$ |  $11$ |     $4$    |
        | $2$ | $3$ | $2$ |        $3$       | $23$ | $10$ |  $36$ |    $-4$    |
        | $3$ | $3$ | $2$ |        $3$       | $74$ | $33$ | $119$ |     $4$    |
    
        Duljina perioda $\ell=1$ je neparna. Najmanje pozitivno cjelobrojno rješenje jednadžbe $x^2-13y^2=-4$ je $(G_0,B_0)=(3,1)$, a najmanje pozitivno cjelobrojno rješenje jednadžbe $x^2-13y^2=4$ je $(G_1,B_1)=(11,3)$.
    
        Budući da su najmanja pozitivna cjelobrojna rješenja te jednadžbe oba neparna, pomoću para $(G_2,B_2)=(36,10)$ na kraju trećeg perioda možemo dobiti najmanje pozitivno cjelobrojno rješenje $(18,5)$ pripadne (negativne) Pellove jednadžbe $x^2-13y^2=\pm 1$. Ono se može dobiti i izravnim računom:
    
        $$
        \dfrac{36+10\sqrt{13}}{2}=\left(\dfrac{3+\sqrt{13}}{2}\right)^3.
        $$
    
        Štoviše, to je rješenje negativne Pellove jednadžbe. Najmanje pozitivno cjelobrojno rješenje pripadne Pellove jednadžbe je $(649,180)$.
    4.  Riješimo jednadžbu $x^2-52y^2=\pm 4$.
    
        Budući da su najmanja pozitivna cjelobrojna rješenja jednadžbe $x^2-13y^2=\pm 1$ redom $(18,5)$ i $(649,180)$, najmanja pozitivna cjelobrojna rješenja jednadžbe $x^2-52y^2=\pm 4$ redom su $(36,10)$ i $(1298,360)$.

### Opći slučaj

Na kraju razmatramo rješavanje poopćene Pellove jednadžbe.

Za slučaj $|N|<\sqrt{D}$ postoji jednostavna metoda. Raniji rezultat pokazuje da rješenje $(x,y)$ jednadžbe $x^2-Dy^2=N$ nužno zadovoljava da je $\dfrac{x}{y}$ jednak nekoj konvergenti od $\sqrt{D}$. Štoviše, prema ranije razmotrenoj strukturi rješenja, svako fundamentalno rješenje $(x,y)$ zadovoljava da je $x+y\sqrt{D}$ manji ili jednak fundamentalnom rješenju $x_1+y_1\sqrt{D}$ pripadne Pellove jednadžbe $x^2-Dy^2=1$. Iz monotonosti niza nazivnika $B_k$ u PQa algoritmu slijedi da se ta fundamentalna rješenja poopćene Pellove jednadžbe sigurno pojavljuju prije pojave fundamentalnog rješenja pripadne Pellove jednadžbe. Stoga je dovoljno izvesti PQa algoritam za $(P_0,Q_0,D)=(0,1,D)$ sve dok ne bude $Q_{\ell'}=1$ uz paran $\ell'$, a usput za svaki dobiveni $(A_k,B_k)$ provjeriti postoji li cijeli broj $f$ takav da vrijedi

$$
A_k^2-DB_k^2 = (-1)^{k+1}Q_{k+1} = N/f^2
$$

ako vrijedi, bilježimo da je $(fA_{k},fB_{k})$ jedno najmanje pozitivno cjelobrojno rješenje. Svi $(fA_k,fB_k)$ zabilježeni tim postupkom upravo su sva najmanja pozitivna cjelobrojna rješenja jednadžbe $x^2-Dy^2=N$. Pomoću $(A_{\ell'-1},B_{\ell'-1})$, tj. fundamentalnog rješenja pripadne Pellove jednadžbe, iz tih nađenih najmanjih pozitivnih cjelobrojnih rješenja možemo generirati sva rješenja poopćene Pellove jednadžbe. Uočimo da, ovisno o tome je li duljina perioda $\ell$ parna ili neparna, gornji $\ell'$ može biti $\ell$ ili $2\ell$.

Za općenitiji $N$ gornja metoda više ne vrijedi. Najprije nabrajamo sve kvadratne faktore $f^2$ od $N$, stavljamo $m=N/f^2$ i nabrajamo sva rješenja $z$ kongruencije $z^2\equiv D\pmod{|m|}$ koja zadovoljavaju $-|m|/2<z \le |m|/2$. Zatim izvodimo PQa algoritam za $(P_0,Q_0,D)=(z,|m|,D)$ sve dok ne bude $Q_k=\pm 1$ ili dok ne završi jedan period. U drugom slučaju rješenje jednadžbe povezano s tim parom $(f,z)$ ne postoji. U prvom slučaju treba dodatno provjeriti vrijedi li $(-1)^kQ_k=N/|N|$. Ako se predznaci podudaraju, $(fG_{k-1},fB_{k-1})$ je rješenje jednadžbe $x^2-Dy^2=N$. Inače je ono rješenje jednadžbe $x^2-Dy^2=-N$, i rješenje jednadžbe $x^2-Dy^2=N$ iz njega možemo dobiti slaganjem s fundamentalnim rješenjem pripadne negativne Pellove jednadžbe ako i samo ako rješenje te negativne Pellove jednadžbe postoji. Kad prođemo sve parove $(f,z)$, dobivamo u svakoj klasi ekvivalencije rješenja jednadžbe $x^2-Dy^2=N$ po točno jedno rješenje, i to fundamentalno rješenje ili najmanje pozitivno cjelobrojno rješenje te klase ekvivalencije. Pomoću njih i fundamentalnog rješenja pripadne Pellove jednadžbe mogu se generirati sva cjelobrojna rješenja te jednadžbe. Taj se algoritam naziva **Lagrange–Matthews–Mollinov algoritam**.

Točnost tog algoritma jamči sljedeći teorem:

???+ note "Teorem"
    Neka jednadžba $x^2-Dy^2=N$ ima cjelobrojno rješenje $(x,y)$ uz $x\ge 0, y>0,\gcd(x,y)=1$. Stavimo $Q_0=|N|$; tada je $\gcd(Q_0,y)=1$. Neka je $P_0$ rješenje kongruencije $x\equiv -P_0y\pmod{Q_0}$ uz $-Q_0/2<P_0\le Q_0/2$, i neka je $X$ cijeli broj za koji vrijedi $x=Q_0X-P_0y$. Tada je $P_0^2\equiv D\pmod{Q_0}$, $\dfrac{X}{y}$ je neka konvergenta $\dfrac{A_{k-1}}{B_{k-1}}$ od $\omega=\dfrac{P_0+\sqrt{D}}{Q_0}$, i $Q_k=(-1)^k\dfrac{N}{|N|}$.

??? note "Dokaz"
    Iz $x\equiv -P_0y\pmod{Q_0}$ i $x^2-Dy^2=N\equiv 0\pmod{Q_0}$ očito slijedi $P_0^2\equiv D\pmod{Q_0}$. Stoga je
    
    $$
    P_0x+Dy\equiv -P_0^2y+Dy = (D-P_0^2)y\equiv 0\pmod{Q_0}.
    $$
    
    Na temelju toga možemo promatrati cjelobrojnu matricu
    
    $$
    \begin{pmatrix}P & R \\ Q & S\end{pmatrix}
    =
    \begin{pmatrix}X & \dfrac{P_0x+Dy}{Q_0} \\ y & x\end{pmatrix}.
    $$
    
    Njezina je determinanta
    
    $$
    PS-QR = \dfrac{x(x+P_0y)-y(P_0x+Dy)}{Q_0} = \dfrac{x^2-Dy^2}{Q_0} = \pm 1.
    $$
    
    Štoviše, stavimo li $\zeta =\sqrt{D} > 1$, imamo
    
    $$
    \dfrac{P\zeta+R}{Q\zeta+S} = \dfrac{(x+P_0y)\sqrt{D}+(P_0x+Dy)}{(x+y\sqrt{D})Q_0} = \dfrac{P_0+\sqrt{D}}{Q_0} = \omega.
    $$
    
    Sada treba dokazati da je $\dfrac{P}{Q}$ konvergenta od $\omega$. Neka $\dfrac{P}{Q}$ ima [razvoj u verižni razlomak](./continued-fraction.md#简单连分数)
    
    $$
    \dfrac{P}{Q} = [a_0,a_1,\cdots,a_k]
    $$
    
    takav da je $PS-QR = (-1)^{k-1}$. Ako je $\dfrac{p_k}{q_k}$ njegova $k$-ta konvergenta, onda je $(p_k,q_k)=(P,Q)$, a prema [formuli za razliku konvergenti](./continued-fraction.md#误差估计) vrijedi $p_kq_{k-1}-q_kp_{k-1}=(-1)^{k-1}$. To znači
    
    $$
    p_k(S-q_{k-1}) = q_k(R-p_{k-1}).
    $$
    
    Razlikujemo slučajeve:
    
    -   Ako je $S=0$, lako se provjeri da je $Q=R=1$, pa je $\omega=P+\zeta^{-1}=[P,\zeta]$ i stoga je $\dfrac{P}{Q}=P$ $0$. konvergenta od $\omega$;
    -   Ako je $Q=S>0$, onda je $Q=S=1$ i $P-R=\pm 1$. Tada,
        -   ako je $P=R+1$, onda je $\omega=R+\dfrac{1}{1+\zeta^{-1}}=[R,1,\zeta]$, pa je $\dfrac{P}{Q}=\dfrac{R+1}{1}=[R,1]$ $1$. konvergenta od $\omega$;
        -   ako je $P=R-1$, onda je $\omega=R-1+\dfrac{1}{1+\zeta}=[R-1,\zeta-1]$, pa je $\dfrac{P}{Q}=R-1$ $0$. konvergenta od $\omega$;
    -   Ako je $Q\neq S>0$, onda zbog $Q=q_k\mid(S-q_{k-1})$ uvijek postoji cijeli broj $\kappa$ takav da vrijedi $S=\kappa q_k+q_{k-1}$ i $R=\kappa p_k+p_{k-1}$. Budući da je $q_k\ge q_{k-1}$ i $S>0$, vrijedi $\kappa\ge 0$. Stoga je $\omega=\dfrac{(\kappa+\zeta)p_k+p_{k-1}}{(\kappa+\zeta)q_k+q_{k-1}}=[a_0,a_1,\cdots,a_k,\kappa+\zeta]$, pa je $\dfrac{P}{Q}$ njegova $k$-ta konvergenta.
    
    Sve u svemu, $\dfrac{X}{y}$ je uvijek konvergenta od $\omega=\dfrac{P_0+\sqrt{D}}{Q_0}$ i u oznakama PQa algoritma zapisujemo je kao $\dfrac{A_{k-1}}{B_{k-1}}$. Budući da je $A_{k-1}^2-DB_{k-1}^2=(-1)^kQ_0Q_k$, vrijedi $Q_k=(-1)^k\dfrac{N}{|N|}$.

Taj teorem jamči da se sva pozitivna rješenja jednadžbe nalaze među konvergentama pripadnih kvadratnih iracionalnosti. Budući da pri računanju konvergenti PQa algoritmom, čim uđemo u period, konvergente sigurno postaju pozitivne, dovoljno je nabrojiti sve kvadratne iracionalnosti dopuštene uvjetima teorema i izračunati njihove konvergente do kraja jednog perioda da bismo našli rješenje. Budući da su dva rješenja koja se pojave među konvergentama iste kvadratne iracionalnosti nužno ekvivalentna, čim dobijemo prvo rješenje koje zadovoljava $(-1)^kQ_k=N/|N|$, možemo prekinuti daljnji račun. Za razliku od svih prethodnih algoritama, ovdje se odgovarajući $k$ može pojaviti i prije ulaska u period.

??? example "Primjeri"
    1.  Riješimo jednadžbu $x^2-157y^2=12$.
    
        Budući da je $12^2<157$, izvodimo PQa algoritam za $(P_0,Q_0,D)=(0,1,157)$; rezultat je sljedeći (crveno je označen prvi period):
    
        |  $k$ |  $P$ |  $Q$ |        $a$        |         $A$        |        $B$       |         $G$        | $G^2-DB^2$ |
        | :--: | :--: | :--: | :---------------: | :----------------: | :--------------: | :----------------: | :--------: |
        |  $0$ |  $0$ |  $1$ |        $12$       |        $12$        |        $1$       |        $12$        |    $-13$   |
        |  $1$ | $12$ | $13$ |   $\color{red}1$  |        $13$        |        $1$       |        $13$        |    $12$    |
        |  $2$ |  $1$ | $12$ |   $\color{red}1$  |        $25$        |        $2$       |        $25$        |    $-3$    |
        |  $3$ | $11$ |  $3$ |   $\color{red}7$  |        $188$       |       $15$       |        $188$       |    $19$    |
        |  $4$ | $10$ | $19$ |   $\color{red}1$  |        $213$       |       $17$       |        $213$       |    $-4$    |
        |  $5$ |  $9$ |  $4$ |   $\color{red}5$  |       $1253$       |       $100$      |       $1253$       |     $9$    |
        |  $6$ | $11$ |  $9$ |   $\color{red}2$  |       $2719$       |       $217$      |       $2719$       |    $-12$   |
        |  $7$ |  $7$ | $12$ |   $\color{red}1$  |       $3972$       |       $317$      |       $3972$       |    $11$    |
        |  $8$ |  $5$ | $11$ |   $\color{red}1$  |       $6691$       |       $534$      |       $6691$       |    $-11$   |
        |  $9$ |  $6$ | $11$ |   $\color{red}1$  |       $10663$      |       $851$      |       $10663$      |    $12$    |
        | $10$ |  $5$ | $12$ |   $\color{red}1$  |       $17354$      |      $1385$      |       $17354$      |    $-9$    |
        | $11$ |  $7$ |  $9$ |   $\color{red}2$  |       $45371$      |      $3621$      |       $45371$      |     $4$    |
        | $12$ | $11$ |  $4$ |   $\color{red}5$  |      $244209$      |      $19490$     |      $244209$      |    $-19$   |
        | $13$ |  $9$ | $19$ |   $\color{red}1$  |      $289580$      |      $23111$     |      $289580$      |     $3$    |
        | $14$ | $10$ |  $3$ |   $\color{red}7$  |      $2271269$     |     $181267$     |      $2271269$     |    $-12$   |
        | $15$ | $11$ | $12$ |   $\color{red}1$  |      $2560849$     |     $204378$     |      $2560849$     |    $13$    |
        | $16$ |  $1$ | $13$ |   $\color{red}1$  |      $4832118$     |     $385645$     |      $4832118$     |    $-1$    |
        | $17$ | $12$ |  $1$ | $\color{red}{24}$ |     $118531681$    |     $9459858$    |     $118531681$    |    $13$    |
        | $18$ | $12$ | $13$ |        $1$        |     $123363799$    |     $9845503$    |     $123363799$    |    $-12$   |
        | $19$ |  $1$ | $12$ |        $1$        |     $241895480$    |    $19305361$    |     $241895480$    |     $3$    |
        | $20$ | $11$ |  $3$ |        $7$        |    $1816632159$    |    $144983030$   |    $1816632159$    |    $-19$   |
        | $21$ | $10$ | $19$ |        $1$        |    $2058527639$    |    $164288391$   |    $2058527639$    |     $4$    |
        | $22$ |  $9$ |  $4$ |        $5$        |    $12109270354$   |    $966424985$   |    $12109270354$   |    $-9$    |
        | $23$ | $11$ |  $9$ |        $2$        |    $26277068347$   |   $2097138361$   |    $26277068347$   |    $12$    |
        | $24$ |  $7$ | $12$ |        $1$        |    $38386338701$   |   $3063563346$   |    $38386338701$   |    $-11$   |
        | $25$ |  $5$ | $11$ |        $1$        |    $64663407048$   |   $5160701707$   |    $64663407048$   |    $11$    |
        | $26$ |  $6$ | $11$ |        $1$        |   $103049745749$   |   $8224265053$   |   $103049745749$   |    $-12$   |
        | $27$ |  $5$ | $12$ |        $1$        |   $167713152797$   |   $13384966760$  |   $167713152797$   |     $9$    |
        | $28$ |  $7$ |  $9$ |        $2$        |   $438476051343$   |   $34994198573$  |   $438476051343$   |    $-4$    |
        | $29$ | $11$ |  $4$ |        $5$        |   $2360093409512$  |  $188355959625$  |   $2360093409512$  |    $19$    |
        | $30$ |  $9$ | $19$ |        $1$        |   $2798569460855$  |  $223350158198$  |   $2798569460855$  |    $-3$    |
        | $31$ | $10$ |  $3$ |        $7$        |  $21950079635497$  |  $1751807067011$ |  $21950079635497$  |    $12$    |
        | $32$ | $11$ | $12$ |        $1$        |  $24748649096352$  |  $1975157225209$ |  $24748649096352$  |    $-13$   |
        | $33$ |  $1$ | $13$ |        $1$        |  $46698728731849$  |  $3726964292220$ |  $46698728731849$  |     $1$    |
        | $34$ | $12$ |  $1$ |        $24$       | $1145518138660728$ | $91422300238489$ | $1145518138660728$ |    $-13$   |
        | $35$ | $12$ | $13$ |        $1$        | $1192216867392577$ | $95149264530709$ | $1192216867392577$ |    $12$    |
    
        Duljina perioda $\ell=17$ je neparna, pa unutar dvaju perioda treba promotriti slučajeve u kojima se $G_k^2-157B_k^2$ razlikuje od $12$ za kvadratni faktor, tj. slučajeve $k=1,9,13,19,23,31$. Pripadna rješenja su $(fG,fB)$ iz sljedeće tablice:
    
        |  $k$ | $f$ |      $fG_k$      |      $fB_k$     |    $x$    |   $y$   |
        | :--: | :-: | :--------------: | :-------------: | :-------: | :-----: |
        |  $1$ | $1$ |       $13$       |       $1$       |    $13$   |   $1$   |
        |  $9$ | $1$ |      $10663$     |      $851$      |  $10663$  |  $851$  |
        | $13$ | $2$ |     $579160$     |     $46222$     |  $579160$ | $46222$ |
        | $19$ | $2$ |    $483790960$   |    $38610722$   | $-579160$ | $46222$ |
        | $23$ | $1$ |   $26277068347$  |   $2097138361$  |  $-10663$ |  $851$  |
        | $31$ | $1$ | $21950079635497$ | $1751807067011$ |   $-13$   |   $1$   |
    
        Svi $(fG,fB)$ upravo su najmanja pozitivna cjelobrojna rješenja u svim klasama ekvivalencije skupa rješenja jednadžbe $x^2-157y^2=12$. Da bismo iz tih rješenja dobili sva rješenja, možemo iskoristiti fundamentalno rješenje $(46698728731849,3726964292220)$ pripadne Pellove jednadžbe. Primjerice, možemo ih pretvoriti u fundamentalna rješenja $(x,y)$ svojih klasa ekvivalencije; ta su rješenja također navedena u gornjoj tablici.
    2.  Riješimo jednadžbu $x^2-157y^2=12$.
    
        Ovaj put rješavamo Lagrange–Matthews–Mollinovim algoritmom. Najprije nabrajamo kvadratne faktore od $N=12$:
    
        -   za $f^2=1^2$ imamo $m=12$, a kongruencija $z^2\equiv 157\pmod{12}$ ima rješenja $z=\pm 1,\pm 5$;
        -   za $f^2=2^2$ imamo $m=3$, a kongruencija $z^2\equiv 157\pmod{3}$ ima rješenja $z=\pm 1$.
    
        Za sve moguće kombinacije $(f,z)$ izvodimo PQa algoritam s početnim parametrima $(P_0,Q_0,D)=(z,|m|,D)$ i tražimo prvo mjesto na kojem je $(-1)^kQ_k=1$; pripadni $(fG_{k-1},fB_{k-1})$ je jedno rješenje. Rezultati su u sljedećoj tablici:
    
        | $f$ |  $z$ |  $m$ |  $k$ |    $fG_{k-1}$    |    $fB_{k-1}$   |
        | :-: | :--: | :--: | :--: | :--------------: | :-------------: |
        | $1$ |  $1$ | $12$ | $32$ | $21950079635497$ | $1751807067011$ |
        | $1$ | $-1$ | $12$ |  $2$ |       $13$       |       $1$       |
        | $1$ |  $5$ | $12$ | $24$ |   $26277068347$  |   $2097138361$  |
        | $1$ | $-5$ | $12$ | $10$ |      $10663$     |      $851$      |
        | $2$ |  $1$ |  $3$ | $20$ |    $483790960$   |    $38610722$   |
        | $2$ | $-1$ |  $3$ | $14$ |     $579160$     |     $46222$     |
    
        To su upravo ranije navedena najmanja pozitivna cjelobrojna rješenja svih klasa ekvivalencije; pomoću fundamentalnog rješenja Pellove jednadžbe mogu se pretvoriti u fundamentalna rješenja.
    3.  Riješimo jednadžbu $x^2-79y^2=\pm 101$.
    
        I dalje koristimo Lagrange–Matthews–Mollinov algoritam. Budući da je $N=101$ prost, sigurno je $f=1$. Tada je $m=101$, a pripadna kongruencija $z^2\equiv 79\pmod{101}$ ima rješenja $z=\pm 33$.
    
        Rezultat izvođenja PQa algoritma za $(P_0,Q_0,D)=(33,101,79)$ je sljedeći (crveno je označen prvi period):
    
        | $k$ |  $P$  |  $Q$  |       $a$      |  $A$  |   $B$  |   $G$   | $G^2-DB^2$ |
        | :-: | :---: | :---: | :------------: | :---: | :----: | :-----: | :--------: |
        | $0$ |  $33$ | $101$ |       $0$      |  $0$  |   $1$  |  $-33$  |   $1010$   |
        | $1$ | $-33$ | $-10$ |       $2$      |  $1$  |   $2$  |   $35$  |    $909$   |
        | $2$ |  $13$ |  $9$  |       $2$      |  $2$  |   $5$  |   $37$  |   $-606$   |
        | $3$ |  $5$  |  $6$  | $\color{red}2$ |  $5$  |  $12$  |  $109$  |    $505$   |
        | $4$ |  $7$  |  $5$  | $\color{red}3$ |  $17$ |  $41$  |  $364$  |   $-303$   |
        | $5$ |  $8$  |  $3$  | $\color{red}5$ |  $90$ |  $217$ |  $1929$ |   $1010$   |
        | $6$ |  $7$  |  $10$ | $\color{red}1$ | $107$ |  $258$ |  $2293$ |   $-707$   |
        | $7$ |  $3$  |  $7$  | $\color{red}1$ | $197$ |  $475$ |  $4222$ |    $909$   |
        | $8$ |  $4$  |  $9$  | $\color{red}1$ | $304$ |  $733$ |  $6515$ |   $-606$   |
        | $9$ |  $5$  |  $6$  |       $2$      | $805$ | $1941$ | $17252$ |    $505$   |
    
        Duljina perioda $\ell=6$ je parna. Sve do kraja jednog perioda ne pojavljuje se $Q_k=\pm 1$, pa u tom slučaju nema rješenja. Slično se može uočiti i pri izvođenju PQa algoritma za $(P_0,Q_0,D)=(-33,101,79)$. Stoga ta jednadžba nema rješenja.

## Zadaci

-   [LOJ 6687.「Project Euler 66」解方程 (Rješavanje jednadžbe)](https://loj.ac/p/6687)
-   [SPOJ EQU2 - Yet Another Equation](https://www.spoj.com/problems/EQU2/)
-   [SPOJ PELL2 - Pell (Mid pelling)](https://www.spoj.com/problems/PELL2/)
-   [UVa 12909. Numeric Center](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4774)
-   [UVa 10241. Semi-triangular and also Square](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=14&page=show_problem&problem=1182)

## Literatura i napomene

-   [Pell's equation - Wikipedia](https://en.wikipedia.org/wiki/Pell%27s_equation)
-   [John P. Robertson - Solving the generalized Pell equation $x^2-Dy^2=N$](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=5ac34a344ee346855184ff949eeaed18685b155c)
-   [Keith Matthews - The Diophantine Equation $x^2-Dy^2=N$,$D>0$](http://www.numbertheory.org/PDFS/patz5.pdf)
-   [Existence of Solution to Pell’s Equation - Suryateja Gavva's Blog](https://surya-teja.com/2011/01/11/existence-of-solution-to-pells-equation/)
-   [Calculating the simple continued fraction of a quadratic irrational - Number Theory Web](http://www.numbertheory.org/php/surd.html) (PQa algoritam)
-   [Solving the diophantine equation x2–Dy2 = N, D > 0 and not a perfect square, N ≠ 0 - Number Theory Web](http://www.numbertheory.org/php/patz.html) (Lagrange–Matthews–Mollinov algoritam)

[^not-square]: Kad je $D$ potpun kvadrat, izravnim rastavom na faktore dobivamo $(x+y\sqrt{D})(x-y\sqrt{D})=N$, pa se sva rješenja mogu naći prolaskom po djeliteljima od $N$. Posebno, za $N=1$ jednadžba ima samo rješenja $(\pm 1,0)$; za $N=-1$ i $D\neq 1$ jednadžba nema rješenja.

[^neg-pell]: U nekoj kineskoj literaturi naziva se i Pellovom jednadžbom druge vrste.

[^half-int]: Tj. racionalni brojevi oblika $n+\dfrac12$ uz $n\in\mathbf Z$.

[^fundamental-solution]: Uočimo da se definicija fundamentalnog rješenja Pellove jednadžbe ne podudara s definicijom fundamentalne jedinice prstena realnih kvadratnih cijelih brojeva. Prvo, u nekim prstenima realnih kvadratnih cijelih brojeva fundamentalna jedinica $x+y\sqrt{D}$ ima polucijele $x,y$, pa nije rješenje Pellove jednadžbe. Drugo, isti prsten realnih kvadratnih cijelih brojeva ima četiri fundamentalne jedinice, ali fundamentalno rješenje je samo jedno, jer se za fundamentalno rješenje zahtijeva da su $x,y$ oba pozitivna.

[^solubility-neg-pell]: Praktičniji kriterij i alat nalaze se [ovdje](http://www.numbertheory.org/php/hardy_williams.html) i u ondje navedenoj literaturi. Popis pozitivnih cijelih brojeva $D$ za koje jednadžba $x^2-Dy^2=-1$ ima rješenje je [OEIS A031396](https://oeis.org/A031396).
