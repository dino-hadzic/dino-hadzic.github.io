---
title: Najniži zajednički predak (LCA)
---

## Definicija

Najniži zajednički predak skraćeno se zove LCA (Lowest Common Ancestor). Najniži zajednički predak dvaju čvorova jest onaj među njihovim zajedničkim precima koji je najudaljeniji od korijena.
Radi jednostavnosti, najniži zajednički predak skupa čvorova $S=\{v_1,v_2,\ldots,v_n\}$ označavamo $\text{LCA}(v_1,v_2,\ldots,v_n)$ ili $\text{LCA}(S)$.

## Svojstva

> Sadržaj odjeljka **Svojstva** preveden je, uz izmjene, s [wcipeg](http://wcipeg.com/wiki/Lowest_common_ancestor).

1.  $\text{LCA}(\{u\})=u$;
2.  $u$ je predak od $v$ ako i samo ako je $\text{LCA}(u,v)=u$;
3.  ako $u$ nije predak od $v$ i $v$ nije predak od $u$, onda se $u$ i $v$ nalaze u dvama različitim podstablima čvora $\text{LCA}(u,v)$;
4.  u preorder obilasku $\text{LCA}(S)$ pojavljuje se prije svih elemenata od $S$, a u postorder obilasku $\text{LCA}(S)$ pojavljuje se nakon svih elemenata od $S$;
5.  najniži zajednički predak unije dvaju skupova čvorova jest najniži zajednički predak njihovih najnižih zajedničkih predaka, tj. $\text{LCA}(A\cup B)=\text{LCA}(\text{LCA}(A), \text{LCA}(B))$;
6.  najniži zajednički predak dvaju čvorova nužno leži na najkraćem putu između njih u stablu;
7.  $d(u,v)=h(u)+h(v)-2h(\text{LCA}(u,v))$, gdje je $d$ udaljenost dvaju čvorova u stablu, a $h$ udaljenost čvora od korijena.

## Postupci

### Naivni algoritam

#### Postupak

U svakom koraku možemo uzeti dublji od dvaju čvorova i pomaknuti ga prema gore. Očito se u stablu ta dva čvora na kraju moraju sresti, a mjesto susreta traženi je LCA.
Ili najprije dublji čvor pomičemo prema gore dok im dubine ne budu jednake, a zatim oba zajedno pomičemo prema gore; i tako se na kraju sigurno sretnu.

#### Svojstva

Naivni algoritam u predobradi treba dfs cijelog stabla, vremenske složenosti $O(n)$, a jedan upit ima vremensku složenost $\Theta(n)$. Ako je stablo slučajno, vremenska složenost ovisi o očekivanoj visini takvog slučajnog stabla.

### Binary lifting

#### Postupak

Binary lifting najklasičniji je način računanja LCA i poboljšanje je naivnog algoritma. Predobradom polja $\text{fa}_{x,i}$ pokazivač se može brzo pomicati, što znatno smanjuje broj skokova. $\text{fa}_{x,i}$ označava $2^i$-tog pretka čvora $x$. Polje $\text{fa}_{x,i}$ može se predobradom izračunati dfs-om.

Pogledajmo sada kako optimizirati skokove:
U prvoj fazi pomicanja pokazivača čvorove $u,v$ treba dovesti na istu dubinu. Možemo izračunati razliku dubina čvorova $u,v$, označimo je $y$. Binarnim rastavom $y$ pretvaramo $y$ skokova u „broj jedinica u binarnom zapisu od $y$” skokova.
U drugoj fazi krećemo od najvećeg $i$ i pokušavamo redom sve do $0$ (uključivo): ako je $\text{fa}_{u,i}\not=\text{fa}_{v,i}$, onda $u\gets\text{fa}_{u,i},v\gets\text{fa}_{v,i}$; konačni LCA tada je $\text{fa}_{u,0}$.

#### Svojstva

Predobrada binary liftinga ima vremensku složenost $O(n \log n)$, a jedan upit $O(\log n)$.
Osim toga, u binary liftingu možemo zamijeniti dvije dimenzije polja `fa` tako da manja dimenzija bude prva. To smanjuje broj promašaja predmemorije (cache miss) i povećava učinkovitost programa.

??? note "Primjer zadatka"
    [HDU 2586 How far away?](https://acm.hdu.edu.cn/showproblem.php?pid=2586) Upiti najkraćeg puta u stablu.

Možemo najprije izračunati LCA pa odgovoriti pomoću svojstva $7$. Rezultat se može izračunati i izravno tijekom računanja LCA.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/lca/lca_1.cpp"
    ```

### Tarjanov algoritam

#### Postupak

Tarjanov algoritam je **offline algoritam** koji [union-find strukturom](../ds/dsu.md) bilježi pretka pojedinog čvora. Postupak je sljedeći:

1.  Najprije učitamo bridove (lista susjedstva) i upite (pohranjene u drugoj listi susjedstva). Upiti su zapravo virtualno dodani bridovi; radi jednostavnosti, pri učitavanju svakog upita dodajemo i taj brid i njemu suprotan u polje `queryEdge`.
2.  Zatim napravimo jedan DFS obilazak, pri čemu poljem `visited` bilježimo je li čvor posjećen, a poljem `parent` roditelja trenutačnog čvora.
3.  Pritom se koristi **ideja povratka (backtracking)**: kad dođemo do nekog čvora, smatramo da je korijen tog čvora on sam. Tek nakon što DFS s korijenom u tom čvoru u potpunosti završi, korijen tog čvora postavljamo na njegova roditelja.
4.  Pri povratku, ako je za upit iz `queryEdge` s početkom u tom čvoru drugi čvor upita već posjećen, izravno ažuriramo rezultat LCA tog upita.
5.  Na kraju ispišemo rezultate.

#### Svojstva

Tarjanov algoritam mora inicijalizirati union-find, pa predobrada ima vremensku složenost $O(n)$.

Naivni Tarjanov algoritam obrađuje svih $m$ upita u vremenu $O(m \alpha(m+n, n) + n)$, ali ima veću konstantu od binary liftinga. Postoji i implementacija složenosti $O(m + n)$.

???+ warning "Napomena"
    Nije točna tvrdnja da „union-find korišten u naivnom Tarjanovu LCA algoritmu ima posebna svojstva zbog kojih jedan poziv funkcije `find()` ima amortiziranu složenost $O(1)$”.
    
    Složenost naivne Tarjanove implementacije u nastavku je $O(m \alpha(m+n, n) + n)$. Ako želite strogo linearnu složenost, pogledajte [rad Gabowa i Tarjana iz 1983.](https://dl.acm.org/doi/pdf/10.1145/800061.808753), u kojem je dan postupak složenosti $O(m + n)$.

#### Implementacija

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/lca/lca_tarjan.cpp"
    ```

### Svođenje na RMQ pomoću Eulerova obilaska

#### Definicija

Napravimo DFS stabla i svaki put kad dođemo u neki čvor, bilo pri prvom posjetu bilo pri povratku, zabilježimo njegov indeks; dobivamo niz duljine $2n-1$ koji se zove Eulerov obilazak (Euler tour) tog stabla.

U nastavku položaj prvog pojavljivanja čvora $u$ u Eulerovu obilasku označavamo $pos(u)$ (naziva se i Eulerov indeks čvora $u$), a sam Eulerov obilazak označavamo $E[1..2n-1]$.

#### Postupak

S Eulerovim obilaskom problem LCA može se u linearnom vremenu svesti na problem RMQ, tj. $pos(LCA(u, v))=\min\{pos(k)|k\in E[pos(u)..pos(v)]\}$.

Tu jednakost nije teško razumjeti: na putu od $u$ do $v$ sigurno prolazimo kroz $LCA(u,v)$, ali ne i kroz pretke od $LCA(u,v)$. Stoga je čvor s najmanjim Eulerovim indeksom kroz koji prolazimo na putu od $u$ do $v$ upravo $LCA(u, v)$.

Računanje Eulerova obilaska DFS-om ima vremensku složenost $O(n)$, a i duljina Eulerova obilaska je $O(n)$, pa se problem LCA u vremenu $O(n)$ svodi na problem RMQ iste veličine.

#### Implementacija

???+ note "Primjer koda"
    ```cpp
    int dfn[N << 1], pos[N], tot, st[30][(N << 1) + 2],
        rev[30][(N << 1) + 2];  // rev je indeks čvora koji odgovara najmanjoj dubini
    
    void dfs(int cur, int dep) {
      dfn[++tot] = cur;
      depth[tot] = dep;
      pos[cur] = tot;
      for (int i = head[t]; i; i = side[i].next) {
        int v = side[i].to;
        if (!pos[v]) {
          dfs(v, dep + 1);
          dfn[++tot] = cur, depth[tot] = dep;
        }
      }
    }
    
    void init() {
      for (int i = 2; i <= tot + 1; ++i)
        lg[i] = lg[i >> 1] + 1;  // predobrada lg umjesto bibliotečne funkcije log2 radi manje konstante
      for (int i = 1; i <= tot; i++) st[0][i] = depth[i], rev[0][i] = dfn[i];
      for (int i = 1; i <= lg[tot]; i++)
        for (int j = 1; j + (1 << i) - 1 <= tot; j++)
          if (st[i - 1][j] < st[i - 1][j + (1 << i - 1)])
            st[i][j] = st[i - 1][j], rev[i][j] = rev[i - 1][j];
          else
            st[i][j] = st[i - 1][j + (1 << i - 1)],
            rev[i][j] = rev[i - 1][j + (1 << i - 1)];
    }
    
    int query(int l, int r) {
      int k = lg[r - l + 1];
      return st[k][l] < st[k][r + 1 - (1 << k)] ? rev[k][l]
                                                : rev[k][r + 1 - (1 << k)];
    }
    ```

Kad trebamo LCA para $(u, v)$, dovoljno je upitati čvor koji odgovara minimumu na intervalu $[\min\{pos[u], pos[v]\}, \max\{pos[u], pos[v]\}]$.

Ako RMQ rješavamo sparse tableom, algoritam ne podržava online izmjene, predobrada ima vremensku složenost $O(n\log n)$, a svaki upit LCA $O(1)$.

### Svođenje na RMQ pomoću DFS poretka

Eulerov obilazak ima duljinu $2n-1$, pa su vremenska i prostorna konstanta nešto veće. Zapravo LCA možemo računati izravno pomoću DFS vremenskih oznaka $\operatorname{dfn}$.

Promotrimo LCA para $(u,v)$ i označimo $d=\operatorname{LCA}(u,v)$. Ako je $u=v$, onda je $d=u$ i to treba posebno obraditi. Inače bez smanjenja općenitosti neka je $\operatorname{dfn}(u) < \operatorname{dfn}(v)$; tada $v$ sigurno nije predak od $u$. Za razliku od Eulerova obilaska, u DFS poretku se $d$ ne pojavljuje u intervalu $(\operatorname{dfn}(u), \operatorname{dfn}(v)]$. No taj interval sigurno sadrži ono dijete čvora $d$ koje leži na putu od $d$ do $v$. To vrijedi bez obzira na to je li $u$ predak od $v$. Stoga, čim pronađemo čvor najmanje dubine (ne nužno jedinstven) u intervalu $[\operatorname{dfn}(u) + 1, \operatorname{dfn}(v)]$, njegov roditelj sigurno je LCA. Interval počinje od $\operatorname{dfn}(u) + 1$ zato što bi, ako je $u$ predak od $v$ i interval sadrži $u$, čvor najmanje dubine bio sam $u$, a njegov roditelj nije LCA.

Time računanje LCA ponovno postaje problem RMQ.

Ako ne želimo pohranjivati dodatne podatke o dubini i roditelju, možemo u DFS poretku na položaj $\operatorname{dfn}(u)$ izravno pohraniti $\operatorname{fa}(u)$. Zatim u tom nizu uspoređujemo vrijednosti prema vremenskim oznakama. Tada je element tog niza s najmanjom vremenskom oznakom u intervalu $[\operatorname{dfn}(u) + 1, \operatorname{dfn}(v)]$ upravo $\operatorname{LCA}(u,v)$. Naime, čvorovi u intervalu $[\operatorname{dfn}(u) + 1, \operatorname{dfn}(v)]$ sigurno su pravi potomci od $d$, pa DFS vremenske oznake njihovih roditelja nisu manje od $\operatorname{dfn}(d)$; a u intervalu se kod djeteta od $d$ postiže upravo minimum $\operatorname{dfn}(d)$, pri čemu takvo dijete prema prethodnoj raspravi sigurno postoji.

Svođenje LCA na RMQ pomoću DFS poretka je $O(n)$, a ukupna složenost ovisi o korištenoj RMQ metodi. Primjer implementacije sa sparse tableom, predobradom $O(n\log n)$ i upitom $O(1)$:

??? example "Primjer implementacije"
    ```cpp
    --8<-- "docs/graph/code/lca/lca-dfs.cpp:lca"
    ```

### Heavy-light dekompozicija

LCA je čvor na koji pokazuje pliće od dvaju pokazivača u trenutku kad oba skoče na isti teški lanac.

Predobrada heavy-light dekompozicije ima vremensku složenost $O(n)$, jedan upit $O(\log n)$, a konstanta je mala.

### Link Cut Tree

U [Link Cut Treeu](../ds/lct.md), ako su čvorovi dviju uzastopnih operacija [access](../ds/lct.md#access) redom `u` i `v`, onda je čvor koji vraća druga operacija [access](../ds/lct.md#access) upravo LCA čvorova `u` i `v`.

Bez operacija link i cut, jedan upit Link Cut Treeom ima vremensku složenost $O(\log n)$.

### Standardni RMQ

Ranije je opisano svođenje LCA na RMQ pomoću Eulerova obilaska; usko grlo je RMQ. Ako RMQ možemo riješiti u $O(n) \sim O(1)$, onda i LCA možemo riješiti u $O(n) \sim O(1)$.

Uočimo da se u Eulerovu obilasku susjedni elementi razlikuju za 1 ili -1, pa možemo primijeniti [±1 RMQ](../topic/rmq.md#加减-1rmq) složenosti $O(n) \sim O(1)$.

Vremenska složenost $O(n) \sim O(1)$, prostorna $O(n)$, podržava online upite, konstanta je velika.

#### Primjer zadatka [Luogu P3379【模板】Najniži zajednički predak (LCA)](https://www.luogu.com.cn/problem/P3379)

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/lca/lca_2.cpp"
    ```

## Zadaci za vježbu

-   [Upiti predak–potomak](https://loj.ac/problem/10135)
-   [Prijevoz kamionima](https://loj.ac/problem/2610)
-   [Udaljenost čvorova](https://loj.ac/problem/10130)

## Literatura

-   [Malo poznata tehnika – LCA pomoću DFS poretka, Alex\_Wei – Luogu](https://www.luogu.com.cn/article/pu52m9ue)
