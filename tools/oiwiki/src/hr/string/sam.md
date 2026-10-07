---
title: Sufiksni automat (SAM)
---

## Oznake

-   $\Sigma$: abeceda. Veličinu abecede označavamo $|\Sigma|$.
-   $s$: niz znakova. Duljina niza je $|s| = n$, indeksi počinju od $0$.
-   $t_0$: početno stanje.
-   $\operatorname{endpos}(t)$: skup završnih pozicija podniza $t$ u nizu $s$.
-   $\operatorname{link}(v)$: sufiksna poveznica stanja $v$.
-   $\operatorname{len}(v)$: duljina najduljeg podniza koji odgovara stanju $v$.
-   $\operatorname{longest}(v)$: najdulji podniz koji odgovara stanju $v$.
-   $\operatorname{minlen}(v)$: duljina najkraćeg podniza koji odgovara stanju $v$.
-   $\operatorname{shortest}(v)$: najkraći podniz koji odgovara stanju $v$.

## Pregled sufiksnog automata

**Sufiksni automat** (suffix automaton, SAM) moćna je struktura podataka kojom se može riješiti mnogo problema vezanih uz nizove znakova.

Primjerice, sljedeći se problemi na nizovima mogu pomoću SAM-a riješiti u linearnom vremenu:

-   pronaći sva pojavljivanja jednog niza u drugom nizu;
-   izračunati koliko različitih podnizova ima zadani niz.

Intuitivno, SAM niza može se shvatiti kao sažeti oblik **svih podnizova** zadanog niza. Vrijedi istaknuti da SAM sve te informacije pohranjuje u izrazito sažetom obliku. Za niz duljine $n$ njegova je prostorna složenost samo $O(n)$. Štoviše, i vremenska složenost izgradnje SAM-a iznosi samo $O(n)$. Preciznije, za $n\ge 3$ SAM ima najviše $2n-1$ čvorova i $3n-4$ prijelaza.

## Definicija

SAM niza $s$ najmanji je [DFA](../misc/fsm.md#确定性有限状态自动机) koji prihvaća sve sufikse niza $s$.

Drugim riječima:

-   SAM je usmjereni aciklički graf. Čvorovi se nazivaju **stanja**, a bridovi **prijelazi** među stanjima.
-   Graf ima izvor $t_0$, koji se naziva **početno stanje**, i svi su ostali čvorovi dostupni iz $t_0$.
-   Svaki je **prijelaz** označen nekim znakom. Svi prijelazi iz istog čvora međusobno su **različiti**.
-   Postoji jedno ili više **završnih stanja**. Ako iz početnog stanja $t_0$ prijelazima na kraju stignemo u završno stanje, spoj oznaka svih prijelaza na tom putu nužno je sufiks niza $s$. Obrnuto, svaki sufiks niza $s$ može se dobiti nekim putem od $t_0$ do nekog završnog stanja.
-   Među svim automatima koji zadovoljavaju gornje uvjete SAM ima najmanji broj čvorova.

Ključ SAM-a upravo je u toj minimalnosti. Zapravo, i izravna izgradnja [trieja](./trie.md) nad svim sufiksima niza $s$ (tzv. sufiksni trie) daje DFA koji prihvaća sve sufikse niza $s$. No u najgorem slučaju tako dobiveni automat ima $\Theta(n^2)$ čvorova, što je neprihvatljivo. Iz primjera u nastavku vidi se da u DFA-u dobivenom izgradnjom trieja nad svim sufiksima mnogo čvorova ponavlja iste informacije, pa se mogu spojiti. SAM to spajanje čvorova dovodi do krajnosti i tako veličinu dobivenog DFA-a drži u $O(n)$. U tom je smislu SAM „sažeti” trie svih sufiksa niza.

### Podnizovi i putovi

Najjednostavnije i ujedno najvažnije svojstvo SAM-a jest da sadrži informacije o svim podnizovima niza $s$. Za svaki put koji počinje u početnom stanju $t_0$, ako zapišemo oznake svih prijelaza na njemu, dobivamo **podniz** niza $s$. Obrnuto, svaki podniz niza $s$ odgovara nekom putu koji počinje u $t_0$.

Radi jednostavnosti kažemo da podniz **odgovara** tom putu (koji počinje u $t_0$ i čije oznake prijelaza čine taj podniz). Obrnuto, kažemo da svaki put **odgovara** nizu koji čine njegove oznake.

Do nekog stanja može voditi više putova, pa kažemo da stanje odgovara skupu nizova, pri čemu nizovi iz tog skupa odgovaraju tim putovima.

### Jednostavni primjeri

Ovdje ćemo prikazati sufiksne automate nekoliko jednostavnih nizova.

Početno stanje označeno je plavom, a završna stanja zelenom bojom.

Za niz $s=\varepsilon$:

![](./images/SAM/SA.svg)

Za niz $s=\texttt{a}$:

![](./images/SAM/SAa.svg)

Za niz $s=\texttt{aa}$:

![](./images/SAM/SAaa.svg)

Za niz $s=\texttt{ab}$:

![](./images/SAM/SAab.svg)

Za niz $s=\texttt{abb}$:

![](./images/SAM/SAabb.svg)

Za niz $s=\texttt{abbb}$:

![](./images/SAM/SAabbb.svg)

U posljednjem se primjeru vidi da bi, kad bismo izravno izgradili trie svih sufiksa, putovi $\texttt{bbb}$ i $\texttt{abbb}$ vodili u različite čvorove; no oba su ta čvora završna stanja i, koji god znak dodali, ne možemo dobiti dulje podudaranje, što znači da se ta dva čvora u pogledu prijelaza automata ponašaju jednako te se mogu spojiti u jedan čvor. Tako se dobiva SAM prikazan na slici. U nastavku ćemo ideju spajanja čvorova proširiti na sve slučajeve i pokazati da, uz razumno spajanje čvorova, konačni SAM ima samo $O(n)$ čvorova i prijelaza.

## Algoritam izgradnje linearne složenosti

Prije nego što opišemo algoritam izgradnje SAM-a u linearnom vremenu, moramo uvesti dva pojma iznimno važna za razumijevanje postupka izgradnje i ukratko dokazati njihova svojstva. Završne pozicije $\operatorname{endpos}$ definiraju čvorove SAM-a (tj. daju nužan i dovoljan uvjet za spajanje čvorova), a sufiksna poveznica $\operatorname{link}$ samo je prirodna inačica [pokazivača neuspjeha](./ac-automaton.md#失配指针) iz Aho–Corasick automata u SAM-u.

### Završne pozicije `endpos`

Promotrimo proizvoljan neprazan podniz $t$ niza $s$ i označimo s $\operatorname{endpos}(t)$ skup svih završnih pozicija podniza $t$ u nizu $s$ (pretpostavljamo da se znakovi niza indeksiraju od nule). Primjerice, za niz $\texttt{abcbc}$ vrijedi $\operatorname{endpos}(\texttt{bc})=\{2,4\}$.

Dva podniza $t_1$ i $t_2$ mogu imati potpuno iste završne pozicije: $\operatorname{endpos}(t_1)=\operatorname{endpos}(t_2)$. To definira relaciju ekvivalencije među podnizovima niza $s$. Svi neprazni podnizovi niza $s$ mogu se prema svojim skupovima završnih pozicija $\operatorname{endpos}$ podijeliti u **klase ekvivalencije**.

Činjenica je da svaka takva klasa ekvivalencije odgovara jednom stanju SAM-a[^state-endpos]. Drugim riječima, čim dva podniza imaju iste završne pozicije, njihovi putovi u SAM-u završavaju u istom stanju. Rečeno drukčije, svako nepočetno stanje SAM-a odgovara jednom ili više nepraznih podnizova s istim $\operatorname{endpos}$. Ukratko, stanja SAM-a upravo su klase ekvivalencije svih nepraznih podnizova, uz dodatak početnog stanja.

Prihvatimo zasad tu činjenicu; na njoj ćemo temeljiti algoritam izgradnje SAM-a. Pokazat ćemo i da su sva svojstva koja SAM mora zadovoljavati, osim minimalnosti, ispunjena; minimalnost pak slijedi iz [Myhill–Nerodeova teorema](../misc/fsm.md#myhillnerode-定理).

Iz vrijednosti $\operatorname{endpos}$ možemo izvesti nekoliko važnih zaključaka koji objašnjavaju odnos među različitim podnizovima koji odgovaraju istom stanju.

???+ note "Lema 1"
    Dva neprazna podniza $u$ i $w$ niza $s$ (pretpostavimo $\left|u\right|\le \left|w\right|$) imaju isti $\operatorname{endpos}$ ako i samo ako se niz $u$ pri svakom pojavljivanju u $s$ pojavljuje kao sufiks niza $w$.

??? note "Dokaz"
    Lema je očita. Ako $u$ i $w$ imaju isti $\operatorname{endpos}$, onda je $u$ sufiks niza $w$ i u $s$ se pojavljuje samo kao sufiks niza $w$. Obrnuto, prema definiciji, ako je $u$ sufiks niza $w$ i u $s$ se pojavljuje samo kao sufiks niza $w$, onda ta dva podniza imaju isti $\operatorname{endpos}$.

???+ note "Lema 2"
    Promotrimo dva neprazna podniza $u$ i $w$ (pretpostavimo $\left|u\right|\le \left|w\right|$). Tada je ili $\operatorname{endpos}(u)\cap \operatorname{endpos}(w)=\varnothing$ ili $\operatorname{endpos}(w)\subseteq \operatorname{endpos}(u)$, ovisno o tome je li $u$ sufiks niza $w$:
    
    $$
    \begin{cases}
    \operatorname{endpos}(w) \subseteq \operatorname{endpos}(u), & \text{if } u \text{ is a suffix of } w, \\
    \operatorname{endpos}(w) \cap \operatorname{endpos}(u) = \varnothing, & \text{otherwise}.
    \end{cases}
    $$

??? note "Dokaz"
    Ako skupovi $\operatorname{endpos}(u)$ i $\operatorname{endpos}(w)$ imaju bar jedan zajednički element, onda nizovi $u$ i $w$ završavaju na istoj poziciji, pa je $u$ sufiks niza $w$. Stoga se na svakoj poziciji na kojoj se pojavljuje $w$ pojavljuje i podniz $u$. Dakle $\operatorname{endpos}(w)\subseteq \operatorname{endpos}(u)$.

???+ note "Lema 3"
    Promotrimo jednu klasu ekvivalencije podnizova s istim $\operatorname{endpos}$ i poredajmo sve podnizove u klasi po padajućoj duljini. Tada je svaki podniz točno za $1$ kraći od prethodnoga i ujedno je sufiks prethodnoga. Drugim riječima, za bilo koja dva podniza iste klase ekvivalencije kraći je sufiks duljega, a duljine podnizova u klasi su uzastopne i poprimaju sve cjelobrojne vrijednosti nekog intervala.

??? note "Dokaz"
    Ako klasa ekvivalencije sadrži samo jedan podniz, lema očito vrijedi. Razmotrimo sada klase ekvivalencije s više od $1$ podniza.
    
    Prema lemi 1, od dvaju različitih nizova s istim $\operatorname{endpos}$ jedan je nužno dulji, a drugi kraći, i kraći je uvijek pravi sufiks duljega. Dakle, u klasi ekvivalencije nema nizova jednake duljine.
    
    Neka je $w$ najdulji niz u klasi, a $u$ najkraći. Prema lemi 1, niz $u$ pravi je sufiks niza $w$. Promotrimo sada proizvoljan sufiks niza $w$ duljine iz intervala $[\left|u\right|,\left|w\right|]$. Lako se vidi da je i taj sufiks u istoj klasi ekvivalencije, jer se u nizu $s$ može pojaviti samo kao sufiks niza $w$ (zato što se kraći sufiks $u$ u $s$ pojavljuje samo kao sufiks niza $w$). Stoga, prema lemi 1, taj sufiks i niz $w$ imaju isti $\operatorname{endpos}$.

Ukratko: podnizovi koji odgovaraju istom stanju imaju međusobno različite duljine koje čine uzastopne prirodne brojeve, a kraći su uvijek sufiksi duljih podnizova.

### Sufiksna poveznica `link`

Promotrimo neko stanje $v\neq t_0$ u SAM-u. Već znamo da stanje $v$ odgovara klasi ekvivalencije podnizova s istim $\operatorname{endpos}$. Ako s $w$ označimo najdulji od tih nizova, svi su ostali nizovi sufiksi niza $w$.

Znamo i da prvih nekoliko sufiksa niza $w$ (gledano po padajućoj duljini) pripada toj klasi ekvivalencije, dok su ostali sufiksi (barem jedan — prazni sufiks) u drugim klasama. Neka je $t$ najdulji među tim ostalim sufiksima; tada sufiksnu poveznicu stanja $v$ usmjeravamo na stanje koje odgovara klasi ekvivalencije niza $t$.

Drugim riječima, stanje na koje pokazuje **sufiksna poveznica** $\operatorname{link}(v)$ stanja $v$ odgovara najduljem sufiksu niza $w$ čiji se skup $\operatorname{endpos}$ razlikuje od njegova, odnosno najduljem sufiksu niza $w$ koji se u $s$ pojavljuje više puta nego $w$.

Radi jednostavnosti dogovorimo se da klasa ekvivalencije početnog stanja $t_0$ sadrži samo prazni niz te da je $\operatorname{endpos}(t_0)=\{-1,0,\ldots,\left|s\right|-1\}$.

???+ note "Lema 4"
    Sve sufiksne poveznice tvore stablo s korijenom $t_0$.

??? note "Dokaz"
    Promotrimo proizvoljno stanje $v\neq t_0$; stanje na koje pokazuje sufiksna poveznica $\operatorname{link}(v)$ odgovara strogo kraćim nizovima (definicija sufiksne poveznice, lema 3). Stoga, krećući se po sufiksnim poveznicama, uvijek stižemo u početno stanje $t_0$ koje odgovara praznom nizu.

???+ note "Lema 5"
    Stablo čiji su čvorovi skupovi $\operatorname{endpos}$, a bridovi relacija sadržavanja među skupovima (tj. skup $\operatorname{endpos}$ svakog djeteta sadržan je u skupu $\operatorname{endpos}$ roditelja) jednako je stablu izgrađenom od sufiksnih poveznica $\operatorname{link}$.

??? note "Dokaz"
    Prema lemi 2, skupovi $\operatorname{endpos}$ bilo kojeg SAM-a tvore stablo (jer su dva skupa ili disjunktna ili je jedan podskup drugoga).
    
    Promotrimo sada proizvoljno stanje $v\neq t_0$ i njegovu sufiksnu poveznicu $\operatorname{link}(v)$; iz definicije sufiksne poveznice i leme 2 dobivamo
    
    $$
    \operatorname{endpos}(v)\subsetneq \operatorname{endpos}(\operatorname{link}(v)).
    $$
    
    Uočimo da ovdje treba stajati $\subsetneq$, a ne $\subseteq$, jer kad bi bilo $\operatorname{endpos}(v)=\operatorname{endpos}(\operatorname{link}(v))$, stanja $v$ i $\operatorname{link}(v)$ trebala bi biti spojena u jedan čvor.
    
    Štoviše, $\operatorname{endpos}(\operatorname{link}(v))$ upravo je najmanji skup $\operatorname{endpos}$ koji pravo sadrži $\operatorname{endpos}(v)$.

Zajedno s prethodnim lemama slijedi: stablo sufiksnih poveznica u biti je stablo skupova $\operatorname{endpos}$.

Slijedi **primjer** stabla sufiksnih poveznica koje nastaje izgradnjom SAM-a za niz $\texttt{abcbc}$; čvorovi su označeni najduljim podnizom pripadne klase ekvivalencije.

![](./images/SAM/SA_suffix_links.svg)

Steknemo li uz sliku određeni osjećaj za sufiksni automat, to će pomoći u razumijevanju algoritma izgradnje i primjena u nastavku.

???+ example "Objašnjenje slike"
    -   U SAM-u postoji najdulji put čije su oznake upravo sam niz $\texttt{abcbc}$. Taj put počinje u početnom stanju, a svako stanje kroz koje prolazi odgovara nekom prefiksu niza $\texttt{abcbc}$ ($\varepsilon,\texttt{a},\texttt{ab},\texttt{abc},\texttt{abcb},\texttt{abcbc}$). Ta su stanja ključna u kasnijim [primjenama](#stablo-sufiksnih-poveznica).
    -   Stablo sufiksnih poveznica može se shvatiti kao „sažetak” putova kojima se ta „prefiksna stanja” po sufiksnim poveznicama kreću prema korijenu (tj. početnom stanju).
    
        -   Duž svakog takvog puta skupovi nizova koji odgovaraju čvorovima čine particiju skupa svih sufiksa pripadnog prefiksa. Primjerice, put od stanja označenog $\texttt{abcbc}$ po sufiksnim poveznicama do korijena glasi $\texttt{abcbc}\rightarrow\texttt{bc}\rightarrow\varepsilon$. Pritom čvor $\texttt{abcbc}$ zapravo odgovara skupu nizova $\{\texttt{abcbc},\texttt{bcbc},\texttt{cbc}\}$, čvor $\texttt{bc}$ skupu $\{\texttt{bc},\texttt{c}\}$, a čvor $\varepsilon$ praznom nizu.
        -   Različiti putovi mogu dijeliti isti čvor, i zato govorimo o „sažimanju”. Primjerice, putovi $\texttt{abc}\rightarrow\texttt{bc}\rightarrow\varepsilon$ i $\texttt{abcbc}\rightarrow\texttt{bc}\rightarrow\varepsilon$ dijele čvor $\texttt{bc}$. Razlog je to što je $\operatorname{endpos}(\texttt{bc})=\{2,4\}$, a nizu $\texttt{bc}$ koji završava na poziciji $2$ neposredno prethodi znak $\texttt{a}$, dok nizu $\texttt{bc}$ koji završava na poziciji $4$ neposredno prethodi znak $\texttt{c}$; stoga se pri dodavanju znaka sprijeda (tj. kretanju suprotno od sufiksnih poveznica) skup završnih pozicija (tj. stanje) razdvaja.
        -   Stablo sufiksnih poveznica treba samo razumno „sažeti” te sufiksne putove, bez razmatranja drugih čvorova. Naime, svaki je podniz sufiks nekog prefiksa, pa se nužno pojavljuje na nekom takvom putu. Algoritam izgradnje u nastavku u biti dodaje znak po znak i za svaki novi prefiks gradi takav sufiksni put te ga razumno „sažima” u već postojeće putove (tj. ne gradi ponovno već postojeća stanja i prijelaze).
        -   Završna su stanja upravo svi čvorovi na sufiksnom putu samog niza $\texttt{abcbc}$.
    -   Prijelazi koji vode u isto stanje nužno imaju istu oznaku, a njihova se polazišta nalaze na nekom (neprekinutom) putu u stablu sufiksnih poveznica. Primjerice, u stanje $\texttt{abcb}$ prelaze dva stanja: $\texttt{abc}$ i $\texttt{bc}$. Ona leže na putu $\texttt{abc}\rightarrow\texttt{bc}$ u stablu sufiksnih poveznica. Uočimo da ona odgovaraju skupovima nizova $\{\texttt{abc}\}$ odnosno $\{\texttt{bc},\texttt{c}\}$; dodamo li tim nizovima na kraj znak $\texttt{b}$, dobivamo skup nizova $\{\texttt{abcb},\texttt{bcb},\texttt{cb}\}$ koji odgovara stanju $\texttt{abcb}$.
    
        -   Nakon dodavanja znaka različita stanja mogu prijeći u isto stanje zato što se dodavanjem znaka na kraj broj pojavljivanja može samo smanjiti, pa izvorno različiti skupovi završnih pozicija mogu postati jednaki.
    -   U stablu sufiksnih poveznica skup $\operatorname{endpos}$ svakog čvora unija je skupova $\operatorname{endpos}$ njegove djece, uvećana za najviše jednu poziciju. Ta nova pozicija postoji ako i samo ako čvor odgovara upravo prefiksu izvornog niza koji završava na toj poziciji. Budući da na slici nijedan unutarnji čvor stabla sufiksnih poveznica (koji nije ni korijen ni list) ne odgovara prefiksu niza $\texttt{abcbc}$, takav se slučaj ondje ne pojavljuje.

Sufiksni automat pohranjuje informacije o svim podnizovima niza. To se može razumjeti iz dvaju kutova:

-   Sam SAM može se shvatiti kao sažeta inačica trieja svih sufiksa niza. Stoga pohranjuje informacije o svim prefiksima svih sufiksa niza, što je isto što i informacije o svim podnizovima niza.
-   Stablo sufiksnih poveznica SAM-a može se shvatiti kao sažeta inačica sufiksnih putova svih prefiksa niza. Stoga pohranjuje informacije o svim sufiksima svih prefiksa niza, što je također isto što i informacije o svim podnizovima niza.

Oba su ta gledišta korisna pri rješavanju različitih problema.

### Sažetak

Prije nego što nastavimo s raspravom o samom algoritmu, sažmimo dosadašnje i uvedimo nekoliko pomoćnih oznaka.

-   Podnizovi niza $s$ mogu se prema svojim skupovima završnih pozicija $\operatorname{endpos}$ podijeliti u više klasa ekvivalencije.

-   SAM se sastoji od početnog stanja $t_0$ i po jednog stanja za svaku klasu ekvivalencije $\operatorname{endpos}$ (nepraznih podnizova).

-   Svakom stanju $v$ odgovara jedan ili više podnizova. Najdulji od njih označavamo $\operatorname{longest}(v)$, a njegovu duljinu $\operatorname{len}(v)$. Slično, najkraći podniz označavamo $\operatorname{shortest}(v)$, a njegovu duljinu $\operatorname{minlen}(v)$. Tada su svi nizovi koji odgovaraju tom stanju različiti sufiksi niza $\operatorname{longest}(v)$, a njihove duljine poprimaju točno sve cijele brojeve iz intervala $[\operatorname{minlen}(v),\operatorname{len}(v)]$.

-   Za svako stanje $v\neq t_0$ sufiksnu poveznicu definiramo kao brid prema stanju koje odgovara sufiksu niza $\operatorname{longest}(v)$ duljine $\operatorname{minlen}(v)-1$. Sve sufiksne poveznice tvore stablo s korijenom $t_0$. To stablo ujedno prikazuje relaciju sadržavanja među skupovima $\operatorname{endpos}$.

-   Za svako stanje $v\neq t_0$ vrijednost $\operatorname{minlen}(v)$ može se izraziti preko sufiksne poveznice $\operatorname{link}(v)$:

    $$
    \operatorname{minlen}(v)=\operatorname{len}(\operatorname{link}(v))+1.
    $$

-   Krenemo li iz proizvoljnog stanja $v_0$ po sufiksnim poveznicama, uvijek stižemo u početno stanje $t_0$. Pritom dobivamo niz međusobno disjunktnih intervala $[\operatorname{minlen}(v_i),\operatorname{len}(v_i)]$ čija unija tvori neprekinuti interval $[0,\operatorname{len}(v_0)]$.

### Algoritam

Sada možemo opisati algoritam izgradnje SAM-a. Algoritam je **online**: znakove niza možemo dodavati jedan po jedan i u svakom koraku odgovarajuće održavati SAM.

Prije detaljne implementacije, najprije na slikama steknimo dojam o tome kako se SAM može promijeniti pri dodavanju novog znaka $c$.

???+ note "Jednostavno razumijevanje inkrementalne izgradnje"
    Na temelju SAM-a niza $s$ može se izgraditi SAM niza $s+c$. Prema ranijem objašnjenju slike, dovoljno je izgraditi sufiksni put novog prefiksa (tj. niza $s+c$) i sažeti ga u postojeće putove. Štoviše, prema ranijem opisu, svi čvorovi na novom sufiksnom putu nužno se mogu dobiti prijelazom po znaku $c$ iz čvorova na sufiksnom putu izvornog niza $s$.
    
    Najprije razmotrimo kakav oblik može imati sufiksni put izvornog niza $s$ prije dodavanja novog znaka $c$ i kako prelazi po znaku $c$. Najopćenitiji slučaj prikazan je na sljedećoj slici:
    
    ![](./images/SAM/sam-suffix-path-1.svg)
    
    Na slici je sufiksni put izvornog niza $s$ jednak $p_0\rightarrow p_1\rightarrow\cdots\rightarrow p_6\rightarrow t_0$, a sufiksne poveznice prikazane su crvenim strelicama. Neki od tih čvorova (naime $p_2\sim p_6$) već imaju prijelaz po znaku $c$; budući da dodavanje istog znaka uzastopnim sufiksima opet daje uzastopne sufikse, odredišta tih prijelaza tvore drugi sufiksni put $q_1\rightarrow q_2\rightarrow q_3\rightarrow t_0$. Ovdje su dva zapažanja:
    
    -   Na sufiksnom putu izvornog niza $s$ čvorovi bez prijelaza po $c$ nužno su prvih nekoliko čvorova. Čim od nekog čvora (na slici $p_2$) postoji prijelaz po $c$, i svi sljedeći čvorovi na putu imaju prijelaz po $c$.
    
        **Objašnjenje**: neka je $s_2=\operatorname{longest}(p_2)$; tada svi sljedeći čvorovi odgovaraju sufiksima niza $s_2$, pa ako se $s_2+c$ pojavljuje u $s$, onda se u $s$ pojavljuje i svaki sufiks niza $s_2$ s dodanim $c$, pa svi ti čvorovi imaju prijelaz po $c$.
    -   Iako su čvorovi koji po znaku $c$ prelaze u čvor $q_i$ nužno neprekinuti segment u stablu sufiksnih poveznica, taj segment ne mora cijeli ležati na sufiksnom putu od $p_0$ do korijena. Točnije, samo početnih nekoliko čvorova segmenta koji pripada prvom čvoru $q_1$ **možda** nije na tom sufiksnom putu. Primjerice, čvoru $q_1$ na slici odgovara segment $p_1'\rightarrow p_2\rightarrow p_3$, pri čemu $p_1'$ nije na sufiksnom putu od $p_0$.
    
        **Objašnjenje**: neka je $s_2=\operatorname{longest}(p_2)$; tada $s_2+c$ odgovara čvoru $q_1$, ali na slici je očito $s_2+c\neq\operatorname{longest}(q_1)$, jer je potonji jednak $\operatorname{longest}(p'_1)+c$. To znači da se dio nizova koji odgovaraju $q_1$ ne može dobiti prijelazom iz $s_2$ i njegovih sufiksa. Obrnuto, nizovi u $q_2$ nužno su sufiksi niza $s_2+c$, pa su nakon brisanja završnog $c$ nužno sufiksi niza $s_2$. Dakle, čvorovi koji po $c$ prelaze u $q_2$ nužno su na sufiksnom putu koji počinje u $p_2$. Zato samo dio segmenta koji pripada početnom čvoru $q_1$ možda nije na sufiksnom putu od $p_0$.
    
    Što se u ovom prikazu mijenja ako na kraj izvornog niza $s$ dodamo znak $c$ i izgradimo odgovarajući sufiksni put? Odgovor je na sljedećoj slici:
    
    ![](./images/SAM/sam-suffix-path-2.svg)
    
    Budući da se čvor $q_0$ dobiva prijelazom po znaku $c$ iz čvora $p_0$ koji odgovara izvornom nizu $s$, on odgovara novom nizu $s+c$. Stoga je njegov sufiksni put $q_0\rightarrow q_1''\rightarrow q_2\rightarrow q_3\rightarrow t_0$ upravo novi sufiksni put. Ako je čvor $p_i$ na izvornom sufiksnom putu već imao prijelaz po $c$, novi sufiksni put nužno prolazi kroz čvorove u koje ti prijelazi vode, pa se stari čvorovi mogu izravno ponovno iskoristiti. Na novom sufiksnom putu postoji točno jedan potpuno novi čvor, $q_0$, koji prima prijelaze iz onih početnih čvorova izvornog sufiksnog puta koji nisu imali prijelaz po $c$.
    
    Osim tih očitih činjenica, uočimo da je i stari čvor $q_1$ jednom kopiran, odnosno razdvojen na dva čvora $q'_1\rightarrow q_1''$. Razlog je to što se novi sufiksni put samo djelomično preklapa s postojećim putem: od nizova koji odgovaraju starom čvoru $q_1$ samo se kraći (tj. oni u koje mogu prijeći čvorovi $p_2$ i $p_3$) pojavljuju na novom sufiksnom putu, dok se dulji (tj. oni u koje može prijeći čvor $p_1'$) na njemu ne pojavljuju; stoga novi sufiksni put može proći samo kroz dio čvora $q_1$, pa se on mora razdvojiti na dva čvora kako bi se taj slučaj prikazao. Iz istog razloga, kako je već objašnjeno, u čvorove $q_2$ i $q_3$ nakon $q_1$ ne može se prijeći iz čvorova koji nisu na sufiksnom putu od $p_0$, pa se svi nizovi koji im odgovaraju pojavljuju na novom sufiksnom putu i razdvajanje nije potrebno.
    
    Gledano kroz značenje stanja u SAM-u, svako je stanje jedan skup $\operatorname{endpos}$. Neka je $i$ nova završna pozicija nastala produljenjem niza; tada je novi čvor $q_0$ skup završnih pozicija $\{i\}$, razdvojeni čvorovi $q_1'$ i $q_1''$ odgovaraju skupovima $\operatorname{endpos}(q_1)$ odnosno $\operatorname{endpos}(q_1)\cup\{i\}$, a sljedeći čvorovi $q_2$ i $q_3$ zapravo su svojim postojećim skupovima završnih pozicija dodali $i$. Drugim riječima, iako se $q_2$ i $q_3$ i njihovi prijelazi nisu promijenili, njihovi su se skupovi $\operatorname{endpos}$ doista proširili.
    
    Gore je opisan najsloženiji, najopćenitiji slučaj (tj. **slučaj 3** u nastavku). U praksi čvor $p'_1$ možda ne postoji, pa razdvajanje nije potrebno (tj. **slučaj 2** u nastavku). Da bismo to prepoznali, dovoljno je provjeriti vrijedi li $\operatorname{longest}(q_1)=\operatorname{longest}(p_2)+c$, odnosno $\operatorname{len}(q_1)=\operatorname{len}(p_2)+1$. Moguće je i da nijedan čvor na sufiksnom putu od $p_0$ nema prijelaz po $c$; tada je dovoljno stvoriti novi čvor $q_0$ (tj. **slučaj 1** u nastavku).

Kad smo svladali ideju dodavanja sufiksnog puta, razmotrimo konkretne korake inkrementalne izgradnje.

#### Postupak

Da bismo zajamčili linearnu prostornu složenost, pamtit ćemo samo vrijednosti $\operatorname{len}$ i $\operatorname{link}$ te popis prijelaza svakog stanja; završna stanja nećemo označavati (ali ćemo poslije pokazati kako te oznake dodijeliti nakon izgradnje SAM-a).

Na početku SAM sadrži samo jedno stanje $t_0$ s brojem $0$ (ostala stanja dobivaju brojeve $1,2,\ldots$). Radi jednostavnosti za stanje $t_0$ postavljamo $\operatorname{len}(t_0)=0$ i $\operatorname{link}(t_0)=-1$ ($-1$ označava virtualno stanje).

Sada treba samo implementirati postupak dodavanja jednog znaka $c$ na kraj trenutačnog niza. Tijek algoritma je sljedeći:

???+ note "Postupak inkrementalne izgradnje SAM-a"
    -   Neka je $\textit{last}$ stanje koje odgovara cijelom nizu prije dodavanja znaka $c$ (na početku postavljamo $\textit{last}=0$, a u posljednjem koraku algoritma ažuriramo $\textit{last}$).
    -   Stvorimo novo stanje $\textit{cur}$ i postavimo $\operatorname{len}(\textit{cur})=\operatorname{len}(\textit{last})+1$; vrijednost $\operatorname{link}(\textit{cur})$ zasad je nepoznata.
    -   Zatim provodimo sljedeći postupak: počevši od stanja $\textit{last}$, ako trenutačno stanje još nema prijelaz označen znakom $c$, dodajemo prijelaz po znaku $c$ u stanje $\textit{cur}$ i pomičemo se po sufiksnoj poveznici. Ako pritom naiđemo na stanje koje već ima prijelaz po znaku $c$, zaustavljamo se i to stanje označavamo $p$.
    -   **Slučaj 1**: ako takvo stanje $p$ nismo pronašli, stigli smo u virtualno stanje $-1$; postavljamo $\operatorname{link}(\textit{cur})=0$ i prelazimo na posljednji korak.
    -   Pretpostavimo sada da smo pronašli stanje $p$ koje ima prijelaz po znaku $c$. Stanje u koje taj prijelaz vodi označimo $q$. Tada je ili $\operatorname{len}(p)+1=\operatorname{len}(q)$ ili $\operatorname{len}(p)+1<\operatorname{len}(q)$.
    -   **Slučaj 2**: ako je $\operatorname{len}(p)+1=\operatorname{len}(q)$, samo postavimo $\operatorname{link}(\textit{cur})=q$ i prijeđemo na posljednji korak.
    -   **Slučaj 3**: inače je nešto složenije i stanje $q$ treba **klonirati**: stvaramo novo stanje $\textit{clone}$ i kopiramo sve informacije stanja $q$ osim vrijednosti $\operatorname{len}$ (sufiksnu poveznicu i prijelaze). Postavljamo $\operatorname{len}(\textit{clone})=\operatorname{len}(p)+1$.
    
        Nakon kloniranja sufiksnu poveznicu iz $\textit{cur}$ usmjeravamo na $\textit{clone}$, a također i iz $q$ na $\textit{clone}$.
    
        Na kraju se od stanja $p$ vraćamo po sufiksnim poveznicama i, dok god posjećeno stanje ima prijelaz u stanje $q$, taj prijelaz preusmjeravamo na stanje $\textit{clone}$.
    -   Nakon obrade bilo kojeg od tri slučaja ažuriramo $\textit{last}$ na stanje $\textit{cur}$.

Želimo li još znati koja su stanja **završna**, a koja nisu, sva završna stanja možemo pronaći nakon što izgradimo potpuni SAM niza $s$. U tu svrhu krenemo od stanja koje odgovara cijelom nizu (pohranjeno u varijabli $\textit{last}$) i pratimo njegove sufiksne poveznice dok ne stignemo u početno stanje. Sva posjećena stanja označimo kao završna. Lako je uvidjeti da tako označavamo točno sve sufikse niza $s$, a to su upravo završna stanja.

Budući da za svaki znak niza $s$ stvaramo jedno ili dva nova stanja, SAM sadrži samo **linearno mnogo** stanja. To da SAM ima i linearno mnogo prijelaza te da je ukupno vrijeme rada algoritma linearno još nije jasno i bit će objašnjeno u nastavku.

#### Objašnjenje

Detaljno ćemo objasniti pojedinosti svakog koraka algoritma i pokazati njegovu **ispravnost**.

???+ note "Detaljno objašnjenje algoritma"
    -   Ako prijelaz $(p,q)$ zadovoljava $\operatorname{len}(p)+1=\operatorname{len}(q)$, kažemo da je **kontinuiran**. Inače, tj. kad je $\operatorname{len}(p)+1<\operatorname{len}(q)$, prijelaz zovemo **nekontinuiranim**.
    
        Iz opisa algoritma vidi se da se kontinuirani i nekontinuirani prijelazi u algoritmu obrađuju različito. Kontinuirani su prijelazi fiksni i više ih ne mijenjamo. Nasuprot tome, pri umetanju novog znaka u niz nekontinuirani prijelazi mogu se promijeniti (krajevi brida prijelaza mogu se promijeniti).
    -   Radi izbjegavanja dvosmislenosti, niz prije umetanja trenutačnog znaka $c$ u SAM označavamo $s$.
    -   Algoritam počinje stvaranjem novog stanja $\textit{cur}$, koje odgovara cijelom nizu $s+c$. Razlog za stvaranje novog čvora jasan je: ujedno stvaramo i novu klasu ekvivalencije.
    -   Nakon stvaranja novog stanja krećemo se od stanja $\textit{last}$, koje odgovara cijelom nizu $s$, po sufiksnim poveznicama. Za svako posjećeno stanje pokušavamo dodati prijelaz po znaku $c$ u novo stanje $\textit{cur}$.
    
        No smijemo dodavati samo prijelaze koji nisu u sukobu s postojećima. Stoga se, čim naiđemo na postojeći prijelaz po $c$, moramo zaustaviti.
    -   Najjednostavniji je slučaj kad stignemo u virtualno stanje $-1$; to znači da smo svim sufiksima niza $s$ dodali prijelaz po $c$. To ujedno znači da se znak $c$ nikad prije nije pojavio u nizu $s$. Stoga je sufiksna poveznica stanja $\textit{cur}$ stanje $0$.
    -   Inače (tj. u slučajevima 2 i 3) pronašli smo postojeći prijelaz $(p,q)$. To znači da pokušavamo u automat dodati niz $x+c$ koji **već postoji** (pri čemu je $x=\operatorname{longest}(p)$ sufiks niza $s$, a niz $x+c$ već se pojavio kao podniz niza $s$). Budući da pretpostavljamo da je automat niza $s$ ispravno izgrađen, ovdje ne smijemo dodati novi prijelaz.
    
        Teškoća je, međutim, u pitanju: na koje stanje treba pokazivati sufiksna poveznica iz stanja $\textit{cur}$? Sufiksnu poveznicu moramo usmjeriti na stanje čiji je najdulji niz upravo $x+c$, tj. čiji je $\operatorname{len}$ jednak $\operatorname{len}(p)+1$. No takvo stanje možda ne postoji, tj. $\operatorname{len}(q)>\operatorname{len}(p)+1$. U tom slučaju takvo stanje moramo stvoriti razdvajanjem stanja $q$.
    -   Naravno, ako je prijelaz $(p,\,q)$ kontinuiran, onda je $\operatorname{len}(q)=\operatorname{len}(p)+1$. Tada je sve jednostavno: samo sufiksnu poveznicu stanja $\textit{cur}$ usmjerimo na stanje $q$.
    -   Inače je prijelaz nekontinuiran, tj. $\operatorname{len}(q)>\operatorname{len}(p)+1$, što znači da stanje $q$ ne odgovara samo sufiksu $x+c$ duljine $\operatorname{len}(p)+1$, nego i duljim podnizovima niza $s$. Nemamo drugog izbora nego stanje $q$ razdvojiti na dva podstanja, pri čemu duljina prvog podstanja postaje $\operatorname{len}(p)+1$.
    
        Kako razdvajamo stanje? **Kloniramo** stanje $q$ u novo stanje $\textit{clone}$ i postavimo $\operatorname{len}(\textit{clone})=\operatorname{len}(p)+1$. Budući da ne želimo mijenjati putove koji prolaze kroz $q$, kopiramo sve prijelaze stanja $q$ u $\textit{clone}$. Također sufiksnu poveznicu iz $\textit{clone}$ postavljamo na odredište sufiksne poveznice stanja $q$, a sufiksnu poveznicu stanja $q$ postavljamo na $\textit{clone}$.
    
        Nakon razdvajanja stanja sufiksnu poveznicu iz $\textit{cur}$ postavljamo na $\textit{clone}$.
    
        U posljednjem koraku neke prijelaze koji su izvorno vodili u $q$ preusmjeravamo na $\textit{clone}$. Koje prijelaze treba izmijeniti? Dovoljno je preusmjeriti prijelaze koji odgovaraju svim sufiksima niza $x+c$ (gdje je $x=\operatorname{longest}(p)$). Drugim riječima, nastavljamo se kretati po sufiksnim poveznicama od čvora $p$ sve do virtualnog stanja $-1$ ili dok prijelaz trenutačnog stanja po $c$ više ne pokazuje na stanje $q$.

### Linearna vremenska složenost

Pretpostavljamo da je veličina abecede **konstantna**, tj. da operacije traženja prijelaza po znaku, dodavanja prijelaza i pronalaženja sljedećeg prijelaza imaju vremensku složenost $O(1)$. Ako prijelaze svakog čvora pohranimo i kao polje duljine $\left|\Sigma\right|$ (za brzo pronalaženje prijelaza po zadanoj oznaci) i kao dinamičku listu (za brzo obilaženje svih postojećih prijelaza), trošeći prostor za vrijeme, vremenska složenost algoritma[^time-complexity] iznosi $O(n)$, a prostorna $O(n\left|\Sigma\right|)$.

??? note "Dokaz"
    Promotrimo li dijelove algoritma, postoje tri mjesta na kojima linearnost vremenske složenosti nije očita:
    
    -   prvo je obilazak sufiksnih poveznica od stanja $\textit{last}$ uz dodavanje prijelaza po znaku $c$;
    -   drugo je kopiranje prijelaza pri kloniranju stanja $q$ u novo stanje $\textit{clone}$;
    -   treće je izmjena prijelaza koji vode u $q$ i njihovo preusmjeravanje na $\textit{clone}$.
    
    Koristimo činjenicu da je veličina SAM-a (broj stanja i prijelaza) **linearna** (dokaz linearnosti broja stanja sam je algoritam, a dokaz linearnosti broja prijelaza dat ćemo nakon implementacije algoritma).
    
    Stoga je ukupna složenost **prvog i drugog mjesta** očito linearna, jer svaka pojedina operacija amortizirano dodaje automatu samo jedan novi prijelaz.
    
    Ostaje procijeniti ukupnu složenost **trećeg mjesta**, gdje prijelaze koji su izvorno vodili u $q$ preusmjeravamo na $\textit{clone}$. Označimo $v=\operatorname{longest}(p)$; to je sufiks niza $s$. U svakoj iteraciji duljina niza $v$ se smanjuje, pa se početna pozicija niza $v$ kao sufiksa niza $s$ nužno pomiče udesno. Stoga broj pomaka $p$ po sufiksnim poveznicama u petlji ne premašuje udaljenost za koju se početna pozicija $v$ kao sufiksa niza $s$ pomaknula udesno. Budući da se $p$ mora pomaknuti barem jednom da bi petlja završila i da je $p$ barem rezultat jednog pomaka $\textit{last}$ po sufiksnoj poveznici, pri završetku petlje početna pozicija $v$ kao sufiksa niza $s$ nije lijevo od početne pozicije niza $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$. Štoviše, pri završetku petlje početna pozicija niza $v$ kao sufiksa niza $s$ upravo je početna pozicija niza $v+c$ kao sufiksa niza $s+c$, a kao sufiks niza $s+c$ niz $v+c$ upravo je niz $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{cur})))$. Budući da je $\textit{cur}$ nova vrijednost $\textit{last}$, broj pomaka u petlji ne premašuje udaljenost za koju se početna pozicija niza $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$ kao sufiksa trenutačnog niza pomaknula udesno između stare i nove vrijednosti, uvećanu za jedan (tj. za pomak nužan za završetak petlje).
    
    Budući da pozicija niza $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$ kao sufiksa trenutačnog niza tijekom cijele izgradnje SAM-a monotono raste[^monotone-loc], njezin ukupni pomak ne premašuje $n$. To pokazuje da broj iteracija petlje u kojoj mijenjamo prijelaze koji vode u $q$ ne premašuje $2n$. Upravo smo to trebali dokazati.

Naravno, ako veličina abecede nije konstantna, a ne želimo potrošiti $O(n\left|\Sigma\right|)$ prostora, vremenska složenost SAM-a nije linearna. Prijelaze iz jednog čvora tada treba pohraniti u balansirano stablo koje podržava brzo pretraživanje i umetanje. Označimo li s $\Sigma$ abecedu, a s $\left|\Sigma\right|$ njezinu veličinu, asimptotska vremenska složenost algoritma je $O(n\log\left|\Sigma\right|)$, a prostorna $O(n)$.

### Implementacija

Najprije implementiramo strukturu podataka koja pohranjuje sve informacije o jednom prijelazu. Po potrebi ovdje možete dodati oznaku završnog stanja ili neke druge informacije. Popis prijelaza pohranit ćemo u `map`, što nam omogućuje obradu cijelog niza u ukupno $O(n)$ prostora i $O(n\log\left|\Sigma\right|)$ vremena. Naravno, kad je veličina abecede $\left|\Sigma\right|=K$ mala konstanta (npr. 26), prikladnije je `next` deklarirati kao `int[K]`.

```cpp
struct state {
  int len, link;
  std::map<char, int> next;
};
```

Sam SAM bit će pohranjen u polju struktura `state`. Pamtimo trenutačnu veličinu automata `sz` i varijablu `last`, stanje koje odgovara trenutačnom cijelom nizu.

```cpp
constexpr int MAXLEN = 100000;
state st[MAXLEN * 2];
int sz, last;
```

Definiramo funkciju za inicijalizaciju SAM-a (stvara SAM sa samo početnim stanjem).

```cpp
void sam_init() {
  for (int i = 0; i < sz; i++) st[i].next.clear();
  st[0].len = 0;
  st[0].link = -1;
  sz = 1;
  last = 0;
}
```

Na kraju dajemo implementaciju glavne funkcije: dodaje znak na kraj trenutačnog niza i odgovarajuće nadograđuje automat.

???+ note "Implementacija"
    ```cpp
    void sam_extend(char c) {
      int cur = sz++;
      st[cur].len = st[last].len + 1;
      int p = last;
      while (p != -1 && !st[p].next.count(c)) {
        st[p].next[c] = cur;
        p = st[p].link;
      }
      if (p == -1) {
        st[cur].link = 0;
      } else {
        int q = st[p].next[c];
        if (st[p].len + 1 == st[q].len) {
          st[cur].link = q;
        } else {
          int clone = sz++;
          st[clone].len = st[p].len + 1;
          st[clone].next = st[q].next;
          st[clone].link = st[q].link;
          while (p != -1 && st[p].next[c] == q) {
            st[p].next[c] = clone;
            p = st[p].link;
          }
          st[q].link = st[cur].link = clone;
        }
      }
      last = cur;
    }
    ```

Kao što je ranije spomenuto, ako memoriju mijenjate za vrijeme (prostorna složenost $O(n\left|\Sigma\right|)$, gdje je $\left|\Sigma\right|$ veličina abecede), SAM nad abecedom proizvoljne veličine možete izgraditi u vremenu $O(n)$[^time-complexity]. No tada za svako stanje morate pohraniti polje veličine $\left|\Sigma\right|$ (za brzo pronalaženje prijelaza po znaku) i listu svih postojećih prijelaza (za brzo obilaženje svih postojećih prijelaza).

## Daljnja svojstva

### Broj stanja

Za niz $s$ duljine $n$ broj stanja njegova SAM-a **ne premašuje** $2n-1$ (uz pretpostavku $n\ge 2$).

??? note "Dokaz"
    Tvrdnja slijedi iz samog algoritma. Na početku automat sadrži jedno stanje, u prvoj i drugoj iteraciji stvara se samo po jedan čvor, a u preostalih $n-2$ koraka svaki stvara najviše $2$ stanja.
    
    No tu ocjenu možemo **dokazati** i **bez pozivanja na algoritam**. Ako se $s$ sastoji od istog znaka, broj stanja je $n+1$ i tvrdnja je očita; pretpostavimo dalje da $s$ sadrži barem dva različita znaka. Podsjetimo se da je broj stanja jednak broju različitih skupova $\operatorname{endpos}$. Ti skupovi $\operatorname{endpos}$ tvore stablo (skup $\operatorname{endpos}$ roditelja sadrži skup $\operatorname{endpos}$ djeteta). Malo preoblikujmo to stablo: kad god ono ima unutarnji čvor sa samo jednim djetetom (što znači da skupu djeteta nedostaje barem jedna pozicija iz skupa roditelja), dodamo mu kao dijete skup koji sadrži te nedostajuće pozicije. Na kraju dobivamo stablo u kojem svaki unutarnji čvor ima više od jednog djeteta, a broj listova ne premašuje $n$. Takvo stablo ima najviše $2n-1$ čvorova, pa ni broj različitih skupova $\operatorname{endpos}$ u izvornom stablu ne premašuje $2n-1$.
    
    Niz $\texttt{abbb} \cdots \texttt{bbb}$ dostiže tu gornju granicu: u svakoj iteraciji počevši od treće algoritam razdvaja jedno stanje, pa na kraju nastaje točno $2n-1$ stanja.

### Broj prijelaza

Za niz $s$ duljine $n$ broj prijelaza njegova SAM-a **ne premašuje** $3n-4$ (uz pretpostavku $n\ge 3$).

??? note "Dokaz"
    Najprije ocijenimo broj kontinuiranih prijelaza. Promotrimo razapinjuće stablo automata sastavljeno od najduljih putova od stanja $t_0$ do svih stanja. Razapinjuće stablo sadrži samo kontinuirane bridove, pa ih je manje nego stanja, tj. broj bridova ne premašuje $2n-2$.
    
    Sada ocijenimo broj nekontinuiranih prijelaza. Neka je trenutačni nekontinuirani prijelaz $(p,\,q)$ sa znakom $c$. Uzmimo njemu pripadni niz $u+c+w$, gdje niz $u$ odgovara najduljem putu od početnog stanja do $p$, a $w$ najduljem putu od $q$ do nekog završnog stanja. S jedne strane, nizovi oblika $u+c+w$ pripadni različitim nekontinuiranim prijelazima međusobno su različiti (jer se $u$ sastoji samo od kontinuiranih prijelaza, pa je prvi nekontinuirani prijelaz na putu $u+c+w$ upravo $(p,\,q)$). S druge strane, po definiciji završnog stanja, svaki je niz oblika $u+c+w$ sufiks cijelog niza $s$. Budući da $s$ ima samo $n$ nepraznih sufiksa i da nijedan niz oblika $u+c+w$ nije jednak $s$ (jer put koji odgovara $s$ sadrži samo kontinuirane prijelaze), ukupan broj nekontinuiranih prijelaza ne premašuje $n-1$.
    
    Zbrajanjem tih dviju ocjena dobivamo gornju granicu $3n-3$. No najveći broj stanja postiže se samo u slučajevima poput $\texttt{abbb} \cdots \texttt{bbb}$, a tada je broj prijelaza očito manji od $3n-3$.
    
    Stoga dobivamo strožu gornju granicu za broj prijelaza SAM-a: $3n-4$. Niz $\texttt{abbb} \cdots \texttt{bbbc}$ dostiže tu granicu.

### Stablo sufiksnih poveznica

Iako SAM gradimo radi informacija o njegovim stanjima i prijelazima, sufiksne poveznice $\operatorname{link}$ zabilježene tijekom izgradnje i duljine najduljih podnizova $\operatorname{len}$ pripadnih stanjima u primjenama su često važnije od prijelaza SAM-a i mogu se čak koristiti samostalno, bez prijelaza.

Tijekom izgradnje SAM-a ažuriramo vrijednost stanja $\textit{last}$. Ono odgovara nizu prije (odnosno poslije) svakog dodavanja znaka, tj. svim prefiksima cijelog niza $s$. Označimo stanje koje odgovara $i$-tom prefiksu s $v_i$; tako dobivamo ukupno $n$ stanja $v_0,v_1,\cdots,v_{n-1}$. Dodatno, početno stanje $t_0$ proglašavamo $v_{-1}$, koje odgovara praznom prefiksu. Ta ćemo stanja zvati „prefiksnim čvorovima”.

U lemi 4 spomenuto je da sva stanja i sve sufiksne poveznice tvore stablo usmjereno prema korijenu $t_0$; to se stablo naziva i **stablo sufiksnih poveznica** (kineski natjecatelji često ga zovu i **parent stablo**). Ono bilježi informacije o svim sufiksima svih prefiksa niza, tj. o svim podnizovima.

Stablo sufiksnih poveznica ima sljedeća svojstva:

-   Niz koji odgovara pretku uvijek je sufiks niza koji odgovara potomku.
-   Skup $\operatorname{endpos}$ svakog čvora upravo je skup indeksa $i$ svih „prefiksnih čvorova” $v_i$ u njegovu podstablu.
-   Skup $\operatorname{endpos}$ pretka u stablu sufiksnih poveznica uvijek strogo sadrži skup $\operatorname{endpos}$ potomka.
-   Vrijednost $\operatorname{len}$ svakog čvora jednaka je duljini najduljeg zajedničkog sufiksa prefiksa koji odgovaraju svim „prefiksnim čvorovima” $v_i$ u njegovu podstablu.
-   Osim za korijen $t_0$, broj različitih podnizova koji odgovaraju čvoru jednak je njegovoj vrijednosti $\operatorname{len}$ umanjenoj za vrijednost $\operatorname{len}$ njegova roditelja, tj. $\operatorname{len}(v)-\operatorname{len}(\operatorname{link}(v))$.

Ta svojstva imaju mnogo primjena. Primjerice, najdulji zajednički sufiks $i$-tog i $j$-tog prefiksa upravo je najdulji niz koji odgovara LCA čvorova $v_i$ i $v_j$.

Naposljetku, stablo sufiksnih poveznica izgrađeno za niz $s$ ima istu strukturu kao [sufiksno stablo](./suffix-tree.md) izgrađeno za njegov obrat $s_R$. To se često koristi za offline izgradnju sufiksnog stabla.

## Primjene

Pogledajmo sada neke probleme koji se mogu riješiti SAM-om. Radi jednostavnosti pretpostavljamo da je veličina abecede $|\Sigma|$ konstantna. To nam dopušta da složenost dodavanja znaka i obilaska smatramo konstantnom.

### Provjera pojavljuje li se niz

???+ example "Problem"
    Zadan je tekst $T$ i više uzoraka $P$; treba provjeriti pojavljuje li se niz $P$ kao podniz niza $T$.

??? note "Rješenje"
    U vremenu $O(\left|T\right|)$ izgradimo sufiksni automat teksta $T$. Da bismo provjerili pojavljuje li se uzorak $P$ u $T$, krećemo se prijelazima (bridovima) od $t_0$ prema znakovima niza $P$. Ako u nekom trenutku prijelaz ne postoji, uzorak $P$ nije podniz niza $T$. Ako tako uspijemo obraditi cijeli niz $P$, uzorak se pojavljuje u $T$.
    
    Za svaki niz $P$ vremenska složenost algoritma je $O(\left|P\right|)$. Osim toga, algoritam pronalazi i najveću duljinu prefiksa uzorka $P$ koji se pojavljuje u tekstu.

### Broj različitih podnizova

???+ example "Problem"
    Zadan je niz $S$; izračunaj broj različitih podnizova.

??? note "Rješenje 1"
    Izgradimo sufiksni automat niza $S$.
    
    Svaki podniz niza $S$ odgovara jednom putu u automatu. Stoga je broj različitih podnizova jednak broju različitih nepraznih putova u automatu koji počinju u $t_0$.
    
    Budući da je SAM usmjereni aciklički graf, broj različitih putova može se izračunati dinamičkim programiranjem. Neka je $d_{v}$ broj putova koji počinju u stanju $v$ (uključujući put duljine nula); tada vrijedi rekurzija:
    
    $$
    d_{v}=1+\sum_{w:(v,w,c)\in \text{SAM}}d_{w}
    $$
    
    Dakle, $d_{v}$ jednak je $1$ plus zbroj vrijednosti $d$ odredišta svih prijelaza iz $v$, gdje $(v,w,c)\in \text{SAM}$ označava da u sufiksnom automatu postoji prijelaz iz $v$ po $c$ u $w$.
    
    Broj različitih podnizova stoga je $d_{t_0}-1$ (jer treba izostaviti prazni podniz).
    
    Ukupna vremenska složenost: $O(\left|S\right|)$.

??? note "Rješenje 2"
    Druga je metoda da nakon izgradnje sufiksnog automata iskoristimo informacije iz dobivenog stabla sufiksnih poveznica. Broj podnizova koji odgovaraju čvoru jednak je $\operatorname{len}(v)-\operatorname{len}(\operatorname{link}(v))$; dovoljno je zbrojiti po svim čvorovima osim $t_0$.
    
    Ukupna vremenska složenost i dalje je $O(\left|S\right|)$.

Primjeri zadataka: [[predložak] Sufiksni automat](https://www.luogu.com.cn/problem/P3804), [SDOI2016 Generiranje čarolija (生成魔咒)](https://loj.ac/problem/2033)

### Ukupna duljina svih različitih podnizova

???+ example "Problem"
    Zadan je niz $S$; izračunaj ukupnu duljinu svih različitih podnizova.

??? note "Rješenje 1"
    Postupak je sličan prethodnom zadatku, samo što sada dinamičko programiranje provodimo u dva dijela: broj različitih podnizova $d_{v}$ i njihova ukupna duljina $ans_{v}$.
    
    Kako se računa $d_{v}$ opisali smo u prethodnom zadatku. Vrijednost $ans_{v}$ može se izračunati sljedećom rekurzijom:
    
    $$
    ans_{v}=\sum_{w:(v,w,c)\in \text{SAM}}(d_{w}+ans_{w})
    $$
    
    Uzimamo odgovor svakog susjednog čvora $w$ i dodajemo $d_{w}$ (jer je svaki podniz koji počinje u stanju $v$ dulji za jedan znak).
    
    Vremenska složenost algoritma i dalje je $O(\left|S\right|)$.

??? note "Rješenje 2"
    I ovdje možemo iskoristiti informacije iz stabla sufiksnih poveznica. Zbroj duljina svih sufiksa najduljeg podniza koji odgovara čvoru jednak je
    
    $$
    \dfrac{\operatorname{len}(v)\times (\operatorname{len}(v)+1)}{2},
    $$
    
    a oduzmemo li odgovarajuću vrijednost njegova čvora $\operatorname{link}$, dobivamo neto doprinos tog čvora; dovoljno je zbrojiti po svim čvorovima osim $t_0$.
    
    Ukupna vremenska složenost i dalje je $O(\left|S\right|)$.

### Leksikografski k-ti najmanji podniz

???+ example "Problem"
    Zadan je niz $S$. Više upita; u svakom je zadan broj $K_i$ i traži se leksikografski $K_i$-ti najmanji među svim različitim podnizovima niza $S$.

??? note "Rješenje"
    Ideja rješenja proizlazi iz ideja za prethodna dva problema. Leksikografski $K_i$-ti najmanji podniz odgovara leksikografski $K_i$-tom najmanjem nepraznom putu u SAM-u, pa nakon što izračunamo broj putova iz svakog stanja, $K_i$-ti najmanji put lako pronalazimo krenuvši od korijena SAM-a.
    
    Vremenska složenost pretprocesiranja je $O(\left|S\right|)$, a jednog upita $O(\left|ans\right|\cdot\left|\Sigma\right|)$ (gdje je $ans$ odgovor na upit, a $\left|\Sigma\right|$ veličina abecede).

??? info "Napomena"
    Iako je ovo klasičan zadatak za sufiksni automat, zbog leksikografskog poretka zapravo ga je najzgodnije riješiti sufiksnim poljem.

Primjeri zadataka: [SPOJ - SUBLEX](https://www.spoj.com/problems/SUBLEX/), [TJOI2015 Teorija struna (弦论)](https://loj.ac/problem/2102)

### Najmanji ciklički pomak

???+ example "Problem"
    Zadan je niz $S$. Pronađi leksikografski najmanji ciklički pomak.

??? note "Rješenje"
    Lako se vidi da niz $S+S$ sadrži sve cikličke pomake niza $S$ kao podnizove.
    
    Problem se stoga svodi na pronalaženje najmanjeg puta duljine $\left|S\right|$ u sufiksnom automatu niza $S+S$, što se postiže trivijalno: krenemo iz početnog stanja i pohlepno (greedy) biramo najmanji znak.
    
    Ukupna vremenska složenost je $O(\left|S\right|)$.

### Broj pojavljivanja

???+ example "Problem"
    Za zadani tekst $T$ postavlja se više upita; u svakom je zadan uzorak $P$ i treba odgovoriti koliko se puta $P$ pojavljuje u $T$ kao podniz.

??? note "Rješenje 1"
    Iskoristimo informacije iz stabla sufiksnih poveznica: DFS-om pretprocesiramo veličinu skupa $\operatorname{endpos}$ svakog čvora.
    
    Početna veličina skupa svih „prefiksnih čvorova” je $1$, a čvorova koji nisu „prefiksni” $0$. Zatim, vraćajući se po sufiksnim poveznicama odozdo prema gore, veličini skupa svakog roditelja dodajemo veličine skupova sve njegove djece (ne zaboravimo početnu vrijednost samog roditelja). Tako dobivena vrijednost u svakom čvoru upravo je veličina skupa $\operatorname{endpos}$ tog čvora. Veličine skupova različite djece smijemo izravno zbrajati jer se isti $v_i$ pojavljuje samo u jednom podstablu, pa nema dvostrukog brojanja.
    
    Pri upitu u automatu pronađemo čvor koji odgovara uzorku $P$; ako postoji, odgovor je veličina skupa $\operatorname{endpos}$ tog čvora, a ako ne postoji, odgovor je $0$.
    
    Vremenska složenost pretprocesiranja je $O(|T|)$, a jednog upita $O(|P|)$.

??? note "Rješenje 2"
    Izgradimo sufiksni automat teksta $T$.
    
    Zatim pretprocesiramo: za svako stanje $v$ automata izračunamo $cnt_{v}$ jednak veličini skupa $\operatorname{endpos}(v)$. Naime, svi podnizovi koji odgovaraju istom stanju $v$ pojavljuju se u tekstu $T$ jednako mnogo puta, a to je upravo broj pozicija u skupu $\operatorname{endpos}$.
    
    No skupove $\operatorname{endpos}$ ne možemo eksplicitno izgraditi, pa promatramo samo njihove veličine $cnt$.
    
    Da bismo izračunali te vrijednosti, postupamo ovako. Za svako stanje koje nije nastalo kloniranjem (i nije početno stanje $t_0$) postavimo $cnt$ na 1. Zatim obiđemo sva stanja po padajućoj duljini $\operatorname{len}$ i trenutačnu vrijednost $cnt_{v}$ dodamo stanju na koje pokazuje sufiksna poveznica, tj.:
    
    $$
    cnt_{\operatorname{link}(v)}+=cnt_{v}
    $$
    
    Tako dobivamo ispravan odgovor za svako stanje.
    
    Zašto je to ispravno? Stanja koja nisu nastala kloniranjem (osim $t_0$) ima točno $\left|T\right|$, a prvih $i$ od njih nastaje pri umetanju prvih $i$ znakova i svako odgovara jednoj završnoj poziciji. Zato tim stanjima na početku dodjeljujemo $cnt=1$, a ostalima $cnt=0$.
    
    Zatim za svaki $v$ izvodimo $cnt_{\operatorname{link}(v)}+=cnt_{v}$. Smisao je u tome da, ako se niz koji odgovara stanju $v$ pojavljuje $cnt_{v}$ puta, onda i svi njegovi sufiksi završavaju na potpuno istim mjestima, tj. također se pojavljuju $cnt_{v}$ puta.
    
    Zašto pritom ne brojimo dvostruko (tj. ne brojimo neke pozicije dvaput)? Zato što pozicije jednog stanja dodajemo samo **jednom** drugom stanju, pa jedno stanje ne može na dva različita načina svoje pozicije proslijediti istom drugom stanju.
    
    Stoga vrijednosti $cnt$ svih stanja možemo izračunati u vremenu $O(\left|T\right|)$.
    
    Na kraju, za odgovor na upit dovoljno je pročitati vrijednost $cnt_{t}$, gdje je $t$ stanje koje odgovara uzorku; ako uzorak ne postoji, odgovor je $0$. Vremenska složenost jednog upita je $O(\left|P\right|)$.

### Pozicija prvog pojavljivanja

???+ example "Problem"
    Zadan je tekst $T$ i više upita. U svakom se traži pozicija prvog pojavljivanja niza $P$ u nizu $T$ (početna pozicija niza $P$).

??? note "Rješenje 1"
    Iskoristimo informacije iz stabla sufiksnih poveznica: DFS-om pretprocesiramo najmanji element skupa $\operatorname{endpos}$ svakog čvora.
    
    Početna vrijednost svih „prefiksnih čvorova” $v_i$ je $i$, a čvorova koji nisu „prefiksni” $\infty$. Zatim, vraćajući se po sufiksnim poveznicama odozdo prema gore, vrijednost svakog roditelja uspoređujemo s vrijednostima sve njegove djece i uzimamo minimum (ne zaboravimo početnu vrijednost samog roditelja). Tako dobivena vrijednost u svakom čvoru upravo je najmanji element skupa $\operatorname{endpos}$ tog čvora.
    
    Pri upitu u automatu pronađemo čvor koji odgovara uzorku $P$; ako postoji, odgovor je vrijednost tog čvora umanjena za $|P|-1$, a ako ne postoji, odgovor ne postoji.
    
    Vremenska složenost pretprocesiranja je $O(|T|)$, a jednog upita $O(|P|)$.

??? note "Rješenje 2"
    Izgradimo sufiksni automat. Za sva stanja SAM-a pretprocesiramo pozicije $\operatorname{firstpos}$. Drugim riječima, za svako stanje $v$ želimo pronaći poziciju kraja prvog pojavljivanja tog stanja, $\operatorname{firstpos}[v]$. Želimo, dakle, najprije pronaći najmanji element svakog skupa $\operatorname{endpos}$ (očito ne možemo eksplicitno održavati sve skupove $\operatorname{endpos}$).
    
    Da bismo održavali pozicije $\operatorname{firstpos}$, proširujemo funkciju `sam_extend()`. Kad stvaramo novo stanje $\textit{cur}$, postavljamo:
    
    $$
    \operatorname{firstpos}(\textit{cur})=\operatorname{len}(\textit{cur})-1.
    $$
    
    Kad kloniramo čvor $q$ u $\textit{clone}$, postavljamo:
    
    $$
    \operatorname{firstpos}(\textit{clone})=\operatorname{firstpos}(q).
    $$
    
    (Jer je jedina druga moguća vrijednost, $\operatorname{firstpos}(\textit{cur})$, očito prevelika.)
    
    Odgovor na upit tada je $\operatorname{firstpos}(t)-\left|P\right|+1$, gdje je $t$ stanje koje odgovara nizu $P$. Jedan upit zahtijeva samo $O(\left|P\right|)$ vremena.

### Sve pozicije pojavljivanja

???+ example "Problem"
    Problem je isti kao prethodni, ali sada treba pronaći sve pozicije pojavljivanja uzorka $P$ u tekstu $T$.

??? note "Rješenje 1"
    Nakon što pronađemo čvor koji odgovara uzorku $P$, iskoristimo informacije iz stabla sufiksnih poveznica i obiđemo podstablo; čim naiđemo na „prefiksni čvor”, ispišemo ga.
    
    Složenost jednog upita je $O(|P|)+O(\textit{answer}(P))$, gdje je $\textit{answer}(P)$ broj odgovora na taj upit. Po uzoru na [dokaz linearnosti broja stanja](#broj-stanja) može se pokazati da veličina podstabla u stablu sufiksnih poveznica ne premašuje dvostruku veličinu skupa $\operatorname{endpos}$ tog čvora, pa je složenost obilaska podstabla $O(\textit{answer}(P))$.

??? note "Rješenje 2"
    I ovdje izgradimo sufiksni automat teksta $T$. Slično kao u prethodnom problemu, za sva stanja izračunamo pozicije $\operatorname{firstpos}$.
    
    Ako je $t$ stanje koje odgovara uzorku $P$, očito je $\operatorname{firstpos}(t)$ jedan od odgovora. Pronašli smo stanje automata koje odgovara $P$. Koje još pozicije treba pronaći? Upravo one koje odgovaraju stanjima nizova kojima je $P$ sufiks. Drugim riječima, trebamo pronaći sva stanja iz kojih se sufiksnim poveznicama može stići u stanje $t$.
    
    Stoga za rješavanje problema za svako stanje pamtimo popis sufiksnih poveznica koje pokazuju na njega. Odgovor na upit čine vrijednosti $\operatorname{firstpos}$ svih stanja do kojih iz stanja $t$ dolazimo DFS-om ili BFS-om isključivo po obrnutim sufiksnim poveznicama.
    
    Složenost pretprocesiranja je $O(|T|)$, a jednog upita $O(|P|+\textit{answer}(P))$.
    
    Nijedno stanje nećemo posjetiti dvaput (jer svako stanje ima samo jednu sufiksnu poveznicu, pa ne postoje dva različita puta do istog stanja).
    
    Treba samo razmotriti dva različita stanja koja mogu imati istu vrijednost $\operatorname{firstpos}$. To se događa samo kad je jedno stanje klon drugoga. No to ne utječe na analizu složenosti. Po uzoru na [dokaz linearnosti broja stanja](#broj-stanja), broj svih takvih stanja sa sufiksom $P$ ne premašuje $2\textit{answer}(P)$.
    
    Osim toga, dvostruke pozicije možemo ukloniti tako da ne uzimamo u obzir vrijednosti $\operatorname{firstpos}$ kloniranih čvorova. Naime, svakoj poziciji pojavljivanja u podstablu čvora $t$ odgovara točno jedno neklonirano stanje. Stoga, ako za svako stanje bilježimo oznaku `is_clone` koja govori je li stanje nastalo kloniranjem, klonirana stanja možemo jednostavno zanemariti i ispisati vrijednosti $\operatorname{firstpos}$ svih ostalih stanja.
    
    Slijedi okvirna implementacija:
    
    ```cpp
    struct state {
      bool is_clone;
      int first_pos;
      std::vector<int> inv_link;
      // some other variables
    };
    
    // nakon izgradnje SAM-a
    for (int v = 1; v < sz; v++) st[st[v].link].inv_link.push_back(v);
    
    // ispis svih pozicija pojavljivanja
    void output_all_occurrences(int v, int P_length) {
      if (!st[v].is_clone) cout << st[v].first_pos - P_length + 1 << endl;
      for (int u : st[v].inv_link) output_all_occurrences(u, P_length);
    }
    ```

### Najkraći niz koji se ne pojavljuje

???+ example "Problem"
    Zadan je niz $S$ i određena abeceda; treba pronaći najkraći niz koji se ne pojavljuje u $S$.

??? note "Rješenje"
    Provodimo dinamičko programiranje na sufiksnom automatu niza $S$.
    
    Pretpostavimo da smo već obradili dio podniza i da se nalazimo u stanju $v$; želimo pronaći najmanji broj znakova koje treba dodati da bismo naišli na nepostojeći prijelaz, i taj broj u čvoru $v$ označimo $d_v$.
    
    Računanje $d_{v}$ vrlo je jednostavno. Ako barem jedan znak abecede nema prijelaz iz $v$, onda je $d_{v}=1$. Inače dodavanje jednog znaka nije dovoljno i trebamo minimum po svim prijelazima:
    
    $$
    d_{v}=1+\min_{w:(v,w,c)\in \text{SAM}}d_{w}
    $$
    
    Odgovor na problem je $d_{t_0}$, a sam niz možemo rekonstruirati unatrag iz izračunatog polja $d$.

### Najdulji zajednički podniz dvaju nizova

???+ example "Problem"
    Zadana su dva niza $S$ i $T$; treba pronaći najdulji zajednički podniz, pri čemu je zajednički podniz niz $X$ koji se pojavljuje kao podniz i u $S$ i u $T$.

??? note "Rješenje"
    Izgradimo sufiksni automat niza $S$.
    
    Sada obrađujemo niz $T$: za svaki njegov prefiks tražimo najdulji sufiks tog prefiksa koji se pojavljuje u $S$. Drugim riječima, za svaku poziciju u nizu $T$ želimo pronaći duljinu najduljeg zajedničkog podniza nizova $S$ i $T$ koji završava na toj poziciji.
    
    U tu svrhu koristimo dvije varijable: **trenutačno stanje** $v$ i **trenutačnu duljinu** $l$. One opisuju trenutačno podudaranje: njegovu duljinu i stanje koje mu odgovara.
    
    Na početku je $v=t_0$ i $l=0$, tj. podudaranje je prazni niz.
    
    Opišimo sada kako dodati znak $T_{i}$ i za njega ponovno izračunati odgovor:
    
    -   Ako iz $v$ postoji prijelaz po znaku $T_{i}$, samo prijeđemo i povećamo $l$ za jedan.
    -   Ako takav prijelaz ne postoji, moramo skratiti trenutačno podudaranje, što znači da prelazimo po sufiksnoj poveznici:
    
        $$
        v=\operatorname{link}(v)
        $$
    
        Istodobno treba skratiti trenutačnu duljinu. Očito $l$ postavljamo na $\operatorname{len}(v)$, jer je najdulji niz koji odgovara stanju u koje stižemo nakon tog prijelaza po sufiksnoj poveznici jedan podniz.
    -   Ako i dalje nema prijelaza po tom znaku, ponavljamo prelaženje po sufiksnim poveznicama uz smanjivanje $l$ dok ne pronađemo prijelaz ili ne stignemo u početno stanje $t_0$ koje također nema taj prijelaz (što znači da se znak $T_{i}$ uopće ne pojavljuje u $S$; tada je $v=l=0$).
    
    Očito je odgovor na problem najveća od svih vrijednosti $l$.
    
    Vremenska složenost ovog dijela je $O(\left|T\right|)$, jer pri svakom pomaku ili povećamo $l$ za jedan ili se nekoliko puta pomaknemo po sufiksnim poveznicama, svaki put smanjujući $l$.
    
    Implementacija:
    
    ```cpp
    string lcs(const string &S, const string &T) {
      sam_init();
      for (int i = 0; i < S.size(); i++) sam_extend(S[i]);
    
      int v = 0, l = 0, best = 0, bestpos = 0;
      for (int i = 0; i < T.size(); i++) {
        while (v && !st[v].next.count(T[i])) {
          v = st[v].link;
          l = st[v].len;
        }
        if (st[v].next.count(T[i])) {
          v = st[v].next[T[i]];
          l++;
        }
        if (l > best) {
          best = l;
          bestpos = i;
        }
      }
      if (best == 0) return "";
      return T.substr(bestpos - best + 1, best);
    }
    ```

Primjer zadatka: [SPOJ Longest Common Substring](https://www.spoj.com/problems/LCS/en/)

### Najdulji zajednički podniz više nizova

???+ example "Problem"
    Zadano je $k$ nizova $S_i$. Treba pronaći njihov najdulji zajednički podniz, tj. niz $X$ koji se pojavljuje kao podniz u svakom od nizova.

??? note "Rješenje 1"
    Sve nizove spojimo u jedan dulji niz $T$, odvajajući ih posebnim znakovima $D_i$ (po jedan znak za svaki niz):
    
    $$
    T=S_1+D_1+S_2+D_2+\cdots+S_k+D_k.
    $$
    
    Zatim izgradimo sufiksni automat niza $T$.
    
    Sada u automatu trebamo pronaći niz koji postoji u svim nizovima $S_i$, za što možemo iskoristiti dodane posebne znakove. Ako $S_j$ sadrži podniz $X$, onda iz čvora $t$ koji odgovara podnizu $X$ nužno postoji put do $D_j$ koji ne prolazi ni kroz jedan drugi posebni znak $D_1,\cdots,D_{j-1},D_{j+1},\cdots,D_k$. Za zajednički podniz $X$ takav put mora postojati za svaki posebni znak $D_j$.
    
    Stoga trebamo izračunati dostižnost, tj. za svako stanje automata i svaki znak $D_i$ postoji li takav put. To se lako računa DFS-om ili BFS-om i dinamičkim programiranjem. Nakon toga je odgovor najdulji među nizovima $\operatorname{longest}(v)$ svih stanja $v$ iz kojih su dostižni svi posebni znakovi.

??? note "Rješenje 2"
    Neka je **najkraći** niz $S_1$; za njega izgradimo SAM. Algoritmom za najdulji zajednički podniz dvaju nizova izračunamo duljinu najduljeg zajedničkog podniza svakog od preostalih nizova sa $S_1$. Tijekom podudaranja, za svaki dodani znak niza $S_j$ koji podudaramo odgovarajuće se pomičemo po SAM-u, pa možemo izravno zabilježiti najveću duljinu podniza niza $S_j$ koju je svako stanje SAM-a podudarilo **tijekom podudaranja**.
    
    Budući da pri podudaranju, kad god podudarimo neko stanje SAM-a, nužno podudarimo i sve njegove pretke u stablu sufiksnih poveznica, ali informacija o duljini podudaranja predaka nije ažurirana, nakon završetka podudaranja niza $S_j$ treba odozdo prema gore po sufiksnim poveznicama ažurirati informaciju o najduljem podudarenom podnizu s djece na roditelje. Pritom treba paziti da najveća zabilježena duljina podudaranja u roditelju ne premaši njegovu vlastitu vrijednost $\operatorname{len}$. Tako za svako stanje SAM-a niza $S_1$ dobivamo duljinu najduljeg podniza niza $S_j$ koji ono **stvarno može podudariti**.
    
    Na kraju je dovoljno podudariti svaki od $S_2,\cdots,S_k$ i za svako stanje SAM-a uzeti minimum zabilježenih stvarno podudarenih duljina; time dobivamo duljinu najduljeg zajedničkog podniza nizova $S_2,\cdots,S_k$ koji svako stanje SAM-a stvarno može podudariti. Zatim obiđemo sva stanja SAM-a i maksimum je duljina najduljeg zajedničkog podniza tih $k$ nizova.
    
    Vremenska složenost algoritma je $O(\sum_i |S_i|)$. Iako SAM niza $S_1$ obilazimo $k$ puta, kako je $|S_1|$ najmanji, vrijedi $k|S_1|\le \sum_i |S_i|$, pa je glavni član složenosti i dalje obilazak svih nizova tijekom podudaranja.

Primjer zadatka: [SPOJ Longest Common Substring II](https://www.spoj.com/problems/LCS2/)

## Zadaci

-   [[predložak] Sufiksni automat](https://www.luogu.com.cn/problem/P3804)
-   [SDOI2016 Generiranje čarolija (生成魔咒)](https://loj.ac/problem/2033)
-   [SPOJ - SUBLEX](https://www.spoj.com/problems/SUBLEX/)
-   [TJOI2015 Teorija struna (弦论)](https://loj.ac/problem/2102)
-   [SPOJ Longest Common Substring](https://www.spoj.com/problems/LCS/en/)
-   [SPOJ Longest Common Substring II](https://www.spoj.com/problems/LCS2/)
-   [Codeforces 1037H Security](https://codeforces.com/problemset/problem/1037/H)
-   [Codeforces 666E Forensic Examination](https://codeforces.com/problemset/problem/666/E)
-   [HDU4416 Good Article Good sentence](https://acm.hdu.edu.cn/showproblem.php?pid=4416)
-   [HDU4436 str2int](https://acm.hdu.edu.cn/showproblem.php?pid=4436)
-   [HDU6583 Typewriter](https://acm.hdu.edu.cn/showproblem.php?pid=6583)
-   [Codeforces 235C Cyclical Quest](https://codeforces.com/problemset/problem/235/C)
-   [CTSC2012 Poznati članak (熟悉的文章)](https://www.luogu.com.cn/problem/P4022)
-   [NOI2018 Tvoje ime (你的名字)](https://uoj.ac/problem/395)

## Literatura

Najprije navodimo neke od prvih radova o SAM-u:

-   A. Blumer, J. Blumer, A. Ehrenfeucht, D. Haussler, R. McConnell. Linear Size Finite Automata for the Set of All Subwords of a Word. An Outline of Results. \[1983]
-   A. Blumer, J. Blumer, A. Ehrenfeucht, D. Haussler. The Smallest Automaton Recognizing the Subwords of a Text. \[1984]
-   Maxime Crochemore. Optimal Factor Transducers. \[1985]
-   Maxime Crochemore. Transducers and Repetitions. \[1986]
-   A. Nerode. Linear automaton transformations. \[1958]

Osim toga, tema se može naći u novijim izvorima i u mnogim knjigama o algoritmima na nizovima:

-   Maxime Crochemore, Wojciech Rytter. Jewels of Stringology. \[2002]
-   Bill Smyth. Computing Patterns in Strings. \[2003]
-   Bill Smyth. Методы и алгоритмы вычислений на строках (ruski prijevod prethodne knjige). \[2006]

Još neki materijali:

-   „Sufiksni automat” (《后缀自动机》), Chen Lijie.
-   „Proširenje sufiksnog automata na trie” (《后缀自动机在字典树上的拓展》), Liu Yanyi.
-   „Sufiksni automat i njegove primjene” (《后缀自动机及其应用》), Zhang Tianyang.
-   <https://www.cnblogs.com/zinthos/p/3899679.html>
-   <https://codeforces.com/blog/entry/20861>
-   <https://zhuanlan.zhihu.com/p/25948077>

**Ova je stranica uglavnom prevedena prema blogu [Суффиксный автомат](http://e-maxx.ru/algo/suffix_automata) i njegovu engleskom prijevodu [Suffix Automaton](https://cp-algorithms.com/string/suffix-automaton.html). Ruska je inačica pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0.**

[^state-endpos]: Razlog zbog kojeg svako stanje treba uzeti kao jednu klasu ekvivalencije $\operatorname{endpos}$ zapravo je Myhill–Nerodeov teorem spomenut u sljedećem odlomku. Ukratko, ako dva niza $t$ i $u$ imaju različite skupove $\operatorname{endpos}$, ona ne mogu odgovarati istom stanju SAM-a: putovi od istog stanja do završnih stanja uvijek su isti, što znači da su načini na koje se dodavanjem znakova na kraj nizova $t$ i $u$ stiže do kraja niza $s$ također isti, a to upravo znači da $t$ i $u$ imaju iste završne pozicije u nizu $s$. Obrnuto, čim dva niza $t$ i $u$ imaju iste skupove $\operatorname{endpos}$, mogu se pridružiti istom stanju SAM-a. To da je to izvedivo sadržaj je dokaza Myhill–Nerodeova teorema i ovdje o tome nećemo dalje raspravljati. No iz ove se rasprave barem može vjerovati da je SAM dobiven stavljanjem nizova s istim skupovima $\operatorname{endpos}$ u isto stanje nužno minimalan, jer daljnje spajanje čvorova nije moguće.

[^time-complexity]: Ako ne koristimo dodatnu listu postojećih prijelaza trenutačnog stanja, nego sve moguće prijelaze (postojeće ili ne) pohranjujemo samo u polje i pri kloniranju čvora izravno ga kopiramo, vremenska složenost također je $O(n\left|\Sigma\right|)$.

[^monotone-loc]: Ono što u glavnom tekstu nije objašnjeno jest je li i u slučajevima 1 i 2 pozicija niza $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$ monotono (slabo) rastuća. Slučaj 1 lako se provjerava: nakon ažuriranja je $\operatorname{link}(\textit{last})=t_0$, a $\operatorname{link}(\operatorname{link}(\textit{last}))$ virtualno je stanje $-1$; niz koji mu odgovara možemo smatrati praznim nizom na kraju trenutačnog niza, čija pozicija poprima najveću vrijednost. U slučaju 2 prijelaz je kontinuiran, što znači $\operatorname{longest}(q) = \operatorname{longest}(p)+c$. No dodavanje novog znaka na kraj podniza samo otežava njegovo pojavljivanje u nizu; drugim riječima, kad skup završnih pozicija sufiksa niza $\operatorname{longest}(p)$ duljine $\operatorname{len}(\operatorname{link}(p))$ strogo sadrži $\operatorname{endpos}(p)$, skup završnih pozicija sufiksa niza $\operatorname{longest}(q)$ duljine $\operatorname{len}(\operatorname{link}(p))+1$ možda je i dalje jednak $\operatorname{endpos}(q)$. Stoga je $\operatorname{len}(\operatorname{link}(q))\le\operatorname{len}(\operatorname{link}(p))+1$, tj. početna pozicija niza $\operatorname{longest}(\operatorname{link}(p))$ kao sufiksa niza $s$ nije veća od početne pozicije niza $\operatorname{longest}(\operatorname{link}(q))$ kao sufiksa niza $s+c$. A kad prvi put pronađemo stanje $p$ koje ima prijelaz po $c$, nužno smo se pomaknuli barem jednom, što znači da početna pozicija niza $\operatorname{longest}(\operatorname{link}(p))$ kao sufiksa niza $s$ nije manja od početne pozicije niza $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$ kao sufiksa niza $s$. Naposljetku, $\operatorname{longest}(\operatorname{link}(q))=\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{cur})))$. To pokazuje da je i u slučaju 2 pozicija niza $\operatorname{longest}(\operatorname{link}(\operatorname{link}(\textit{last})))$ monotono (slabo) rastuća.
