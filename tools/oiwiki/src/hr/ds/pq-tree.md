---
title: PQ stablo
---

author: isdanni,xyf007

PQ stablo struktura je podataka temeljena na stablu koja predstavlja skup permutacija nekog skupa elemenata; otkrili su je i imenovali Kellogg S. Booth i George S. Lueker 1976. godine, a služi za rješavanje sljedećeg problema:

> Zadano je $m$ skupova $S_i$; treba pronaći permutaciju brojeva $1\sim n$ u kojoj su elementi svakog skupa međusobno susjedni.

PQ stablo može se izgraditi u vremenu $O(n+\sum|S_i|)$. Metoda izgradnje opisana u ovom članku ima složenost $O(nm)$.

## Definicija

PQ stablo ima tri vrste čvorova: **listove**, **P čvorove** i **Q čvorove**. List predstavlja jedan element permutacije, P čvor označava da se njegova djeca mogu proizvoljno permutirati, a Q čvor označava da se redoslijed njegove djece može obrnuti. Svi čvorovi koji nisu listovi su P ili Q čvorovi. P čvor ima barem 2 djeteta, a Q čvor barem 3.  
Zbog definicije čvorova PQ stablo predstavlja **sva** dopustiva rješenja, a njegov preorder obilazak jedno je od njih.  
Donja slika prikazuje jedno PQ stablo.  
![](https://gregable.com/2008/11/i/pq-tree.webp)  
Njegov preorder obilazak 1,2,3,4,5 predstavlja jedno dopustivo rješenje. Ako djecu P čvora preuredimo u 4,2,3, dobivamo drugo dopustivo rješenje 1,4,2,3,5. Ako redoslijed djece P čvora ostavimo nepromijenjen, a redoslijed djece Q čvora obrnemo, dobivamo još jedno dopustivo rješenje 5,3,2,4,1.

## Izgradnja

**PQ stablo koristi prikaz dijete-brat (child-sibling).**

PQ stablo gradimo inkrementalno.

Najprije izgradimo stablo čiji je korijen P čvor s ukupno $n$ djece, redom $1,2,\ldots,n$; ono predstavlja PQ stablo bez ikakvih ograničenja. Kako dodajemo ograničenja, stablo neprestano mijenjamo.

Kad dodamo novi skup ograničenja $S$, sve listove koji pripadaju tom skupu označimo **crnom**, a listove koji nisu u skupu **bijelom**. Za sve čvorove koji nisu listovi: ako su im sva djeca crna, označimo ih crnom; ako su im sva djeca bijela, označimo ih bijelom; inače ih označimo **sivom**. Na donjim slikama crni, bijeli i sivi čvorovi prikazani su redom crnom, sivom te pola crnom pola sivom bojom.

Zahtijevamo da su čvorovi PQ stabla poredani po boji.

### Metoda odozdo prema gore

Najmanje podstablo koje sadrži sve crne čvorove naziva se **relevantno podstablo**, a korijen relevantnog podstabla (koji ne mora biti korijen cijelog stabla) **relevantni korijen**.

Postupak dodavanja jednog ograničenja naziva se redukcija (reduction). Jedna redukcija ima dvije faze: fazu izdizanja (bubbling) i fazu smanjivanja.

#### Faza izdizanja

Faza izdizanja obrađuje samo relevantno podstablo. Sve čvorove relevantnog podstabla označimo crnom ili sivom i za svaki čvor izračunamo broj njegove relevantne djece. Da bismo to učinkovito obavili, relevantno podstablo obrađujemo od listova prema korijenu. Za to je potrebno pamtiti roditelja svakog čvora, ali se u fazi smanjivanja roditelj čvora često mijenja. Da bi izgradnja bila linearna, samo djeca P čvorova i **posljednje dijete Q čvora** uvijek imaju ispravno zapisanog roditelja. Ostaloj djeci Q čvora roditelj se u fazi izdizanja ažurira roditeljem posljednjeg djeteta.

Kad naiđemo na čvor u sredini, provjerimo imaju li njegova braća već ispravnog roditelja. Ako ne, označimo ga **blokiranim**. Ako njegov brat kasnije dobije ispravnog roditelja, ažuriramo roditelja ovog čvora i uklonimo oznaku. Ako na kraju faze izdizanja i dalje postoji niz uzastopnih blokiranih čvorova (kao u slučaju Q3 dolje), „pseudočvor” bez roditelja postaje roditelj tog bloka i uklanja se u fazi smanjivanja.

#### Faza smanjivanja

Faza smanjivanja obrađuje čvorove pomoću reda. Najprije u red dodamo sve listove iz ograničenja. Svaki put uzmemo čvor $u$ s početka reda i obradimo ga. Ako je roditelj čvora $u$ također čvor relevantnog podstabla, u red dodamo $\mathit{fa}_u$.  
Za svaki čvor $u$ razlikujemo slučajeve. Ako ne pripada nijednom od njih, rješenje ne postoji.

##### List

Označimo $u$ crnom.

##### P čvor

Ako su sva djeca crna, označimo $u$ crnom.  
![](https://gregable.com/2008/11/i/p1-template.png)  
![](https://gregable.com/2008/11/i/p1-replacement.png)

Ako $u$ ima i crnu i bijelu djecu te je $u$ relevantni korijen, stvorimo novi P čvor $v$ koji postaje korijen sve njegove crne djece.  
![](https://gregable.com/2008/11/i/p2-template.png)  
![](https://gregable.com/2008/11/i/p2-replacement.png)

Ako $u$ ima i crnu i bijelu djecu, a $u$ nije relevantni korijen, učinimo sljedeće:

-   Stvorimo novi P čvor $f$ koji postaje korijen sve crne djece.
-   Stvorimo novi P čvor $e$ koji postaje korijen sve bijele djece.
-   Ako $e$ (i/ili $f$) ima samo jedno dijete, ne stvaramo novi čvor, nego $e$ (i/ili $f$) izravno postavimo na to dijete.
-   Čvor $u$ pretvorimo u Q čvor s djecom $e$ i $f$ i označimo ga sivom.

Primijetite da prema ranijoj definiciji Q čvor ima barem 3 djeteta, pa se ovaj $u$ smatra „pseudočvorom” i obrađuje se dalje poslije.  
![](https://gregable.com/2008/11/i/p3-template.png)  
![](https://gregable.com/2008/11/i/p3-replacement.png)

Ako $u$ ima jedno sivo dijete $p$ i $u$ je relevantni korijen, stvorimo novi P čvor $v$ kao korijen sve njegove crne djece, brata čvora $v$ postavimo na posljednje crno dijete čvora $p$, a zatim $v$ postavimo kao posljednje dijete čvora $p$.  
![](https://gregable.com/2008/11/i/p4-template.png)  
![](https://gregable.com/2008/11/i/p4-replacement.png)

Ako $u$ ima jedno sivo dijete $p$, a $u$ nije relevantni korijen, učinimo sljedeće:

-   Stvorimo novi P čvor $f$ koji postaje korijen sve crne djece.
-   Stvorimo novi P čvor $e$ koji postaje korijen sve bijele djece.
-   Ako $e$ (i/ili $f$) ima samo jedno dijete, ne stvaramo novi čvor, nego $e$ (i/ili $f$) izravno postavimo na to dijete.
-   Brata čvora $e$ postavimo na posljednje bijelo dijete čvora $p$, a zatim $e$ postavimo kao posljednje dijete čvora $p$.
-   Brata čvora $f$ postavimo na posljednje crno dijete čvora $p$, a zatim $f$ postavimo kao posljednje dijete čvora $p$.

![](https://gregable.com/2008/11/i/p5-template.png)  
![](https://gregable.com/2008/11/i/p5-replacement.png)

Ako $u$ ima točno dvoje sive djece $p_1,p_2$, učinimo sljedeće:

-   Stvorimo novi P čvor $f$ koji postaje korijen sve crne djece.
-   Ako $f$ ima samo jedno dijete, ne stvaramo novi čvor, nego $f$ izravno postavimo na to dijete.
-   Brata posljednjeg crnog djeteta čvora $p_1$ postavimo na $f$.
-   Brata čvora $f$ postavimo na posljednje crno dijete čvora $p_2$.
-   Posljednje dijete čvora $p_2$ postavimo na posljednje bijelo dijete čvora $p_2$.

Vidimo da je tako $p_2$ spojen u $p_1$.  
![](https://gregable.com/2008/11/i/p6-template.png)  
![](https://gregable.com/2008/11/i/p6-replacement.png)

##### Q čvor

Ako $u$ ima samo crnu djecu, označimo $u$ crnom. (Oblik na donjoj slici je pogrešan.)  
![](https://gregable.com/2008/11/i/q1-template.png)  
![](https://gregable.com/2008/11/i/q1-replacement.png)

Ako $u$ ima jedno sivo dijete $p$ i sva djeca iste oznake pojavljuju se uzastopno, učinimo sljedeće:

-   Neka je $p_f$ posljednje crno dijete čvora $p$, $p_e$ posljednje bijelo dijete čvora $p$, $f$ crni brat čvora $p$, a $e$ bijeli brat čvora $p$.
-   Brata čvora $f$ postavimo na $p_f$, a brata čvora $e$ na $p_e$.
-   Ako $p$ nema bijelog ili crnog brata, posljednje dijete čvora $u$ postavimo na posljednje dijete čvora $p$.
-   Izbrišemo $p$.

![](https://gregable.com/2008/11/i/q2-template.png)  
![](https://gregable.com/2008/11/i/q2-replacement.png)

Ako $u$ ima točno dvoje sive djece $p_1,p_2$ i sva djeca iste oznake pojavljuju se uzastopno, dovoljno je prethodnu operaciju primijeniti i na $p_1$ i na $p_2$.  
![](https://gregable.com/2008/11/i/q3-template.png)  
![](https://gregable.com/2008/11/i/q3-replacement.png)

Ova je metoda izgradnje iz izvornog rada, ali je nezgodna za implementaciju.

### Metoda odozgo prema dolje

Većina implementacija u natjecateljskom programiranju trenutačno koristi ovu metodu. Metoda je zapravo slična; slučajevi koji se pojavljuju dolje uglavnom se mogu pronaći gore.

Primijetite da prema prethodnom postupku bojenja svi crni i bijeli čvorovi već zadovoljavaju uvjet, pa **trebamo obraditi samo sive čvorove**.

#### P čvor

-   Ako $u$ ima više od dvoje sive djece, rješenje ne postoji.
-   Ako $u$ ima samo jedno sivo dijete i nema crne djece, rekurzivno obradimo sivo dijete.
-   Inače najprije ispraznimo djecu čvora $u$, a zatim dodamo svu bijelu djecu. Stvorimo novi Q čvor $q_1$ koji postaje dijete čvora $u$. U $q_1$ dodamo svu sivu djecu. Stvorimo novi P čvor $p$ kao korijen sve crne djece i umetnemo $p$ u sredinu $q_1$. (Odgovara svim slučajevima P čvora u metodi odozdo prema gore.)

Primijetite da ćemo za dva siva čvora zahtijevati da su svi bijeli s lijeve, a svi crni s desne strane (ili obrnuto), pa trebamo implementirati funkciju razdvajanja `split` koja čvorove tog podstabla razdvaja na crni i bijeli dio i pri tome čuva **sve mogućnosti** čvorova nastalih podstabala.

#### Q čvor

-   Nađemo položaje $l,r$ krajnjeg lijevog i krajnjeg desnog čvora koji nije bijel. Ako unutar $[l+1,r-1]$ postoji čvor koji nije crn, rješenje ne postoji.
-   Ako nema crnih čvorova i postoji samo jedan sivi čvor, rekurzivno obradimo taj sivi čvor; inače je dovoljno razdvojiti čvorove na položajima $l$ i $r$.

#### Funkcija razdvajanja

Neka je čvor koji razdvajamo $u$; želimo $u$ razdvojiti u šumu u kojoj je lijevo sve bijelo, a desno sve crno. Ako $u$ nije siv, izravno vratimo podstablo. Razmatramo samo sive čvorove.
Ako je $u$ P čvor:

-   Ako $u$ ima barem dvoje sive djece, rješenje ne postoji.
-   Inače su lijevo sva bijela djeca, u sredini rekurzivno obrađeno sivo dijete, a desno sva crna djeca. Da bismo zadržali sve mogućnosti, stvaramo dva nova P čvora kao korijene bijele odnosno crne djece. (Odgovara slučaju P4 u metodi odozdo prema gore.)
-   Izbrišemo $u$.

Ako je $u$ Q čvor:

-   Ako ni izravni ni obrnuti redoslijed ne zadovoljava raspored bijelo-sivo-crno, rješenje ne postoji.
-   Ako ima barem dvoje sive djece, rješenje također ne postoji.
-   Inače rekurzivno razdvojimo sivo dijete.
-   Izbrišemo $u$.

Na kraju izbrišemo sve suvišne čvorove (čvorove sa samo jednim djetetom).

## Implementacija

```cpp
class PQTree {
 public:
  PQTree() {}

  void Init(int n) {
    n_ = n, rt_ = tot_ = n + 1;
    for (int i = 1; i <= n; i++) g_[rt_].emplace_back(i);
  }

  void Insert(const std::string &s) {
    s_ = s;
    Dfs0(rt_);
    Work(rt_);
    while (g_[rt_].size() == 1) rt_ = g_[rt_][0];
    Remove(rt_);
  }

  std::vector<int> ans() {
    DfsAns(rt_);
    return ans_;
  }

  ~PQTree() {}

 private:
  int n_, rt_, tot_, pool_[100001], top_, typ_[100001] /* 0-P 1-Q */,
      col_[100001] /* 0-black 1-white 2-grey */;
  std::vector<int> g_[100001], ans_;
  std::string s_;

  void Fail() {
    std::cout << "NO\n";
    std::exit(0);
  }

  int NewNode(int ty) {
    int x = top_ ? pool_[top_--] : ++tot_;
    typ_[x] = ty;
    return x;
  }

  void Delete(int u) { g_[u].clear(), pool_[++top_] = u; }

  void Dfs0(int u) {  // get color of each node
    if (u >= 1 && u <= n_) {
      col_[u] = s_[u] == '1';
      return;
    }
    bool c0 = false, c1 = false;
    for (auto &&v : g_[u]) {
      Dfs0(v);
      if (col_[v]) c1 = true;
      if (col_[v] != 1) c0 = true;
    }
    if (c0 && !c1)
      col_[u] = 0;
    else if (!c0 && c1)
      col_[u] = 1;
    else
      col_[u] = 2;
  }

  bool Check(const std::vector<int> &v) {
    int p2 = -1;
    for (int i = 0; i < static_cast<int>(v.size()); i++)
      if (col_[v[i]] == 2) {
        if (p2 != -1) return false;
        p2 = i;
      }
    if (p2 == -1)
      for (int i = 0; i < static_cast<int>(v.size()); i++)
        if (col_[v[i]]) {
          p2 = i;
          break;
        }
    for (int i = 0; i < p2; i++)
      if (col_[v[i]]) return false;
    for (int i = p2 + 1; i < static_cast<int>(v.size()); i++)
      if (col_[v[i]] != 1) return false;
    return true;
  }

  std::vector<int> Split(int u) {
    if (col_[u] != 2) return {u};
    std::vector<int> ng;
    if (typ_[u]) {  // Q
      if (!Check(g_[u])) {
        std::reverse(g_[u].begin(), g_[u].end());
        if (!Check(g_[u])) Fail();
      }
      for (auto &&v : g_[u])
        if (col_[v] != 2) {
          ng.emplace_back(v);
        } else {
          auto s = Split(v);
          ng.insert(ng.end(), s.begin(), s.end());
        }
    } else {  // P
      std::vector<int> son[3];
      for (auto &&x : g_[u]) son[col_[x]].emplace_back(x);
      if (son[2].size() > 1) Fail();
      if (!son[0].empty()) {
        int n0 = NewNode(0);
        g_[n0] = son[0];
        ng.emplace_back(n0);
      }
      if (!son[2].empty()) {
        auto s = Split(son[2][0]);
        ng.insert(ng.end(), s.begin(), s.end());
      }
      if (!son[1].empty()) {
        int n1 = NewNode(0);
        g_[n1] = son[1];
        ng.emplace_back(n1);
      }
    }
    Delete(u);
    return ng;
  }

  void Work(int u) {
    if (col_[u] != 2) return;
    if (typ_[u]) {  // Q
      int l = 1e9, r = -1e9;
      for (int i = 0; i < static_cast<int>(g_[u].size()); i++)
        if (col_[g_[u][i]]) checkmin(l, i), checkmax(r, i);
      for (int i = l + 1; i < r; i++)
        if (col_[g_[u][i]] != 1) Fail();
      if (l == r && col_[g_[u][l]] == 2) {
        Work(g_[u][l]);
        return;
      }
      std::vector<int> ng;
      for (int i = 0; i < l; i++) ng.emplace_back(g_[u][i]);
      auto s = Split(g_[u][l]);
      ng.insert(ng.end(), s.begin(), s.end());
      for (int i = l + 1; i < r; i++) ng.emplace_back(g_[u][i]);
      if (l != r) {
        s = Split(g_[u][r]);
        std::reverse(s.begin(), s.end());
        ng.insert(ng.end(), s.begin(), s.end());
      }
      for (int i = r + 1; i < static_cast<int>(g_[u].size()); i++)
        ng.emplace_back(g_[u][i]);
      g_[u] = ng;
    } else {  // P
      std::vector<int> son[3];
      for (auto &&x : g_[u]) son[col_[x]].emplace_back(x);
      if (son[1].empty() && son[2].size() == 1) {
        Work(son[2][0]);
        return;
      }
      g_[u].clear();
      if (son[2].size() > 2) Fail();
      g_[u] = son[0];
      int n1 = NewNode(1);
      g_[u].emplace_back(n1);
      if (son[2].size() >= 1) {
        auto s = Split(son[2][0]);
        g_[n1].insert(g_[n1].end(), s.begin(), s.end());
      }
      if (son[1].size()) {
        int n2 = NewNode(0);
        g_[n1].emplace_back(n2);
        g_[n2] = son[1];
      }
      if (son[2].size() >= 2) {
        auto s = Split(son[2][1]);
        std::reverse(s.begin(), s.end());
        g_[n1].insert(g_[n1].end(), s.begin(), s.end());
      }
    }
  }

  void Remove(int u) {  // remove the nodes with only one child
    for (auto &&v : g_[u]) {
      int tv = v;
      while (g_[tv].size() == 1) {
        int t = tv;
        tv = g_[tv][0];
        Delete(t);
      }
      v = tv, Remove(v);
    }
  }

  void DfsAns(int u) {
    if (u >= 1 && u <= n_) {
      ans_.emplace_back(u);
      return;
    }
    for (auto &&v : g_[u]) DfsAns(v);
  }
} T;
```

## Zadatci

-   [CF243E Matrix](https://codeforces.com/problemset/problem/243/E)
-   [CF1552I Organizing a Music Festival](https://codeforces.com/contest/1552/problem/I)

## Literatura

-   Booth, Kellogg S. & Lueker, George S. (1976).["Testing for the consecutive ones property, interval graphs, and graph planarity using PQ-tree algorithms"](https://www.sciencedirect.com/science/article/pii/S0022000076800451?via%3Dihub).*[Journal of Computer and System Sciences](https://en.wikipedia.org/wiki/Journal_of_Computer_and_System_Sciences)*.**13**(3): 335–379.[doi](https://en.wikipedia.org/wiki/Doi_%28identifier%29):[10.1016/S0022-0000(76)80045-1](https://doi.org/10.1016%2FS0022-0000%2876%2980045-1).
-   [PQ Tree Algorithm and Consecutive Ones Problem](https://gregable.com/2008/11/pq-tree-algorithm.html)
-   [CF243E Matrix PQTree - RainAir's Blog](https://blog.aor.sd.cn/archives/1657/)
