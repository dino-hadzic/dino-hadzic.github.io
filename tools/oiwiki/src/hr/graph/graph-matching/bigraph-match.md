---
title: Najveće sparivanje u bipartitnom grafu
---

Potrebno predznanje: [bipartitni graf](../bi-graph.md), [sparivanje u grafu](./graph-match.md)

## Uvod

Ovaj članak obrađuje problem najvećeg sparivanja (maximum matching) u bipartitnom grafu $G=(X,Y,E)$.

Tipičan primjer sparivanja u bipartitnom grafu iz svakodnevnog života jest sparivanje muškaraca i žena. Neka je dano nekoliko muškaraca ($X$) i žena ($Y$); svaka se osoba može spariti najviše jednom, a dopušteni parovi zadani su nekim popisom ($E$). Zadatak algoritma za najveće sparivanje u bipartitnom grafu jest da uz ta ograničenja pronađe najveći broj parova, tako da što više osoba bude uspješno spareno.

???+ info "Napomena"
    U ovom članku pretpostavljamo da je poznata jedna podjela (bojanje) skupa vrhova $V$ bipartitnog grafa: $V=X\cup Y$. Ako podjela skupa vrhova $V$ nije unaprijed poznata, može se naći [algoritmom bojanja bipartitnog grafa](../bi-graph.md#判定) u vremenu $O(|V|+|E|)$.

## Kuhnov algoritam

Kuhnov algoritam izravna je primjena [Bergeove leme](./graph-match.md#berge-引理). On je ujedno i dio [mađarskog algoritma](./bigraph-weight-match.md#mađarski-algoritam-kuhnmunkresov-algoritam).

### Postupak

Da bi pronašao najveće sparivanje, algoritam redom prolazi sve vrhove, pokušava naći uvećavajući put (augmenting path) koji počinje u tom vrhu i uvećava sparivanje duž njega. Budući da je duljina uvećavajućeg puta uvijek neparna, u bipartitnom grafu njegovi krajevi nužno leže u različitim dijelovima. To znači da je dovoljno promatrati samo uvećavajuće putove koji počinju u lijevom dijelu.

Za traženje uvećavajućeg puta bipartitni graf možemo orijentirati prema trenutnom sparivanju $M$. Uvećavajući put (ili bilo koji alternirajući put) koji počinje u nesparenom lijevom vrhu može iz lijevog vrha u desni prijeći samo nesparenim bridom, a iz desnog vrha u lijevi samo sparenim bridom. Stoga možemo odrediti da svi nespareni bridovi pokazuju prema desnim vrhovima, a svi spareni bridovi prema lijevim vrhovima. Problem traženja uvećavajućeg puta tada se svodi na traženje jednostavnog puta u usmjerenom grafu od nekog nesparenog lijevog vrha do nekog nesparenog desnog vrha. Taj se problem lako rješava [DFS-om](../dfs.md) ili [BFS-om](../bfs.md) u vremenu $O(|E|)$.

![](images/bigraph-match-1.svg)

(Na slici su tamni vrhovi spareni, svijetli nespareni, crveni bridovi spareni, crni nespareni, a strelice označavaju orijentaciju prema trenutnom sparivanju. Vidi se da je put $1\rightarrow 8\rightarrow 3\rightarrow 11\rightarrow 6\rightarrow 12$ uvećavajući put u odnosu na trenutno sparivanje.)

Na početku algoritma svi bridovi pokazuju prema desnim vrhovima. Nakon svakog pronađenog uvećavajućeg puta treba sve bridove na njemu okrenuti, čime se označava da im je stanje sparenosti promijenjeno. Na kraju algoritma svi bridovi koji pokazuju prema lijevim vrhovima su spareni bridovi.

Budući da je dovoljno proći $O(|V|)$ lijevih vrhova, [svaki po jednom](./graph-match.md#berge-引理), ukupna vremenska složenost algoritma je $O(|V||E|)$.

### Optimizacije

Postoji nekoliko jednostavnih trikova kojima se smanjuje konstanta Kuhnova algoritma:

1.  Kuhnov algoritam temelji se na Bergeovoj lemi, a ona ne zahtijeva da lijevi i desni dio bipartitnog grafa budu zadani unaprijed. Stoga Kuhnov algoritam radi ispravno i kad dijelovi nisu izričito podijeljeni, dokle god je graf bipartitan. Ipak, obično je učinkovitije najprije obojiti graf i odrediti lijevi i desni dio.
2.  Budući da je vremenska složenost gore opisanog Kuhnova algoritma zapravo $O(|X||E|)$, za lijevi dio $X$ možemo uzeti manji od dvaju dijelova.
3.  Pri traženju uvećavajućeg puta oznake kojima se izbjegava ponovno pretraživanje ne treba brisati prije svakog DFS-a. Prije brisanja oznaka možemo pokušati naći uvećavajući put za sve nesparene lijeve vrhove. U jednom takvom krugu svaki se brid posjećuje najviše jednom, pa je složenost i dalje $O(|E|)$; no u jednom krugu može se pronaći više uvećavajućih putova, pa ukupan broj krugova $k$ ne prelazi $|M|+1$, gdje je $M$ najveće sparivanje. Time se ukupna složenost algoritma smanjuje na $O(k|E|)$.
4.  Pri traženju uvećavajućeg puta prednost dajemo nesparenim desnim vrhovima, jer to znači kraći uvećavajući put.
5.  Budući da Bergeova lema ne zahtijeva da početno sparivanje bude prazno, na početku Kuhnova algoritma možemo nasumično odabrati nekoliko međusobno disjunktnih bridova kao početno sparivanje, da bismo smanjili broj kasnijih pretraživanja. Ako je već primijenjena optimizacija 3, ovu optimizaciju možemo zanemariti.

Iako je najgora složenost i dalje $O(|V||E|)$, dobro optimiziran Kuhnov algoritam nije loše učinkovit. Ipak, da pojedini testni podaci ne bi izazvali najgori slučaj, prije sparivanja treba nasumično promiješati redoslijed bridova ili vrhova.

### Referentna implementacija

U implementaciji nije potrebno zaista održavati orijentaciju; dovoljno je za svaki vrh pamtiti vrh s kojim je sparen.

??? example "Ogledni zadatak [Library Checker - Matching on Bipartite Graph](https://judge.yosupo.jp/problem/bipartitematching)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_1.cpp"
    ```

## Hopcroft–Karpov algoritam

Hopcroft–Karpov algoritam dodatno optimizira način na koji Kuhnov algoritam traži uvećavajuće putove: ukupan broj krugova smanjuje na $O(|V|^{1/2})$ i tako postiže vremensku složenost $O(|V|^{1/2}|E|)$. Taj je algoritam zapravo poseban slučaj [Dinicova algoritma](../flow/max-flow.md#dinic-算法).

### Postupak

Algoritam i dalje traži uvećavajuće putove, ali da bi sparivanje završio u manje krugova, u svakom krugu primjenjuje sljedeću strategiju:

1.  Sparene bridove orijentira prema lijevim vrhovima, a nesparene prema desnim vrhovima.
2.  Iz svih nesparenih lijevih vrhova pokreće BFS na usmjerenom grafu i za svaki posjećeni vrh bilježi sloj $d(v)$ u kojem se nalazi, sve dok se u nekom sloju ne pojavi nespareni desni vrh. Ako BFS završi, a nespareni desni vrh nije pronađen, trenutno sparivanje je već najveće.
3.  Redom iz svakog nesparenog lijevog vrha pokreće DFS, traži uvećavajući put i uvećava sparivanje duž njega. DFS se širi samo bridovima čiji slojevi rastu uzastopno i strogo (tj. $d(v') = d(v) + 1$) i posjećuje samo vrhove koji još nisu posjećeni u DFS-u ovog kruga. Posebno, DFS ne posjećuje vrhove koje prethodni BFS nije dosegnuo.

Rečeno terminologijom mrežnih tokova, korak 2 gradi slojeviti graf (level graph), a korak 3 nalazi blokirajući tok (blocking flow) u slojevitom grafu. Slojeviti graf je graf u kojem svaki brid nužno vodi iz jednog sloja u sljedeći; blokirajući tok je u ovom kontekstu maksimalan skup uvećavajućih putova koji u parovima nemaju zajedničkih vrhova. Skup uvećavajućih putova dobiven u koraku 3 nužno je maksimalan: kad bi postojao još jedan uvećavajući put, bio bi pronađen već u trenutku kad je algoritam obrađivao njegov početni vrh.

U odnosu na prethodno opisani Kuhnov algoritam, ključna je promjena Hopcroft–Karpova algoritma dodavanje koraka izgradnje slojevitog grafa prije traženja blokirajućeg toka. DFS po slojevitom grafu ograničava algoritam na to da do svakog vrha uvijek dolazi najkraćim putem. Prednost je u tome što duljine uvećavajućih putova koje algoritam nalazi u različitim krugovima strogo rastu. Štoviše, može se dokazati da se do pronalaska najvećeg sparivanja duljina uvećavajućeg puta poveća najviše $3|M|^{1/2}$ puta, gdje je $|M|$ veličina najvećeg sparivanja. Time je ukupan broj krugova uvećavanja ograničen na $O(|M|^{1/2})$, što daje vremensku složenost $O(|M|^{1/2}|E|)$. Budući da je $2|M|\le |V|$, složenost se može zapisati i labavijom gornjom ogradom $O(|V|^{1/2}|E|)$.

??? note "Dokaz"
    Najprije pokazujemo da duljine uvećavajućih putova koje algoritam nalazi u različitim krugovima strogo rastu.
    
    Pretpostavimo da se BFS u trenutnom krugu proširio $\ell$ slojeva. Budući da se svi nespareni desni vrhovi pronađeni BFS-om nalaze u istom sloju, svi uvećavajući putovi koje DFS u ovom krugu može naći imaju duljinu $\ell$. Treba dokazati da nakon uvećavanja duž skupa uvećavajućih putova $\{P_i\}$ pronađenih u ovom krugu u ponovno orijentiranom usmjerenom grafu više ne postoji uvećavajući put duljine najviše $\ell$.
    
    Zapravo, ako je $P$ najkraći uvećavajući put u odnosu na $M$, a $P'$ uvećavajući put u odnosu na $M\oplus P$, vrijedi $|P'|\ge |P| + 2|P\cap P'|$. Naime, $N=(M\oplus P)\oplus P'$ je u odnosu na $M$ uvećano dvaput, pa se slično kao u [dokazu Bergeove leme](./graph-match.md#berge-引理) može pokazati da simetrična razlika $M\oplus N=P\oplus P'$ sadrži barem dva disjunktna uvećavajuća puta $P_1$ i $P_2$ u odnosu na $M$. Zbog minimalnosti $P$ vrijedi
    
    $$
    2|P|\le |P_1|+|P_2|\le |P\oplus P'| = |P| + |P'| - 2|P\cap P'|.
    $$
    
    Odatle slijedi $|P'|\ge |P| + 2|P\cap P'|$. Dakle, ako je nakon dodavanja uvećavajućih putova $\{P_i\}$ novi uvećavajući put $P'$ jednako dug kao oni, on mora biti disjunktan sa svakim od njih, što proturječi maksimalnosti skupa $\{P_i\}$. Ta kontradikcija pokazuje da je nakon uvećavanja duž blokirajućeg toka novi uvećavajući put nužno strogo duži.
    
    Na kraju treba pokazati da se duljina uvećavajućeg puta poveća najviše $3|M|^{1/2}$ puta.
    
    Označimo $p=\lfloor|M|^{1/2}\rfloor$. Nakon prvih $p$ krugova preostali uvećavajući putovi imaju duljinu barem $|M|^{1/2}$. Neka je trenutno sparivanje $M_p$; tada se, slično kao gore, može pokazati da graf $(V,M\oplus M_p)$ sadrži $|M|-|M_p|$ uvećavajućih putova u odnosu na $M_p$ koji u parovima nemaju zajedničkih vrhova. Svaki od njih koristi barem $|M|^{1/2}/2$ sparenih bridova iz $M$, pa ih ukupno nema više od $2|M|^{1/2}$, tj. $|M|-|M_p|\le 2|M|^{1/2}$. To znači da se od $M_p$ može uvećavati još najviše $2|M|^{1/2}$ puta, odnosno da algoritam izvodi još najviše $2|M|^{1/2}$ krugova uvećavanja. Stoga se duljina uvećavajućeg puta ukupno poveća najviše $3|M|^{1/2}$ puta.

Ovo je samo ocjena najgore složenosti Hopcroft–Karpova algoritma. Na slučajnim grafovima vremenska je složenost Hopcroft–Karpova algoritma s velikom vjerojatnošću $O(|E|\log |V|)$[^hk-comp-ref].

### Optimizacija

Pri gradnji slojevitog grafa Hopcroft–Karpov algoritam, kao i uobičajeni Dinicov algoritam, staje čim dosegne nespareni desni vrh. No za sam problem sparivanja u bipartitnom grafu to nije nužno. Štoviše, prerano zaustavljanje BFS-a ograničava doseg kasnijeg DFS-a, pa se u svakom krugu pronađe ograničen broj uvećavajućih putova, što usporava cjelokupno sparivanje. Na nekim je grafovima čak manje učinkovit od optimiziranog Kuhnova algoritma. Jednostavno je poboljšanje stoga da BFS ne zaustavljamo rano, nego slojeviti graf gradimo za sve dostižne vrhove.

??? note "Dokaz ispravnosti"
    U optimiziranom algoritmu uvećavajući putovi u blokirajućem toku više nisu jednake duljine, pa gornji dokaz složenosti više ne vrijedi. No može se pokazati da se, uvođenjem pomoćnog grafa za svaki krug algoritma, i dalje dobiva zaključak da duljina najkraćeg uvećavajućeg puta strogo raste, čime je najgora složenost i dalje ispravna.
    
    Neka je bipartitni graf $G=(X,Y,E)$ i trenutno sparivanje $M$. Neka je $W\subseteq Y$ skup nesparenih desnih vrhova dostižnih BFS-om i neka je $d(y)$ duljina najkraćeg uvećavajućeg puta do $y\in W$. Označimo $d_\text{max} = \max_{y\in W}d(y)$. Za svaki $y\in W$ možemo dodati novi lanac koji počinje u $y$ i ima duljinu $d_\text{max} - d(y)$, pri čemu nove vrhove naizmjence označavamo kao lijeve i desne, a nove bridove naizmjence kao sparene i nesparene. Neka je tako dobiveni graf $G'=(X',Y',E')$, sparivanje $M'$, a duljina najkraćeg uvećavajućeg puta $d_\text{max}$. Tada postoji bijekcija između uvećavajućih putova u odnosu na $M$ koje se u grafu $G$ mogu naći duž slojevitog grafa – dakle najkraćih uvećavajućih putova do odgovarajućih vrhova – i globalno najkraćih uvećavajućih putova u odnosu na $M'$ u grafu $G'$. Stoga je nalaženje blokirajućeg toka i uvećavanje u slojevitom grafu grafa $G$ isto što i nalaženje blokirajućeg toka i uvećavanje u slojevitom grafu grafa $G'$. Prema prethodnom dokazu, nakon uvećavanja u grafu $G'$ više ne postoji uvećavajući put duljine $d_\text{max}$. Dakle ni u grafu $G$ više ne postoji uvećavajući put duljine $d_\text{min}=\min_{y\in W} d(y)$: takav bi put, produžen novim alternirajućim putem, nužno odgovarao uvećavajućem putu duljine $d_\text{max}$ u grafu $G'$. Time ponovno dobivamo da duljina najkraćeg uvećavajućeg puta strogo raste između krugova algoritma, pa je ukupna složenost i dalje $O(|M|^{1/2}|E|)$.

### Referentna implementacija

??? example "Ogledni zadatak [Library Checker - Matching on Bipartite Graph](https://judge.yosupo.jp/problem/bipartitematching)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_2.cpp"
    ```

## Svođenje na problem najvećeg toka

Problem najvećeg sparivanja u bipartitnom grafu može se svesti na problem najvećeg toka.

![](images/bigraph-match-2.svg)

Kao na slici, dodamo dva vrha: izvor i ponor. Iz izvora povučemo brid do svakog lijevog vrha; iz svakog desnog vrha povučemo brid do ponora; za svaki neusmjereni brid bipartitnog grafa povučemo usmjereni brid od lijevog vrha prema desnom. Kapacitet svih bridova je $1$. Svaki cjelobrojni tok u tako dobivenom usmjerenom grafu odgovara točno jednom sparivanju u bipartitnom grafu, a vrijednost toka jednaka je veličini odgovarajućeg sparivanja. Stoga je nalaženje najvećeg sparivanja u bipartitnom grafu isto što i nalaženje najvećeg toka u odgovarajućem usmjerenom grafu.

Svaki algoritam za najveći tok može se upotrijebiti za najveće sparivanje u bipartitnom grafu. Lako se vidi da su Kuhnov i Hopcroft–Karpov algoritam posebni slučajevi odgovarajućih algoritama za najveći tok. Jednako tako, za najveće sparivanje u bipartitnom grafu može se upotrijebiti i [push-relabel algoritam](../flow/max-flow.md#push-relabel-预流推进算法) i drugi. Treba, međutim, imati na umu da svaki algoritam za najveći tok, kad se primjenjuje na najveće sparivanje u bipartitnom grafu, treba ciljano optimizirati kako bi se izbjegla prevelika konstanta.

### Oblik linearnog programa

Kao i drugi problemi najvećeg toka, problem najvećeg sparivanja u bipartitnom grafu $G=(X,Y,E)$ (označimo $V=X\cup Y$) može se zapisati kao problem linearnog programiranja. Ako $x_e\in\{0,1\}$ označava pripada li brid $e$ sparivanju, dobivamo sljedeći linearni program:

$$
\begin{aligned}
\max_{\{x_e\}}\;& \sum_{e\in E}x_e \\
\text{subject to } & \sum_{e\sim v} x_{e} \le 1,~\forall v\in V,\\
& x_e\ge 0,~\forall e\in E.
\end{aligned}
$$

Ovdje $e\sim v$ označava incidenciju, tj. da je vrh $v$ jedan od krajeva brida $e$. Osim nenegativnosti, ograničenja zahtijevaju da je svaki vrh $v\in V$ incidentan s najviše jednim odabranim bridom, što je upravo definicija sparivanja. Stoga sva sparivanja odgovaraju nekim cjelobrojnim točkama dopustivog područja ovog linearnog programa.

Obrat ne vrijedi. U dopustivom rješenju $x_e$ može biti razlomak, što ne predstavlja nikakvo stvarno sparivanje. Ipak, za bipartitni graf $G$ sve su ekstremne točke gornjeg linearnog programa cjelobrojne. To znači da se optimalna vrijednost funkcije cilja uvijek postiže u cjelobrojnoj točki, pa necjelobrojne slučajeve ne treba razmatrati. To svojstvo ne vrijedi za opće grafove, pa u općem grafu gornji linearni program nije ekvivalentan problemu najvećeg sparivanja.

Dualni problem ovog linearnog programa može se zapisati ovako:

$$
\begin{aligned}
\min_{\{y_v\}}\;& \sum_{v\in V}y_v \\
\text{subject to } & y_u+y_v \ge 1,~\forall (u,v)\in E,\\
& y_v\ge 0,~\forall v\in V.
\end{aligned}
$$

Ubrzo ćemo vidjeti da je to upravo problem najmanjeg vršnog pokrivača u bipartitnom grafu.

## Dulmage–Mendelsohnova dekompozicija

Pomoću najvećeg sparivanja bipartitnog grafa vrhovi se mogu podijeliti u nekoliko međusobno disjunktnih podskupova koji potpuno opisuju raspodjelu i strukturu svih najvećih sparivanja tog grafa. To je Dulmage–Mendelsohnova dekompozicija. U natjecateljskom programiranju ovom se dekompozicijom mogu prepoznati ključni vrhovi i ključni bridovi najvećeg sparivanja, a time i utvrditi jedinstvenost najvećeg sparivanja ili riješiti igre na bipartitnim grafovima i slični problemi.

### Konstrukcija

Neka je $M$ jedno najveće sparivanje bipartitnog grafa $G=(X,Y,E)$.

![](images/bigraph-match-4.svg)

Kao na slici, za sve vrhove $V=X\cup Y$ definiramo sljedeća tri podskupa:

-   parno dostižni vrhovi $\mathcal E$: svi vrhovi do kojih se iz nekog nesparenog vrha može doći alternirajućim putem parne duljine;
-   neparno dostižni vrhovi $\mathcal O$: svi vrhovi do kojih se iz nekog nesparenog vrha može doći alternirajućim putem neparne duljine;
-   nedostižni vrhovi $\mathcal U$: svi vrhovi do kojih se iz nesparenog vrha ne može doći alternirajućim putem.

Može se dokazati da tako dobivena tri skupa vrhova $\mathcal E,\mathcal O,\mathcal U$ imaju sljedeća svojstva:

???+ note "Svojstva"
    1.  Skupovi $\mathcal E,\mathcal O,\mathcal U$ čine particiju skupa vrhova, a ta particija ne ovisi o izboru najvećeg sparivanja $M$.
    2.  Svako najveće sparivanje grafa $G$ sadrži perfektno sparivanje među vrhovima skupa $\mathcal U$ i svaki vrh iz $\mathcal O$ sparuje s nekim vrhom iz $\mathcal E$. Drugim riječima, veličina najvećeg sparivanja grafa $G$ jednaka je $|\mathcal O|+|\mathcal U|/2$.
    3.  Graf $G$ ne sadrži brid koji spaja vrh iz $\mathcal E$ s vrhom iz $\mathcal E\cup\mathcal U$.

??? note "Dokaz"
    1.  Po definiciji su $\mathcal U$ i $\mathcal E\cup\mathcal O$ disjunktni. Treba još pokazati da su $\mathcal E$ i $\mathcal O$ disjunktni. Pretpostavimo suprotno: za vrh $v\in\mathcal E\cap\mathcal O$ postoji alternirajući put parne duljine od nesparenog vrha $a$ do $v$ i alternirajući put neparne duljine od nesparenog vrha $b$ do $v$. Budući da je $G$ bipartitan, $a\neq b$, a bridovi kojima ta dva puta ulaze u $v$ su redom spareni i nespareni. Spajanjem tih dvaju putova dobivamo alternirajući put od $a$ preko $v$ do $b$. To je uvećavajući put, što proturječi tome da je $M$ najveće sparivanje. Dakle $\mathcal E\cap\mathcal O=\varnothing$.
    
        Neka je $M'$ najveće sparivanje različito od $M$. Ponavljanjem [dokaza Bergeove leme](./graph-match.md#berge-引理) može se pokazati da se $M'\oplus M$ sastoji samo od putova parne duljine i parnih ciklusa. Počevši od najvećeg sparivanja $M$, bridove u tim komponentama (putovima i ciklusima) možemo jednu po jednoj okrenuti (zamijeniti sparene i nesparene bridove) i tako dobiti najveće sparivanje $M'$. Pri okretanju parnog ciklusa nespareni vrhovi ostaju nespareni, a parnost duljine alternirajućih putova iz njih se ne mijenja; pri okretanju puta parne duljine krajevi puta zamjenjuju stanje sparenosti, ali parnost duljine puta od njih do bilo kojeg vrha na putu je jednaka. Stoga skupovi $\mathcal E,\mathcal O,\mathcal U$ tijekom okretanja ostaju nepromijenjeni. To pokazuje da dekompozicija ne ovisi o izboru najvećeg sparivanja $M$.
    2.  Ako se spareni brid pojavljuje na nekom alternirajućem putu iz nesparenog vrha $v$, parnosti udaljenosti njegovih krajeva od $v$ nužno su različite, pa oni pripadaju redom skupovima $\mathcal E$ i $\mathcal O$; inače su oba kraja nužno u $\mathcal U$. To znači da su spareni bridovi najvećeg sparivanja nužno $\mathcal E\mathcal O$ bridovi ili $\mathcal U\mathcal U$ bridovi. Obratno, nespareni vrh dostižan je iz samog sebe alternirajućim putem duljine nula, pa se pojavljuje samo u skupu $\mathcal E$; dakle u skupovima $\mathcal O$ i $\mathcal U$ svi su vrhovi spareni. Jednostavnim prebrojavanjem dobivamo da je veličina najvećeg sparivanja $|\mathcal O|+|\mathcal U|/2$.
    3.  Po definiciji je svaki vrh $a\in\mathcal E$ dostižan iz nesparenog vrha $v$ alternirajućim putem parne duljine; drugim riječima, vrh iz $\mathcal E$ ili je nesparen ili alternirajući put $P$ do njega završava sparenim bridom. Kad bi u grafu $G$ postojao brid koji spaja $a$ s nekim vrhom $b\in\mathcal E\cup\mathcal U$, prema prethodnom bi taj brid nužno bio nesparen, pa bismo njime mogli produžiti alternirajući put $P$. To bi značilo da vrh $b$ pripada i skupu $\mathcal O$, što proturječi prvom svojstvu. Dakle u grafu $G$ ne postoji brid koji spaja vrh iz $\mathcal E$ s vrhom iz $\mathcal E\cup\mathcal U$.

Tako dobivena dekompozicija skupa vrhova $V=\mathcal E\cup\mathcal O\cup\mathcal U$ zove se **Dulmage–Mendelsohnova dekompozicija**. Nakon što se gore opisanim algoritmima nađe najveće sparivanje, Dulmage–Mendelsohnova dekompozicija može se izračunati BFS-om u vremenu $O(|V|+|E|)$.

### Ključni vrhovi najvećeg sparivanja

Ako je vrh $v$ sparen u svakom najvećem sparivanju bipartitnog grafa $G$, zovemo ga ključnim vrhom najvećeg sparivanja. Sljedeći rezultat pokazuje: vrh je ključan ako i samo ako u nekom najvećem sparivanju ne postoji alternirajući put parne duljine od nesparenog vrha do tog vrha.

???+ note "Teorem"
    Neka je $V=\mathcal E\cup\mathcal O\cup\mathcal U$ Dulmage–Mendelsohnova dekompozicija bipartitnog grafa $G=(X,Y,E)$. Tada je vrh $v\in V$ ključan ako i samo ako je $v\in\mathcal O\cup \mathcal U$.

??? note "Dokaz"
    Iz svojstava Dulmage–Mendelsohnove dekompozicije slijedi da su u svakom najvećem sparivanju grafa $G$ vrhovi iz $\mathcal O$ i $\mathcal U$ nužno spareni. Stoga su vrhovi iz $\mathcal O\cup \mathcal U$ nužno ključni. Treba još pokazati da u skupu $\mathcal E$ nema ključnih vrhova. Ako je u najvećem sparivanju $M$ vrh $a\in\mathcal E$ ključan, postoji alternirajući put $P$ parne duljine koji spaja $a$ s nekim nesparenim vrhom $b\in\mathcal E$. Okretanjem svih bridova na tom putu dobivamo najveće sparivanje $M\oplus P$ u kojem je vrh $a$ nesparen. Dakle u skupu $\mathcal E$ nema ključnih vrhova.

Stoga je za nalaženje ključnih vrhova najvećeg sparivanja dovoljno izračunati Dulmage–Mendelsohnovu dekompoziciju.

### Ključni bridovi najvećeg sparivanja

Slično, ako je brid $e$ sparen u svakom najvećem sparivanju bipartitnog grafa $G$, zovemo ga ključnim bridom najvećeg sparivanja. Najveće sparivanje bipartitnog grafa jedinstveno je ako i samo ako su u nekom njegovom najvećem sparivanju svi spareni bridovi ključni.

???+ note "Teorem"
    Neka je $V=\mathcal E\cup\mathcal O\cup\mathcal U$ Dulmage–Mendelsohnova dekompozicija bipartitnog grafa $G=(X,Y,E)$ i neka je $M$ jedno njegovo najveće sparivanje. Tada je brid $e\in E$ ključan ako i samo ako su oba kraja brida $e$ u $\mathcal U$, brid $e$ je sparen u $M$ i u odnosu na $M$ ne postoji alternirajući ciklus koji sadrži brid $e$.

??? note "Dokaz"
    Krajevi ključnog brida moraju biti ključni vrhovi. Prema svojstvima Dulmage–Mendelsohnove dekompozicije, bridovi najvećeg sparivanja mogu biti samo $\mathcal E\mathcal O$ bridovi ili $\mathcal U\mathcal U$ bridovi. No u $\mathcal E$ nema ključnih vrhova, pa ključni brid može biti samo $\mathcal U\mathcal U$ brid. Naravno, ključni brid mora biti i sparen u $M$. Neka je $e\in M$ neki $\mathcal U\mathcal U$ brid. On nije ključan ako i samo ako postoji drugo najveće sparivanje $M'\neq M$ takvo da je $e\in M\oplus M'$. Ponavljanjem [dokaza Bergeove leme](./graph-match.md#berge-引理) može se pokazati da se $M'\oplus M$ sastoji samo od putova parne duljine i parnih ciklusa. Jedan od krajeva svakog takvog puta je vrh nesparen u $M$, pa nijedan vrh na tom putu nije u $\mathcal U$, što proturječi izboru brida $e$. Dakle brid $e$ može se pojaviti samo u parnom ciklusu. Stoga $\mathcal U\mathcal U$ brid $e\in M$ nije ključan ako i samo ako u odnosu na $M$ postoji alternirajući ciklus koji sadrži brid $e$. To je i trebalo dokazati.

Dakle, ključne bridove najvećeg sparivanja nalazimo ovako:

1.  nađemo najveće sparivanje $M$ grafa $G$;
2.  orijentiramo bridove grafa $G$ prema $M$ i dobijemo usmjereni graf $G_M$;
3.  BFS-om nađemo skup $\mathcal U$ Dulmage–Mendelsohnove dekompozicije, tj. skup vrhova do kojih se iz nesparenih vrhova ne može doći alternirajućim putem;
4.  [Tarjanovim algoritmom](../scc.md#tarjan-算法) nađemo sve jako povezane komponente usmjerenog grafa $G_M$;
5.  prođemo bridove sparivanja $M$: ako su oba kraja brida u $\mathcal U$, ali nisu u istoj jako povezanoj komponenti, brid je ključan.

Nakon što imamo najveće sparivanje, vremenska složenost preostalih koraka je $O(|V|+|E|)$.

## Povezani problemi

Algoritmima za najveće sparivanje u bipartitnom grafu mogu se riješiti i drugi problemi kombinatorne optimizacije.

### Najmanji vršni pokrivač bipartitnog grafa

Problem najmanjeg vršnog pokrivača (minimum vertex cover) traži da se u neusmjerenom grafu odabere najmanji broj vrhova tako da svaki brid ima barem jedan odabrani kraj.

Za opće grafove problem najmanjeg vršnog pokrivača je NP-težak, ali za bipartitne grafove Kőnigov teorem pokazuje da se svodi na problem najvećeg sparivanja, pa se može učinkovito riješiti. Dokaz teorema ujedno daje i konstrukciju najmanjeg vršnog pokrivača.

???+ note "Kőnigov teorem"
    U bipartitnom grafu broj vrhova najmanjeg vršnog pokrivača jednak je broju bridova najvećeg sparivanja.

??? note "Dokaz"
    Neka je $M$ najveće sparivanje bipartitnog grafa $G=(X,Y,E)$. Neka je $U$ skup nesparenih lijevih vrhova, a $Z$ skup vrhova grafa $G$ do kojih se iz vrhova skupa $U$ može doći nekim alternirajućim putem. Tada je skup vrhova $C=(X\setminus Z)\cup(Y\cap Z)$ traženi najmanji vršni pokrivač.
    
    ![](images/bigraph-match-3.svg)
    
    Najprije, skup $C$ je vršni pokrivač. Pretpostavimo suprotno: postoji brid $(u,v)\in E$ takav da je $u\in X\cap Z$ i $v\in Y\setminus Z$. Neka je $P_u$ alternirajući put koji dolazi do $u$. Ako je brid $(u,v)$ sparen, posljednji brid puta $P_u$ je $(v,u)$, što proturječi $v\notin Z$; ako brid $(u,v)$ nije sparen, put $P_u$ možemo produžiti bridom $(u,v)$ do alternirajućeg puta koji dolazi do $v$, što također proturječi $v\notin Z$. Te kontradikcije pokazuju da svaki brid ima barem jedan kraj u $C$, pa je $C$ vršni pokrivač.
    
    Zatim treba pokazati da je $C$ najmanji vršni pokrivač. Da bi pokrio sve bridove najvećeg sparivanja $M$, svaki vršni pokrivač treba barem $|M|$ vrhova. Dovoljno je stoga dokazati $|C|=|M|$, iz čega slijedi da je $C$ najmanji vršni pokrivač. To je ekvivalentno tvrdnji da $C$, osim po jednog kraja svakog sparenog brida, ne sadrži druge vrhove; drugim riječima, $C$ ne sadrži nesparene vrhove. Pretpostavimo suprotno: postoji nespareni vrh $v\in C$. Ako je $v\in X$, nužno je $v\in U\subseteq Z$, što proturječi konstrukciji skupa $C$; ako je $v\in Y$, alternirajući put koji dolazi do $v$ je uvećavajući put u odnosu na $M$, što po Bergeovoj lemi proturječi tome da je $M$ najveće sparivanje. Te kontradikcije pokazuju da takav nespareni vrh ne postoji, pa je $C$ najmanji vršni pokrivač.

Gledano iz perspektive mrežnih tokova, problem najmanjeg vršnog pokrivača je problem najmanjeg reza: odabir lijevog vrha odgovara rezanju brida između njega i izvora, a odabir desnog vrha rezanju brida između njega i ponora. Gledano iz perspektive linearnog programiranja, problem najmanjeg vršnog pokrivača dualan je problemu najvećeg sparivanja. Stoga se Kőnigov teorem može shvatiti kao poseban slučaj [teorema o najvećem toku i najmanjem rezu](../flow/max-flow.md#最大流最小割定理) ili, općenitije, kao poseban slučaj teorema o jakoj dualnosti u linearnom programiranju.

### Najveći nezavisni skup bipartitnog grafa

Problem najvećeg nezavisnog skupa (maximum independent set) traži da se u neusmjerenom grafu odabere najveći broj vrhova od kojih nikoja dva nisu susjedna.

Za opće grafove vrijedi sljedeći teorem:

???+ note "Teorem"
    U grafu $G=(V,E)$ skup vrhova $C\subseteq V$ je vršni pokrivač ako i samo ako je njegov komplement $V\setminus C$ nezavisan skup.

??? note "Dokaz"
    Skup $C$ je vršni pokrivač ako i samo ako za svaki brid $e$ iz $E$ barem jedan od njegovih krajeva pripada skupu $C$, ako i samo ako nijedan brid iz $E$ nema oba kraja u skupu $V\setminus C$, ako i samo ako je $V\setminus C$ nezavisan skup.

???+ note "Korolar"
    U grafu $G=(V,E)$ zbroj veličina najmanjeg vršnog pokrivača i najvećeg nezavisnog skupa jednak je broju vrhova.

Stoga je, kao i problem najmanjeg vršnog pokrivača, problem najvećeg nezavisnog skupa NP-težak za opće grafove, ali se za bipartitne grafove svodi na problem najvećeg sparivanja i može se učinkovito riješiti.

### Najmanji pokrivač putovima u usmjerenom acikličkom grafu

Problem najmanjeg pokrivača putovima (minimum path cover) traži da se u usmjerenom grafu odabere najmanji broj jednostavnih putova tako da se svaki vrh pojavljuje u točno jednom putu.

Za opće usmjerene grafove problem najmanjeg pokrivača putovima je NP-težak, ali za usmjerene acikličke grafove svodi se na problem najvećeg sparivanja u bipartitnom grafu. Za usmjereni aciklički graf $G=(V,E)$ konstruiramo bipartitni graf $G'=(V^\text{in},V^\text{out},E')$ ovako:

-   Za svaki vrh $v\in V$ napravimo ulazni vrh $v^\text{in}$ i izlazni vrh $v^\text{out}$. Skupove svih ulaznih i svih izlaznih vrhova označimo $V^\text{in}$ i $V^\text{out}$. Oni postaju lijevi odnosno desni dio novog grafa.
-   Za svaki usmjereni brid $(u,v)\in E$ napravimo neusmjereni brid $(u^\text{out},v^\text{in})$. Skup svih tih neusmjerenih bridova je $E'$.

Tada vrijedi:

???+ note "Teorem"
    Zbroj veličine najmanjeg pokrivača putovima usmjerenog acikličkog grafa $G=(V,E)$ i veličine najvećeg sparivanja odgovarajućeg bipartitnog grafa $G'=(V^\text{in},V^\text{out},E')$ jednak je broju vrhova.

??? note "Dokaz"
    Svako sparivanje $M'$ bipartitnog grafa $G'$ odgovara podgrafu $F$ grafa $G$ u kojem svaki vrh ima ulazni i izlazni stupanj najviše jedan; drugim riječima, podgraf $F$ je skup međusobno disjunktnih putova ili ciklusa u usmjerenom grafu $G$. No pretpostavili smo da $G$ nema ciklusa, pa $F$ sadrži samo disjunktne putove. Obratno, za svaki takav podgraf $F$ može se konstruirati odgovarajuće sparivanje. Budući da je veličina sparivanja $M'$ jednaka razlici broja vrhova i broja putova u $F$, problem najmanjeg pokrivača putovima grafa $G$ odgovara problemu najvećeg sparivanja grafa $G'$.

Dokaz je konstruktivan, pa se iz dobivenog najvećeg sparivanja lako konstruira odgovarajući najmanji pokrivač putovima. Štoviše, konstrukcija pokazuje da za opće usmjerene grafove ovo svođenje više ne vrijedi, upravo zato što sparivanje u bipartitnom grafu može odgovarati ciklusu u usmjerenom grafu.

Posebno, za skup $X$ i relaciju parcijalnog uređaja $P$ na njemu možemo napraviti usmjereni aciklički graf $G=(X,P)$. Prema [Dilworthovu teoremu](../../math/order-theory.md#dilworth-定理与-mirsky-定理), veličina najmanjeg pokrivača putovima grafa $G$ tada je jednaka duljini najduljeg antilanca, tj. širini parcijalno uređenog skupa $(X,P)$. Dakle ovaj odjeljak zapravo daje učinkovit način računanja širine proizvoljnog parcijalno uređenog skupa.

## Primjeri zadataka

Teži dio primjene sparivanja u bipartitnom grafu jest konstrukcija grafa; u ovom odjeljku kroz nekoliko zadataka pokazujemo tehnike konstrukcije.

???+ example "[Luogu P1129 矩阵游戏](https://www.luogu.com.cn/problem/P1129)"
    Dana je kvadratna 01-matrica. U jednom potezu smijemo zamijeniti dva retka ili dva stupca. Može li se zamjenama postići da glavna dijagonala (od gornjeg lijevog do donjeg desnog kuta) sadrži samo jedinice?

??? note "Rješenje"
    Uočimo: ako postoji $n$ jedinica od kojih nikoje dvije nisu u istom retku ni istom stupcu, rješenje sigurno postoji; inače sigurno ne postoji. Problem se svodi na to može li se naći tih $n$ jedinica.
    
    Za pojedinu jedinicu, njezin odabir u konačnom rješenju znači da su njezin redak i stupac zauzeti. Zato konstruiramo bipartitni graf s $n$ lijevih i $n$ desnih vrhova, u kojem za svaki element jednak $1$ povučemo brid između lijevog vrha njegova retka i desnog vrha njegova stupca. Zatim tražimo sparivanje u bipartitnom grafu.

??? note "Kôd"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_3.cpp"
    ```

???+ example "[Gym 104427B Lawyers](https://codeforces.com/gym/104427/problem/B)"
    Ima $n$ odvjetnika, svi optuženi za prijevaru. Moraju se međusobno braniti tako da svaki odvjetnik bude oslobođen. Među tih $n$ odvjetnika postoji $m$ parova povjerenja; par povjerenja $(a, b)$ znači da $a$ može braniti $b$. Svaki odvjetnik koji ima branitelja bit će oslobođen, uz jednu iznimku: ako $a$ i $b$ brane jedan drugoga, obojica će biti osuđeni.
    
    Odredite može li se postići da svaki odvjetnik bude oslobođen.

??? note "Rješenje"
    Za svaki **neuređeni par** $(a, b)$: ako $a$ može braniti $b$, povučemo brid od tog neuređenog para do $b$, i obratno.
    
    Čuvamo samo parove $(a, b)$ koji su povezani bridom; problem se tako svodi na najveće sparivanje u bipartitnom grafu s $m$ lijevih i $n$ desnih vrhova.

??? note "Kôd"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_4.cpp"
    ```

???+ example "[Codeforces 1404E Bricks](https://codeforces.com/problemset/problem/1404/E)"
    Treba točno pokriti mrežu $n \times m$ ciglama dimenzija $1 \times x$; cigle se smiju rotirati, a neka polja ne smiju biti pokrivena.

??? note "Rješenje"
    Razmotrimo kako nastaje konačno rješenje:
    
    Najprije sva polja koja se smiju pokriti pokrijemo ciglama $1 \times 1$. Cigla $1 \times x$ može nastati uzastopnim „spajanjem po retku” $x$ susjednih cigli $1 \times 1$ u istom retku. Slično, cigla $x \times 1$ može nastati uzastopnim „spajanjem po stupcu” $x$ susjednih cigli $1 \times 1$ u istom stupcu.
    
    Očito jedno spajanje po retku i jedno spajanje po stupcu ne mogu zahvatiti istu ciglu, a što je spajanja više, to je cigli manje. Zato spajanja po retku uzmemo za lijeve vrhove, spajanja po stupcu za desne, a opisane sukobe za bridove, i tako dobijemo bipartitni graf. Izvorni problem time postaje problem najvećeg nezavisnog skupa u bipartitnom grafu.

??? note "Kôd"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_5.cpp"
    ```

???+ example "[Codeforces 1139E - Maximize Mex](https://codeforces.com/problemset/problem/1139/E)"
    Dano je $m$ multiskupova s ukupno $n$ elemenata. U svakom koraku iz nekog multiskupa izbrišemo jedan element, a zatim postavimo upit: „ako iz svakog multiskupa odaberemo najviše jedan element, koliki je najveći mogući $\operatorname{mex}$?”

??? note "Rješenje"
    Razmotrimo najprije kako riješiti zadatak bez brisanja elemenata.
    
    Za svaki multiskup napravimo novi vrh; za svaki mogući odgovor napravimo novi vrh. Zatim za svaki element $a$ multiskupa koji odgovara vrhu $l_i$ povučemo brid od $l_i$ do $r_a$. Ova je pojednostavljena inačica tada problem najvećeg sparivanja u bipartitnom grafu.
    
    Vratimo li sada brisanje elemenata, vidimo da s njim ne možemo izaći na kraj: brisanje jednog brida može drastično promijeniti sparivanje i složenost je neprihvatljiva. Zato postupimo obrnuto: svaki put dodamo jedan brid i odmah ponovno uvećamo sparivanje. Zbog toga se u ovom zadatku može upotrijebiti samo Kuhnov algoritam.

??? note "Kôd"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_6.cpp"
    ```

???+ example "[Luogu P3355 - 骑士共存问题](https://www.luogu.com.cn/problem/P3355)"
    Dana je šahovska ploča $n \times n$ na kojoj se na neka polja ne smiju stavljati figure. Koliko se najviše skakača može postaviti tako da se nikoja dva međusobno ne napadaju?

??? note "Rješenje"
    Uočimo: ako ploču obojimo tako da nikoja dva crna ni dva bijela polja nisu susjedna, skakač može napasti samo polja suprotne boje.
    
    Zatim izravno primijenimo najveći nezavisni skup u bipartitnom grafu.

??? note "Kôd"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_7.cpp"
    ```

## Zadaci

-   [Codeforces 1765A - Access Levels](https://codeforces.com/problemset/problem/1765/A)
-   [AtCoder abc274G - Security Camera 3](https://atcoder.jp/contests/abc274/tasks/abc274_g)
-   [Codeforces 1773D - Dominoes](https://codeforces.com/problemset/problem/1773/D)
-   [Luogu P5030 - 长脖子鹿放置](https://www.luogu.com.cn/problem/P5030)
-   [Luogu P2071 - 座位安排](https://www.luogu.com.cn/problem/P2071)
-   [LibreOJ 6002 - 最小路径覆盖](https://loj.ac/p/6002)

## Literatura

-   [Kuhn's Algorithm - Maximum Bipartite Matching](https://cp-algorithms.com/graph/kuhn_maximum_bipartite_matching.html)
-   [二分图最大匹配的 König 定理及其证明 (Kőnigov teorem o najvećem sparivanju u bipartitnom grafu i njegov dokaz)](https://matrix67.com/blog/archives/116)
-   [Implementing Dinitz on bipartite graphs by adamant - Codeforces blogs](https://codeforces.com/blog/entry/118098)
-   Bondy, John Adrian, and Uppaluri Siva Ramachandra Murty. Graph theory with applications. Vol. 290. London: Macmillan, 1976.
-   陈胤伯 (Chen Yinbo). 浅谈图的匹配算法及其应用 (O algoritmima sparivanja u grafovima i njihovim primjenama). Zbornik radova kandidata za kinesku reprezentaciju na Informatičkoj olimpijadi, 2015.
-   [Dulmage–Mendelsohn decomposition - Wikipedia](https://en.wikipedia.org/wiki/Dulmage%E2%80%93Mendelsohn_decomposition)
-   [Notes on Dulmage–Mendelsohn decomposition](https://www.cse.iitm.ac.in/~meghana/matchings/bip-decomp.pdf)

[^hk-comp-ref]: Bast, Holger; Mehlhorn, Kurt; Schäfer, Guido; Tamaki, Hisao (2006), "Matching algorithms are fast in sparse random graphs", Theory of Computing Systems, 39 (1): 3–14.
