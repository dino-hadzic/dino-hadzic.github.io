---
title: AC automat
---

## Pregled

AC (Aho–Corasick) automat je automat izgrađen **na strukturi trieja** u kombinaciji s **idejom KMP-a**, a služi za rješavanje zadataka poput podudaranja više uzoraka (multi-pattern matching).

AC automat je u biti automat nad triejem.

Prije čitanja ovog članka pročitajte [KMP](./kmp.md) i [Trie](./trie.md).

## Objašnjenje

Jednostavno rečeno, izgradnja AC automata ima dva koraka:

1.  osnovna struktura trieja: od svih uzoraka izgradimo trie;
2.  ideja KMP-a: za sve čvorove trieja izgradimo fail pokazivače (pokazivače nepodudaranja).

Nakon izgradnje možemo ga koristiti za podudaranje više uzoraka.

## Izgradnja trieja

AC automat na početku umetne nekoliko uzoraka u trie, a zatim nad tim triejem izgradi AC automat. Taj je trie običan trie i gradi se uobičajenim postupkom izgradnje trieja.

Treba uočiti da čvor trieja predstavlja prefiks nekog uzorka. U nastavku ga zovemo i stanjem. Jedan čvor predstavlja jedno stanje, a bridovi trieja su prijelazi među stanjima.

Formalno, za uzorke $s_1,s_2,\cdots,s_n$ skup svih stanja nakon izgradnje trieja od njih označimo s $Q$.

## Fail pokazivači

AC automat koristi fail pokazivač kao pomoć pri podudaranju više uzoraka.

Fail pokazivač stanja $u$ pokazuje na drugo stanje $v$, gdje je $v\in Q$ i $v$ je najdulji sufiks od $u$ (tj. među svim stanjima koja su sufiksi uzimamo najdulje kao fail pokazivač).

Usporedba fail pokazivača s next pokazivačem iz [KMP-a](./kmp.md):

1.  Sličnost: oba su pokazivači na koje skačemo pri nepodudaranju.
2.  Razlika: next pokazivač daje najdulji border (tj. najdulji jednaki prefiks i sufiks), dok fail pokazivač pokazuje na najdulji sufiks trenutnog stanja među prefiksima svih uzoraka.

Naime, KMP podudara samo jedan uzorak, a AC automat podudara više uzoraka. Čvor na koji pokazuje fail pokazivač može pripadati drugom uzorku, čiji je prefiks različit.

Ukratko, fail pokazivač AC automata pokazuje na stanje koje je najdulji sufiks trenutnog stanja.

Napomena: pri podudaranju AC automata na istoj se poziciji može podudariti više uzoraka.

### Izgradnja pokazivača

Slijedi **osnovna ideja** izgradnje fail pokazivača:

Pri izgradnji fail pokazivača možemo se poslužiti idejom izgradnje next pokazivača iz KMP-a.

Promotrimo trenutni čvor $u$ u trieju; roditelj čvora $u$ je $p$, a $p$ bridom sa znakom $c$ pokazuje na $u$, tj. $\operatorname{trie}(p, c)=u$. Pretpostavimo da su fail pokazivači svih čvorova dubine manje od dubine $u$ već izračunati.

1.  Ako $\operatorname{trie}(\operatorname{fail}(p), c)$ postoji: fail pokazivač od $u$ postavimo na $\operatorname{trie}(\operatorname{fail}(p), c)$. To odgovara dodavanju znaka $c$ iza $p$ odnosno $\operatorname{fail}(p)$, čime dobivamo $u$ odnosno $\operatorname{fail}(u)$;
2.  ako $\operatorname{trie}(\operatorname{fail}(p), c)$ ne postoji: tražimo dalje $\operatorname{trie}(\operatorname{fail}(\operatorname{fail}(p)), c)$. Ponavljamo provjeru i skačemo po fail pokazivačima sve do korijena;
3.  ako i dalje ne postoji, fail pokazivač postavimo na korijen.

Time je izgradnja $\operatorname{fail}(u)$ dovršena.

### Primjer

Nekoliko GIF animacija u nastavku prikazuje izgradnju fail pokazivača za trie sastavljen od stringova $\mathtt{i}$, $\mathtt{he}$, $\mathtt{his}$, $\mathtt{she}$, $\mathtt{hers}$:

1.  Žuti čvor: trenutni čvor $u$.
2.  Zeleni čvorovi: čvorovi koje je BFS već obradio.
3.  Narančasti bridovi: fail pokazivači.
4.  Crveni brid: upravo izračunati fail pokazivač.

![AC\_automation\_gif\_b\_3.gif](./images/ac-automaton1.gif)

Posebno analizirajmo izgradnju fail pokazivača čvora $6$:

![AC\_automation\_6\_9.png](./images/ac-automaton1.png)

Nađemo roditelja čvora $6$, čvor $5$, i $\operatorname{fail}(5)=10$. No čvor $10$ nema izlazni brid sa slovom $\mathtt{s}$; skačemo dalje na fail pokazivač od $10$, $\operatorname{fail}(10)=0$. Čvor $0$ ima izlazni brid sa slovom $\mathtt{s}$ koji vodi u čvor $7$; stoga je $\operatorname{fail}(6)=7$.

Sljedeća slika prikazuje stanje nakon završetka izgradnje:

![finish](./images/ac-automaton4.png)

## Trie i trie-graf

Pogledajmo funkciju izgradnje `build`. Ona ima dva cilja: izgraditi fail pokazivače i izgraditi automat. Pripadne varijable definirane su ovako:

1.  `tr[u].son[c]`: može se shvatiti na dva načina. Možemo ga jednostavno shvatiti kao brid trieja, tj. $\operatorname{trie}(u, c)$; ili kao stanje (čvor) u koje dolazimo kad stanju (čvoru) $u$ dodamo znak $c$, tj. kao funkciju prijelaza $\operatorname{trans}(u, c)$. Radi jednostavnosti u nastavku koristimo drugo tumačenje.
2.  Red `q`: za BFS obilazak trieja.
3.  `tr[u].fail`: fail pokazivač čvora $u$.

???+ note "Implementacija"
    === "C++"
        ```cpp
        void build() {
          queue<int> q;
          for (int i = 0; i < 26; i++)
            if (tr[0].son[i]) q.push(tr[0].son[i]);
          while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int i = 0; i < 26; i++) {
              if (tr[u].son[i]) {
                tr[tr[u].son[i]].fail = tr[tr[u].fail].son[i];
                q.push(tr[u].son[i]);
              } else
                tr[u].son[i] = tr[tr[u].fail].son[i];
            }
          }
        }
        ```
    
    === "Python"
        ```python
        def build():
            for i in range(0, 26):
                if tr[0][i] != 0:
                    q.append(tr[0][i])
            while q:
                u = q.pop(0)
                for i in range(0, 26):
                    if tr[u][i] != 0:
                        fail[tr[u][i]] = tr[fail[u]][i]
                        q.append(tr[u][i])
                    else:
                        tr[u][i] = tr[fail[u]][i]
        ```

### Objašnjenje

Funkcija `build` stavlja čvorove u red u BFS poretku i redom računa fail pokazivače. Korijen trieja ovdje je $0$; u red stavljamo djecu korijena jedno po jedno. Kad bismo u red stavili korijen, pri prvom koraku BFS-a fail pokazivači djece korijena bili bi postavljeni na njih same. Zato u red stavljamo djecu korijena, a ne sam korijen.

Zatim počinje BFS: svaki put uzmemo čvor $u$ s početka reda ($\operatorname{fail}(u)$ već je izračunat u prethodnom tijeku BFS-a) i prolazimo kroz abecedu (ovdje $0 \sim 25$, što odgovara $\mathtt{a} \sim \mathtt{z}$, tj. kroz djecu čvora $u$):

1.  Ako $\operatorname{trans}(u, c)$ postoji, fail pokazivač od $\operatorname{trans}(u, c)$ postavimo na $\operatorname{trans}(\operatorname{fail}(u), c)$. Prema prethodnom opisu trebali bismo petljom `while` neprestano skakati po fail pokazivačima i provjeravati postoji li čvor za znak $c$, pa tek onda pridružiti vrijednost, ali ovdje je taj kôd pojednostavnjen posebnom obradom koju objašnjavamo u nastavku;
2.  inače $\operatorname{trans}(u, c)$ usmjerimo na stanje $\operatorname{trans}(\operatorname{fail}(u), c)$.

Postupak je ovdje taj da kôd u grani `else` mijenja strukturu trieja: nepostojeća stanja trieja povezuje s odgovarajućim stanjem fail pokazivača. U izvornom trieju svaki čvor predstavlja string $S$ koji je prefiks nekog uzorka. Nakon izmjene strukture trieja, iako je dodano mnogo prijelaza, stringovi koje čvorovi (stanja) predstavljaju ostaju nepromijenjeni.

A $\operatorname{trans}(S, c)$ odgovara dodavanju znaka $c$ iza $S$, čime nastaje drugo stanje $S'$. Ako $S'$ postoji, to znači da postoji uzorak čiji je prefiks $S'$; inače $\operatorname{trans}(S, c)$ usmjerimo na $\operatorname{trans}(\operatorname{fail}(S), c)$. Budući da je string koji odgovara $\operatorname{fail}(S)$ sufiks od $S$, string koji odgovara $\operatorname{trans}(\operatorname{fail}(S), c)$ također je sufiks od $S'$.

Drugim riječima, pri skakanju po trieju iz $S$ skačemo samo u $S'$, što odgovara podudaranju $S'$; a pri skakanju po AC automatu iz $S$ skačemo u sufiks od $S'$, tj. podudarimo znak $c$ i zatim odbacimo dio prefiksa od $S$. Odbacivanje prefiksa očito čuva podudaranje. Istodobno, ako se tekst podudara sa $S$, očito se podudara i sa sufiksom od $S$, pa i fail pokazivač jednako odbacuje prefiks. Takozvani fail pokazivač zapravo je skup sufiksa od $S$.

Polje djece `son` čvora trieja ima još jedno jednostavnije tumačenje: ako na poziciji $u$ dođe do nepodudaranja, skočit ćemo na poziciju $\operatorname{fail}(u)$. Uočimo da to može značiti više skokova po polju fail prije dolaska na sljedeću poziciju koja se podudara. Zato u `son` izravno zapisujemo sljedeću poziciju koja se podudara, čime jamčimo vremensku složenost programa.

Ova izmjena strukture trieja čini prijelaze podudaranja potpunijima. Ujedno sažima putove skokova po fail pokazivačima, pa ono što bi zahtijevalo mnogo skokova postaje jedan skok.

### Postupak

I ovdje nekoliko GIF animacija prikazuje postupak izgradnje:

![AC\_automation\_gif\_b\_pro3.gif](./images/ac-automaton2.gif)

1.  Plavi čvor: čvor $u$ do kojeg je BFS došao.
2.  Plavi bridovi: bridovi koje AC automat izmjenom strukture trieja dodaje iz trenutnog čvora.
3.  Crni bridovi: bridovi koje AC automat dodaje izmjenom strukture trieja.
4.  Crveni brid: fail pokazivač izračunat za trenutni čvor.
5.  Žuti bridovi: fail pokazivači.
6.  Sivi bridovi: bridovi trieja.

Vidimo da mnogi isprepleteni crni bridovi pretvaraju trie u **trie-graf**. Na slici su izostavljeni crni bridovi prema korijenu (inače bi bila još nepreglednija). Posebno analizirajmo situaciju pri obradi čvora $5$. Računamo fail pokazivač od $\operatorname{trans}(5, \mathtt{s})=6$:

![AC\_automation\_b\_7.png](./images/ac-automaton2.png)

Izvorna je strategija tražiti preko fail pokazivača: skočimo na $\operatorname{fail}(5)=10$, vidimo da nema brida trieja sa $\mathtt{s}$, skočimo na $\operatorname{fail}(10)=0$, nađemo $\operatorname{trie}(0, \mathtt{s})=7$, pa je $\operatorname{fail}(6)=7$; no s crnim i plavim bridovima nakon skoka na $\operatorname{fail}(5)=10$ izravno idemo preko $\operatorname{trans}(10, \mathtt{s})=7$ i stižemo u čvor $7$.

To su dvije stvari koje `build` obavlja: izgradnja fail pokazivača i izgradnja trie-grafa. Taj trie-graf ima ključnu ulogu i pri upitima.

## Podudaranje više uzoraka

Analizirajmo sada funkciju podudaranja `query`:

???+ note "Implementacija"
    === "C++"
        ```cpp
        int query(const char t[]) {
          int u = 0, res = 0;
          for (int i = 1; t[i]; i++) {
            u = tr[u].son[t[i] - 'a'];
            for (int j = u; j && tr[j].cnt != -1; j = tr[j].fail) {
              res += tr[j].cnt, tr[j].cnt = -1;
            }
          }
          return res;
        }
        ```
    
    === "Python"
        ```python
        def query(t: str) -> int:
            u, res = 0, 0
            for c in t:
                u = tr[u][c - ord("a")]
                j = u
                while j and e[j] != -1:
                    res += e[j]
                    e[j] = -1
                    j = fail[j]
            return res
        ```

### Objašnjenje

Ovdje je $u$ čvor trieja do kojeg je podudaranje trenutno došlo, a `res` je odgovor koji vraćamo. Petljom prolazimo kroz tekst, a $u$ u trieju prati trenutni znak. Pomoću fail pokazivača pronalazimo sve podudarene uzorke i pribrajamo ih odgovoru. Zatim broj pojavljivanja podudarenih uzoraka postavimo na nulu, da isti uzorak ne brojimo više puta. Gore smo analizirali da je struktura trieja zapravo funkcija trans; kad je ona izgrađena, pri podudaranju stringa odbacujemo dio prefiksa da bismo postigli minimalno podudaranje. Fail pokazivači pak pokazuju na dodatna podudarena stanja. Na kraju još jedna slika. Za upravo opisani automat:

![AC\_automation\_b\_13.png](./images/ac-automaton3.png)

Ako od korijena pokušamo podudariti $\mathtt{ushersheishis}$, $p$ će se mijenjati ovako:

![AC\_automation\_gif\_c.gif](./images/ac-automaton3.gif)

1.  Crveni čvor: čvor $p$.
2.  Ružičaste strelice: skokovi $p$ po automatu.
3.  Plavi bridovi: uspješno podudareni uzorci.
4.  Plavi čvorovi: čvorovi (stanja) pri skakanju po fail pokazivačima.

## Optimizacija učinkovitosti

Zadatak: vidi Luogu [P5357 [predložak] AC automat](https://www.luogu.com.cn/problem/P5357).

U našem AC automatu pri svakom podudaranju neprestano skačemo po fail bridovima da bismo pronašli sva podudaranja, no to je razmjerno sporo i u nekim zadacima premašuje vremensko ograničenje.

Kako to optimirati? Najprije treba uočiti jedno svojstvo fail pokazivača: ako u AC automatu zadržimo samo fail bridove, preostali je graf nužno stablo.

To je očito, jer fail pokazivači ne tvore ciklus i uvijek vode na manju dubinu; time je tvrdnja dokazana.

Tako se podudaranje AC automata svodi na problem zbrajanja po lancima u fail stablu, pa je dovoljno optimirati taj dio.

Dajemo dva pristupa.

### Optimizacija topološkim sortiranjem

Uočimo da se vrijeme uglavnom troši na skakanje po fail pokazivačima pri svakom koraku. Ako to možemo unaprijed zabilježiti i na kraju sve odjednom zbrojiti, učinkovitost se poboljšava.

Stoga po fail stablu napravimo jedno topološko sortiranje (stablo s bridovima prema korijenu) i odjednom izračunamo broj pojavljivanja svih uzoraka.

Funkcija `build` u odnosu na izvornu dodaje dio za brojanje ulaznih stupnjeva, kao pripremu za topološko sortiranje.

???+ note "Izgradnja"
    ```cpp
    void build() {
      queue<int> q;
      for (int i = 0; i < 26; i++)
        if (tr[0].son[i]) q.push(tr[0].son[i]);
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i = 0; i < 26; i++) {
          if (tr[u].son[i]) {
            tr[tr[u].son[i]].fail = tr[tr[u].fail].son[i];
            tr[tr[tr[u].fail].son[i]].du++;  // brojanje ulaznog stupnja
            q.push(tr[u].son[i]);
          } else
            tr[u].son[i] = tr[tr[u].fail].son[i];
        }
      }
    }
    ```

Zatim pri upitu samo označimo `ans` pronađenog čvora, a na kraju topološkim sortiranjem izračunamo odgovor.

???+ note "Upit"
    ```cpp
    void query(const char t[]) {
      int u = 0;
      for (int i = 1; t[i]; i++) {
        u = tr[u].son[t[i] - 'a'];
        tr[u].ans++;
      }
    }
    
    void topu() {
      queue<int> q;
      for (int i = 0; i <= tot; i++)
        if (tr[i].du == 0) q.push(i);
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        ans[tr[u].idx] = tr[u].ans;
        int v = tr[u].fail;
        tr[v].ans += tr[u].ans;
        if (!--tr[v].du) q.push(v);
      }
    }
    ```

Na kraju glavna funkcija:

???+ note "Glavna funkcija"
    ```cpp
    int main() {
      // do_something();
      AC::build();
      scanf("%s", s + 1);
      AC::query(s);
      AC::topu();
      for (int i = 1; i <= n; i++) printf("%d\n", AC::ans[idx[i]]);
      // do_another_thing();
    }
    ```

??? note "Zadatak-predložak [Luogu P5357 [predložak] AC automat](https://www.luogu.com.cn/problem/P5357), referentni kôd s optimizacijom topološkim sortiranjem"
    ```cpp
    --8<-- "docs/string/code/ac-automaton/ac-automaton_topu.cpp"
    ```

### Optimizacija DFS-om

Ideja je bliska topološkom sortiranju, samo što umjesto njega koristimo DFS. Obje su metode u biti iste: zbrajaju podstabla fail stabla.

Potpuni kôd nalazi se u predlošku 3 u sažetku.

## DP na AC automatu

Ovaj dio objašnjavamo na primjeru zadatka [P2292 \[HNOI2004\] Jezik L](https://www.luogu.com.cn/problem/P2292).

Lako se dosjetiti naivnog pristupa: izgradimo AC automat, na njemu izvodimo prijelaze preko podstringova svih fail pokazivača i na kraju uzmemo maksimum kao odgovor.

Glavni dio koda slijedi. Ako vam definicije tipova u kodu nisu poznate, pogledajte najprije potpuni kôd na kraju:

???+ note "Glavni dio koda upita"
    ```cpp
    int query(const char t[]) {
      int u = 0, len = strlen(t + 1);
      for (int i = 1; i <= len; i++) dp[i] = 0;
      for (int i = 1; i <= len; i++) {
        u = tr[u].son[t[i] - 'a'];
        for (int j = u; j; j = tr[j].fail) {
          if (tr[j].idx && (dp[i - tr[j].depth] || i - tr[j].depth == 0)) {
            dp[i] = dp[i - tr[j].depth] + tr[j].depth;
          }
        }
      }
      int ans = 0;
      for (int i = 1; i <= len; i++) ans = std::max(ans, dp[i]);
      return ans;
    }
    ```

No složenost ovog pristupa nije linearna (jer za svaki čvor skačemo po fail pokazivačima), pa na drugom podzadatku premašuje vremensko ograničenje; stoga ga moramo optimirati.

Pogledajmo posebna svojstva zadatka: uočavamo da su sve riječi duljine najviše $20$, pa se nameće optimizacija bitmaskom (state compression).

Vidimo da je trenutno usko grlo skakanje po fail pokazivačima; ako taj korak optimiramo na $O(1)$, cijeli se problem rješava u strogo linearnom vremenu.

Među prvih $20$ slova možemo zapisati moguće duljine podstringova, komprimirati ih u stanje i pohraniti u svaki čvor-dijete.

Tada u `build` možemo pisati ovako:

???+ note "Izgradnja fail pokazivača"
    ```cpp
    void build() {
      queue<int> q;
      for (int i = 0; i < 26; i++)
        if (tr[0].son[i]) {
          q.push(tr[0].son[i]);
          tr[tr[0].son[i]].depth = 1;
        }
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        int v = tr[u].fail;
        // ovdje se ažurira stanje
        tr[u].stat = tr[v].stat;
        if (tr[u].idx) tr[u].stat |= 1 << tr[u].depth;
        for (int i = 0; i < 26; i++) {
          if (tr[u].son[i]) {
            tr[tr[u].son[i]].fail = tr[tr[u].fail].son[i];
            tr[tr[u].son[i]].depth = tr[u].depth + 1;  // bilježimo dubinu
            q.push(tr[u].son[i]);
          } else
            tr[u].son[i] = tr[tr[u].fail].son[i];
        }
      }
    }
    ```

Zatim pri upitu možemo ukloniti petlju skakanja po fail pokazivačima i pojednostavniti kôd ovako:

???+ note "Upit"
    ```cpp
    int query(const char t[]) {
      int u = 0, mx = 0;
      unsigned st = 1;
      for (int i = 1; t[i]; i++) {
        u = tr[u].son[t[i] - 'a'];
        st <<= 1;  // pomak za jedno mjesto: duljina svakog bita raste za 1
        if (tr[u].stat & st) st |= 1, mx = i;
      }
      return mx;
    }
    ```

Naš `tr[u].stat` održava skup duljina na cijelom fail lancu počevši od čvora $u$ (budući da su duljine manje od $32$, to ne smeta), a `st` održava skup duljina posljednjih $32$ pozicije teksta upita do trenutnog mjesta (zbog prirodnog prelijevanja komprimiranog stanja).

Ako rezultat operacije `&` nije $0$, presjek dvaju skupova duljina nije prazan i pronašli smo podudaranje.

??? note "[P2292 \[HNOI2004\] Jezik L](https://www.luogu.com.cn/problem/P2292), potpuni kôd"
    ```cpp
    --8<-- "docs/string/code/ac-automaton/ac_automaton_luoguP2292.cpp"
    ```

## Sažetak

Vremenska složenost: neka je $|s_i|$ duljina uzorka, $|S|$ duljina teksta, a $|\Sigma|$ veličina abecede (konstanta, obično $26$). Ako gradimo trie-graf, vremenska je složenost $O(\sum|s_i|+n|\Sigma|+|S|)$, gdje je $n$ broj čvorova AC automata, koji može doseći $O(\sum|s_i|)$. Ako ne gradimo trie-graf i pri izgradnji fail pokazivača izbjegavamo obilazak prazne djece, vremenska je složenost $O(\sum|s_i|+|S|)$.

??? note "Zadatak-predložak [Luogu P3808 AC automat (jednostavna verzija)](https://www.luogu.com.cn/problem/P3808), referentni kôd"
    ```cpp
    --8<-- "docs/string/code/ac-automaton/ac-automaton_1.cpp"
    ```

??? note "Zadatak-predložak [Luogu P3796 AC automat (jednostavna verzija II)](https://www.luogu.com.cn/problem/P3796), referentni kôd"
    ```cpp
    --8<-- "docs/string/code/ac-automaton/ac-automaton_2.cpp"
    ```

??? note "Zadatak-predložak [Luogu P5357 [predložak] AC automat](https://www.luogu.com.cn/problem/P5357), referentni kôd s optimizacijom DFS-om"
    ```cpp
    --8<-- "docs/string/code/ac-automaton/ac-automaton_3.cpp"
    ```
