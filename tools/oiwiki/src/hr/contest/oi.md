---
title: OI natjecanja i formati natjecanja
---

## Uvod u natjecanja

**Informatička olimpijada** (engl. Olympiad in Informatics, skraćeno OI) predmetno je natjecanje široko rasprostranjeno među srednjoškolcima, iste naravi kao natjecanja iz fizike, matematike i sl. OI provjerava sposobnost natjecatelja da primjenom algoritama, struktura podataka i matematičkog znanja pisanjem računalnih programa rješavaju konkretne probleme.

Postoji mnogo vrsta OI natjecanja; samo u Kini to su, među ostalim:

-   Kinesko nacionalno informatičko olimpijsko natjecanje po pokrajinama (NOIP)
-   Kinesko nacionalno informatičko olimpijsko natjecanje (NOI)
-   Zimski kamp kineskog nacionalnog informatičkog olimpijskog natjecanja (WC)
-   Kinesko izborno natjecanje za Međunarodnu informatičku olimpijadu (CTSC)

Međunarodna OI natjecanja uključuju:

-   Međunarodnu informatičku olimpijadu (IOI)
-   Američku računalnu olimpijadu (USACO)
-   Japansku informatičku olimpijadu (JOI)
-   Azijsko-pacifičku informatičku olimpijadu (APIO)

    …

Za većinu natjecatelja nova sezona svake godine počinje prvim krugom CSP-J/S u rujnu.

U Kini je jedini dopušteni jezik na OI natjecanjima C++ (nekad su bili dopušteni i C i Pascal, ali je njihova podrška ukinuta). Različita natjecanja imaju različita pravila o inačici C++-a. Zadaci su obično vezani uz algoritme ili strukture podataka, a po obliku su klasični (najčešći oblik, sa zadanim ulazom i izlazom u datoteke) i neklasični (zadaci s predajom odgovora, interaktivni zadaci, zadaci dopunjavanja koda itd.).

## Uvod u formate natjecanja

### OI format

Natjecatelj ima samo jednu priliku za predaju. Tijekom natjecanja rezultati ocjenjivanja nisu vidljivi; bodovi se objavljuju nakon natjecanja. Svaki zadatak ima više test-primjera i bodovi se dodjeljuju prema broju riješenih test-primjera; svaki test-primjer može nositi i djelomične bodove, pa se bodovi mogu dobiti i ako prođe samo dio podataka.

???+ note "Alat za samoocjenjivanje selfEval"
    Danas se na nekim natjecanjima serije NOI nudi alat za samoocjenjivanje selfEval. selfEval je ugrađen u posebnu inačicu NOI Linuxa za nacionalno natjecanje. Otkako je službeno predstavljen i pušten u upotrebu na NOI 2023, selfEval se postupno koristi na kasnijim nacionalnim NOI natjecanjima, APIO-u (kineska regija), NOI zimskom kampu i drugdje. Natjecatelji pomoću selfEvala mogu testirati svoj program na skupu test-podataka (tzv. pretest-podaci) i dobiti povratnu informaciju. Broj samotestiranja po natjecanju ograničen je (na NOI 2024 najviše 50, na NOI 2025 najviše 30), a ni pretest-podaci nisu vidljivi natjecateljima. Budući da se pretest-podaci razlikuju od službenih test-podataka, rezultati samotestiranja služe samo za otklanjanje pogrešaka i ne mogu se smatrati službenim rezultatom. Pri više pretestiranja istog zadatka koriste se isti pretest-podaci.

Drugi krug CSP-J/S, NOIP, pokrajinski izbori i NOI svi koriste OI format.

### IOI format

Natjecatelj tijekom natjecanja ima više prilika za predaju. Rješenja se ocjenjuju u stvarnom vremenu i rezultat se vraća odmah; za netočnu predaju nema nikakve kazne. Svaki zadatak ima više test-primjera, a bodovi se dodjeljuju prema broju riješenih test-primjera.

APIO i IOI koriste IOI format. Trenutno se i domaća natjecanja postupno približavaju IOI formatu.

### Codeforces (CF) format

[Codeforces](https://codeforces.com) je online sustav za ocjenjivanje koji redovito organizira natjecanja.

Posebnost njegovih natjecanja jest da se tijekom natjecanja testira samo dio podataka (Pretests), a nakon završetka natjecanja vraćaju se rezultati na svim test-primjerima (System Tests). Tijekom natjecanja može se predavati više puta, a dopušteno je i hackati tuđi kod (hack ovdje znači predati test-podatak na kojem tuđi kod ne daje točan odgovor). Da bi mogao hackati, natjecatelj mora zaključati svoj kod (drugim riječima, taj zadatak tijekom natjecanja više ne može ponovno predati). Pri hackanju nije dopušteno kopirati tuđi program na lokalno računalo radi testiranja; izvorni kod prikazuje se kao slika.

Codeforces nudi i drugi format, zvan prošireni ICPC (Extended ICPC ili ICPC+). U tom se formatu tijekom natjecanja testiraju svi podaci, ali nakon natjecanja slijedi 12 sati otvorenog hackanja za sve. Pri hackanju je dopušteno kopirati tuđi program na lokalno računalo radi testiranja.

## Glavna natjecanja

### CSP-J/S

**CSP-J/S** (engl. Certified Software Professional Junior/Senior) neprofesionalna je certifikacija programskih sposobnosti koju je CCF uveo nakon ukidanja NOIP-a 2019. Do 2025. bila je otvorena svim dobnim skupinama, a [poslije je ograničena na osobe starije od 12 godina](https://www.noi.cn/xw/2025-02-13/837984.shtml).

CSP-J/S dijeli se na početnu razinu (Junior, skraćeno CSP-J) i naprednu razinu (Senior, skraćeno CSP-S), a natjecanje ima dva kruga: prvi (obično u rujnu) i drugi (obično u listopadu). Prvi krug pisani je ispit koji provjerava računalnu teoriju, opće znanje o radu s računalom te osnove algoritama i matematike; drugi je krug ispit na računalu, s po 4 zadatka u obje skupine, pri čemu početna skupina ima 3,5 sata, a napredna 4 sata (osim CSP-S 2019, koje je koristilo stari format napredne skupine NOIP-a: dva dana, svaki dan 3 zadatka u 3,5 sata). Na prvi krug mogu se prijaviti svi učenici stariji od 12 godina, a najbolji nakon određenog odabira po rangu dobivaju priliku sudjelovati u drugom krugu.

Za prijavu na prvi/drugi krug te za žalbe na zadatke nakon drugog kruga CCF-u se plaća naknada.

Rezultati obaju krugova certificiraju se po pokrajinama prema rangu, u tri razreda: prvi, drugi i treći.

### NOIP

**NOIP** (engl. National Olympiad in Informatics in Provinces, kin. Kinesko nacionalno informatičko olimpijsko natjecanje po pokrajinama) informatičko je natjecanje koje organizira Narodna Republika Kina za srednjoškolce iz Kine (uključujući Hong Kong i Macau).

Stari format do zaključno 2018.: NOIP se po sudionicima dijelio na popularizacijsku (普及) i naprednu (提高) skupinu, a 2018. u Šangaju je pokusno uvedena i početna skupina; po fazama dijelio se na preliminarno i završno natjecanje. Preliminarno natjecanje provjeravalo je osnove računarstva i algoritama, a završno je bilo ispit na računalu. Održavao se obično drugog vikenda u studenom: u subotu ujutro prvi ispit napredne skupine 8:30–12:00 (3,5 sata, 3 zadatka), poslijepodne 14:30–18:00 popularizacijska skupina (3,5 sata, 4 zadatka), u nedjelju ujutro drugi ispit napredne skupine 8:30–12:00 (3,5 sata, 3 zadatka). U cijeloj se zemlji koristio isti skup zadataka, ali je pravila nagrađivanja prema stanju u pojedinoj pokrajini jedinstveno određivao CCF (China Computer Federation) i objavljivao ih nakon natjecanja na [službenim stranicama NOI-ja](http://www.noi.cn). Bodovni prag za prvu nagradu malo se razlikovao po pokrajinama.

NOIP je 16. kolovoza 2019. [CCF privremeno obustavio](http://www.noi.cn/xw/2019-08-16/715365.shtml), a 21. siječnja 2020. [objavljeno je da se obnavlja](http://www.noi.cn/xw/2020-01-21/715520.shtml). Format NOIP-a od 2020. razlikuje se od prijašnjeg, i to ovako:

-   ukinuto je preliminarno natjecanje; zamjenjuje ga prvi krug CSP-J/S;
-   ukinuta je popularizacijska skupina; zamjenjuje je CSP-J, pa NOIP otad ima samo jednu skupinu, namijenjenu natjecateljima napredne razine;
-   raspored je s prijašnja dva dana i ukupno 6 zadataka, po 3,5 sata dnevno, skraćen na jedan dan s 4 zadatka u ukupno 4,5 sata;
-   natjecatelji moraju ostvariti određeni plasman u drugom krugu CSP-S da bi stekli pravo nastupa na NOIP-u; konkretne kvote razlikuju se po pokrajinama. Pokrajinske kvote za NOIP ovise o broju sudionika i rezultatima te pokrajine u prošloj sezoni i sl.

Za prijavu na NOIP i za žalbe na zadatke ne plaća se dodatna naknada.

NOIP se rangira i nagrađuje po pokrajinama. Do 2019. natjecatelji s pokrajinskom prvom nagradom u naprednoj skupini mogli su na većini sveučilišta steći pravo na samostalni prijamni postupak.

> U siječnju 2020. Ministarstvo obrazovanja Narodne Republike Kine objavilo je [Mišljenje o pokusnoj reformi upisa u temeljne znanstvene discipline na nekim sveučilištima](http://www.moe.gov.cn/srcsite/A15/moe_776/s3258/202001/t20200115_415589.html). U njemu se navodi da se od 2020. više ne provodi samostalni prijamni postupak sveučilišta te da se na nekim vodećim sveučilištima pokusno uvodi reforma upisa u temeljne discipline (program Qiangji).

### Pokrajinski izbori

**Pokrajinski izbori** (skraćeno: 省选, provincial selection) služe za odabir pokrajinskih reprezentacija za nacionalno natjecanje i obično se održavaju od siječnja do travnja. Raspored obično obuhvaća dva dana, svaki dan 3 zadatka u 4,5 sata.

Zadatke pokrajinskih izbora određuje svaka pokrajina samostalno; trenutno je trend da se mnoge pokrajine udružuju u zajedničkom sastavljanju zadataka.

Kvote pokrajinskih reprezentacija računaju se po složenim formulama, obično ovisno o prijašnjim rezultatima i broju sudionika. NOIP bodovi u pravilu moraju činiti određeni udio u kriterijima pokrajinskih izbora. Prema pravilima, natjecatelji iz osnovne škole mogu biti izabrani samo kao natjecatelji razreda E i ne mogu sudjelovati u izboru za razrede A i B. Razred A čini 5 natjecatelja ([od toga barem 1 djevojka](https://www.noi.cn/xw/2024-08-26/829152.shtml)), a ostali natjecatelji prema zadanim kvotama i osvojenim bodovima redom ulaze u ekipu B. Broj sudionika NOI-ja iz jedne škole ne smije premašiti trećinu ukupnog broja mjesta A i B te pokrajine (zaokruženo), pri čemu se najbolje rangirana djevojka izabrana u ekipu A ne računa u taj udio (tzv. ograničenje 1/3 ili eliminacija 1/3; vidi [službeno objašnjenje CCF-a](https://www.noi.cn/xw/2022-12-14/781364.shtml)).

Od 2020. zadatke i ocjenjivanje pokrajinskih izbora za NOI jedinstveno provodi CCF; pokrajine koje su to u stanju mogu sastavljati vlastite zadatke, ali način odabira mora odobriti CCF. Od 2024. pokrajinski izbori za NOI vraćaju se samostalnom sastavljanju zadataka po pokrajinama; pokrajine koje to žele mogu organizirati zajednička natjecanja ili koristiti zadatke drugih pokrajina, ali konkretni plan mora odobriti CCF.

### NOI

**NOI** (engl. National Olympiad in Informatics, kin. Kinesko nacionalno informatičko olimpijsko natjecanje) najviše je domaće natjecanje pokrajinskih reprezentacija, uključujući Hong Kong i Macau.

NOI se obično održava u srpnju, a natjecatelji se dijele na službene natjecatelje i natjecatelje ljetnog kampa. Službeni natjecatelji dijele se u tri razreda: A i B službeni su natjecatelji pokrajinskih reprezentacija, a razred C čine natjecatelji pozivnog natjecanja. Razredi A i B odgovaraju razredima A i B pokrajinskih reprezentacija (razred A pri računanju rezultata dobiva 5 dodatnih bodova); razred C nominalno su nagradna mjesta za škole koje su dale izniman doprinos CCF-u. Natjecatelji ljetnog kampa dijele se na razrede D i E, koji odgovaraju neslužbenim natjecateljima srednjoškolske odnosno osnovnoškolske skupine. Ako natjecatelji ljetnog kampa premaše bodovni prag, dobivaju samo potvrdu o rezultatu, a ne medalju (isti rezultat vrijedi nešto manje). Najboljih 50 službenih natjecatelja čini nacionalnu pripremnu ekipu i stječe pravo izravnog upisa na sveučilište.

Na međunarodnoj razini, radi razlikovanja od drugih natjecanja koja se također zovu NOI, ponekad se naziva CNOI.

### CTT

**CTT** (engl. China Team Training, kin. priprema nacionalne pripremne ekipe za Međunarodnu informatičku olimpijadu) pripremna je i izborna aktivnost za članove nacionalne pripremne ekipe za IOI koja se održava svake zime i sastoji se od 3–4 testa. Osim nacionalne pripremne ekipe, u CTT-u pod nazivom „elitne pripreme” mogu sudjelovati i neki natjecatelji s izvrsnim rezultatima na NOI-ju te godine.

CTT zajedno s domaćim zadaćama i ostalim postupcima čini prvu fazu odabira nacionalne ekipe. Od 2021. najboljih 30 natjecatelja u prvoj fazi postaje nacionalna kandidatska ekipa i ulazi u drugu fazu odabira (WC).

### WC

**WC** (engl. Winter Camp, kin. Zimski kamp kineskog nacionalnog informatičkog olimpijskog natjecanja) aktivnost je koja se svake zime održava u mjestu održavanja NOI-ja te godine. Iako aktivnost prvenstveno služi pripremi pripremne ekipe i odabiru nacionalne ekipe, kao neslužbeni polaznici mogu sudjelovati i natjecatelji s dobrim rezultatima na NOIP-u i drugom krugu CSP-S prethodne godine.

WC obuhvaća nekoliko dana predavanja i testova; rezultati testova zbrajaju se s rezultatima prethodnih faza u ukupni poredak članova pripremne ekipe. Do 2020. održavao se samo jedan test, s istim zadacima za pripremnu ekipu i neslužbene polaznike, a najboljih 15 članova pripremne ekipe po ukupnom poretku postajalo je nacionalna kandidatska ekipa i sudjelovalo u završnoj fazi odabira (CTS i sl.). Od 2021., kad je funkcija odabira nacionalne ekipe s CTS-a prebačena na WC, kandidatska ekipa polaže dva testa, dok neslužbeni polaznici i dalje polažu jedan, a zadaci neslužbenih polaznika djelomično se preklapaju sa zadacima kandidatske ekipe. Najboljih 6 kandidata po ukupnom poretku ide na završni razgovor, nakon kojeg se biraju 4 službena natjecatelja i 2 pričuvna za IOI te godine.

### APIO

**APIO** (engl. Asia-Pacific Informatics Olympiad, kin. Azijsko-pacifička informatička olimpijada) informatičko je natjecanje za srednjoškolce iz azijsko-pacifičke regije. CCF svake godine početkom svibnja organizira zrcalno natjecanje za kinesku regiju. Oko dana natjecanja održavaju se i pripreme.

Natjecatelji APIO-a dijele se na razrede A i B: šest najboljih iz razreda A (uključujući izjednačene) može sudjelovati u dodjeli međunarodnih nagrada APIO-a, dok natjecatelji razreda B sudjeluju samo u dodjeli nagrada kineske regije.

### CTS

**CTS** (prijašnji naziv: CTSC, engl. China Team Selection Competition, kin. Kinesko izborno natjecanje za Međunarodnu informatičku olimpijadu) služi za odabir nacionalne ekipe (6 osoba) iz nacionalne kandidatske ekipe (15 osoba) za IOI tog ljeta; od toga su 4 službena natjecatelja i 2 pričuvna. Kao i na WC-u, mogu sudjelovati i natjecatelji s dobrim rezultatima na NOIP-u prethodne godine (ali ne sudjeluju u odabiru).

Na APIO i CTS prijavljuje se po pokrajinama, a sudionici APIO-a i CTS-a obično se određuju prema poretku na NOIP-u (ta su dva natjecanja obično vremenski vrlo blizu).

CTS 2020. otkazan je zbog pandemije, a nacionalna pripremna ekipa te godine izabrana je putem NOI-ja; od 2021. izborni postupak CTS-a zamijenjen je WC-om.

### IOI

**IOI** (engl. International Olympiad in Informatics, kin. Međunarodna informatička olimpijada) godišnje je informatičko natjecanje za srednjoškolce iz cijelog svijeta. Svaku zemlju predstavljaju četiri natjecatelja, a natjecanje se obično prenosi uživo. U IOI formatu svaki zadatak ima podzadatke (Subtask), a svaki podzadatak nosi određeni broj bodova.

### Sveučilišni kampovi

#### Sveučilište u Pekingu (PKU)

-   Zimski informatički kamp Sveučilišta u Pekingu (PKUWC): održava se oko zimskog kampa.
-   Informatički kamp Sveučilišta u Pekingu (PKUSC): obično se održava u lipnju u kampusu. Budući da se natjecanje održava u sveučilišnoj računalnoj učionici, okruženje je Windows, a sustav za natjecanje OpenJudge.
-   Ljetna škola Sveučilišta u Pekingu za srednjoškolce (informatika): održava se tijekom ljetnih praznika za učenike prirodoslovnog smjera trećeg razreda srednje škole.

#### Sveučilište Tsinghua (THU)

-   Zimski seminar i nastava „povezivanja srednje škole i sveučilišta” Odsjeka za računarstvo: odgovara zimskom informatičkom kampu, a ponekad se na engleskom skraćeno naziva THUWC. Obično traje dva dana; ujutro je natjecanje (prvi dan standardno OI natjecanje, drugi dan natjecanje u „inženjerskim zadacima” koje je osmislila Tsinghua), a poslijepodne predavanja.

## OI natjecanja u drugim zemljama i regijama

### SAD: USACO

Službene stranice: <http://www.usaco.org/>

USACO je možda strano OI natjecanje najpoznatije kineskim natjecateljima (a vjerojatno i strano OI natjecanje s najviše rješenja na kineskom).

Svake godine od zime do ranog proljeća USACO održava jedno online natjecanje mjesečno. Jedno natjecanje traje 3–5 sati.

Prema opisu na službenim stranicama, natjecanja USACO-a imaju 4 razine težine (do školske godine 2015./2016. bile su 3):

-   brončana razina, za početnike u programiranju, osobito učenike koji znaju samo najosnovnije algoritme (npr. sortiranje, binarno pretraživanje);
-   srebrna razina, za učenike koji počinju učiti osnovne algoritamske tehnike (npr. rekurzija, pretraživanje, greedy algoritmi) i osnovne strukture podataka;
-   zlatna razina, u kojoj se učenici susreću sa složenijim algoritmima (npr. najkraći putovi, DP) i naprednijim strukturama podataka;
-   platinasta razina, za natjecatelje s čvrstim vještinama dizajna algoritama; platinasta im razina pomaže da se okušaju na složenim i otvorenijim problemima.

U Kini je trenutno online sudac s najpotpunijom zbirkom zadataka USACO-a Luogu.

### Poljska: POI

Službene stranice: <https://oi.edu.pl/>

Službena stranica za predaju: <https://szkopul.edu.pl/p/default/problemset/>

POI je strano OI natjecanje koje najčešće rješavaju natjecatelji koji se pripremaju za pokrajinske izbore.

Prema opisu na [službenim stranicama POI-ja](https://oi.edu.pl/l/42/), POI se odvija ovako:

-   prvi krug: šest zadataka (do zaključno 31. izdanja pet), online natjecanje;
-   drugi krug: jedno probno natjecanje i dva službena natjecanja; probno ima jedan zadatak, a svako službeno dva;
-   treći krug: jedno probno natjecanje i dva službena natjecanja; probno ima jedan zadatak, a svako službeno tri.

Nekih godina održavalo se natjecanje pod nazivom ONTAK, službeno nazvano pripremni kamp POI-ja, usporedivo s kineskim pripremnim natjecanjem nacionalne pripremne ekipe (CTT).

Osim toga, u Poljskoj se održava i otvoreno natjecanje PA, u slobodnom prijevodu „Algoritamski okršaji”, čije su službene stranice: <https://potyczki.mimuw.edu.pl/>.

Među kineskim online sucima trenutno najpotpuniju zbirku zadataka POI-ja ima BZOJ.

### Hrvatska: COCI

Službene stranice (engleski): <http://www.hsin.hr/coci/>

Službene stranice (hrvatski): <http://www.hsin.hr/honi/>

Natjecanje vrlo širokog raspona težine, otprilike od popularizacijske razine minus do pokrajinskih izbora minus.

Nekad je COCI za sve zadatke objavljivao tekst zadataka, test-podatke, rješenja i službena rješenja u kodu. Od kraja 2017. rješenja i službeni kodovi COCI-ja prestali su se objavljivati. U sezoni 2019./2020. objavljivanje rješenja i službenih kodova ponovno je pokrenuto.

Luogu, BZOJ i LibreOJ imaju manji broj zadataka s COCI-ja.

### Japan: JOI

Službene stranice: <https://www.ioi-jp.org/>

JOI (jap. 日本情報オリンピック, Japanska informatička olimpijada) za sve zadatke objavljuje tekst zadataka, test-podatke, rješenja i službene kodove. Posljednjih nekoliko godina završno natjecanje JOI-ja i proljetni kamp imaju tekst zadataka na engleskom, ali ne i rješenja na engleskom. JOI Open svih godina ima tekstove zadataka i rješenja na engleskom.

Tijek JOI-ja:

-   predizbor (予選)
-   završno natjecanje (本選/JOI Final)
-   proljetni kamp (春季トレーニング合宿/JOI Spring Camp/JOISC)
-   otvoreno natjecanje (通信教育/JOI Open Contest)

Predizbor je razmjerno lagan, a od sezone 2019./2020. ima više krugova. Težina JOI Finala kreće se otprilike od napredne razine minus do napredne razine plus. Zadaci JOISC-a i JOI Opena po težini se kreću od napredne razine do NOI minus.

Velika većina zadataka JOI-ja može se predati na [AtCoderu](https://atcoder.jp/). Više zadataka JOI-ja (tekstovi na japanskom) možete pronaći na službenim stranicama JOI-ja ili na AtCoderu.

LibreOJ i BZOJ trenutno imaju zadatke JOI Finala, JOISC-a i JOI Opena iz posljednjih godina.

### Rusija: ROI

Službene stranice: <http://neerc.ifmo.ru/school/archive/index.html>

Online predaja: <https://contest.yandex.ru/roiarchive/> i Codeforces (djelomično).

ROI (rus. олимпиадная информатика, Ruska informatička olimpijada) rusko je informatičko natjecanje.

Tijek:

-   gradsko natjecanje (Municipal Stage/Муниципальный этап)
-   regionalno natjecanje (Regional Stage/Региональный этап)
-   završno natjecanje (Final Stage/Заключительный этап)

LibreOJ trenutno ima prijevode zadataka završnog natjecanja ROI-ja iz posljednjih godina.

Osim toga, veća ruska natjecanja za srednjoškolce su i:

-   Internetska informatička olimpijada (rus. Интернет-олимпиады по информатике)
    -   službene stranice: <http://neerc.ifmo.ru/school/io/index.html>
    -   natjecanje organiziraju autori zadataka ROI-ja.
-   Sverusko ekipno informatičko natjecanje za školarce (rus. Всероссийской командной олимпиады школьников)
    -   službene stranice: <http://neerc.ifmo.ru/school/russia-team/index.html>
    -   njegovo kvalifikacijsko natjecanje Moscow Team Olympiad može se predavati na Codeforcesu.
-   Innopolis Open
    -   službene stranice: <https://olymp.innopolis.ru/en/ooui/information/>
-   Otvorena programerska olimpijada za školarce (Открытая олимпиада школьников по программированию)
    -   službene stranice: <https://olympiads.ru/zaoch/>
    -   prema službenim stranicama natjecanje je usporedivo s ROI-jem.

### Kanada: CCC & CCO

CCC (engl. Canadian Computing Competition) i CCO (engl. Canadian Computing Olympiad); informacije i zadaci prijašnjih izdanja mogu se pronaći na [službenim stranicama](https://cemc.math.uwaterloo.ca/contests/past_contests.html#ccc).

Na DMOJ-u se mogu predavati zadaci [CCC-a](https://dmoj.ca/problems/?category=4) i [CCO-a](https://dmoj.ca/problems/?category=24), a taj online sudac ima i rješenja zadataka CCC-a.

CCC Junior/Senior po težini je blizu popularizacijske/napredne skupine NOIP-a. Za zlatnu medalju na CCO-u vjerojatno treba razina srebrne medalje NOI-ja.

### Singapur: NOI SG

Službene stranice: <https://noisg.comp.nus.edu.sg/noi/>

Puni naziv je Singapore National Olympiad in Informatics; u singapurskom kontekstu, kad nema dvosmislenosti, naziva se i NOI. Po formatu se dijeli na Online Qualification Contest (online kvalifikacije) i Final Contest (nacionalno finale). Na online kvalifikacije prijavljuju se škole; natjecatelji se natječu u vlastitoj školi i predaju rješenja daljinski putem interneta. Rezultati kvalifikacija rangiraju se samo unutar škole, a najboljih 5 s nenultim rezultatom stječe pravo predstavljati školu u nacionalnom finalu.

Kineski online suci trenutno imaju vrlo malo zadataka NOI SG-a; tekstovi zadataka, test-podaci i službeni kodovi svih godina mogu se pronaći na [službenom GitHub računu](https://github.com/noisg).

### Tajvan: Informatička olimpijada (資訊奧林匹亞競賽)

Na Tajvanu se riječ informatics iz OI prevodi kao „資訊”, a ne kao „信息”, što je uobičajeni prijevod u kontinentalnoj Kini.

Tajvanski natjecatelji koji žele sudjelovati na IOI-ju moraju proći ove krugove natjecanja:

-   regionalno natjecanje iz informatike (區域資訊學科能力競賽)
-   nacionalno natjecanje iz informatike (全國資訊學科能力競賽)
-   informatički pripremni kamp (資訊研習營, TOI)

### Ostale zemlje

-   Australija: AIO: <https://orac.amt.edu.au/hub/aio/>

    -   težina slična NOI-ju.

-   Ujedinjeno Kraljevstvo: British Informatics Olympiad: <https://www.olympiad.org.uk/>

    -   preniska težina.

-   Češka: Matematická olympiáda–kategorie P: <http://mo.mff.cuni.cz/p/archiv.html>

-   Rumunjska: Olimpiada Nationala de Informatica: <http://olimpiada.info/>
    -   tekstove zadataka, test-podatke i rješenja potražite na karticama s natpisom Subiecte.

## Ostala međunarodna OI natjecanja

### BalticOI

**BalticOI** namijenjen je zemljama oko Baltičkog mora. Na BalticOI 2018 sudjelovalo je 9 zemalja, među kojima Litva, Poljska, Estonija i Finska. Zadaci su teški.

Osim 2017., BalticOI svake godine objavljuje tekstove zadataka, test-podatke i rješenja. BalticOI nema stalne službene stranice; domaćin svake godine izrađuje novu stranicu. Adrese službenih stranica po godinama vidi u [objavi](https://loj.ac/article/416).

LibreOJ trenutno ima zadatke BalticOI-ja iz posljednjih desetak godina.

### BalkanOI

**BalkanOI** namijenjen je zemljama balkanske regije. Na BalkanOI 2018 sudjelovalo je 12 zemalja, među kojima Rumunjska, Grčka, Bugarska i Srbija. Zadaci su teški.

BalkanOI je samo nekih godina objavio tekstove zadataka, test-podatke i rješenja; adrese službenih stranica vidi u [objavi](https://loj.ac/article/416).

### CEOI

Zemlje sudionice CEOI-ja 2018 djelomično se preklapaju s gornjim dvama natjecanjima, a uključuju Poljsku, Rumunjsku, Gruziju, Hrvatsku i druge. Zadaci su teški.

CEOI svake godine objavljuje tekstove zadataka, test-podatke i rješenja; adrese službenih stranica vidi u [objavi](https://loj.ac/article/416).

### eJOI

**eJOI** je skraćeno od European Junior Olympiad in Informatics. Zemlje sudionice uključuju Rusiju, Armeniju, Bugarsku, Poljsku i druge. Zadaci su razmjerno teški.

eJOI svake godine objavljuje tekstove zadataka, test-podatke i rješenja; adrese službenih stranica vidi u [objavi](https://loj.ac/article/416).

### NOI

???+ warning "Upozorenje"
    Ovdje nije riječ o Kineskom nacionalnom informatičkom olimpijskom natjecanju.

**NOI** je skraćeno od Nordic Olympiads in Informatics.

Službene stranice: <http://nordic.progolymp.se>

Natjecanje se održava tek posljednjih nekoliko godina i namijenjeno je nordijskim zemljama.

## Literatura

-   [ICPC/CCPC natjecanja i formati natjecanja](./icpc.md)
-   [„Prevoditeljska skupina” – adrese nekih kontinentalnih OI natjecanja](https://loj.ac/article/416)
