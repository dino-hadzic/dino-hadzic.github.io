---
title: Slučajna šetnja na grafu
---

Ova stranica obrađuje problem slučajne šetnje na grafu. Problem se proučava iz tri kuta: rešetkasti grafovi, rijetki grafovi i opći grafovi; opisane su razne metode za rješavanje ove vrste problema te su uspoređene njihove prednosti i nedostaci pri rješavanju različitih zadataka.

## Definicija

Zadan je usmjereni jednostavni graf $G=(V, E)(V=\{v_1, v_2, \cdots, v_{|V|}\})$, početni vrh $s \in V$ i završni vrh $t \in V$; svaki brid $e=\left(x, y\right)$ ima pozitivnu težinu $w_e$ tako da za svaki $x \in V \backslash\left\{t\right\}$ vrijedi $\sum_{\left(x, y\right) \in E} w_{\left(x, y\right)}=1$, a iz svakog vrha $x$ postoji put koji vodi u $t$. Figura kreće iz početnog vrha i svake sekunde iz trenutnog vrha $x$ s vjerojatnošću $w_{(x, y)}$ bira izlazni brid $\left(x, y\right)$ i prelazi u $y$; kad stigne u završni vrh, zaustavlja se. Treba odrediti očekivano utrošeno vrijeme.

Zapravo se ovaj problem može zapisati i u matričnom obliku. Definirajmo matricu $P$:

$$
P_{x, y}=
\begin{cases}
w_{(x, y)} & \text{ako } (x, y) \in E \text{ i } x \neq t \\
0 & \text{ako } (x, y) \notin E \text{ ili } x=t \\
\end{cases}
$$

Traženi odgovor je tada:

$$
\sum_{k \geq 0} k \times\left(P^k\right)_{s, t}
$$

gdje $\left(P^k\right)_{s, t}$ označava vjerojatnost da se završni vrh prvi put dosegne nakon $k$ koraka. Kad je graf konačan i svi vrhovi mogu doseći završni vrh, iz definicije $P$ može se dokazati da su sve njezine svojstvene vrijednosti manje od 1, pa odgovor sigurno konvergira.

Radi jednostavnosti, na ovoj stranici, ako nije drugačije rečeno, $n$ označava $|V|$, a $m$ označava $|E|$.

Osim toga, na ovoj stranici rijetki graf označava graf u kojem je broj bridova istog reda veličine kao broj vrhova.

## Rešetkasti grafovi

???+ note "Primjer 1 [Circles of Waiting](https://codeforces.com/problemset/problem/963/E)"
    Figura se na početku nalazi u točki $(0,0)$ pravokutnog koordinatnog sustava. Svake sekunde figura se nasumično pomiče. Ako je trenutno u $(x, y)$, sljedeće sekunde s vjerojatnošću $p_1$ prelazi u $(x-1, y)$, s vjerojatnošću $p_2$ u $(x, y-1)$, s vjerojatnošću $p_3$ u $(x+1, y)$, a s vjerojatnošću $p_4$ u $(x, y+1)$. Zajamčeno je $p_1+p_2+p_3+p_4=1$.
    Odredite očekivano vrijeme nakon kojeg će se pomaknuti na položaj čija je euklidska udaljenost od ishodišta veća od $R$. $0 \leq R \leq 50$, $p_1, p_2, p_3, p_4>0$, odgovor se traži modulo $10^9+7$.

### Naivni pristup

Neka $f(i, j)$ označava očekivano vrijeme potrebno da figura iz $(i, j)$ dođe na položaj čija je euklidska udaljenost od ishodišta veća od $R$. Prijelazna jednadžba glasi:

$$
f(i, j)=
\begin{cases}
p_1 f(i-1, j) + p_2 f(i, j-1) + p_3 f(i+1, j) + p_4 f(i, j+1) + 1 & i^2 + j^2 \leq R^2 \\
0 & i^2 + j^2 > R^2
\end{cases}
$$

Budući da prijelazi nemaju topološki poredak, treba koristiti Gaussovu eliminaciju. Vremenska složenost je $O\left(R^6\right)$, što ne prolazi ovaj zadatak.

### Izravna eliminacija

Uočimo da je većina koeficijenata jednadžbi koje treba eliminirati jednaka 0; ako pri eliminaciji računamo samo na pozicijama gdje je vrijednost različita od 0, složenost se smanjuje.

Promotrimo postupak eliminacije: jednadžbe eliminiramo redom odozgo prema dolje u koordinatnom sustavu, a unutar istog retka slijeva nadesno. Već eliminirane jednadžbe obojimo žuto, točke susjedne žutima obojimo zeleno, a ostale točke crno, kao na slici:

![graph-random-walk-1](images/graph-random-walk-1.svg)

Sljedeći korak je eliminacija jednadžbe koja odgovara sljedećem zelenom polju. U toj jednadžbi samo varijable zelenih polja i prvog crnog polja ispod njega mogu imati koeficijent različit od 0; a samo u jednadžbama zelenih polja i prvog crnog polja ispod njega koeficijent varijable trenutnog polja može biti različit od 0.

Uočimo da zelenih polja ima samo $O(R)$, pa je složenost eliminacije jedne jednadžbe $O\left(R^2\right)$. Ukupno ima samo $O\left(R^2\right)$ jednadžbi, pa se složenost smanjuje na $O\left(R^4\right)$, što prolazi ovaj zadatak.

### Metoda glavnih varijabli

Jednadžbi i varijabli ima po $O\left(R^2\right)$; ako bismo veličinu problema smanjili na $O(R)$, naivna Gaussova eliminacija bi prolazila.

Varijablu prvog polja slijeva u svakom retku proglasimo glavnom varijablom, ukupno njih $2 R+1$, i pokušajmo varijable ostalih polja izraziti kao linearne funkcije tih glavnih varijabli. Promatramo stupac po stupac slijeva nadesno; za svako polje $(i, j)$ trenutnog stupca uočimo da su $f(i, j), f(i-1, j), f(i, j-1), f(i, j+1)$ već poznate linearne funkcije glavnih varijabli, pa preslagivanjem prijelazne jednadžbe dobivamo:

$$
f(i+1, j)=\frac{f(i, j)-p_1 f(i-1, j)-p_2 f(i, j-1)-p_4 f(i, j+1)-1}{p_3}
$$

Tako dobivamo prikaz $f(i+1, j)$ kao linearne funkcije glavnih varijabli. Ako je $(i+1, j)$ već na euklidskoj udaljenosti od ishodišta većoj od $R$, dobivamo jednadžbu $f(i+1, j)=0$. Na kraju dobivamo $2 R+1$ jednadžbi, na koje primijenimo Gaussovu eliminaciju.

U fazi rekurzivnog izvođenja linearnih funkcija glavnih varijabli ima $O\left(R^2\right)$ varijabli, a izvođenje jedne varijable traje $O(R)$; nakon toga je veličina problema smanjena na $O(R)$. Oba dijela imaju vremensku složenost $O\left(R^3\right)$, pa je i ukupna složenost $O\left(R^3\right)$, što prolazi ovaj zadatak.

### Usporedba dvaju pristupa

Usporedimo oba pristupa s više strana:

Što se tiče vremenske složenosti, najgora složenost metode glavnih varijabli na rešetkastom grafu je $O(n \sqrt{n})$ (najveća je kad su i duljina i širina rešetke reda $O(\sqrt{n})$), dok je najgora složenost izravne eliminacije na rešetkastom grafu $O\left(n^2\right)$; metoda glavnih varijabli je bolja.

Što se tiče preciznosti, za zadatke u kojima se računa s realnim brojevima umjesto modulo, izravna eliminacija preciznija je od metode glavnih varijabli.

Što se tiče primjenjivosti, dva su pristupa prikladna za različite situacije.

Kad u rešetkastom grafu postoje prepreke ili bridovi s vjerojatnošću prolaska $0$, metoda glavnih varijabli za svaku prepreku ili brid s vjerojatnošću $0$ treba dodati jednu glavnu varijablu; kad je broj prepreka ili bridova s vjerojatnošću $0$ veći od $O(R)$, složenost metode glavnih varijabli raste, dok složenost izravne eliminacije ostaje ista.

No metoda glavnih varijabli može eliminirati i jednadžbe slične onima na rešetkastom grafu, npr. $f(i, j)=p_1 f(i+1, j)+p_2 f(i, j+1)+p_3 f(\operatorname{pre}(i, j))+1$, gdje je $\operatorname{pre}(i, j)=(x, y)(x \leq i, y \leq j)$ vrijednost zadana u zadatku, dok analiza složenosti izravne eliminacije u ovom modelu ne vrijedi.

Osim toga, za računanje determinante matrice susjedstva rešetkastog grafa ne može se koristiti metoda glavnih varijabli; složenost se može poboljšati samo izravnom eliminacijom.

Ukratko, oba pristupa imaju svoje prednosti i treba ih odabrati prema konkretnom zadatku.

## Rijetki grafovi

???+ note "Primjer 2 Expected Value"
    Zadan je jednostavan neusmjeren povezan rijedak graf $G=(V, E)$. Figura se na početku nalazi u $v_1$; svake sekunde figura ravnomjerno nasumično bira jedan od bridova incidentnih s trenutnim vrhom i prelazi u vrh na koji on pokazuje. Odredite očekivano vrijeme dolaska u $v_n$. $n \leq 2000$, odgovor se traži modulo $p$, gdje je $p$ prost broj nasumično odabran iz intervala $\left[10^9, 1.01 \times 10^9\right]$.

### Osnove

**Definicija 4.1.** Svaki polinom $p(λ)$ za koji vrijedi $p(A) = 0$ naziva se poništavajući polinom matrice $A$.

**Definicija 4.2.** Neka $I_n$ označava jediničnu matricu reda $n$. Karakteristični polinom matrice $A$ dimenzija $n × n$ definira se kao $p(λ) = \det(λI_n - A)$, gdje $\det$ označava determinantu matrice.
Lako se vidi da stupanj karakterističnog polinoma matrice $A$ reda $n$ ne prelazi $n$.

**Teorem 4.2.** (Cayley–Hamiltonov teorem) Karakteristični polinom bilo koje matrice njezin je poništavajući polinom.

Stoga ni stupanj poništavajućeg polinoma najmanjeg stupnja matrice reda $n$ ne prelazi $n$.

### Rješavanje izvornog problema

Uočimo da je očekivano vrijeme šetnje $E(t)=\sum_{i\geq0}\Pr[t>i]$; ako možemo izračunati vjerojatnost da šetnja nakon $i$ koraka još nije završila, zbroj po svim $i ≥ 0$ daje odgovor.

Neka $f(i, j)$ označava vjerojatnost da smo nakon $i$ koraka u vrhu $j$ i da još nismo posjetili $n$. Tada vrijedi:

$$
f(i,j)=\sum_{(k,j)\in E}\frac{f(i-1,k)}{\deg_k}(j\neq n)
$$

gdje $\deg_k$ označava stupanj vrha $k$.

Uočimo da prijelaz za $f$ ne ovisi o $i$, pa se jedan prijelaz može shvatiti kao množenje matricom, tj. $f{i+1}=f_iM$. Budući da stupanj minimalnog poništavajućeg polinoma matrice $M$ ne prelazi $n$, ni duljina najkraće rekurzije za $f$ ne prelazi $n$, pa ni duljina najkraće rekurzije za $\Pr[t>i]=\sum_{j=1}^{n-1}f(i,j)$ ne prelazi $n$. U vremenu $O(nm)$ možemo izračunati $\Pr[t>0],\Pr[t>1],\cdots,\Pr[t>3n]$, a zatim *Berlekamp–Masseyjevim* algoritmom u vremenu $O(n^2)$ pronaći najkraću rekurziju za $\Pr[t > i]$.

Promotrimo računanje funkcije izvodnice linearno rekurzivnog niza $a$ reda $k$. Pretpostavimo da za $i ≥ i_0$ vrijedi $a_i=\sum_{j=1}^kc_ja_{i-j}$, i označimo funkcije izvodnice od $a$ i $c$ s $A(x)$ i $C(x)$. Tada je $A(x)=A(x)C(x)+A_0(x)$, gdje je $A_0(x)$ određen članovima s $i < i_0$.

Vratimo se izvornom problemu: budući da možemo odrediti najkraću rekurziju za $\Pr[t > i]$, možemo izračunati $C(x)$ i $A_0(x)$ (s istim definicijama kao u prethodnom odlomku), a preslagivanjem dobivamo $A(x)=\frac{A_0(x)}{1-C(x)}$. Tražimo $\sum_{i\geq0}[x^i]A(x)$; lako se vidi da je ta vrijednost jednaka $A(1)$, pa je dovoljno uvrstiti $x = 1$. Budući da je modul nasumičan prost broj, možemo smatrati da nazivnik neće biti $0$.

Tako smo zadatak riješili u vremenskoj složenosti $O(nm+n^2)$. Ako je broj bridova grafa $G$ istog reda kao broj vrhova, složenost u ovom zadatku možemo smatrati $O(n^2)$.

## Opći grafovi

???+ note "Primjer 3 Frank"
    Zadan je jednostavan jako povezan usmjeren graf $G = (V, E)$. Za sve $1 ≤ s ≤ n$, $1 ≤ t ≤ n$, $s ≠ t$ odgovorite na sljedeće pitanje:
    figura se na početku nalazi u $v_s$; svake sekunde figura ravnomjerno nasumično bira jedan od izlaznih bridova trenutnog vrha i prelazi u vrh na koji on pokazuje. Odredite očekivano vrijeme dolaska u $v_t$. $3 ≤ n ≤ 400$.

### Analiza i transformacija

Neka $p_{i, j}$ označava vjerojatnost da figura u vrhu $i$ odabere izlazni brid $(i, j)$ i prijeđe u $j$; posebno, ako izlazni brid ne postoji, vjerojatnost je $0$. Neka $f_{i,j}$ označava očekivano vrijeme slučajne šetnje iz $i$ do $j$; posebno, $f_{i,i} = 0$. Za $i ≠ j$ prijelazna jednadžba glasi:

$$
f_{i,j}=1+\sum_{1\leq k\leq n}p_{i,k}f_{k,j}
$$

Za $i = j$, neka $g_i$ označava očekivano vrijeme prvog povratka u $i$ pri slučajnoj šetnji iz $i$; tada:

$$
f_{i,i}=1-g_i+\sum_{1\le k\le n}p_{i,k}f_{k,i}
$$

Radi preglednosti zapišimo prijelazne jednadžbe u matričnom obliku. Neka $P$ označava prijelaznu matricu ovog grafa, $F$ matricu odgovora, $I$ jediničnu matricu reda $n$, $J$ matricu reda $n$ sa svim jedinicama, a $G$ matricu reda $n$ takvu da je $G_{i,i} = g_i$, a ostale pozicije su $0$. Tada:

$$
F=J-G+PF
$$

Ako možemo izračunati $G$, ostaje samo riješiti jednadžbu:

$$
(I − P)F = J − G
$$

### Računanje G

**Definicija 5.1.** Stacionarna distribucija prijelazne matrice $P$ reda $n$ je $n$-dimenzionalni vektor $π$ takav da $\sum_{i=1}^{n}\pi_{i}=1$ i $πP = π$. Pri tome je vrijednost svake komponente $π$ u intervalu $[0,1]$.

Lako se uočava praktično značenje stacionarne distribucije. Ako se u nekom trenutku figura s vjerojatnošću $π_i$ nalazi u $v_i$, tada u svakom kasnijem trenutku figura i dalje zadovoljava ovu raspodjelu vjerojatnosti. Vektor $π$ možemo izračunati u vremenu $O(n^3)$ rješavanjem sustava Gaussovom eliminacijom. Kakva je, dakle, veza između $π$ i $G$?

**Teorem 5.1.** Za svaki $1 ≤ i ≤ n$ vrijedi $π_ig_i = 1$.

???+ note "Dokaz"
    Iz $F = J - G + PF$ preslagivanjem dobivamo:
    
    $$
    G = PF + J − F
    $$
    
    Množenjem obiju strana s lijeve strane s $π$ dobivamo:
    
    $$
    πG = πPF + πJ − πF
    $$
    
    Po definiciji $π$ vrijedi $πP = π$, pa:
    
    $$
    πG = πJ
    $$
    
    Stoga:
    
    $$
    \pi_ig_i=\sum_{j=1}^n\pi_j=1  
    $$

Time je tvrdnja dokazana.

Dakle, uvođenjem stacionarne distribucije možemo izračunati $G$ u vremenu $O(n^3)$.

### Rješavanje izvornog problema

Pri rješavanju sustava nailazimo na problem: $(I - P)$ nije punog ranga, pa se sustav ne može riješiti množenjem inverznom matricom.

**Definicija 5.2.** Usmjereno razapinjuće stablo usmjerenog grafa $G = (V,E)$ s korijenom $r\in V$ je podgraf $T = (V,A)$ grafa $G$ takav da:

1.  za svaki $i ≠ r$ izlazni stupanj od $i$ je $1$;
2.  izlazni stupanj od $r$ je $0$;
3.  u $T$ nema ciklusa.

**Lema 5.1.** (Teorem o matrici i stablima za usmjerene grafove) Za usmjereni graf $G$ neka $D$ označava njegovu matricu izlaznih stupnjeva, tj. $D_{i,i} = d_i$, $D_{i,j} = 0(i ≠ j)$, gdje je $d_i$ izlazni stupanj vrha $i$, a $A$ njegovu matricu susjedstva. Tada je broj usmjerenih razapinjućih stabala s korijenom $r$ jednak determinanti matrice $D - A$ bez $r$-tog retka i $r$-tog stupca.

**Teorem 5.2.** Za prijelaznu matricu $P$ jako povezanog grafa $G = (V,E)$, rang matrice $(I - P)$ jednak je $n - 1$.

???+ note "Dokaz"
    Budući da se množenjem nekog retka matrice konstantom različitom od nule rang ne mijenja, pomnožimo $i$-ti redak matrice $(I - P)$ izlaznim stupnjem vrha $v_i$ i dobijemo novu matricu $L$; dovoljno je dokazati da je rang matrice $L$ jednak $n - 1$.  
    Budući da je zbroj svakog retka matrice $L$ jednak $0$, zbrajanjem svih stupčanih vektora matrice $L$ dobivamo nul-vektor, tj. ti su vektori linearno
    zavisni, pa rang matrice $L$ nije $n$.  
    Lako se vidi da je $L$ jednaka matrici izlaznih stupnjeva grafa $G$ umanjenoj za njegovu matricu susjedstva, pa po lemi 5.1 determinanta matrice $L$ bez $i$-tog retka i $i$-tog stupca
    predstavlja broj usmjerenih razapinjućih stabala s korijenom $v_i$.  
    Budući da je G jako povezan, broj usmjerenih razapinjućih stabala s korijenom u bilo kojem vrhu različit je od $0$, tj. $L$ bez $i$-tog retka i
    $i$-tog stupca i dalje je punog ranga.  
    Budući da se dodavanjem stupca rang ne smanjuje, svi redčani vektori matrice $L$ bez $i$-tog retka linearno su nezavisni. Dakle, rang matrice $L$ je $n - 1$.  
    Vratimo se izvornom problemu i promotrimo rješavanje njegova sustava. Radi jednostavnosti zapišimo sustav u obliku $AX = B$,
    gdje su $A$, $B$ poznati, a treba odrediti $X$. Budući da $A$ nije punog ranga, rješenja ima beskonačno mnogo; najprije nađimo jedno partikularno rješenje.
    Gaussovu eliminaciju provodimo istodobno na $A$ i $B$. Prvih $n - 1$ redaka matrice $A$ eliminiramo u oblik u kojem su vrijednosti samo na glavnoj dijagonali i u $n$-tom stupcu,
    a posljednji redak u sve nule, tj. u sljedeći oblik:
    
    $$
    \begin{bmatrix}
    1 & 0 & 0 & \cdots & 0 & a_1 \\0&1&0&\cdots&0&a_2\\0&0&1&\cdots&0&a_3\\
    \vdots&\vdots&\vdots&\ddots&\vdots&\vdots
    \\0&0&0&\cdots&1&a_{n-1}\\0&0&0&\cdots&0&0
    \end{bmatrix}
    X=
    \begin{bmatrix}
    b_{1,1}&b_{1,2}&b_{1,3}&\cdots&b_{1,n-1}&b_{1,n}
    \\b_{2,1}&b_{2,2}&b_{2,3}&\cdots&b_{2,n-1}&b_{2,n}
    \\b_{3,1}&b_{3,2}&b_{3,3}&\cdots&b_{3,n-1}&b_{3,n}
    \\\vdots&\vdots&\vdots&\ddots&\vdots&\vdots
    \\b_{n-1,1}&b_{n-1,2}&b_{n-1,3}&\cdots&b_{n-1,n-1}&b_{n-1,n}
    \\0&0&0&\cdots&0&0
    \end{bmatrix}
    $$
    
    Stavimo $X_{n,i} = 0$; tako dobivamo jedno partikularno rješenje, označimo ga $Y$. Zatim partikularno rješenje prilagodimo u pravo rješenje.  
    Uočimo da je $X_{n,i} = 0$; iz kombinatornog značenja slijedi $Y_{i,j} = 1 + Y_{j,j} + P_{i,k}X_{k,j}$, odakle se lako dobiva $X_{i,j} = Y_{i,j} - Y_{j,j}$.
    Time je zadatak riješen u vremenskoj složenosti $O(n^3)$.

## Literatura

1.  浅谈图模型上的随机游走问题 (O problemu slučajne šetnje na grafovskim modelima). Zbornik radova kineske nacionalne reprezentacije za IOI 2019 (str. 17–26)
