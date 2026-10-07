---
title: Alpha–beta odsijecanje
---

Ova stranica kratko predstavlja algoritam Minimax i alpha–beta odsijecanje.

## Algoritam Minimax

Algoritam Minimax, zvan i algoritam minimizacije maksimuma, algoritam je koji minimizira potencijalni gubitak u najgorem (tj. najvećem gubitku) slučaju.

### Postupak

U igrama dvaju igrača s nultom sumom i potpuno određenim pozicijama često se provodi protivničko pretraživanje: gradi se stablo pretraživanja u kojem je svaki čvor jedno određeno stanje. Na neparnim razinama na potezu smo mi, a na parnim protivnik. Svakom listu stabla pridružuje se procjena; što je procjena veća, veće su naše šanse za pobjedu. Mi težimo većim šansama, a protivnik ih nastoji smanjiti; na stablu pretraživanja to znači da čvorovi na neparnim razinama (naši čvorovi) uvijek biraju stanje djeteta s najvećim šansama, a čvorovi na parnim razinama (protivnikovi čvorovi) uvijek biraju stanje djeteta s najmanjim (našim) šansama.

Algoritam Minimax obilazi stablo pretraživanja odozgo prema dolje, pri povratku ažurira odgovor informacijama iz podstabala i na kraju dobiva vrijednost korijena — to je najveći rezultat koji možemo postići ako obje strane igraju optimalno.

### Primjer

Pogledajmo jednostavan primjer.

Nazovimo nas MAX, a protivnika MIN; slika je sljedeća:

![](images/minimax-1.svg)

Na primjer, u sljedećoj situaciji, pretpostavimo da pretražujemo slijeva nadesno, a vrijednost korijena su naše šanse za pobjedu:

![](images/minimax-2.svg)

Trebamo odabrati srednji put. Naime, odaberemo li lijevi put, najlošije šanse su $3$; odaberemo li srednji, najlošije šanse su $15$; odaberemo li desni, najlošije šanse su $1$. Iako desni put možda nudi šanse $22$, dovoljno racionalan protivnik ostavit će nam šanse samo $1$. Nakon odvagivanja, očito je srednji put bolji.

![](images/minimax-3.svg)

Zapravo, pri razmatranju desnog puta, čim otkrijemo da šanse mogu biti $1$, ne moramo više gledati grane sa šansama $12$, $20$ i $22$. Naime, u usporedbi sa šansama dvaju lijevih putova već možemo zaključiti da desni put nije najbolji.

Naivni algoritam Minimax često mora izgraditi golemo stablo pretraživanja, pa vremenska i prostorna složenost postaju neprihvatljive. Alpha–beta odsijecanje metoda je koja Minimax optimizira odsijecanjem pomoću donjih i gornjih granica rezultata obiju strana u svakom čvoru stabla.

Treba napomenuti da u različitim problemima vrijednosti u čvorovima stabla pretraživanja imaju različita značenja: može biti procjena, rezultat, vjerojatnost pobjede itd. Radi jednostavnosti u nastavku ih sve zovemo rezultatima.

## Alpha–beta odsijecanje

Alpha–beta odsijecanje jest odsijecanje pretraživanja za algoritam Minimax.

### Postupak

U algoritmu Minimax, ako znamo rezultate sve djece nekog čvora, možemo izračunati rezultat tog čvora: za MAX čvor uzimamo najveći rezultat, a za MIN čvor najmanji.

Kad pretraživanje dođe do nekog čvora, ali još nije završeno, ne možemo izračunati rezultat tog čvora, ali možemo izračunati raspon rezultata obiju strana **među dosad pretraženim čvorovima**. Tijekom pretraživanja održavamo dvije varijable, $\alpha$ i $\beta$, koje označavaju donju i gornju granicu rezultata koje, kad igra dođe do tog čvora, **uzimajući u obzir sve dosad pretražene čvorove**, mogu jamčiti igrač Alpha (onaj koji traži najveći rezultat) odnosno igrač Beta (onaj koji traži najmanji rezultat).

Strategija alpha–beta odsijecanja ovisi o vrijednostima $\alpha$ i $\beta$ pri pretraživanju trenutnog čvora. Ako je trenutni čvor MAX čvor, igrač Alpha može nastaviti pretraživati njegovu djecu kako bi povećao donju granicu rezultata $\alpha$. No ako nakon nekog pretraživanja već vrijedi $\alpha\ge\beta$, daljnje pretraživanje tog čvora ne utječe na ishod igre: čim dođe do tog čvora, igrač Alpha može jamčiti rezultat od barem $\alpha$; ali igrač Beta već zna da postoji strategija (koja odstupa od trenutnog puta) koja jamči rezultat ne veći od $\beta\le\alpha$, pa igrač Beta nema razloga dopustiti da igra dođe do **trenutnog čvora**. Slično, ako je trenutni čvor MIN čvor i nakon pretraživanja nekog njegovog djeteta već vrijedi $\beta\le\alpha$, također ne treba pretraživati ostalu djecu, jer igrač Alpha nema razloga dopustiti da igra uđe u **trenutni čvor**. Sažimajući oba slučaja vidimo: kad je $\alpha \geq \beta$, preostale grane tog čvora ne treba dalje pretraživati (tj. može se odsijecati). Uočite da se odsijecati može i kad je $\alpha = \beta$, jer protivnik već ima alternativu koja mu jamči rezultat ne lošiji od $\alpha$ (tj. $\beta$), pa daljnje pretraživanje preostalih grana ne mijenja rezultat čvorova iznad.

Tijekom pretraživanja ne treba održavati rezultate čvorova; dovoljno je održavati $\alpha$ i $\beta$. Na početku postavimo $\alpha=-\infty,~\beta=+\infty$. Pri spuštanju prosljeđujemo informacije $\alpha$ i $\beta$ prema dolje, kako bismo zabilježili alternative obaju igrača.

Kad je dijete pretraženo, treba ažurirati informacije u trenutnom čvoru. Pretpostavimo da je trenutni čvor $X$ MAX čvor i da smo upravo pretražili njegovo dijete $Y$. Tada se vrijednost $\beta$ u čvoru $X$ ne mijenja; samo vrijednost $\alpha$ treba uzeti kao maksimum s rezultatom djeteta $Y$. Ako je dijete $Y$ list, izravno rezultatom djeteta $Y$ ažuriramo vrijednost $\alpha$ u trenutnom čvoru $X$; inače je dovoljno vrijednošću $\beta$ djeteta $Y$ ažurirati vrijednost $\alpha$ trenutnog čvora $X$. Tada postoje tri mogućnosti:

1.  Vrijednost $\beta$ djeteta $Y$ strogo je između vrijednosti $\alpha$ i $\beta$ čvora $X$. Budući da je dijete $Y$ naslijedilo vrijednost $\alpha$ čvora $X$ i ne ažurira je, nakon pretraživanja djeteta $Y$ i dalje vrijedi $\beta > \alpha$, što znači da pri pretraživanju djeteta $Y$ nije bilo odsijecanja. Konačna vrijednost $\beta$ djeteta $Y$ jednaka je najmanjoj od vrijednosti: naslijeđene vrijednosti $\beta$ čvora $X$ i rezultata sve djece (djeteta $Y$). Budući da je ta najmanja vrijednost strogo manja od vrijednosti $\beta$ čvora $X$, ona je sigurno najmanji rezultat sve djece djeteta $Y$. Zato je, kao MIN čvor, rezultat djeteta $Y$ upravo ta vrijednost $\beta$. Ažurirati njome vrijednost $\alpha$ čvora $X$ je opravdano.
2.  Vrijednost $\beta$ djeteta $Y$ jednaka je vrijednosti $\beta$ čvora $X$. Kao što je gore rečeno, to znači da rezultati sve djece djeteta $Y$ nisu manji od vrijednosti $\beta$ čvora $X$. To dalje znači da igrač Beta nema razloga dopustiti da igra uđe u čvor $X$: čim igrač Alpha odabere dijete $Y$, igrač Beta ne može postići rezultat manji od $\beta$. Zato se u tom slučaju vrijednošću $\beta$ djeteta $Y$ ažurira vrijednost $\alpha$ čvora $X$ kako bi u čvoru $X$ vrijedilo $\alpha=\beta$ i aktivirao se uvjet odsijecanja. Učinak je isti kao da smo vrijednost $\alpha$ čvora $X$ ažurirali stvarnim rezultatom u $Y$ — brojem većim ili jednakim vrijednosti $\beta$ u čvoru $X$.
3.  Vrijednost $\beta$ djeteta $Y$ manja je ili jednaka vrijednosti $\alpha$ čvora $X$. Tada je dijete $Y$ aktiviralo uvjet odsijecanja; njegov stvarni rezultat ne premašuje vrijednost $\beta$ djeteta $Y$, a tim manje vrijednost $\alpha$ čvora $X$. Ažuriranje vrijednosti $\alpha$ čvora $X$ stvarnim rezultatom djeteta $Y$ ne mijenja vrijednost $\alpha$. To ima isti učinak kao ažuriranje vrijednosti $\alpha$ čvora $X$ vrijednošću $\beta$ djeteta $Y$.

Ova analiza pokazuje da nakon završetka pretraživanja nekog djeteta samo u prvom slučaju $\alpha$ (ili $\beta$) točno bilježi stvarni rezultat tog djeteta kao MAX čvora (ili MIN čvora). U ostalim slučajevima to nije nužno točan rezultat, ali informacija koju daje dovoljna je da jamči ispravno odsijecanje, pa ne utječe na rezultat zabilježen u korijenu.

### Primjer

U ovom odjeljku analizom primjera pokazujemo kako se tijekom pretraživanja ažuriraju vrijednosti $\alpha$ i $\beta$ u pojedinim čvorovima. Usput računamo i rezultate uključenih čvorova. Tako možemo promatrati odnos između stvarnog rezultata svakog čvora i zabilježenih vrijednosti $\alpha$ i $\beta$. No treba imati na umu da se pri implementaciji algoritma stvarni rezultati tih čvorova ne računaju.

Za sljedeću situaciju pretpostavimo da pretražujemo slijeva nadesno:

![](images/alpha-beta-1.svg)

Pri inicijalizaciji postavimo $\alpha = -\infty,~\beta = +\infty$ i te informacije prosljeđujemo dolje duž puta pretraživanja.

![](images/alpha-beta-2.svg)

Kad pretraživanje dođe do čvora A, budući da je rezultat lijevog djeteta $3$, a čvor A je MIN čvor koji traži potez s manjim rezultatom, vrijednost $\beta$ mijenjamo u $3$, jer je $3$ manje od trenutne vrijednosti $\beta$ ($\beta = +\infty$). Zatim je rezultat desnog djeteta čvora A $17$; tada ne mijenjamo vrijednost $\beta$ čvora A, jer je $17$ veće od trenutne vrijednosti $\beta$ ($\beta = 3$). Sad su sva djeca čvora A pretražena, pa možemo izračunati da je rezultat čvora A $3$, što se podudara s vrijednošću $\beta$ zabilježenom u tom čvoru (slučaj 1 iz prethodnog teksta).

![](images/alpha-beta-3.svg)

Čvor A dijete je čvora B; nakon izračuna rezultata čvora A možemo ažurirati vrijednosti $\alpha$ i $\beta$ čvora B. Budući da je čvor B MAX čvor koji traži potez s većim rezultatom, vrijednost $\alpha$ mijenjamo u $3$, jer je vrijednost $\beta$ u djetetu A ($\beta=3$) veća od trenutne vrijednosti $\alpha$ ($\alpha = -\infty$). Zatim pretražujemo desno dijete C čvora B i prosljeđujemo mu vrijednosti $\alpha$ i $\beta$ čvora B.

![](images/alpha-beta-4.svg)

Za čvor C, budući da je rezultat lijevog djeteta $2$, a čvor C je MIN čvor, vrijednost $\beta$ mijenjamo u $2$. Sad je $\alpha \geq \beta$, pa preostalu djecu čvora C ne treba pretraživati, jer je sigurno da igrač Alpha ne bi dopustio da igra dođe do čvora C. Čvor C je MIN čvor i njegov je rezultat $2$, što ne premašuje zabilježenu vrijednost $\beta$ (slučaj 3 iz prethodnog teksta). Budući da su sva djeca čvora B pretražena, možemo izračunati da je rezultat čvora B $3$, jednak zabilježenoj vrijednosti $\alpha$ (slučaj 1 iz prethodnog teksta).

![](images/alpha-beta-5.svg)

Nakon izračuna rezultata čvora B, budući da je čvor B dijete čvora D, možemo ažurirati vrijednosti $\alpha$ i $\beta$ čvora D. Čvor D je MIN čvor, pa vrijednost $\beta$ mijenjamo u $3$. Zatim čvor D prosljeđuje vrijednosti $\alpha$ i $\beta$ čvoru E, a čvor E čvoru F. Čvor F ima samo jedno dijete, s rezultatom $15$; budući da je $15$ veće od trenutne vrijednosti $\beta$, a čvor F je MIN čvor, njegovu vrijednost $\beta$ ne ažuriramo, a zatim možemo izračunati da je rezultat čvora F $15$, veći od zabilježene vrijednosti $\beta$ (slučaj 2 iz prethodnog teksta).

![](images/alpha-beta-6.svg)

Nakon izračuna rezultata čvora F, budući da je čvor F dijete čvora E, možemo ažurirati vrijednosti $\alpha$ i $\beta$ čvora E. Čvor E je MAX čvor, pa ažuriramo vrijednost $\alpha$; sad je $\alpha \geq \beta$, pa možemo odsjeći preostale grane čvora E (tj. čvor G). Zatim, budući da je čvor E MAX čvor, rezultat čvora E postavljamo na $15$, strogo veći od zabilježene vrijednosti $\alpha$ (slučaj 3 iz prethodnog teksta). Vrijednošću $\alpha$ čvora E ažuriramo vrijednost $\beta$ čvora D, koja ostaje $3$. Sad su sva djeca čvora D pretražena, pa možemo izračunati da je rezultat čvora D $3$, jednak zabilježenoj vrijednosti $\beta$ (slučaj 1 iz prethodnog teksta).

![](images/alpha-beta-7.svg)

Nakon izračuna rezultata čvora D, budući da je čvor D dijete čvora H, možemo ažurirati vrijednosti $\alpha$ i $\beta$ čvora H. Čvor H je MAX čvor, pa ažuriramo $\alpha$. Zatim, prema redoslijedu pretraživanja, vrijednosti $\alpha$ i $\beta$ čvora H prosljeđujemo redom čvorovima I, J, K. Za čvor K rezultat lijevog djeteta je $2$, a čvor K je MIN čvor, pa ažuriramo $\beta$; sad je $\alpha \geq \beta$, pa možemo odsjeći preostale grane čvora K. Zatim rezultat čvora K postavljamo na $2$, manji ili jednak zabilježenoj vrijednosti $\beta$ (slučaj 3 iz prethodnog teksta).

![](images/alpha-beta-8.svg)

Nakon izračuna rezultata čvora K, budući da je čvor K dijete čvora J, možemo ažurirati vrijednosti $\alpha$ i $\beta$ čvora J. Čvor J je MAX čvor, pa ažuriramo $\alpha$, ali budući da je rezultat čvora K manji od $\alpha$, vrijednost $\alpha$ čvora J ostaje $3$. Zatim vrijednosti $\alpha$ i $\beta$ čvora J prosljeđujemo čvoru L. Budući da je čvor L MIN čvor, ažuriramo $\beta = 3$; sad je $\alpha \geq \beta$, pa možemo odsjeći preostale grane čvora L. Kako čvor L nema preostalih grana, ovdje zapravo nema odsijecanja. Zatim rezultat čvora L postavljamo na $3$, manji ili jednak zabilježenoj vrijednosti $\beta$ (slučaj 3 iz prethodnog teksta).

![](images/alpha-beta-9.svg)

Nakon izračuna rezultata čvora L, budući da je čvor L dijete čvora J, možemo ažurirati vrijednosti $\alpha$ i $\beta$ čvora J. Čvor J je MAX čvor, pa ažuriramo $\alpha$, ali budući da je rezultat čvora L manji ili jednak $\alpha$, vrijednost $\alpha$ čvora J ostaje $3$. Sad su sva djeca čvora J pretražena, pa možemo izračunati da je rezultat čvora J $3$, jednak zabilježenoj vrijednosti $\alpha$ (slučaj 2 iz prethodnog teksta).

Nakon izračuna rezultata čvora J, budući da je čvor J dijete čvora I, možemo ažurirati vrijednosti $\alpha$ i $\beta$ čvora I. Čvor I je MIN čvor, pa ažuriramo $\beta$; sad je $\alpha \geq \beta$, pa možemo odsjeći preostale grane čvora I. Vrijedi primijetiti da je, zbog postojanja desnog djeteta, stvarni rezultat čvora I $2$, manji od zabilježene vrijednosti $\beta$ (slučaj 3 iz prethodnog teksta).

Nakon izračuna rezultata čvora I, budući da je čvor I dijete čvora H, možemo ažurirati vrijednosti $\alpha$ i $\beta$ čvora H. Čvor H je MAX čvor, pa ažuriramo $\alpha$, ali budući da je rezultat čvora I manji ili jednak $\alpha$, vrijednost $\alpha$ čvora H ostaje $3$. Sad su sva djeca čvora H pretražena, pa možemo izračunati da je rezultat čvora H $3$, jednak zabilježenoj vrijednosti $\alpha$ (slučaj 1 iz prethodnog teksta).

![](images/alpha-beta-10.svg)

To je konačni rezultat.

### Implementacija

???+ example "Primjer koda"
    ```cpp
    int alpha_beta(int u, int alph, int beta, bool is_max) {
      if (!son_num[u]) return val[u];
      if (is_max) {
        for (int i = 0; i < son_num[u]; ++i) {
          int d = son[u][i];
          alph = max(alph, alpha_beta(d, alph, beta, !is_max));
          if (alph >= beta) break;
        }
        return alph;
      } else {
        for (int i = 0; i < son_num[u]; ++i) {
          int d = son[u][i];
          beta = min(beta, alpha_beta(d, alph, beta, !is_max));
          if (alph >= beta) break;
        }
        return beta;
      }
    }
    ```

## Literatura i bilješke

-   [Minimax Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Minimax#Minimax_algorithm_with_alternate_moves)
-   [Alpha–beta pruning - Wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

**Dio ovog članka preuzet je iz blog-zapisa [Detaljno o algoritmu Minimax i α-β odsijecanju – 文剑木然 (kineski)](https://blog.csdn.net/wenjianmuran/article/details/90633418), pod licencijom CC 4.0 BY-SA. Sadržaj je izmijenjen.**
