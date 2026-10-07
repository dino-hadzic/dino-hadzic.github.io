---
title: Razdvajanje vrhova
---

Razdvajanje vrhova (vertex splitting) tehnika je modeliranja u teoriji grafova, često korištena u [mrežnim tokovima](./flow.md) za rješavanje problema s **težinama vrhova ili ograničenjima protoka kroz vrhove**, a često i u **slojevitim grafovima**.

## Maksimalni tok s ograničenjima protoka na vrhovima

Ako vrhove pretvorimo u bridove, problem se može riješiti standardnim predloškom.

Vrh s ograničenjem protoka pretvaramo u sljedeći oblik: dio koji se sastoji od dvaju vrhova $u,v$ i jednog brida $\left\langle u,v \right\rangle$. Vrh $u$ prima sve bridove koji u izvornom grafu iz drugih vrhova ulaze u taj vrh, a iz vrha $v$ izlaze svi bridovi koji u izvornom grafu iz tog vrha vode u druge vrhove. Ograničenje protoka brida $\left\langle u,v \right\rangle$ jednako je ograničenju protoka tog vrha u izvornom grafu; zatim se primijeni predložak i zadatak je riješen. To je osnovna ideja razdvajanja vrhova.

Ako izvorni graf izgleda ovako:

![](./images/node.svg)

graf nakon razdvajanja vrhova izgleda ovako:

![](./images/node-split.svg)

## Najkraći put u slojevitom grafu

Najkraći put u slojevitom grafu, npr.: $k$ puta smijemo besplatno proći jednim bridom; nađi najmanji ukupni trošak. Za takve zadatke možemo primijeniti ideju sličnu DP-u: neka $\text{dis}_{i, j}$ označava najkraći put od početnog vrha do vrha $i$ uz iskorištenih $j$ besplatnih prolazaka. Očito se niz $\text{dis}$ može računati ovako:

$\text{dis}_{i, j} = \min\{\min\{\text{dis}_{from, j - 1}\}, \min\{\text{dis}_{from,j} + w\}\}$

pri čemu $from$ označava prethodnik (roditelja) vrha $i$, a $w$ težinu brida kojim trenutno prolazimo. Kad je $j - 1 \geq k$, vrijedi $\text{dis}_{from, j}$=$\infty$.

Zapravo, ovaj DP odgovara razdvajanju svakog vrha na $k+1$ vrhova, pri čemu svaki novi vrh predstavlja vrh izvornog grafa u koji smo stigli nakon određenog broja besplatnih prolazaka. Drugim riječima, vrh $u_i$ predstavlja dolazak u vrh $u$ nakon $i$ iskorištenih besplatnih prolazaka.

??? note "[„JLOI2011” Zračne linije](https://www.luogu.com.cn/problem/P4568)"
    Zadatak: zadan je neusmjeren graf s $n$ vrhova i $m$ bridova; smiješ odabrati $k$ cesta i proći njima besplatno. Nađi najmanji trošak puta od $s$ do $t$.
    
    Ključni dio koda za referencu:
    
    ```cpp
    struct State {    // struktura čvora prioritetnog reda
      int v, w, cnt;  // cnt je broj dosad iskorištenih besplatnih prolazaka
    
      State() {}
    
      State(int v, int w, int cnt) : v(v), w(w), cnt(cnt) {}
    
      bool operator<(const State &rhs) const { return w > rhs.w; }
    };
    
    void dijkstra() {
      memset(dis, 0x3f, sizeof dis);
      dis[s][0] = 0;
      pq.push(State(s, 0, 0));  // za dolazak u početni vrh ne treba besplatni prolazak, udaljenost je nula
      while (!pq.empty()) {
        const State top = pq.top();
        pq.pop();
        int u = top.v, nowCnt = top.cnt;
        if (done[u][nowCnt]) continue;
        done[u][nowCnt] = true;
        for (int i = head[u]; i; i = edge[i].next) {
          int v = edge[i].v, w = edge[i].w;
          if (nowCnt < k && dis[v][nowCnt + 1] > dis[u][nowCnt]) {  // može se proći besplatno
            dis[v][nowCnt + 1] = dis[u][nowCnt];
            pq.push(State(v, dis[v][nowCnt + 1], nowCnt + 1));
          }
          if (dis[v][nowCnt] > dis[u][nowCnt] + w) {  // ne prolazi se besplatno
            dis[v][nowCnt] = dis[u][nowCnt] + w;
            pq.push(State(v, dis[v][nowCnt], nowCnt));
          }
        }
      }
    }
    
    int main() {
      n = read(), m = read(), k = read();
      // autor obično numerira vrhove od 1 do n, a u ovom su zadatku numerirani od 0 do n - 1, pa to treba uskladiti
      s = read() + 1, t = read() + 1;
      while (m--) {
        int u = read() + 1, v = read() + 1, w = read();
        add(u, v, w), add(v, u, w);  // u ovom su zadatku bridovi dvosmjerni
      }
      dijkstra();
      int ans = std::numeric_limits<int>::max();  // početna vrijednost ans je najveći int
      for (int i = 0; i <= k; ++i)
        ans = std::min(ans, dis[t][i]);  // uzmi najbolju od svih mogućnosti dolaska u odredište
      println(ans);
    }
    ```
