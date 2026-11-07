---
title: Vektorski prostor
---

Vektorski (linearni) prostor poopćenje je $d$-dimenzionalnog euklidskog prostora ($0\leq d\leq 3$) i sličnih struktura; odnos među pripadnim pojmovima prikazan je u odjeljku [Odnos euklidskog i vektorskog prostora](#odnos-euklidskog-i-vektorskog-prostora).

Predznanje: Abelova grupa, polje.

Jednostavno rečeno, skup koji je zatvoren s obzirom na neku operaciju te zadovoljava asocijativnost, ima neutralni element i inverzne elemente čini grupu. Ako k tome vrijedi i komutativnost, čini Abelovu grupu.

Ako je skup zatvoren s obzirom na četiri osnovne računske operacije, čini polje. Pripadne definicije potražite u [Osnovni pojmovi apstraktne algebre](../algebra/basic.md#域).

## Definicija

Vektorski prostor (linearni prostor) osnovni je pojam i važan predmet proučavanja linearne algebre. Vektorski prostor algebarska je struktura tipa modula sastavljena od skupa vektora $V$, polja $\Bbb{P}$, operacije zbrajanja $+$ i množenja skalarom.

Konkretno, neka je $(V,+)$ Abelova grupa, a $\Bbb{P}$ polje.

Definiramo algebarsku operaciju između brojeva iz $\Bbb{P}$ i elemenata iz $V$, koju nazivamo **množenje skalarom**: $\cdot:\Bbb{P}\times V\mapsto V$, pišemo $p\cdot v$ ili $pv$, pri čemu je $p$ u polju $\Bbb{P}$, a $v$ u Abelovoj grupi $V$. Zahtijevamo da ta operacija bude zatvorena, tj. da rezultat uvijek ima smisla i da se također nalazi u grupi $V$.

Osim toga, moraju vrijediti sljedeći uvjeti:

1.  **Distributivnost množenja skalarom prema zbrajanju vektora**: za $\mathbf u,\mathbf v\in V,a\in \Bbb{P}$ vrijedi $a(\mathbf u+\mathbf v)=a\mathbf u+a\mathbf v$
2.  **Distributivnost množenja skalarom prema zbrajanju skalara**: za $a,b\in \Bbb{P},\mathbf u\in V$ vrijedi $(a+b)\mathbf u=a\mathbf u+b\mathbf u$
3.  **Asocijativnost množenja skalarom (usklađenost s množenjem u polju)**: za $a,b\in \Bbb{P},\mathbf u\in V$ vrijedi $a(b\mathbf u)=(ab)\mathbf u$
4.  **Neutralni element množenja skalarom**: neka je $1\in \Bbb{P}$ neutralni element množenja u $\Bbb{P}$; tada za $u\in V$ vrijedi $1\mathbf u=\mathbf u$

Tada kažemo da algebarska struktura $(V,+,\cdot,\mathbb{P})$, odnosno $V$ s obzirom na $+,\cdot$, čini **vektorski prostor** nad $\Bbb{P}$; $\Bbb{P}$ je **polje skalara** (osnovno polje) tog vektorskog prostora, elementi skupa $V$ nazivaju se **vektori**, a elementi polja $\Bbb{P}$ **skalari**. Kad je polje $\Bbb{P}$ polje realnih brojeva, govorimo o realnom vektorskom prostoru. Kad je polje $\Bbb{P}$ polje kompleksnih brojeva, govorimo o kompleksnom vektorskom prostoru.

Bez obzira na to radi li se o nizu brojeva, strelicama ili bilo čemu drugom, sve što zadovoljava gornje aksiome može se smatrati vektorom, pa se stoga može proučavati pomoću teorije linearne algebre.

Neutralni element aditivne grupe naziva se nul-vektor i označava $\mathbf 0$ ili $\mathbf\theta$.

Zbrajanje i oduzimanje vektora iz izvorne Abelove grupe te novodefinirano množenje skalarom zajednički se nazivaju **linearne operacije**.

???+ note "Napomena"
    Radi jednostavnosti zapisa u nastavku teksta:
    
    1.  elementi skupa $V$ ne pišu se podebljano;
    2.  algebarsku strukturu $(V,+,\cdot,\mathbb{P})$ koja zadovoljava definiciju vektorskog prostora također nazivamo vektorskim prostorom.
    
    Vodite računa o razlici.

### Intuitivno shvaćanje

Ne sasvim strogo rečeno, množenje skalarom odgovara „**skaliranju**”, elementi polja skalara $\Bbb{P}$ predstavljaju „**omjer**” skaliranja, a zbrajanje vektora odgovara „**slaganju**” (superpoziciji). Istodobno, elementi polja $\Bbb{P}$ predstavljaju i skup vrijednosti koje mogu poprimiti „**koordinate**” vektora.

Uvjeti 1–4 opisuju vezu između „skaliranja” i „slaganja”. Možete ih razumjeti pomoću strelica u dvodimenzionalnoj ravnini.

### Jednostavna svojstva

???+ note "Napomena"
    Sljedeća se svojstva mogu naći u teoriji grupa i srodnim područjima.

Za vektorski prostor $(V,+,\cdot,\Bbb{P})$ vrijedi:

1.  $\theta$ je jedinstven
2.  $\forall\alpha\in V$, $-\alpha$ je jedinstven
3.  $\exists 0\in\mathbb{P}$, $\forall\alpha\in V$ vrijedi $0\alpha=\theta$
4.  $\forall k\in\mathbb{P}$ vrijedi $k\theta=\theta$
5.  $(-1)\alpha=-\alpha,~\forall\alpha\in V$
6.  Nema djelitelja nule: $\forall\alpha\in V,k\in\mathbb{P}$ vrijedi $k\alpha=\theta\implies k=0\lor\alpha=\theta$
7.  Zakon kraćenja za zbrajanje: $\forall\alpha,\beta,\gamma\in V$ vrijedi $\alpha+\beta=\alpha+\gamma\implies\beta=\gamma$

    > Zapravo, zakon kraćenja za zbrajanje svojstvo je Abelove grupe.

### Primjeri

1.  $\Bbb{P}^n$ s obzirom na zbrajanje i množenje nad poljem $\Bbb{P}$ čini vektorski prostor nad $\Bbb{P}$. Na primjer, $\Bbb{P}$ može biti $\Bbb{R}$, $\Bbb{C}$, $\Bbb{N}_p$ ($p$ prost) itd.
2.  Matrice reda $n\times m$ nad poljem $\Bbb{P}$, $\Bbb{P}^{n\times m}$, s obzirom na zbrajanje matrica i množenje skalarom čine vektorski prostor nad $\Bbb{P}$.
3.  Prsten polinoma u jednoj varijabli $\Bbb{P}[x]$ nad poljem $\Bbb{P}$ s obzirom na zbrajanje polinoma i množenje skalarom čini vektorski prostor nad $\Bbb{P}$.
4.  Skup svih neprekidnih funkcija na segmentu $[a,b]$ (označava se $C[a,b]$) s obzirom na „zbrajanje funkcija” i „množenje neprekidne funkcije vrijednošću” čini vektorski prostor nad poljem vrijednosti.

## Srodni pojmovi

### Linearna zavisnost i linearna nezavisnost

Za vektorski prostor $(V,+,\cdot,\Bbb{P})$:

1.  $a_1,a_2,\dots,a_n\in V$ nazivamo **skupom vektora** (sustavom vektora) u $V$.
2.  Za $k_1,k_2,\dots,k_n\in\Bbb{P}$, $\sum_{i=1}^nk_ia_i$ nazivamo **linearnom kombinacijom** skupa vektora $a_1,a_2,\dots,a_n$.
3.  Ako se vektor $\beta\in V$ može prikazati kao linearna kombinacija skupa vektora $a_1,a_2,\dots,a_n$, kažemo da se $\beta$ može **linearno izraziti** pomoću skupa vektora $a_1,a_2,\dots,a_n$.
4.  Za $k_1,k_2,\dots,k_n\in\Bbb{P}$, ako skup vektora $a_1,a_2,\dots,a_n$ zadovoljava $\sum_{i=1}^nk_ia_i=\theta\iff k_i=0, i=1,2,\dots,n$, kažemo da je skup vektora $a_1,a_2,\dots,a_n$ **linearno nezavisan**; u suprotnom kažemo da je skup vektora $a_1,a_2,\dots,a_n$ **linearno zavisan**.

Dogovorno, nul-vektor je linearno zavisan sa svakim vektorom.

Izraz za linearni prikaz ili linearnu zavisnost može se zapisati u obliku množenja matrica:

$$
\beta=k_1a_1+k_2a_2+\cdots+k_ra_r=(a_1,a_2,\cdots,a_r)\begin{pmatrix} k_1 \\ k_2 \\ \vdots \\ k_r \end{pmatrix}
$$

Po dogovoru, vektori $a$ pišu se redom jedan pokraj drugoga s lijeve strane, a skalari $k$ redom okomito s desne strane, tvoreći „vektor-stupac”.

Napomena: „vektor-stupac” sastavljen od skalara ovdje je samo prikladna formalna oznaka; on nije u prostoru $V$ i bitno se razlikuje od vektora s lijeve strane. Ako su vektori s lijeve strane slučajno vektori-stupci, njihovim se slaganjem jedan pokraj drugoga formalno može dobiti „matrica”, a gornji je umnožak upravo uobičajeni oblik „množenja matrice vektorom-stupcem s desne strane”.

U nastavku se pokazuje da je ovaj linearni prikaz ekvivalentan i tvrdnji da vektor $\beta$ leži u slici matrice $(a_1,a_2\cdots,a_r)$.

Prema definiciji u nastavku, nul-vektor uvijek leži u slici. Gledano s gledišta linearnih transformacija, linearna zavisnost ekvivalentna je tome da se nakon transformacije više vektora preslikava u nul-vektor, a linearna nezavisnost tome da se samo sam nul-vektor preslikava u nul-vektor.

#### Svojstva

Za vektorski prostor $(V,+,\cdot,\Bbb{P})$ vrijedi:

1.  Ako je dio skupa vektora linearno zavisan, onda je cijeli skup vektora linearno zavisan. Ako je skup vektora linearno nezavisan, onda je svaki njegov neprazan podskup linearno nezavisan. Kratko: **„velik nezavisan – mali nezavisan”; „mali zavisan – velik zavisan”**.
2.  Skup vektora koji sadrži $\theta$ linearno je zavisan.
3.  Skup vektora linearno je zavisan ako i samo ako se neki od njegovih vektora može linearno izraziti pomoću preostalih vektora.
4.  Ako se vektor $\beta$ može linearno izraziti pomoću skupa vektora $a_1,a_2,\dots,a_n$, onda je taj prikaz jedinstven ako i samo ako je skup vektora $a_1,a_2,\dots,a_n$ linearno nezavisan.
5.  Ako je skup vektora $a_1,a_2,\dots,a_n$ linearno nezavisan, onda se vektor $\beta$ može linearno izraziti pomoću skupa vektora $a_1,a_2,\dots,a_n$ ako i samo ako je skup vektora $a_1,a_2,\dots,a_n,\beta$ linearno zavisan.

### Maksimalan linearno nezavisan podskup, rang

Linearnu zavisnost možemo shvatiti kao „suvišnost”: ona znači da se neki vektori u skupu mogu izraziti pomoću drugih pa se mogu ukloniti. Nakon što ih uklonimo, preostaje maksimalan linearno nezavisan podskup.

Za vektorski prostor $(V,+,\cdot,\Bbb{P})$:

1.  Za skup vektora $b_1,b_2,\dots,b_m$ neka je $\{a_1,a_2,\dots,a_n\}\subseteq\{b_1,b_2,\dots,b_m\}$ takav da vrijedi:

    -   skup vektora $a_1,a_2,\dots,a_n$ linearno je nezavisan;
    -   $\forall\beta\in\{b_1,b_2,\dots,b_m\}\setminus\{a_1,a_2,\dots,a_n\}$, skup vektora $a_1,a_2,\dots,a_n,\beta$ linearno je zavisan.

    Tada skup vektora $a_1,a_2,\dots,a_n$ nazivamo **maksimalnim linearno nezavisnim podskupom** skupa vektora $b_1,b_2,\dots,b_m$. Analogno se definira maksimalan linearno nezavisan podskup vektorskog prostora $V$.

    Dogovorno, maksimalan linearno nezavisan podskup skupa vektora $\theta,\theta,\dots,\theta$ prazan je skup, pa skup vektora koji odgovara matrici čiji su svi elementi $0$ nema maksimalan linearno nezavisan podskup.

    Način uklanjanja vektora iz skupa nije jedinstven, pa ni maksimalan linearno nezavisan podskup nije jedinstven. Uobičajeno je uklanjati redom slijeva nadesno.

    Zgodna je slučajnost da su vektori koji preostanu pri uklanjanju redom upravo oni koji, u gledištu „po retcima”, odgovaraju stupcima u kojima se nalaze elementi $1$ u reduciranom ešelonskom obliku matrice dobivenom Gaussovom eliminacijom.

    Veličina maksimalnog linearno nezavisnog podskupa skupa vektora $b_1,b_2,\dots,b_m$ naziva se **rang** tog skupa vektora i označava $\operatorname{rank}\{b_1,b_2,\dots,b_m\}$; dogovorno je $\operatorname{rank}\{\theta,\theta,\dots,\theta\}=0$.

    Dakle, definicija ranga skupa vektora potpuno se podudara s definicijom ranga matrice.

2.  Ako se pomoću skupa vektora $a_1,a_2,\dots,a_n$ mogu linearno izraziti svi vektori skupa $b_1,b_2,\dots,b_m$, kažemo da se skup vektora $b_1,b_2,\dots,b_m$ može linearno izraziti pomoću skupa vektora $a_1,a_2,\dots,a_n$.

3.  Ako se skup vektora $a_1,a_2,\dots,a_n$ može linearno izraziti pomoću skupa vektora $b_1,b_2,\dots,b_m$ i skup vektora $b_1,b_2,\dots,b_m$ može se linearno izraziti pomoću skupa vektora $a_1,a_2,\dots,a_n$, kažemo da su ta dva skupa vektora **ekvivalentna** i pišemo $\{a_1,a_2,\dots,a_n\}\cong\{b_1,b_2,\dots,b_m\}$.

    **Ekvivalentnost** skupova vektora znači da razapinju isti prostor. Skupovi vektora koji razapinju isti prostor međusobno su ekvivalentni, a skupovi vektora koji razapinju različite prostore nisu ekvivalentni.

    Ekvivalentnost skupova vektora jači je uvjet od ekvivalentnosti matrica: ne zahtijeva se samo jednak rang, nego i potpuno isti prostor. Stoga, ako dvije matrice spojimo **vodoravno** jednu uz drugu, rang se ne smije promijeniti.

    Ekvivalentnost matrica zahtijeva samo jednak rang, pa ekvivalentnost matrica znači da se od prve matrice ili prostora regularnom (invertibilnom) transformacijom može doći do druge matrice ili prostora.

#### Svojstva

Za vektorski prostor $(V,+,\cdot,\Bbb{P})$ vrijedi:

1.  Neka se skup vektora $a_1,a_2,\dots,a_n$ može linearno izraziti pomoću skupa vektora $b_1,b_2,\dots,b_m$.
    -   Ako je $n>m$, skup vektora $a_1,a_2,\dots,a_n$ linearno je zavisan.
    -   Ako je skup vektora $a_1,a_2,\dots,a_n$ linearno nezavisan, onda je $n\leq m$.

2.  Ekvivalentni linearno nezavisni skupovi vektora jednake su veličine.

    Svi maksimalni linearno nezavisni podskupovi nekog skupa vektora jednake su veličine.

3.  Skup vektora linearno je nezavisan ako i samo ako je njegov rang jednak njegovoj veličini.

4.  Ako se skup vektora $a_1,a_2,\dots,a_n$ može linearno izraziti pomoću skupa vektora $b_1,b_2,\dots,b_m$, onda je $\operatorname{rank}\{a_1,a_2,\dots,a_n\}\leq\operatorname{rank}\{b_1,b_2,\dots,b_m\}$.

5.  Ekvivalentni skupovi vektora imaju jednak rang.

### Linearna ljuska

Za vektorski prostor $(V,+,\cdot,\Bbb{P})$, skup $\left\{v=\sum_{i=1}^nk_ia_i:a_i\in V,k_i\in\Bbb{P},i=1,2,\dots,n\right\}$ također čini vektorski prostor, koji nazivamo vektorskim prostorom **razapetim** skupom vektora $a_1,a_2,\dots,a_n$ (ili **linearnom ljuskom**, engl. span) i označavamo $\operatorname{span}\{a_1,a_2,\dots,a_n\}$.

Ovih $n$ vektora $a$ ne mora biti linearno nezavisno.

### Potprostor

Za vektorski prostor $(V,+,\cdot,\Bbb{P})$, ako algebarska struktura $(V_1,+,\cdot,\Bbb{P})$ zadovoljava:

1.  $\varnothing\ne V_1$
2.  $V_1\subseteq V$
3.  $V_1$ s obzirom na $+,\cdot$ čini vektorski prostor nad $\mathbb{P}$

tada $V_1$ nazivamo vektorskim potprostorom (kraće: potprostorom) prostora $V$ i pišemo $V_1\leq V$.

Svaki prostor $V$ ima dva **trivijalna potprostora**: sam $V$ i nul-potprostor. Nul-potprostor sadrži samo nul-vektor i ne sadrži linearno nezavisne vektore.

Ako se u 2. uvjetu $\subseteq$ zamijeni sa $\subset$, tada $V_1$ nazivamo pravim potprostorom prostora $V$ i pišemo $V_1<V$.

Nije teško dokazati: neprazan podskup $V_1$ vektorskog prostora $V$ njegov je potprostor ako i samo ako su linearne operacije zatvorene na $V_1$, tj.:

1.  $\forall u,v\in V_1$, $u+v\in V_1$
2.  $\forall v\in V_1$, $\forall k\in \Bbb{P}$, $kv\in V_1$

### Presjek, suma i direktna suma, direktni produkt

Za vektorske prostore $(V_1,+,\cdot,\Bbb{P})$ i $(V_2,+,\cdot,\Bbb{P})$:

1.  Lako se provjerava da su zbrajanje i množenje skalarom zatvoreni na $V_1\cap V_2$, pa $V_1\cap V_2$ nazivamo **presjekom** vektorskih prostora $V_1$ i $V_2$.

    Analogno se definira presjek više vektorskih prostora $\bigcap_{i=1}^m V_i$.

2.  Ako vektorski prostor $V$ zadovoljava $V=\{u+v|u\in V_1,v\in V_2\}$, tada $V$ nazivamo **sumom** vektorskih prostora $V_1$ i $V_2$ i pišemo $V=V_1+V_2$.

    Može se provjeriti da je $V_1+V_2$ najmanji potprostor koji sadrži $V_1\cup V_2$.

    Analogno se definira suma više vektorskih prostora $\sum_{i=1}^m V_i$.

3.  Neka je $V=V_1+V_2$. Ako za svaki element $v$ vektorskog prostora $V$ postoji samo jedan par vektora $v_1,v_2$ takav da je $v=v_1+v_2$, tada $V$ nazivamo **direktnom sumom** (engl. direct sum) vektorskih prostora $V_1$ i $V_2$ i pišemo $V_1\oplus V_2$.

    Analogno se definira direktna suma više vektorskih prostora $\bigoplus_{i=1}^m V_i$.

4.  **Direktni produkt** $V_1\times V_2$ prostora $V_1$ i $V_2$ definira se kao njihov Kartezijev produkt koji s obzirom na sljedeće zbrajanje i množenje skalarom čini vektorski prostor nad $\Bbb{P}$:

    1.  $+:(V_1\times V_2)\times(V_1\times V_2)\mapsto V_1\times V_2; ((u_1,v_1),(u_2,v_2))\to (u_1+u_2,v_1+v_2)$
    2.  $\cdot:\Bbb{P}\times(V_1\times V_2)\mapsto V_1\times V_2; (k,(u,v))\to (ku,kv)$

    Analogno se definira direktni produkt više vektorskih prostora $\prod_{i=1}^m V_i$.

#### Primjeri

Za vektorski prostor $V=\Bbb{R}^3$ neka su zadani vektorski prostori:

-   $V_1:=\{(x,0,0)|x\in\Bbb{R}\}$
-   $V_2:=\{(x,y,0)|x,y\in\Bbb{R}\}$
-   $V_3:=\{(0,y,z)|y,z\in\Bbb{R}\}$
-   $V_4:=\{(x,0,z)|x,z\in\Bbb{R}\}$

Tada vrijedi:

1.  $V_1<V_2<V$, $V_3<V$
2.  $V_2=V_1+V_2$
3.  $V=V_1\oplus V_3=V_2+V_3$
4.  $V_2+V_3\leq V$

#### Svojstva

1.  Neka su $V_1,V_2,V_3$ vektorski prostori nad $\Bbb{P}$. Kao i za presjek skupova, za presjek vektorskih prostora vrijede sljedeća pravila:
    1.  komutativnost: $V_1\cap V_2=V_2\cap V_1$
    2.  asocijativnost: $V_1\cap(V_2\cap V_3)=(V_1\cap V_2)\cap V_3$
2.  Neka su $V_1,V_2,V_3$ vektorski prostori nad $\Bbb{P}$. Slično kao za uniju skupova, za sumu vektorskih prostora vrijede sljedeća pravila:
    1.  komutativnost: $V_1+V_2=V_2+V_1$
    2.  asocijativnost: $V_1+(V_2+V_3)=(V_1+V_2)+V_3$
3.  Neka su $V_1,V_2,V_3$ vektorski prostori nad $\Bbb{P}$. Presjek i suma vektorskih prostora u sljedećem su odnosu:
    1.  $V_1\cap (V_2+V_3)\supseteq (V_1\cap V_2)+(V_1\cap V_3)$
    2.  $V_1+(V_2\cap V_3)\subseteq (V_1+V_2)\cap (V_1+V_3)$
4.  $\operatorname{span}\{a_1,a_2,\dots,a_n\}+\operatorname{span}\{b_1,b_2,\dots,b_m\}=\operatorname{span}\{a_1,a_2,\dots,a_n,b_1,b_2,\dots,b_m\}$
5.  Neka su $V_1,V_2$ vektorski prostori nad $\Bbb{P}$. Tada su sljedeće tvrdnje ekvivalentne:

    1.  $V_1+V_2=V_1\oplus V_2$

    2.  $\exists \beta\in V_1+V_2$ koji se na jedinstven način rastavlja na sumu vektora iz $V_1$ i $V_2$ („za svaki” $\to$ „postoji”)

    3.  $\theta$ se na jedinstven način rastavlja na sumu vektora iz $V_1$ i $V_2$

    4.  $V_1\cap V_2=\{\theta\}$

    ???+ note "Dokaz"
        $1\implies 2$: slijedi izravno iz definicije.
        
        $2 \implies 3$:
        
        Neka je $\beta=\beta_1+\beta_2$, gdje je $\beta_1\in V_1, \beta_2\in V_2$. Ako je $\theta=\alpha_1+\alpha_2$, $\theta\ne\alpha_1\in V_1,\alpha_2\in V_2$, onda je $\beta=\beta+\theta=(\beta_1+\alpha_1)+(\beta_2+\alpha_2)$.
        
        No $\beta_1\ne\beta_1+\alpha_1$, što je u suprotnosti s pretpostavkom.
        
        $3 \implies 4$:
        
        Uzmimo vektor $\alpha$ različit od nule koji je i u $V_1$ i u $V_2$. Tada je $\theta=\alpha+(-\alpha)=(-\alpha)+\alpha$, što je u suprotnosti s pretpostavkom.
        
        $4 \implies 1$:
        
        Ako $V_1+V_2$ nije direktna suma, postoji $\beta\in V_1+V_2$ takav da je $\beta=\beta_1+\beta_2=\gamma_1+\gamma_2$, gdje je $\beta_1,\gamma_1\in V_1,\beta_2,\gamma_2\in V_2$ i $\beta_1,\beta_2,\gamma_1,\gamma_2$ međusobno su različiti.
        
        Tada je $\theta\ne\beta_1-\gamma_1=\gamma_2-\beta_2\in V_1\cap V_2$, što je u suprotnosti s pretpostavkom.

### Izomorfizam

Neka su $V,V'$ vektorski prostori nad poljem $\Bbb{P}$. Ako postoji bijekcija $\sigma:V\mapsto V'$ koja čuva zbrajanje i množenje skalarom, tj. $\forall u,v\in V$, $\forall k\in\Bbb{P}$ vrijedi:

1.  $\sigma(u+v)=\sigma(u)+\sigma(v)$
2.  $\sigma(ku)=k\sigma(u)$

tada $\sigma$ nazivamo **izomorfizmom** prostora $V$ na $V'$, a za $V$ i $V'$ kažemo da su **izomorfni** i pišemo $V\cong V'$.

???+ note "Napomena"
    Ako je $\sigma$ injekcija, može se definirati **monomorfizam**; ako je $\sigma$ surjekcija, može se definirati **epimorfizam**.

#### Svojstva

1.  Dva vektorska prostora nad poljem $\Bbb{P}$ izomorfna su ako i samo ako su im dimenzije jednake. (Definiciju dimenzije vidi u [Linearna baza](./basis.md).)
2.  (Posljedica 1.) $n$-dimenzionalni vektorski prostor nad poljem $\Bbb{P}$ izomorfan je vektorskom prostoru $\Bbb{P}^n$.

    ???+ note "Napomena"
        Ovo svojstvo pokazuje da u osnovi koordinate i vektore možemo poistovjetiti.

## Odnos euklidskog i vektorskog prostora

Na primjeru nama najpoznatijeg trodimenzionalnog euklidskog prostora, nekim njegovim pojmovima u vektorskom prostoru odgovaraju pojmovi iz sljedeće tablice:

| Trodimenzionalni euklidski prostor | Vektorski prostor |
| -------- | ----------------- |
| vektor | vektor |
| okomitost | ortogonalnost (tj. skalarni produkt jednak $0$) |
| tri vektora kolinearna/komplanarna | $k$ vektora linearno zavisno |
| tri vektora nekomplanarna | $k$ vektora linearno nezavisno |
| bazni vektori | [linearna baza](./basis.md) |
| dimenzija prostora | dimenzija prostora |

## Primjene

Od ovog odjeljka nadalje uglavnom se bavimo gledištem „po stupcima” na sustave linearnih jednadžbi.

Matrica $A$ i sama se sastoji od vektora-stupaca. Promatramo $A$ kao skup vektora-stupaca, a $x$ su nepoznati koeficijenti; pitamo se može li se taj skup vektora-stupaca iz $A$, uparen s nepoznanicama, složiti u vektor-stupac $b$. Vektor-stupac $x$ ovdje je potpuno nepoznat.

Jednadžba $Ax=b$ koju proučavamo tada se može zapisati kao:

$$
\alpha_1 x_1 +\alpha_2 x_2 +\cdots+\alpha_n x_n=b 
$$

Dakle, u množenju matrica, matrica $A$ s lijeve strane može se promatrati kao skup vektora, tj. skup vektora-stupaca. Taj skup vektora-stupaca, kao baza, razapinje prostor, a pitanje je leži li vektor-stupac $b$ u tom prostoru.

### Rješenja sustava linearnih jednadžbi gledana po stupcima

Rang je broj vektora u maksimalnom linearno nezavisnom podskupu i predstavlja „ograničenja”. Preostali vektori tada daju rješenju stupnjeve slobode, tj. dopuštaju dodavanje suvišnih vektora u drugim smjerovima.

Ako s $n$ označimo broj stupaca matrice $A$, tj. broj vektora-stupaca koje sadrži, a s $r(A)$ rang matrice A, onda je broj stupnjeva slobode $S$:

$$
S=n-r(A)
$$

Sva rješenja sustava također čine skup vektora, a broj stupnjeva slobode $S$ upravo je rang skupa vektora rješenja sustava $Ax=0$, tj. dimenzija jezgre o kojoj je riječ u nastavku.

### Ekvivalentnost sustava jednadžbi

Zajedničko rješenje dvaju sustava jednadžbi definira se kao presjek njihovih skupova rješenja.

Sustavi jednadžbi **ekvivalentni** su (imaju ista rješenja) ako su im skupovi rješenja jednaki. Sustavi s jednakim skupovima rješenja ekvivalentni su, a sustavi s različitim skupovima rješenja nisu ekvivalentni.

Ekvivalentnost sustava jednadžbi također je jači uvjet od ekvivalentnosti matrica: ne zahtijeva se samo jednak rang, nego i da se rang ne promijeni kad se dvije matrice spoje **okomito** jedna ispod druge.

Usporedimo to s ekvivalentnošću skupova vektora: ekvivalentnost skupova vektora zahtijeva da se rang ne promijeni pri vodoravnom spajanju matrica. Stoga vrijedi sljedeći odnos:

Iz ekvivalentnosti matrica ne slijedi nužno ekvivalentnost pripadnih skupova vektora niti ekvivalentnost sustava jednadžbi, ali iz ekvivalentnosti skupova vektora ili ekvivalentnosti sustava jednadžbi nužno slijedi ekvivalentnost pripadnih matrica (jednak rang).

Ako su skupovi vektora koji odgovaraju matricama ekvivalentni, onda su nakon transponiranja matrica pripadni sustavi jednadžbi ekvivalentni, i obratno.

### Jezgra i slika matrice

Jezgra i slika ovdje se opisuju s gledišta vektorskih prostora.

Za matricu $A$ neka je $W$ skup svih rješenja $x$ jednadžbe $Ax=0$. Tada je $W$ vektorski prostor, a polje skalara prostora $W$ jednako je polju kojemu pripadaju elementi matrice $A$.

Takav $W$ nazivamo **jezgrom** (nul-prostorom) matrice $A$ i označavamo $N(A)$.

Jezgra $N(A)$ matrice $A$ upravo je **prostor rješenja** jednadžbe $Ax=0$. Prema definiciji baze u nastavku, **fundamentalni sustav rješenja** te jednadžbe upravo je baza jezgre.

Ako je matrica $A$ invertibilna (regularna), jezgra $N(A)$ matrice $A$ sadrži samo nul-vektor.

Za matricu $A$ čijih je $n$ stupaca vektori $\alpha$, prostor razapet tih $n$ vektora-stupaca $\alpha$ nazivamo **slikom** matrice $A$, ili **prostorom stupaca**, i označavamo:

$$
R(A)=\operatorname{span}\{\alpha_1,\alpha_2,\cdots,\alpha_n\}
$$

Prema definiciji dimenzije u nastavku, dimenzija slike jednaka je rangu matrice $A$.

Po definiciji, svaki element $y$ slike $R(A)$ ima odgovarajući prikaz:

$$
y=k_1\alpha_1+k_2\alpha_2+\cdots+k_n\alpha_n=(\alpha_1,\alpha_2,\cdots,\alpha_n)\begin{pmatrix}k_1\\k_2\\\vdots\\k_n\end{pmatrix}=A\begin{pmatrix}k_1\\k_2\\\vdots\\k_n\end{pmatrix}
$$

Stoga je slika $R(A)$ upravo **skup vrijednosti** izraza $Ax$ za sve vektore $x$.

Analogno se definira **prostor redaka** matrice $A$, tj. skup vrijednosti transponirane matrice od $A$, $R(A^T)$.

Budući da je rang po retcima jednak rangu po stupcima, dimenzija prostora redaka također je jednaka rangu matrice, pa transponiranje mijenja sliku, ali ne mijenja njezinu dimenziju.

Ovdje možemo uspostaviti vezu s prethodnim tekstom:

Ekvivalentnost skupova vektora ekvivalentna je jednakosti slika $R(A)$ pripadnih matrica.

Ekvivalentnost sustava jednadžbi ekvivalentna je jednakosti prostora redaka $R(A^T)$ pripadnih matrica.

## Literatura i bilješke

1.  丘维声，高等代数（下）．清华大学出版社． (Qiu Weisheng, Viša algebra (2. dio). Tsinghua University Press.)
2.  [Vector space](https://en.wikipedia.org/w/index.php?title=Vector_space&oldid=1108546097). *Wikipedia, The Free Encyclopedia*.
