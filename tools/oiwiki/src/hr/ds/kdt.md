---
title: K-D Tree
---

k-D Tree (KDT, k-Dimension Tree) struktura je podataka koja može **učinkovito obrađivati informacije u $k$-dimenzionalnom prostoru**.

Kad je broj čvorova $n$ znatno veći od $2^k$, k-D Tree je vremenski vrlo učinkovit.

U natjecateljskim zadacima obično je $k=2$. Pri analizi vremenske složenosti na ovoj stranici smatrat ćemo da je $k$ konstanta.

## Izgradnja stabla

k-D Tree ima oblik binarnog stabla pretraživanja, a svaki čvor tog stabla odgovara jednoj točki $k$-dimenzionalnog prostora. Točke svakog podstabla nalaze se unutar jednog $k$-dimenzionalnog hiperkvadra, a sve točke tog hiperkvadra pripadaju tom podstablu.

Pretpostavimo da znamo koordinate $n$ različitih točaka $k$-dimenzionalnog prostora i želimo od njih izgraditi k-D Tree. Koraci su sljedeći:

1.  Ako je u trenutnom hiperkvadru samo jedna točka, vratimo tu točku.

2.  Odaberemo jednu dimenziju i po njoj podijelimo trenutni hiperkvadar na dva hiperkvadra.

3.  Odaberemo točku podjele: u odabranoj dimenziji biramo jednu točku; točke čija je vrijednost u toj dimenziji manja od vrijednosti te točke idu u jedan hiperkvadar (lijevo podstablo), a ostale u drugi (desno podstablo).

4.  Odabrana točka postaje korijen tog podstabla; rekurzivno izgradimo lijevo i desno podstablo nad dvama dobivenim hiperkvadrima i održavamo informacije o podstablu.

Radi lakšeg razumijevanja pogledajmo primjer za $k=2$.

![](./images/kdt1.jpg)

Izgrađeni k-D Tree mogao bi izgledati ovako:

![](./images/kdt2.jpg)

Koordinate na svakom čvoru stabla koordinate su odabrane točke podjele, a $x$ ili $y$ uz unutarnje čvorove označava odabranu dimenziju podjele.

Ovako složenost nije zajamčena. Za korake $2$ i $3$ predlažemo dvije optimizacije:

1.  Naizmjence biramo $k$ dimenzija, tako da se u bilo kojih $k$ uzastopnih razina po svakoj dimenziji dijeli točno jednom.
2.  Pri odabiru točke podjele u nekoj dimenziji biramo **medijan** po toj dimenziji; tako lijevo i desno podstablo budu što je moguće jednake veličine.

Može se primijetiti da je uz optimizaciju $2$ visina izgrađenog k-D Treea najviše $\log n+O(1)$.

Usko grlo vremenske složenosti izgradnje k-D Treea sada je brzo pronalaženje medijana u jednoj dimenziji te premještanje točaka s manjom vrijednošću u toj dimenziji lijevo od medijana, a ostalih desno. Ako bismo svaki put sortirali po toj dimenziji funkcijom `sort`, složenost bi bila $O(n\log^2 n)$. Zapravo, pronaći medijan $n$ elemenata i staviti ga na mjesto koje bi imao nakon sortiranja može se u $O(n)$.

Prisjetimo se ideje quicksorta. Svaki put odaberemo jedan broj, brojeve manje od njega stavimo lijevo, a veće desno, čime je taj broj na svom konačnom mjestu, a zatim rekurzivno sortiramo lijevi i desni dio. Očekivana je složenost $O(n\log n)$. No k-D Tree zahtijeva samo da medijan bude na svom konačnom mjestu, pa je dovoljno rekurzivno obraditi samo **onu stranu** koja sadrži medijan. Može se dokazati da je očekivana složenost tada $O(n)$. U biblioteci `algorithm` postoji funkcija `nth_element()` koja radi upravo to: da bismo među vrijednostima od `s[l]` do `s[r]` pronašli onu koja bi se po pravilu uspoređivanja `cmp` nakon sortiranja našla na poziciji `s[mid]`, uz jamstvo da su vrijednosti lijevo od `s[mid]` manje od `s[mid]`, a desno veće, dovoljno je napisati `nth_element(s+l,s+mid,s+r+1,cmp)`.

S tom je idejom vremenska složenost izgradnje k-D Treea $O(n\log n)$.

## Operacije u višedimenzionalnom prostoru

Pri upitu o nekoj informaciji o svim točkama unutar višedimenzionalnog kvadra, za svaki čvor pamtimo najveću i najmanju koordinatu po svakoj dimenziji unutar njegova podstabla. Ako se kvadar trenutnog podstabla ne siječe s traženim kvadrom, podstablo dalje ne pretražujemo; ako je kvadar trenutnog podstabla u potpunosti sadržan u traženom, vratimo zbroj težina svih točaka podstabla; inače provjerimo je li trenutna točka unutar traženog kvadra, ažuriramo odgovor i rekurzivno tražimo u lijevom i desnom podstablu.

??? note "Implementacija"
    ```cpp
    int query(int p) {
      if (!p) return 0;
      bool flag{false};
      for (int k : {0, 1}) flag |= (!(l.x[k] <= t[p].L[k] && t[p].R[k] <= h.x[k]));
      if (!flag) return t[p].sum;
      for (int k : {0, 1})
        if (t[p].R[k] < l.x[k] || h.x[k] < t[p].L[k]) return 0;
      int ans{0};
      flag = false;
      for (int k : {0, 1}) flag |= (!(l.x[k] <= t[p].x[k] && t[p].x[k] <= h.x[k]));
      if (!flag) ans = t[p].v;
      return ans += query(t[p].l) + query(t[p].r);
    }
    ```

### Analiza složenosti

Razmotrimo najprije dvodimenzionalni slučaj. Pri upitu za pravokutnik $R$ čvorove k-D Treea dijelimo u tri skupine:

1.  nemaju presjeka s $R$;
2.  u potpunosti su sadržani u $R$;
3.  djelomično su sadržani u $R$.

Očito je složenost jednog upita jednaka broju čvorova 3. skupine. Primijetimo da pravokutnik čvora 3. skupine ili u potpunosti sadrži $R$, ili se takvi pravokutnici međusobno ne sadrže; prvih očito ima samo $O(h)=O(\log n)$, pa analizirajmo broj drugih.

Najprije, bez smanjenja općenitosti, sve stranice pravokutnika pomaknemo za $\epsilon$ tako da pravokutnik upita ne prolazi ni kroz jednu postojeću točku. To očito ne mijenja skup točaka koje upit obuhvaća.

Primijetimo da kroz pravokutnik svakog čvora 3. skupine koji nije u odnosu sadržavanja nužno prolazi neka stranica pravokutnika $R$. Dovoljno je stoga izračunati koliko pravokutnika siječe svaka stranica $R$, tj. kroz najviše koliko pravokutnika čvorova može proći jedna dužina.

Promotrimo neki čvor $u$: on ima četiri unuka, a na putu do svakog unuka po jednom je podijeljen u svakoj od dviju dimenzija. Promatranjem se vidi da, kad se pravokutnik na ovaj način podijeli na četiri potpravokutnika, dužina paralelna s koordinatnom osi prolazi kroz najviše dva od njih; dakle upit koji krene iz $u$ spušta se u najviše dva unuka u kojima još ima čvorova 3. skupine (ako se dužina točno poklapa s granicom podjele, to ne mora vrijediti, ali smo pomicanjem granica pravokutnika upita taj slučaj isključili).

Budući da je pri izgradnji svaka točka medijan svog podstabla po trenutnoj dimenziji, veličina podstabla nužno se prepolavlja. Ako je veličina podstabla čvora $u$ jednaka $n$, dobivamo rekurziju:

$$
T(n)=2T(n/4)+O(1)
$$

Po master teoremu $T(n)=O(\sqrt{n})$.

Poopćimo li rekurziju na $k$ dimenzija, dobivamo $T(n)=2^{k-1}T(n/2^k)+O(1)$, pa je $T(n)=O(n^{1-\frac1k})$ (uz $k$ kao konstantu).

### Umetanje/brisanje

Ako se skup $k$-dimenzionalnih točaka koji održavamo mijenja, tj. ako se točke umeću ili brišu, balansiranost k-D Treea više nije zajamčena. Zbog načina izgradnje k-D Tree ne podržava rotacije, a ni slučajni prioriteti poput onih u FHQ treapu ne jamče složenost. Postoje dva uobičajena pristupa održavanju.

???+ note "Napomena"
    Mnogi natjecatelji koriste strukturu scapegoat stabla. No primijetimo da je u maloprijašnjoj analizi složenosti bilo potrebno da se veličina podstabla djece strogo prepolavlja, tj. da visina stabla bude strogo $\log n+O(1)$, dok scapegoat stablo jamči samo visinu $O(\log n)$, pa složenost upita nije zajamčena.

#### Rekonstrukcija svakih korijen puta

Pri umetanju točke koje treba umetnuti najprije spremimo, a svakih $B$ umetanja napravimo rekonstrukciju.

Za brisanje je dovoljno označiti čvor obrisanim. Želimo li biti stroži, možemo pratiti koliko je čvorova u stablu obrisano i rekonstruirati kad ih bude $B$.

Složenost promjene amortizirano je $O(n\log n/B)$, a upita $O(B+n^{1-\frac1k})$; ako su brojevi promjena i upita istog reda veličine, optimalno je $B=O(\sqrt{n\log n})$ (promjena $O(\sqrt{n\log n})$, upit $O(\sqrt{n\log n}+n^{1-\frac1k})$).

#### Binarno grupiranje

Održavamo više k-D Treeova čije su veličine potencije broja $2$, tako da je zbroj njihovih veličina $n$.

Pri umetanju dodamo novi k-D Tree veličine $1$ i zatim uzastopno spajamo stabla jednake veličine (jednostavno ih „spljoštimo” i rekonstruiramo). U implementaciji je dovoljno rekonstruirati samo jednom.

Lako se vidi da veličine stabala koja treba spojiti nužno počinju od $2^0$ i imaju uzastopne eksponente. Složenost je slična binarnom zbrajanju, amortizirano $O(n\log^2 n)$, jer sama rekonstrukcija nosi faktor $\log$.

Pri upitu jednostavno upitamo svako stablo zasebno; složenost je $O\left(\sum_{i\geq0} (\frac n{2^i})^{1-\frac1k}\right)=O(n^{1-\frac1k})$.

### Primjer

???+ note "[Luogu P4148 简单题](https://www.luogu.com.cn/problem/P4148)"
    Na dvodimenzionalnoj matrici $n\times n$ s početnim vrijednostima $0$ izvršava se $q$ operacija, svaka jednog od dvaju tipova:
    
    1.  `1 x y A`: broju na koordinatama $(x,y)$ dodaj $A$.
    2.  `2 x1 y1 x2 y2`: ispiši zbroj brojeva u pravokutniku s donjim lijevim kutom $(x1,y1)$ i gornjim desnim kutom $(x2,y2)$ (uključujući rub).
    
    Forsirano online. Memorijsko ograničenje `20M`. Garantira se da odgovor i sve međuvrijednosti stanu u `int`.
    
    $1\le n\le 500000 , 1\le q\le 200000$

Ograničenje od 20M memorije ruši sva ugniježđena stabla, forsirano online ruši CDQ divide and conquer; preostaje jedino k-D Tree.

Slijedi primjer koda s binarnim grupiranjem.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/kdt/kdt_3.cpp"
    ```

## Upiti o susjedstvu

???+ warning "Upozorenje"
    Vremenska složenost jednog upita za najbližu točku k-D Treeom u najgorem je slučaju i dalje $O(n)$, ali je to ipak izvrstan heuristički algoritam za skupljanje bodova; koristite ga s oprezom. Objašnjenje upita o susjedstvu ovdje služi samo boljem razumijevanju strukture k-D Treea.

???+ note "Primjer [Luogu P1429 平面最近点对（加强版）](https://www.luogu.com.cn/problem/P1429)"
    Zadano je $n$ točaka $(x_i,y_i)$ u ravnini; pronađite [euklidsku udaljenost](../geometry/distance.md#euklidska-udaljenost) između dviju najbližih točaka ravnine.
    
    $2\le n\le 200000 , 0\le x_i,y_i\le 10^9$

Najprije izgradimo 2-D Tree nad tih $n$ točaka.

Prolazimo sve čvorove i za svaki pronađemo najbližu točku različitu od njega; tako dobivamo odgovor. Grubom silom obići sve čvorove 2-D Treea za svaki čvor košta $O(n)$, pa je potrebno rezanje. Za svako podstablo možemo održavati najmanju i najveću koordinatu svih njegovih čvorova po svakoj dimenziji. Ako je dosad pronađena najmanja udaljenost para točaka $ans$ i ako je **najmanja** udaljenost od točke upita do pravokutnika koji obuhvaća sve točke podstabla veća ili jednaka $ans$, u tom podstablu sigurno nema odgovora, pa u njega ne ulazimo.

Osim toga može se koristiti i heurističko pretraživanje: ako oba podstabla nekog čvora mogu sadržavati odgovor, najprije tražimo u podstablu bližem točki upita. Možemo reći da je **najmanja udaljenost točke upita do pravokutnika podstabla heuristička funkcija ovog zadatka**.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/kdt/kdt_1.cpp"
    ```

???+ note "Primjer [CQOI2016 K 远点对](https://loj.ac/problem/2043)"
    Zadano je $n$ točaka $(x_i,y_i)$ u ravnini; odredite udaljenost $k$-tog najudaljenijeg neuređenog para točaka u euklidskoj metrici.
    
    $n\le 100000 , 1\le k\le 100 , 0\le x_i,y_i<2^{31}$

Slično prethodnom primjeru, samo što umjesto najbližeg para tražimo $k$-ti najudaljeniji par, a heuristička funkcija postaje najveća udaljenost od točke upita do pravokutnika podstabla. Min-heapom održavamo udaljenosti dosad pronađenih $k$ najudaljenijih parova; ako je udaljenost trenutno pronađenog para veća od vrha heapa, izbacimo vrh i umetnemo tu udaljenost. Jednako tako, udaljenošću na vrhu heapa režemo pretragu.

Budući da zadatak naglašava neuređene parove, tj. par ostaje isti i nakon zamjene redoslijeda točaka, svaki se uređeni par broji dvaput, pa učitani $k$ treba pomnožiti s $2$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/ds/code/kdt/kdt_2.cpp"
    ```

## Zadaci

[SDOI2010 捉迷藏](https://www.luogu.com.cn/problem/P2479)

[Violet 天使玩偶/SJY 摆棋子](https://www.luogu.com.cn/problem/P4169)

[国家集训队 JZPFAR](https://www.luogu.com.cn/problem/P2093)

[BOI2007 Mokia 摩基亚](https://www.luogu.com.cn/problem/P4390)

[Luogu P4475 巧克力王国](https://www.luogu.com.cn/problem/P4475)

[CH 弱省胡策 R2 TATT](https://www.luogu.com.cn/problem/P3769)
