---
title: Maksimalni tok
---

Ova stranica uglavnom opisuje algoritme vezane uz problem maksimalnog toka.

## Pregled

Za osnovne pojmove o tokovima vidi [Uvod u tokove u mrežama](../flow.md).

Neka je $G=(V,E)$ mreža s izvorom i ponorom; želimo na $G$ odrediti prikladan tok $f$ koji maksimizira ukupni tok mreže $|f|$ (tj. $\sum_{x \in V} f(s, x) - \sum_{x \in V} f(x, s)$). Taj se problem zove problem maksimalnog toka (maximum flow problem).

## Ford–Fulkersonovo povećanje

Ford–Fulkersonovo povećanje zajednički je naziv za klasu algoritama za računanje maksimalnog toka. Metoda koristi greedy ideju: traženjem povećavajućih putova ažurira tok i izračunava maksimalni tok.

### Pregled

Za mrežu $G$ i tok $f$ na $G$ definiramo sljedeće.

Za brid $(u, v)$ razliku kapaciteta i toka zovemo rezidualni kapacitet $c_f(u,v)$ (residual capacity), tj. $c_f(u,v)=c(u,v)-f(u,v)$.

Podgraf grafa $G$ koji čine svi vrhovi i bridovi s rezidualnim kapacitetom većim od $0$ zovemo rezidualna mreža $G_f$ (residual network), tj. $G_f=(V,E_f)$, gdje je $E_f=\left\{(u,v) \mid c_f(u,v)>0\right\}$.

???+ warning "Upozorenje"
    Kao što ćemo odmah spomenuti, tok može biti negativan, pa bridovi iz $E_f$ ne moraju biti u $E$. Nakon uvođenja pojma povećanja to ćemo u nastavku konkretno objasniti.

Put od izvora $s$ do ponora $t$ u $G_f$ zovemo povećavajući put (augmenting path). Za povećavajući put svakom bridu $(u, v)$ dodamo jednaku količinu toka kako bi se ukupni tok mreže povećao; taj postupak zovemo povećanje (augment). Stoga se računanje maksimalnog toka može promatrati kao superpozicija tokova dobivenih u nizu povećanja.

Osim toga, tijekom Ford–Fulkersonova povećanja za svaki brid $(u, v)$ stvaramo i obrnuti brid $(v, u)$. Dogovorno vrijedi $f(u, v) = -f(v, u)$; to se svojstvo osigurava uvođenjem operacije poništavanja toka pri svakom povećanju, tj. kad $f(u, v)$ raste, $f(v, u)$ treba pasti za isti iznos.

???+ tip "Savjet"
    U implementacijama algoritama za maksimalni tok često trebamo brz pristup obrnutom bridu. U matrici susjedstva ta je operacija trivijalna ($g_{u, v} \leftrightarrow g_{v, u}$). No uobičajena implementacija je bolja lista susjedstva s lančanim bridovima (chained forward star). Česta je tehnika da bridove numeriramo od parnog broja (obično $0$) i pri dodavanju brida odmah dodamo i njegov obrnuti brid tako da su im indeksi susjedni. Tako brid s indeksom $i$ i brid s indeksom $i \oplus 1$ uvijek ostaju međusobno obrnuti.

Čitatelji koji se prvi put susreću s ovom metodom mogu primijetiti protuintuitivnu situaciju: tok obrnutog brida $f(v, u)$ može biti negativan. Zapravo, tijekom Ford–Fulkersonova povećanja važan je samo rezidualni kapacitet $c_f$, a apsolutna vrijednost $f(v, u)$ nije bitna; smanjenje toka obrnutog brida možemo gledati kao povećanje rezidualnog kapaciteta obrnutog brida $c_f(v, u)$, što se slaže sa smislom poništavanja toka: povećanje rezidualnog kapaciteta obrnutog brida znači da kasnije prolaskom obrnutim bridom možemo poništiti ranije povećanje u smjeru naprijed, što predstavlja svojevrsno „kajanje”.

Sljedeći primjer može pomoći u razumijevanju postupka. Neka je $G$ mreža s jediničnim kapacitetima; promotrimo sljedeći postupak:

-   Na $G$ postoji više povećavajućih putova; odaberemo povećanje koje redom prolazi kroz $u, v$ (kao na lijevoj slici) i tok se poveća za $1$.
-   Primjećujemo da bi, kad bismo izveli povećanje sa srednje slike, lokalni maksimalni tok bio $2$, a ne $1$. No kako su brid koji ulazi u $u$ i brid koji izlazi iz $v$ u prvom povećanju iscrpili kapacitet, povećanje sa srednje slike sad ne možemo izvesti. To znači da trenutni tok nije dovoljno dobar, ali lokalno možda više nema drugih povećavajućih putova (koji prolaze samo bridovima izvornog grafa, bez obrnutih bridova).
-   Sada uvedimo poništavanje toka. Nakon prvog povećanja poništavanje znači da se $c_f(v, u)$ povećao za $1$ rezidualnog kapaciteta, što je kao da je dodan brid $(v, u)$, pa možemo izvesti još jedno povećanje koje redom prolazi kroz $p, v, u, q$ (narančasti put na desnoj slici). Tok na neusmjerenom bridu $(u, v)$ u dva se povećanja poništava i iznenađeno otkrivamo da je superpozicija dvaju povećanja zapravo ekvivalentna srednjoj slici.

![](./images/flow2.png)

Ovaj nam primjer govori da zbog učinka „poništavanja” koji donosi operacija poništavanja toka ne moramo brinuti jesmo li povećavajuće putove birali „pogrešnim” redoslijedom.

Lako se vidi: dok god na $G_f$ postoji povećavajući put, povećanjem duž njega ukupni tok raste; inače je ukupni tok dosegnuo najveću moguću vrijednost i postupak je gotov. To je postupak Ford–Fulkersonova povećanja.

### Teorem o maksimalnom toku i minimalnom rezu

Otprilike smo shvatili ideju Ford–Fulkersonova povećanja, ali kako dokazati ispravnost te metode? Zašto je tok $f$ nakon završetka povećanja maksimalni tok?

Zapravo, ispravnost Ford–Fulkersonova povećanja ekvivalentna je teoremu o maksimalnom toku i minimalnom rezu (max-flow min-cut theorem). Teorem kaže da za svaku mrežu $G = (V, E)$ maksimalni tok $f$ i minimalni rez $\{S, T\}$ uvijek zadovoljavaju $|f| = ||S, T||$.

Za dokaz teorema krenimo od leme: za mrežu $G = (V, E)$, za bilo koji tok $f$ i bilo koji rez $\{S, T\}$ uvijek vrijedi $|f| \leq ||S, T||$, pri čemu jednakost vrijedi ako i samo ako su svi bridovi iz $\{(u, v) | u \in S, v \in T\}$ zasićeni, a svi bridovi iz $\{(u, v) | u \in T, v \in S\}$ prazni.

???+ note "Dokaz"
    $$
    \begin{aligned}
    |f| & = f(s) \\
        & = \sum_{u \in S} f(u) \\
        & = \sum_{u \in S} \left( \sum_{v \in V} f(u, v) - \sum_{v \in V} f(v, u) \right) \\
        & = \sum_{u \in S} \left( \sum_{v \in T} f(u, v) + \sum_{v \in S} f(u, v) - \sum_{v \in T} f(v, u) - \sum_{v \in S} f(v, u) \right) \\
        & = \sum_{u \in S} \left( \sum_{v \in T} f(u, v) - \sum_{v \in T} f(v, u) \right) + \sum_{u \in S} \sum_{v \in S} f(u, v) - \sum_{u \in S} \sum_{v \in S} f(v, u) \\
        & = \sum_{u \in S} \left( \sum_{v \in T} f(u, v) - \sum_{v \in T} f(v, u) \right) \\
        & \leq \sum_{u \in S} \sum_{v \in T} f(u, v) \\
        & \leq \sum_{u \in S} \sum_{v \in T} c(u, v) \\
        & = ||S, T|| \\
    \end{aligned}
    $$
    
    Da bi vrijedila jednakost, prva nejednakost zahtijeva da su svi bridovi iz $\{(u, v) \mid u \in T, v \in S\}$ prazni, a druga da su svi bridovi iz $\{(u, v) \mid u \in S, v \in T\}$ zasićeni. Time je lema dokazana.

Može li se, dakle, za svaku mrežu uvjet jednakosti uvijek postići? Ako je odgovor potvrdan, teorem o maksimalnom toku i minimalnom rezu je dokazan. Pokušajmo to dokazati.

???+ note "Dokaz"
    Pretpostavimo da smo nakon neke runde povećanja dobili tok $f$ takav da na $G_f$ nema povećavajućeg puta, tj. na $G_f$ nema puta od $s$ do $t$. Označimo sa $S$ skup vrhova dostupnih iz $s$ i neka je $T = V \setminus S$.
    
    Očito je $\{S, T\}$ rez grafa $G_f$ i $||S, T|| = \sum_{u \in S} \sum_{v \in T} c_f(u, v) = 0$. Budući da su rezidualni kapaciteti nenegativni, to znači da za sve $u \in S, v \in T, (u, v) \in E_f$ vrijedi $c_f(u, v) = 0$. Te bridove dijelimo na dva slučaja: bridove koji postoje u izvornom grafu i obrnute bridove:
    
    -   $(u, v) \in E$: tada je $c_f(u, v) = c(u, v) - f(u, v) = 0$, pa je $c(u, v) = f(u, v)$, tj. svi bridovi iz $\{(u, v) \mid u \in S, v \in T\}$ su zasićeni;
    -   $(v, u) \in E$: tada je $c_f(u, v) = c(u, v) - f(u, v) = 0 - f(u, v) = f(v, u) = 0$, tj. svi bridovi iz $\{(v, u) \mid u \in S, v \in T\}$ su prazni.
    
    Dakle, nakon zaustavljanja povećanja tok $f$ zadovoljava uvjet jednakosti. Prema odnosu veličina iz leme, $f$ je prirodno maksimalni tok grafa $G$, a $\{S, T\}$ minimalni rez grafa $G$.

Lako se vidi da je Kőnigov teorem poseban slučaj teorema o maksimalnom toku i minimalnom rezu. Zapravo su oba povezana s dualnošću u linearnom programiranju.

### Analiza vremenske složenosti

Na mreži $G = (V, E)$ s cjelobrojnim tokovima trivijalno pretpostavljamo da je tok svakog povećanja cijeli broj; tada je jedna gornja granica vremenske složenosti Ford–Fulkersonova povećanja $O(|E||f|)$, gdje je $f$ maksimalni tok na $G$. Naime, složenost jedne runde povećanja je $O(|E|)$, a povećanje povećava ukupni tok, pa broj rundi ne može premašiti $|f|$.

Različite implementacije Ford–Fulkersonova povećanja imaju različite složenosti. Među uobičajenijima su algoritmi Edmonds–Karp, Dinic, SAP, ISAP itd., koje ćemo redom predstaviti u nastavku.

### Edmonds–Karpov algoritam

#### Ideja algoritma

Kako tražiti povećavajući put u $G_f$? Kad razmatramo konkretnu implementaciju Ford–Fulkersonova povećanja, najprirodniji je izbor BFS. Tada Ford–Fulkersonovo povećanje postaje Edmonds–Karpov algoritam. Konkretan postupak je sljedeći:

-   Ako na $G_f$ BFS-om iz $s$ možemo doći do $t$, našli smo novi povećavajući put.

-   Za povećavajući put $p$ izračunamo najmanji rezidualni kapacitet bridova kroz koje $p$ prolazi, $\Delta = \min_{(u, v) \in p} c_f(u, v)$. Svakom bridu na $p$ dodamo $\Delta$ toka, a njihovim obrnutim bridovima oduzmemo $\Delta$ toka, pa maksimalni tok raste za $\Delta$.

-   Budući da smo promijenili tok, dobivamo novi $G_f$; na novom $G_f$ ponavljamo postupak dok povećavajući put ne prestane postojati, nakon čega tok više ne raste.

Opisani algoritam je Edmonds–Karpov algoritam.

#### Analiza vremenske složenosti

Pokušajmo analizirati vremensku složenost Edmonds–Karpova algoritma.

Očito je složenost jedne runde BFS povećanja $O(|E|)$.

Gornja granica ukupnog broja rundi povećanja je $O(|V||E|)$. Ta se tvrdnja u internetskim izvorima često lažno dokazuje (ili neodređeno preskače). U nastavku pokušavamo dati formalniji dokaz[^ref_ek].

???+ note "Dokaz gornje granice ukupnog broja rundi povećanja"
    Najprije uvodimo lemu — lemu o nepadanju najkraćeg puta. Konkretno, označimo s $d_f(u)$ udaljenost (tj. duljinu najkraćeg puta, i dalje u tekstu) vrha $u$ od izvora $s$ na $G_f$. Za neku rundu povećanja neka $f$ i $f'$ označavaju tok prije odnosno poslije povećanja; tvrdimo da za svaki vrh $u$ povećanje uvijek daje $d_{f'}(u) \geq d_f(u)$. Tu lemu dokazat ćemo malo kasnije.
    
    Nazovimo brid s najmanjim rezidualnim kapacitetom na povećavajućem putu zasićenim bridom (ako ih je više najmanjih, uzmemo bilo koji). Ako je usmjereni brid $(u, v)$ odabran kao zasićeni brid, povećanje mu ispražnjava rezidualni kapacitet pa zasićeni brid nestaje, a poništavanje toka stvara novi obrnuti brid (ako prije nije postojao), tj. $(u, v) \not \in E_{f'}$ i $(v, u) \in E_{f'}$. Iz ove analize znamo da se za neusmjereni brid $(u, v)$ dva smjera povećanja uvijek izmjenjuju.
    
    Pri povećanju duž $(u, v)$ na $G_f$ vrijedi $d_f(u) + 1 = d_f(v)$, a nakon toga rezidualna mreža postaje $G_{f'}$. Pri povećanju duž $(v, u)$ na $G_{f'}$ vrijedi $d_{f'}(v) + 1 = d_{f'}(u)$. Prema lemi o nepadanju najkraćeg puta još je $d_{f'}(v) \geq d_f(v)$; povezivanjem svih izraza dobivamo $d_{f'}(u) \geq d_{f}(u) + 2$. Drugim riječima, ako je usmjereni brid $(u, v)$ odabran kao zasićeni brid, udaljenost od $u$ do $s$ veća je barem za $2$ u odnosu na prethodni put kad je bio odabran kao zasićeni brid.
    
    Udaljenost od $s$ do bilo kojeg vrha ne može premašiti $|V|$; u kombinaciji s gornjim svojstvom vidimo da je broj puta koliko je svaki brid odabran kao zasićeni brid $O(|V|)$, a množenjem brojem bridova dobivamo gornju granicu ukupnog broja rundi povećanja $O(|V||E|)$.
    
    Zatim dokazujemo lemu o nepadanju najkraćeg puta, tj. $d_{f'}(u) \geq d_f(u)$. Dokaz nije težak, ali može biti pomalo zamršen; čitatelj može zastati i pažljivo razmisliti.
    
    ???+ note "Dokaz leme o nepadanju najkraćeg puta"
        Dokazujemo kontradikcijom. Za neku rundu povećanja pretpostavimo da postoje vrhovi čija se udaljenost do $s$ nakon te runde smanjila u odnosu na stanje prije povećanja. Označimo s $v$ onaj od njih s najmanjom udaljenošću do $s$ (tj. $v = \arg \min_{x \in V, d_{f'}(x) < d_f(x)} d_{f'}(x)$). Uočimo da je prema pretpostavci kontradikcije $d_{f'}(v) < d_f(v)$ poznato.
        
        Na najkraćem putu od $s$ do $v$ u $G_{f'}$ označimo s $u$ prethodnik vrha $v$, tj. $d_{f'}(u) + 1 = d_{f'}(v)$.
        
        Da $u$ ne bi narušio svojstvo „najmanje udaljenosti” vrha $v$, mora vrijediti $d_{f'}(u) \geq d_f(u)$.
        
        Dodavanjem iste vrijednosti objema stranama dobivamo $d_{f'}(v) \geq d_f(u) + 1$. Ocjenom prema pretpostavci kontradikcije dobivamo $d_f(v) > d_f(u) + 1$.
        
        Razmotrimo sada smjer povećanja na $(u, v)$.
        
        -   Pretpostavimo da je usmjereni brid $(u, v) \in E_f$. Prema svojstvu „pretrage u širinu” BFS-a vrijedi $d_f(u) + 1 \geq d_f(v)$. To je u sukobu s rezultatom ocjene, što je kontradikcija.
        -   Pretpostavimo da usmjereni brid $(u, v) \not \in E_f$. Prema definiciji $u$ znamo da $(u, v) \in E_{f'}$, pa postojanje tog brida mora biti rezultat toga da je povećanje u ovoj rundi prošlo kroz $(v, u)$ i poništavanjem stvorilo obrnuti brid, tj. $d_f(v) + 1 = d_f(u)$. To je u sukobu s rezultatom ocjene, što je kontradikcija.
        
        Budući da povećanje duž $(u, v)$ u bilo kojem smjeru vodi u kontradikciju, pretpostavka kontradikcije ne vrijedi i lema o nepadanju najkraćeg puta je dokazana.

Množenjem složenosti jedne runde BFS povećanja s gornjom granicom broja rundi dobivamo da je vremenska složenost Edmonds–Karpova algoritma $O(|V||E|^2)$.

#### Implementacija

Moguća implementacija Edmonds–Karpova algoritma izgleda ovako.

??? note "Referentni kod"
    ```cpp
    constexpr int MAXN = 250;
    constexpr int INF = 0x3f3f3f3f;
    
    struct Edge {
      int from, to, cap, flow;
    
      Edge(int u, int v, int c, int f) : from(u), to(v), cap(c), flow(f) {}
    };
    
    struct EK {
      int n, m;             // n: broj vrhova, m: broj bridova
      vector<Edge> edges;   // edges: skup svih bridova
      vector<int> G[MAXN];  // G: vrh x -> indeksi svih bridova iz x u edges
      int a[MAXN], p[MAXN];  // a: vrh x -> najveći tok koji vrhu x daje brid kojim smo mu zadnje prišli u BFS-u
                             // p: vrh x -> brid kojim smo vrhu x zadnje prišli u BFS-u
    
      void init(int n) {
        for (int i = 0; i < n; i++) G[i].clear();
        edges.clear();
      }
    
      void AddEdge(int from, int to, int cap) {
        edges.push_back(Edge(from, to, cap, 0));
        edges.push_back(Edge(to, from, 0, 0));
        m = edges.size();
        G[from].push_back(m - 2);
        G[to].push_back(m - 1);
      }
    
      int Maxflow(int s, int t) {
        int flow = 0;
        for (;;) {
          memset(a, 0, sizeof(a));
          queue<int> Q;
          Q.push(s);
          a[s] = INF;
          while (!Q.empty()) {
            int x = Q.front();
            Q.pop();
            for (int i = 0; i < G[x].size(); i++) {  // prođi bridove s početkom u x
              Edge& e = edges[G[x][i]];
              if (!a[e.to] && e.cap > e.flow) {
                p[e.to] = G[x][i];  // G[x][i] je brid kojim smo zadnje prišli vrhu e.to
                a[e.to] =
                    min(a[x], e.cap - e.flow);  // tok koji vrhu e.to daje brid kojim smo mu zadnje prišli
                Q.push(e.to);
              }
            }
            if (a[t]) break;  // ako je ponor primio tok, prekini BFS
          }
          if (!a[t])
            break;  // ako ponor nije primio tok, izvor i ponor nisu u istoj komponenti povezanosti
          for (int u = t; u != s;
               u = edges[p[u]].from) {  // preko u slijedi put s -> t iz BFS-a
            edges[p[u]].flow += a[t];      // povećaj flow bridova na putu
            edges[p[u] ^ 1].flow -= a[t];  // smanji flow obrnutih bridova
          }
          flow += a[t];
        }
        return flow;
      }
    };
    ```

### Dinicov algoritam

#### Ideja algoritma

Razmotrimo da prije povećanja BFS-om razdijelimo $G_f$ na slojeve, tj. vrhove podijelimo u slojeve prema udaljenosti $d(u)$ vrha $u$ od izvora $s$. Zahtijevamo da tok kroz $u$ smije teći samo u vrhove $v$ sljedećeg sloja, tj. brišemo izlazne bridove iz $u$ prema vrhovima s jednakom ili manjom oznakom sloja; ostatak grafa $G_f$ zovemo slojeviti graf (level graph). Formalno, $G_L = (V, E_L)$ je slojeviti graf grafa $G_f = (V, E_f)$, gdje je $E_L = \left\{ (u, v) \mid (u, v) \in E_f, d(u) + 1 = d(v) \right\}$.

Ako na slojevitom grafu $G_L$ nađemo maksimalan (po inkluziji) povećavajući tok $f_b$ takav da ga samo unutar $G_L$ nije moguće dalje povećati, $f_b$ zovemo blokirajući tok (blocking flow) grafa $G_L$.

??? warning "Upozorenje"
    Iako smo gore povećanje/povećavajući tok definirali samo na jednom povećavajućem putu, u širem smislu riječ „povećanje” ne odnosi se samo na povećavajući tok na jednom putu, nego i na uniju više povećavajućih tokova — upravo u tom smislu definiramo blokirajući tok.

Nakon definicije slojevitog grafa i blokirajućeg toka, postupak Dinicova algoritma je sljedeći.

1.  Na $G_f$ BFS-om izgradimo slojeviti graf $G_L$.
2.  Na $G_L$ DFS-om nađemo blokirajući tok $f_b$.
3.  Spojimo $f_b$ s dosadašnjim tokom $f$, tj. $f \leftarrow f + f_b$.
4.  Ponavljamo postupak dok ne prestane postojati put od $s$ do $t$.

Tada je $f$ maksimalni tok.

Prije analize složenosti ovog algoritma moramo posebno objasniti postupak „na $G_L$ DFS-om nađemo blokirajući tok $f_b$”. Iako bi BFS za slojeviti graf čitateljima ove stranice trebao biti trivijalan, DFS za blokirajući tok traži malo vještine — moramo uvesti optimizaciju trenutnog luka (current arc).

Uočimo da tijekom DFS-a na $G_L$, ako vrh $u$ ima mnogo ulaznih i izlaznih bridova i pri svakom primanju toka iz ulaznog brida prolazi cijeli popis izlaznih bridova da odluči kojem izlaznom bridu proslijediti tok, lokalna složenost u $u$ u najgorem slučaju doseže $O(|E|^2)$. Da bismo to izbjegli: ako u nekom trenutku već znamo da je brid $(u, v)$ povećan do kraja (brid $(u, v)$ više nema rezidualnog kapaciteta ili je dio iza $v$ povećan do blokade), tok iz $u$ više nema smisla pokušavati slati izlaznim bridom $(u, v)$. Stoga za svaki vrh $u$ održavamo prvi izlazni brid u popisu izlaznih bridova od $u$ koji još ima smisla pokušati. Po običaju taj pokazivač zovemo trenutni luk, a postupak optimizacija trenutnog luka.

??? note "Višestruko povećanje"
    Višestruko povećanje konstantna je optimizacija Dinicova algoritma: ako smo na slojevitom grafu našli povećavajući put $p$ od $s$ do $t$, ne moramo nužno sljedeći povećavajući put tražiti iznova od $s$, nego možemo krenuti od posljednjeg mjesta na $p$ koje još ima rezidualnog kapaciteta i potražiti ogranak za povećanje. S obzirom na podudarnost s oblikom povratnog hoda (backtracking), ova je optimizacija u DFS implementaciji prirodna.
    
    ??? failure "Česta zabluda"
        Vjerojatno zbog pogrešnih formulacija u brojnim internetskim izvorima koje se prenose dalje, mnogi natjecatelji vole optimizaciju trenutnog luka i višestruko povećanje zajedno nazivati dvjema optimizacijama Dinicova algoritma. Zapravo je optimizacija trenutnog luka dio koji jamči ispravnost složenosti Dinicova algoritma, a višestruko povećanje tek konstantna optimizacija koja ne utječe na složenost.

#### Analiza vremenske složenosti

Uz optimizaciju trenutnog luka analiza složenosti Dinicova algoritma je sljedeća.

Najprije pokušajmo dokazati da je složenost DFS-a za blokirajući tok u jednoj rundi povećanja $O(|V||E|)$.

???+ note "Dokaz vremenske složenosti jedne runde povećanja"
    Promotrimo svaki povećavajući put u blokirajućem toku $f_b$; svi su dobiveni skakanjem duž trenutnog luka na $G_L$, pri čemu broj skokova svakog povećavajućeg puta ne može premašiti $|V|$.
    
    Svakim pronađenim povećavajućim putem nestaje jedan zasićeni brid (rezidualni kapacitet pada na nulu). Za sve povećavajuće putove u blokirajućem toku $f_b$, skup zasićenih bridova koje oni ispražnjavaju označimo $E_1$. S obzirom na slojevitost $G_L$, nakon nestanka zasićenog brida njegov obrnuti brid ne može u istoj rundi povećanja proći drugi povećavajući put, pa je $E_1$ podskup od $E_L$.
    
    Nadalje, za slučajeve u kojima smo skakali duž trenutnog luka, ali zbog blokade na nekom mjestu nismo uspjeli dobiti povećavajući put, skup posljednjih bridova tih nepotpunih putova označimo $E_2$. Članovi $E_2$ nisu zasićeni, pa su $E_1$ i $E_2$ disjunktni, a $E_1 \cup E_2$ i dalje je podskup od $E_L$.
    
    Budući da nijedan član $E_1 \cup E_2$ nije potrošio više od $|V|$ skokova (a uz optimizaciju višestrukog povećanja neki se skokovi broje višestruko), zaključno, ukupni broj skokova tijekom DFS-a ne može premašiti $|V||E_L|$.
    
    ??? failure "Jedan čest lažni dokaz"
        Za svaki vrh održavamo sljedeći brid kojim se može povećavati, a trenutni luk mijenja se najviše $|E|$ puta, pa je najgora složenost jedne runde povećanja $O(|V||E|)$.
    
    ??? bug "Greška"
        Iz „trenutni luk mijenja se najviše $|E|$ puta” ne slijedi „svaki vrh posjećuje svoje izlazne bridove najviše $|E|$ puta”. Naime, posjet trenutnom luku ne iscrpljuje nužno njegov rezidualni kapacitet, pa vrh $u$ može isti trenutni luk posjetiti više puta.

Uočimo da broj slojeva slojevitog grafa očito ne može premašiti $|V|$; ako dokažemo da broj slojeva tijekom povećanja strogo raste, broj rundi povećanja Dinicova algoritma je $O(|V|)$. Pokušajmo to dokazati[^ref_dinic].

???+ note "Dokaz monotonosti broja slojeva slojevitog grafa"
    Moramo uvesti pojam iz algoritama tipa push-relabel (druge klase algoritama za maksimalni tok): visinsku oznaku. Da bismo dokaz lakše izrazili visinskim oznakama, u dokazu neka je $d_f(u)$ udaljenost vrha $u$ do **ponora** $t$ na $G_f$ i slojeve gradimo od **ponora**, a ne od izvora (u tome nema bitne razlike). Za neku rundu povećanja neka $f$ i $f'$ označavaju tok prije odnosno poslije povećanja. Nakon računanja i dodavanja blokirajućeg toka u toj rundi neka se slojeviti graf promijeni iz $G_L = (V, E_L)$ u $G'_{L} = (V, E'_L)$.
    
    Dajemo nestrogu privremenu definiciju visinske oznake: na mreži $G = (V, E)$ neka je $h$ funkcija sa skupa vrhova $V$ u skup cijelih brojeva $N$; $h$ je valjana visinska oznaka na $G$ ako i samo ako $h(u) \leq h(v) + 1$ vrijedi za sve $(u, v) \in E$.
    
    Promotrimo sve članove $(u, v)$ skupa $E_{f'}$; uočavamo da je razlog za $(u, v) \in E_{f'}$ jedan od sljedeća dva.
    
    -   $(u, v) \in E_f$ i rezidualni kapacitet nije iscrpljen tijekom te runde povećanja — prema definiciji najkraćeg puta tada je $d_f(u) \leq d_f(v) + 1$;
    -   $(u, v) \not \in E_f$, ali je u toj rundi blokirajući tok prošao kroz $(v, u)$ i poništavanjem stvorio obrnuti brid — prema definiciji slojevitog grafa i blokirajućeg toka tada je $d_f(u) + 1 = d_f(v)$.
    
    Iz tog zapažanja zaključujemo: $d_f$ je valjana visinska oznaka na $G_{f'}$. Naravno, i na podgrafu $G'_L$ grafa $G_{f'}$.
    
    Sada, za povećavajući put $p = (s, \dots, u, v, \dots, t)$ na $G'_L$, razmotrimo postupak u kojem od praznog puta dodajemo po jedan vrh obrnutim redoslijedom vrhova na $p$ (od $t$ prema $s$). Pretpostavimo da je vrh $v$ već dodan, a vrh $u$ upravo dodajemo; uočavamo da se nakon dodavanja vrha $u$, prema definiciji slojevitog grafa, vrijednost $d_{f'}(u)$ u odnosu na $d_{f'}(v)$ poveća za $1$; istodobno, budući da je $d_f$ visinska oznaka na $G'_L$, vrijednost $d_f(u)$ u odnosu na $d_f(v)$ može se povećati za $1$, ostati ista ili se smanjiti. Stoga nakon dodavanja cijelog puta dobivamo $d_{f'}(s) \geq d_f(s)$, pri čemu jednakost vrijedi ako i samo ako $d_f(u) = d_f(v) + 1$ vrijedi za sve $(u, v) \in p$. Ako jednakost ne može nastupiti, vrijedi $d_{f'}(s) > d_f(s)$ — upravo željeni zaključak „broj slojeva slojevitog grafa tijekom povećanja strogo raste”. Pokušajmo dokazati da jednakost ne može nastupiti.
    
    Dokazujemo kontradikcijom: pretpostavimo da vrijedi $d_{f'}(s) = d_f(s)$ i pokušajmo izvesti kontradikciju. Tvrdimo da na $G'_L$ put $p$ sadrži barem jedan brid $(u, v)$ koji ne postoji na $G_L$. Kad takvog brida ne bi bilo, s obzirom na $d_f(s) = d_{f'}(s)$ i definicije slojevitog grafa i blokirajućeg toka, povećanje na $G_L$ ne bi još bilo dovršeno. Da bi se izbjegla ta kontradikcija, naša tvrdnja mora biti točna.
    
    Neka je $(u, v)$ brid koji zadovoljava tvrdnju; razlog može biti samo jedan od sljedeća dva.
    
    -   $(u, v) \in E_f$, ali u $d_f(u) \leq d_f(v) + 1$ ne vrijedi jednakost, pa prema definiciji slojevitog grafa $(u, v) \not \in E_L$, a nakon povećanja u novom slojevanju dodan je u $E'_L$;
    -   $(u, v) \not \in E_f$, što znači da je brid $(u, v)$ nastao tako što je blokirajući tok u ovoj rundi prošao kroz $(v, u)$ i poništavanjem stvorio obrnuti brid, tj. $d_f(u) = d_f(v) - 1$.
    
    Budući da u oba slučaja u kojima tvrdnja vrijedi dobivamo $d_f(u) \neq d_f(v) + 1$, tj. nužan i dovoljan uvjet za jednakost u $d_{f'}(s) \geq d_f(s)$ ne može biti ispunjen, to je u sukobu s pretpostavkom $d_{f'}(s) = d_f(s)$ i tvrdnja je dokazana.
    
    ??? failure "Još jedan čest lažni dokaz"
        Dokazujemo kontradikcijom. Pretpostavimo da je nakon jedne runde povećanja broj slojeva slojevitog grafa jednak prijašnjem; tada bi na slojevitom grafu još postojao barem jedan povećavajući put od $s$ do $t$ u kojem je razlika slojeva susjednih vrhova $1$. To što taj put nije povećan znači da runda povećanja nije završila. Da se izbjegne ta kontradikcija, tvrdnja vrijedi.
    
    ??? bug "Greška"
        Iz „najkraći $s$-$t$ put na novom slojevitom grafu nakon runde povećanja jednak je prijašnjem” ne slijedi „runda povećanja na starom slojevitom grafu nije završila”. Naime, nema razloga da skupovi bridova dvaju slojevitih grafova budu jednaki; najkraći $s$-$t$ put na novom slojevitom grafu može prolaziti bridovima koji na starom nisu postojali.

Množenjem složenosti jedne runde povećanja $O(|V||E|)$ s brojem rundi $O(|V|)$ dobivamo da je vremenska složenost Dinicova algoritma $O(|V|^2|E|)$.

Da bi stvarno vrijeme izvođenja Dinicova algoritma bilo blizu teorijske gornje granice, kao ulaz treba konstruirati mreže s posebnim svojstvima. Budući da se u natjecateljskoj praksi provjera znanja o tokovima često usredotočuje na tehniku modeliranja izvornog problema kao problema toka, naši modeli obično nemaju posebna svojstva zbog kojih bi Dinicov algoritam bio spor; naprotiv, Dinicov je algoritam na većini grafova vrlo učinkovit. Zato su ograničenja u zadacima s tokovima obično velika i način „uvrsti $|V|, |E|$ u $|V|^2|E|$ da procijeniš vrijeme” nije primjenjiv. Za točnu procjenu natjecatelju treba iskustvo s praktičnom učinkovitošću Dinicova algoritma; čitatelj može više vježbati.

#### Analiza vremenske složenosti u posebnim slučajevima

Na nekim grafovima s dobrim svojstvima Dinicov algoritam ima bolju složenost.

Za mrežu $G = (V, E)$, ako su kapaciteti svih bridova $1$, tj. $c(u, v) \in \{0, 1\}$ za sve $(u, v) \in E$, kažemo da je $G$ mreža jediničnih kapaciteta (unit capacity).

U mreži jediničnih kapaciteta složenost jedne runde povećanja Dinicova algoritma je $O(|E|)$.

???+ note "Dokaz"
    Naime, svako povećanje čini sve bridove na povećavajućem putu zasićenima pa oni nestaju; stoga se u jednoj rundi svaki brid može povećati samo jednom.

U mreži jediničnih kapaciteta broj rundi povećanja Dinicova algoritma je $O(|E|^{\frac{1}{2}})$.

???+ note "Dokaz"
    Slojeve gradimo oko izvora $s$; neka je $d_f(u)$ udaljenost vrha $u$ do izvora $s$ na $G_f$. Nadalje, skup vrhova $\left\{u \mid u \in V, d_f(u) = k \right\}$ definiramo kao sloj $D_k$ s indeksom $k$ i označimo $S_k = \cup_{i \leq k} D_i$.
    
    Pretpostavimo da smo već izveli $|E|^{\frac{1}{2}}$ rundi povećanja. Prema Dirichletovu principu postoji barem jedan $k$ za koji skup bridova $\left\{ (u, v) \mid u \in D_k, v \in D_{k+1}, (u, v) \in E_f \right\}$ nema više od $\frac {|E|} {|E|^{\frac{1}{2}}} \approx |E|^{\frac{1}{2}}$ članova. Očito je $\{S_k, V - S_k\}$ $s$-$t$ rez na $G_f$ kapaciteta najviše $|E|^{\frac{1}{2}}$. Prema teoremu o maksimalnom toku i minimalnom rezu maksimalni tok na $G_f$ nije veći od $|E|^{\frac{1}{2}}$, tj. na $G_f$ se može izvesti još najviše $|E|^{\frac{1}{2}}$ rundi povećanja. Stoga je ukupan broj rundi $O(|E|^{\frac{1}{2}})$.

U mreži jediničnih kapaciteta broj rundi povećanja Dinicova algoritma je $O(|V|^{\frac{2}{3}})$.

???+ note "Dokaz"
    Pretpostavimo da smo već izveli $2 |V|^{\frac{2}{3}}$ rundi povećanja. Budući da najviše polovica slojeva ($|V|^{\frac{2}{3}}$ njih) sadrži više od $|V|^{\frac{1}{3}}$ vrhova, bez obzira na raspodjelu veličina slojeva postoji barem jedan $k$ za koji dva susjedna sloja oba sadrže najviše $|V|^{\frac{1}{3}}$ vrhova, tj. $|D_k| \leq |V|^{\frac{1}{3}}$ i $|D_{k+1}| \leq |V|^{\frac{1}{3}}$.
    
    Da bismo maksimizirali broj bridova između $D_k$ i $D_{k+1}$, pretpostavimo da tvore potpun bipartitan graf; tada skup bridova $\left\{ (u, v) \mid u \in D_k, v \in D_{k+1}, (u, v) \in E_f \right\}$ nema više od $|V|^{\frac{2}{3}}$ članova. Očito je $\{S_k, V - S_k\}$ $s$-$t$ rez na $G_f$ kapaciteta najviše $|V|^{\frac{2}{3}}$. Prema teoremu o maksimalnom toku i minimalnom rezu maksimalni tok na $G_f$ nije veći od $|V|^{\frac{2}{3}}$, tj. na $G_f$ se može izvesti još najviše $|V|^{\frac{2}{3}}$ rundi povećanja. Stoga je ukupan broj rundi $O(|V|^{\frac{2}{3}})$.

U mreži jediničnih kapaciteta, ako za svaki vrh $u$ osim izvora i ponora vrijedi $\mathit{deg}_{\mathit{in}}(u) = 1$ ili $\mathit{deg}_{\mathit{out}}(u) = 1$, broj rundi povećanja Dinicova algoritma je $O(|V|^{\frac{1}{2}})$. Pritom $\mathit{deg}_{\mathit{in}}(u)$ i $\mathit{deg}_{\mathit{out}}(u)$ označavaju ulazni odnosno izlazni stupanj vrha $u$.

???+ note "Dokaz"
    Uvodimo lemu: za mrežu ovog oblika svaki se tok na njoj može rastaviti na nekoliko **vršno disjunktnih** povećavajućih putova jediničnog toka.
    
    Pretpostavimo da smo već izveli $|V|^{\frac{1}{2}}$ rundi povećanja. Prema definiciji slojevitog grafa duljina svakog novog povećavajućeg puta tada je barem $|V|^{\frac{1}{2}}$.
    
    Promotrimo rastav maksimalnog toka na $G_f$ na povećavajuće putove; broj dobivenih putova ne može biti veći od $\frac {|V|} {|V|^{\frac{1}{2}}} \approx |V|^{\frac{1}{2}}$, što znači da se na $G_f$ može izvesti još najviše $|V|^{\frac{1}{2}}$ rundi povećanja. Stoga je ukupan broj rundi $O(|V|^{\frac{1}{2}})$.

Zaključno, izvodimo neke posljedice.

-   Na mreži jediničnih kapaciteta ukupna složenost Dinicova algoritma je $O(|E| \min(|E|^\frac{1}{2}, |V|^{\frac{2}{3}}))$.
-   Na mreži jediničnih kapaciteta, ako za svaki vrh $u$ osim izvora i ponora vrijedi $\mathit{deg}_{\mathit{in}}(u) = 1$ ili $\mathit{deg}_{\mathit{out}}(u) = 1$, ukupna složenost Dinicova algoritma je $O(|E||V|^{\frac{1}{2}})$. Za problem najvećeg sparivanja u bipartitnom grafu često koristimo Hopcroft–Karpov algoritam, koji je zapravo poseban slučaj Dinicova algoritma na mreži jediničnih kapaciteta koja zadovoljava navedeno ograničenje stupnjeva.

#### Implementacija

??? note "Referentni kod"
    ```cpp
    struct MF {
      struct edge {
        int v, nxt, cap, flow;
      } e[N];
    
      int fir[N], cnt = 0;
    
      int n, S, T;
      ll maxflow = 0;
      int dep[N], cur[N];
    
      void init() {
        memset(fir, -1, sizeof fir);
        cnt = 0;
      }
    
      void addedge(int u, int v, int w) {
        e[cnt] = {v, fir[u], w, 0};
        fir[u] = cnt++;
        e[cnt] = {u, fir[v], 0, 0};
        fir[v] = cnt++;
      }
    
      bool bfs() {
        queue<int> q;
        memset(dep, 0, sizeof(int) * (n + 1));
    
        dep[S] = 1;
        q.push(S);
        while (q.size()) {
          int u = q.front();
          q.pop();
          for (int i = fir[u]; ~i; i = e[i].nxt) {
            int v = e[i].v;
            if ((!dep[v]) && (e[i].cap > e[i].flow)) {
              dep[v] = dep[u] + 1;
              q.push(v);
            }
          }
        }
        return dep[T];
      }
    
      int dfs(int u, int flow) {
        if ((u == T) || (!flow)) return flow;
    
        int ret = 0;
        for (int& i = cur[u]; ~i; i = e[i].nxt) {
          int v = e[i].v, d;
          if ((dep[v] == dep[u] + 1) &&
              (d = dfs(v, min(flow - ret, e[i].cap - e[i].flow)))) {
            ret += d;
            e[i].flow += d;
            e[i ^ 1].flow -= d;
            if (ret == flow) return ret;
          }
        }
        return ret;
      }
    
      void dinic() {
        while (bfs()) {
          memcpy(cur, fir, sizeof(int) * (n + 1));
          maxflow += dfs(S, INF);
        }
      }
    } mf;
    ```

### Algoritam MPM

Algoritam **MPM** (Malhotra, Pramodh-Kumar i Maheshwari) maksimalni tok dobiva na dva načina: prioritetnim redom zasnovanim na gomili, sa složenošću $O(n^3\log n)$, ili češćim rješenjem s BFS-om, sa složenošću $O(n^3)$. Napomena: ovaj se odjeljak bavi samo analizom boljeg i jednostavnijeg algoritma $O(n^3)$.

Opća struktura algoritma MPM slična je Dinicovu algoritmu; također radi u fazama. U svakoj fazi traži povećavajuće putove u slojevitoj mreži rezidualne mreže od $G$. Glavna razlika u odnosu na Dinicov algoritam jest način traženja povećavajućih putova: dio algoritma MPM koji traži povećavajuće putove troši samo $O(n^2)$, što je složenost bolja od Dinicove.

Algoritam MPM razmatra kapacitete vrhova, a ne bridova. Ako u slojevitoj mreži $L$ kapacitet $p(v)$ vrha $v$ definiramo kao manji od njegova ulaznog i izlaznog rezidualnog kapaciteta, vrijedi:

$$
\begin{aligned}
p_{in}(v) &= \sum\limits_{(u,v) \in L} (c(u, v) - f(u, v)) \\
p_{out}(v) &= \sum\limits_{(v,u) \in L} (c(v, u) - f(v, u)) \\
p(v) &= \min (p_{in}(v), p_{out}(v))
\end{aligned}
$$

Vrh $r$ zovemo referentnim vrhom ako i samo ako $p(r) = \min {p(v)}$. Za referentni vrh $r$ sigurno možemo tok kroz $r$ povećati za $p(r)$ tako da mu kapacitet padne na $0$. Naime, $L$ je usmjeren aciklički graf i kapaciteti vrhova u $L$ iznose barem $p(r)$, pa sigurno postoji usmjereni put od $s$ preko $r$ do $t$. Tada tok svih bridova na tom putu povećamo za $p(r)$. Taj je put povećavajući put ove faze. Povećavajući put može se naći BFS-om. Nakon povećanja svi zasićeni bridovi mogu se izbrisati iz $L$, jer se u ovoj fazi više neće koristiti. Isto tako, mogu se izbrisati svi vrhovi različiti od $s$ i $t$ koji nemaju izlaznih ili ulaznih bridova.

#### Analiza vremenske složenosti

Svaka faza algoritma MPM treba $O(V^2)$, jer ima najviše $V$ iteracija (jer se barem odabrani referentni vrh briše), a u svakoj iteraciji brišemo sve bridove kroz koje smo prošli osim najviše $V$ njih. Zbrajanjem dobivamo $O(V^2+E)=O(V^2)$. Budući da je ukupni broj faza manji od $V$, ukupno vrijeme izvođenja algoritma MPM je $O(V^3)$.

???+ note "Dokaz da je ukupni broj faza manji od V"
    Algoritam MPM završava u manje od $V$ faza. Da bismo to dokazali, moramo najprije dokazati dvije leme.
    
    **Lema 1**: nakon svake iteracije udaljenost od $s$ do svakog vrha ne smanjuje se, tj. $level_{i+1}[v] \ge level_{i}[v]$.
    
    **Dokaz**: fiksirajmo fazu $i$ i vrh $v$. Promotrimo bilo koji najkraći put $P$ od $s$ do $v$ u $G_{i}^R$. Duljina puta $P$ jednaka je $level_{i}[v]$. Uočimo da $G_{i}^R$ može sadržavati samo unatražne i unaprijedne bridove iz $G_{i}^R$. Ako $P$ nema unatražnih bridova iz $G_{i}^R$, onda $level_{i+1}[v] \ge level_{i}[v]$, jer je $P$ i put u $G_{i}^R$. Pretpostavimo sada da $P$ ima barem jedan unatražni brid i da je prvi takav $(u,w)$; tada $level_{i+1}[u] \ge level_{i}[u]$ (zbog prvog slučaja). Brid $(u,w)$ ne pripada $G_{i}^R$, pa je na $(u,w)$ utjecao povećavajući put prethodne iteracije. To znači $level_{i}[u] = level_{i}[w]+1$. Osim toga, $level_{i+1}[w] = level_{i+1}[u]+1$. Iz te dvije jednadžbe i $level_{i+1}[u] \ge level_{i}[u]$ dobivamo $level_{i+1}[w] \ge level_{i}[w]+2$. Ista ideja može se primijeniti na ostatak puta.
    
    **Lema 2**: $level_{i+1}[t] > level_{i}[t]$.
    
    **Dokaz**: iz leme 1 dobivamo $level_{i+1}[t] \ge level_{i}[t]$. Pretpostavimo $level_{i+1}[t] = level_{i}[t]$; uočimo da $G_{i}^R$ može sadržavati samo unatražne i unaprijedne bridove iz $G_{i}^R$. To znači da u $G_{i}^R$ postoji najkraći put koji nije blokiran povećavajućim putovima. To je kontradikcija.

#### Implementacija

??? note "Referentni kod"
    ```cpp
    struct MPM {
      struct FlowEdge {
        int v, u;
        long long cap, flow;
    
        FlowEdge() {}
    
        FlowEdge(int _v, int _u, long long _cap, long long _flow)
            : v(_v), u(_u), cap(_cap), flow(_flow) {}
    
        FlowEdge(int _v, int _u, long long _cap)
            : v(_v), u(_u), cap(_cap), flow(0ll) {}
      };
    
      constexpr static long long flow_inf = 1e18;
      vector<FlowEdge> edges;
      vector<char> alive;
      vector<long long> pin, pout;
      vector<list<int>> in, out;
      vector<vector<int>> adj;
      vector<long long> ex;
      int n, m = 0;
      int s, t;
      vector<int> level;
      vector<int> q;
      int qh, qt;
    
      void resize(int _n) {
        n = _n;
        ex.resize(n);
        q.resize(n);
        pin.resize(n);
        pout.resize(n);
        adj.resize(n);
        level.resize(n);
        in.resize(n);
        out.resize(n);
      }
    
      MPM() {}
    
      MPM(int _n, int _s, int _t) {
        resize(_n);
        s = _s;
        t = _t;
      }
    
      void add_edge(int v, int u, long long cap) {
        edges.push_back(FlowEdge(v, u, cap));
        edges.push_back(FlowEdge(u, v, 0));
        adj[v].push_back(m);
        adj[u].push_back(m + 1);
        m += 2;
      }
    
      bool bfs() {
        while (qh < qt) {
          int v = q[qh++];
          for (int id : adj[v]) {
            if (edges[id].cap - edges[id].flow < 1) continue;
            if (level[edges[id].u] != -1) continue;
            level[edges[id].u] = level[v] + 1;
            q[qt++] = edges[id].u;
          }
        }
        return level[t] != -1;
      }
    
      long long pot(int v) { return min(pin[v], pout[v]); }
    
      void remove_node(int v) {
        for (int i : in[v]) {
          int u = edges[i].v;
          auto it = find(out[u].begin(), out[u].end(), i);
          out[u].erase(it);
          pout[u] -= edges[i].cap - edges[i].flow;
        }
        for (int i : out[v]) {
          int u = edges[i].u;
          auto it = find(in[u].begin(), in[u].end(), i);
          in[u].erase(it);
          pin[u] -= edges[i].cap - edges[i].flow;
        }
      }
    
      void push(int from, int to, long long f, bool forw) {
        qh = qt = 0;
        ex.assign(n, 0);
        ex[from] = f;
        q[qt++] = from;
        while (qh < qt) {
          int v = q[qh++];
          if (v == to) break;
          long long must = ex[v];
          auto it = forw ? out[v].begin() : in[v].begin();
          while (true) {
            int u = forw ? edges[*it].u : edges[*it].v;
            long long pushed = min(must, edges[*it].cap - edges[*it].flow);
            if (pushed == 0) break;
            if (forw) {
              pout[v] -= pushed;
              pin[u] -= pushed;
            } else {
              pin[v] -= pushed;
              pout[u] -= pushed;
            }
            if (ex[u] == 0) q[qt++] = u;
            ex[u] += pushed;
            edges[*it].flow += pushed;
            edges[(*it) ^ 1].flow -= pushed;
            must -= pushed;
            if (edges[*it].cap - edges[*it].flow == 0) {
              auto jt = it;
              ++jt;
              if (forw) {
                in[u].erase(find(in[u].begin(), in[u].end(), *it));
                out[v].erase(it);
              } else {
                out[u].erase(find(out[u].begin(), out[u].end(), *it));
                in[v].erase(it);
              }
              it = jt;
            } else
              break;
            if (!must) break;
          }
        }
      }
    
      long long flow() {
        long long ans = 0;
        while (true) {
          pin.assign(n, 0);
          pout.assign(n, 0);
          level.assign(n, -1);
          alive.assign(n, true);
          level[s] = 0;
          qh = 0;
          qt = 1;
          q[0] = s;
          if (!bfs()) break;
          for (int i = 0; i < n; i++) {
            out[i].clear();
            in[i].clear();
          }
          for (int i = 0; i < m; i++) {
            if (edges[i].cap - edges[i].flow == 0) continue;
            int v = edges[i].v, u = edges[i].u;
            if (level[v] + 1 == level[u] && (level[u] < level[t] || u == t)) {
              in[u].push_back(i);
              out[v].push_back(i);
              pin[u] += edges[i].cap - edges[i].flow;
              pout[v] += edges[i].cap - edges[i].flow;
            }
          }
          pin[s] = pout[t] = flow_inf;
          while (true) {
            int v = -1;
            for (int i = 0; i < n; i++) {
              if (!alive[i]) continue;
              if (v == -1 || pot(i) < pot(v)) v = i;
            }
            if (v == -1) break;
            if (pot(v) == 0) {
              alive[v] = false;
              remove_node(v);
              continue;
            }
            long long f = pot(v);
            ans += f;
            push(v, s, f, false);
            push(v, t, f, true);
            alive[v] = false;
            remove_node(v);
          }
        }
        return ans;
      }
    };
    ```

### ISAP

U Dinicovu algoritmu nakon svakog računanja povećavajućih putova moramo pokrenuti BFS za slojevanje; postoji li učinkovitiji način?

Odgovor je algoritam ISAP koji slijedi.

#### Postupak

Kao i u Dinicovu algoritmu, najprije BFS-om razdijelimo vrhove grafa u slojeve, ali za razliku od Dinica BFS radimo na obrnutom grafu, od vrha $t$ prema vrhu $s$.

Nakon slojevanja DFS-om tražimo povećavajuće putove.

Postupak povećanja sličan je Dinicovu: povećavamo samo prema vrhovima čiji je sloj za $1$ manji od sloja trenutnog vrha.

Za razliku od Dinica, ne pokrećemo ponovno BFS da bismo iznova razdijelili vrhove u slojeve, nego ponovno slojevanje obavljamo tijekom samog povećanja.

Konkretno, neka je $d_i$ sloj vrha $i$; kad završimo s povećanjem u vrhu $i$, prođemo sve izlazne bridove vrha $i$ u rezidualnoj mreži, nađemo odredišni vrh $j$ s najmanjim slojem i postavimo $d_i \gets d_j+1$. Posebno, ako $i$ u rezidualnoj mreži nema izlaznih bridova, postavimo $d_i \gets n$.

Lako se vidi da kad je $d_s \geq n$, u grafu nema povećavajućeg puta i algoritam možemo zaustaviti.

Slično Dinicu, i u ISAP-u postoji **optimizacija trenutnog luka**.

ISAP ima još jednu optimizaciju: pamtimo broj vrhova $num_i$ sa slojem $i$; svaki put kad sloj nekog vrha ažuriramo s $x$ na $y$, ažuriramo i polje $num$, a ako je nakon ažuriranja $num_x=0$, u grafu je nastao „procjep” i povećavajući put više se ne može naći, pa algoritam možemo odmah zaustaviti (u implementaciji jednostavno postavimo $d_s$ na $n$). Ta se optimizacija zove **GAP optimizacija**.

#### Implementacija

??? note "Referentni kod"
    ```cpp
    struct Edge {
      int from, to, cap, flow;
    
      Edge(int u, int v, int c, int f) : from(u), to(v), cap(c), flow(f) {}
    };
    
    bool operator<(const Edge& a, const Edge& b) {
      return a.from < b.from || (a.from == b.from && a.to < b.to);
    }
    
    struct ISAP {
      int n, m, s, t;
      vector<Edge> edges;
      vector<int> G[MAXN];
      bool vis[MAXN];
      int d[MAXN];
      int cur[MAXN];
      int p[MAXN];
      int num[MAXN];
    
      void AddEdge(int from, int to, int cap) {
        edges.push_back(Edge(from, to, cap, 0));
        edges.push_back(Edge(to, from, 0, 0));
        m = edges.size();
        G[from].push_back(m - 2);
        G[to].push_back(m - 1);
      }
    
      bool BFS() {
        memset(vis, 0, sizeof(vis));
        queue<int> Q;
        Q.push(t);
        vis[t] = true;
        d[t] = 0;
        while (!Q.empty()) {
          int x = Q.front();
          Q.pop();
          for (int i = 0; i < G[x].size(); i++) {
            Edge& e = edges[G[x][i] ^ 1];
            if (!vis[e.from] && e.cap > e.flow) {
              vis[e.from] = true;
              d[e.from] = d[x] + 1;
              Q.push(e.from);
            }
          }
        }
        return vis[s];
      }
    
      void init(int n) {
        this->n = n;
        for (int i = 0; i < n; i++) G[i].clear();
        edges.clear();
      }
    
      int Augment() {
        int x = t, a = INF;
        while (x != s) {
          Edge& e = edges[p[x]];
          a = min(a, e.cap - e.flow);
          x = edges[p[x]].from;
        }
        x = t;
        while (x != s) {
          edges[p[x]].flow += a;
          edges[p[x] ^ 1].flow -= a;
          x = edges[p[x]].from;
        }
        return a;
      }
    
      int Maxflow(int s, int t) {
        this->s = s;
        this->t = t;
        int flow = 0;
        BFS();
        memset(num, 0, sizeof(num));
        for (int i = 0; i < n; i++) num[d[i]]++;
        int x = s;
        memset(cur, 0, sizeof(cur));
        while (d[s] < n) {
          if (x == t) {
            flow += Augment();
            x = s;
          }
          int ok = 0;
          for (int i = cur[x]; i < G[x].size(); i++) {
            Edge& e = edges[G[x][i]];
            if (e.cap > e.flow && d[x] == d[e.to] + 1) {
              ok = 1;
              p[e.to] = G[x][i];
              cur[x] = i;
              x = e.to;
              break;
            }
          }
          if (!ok) {
            int m = n - 1;
            for (int i = 0; i < G[x].size(); i++) {
              Edge& e = edges[G[x][i]];
              if (e.cap > e.flow) m = min(m, d[e.to]);
            }
            if (--num[d[x]] == 0) break;
            num[d[x] = m + 1]++;
            cur[x] = 0;
            if (x != s) x = edges[p[x]].from;
          }
        }
        return flow;
      }
    };
    ```

## Push-relabel algoritmi (predtok)

Ova metoda tijekom rješavanja zanemaruje očuvanje toka i svaki put ažurira podatke jednog vrha kako bi izračunala maksimalni tok.

### Opći push-relabel algoritam

Najprije predstavljamo glavnu ideju push-relabel algoritma i jednu izvedivu grubu implementaciju.

Push-relabel algoritam računa maksimalni tok ažuriranjem pojedinačnih vrhova sve dok više nema vrhova koje treba ažurirati.

Funkcija toka koju algoritam održava ne mora čuvati očuvanje toka: za vrh dopuštamo da ulazni tok premaši izlazni; višak zovemo **višak toka** (excess) $e(u)$ vrha $u(u\in V-\{s,t\})$:

$$
e(u)=\sum_{(x,u)\in E}f(x,u)-\sum_{(u,y)\in E}f(u,y)
$$

Ako je $e(u)>0$, kažemo da vrh $u$ **prelijeva**[^note1]; uočimo da kad govorimo o prelijevajućim vrhovima, ne uključujemo $s$ i $t$.

Push-relabel algoritam održava visinu $h(u)$ svakog vrha i propisuje da prelijevajući vrh $u$, ako želi gurnuti višak toka, to smije učiniti samo prema vrhu visine manje od $u$; ako $u$ nema susjednog vrha visine manje od $u$, mijenjamo visinu vrha $u$ (relabel, ponovno označavanje).

#### Funkcija visine[^note2]

Precizno, push-relabel održava preslikavanje $h:V\to \mathbf{N}$ takvo da:

-   $h(s)=|V|,h(t)=0$
-   $\forall (u,v)\in E_f,h(u)\leq h(v)+1$

Takav $h$ zovemo funkcijom visine rezidualne mreže $G_f=(V_f,E_f)$.

Lema 1: neka je $h$ funkcija visine na $G_f$; za bilo koja dva vrha $u,v\in V$, ako je $h(u)>h(v)+1$, onda $(u,v)$ nije brid u $G_f$.

Algoritam guranje izvodi samo na bridovima s $h(u)=h(v)+1$.

#### Guranje (push)

Uvjet primjene: vrh $u$ prelijeva i postoji vrh $v((u,v)\in E_f,c(u,v)-f(u,v)>0,h(u)=h(v)+1)$; tada je operacija push primjenjiva na $(u,v)$.

Tada što više viška toka guramo iz $u$ u $v$; pri guranju nas zanima samo manja od vrijednosti viška toka i $c(u,v)-f(u,v)$, a ne zanima nas prelijeva li $v$.

Ako je $(u,v)$ nakon guranja zasićen, brišemo ga iz rezidualne mreže.

#### Ponovno označavanje (relabel)

Uvjet primjene: ako vrh $u$ prelijeva i $\forall (u,v)\in E_f,h(u)\leq h(v)$, operacija relabel primjenjiva je na $u$.

Tada $h(u)$ postavimo na $\min_{(u,v)\in E_f}h(v)+1$.

#### Inicijalizacija

$$
\forall (u,v)\in E,~~f(u,v)=\begin{cases}
c(u,v),&u=s\\
0,&u\neq s
\end{cases}
$$

$$
\forall u\in V,~~h(u)=\begin{cases}
|V|,&u=s\\
0,&u\neq s
\end{cases}
$$

$$
e(u)=\sum_{(x,u)\in E}f(x,u)-\sum_{(u,y)\in E}f(u,y)
$$

Gore smo bridove $(s,v)\in E$ napunili tokom i podigli $h(s)$ tako da $(s,v)\notin E_f$, jer je $h(s)>h(v)$, a $(s,v)$ je ionako zasićen pa ga nema smisla ostaviti u rezidualnoj mreži; također smo $e(s)$ inicijalizirali na suprotnu vrijednost od $\sum_{(s,v)\in E}f(s,v)$.

#### Postupak

Svaki put prolazimo cijeli graf i čim postoji vrh $u$ koji zadovoljava uvjet za push ili relabel, izvodimo odgovarajuću operaciju.

Na slici sredina svakog vrha prikazuje indeks, dolje lijevo visinu $h(u)$, dolje desno višak toka $e(u)$; tamnija boja vrha označava i veću visinu; težina brida označava $c(u,v)-f(u,v)$, a zeleni bridovi su bridovi $(u,v)$ koji zadovoljavaju $h(u)=h(v)+1$ (tj. bridovi rezidualne mreže $E_f$):

![p1](./images/2148.png)

Pogledajmo ugrubo tijek cijelog algoritma; autor ovdje koristi grubi algoritam, tj. grubo provjerava postoji li prelijevajući vrh i, ako postoji, ažurira ga.

![p2](./images/2149.gif)

Konačni rezultat

![p3](./images/2150.png)

Vidimo da se dio viška toka na kraju vratio u $s$ i da, osim izvora i ponora, nijedan vrh ne prelijeva; tadašnja funkcija toka $f$ zadovoljava očuvanje toka, maksimalni je tok, a vrijednost toka je $e(t)$.

No rad[^ref1] zapravo navodi da se točna vrijednost maksimalnog toka dobiva i ako obrađujemo samo prelijevajuće vrhove visine manje od $n$; međutim, tada na kraju algoritma predtok još ne zadovoljava svojstva funkcije toka pa ne znamo stvarni tok na svakom bridu.

#### Implementacija

???+ note "Ključni kod"
    ```cpp
    constexpr int N = 1e4 + 4, M = 1e5 + 5, INF = 0x3f3f3f3f;
    int n, m, s, t, maxflow, tot;
    int ht[N], ex[N];
    
    void init() {  // inicijalizacija
      for (int i = h[s]; i; i = e[i].nex) {
        const int &v = e[i].t;
        ex[v] = e[i].v, ex[s] -= ex[v], e[i ^ 1].v = e[i].v, e[i].v = 0;
      }
      ht[s] = n;
    }
    
    bool push(int ed) {
      const int &u = e[ed ^ 1].t, &v = e[ed].t;
      int flow = min(ex[u], e[ed].v);
      ex[u] -= flow, ex[v] += flow, e[ed].v -= flow, e[ed ^ 1].v += flow;
      return ex[u];  // ako u i dalje prelijeva, vrati 1
    }
    
    void relabel(int u) {
      ht[u] = INF;
      for (int i = h[u]; i; i = e[i].nex)
        if (e[i].v) ht[u] = min(ht[u], ht[e[i].t]);
      ++ht[u];
    }
    ```

### Algoritam HLPP

Algoritam s najvišom oznakom (Highest Label Preflow Push) u gornjem općem push-relabel algoritmu pri svakom izboru vrha daje prednost prelijevajućem vrhu najveće visine; složenost mu je $O(n^2\sqrt m)$.

#### Postupak

Konkretno, postupak algoritma HLPP je sljedeći:

1.  inicijalizacija (kao u push-relabel algoritmu);
2.  među prelijevajućim vrhovima odaberemo vrh $u$ najveće visine i guramo po svim bridovima po kojima se može gurati;
3.  ako $u$ i dalje prelijeva, ponovno ga označimo i vratimo se na korak 2;
4.  ako nema prelijevajućih vrhova, algoritam završava.

Rad[^ref2] koji testira praktične performanse algoritama za maksimalni tok pokazuje da algoritmi zasnovani na predtoku znatan dio vremena troše na korak ponovnog označavanja. U nastavku su dvije optimizacije iz rada[^ref3] koje znatno smanjuju broj ponovnih označavanja.

#### BFS optimizacija

Gornja granica HLPP-a je $O(n^2\sqrt m)$, ali je u praksi prilično tijesna; možemo optimizirati inicijalizaciju visina. Konkretno, $h(u)$ inicijaliziramo na najkraću udaljenost od $u$ do $t$; posebno, $h(s)=n$.

Tijekom BFS-a usput provjeravamo povezanost grafa i isključujemo slučaj bez rješenja.

#### GAP optimizacija

Uvjet guranja u HLPP-u je $h(u)=h(v)+1$; ako u nekom trenutku algoritma postoji $k$ takav da je broj vrhova s $h(u)=k$ jednak $0$, vrhovi s $h(u)>k$ nikad više neće moći gurnuti višak toka do $t$, pa ga mogu samo vratiti u $s$. Zato im u tom trenutku visinu odmah postavimo na barem $n+1$ da ih što prije gurnemo natrag u $s$ i smanjimo broj ponovnih označavanja.

Sljedeća implementacija koristi pristup iz rada[^ref2]: koristi $N*2-1$ pretinaca `B`, gdje `B[i]` sadrži sve prelijevajuće vrhove trenutne visine $i$. Uključene su obje spomenute optimizacije i obrađuju se samo prelijevajući vrhovi visine manje od $n$.

Vrijedi napomenuti da su pretinci u radu[^ref2] stogovi zasnovani na vezanim listama, dok je zadani spremnik STL-ova `stack` `deque`. Jednostavnim testovima pokazalo se da se `vector`, `deque` i `list` u stvarnom izvođenju na ovom zadatku ne razlikuju bitno u učinkovitosti.

#### Implementacija

??? note "Luogu P4722 [Predložak] Maksimalni tok, pojačana verzija / push-relabel"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <queue>
    #include <stack>
    using namespace std;
    constexpr int N = 1200, M = 120000, INF = 0x3f3f3f3f;
    int n, m, s, t;
    
    struct qxx {
      int nex, t;
      long long v;
    };
    
    qxx e[M * 2 + 1];
    int h[N + 1], cnt = 1;
    
    void add_path(int f, int t, long long v) {
      e[++cnt] = qxx{h[f], t, v}, h[f] = cnt;
    }
    
    void add_flow(int f, int t, long long v) {
      add_path(f, t, v);
      add_path(t, f, 0);
    }
    
    int ht[N + 1];        // visina;
    long long ex[N + 1];  // višak toka;
    int gap[N];           // gap optimizacija. gap[i] je broj vrhova visine i
    stack<int> B[N];      // pretinac B[i] sadrži sve v s ht[v]==i
    int level = 0;        // najveća visina prelijevajućih vrhova
    
    int push(int u) {      // gurni višak toka što više kroz bridove po kojima se može gurati
      bool init = u == s;  // jesmo li u inicijalizaciji
      for (int i = h[u]; i; i = e[i].nex) {
        const int &v = e[i].t;
        const long long &w = e[i].v;
        // pri inicijalizaciji ne gledamo razliku visina 1
        if (!w || (init == false && ht[u] != ht[v] + 1) || ht[v] == INF) continue;
        long long k = init ? w : min(w, ex[u]);
        // uzmi manju od rezidualnog kapaciteta i viška toka; pri inicijalizaciji višak izvora može postati negativan.
        if (v != s && v != t && !ex[v]) B[ht[v]].push(v), level = max(level, ht[v]);
        ex[u] -= k, ex[v] += k, e[i].v -= k, e[i ^ 1].v += k;  // push
        if (!ex[u]) return 0;  // ako je sve gurnuto, vrati se
      }
      return 1;
    }
    
    void relabel(int u) {  // ponovno označavanje (visina)
      ht[u] = INF;
      for (int i = h[u]; i; i = e[i].nex)
        if (e[i].v) ht[u] = min(ht[u], ht[e[i].t]);
      if (++ht[u] < n) {  // obrađuj samo vrhove visine manje od n
        B[ht[u]].push(u);
        level = max(level, ht[u]);
        ++gap[ht[u]];  // nova visina, ažuriraj gap
      }
    }
    
    bool bfs_init() {
      memset(ht, 0x3f, sizeof(ht));
      queue<int> q;
      q.push(t), ht[t] = 0;
      while (q.size()) {  // obrnuti BFS, neposjećene vrhove stavljamo u red
        int u = q.front();
        q.pop();
        for (int i = h[u]; i; i = e[i].nex) {
          const int &v = e[i].t;
          if (e[i ^ 1].v && ht[v] > ht[u] + 1) ht[v] = ht[u] + 1, q.push(v);
        }
      }
      return ht[s] != INF;  // ako graf nije povezan, vrati 0
    }
    
    // odaberi jedan od vrhova trenutno najveće visine; ako više nema prelijevajućih vrhova, vrati 0
    int select() {
      while (level > -1 && B[level].size() == 0) level--;
      return level == -1 ? 0 : B[level].top();
    }
    
    long long hlpp() {            // vraća maksimalni tok
      if (!bfs_init()) return 0;  // graf nije povezan
      memset(gap, 0, sizeof(gap));
      for (int i = 1; i <= n; i++)
        if (ht[i] != INF) gap[ht[i]]++;  // inicijaliziraj gap
      ht[s] = n;
      push(s);  // inicijaliziraj predtok
      int u;
      while ((u = select())) {
        B[level].pop();
        if (push(u)) {  // i dalje prelijeva
          if (!--gap[ht[u]])
            for (int i = 1; i <= n; i++)
              if (i != s && ht[i] > ht[u] && ht[i] < n + 1)
                ht[i] = n + 1;  // vrhovi koje ovdje označavamo s n+1 nisu prelijevajući
          relabel(u);
        }
      }
      return ex[t];
    }
    
    int main() {
      scanf("%d%d%d%d", &n, &m, &s, &t);
      for (int i = 1, u, v, w; i <= m; i++) {
        scanf("%d%d%d", &u, &v, &w);
        add_flow(u, v, w);
      }
      printf("%lld", hlpp());
      return 0;
    }
    ```

Osjetite tijek izvođenja

![HLPP](./images/1152.png)

Pritom je između pic13 i pic14 izveden Relabel(4) i GAP optimizacija.

## Bilješke

[^ref_ek]: <http://pisces.ck.tp.edu.tw/~peng/index.php?action=showfile&file=f6cdf7ef750d7dc79c7d599b942acbaaee86a2e3e>

[^ref_dinic]: <https://people.orie.cornell.edu/dpw/orie633/LectureNotes/lecture9.pdf>

[^ref1]: Cherkassky B V, Goldberg A V. On implementing push-relabel method for the maximum flow problem\[C]//International Conference on Integer Programming and Combinatorial Optimization. Springer, Berlin, Heidelberg, 1995: 157-171.

[^ref2]: Ahuja R K, Kodialam M, Mishra A K, et al. Computational investigations of maximum flow algorithms\[J]. European Journal of Operational Research, 1997, 97(3): 509-542.

[^ref3]: Derigs U, Meier W. Implementing Goldberg's max-flow-algorithm—A computational investigation\[J]. Zeitschrift für Operations Research, 1989, 33(6): 383-403.

[^note1]: U engleskoj literaturi obično se kaže „active”.

[^note2]: U engleskoj literaturi visina vrha obično se zove „distance label”. Ovdje korišteni naziv „visina” potječe iz odgovarajućeg poglavlja knjige Introduction to Algorithms. Razlog za to možete naći u fusnoti na str. 432 kineskog izdanja (izvorno 3. izdanje, izdavač China Machine Press).
