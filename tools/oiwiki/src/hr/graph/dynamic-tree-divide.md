---
title: Dinamička centroidna dekompozicija
---

## Dinamička centroidna dekompozicija

Dinamička centroidna dekompozicija služi za probleme prebrojavanja informacija o putovima u stablu **s izmjenama težina vrhova ili bridova**.

### Centroidno stablo

Prisjetimo se postupka centroidne dekompozicije.

Za vrh $x$, jednostavni putovi u njegovu podstablu dvije su vrste: oni koji prolaze kroz vrh $x$ i sastoje se od jednog ili dva puta koji kreću iz $x$, te oni koji ne prolaze kroz $x$, tj. već su sadržani u podstablima njegove djece.

Za računanje jednostavnih putova u podstablu odaberemo središte dekompozicije $rt$, izračunamo informacije o putovima u podstablu koji prolaze kroz taj vrh, a zatim za svako njegovo dijete komponentu u kojoj se to dijete nalazi nakon uklanjanja $rt$ promatramo kao podstablo i računamo rekurzivno. Odabrana središta dekompozicije tvore stablastu strukturu koja se naziva **centroidno stablo**. Uočimo da je zbroj veličina komponenata koje predstavljaju vrhovi iste razine centroidnog stabla (tj. komponenata kojima je taj vrh središte dekompozicije) $O(n)$. To znači da vremenska složenost centroidne dekompozicije ovisi o dubini centroidnog stabla: ako je dubina centroidnog stabla $h$, složenost je $O(nh)$.

Može se dokazati da je dubina centroidnog stabla najmanja, $O(\log n)$, kad svaki put kao središte dekompozicije odaberemo centroid komponente. Tako u vremenu $O(n\log n)$ možemo prebrojiti informacije o $O(n^2)$ putova u stablu.

Budući da se oblik stabla tijekom dinamičke centroidne dekompozicije ne mijenja, ne mijenja se ni oblik centroidnog stabla.

Slijedi referentni kod za izgradnju centroidnog stabla:

```cpp
void calcsiz(int x, int f) {
  siz[x] = 1;
  maxx[x] = 0;
  for (int j = h[x]; j; j = nxt[j])
    if (p[j] != f && !vis[p[j]]) {
      calcsiz(p[j], x);
      siz[x] += siz[p[j]];
      maxx[x] = max(maxx[x], siz[p[j]]);
    }
  maxx[x] =
      max(maxx[x], sum - siz[x]);  // maxx[x] je veličina najvećeg podstabla kad je x korijen
  if (maxx[x] < maxx[rt])
    rt = x;  // ovdje ne smije biti <=, da se rt ne promijeni pri drugom pozivu calcsiz
}

void pre(int x) {
  vis[x] = true;  // vrh x se u nastavku više ne razmatra
  for (int j = h[x]; j; j = nxt[j])
    if (!vis[p[j]]) {
      sum = siz[p[j]];
      rt = 0;
      maxx[rt] = inf;
      calcsiz(p[j], -1);
      calcsiz(rt, -1);  // računa se dvaput; drugi put dobivamo veličine podstabala s korijenom rt
      fa[rt] = x;
      pre(rt);  // zapamti roditelja u centroidnom stablu
    }
}

int main() {
  sum = n;
  rt = 0;
  maxx[rt] = inf;
  calcsiz(1, -1);
  calcsiz(rt, -1);
  pre(rt);
}
```

### Izvođenje izmjena

Pri upitima i izmjenama u centroidnom stablu jednostavno skačemo po roditeljima i ažuriramo. Budući da je dubina centroidnog stabla najviše $O(\log n)$, složenost je zajamčena.

Tijekom dinamičke centroidne dekompozicije trebaju nam udaljenosti vrha do njegovih predaka u centroidnom stablu i slične informacije. Budući da vrh ima najviše $O(\log n)$ predaka, pri izgradnji centroidnog stabla možemo dodatno računati dubinu $dep[x]$ ili koristiti LCA, pa te udaljenosti unaprijed izračunati ili ih računati na zahtjev. **Pozor**: udaljenosti vrha do njegovih predaka u centroidnom stablu nisu nužno rastuće i ne smiju se zbrajati!

U dinamičkoj centroidnoj dekompoziciji informacija o vrhu može se u njegovim precima u centroidnom stablu brojati više puta, pa učinak tih ponavljanja treba poništiti. Uobičajeno je za svaku komponentu čuvati dvije vrste zapisa: udaljenosti do središta dekompozicije i udaljenosti do roditelja tog središta u centroidnom stablu. To je prikazano u primjerima.

??? note "Primjer [„ZJOI2007” 捉迷藏](https://www.luogu.com.cn/problem/P2056)"
    Zadano je stablo s $n$ vrhova; početno su svi vrhovi crni. Treba podržati dvije operacije:
    
    1.  promijeni boju vrha (bijela u crnu, crna u bijelu);
    2.  ispiši udaljenost dvaju najudaljenijih crnih vrhova u stablu.
    
        $n\le 10^5,m\le 5\times 10^5$

Izgradimo centroidno stablo i za svaki vrh $x$ čuvajmo dva **heapa s brisanjem**. $dist[x]$ čuva udaljenosti do $x$ svih crnih vrhova komponente koju predstavlja $x$; $ch[x]$ čuva udaljenosti do $x$ crnih vrhova iz sve djece vrha $x$ u centroidnom stablu i iz njega samog. Zbog pohlepnog načina računanja odgovora u ovom zadatku, i zato što dva puta iz istog podstabla ne mogu činiti jedan cijeli put, u taj heap ubacujemo samo vrijednost samog vrha i najveću vrijednost iz svakog podstabla. Uočimo da je zbroj dviju najvećih vrijednosti u $ch[x]$ (ili svih vrijednosti ako ih nema dvije) duljina najduljeg puta s crnim krajevima koji prolazi kroz $x$ kad je $x$ središte dekompozicije. Odgovore svih vrhova čuvamo u heapu s brisanjem $ans$; najveća vrijednost u tom heapu traženi je odgovor.

Prema gornjim definicijama održavamo heapove s brisanjem $dist[x],ch[x],ans$. Kad se vrijednost u $dist[x]$ promijeni, $ch[x]$ i $ans$ također možemo ažurirati u $O(\log n)$.

Pogledajmo sada kako se $dist[x]$ mijenja kad promijenimo boju vrha. Ako je vrh bio crn, izvodimo brisanje; ako je bio bijel, izvodimo umetanje.

Recimo da mijenjamo boju vrha $x$. Za svakog njegova pretka $u$ u $dist[u]$ umetnemo ili izbrišemo $dist(x,u)$ i istodobno ažuriramo $ch[x]$ i $ans$. Posebno, u $ch[x]$ umetnemo ili izbrišemo vrijednost $0$.

Referentni kod:

```cpp
--8<-- "docs/graph/code/dynamic-tree-divide/dynamic-tree-divide_1.cpp"
```

???+ note "Primjer [Luogu P6329【模板】点分树 | 震波](https://www.luogu.com.cn/problem/P6329)"
    Zadano je stablo s $n$ vrhova; svaki vrh $x$ ima težinu $v[x]$. Treba podržati dvije operacije:
    
    1.  upit: zbroj težina vrhova udaljenih od $x$ najviše $y$;
    2.  izmjena: postavi težinu vrha $x$ na $y$, tj. $v[x]=y$.

Informacije o udaljenostima čuvamo u dinamički alociranom segment treeu po vrijednostima.

Slično kao u prethodnom zadatku, za svaki vrh održavamo segment tree $dist[x]$ koji čuva udaljenosti svih vrhova komponente $x$ do vrha $x$: indeks je udaljenost, a vrijednost se uvećava za težinu vrha. Segment tree $ch[x]$ čuva udaljenosti svih vrhova komponente $x$ do roditelja vrha $x$ u centroidnom stablu.

U ovom zadatku sve upite i izmjene treba provesti nad svim precima u centroidnom stablu.

Uzmimo upit za primjer. Tražimo zbroj težina vrhova udaljenih od $x$ najviše $y$. Najprije odgovoru dodamo zbroj vrijednosti u $dist[x]$ s indeksima od $0$ do $y$. Zatim prolazimo po svim precima $u$ vrha $x$; neka je $v$ predak jednu razinu niže od $u$ i neka je $d=dist(x,u)$. Ako ne ulazimo u podstablo koje sadrži $x$, tj. podstablo s korijenom $v$, odgovoru dodamo zbroj vrijednosti u $dist[u]$ s indeksima od $0$ do $y-d$. Budući da smo dio s korijenom $v$ izbrojili dvaput, od odgovora oduzmemo zbroj vrijednosti u $ch[v]$ s indeksima od $0$ do $y-d$.

Pri izmjeni istodobno ažuriramo $dist[x]$ i $ch[x]$.

Referentni kod:

```cpp
--8<-- "docs/graph/code/dynamic-tree-divide/dynamic-tree-divide_2.cpp"
```
