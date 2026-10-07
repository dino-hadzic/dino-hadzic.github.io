---
title: Pojmovi iz teorije grafova
---

Ova stranica daje pregled nekih pojmova iz teorije grafova. Ti pojmovi nisu svi uobičajeni u natjecateljskom programiranju; natjecateljima je dovoljno savladati osnovni dio ove stranice, a ako tijekom učenja naiđu na nepoznat pojam, mogu se vratiti i potražiti ga ovdje.

??? warning "Upozorenje"
    Definicije iz teorije grafova često se razlikuju od udžbenika do udžbenika; kad na njih naiđete, procijenite ih prema kontekstu.

## Graf

**Graf (graph)** je uređeni par $G=(V(G), E(G))$. Pri tome je $V(G)$ neprazan skup koji nazivamo **skup vrhova (vertex set)**; svaki element skupa $V$ nazivamo **vrh (vertex)** ili **čvor (node)**, kratko **vrh**. $E(G)$ je skup bridova među vrhovima iz $V(G)$ i naziva se **skup bridova (edge set)**.

Graf obično označavamo s $G=(V,E)$.

Ako su $V$ i $E$ konačni skupovi, $G$ nazivamo **konačnim grafom**.

Ako je $V$ ili $E$ beskonačan skup, $G$ nazivamo **beskonačnim grafom**.

Postoji više vrsta grafova, među ostalim **neusmjereni graf (undirected graph)**, **usmjereni graf (directed graph)**, **mješoviti graf (mixed graph)** itd.

Ako je $G$ neusmjeren graf, svaki je element skupa $E$ neuređeni par $(u, v)$ koji nazivamo **neusmjereni brid (undirected edge)**, kratko **brid (edge)**, gdje je $u, v \in V$. Ako je $e = (u, v)$, tada $u$ i $v$ nazivamo **krajevima (endpoint)** brida $e$.

Ako je $G$ usmjeren graf, svaki je element skupa $E$ uređeni par $(u, v)$, koji se ponekad piše i $u \to v$, a nazivamo ga **usmjereni brid (directed edge)** ili **luk (arc)**; kad nema opasnosti od zabune, može se zvati i **brid (edge)**. Ako je $e = u \to v$, tada $u$ nazivamo **početkom (tail)** brida $e$, a $v$ **krajem (head)** brida $e$; početak i kraj zajedno nazivamo i **krajevima (endpoint)** brida $e$. Kažemo i da je $u$ izravni prethodnik od $v$, a $v$ izravni sljedbenik od $u$.

???+ note "Zašto se početak zove tail, a kraj head?"
    Bridovi se obično crtaju kao strelice, a strelica pokazuje od „repa” (tail) prema „glavi” (head).

Ako je $G$ mješoviti graf, u $E$ postoje i **usmjereni** i **neusmjereni bridovi**.

Ako je svakom bridu $e_k=(u_k,v_k)$ grafa $G$ pridružen broj kao njegova **težina**, $G$ nazivamo **težinskim grafom**. Ako su sve te težine pozitivni realni brojevi, $G$ nazivamo **grafom s pozitivnim težinama**.

Broj vrhova $\left| V(G) \right|$ grafa $G$ naziva se i **red (order)** grafa $G$.

Slikovito rečeno, graf se sastoji od nekoliko vrhova i bridova koji spajaju parove vrhova.

## Susjedstvo

U neusmjerenom grafu $G = (V, E)$, ako je vrh $v$ jedan od krajeva brida $e$, kažemo da su $v$ i $e$ **incidentni (incident)** ili **susjedni (adjacent)**. Za dva vrha $u$ i $v$, ako postoji brid $(u, v)$, kažemo da su $u$ i $v$ **susjedni (adjacent)**.

**Okolina (neighborhood)** vrha $v \in V$ skup je svih vrhova susjednih s $v$; označava se $N(v)$.

Okolina skupa vrhova $S$ skup je svih vrhova susjednih s barem jednim vrhom iz $S$; označava se $N(S)$, tj.:

$$
N(S) = \bigcup_{v \in S} N(v)
$$

## Jednostavni graf

**Petlja (loop)**: za brid $e = (u, v)$ iz $E$, ako je $u = v$, brid $e$ naziva se petlja.

**Višestruki bridovi (multiple edge)**: ako u $E$ postoje dva potpuno jednaka elementa (brida) $e_1, e_2$, nazivamo ih (parom) višestrukih bridova.

**Jednostavni graf (simple graph)**: graf bez petlji i višestrukih bridova naziva se jednostavni graf. U jednostavnom neusmjerenom grafu s barem dva vrha sigurno postoje vrhovi istog stupnja. ([Dirichletov princip](../math/combinatorics/drawer-principle.md))

Ako graf sadrži petlje ili višestruke bridove, naziva se **multigraf (multigraph)**.

??? warning "Upozorenje"
    U neusmjerenom grafu $(u, v)$ i $(v, u)$ čine par višestrukih bridova, dok u usmjerenom grafu $u \to v$ i $v \to u$ nisu višestruki bridovi.

??? warning "Upozorenje"
    U zadatcima, ako nije posebno rečeno, petlje i višestruki bridovi mogu postojati, pa pri rješavanju na to treba posebno paziti.

## Stupanj

Broj bridova incidentnih s vrhom $v$ naziva se **stupanj (degree)** tog vrha i označava $d(v)$. Posebno, svaki brid oblika $(v, v)$ pridonosi $2$ stupnju $d(v)$.

Za neusmjereni jednostavni graf vrijedi $d(v) = \left| N(v) \right|$.

Lema o rukovanju (također osnovni teorem teorije grafova): za svaki neusmjereni graf $G = (V, E)$ vrijedi $\sum_{v \in V} d(v) = 2 \left| E \right|$.

Korolar: u svakom grafu broj vrhova neparnog stupnja je paran.

Ako je $d(v) = 0$, $v$ nazivamo **izoliranim vrhom (isolated vertex)**.

Ako je $d(v) = 1$, $v$ nazivamo **listom (leaf vertex)**/**visećim vrhom (pendant vertex)**.

Ako $2 \mid d(v)$, $v$ nazivamo **parnim vrhom (even vertex)**.

Ako $2 \nmid d(v)$, $v$ nazivamo **neparnim vrhom (odd vertex)**. Broj neparnih vrhova u grafu je paran.

Ako je $d(v) = \left| V \right| - 1$, $v$ nazivamo **univerzalnim vrhom (universal vertex)**.

Za graf, najmanji stupanj među svim vrhovima naziva se **minimalni stupanj (minimum degree)** grafa $G$ i označava $\delta (G)$; najveći se naziva **maksimalni stupanj (maximum degree)** i označava $\Delta (G)$. Dakle: $\delta (G) = \min_{v \in G} d(v)$, $\Delta (G) = \max_{v \in G} d(v)$.

U usmjerenom grafu $G = (V, E)$ broj bridova koji počinju u vrhu $v$ naziva se **izlazni stupanj (out-degree)** tog vrha i označava $d^+(v)$. Broj bridova koji završavaju u vrhu $v$ naziva se **ulazni stupanj (in-degree)** tog vrha i označava $d^-(v)$. Očito je $d^+(v)+d^-(v)=d(v)$.

Za svaki usmjereni graf $G = (V, E)$ vrijedi:

$$
\sum_{v \in V} d^+(v) = \sum_{v \in V} d^-(v) = \left| E \right|
$$

Ako u neusmjerenom grafu $G = (V, E)$ svaki vrh ima stupanj jednak fiksnoj konstanti $k$, $G$ nazivamo **$k$-regularnim grafom ($k$-regular graph)**.

Ako za zadani niz a postoji graf G čiji je niz stupnjeva upravo a, kažemo da je a **grafički**.

Ako za zadani niz a postoji jednostavni graf G čiji je niz stupnjeva upravo a, kažemo da je a **jednostavno grafički**.

## Putevi

**Šetnja (walk)**: šetnja je niz bridova koji spajaju niz vrhova; može biti konačne ili beskonačne duljine. Formalno, konačna šetnja $w$ niz je bridova $e_1, e_2, \ldots, e_k$ za koji postoji niz vrhova $v_0, v_1, \ldots, v_k$ takav da je $e_i = (v_{i-1}, v_i)$ za $i \in [1, k]$. Takvu šetnju kraće zapisujemo $v_0 \to v_1 \to v_2 \to \cdots \to v_k$. Obično se broj bridova $k$ naziva **duljinom** šetnje (ako bridovi imaju težine, duljina obično označava zbroj težina bridova na šetnji, a zadatci mogu imati i drugačije definicije).

**Staza (trail)**: šetnja $w$ u kojoj su $e_1, e_2, \ldots, e_k$ međusobno različiti naziva se staza.

**Put (path)** (naziva se i **jednostavni put (simple path)**): staza $w$ u kojoj su svi vrhovi u nizu vrhova međusobno različiti naziva se put.

**Zatvorena staza (circuit)**: staza $w$ za koju je $v_0 = v_k$ naziva se zatvorena staza.

**Ciklus (cycle)** (naziva se i **jednostavni ciklus (simple circuit)**): zatvorena staza $w$ u kojoj je $v_0 = v_k$ jedini par vrhova koji se ponavlja u nizu vrhova naziva se ciklus.

??? warning "Upozorenje"
    Definicije puteva mogu se razlikovati ovisno o izvoru; npr. „put” može označavati ono što je ovdje „šetnja”, a „ciklus” ono što je ovdje „zatvorena staza”. Ako u zadatku vidite takve riječi bez posebne napomene poput „jednostavni put”/„put koji nije nužno jednostavan” (tj. ovdje „šetnja”), najbolje je pitati što se točno misli.

## Podgraf

Za graf $G = (V, E)$, ako postoji graf $H = (V', E')$ takav da je $V' \subseteq V$ i $E' \subseteq E$, kažemo da je $H$ **podgraf (subgraph)** grafa $G$ i pišemo $H \subseteq G$.

Ako za $H \subseteq G$ vrijedi da za sve $u, v \in V'$, kad god je $(u, v) \in E$, vrijedi i $(u, v) \in E'$, kažemo da je $H$ **inducirani podgraf (induced subgraph)** grafa $G$.

Lako se vidi da je inducirani podgraf određen samo skupom vrhova podgrafa, pa se inducirani podgraf sa skupom vrhova $V'$ ($V' \subseteq V$) naziva podgrafom induciranim skupom $V'$ i označava $G \left[ V' \right]$.

Ako $H \subseteq G$ zadovoljava $V' = V$, $H$ nazivamo **razapinjućim podgrafom (spanning subgraph)** grafa $G$.

Očito je $G$ sam svoj podgraf, razapinjući podgraf i inducirani podgraf; [graf bez bridova](#posebni-grafovi) razapinjući je podgraf grafa $G$. Izvorni graf $G$ i graf bez bridova trivijalni su podgrafovi grafa $G$.

Ako je neki razapinjući podgraf $F$ neusmjerenog grafa $G$ $k$-regularan graf, $F$ nazivamo **$k$-faktorom ($k$-factor)** grafa $G$.

Ako inducirani podgraf $H = G \left[ V^\ast \right]$ usmjerenog grafa $G = (V, E)$ zadovoljava: za sve $v \in V^\ast$, $(v, u) \in E$ povlači $u \in V^\ast$, tada $H$ nazivamo **zatvorenim podgrafom (closed subgraph)** grafa $G$.

## Povezanost

### Neusmjereni grafovi

U neusmjerenom grafu $G = (V, E)$, za $u, v \in V$, ako postoji šetnja takva da je $v_0 = u, v_k = v$, kažemo da su $u$ i $v$ **povezani (connected)**. Po definiciji je svaki vrh povezan sam sa sobom, a oba kraja svakog brida međusobno su povezana.

Ako su u neusmjerenom grafu $G = (V, E)$ svaka dva vrha povezana, $G$ nazivamo **povezanim grafom (connected graph)**, a to svojstvo grafa $G$ **povezanošću (connectivity)**.

Ako je $H$ povezani podgraf grafa $G$ i ne postoji $F$ takav da je $H\subsetneq F \subseteq G$ i da je $F$ povezan graf, tada je $H$ **komponenta povezanosti (connected component)** grafa $G$ (maksimalni povezani podgraf).

### Usmjereni grafovi

U usmjerenom grafu $G = (V, E)$, za $u, v \in V$, ako postoji šetnja takva da je $v_0 = u, v_k = v$, kažemo da je $v$ **dostižan** iz $u$. Po definiciji je svaki vrh dostižan iz samoga sebe, a kraj svakog brida dostižan je iz njegova početka. (Povezanost u neusmjerenom grafu može se shvatiti kao dostižnost u oba smjera.)

Ako su u usmjerenom grafu svaka dva vrha međusobno dostižna, graf nazivamo **jako povezanim (strongly connected)**.

Ako zamjenom bridova usmjerenog grafa neusmjerenima dobivamo povezan graf, izvorni usmjereni graf nazivamo **slabo povezanim (weakly connected)**.

Slično komponentama povezanosti postoje i **slabo povezane komponente (weakly connected component)** (maksimalni slabo povezani podgrafovi) i **jako povezane komponente (strongly connected component)** (maksimalni jako povezani podgrafovi).

Za odgovarajuće algoritme vidi [Jako povezane komponente](./scc.md).

### Rezovi

Za odgovarajuće algoritme vidi [Artikulacijski vrhovi i mostovi](./cut.md) te [Dvostruko povezane komponente](./bcc.md).

U ovom dijelu „povezan” za usmjereni graf obično znači „jako povezan”.

Za povezani graf $G = (V, E)$, ako je $V'\subseteq V$ i $G\left[V\setminus V'\right]$ (tj. graf $G$ bez vrhova iz $V'$) nije povezan graf, tada je $V'$ **vršni rez (vertex cut/separating set)** grafa $G$. Vršni rez veličine jedan naziva se i **artikulacijski vrh (cut vertex)**.

Za povezani graf $G = (V, E)$ i cijeli broj $k$, ako je $|V|\ge k+1$ i $G$ nema vršni rez veličine $k-1$, kažemo da je graf $G$ **$k$-vršno povezan ($k$-vertex-connected)**, a najveći $k$ za koji to vrijedi naziva se **vršna povezanost (vertex connectivity)** grafa $G$ i označava $\kappa(G)$. (Za grafove koji nisu potpuni vršna povezanost jednaka je veličini najmanjeg vršnog reza, a vršna povezanost potpunog grafa $K_n$ iznosi $n-1$.)

Za graf $G = (V, E)$ i $u, v\in V$ takve da je $u\ne v$, $u$ i $v$ nisu susjedni i $v$ je dostižan iz $u$, ako je $V'\subseteq V$, $u, v\notin V'$ i u $G\left[V\setminus V'\right]$ vrhovi $u$ i $v$ nisu povezani, tada $V'$ nazivamo vršnim rezom između $u$ i $v$. Veličina najmanjeg vršnog reza između $u$ i $v$ naziva se **lokalna vršna povezanost (local connectivity)** između $u$ i $v$ i označava $\kappa(u, v)$.

Slične se definicije mogu dati i za bridove:

Za povezani graf $G = (V, E)$, ako je $E'\subseteq E$ i $G' = (V, E\setminus E')$ (tj. graf $G$ bez bridova iz $E'$) nije povezan graf, tada je $E'$ **bridni rez (edge cut)** grafa $G$. Bridni rez veličine jedan naziva se i **most (bridge)**.

Za povezani graf $G = (V, E)$ i cijeli broj $k$, ako $G$ nema bridni rez veličine $k-1$, kažemo da je graf $G$ **$k$-bridno povezan ($k$-edge-connected)**, a najveći $k$ za koji to vrijedi naziva se **bridna povezanost (edge connectivity)** grafa $G$ i označava $\lambda(G)$. (Za svaki graf bridna povezanost jednaka je veličini najmanjeg bridnog reza.)

Za graf $G = (V, E)$ i $u, v\in V$ takve da je $u\ne v$ i $v$ je dostižan iz $u$, ako je $E'\subseteq E$ i u $G'=(V, E\setminus E')$ vrhovi $u$ i $v$ nisu povezani, tada $E'$ nazivamo bridnim rezom između $u$ i $v$. Veličina najmanjeg bridnog reza između $u$ i $v$ naziva se **lokalna bridna povezanost (local edge-connectivity)** između $u$ i $v$ i označava $\lambda(u, v)$.

**Vršna dvostruka povezanost (biconnected)** gotovo se u potpunosti podudara s $2$-vršnom povezanošću, osim za graf koji se sastoji od jednog brida s dva vrha: on je vršno dvostruko povezan, ali nije $2$-vršno povezan. Drugim riječima, povezani graf bez artikulacijskih vrhova vršno je dvostruko povezan.

**Bridna dvostruka povezanost ($2$-edge-connected)** potpuno se podudara s $2$-bridnom povezanošću. Drugim riječima, povezani graf bez mostova bridno je dvostruko povezan.

Slično komponentama povezanosti postoje i **vršno dvostruko povezane komponente (biconnected component)** (maksimalni vršno dvostruko povezani podgrafovi) i **bridno dvostruko povezane komponente ($2$-edge-connected component)** (maksimalni bridno dvostruko povezani podgrafovi).

**Whitneyjev teorem**: za svaki graf $G$ vrijedi $\kappa(G)\le \lambda(G)\le \delta(G)$. (Tri člana nejednakosti redom su vršna povezanost, bridna povezanost i minimalni stupanj.)

## Rijetki/gusti grafovi

Ako je broj bridova grafa mnogo manji od kvadrata broja vrhova, graf je **rijedak (sparse graph)**.

Ako je broj bridova grafa blizu kvadratu broja vrhova, graf je **gust (dense graph)**.

Ta dva pojma nemaju strogu definiciju; obično se koriste pri raspravi o razlici u učinkovitosti algoritama [vremenske složenosti](../basic/complexity.md) $O(|V|^2)$ i algoritama složenosti $O(|E|)$ (na gustim grafovima ta su dva algoritma podjednako učinkovita, dok je na rijetkim grafovima algoritam složenosti $O(|E|)$ znatno učinkovitiji).

## Komplement grafa

Za neusmjereni jednostavni graf $G = (V, E)$ njegov **komplement (complement graph)** graf je, označen $\bar G$, za koji vrijedi $V \left( \bar G \right) = V \left( G \right)$ i za svaki par vrhova $(u, v)$ vrijedi $(u, v) \in E \left( \bar G \right)$ ako i samo ako $(u, v) \notin E \left( G \right)$.

## Obrnuti graf

Za usmjereni graf $G = (V, E)$ njegov **obrnuti graf (transpose graph)** graf je s istim skupom vrhova u kojem je svakom bridu obrnut smjer, tj.: ako je obrnuti graf grafa $G$ graf $G'=(V, E')$, tada je $E'=\{(v, u)|(u, v)\in E\}$.

## Posebni grafovi

Ako u neusmjerenom jednostavnom grafu $G$ između svaka dva različita vrha postoji brid, $G$ nazivamo **potpunim grafom (complete graph)**; potpuni graf reda $n$ označava se $K_n$. Ako u usmjerenom grafu $G$ između svaka dva različita vrha postoje dva brida suprotnih smjerova, $G$ nazivamo **potpunim usmjerenim grafom (complete digraph)**.

Graf s praznim skupom bridova naziva se **graf bez bridova (edgeless graph)**, **prazni graf (empty graph)** ili **nul-graf (null graph)**; graf bez bridova reda $n$ označava se $\overline{K}_n$ ili $N_n$. $N_n$ i $K_n$ međusobno su komplementi.

??? warning "Upozorenje"
    **Nul-graf (null graph)** može označavati i **graf reda nula (order-zero graph)** $K_0$, tj. graf s praznim skupom vrhova i praznim skupom bridova.

Ako u usmjerenom jednostavnom grafu $G$ između svaka dva različita vrha postoji točno jedan brid (u jednom smjeru), $G$ nazivamo **turnirom (tournament graph)**.

Ako svi bridovi neusmjerenog jednostavnog grafa $G = \left( V, E \right)$ čine točno jedan ciklus, $G$ nazivamo **cikličkim grafom (cycle graph)**; ciklički graf reda $n$ ($n \geq 3$) označava se $C_n$. Lako se vidi da je graf ciklički ako i samo ako je $2$-regularan povezan graf.

Ako u neusmjerenom jednostavnom grafu $G = \left( V, E \right)$ postoji univerzalni vrh $v$, a između ostalih vrhova nema bridova, $G$ nazivamo **zvijezdom (star graph)**; zvijezda reda $n + 1$ ($n \geq 1$) označava se $S_n$.

Ako u neusmjerenom jednostavnom grafu $G = \left( V, E \right)$ postoji univerzalni vrh $v$, a ostali vrhovi čine ciklus, $G$ nazivamo **kotačem (wheel graph)**; kotač reda $n + 1$ ($n \geq 3$) označava se $W_n$.

Ako svi bridovi neusmjerenog jednostavnog grafa $G = \left( V, E \right)$ čine točno jedan jednostavni put, $G$ nazivamo **lancem (chain/path graph)**; lanac reda $n$ označava se $P_n$. Lako se vidi da se lanac dobiva iz cikličkog grafa brisanjem jednog brida.

Ako neusmjereni povezani graf ne sadrži ciklus, nazivamo ga **stablom (tree)**. Više o tome u [Osnove stabala](./tree-basic.md).

Ako neusmjereni povezani graf sadrži točno jedan ciklus, nazivamo ga **pseudostablom (pseudotree)**.

Ako u usmjerenom slabo povezanom grafu svaki vrh ima ulazni stupanj $1$, nazivamo ga **pseudostablom usmjerenim prema van**.

Ako u usmjerenom slabo povezanom grafu svaki vrh ima izlazni stupanj $1$, nazivamo ga **pseudostablom usmjerenim prema unutra**.

Više stabala čini **šumu (forest)**, više pseudostabala čini **pseudošumu (pseudoforest)**, više pseudostabala usmjerenih prema van čini **šumu pseudostabala usmjerenih prema van**, a više pseudostabala usmjerenih prema unutra čini **šumu pseudostabala usmjerenih prema unutra (functional graph)**.

Ako je u neusmjerenom povezanom grafu svaki brid u najviše jednom ciklusu, nazivamo ga **kaktusom (cactus)**. Više kaktusa čini **pustinju**.

Ako se skup vrhova grafa može podijeliti na dva dijela tako da unutar nijednog dijela nema bridova, graf je **bipartitan (bipartite graph)**. Ako u bipartitnom grafu između svaka dva vrha iz različitih dijelova postoji brid, graf je **potpuni bipartitni graf (complete bipartite graph/biclique)**; potpuni bipartitni graf čiji dijelovi imaju $n$ odnosno $m$ vrhova označava se $K_{n, m}$. Više o tome u [Bipartitni grafovi](./bi-graph.md).

Ako se graf može nacrtati u ravnini tako da se nikoja dva brida ne sijeku izvan krajeva, graf je **planaran (planar graph)**. Za jednostavni povezani planarni graf $G=(V, E)$ s $V\ge 3$ vrijedi $|E|\le 3|V|-6$.  
**Kuratowskijev teorem**: graf je planaran ako i samo ako nema podgraf **homeomorfan (homeomorphism)** grafu $K_5$ ili $K_{3, 3}$. Pri tome su grafovi $G$ i $G'$ homeomorfni ako se oba mogu dodavanjem nekoliko vrhova stupnja $2$ na bridove[^ref1] pretvoriti u isti graf.

## Izomorfizam

Za dva grafa $G$ i $H$, ako postoji bijekcija $f : V(G) \to V(H)$ takva da je $(u,v)\in E(G)$ ako i samo ako $(f(u),f(v))\in E(H)$, $f$ nazivamo **izomorfizmom (isomorphism)** iz $G$ u $H$, a grafovi $G$ i $H$ su **izomorfni (isomorphic)**, što pišemo $G \cong H$.

Iz definicije slijedi da ako je $G \cong H$, mora vrijediti:

-   $|V(G)|=|V(H)|,|E(G)|=|E(H)|$
-   $G$ i $H$ imaju jednake nerastuće nizove stupnjeva vrhova
-   $G$ i $H$ imaju izomorfne inducirane podgrafove

## Binarne operacije na neusmjerenim jednostavnim grafovima

Za neusmjerene jednostavne grafove možemo definirati sljedeće binarne operacije:

**Presjek (intersection)**: presjek grafova $G = \left( V_1, E_1 \right), H = \left( V_2, E_2 \right)$ definira se kao graf $G \cap H = \left( V_1 \cap V_2, E_1 \cap E_2 \right)$.

Lako se dokazuje da je presjek dvaju neusmjerenih jednostavnih grafova opet neusmjereni jednostavni graf.

**Unija (union)**: unija grafova $G = \left( V_1, E_1 \right), H = \left( V_2, E_2 \right)$ definira se kao graf $G \cup H = \left( V_1 \cup V_2, E_1 \cup E_2 \right)$.

**Zbroj (sum)/direktni zbroj (direct sum)**: za $G = \left( V_1, E_1 \right), H = \left( V_2, E_2 \right)$ konstruiramo proizvoljni $H' \cong H$ takav da je $V \left( H' \right) \cap V_1 = \varnothing$ ($H'$ može biti jednak $H$). Tada se svaki graf izomorfan s $G \cup H'$ naziva zbrojem/direktnim zbrojem/disjunktnom unijom grafova $G$ i $H$ i označava $G + H$ ili $G \oplus H$.

Ako su skupovi vrhova grafova $G$ i $H$ disjunktni, tada je $G \cup H = G + H$.

Primjerice, šuma se može definirati kao zbroj nekoliko stabala.

???+ note "Razlika između unije i zbroja"
    Može se shvatiti ovako: „unija” spaja vrhove i bridove „istog imena” iz oba grafa, dok ih „zbroj” ne spaja.

## Posebni skupovi vrhova/bridova

### Dominirajući skup

Za neusmjereni graf $G=(V, E)$, ako je $V'\subseteq V$ i za svaki $v\in(V\setminus V')$ postoji brid $(u, v)\in E$ takav da je $u\in V'$, tada je $V'$ **dominirajući skup (dominating set)** grafa $G$.

Veličina najmanjeg dominirajućeg skupa neusmjerenog grafa $G$ označava se $\gamma(G)$. Nalaženje najmanjeg dominirajućeg skupa grafa je [NP-teško](../misc/cc-basic.md#np-hard).

Za usmjereni graf $G=(V, E)$, ako je $V'\subseteq V$ i za svaki $v\in(V\setminus V')$ postoji brid $(u, v)\in E$ takav da je $u\in V'$, tada je $V'$ **izlazni dominirajući skup (out-dominating set)** grafa $G$. Slično se definira **ulazni dominirajući skup (in-dominating set)** usmjerenog grafa.

Veličina najmanjeg izlaznog dominirajućeg skupa usmjerenog grafa $G$ označava se $\gamma^+(G)$, a najmanjeg ulaznog dominirajućeg skupa $\gamma^-(G)$.

### Bridni dominirajući skup

Za graf $G=(V, E)$, ako je $E'\subseteq E$ i za svaki $e\in(E\setminus E')$ postoji brid iz $E'$ koji s njim ima zajednički vrh, $E'$ nazivamo **bridnim dominirajućim skupom (edge dominating set)** grafa $G$.

Nalaženje najmanjeg bridnog dominirajućeg skupa grafa je [NP-teško](../misc/cc-basic.md#np-hard).

### Nezavisni skup

Za graf $G=(V, E)$, ako je $V'\subseteq V$ i nikoja dva vrha iz $V'$ nisu susjedna, tada je $V'$ **nezavisni skup (independent set)** grafa $G$.

Veličina najvećeg nezavisnog skupa grafa $G$ označava se $\alpha(G)$. Nalaženje najvećeg nezavisnog skupa grafa je [NP-teško](../misc/cc-basic.md#np-hard).

### Sparivanje

Za graf $G=(V, E)$, ako je $E'\subseteq E$, nikoja dva različita brida iz $E'$ nemaju zajednički kraj i nijedan brid iz $E'$ nije petlja, tada je $E'$ **sparivanje (matching)** grafa $G$, koje se može zvati i **nezavisni skup bridova (independent edge set)**. Ako je vrh kraj nekog brida iz sparivanja, kažemo da je **spareni (matched)/zasićeni (saturated)**, a inače da je **nespareni (unmatched)**.

Sparivanje s najvećim brojem bridova naziva se **najveće sparivanje (maximum-cardinality matching)** grafa. Veličina najvećeg sparivanja grafa $G$ označava se $\nu(G)$.

Ako bridovi imaju težine, sparivanje s najvećim zbrojem težina naziva se **sparivanje najveće težine (maximum-weight matching)** grafa.

Ako sparivanje nakon dodavanja bilo kojeg brida više nije sparivanje, ono je **maksimalno sparivanje (maximal matching)**. Najveće maksimalno sparivanje je najveće sparivanje, a svako najveće sparivanje je maksimalno. Maksimalno sparivanje sigurno je bridni dominirajući skup, ali bridni dominirajući skup nije nužno sparivanje. Najmanje maksimalno sparivanje i najmanji bridni dominirajući skup iste su veličine, ali najmanji bridni dominirajući skup nije nužno sparivanje. Nalaženje najmanjeg maksimalnog sparivanja je NP-teško.

Ako su u sparivanju svi vrhovi spareni, ono je **savršeno sparivanje (perfect matching)**. Ako je u sparivanju samo jedan vrh nesparen, ono je **gotovo savršeno sparivanje (near-perfect matching)**.

Brojanje sparivanja ili savršenih sparivanja općeg ili bipartitnog grafa je [#P-potpuno](../misc/cc-basic.md#p_1).

Za sparivanje $M$, ako put počinje u nesparenom vrhu i od svaka dva susjedna brida jedan pripada sparivanju, a drugi ne, taj se put naziva **alternirajući put (alternating path)**; alternirajući put koji završava u nesparenom vrhu naziva se **uvećavajući put (augmenting path)**.

**Tutteov teorem**: neusmjereni graf $G$ reda $n$ ima savršeno sparivanje ako i samo ako za svaki $V' \subset V(G)$ vrijedi $p_{\text{odd}}(G-V')\leq |V'|$, gdje $p_{\text{odd}}$ označava broj komponenata povezanosti neparnog reda.

**Tutteov teorem (korolar)**: svaki 3-regularni graf bez mostova ima savršeno sparivanje.

### Vršni pokrivač

Za graf $G=(V, E)$, ako je $V'\subseteq V$ i svaki $e\in E$ ima barem jedan kraj u $V'$, $V'$ nazivamo **vršnim pokrivačem (vertex cover)** grafa $G$.

Vršni pokrivač nužno je dominirajući skup, ali minimalni vršni pokrivač nije nužno minimalni dominirajući skup.

Skup vrhova je vršni pokrivač ako i samo ako je njegov komplement nezavisni skup, pa je komplement najmanjeg vršnog pokrivača najveći nezavisni skup. Nalaženje najmanjeg vršnog pokrivača grafa je [NP-teško](../misc/cc-basic.md#np-hard).

Veličina bilo kojeg sparivanja grafa nije veća od veličine bilo kojeg njegova vršnog pokrivača. U potpunom bipartitnom grafu $K_{n, m}$ veličina najvećeg sparivanja i najmanjeg vršnog pokrivača jednaka je $\min(n, m)$.

### Bridni pokrivač

Za graf $G=(V, E)$, ako je $E'\subseteq E$ i svaki $v\in V$ susjedan je s barem jednim bridom iz $E'$, $E'$ nazivamo **bridnim pokrivačem (edge cover)** grafa $G$.

Veličina najmanjeg bridnog pokrivača označava se $\rho(G)$ i može se dobiti greedy proširenjem najvećeg sparivanja: za svaki nespareni vrh dodamo jedan njegov susjedni brid u najveće sparivanje i dobivamo najmanji bridni pokrivač.

Najveće sparivanje može se dobiti i iz najmanjeg bridnog pokrivača: za svaki par bridova iz najmanjeg bridnog pokrivača sa zajedničkim vrhom izbrišemo jedan od njih.

Veličina najmanjeg bridnog pokrivača grafa plus veličina najvećeg sparivanja jednaka je broju vrhova grafa, tj. $\rho(G)+\nu(G)=|V(G)|$.

Veličina najvećeg sparivanja grafa nije veća od veličine najmanjeg bridnog pokrivača, tj. $\nu(G)\le\rho(G)$. Posebno, savršeno sparivanje sigurno je najmanji bridni pokrivač, i to je jedini slučaj u kojem gornja nejednakost postaje jednakost.

Veličina bilo kojeg nezavisnog skupa grafa nije veća od veličine bilo kojeg njegova bridnog pokrivača. U potpunom bipartitnom grafu $K_{n, m}$ veličina najvećeg nezavisnog skupa i najmanjeg bridnog pokrivača jednaka je $\max(n, m)$.

### Klika

Za graf $G=(V, E)$, ako je $V'\subseteq V$ i svaka dva različita vrha iz $V'$ su susjedna, tada je $V'$ **klika (clique)** grafa $G$. Podgraf induciran klikom je potpuni graf.

Ako klika nakon dodavanja bilo kojeg vrha više nije klika, ona je **maksimalna klika (maximal clique)**.

Veličina najveće klike grafa označava se $\omega(G)$; veličina najveće klike jednaka je veličini najvećeg nezavisnog skupa komplementa, tj. $\omega(G)=\alpha(\bar{G})$. Nalaženje najveće klike grafa je [NP-teško](../misc/cc-basic.md#np-hard).

## Literatura

[OI 中转站 - 图论概念梳理](https://yhx-12243.github.io/OI-transit/memos/14.html)

[Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms) (i članci o pojedinim pojmovima)

离散数学（修订版）, 田文成 周禄新 编著, 天津文学出版社, str. 184-187

戴一奇, 胡冠章, 陈卫. 图论与代数结构 \[M]. 北京: 清华大学出版社, 1995.

[^ref1]: Ta se operacija naziva i subdivizija (subdivision).
