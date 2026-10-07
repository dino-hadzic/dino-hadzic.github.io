---
title: Osnove segment treea
---

## Uvod

Segment tree (segmentno stablo) struktura je podataka koja se u natjecateljskom programiranju često koristi za održavanje **informacija o intervalima**.

Segment tree može u vremenskoj složenosti $O(\log N)$ izvesti izmjenu jednog elementa, upit za jedan element, izmjenu intervala, upit nad intervalom i slične operacije.

## Osnovna struktura i operacije

Segment tree je binarno stablo. Svaki njegov čvor pohranjuje informaciju o jednom intervalu:

-   list pohranjuje informaciju o jednom elementu $x$, što se može shvatiti i kao informacija o intervalu $[x,x]$ duljine $1$;
-   listovi podstabla s korijenom u unutarnjem čvoru čine neprekinuti interval $[l,r]$, pa taj čvor pohranjuje informaciju o intervalu $[l,r]$.

Unutarnji čvor uvijek ima dva djeteta, a njegov je interval upravo disjunktna unija intervala te dvoje djece. Ako unutarnji čvor pohranjuje informaciju o intervalu $[l,r]~(l < r)$, njegova dva djeteta pohranjuju informacije o $[l,m]$ i $[m+1,r]$, gdje je $l \le m < r$.

Korijen segment treea pohranjuje informaciju o cijelom intervalu $[L,R]$. Veličinu segment treea izražavamo duljinom tog intervala $N = R - L + 1$.

### Informacija o intervalu

Segment tree održava informacije o intervalima. U ovom odjeljku opisujemo uobičajena svojstva koja informacija o intervalu mora zadovoljavati i odgovarajuće načine implementacije.

Općenito, **informacija o intervalu** funkcija je $\varphi:\mathcal I\rightarrow M$ čiji je argument interval; pri tome $\mathcal I$ označava skup svih podintervala od $[L,R]$ (uključujući prazan interval), a $M$ prostor vrijednosti koje informacija može poprimiti – u ovom ga članku zovemo **prostor informacija**. Informacija $\varphi$ koju segment tree pohranjuje mora zadovoljavati sljedeća svojstva:

1.  Ako se interval podijeli na dva podintervala, informacija o njemu može se dobiti spajanjem informacija o podintervalima. Drugim riječima, ako je $I$ disjunktna unija od $I_1$ i $I_2$, pri čemu je $I_1$ lijevo od $I_2$, onda je $\varphi(I)=\varphi(I_1)\circ\varphi(I_2)$, gdje operacija $\circ$ označava **spajanje informacija**.
2.  Ako se interval podijeli na disjunktnu uniju više podintervala, rezultat spajanja informacija o tim podintervalima ne ovisi ni o načinu podjele ni o načinu grupiranja i uvijek je jednak informaciji o početnom intervalu. Drugim riječima, operacija $\circ$ je asocijativna.
3.  I prazan interval $\varnothing$ ima dobro definiranu informaciju $e=\varphi(\varnothing)$. Štoviše, budući da se svaki interval $I$ može shvatiti kao disjunktna unija samog sebe i praznog intervala $\varnothing$, spajanje bilo koje informacije s informacijom praznog intervala ne mijenja je. Drugim riječima, $\varphi(I)\circ e = e\circ\varphi(I) = \varphi(I)$. To znači da je $e$ neutralni element operacije $\circ$.

Ta svojstva jamče da je za upit o informaciji intervala $I$ dovoljno pronaći niz čvorova čiji intervali čine particiju od $I$; informacija o $I$ tada se dobiva spajanjem informacija pohranjenih u tim čvorovima.

Informacije o intervalima mogu se spajati, spajanje je asocijativno i postoji neutralni element. Ta svojstva znače da prostor informacija $M$ s operacijom spajanja $\circ$ čini [monoid](../math/algebra/basic.md#群).[^monoid]

???+ info "Dogovor"
    U referentnim implementacijama operacija segment treea u ovom članku pretpostavljamo da su elementi prostora informacija $M$ pohranjeni u strukturi `Info`, čiji zadani konstruktor daje neutralni element i koja preopterećuje operator zbrajanja za spajanje informacija.

???+ example "Primjeri"
    Mnoge informacije o intervalu zadovoljavaju svojstva monoida. Duljina intervala, zbroj, umnožak i maksimum intervala jednostavni su primjeri. Pripadni monoidi redom su $(\mathbf N,+),~(\mathbf R,+),~(\mathbf R,\times),~(\mathbf R\cup\{-\infty\},\max)$, a neutralni elementi redom $0,0,1,-\infty$. Ti se primjeri mogu proširiti na druge uobičajene operacije koje zadovoljavaju svojstva monoida, npr. XOR po bitovima, množenje matrica, kompoziciju funkcija itd.
    
    Postoje i složeniji primjeri. Primjerice, najveći (neprazni) zbroj podintervala također se može održavati monoidom. Naravno, ako održavamo samo tu jednu varijablu, spajanje nije moguće. Za particiju $I = I_1 \cup I_2$ najveći zbroj podintervala intervala $I$ može se postići na podintervalu od $I_1$, na podintervalu od $I_2$ ili na podintervalu koji prelazi iz $I_1$ u $I_2$. Za izračun maksimuma u posljednjem slučaju treba dodatno pamtiti zbroj intervala, najveći (neprazni) prefiksni zbroj i najveći (neprazni) sufiksni zbroj.
    
    === "Zbroj intervala"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-2.cpp:info"
        ```
    
    === "Maksimum intervala (nenegativne vrijednosti)"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-bisect-recursive.cpp:info"
        ```
    
    === "Linearna funkcija"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-recursive.cpp:info"
        ```
    
    === "Najveći neprazni zbroj podintervala"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-1.cpp:info"
        ```

Treba imati na umu da spajanje informacija o intervalima ne mora biti komutativno. Pri spajanju se strogo mora poštovati redoslijed podintervala slijeva nadesno.

### Rekurzivna izgradnja i načini pohrane

Da bi visina stabla bila što manja, interval $[l,r]$ trenutnog čvora treba podijeliti na dva što ravnomjernija dijela. Zato se obično uzima

$$
m = \left\lfloor\dfrac{l + r}{2}\right\rfloor.
$$

Tako, ako interval trenutnog čvora ima duljinu $n > 1$, njegova dva djeteta $[l,m]$ i $[m+1,r]$ odgovaraju intervalima duljine $\lceil n/2\rceil$ odnosno $\lfloor n/2\rfloor$. Visina ovako dobivenog segment treea je $\lceil\log_2N\rceil$. To jamči da je segment tree balansirano binarno stablo i da je složenost operacija nad jednim elementom uvijek $O(\log N)$.

![](images/seg-1.svg)

Za pohranu informacija o intervalu duljine $N$ treba izgraditi segment tree s $N$ listova. Kao puno binarno stablo (svaki čvor ima $0$ ili $2$ djeteta), segment tree ima točno $2N-1$ čvorova koji pohranjuju informacije. Drugim riječima, prostorna složenost ovako izgrađenog segment treea je $\Theta(N)$; pri rekurzivnoj izgradnji svaki se čvor posjeti točno jednom, pa je i vremenska složenost $\Theta(N)$.

Iako je struktura segment treea relativno fiksna, način pohrane nije jedinstven.

![](images/seg-2.svg)

Prvi uobičajeni način je pohrana u obliku hrpe (heap-style, kao na slici), tj. segment tree se uloži u savršeno binarno stablo. Korijen tada ima oznaku $1$; ako trenutni čvor ima oznaku $i$, njegovo lijevo i desno dijete imaju oznake $2i$ i $2i+1$. Budući da je visina stabla $\lceil\log_2N\rceil$, za takvu pohranu treba niz duljine $2^{\lceil\log_2N\rceil + 1}$. Radi jednostavnosti računanja obično se izravno zauzme niz duljine $4N$[^heap-size]; ili se $N$ nadopuni do potencije dvojke $N'$ i zauzme niz duljine $2N'$. Prednost je takve pohrane da ne treba dodatno pohranjivati oznake djece, a nedostatak da postoji dio neiskorištenih čvorova, pa iskoristivost prostora nije visoka.

![](images/seg-3.svg)

Drugi uobičajeni način je korištenje spremišta memorije (memory pool) i dinamičko dodjeljivanje oznaka čvorova. Budući da je oblik segment treea fiksan, dovoljno je oznake dodijeliti jednom, pri izgradnji. Tako nema neiskorištenih čvorova i dovoljan je niz duljine $2N$. Oznake čvorova tada su redni brojevi u preorder obilasku stabla. Međutim, budući da se oznaka (desnog) djeteta ne može izračunati samo iz oznake trenutnog čvora[^child-id], obično se dodatno zauzimaju nizovi ukupne duljine $4N$ za pohranu oznaka lijevog i desnog djeteta. Ako je prostor za jednu oznaku $1$, a za jedan čvor $K$, dinamička dodjela nije prostorno lošija od pohrane u obliku hrpe čim je $2NK + 4N \le 4NK$, tj. $K \ge 2$.

Ova dva načina pohrane i izgradnje segment treea implementiraju se ovako:

???+ example "Referentna implementacija"
    === "Pohrana u obliku hrpe"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-recursive.cpp:build"
        ```
    
    === "Dinamička dodjela čvorova"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-lazy-recursive.cpp:build"
        ```

???+ tip "Savjet"
    1.  Pri računanju sredine $m = \lfloor(l+r)/2\rfloor$ intervala $[l,r]$ koristite `m = l + (r - l) / 2` umjesto `m = (l + r) / 2`; tako izbjegavate prelijevanje cijelih brojeva i probleme sa zaokruživanjem prema nuli pri dijeljenju negativnih brojeva.
    2.  Obično se implementira funkcija `push_up` koja spaja informacije djece u trenutni čvor.

Osim razlike u načinu pristupa djeci, izbor načina pohrane ne utječe na implementaciju operacija nakon izgradnje. Međutim, kod pohrane u obliku hrpe oznaka čvora određena je njegovim položajem u savršenom binarnom stablu, pa je slabo proširiva i ne podržava proširenja poput dinamičkog stvaranja čvorova i perzistentnosti.

### Izmjena i upit za jedan element

Najjednostavnije operacije segment treea su operacije nad jednim elementom (point update / point query).

Promotrimo prvo upit za jedan element. U segment treeu elementi su u listovima poredani. Zato je pri rekurziji u unutarnjem čvoru dovoljno usporediti traženi element sa sredinom trenutnog intervala da bi se odlučilo nastavlja li se u lijevo ili desno dijete. Kad se dođe do lista, vraća se informacija pohranjena u njemu. Time je upit za jedan element dovršen.

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-recursive.cpp:point-get"
    ```

Izmjena jednog elementa je slična. Jednako se odozgo prema dolje pronađe traženi list, zatim se list izmijeni, a na kraju, pri povratku iz rekurzije, treba ažurirati informacije svih predaka tog lista. To je izmjena jednog elementa. Budući da se svaka izmjena jednog elementa može shvatiti kao zamjena njegove vrijednosti, ovdje dajemo samo referentnu implementaciju postavljanja vrijednosti. Općenitije izmjene razmatraju se u odjeljku [Intervalna izmjena](#intervalna-izmjena-i-lijene-oznake).

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-recursive.cpp:point-set"
    ```

Budući da je visina stabla $\Theta(\log N)$, operacije segment treea nad jednim elementom imaju složenost $O(\log N)$.

### Upit nad intervalom

Promotrimo sada upit nad intervalom.

![](images/seg-5.svg)

Već smo objasnili da je dovoljno traženi interval rastaviti na disjunktnu uniju intervala nekoliko čvorova segment treea i zatim redom spojiti informacije tih čvorova. Naravno, što manje čvorova, to bolje. To znači da rastavljeni čvorovi moraju odgovarati **maksimalnim intervalima** sadržanima u intervalu upita. Na slici je svijetlo označen interval operacije, a čvorovi s podebljanim rubom odgovaraju maksimalnim intervalima. Te čvorove lako je pronaći: krenuvši od korijena, pretražujemo prema dolje sve čvorove čiji se interval siječe s intervalom upita; kad naiđemo na čvor koji je potpuno sadržan u intervalu upita, našli smo čvor maksimalnog intervala, pa njegove potomke ne treba dalje pretraživati.

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-recursive.cpp:range-get"
    ```

???+ tip "Savjet"
    1.  Osim gornjeg načina, pretraživanje se može prekinuti i kad se pri silasku naiđe na čvor čiji je interval disjunktan s intervalom upita.
    2.  Budući da se rezultat inicijalizira neutralnim elementom prostora informacija $M$, rezultat lijevog djeteta može ga izravno prepisati, bez spajanja.

Može se pokazati da je ukupan broj čvorova posjećenih tijekom upita nad intervalom – svih čvorova maksimalnih intervala i njihovih predaka – jednak $O(\log N)$. Stoga je i složenost upita nad intervalom $O(\log N)$.

??? note "Dokaz"
    Pri upitu nad intervalom, za svaki posjećeni čvor koji nije korijen interval njegova roditelja nužno sadrži lijevi ili desni kraj intervala upita. Kad ne bi bilo tako, interval roditelja bio bi ili potpuno sadržan u intervalu upita ili disjunktan s njim, pa se u oba slučaja ne bi nastavilo u njegovu djecu (tj. u trenutni čvor). Nadalje, intervali čvorova iste dubine međusobno su disjunktni, pa najviše $1$ sadrži lijevi i najviše $1$ desni kraj, a svaki čvor ima najviše $2$ djeteta. Stoga se pri upitu na svakoj dubini posjećuje najviše $4$ čvora. Visina segment treea je $\Theta(\log N)$, pa je i broj posjećenih čvorova $O(\log N)$.

### Intervalna izmjena i lijene oznake

Na kraju, promotrimo izmjenu intervala.

Za razliku od upita nad intervalom, utjecaj izmjene intervala ne ograničava se na čvorove maksimalnih intervala i njihove pretke, nego zahvaća i njihove potomke. Naime, izmjena intervala utječe na podintervale maksimalnih intervala, tj. na potomke odgovarajućih čvorova. Izmijeniti sve zahvaćene čvorove očito je prekomplicirano i nerealno. Zato se pri implementaciji intervalne izmjene koristi ideja **lijene oznake** (lazy tag). Konkretno, svaka izmjena intervala stvarno mijenja samo čvorove maksimalnih intervala i njihove pretke, a izmjena potomaka tih čvorova odgađa se dok ne bude nužna. Da bi se zabilježile izmjene koje tek treba izvesti, u čvoru maksimalnog intervala ostavlja se oznaka. Ta oznaka bilježi operacije koje nad potomcima (ne uključujući sam čvor) treba izvesti, a još nisu izvedene. To je lijena oznaka.

???+ info "Dogovor"
    U ovom članku pretpostavljamo da je izmjena samog čvora koji nosi lijenu oznaku već dovršena. To nije obvezno i može ovisiti o implementaciji.

U segment treeu koji podržava intervalnu izmjenu treba prilagoditi i implementaciju ostalih operacija. Pri svakoj operaciji, kad god treba pristupiti djeci nekog čvora, provjerava se ima li trenutni čvor nepraznu lijenu oznaku. Ako ima, oznaku treba prvo spustiti (push down), a tek onda nastaviti s pristupom djeci ili drugim operacijama. Spuštanje lijene oznake znači da se nad djecom čvora izvede odgovarajuća izmjena, djeci se dodijeli lijena oznaka, a na kraju se oznaka trenutnog čvora isprazni.

???+ example "Primjer"
    Slika prikazuje segment tree izgrađen nad nizom $[4,1,3,2,5]$.
    
    ![](images/seg-lazy-1.svg)
    
    U svakom čvoru $s$ označava zbroj elemenata trenutnog intervala, a $t$ je lijena oznaka za intervalno zbrajanje. Na početku su svi zbrojevi točni, a sve lijene oznake prazne. Sada svim elementima intervala $[2,5]$ dodamo $2$; rezultat je na sljedećoj slici.
    
    ![](images/seg-lazy-2.svg)
    
    Na slici je svijetlo označen interval operacije, a čvorovi s podebljanim rubom odgovaraju maksimalnim intervalima. U tim čvorovima zbroj $s$ povećao se za $2$ puta duljina intervala, što točno odražava promjenu nastalu intervalnim zbrajanjem; istodobno se lijena oznaka povećala za $2$, što znači da potomci još nisu ažurirani. Preci čvorova maksimalnih intervala dobili su ažurirane zbrojeve od svoje djece. Ako sada postavimo upit za zbroj intervala $[4,4]$, rezultat je na sljedećoj slici.
    
    ![](images/seg-lazy-3.svg)
    
    Pri pristupu intervalu $[4,4]$ prvo se posjeti interval $[4,5]$ i uoči da nosi lijenu oznaku $t=2$. Prije pristupa njegovoj djeci oznaku treba spustiti: nad svakim djetetom izvede se intervalno zbrajanje s $2$, lijene oznake djece također se povećaju za $2$ (što znači da njihovi potomci – iako ih na slici nema – još nisu ažurirani), a na kraju se oznaka na $[4,5]$ isprazni. Nakon spuštanja nastavlja se u dijete $[4,4]$ i čita se točan zbroj $4$.

Pri izmjeni intervala ili spuštanju lijene oznake čvor koji treba označiti može već imati nepraznu lijenu oznaku. Tada se oznaka ne smije jednostavno prepisati, nego je treba zamijeniti kompozicijom dviju operacija. Budući da kompozicija operacija ne mora biti komutativna, pri kompoziciji treba paziti na redoslijed: nova operacija uvijek se primjenjuje nakon postojeće oznake. Pri spuštanju oznake oznaka roditelja uvijek se primjenjuje nakon postojeće oznake djeteta. Razlog je što se prije pristupa djetetu oznaka nužno spušta, pa kad je postojeća oznaka djeteta postavljena, roditelj sigurno nije imao oznaku; trenutna oznaka roditelja može potjecati samo od kasnijih operacija.

Da bi se intervalne izmjene ispravno zabilježile, treba razumjeti svojstva koja takve operacije moraju zadovoljavati. Neka je informacija koju segment tree bilježi i dalje funkcija $\varphi:\mathcal I\rightarrow M$. Nadalje, neka je izmjena $\pi:M\rightarrow M$ koja po nekom pravilu staru informaciju pretvara u novu. Tada intervalna izmjena $\pi$ mora zadovoljavati sljedeća svojstva:

1.  Dobro je definirana. Drugim riječima, rezultat intervalne izmjene ovisi samo o informaciji $m\in M$, a ne o intervalu $I\in\mathcal I$ na kojem se nalazi. Ako rezultat izmjene ovisi o značajkama intervala, te značajke (npr. duljinu intervala, lijevi i desni kraj) treba uključiti u informaciju o intervalu.
2.  Izmjena mora biti kompatibilna sa spajanjem informacija. Drugim riječima, ako se informacija o intervalu može dobiti spajanjem informacija o podintervalima, onda se i rezultat izmjene tog intervala može dobiti spajanjem rezultata izmjene informacija o podintervalima; tj. za $m_1,m_2\in M$ uvijek vrijedi $\pi(m_1\circ m_2) = \pi(m_1)\circ\pi(m_2)$.
3.  Posebno, informacija praznog intervala nakon izmjene ostaje informacija praznog intervala, tj. $\pi(e)=e$.[^endo]

To znači da je izmjena [endomorfizam](../math/algebra/group-theory.md#群同态) monoida $M$. Nadalje, promotrimo skup $\Pi$ svih takvih izmjena: ako je zatvoren na kompoziciju, onda je, budući da je kompozicija asocijativna i identiteta je neutralni element, i $\Pi$ monoid.

???+ info "Dogovor"
    U referentnim implementacijama operacija segment treea u ovom članku pretpostavljamo da su izmjene pohranjene u strukturi `Transform`, čiji zadani konstruktor daje identitetu, koja preopterećuje operator zbrajanja za kompoziciju operacija i operator poziva (zagrade) za izmjenu informacije o intervalu. Radi lakše provjere je li lijena oznaka prazna (tj. ne mijenja ništa), preopterećena je i eksplicitna pretvorba u `bool`.

???+ example "Primjeri"
    Segment tree podržava mnoge izmjene; intervalno zbrajanje, množenje, pridruživanje (assignment) i afina transformacija uobičajeni su primjeri. Teškoća u implementaciji često nije u samoj operaciji, nego u tome kako je primijeniti na informaciju o intervalu, tj. kako zadovoljiti tri gornja svojstva. Primjerice, ako održavamo zbroj intervala i želimo intervalno zbrajanje, doprinos zbroju jednak je dodanom broju pomnoženom duljinom intervala, a duljina intervala nije dio informacije. Tada, prema prvom svojstvu, duljinu intervala jednostavno uključimo u informaciju.
    
    === "Minimum intervala & intervalno zbrajanje"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-perm-recursive.cpp:info"
        --8<-- "docs/ds/code/seg/seg-perm-recursive.cpp:transform"
        ```
    
    === "Zbroj intervala & intervalno zbrajanje"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-5.cpp:info"
        --8<-- "docs/ds/code/seg/seg-5.cpp:transform"
        ```
    
    === "Maksimum intervala & intervalno pridruživanje"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-bisect-recursive.cpp:info"
        --8<-- "docs/ds/code/seg/seg-bisect-recursive.cpp:transform"
        ```

Kad je struktura za pohranu intervalnih izmjena implementirana, lijeno ažuriranje i spuštanje lijenih oznaka implementira se ovako:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-lazy-recursive.cpp:tag"
    ```

???+ tip "Savjet"
    1.  Lijene oznake ne stavljajte na prazne čvorove.
    2.  Uz pažljivu implementaciju lijene oznake ne moraju se stavljati ni na listove.

Složenost jednog spuštanja obično je $O(1)$.

Nadalje, intervalna izmjena implementira se ovako:

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-lazy-recursive.cpp:range-set"
    ```

Kao i upit nad intervalom, intervalna izmjena segment treea s lijenim oznakama ima složenost $O(\log N)$. Ostale operacije segment treea s lijenim oznakama implementiraju se gotovo jednako kao bez njih; dovoljno je prije pristupa djeci dodati spuštanje oznake. Budući da jedna operacija spusti najviše $O(\log N)$ oznaka, vremenska složenost tih operacija i dalje je $O(\log N)$, samo s većom konstantom. Ako nema intervalnih izmjena, obično se implementira segment tree bez lijenih oznaka, radi manje konstante.

### Referentna implementacija

Slijede potpune referentne implementacije segment treea bez lijenih oznaka i s njima.

??? example "Referentna implementacija"
    === "Bez lijenih oznaka"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-recursive.cpp:seg-tree"
        ```
    
    === "S lijenim oznakama"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-lazy-recursive.cpp:seg-tree"
        ```

U konkretnoj primjeni može biti potrebno provjeriti jesu li izmjene i upiti valjani.

## Uobičajene tehnike

U ovom odjeljku opisujemo nekoliko tehnika koje se često koriste pri rješavanju konkretnih zadataka segment treeom. One ili smanjuju konstantu algoritma ili proširuju osnovne mogućnosti.

### Nerekurzivna implementacija

Rekurzivne implementacije segment treea opisane prije mogu se obilaziti samo rekurzivno odozgo prema dolje i plaćaju odgovarajući trošak rekurzije. Drugi je pristup održavati segment tree odozdo prema gore. U kineskim natjecateljskim materijalima ova se implementacija raširila zahvaljujući Zhangu Kunweiju, pa se često naziva i **zkw segment tree**.

![](images/seg-4.svg)

Slika prikazuje način pohrane u nerekurzivnoj implementaciji. Segment tree i dalje je uložen u savršeno binarno stablo, ali se gradi odozdo prema gore. Prvo se svi listovi pohrane na istoj razini, dubine $\lceil\log_2N\rceil$; suvišni listovi pohranjuju neutralni element $e$, koji se može shvatiti kao informacija praznog intervala. Zatim se unutarnji čvorovi obilaze odozdo prema gore i informacije djece spajaju se u trenutni čvor. Budući da su svi listovi na istoj razini, ovako izgrađen segment tree strukturno se malo razlikuje od prethodnih dvaju načina, ali jednako može održavati informacije o intervalima. Prostorno je isti kao pohrana u obliku hrpe: treba niz duljine $2^{\lceil\log_2N\rceil + 1}$.

Najveća je prednost ovog načina pohrane da su oznake listova uzastopne i lako ih je locirati, a oznake roditelja i djece izravno se računaju. Kao na slici, ako je $n=2^{\lceil\log_2N\rceil}$, tj. $N$ nadopunjen do potencije dvojke, vrijednost elementa $x\in[L,R]$ pohranjena je u čvoru s oznakom $n+x-L$; za čvor s oznakom $i$ koji nije korijen roditelj ima oznaku $\lfloor i/2\rfloor$, općenitije, predak na razini $d$ ima oznaku $\lfloor i/2^d\rfloor$; za unutarnji čvor s oznakom $i$ lijevo i desno dijete imaju oznake $2i$ i $2i+1$.

Zbog tih svojstava izgradnja i operacije nad jednim elementom vrlo se lako implementiraju. Za izgradnju je dovoljno kopirati informacije elemenata u odgovarajuće listove i zatim obrnutim redom proći čvorove $[1,n-1]$ spajajući informacije djece. Upit za jedan element izravno vraća informaciju odgovarajućeg lista. Izmjena jednog elementa također izravno mijenja odgovarajući list, a zatim ažurira informacije njegovih predaka.

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-nonrecursive.cpp:build"
    --8<-- "docs/ds/code/seg/seg-nonrecursive.cpp:point-get"
    --8<-- "docs/ds/code/seg/seg-nonrecursive.cpp:point-set"
    ```

![](images/seg-6.svg)

Upit nad intervalom malo je složeniji: treba pronaći sve čvorove maksimalnih intervala intervala $[l,r]$ u segment treeu. Zanemarimo privremeno desni kraj upita i promotrimo maksimalni interval koji sadrži lijevi kraj $l$. Svi čvorovi koji ga sadrže su list koji odgovara $l$ i njegovi preci. Stoga od lista za $l$ skačemo prema gore dok trenutni čvor ne postane desno dijete svog roditelja: tada roditelj sadrži i elemente lijevo od trenutnog čvora, a oni ne pripadaju još neobrađenom dijelu, pa je interval trenutnog čvora upravo maksimalni interval koji sadrži $l$. Nakon što pribrojimo njegovu informaciju, pomaknemo se na istoj razini za jedan čvor udesno i skočimo roditelju; tako dobivamo čvor koji sadrži najljeviji još neobrađeni element, i postupak ponavljamo. Desni kraj obrađuje se simetrično. U stvarnoj implementaciji oba se kraja obrađuju istodobno dok se ne sretnu; tada je interval upita upravo obrađen do kraja. Treba paziti da se informacije skupljaju odvojeno s lijeve i desne strane, a tek se na kraju oba rezultata spoje, kako bi redoslijed spajanja bio ispravan.

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-nonrecursive.cpp:range-get"
    ```

???+ tip "Savjet"
    Kod upita nad intervalom različite implementacije malo se razlikuju. Ovdje je implementiran upit nad zatvorenim intervalom $[l,r]$, [AtCoder Library](https://github.com/atcoder/ac-library/blob/master/atcoder/segtree.hpp#L52-L65) implementira upit nad $[l,r)$, a izvorni materijali Zhanga Kunweija upit nad $(l,r)$. Među njima nema bitne razlike, samo se granice obrađuju drugačije.

Na kraju promotrimo intervalnu izmjenu; ključ je obrada lijenih oznaka. Čvorovima se i dalje može pristupati odozdo prema gore, ali spuštanje oznaka mora ići odozgo prema dolje, inače se ne mogu isprazniti sve oznake na putu od korijena do lista. Stoga je dovoljno pronaći sve pretke čvorova maksimalnih intervala i odozgo prema dolje redom spustiti oznake. Uočimo da roditelj čvora maksimalnog intervala nužno sadrži jedan od krajeva, a svi čvorovi koji sadrže neki kraj leže na putu od korijena do lista tog kraja. Međutim, nije svaki čvor na tom putu predak čvora maksimalnog intervala: dio od čvora maksimalnog intervala koji sadrži taj kraj pa nadolje do lista nije, i pri obradi ga treba preskočiti. Dakle, dovoljno je duž dvaju putova do listova lijevog i desnog kraja jednom od korijena prema listu spustiti oznake, preskačući taj dio. Nakon izmjene duž istih dvaju putova odozdo prema gore ažuriraju se informacije predaka.

???+ example "Referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-lazy-nonrecursive.cpp:range-set"
    ```

???+ tip "Savjet"
    1.  Ovdje je i dalje implementirana izmjena zatvorenog intervala $[l,r]$; za poluotvoreni $[l,r)$ pogledajte [AtCoder Library](https://github.com/atcoder/ac-library/blob/master/atcoder/lazysegtree.hpp#L110-L138). Obje inačice koriste operacije nad bitovima i istu temeljnu ideju: dio čvorova koji treba preskočiti ima lijevi (desni) kraj intervala poravnat s lijevim (desnim) krajem intervala izmjene.
    2.  Za taj dio čvorova preskakanje pri spuštanju utječe samo na učinkovitost, ali pri povratku prema gore preskakanje je nužno: poziv `push_up` na čvoru koji je tek dobio lijenu oznaku prepisao bi ga još neažuriranim informacijama djece.

U nerekurzivnoj implementaciji s lijenim oznakama ostale operacije također samo trebaju prije pristupa dodati spuštanje od korijena prema listu.

Slijedi potpuna referentna implementacija nerekurzivnog segment treea, također u dvjema inačicama – bez lijenih oznaka i s njima:

??? example "Referentna implementacija"
    === "Bez lijenih oznaka"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-nonrecursive.cpp:seg-tree"
        ```
    
    === "S lijenim oznakama"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-lazy-nonrecursive.cpp:seg-tree"
        ```

Osim što se složenost upita za jedan element u segment treeu bez lijenih oznaka smanjuje na $O(1)$, složenosti ostalih operacija jednake su rekurzivnoj inačici, samo s manjom konstantom.

Ukratko, nerekurzivna implementacija također podržava sve osnovne operacije segment treea, uključujući intervalnu izmjenu i lijene oznake. Ali, kao i kod pohrane u obliku hrpe, oznake čvorova određene su položajem, pa cijelo savršeno binarno stablo mora postojati unaprijed; stoga nije moguće dinamičko stvaranje čvorova, a ni perzistentnost nije praktična.

### Dinamičko stvaranje čvorova

Svi dosad opisani načini pohrane zahtijevaju da se pri izgradnji odjednom zauzme prostor veličine $\Theta(N)$. To nije izvedivo kad je duljina intervala $N$ velika (npr. $\sim 10^9$). Radi uštede prostora stablo se ne mora izgraditi odjednom: na početku se stvori samo korijen koji predstavlja cijeli interval, a dijete koje predstavlja neki podinterval stvara se tek kad mu treba pristupiti. Budući da oznake čvorova nisu fiksne, segment tree s dinamičkim stvaranjem čvorova može se implementirati samo dinamičkom dodjelom iz spremišta memorije, s nizovima za oznake djece.

Preduvjet je da je informacija koja odgovara još nestvorenim čvorovima poznata. Najjednostavniji je slučaj kad je informacija intervala nestvorenog čvora upravo neutralni element $e$ prostora informacija $M$ (tj. informacija praznog intervala). Tada upit na praznom čvoru jednostavno vraća $e$, a ni spajanje ne zahtijeva poseban tretman; čvorovi se stvaraju duž puta samo kad izmjena treba upisati informaciju. Općenitiji je slučaj kad informacija nestvorenog čvora ovisi o njegovu intervalu. Kod takvih zadataka pri upitu na praznom čvoru, pri stvaranju novog čvora i pri spajanju informacija djece treba informaciju izračunati iz krajeva trenutnog intervala. U svakom slučaju, segment tree s dinamičkim stvaranjem čvorova obično se ne može izgraditi iz proizvoljnog početnog niza. Osim toga, budući da oznaka čvora više ne nosi informaciju o intervalu, pri dijeljenju intervala treba kao u rekurzivnoj implementaciji interval trenutnog čvora prenositi kao parametar iz razine u razinu; posebno treba paziti da se prije spuštanja lijene oznake prvo stvore djeca.

![](images/seg-7.svg)

Za referencu dajemo implementacije segment treea s dinamičkim stvaranjem čvorova bez lijenih oznaka i s njima. U skladu s dva gore opisana slučaja, prva pretpostavlja da je informacija nestvorenog čvora upravo neutralni element $e$, a druga da ovisi o intervalu.

??? example "Referentna implementacija"
    === "Bez lijenih oznaka"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-dynamic.cpp:seg-tree"
        ```
    
    === "S lijenim oznakama"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-lazy-dynamic.cpp:seg-tree"
        ```

???+ tip "Savjet"
    Pri spuštanju oznaka prvo treba stvoriti djecu, što povećava konstantu prostorne složenosti; zauzmite dovoljno prostora.

Budući da svaka izmjena stvara čvorove samo duž najviše dvaju putova od korijena prema listovima, jedna operacija stvara najviše $O(\log N)$ novih čvorova. Stoga je nakon $q$ operacija ukupan broj čvorova $O(q\log N)$, i upravo zato dinamičko stvaranje čvorova može obraditi velike intervale. Vremenska složenost ista je kao prije: jedna operacija i dalje je $O(\log N)$. Granica $O(q\log N)$ vrlo je labava. U praksi, ako se intervali operacija jako preklapaju, novih će čvorova biti znatno manje; obrnuto, ako svaka operacija zahvaća međusobno disjunktne intervale, broj će se približiti toj granici. Pri inicijalizaciji segment treea prostor treba zauzeti prema toj gornjoj granici.

Dinamičko stvaranje čvorova samo je jedan od načina rješavanja takvih zadataka. Ako su svi krajevi intervala koji se pojavljuju u operacijama poznati unaprijed, mogu se prvo [diskretizirati](../misc/discrete.md) i zatim nad diskretiziranim intervalom izgraditi običan segment tree; učinak je isti, a implementacija jednostavnija. Dinamičko stvaranje čvorova treba razmotriti samo kad operacije nisu poznate unaprijed (npr. kad su prisilno online).

Osim toga, i [perzistentni segment tree](./persistent-seg.md) temelji se na dinamičkom stvaranju čvorova: svaka izmjena stvara nove čvorove samo na jednom putu od korijena do lista, a ostatak dijeli sa starom inačicom, pa svaka izmjena treba samo $O(\log N)$ dodatnog prostora.

### Trajne oznake

Dosad opisane lijene oznake moraju se spuštati. Međutim, svako spuštanje čita i piše djecu, što nije mala konstanta; štoviše, u nekim je situacijama oznake teško spustiti. Da bi se spuštanje izbjeglo, može se koristiti metoda trajnih oznaka (tag permanence): jednom postavljena oznaka ostaje zauvijek na mjestu i više se ne spušta; pri upitu se oznake na putu od korijena do čvora komponiraju i primijene na informaciju pohranjenu u čvoru.

![](images/seg-8.svg)

U skladu s prethodnim dogovorom, oznaka u čvoru $x$ djeluje samo na njegove potomke, a informacija pohranjena u $x$ već uključuje učinak te oznake. Drugim riječima, informacija u $x$ je informacija intervala od $x$ bez uzimanja u obzir oznaka njegovih predaka. Na primjeru rekurzivne implementacije, intervalne operacije segment treea implementiraju se ovako:

-   Intervalna izmjena: rekurzija odozgo prema dolje. Kad se dođe do čvora maksimalnog intervala, u njemu se postavi oznaka, ažurira njegova informacija i odmah se vraća, bez silaska. Pri povratku se iz informacija djece spoji informacija trenutnog čvora i zatim se na nju primijeni oznaka trenutnog čvora.
-   Upit nad intervalom: rekurzija odozgo prema dolje. Kad se dođe do čvora maksimalnog intervala, izravno se vrati njegova pohranjena informacija. Pri povratku se rezultati djece spoje i zatim se na njih primijeni oznaka trenutnog čvora; razinu po razinu prema gore, oznake svih čvorova na putu tako se primijene na rezultat.

Vremenska složenost obiju operacija i dalje je $O(\log N)$, ali bez ikakvog spuštanja, pa je konstanta manja. Nerekurzivna implementacija je slična, samo je rekurzija zamijenjena iteracijom. Referentne implementacije su:

??? example "Referentna implementacija"
    === "Rekurzivna implementacija"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-perm-recursive.cpp:seg-tree"
        ```
    
    === "Nerekurzivna implementacija"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-perm-nonrecursive.cpp:seg-tree"
        ```

Međutim, trajne oznake nisu uvijek izvedive; postavljaju dodatan zahtjev na izmjene. Kompozicija izmjena mora biti **komutativna**. Već smo objasnili da kompozicija lijenih oznaka ne mora biti komutativna, a spuštanje jamči ispravan redoslijed zato što se prije svakog pristupa djetetu oznaka spušta, pa na putu od korijena do lista oznaka bliža korijenu uvijek odgovara kasnijoj operaciji. Trajne oznake upravo odustaju od tog svojstva: oznaka uvijek ostaje gdje jest, položaj joj određuje interval izmjene i ne ovisi o redoslijedu operacija. Stoga oznaka na pretku može biti i ranija i kasnija od oznake na potomku. Pri upitu oznake se komponiraju redom od korijena prema listu, a to daje ispravan rezultat samo ako je kompozicija komutativna.

???+ example "Primjeri"
    Intervalno zbrajanje, množenje i slične operacije komutativne su, pa dopuštaju trajne oznake. Intervalna afina transformacija (tj. istodobno zbrajanje i množenje) i intervalno pridruživanje[^assign] nisu komutativni, pa trajne oznake nisu moguće.

Trajne oznake često se primjenjuju u [perzistentnom segment treeu](./persistent-seg.md) i raznim ugniježđenim stablima (tree-in-tree). U oba je slučaja spuštanje skupo; trajne oznake, ako i nisu nužne, često su prikladniji izbor. U nekim se zadacima oznake uopće ne mogu spustiti (v. primjer „unija površina pravokutnika” u nastavku) i tada su trajne oznake jedini način.

### Binarno pretraživanje na segment treeu

Neki zadaci zahtijevaju binarno pretraživanje nad nizom. Primjerice, za zadani $l$ treba naći najveći $r$ takav da informacija intervala $[l,r]$ zadovoljava neki uvjet. Izravan je pristup binarno pretraživati $r$ i svaki put segment treeom upitati informaciju intervala, što daje složenost $O(\log^2 N)$. Međutim, segment tree sam je po sebi binarna struktura; ako se binarno pretraživanje provede na samom stablu, postiže se $O(\log N)$.

Neka je informacija koju segment tree pohranjuje i dalje $\varphi:\mathcal I\rightarrow M$. Neka je uvjet predikat $g:M\rightarrow\{\text{True},\text{False}\}$ nad prostorom informacija $M$. Da bi binarno pretraživanje imalo smisla, $g$ mora biti **monoton** (u odnosu na spajanje udesno): ako je $g(m)$ laž, onda je za svaki $m'$ i $g(m\circ m')$ laž. Drugim riječima, kad se interval proširi udesno toliko da uvjet više ne vrijedi, uvjet više nikad ne vrijedi. Osim toga, $g(e)$ mora biti istina, tj. prazan interval uvijek zadovoljava uvjet. Zadatak tako postaje: za zadani $l$ naći najveći $r$ takav da je $g(\varphi([l,r]))$ istina; ako je već $g(\varphi([l,l]))$ laž, dogovorno je odgovor $l-1$.

![](images/seg-9.svg)

U rekurzivnoj implementaciji segment treea binarno pretraživanje izvodi se rekurzijom odozgo prema dolje uz održavanje akumulirane informacije $m$, koja predstavlja informaciju dijela intervala već sigurno uključenog u odgovor. Kad rekurzija dođe do čvora čiji interval $I$ cijeli leži u $[l,R]$, prvo pokušamo uključiti cijeli čvor: izračunamo $m\circ\varphi(I)$; ako je $g$ i dalje istina, cijeli se čvor može uključiti, pa ažuriramo $m$ i vratimo desni kraj čvora; inače se granica odgovora nalazi unutar tog čvora i treba nastaviti rekurziju prema dolje. Ako ni u listu uvjet nije zadovoljen, granica je upravo tu.

Složenost je i dalje $O(\log N)$. Naime, u rekurziji prema dolje nastavljaju samo dvije vrste čvorova: oni čiji interval izlazi iz $[l,R]$ – svi leže na putu od korijena do $l$ – i oni čije bi uključivanje učinilo $g$ lažnim – među njima stvarno silaze samo čvorovi na putu na kojem leži granica, najviše jedan po razini. Obje vrste imaju samo $O(\log N)$ čvorova, a ostali se čvorovi ili uključe cijeli ili preskoče cijeli.

![](images/seg-10.svg)

Nerekurzivna implementacija dijeli postupak na dvije faze. Prvo odozdo prema gore: od lista za $l$ skačemo prema gore dok je trenutni čvor lijevo dijete, sve dok ne postane desno dijete; tada je lijevi kraj njegova intervala poravnat s još neuključenim dijelom, pa pokušamo uključiti cijeli čvor; ako uspije, pomaknemo se za jedan čvor udesno i nastavimo skakati prema gore. Čim uključivanje nekog čvora učini $g$ lažnim, prelazimo na silazak odozgo prema dolje: unutar tog čvora se spuštamo i na svakoj razini prvo pokušamo uključiti lijevo dijete; ako uspije, prelazimo u desno dijete, a ako ne, ulazimo u lijevo, sve do lista – to je granica. Svaka faza prolazi jedan put, pa je složenost također $O(\log N)$.

Simetrično, može se za zadani $r$ tražiti najmanji $l$ takav da je $g(\varphi([l,r]))$ istina. Tada akumuliranu informaciju treba spajati zdesna nalijevo, tj. računati $\varphi(I)\circ m$, da bi redoslijed spajanja bio ispravan; kad nema rješenja, dogovorno je odgovor $r+1$. Pri tome $g$ mora biti monoton u odnosu na spajanje ulijevo: ako je $g(m)$ laž, onda je za svaki $m'$ i $g(m'\circ m)$ laž.

??? example "Referentna implementacija"
    === "Rekurzivna implementacija"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-bisect-recursive.cpp:max-right"
        --8<-- "docs/ds/code/seg/seg-bisect-recursive.cpp:min-left"
        ```
    
    === "Nerekurzivna implementacija"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-bisect-nonrecursive.cpp:max-right"
        --8<-- "docs/ds/code/seg/seg-bisect-nonrecursive.cpp:min-left"
        ```

???+ tip "Savjet"
    1.  S lijenim oznakama prije silaska u djecu također treba spustiti oznake. U nerekurzivnoj implementaciji prije faze skakanja prema gore treba jednom spustiti oznake duž puta od korijena do $l$.
    2.  Ako uvjet ovisi samo o informaciji samog trenutnog čvora (npr. „postoji li u intervalu element veći od $x$”), akumuliranu informaciju ne treba održavati i implementacija je jednostavnija.
    3.  U nerekurzivnoj implementaciji suvišni listovi pohranjuju neutralni element, na kojem je $g$ uvijek istina, pa faza skakanja prema gore može proći preko njih. Tada treba izravno vratiti $R$, a ne položaj računati iz oznake čvora.

### Segment tree nad vrijednostima

Dosadašnji segment treeovi građeni su nad indeksima niza. Međutim, segment treeu nije važno značenje indeksa. Ako ga izgradimo nad domenom vrijednosti, tj. ako list koji odgovara elementu $v$ bilježi koliko se puta vrijednost $v$ pojavljuje u multiskupu, dobivamo **segment tree nad vrijednostima** (vrijednosni segment tree; kin. 权值线段树).

![](images/seg-11.svg)

Takav se segment tree može koristiti kao skup koji podržava uobičajene operacije [balansiranog stabla](./bst.md), a sve se one izravno dobivaju iz već opisanih operacija:

-   Umetanje elementa $v$ je uvećanje za jedan na položaju $v$.
-   Brisanje elementa $v$ je umanjenje za jedan na položaju $v$; treba provjeriti postoji li element.
-   Upit za rang od $v$ je upit za zbroj intervala vrijednosti $[L,v-1]$ uvećan za jedan.
-   Upit za $k$-ti najmanji element: binarnim pretraživanjem na segment treeu nađe se najveći $r$ takav da je broj elemenata u intervalu vrijednosti $[L,r]$ manji od $k$; tada je $r+1$ traženi element. Budući da se brojevi mogu oduzimati, pri silasku je dovoljno usporediti broj u lijevom djetetu s $k$, bez održavanja akumulirane informacije.
-   Upit za prethodnik i sljedbenik može se izvesti pomoću operacija ranga i $k$-tog najmanjeg elementa.

U usporedbi s uobičajenim balansiranim stablima, segment tree nad vrijednostima mnogo je jednostavniji za implementaciju i ima manju konstantu; cijena je da može obrađivati samo elemente iz domene vrijednosti i ne podržava operacije poput okretanja intervala koje ovise o samoj strukturi stabla.

Budući da je domena vrijednosti obično mnogo veća od broja elemenata, izravna izgradnja često nije izvediva. Ako su svi elementi poznati unaprijed, domenu vrijednosti treba [diskretizirati](../misc/discrete.md) i izgraditi običan segment tree; inače treba dinamičko stvaranje čvorova. U potonjem je slučaju informacija čvorova za vrijednosti koje se ne pojavljuju upravo neutralni element – upravo najjednostavniji gore opisani slučaj.

??? example "Referentna implementacija"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-as-bst.cpp:seg-tree"
    ```

Segment tree nad vrijednostima najčešća je podloga za proširenja poput [perzistentnog segment treea](./persistent-seg.md) i spajanja segment treeova. Prvi omogućuje upit za $k$-ti najmanji element u intervalu niza, a drugi učinkovito spajanje dvaju skupova.

## Proširenja

Segment tree ima vrlo široku primjenu; uobičajena proširenja i inačice su:

-   [perzistentni segment tree](./persistent-seg.md)
-   razna ugniježđena stabla:
    -   [segment tree u segment treeu](./seg-in-seg.md)
    -   [segment tree u Fenwick treeu](./seg-in-bit.md)
    -   [balansirano stablo u segment treeu](./balanced-in-seg.md)
    -   [segment tree u balansiranom stablu](./seg-in-balanced.md)
-   [Li Chao tree](./li-chao-tree.md)
-   [cat tree](./cat-tree.md)
-   [Segment Tree Beats](./seg-beats.md)

Detalje potražite na odgovarajućim stranicama.

## Primjeri zadataka

Dosad smo opisali osnovna načela segment treea i dali nekoliko predložaka. Međutim, implementacija segment treea vrlo je fleksibilna. Referentne implementacije u ovom odjeljku ne drže se strogo predložaka.

???+ example "[Library Checker - Point Add Range Sum](https://judge.yosupo.jp/problem/point_add_range_sum)"
    Zadan je niz. Treba izvoditi sljedeće operacije:
    
    -   uvećaj $p$-ti broj za $x$;
    -   izračunaj zbroj elemenata u intervalu $[l,r)$.

??? note "Rješenje"
    Dovoljno je implementirati segment tree s izmjenom jednog elementa i upitom nad intervalom.
    
    === "Implementacija 1"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-2.cpp"
        ```
    
    === "Implementacija 2"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-3.cpp"
        ```

???+ example "[Luogu P3372【模板】线段树 1](https://www.luogu.com.cn/problem/P3372)"
    Zadan je niz. Treba izvoditi sljedeće dvije operacije:
    
    -   svakom broju u nekom intervalu dodaj $k$;
    -   izračunaj zbroj brojeva u nekom intervalu.

??? note "Rješenje"
    Dovoljno je implementirati segment tree s intervalnom izmjenom i upitom nad intervalom. Napomena: za intervalno zbrajanje treba održavati duljinu trenutnog intervala kao dio informacije ili je pri izmjeni izračunati iz krajeva intervala.
    
    === "Implementacija 1"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-5.cpp"
        ```
    
    === "Implementacija 2"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-4.cpp"
        ```

???+ example "[Luogu P3373【模板】线段树 2](https://www.luogu.com.cn/problem/P3373)"
    Zadan je niz. Treba izvoditi sljedeće tri operacije:
    
    -   svaki broj u nekom intervalu pomnoži s $x$;
    -   svakom broju u nekom intervalu dodaj $x$;
    -   izračunaj zbroj brojeva u nekom intervalu.

??? note "Rješenje"
    Dovoljno je implementirati segment tree s intervalnom izmjenom i upitom nad intervalom. Može se izravno implementirati intervalna afina transformacija, koja istodobno podržava zbrajanje i množenje. Ako se koriste dvije lijene oznake, jedna za zbrajanje i jedna za množenje, treba paziti na redoslijed njihova spuštanja.
    
    === "Implementacija 1"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-7.cpp"
        ```
    
    === "Implementacija 2"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-6.cpp"
        ```

???+ example "[SPOJ GSS3 - Can you answer these queries III](https://www.spoj.com/problems/GSS3/)"
    Zadan je niz. Treba izvoditi sljedeće operacije:
    
    -   postavi $x$-ti broj na $y$;
    -   izračunaj najveći neprazni zbroj podintervala intervala $[x,y]$.

??? note "Rješenje"
    Dovoljno je implementirati segment tree s izmjenom jednog elementa i upitom nad intervalom. Način održavanja najvećeg nepraznog zbroja podintervala analiziran je [ranije](#informacija-o-intervalu). U ovom zadatku spajanje informacija nije komutativno, pa pri implementaciji treba paziti na redoslijed spajanja.
    
    ```cpp
    --8<-- "docs/ds/code/seg/seg-1.cpp"
    ```

???+ example "[Luogu P13825【模板】线段树 1.5](https://www.luogu.com.cn/problem/P13825)"
    Niz $\{a_i\}$ duljine $n\le 10^9$ na početku je $a_i = i$. Treba izvoditi sljedeće operacije:
    
    -   svakom broju u nekom intervalu dodaj $k$;
    -   izračunaj zbroj brojeva u nekom intervalu.

??? note "Rješenje"
    Budući da je $n$ prevelik, stablo se ne može izravno izgraditi; treba dinamičko stvaranje čvorova. Osim toga, informacija još neizmijenjenog intervala nije neutralni element, pa se informacija praznog čvora računa iz krajeva njegova intervala, a i pri stvaranju novog čvora treba je tako inicijalizirati. To znači da pri spuštanju oznaka i spajanju informacija djece treba prenositi krajeve trenutnog intervala.
    
    U ovom se zadatku zapravo doprinos početnih vrijednosti može izračunati zasebno, a segment tree održava samo prirast svakog elementa. Tada je zbroj prirasta praznog čvora $0$, upravo neutralni element, pa pri stvaranju čvorova i spajanju informacija krajeve intervala više ne treba uzimati u obzir; međutim, pri intervalnom zbrajanju i dalje treba znati duljinu intervala, pa je ona dostupna samo kao parametar rekurzije i ne može se uključiti u informaciju.
    
    Budući da zadatak nije prisilno online, mogu se i sve operacije prvo spremiti, krajevi diskretizirati i zatim upotrijebiti običan segment tree. Nakon diskretizacije svaki list odgovara neprekinutom intervalu izvornog niza, pa mu informaciju treba inicijalizirati prema duljini i zbroju elemenata tog intervala.
    
    === "Implementacija 1"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-8.cpp"
        ```
    
    === "Implementacija 2"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-9.cpp"
        ```
    
    === "Implementacija 3"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-10.cpp"
        ```

???+ example "[Luogu P5490【模板】扫描线 & 矩形面积并](https://www.luogu.com.cn/problem/P5490)"
    Izračunaj površinu unije $n$ pravokutnika sa stranicama paralelnima koordinatnim osima.

??? note "Rješenje"
    Ovo je predložak za [sweep line](../geometry/scanning.md#unija-površina-pravokutnika-u-ravnini). Za detalje pretvorbe zadatka pomoću sweep linea pogledajte navedenu stranicu; ovdje raspravljamo samo o strukturi podataka nakon pretvorbe. Treba održavati strukturu koja podržava intervalno uvećanje i umanjenje broja pokrivanja: svaka operacija nekom intervalu uveća ili umanji broj pokrivanja za jedan, a svaki upit traži ukupnu duljinu položaja čiji je broj pokrivanja barem jedan.
    
    Razmotrimo implementaciju tih intervalnih operacija segment treeom. Prirodna je ideja u svakom čvoru održavati broj pokrivanja intervala i ukupnu duljinu dijela pokrivenog barem jednom. Međutim, kad je interval cijeli pokriven, informacija o pokrivenosti pojedinih podintervala gubi se iz ukupne duljine, pa se nakon uklanjanja tog sloja ne može obnoviti. Rješenje je dvije vrste operacija bilježiti odvojeno: broj pokrivanja uključuje samo operacije koje pokrivaju točno cijeli interval, a ukupna duljina samo pokrivanja zabilježena u potomcima. Tada je stvarno pokrivena duljina intervala: duljina intervala kad je broj pokrivanja veći od nule, inače zabilježena ukupna duljina. Pri spajanju se zbroje stvarno pokrivene duljine obaju djece i to je ukupna duljina ovog čvora. Time se broj pokrivanja više ne može spuštati, jer dodavanje i uklanjanje istog pokrivanja padaju na isti skup čvorova i samo ako broj ostaje na mjestu mogu se međusobno poništiti. To su upravo trajne oznake.
    
    Naravno, zadatak se može riješiti i gornjim predloškom segment treea. Dovoljno je kao informaciju intervala uzeti najmanji broj pokrivanja u intervalu i ukupnu duljinu dijela na kojem se taj minimum postiže. Lako se provjeri da je takav prostor informacija monoid, a uvećanje i umanjenje broja pokrivanja njegov endomorfizam, pa se intervalna izmjena i upit mogu preuzeti iz predloška. Ukupna pokrivena duljina dobiva se tako da se od duljine cijelog intervala oduzme duljina dijela s brojem pokrivanja nula; potonja je zabilježena duljina ako je najmanji broj pokrivanja nula, a inače nula.
    
    === "Implementacija 1"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-11.cpp"
        ```
    
    === "Implementacija 2"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-12.cpp"
        ```

???+ example "[Luogu P2894【USACO08FEB】Hotel G](https://www.luogu.com.cn/problem/P2894)"
    Postoji $n$ soba, na početku sve prazne. Treba izvoditi sljedeće operacije:
    
    -   nađi $x$ uzastopnih praznih soba; ako postoje, useli goste u njih;
    -   sobe $[x,x+y-1]$ se isele.
    
    Pri svakoj prvoj operaciji ispiši najmanji broj sobe među $x$ uzastopnih praznih soba; ako ne postoje, vrati $0$.

??? note "Rješenje"
    Izgradimo segment tree koji za svaki interval održava najveću duljinu uzastopnih praznih soba. Za spajanje te informacije treba održavati i najdulji prazan prefiks, najdulji prazan sufiks i duljinu intervala: uzastopne prazne sobe preko sredine upravo su najdulji sufiks lijevog podintervala nadovezan na najdulji prefiks desnog. Lijena oznaka treba samo intervalno pridruživanje, tj. postavljanje cijelog intervala na prazno ili zauzeto; slučaj bez izmjene bilježi se posebnom vrijednošću (npr. $-1$). Za najmanji dostupni broj sobe dovoljno je naći najmanji $r$ takav da najveća duljina uzastopnih praznih soba u $[1,r]$ nije manja od $x$; broj sobe je tada $r-x+1$. To se izvodi binarnim pretraživanjem na segment treeu.
    
    ```cpp
    --8<-- "docs/ds/code/seg/seg-13.cpp"
    ```

???+ example "[Luogu P1168 中位数](https://www.luogu.com.cn/problem/P1168)"
    Zadan je niz duljine $n$. Za svaki neparan $i\le n$ ispiši medijan prvih $i$ brojeva.

??? note "Rješenje"
    Medijan ovisi samo o odnosu veličina elemenata, a ne o njihovu položaju u nizu, pa se može održavati segment treeom nad vrijednostima. Elementi se redom umeću, a nakon svakog neparnog broja umetnutih elemenata postavlja se upit za $(i+1)/2$-ti najmanji element. Dovoljno je implementirati umetanje i upit za $k$-ti najmanji element.
    
    ```cpp
    --8<-- "docs/ds/code/seg/seg-14.cpp"
    ```

## Zadaci za vježbu

Osnovna implementacija i oblikovanje informacije o intervalu:

-   [Luogu P2574 XOR 的艺术](https://www.luogu.com.cn/problem/P2574)
-   [Luogu P4588【TJOI2018】数学计算](https://www.luogu.com.cn/problem/P4588)
-   [Luogu P1253 扶苏的问题](https://www.luogu.com.cn/problem/P1253)
-   [Luogu P1471 方差](https://www.luogu.com.cn/problem/P1471)
-   [Luogu P4513 小白逛公园](https://www.luogu.com.cn/problem/P4513)
-   [Luogu P2572【SCOI2010】序列操作](https://www.luogu.com.cn/problem/P2572)

Dinamičko stvaranje čvorova:

-   [Codeforces 915 E. Physical Education Lessons](https://codeforces.com/problemset/problem/915/E)
-   [Library Checker - Range Affine Range Sum (Large Array)](https://judge.yosupo.jp/problem/range_affine_range_sum_large_array)
-   [Codeforces 817 F. MEX Queries](https://codeforces.com/problemset/problem/817/F)

Trajne oznake:

-   [Luogu P1502 窗口的星星](https://www.luogu.com.cn/problem/P1502)
-   [2018 Multi-University Training Contest 5 G. Glad You Came](https://acm.hdu.edu.cn/showproblem.php?pid=6356)

Binarno pretraživanje na segment treeu:

-   [AtCoder Library Practice Contest J - Segment Tree](https://atcoder.jp/contests/practice2/tasks/practice2_j)
-   [AtCoder Beginner Contest 292 Ex - Rating Estimator](https://atcoder.jp/contests/abc292/tasks/abc292_h)
-   [Luogu P4137 Rmq Problem/mex](https://www.luogu.com.cn/problem/P4137)
-   [Codeforces 773 E. Blog Post Rating](https://codeforces.com/problemset/problem/773/E)
-   [Codeforces 407 E. k-d-sequence](https://codeforces.com/problemset/problem/407/E)
-   [Codeforces 671 E. Organizing a Race](https://codeforces.com/problemset/problem/671/E)

Segment tree nad vrijednostima:

-   [Luogu P1908 逆序对](https://www.luogu.com.cn/problem/P1908)
-   [Luogu P1801 黑匣子](https://www.luogu.com.cn/problem/P1801)
-   [Luogu P1637 三元上升子序列](https://www.luogu.com.cn/problem/P1637)
-   [Luogu P2286【HNOI2004】宠物收养场](https://www.luogu.com.cn/problem/P2286)

## Primjena: optimizacija izgradnje grafa segment treeom

Pri izgradnji grafa katkad nailazimo na zadatke u kojima jedan vrh treba spojiti bridovima sa svim vrhovima nekog neprekinutog intervala ili neprekinuti interval vrhova s jednim vrhom. Kad bismo bridove stvarno dodavali jedan po jedan, složenost bi eksplodirala čim vrhova ima mnogo; tu intervalno svojstvo segment treea optimizira izgradnju grafa.

Slijedi segment tree.

![](./images/segt5.svg)

Svaki čvor predstavlja interval; pretpostavimo da treba spojiti bridovima s intervalom $[2, 4]$.

![](./images/segt6.svg)

U nekim se zadacima pojavljuje i slučaj kad interval treba spojiti s jednim vrhom; tada se samo obrnu svi usmjereni bridovi na prvoj slici. Gornje stablo zovemo ulaznim stablom, a ovo dolje izlaznim.

![](./images/segt7.svg)

???+ note "[Legacy](https://codeforces.com/problemset/problem/786/B)"
    Sažetak zadatka: zadano je $n$ vrhova i $q$ operacija. Svaka je operacija jednog od tri tipa:
    
    -   tip 1: dodaj usmjereni brid $u \rightarrow v$ težine $w$;
    -   tip 2: za sve $i \in [l,r]$ dodaj usmjereni brid $u \rightarrow i$ težine $w$;
    -   tip 3: za sve $i \in [l,r]$ dodaj usmjereni brid $i \rightarrow u$ težine $w$.
    
    Izračunaj najkraće puteve od vrha $s$ do ostalih vrhova.
    
    $1 \le n,q \le 10^5, 1 \le w \le 10^9$.
    
    ??? note "Primjer koda"
        ```cpp
        --8<-- "docs/ds/code/seg/seg_8.cpp"
        ```

## Literatura i bilješke

-   [统计的力量 – Zhang Kunwei (kineski)](https://github.com/hzwer/shareOI/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/%E7%BB%9F%E8%AE%A1%E7%9A%84%E5%8A%9B%E9%87%8F%E2%80%94%E2%80%94%E7%BA%BF%E6%AE%B5%E6%A0%91%E5%85%A8%E6%8E%A5%E8%A7%A6_%E5%BC%A0%E6%98%86%E7%8E%AE.pptx)
-   [Generalizing Segment Trees by Eklavya](https://sharmaeklavya2.github.io/blog/generalizing-segment-trees.html)
-   [线段树进阶 Part 1 by Alex\_Wei – Luogu (kineski)](https://www.luogu.com.cn/article/r1mp3hga)

[^monoid]: Strogo govoreći, informacija koju segment tree održava treba činiti samo polugrupu; postojanje neutralnog elementa nije nužno. Rekurzivna implementacija koristi neutralni element obično zato što ga upit nad intervalom uzima kao početnu vrijednost akumulirane informacije; to se može izbjeći razlikovanjem slučajeva prema presjeku. Međutim, suvišni listovi u nerekurzivnoj implementaciji i prazni čvorovi pri dinamičkom stvaranju čvorova ne mogu zaobići neutralni element. U krajnjem slučaju, čak i kad je nužan, polugrupi $S$ uvijek se može dodati element $e$ i propisati da je rezultat operacije $e$ s bilo kojim elementom taj element, čime se dobiva monoid $S\cup\{e\}$. Radi jednostavnosti izlaganja u ovom se članku uvijek pretpostavlja da se održava informacija s strukturom monoida.

[^endo]: Slično raspravi o informaciji intervala, u mnogim implementacijama neutralni element nikad nije ulaz izmjene, pa ovo svojstvo nije potrebno; dovoljno je da izmjena bude endomorfizam polugrupe. Međutim, u nerekurzivnoj implementaciji trajnih oznaka u nastavku početna vrijednost akumulirane informacije upravo je neutralni element i na nju se razinu po razinu primjenjuju oznake s puta, pa se ovo svojstvo ne smije zanemariti. Radi jednostavnosti izlaganja u ovom se članku uvijek pretpostavlja da je izmjena endomorfizam monoida.

[^child-id]: Zapravo, kad se čvorovi označavaju u preorder redoslijedu kao na slici, oznaka desnog djeteta može se izračunati iz oznake trenutnog čvora i veličine lijevog podstabla, a veličina lijevog podstabla iz duljine intervala. Budući da se pri rekurzivnom pristupu čvorovima segment treea obično održavaju krajevi intervala, i oznaka desnog djeteta može se izravno izračunati.

[^heap-size]: Promotrimo omjer prostora $2^{\lceil\log_2N\rceil+1}$ koji zauzima binarno stablo i veličine $N$ segment treea. Prvi ovisi samo o visini binarnog stabla. Kad je visina segment treea $k$, najmanja je veličina segment treea $N = 2^{k-1}+1$. Odgovarajući omjer je $(4N-4)/N = 4 - 4/N$, sa supremumom $4$. Zato za pohranu segment treea veličine $N$ odgovarajuće savršeno binarno stablo treba niz veličine $4N$.

[^assign]: Intervalno pridruživanje samo po sebi nije komutativno. Ako se uz pridruživanje bilježi i vremenska oznaka $t$ te se propiše da je kompozicija oznaka $(v_1,t_1)$ i $(v_2,t_2)$ ona s većom vremenskom oznakom, dobiva se komutativna oznaka. Tom se metodom može implementirati segment tree s trajnim oznakama koji podržava intervalno pridruživanje i upit za jedan element: pri upitu se duž puta uzme oznaka s najvećom vremenskom oznakom i primijeni na list. Međutim, upit nad intervalom nije moguć, jer $(v,t)$ nije endomorfizam prostora informacija: iz informacije o intervalu ne može se saznati koji su položaji već prekriveni kasnijim pridruživanjem.
