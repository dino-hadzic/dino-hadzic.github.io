---
title: Matroidi
---

## Uvod

**Matroid** je apstraktna algebarska struktura koju je 1935. godine uveo Hassler Whitney s ciljem da se objedine i poopće pojmovi vezani uz nezavisnost, npr. linearna nezavisnost u linearnoj algebri i acikličnost u teoriji grafova.

Matroidi pružaju snažan teorijski alat za rješavanje optimizacijskih problema povezanih s nezavisnošću; široko se primjenjuju u kombinatorici, teoriji grafova, oblikovanju algoritama i drugim područjima, a posebno važnu ulogu imaju kao matematička podloga za optimizacijske metode poput pohlepnih (greedy) algoritama.

## Definicija

### Matroid

**Matroid** zapisujemo kao $M = (E, \mathcal{I})$, gdje je:

-   $E$ konačan skup, koji nazivamo **osnovni skup (ground set)**.
-   $\mathcal{I}$ familija podskupova skupa $E$, koju nazivamo **familija nezavisnih skupova (family of independent sets)**; njezine članove nazivamo **nezavisni skupovi (independent sets)**. Ona ima sljedeća tri svojstva:

    -   **Nepraznost**: prazan skup je nezavisan, tj. $\emptyset \in \mathcal{I}$.

    -   **Nasljednost**: svaki podskup nezavisnog skupa također je nezavisan skup. Ako je $I \in \mathcal{I}$, onda za svaki $I' \subseteq I$ vrijedi $I' \in \mathcal{I}$.

    -   **Svojstvo zamjene (proširenja)**: ako je $I, J \in \mathcal{I}$ i $|I| < |J|$, onda postoji $j \in J \setminus I$ takav da je $I \cup \{j\} \in \mathcal{I}$.

Ako struktura oblika $(E, \mathcal{I})$ zadovoljava navedena tri svojstva, nazivamo je matroidom.

### Baza

**Baza (basis)** je maksimalan nezavisan skup matroida, tj. nezavisan skup kojemu se ne može dodati ni jedan element a da ostane nezavisan. Skup svih baza nazivamo **familijom baza** i označavamo $\mathcal{B}$.

**Svojstva**:

1.  **Jednaka kardinalnost**: sve baze imaju istu veličinu, koju nazivamo **rang (rank)** matroida.

2.  **Svojstvo proširenja**: svaki nezavisan skup može se dodavanjem elemenata neke baze proširiti do baze.

### Kružnica

**Kružnica (circuit)** je minimalan zavisan skup matroida, tj. skup čiji su svi pravi podskupovi nezavisni, ali on sam nije nezavisan; nikoje dvije kružnice nisu jedna sadržana u drugoj.

### Rang

**Funkcija ranga (rank function)** $r: 2^E \rightarrow \mathbb{Z}_{\geq 0}$ preslikava podskupove osnovnog skupa $E$ u nenegativne cijele brojeve. Za svaki $S \subseteq E$, $r(S)$ se definira kao veličina najvećeg nezavisnog skupa sadržanog u $S$, tj.

$$
r(S) = \max \{ |I| \mid I \subseteq S \wedge I \in \mathcal{I} \}.
$$

**Svojstva**:

1.  **Nenegativnost**: za svaki $S \subseteq E$ vrijedi $0 \leq r(S) \leq |S|$.

2.  **Monotonost**: ako je $A \subseteq B \subseteq E$, onda je $r(A) \leq r(B)$.

3.  **Submodularnost**: za sve $A, B \subseteq E$ vrijedi $r(A \cup B) + r(A \cap B) \leq r(A) + r(B)$.

## Tipični primjeri

### 1. Uniformni matroid (Uniform Matroid)

**Definicija**: za zadani osnovni skup $E$ i nenegativan cijeli broj $k$, familija nezavisnih skupova uniformnog matroida $U_{k,E}$ sastoji se od svih podskupova veličine najviše $k$, tj.

$$
\mathcal{I} = \{ I \subseteq E \mid |I| \leq k \}.
$$

-   **Baze**: svi podskupovi veličine $k$.

-   **Kružnice**: svi podskupovi veličine $k + 1$.

-   **Rang**: $r(E) = \min(k, |E|)$, tj. nezavisan skup može imati najviše $k$ elemenata.

### 2. Grafovski matroid (Graphic Matroid)

**Definicija**: za zadani neusmjereni graf $G = (V, E)$ osnovni skup grafovskog matroida $M(G)$ je skup bridova $E$, a njegova familija nezavisnih skupova sastoji se od svih skupova bridova koji ne sadrže ciklus, tj. od svih šuma.

-   **Baze**: razapinjuća stabla grafa (ako je graf povezan). Razapinjuće stablo je maksimalan nezavisan skup: ne može mu se dodati brid a da se ne stvori ciklus.

-   **Kružnice**: jednostavni ciklusi grafa; ako iz ciklusa uklonimo bilo koji brid, ostatak je nezavisan skup.

-   **Rang**: $r(E) = |V|  - c$, gdje je $c$ broj komponenata povezanosti grafa. Za povezan neusmjereni graf rang je jednak broju vrhova umanjenom za jedan, tj. $|V|  - 1$.

### 3. Linearni matroid (Linear Matroid)

**Definicija**: linearni matroid temelji se na vektorskom prostoru. Za zadani vektorski prostor $V$ osnovni skup $E$ je konačan skup vektora iz $V$, a familija nezavisnih skupova sastoji se od svih linearno nezavisnih podskupova skupa $E$.

-   **Baze**: maksimalni linearno nezavisni skupovi vektora; njihova veličina jednaka je dimenziji vektorskog prostora.

-   **Kružnice**: minimalni linearno zavisni skupovi vektora, tj. skupovi čiji su svi pravi podskupovi nezavisni, a oni sami su linearno zavisni.

-   **Rang**: rang linearnog matroida je $r(E) = \dim(V)$, tj. dimenzija vektorskog prostora. Veličina nezavisnog skupa ne može premašiti dimenziju vektorskog prostora.

### 4. Particijski matroid (Partition Matroid)

**Definicija**: osnovni skup $E$ podijelimo na disjunktne podskupove $E_1, E_2, \dots, E_m$ i svakom podskupu $E_i$ pridružimo nenegativan cijeli broj $k_i$. Familiju nezavisnih skupova particijskog matroida čine podskupovi koji iz svakog dijela uzimaju najviše $k_i$ elemenata, tj.

$$
\mathcal{I} = \left\{ I \subseteq E \mid \forall i,\, |I \cap E_i|  \leq k_i \right\}.
$$

-   **Baze**: nezavisni skupovi za koje vrijedi $|I \cap E_i| = k_i$ su baze particijskog matroida. Svaka baza iz svakog podskupa uzima točno $k_i$ elemenata.

-   **Kružnice**: kružnice particijskog matroida su minimalni zavisni skupovi, tj. skupovi koji iz barem jednog podskupa sadrže više od $k_i$ elemenata.

-   **Rang**: rang particijskog matroida je $r(E) = \sum_{i=1}^m k_i$, tj. veličina najvećeg nezavisnog skupa jednaka je zbroju najvećih dopuštenih brojeva elemenata po podskupovima.

### 5. Obojeni matroid (Colored Matroid)

**Definicija**: obojeni matroid poseban je oblik particijskog matroida u kojem je svakom elementu pridružena boja. Za zadani osnovni skup $E$ i skup boja $C$, svaki element $e \in E$ povezan je s nekom bojom $c \in C$. Nezavisni skupovi obojenog matroida moraju, osim uvjeta nezavisnosti običnog matroida, poštovati i ograničenja zadana po bojama, npr. da se iz nezavisnog skupa smije uzeti najviše određen broj elemenata iste boje.

-   **Baze**: baze obojenog matroida su maksimalni nezavisni skupovi koji zadovoljavaju ograničenja boja i uvjet nezavisnosti.

-   **Kružnice**: kružnice su minimalni zavisni skupovi, tj. skupovi elemenata koji krše nezavisnost ili neko ograničenje boja.

-   **Rang**: rang obojenog matroida je veličina najvećeg nezavisnog skupa koji zadovoljava ograničenja boja. On ovisi i o strukturi matroida i o konkretnim ograničenjima boja.

## Konstrukcije i operacije

### Dualnost

Za zadani matroid $M = (E, \mathcal{I})$ njegov **dualni matroid** $M^* = (E, \mathcal{I}^*)$ definira se kao:

$$
\mathcal{I}^* = \{ I^* \subseteq E \mid \exists B \in \mathcal{I}, |B| = r(E), B \subseteq E \setminus I^* \}.
$$

**Svojstva**:

-   **Baze**: baze dualnog matroida $M^*$ su komplementi baza matroida $M$ u osnovnom skupu $E$. Drugim riječima, ako je $B$ baza od $M$, onda je $E \setminus B$ baza od $M^*$.

-   **Funkcija ranga**: funkcija ranga dualnog matroida je $r^*(S) = |S| - r(E) + r(E \setminus S)$, gdje je $S$ podskup od $E$. To znači da se rang dualnog matroida može izračunati iz veličine osnovnog skupa, ranga izvornog matroida i ranga osnovnog skupa iz kojeg je uklonjen $S$.

-   **Involutivnost**: dual dualnog matroida je ponovno izvorni matroid, tj. $(M^*)^* = M$.

**Primjer**:

Za neusmjereni graf $G = (V, E)$ dual $M(G)^*$ grafovskog matroida $M(G)$ je matroid sastavljen od reznih skupova grafa. Baze grafovskog matroida $M(G)$ su razapinjuća stabla grafa, baze njegova duala $M(G)^*$ su komplementi tih razapinjućih stabala, a kružnice duala $M(G)^*$ su minimalni rezni skupovi grafa, tj. minimalni skupovi bridova čije uklanjanje graf dijeli na dva nepovezana dijela.

Na primjer, promotrimo jednostavan graf-trokut $G$ sa skupom bridova $E = \{e_1, e_2, e_3\}$. Baze grafovskog matroida $M(G)$ su skupovi od dva brida (npr. $\{e_1, e_2\}$), baze dualnog matroida $M(G)^*$ su skupovi od jednog brida (npr. $\{e_3\}$), a kružnice od $M(G)^*$ su skupovi od dva brida (tj. minimalni rezni skupovi, npr. $\{e_2,e_3\}$), jer uklanjanje tih bridova dijeli graf na dvije komponente povezanosti.

### Brisanje i kontrakcija

**Brisanje (deletion)**:

Za $A \subseteq E$, brisanjem skupa $A$ iz matroida $M$ dobivamo novi matroid $M \setminus A$ čija je familija nezavisnih skupova $\mathcal{I}'$ definirana kao:

$$
\mathcal{I}' = \{ I \subseteq E \setminus A \mid I \in \mathcal{I} \}.
$$

Vidimo da brisanje jednostavno uklanja neke elemente iz matroida i zadržava nezavisne skupove sastavljene od preostalih elemenata; izvorni nezavisni skupovi ostaju nepromijenjeni, samo su uklonjeni elementi.

**Kontrakcija (contraction)**:

Za $A \subseteq E$, kontrakcijom skupa $A$ u matroidu $M$ dobivamo matroid $M / A$ čija je familija nezavisnih skupova $\mathcal{I}''$ definirana kao:

$$
\mathcal{I}'' = \left\{ I \subseteq E \setminus A \,\bigg|\, \exists B \subseteq A,\, B \in \mathcal{I},\, r(B) = r(A),\, I \cup B \in \mathcal{I} \right\}
$$

Kontrakciju možemo shvatiti tako da se elementi skupa $A$ „stegnu”, a zatim promatramo nezavisne skupove koje preostali elementi tvore zajedno s bazom skupa $A$. Rezultat kontrakcije ovisi o bazi skupa $A$; nezavisni skupovi nakon kontrakcije zapravo su nezavisni skupovi dobiveni redukcijom podskupova višeg ranga izvornog matroida.

**Primjer – grafovski matroid**:

-   **Brisanje**: u grafovskom matroidu brisanje odgovara uklanjanju nekih bridova iz grafa. Nakon što iz grafa $G$ uklonimo neki brid, promatramo nezavisne skupove sastavljene od preostalih bridova, tj. skupove bridova bez ciklusa. Na primjer, ako iz grafa-trokuta uklonimo jedan brid, preostala dva brida i dalje čine šumu.

-   **Kontrakcija**: kontrakcija odgovara stezanju brida u jedan vrh. U grafovskom matroidu kontrakcija brida znači spajanje njegovih dvaju krajeva u jedan vrh i uklanjanje tog brida; nakon spajanja vrhova ostali bridovi grafa i dalje mogu tvoriti nezavisne skupove. Na primjer, u grafu-trokutu kontrakcija bilo kojeg brida spaja dva vrha u jedan, a preostala dva brida tvore novi matroid.

## Matroidi i pohlepni algoritam

**Opis problema**:

Jedna od primjena matroida je rješavanje optimizacijskih problema pohlepnim algoritmom. Konkretno, zadan je matroid $M = (S, \mathcal{I})$, gdje je $S$ osnovni skup, a $\mathcal{I}$ familija nezavisnih skupova. Svakom elementu $x \in S$ pridružena je pozitivna cjelobrojna težina $w(x)$, a cilj je pronaći nezavisan skup najveće težine, formalno:

$$
\max_{A \in \mathcal{I}} w(A) = \max_{A \in \mathcal{I}} \sum_{x \in A} w(x)
$$

Očito nezavisan skup najveće težine mora biti maksimalan nezavisan skup. Ako nezavisan skup $A$ nije maksimalan, postoji element $x$ koji se može dodati u $A$, a budući da je $w(x) > 0$, dodavanjem tog elementa težina raste, pa $A$ nije nezavisan skup najveće težine.

### Postupak

Pohlepni algoritam za nezavisan skup najveće težine ima sljedeće korake:

1.  **Sortiranje elemenata**: osnovni skup $S$ sortiramo po težini od najveće do najmanje; dobiveni niz označimo $e_1, e_2, \dots, e_n$.
2.  **Inicijalizacija**: postavimo nezavisan skup $A = \emptyset$.
3.  **Izgradnja nezavisnog skupa**: redom razmatramo sortirane elemente $e_i$; ako je $A \cup \{ e_i \} \in \mathcal{I}$, postavimo $A = A \cup \{ e_i \}$.
4.  **Ispis rezultata**: konačni skup $A$ je nezavisan skup najveće težine.

**Analiza složenosti**:

Neka je $n = |S|$ veličina osnovnog skupa, a $f(n)$ složenost provjere je li skup nezavisan. Vremenska složenost pohlepnog algoritma je:

$$
O(n \log n + n f(n))
$$

pri čemu je $O(n \log n)$ složenost sortiranja, a $O(n f(n))$ složenost uzastopnih provjera nezavisnosti.

???+ note "Napomena"
    -   U grafovskom matroidu za učinkovito otkrivanje ciklusa može se koristiti [DSU (union-find)](../ds/dsu.md), čime $f(n)$ postaje gotovo konstantno.
    -   U linearnom matroidu provjera nezavisnosti obično uključuje operacije s matricama, a njezina složenost ovisi o konkretnoj implementaciji.

**Dokaz ispravnosti**:

Neka je $M = (S, \mathcal{I})$ matroid, $A \in \mathcal{I}$ nezavisan skup i neka je $A$ podskup nekog nezavisnog skupa najveće težine $T$. Definirajmo skup $P = \{ x \in S \setminus A \mid A \cup \{x\} \in \mathcal{I} \}$, tj. skup svih elemenata koji, dodani u $A$, ostavljaju $A$ nezavisnim.

Neka je $y$ element skupa $P$ najveće težine. Tada je i $A' = A \cup \{ y \}$ podskup nekog nezavisnog skupa najveće težine, što dokazujemo ovako:

Pretpostavimo da $A' = A \cup \{ y \}$ nije podskup ni jednog nezavisnog skupa najveće težine. Tada postoji nezavisan skup najveće težine $T$ za koji je $|A'| < |T|$.

Budući da je $|A'|< |T|$, prema **svojstvu zamjene** matroida postoji $x \in T \setminus A'$ takav da je $A' \cup \{ x \} \in \mathcal{I}$.

Koristeći **svojstvo zamjene**, uzastopno dodajemo takve $x$ u $A'$ i na kraju dobivamo novi nezavisan skup $A''$ za koji je $|A''| = |T|$.

Neka je $K = A'' \cap T$; tada je $x = T \setminus K$ i $y = A'' \setminus K$. Budući da je $y$ element skupa $P$ najveće težine, vrijedi $w(x) \leq w(y)$.

Stoga je $w(A'') = w(K) + w(y) \geq w(K) + w(x) = w(T)$, pa:

-   ako je $w(A'') > w(T)$, onda $T$ nije nezavisan skup najveće težine, što proturječi pretpostavci;
-   ako je $w(A'') = w(T)$, onda je $A''$ nezavisan skup najveće težine i $A'$ je njegov podskup, što proturječi pretpostavci da $A'$ nije podskup ni jednog nezavisnog skupa najveće težine.

Dakle, pretpostavka ne vrijedi: $A' = A \cup \{ y \}$ mora biti podskup nekog nezavisnog skupa najveće težine, pa uzastopnom primjenom pohlepne strategije na kraju dobivamo nezavisan skup najveće težine.

### Primjer

**Minimalno razapinjuće stablo**:

Zadan je povezan neusmjereni graf $G = (V, E)$ u kojem svaki brid $e \in E$ ima težinu $w(e)$. Cilj je pronaći razapinjuće stablo koje sadrži sve vrhove i ima najmanju ukupnu težinu.

**Konstrukcija matroida**:

Da bismo problem minimalnog razapinjućeg stabla formulirali kao problem na matroidu, konstruiramo grafovski matroid $M(G)$:

-   **Osnovni skup**: $S = E$, tj. svi bridovi grafa.
-   **Familija nezavisnih skupova**: $\mathcal{I}$ su svi skupovi bridova bez ciklusa (tj. sve šume).

**Pohlepni algoritam**:

U okviru grafovskog matroida [Kruskalov algoritam](../graph/mst.md#kruskalov-algoritam) tipičan je pohlepni algoritam zasnovan na teoriji matroida kojim se može izgraditi minimalno razapinjuće stablo. Iako je i [Primov algoritam](../graph/mst.md#primov-algoritam) učinkovit pohlepni algoritam koji također pronalazi minimalno razapinjuće stablo, on se ne oslanja strogo na matroidnu pohlepnost. Zato je u raspravama o teoriji matroida Kruskalov algoritam glavni primjer pohlepnog algoritma.

-   **Kruskalov algoritam**:
    1.  **Sortiranje bridova**: sve bridove sortiramo po težini od najmanje do najveće.
    2.  **Postupni odabir**: redom biramo brid najmanje težine; ako njegovo dodavanje ne stvara ciklus, dodajemo ga u razapinjuće stablo.
    3.  **Uvjet zaustavljanja**: postupak ponavljamo dok razapinjuće stablo ne sadrži $|V| - 1$ bridova.

-   **Primov algoritam**:
    -   **Načelo**: Primov algoritam kreće od početnog vrha i postupno širi razapinjuće stablo, svaki put birajući brid najmanje težine koji spaja vrh unutar stabla s vrhom izvan stabla.
    -   Iako je i Primov algoritam pohlepan, njegova se strategija odabira razlikuje od ostalih pohlepnih algoritama zasnovanih na svojstvu zamjene matroida. Stoga se u strogom smislu teorije matroida Primov algoritam ne smatra tipičnim matroidnim pohlepnim algoritmom.

## Presjek matroida

Za dva matroida $M_1 = (S, \mathcal{I}_1)$ i $M_2 = (S, \mathcal{I}_2)$ definirana na istom osnovnom skupu $S$, ako $\mathcal{I} = \mathcal{I}_1 \cap \mathcal{I}_2$ zadovoljava tri svojstva familije nezavisnih skupova matroida, onda $M = (S, \mathcal{I})$ nazivamo **presjekom** matroida $M_1$ i $M_2$.

**Napomena**: presjek dvaju proizvoljnih matroida nije nužno matroid; on je matroid samo kada presjek familija nezavisnih skupova zadovoljava tri svojstva iz definicije familije nezavisnih skupova.

### Opis problema

1.  **Najveći nezavisan skup**: u $\mathcal{I}_1 \cap \mathcal{I}_2$ pronaći najveći nezavisan skup (tj. nezavisan skup najveće kardinalnosti).
2.  **Težinski najveći nezavisan skup**: za zadanu težinsku funkciju $w: S \to \mathbb{R}$ u $\mathcal{I}_1 \cap \mathcal{I}_2$ pronaći nezavisan skup najvećeg zbroja težina.

### Algoritam

**Netežinska inačica**:

1.  **Inicijalizacija**: odaberemo početni nezavisan skup $I \in \mathcal{I}_1 \cap \mathcal{I}_2$, obično $I = \emptyset$.
2.  **Iteracija**:
    -   **Izgradnja grafa zamjena**: na temelju trenutačnog nezavisnog skupa $I$ izgradimo graf zamjena (exchange graph) $D_{M_1, M_2}(I)$.
    -   **Odabir puta**: u grafu zamjena pronađemo povećavajući put $P$ od izvora $s$ do ponora $t$.
    -   **Povećanje**: prolazimo put $P$ od $s$ do $t$ vrh po vrh:
        -   ako vrh pripada lijevoj strani (tj. element je skupa $I$), uklanjamo taj element iz $I$;
        -   ako vrh pripada desnoj strani (tj. element je skupa $S \setminus I$), dodajemo taj element u $I$.
    -   **Ponavljanje**: nakon ažuriranja nezavisnog skupa $I$ ponavljamo gornje korake dok se više ne može pronaći novi povećavajući put.
3.  **Rezultat**: konačni nezavisan skup $I$ je najveći nezavisan skup presjeka matroida $M = M_1 \cap M_2$.

**Težinska inačica**:

Da bismo pronašli nezavisan skup najvećeg zbroja težina, algoritam mora pažljivije birati povećavajući put.

1.  **Postavljanje težina**: svakom elementu $e \in S$ pridružimo težinu $w'(e)$ u grafu zamjena:
    -   **vrhovi lijeve strane** (elementi skupa $I$): $w'(e) = -w(e)$;
    -   **vrhovi desne strane** (elementi skupa $S \setminus I$): $w'(e) = w(e)$.
2.  **Odabir puta**: u grafu zamjena $D_{M_1, M_2}(I)$ tražimo **povećavajući put** $P$ od izvora $s$ do ponora $t$ takav da se nakon povećanja duž tog puta ukupna težina nezavisnog skupa $I$ najviše poveća.
    -   **Uvjet povećanja**: zbroj težina elemenata dodanih duž puta $P$ veći je od zbroja težina uklonjenih elemenata, tj. $\sum_{y \in \text{dodani elementi}} w(y) > \sum_{x \in \text{uklonjeni elementi}} w(x)$
3.  **Operacija povećanja**: prolazimo put $P$ od $s$ do $t$ vrh po vrh:
    -   ako vrh pripada lijevoj strani (tj. element je skupa $I$), uklanjamo taj element iz $I$;
    -   ako vrh pripada desnoj strani (tj. element je skupa $S \setminus I$), dodajemo taj element u $I$.
4.  **Iteracija**: ponavljamo korake 1 do 3, iznova gradimo graf zamjena i tražimo povećavajuće putove, postupno povećavajući ukupnu težinu nezavisnog skupa $I$.
5.  **Uvjet zaustavljanja**: algoritam završava kada se u grafu zamjena više ne može pronaći put koji zadovoljava uvjet povećanja.
6.  **Rezultat**: konačni nezavisan skup $I$ je **nezavisan skup najveće težine** presjeka matroida $M = M_1 \cap M_2$.

**Složenost**:

-   **Broj povećanja**: ako su rangovi dvaju matroida $r_1$ i $r_2$, najveći broj povećanja je $\min(r_1, r_2)$.

-   **Složenost jednog povećanja**:
    -   izgradnja grafa zamjena ima složenost $O(n^2)$, gdje je $n = |S|$;
    -   složenost traženja povećavajućeg puta ovisi o strategiji pretraživanja, obično je $O(n^2)$, npr. pretraživanjem u širinu (BFS).

-   **Ukupna vremenska složenost**: ukupna vremenska složenost je $O(r \cdot n^2)$, gdje je $r = \min(r_1, r_2)$.

## Primjeri zadataka

**Minimalno razapinjuće stablo**:

Zadan je neusmjereni graf $G = (V, E)$ u kojem svaki brid $e \in E$ ima težinu $w(e)$. Treba pronaći razapinjuće stablo koje sadrži sve vrhove i ima najmanju ukupnu težinu.

-   Detaljan opis: [Minimalno razapinjuće stablo](../graph/mst.md).
-   Predložak zadatka: [Luogu P3366【模板】最小生成树 (predložak: minimalno razapinjuće stablo)](https://www.luogu.com.cn/problem/P3366).

??? note "Ideja rješenja"
    Koristimo Kruskalov algoritam: sve bridove sortiramo po težini od najmanje do najveće, zatim ih redom biramo i, ako dodavanje brida ne stvara ciklus, dodajemo ga u razapinjuće stablo; dobiveno razapinjuće stablo je minimalno.

**Colorful Graph**:

Zadan je neusmjereni graf $G = (V, E)$ s više boja, pri čemu svaki brid ima boju. Treba pronaći najveći skup bridova takav da:

1.  odabrani bridovi ne tvore nijedan ciklus;
2.  broj bridova svake boje nije veći od $k$ (gdje je $k$ zadani pozitivan cijeli broj).

??? note "Ideja rješenja"
    1.  **Modeliranje matroidima**:
    
        -   **Grafovski matroid ($M_1$)**: definiran kao skupovi bridova koji ne tvore ciklus, tj. familija nezavisnih skupova $\mathcal{I}_1$ sadrži sve skupove bridova bez ciklusa.
        -   **Matroid boja ($M_2$)**: definiran kao skupovi bridova u kojima je broj bridova svake boje najviše $k$, tj. familija nezavisnih skupova $\mathcal{I}_2$ sadrži sve skupove bridova u kojima je broj bridova svake boje $\leq k$.
    2.  **Rješavanje presjeka matroida**: rješavanjem $M = M_1 \cap M_2$ pronalazimo najveći skup bridova koji ne tvori ciklus i u kojem broj bridova svake boje nije veći od $k$.

**Problem raspodjele resursa s ograničenjima**:

U problemu raspodjele resursa zadan je skup resursa $R = \{r_1, r_2, \dots, r_n\}$ i skup projekata $P = \{p_1, p_2, \dots, p_m\}$. Svakom projektu $p_i$ treba dodijeliti određenu količinu resursa, a ukupna dodijeljena količina svakog resursa ne smije premašiti njegovu zalihu.

**Cilj**: pronaći raspodjelu resursa koja zadovoljava potrebe svih projekata i ne premašuje zalihe resursa.

??? note "Ideja rješenja"
    1.  **Modeliranje matroidima**:
    
        -   **Matroid potreba ($M_1$)**: definiran kao raspodjele koje zadovoljavaju potrebe projekata za resursima, tj. familija nezavisnih skupova $\mathcal{I}_1$ sadrži sve skupove dodjela resursa koji zadovoljavaju potrebe projekata.
        -   **Matroid zaliha ($M_2$)**: definiran kao raspodjele koje ne premašuju zalihu nijednog resursa, tj. familija nezavisnih skupova $\mathcal{I}_2$ sadrži sve skupove dodjela resursa koji poštuju ograničenja zaliha.
    2.  **Rješavanje presjeka matroida**: rješavanjem $M = M_1 \cap M_2$ pronalazimo raspodjelu resursa koja zadovoljava potrebe svih projekata i ne premašuje zalihe resursa.

## Literatura i bilješke

1.  [Wikipedia – Matroid](https://en.wikipedia.org/wiki/Matroid)
2.  [Baidu Baike – 拟阵 (matroid)](https://baike.baidu.com/item/%E6%8B%9F%E9%98%B5)
3.  [Luogu – 拟阵与最优化问题 (Matroidi i optimizacijski problemi)](https://www.luogu.com.cn/article/87d02q9f)
4.  [Luogu – 从拟阵基础到 Shannon 开关游戏 (Od osnova matroida do Shannonove igre prekidača)](https://www.luogu.com.cn/article/fuj3x886)
