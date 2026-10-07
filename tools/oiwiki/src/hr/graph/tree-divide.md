---
title: Dekompozicija stabla
---

## Centroidna dekompozicija

Centroidna dekompozicija (point divide and conquer, centroid decomposition) prikladna je za probleme s informacijama o putovima u velikim stablima.

??? note "Primjer 1 [Luogu P3806【模板】点分治 1](https://www.luogu.com.cn/problem/P3806)"
    Zadano je stablo s $n$ vrhova i težinama na bridovima te $m$ upita; u svakom upitu zadano je $k$ i pita se postoji li u stablu par vrhova na udaljenosti $k$.
    
    $n\le 10000,m\le 100,k\le 10000000$

Najprije proizvoljno odaberemo vrh $\mathit{rt}$ kao korijen. Svi putovi koji u cijelosti leže u njegovu podstablu dijele se na dvije vrste: one koji prolaze kroz trenutni korijen i one koji ne prolaze. Putovi kroz trenutni korijen dijele se dalje na dvije vrste: one kojima je korijen jedna krajnja točka i one kojima nijedna krajnja točka nije korijen. Potonji se mogu dobiti spajanjem dvaju lanaca prve vrste. Dakle, za odabrani korijen $rt$ najprije izračunamo doprinos odgovoru svih putova u njegovu podstablu koji prolaze kroz taj vrh, a zatim rekurzivno riješimo njegova podstabla za putove koji kroz njega ne prolaze.

U ovom zadatku za putove kroz korijen $\mathit{rt}$ najprije prolazimo kroz svu njegovu djecu $\mathit{ch}$ i, s $\mathit{ch}$ kao korijenom, računamo udaljenosti svih vrhova podstabla $\mathit{ch}$ do $\mathit{rt}$. Označimo s $\mathit{dist}_i$ udaljenost vrha $i$ do trenutnog korijena $rt$, a s $\mathit{tf}_{d}$ postoji li u već obrađenim podstablima vrh $v$ takav da je $\mathit{dist}_v=d$. Ako za neki upit $k$ vrijedi $tf_{k-\mathit{dist}_i}=true$, postoji put duljine $k$. Nakon što izračunamo mogu li bridovi iz podstabla $\mathit{ch}$ dati odgovor, te nove udaljenosti dodajemo u niz $\mathit{tf}$.

Pazite da se niz $\mathit{tf}$ ne smije prazniti izravno s `memset`; umjesto toga prethodno zauzete pozicije u $\mathit{tf}$ stavljamo u red i tako ih praznimo, jer samo tako jamčimo vremensku složenost.

U centroidnoj dekompoziciji svi rekurzivni pozivi na jednoj razini zajedno obrade svaki vrh jednom; ako ima ukupno $h$ razina rekurzije, ukupna je vremenska složenost $O(hn)$.

Ako svaki put kao korijen odaberemo [centroid](./tree-centroid.md) podstabla, broj razina rekurzije je najmanji mogući, a vremenska složenost $O(n\log n)$. Zato se ovaj postupak u međunarodnoj natjecateljskoj zajednici obično naziva **centroidna dekompozicija** (centroid decomposition) stabla.

Pazite da nakon ponovnog odabira korijena obavezno treba ponovno izračunati veličine podstabala; inače naizgled sitna promjena može pokvariti vremensku složenost ili ugroziti ispravnost.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/graph/code/tree-divide/tree-divide_1.cpp"
    ```

??? note "Primjer 2 [Luogu P4178 Tree](https://www.luogu.com.cn/problem/P4178)"
    Zadano je težinsko stablo s $n$ vrhova i broj $k$; treba odrediti broj parova vrhova čija je udaljenost u stablu najviše $k$.
    
    $n\le 40000,k\le 20000,w_i\le 1000$

Budući da ovdje tražimo broj parova vrhova na udaljenosti iz $[0,k]$, za održavanje i upite koristimo segment tree.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/graph/code/tree-divide/tree-divide_2.cpp"
    ```

??? note "Primjer 3 [Luogu P2664 树上游戏](https://www.luogu.com.cn/problem/P2664)"
    Zadano je stablo u kojem svaki vrh ima boju. Definiramo $s(i,j)$ kao broj različitih boja na putu od $\mathit{i}$ do $\mathit{j}$ i $\mathit{sum_{i}}=\sum_{j=1}^n s(i,j)$. Za sve $1\leq i\leq n$ izračunajte $sum_i$. ($1 \le n, c_i \le 10^5$)

Ovaj zadatak dobro ispituje razumijevanje i primjenu ideje centroidne dekompozicije; pogodan je kao teži primjer i vježba.

Prvo moramo shvatiti jednu pretvorbu. Zadatak definira $\mathit{sum_i}$ kao zbroj brojeva boja na putovima od $i$ do svih vrhova, ali s tom definicijom odgovor je u centroidnoj dekompoziciji teško zbrajati, jer je teško spojiti informacije dvaju podstabala koja izlaze iz trenutnog korijena. Zato mijenjamo značenje $\mathit{sum_i}$. Za svaku boju $j$ označimo s $\mathit{cnt_j}$ broj putova kojima je jedna krajnja točka $i$ i koji sadrže boju $j$; tada je $\mathit{sum_i}$ zapravo $\sum \mathit{cnt_j}$. Ta pretvorba samo mijenja predmet promatranja: gledamo doprinos svake boje vrijednosti $\mathit{sum_i}$. A $\mathit{cnt_j}$ je lako izračunati: svaki put kad naiđemo na novu boju napravimo $\mathit{cnt_{col_u}}+=\mathit{size_u}$, gdje je $\mathit{size_u}$ veličina podstabla vrha $u$, što znači da svi vrhovi tog podstabla preko te boje daju po jedan doprinos odgovoru za $u$.

U centroidnoj dekompoziciji dovoljno je zasebno izbrojiti:

1.  doprinos korijenu od putova u podstablu kojima je trenutni korijen krajnja točka;
2.  doprinos svakom vrhu podstabla od putova kojima je LCA trenutni korijen.

Dio 1 je jednostavan: budući da u centroidnoj dekompoziciji broj razina rekurzije ne prelazi $\log{n}$, na svakoj razini možemo obići cijelo podstablo i tada, tijekom obilaska, odgovor zbrajati izravno po definiciji $\mathit{sum_i}$.

Za dio 2 neka je $d$ dijete trenutnog korijena $u$, a $v$ proizvoljan vrh iz podstabla $d$. Odgovor za $v$ dijeli se na dva dijela:

1.  Boje koje se pojavljuju na putu $(u, v)$; neka ih je $\mathit{num}$, a neka je $\mathit{siz1}$ ukupna veličina svih podstabala vrha $u$ osim $d$. Tada je doprinos tih boja odgovoru za $v$ jednak $\mathit{num}\times \mathit{siz1}$.
2.  Boje $j$ koje se ne pojavljuju na putu $(u, v)$; njihov doprinos dolazi iz $\mathit{cnt_j}$ svih podstabala vrha $u$ osim $d$, pa je taj dio odgovora $\sum_{j \notin (u, v)} \mathit{cnt_j}$.

To je cijela ideja prebrojavanja; detalji implementacije nalaze se u referentnom kodu.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/graph/code/tree-divide/tree-divide_3.cpp"
    ```

## Bridna dekompozicija

Slično centroidnoj dekompoziciji, odaberemo brid koji stablo dijeli što ravnomjernije na dva dijela (tako da su $\mathit{size}$ dvaju podstabala koja brid spaja što bliži). Zatim rekurzivno obradimo lijevo i desno podstablo i prikupimo informacije.

No to ne radi; promotrimo zvjezdasti graf (tzv. „graf tratinčice”):

![zvjezdasti graf](./images/tree-divide1.svg)

Vidimo da je vremenska složenost bridne dekompozicije neprihvatljiva kad vrh ima mnogo djece sličnog $\mathit{size}$.

Da je graf binarno stablo, nedostatak bridne dekompozicije na zvjezdastom grafu ne bi se pojavio. Zato pretvaramo stablo s proizvoljnim stupnjevima u binarno stablo.

Očito je dovoljno graditi stablo kao kod segment treea, ovako:

![gradnja stabla](./images/tree-divide2.svg)

Novostvorenim vrhovima dajemo odgovarajuće informacije prema zahtjevima zadatka. Na primjer, kad brojimo duljine putova, izvornim bridovima dajemo težinu $1$, a novim bridovima težinu $0$.

Analiza složenosti pokazuje da se dodaje najviše $O(n)$ vrhova, pa je ukupna složenost $O(n\log n)$.

Gotovo svaki zadatak koji se rješava centroidnom dekompozicijom može se riješiti i bridnom (razlika je u konstanti, ali nije presudna), pa primjere ne navodimo.

## Centroidno stablo

Centroidno stablo (point divide tree) rekonstruirano je stablo koje promjenom oblika izvornog stabla broj razina čini stabilno $\log n$.

Često se koristi za probleme s izmjenama koji ne ovise o izvornom obliku stabla.

### Analiza algoritma

Izvorno stablo rekonstruiramo tako da u centroidnoj dekompoziciji svaki put tražimo centroid.

Svaki pronađeni centroid povežemo kao dijete s centroidom prethodne razine; tako nastaje stablo s $\log n$ razina.

Budući da stablo ima $\log n$ razina, mnogi brute-force pristupi koji inače ne bi prošli na centroidnom stablu imaju ispravnu složenost.

### Implementacija

Mali trik: ako od ukupne veličine $\mathit{tot}$ prethodne razine rekurzije oduzmemo veličinu teškog djeteta vrha prethodne razine, dobivamo ukupnu veličinu ove razine. Tako je za traženje centroida dovoljan jedan DFS.

???+ note "Referentni kod"
    ```cpp
    #include <algorithm>
    #include <iostream>
    #include <vector>
    using namespace std;
    
    using IT = vector<int>::iterator;
    
    struct Edge {
      int to, nxt, val;
    
      Edge() {}
    
      Edge(int to, int nxt, int val) : to(to), nxt(nxt), val(val) {}
    } e[300010];
    
    int head[150010], cnt;
    
    void addedge(int u, int v, int val) {
      e[++cnt] = Edge(v, head[u], val);
      head[u] = cnt;
    }
    
    int siz[150010], son[150010];
    bool vis[150010];
    
    int tot, lasttot;
    int maxp, root;
    
    void getG(int now, int fa) {
      siz[now] = 1;
      son[now] = 0;
      for (int i = head[now]; i; i = e[i].nxt) {
        int vs = e[i].to;
        if (vs == fa || vis[vs]) continue;
        getG(vs, now);
        siz[now] += siz[vs];
        son[now] = max(son[now], siz[vs]);
      }
      son[now] = max(son[now], tot - siz[now]);
      if (son[now] < maxp) {
        maxp = son[now];
        root = now;
      }
    }
    
    struct Node {
      int fa;
      vector<int> anc;
      vector<int> child;
    } nd[150010];
    
    int build(int now, int ntot) {
      tot = ntot;
      maxp = 0x7f7f7f7f;
      getG(now, 0);
      int g = root;
      vis[g] = true;
      for (int i = head[g]; i; i = e[i].nxt) {
        int vs = e[i].to;
        if (vis[vs]) continue;
        int tmp = build(vs, ntot - son[vs]);
        nd[tmp].fa = now;
        nd[now].child.push_back(tmp);
      }
      return g;
    }
    
    int virtroot;
    
    int main() {
      int n;
      cin >> n;
      for (int i = 1; i < n; i++) {
        int u, v, val;
        cin >> u >> v >> val;
        addedge(u, v, val);
        addedge(v, u, val);
      }
      virtroot = build(1, n);
    }
    ```
