---
title: Booleova algebra
---

U matematičkoj logici Booleova algebra (Boolean algebra) grana je algebre. U elementarnoj algebri vrijednosti varijabli su brojevi, a glavne operacije koje se proučavaju jesu zbrajanje, množenje, potenciranje i njihove inverzne operacije. U Booleovoj algebri varijable poprimaju samo dvije vrijednosti, **istina** i **laž** (obično se označavaju $1$ i $0$), a glavne operacije koje se proučavaju jesu konjunkcija (i, $\land$), disjunkcija (ili, $\lor$) i negacija (ne, $\lnot$). Kao što je elementarna algebra formalizam za opisivanje operacija s brojevima, tako je Booleova algebra formalizam za opisivanje logičkih operacija.

## Booleove funkcije

???+ abstract "Definicija"
    **Booleova funkcija** (Boolean function) funkcija je oblika $f:\mathbf{B}^k\to \mathbf{B}$, gdje je $\mathbf{B}=\{0,1\}$ **Booleova domena** (Boolean domain), a nenegativni cijeli broj $k$ **arnost** (arity) te Booleove funkcije. Booleova funkcija s $k=1$ jest unarna funkcija, i tako dalje. Za $k=0$ smatramo da se funkcija degenerira u konstantu iz $\mathbf{B}$.

Uglavnom proučavamo samo unarne i binarne Booleove funkcije. Ako nije drukčije rečeno, Booleove funkcije u nastavku ograničene su na unarni i binarni slučaj.

Osim uobičajenim zapisom funkcije, Booleove funkcije možemo prikazati i **tablicom istinitosti** (truth table), **logičkim vratima** (logic gate) i [Vennovim dijagramom](https://en.wikipedia.org/wiki/Venn_diagram).

???+ abstract "Tablica istinitosti"
    Za Booleovu funkciju nabrojimo sve slučajeve njezinih ulaza te ulaze i pripadne izlaze popišemo u tablicu; ta se tablica naziva tablica istinitosti.

$n$-arna Booleova funkcija može se prikazati i **propozicijskom formulom** (propositional formula) s $n$ varijabli; propozicijske formule $p$ i $q$ **logički su ekvivalentne** (logically equivalent) ako i samo ako opisuju istu Booleovu funkciju, što zapisujemo $p\iff q$.

Slijede neke česte Booleove funkcije; te Booleove funkcije zajednički nazivamo i **logičkim veznicima** (logical connective) ili **logičkim operatorima** (logical operator):

| Naziv (matematička logika)                                           | Drugi nazivi                 | Oznaka                               |
| -------------------------------------------------- | -------------------- | -------------------------------- |
| tautologija (truth, tautology)                                |                      | $\top$                           |
| kontradikcija (falsity, contradiction)                          |                      | $\bot$                           |
| propozicija                                                 | identitet                   | $A$                              |
| negacija (negation)                                       | ne (NOT)               | $\lnot A$                        |
| konjunkcija (conjunction)                                    | i (AND)               | $A \land B$                      |
| disjunkcija (disjunction)                                    | ili (OR)                | $A \lor B$                       |
| nekonjunkcija (non-conjunction)                               | ni (NAND), Shefferova crta  | $A \bar{\land} B$, $A\uparrow B$  |
| nedisjunkcija (non-disjunction)                               | nili (NOR)              | $A \bar{\lor} B$, $A\downarrow B$ |
|                                                    | isključivo ili (exclusive OR, XOR) | $A \oplus B$                     |
|                                                    | isključivo nili (exclusive NOR)    | $A \odot B$                      |
| materijalna implikacija (material implication)[^note1]                 |                      | $A \to B$                        |
| materijalna neimplikacija (material nonimplication)[^note1]             |                      | $A \nrightarrow B$               |
| obratna implikacija (converse implication)[^note1]                  |                      | $A \gets B$                      |
| obratna neimplikacija (converse nonimplication)[^note1]              |                      | $A \nleftarrow B$                |
| bikondicional (biconditional), ekvivalencija (equivalence)[^note1][^note2] |                      | $A \leftrightarrow B$            |
| neekvivalencija (non-equivalence)[^note1][^note3]               |                      | $A \nleftrightarrow B$           |

Pripadne tablice istinitosti (izvor: [Wikipedia](https://commons.wikimedia.org/wiki/File:Logical_connectives_table.svg)):

![](./images/logical-connectives-table.svg)

Pripadni Vennovi dijagrami i [Hasseov dijagram](./order-theory.md#偏序集的可视化表示hasse-图) (s relacijom inkluzije skupova $\subseteq$ kao parcijalnim uređajem; izvor: [Wikipedia](https://en.wikipedia.org/wiki/File:Logical_connectives_Hasse_diagram.svg)):

![](./images/logical-connectives-hasse-diagram.svg)

Budući da $n$-arna Booleova funkcija ima $2^n$ mogućih ulaza, postoji $2\uparrow (2\uparrow n)$ $n$-arnih Booleovih funkcija, gdje je $\uparrow$ Knuthova strelica.

Kombinaciju logičkih operatora nazivamo **logičkim izrazom** (logical expression).

Ako $\mathbf{B}$ promatramo kao [klase ostataka](./number-theory/basic.md#同余类与剩余系) po modulu $2$, tada je isključivo ili ekvivalentno zbrajanju po modulu $2$, a i množenju po modulu $2$, pa Booleovu domenu ponekad označavamo i $\mathbf{Z}_2$.

### Prioritet

Unarni logički operatori imaju viši prioritet od binarnih, tj. $\lnot$ ima viši prioritet od $\land$, $\lor$, $\oplus$ itd.

Za prioritet među binarnim logičkim operatorima postoji više konvencija: neki izvori smatraju da $\land$, $\lor$, $\oplus$ imaju viši prioritet od $\to$, $\gets$, $\leftrightarrow$, a drugi zastupaju suprotno. Stoga se pri uporabi preporučuje dodavati zagrade kako bi redoslijed bio jasan.

Za pravila u C++-u pogledajte [Tablicu prioriteta operatora u C++-u](../lang/op.md#c-运算符优先级总表).

### Dostatni operatori i funkcionalno potpuni skupovi operatora

Zapravo, sve ostale logičke operatore možemo izraziti samo pomoću NAND-a ili samo pomoću NOR-a, a na tome se temelji i konstrukcija CPU-a. Međutim, budući da četiri logička operatora **i, ili, ne, isključivo ili** imaju bolja svojstva, pri proučavanju Booleove algebre obično koristimo samo te četiri funkcije.

??? example "Kako ostale logičke operatore izraziti pomoću NAND-a odnosno NOR-a"
    Vrijedi
    
    -   $\lnot p=p\bar{\land} p=p\bar{\lor} p$,
    -   $p\land q=(p\bar{\land}q)\bar{\land}(p\bar{\land}q)=(p\bar{\lor}p)\bar{\lor}(q\bar{\lor}q)$,
    -   $p\lor q=(p\bar{\land}p)\bar{\land}(q\bar{\land}q)=(p\bar{\lor}q)\bar{\lor}(p\bar{\lor}q)$,
    -   $p\to q=p\bar{\land} (q\bar{\land} q)=((p\bar{\lor}p)\bar{\lor}q)\bar{\lor}((p\bar{\lor}p)\bar{\lor}q)$.
    
    Osim toga
    
    -   $p=\lnot\lnot p$,
    -   $p\nleftrightarrow q=p\oplus q=(p\lor q)\land\lnot (p\land q)$,
    -   $p\leftrightarrow q=p\odot q=\lnot(p\oplus q)$,
    -   $p\nrightarrow q=\lnot(p\to q)$,
    -   $p\gets q=q\to p$,
    -   $p\nleftarrow q=\lnot(p\gets q)$.

Možemo li zadanim skupom logičkih operatora opisati sve logičke operatore? To nas dovodi do definicije funkcionalno potpunog skupa operatora.

???+ abstract "Definicija"
    Ako se za zadani skup logičkih operatora svi logički operatori mogu opisati samo funkcijama iz tog skupa, taj se skup naziva **funkcionalno potpun skup operatora** (functionally complete operator set). Posebno, ako se svi logički operatori mogu opisati jednim jedinim logičkim operatorom, taj se operator naziva **dostatni operator** (sole sufficient operator) ili **Shefferova funkcija** (Sheffer function).
    
    Ako se uklanjanjem bilo kojeg elementa iz funkcionalno potpunog skupa operatora više ne mogu opisati svi logički operatori, taj se skup naziva **minimalni funkcionalno potpun skup operatora** (minimal functionally complete operator set).

Može se dokazati da su među logičkim operatorima samo $\bar{\land}$ i $\bar{\lor}$ dostatni operatori.

Slijede uobičajeni minimalni funkcionalno potpuni skupovi operatora[^vaughan1942complete]:

-   $\{\bar{\land}\}$, $\{\bar{\lor}\}$,
-   $\{\land,\lnot\}$, $\{\lor,\lnot\}$, $\{\gets,\lnot\}$, $\{\to,\lnot\}$, $\{\nleftarrow,\lnot\}$, $\{\nrightarrow,\lnot\}$,
-   $\{\gets,\bot\}$, $\{\to,\bot\}$, $\{\nleftarrow,\top\}$, $\{\nrightarrow,\top\}$,
-   $\{\gets,\nleftarrow\}$, $\{\to,\nleftarrow\}$, $\{\gets,\nrightarrow\}$, $\{\to,\nrightarrow\}$,
-   $\{\gets,\nleftrightarrow\}$, $\{\to,\nleftrightarrow\}$, $\{\nleftarrow,\leftrightarrow\}$, $\{\nrightarrow,\leftrightarrow\}$,
-   $\{\lor,\leftrightarrow,\bot\}$, $\{\lor,\leftrightarrow,\nleftrightarrow\}$, $\{\lor,\nleftrightarrow,\top\}$,
-   $\{\land,\leftrightarrow,\bot\}$, $\{\land,\leftrightarrow,\nleftrightarrow\}$, $\{\land,\nleftrightarrow,\top\}$.

### Svojstva

Najprije svojstva vezana uz algebarske strukture:

-   I i ili na $\mathbf{B}$ čine [komutativni monoid](./algebra/basic.md#群). Dakle, operacije i i ili komutativne su, asocijativne i imaju neutralni element ($x\land 1=x\lor 0=x$).
-   Isključivo ili i isključivo nili na $\mathbf{B}$ čine [grupu](./algebra/basic.md#群). Dakle, operacije isključivo ili i isključivo nili komutativne su, asocijativne, imaju neutralni element ($x\oplus 0=x\odot 1=x$) i inverzni element ($x\oplus x=0$, $x\odot x=1$).
-   NAND i NOR nisu asocijativni, pa ne čine polugrupu.

Za $\land$ i $\lor$ vrijedi

-   distributivnost:
    -   $a\land(b\diamond c)=(a\land b)\diamond (a\land c)$, gdje $\diamond$ može biti $\land$, $\lor$, $\oplus$,
    -   $a\lor(b\diamond c)=(a\lor b)\diamond (a\lor c)$, gdje $\diamond$ može biti $\land$, $\lor$, $\odot$.
-   **idempotentnost** (idempotence): $x\land x=x$, $x\lor x=x$.
-   monotonost: $a\to b\iff(a\land c)\to(b\land c)$, $a\to b\iff(a\lor c)\to(b\lor c)$.
-   **apsorpcija** (absorption): $x\land(x\lor y)=x\lor(x\land y)=x$.
-   odnos prema „$\to$”:
    -   $a \lor b \iff (\lnot a \to b) \land (\lnot b \to a)$,
    -   $a \land b \iff \lnot((a \to \lnot b) \lor (b \to \lnot a))$.

???+ abstract "Monotonost Booleove funkcije"
    Za Booleovu funkciju $f(x_1,\dots,x_n)$ i dva elementa $(a_1,\dots,a_n),(b_1,\dots,b_n)$ iz $\mathbf{B}^n$, ako iz $a_i\leq b_i,~~\forall i=1,\dots,n$ uvijek slijedi $f(a_1,\dots,a_n)\leq f(b_1,\dots,b_n)$, kažemo da je ta Booleova funkcija monotona.

Vrijede i sljedeća svojstva:

-   **zakon isključenja trećega** (law of excluded middle): $p\lor\lnot p$ je tautologija.
-   $\lnot p\iff p\to\bot$.
-   dvostruka negacija / **involutivnost** (involution) od $\lnot$: $\lnot\lnot x=x$.
-   involutivnost od $\oplus$ i $\odot$: $x\oplus y\oplus y=x$, $x\odot y\odot y=x$.
-   De Morganovi zakoni: $\lnot(p\land q)=\lnot p\lor \lnot q$, $\lnot(p\lor q)=\lnot p\land \lnot q$.

## Normalizacija logičkih izraza

Na temelju gornjih svojstava logičke izraze možemo ekvivalentno preoblikovati tako da zadovoljavaju određenu normalnu formu, što se koristi u automatskom dokazivanju teorema. Uobičajene normalne forme jesu **konjunktivna normalna forma** (conjunctive normal form, CNF), **disjunktivna normalna forma** (disjunctive normal form, DNF) i **algebarska normalna forma** (algebraic normal form, ANF).

???+ abstract "Konjunktivna i disjunktivna normalna forma"
    Definiramo rekurzivno:
    
    1.  **Literal** (literal): za varijablu $x$, $x$ i $\lnot x$ su literali.
    2.  Klauzula:
        -   literal je klauzula,
        -   ako je $A$ literal, a $B$ klauzula, tada je $A\lor B$ klauzula.
    3.  Konjunktivna normalna forma:
        -   ako je $A$ klauzula, tada je $(A)$ konjunktivna normalna forma,
        -   ako je $A$ klauzula, a $B$ konjunktivna normalna forma, tada je $(A)\land B$ konjunktivna normalna forma.
    
    Analogno, zamjenom $\land$ i $\lor$ u gornjoj definiciji dobivamo definiciju disjunktivne normalne forme.

Na primjer, sljedeći su logički izrazi u disjunktivnoj normalnoj formi:

-   $(A\land\lnot B)\lor(C\land D\land\lnot E)$,
-   $(A\land B)\lor (C)$,
-   $(A\land B)$,
-   $(A)$.

Sljedeći su logički izrazi u konjunktivnoj normalnoj formi:

-   $(\lnot A\lor\lnot B\lor C)\land(\lor D\lor\lnot E)$,
-   $(A\lor B)\land (C)$,
-   $(A\lor B)$,
-   $(A)$.

Sljedeći logički izrazi nisu ni u konjunktivnoj ni u disjunktivnoj normalnoj formi:

-   $\lnot(A\land B)$,
-   $A\land (B\lor (C\land D))$.

Sljedećim koracima možemo bilo koji logički izraz koji sadrži samo operacije $\lnot$, $\land$, $\lor$ preoblikovati u DNF:

$$
\begin{array}{rcccl}
    \lnot\lnot x &&\mapsto&& x,\\
    \lnot(x\lor y) &&\mapsto&& \lnot x\land \lnot y,\\
    \lnot(x\land y) &&\mapsto&& \lnot x\lor \lnot y,\\
    x\land(y\lor z) &&\mapsto&& (x\land y)\lor (x\land z),\\
    (x\lor y)\land z &&\mapsto&& (x\land z)\lor (y\land z).
\end{array}
$$

Da bismo dobili CNF izraza $X$, dovoljno je dobiti DNF od $\lnot X$, negirati ga i primijeniti De Morganove zakone.

???+ abstract "Algebarska normalna forma"
    Najprije sljedećom rekurzivnom definicijom definiramo monom:
    
    -   varijabla $x$ je monom,
    -   ako je $A$ monom, a $x$ varijabla, tada je $x\land A$ monom.
    
    Logički izraz koji je jednog od sljedećih triju oblika jest algebarska normalna forma:
    
    1.  $1$, $0$,
    2.  isključivo ili nekoliko neekvivalentnih monoma, npr. $a\oplus b\oplus(a\land b)\oplus(a\land b\land c)$,
    3.  isključivo ili nekoliko neekvivalentnih monoma i jedne jedine $1$, npr. $1\oplus a\oplus b\oplus(a\land b)\oplus(a\land b\land c)$.

Uočimo da algebarske normalne forme bijektivno odgovaraju polinomima nad $\mathbf{Z}_2$, pa se algebarska normalna forma naziva i **Žegalkinov polinom** (Zhegalkin polynomial).

Sljedećim koracima možemo bilo koji logički izraz koji sadrži samo operacije $\lnot$, $\land$, $\lor$, $\oplus$ preoblikovati u ANF:

1.  $\oplus$: izravno raspišemo, npr. $(1\oplus x)\oplus(1\oplus x\oplus y)=1\oplus x\oplus 1\oplus x\oplus y=y$,
2.  $\land$: raspišemo distributivnošću, npr. $x\land(1\oplus x\oplus y)=(x\land 1)\oplus (x\land x)\oplus (x\land y)=x\oplus (x\land y)$,
3.  $\lnot$: $\lnot x$ zamijenimo s $1\oplus x$, npr. $\lnot(1\oplus x\oplus y)=1\oplus 1\oplus x\oplus y=x\oplus y$,
4.  $\lor$: $x\lor y$ zamijenimo s $1\oplus((1\oplus x)\land(1\oplus y))$ ili $x\oplus y\oplus (x\land y)$, npr. $(1\oplus x)\lor(1\oplus x\oplus y)=1\oplus((1\oplus 1\oplus x)\land(1\oplus 1\oplus x\oplus y))=1\oplus x\oplus(x\land y)$.

## Literatura i napomene

1.  [Boolean algebra - Wikipedia](https://en.wikipedia.org/wiki/Boolean_algebra)
2.  [Boolean function - Wikipedia](https://en.wikipedia.org/wiki/Boolean_function)
3.  [Logical connective - Wikipedia](https://en.wikipedia.org/wiki/Logical_connective)
4.  [Disjunctive normal form - Wikipedia](https://en.wikipedia.org/wiki/Disjunctive_normal_form)
5.  [Zhegalkin polynomial - Wikipedia](https://en.wikipedia.org/wiki/Zhegalkin_polynomial)

[^note1]: Pri izvođenju propozicija treba koristiti dvostruke dugačke strelice, npr. $A\implies B$, $A\impliedby B$, $A\iff B$ itd.

[^note2]: Ekvivalentno isključivom nili.

[^note3]: Ekvivalentno isključivom ili.

[^vaughan1942complete]: Vaughan, H. E. (1942). Complete sets of logical functions.*Transactions of the American Mathematical Society 51*: 117–32.
