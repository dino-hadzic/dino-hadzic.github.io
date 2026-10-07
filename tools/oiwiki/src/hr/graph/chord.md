---
title: Tetivni grafovi
---

Tetivni grafovi posebna su vrsta grafova: mnogi problemi koji su na općim grafovima NP-teški na tetivnim grafovima imaju lijepe algoritme linearne vremenske složenosti.

## Neke definicije i svojstva

**Podgraf**: graf čiji su skup vrhova i skup bridova podskupovi skupa vrhova i skupa bridova izvornog grafa.

**Inducirani podgraf**: graf čiji je skup vrhova podskup skupa vrhova izvornog grafa, a skup bridova sastoji se od svih bridova **čija oba kraja leže u odabranom skupu vrhova**.

**Klika**: potpun podgraf.

**Maksimalna klika**: klika koja nije podgraf nijedne druge klike.

**Najveća klika**: klika s najvećim brojem vrhova.

**Klikovni broj**: broj vrhova najveće klike, označava se s $\omega(G)$.

**Minimalno bojenje**: bojenje vrhova s najmanjim brojem boja tako da krajevi svakog brida imaju različite boje.

**Kromatski broj**: broj boja minimalnog bojenja, označava se s $\chi(G)$.

**Najveći nezavisan skup**: najveći skup vrhova u kojem nikoja dva vrha nisu izravno spojena bridom. Njegova se veličina označava s $\alpha(G)$.

**Najmanji pokrivač klikama**: pokrivanje svih vrhova najmanjim brojem klika. Broj upotrijebljenih klika označava se s $\kappa(G)$.

**Tetiva**: brid koji spaja dva nesusjedna vrha ciklusa.

**Tetivni graf**: graf u kojem svaki ciklus duljine veće od $3$ ima tetivu.

**Lema 1**: klikovni broj $\omega(G)\le \chi(G)$ kromatski broj

Dokaz: promotrimo bojenje samo induciranog podgrafa najveće klike; za njega treba barem $\omega(G)$ boja.

**Lema 2**: veličina najvećeg nezavisnog skupa $\alpha(G)\le \kappa(G)$ veličina najmanjeg pokrivača klikama

Dokaz: iz svake klike može se odabrati najviše jedan vrh.

**Lema 3**: svaki inducirani podgraf tetivnog grafa je tetivni graf.

Dokaz: kad bi tetivni graf imao inducirani podgraf koji nije tetivni, u tom bi induciranom podgrafu postojao ciklus duljine veće od $3$ bez tetive; tada izvorni graf, kakav god bio (kako god dodavali bridove), ne bi bio tetivni, što je kontradikcija.

**Lema 4**: nijedan inducirani podgraf tetivnog grafa ne može biti ciklus s više od $3$ vrha.

Dokaz: ciklus s više od $3$ vrha nije tetivni graf; primijenimo prethodnu lemu.

## Prepoznavanje tetivnih grafova

### Opis problema

Zadan je neusmjereni graf; odluči je li tetivni.

### Vršni separatori

Za dva vrha $u,v$ grafa $G$ **vršni separator** tih dvaju vrhova je skup vrhova čijim uklanjanjem $u,v$ prestaju biti povezani. Ako nijedan pravi podskup nekog vršnog separatora za $u,v$ nije vršni separator, zovemo ga **minimalnim vršnim separatorom**.

**Lema 5**: minimalni vršni separator za $u,v$ dijeli izvorni graf na nekoliko komponenata povezanosti; neka je $V_1$ komponenta koja sadrži $u$, a $V_2$ komponenta koja sadrži $v$. Tada za svaki vrh $a$ minimalnog vršnog separatora skup $N(a)$ sigurno sadrži vrhove i iz $V_1$ i iz $V_2$.

Dokaz: ako $N(a)$ sadrži vrhove iz najviše jedne od komponenata $V_1$ i $V_2$, uklonimo li $a$ iz separatora, oni ostaju nepovezani, pa izvorni separator nije minimalan.

**Lema 6**: inducirani podgraf minimalnog vršnog separatora za bilo koja dva vrha tetivnog grafa je klika.

Dokaz: ako minimalni vršni separator ima veličinu $\le 1$, inducirani je podgraf očito klika.

Inače neka su $x,y$ dva vrha minimalnog vršnog separatora; po **lemi 5** $N(x)$ sadrži vrhove iz $V_1,V_2$, nazovimo ih $x_1,x_2$, a analogno uzmimo $y_1,y_2$; pazi, može biti $x_1=y_1,x_2=y_2$.

Budući da su $V_1,V_2$ komponente povezanosti, između parova $x_1,y_1$ i $x_2,y_2$ postoje najkraći putovi. Neka su najkraći putovi između $x,y$ unutar $V_1,V_2$ redom $x-x_1\sim y_1-y,x-x_2\sim y_2-y$; tada u grafu postoji ciklus $x-x_1\sim y_1-y-y_2\sim x_2-x$ duljine sigurno $\ge 4$, pa po definiciji tetivnog grafa na tom ciklusu postoji tetiva.

Ako ta tetiva spaja komponente $V_1,V_2$, skup nije vršni separator. Ako spaja dva vrha unutar iste komponente ili vrh unutar komponente s vrhom separatora, narušava svojstvo najkraćeg puta. Dakle, tetiva može spajati samo $x,y$.

Time je dokazano da su u tetivnom grafu svaka dva vrha minimalnog vršnog separatora izravno spojena bridom, pa svojstvo vrijedi.

### Simplicijalni vrhovi

Neka $N(x)$ označava skup vrhova susjednih vrhu $x$. Ako je inducirani podgraf skupa $\{x\}+N(x)$ klika, vrh $x$ zovemo simplicijalnim.

**Lema 7**: svaki tetivni graf ima barem jedan simplicijalni vrh, a tetivni graf koji nije potpun ima barem dva nesusjedna simplicijalna vrha.

Dokaz: matematičkom indukcijom. Svaku komponentu povezanosti promatramo zasebno.

Baza indukcije: kad je graf izomorfan potpunom grafu, svaki je vrh simplicijalan. Kad graf ima $\le 3$ vrha, lema vrijedi.

Ako graf ima $\ge 4$ vrha i nije potpun, postoje $u,v$ takvi da $(u,v)\notin E$. Neka je $I$ minimalni vršni separator za $u,v$. Neka su $A,B$ komponente povezanosti induciranog podgrafa nakon uklanjanja $I$ koje sadrže $u,v$. Zbog simetrije promatramo samo stranu $A$; neka je $L=A+I$. Ako je $L$ potpun graf, $u$ je simplicijalan; ako nije, budući da je $L$ inducirani podgraf izvornog grafa, i on je tetivni, pa ima dva nesusjedna simplicijalna vrha; kako je $I$ klika i svaka dva njezina vrha su susjedna, u $A$ sigurno postoji simplicijalni vrh. Taj je vrh simplicijalan i u cijelom grafu.

Budući da pri svakom koraku graf dijelimo na komponente čija se veličina sigurno smanjuje i koje zadovoljavaju svojstvo, indukcija prolazi.

### Savršeni eliminacijski poredak

Neka je $n=|V|$; savršeni eliminacijski poredak $v_1,v_2,\ldots ,v_n$ je permutacija brojeva $1,2,\ldots ,n$ takva da je $v_i$ simplicijalan vrh u induciranom podgrafu skupa $\{v_i,v_{i+1},\ldots ,v_n\}$.

**Lema 8**: neusmjereni graf je tetivni ako i samo ako ima savršeni eliminacijski poredak.

Dovoljnost: tetivni graf s $1$ vrhom ima savršeni eliminacijski poredak. Po **lemi 3** i **lemi 7** savršeni eliminacijski poredak tetivnog grafa s $n$ vrhova dobiva se iz savršenog eliminacijskog poretka tetivnog grafa s $n-1$ vrhova dodavanjem jednog simplicijalnog vrha.

Nužnost: pretpostavimo da neusmjereni graf ima ciklus s $>3$ vrha i savršeni eliminacijski poredak; neka je $v$ prvi vrh tog ciklusa koji se pojavljuje u savršenom eliminacijskom poretku i neka je $v$ na ciklusu spojen s $v_1,v_2$. Po svojstvu savršenog eliminacijskog poretka, tj. definiciji simplicijalnog vrha, $v_1,v_2$ su izravno spojeni bridom, što je kontradikcija.

### Naivni algoritam

Svaki put nađemo **simplicijalni vrh** $v$ i dodamo ga u savršeni eliminacijski poredak.

Uklonimo vrh $v$ i bridove uz njega iz grafa.

Ponavljamo postupak; ako su svi vrhovi uklonjeni, graf je tetivni i našli smo savršeni eliminacijski poredak; ako u grafu nema simplicijalnog vrha, graf nije tetivni.

Vremenska složenost $O(n^4)$.

### Algoritam MCS

**Algoritam pretraživanja po najvećoj kardinalnosti** (Maximum Cardinality Search) metoda je koja savršeni eliminacijski poredak neusmjerenog grafa nalazi u vremenskoj složenosti $O(n+m)$.

Vrhove numeriramo obrnutim redoslijedom, tj. oznake dodjeljujemo redom od $n$ do $1$.

Neka $label_x$ označava s koliko je već označenih vrhova susjedan vrh $x$; svaki put označimo neoznačeni vrh s najvećom vrijednošću $label$.

Vezanim listama održavamo, za svaki $i$, sve $x$ s $label_x=i$.

Budući da svaki brid doprinosi sumi $\sum_{i=1}^n label_i$ najviše $2$, vremenska složenost je $O(n+m)$.

**Dokaz ispravnosti**:

Neka je $\alpha(x)$ položaj vrha $x$ u tom poretku.
Trebamo dokazati da je za svaki tetivni graf poredak koji algoritam nađe savršeni eliminacijski poredak, tj. da su svi vrhovi koji su u poretku iza nekog vrha i susjedni mu međusobno susjedni.

**Lema 9**: promotrimo tri vrha $u,v,w$ s $\alpha(u)<\alpha(v)<\alpha(w)$; ako je $uw$ brid, a $vw$ nije, tada $w$ doprinosi samo $label$ vrha $u$, a ne vrha $v$. Da bi $v$ ušao u poredak prije $u$, treba postojati $x$ s $\alpha(v)<\alpha(x)$ takav da je $vx$ brid, a $ux$ nije, tj. $x$ doprinosi samo $v$, a ne $u$.

**Lema 10**: u tetivnom grafu sigurno ne postoji niz $v_0,v_1,\dots,v_k(k\ge 2)$ sa sljedećim svojstvima:

1.  $v_iv_j$ je brid ako i samo ako $|i-j|=1$.
2.  $\alpha(v_0)>\alpha(v_i)(i\in[1,k])$.
3.  Postoji $i\in[1,k-1]$ takav da $\alpha(v_i)<\alpha(v_{i+1})<\dots<\alpha(v_k)$ i $\alpha(v_i)<\alpha(v_{i-1})<\dots<\alpha(v_1)<\alpha(v_k)<\alpha(v_0)$.

Dokaz:

Budući da je $\alpha(v_1)<\alpha(v_k)<\alpha(v_0)$, $v_1v_0$ je brid, a $v_kv_0$ nije, po prvom svojstvu postoji $x$ s $\alpha(v_k)<\alpha(x)$ takav da je $v_kx$ brid, a $v_1x$ nije.

Promotrimo najmanji $j\in(1,k]$ takav da je $v_jx$ brid; zaključujemo da $v_0x$ nije brid, jer bi inače $v_0v_1\cdots v_jx$ bio ciklus duljine $\ge 4$ bez tetive.

Ako je $x<v_0$, tada je i $v_0,v_1,\dots,v_j,x$ niz s tim svojstvima; ako je $v_0<x$, tada je $x,v_j,\dots,v_1,v_0$ niz s tim svojstvima.

U gornjem smo izvodu povećali $\min(v_0,v_k)$, pa nastavljajući tako nužno dolazimo do kontradikcije.

**Teorem 1**: za svaki tetivni graf poredak koji nađe algoritam pretraživanja po najvećoj kardinalnosti savršeni je eliminacijski poredak.

Dokaz: promotrimo bilo koja tri vrha $u,v,w$ s $\alpha(u)<\alpha(v)<\alpha(w)$; trebamo dokazati da ako su $uv$ i $uw$ bridovi, onda je i $vw$ brid.

Dokazujemo kontradikcijom: pretpostavimo da nisu susjedni; tada je $w,u,v$ niz sa svojstvima iz **leme 10**, a dokazali smo da takav niz ne postoji; kontradikcija, pa je $vw$ brid.

???+ note "Referentna implementacija"
    ```cpp
    --8<-- "docs/graph/code/chord/chord_1.cpp:var"
    --8<-- "docs/graph/code/chord/chord_1.cpp:mcs"
    ```

Ako je izvorni graf tetivni, dobiveni je poredak savršeni eliminacijski poredak; no budući da izvorni graf možda nije tetivni, i tada dobiveni poredak sigurno nije savršeni eliminacijski poredak, pa se problem svodi na **provjeru je li dobiveni poredak savršeni eliminacijski poredak izvornog grafa**.

### Provjera je li poredak savršeni eliminacijski poredak

#### Naivni algoritam

Po definiciji redom provjeravamo tvore li vrhovi iz $\{v_i,v_{i+1},\ldots ,v_n\}$ susjedni vrhu $v_i$ u poretku $v$ kliku. Vremenska složenost $O(nm)$.

#### Poboljšani algoritam

Neka je $N^+(u)$ skup vrhova koji su u poretku iza $u$ i susjedni s $u$, a $f(u)$ onaj među njima koji je u poretku najraniji. Za svaki vrh $u$ s nepraznim $N^+(u)$ dovoljno je provjeriti je li svaki vrh iz $N^+(u)\setminus\{f(u)\}$ susjedan s $f(u)$.

Taj je uvjet očito nužan. Dovoljnost se dokazuje indukcijom po poretku odostraga: ako svi kasniji vrhovi zadovoljavaju zahtjev savršenog eliminacijskog poretka, tada je $N^+(f(u))$ klika. Ako provjera prolazi, $N^+(u)\setminus\{f(u)\}\subseteq N^+(f(u))$ i svi su ti vrhovi susjedni s $f(u)$, pa je i $N^+(u)$ klika. Kad je $N^+(u)$ prazan, provjera nije potrebna.

Najprije prolaskom po listama susjedstva odredimo $f(u)$ za svaki vrh i vrhove s jednakim $f(u)$ stavimo u istu grupu. Pri obradi grupe s $f(u)=v$ najprije označimo sve susjede vrha $v$, a zatim prođemo po listi susjedstva svakog vrha $u$ u grupi i provjerimo jesu li svi susjedi koji su u poretku iza $v$ označeni. Koristimo li broj vrha $v$ kao vrijednost oznake, ne moramo brisati polje oznaka nakon svake grupe. Svaki vrh pripada najviše jednoj grupi, a lista susjedstva svakog vrha prolazi se najviše jednom pri određivanju $f(u)$, pri označavanju i pri provjeri, pa je ukupna vremenska složenost $O(n+m)$.

???+ note "Referentna implementacija"
    ```cpp
    --8<-- "docs/graph/code/chord/chord_1.cpp:var"
    --8<-- "docs/graph/code/chord/chord_1.cpp:core"
    ```

Time se **problem prepoznavanja tetivnih grafova** rješava u vremenskoj složenosti $O(n+m)$.

## Maksimalne klike tetivnog grafa

Neka je $N(x)$ skup vrhova izravno spojenih bridom s $x$ koji su u savršenom eliminacijskom poretku iza $x$. Tada je svaka maksimalna klika tetivnog grafa oblika $\{x\}+N(x)$.

Dokaz: promotrimo maksimalnu kliku $V$ tetivnog grafa i njezin vrh $x$ koji se prvi pojavljuje u savršenom eliminacijskom poretku; sigurno je $V\subseteq \{x\}+N(x)$, a kako je $V$ maksimalna klika, $V=\{x\}+N(x)$.

Tetivni graf ima najviše $n$ maksimalnih klika. Da bismo našli sve maksimalne klike tetivnog grafa, možemo za svaki $\{x\}+N(x)$ provjeriti je li maksimalna klika.

Neka je $A=\{x\}+N(x),B=\{y\}+N(y)$; ako je $A\subsetneqq B$, $A$ nije maksimalna klika. Tada je u savršenom eliminacijskom poretku očito $y$ ispred $x$.

Neka $nxt_x$ označava vrh iz $N(x)$ koji je u savršenom eliminacijskom poretku najraniji, a $y*$ najkasniji među svim $y$ za koje vrijedi $A\subseteq B$. Tada nužno vrijedi $nxt_{y*}=x$, jer inače $y*$ ne bi bio najkasniji: $y*=nxt_{y*}$ i dalje bi zadovoljavao uvjet.

$A\subsetneqq B$ ako i samo ako $|A|+1\le |B|$.

Problem se svodi na provjeru postoji li $y$ takav da $nxt_y=x$ i $|N(x)|+1\le |N(y)|$. Vremenska složenost $O(n+m)$.

```cpp
for (int i = 1; i <= n; i++) {
  cur = 0;
  for (vector<int>::iterator it = G[p[i]].begin(); it != G[p[i]].end(); it++)
    if (rnk[p[i]] < rnk[*it]) {
      s[++cur] = *it;
      if (rnk[s[cur]] < rnk[s[1]]) swap(s[1], s[cur]);
    }
  fst[p[i]] = s[1];
  N[p[i]] = cur;
}
for (int i = 1; i <= n; i++) {
  if (!vis[p[i]]) ans++;
  if (N[p[i]] >= N[fst[p[i]]] + 1) vis[fst[p[i]]] = true;
}
```

## Kromatski broj / klikovni broj tetivnog grafa

Konstrukcija: vrhove bojimo redom po savršenom eliminacijskom poretku odostraga, svakom vrhu dajući najmanju boju koju smije dobiti. Vremenska složenost $O(m+n)$.

Dokaz ispravnosti: neka opisana metoda koristi $t$ boja; tada je $t\ge \chi(G)$. Budući da svi vrhovi klike imaju različite boje, $t=\omega(G)$, a po **lemi 1** $t=\omega(G)\le \chi(G)$. Dakle, $t=\chi(G)=\omega(G)$.

Kad ne trebamo samo bojenje, nego samo kromatski/klikovni broj tetivnog grafa, dovoljno je uzeti najveću vrijednost $|\{x\}+N(x)|$.

```cpp
for (int i = 1; i <= n; i++) ans = max(ans, deg[i] + 1);
```

## Najveći nezavisan skup / najmanji pokrivač klikama tetivnog grafa

Najveći nezavisan skup: idemo po savršenom eliminacijskom poretku od početka i biramo svaki vrh koji nije izravno spojen bridom ni s jednim već odabranim vrhom.

Najmanji pokrivač klikama: neka je najveći nezavisan skup $\{v_1,v_2,\ldots ,v_t\}$; tada je skup klika $\{\{v_1+N(v_1)\},\{v_2+N(v_2)\},\ldots ,\{v_t+N(v_t)\} \}$ najmanji pokrivač klikama grafa. Vremenska složenost obaju postupaka je $O(n+m)$.

Dokaz ispravnosti: neka su veličina nezavisnog skupa i broj klika u pokrivaču iz gornjeg postupka jednaki $t$; po definiciji je $t\le \alpha(G),t\ge \kappa(G)$, a po **lemi 2** $\alpha(G)\le \kappa(G)$, pa je $t=\alpha(G)=\kappa(G)$.

```cpp
for (int i = 1; i <= n; i++)
  if (!vis[p[i]]) {
    ans++;
    for (vector<int>::iterator it = G[p[i]].begin(); it != G[p[i]].end(); it++)
      vis[*it] = true;
  }
```

## Zadaci

[Library Checker - Chordal Graph Recognition](https://judge.yosupo.jp/problem/chordal_graph_recognition)

[SPOJ FISHNET - Fishing Net](https://www.spoj.com/problems/FISHNET)

[P3196 \[HNOI2008\] Čarobna zemlja](https://www.luogu.com.cn/problem/P3196)

[P3852 \[TJOI2007\] Djeca](https://www.luogu.com.cn/problem/P3852)

## Literatura

[O tetivnim grafovima (kineski)](https://yhx-12243.github.io/OI-transit/memos/15.html)

[Predavanje s WC 2009 (kineski)](https://github.com/hzwer/shareOI/blob/master/%E5%9B%BE%E8%AE%BA/%E5%BC%A6%E5%9B%BE%E4%B8%8E%E5%8C%BA%E9%97%B4%E5%9B%BE_%E9%99%88%E4%B8%B9%E7%90%A6.pptx)

[Sažetak o tetivnim grafovima - zhoushuyu (kineski)](https://www.cnblogs.com/zhoushuyu/p/8716935.html)

[R. E. Tarjan and M. Yannakakis, Simple linear-time algorithms to test chordality of graphs,test acyclicity of hypergraphs,and selectively reduce acyclic hypergraphs, SIAM J. Comput., 13 (1984), pp. 566–579.](https://dl.acm.org/doi/abs/10.1137/0213035)
