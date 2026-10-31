---
title: Formula uključivanja-isključivanja
---

## Uvod

???+ note "Uvodni primjer"
    Pretpostavimo da u razredu $10$ učenika voli matematiku, $15$ učenika voli kineski jezik, a $21$ učenik voli programiranje. Koliko učenika u razredu voli barem jedan predmet?

Je li to $10+15+21=46$ učenika? Nije, jer neki učenici možda istodobno vole matematiku i kineski jezik, ili kineski jezik i programiranje, a možda čak i sve troje.

Radi jednostavnosti, skupove učenika koji vole kineski jezik, matematiku odnosno programiranje označimo redom s $A,B,C$; tada je ukupan broj učenika jednak $|A\cup B\cup C|$. Kako smo upravo rekli, ako jednostavno zbrojimo brojeve elemenata $|A|,|B|,|C|$ tih triju skupova, neki će elementi biti prebrojeni više puta, pa treba oduzeti $|A\cap B|,|B\cap C|,|C\cap A|$; no time je jedan mali dio oduzet previše puta i treba ga vratiti, naime $|A\cap B\cap C|$. Dakle

$$
|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|B\cap C|-|C\cap A|+|A\cap B\cap C|
$$

![Formula uključivanja-isključivanja – primjer Vennova dijagrama](./images/incexcp.png)

Poopćimo li gornji problem na opći slučaj, dobivamo dobro poznatu formulu uključivanja-isključivanja (inclusion–exclusion principle).

## Definicija

Neka elementi skupa U imaju n različitih svojstava, neka se i-to svojstvo zove $P_i$, a elementi koji imaju svojstvo $P_i$ neka čine skup $S_i$. Tada je

$$
\begin{aligned}
\left|\bigcup_{i=1}^{n}S_i\right|=&\sum_{i}|S_i|-\sum_{i<j}|S_i\cap S_j|+\sum_{i<j<k}|S_i\cap S_j\cap S_k|-\cdots\\
&+(-1)^{m-1}\sum_{a_i<a_{i+1} }\left|\bigcap_{i=1}^{m}S_{a_i}\right|+\cdots+(-1)^{n-1}|S_1\cap\cdots\cap S_n|
\end{aligned}
$$

odnosno

$$
\left|\bigcup_{i=1}^{n}S_i\right|=\sum_{m=1}^n(-1)^{m-1}\sum_{a_i<a_{i+1} }\left|\bigcap_{i=1}^mS_{a_i}\right|
$$

### Dokaz

Za svaki element binomnim teoremom izračunamo koliko je puta prebrojen. Za element x pretpostavimo da se pojavljuje u skupovima $T_1,T_2,\cdots,T_m$; tada je broj njegovih pojavljivanja

$$
\begin{aligned}
Cnt=&|\{T_i\}|-|\{T_i\cap T_j|i<j\}|+\cdots+(-1)^{k-1}\left|\left\{\bigcap_{i=1}^{k}T_{a_i}|a_i<a_{i+1}\right\}\right|\\
&+\cdots+(-1)^{m-1}|\{T_1\cap\cdots\cap T_m\}|\\
=&\dbinom{m}{1}-\dbinom{m}{2}+\cdots+(-1)^{m-1}\dbinom{m}{m}\\
=&\dbinom{m}{0}-\sum_{i=0}^m(-1)^i\dbinom{m}{i}\\
=&1-(1-1)^m=1
\end{aligned}
$$

Dakle, svaki je element prebrojen točno jednom, pa sve zajedno daje uniju. Time je dokaz završen.

### Komplement

Za **uniju skupova** unutar univerzalnog skupa U može se koristiti formula uključivanja-isključivanja, dok se presjek skupova dobiva tako da se od univerzalnog skupa oduzme **unija komplemenata**:

$$
\left|\bigcap_{i=1}^{n}S_i\right|=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|
$$

Na desnu stranu dovoljno je primijeniti uključivanje-isključivanje.

Čitateljima koji su se već susreli s uključivanjem-isključivanjem gornje je gradivo poznato; njih više zanimaju primjene.

Stoga ćemo u nastavku dati 3 primjera različitih razina težine kako bismo pokazali primjenu formule uključivanja-isključivanja.

## Prebrojavanje nenegativnih cjelobrojnih rješenja neodređene jednadžbe

???+ note "Prebrojavanje nenegativnih cjelobrojnih rješenja neodređene jednadžbe"
    Zadana je neodređena jednadžba $\sum_{i=1}^nx_i=m$ i $n$ ograničenja $x_i\leq b_i$, gdje je $m,b_i \in \mathbb{N}$. Odredite broj nenegativnih cjelobrojnih rješenja jednadžbe.

### Bez ograničenja

Ako nema ograničenja $x_i\leq b_i$, broj nenegativnih cjelobrojnih rješenja neodređene jednadžbe $\sum_{i=1}^nx_i=m$ jednak je $\dbinom{m+n-1}{n-1}$.

Skica dokaza: metoda pregrada (stars and bars).

To je isto kao da $m$ kuglica treba razdijeliti u $n$ kutija, pri čemu neka kutija smije ostati prazna. Taj se problem ne može izravno riješiti binomnim koeficijentom.

Zato dodamo još $n-1$ kuglicu; problem tada postaje: u nizu od $m+n-1$ kuglice odabrati $n-1$ kuglicu, a tih $n-1$ kuglica dijeli niz na $n$ dijelova koji točno odgovaraju (jedan na jedan) $n$ kutijama. Broj načina da se među $m+n-1$ kuglicom odabere $n-1$ kuglica jest $\dbinom{m+n-1}{n-1}$.

### Model uključivanja-isključivanja

Pokušajmo zatim apstrahirati model formule uključivanja-isključivanja:

1.  Univerzalni skup U: nenegativna cjelobrojna rješenja neodređene jednadžbe $\sum_{i=1}^nx_i=m$
2.  Elementi: varijable $x_i$.
3.  Svojstva: svojstvo varijable $x_i$ jest uvjet koji $x_i$ zadovoljava, tj. uvjet $x_i\leq b_i$

Cilj: veličina skupa u kojem sve varijable zadovoljavaju pripadna svojstva, tj. $|\bigcap_{i=1}^nS_i|$.

To se može izračunati pomoću $\left|\bigcap_{i=1}^{n}S_i\right|=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|$. $|U|$ se računa binomnim koeficijentom, a drugi se dio prirodno razvija formulom uključivanja-isključivanja.

Problem se tako svodi na računanje veličine presjeka nekih skupova $\overline{S_{a_i}}$. Razmotrimo značenje skupa $\overline{S_{a_i} }$: on označava broj rješenja za koja je $x_{a_i}\geq b_{a_i}+1$, a presjek znači da su svi ti uvjeti ispunjeni istodobno. Stoga u neodređenoj jednadžbi koja odgovara tom presjeku neke varijable imaju **ograničenje odozdo**, a neke nemaju nikakvo ograničenje.

Možemo li se riješiti tih donjih ograničenja? Budući da tražimo nenegativna cjelobrojna rješenja, a donje su granice nekih varijabli veće od $0$, jednostavno **oduzmemo tu donju granicu** i donja granica tih varijabli postaje $0$, tj. nestaje. Stoga za

$$
\left|\bigcap_{a_i<a_{i+1} }^{1\leq i\leq k}S_{a_i}\right|
$$

pripadna neodređena jednadžba glasi

$$
\sum_{i=1}^nx_i=m-\sum_{i=1}^k(b_{a_i}+1)
$$

pa se i to može izračunati binomnim koeficijentom. Niz $a$ duljine $k$ zapravo odgovara nabrajanju podskupova.

## HAOI2008 硬币购物 (Kupovina novčićima)

???+ note "HAOI2008 硬币购物 (Kupovina novčićima)"
    Postoje 4 vrste novčića; novčić i-te vrste ima vrijednost $C_i$. Slijedi $n$ upita; u svakom su upitu zadani broj novčića $D_i$ svake vrste i cijena $S$, a pitanje je na koliko se načina može platiti.
    
    $n\leq 10^3,S\leq 10^5$.

Rješavanje ruksakom (knapsack) imalo bi složenost $O(4nS)$, što je neprihvatljivo. Najuočljivija značajka ovog zadatka jest da postoje samo četiri vrste novčića. Apstrahiramo li model, zapravo tražimo broj nenegativnih cjelobrojnih rješenja jednadžbe $\sum_{i=1}^4C_ix_i=S,x_i\leq D_i$.

Primijenimo isto uključivanje-isključivanje: svojstvo varijable $x_i$ jest $x_i\leq D_i$. Uvrstimo li u formulu uključivanja-isključivanja, na kraju treba riješiti

$$
\sum_{i=1}^4C_ix_i=S-\sum_{i=1}^kC_{a_i}(D_{a_i}+1)
$$

što je neograničeni ruksak (unbounded knapsack). Taj se problem može unaprijed izračunati, pa je ukupna složenost zajedno s upitima $O(4S+2^4n)$.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/math/code/inclusion-exclusion-principle/inclusion-exclusion-principle_1.cpp"
    ```

## Problem bojenja podgrafova potpunog grafa

Prethodna su tri zadatka bila izravna primjena formule uključivanja-isključivanja; ovaj zadatak zahtijeva njezinu primjenu u obrnutom smjeru.

???+ note "Problem bojenja podgrafova potpunog grafa"
    A i B vole bojiti grafove (ne nužno povezane), a pravilo im je da susjedni vrhovi moraju biti obojeni istom bojom. Danas A i B igraju igru na **potpunom grafu** $G=(V,E)$ reda $n$. Definiraju funkciju vrijednosti $F(S)$, gdje je S skup bridova, $S\subseteq E$. Vrijednost $F(S)$ jest ukupan broj načina bojenja grafa $G'=(V,S)$ s $m$ boja. Drugo im je pravilo: ako je $|S|$ neparan, rezultat igrača A povećava se za $F(S)$, inače se rezultat igrača B povećava za $F(S)$. Pitanje je kolika je razlika rezultata igrača A i B.

### Matematički oblik

Na prvi pogled nije očito kojim algoritmom pristupiti ovom zadatku, pa za ovakve nezgodne zadatke prvo apstrahiramo matematički oblik. Razlika rezultata zapravo je razlika po parnosti, pa se kao koeficijent može uzeti potencija broja -1. Tražimo

$$
Ans=\sum_{S\subseteq E}(-1)^{|S|-1}F(S)
$$

### Model uključivanja-isključivanja

Uvjet da su susjedni vrhovi obojeni istom bojom shvatimo kao svojstvo. Ovdje se najprije ne držimo pravila bojenja, nego pretpostavimo da graf izravno bojimo s m boja. Graf $G'=(V,S)$ shvaćamo kao **element**. **Svojstvo** $x_i=x_j$ znači da su vrhovi i,j obojeni istom bojom (uočite da se ne zahtijeva da između i i j postoji brid).

**Skup** koji odgovara svojstvu $x_i=x_j$ definiramo kao $Q_{i,j}$; on sadrži sva bojenja grafova $G'$ koja zadovoljavaju to svojstvo, njegova je veličina broj bojenja koja zadovoljavaju to svojstvo, a njegovi su elementi obojeni grafovi $G'$ koji zadovoljavaju to svojstvo.

Vratimo se zadatku: „susjedni vrhovi moraju biti obojeni istom bojom” može se shvatiti kao presjek nekoliko skupova $Q$. Stoga možemo zapisati

$$
F(S)=\left|\bigcap_{(i,j)\in S}Q_{i,j}\right|
$$

Desna strana gornje jednakosti označava broj bojenja za koja za svaki brid $(i,j)$ iz S vrijedi $x_i=x_j$, a to je upravo $F(S)$.

Zar ne miriše na uključivanje-isključivanje? Budući da formula uključivanja-isključivanja sama po sebi nema oblik s uređenim parovima, **sve** bridove $(i,j)$ preslikamo na $T=\frac{n(n+1)}{2}$ cijelih brojeva: pretpostavimo da se $(i,j)$ preslikava u $k,1\leq k\leq T$, a istodobno se $Q_{i,j}$ preslikava u $Q_k$. Svojstvo $x_i=x_j$ tada definiramo kao $P_k$.

Istodobno se S može prikazati kao skup nekoliko brojeva k, tj. $S\iff K=\{k_1,k_2,\cdots,k_m\}$. (Drugim riječima, uspostavili smo ekvivalenciju između skupova bridova i skupova brojeva.)

A skupu E odgovara skup $M=\left\{1,2,\cdots,\frac{n(n+1)}{2}\right\}$. Dakle

$$
F(S)\iff F(\{ {k_i}\})=\left|\bigcap_{k_i}Q_{k_i}\right|
$$

### Analiza u obrnutom smjeru

Razvijmo traženi izraz

$$
\begin{aligned}
Ans &= \sum_{K\subseteq M}(-1)^{|K|-1}\left|\bigcap_{k_i\in K}Q_{k_i}\right|\\
    &= \sum_{i}|Q_i|-\sum_{i<j}|Q_i\cap Q_j|+\sum_{i<j<k}|Q_i\cap Q_j\cap Q_k|-\cdots+(-1)^{T-1}\left|\bigcap_{i=1}^TQ_i\right|
\end{aligned}
$$

i pojavljuje se razvijeni oblik formule uključivanja-isključivanja; stoga ovaj izraz izvedemo u obrnutom smjeru

$$
Ans=\left|\bigcup_{i=1}^TQ_i\right|
$$

Razmotrimo sada značenje desne strane: dovoljno je da bude ispunjen bilo koji od uvjeta $1\sim T$, tj. to je broj bojenja u kojima postoje dva vrha iste boje (ne nužno susjedna)! Znamo da je univerzalni skup svih bojenja $U$ i očito je $|U|=m^n$. Prijelazom na komplement tražimo broj bojenja u kojima su svaka dva vrha različite boje, tj. $A_m^n=\frac{m!}{(m-n)!}$. Stoga

$$
Ans=m^n-A_m^n
$$

Pri rješavanju ovog zadatka najprije smo apstrahirali njegov matematički oblik, zatim krenuli od uvjeta u zadatku koji nosi najviše informacija, definicije funkcije $F(S)$, i pretvorili je u presjek, uniju i komplement skupova. Potom smo izraz pretvorili u oblik formule uključivanja-isključivanja i **izvođenjem u obrnutom smjeru** dobili konačni rezultat. Ovaj zadatak pokazuje upravo obrnutu primjenu formule uključivanja-isključivanja.

## Uključivanje-isključivanje u teoriji brojeva

Formulom uključivanja-isključivanja mogu se elegantno riješiti neki problemi iz teorije brojeva.

### Broj parova s najvećim zajedničkim djeliteljem k pomoću uključivanja-isključivanja

Razmotrimo sljedeći problem:

???+ note "Broj parova s najvećim zajedničkim djeliteljem $k$"
    Neka je $1 \le x, y \le N$ i neka $f(k)$ označava broj uređenih parova $(x, y)$ čiji je najveći zajednički djelitelj $k$. Odredite vrijednosti $f(1)$ do $f(N)$.

Ovaj se zadatak svakako može riješiti Eulerovom funkcijom ili Möbiusovom inverzijom, ali nijedan od tih načina nije tako jednostavan kao formula uključivanja-isključivanja.

Prema formuli uključivanja-isključivanja, najprije pronađemo sve parove kojima je $k$ **zajednički djelitelj**, zatim iz njih izbacimo sve parove kojima je neki višekratnik od $k$ **zajednički djelitelj**, a preostali su parovi upravo oni kojima je $k$ **najveći zajednički djelitelj**. Dakle $f(k)=$ broj parova kojima je $k$ **zajednički djelitelj** $-$ broj parova kojima je neki višekratnik od $k$ **zajednički djelitelj**.

Nadalje, broj parova kojima je neki višekratnik od $k$ **zajednički djelitelj** jednak je zbroju brojeva parova kojima je neki višekratnik od $k$ **najveći zajednički djelitelj**. Stoga možemo zapisati sljedeći izraz:

$$
f(k)= \lfloor (N/k) \rfloor ^2 - \sum_{i=2}^{i*k \le N} f(i*k)
$$

Budući da za $k>N/2$ možemo izravno izračunati $f(k)= \lfloor (N/k) \rfloor ^2$, možemo ići obrnutim redom i računati od $f(N)$ do $f(1)$. Tako smo zadatak riješili formulom uključivanja-isključivanja.

```cpp
for (long long k = N; k >= 1; k--) {
  f[k] = (N / k) * (N / k);
  for (long long i = k + k; i <= N; i += k) f[k] -= f[i];
}
```

Vremenska složenost gornjeg postupka jest $O( \sum_{i=1}^{N} N/i)=O(N \sum_{i=1}^{N} 1/i)=O(N \log N)$.

Kao bonus, evo tri zadatka s istim rješenjem za vježbu.

-   [Luogu P2398 GCD SUM](https://www.luogu.com.cn/problem/P2398)
-   [Luogu P2158 \[SDOI2008\] 仪仗队 (Počasna garda)](https://www.luogu.com.cn/problem/P2158)
-   [Luogu P1447 \[NOI2010\] 能量采集 (Prikupljanje energije)](https://www.luogu.com.cn/problem/P1447)

### Izvod Eulerove funkcije pomoću uključivanja-isključivanja

Razmotrimo sljedeći problem:

???+ note "Formula za Eulerovu funkciju"
    Odredite Eulerovu funkciju $\varphi(n)$, gdje je $\varphi(n)=|\{1\leq x\leq n|\gcd(x,n)=1\}|$.

Izravno računanje ima složenost $O(n\log n)$, linearnim sitom $O(n)$, a Du sitom $O(n^{\frac{2}{3}})$ (doduše, zašto uopće spominjati Du sito kad uvodni teorijsko-brojevni zadatak rješavamo uključivanjem-isključivanjem); u nastavku ćemo formulu za Eulerovu funkciju izvesti uključivanjem-isključivanjem.

Da bismo provjerili jesu li dva broja relativno prosta, najprije rastavimo na proste faktore

$$
n=\prod_{i=1}^k{p_i}^{c_i}
$$

Tada se zahtijeva da za svaki $p_i$ broj $x$ nije višekratnik od $p_i$, tj. $p_i\nmid x$. To shvatimo kao svojstvo kojem odgovara skup $S_i$, pa vrijedi

$$
\varphi(n)=\left|\bigcap_{i=1}^kS_i\right|=|U|-\left|\bigcup_{i=1}^k\overline{S_i}\right|
$$

Veličina univerzalnog skupa jest $|U|=n$, a $\overline{S_i}$ je skup određen uvjetom $p_i\mid x$, pa je očito $|\overline{S_i}|=\frac{n}{p_i}$, iz čega slijedi

$$
\left|\bigcap_{a_i<a_{i+1}}S_{a_i}\right|=\frac{n}{\prod p_{a_i}}
$$

Stoga dobivamo

$$
\begin{aligned}
\varphi(n)&=n-\sum_{i}\frac{n}{p_i}+\sum_{i<j}\frac{n}{p_ip_j}-\cdots+(-1)^k\frac{n}{p_1p_2 \cdots p_k}\\
&=n\left(1-\frac{1}{p_1}\right)\left(1-\frac{1}{p_2}\right)\cdots\left(1-\frac{1}{p_k}\right)\\
&=n\prod_{i=1}^k\left(1-\frac{1}{p_i}\right)
\end{aligned}
$$

a to je upravo matematički izraz za Eulerovu funkciju.

## Poopćenje formule uključivanja-isključivanja

Formula uključivanja-isključivanja često se koristi u problemima prebrojavanja skupova; za dvije funkcije skupova $f(S),g(S)$, ako je

$$
f(S)=\sum_{T\subseteq S}g(T)
$$

onda vrijedi

$$
g(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}f(T)
$$

### Dokaz

Dokažimo to ukratko. Krećemo od desne strane jednakosti:

$$
\begin{aligned}
&\sum_{T\subseteq S}(-1)^{|S|-|T|}f(T)\\
=&\sum_{T\subseteq S}(-1)^{|S|-|T|}\sum_{Q\subseteq T}g(Q)\\
=&\sum_{Q}g(Q)\sum_{Q\subseteq T\subseteq S}(-1)^{|S|-|T|}\\
\end{aligned}
$$

Primjećujemo da drugi dio sume ne ovisi o $Q$, pa iz njega uklonimo $Q$:

$$
=\sum_{Q}g(Q)\sum_{T\subseteq (S\setminus Q)}(-1)^{|S\setminus Q|-|T|}
$$

Označimo funkciju skupa $P$ s $F(P)=\sum_{T\subseteq P}(-1)^{|P|-|T|}$ i pojednostavnimo je:

$$
\begin{aligned}
F(P)&=\sum_{T\subseteq P}(-1)^{|P|-|T|}\\
&=\sum_{i=0}^{|P|}\dbinom{|P|}{i}(-1)^{|P|-i}=\sum_{i=0}^{|P|}\dbinom{|P|}{i}1^i(-1)^{|P|-i}\\
&=(1-1)^{|P|}=0^{|P|}
\end{aligned}
$$

Stoga je vrijednost polaznog izraza

$$
\sum_{Q}g(Q)\sum_{T\subseteq (S\setminus Q)}(-1)^{|S\setminus Q|-|T|}=\sum_{Q}g(Q)F(S\setminus Q)=\sum_{Q}g(Q)\cdot 0^{|S\setminus Q|}
$$

Analizom vidimo da je samo za $|S\setminus Q|=0$ vrijednost $0^0=1$; tada je $Q=S$, a doprinos rezultatu jest $g(S)$. U ostalim je slučajevima $0^{|S\setminus Q|}=0$, pa doprinosa nema. Tako dobivamo

$$
\sum_{Q}g(Q)\cdot 0^{|S\setminus Q|}=g(S)
$$

Time je tvrdnja dokazana.

### Korolar

Ovaj oblik ima i sljedeći korolar. Ako za funkcije $f(S),g(S)$ u univerzalnom skupu $U$ vrijedi

$$
f(S)=\sum_{S\subseteq T}g(T)
$$

onda je

$$
g(S)=\sum_{S\subseteq T}(-1)^{|T|-|S|}f(T)
$$

Taj je korolar zapravo oblik s komplementima, a dokaz je analogan.

## Prebrojavanje DAG-ova

???+ note "Prebrojavanje DAG-ova"
    Prebrojite označene usmjerene acikličke grafove s $n$ vrhova, modulo $10^9+7$. $n\leq 5\times 10^3$.

### Izravni DP

Razmotrimo DP: neka $f[i,j]$ označava broj DAG-ova s $i$ vrhova od kojih $j$ vrhova ima ulazni stupanj $0$. Pretpostavimo da nakon uklanjanja tih $j$ vrhova $k$ vrhova ima ulazni stupanj $0$; tada je prije uklanjanja svaki od tih $k$ vrhova bio spojen s barem nekima od tih $j$ vrhova, što daje $2^j-1$ mogućnosti; osim bridova prema tih $k$ vrhova, tih $j$ vrhova može biti proizvoljno spojeno s preostalim vrhovima, što daje $2^{i-j-k}$ mogućnosti. Stoga jednadžba glasi:

$$
f[i,j]=\binom{i}{j}\sum_{k=1}^{i-j}(2^j-1)^k2^{(i-j-k)j}f[i-j,k]
$$

Složenost računanja gornjeg izraza jest $O(n^3)$.

### Opuštanje ograničenja

Definicija gornjeg DP-a, točno $j$ vrhova ulaznog stupnja $0$, prestroga je; može se opustiti na barem $j$ vrhova ulaznog stupnja $0$. Izravno definirajmo $f[i]$ kao broj DAG-ova s $i$ vrhova. Može se izravno primijeniti uključivanje-isključivanje. Promotrimo odabranih $j$ vrhova: tih $j$ vrhova može biti proizvoljno spojeno s preostalih $i-j$ vrhova, tj. $\left(2^{i-j}\right)^j=2^{(i-j)j}$ mogućnosti:

$$
f[i]=\sum_{j=1}^i(-1)^{j-1}\binom{i}{j}2^{(i-j)j}f[i-j]
$$

Složenost računanja gornjeg izraza jest $O(n^2)$.

## Min-max uključivanje-isključivanje

Za niz $\{x_i\}$ koji zadovoljava relaciju [potpunog uređaja](../order-theory.md#偏序集) i čiji se elementi mogu zbrajati i oduzimati, neka je njegova duljina $n$ i neka je $S=\{1,2,3,\cdots,n\}$; tada vrijedi:

$$
\max_{i\in S}{x_i}=\sum_{T\subseteq S}{(-1)^{|T|-1}\min_{j\in T}{x_j}}
$$

$$
\min_{i\in S}{x_i}=\sum_{T\subseteq S}{(-1)^{|T|-1}\max_{j\in T}{x_j}}
$$

**Dokaz:** Konstruirajmo preslikavanje na običnu formulu uključivanja-isključivanja. Za $x\in S$ pretpostavimo da je $x$ $k$-ti najmanji element. Definirajmo preslikavanje $f:x\mapsto \{1,2,\cdots,k\}$. Očito je to bijekcija.

Lako se vidi da za $x,y\in S$ vrijedi $f(\min(x,y))=f(x)\cap f(y)$ i $f(\max(x,y))=f(x)\cup f(y)$. Stoga dobivamo:

$$
\begin{aligned}
\left|f\left(\max_{i\in S}{x_i}\right)\right|
&= \left| \bigcup_{i\in S} f(x_i) \right|\\
&= \sum_{T\subseteq S}(-1)^{|T|-1} \left|\bigcap_{j\in T}f(x_j)\right|\\
&= \sum_{T\subseteq S}(-1)^{|T|-1} \left|f\left(\min_{j\in T}{x_j}\right)\right|\\
\end{aligned}
$$

Zatim $\left|f\left(\max_{i\in S}{x_i}\right)\right|$ preslikamo natrag u $\max_{i\in S}{x_i}$; za $\min$ je analogno.

Time je dokaz završen.

No možda vam se ova formula čini vrlo glupom – maksimum se ionako može izravno izračunati. Min-max uključivanje-isključivanje toliko je važno zato što vrijedi i za očekivanja, tj.:

$$
E\left(\max_{i\in S}{x_i}\right)=\sum_{T\subseteq S}{(-1)^{|T|-1}E\left(\min_{j\in T}{x_j} \right)}
$$

$$
E\left(\min_{i\in S}{x_i}\right)=\sum_{T\subseteq S}{(-1)^{|T|-1}E\left(\max_{j\in T}{x_j} \right)}
$$

**Dokaz:** Promotrimo jedan način računanja očekivanja:

$$
E\left(\max_{i\in S}{x_i}\right)=\sum_{y}{P(y=x)\max_{j\in S}{y_j}}
$$

gdje je $y$ niz duljine $n$.

Na $\max$ s desne strane primijenimo prethodnu formulu:

$$
\begin{aligned}E\left(\max_{i\in S}{x_i}\right)&=\sum_{y}{P(y=x)\max_{j\in S}{y_j}}\\
&=\sum_{y}{P(y=x)\sum_{T\subseteq S}{(-1)^{|T|-1}\min_{j\in T}{y_j}}} \end{aligned}
$$

Zamijenimo redoslijed sumiranja:

$$
\begin{aligned}E\left(\max_{i\in S}{x_i}\right)
&=\sum_{y}{P(y=x)\sum_{T\subseteq S}{(-1)^{|T|-1}\min_{j\in T}{y_j}}}\\
&=\sum_{T\subseteq S}{(-1)^{|T|-1}\sum_y{P(y=x)\min_{j\in T}{y_j}}}\\
&=\sum_{T\subseteq S}{(-1)^{|T|-1}E\left(\min_{j\in T}{y_j}\right)} \end{aligned}
$$

Za $\min$ je analogno.

Time je dokaz završen.

Postoji i jača tvrdnja:

$$
\underset{i\in S}{\operatorname{kthmax}{x_i}}=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\min_{j\in T}{x_j}}
$$

$$
\underset{i\in S}{\operatorname{kthmin}{x_i}}=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\max_{j\in T}{x_j}}
$$

$$
E\left(\underset{i\in S}{\operatorname{kthmax}{x_i}}\right)=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}E\left(\min_{j\in T}{x_j}\right)}
$$

$$
E\left(\underset{i\in S}{\operatorname{kthmin}{x_i}}\right)=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}E\left(\max_{j\in T}{x_j}\right)}
$$

Dogovorno, ako je $n< m$, onda je $\dbinom nm=0$.

**Dokaz:** Bez smanjenja općenitosti neka je $\forall 1\le i<n,x_i\le x_{i+1}$. Tada vrijedi:

$$
\begin{aligned}
\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\min_{j\in T}{x_j}}
&=\sum_{i\in S}{x_i\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\left[x_i=\min_{j\in T}{x_j} \right]}}\\
&=\sum_{i\in S}{x_i\sum_{j=k}^n{\dbinom {n-i}{j-1}\dbinom {j-1}{k-1}(-1)^{j-k}}}
\end{aligned}
$$

Budući da vrijedi kombinatorni identitet $\dbinom ab\dbinom bc=\dbinom ac\dbinom {a-c}{b-c}$, imamo:

$$
\begin{aligned}
\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\min_{j\in T}{x_j}}
&=\sum_{i\in S}{x_i\sum_{j=k}^n{\dbinom {n-i}{j-1}\dbinom {j-1}{k-1}(-1)^{j-k}}}\\
&=\sum_{i\in S}{x_i\sum_{j=k}^n{\dbinom {n-i}{k-1}\dbinom {n-i-k+1}{j-k}(-1)^{j-k}}}\\
&=\sum_{i\in S}{\dbinom {n-i}{k-1}x_i\sum_{j=k}^n{\dbinom {n-i-k+1}{j-k}(-1)^{j-k}}}\\
&=\sum_{i\in S}{\dbinom {n-i}{k-1}x_i\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}}
\end{aligned}
$$

Za $i=n-k+1$:

$$
\dbinom {n-i}{k-1}\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}=1
$$

inače:

$$
\dbinom {n-i}{k-1}\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}=0
$$

Stoga:

$$
\sum_{i\in S}{\dbinom {n-i}{k-1}x_i\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}}=\underset{i\in S}{\operatorname{kthmax}}{x_i}
$$

Preostale su tri tvrdnje analogne.

Time je dokaz završen.

Iz min-max uključivanja-isključivanja možemo dobiti i sljedeću formulu:

$$
\underset{i\in S}{\operatorname{lcm}}{x_i}=\prod_{T\subseteq S}{\left(\gcd_{j\in T}{x_j} \right)^{(-1)^{|T|-1}}}
$$

jer $\operatorname{lcm},\gcd,a^{1},a^{-1}$ redom odgovaraju $\max,\min,+,-$; drugim riječima, to je min-max uključivanje-isključivanje primijenjeno na eksponente, pa formula prirodno vrijedi.

## PKUWC2018 随机游走 (Slučajna šetnja)

???+ note "[PKUWC2018 随机游走 (Slučajna šetnja)](https://loj.ac/problem/2542)"
    Zadano je stablo s $n$ vrhova. Krećete iz vrha $x$ i u svakom koraku s jednakom vjerojatnošću nasumično birate jedan brid incidentan s trenutačnim vrhom te prelazite preko njega.
    
    Slijedi $Q$ upita. U svakom je upitu zadan skup $S$; odredite očekivani broj koraka ako, krenuvši iz $x$, nasumično šećete sve dok svaki vrh iz skupa $S$ ne bude posjećen barem jednom.
    
    Posebno, smatra se da je vrh $x$ (tj. početni vrh) već na početku posjećen jednom.
    
    Rezultat se traži modulo $998244353$.
    
    $1\le n\le 18,1\le Q\le 5000,1\le |S|\le n$.

Očekivani broj koraka šetnje ujedno je i vrijeme šetnje. Neka slučajna varijabla $x_i$ označava trenutak prvog dolaska u vrh $i$. Tada tražimo

$$
E\left(\max_{i\in S}x_i\right)
$$

Min-max uključivanjem-isključivanjem dobivamo

$$
E\left(\max_{i\in S}x_i\right)
=E\left(\sum_{T\subseteq S}(-1)^{|T|-1}\min_{i\in T}x_i\right)
=\sum_{T\subseteq S}(-1)^{|T|-1}E\left(\min_{i\in T}x_i\right)
$$

Za skup $T\in[n]$ pokušajmo izračunati $F(T)=E(\min_{i\in T}x_i)$.

Razmotrimo značenje $E(\min_{i\in T}x_i)$: to je očekivano vrijeme prvog dolaska u neki vrh iz $T$. Neka $f(i)$ označava očekivano vrijeme da se, krenuvši iz vrha $i$, prvi put stigne u neki vrh iz $T$.

-   Za $i\in T$ vrijedi $f(i)=0$.
-   Za $i\notin T$ vrijedi $f(i)=1+\frac{1}{\text{deg}(i)}\sum_{(i,j)\in E}f(j)$.

Izravna Gaussova eliminacija ima složenost $O(n^3)$, pa bi računanje $F(T)$ za svaki $T$ imalo ukupnu složenost $O(2^nn^3)$, što je neprihvatljivo. Upotrijebit ćemo tehniku eliminacije na stablu.

Neka je korijen vrh $1$, a roditelj vrha $u$ neka je $p_u$. Za list $i$ vrijednost $f(i)$ ovisi samo o roditelju vrha $i$ (a može biti i $f(i)=0$, što je još bolje). Stoga $f(i)$ možemo zapisati u obliku $f(i)=A_i+B_if(p_i)$, gdje se $A_i,B_i$ mogu brzo izračunati.

Za unutarnji vrh $i$ promotrimo niz njegove djece $j_1,\cdots,j_k$. Budući da je $f(j_e)=A_{j_e}+B_{j_e}f(i)$, dobivamo

$$
f(i)=1+\frac{1}{\deg(i)}\sum_{e=1}^k\left(A_{j_e}+B_{j_e}f(i)\right)+\frac{f(p_i)}{\deg(i)}
$$

Preuređivanjem dobivamo

$$
f(i)=\frac{\deg(i)+\sum_{e=1}^kA_{j_e}}{\deg(i)-\sum_{e=1}^kB_{j_e}}+
\frac{f(p_i)}{\deg(i)-\sum_{e=1}^kB_{j_e}}
$$

Tako smo i $f(i)$ zapisali u obliku $A_i+B_if(p_i)$. Na taj način možemo ići unatrag sve do korijena, a korijen nema roditelja, što znači

$$
f(1)=\frac{\deg(1)+\sum_{e=1}^kA_{j_e}}{\deg(1)-\sum_{e=1}^kB_{j_e}}
$$

Rješavanjem te jednadžbe dobivamo $f(1)$, a zatim još jednim prolazom odozgo prema dolje dobivamo $f(i)$ za svaki vrh. Tada je $F(T)=f(x)$. Vremenska je složenost $O(n)$.

Tako za svaki $T$ možemo izračunati $F(T)$ u ukupnoj vremenskoj složenosti $O(2^nn)$.

Vratimo se na dio s uključivanjem-isključivanjem: znamo da je $E(\max_{i\in S}x_i)=\sum_{T\subseteq S}(-1)^{|T|-1}F(T)$.

Neka je $F'(T)=(-1)^{|T|-1}F(T)$; tada dalje dobivamo $E(\max_{i\in S}x_i)=\sum_{T\subseteq S}F'(T)$. Stoga pomoću FMT-a (koji se naziva i prefiksnim sumama po podskupovima, FWT-om ili transformacijom „ili”) u vremenu $O(2^nn)$ možemo izračunati $E(\max_{i\in S}x_i)$ za svaki $S$ i tako na upite odgovarati u $O(1)$.

### Zadaci za vježbu

-   [ABC331 - G - Collect Them All](https://atcoder.jp/contests/abc331/tasks/abc331_g)
-   [Luogu P4707 重返现世 (Povratak u stvarni svijet)](https://www.luogu.com.cn/problem/P4707)

## Literatura

[浅探容斥原理 (Kratki uvid u formulu uključivanja-isključivanja) – Wang Di](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2013%E8%AE%BA%E6%96%87%E9%9B%86.pdf), zbornik radova kandidata kineske nacionalne reprezentacije za informatičku olimpijadu 2013.

[有标号的 DAG 计数系列问题 (Serija problema prebrojavanja označenih DAG-ova) – Cyhlnj](https://www.cnblogs.com/cjoieryl/p/10078167.html)

[Total order – Wikipedia](https://en.wikipedia.org/wiki/Total_order)
