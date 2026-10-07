---
title: Optimizacija Slope Trick
---

## Uvod

Za jednu klasu dvodimenzionalnih DP problema, ako je funkcija vrijednosti $f(i,x)$ za svaki fiksni $i$ konveksna funkcija od $x$, tada se cijela funkcija $f(i,\cdot)$ može promatrati kao stanje u $i$ i umjesto same funkcije održavati njezina diferencija (ili nagib)

$$
\Delta f(i,x) = f(i,x+1)-f(i,x)
$$

što često optimizira prijelaze. Ta se ideja optimizacije DP-a naziva Slope Trick.

???+ info "„Nagib”"
    Budući da funkcije u većini zadataka poprimaju vrijednosti samo u cjelobrojnim točkama, nema bitne razlike između naziva „diferencija” i „nagib”; u skladu s nazivom Slope Trick, ovaj ga tekst dosljedno zove nagib.

Način održavanja nagiba može se razlikovati od zadatka do zadatka. Ako je raspon vrijednosti nagiba uzak, zgodnije je održavati točke u kojima se nagib mijenja (tj. lomne točke); ako je pak domena funkcije uska, možda je zgodnije održavati sam niz nagiba. U složenijim situacijama može biti potrebno istodobno održavati i veličinu nagiba svakog segmenta i njegovu duljinu. Bez obzira na konkretan način održavanja, bit ovih problema jest iskoristiti činjenicu da se niz nagiba pri prijelazu stanja malo mijenja kako bi se prijelaz pojednostavnio. Stoga se svi oni mogu zvati Slope Trick.

## Konveksne funkcije

Prije rasprave o konkretnim zadacima potrebno je najprije upoznati osnovna svojstva konveksnih funkcija te kako se njihov nagib mijenja pri raznim transformacijama konveksnih funkcija.

### Konveksne funkcije na realnom pravcu

Općenitija definicija konveksne funkcije daje se na $\mathbf R$.

![](../images/slope-trick/epigraph-convex-def.svg)

???+ abstract "Konveksna funkcija na $\mathbf R$"
    Ako funkcija $f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$ za sve $x,y\in\mathbf R$ i $\alpha\in(0,1)$ zadovoljava
    
    $$
    f(\alpha x+(1-\alpha)y) \le \alpha f(x)+(1-\alpha)f(y),
    $$
    
    kažemo da je $f$ **konveksna funkcija** (convex function); pritom su pravila računanja s $\pm\infty$ takva da $\pm\infty$ pomnoženo bilo kojim pozitivnim realnim brojem ili uvećano za bilo koji realni broj ostaje $\pm\infty$, a za svaki realni broj $x\in\mathbf R$ vrijedi $-\infty<x<+\infty$.

Naravno, zamijeni li se znak nejednakosti sa $\ge$, funkcija se zove konkavnom[^convex-def]. Budući da je za konkavnu funkciju $f$ funkcija $-f$ uvijek konveksna, u ovom odjeljku razmatramo samo konveksne funkcije.

???+ info "Ovaj tekst razmatra samo prave konveksne funkcije"
    Da bismo izbjegli raspravu o vrijednosti $\infty-\infty$ i dodatnu složenu analizu, pri raspravi o pojmovima vezanim uz konveksne funkcije u ovom tekstu uvijek pretpostavljamo da funkcija ne poprima vrijednost $-\infty$ i da nije identički jednaka $+\infty$. Takve se konveksne funkcije zovu **prave konveksne funkcije** (proper convex function). To je dovoljno za razumijevanje sadržaja koji se javlja u algoritamskim natjecanjima.

Naravno, funkcija $f$ često nije definirana za sve realne brojeve. Ako je domena funkcije $f$ samo podskup od $\mathbf R$, možemo je proširiti na funkciju na $\mathbf R$:

$$
\tilde f(x) = \begin{cases} f(x), & x\in\operatorname{dom}f,\\ +\infty,& x\notin\operatorname{dom}f.\end{cases}
$$

Tada kažemo da je $f$ konveksna ako i samo ako pripadna $\tilde f$ zadovoljava gornju definiciju konveksne funkcije. Stoga, ako nije posebno naglašeno, domena konveksnih funkcija spomenutih u ovom tekstu uvijek je skup realnih brojeva $\mathbf R$. Očito, konveksna funkcija $f$ može poprimati konačne vrijednosti samo na jednom intervalu (tj. konveksnom podskupu od $\mathbf R$).

???+ example "Jednostavni primjeri"
    Uobičajeni primjeri konveksnih funkcija su:
    
    1.  konstantna funkcija: $f(x)=c$, gdje je $c\in\mathbf R$;
    2.  linearna funkcija: $f(x)=kx+b$, gdje su $k,b\in\mathbf R$ i $k\neq 0$;
    3.  apsolutna vrijednost: $f(x)=|x-a|$, gdje je $a\in\mathbf R$;
    4.  restrikcija bilo koje konveksne funkcije na neki interval, npr. $0_{[a,b]}(x)$ (u kontekstu konveksne analize zove se i indikatorska funkcija intervala $[a,b]$).

Naravno, pomoću transformacija koje čuvaju konveksnost, opisanih u nastavku, mogu se sastaviti složenije konveksne funkcije.

### Konveksne funkcije na diskretnim skupovima točaka

U algoritamskim natjecanjima mnoge su funkcije definirane samo u nekim cjelobrojnim točkama. One općenito nisu konveksne funkcije (u gore definiranom smislu), jer im domena više nije konveksan skup. Da bismo obradili tu situaciju, konveksnost funkcija na diskretnim skupovima točaka treba definirati zasebno. Ukratko, funkciju najprije treba linearno interpolirati, čime se njezina domena proširuje na interval, a zatim ispitati njezinu konveksnost.

![](../images/slope-trick/epigraph-convex-discrete.svg)

???+ abstract "Konveksna funkcija na diskretnom skupu točaka"
    Neka je $S\subset\mathbf R$ diskretan skup točaka, tj. za svaki zatvoreni interval $[a,b]$ skup $S\cap[a,b]$ je konačan. Za funkciju $f:S\rightarrow\mathbf R\cup\{\pm\infty\}$ možemo definirati funkciju $\tilde f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$ tako da:
    
    -   za $x\in S$ vrijedi $\tilde f(x)=f(x)$,
    -   za $x\in(\inf S,\sup S)\setminus S$, uz $s_-=\max\{s\in S:s\le x\}$ i $s_+=\min\{s\in S:s\ge x\}$, vrijedi
    
        $$
        \tilde f(x) = \dfrac{s_+-x}{s_+-s_-}f(s_-)+\dfrac{x-s_-}{s_+-s_-}f(s_+),
        $$
    -   za $x\notin[\inf S,\sup S]$ vrijedi $\tilde f(x)=+\infty$.
    
    Ako je tada $\tilde f(x)$ konveksna funkcija na $\mathbf R$, kažemo da je $f(x)$ **konveksna funkcija** na $S$.

Budući da je s konveksnim funkcijama na $\mathbf R$ lakše raditi, kad se u ovom tekstu spominju konveksne funkcije, ako nije posebno rečeno, misli se na konveksne funkcije na $\mathbf R$. Ako su za neku funkciju u ovom tekstu zadane vrijednosti samo u nekim cjelobrojnim točkama, njezine vrijednosti u ostalim realnim točkama određene su funkcijom $\tilde f$ iz definicije, što je isto kao da izravno razmatramo pripadnu po dijelovima linearnu funkciju $\tilde f$.

Konveksne funkcije na skupu cijelih brojeva $\mathbf Z$ imaju zorniju ekvivalentnu definiciju:

???+ note "Ekvivalentna definicija konveksne funkcije na $\mathbf Z$"
    Funkcija $f:\mathbf Z\rightarrow\mathbf R\cup\{\pm\infty\}$ je konveksna ako i samo ako
    
    $$
    f(x)-f(x-1)\le f(x+1)-f(x)
    $$
    
    vrijedi za sve $x\in\mathbf Z$.

??? note "Dokaz"
    Ova je tvrdnja jednostavna posljedica karakterizacije konveksnih funkcija nagibom.
    
    Ako je $f$ konveksna funkcija na $\mathbf Z$, tada, budući da je nagib slabo rastući, vrijedi
    
    $$
    \Delta f(x-1,x)\le \Delta f(x-1,x+1) \le\Delta f(x,x+1).
    $$
    
    To je upravo gornji uvjet.
    
    Obratno, ako gornji uvjet vrijedi, tada za sve $x_1<x_2$ imamo
    
    $$
    \Delta f(x_1,x_2) = \dfrac{1}{x_2-x_1}\sum_{i=x_1}^{x_2-1}\left(f(i+1)-f(i)\right).
    $$
    
    To je aritmetička sredina svih diferencija za $x_1\le i<x_2$. Poveća li se $x_2$ za jedan, to odgovara umetanju jedne veće diferencije; poveća li se $x_1$ za jedan, to odgovara uklanjanju najmanje diferencije. Obje operacije čine da sredina slabo raste. To pokazuje da nagib $\Delta f(x_1,x_2)$ slabo raste, tj. da je $f$ konveksna funkcija na $\mathbf Z$.

Drugim riječima, čim je nagib (diferencija) monotono nepadajući, niz se može promatrati kao konveksna funkcija na $\mathbf Z$.

### Dvije karakterizacije konveksnih funkcija

Zapravo, karakterizacija konveksnih funkcija nagibom može se poopćiti na opći slučaj.

???+ note "Karakterizacija konveksnih funkcija nagibom"
    Neka je $S$ skup $\mathbf R$ ili njegov diskretan podskup. Funkcija $f:S\rightarrow\mathbf R\cup\{\pm\infty\}$ konveksna je ako i samo ako je nagib
    
    $$
    \Delta f(x_1,x_2) = \dfrac{f(x_2)-f(x_1)}{x_2-x_1}
    $$
    
    za sve $x_1,x_2\in S$ s $x_1<x_2$ slabo rastuća funkcija od $x_1$ i od $x_2$.

??? note "Dokaz"
    Za funkciju $f(x)$ na $\mathbf R$ i $x_1<x_2$, te za $\alpha\in(0,1)$, neka je $x_3=\alpha x_1+(1-\alpha)x_2$; tada je
    
    $$
    \Delta f(x_1,x_3) \le \Delta f(x_1,x_2) \le \Delta f(x_3,x_2)
    $$
    
    ekvivalentno s
    
    $$
    \dfrac{f(x_3)-f(x_1)}{1-\alpha} \le f(x_2)-f(x_1) \le \dfrac{f(x_2)-f(x_3)}{\alpha}.
    $$
    
    Obje su nejednakosti ekvivalentne s $f(x_3)\le\alpha f(x_1)+(1-\alpha)f(x_2)$, tj. s konveksnošću funkcije $f(x)$.
    
    Za funkciju $f(x)$ na diskretnom podskupu $S$ od $\mathbf R$, nužnost uvjeta slabog rasta nagiba slijedi iz konveksnosti $\tilde f(x)$. Treba još dokazati dovoljnost, a za to je dovoljno pokazati da je i $\Delta\tilde f(x_1,x_2)$ slabo rastući. Neka je $S=\{s_i\}$, gdje je $s_i$ strogo rastući po $i$, te neka je $s_{i_1}\le x_1\le s_{i_1+1}$ i $s_{i_2}\le x_2\le s_{i_2+1}$; prirodno je $i_1\le i_2$. Neka je $\Delta_i=\Delta f(s_i,s_{i+1})$; tada se može dokazati $\Delta_{i_1}\le\Delta\tilde f(x_1,x_2)\le\Delta_{i_2}$.
    
    Razlikujemo dva slučaja. Ako je $i_1=i_2$, tada je $\Delta_{i_1}=\Delta\tilde f(x_1,x_2)=\Delta_{i_2}$ i nejednakost očito vrijedi. Inače je
    
    $$
    \Delta\tilde f(x_1,x_2) = \dfrac{1}{x_2-x_1}\left((s_{i_1+1}-x_1)\Delta_{i_1}+(x_2-s_{i_2})\Delta_{i_2}+\sum_{j=i_1+1}^{i_2-1}(s_{j+1}-s_j)\Delta_j\right).
    $$
    
    Iz rasta nagiba na $S$ slijedi da je $\Delta_i$ rastući po $i$, pa je $\Delta_{i_1}\le\Delta\tilde f(x_1,x_2)\le\Delta_{i_2}$.
    
    Pomoću tog zaključka, za $x_1<x_2$ i $\alpha\in(0,1)$ neka je $x_3=\alpha x_1+(1-\alpha)x_2$ i odaberimo $i_3$ tako da je $s_{i_3}\le x_3\le s_{i_3+1}$; tada je
    
    $$
    \Delta\tilde f(x_1,x_3) \le \Delta_{i_3} \le \Delta\tilde f(x_3,x_2).
    $$
    
    Uvrštavanjem izraza za $x_3$ dobivamo konveksnost $\tilde f(x)$.

Monotono nepadajući nagib može se smatrati ekvivalentnom definicijom konveksne funkcije. Upravo zato što nagib konveksne funkcije ima svojstvo monotonosti, pri održavanju nagiba obično se biraju strukture podataka poput [hrpe (prioritetnog reda)](../../ds/heap.md) ili [balansiranog stabla](../../ds/bst.md).

U ovom će se tekstu koristiti i druga ekvivalentna karakterizacija konveksnih funkcija. Za funkciju $f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$ možemo promatrati područje ravnine iznad grafa funkcije, tj.

$$
\operatorname{epi} f = \{(x,y)\in\mathbf R^2 : y\ge f(x)\}.
$$

To se područje zove i **epigraf** (epigraph) funkcije $f$. Konveksnost funkcije ekvivalentna je konveksnosti njezina epigrafa:

???+ note "Karakterizacija konveksnih funkcija epigrafom"
    Funkcija $f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$ konveksna je ako i samo ako je $\operatorname{epi}f$ konveksan skup u $\mathbf R^2$.

??? note "Dokaz"
    Ako je $f$ konveksna, tada za $(x_1,y_1),(x_2,y_2)\in\operatorname{epi}f$ i bilo koji $\alpha\in(0,1)$ vrijedi
    
    $$
    \alpha y_1+(1-\alpha)y_2 \ge \alpha f(x_1)+(1-\alpha)f(x_2) \ge f(\alpha x_1+(1-\alpha) x_2).
    $$
    
    Dakle, $\alpha(x_1,y_1)+(1-\alpha)(x_2,y_2)\in\operatorname{epi}f$.
    
    Obratno, ako je $\operatorname{epi}f$ konveksan skup, tada za sve $x_1<x_2$ i $\alpha\in(0,1)$ vrijedi
    
    $$
    \alpha(x_1,f(x_1))+(1-\alpha)(x_2,f(x_2)) \in \operatorname{epi}f.
    $$
    
    To je ekvivalentno s $\alpha f(x_1)+(1-\alpha)f(x_2)\ge f\left(\alpha x_1+(1-\alpha)x_2\right)$, tj. s konveksnošću $f$.

Kasnije ćemo vidjeti da se pomoću epigrafa infimalna konvolucija konveksnih funkcija može povezati sa sumom Minkowskog konveksnih skupova.

## Transformacije konveksnih funkcija

U nastavku predstavljamo neke transformacije koje čuvaju konveksnost, a često se susreću u Slope Tricku.

### Nenegativna linearna kombinacija

Za konveksne funkcije $f$ i $g$ te nenegativne realne brojeve $\alpha,\beta\ge0$, funkcija $\alpha f+\beta g$ također je konveksna. Štoviše,

$$
\Delta(\alpha f+\beta g) = \alpha\Delta f + \beta\Delta g.
$$

Stoga, ako održavamo nagibe konveksnih funkcija $f$ i $g$, nagib njihove nenegativne linearne kombinacije $\alpha f+\beta g$ dobivamo jednostavno računanjem segment po segment.

U problemima u kojima se održavaju nagibi često je jedna od funkcija jednostavna oblika pa se složenost izmjena može smanjiti lijenim oznakama (lazy tags). U problemima u kojima se održavaju lomne točke, za izračun lomnih točaka nagiba funkcije $f+g$ dovoljno je spojiti lomne točke nagiba funkcija $f$ i $g$.

### Infimalna konvolucija (suma Minkowskog)

Druga česta operacija nad konveksnim funkcijama jest infimalna konvolucija. Za funkcije $f$ i $g$ funkcija

$$
h(x) = \inf_{y\in\mathbf R}f(y)+g(x-y)
$$

zove se **infimalna konvolucija**[^inf-conv] (infimal convolution) funkcija $f$ i $g$. Ako su $f$ i $g$ konveksne, konveksna je i njihova infimalna konvolucija.

![](../images/slope-trick/epigraph-convex-minkowski.svg)

??? example "Objašnjenje slike"
    Kao na slici, da bismo dobili infimalnu konvoluciju $h$ funkcija $f$ i $g$, svaku točku grafa funkcije $f$ (crvena isprekidana crta na trećoj slici) možemo smatrati ishodištem i u pripadnom koordinatnom sustavu nacrtati graf funkcije $g$ (plava isprekidana crta na trećoj slici). Kad se ishodište koordinatnog sustava pomiče po grafu funkcije $f$, obris traga koji ostavlja graf (epigraf) funkcije $g$ (tj. donja konveksna ljuska) upravo je graf funkcije $h$. Vidi se da je svaki segment nagiba funkcije $h$ ili segment nagiba funkcije $f$ ili segment nagiba funkcije $g$: samo su iznova poredani po veličini nagiba. Pritom se uloge $f$ i $g$ mogu zamijeniti, tj. pomičemo li graf funkcije $f$ po grafu funkcije $g$, rezultat je isti.

Geometrijski gledano, $\operatorname{epi}h$ je upravo [suma Minkowskog](../../geometry/convex-hull.md#闵可夫斯基和) skupova $\operatorname{epi}f$ i $\operatorname{epi}g$. Ako su $f$ i $g$ po dijelovima linearne funkcije, tada je i $h$ po dijelovima linearna, a njezini segmenti nagiba mogu se promatrati kao rezultat spajanja (i ponovnog sortiranja) segmenata nagiba funkcija $f$ i $g$.

??? note "Dokaz"
    Neka su $f,g$ konveksne funkcije i $h$ njihova infimalna konvolucija. Neka je $x_1<x_2$ i $\alpha\in(0,1)$. Prema definiciji infimalne konvolucije, za svaki $\varepsilon>0$ postoje $y_i,z_i\in\mathbf R$ takvi da je $y_i+z_i=x_i$ i
    
    $$
    h(x_i) + \varepsilon > f(y_i) + g(z_i).
    $$
    
    Stoga, kombinirajući konveksnost $f,g$ i definiciju $h$, imamo
    
    $$
    \begin{aligned}
    \alpha h(x_1)+(1-\alpha)h(x_2) + \varepsilon 
    &> \alpha f(y_1) + (1-\alpha) f(y_2) + \alpha g(z_1) + (1-\alpha) g(z_2)\\
    &\ge f\left(\alpha y_1+(1-\alpha)y_2\right) + g\left(\alpha z_1+(1-\alpha)z_2\right)\\
    &\ge h(\alpha x_1+(1-\alpha)x_2).
    \end{aligned}
    $$
    
    Budući da je $\varepsilon>0$ odabran proizvoljno, vrijedi
    
    $$
    \alpha h(x_1)+(1-\alpha)h(x_2) \ge h(\alpha x_1+(1-\alpha)x_2).
    $$
    
    Time je dobivena konveksnost $h$.
    
    Zatim, što se tiče geometrijske intuicije, strogo govoreći može se dokazati samo sljedeće:
    
    $$
    \operatorname{epi} f + \operatorname{epi} g\subseteq \operatorname{epi}h \subseteq \operatorname{cl}(\operatorname{epi} f + \operatorname{epi} g).
    $$
    
    Ovdje $\operatorname{cl}$ označava zatvarač.
    
    Za svaki $(x,y)\in\operatorname{epi} f + \operatorname{epi} g$ postoje $(x_1,y_1)\in\operatorname{epi} f$ i $(x_2,y_2)\in\operatorname{epi} g$ takvi da je $x=x_1+x_2$ i
    
    $$
    y = y_1+y_2 \ge f(x_1)+g(x_2) \ge h(x_1+x_2)=h(x).
    $$
    
    Stoga je $(x,y)\in\operatorname{epi}h$. To pokazuje $\operatorname{epi} f + \operatorname{epi} g\subseteq \operatorname{epi}h$.
    
    Obratno, za svaki $(x,y)\in\operatorname{epi}h$ vrijedi $y\ge h(x)$. Prema definiciji $h$, za svaki $\varepsilon>0$ postoje $x_1+x_2=x$ takvi da je
    
    $$
    y + \varepsilon > f(x_1) + g(x_2).
    $$
    
    Neka je $y_1=f(x_1)$ i $y_2=g(x_2)$; tada je $y+\varepsilon>y_1+y_2$. To pokazuje da za svaki $\varepsilon>0$ postoji $(x_1,y_1)+(x_2,y_2)\in\operatorname{epi} f + \operatorname{epi} g$ koji leži na spojnici točaka $(x,y)$ i $(x,y+\varepsilon)$. Puštajući $\varepsilon\rightarrow 0$ dobivamo $\operatorname{epi}h \subseteq \operatorname{cl}(\operatorname{epi} f + \operatorname{epi} g)$.
    
    Dakle, čim je $\operatorname{epi} f + \operatorname{epi} g$ zatvoren skup, vrijedi $\operatorname{epi} f + \operatorname{epi} g = \operatorname{epi}h$. Jedan uvjet koji to osigurava jest da su $f$ i $g$ prave konveksne funkcije i [odozdo poluneprekidne](https://en.wikipedia.org/wiki/Semi-continuity). Za primjene u algoritamskim natjecanjima to je dovoljno; primjerice, po dijelovima linearne funkcije uvijek zadovoljavaju te uvjete.

U praktičnim zadacima, ako jedna od funkcija $f$ i $g$ ima malo segmenata nagiba, manji skup segmenata možemo izravno umetnuti u veći; inače može biti potrebno upotrijebiti [heurističko spajanje](../../graph/dsu-on-tree.md) ili [spojive hrpe](../../ds/heap.md) i slične metode kako bi se smanjila ukupna složenost spajanja, ili pronaći odgovarajući postupak ovisno o konkretnom zadatku.

### Operacije minimuma i maksimuma

Maksimum dviju konveksnih funkcija opet je konveksna funkcija, ali minimum dviju konveksnih funkcija ne mora biti konveksan.

Mnoge se uobičajene operacije minimuma mogu svesti na infimalnu konvoluciju:

???+ example "Primjeri"
    -   $f(x)=\min_{y\in [x+a,x+b]}g(y)$ i dalje je konveksna funkcija, jer se može promatrati kao infimalna konvolucija:
    
        $$
        f(x) = \min_{y\in\mathbf R}g(y) + 0_{[-b,-a]}(x-y).
        $$
    -   $f(x)=\min\{g(x-a_i)+b_i\}$ konveksna je funkcija na $\mathbf Z$ čim je $g(x)$ konveksna funkcija na $\mathbf Z$, a funkcija $h:a_i\mapsto b_i$ definirana na konačnom skupu $\{a_i\}\subset\mathbf Z$ također je konveksna na tom diskretnom skupu. Naime, proširena funkcija $\tilde f(x)$ može se promatrati kao infimalna konvolucija:
    
        $$
        \tilde f(x) = \min_{y\in\mathbf R}\tilde h(y)+\tilde g(x-y).
        $$
    
        Stoga je i funkcija $f(x)$ prije proširenja konveksna.

No ne čuvaju sve operacije minimuma konveksnost.

???+ example "Protuprimjer"
    Neka je $g(x)$ konveksna funkcija; funkcija $f(x)=\min\{g(x-1)+kx,g(x)\}$ ne mora biti konveksna.

U nekim posebnim zadacima, iako se jednadžba prijelaza dinamičkog programiranja može zapisati kao minimum dviju konveksnih funkcija i teško ju je svesti na oblik infimalne konvolucije, funkcija vrijednosti ipak ostaje konveksna. U praksi je za takve zadatke obično potrebno kombinirati ispisivanje tablica i pogađanje kako bi se pronašao razuman način prijelaza nagiba.

Nakon što smo upoznali konveksne funkcije i njihove uobičajene transformacije, metodu optimizacije DP-a Slope Trickom možemo razumjeti kroz konkretne zadatke. Primjeri u ovom tekstu grubo se dijele u dvije skupine, održavanje lomnih točaka i održavanje nagiba, kako bi se razumjele uobičajene operacije i detalji implementacije tih dvaju načina održavanja. No, kao što je ranije naglašeno, način održavanja nije bit Slope Tricka; prikladan način održavanja segmenata nagiba treba odabrati prema potrebama konkretnog zadatka.

## Održavanje lomnih točaka

Ova se klasa problema obično javlja u zadacima u kojima treba minimizirati zbroj nekoliko apsolutnih vrijednosti. Budući da u tim zadacima apsolutna vrijednost nagiba funkcije vrijednosti nije velika, zgodnije je održavati lomne točke u kojima se nagib mijenja.

Održavanje lomnih točaka znači održavanje točaka po dijelovima linearne funkcije u kojima se nagib mijenja. To odgovara tome da za svaki segment nagiba $[l_i,r_i]$ s nagibom $k_i$ održavamo samo podatke o krajevima, dok sam nagib ne treba dodatno održavati; stoga se u tim zadacima nagib pri svakoj promjeni mora promijeniti samo za fiksnu veličinu. Na primjer, ako održavamo skup lomnih točaka $\xi_{-s}\le\cdots\le\xi_{-1}\le\xi_{1}\le\cdots\le\xi_{t}$, to znači: na intervalu $[\xi_{-1},\xi_1]$ nagib je $0$; pri svakom prelasku lomne točke ulijevo nagib se smanjuje za jedan; pri svakom prelasku lomne točke udesno nagib se povećava za jedan; stoga je na intervalu $[\xi_2,\xi_3]$ nagib $2$, na intervalu $[\xi_{-3},\xi_{-2}]$ nagib je $-2$, i tako dalje. Formalno, funkcija se pomoću lomnih točaka nagiba može zapisati kao

$$
f(x) = f(\xi_1) + \sum_{i=-s}^{-1}\max\{\xi_i-x,0\} + \sum_{i=1}^{t}\max\{x-\xi_i,0\}.
$$

Njezin je minimum $f(\xi_{-1})=f(\xi_1)$ i postiže se u bilo kojoj točki intervala $[\xi_{-1},\xi_1]$.

![](../images/slope-trick/epigraph-convex-kinks.svg)

### Primjer: rastući niz najmanje cijene

???+ example "[\[BalticOI 2004\] Sequence](https://www.luogu.com.cn/problem/P4331)"
    Zadan je niz $\{a_i\}$ duljine $n$. Pronađite strogo rastući niz $\{b_i\}$ koji minimizira $\sum_i|a_i-b_i|$; ispišite minimum i bilo koje optimalno rješenje $\{b_i\}$.

??? note "Rješenje"
    Najprije, $\{b_i\}$ je strogo rastući ako i samo ako je $\{b'_i\}=\{b_i-i\}$ slabo rastući. Stoga za $\{a'_i\}=\{a_i-i\}$ možemo pronaći slabo rastući niz $\{b'_i\}=\{b_i-i\}$ s najmanjom razlikom i zatim ga vratiti u niz $\{b_i\}$.
    
    Razmotrimo naivno DP rješenje. Neka je $f_i(x)$ najmanja razlika između odabranih brojeva i prvih $i$ brojeva niza $\{a'_i\}$ kad je odabrano prvih $i$ brojeva niza $\{b'_i\}$, a $i$-ti broj ne premašuje $x$:
    
    $$
    f_i(x) = \min\sum_{j=1}^i|a'_j-b'_j|\text{ s.t. }b'_1\le b'_2\le\cdots\le b'_i\le x.
    $$
    
    Lako se dobiva jednadžba prijelaza stanja
    
    $$
    f_i(x) = \min_{y\le x}f_{i-1}(y)+|a'_i-y|.
    $$
    
    Početno stanje je $f_0(x)\equiv 0$, a traži se $\min_xf_n(x)$. Koristeći ranije spomenute transformacije konveksnih funkcija, od $f_{i-1}(x)$ do $f_i(x)$ dolazimo u dva koraka:
    
    1.  Najprije dodamo $|a'_i-x|$, što odgovara tome da svim segmentima nagiba na intervalu $(-\infty,a'_i]$ dodamo $-1$, a svim segmentima nagiba na intervalu $[a'_i,+\infty)$ dodamo $1$;
    2.  Zatim dobivenoj funkciji uzmemo minimum, pretvarajući $g(x)=f_{i-1}(x)+|a'_i-x|$ u $f_i(x)=\min_{y\le x}g(y)$. Prema ranijoj analizi, to odgovara infimalnoj konvoluciji $g(x)$ i $0_{[0,+\infty)}$. Budući da potonja ima samo jedan segment nagiba, s nagibom $0$ i beskonačno dugačak udesno, njegovo umetanje među segmente nagiba funkcije $g(x)$ odgovara brisanju svih njezinih segmenata pozitivnog nagiba.
    
    Nakon što smo razjasnili ove operacije, sve bismo segmente nagiba već mogli održavati balansiranim stablom, ali je kod složen. Uočimo da se u zadatku nagib pri svakoj promjeni mijenja za najviše $1$, pa apsolutna vrijednost svakog nagiba ne premašuje $n$. Zgodnije je ne održavati izravno segmente nagiba, nego lomne točke nagiba.
    
    Neka je skup lomnih točaka funkcije $f_{i-1}(x)$ jednak $\xi_{-k}\le\cdots\le\xi_{-1}\le\xi_{1}\le\cdots\le\xi_{\ell}$. Tada gornja dva koraka redom odgovaraju:
    
    1.  dodavanju jedne lomne točke $a'_i$ segmenta negativnog nagiba i jedne lomne točke $a'_i$ segmenta pozitivnog nagiba;
    2.  izbacivanju svih lomnih točaka $\xi_1,\cdots,\xi_{\ell}$ segmenata pozitivnog nagiba.
    
    Pri stvarnom održavanju, budući da nakon svake operacije nema lomnih točaka segmenata pozitivnog nagiba, tj. lomne točke nagiba imaju oblik $\xi_{-k}\le\cdots\le\xi_{-1}$, a operacije se uvijek događaju na granici segmenata pozitivnog i negativnog nagiba, dovoljno je izravno održavati max-hrpu sa svim lomnim točkama. Dva koraka redom odgovaraju:
    
    1.  dvostrukom umetanju $a'_i$;
    2.  izbacivanju vrha hrpe.
    
    Naravno, nakon svakog koraka treba održavati i minimum trenutne funkcije. Budući da nakon operacije nema segmenata pozitivnog nagiba, minimum funkcije je njezina vrijednost u vrhu max-hrpe. Neka je prije svake operacije vrh hrpe $\xi_{-1}$, a minimum $f_{i-1}(\xi_{-1})$. Budući da je izbačeni vrh hrpe najmanja lomna točka segmenata pozitivnog nagiba, minimum funkcije jednak je vrijednosti funkcije u toj točki, pa je dovoljno izravno izračunati vrijednost funkcije u vrhu hrpe prije izbacivanja, tj.
    
    $$
    f_{i-1}(\max\{a'_i,\xi_{-1}\})+|\max\{a'_i,\xi_{-1}\}-a'_i|=f_{i-1}(\xi_{-1})+\max\{0,\xi_{-1}-a'_i\}.
    $$
    
    Pritom su prvi članovi jednaki jer $f_{i-1}(x)$ nema segmenata pozitivnog nagiba. Stoga je svaki put dovoljno minimumu dodavati $\max\{0,\xi_{-1}-a'_i\}$.
    
    Zadatak traži i ispis jednog optimalnog rješenja. Budući da je po završetku posljednje operacije optimalno rješenje vrh hrpe, vrijednost $b'_n$ može se izravno odrediti. Ako je poznato $i$-to optimalno rješenje $b'_i$ i tražimo optimalno rješenje funkcije $f_{i-1}(x)$ uz $x\le b'_i$, dovoljno je primijetiti da je, zbog konveksnosti $f_{i-1}(x)$, rješenje to bolje što je bliže njezinu globalnom minimumu; stoga je dovoljno zabilježiti točku globalnog minimuma funkcije $f_{i-1}(x)$ i uzeti minimum nje i $b'_i$ da bismo dobili optimalni $b'_{i-1}$.
    
    Vremenska složenost je $O(n\log n)$.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/sequence.cpp"
    ```

Ogledni zadaci:

-   [Codeforces 713 C. Sonya and Problem Without a Legend](https://codeforces.com/problemset/problem/713/C)
-   [Luogu P2893 \[USACO08FEB\] Making the Grade G](https://www.luogu.com.cn/problem/P2893)
-   [Luogu P4331 \[BalticOI 2004\] Sequence](https://www.luogu.com.cn/problem/P4331)
-   [Luogu P4597 Niz (sequence)](https://www.luogu.com.cn/problem/P4597)
-   [AtCoder Dwango Programming Contest 2 Qualifiers E - Fireworks](https://atcoder.jp/contests/dwango2016-prelims/tasks/dwango2016qual_e)

### Primjer: prijelazi s ograničenjima

???+ example "[\[NOISG 2018 Finals\] Safety](https://www.luogu.com.cn/problem/P11598)"
    Zadan je niz $\{a_i\}$ duljine $n$. Pronađite niz $\{b_i\}$ takav da vrijedi $|b_i-b_{i-1}|\le h$ za sve $1<i\le n$ i da je $\sum_i|a_i-b_i|$ najmanji mogući; ispišite minimum.

??? note "Rješenje"
    Sadržaj je uglavnom sličan prethodnom zadatku, samo se promijenilo ograničenje na niz $\{b_i\}$. Jednako tako, neka je $f_i(x)$ najmanja razlika prvih $i$ brojeva kad $i$-ti broj ima vrijednost $x$:
    
    $$
    f_i(x) = \min\sum_{j=1}^i|a_j-b_j|\text{ s.t. }|b_{j-1}-b_j|\le h,\forall 1<j\le i,~b_i=x.
    $$
    
    Odatle je jednadžba prijelaza stanja
    
    $$
    f_i(x) = |a_i-x| + \min_{|y-x|\le h} f_{i-1}(y). 
    $$
    
    Početni uvjet je $f_0(x)\equiv 0$. Na kraju i dalje tražimo $\min_xf_n(x)$.
    
    Prijelaz stanja rastavljamo na operacije nad konveksnim funkcijama, u dva koraka:
    
    1.  Najprije od $f_{i-1}(x)$ uzmemo minimum, dobivajući $\min_{|y-x|\le h} f_{i-1}(y)$, što odgovara infimalnoj konvoluciji $f_{i-1}(x)$ i $0_{[-h,h]}(x)$;
    2.  Zatim dobivenoj funkciji dodamo $|a_i-x|$.
    
    Budući da se i ovdje nagib svaki put mijenja za jedan, možemo razmotriti održavanje lomnih točaka. Tada se ova dva koraka opisuju kao:
    
    1.  pomak svih segmenata negativnog nagiba ulijevo za $h$ i svih segmenata pozitivnog nagiba udesno za $h$;
    2.  dvostruko umetanje $a_i$.
    
    Očito je za ovaj zadatak zgodno zasebno održavati segmente pozitivnog i negativnog nagiba. Budući da su operacije uglavnom koncentrirane oko segmenta nultog nagiba, razmotrimo [par hrpa](../../ds/binary-heap.md#对顶堆), tj. max-hrpom i min-hrpom zasebno održavamo lomne točke segmenata negativnog i pozitivnog nagiba. Pomak svih lomnih točaka izvodimo lijenom oznakom. U drugom koraku u svaku od dviju hrpa umećemo po jedan $a_i$; nakon umetanja vrh max-hrpe ne mora više biti manji ili jednak vrhu min-hrpe. Tada zamjenjujemo vrhove hrpa dok odnos veličina vrhova ne bude zadovoljen.
    
    Na kraju razmotrimo kako tijekom operacija ažurirati minimum. Budući da pomak u prvom koraku ne mijenja minimum, dovoljno je razmotriti operaciju zamjene vrhova hrpa. Neka je $\xi_{-1}>\xi_1$; pri zamjeni vrhova $\xi_{-1}$ i $\xi_1$ funkcija se iz
    
    $$
    \max\{0,\xi_{-1}-x\}+\max\{0,x-\xi_1\}
    $$
    
    mijenja u
    
    $$
    \max\{0,\xi_{1}-x\}+\max\{0,x-\xi_{-1}\}.
    $$
    
    Pritom se oblik funkcije ne mijenja, samo se pomiče prema dolje za $|\xi_{-1}-\xi_1|$. Stoga, da bi funkcija prije i poslije zamjene vrhova ostala ista, dovoljno je minimumu dodati $|\xi_{-1}-\xi_1|$.
    
    Vremenska složenost algoritma i dalje je $O(n\log n)$, jer se nakon svakog dodavanja elementa zamjena vrhova hrpa izvodi najviše jednom.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/safety.cpp"
    ```

Ogledni zadaci:

-   [Luogu P4272 \[CTSC2009\] Transformacija niza](https://www.luogu.com.cn/problem/P4272)
-   [Luogu P11598 \[NOISG 2018 Finals\] Safety](https://www.luogu.com.cn/problem/P11598)
-   [AtCoder Beginner Contest 217 H - Snuketoon](https://atcoder.jp/contests/abc217/tasks/abc217_h)
-   [AtCoder Regular Contest 070 E - NarrowRectangles](https://atcoder.jp/contests/arc070/tasks/arc070_c)
-   [AtCoder Regular Contest 123 D - Inc, Dec - Decomposition](https://atcoder.jp/contests/arc123/tasks/arc123_d)

## Održavanje nagiba

Postoje i problemi u kojima je zgodnije održavati nagibe. Takvi se problemi obično mogu riješiti i [greedyjem s odustajanjem](../../basic/greedy.md#rješavanje-žaljenjem) ili idejom simuliranog toka s troškom. U modelu toka s troškom najmanji je trošak često konveksna funkcija toka, što daje temelj za primjenu Slope Tricka.

### Primjer: trgovanje dionicama

???+ example "[Codeforces 865 D. Buy Low Sell High](https://codeforces.com/problemset/problem/865/D)"
    Zadan je niz cijena dionice $\{p_i\}$ kroz $n$ dana (sve pozitivne). Na početku ne posjedujemo dionice; svaki dan možemo kupiti jednu dionicu, prodati jednu dionicu ili ne trgovati. Odredite najveću dobit nakon $n$ dana.

??? note "Rješenje"
    Najprije razmotrimo naivno DP rješenje. Neka je $f_i(x)$ najveća dobit na kraju $i$-tog dana ako posjedujemo $x\ge 0$ dionica; tada je
    
    $$
    f_i(x) = \max\{f_{i-1}(x-1)-p_i,f_{i-1}(x),f_{i-1}(x+1)+p_i\}.
    $$
    
    Početno stanje je $f_0(0)=0$ i $f_0(x)=-\infty$ za sve $x\neq 0$. Odgovor na zadatak je $f_n(0)$.
    
    Od $f_{i-1}(x)$ do $f_i(x)$ potrebne su dvije transformacije:
    
    1.  Napravimo supremalnu konvoluciju $f_{i-1}(x)$ i po dijelovima linearne funkcije $\tilde h_i(x)$ (očito konkavne) koja odgovara funkciji
    
        $$
        h_i(x) = \begin{cases}p_i,&x=-1,\\0,&x=0,\\-p_i,&x=1\end{cases}
        $$
    
    2.  Budući da time funkcija dobiva konačne vrijednosti na intervalu $[-1,0)$, što proturječi zahtjevu $x\ge 0$, treba odrezati dio funkcije na $[0,+\infty)$.
    
    Pretvorene u promjene segmenata nagiba, to su sljedeća dva koraka:
    
    1.  umetanje segmenta nagiba duljine $2$ s nagibom $-p_i$;
    2.  brisanje, među segmentima konačnog nagiba, segmenta duljine $1$ s najvećim nagibom.
    
    Budući da su duljine segmenata nagiba uvijek prirodni brojevi, možemo održavati nekoliko segmenata nagiba duljine jedan, pa je dovoljno bilježiti nagib svakog segmenta. Budući da trebamo samo operacije umetanja i pristupa maksimumu, dovoljna je jedna max-hrpa. Operacija ima dva koraka:
    
    1.  dvostruko umetanje $-p_i$;
    2.  izbacivanje vrha hrpe.
    
    Treba održavati i vrijednost $f_i(0)$. Budući da je vrijednost funkcije dobivene prvim korakom u $x=-1$ jednaka $f_{i-1}(0)+p_i$, njezina je vrijednost u $x=0$ jednaka toj vrijednosti uvećanoj za vrh hrpe koji ćemo upravo izbaciti — on je nagib funkcije na intervalu $[-1,0]$. Budući da odsijecanje ne mijenja vrijednost funkcije u $x=0$, to je upravo $f_i(0)$.
    
    Usporedbom implementacije ovog algoritma s kodom iz odjeljka [Rastući niz najmanje cijene](#primjer-rastući-niz-najmanje-cijene) vidi se da je ovaj algoritam ekvivalentan računanju najmanje cijene pretvaranja niza cijena dionice u slabo padajući niz.
    
    Vremenska složenost je $O(n\log n)$.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/stock.cpp"
    ```

Ogledni zadaci:

-   [Codeforces 865 D. Buy Low Sell High](https://codeforces.com/problemset/problem/865/D)

### Primjer: prijevoz zemlje

???+ example "[\[USACO16OPEN\] Landscaping P](https://www.luogu.com.cn/problem/P2748)"
    Zadani su nizovi $\{a_i\}$ i $\{b_i\}$ duljine $n$ koji redom označavaju količinu zemlje koju $i$-ti vrt već ima i količinu koju treba imati (ni više ni manje). Kupnja jedne jedinice zemlje i stavljanje u bilo koji vrt stoji $X$, odvoz jedne jedinice zemlje iz bilo kojeg vrta stoji $Y$, a prijevoz jedne jedinice zemlje iz vrta $i$ u vrt $j$ stoji $Z|i-j|$. Odredite najmanji trošak zadovoljavanja potreba svih vrtova. ($a_i,b_i\le 10$)

??? note "Rješenje"
    Razmotrimo naivno DP rješenje. Neka je $f_i(x)$ najmanji trošak zadovoljavanja potreba prvih $i$ vrtova uz neto višak od $x$ jedinica zemlje koje se prevoze u sljedeće vrtove. Ako je $x<0$, to znači neto manjak od $|x|$ jedinica zemlje koje treba dovesti iz sljedećih vrtova. Tada se jednadžba prijelaza stanja može zapisati kao
    
    $$
    f_i(x) = \min_{y\in\mathbf R} f_{i-1}(y) + |y|Z + h((x-y)+(b_i-a_i)).
    $$
    
    Ovdje funkcija $h(\delta)$ označava trošak kad je neto kupljena količina zemlje za trenutni vrt jednaka $\delta$, tj.
    
    $$
    h(\delta) = \max\{0,\delta\}X + \max\{0,-\delta\}Y = \max\{\delta X,-\delta Y\}.
    $$
    
    Ona je očito konveksna. Značenje ove jednadžbe prijelaza stanja je sljedeće:
    
    -   kad je neto višak zemlje prethodnih $i-1$ vrtova jednak $y$, najmanji trošak je $f_{i-1}(y)$;
    -   trošak prijevoza neto viška (manjka) zemlje između $i$ i $i-1$ je $|y|Z$;
    -   najmanji trošak da se kupnjom i prodajom količina zemlje u $i$-tom vrtu prilagodi s $a_i$ na $b_i$, a neto višak zemlje s $y$ na $x$, iznosi $h((x-y)+(b_i-a_i))$.
    
    Početno stanje je $f_0(0)=0$ i $f_0(x)=+\infty$ za sve $x\neq 0$. Odgovor na zadatak je $f_n(0)$.
    
    Transformacija funkcije $f_{i-1}(x)$ u $f_i(x)$ može se podijeliti u tri koraka:
    
    1.  Najprije dodamo $|x|Z$ i dobijemo $f_{i-1}(x)+|x|Z$;
    2.  Zatim napravimo infimalnu konvoluciju s $h(x)$ i dobijemo $\min_{y\in\mathbf R}f_{i-1}(y)+|y|Z+h(x-y)$;
    3.  Na kraju funkciju pomaknemo ulijevo za $(b_i-a_i)$ jedinica.
    
    Pretvoreno u operacije nad segmentima nagiba, također u tri koraka:
    
    1.  svim segmentima nagiba lijevo od ishodišta dodamo $-Z$, a svim segmentima nagiba desno od ishodišta dodamo $Z$;
    2.  sve segmente nagiba manjeg od $-Y$ zamijenimo s $-Y$, a sve segmente nagiba većeg od $X$ zamijenimo s $X$;
    3.  sve segmente nagiba pomaknemo ulijevo za $(b_i-a_i)$ jedinica.
    
    U izvornom su zadatku $a_i$ i $b_i$ vrlo mali, pa je dovoljno održavati nekoliko segmenata nagiba duljine $1$. Iako segmenata nagiba ima beskonačno mnogo, postoje gornja granica $X$ i donja granica $-Y$, a broj segmenata nagiba strogo između njih nije velik. Budući da nema operacija umetanja, segmente nagiba s obje strane ishodišta možemo održavati dvama stogovima, a operacije dodavanja na intervalu i minimuma/maksimuma na intervalu izvodimo lijenim oznakama. Gornja tri koraka redom odgovaraju:
    
    1.  postavljanju lijene oznake na lijevi i desni stog: lijevom dodajemo $-Z$, desnom $Z$;
    2.  pri svakom izbacivanju elementa sa stoga uzimamo maksimum s $-Y$ i minimum s $X$. Ako je lijevi stog prazan, izbacujemo $-Y$. Ako je desni stog prazan, izbacujemo $X$;
    3.  izbacivanju $(b_i-a_i)$ elemenata s vrha lijevog stoga i njihovu umetanju u desni stog; naravno, za $b_i-a_i<0$ obrnuto.
    
    Pri premještanju vrhova stogova ažuriramo odgovor: pri pomaku ulijevo oduzimamo trenutni nagib, a pri pomaku udesno dodajemo trenutni nagib.
    
    Složenost algoritma je $O(n\max\{a_i,b_i\})$.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/landscaping.cpp"
    ```

Ogledni zadaci:

-   [Luogu P2748 \[USACO16OPEN\] Landscaping P](https://www.luogu.com.cn/problem/P2748)
-   [Kyoto University PC 2016 H - WAAAAAAAAAAAAALL](https://atcoder.jp/contests/kupc2016/tasks/kupc2016_h)
-   [JAG Practice Contest 2017 J - Farm Village](https://atcoder.jp/contests/jag2017autumn/tasks/jag2017autumn_j)

## Zadaci

Na kraju ovog teksta navodimo nekoliko zadataka s raznih algoritamskih natjecanja koji se mogu riješiti Slope Trickom, za vježbu.

-   [Luogu P3642 \[APIO2016\] Vatromet](https://www.luogu.com.cn/problem/P3642)
-   [Luogu P9962 \[THUPC 2024 kvalifikacije\] Jedno stablo](https://www.luogu.com.cn/problem/P9962)
-   [Luogu P11317 \[RMI 2021\] Paths](https://www.luogu.com.cn/problem/P11317)
-   [AtCoder Beginner Contest 383 G - Bar Cover](https://atcoder.jp/contests/abc383/tasks/abc383_g)
-   [Codeforces 280 D. k-Maximum Subsequence Sum](https://codeforces.com/problemset/problem/280/D)
-   [Codeforces 280 E. Sequence Transformation](https://codeforces.com/problemset/problem/280/E)
-   [Codeforces 802 O. April Fools' Problem (hard)](https://codeforces.com/contest/802/problem/O)
-   [Codeforces 1209 H. Moving Walkways](https://codeforces.com/contest/1209/problem/H)
-   [Codeforces 1229 F. Mateusz and Escape Room](https://codeforces.com/contest/1229/problem/F)
-   [Codeforces 1534 G. A New Beginning](https://codeforces.com/problemset/problem/1534/G)
-   [Codeforces 1787 H. Codeforces Scoreboard](https://codeforces.com/problemset/problem/1787/H)
-   [2019 Summer Petrozavodsk Camp H. Honorable Mention](https://codeforces.com/gym/102331/problem/H)
-   [2018 ACM-ICPC World Finals C. Conquer The World](https://codeforces.com/gym/102482/problem/C)
-   [300iq Contest 3 F. Farm of Monsters](https://codeforces.com/gym/102538/problem/F)

## Literatura i bilješke

-   [\[Tutorial\] Slope Trick - zscoder](https://codeforces.com/blog/entry/47821)
-   [Slope trick explained - Kuroni](https://codeforces.com/blog/entry/77298)
-   [Slope Trick - USACO Guide](https://usaco.guide/adv/slope-trick?lang=cpp)
-   [\[Tutorial\] Intuition on Slope Trick - maomao90](https://codeforces.com/blog/entry/103222)

[^convex-def]: Različiti udžbenici mogu različito nazivati konveksne funkcije.

[^inf-conv]: Često se naziva i $\min$-konvolucija, $\inf$-konvolucija ili $(\min,+)$-konvolucija.
