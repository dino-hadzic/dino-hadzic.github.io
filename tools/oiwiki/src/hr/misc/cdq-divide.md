---
title: CDQ podjela
---

Ova stranica predstavlja CDQ podjelu (CDQ divide and conquer).

## Uvod

CDQ podjela je ideja, a ne konkretan algoritam, slično kao [dinamičko programiranje](../dp/index.md). Ta se ideja danas vrlo široko proširila i prema načelu rada i načinu pisanja grubo se dijeli na tri vrste:

-   rješavanje zadataka o parovima točaka;
-   optimizacija i prijelazi 1D dinamičkog programiranja;
-   pretvaranje nekih dinamičkih problema u statičke pomoću CDQ podjele.

Ideju CDQ podjele prva je još u srednjoj školi uredila i sažela Chen Danqi (陈丹琦), osvajačica zlatne medalje na IOI-ju 2008., pa je po njoj i dobila ime.[^ref1]

## Rješavanje zadataka o parovima točaka

Zadaci ovog tipa većinom nalikuju na „zadan je niz duljine $n$, prebroji parove točaka $(i,j)$ s određenim svojstvima” ili „zadan je niz duljine $n$, pronađi par točaka $(i,j)$ koji maksimizira vrijednost neke funkcije”.

Tijek algoritma kojim CDQ podjela rješava takve zadatke je sljedeći:

1.  pronađemo sredinu niza $mid$;

2.  sve parove točaka $(i,j)$ podijelimo u 3 vrste:

    1.  parove s $1 \leq i \leq mid,1 \leq j \leq mid$;
    2.  parove s $1  \leq i \leq mid ,mid+1 \leq j \leq n$;
    3.  parove s $mid+1 \leq  i \leq n,mid+1 \leq j \leq n$.

3.  niz $(1,n)$ razdvojimo na dva niza $(1,mid)$ i $(mid+1,n)$. Tada se parovi prve i treće vrste nalaze unutar tih dvaju nizova;

4.  rekurzivno obradimo te dvije vrste parova;

5.  smislimo način za obradu parova druge vrste.

Vidimo da je ideja CDQ podjele neprestano rekurzivno raspodjeljivati parove točaka na lijevi i desni interval.

U praksi obično koristimo funkciju `solve(l,r)` koja obrađuje parove s $l \leq i \leq r,l \leq j \leq r$. Rekurzivni dio gornjeg tijeka algoritma ostvaruje se pozivima `solve(l,mid)` i `solve(mid+1,r)`. Za preostale parove druge vrste treba dodatno osmisliti algoritam.

### Primjeri zadataka

???+ example "[三维偏序 (Trodimenzionalni parcijalni uređaj)](https://www.luogu.com.cn/problem/P3810)"
    Zadan je niz u kojem svaka točka ima tri svojstva $a_i,b_i,c_i$. Odredite koliko parova točaka $(i,j)$ u tom nizu zadovoljava $a_j \leq a_i$ i $b_j \leq b_i$ i $c_j \leq c_i$ i $j \ne i$.

??? note "Ideja rješenja"
    Trodimenzionalni parcijalni uređaj klasičan je zadatak za CDQ podjelu.
    
    Zadatak traži da prebrojimo parove točaka u nizu, pa pokušajmo s CDQ podjelom.
    
    Najprije niz sortiramo po $a$.
    
    Pretpostavimo da smo već napisali `solve(l,r)` i da smo rekurzijom riješili `solve(l,mid)` i `solve(mid+1,r)`. Sada moramo prebrojati koliko parova točaka $(i,j)$ s $l \leq i \leq mid$, $mid+1 \leq j \leq r$ još zadovoljava i ograničenja $a_{i} \leq a_{j}$, $b_{i} \leq b_{j}$, $c_{i} \leq c_{j}$.
    
    Nakon kratkog razmišljanja uočavamo da ograničenje $a_{i} \leq a_{j}$ više ničemu ne služi: budući da je $i$ manji od $mid$, a $j$ veći od $mid$, $i$ je sigurno manji od $j$; a kako je niz već sortiran po $a$, nužno vrijedi $a_{i} \leq a_{j}$. Preostaju još dva ograničenja: $b_{i} \leq b_{j}$ i $c_{i} \leq c_{j}$. Prema njima možemo iterirati po $j$ i odrediti koliko $i$ zadovoljava uvjete.
    
    Radi lakšeg iteriranja, sve točke u $(l,mid)$ i $(mid+1,r)$ sortiramo uzlazno po vrijednosti $b$. Zatim redom prolazimo kroz svaki $j$ i sve točke $i$ s $b_{i} \leq b_{j}$ ubacujemo u neku strukturu podataka (ovdje biramo [Fenwick tree](../ds/fenwick.md)). Tada je dovoljno upitati koliko točaka u Fenwick treeju ima vrijednost $c$ manju ili jednaku $c_{j}$ i dobili smo koliko $i$ se može valjano upariti s tom točkom $j$.
    
    Kad ubacujemo točku čija je vrijednost $c$ jednaka $x$, na poziciji $x$ Fenwick treeja povećamo vrijednost za jedan, a upit koliko točaka u Fenwick treeju ima vrijednost manju od $x$ zapravo je računanje [prefiksne sume](../basic/prefix-sum.md); ako smo unaprijed [diskretizirali](../misc/discrete.md) sve vrijednosti $c$, složenost je ispravna.
    
    Za svaki $j$ moramo u Fenwick tree ubaciti sve točke $i$ s $b_{i} \leq b_{j}$. Budući da su svi $i$ i $j$ već unaprijed sortirani po vrijednosti $b$, dovoljno je točke ubacivati u Fenwick tree tehnikom dvostrukih pokazivača (two pointers), čime broj umetanja u Fenwick tree pada s $O(n^2)$ na $O(n)$.
    
    Ovakvim tijekom algoritma informacije o parovima druge vrste obradili smo u vremenu $O(n\log n)$. Ukupna vremenska složenost algoritma tada je $T(n)=T(\lfloor \frac{n}{2} \rfloor)+T(\lceil \frac{n}{2} \rceil)+O(n\log n)=O(n\log^2n)$.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/cdq-divide/cdq-divide_1.cpp"
    ```

???+ example "[CQOI2011 动态逆序对 (Dinamičke inverzije)](https://www.luogu.com.cn/problem/P3157)"
    Za niz $a$ broj inverzija definiran je kao broj elemenata skupa $\{(i,j)| i < j \wedge a_i > a_j \}$.
    
    Zadana je permutacija brojeva $1\sim n$ iz koje se nekim redoslijedom redom briše $m$ elemenata. Vaš je zadatak prije svakog brisanja elementa izračunati broj inverzija cijelog niza.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/cdq-divide/cdq-divide_2.cpp"
    ```

## Optimizacija prijelaza 1D/1D dinamičkog programiranja CDQ podjelom

Povezani sadržaj: [optimizacija DP-a CDQ podjelom](../dp/opt/dp-opt.md#optimizacija-dp-a-cdq-podjelom)

1D/1D dinamičko programiranje označava posebnu klasu DP zadataka kod kojih je DP polje jednodimenzionalno, a prijelaz je $O(n)$. Ako su uvjeti povoljni, ponekad se CDQ podjelom njihova vremenska složenost može smanjiti s $O(n^2)$ na $O(n\log^2n)$.

Na primjer, zadan je niz u kojem svaki element ima dva svojstva $a$, $b$. Želimo izračunati vrijednost DP izraza čija je jednadžba prijelaza sljedeća:

$dp_{i}=1+ \max_{j=1}^{i-1}dp_{j}[a_{j} < a_{i}][b_{j} < b_{i}]$

To je DP jednadžba dvodimenzionalnog najduljeg rastućeg podniza, tj. samo točke $j$ s $j < i,a_{j} < a_{i},b_{j} < b_{i}$ mogu ažurirati DP vrijednost točke $i$.

Izravan prijelaz očito je $O(n^2)$. Slijedi objašnjenje kako se postupak prijelaza optimizira CDQ podjelom.

Primjećujemo da je i odnos prijelaza iz $dp_{j}$ u $dp_{i}$ odnos između parova točaka, pa ga obrađujemo na način sličan onome kojim CDQ podjela obrađuje odnose među parovima točaka.

Taj je postupak prijelaza prilično shematičan. Pretpostavimo da je interval koji trenutno obrađujemo $(l,r)$; tijek algoritma otprilike je sljedeći:

1.  ako je $l=r$, dio $\max$ vrijednosti $dp_{r}$ već je izračunat, pa samo postavimo $dp_{r} \gets dp_{r} + 1$ i vratimo se;
2.  rekurzivno pozovemo `solve(l,mid)`;
3.  obradimo sve odnose prijelaza s $l \leq j \leq mid$, $mid+1 \leq i \leq r$;
4.  rekurzivno pozovemo `solve(mid+1,r)`.

Treći korak radi se gotovo jednako kao kod CDQ podjele za trodimenzionalni parcijalni uređaj. Pri obradi odnosa prijelaza s $l \leq j \leq mid$, $mid+1 \leq i \leq r$ uočavamo da se više ne moramo brinuti o ograničenju $j < i$. Stoga i dalje sve točke $i$ i $j$ najprije sortiramo po vrijednosti $a$, zatim tehnikom dvostrukih pokazivača točke $j$ ubacujemo u Fenwick tree i na kraju upitom za prefiksni maksimum ažuriramo $dp_{i}$.

### Dokaz ispravnosti postupka prijelaza

Najveća razlika između ovog načina pisanja CDQ-a i onoga za obradu odnosa među parovima točaka jest dio u kojem se obrađuju parovi s $l \leq j \leq mid$, $mid+1 \leq i \leq r$. Kod CDQ-a za odnose među parovima točaka taj se dio može staviti bilo gdje. No kad CDQ podjelom optimiziramo DP, taj postupak mora biti umetnut između $solve(l,mid)$ i $solve(mid+1,r)$. Razlog je to što su DP prijelazi **uređeni** i moraju zadovoljavati dva uvjeta, inače nisu ispravni:

1.  sve vrijednosti $dp_{j}$ koje se koriste za izračun $dp_{i}$ moraju već biti do kraja izračunate, ne smije postojati „poluproizvod”;

2.  sve vrijednosti $dp_{j}$ koje se koriste za izračun $dp_{i}$ moraju ažurirati $dp_{i}$, ne smije postojati vrijednost $dp_{j}$ koja ga nije ažurirala.

Ta su dva uvjeta kod $O(n^2)$ grube sile vrlo lako zadovoljena, ali nakon primjene CDQ podjele redoslijed prijelaza očito je ispremiješan, pa je potrebno ispitati ispravnost prijelaza.

Rekurzivno stablo CDQ podjele prikazano je u nastavku.

![Rekurzivno stablo CDQ podjele](./images/cdq-divide.svg)

Ako izvedemo upravo opisani algoritam, uzmimo za primjer točku $8$: njezina DP vrijednost dovršava se u 3 funkcije, `solve(1,8)`, `solve(5,8)`, `solve(7,8)`, a točke koje je ta tri puta ažuriraju redom su tri disjunktna intervala $(1,4)$, $(5,6)$, $(7,7)$; uzmimo zatim za primjer točku $5$: njezina se DP vrijednost rješava u funkciji `solve(1,4)`, a interval koji je ažurira je $(1,4)$. Pažljivim promatranjem uočavamo da se DP vrijednost točke $i$ ažurira $\log$ puta i da su intervali koji je ažuriraju upravo onih $\log$ intervala na koje se $(1,i)$ rastavlja u segment treeju. Dakle, doista smo osigurali da je svaki valjani $j$ ažurirao točku $i$, pa je 2. uvjet zadovoljen.

Analizirajmo zatim tijek izvođenja našeg algoritma:

1.  prva funkcija koja završava je `solve(1,1)`. Tada uočavamo da je vrijednost $dp_{1}$ već izračunata;
2.  prva funkcija koja izvodi postupak prijelaza je `solve(1,2)`. Tada uočavamo da je vrijednost $dp_{2}$ već prenesena;
3.  druga funkcija koja završava je `solve(2,2)`. Tada uočavamo da je vrijednost $dp_{2}$ već izračunata;
4.  zatim završava `solve(1,2)` i sve vrijednosti $dp$ na intervalu $(1,2)$ su izračunate;
5.  sljedeća funkcija koja izvodi postupak prijelaza je `solve(1,4)`. Nakon tog prijelaza uočavamo da je vrijednost $dp_{3}$ već prenesena;
6.  sljedeća funkcija koja završava je `solve(3,3)`. Uočavamo da je dp vrijednost $dp_{3}$ izračunata;
7.  sljedeći prijelaz koji se izvodi je `solve(3,4)`. Tada je $dp_{4}$ u `solve(1,4)` jednom preneseno iz $(1,2)$, a sada još i iz $(3,3)$, pa je i vrijednost $dp_{4}$ prenesena;
8.  `solve(4,4)` završava, vrijednost $dp_{4}$ je izračunata;
9.  `solve(3,4)` završava, vrijednosti na $(3,4)$ su izračunate;
10. `solve(1,4)` završava, vrijednosti na $(1,4)$ su izračunate.
11. …

Simulirajući tijek funkcija uočavamo jedno: svaki put kad `solve(l,r)` završi, sve DP vrijednosti na intervalu $(l,r)$ su do kraja izračunate. Budući da je svaki put kad izvodimo funkciju prijelaza `solve(l,mid)` već završio, svaki postupak prijelaza koji izvodimo je valjan, pa je 1. uvjet zadovoljen.

U upravo opisanom postupku uočili smo: ako rekurzivno stablo CDQ podjele promatramo kao segment tree, CDQ podjela je **funkcija inorder obilaska** tog segment treeja, pa smo zapravo sve DP vrijednosti obradili redom, samo je redoslijed prijelaza rastavljen; stoga je algoritam ispravan.

### Primjeri zadataka

???+ example "[SDOI2011 拦截导弹 (Presretanje projektila)](https://www.luogu.com.cn/problem/P2487)"
    Neka je država, radi obrane od raketnih napada neprijateljske države, razvila sustav za presretanje projektila. No taj sustav ima manu: iako njegov prvi projektil može doseći bilo koju visinu i presresti projektil bilo koje brzine, svaki sljedeći projektil ne smije biti viši od prethodnoga, a ni brzina leta projektila koji presreće ne smije biti veća od brzine prethodnoga. Jednog dana radar je zabilježio dolazak neprijateljskih projektila. Budući da je sustav još u probnoj fazi, postoji samo jedan komplet sustava, pa možda neće biti moguće presresti sve projektile.
    
    Ako nije moguće presresti sve projektile, naravno da biramo plan koji državi nanosi najmanju štetu, tj. kojim se presreće najviše projektila. No planova s najvećim brojem presretnutih projektila može biti više; ako postoji više optimalnih planova, nasumično biramo jedan kao konačni plan akcije presretanja.
    
    Naši špijuni već su pribavili visine i brzine svih neprijateljskih projektila. Vaš je zadatak izračunati, uz provođenje gore opisane odluke, vjerojatnost da svaki pojedini projektil bude presretnut.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/cdq-divide/cdq-divide_3.cpp"
    ```

## Pretvaranje dinamičkih problema u statičke

U prva dva slučaja svrha CDQ podjele bila je prepoloviti niz i zatim rekurzivno obraditi odnose među parovima točaka kako bi se postigla dobra složenost. No u ovom odjeljku ne polovimo običan niz, nego vremenski niz.

Primjenjiva je na neke zadatke sa strukturama podataka tipa „treba podržati izmjene xxx i zatim upite xxx”. Takvi zadaci imaju dvije značajke:

-   ako upite obradimo [offline](offline.md), sve se operacije prirodno poredaju u niz po vremenu;
-   svaka je izmjena usko povezana s upitima koji dolaze nakon nje, a takvih odnosa „izmjena – upit” ima ukupno $O(n^2)$.

CDQ podjelom možemo podijeliti taj niz operacija i obraditi odnose između izmjena i upita.

Slično CDQ podjeli za odnose među parovima točaka, pretpostavimo da je niz koji trenutno dijelimo $(l,r)$: najprije rekurzivno obradimo odnose izmjena – upit unutar $(l,mid)$ i $(mid,r)$, a zatim sve odnose izmjena – upit s $l \leq i \leq mid$, $mid+1 \leq j \leq r$, gdje je $i$ izmjena, a $j$ upit.

Uočimo: ako su pojedine izmjene međusobno **neovisne**, ne moramo voditi računa o vremenskom odnosu između $l \leq i \leq mid$ i $mid+1 \leq j \leq r$ te između `solve(l,mid)` i `solve(mid+1,r)` (npr. kod običnih zadataka sa zbrajanjem i oduzimanjem). No ako izmjene nisu neovisne (npr. operacije pridruživanja vrijednosti), izgled niza nakon izmjene može ovisiti o prethodnom nizu. Tada se korak obrade svih odnosa izmjena – upit koji prelaze preko mid mora smjestiti između `solve(l,mid)` i `solve(mid+1,r)`. Razlog je isti kao kod optimizacije 1D/1D dinamičkog programiranja CDQ podjelom: samo podjela po inorder redoslijedu jamči da se svaka izmjena izvodi strogo po vremenskom redoslijedu.

### Primjeri zadataka

???+ example "Dodavanje na pravokutniku i zbroj pravokutnika"
    Održavajte dvodimenzionalno polje uz podršku dodavanja broja na pravokutno područje i upita o zbroju pravokutnog područja.

??? note "Ideja rješenja"
    Za inačicu ovog problema bez izmjena, tj. „zadano je dvodimenzionalno polje, više puta se pita zbroj pravokutnog područja”, postoji klasično rješenje pomoću sweep linea i segment treeja. Konkretno, svaki pravokutnik najprije rastavimo na dvije operacije, umetanje i brisanje, zatim svaki upit rastavimo na oblik razlike dvodimenzionalnih prefiksnih suma i na kraju sve obradimo offline. Međutim, izvorni zadatak ima izmjene, pa se to rješenje ne može izravno primijeniti.
    
    Pokušajmo na njega primijeniti CDQ podjelu. Sve upite i izmjene obradimo offline. Te operacije tvore niz i postoji $O(N^2)$ parova odnosa izmjena – upit. I dalje slijedimo uobičajeni tijek CDQ podjele: sve odnose dijelimo u tri vrste, na ovoj razini podjele obrađujemo samo odnose izmjena – upit koji prelaze preko $mid$, a preostale odnose izmjena – upit rješavamo rekurzijom.
    
    Uočavamo da su sve izmjene dovršene prije upita. Tada je izvorni problem ekvivalentan problemu „u ravnini se nalaze statični pravokutnici, neprestano se pita zbroj pravokutnog područja”.
    
    Sweep lineom u vremenu $O(n\log n)$ obradimo sve odnose izmjena – upit koji prelaze preko $mid$, a ostaje još samo rekurzivno podijeliti odnose izmjena – upit na lijevoj i desnoj strani.
    
    U ovako implementiranoj CDQ podjeli isti se upit obrađuje $O(\log n)$ puta. No to nije problem, jer su izmjene koje svaki put doprinose tom upitu međusobno disjunktne. Vremenska složenost cijelog postupka je $T(n)=T(\lfloor \frac{n}{2} \rfloor)+T(\lceil \frac{n}{2} \rceil)+ O(n\log n)=O(n\log^2n)$.
    
    Promatrajući gornji tijek algoritma uočavamo da smo u početku znali riješiti samo statični problem dodavanja na pravokutniku i zbroja pravokutnika, ali jednostavnom primjenom CDQ podjele možemo offline riješiti i dinamički problem dodavanja na pravokutniku i zbroja pravokutnika. Bit pretvaranja dinamičkog problema u statički leži u tome što CDQ podjela svaki put obrađuje samo odnose izmjena i upita koji prelaze preko neke točke, pa tada moramo razmotriti samo jednostavan problem u kojem „su svi upiti nakon izmjena”. Upravo se zbog toga CDQ podjela naziva „alatom za pretvaranje dinamičkih problema u statičke”.

???+ example "[\[Ynoi2016\] 镜中的昆虫 (Kukci u zrcalu)](https://www.luogu.com.cn/problem/P4690)"
    Održavajte niz $a_i$ duljine $n$ uz $m$ operacija.
    
    1.  Vrijednosti na intervalu $[l,r]$ postavi na $x$;
    2.  Odgovori koliko se različitih brojeva pojavljuje na intervalu $[l,r]$, tj. isti broj koji se pojavljuje više puta broji se samo jednom.
    
    Zadatak u jednoj rečenici: pridruživanje vrijednosti na intervalu i brojanje boja na intervalu.

??? note "Ideja rješenja"
    Za svaku poziciju održavamo poziciju prve točke iste boje lijevo od nje, označimo je s $pre_{i}$; time se brojanje boja na intervalu pretvara u klasičan problem brojanja točaka u ravnini (2D dominance counting).
    
    Promatrajući uzastopan segment iste boje kao jednu točku, može se dokazati da je ukupna količina promjena $pre$ jednaka $O(n+m)$, tj. jedna operacija uzrokuje samo $O(1)$ promjena vrijednosti $pre$; stoga dinamički problem dodavanja u točki i zbroja pravokutnika možemo riješiti CDQ podjelom.
    
    Konkretne promjene polja $pre$ mogu se obraditi pomoću `std::set`. Ta tehnika održavanja uzastopnih intervala setom naziva se i [old driver tree](./odt.md).

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/cdq-divide/cdq-divide_4.cpp"
    ```

???+ example "[\[HNOI2010\] 城市建设 (Izgradnja gradova)](https://www.luogu.com.cn/problem/P3206)"
    Država PS velika je zemlja s mnogo gradova. Kralj Louis razbija glavu oko izgradnje prometne infrastrukture među gradovima. Louis može graditi ceste između nekih gradova, a gradnja ceste između različitih gradova ima različitu cijenu.
    
    Louis želi izgraditi najmanje cesta tako da svi gradovi u državi budu povezani. No zbog određenih čimbenika cijena gradnje ceste između gradova mijenja se s vremenom. Louis neprestano dobiva vijesti o promjeni cijene gradnje neke ceste. Želi nakon svake vijesti odmah znati najmanji ukupni trošak kojim se gradovi mogu povezati. Louis je odlučio zatražiti vašu pomoć za taj zadatak.
    
    Zadatak u jednoj rečenici: zadan je graf uz podršku dinamičke izmjene težina bridova; nakon svake izmjene težine brida treba ispisati najmanju ukupnu cijenu minimalnog razapinjućeg stabla tog grafa.

??? note "Ideja rješenja"
    Zapravo postoji rješenje podjelom po segment treeju u kombinaciji s LCT-om, ali ta implementacija ima prevelik konstantni faktor i vjerojatno zahtijeva vješto optimiziranje konstanti da bi prošla ovaj zadatak, pa razmotrimo rješenje CDQ podjelom.
    
    Za razliku od problema koje CDQ podjela obično rješava, ovdje pri primjeni CDQ podjele nemamo odnos izmjena – upit po kojem bismo dijelili, jer ne možemo zasebno razmatrati „kakav doprinos izmjena jednog brida ima na minimalno razapinjuće stablo cijelog grafa”. Čini se da tradicionalna ideja CDQ podjele ovdje ne radi baš dobro.
    
    Iz prethodnih primjera vidi se da obična CDQ podjela ima posebnu vezu sa segment treejem: tijekom CDQ podjele zapravo implicitno gradimo segment tree (jer je rekurzivno stablo CDQ podjele upravo segment tree). Uobičajeni CDQ razmatra vezu između lijevog i desnog djeteta u segment treeju. A u ovom zadatku trebamo razmotriti odnos između roditelja i djeteta; drugim riječima, kad obrađujemo interval `$solve(l,r)$`, ako uspijemo veličinu grafa svesti na veličinu ovisnu o duljini intervala, problem je riješen.
    
    Kako onda konkretno osmisliti algoritam?
    
    Pretpostavimo da gradimo skup bridova minimalnog razapinjućeg stabla za interval $(l,r)$ i da već znamo skup bridova minimalnog razapinjućeg stabla njegova roditelja. Bridovima koji se mijenjaju unutar intervala $(l,r)$ pridružimo težine $+ \infty$ odnosno $-\infty$ te za svaku od tih dviju varijanti pokrenemo Kruskal i odredimo koji su bridovi u minimalnom razapinjućem stablu.
    
    Za pojedini brid:
    
    -   ako su svim izmijenjenim bridovima pridružene težine $+\infty$, a brid se ne pojavljuje u minimalnom razapinjućem stablu, dokazano je da se ne može pojaviti u minimalnom razapinjućem stablu ni za jedan upit iz $(l,r)$. Zato u skup bridova za $(l,r)$ dodajemo samo bridove tog minimalnog razapinjućeg stabla;
    -   ako su svim izmijenjenim bridovima pridružene težine $-\infty$, a brid se pojavljuje u minimalnom razapinjućem stablu, dokazano je da će se sigurno pojaviti u minimalnom razapinjućem stablu na cijelom intervalu $(l,r)$. Tada pomoću union–finda (disjoint set union) sažmemo vrhove tih bridova u jedan i njihove težine dodamo odgovoru.
    
    Tako smo konstruirali skup bridova za interval $(l,r)$. Minimalno razapinjuće stablo dobiveno iz tih bridova ekvivalentno je minimalnom razapinjućem stablu izvornog grafa.
    
    Zašto je onda naša složenost ispravna?
    
    Prvo, izmijenjeni bridovi sigurno ulaze u naš skup bridova, a njihov je broj reda $O(len)$.
    
    Zatim moramo dokazati da u skupu bridova neće biti previše neizmijenjenih bridova. Dodajemo samo bridove minimalnog razapinjućeg stabla u kojem sve izmijenjene težine iznose $+\infty$, pa broj dodanih bridova ne premašuje broj vrhova trenutnog grafa.
    
    Sada još samo treba dokazati da je broj vrhova grafa na svakoj razini rekurzije reda $O(len)$ i time je pokazano da je i broj bridova grafa reda $O(len)$.
    
    Dokaz da je broj vrhova reda $O(len)$ postaje vrlo jednostavan. Bridovi koje sažimamo pri svakom spuštanju u rekurziju su neizmijenjeni bridovi koji se pojavljuju u razapinjućem stablu s $-\infty$; gledano obrnuto, odrezali smo sve izmijenjene bridove koji se pojavljuju u razapinjućem stablu s $-\infty$. Očito odrežemo najviše $len$ bridova, pa se cijeli graf raspada na najviše $O(len)$ komponenata povezanosti, a time je broj vrhova novog grafa reda $O(len)$. Time smo dokazali da je graf na kojem pokrećemo Kruskal svaki put reda $O(len)$, pa je vremenska složenost svake razine $O(n\log n)$.
    
    Vremenska složenost je $T(n)=T(\lfloor \frac{n}{2} \rfloor)+T(\lceil \frac{n}{2} \rceil)+ O(n\log n)=O(n\log^2n)$.
    
    Implementacija može biti ponešto zahtjevna. Treba paziti da union–find ne smije koristiti kompresiju puta, jer inače ne bi podržavao vraćanje (rollback). Sažimanje vrhova također nije potrebno doista izvoditi; dovoljno je da se Kruskal na svakoj razini izravno izvodi u union–findu prethodne razine.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/cdq-divide/cdq-divide_5.cpp"
    ```

## Literatura i napomene

[^ref1]: [从《Cash》谈一类分治算法的应用 (O primjeni jedne klase algoritama podjele na primjeru zadatka „Cash”)](https://www.cs.princeton.edu/~danqic/papers/divide-and-conquer.pdf)
