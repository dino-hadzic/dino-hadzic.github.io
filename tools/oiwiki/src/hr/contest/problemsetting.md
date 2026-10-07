---
title: Sastavljanje zadataka
---

## Priprema prije sastavljanja zadataka

### Posjedovati određenu razinu

S jedne strane, teško je da netko sam sastavi zadatak teži od vlastite razine; određena razina u OI-ju pomaže da se dođe do kvalitetnije ideje i osmisli dobro rješenje. S druge strane, razina u OI-ju donekle odražava i OI iskustvo: natjecatelj koji je vidio više zadataka ima i vlastito mišljenje o tome što je „dobar zadatak”.

### Imati ozbiljan i odgovoran stav

Zadaci se sastavljaju da bi ih drugi rješavali; više nego pokazivanju sebe, služe drugima. Algoritamsko natjecanje natjecanje je među natjecateljima, a ne nadmetanje autora zadataka i rješavača. Zato cilj sastavljanja ne smije biti srušiti natjecatelje (naravno, primjerena zaštita od AK-a i dobra razlučivost također su vrlo važni), nego omogućiti natjecateljima da na natjecanju nešto nauče. Vrlo je važno uložiti dovoljno vremena i truda da se nauči kako sastavljati zadatke te ih sastavljati ozbiljno i odgovorno.

### Pripremiti se na velik utrošak vremena

Tko želi ozbiljno sastavljati zadatke, nužno će potrošiti mnogo vremena. Bez mentalne pripreme to može dovesti do užurbane pripreme natjecanja i nedovoljne kvalitete, a poslije i do žaljenja što vrijeme nije uloženo u učenje. No sastavljanje zadataka može donijeti i mnogo lijepih uspomena; ako vas ono doista zanima i mentalno ste se dobro pripremili, ono što sastavljanjem dobijete može nadoknaditi utrošeno vrijeme.

### Pažljivo pročitati ovaj tekst

Ovaj tekst opisuje cijeli postupak sastavljanja zadataka s dvaju gledišta: kako sastaviti zadatak i kako ga sastaviti dobro. Tko želi sastavljati zadatke, pažljivim će čitanjem ovog teksta sigurno mnogo dobiti.

## Sadržaj zadatka

Pri sastavljanju zadatka ideja, tj. bitni sadržaj zadatka, duša je zadatka i prvi korak u sastavljanju.

### Izvori ideja

1.  Inspiracija postojećim zadacima (ali bez prepisivanja ili besmislenog pojačavanja, npr. prenošenja zadatka s nizovima na kaktus).
2.  Inspiracija naučenim gradivom (ali bez nepovezanog slaganja tema).
3.  Inspiracija iz života/igara (ali pazite da od igre ne napravite veliku simulaciju).
4.  Ne znate zašto, jednostavno vam je pao na pamet zadatak.

### Kakve ideje nisu dobre

#### O već postojećim zadacima

Postojeći (već viđeni) zadaci dijele se otprilike na tri vrste: potpuno jednaki, gotovo jednaki i jednaki po rješenju.

-   Potpuno jednaki: AC kodom jednog zadatka može se dobiti AC na drugom.
-   Gotovo jednaki: preinaku AC koda jednog zadatka u AC kod drugog može napraviti netko tko taj zadatak ne zna riješiti.
-   Jednaki po rješenju: ključna ideja i rješenje su jednaki, ali se razlikuju u implementaciji i manje bitnim detaljima.

Ove tri vrste odozdo prema gore stoje u odnosu uključivanja.

Sljedeće se ne smije dogoditi:

1.  Sastaviti postojeći zadatak znajući da postoji „gotovo jednak” zadatak.
2.  Sastaviti „gotovo jednak” postojeći zadatak jer se nije provjerilo tražilicom pa se za postojeći zadatak nije znalo.
3.  Sastaviti postojeći zadatak kad je zadatak „jednak po rješenju” općepoznat (npr. zadatak s NOIP-a ili NOI-ja).
4.  Pojava zadatka „jednakog po rješenju” među zadacima koji nisu „poklon-zadaci” na selekcijskom ispitu.

Sljedeće je bolje izbjegavati:

1.  Sastaviti postojeći zadatak znajući da postoji zadatak barem „jednak po rješenju”.
2.  Sastaviti zadatak „jednak po rješenju” jer se nije provjerilo tražilicom pa se za postojeći zadatak nije znalo.
3.  U bilo kojim okolnostima sastaviti „gotovo jednak” postojeći zadatak.

Iznimke u kojima se zahtjevi mogu ublažiti:

1.  Školska probna natjecanja.
2.  Probna natjecanja s ciljem tematskog treninga.
3.  Natjecanja niže težine ili zadaci zamišljeni kao „poklon-zadaci”.

#### O „otrovnim” zadacima

„Otrovni zadatak” vrlo je nejasan i subjektivan pojam; ovdje samo navodimo neke ranije rasprave o tome uz vlastito tumačenje. Tema je vrlo otvorena i svatko je pozvan iznijeti svoje mišljenje.

> Dobar zadatak ne bi smio biti dva zadatka spojena u jedan; dobar zadatak ima vlastitu ideju – i trebao bi tu ideju istaknuti bez previše omota.
>
> Dobar zadatak treba biti nov. Pravi dobar zadatak onaj je koji ljude potiče da smisle nove dobre zadatke.
>
> — [vfk, „UOJ 精神之源流” (Izvor duha UOJ-a)][1]

Primjer: [„XR-1” 柯南家族](https://www.luogu.com.cn/problem/P5346) – dva dijela rješenja potpuno su odvojena: prvi je dio [„predložak” sufiksno sortiranje na stablu](https://www.luogu.com.cn/problem/P5353), a drugi klasični problem na stablu. Čak i ako se težine vrhova stabla unesu proizvoljno, drugi se dio i dalje može riješiti; dijelovi nisu povezani.

> Jedna vrsta OI zadataka pretežno je matematička: i opis zadatka i rješenje imaju obilježja matematičkog zadatka, a rješenje ne sadrži algoritamska znanja. Takvi se OI zadaci zajednički nazivaju čisto matematičkim zadacima.
>
> — [王天懿, „论偏题的危害” (O štetnosti neuobičajenih zadataka)][2]

Klasičan primjer: [NOIP2017 小凯的疑惑](https://uoj.ac/problem/329)

Razlika između matematičkih zadataka u OI-ju i ostalih matematičkih zadataka, koja ujedno odražava bit OI-ja, jest u tome što u OI-ju težište često nije na tome **koji** je odgovor, nego kako **ubrzati** njegovo računanje. Ako je težište zadatka na „kako izračunati” umjesto na „kako brzo izračunati”, takav matematički zadatak u pravilu nije prikladan za OI.

> Dio neuobičajenih zadataka uključuje gradivo sveučilišne fizike, zbog čega su natjecatelji suočeni s fizikalnim pojmovima s kojima se nikad nisu susreli bespomoćni, što stvara barijeru u znanju.
>
> — [王天懿, „论偏题的危害” (O štetnosti neuobičajenih zadataka)][2]

Klasičan primjer: [„清华集训 2015” 多边形下海](https://uoj.ac/problem/159)

Ne samo fizika: OI zadaci ne bi smjeli previše zadirati u znanja iz drugih područja, a ako zadiru, treba dati detaljno objašnjenje; znanje iz drugih područja ne smije biti velika prepreka rješavanju.

> Dobar zadatak, bez obzira na težinu, treba imati vlastitu misaonu težinu i zahtijevati od natjecatelja da razmisli i otkrije neka svojstva.
>
> Kod dobrog zadatka može biti dug, ali nikako ne zato što je dužina nasilno postignuta ugnježđivanjem ili dodavanjem uvjeta, nego prirodno, tako da čovjek osjeća da kod tog zadatka jednostavno treba biti toliko dug.
>
> — [王天懿, „论偏题的危害” (O štetnosti neuobičajenih zadataka)][2]

Klasični primjeri: [„SDOI2010” 猪国杀](https://loj.ac/problem/2885), [„集训队互测 2015” 未来程序·改](https://uoj.ac/problem/98)

Na običnim OI natjecanjima misaona težina trebala bi činiti glavni dio. Naravno, inženjerski zadaci poput onih s Day 2+ na THUWC/THUSC također imaju svoje opravdanje – cilj tih kampova, osim provjere sposobnosti natjecatelja da osmisle algoritme, jest i povezivanje sa sveučilišnim učenjem, inženjerskim kodom i čitanjem dokumentacije. No na običnim OI natjecanjima više bi se trebale provjeravati sposobnost osmišljavanja algoritama i razmišljanje.

## Tekst zadatka

### Pisanje formula u LaTeX-u

Na internetu postoji mnogo LaTeX tutorijala, npr.:

-   [Uvod u LaTeX](../tools/latex.md#图表)
-   [Zbirka LaTeX matematičkih formula](https://www.luogu.com.cn/blog/IowaBattleship/latex-gong-shi-tai-quan)
-   [Razne LaTeX naredbe i simboli](https://blog.csdn.net/anxiaoxi45/article/details/39449445)

Pri upotrebi obratite pozornost na [zahtjeve za oblikovanje LaTeX formula](../intro/format.md).

### Pozadina zadatka

Pozadina zadatka trebala bi biti što kraća. Ako je pozadina dulja, treba je odvojiti od opisa zadatka.

Apsolutno treba izbjeći da pozadina zadatka ozbiljno otežava razumijevanje zadatka.

Po potrebi se mogu ponuditi dvije inačice: opis zadatka povezan s pozadinom i sažeti opis zadatka.

### Opis zadatka

Ukratko, opis zadatka mora biti **jasan i razumljiv**.

Svaka definicija u tekstu koja bi mogla biti nerazumljiva mora biti objašnjena; ne smiju se niotkuda pojavljivati nedefinirani pojmovi. Na primjer: u [CF1172D Nauuo and Portals](https://codeforces.com/problemset/problem/1172/D) u tekstu morate objasniti što je „portal”.

Svaki pojam u tekstu treba opisivati jednim jedinim izrazom. Na primjer: ne smije se čas govoriti „trošak”, čas „cijena”.

Ne smiju se bez objašnjenja koristiti riječi u značenju različitom od izvornog ili uobičajenog. Na primjer: ne smije se bez objašnjenja „put” koristiti za brid.

Morate osigurati da tekst zadatka nije proturječan. Na primjer: u [CF1173A Nauuo and Votes](https://codeforces.com/problemset/problem/1173/A) "?" nije uvršten kao jedan od "result" zato što "?" znači "there are more than one possible results".

Morate osigurati da se tekst ne može pogrešno protumačiti na dosljedan način, čak i ako je takvo tumačenje protivno zdravom razumu i nitko ne bi tako razmišljao. Na primjer: u [CF1172D Nauuo and Portals](https://codeforces.com/problemset/problem/1172/D) razlog zbog kojeg se opširno definira "walk into" i razlikuje od "teleport" jest sprječavanje tumačenja: kroz portal se dolazi do drugog portala, a dolaskom na portal se teleportira, pa bi se beskonačno skakalo naprijed-natrag.

Čitajući opis zadatka redom, trebalo bi razumjeti svaku rečenicu te shvatiti zadaću i zahtjeve zadatka. Nedoumica bi se trebala razjasniti barem u sljedećem odlomku, a ne tek nekoliko odlomaka kasnije, ili tek nakon čitanja formata ulaza i izlaza, ili čak pogađanjem iz primjera. Na primjer: u [„GuOJ Round #1” 琪露诺的冰雪宴会](https://github.com/OI-wiki/problemset/blob/master/contest/online/GuOJ/OI%20Archive%20-%20GuOJ1171.pdf) cilj zadatka, „najveća količina vode koju Jezero magle na kraju može primiti”, prvi se put pojavljuje tek u formatu izlaza, a uz zavaravajuću rečenicu „Reimu naravno može brzo izračunati koliki je ukupni trošak čišćenja svih potoka” još je lakše pogrešno shvatiti zadatak; to nije prihvatljivo – cilj zadatka treba objasniti već u opisu zadatka. (U ovom primjeru postoji i problem da pozadina ozbiljno otežava razumijevanje zadatka.) Ista se greška pojavljuje i u [CF1423(4)N Bubblesquare Tokens](https://codeforces.com/problemset/problem/1423/N), gdje se cilj zadatka, "friend pairs and number of tokens each of them gets on behalf of their friendship", prvi put pojavljuje tek u formatu izlaza.

### Format ulaza i izlaza

Dovoljno je da format ulaza i izlaza bude jasan i **potpun**; nema krutih pravila. Osobno preporučujem pisati format ulaza i izlaza po uzoru na zadatke s CF-a; vidi [Upute za autore zadataka na CF-u][3].

Radi lakšeg rješavanja u formatu ulaza i izlaza najbolje je objasniti konkretno značenje svake varijable, osim ako je značenje varijable vrlo dugačko i ne može se objasniti jednom rečenicom (tada se može napisati „značenje vidi u opisu zadatka”).

Posebno treba paziti: ako izlaz sadrži decimalne brojeve, po mogućnosti upotrijebite [SPJ](#special-judge) za ograničavanje veličine pogreške umjesto zahtjeva „zaokružite na x decimala”.

Zahtjev „zaokružite na x decimala” može tražiti beskonačnu preciznost. Na primjer: traži se zaokruživanje na tri decimale, a stvarni je odgovor $0.0015$; tada svaka, ma kako mala, pogreška zbog koje je izračunati odgovor manji od $0.0015$, pa makar bio $0.00149999\cdots$, daje pogrešan ispis.

Ako SPJ nije moguć, osigurajte da je zahtjev za preciznost konačan, npr.: ispišite odgovor zaokružen na tri decimale. Neka je točan odgovor $ans$; podaci jamče da za svaki $x$ koji zadovoljava $\frac{|x-ans|}{\max(1,ans)}<10^{-9}$ rezultat zaokruživanja jednak rezultatu zaokruživanja $ans$.

Nekoliko rečenica koje mogu poslužiti kao uzor:

```latex
Prvi redak ulaza sadrži tri prirodna broja $n$, $m$, $k$ ($1\le n,m\le 2\cdot 10^5$, $1\le k\le 100$) — $n$ je duljina niza, $m$ broj operacija, a značenje $k$ vidi u opisu zadatka.
```

```latex
Drugi redak ulaza sadrži $n$ nenegativnih cijelih brojeva $a_1,a_2,\ldots,a_n$ ($1\le a_i\le 10^9$) — niz zadan u zadatku.
```

```latex
$i$-ti od sljedećih $m$ redaka sadrži dva prirodna broja $l_i$ i $r_i$ ($1\le l_i\le r_i\le n$), što znači da se $i$-ta operacija izvodi na intervalu $[l_i,r_i]$.
```

```latex
Svaki od sljedećih $n-1$ redaka sadrži dva prirodna broja $u$ i $v$ ($1\le u,v\le n$), što znači da su $u$ i $v$ povezani bridom.

Podaci jamče da zadani bridovi čine stablo.
```

```latex
Jedini redak ulaza sadrži neprazan string sastavljen od malih slova engleske abecede, duljine najviše $10^6$.
```

```latex
Drugi redak ulaza sadrži realan broj $x$ ($-10^6\le x\le 10^6$) s najviše tri decimale, značenje vidi u opisu zadatka.
```

```latex
Izlaz sadrži jedan realan broj; vaš se izlaz smatra točnim ako je apsolutna ili relativna pogreška u odnosu na točan odgovor manja od $10^{-6}$.
```

```latex
Drugi redak izlaza sadrži $n$ prirodnih brojeva koji opisuju konstruirano rješenje — $i$-ti broj je oznaka $i$-te karte koju ste odigrali.

Ako postoji više ispravnih rješenja, ispišite bilo koje.
```

???+ note "Generiranje ulaznih podataka generatorom slučajnih brojeva u kodu natjecatelja"
    Kod nekih zadataka ulazni su podaci toliko veliki da se, kako učitavanje ne bi predugo trajalo, od natjecatelja traži da podatke generiraju u kodu zadanim generatorom umjesto učitavanja sa standardnog ulaza ili iz datoteke.
    
    Ovaj pristup treba pažljivo razmotriti jer ima mnogo nedostataka:
    
    -   može unijeti slučajnost podataka koja za točno rješenje nije potrebna ili otežati konstruiranje podataka
    -   može otežati razumijevanje formata ulaza
    -   ako generator nije dobro enkapsuliran, već samo razumijevanje njegove upotrebe može biti teško
    -   ako natjecatelj ne koristi jezik koji autor preporučuje, možda mora sam napisati generator podataka
    
    Ovaj se pristup obično koristi da učitavanje ne bi predugo trajalo, pa je moguća zamjena podijeliti natjecateljima dovoljno brz predložak za [optimizaciju učitavanja i ispisa](./io.md), kako bi vrijeme učitavanja bilo što ujednačenije za sve; tada ni dugo učitavanje ne utječe na razlike u vremenu među natjecateljima. Drugo je rješenje zadatak oblikovati kao interaktivni zadatak s pozivima funkcija (umjesto I/O-a); čak i ako u algoritmu nema interakcije, interaktivni zadatak ujednačuje vrijeme učitavanja, a IOI je usvojio pristup da su svi zadaci interaktivni. No oba ova rješenja ograničavaju jezike koje natjecatelji mogu koristiti, pa autor mora ručno podržati svaki dopušteni jezik.
    
    Vraćajući se izvoru problema, vrijedi razmisliti i jesu li preveliki ulazni podaci uopće nužni, može li se cilj postići manjim ulazom te je li potrebno rušiti rješenja složenosti tek nešto lošije od točnog.

### Ograničenja podataka

Prema zahtjevima CF-a ograničenja podataka pišu se u formatu ulaza, ali se u Kini obično pišu na kraju zadatka.

Najčešća greška u ograničenjima jest nepotpunost. Svaki broj i svaki string u ulazu mora imati jasno određene granice. U gore navedenim primjerima formata ulaza i izlaza ima ispravno napisanih ograničenja.

Česti propusti u ograničenjima:

1.  „Cijeli” u „cijeli broj”.
2.  U tekstu piše samo „cijeli broj”, a ne „prirodan broj”, dok ograničenje ima samo gornju, a ne i donju granicu.
3.  Za string nije naveden skup znakova.
4.  Za realni broj nije naveden broj decimala.
5.  Za neke varijable nije zadan raspon.

Morate osigurati da službeno rješenje prolazi na **svakom skupu podataka** koji zadovoljava ograničenja iz teksta.

???+ note "O „jamči se da su podaci generirani slučajno”"
    U nekim zadacima stoji „jamči se da su podaci generirani slučajno”; često takvo ograničenje nije najbolje rješenje, jer „slučajno generirano” nije jasno ograničenje podataka i otežava procjenu stvarnih ograničenja i izradu hack podataka.
    
    U pravilu se „jamči se da su podaci generirani slučajno” može zamijeniti svojstvom podataka koje rješenje treba. Na primjer, slučajno generirano stablo često se može zamijeniti ograničenjem visine stabla.
    
    Ako se ipak mora jamčiti slučajno generiranje, treba navesti konkretan postupak generiranja. Na primjer, generira li se stablo slučajnim odabirom roditelja ili slučajnim generiranjem Prüferova niza.
    
    Treba napomenuti da se nedeterministički algoritmi razlikuju od algoritama koji ovise o slučajnosti podataka. Prvi za bilo koje podatke s velikom vjerojatnošću daju točan rezultat, dok drugi daju točan rezultat za većinu podataka, a za neke posebne podatke ga ne mogu dati.

### Primjeri

Primjeri trebaju imati određenu snagu i otkrivati neke jednostavne greške. Tko pogrešno shvati zadatak, trebao bi iz primjera moći uočiti da ga je pogrešno shvatio.

Kod zadataka s više vrsta operacija svaka se operacija treba pojaviti u primjeru.

Kod zadataka s više vrsta izlaza (npr. [CF1173A Nauuo and Votes](https://codeforces.com/problemset/problem/1173/A)) svaka se vrsta izlaza treba pojaviti u primjeru. Iznimka: zadaci u kojima se traži provjera postoji li rješenje, iako rješenje zapravo uvijek postoji.

### Objašnjenje primjera

Što je opis zadatka složeniji i teži za razumijevanje, to je potrebnije detaljno objašnjenje primjera.

Što je zadatak lakši, to je potrebnije detaljno objašnjenje primjera.

Detaljno objašnjenje primjera može se popratiti slikom.

Veliki primjeri ne moraju imati objašnjenje.

Iz obzira prema osobama s poremećajem raspoznavanja boja najbolje je da boja ne bude nužna za razumijevanje objašnjenja primjera. Slike u boji mogu uljepšati objašnjenje, ali ako se bojom mora prenijeti neka nužna informacija, bolje je izbjegavati istodobnu upotrebu crvene i žute ili crvene i zelene.

## Vremensko i memorijsko ograničenje te djelomični bodovi

Svrha vremenskog i memorijskog ograničenja jest srušiti rješenja pogrešne složenosti. (Naravno, i spriječiti predugo ocjenjivanje; npr. i interaktivni zadaci koji ograničavaju samo broj interakcija, a ne vremensku složenost, imaju vremensko ograničenje.)

Zato bi načelno vremensko ograničenje trebalo biti što veća vrijednost koja još ne propušta pogrešna rješenja.

Općenito, vremensko ograničenje treba zadovoljavati:

1.  Barem dvostruko vrijeme izvođenja std-a u najgorem slučaju.
2.  Ako natjecanje dopušta Javu, Java mora moći proći.
3.  Ne smije propustiti pogrešna rješenja (osim ako ih je nemoguće srušiti ili se neko pogrešno rješenje namjerno želi propustiti).

Da bi se istodobno propustila rješenja s velikom konstantom i srušila pogrešna, obično se mogu povećati i ograničenja podataka i vremensko ograničenje. No pazite: ponekad točno rješenje (zbog cachea i sličnih „mističnih” razloga) pri povećanju ograničenja dobiva golemo povećanje konstante, pa povećanje ograničenja ne mora povećati razliku u vremenu između točnog i pogrešnog rješenja.

U formatima s djelomičnim bodovima mogu se dodati i stupnjevani podaci ili podaci s nešto manjim ograničenjima, tako da bolja pogrešna rješenja i točna rješenja s velikom konstantom ne prolaze u cijelosti, ali dobivaju visoke djelomične bodove.

Treba napomenuti da pri ograničenjima manjim od $5\cdot 10^5$ treba razmotriti može li se zadatak proći [instrukcijskim skupovima](https://ouuan.github.io/post/n方过百万-暴力碾标算——指令集优化的基础使用).

U pravilu memorijsko ograničenje treba postaviti dovoljno velikim, osim ako je rješenje bolje prostorne složenosti doista toliko domišljato da se isplati srušiti rješenja veće prostorne složenosti. U tom se slučaju može razmotriti djelomični bod s blažim memorijskim ograničenjem. Vrijedi napomenuti da zadaci sa strukturama podataka obično trebaju veće memorijsko ograničenje ako se ne žele srušiti rješenja s velikom potrošnjom memorije.

> Dobar zadatak treba imati selekcijsko svojstvo, dovoljnu razlučivost. Treba imati barem 4 stupnja djelomičnih bodova, kako bi početnici mogli osvojiti bodove, a napredni pokazati svoju snagu.
>
> — vfk, „UOJ 精神之源流” (Izvor duha UOJ-a)

Djelomični se bodovi obično dijele na manja ograničenja podataka i posebna svojstva.

Manja ograničenja obično treba podijeliti u više stupnjeva; čak i ako se ne možete sjetiti rješenja neke složenosti, možete razmotriti da toj složenosti dodijelite stupanj. U pravilu, da bi se izbjeglo rušenje na konstanti, može se postaviti stupanj s najvećim podacima podijeljenima s dva.

„Stupnjevane podatke” bolje je zamijeniti s više stupnjeva djelomičnih bodova.

Djelomični bodovi za posebna svojstva ovise o konkretnom zadatku. Idealni djelomični bodovi za posebna svojstva trebali bi natjecatelja voditi prema točnom rješenju. Za razliku od djelomičnih bodova za manja ograničenja, ako ne znate rješenje za neko posebno svojstvo, bolje je tom svojstvu ne dodjeljivati stupanj. Na primjer: stupanj $k=1$ u [„CTS2019” 随机立方体](https://loj.ac/problem/3119) mnogi su na raspravi rješenja kritizirali, govoreći da ometa razmišljanje o točnom rješenju.

Ako se zadatak boduje drugačije od uobičajenog (npr. vezani subtaskovi na natjecanju u uobičajenom OI formatu), to se obavezno mora navesti u tekstu zadatka.

Ne preporučuje se formulacija „XX % podataka zadovoljava XX”, osobito kad ograničenja uključuju više varijabli. Na primjer, „$30\%$ podataka zadovoljava $n \le 1000$” i „$40\%$ podataka zadovoljava $m \le 100$” mogu opisivati svojstva $70\%$ podataka, a mogu i samo $40\%$. U pravilu su subtaskovi ili tablica ograničenja bolji izbor.

## Izrada testnih podataka

Generiranje podataka nužan je korak u sastavljanju zadatka, a nužno je i za stress testiranje; svladavanjem nekih tehnika generiranja podataka postupak postaje lakši, a podaci jači.

### Generiranje slučajnih podataka

#### Generiranje slučajnih brojeva

Vidi stranicu [Funkcije za slučajne brojeve](../misc/random.md).

Posebno upozorenje: pri generiranju brojeva iz raspona većeg od povratne vrijednosti funkcije za slučajne brojeve **nemojte** pisati `rand() * rand()` i slično; tako generirani slučajni brojevi vrlo su neravnomjerni.

Osim toga, pri sastavljanju zadataka preporučuje se podatke generirati pomoću [testliba](../tools/testlib/generator.md), koji jamči da isto sjeme na različitim platformama daje iste slučajne brojeve, a sjeme se automatski generira iz argumenata naredbenog retka.

#### Generiranje slučajne permutacije

Može se upotrijebiti funkcija `std::shuffle` iz STL-a, u obliku `std::shuffle(a, a + n, rng)`, gdje je `rng` generator slučajnih brojeva, npr. `std::mt19937 rng(std::chrono::steady_clock::now().time_since_epoch().count())`.

**Nemojte** koristiti `std::random_shuffle`; zastario je u C++14, a uklonjen u C++17.

#### Generiranje slučajnog intervala

Česta pogrešna metoda: slučajno generirati lijevi kraj $l$ iz $[1,n]$, a zatim desni kraj $r$ iz $[l, n]$. Tako generirani intervali bit će pomaknuti udesno.

Približno ispravna metoda (preporučena): slučajno generirati dva broja iz $[1, n]$, manji uzeti kao lijevi, a veći kao desni kraj.

Doista uniformno slučajna metoda: generirati slučajan broj $x$ iz $[0, n]$; ako je $x = 0$, generirati slučajan broj $y$ iz $[1, n]$ i interval je $[y, y]$; inače generirati prema „približno ispravnoj metodi”.

#### Generiranje slučajnog stabla

Uobičajena je metoda za svaki vrh $i$ od $2\sim n$ slučajno odabrati roditelja iz $[1,i-1]$. Tako generirano stablo nije uniformno slučajno, a očekivana visina je $O(\log n)$.

Postoji i ova slučajna metoda: roditelja vrha $i$ slučajno odabrati iz $[i\cdot low, i\cdot high]$. Uz dobro odabrane $low$ i $high$ mogu se napraviti razmjerno jaka stabla.

Doista uniformno slučajna metoda koristi [Prüferov niz](../graph/prufer.md): najprije se generira slučajan Prüferov niz, a zatim iz njega stablo. Očekivana visina stabla tada je $O(\sqrt n)$.

Osim toga, može se generirati slučajna permutacija za prenumeriranje vrhova / miješanje redoslijeda bridova.

### Konstruiranje podataka

#### Zadaci s intervalima

Uobičajene konstrukcije: vrlo kratke duljine (posebno: sve jednočlane točke), vrlo velike duljine (posebno: sve cijeli niz).

#### Zadaci koji zahtijevaju rastav na faktore

Što više prostih faktora s ponavljanjem: potencije broja $2$.

Što više različitih prostih faktora: umnožak nekoliko najmanjih prostih brojeva.

Što više djelitelja: vidi niz [A002182](http://oeis.org/A002182) na OEIS-u.

#### Zadaci koji zahtijevaju najveći zajednički djelitelj

Ako su dva broja čiji se najveći zajednički djelitelj traži susjedni članovi [Fibonaccijeva niza](../math/combinatorics/fibonacci.md), Euklidov algoritam postiže najgoru vremensku složenost.

#### Problemi na stablima

Uobičajene konstrukcije:

-   lanac
-   zvijezda
-   potpuno binarno stablo
-   potpuno binarno stablo u kojem je svaki vrh zamijenjen lancem duljine $\sqrt n$
-   zvijezda s obješenim lancem
-   lanac s obješenim pojedinačnim vrhovima
-   stablo visine $d$, $d>1$, čiji korijen ima dva djeteta: lijevo podstablo je lanac duljine $d-1$, a desno podstablo takvo stablo visine $d-1$.

Izvan natjecanja mogu se pomoću [Tree-Generatora](https://github.com/ouuan/Tree-Generator) generirati najrazličitija stabla.

### Skupno generiranje podataka

Autor preporučuje metodu argumenata naredbenog retka + bat/sh.

Na primjer:

`gen.cpp`:

```cpp
#include "testlib.h"

using namespace std;

int n, m, k;
vector<int> p;

int main(int argc, char* argv[]) {
  registerGen(argc, argv, 1);

  int i;

  n = atoi(argv[1]);
  m = atoi(argv[2]);
  k = rnd.next(1, n);

  for (i = 1; i <= n; ++i) p.push_back(i);

  shuffle(p.begin(), p.end());
  // shuffle koristi rnd.next()

  printf("%d %d %d\n", n, m, k);
  for (i = 0; i < n; ++i) {
    printf("%d%c", p[i], " \n"[i == n - 1]);
    // string se koristi kao niz: razmak u sredini, novi red na kraju – čest trik pri generiranju podataka
  }

  return 0;
}
```

`gen_scripts.bat`:

```bat
gen 10 10 > 1.in
gen 1 1 > 2.in
gen 100 200 > 3.in
gen 2000 1000 > 4.in
gen 100000 100000 > 5.in
```

Prednost je što za različite podatke treba napisati samo jedan generator, a parametri pojedinog testa lako se mijenjaju.

### Zahtjevi za testne podatke

Podaci trebaju sadržavati najmanje i najveće vrijednosti svih parametara.

Podaci trebaju sadržavati razne rubne slučajeve.

Pri upotrebi subtaskova podaci (uključujući ulaz i izlaz) trebali bi pokriti sve dijelove raspona vrijednosti, a ne samo najveće vrijednosti ograničenja.

Da bi se spriječilo prolaženje posebnih provjera (if-ova) usmjerenih na posebne konstrukcije, u jednom se testu mogu kombinirati različite konstrukcije, ili većinu podataka činiti konstrukcijom uz manji dio slučajnih.

Podaci trebaju sadržavati najrazličitije konstrukcije, čak i ako ne znate koje bi pogrešno rješenje na njima palo. (U formatima s bodovanjem po testu to treba primjereno odvagnuti.)

Naravno, ako znate za neko (koje normalan čovjek može smisliti i napisati) pogrešno rješenje s problemom točnosti, nastojte ga srušiti.

Posebno upozorenje: ako postoji mogućnost prekoračenja cijelih brojeva, obavezno srušite rješenja koja prekoračuju. U formatima s djelomičnim bodovima onaj tko ne stavi long long ne bi smio dobiti jednako ili čak manje bodova od grube sile.

Ako postoje pretestovi, trebaju biti što jači (i istodobno što malobrojniji). Drugim riječima, pretestovi trebaju (sa što manje testova) obuhvatiti sve poznate zamke zadatka.

Ako želite malo, a ne nimalo FST-ova, ipak osigurajte jake pretestove, jer se na stvarnom natjecanju vrlo vjerojatno pojave greške koje niste predvidjeli, pa broj FST-ova daleko premaši očekivanja.

### Format podataka

Ovdje navodimo neke uobičajene zahtjeve za format ulaznih podataka, kao opću referencu:

> 1.  Koristite format novog reda testnog okruženja.
> 2.  Na kraju posljednjeg retka datoteke nalazi se znak novog reda, tj. posljednji znak cijele datoteke mora biti `\n`.
> 3.  Nijedan redak ne počinje ni ne završava bjelinom.
> 4.  Nema više od 1 uzastopnog razmaka.

Podaci generirani u Windows okruženju obično imaju novi red `\r\n`, dok glavni sustavi za ocjenjivanje rade na Linuxu s novim redom `\n`. Učitavanje podataka u Windows formatu na Linuxu može dovesti do neispravne obrade novog reda pri učitavanju stringova, pa program u različitim okruženjima daje različite rezultate; usporedba izlaza generiranog na Linuxu sa službenim izlazom generiranim na Windowsu može zbog različitog formata novog reda dati razlike. Da bi ponašanje programa bilo dosljedno, format novog reda svih podataka mora se pretvoriti u format okruženja u kojem se program izvodi.

Podaci s Linux formatom novog reda obično se mogu generirati ovako:

1.  Izravno generirati podatke u Linux okruženju.
2.  Pretvoriti ulazne i izlazne datoteke alatom [`dos2unix`](https://dos2unix.sourceforge.io/), koji je uključen u alate poput Cygwina i MinGW-a.
3.  Otvoriti izlaznu datoteku u binarnom načinu i koristiti `\n` kao novi red.
4.  Napisati vlastiti alat prema kodu `dos2unix.cpp` s [ove stranice](https://help.luogu.com.cn/manual/luogu/problem/testcase-format#附录windows-环境下造数据注意事项).

## Special Judge

[Tutorijal za pisanje SPJ-a](../tools/special-judge.md)

Zadaci s ispisom konstrukcije i zadaci s ispisom realnih brojeva dvije su češće vrste zadataka koje zahtijevaju SPJ; i drugi zadaci po potrebi trebaju SPJ. Na CF-u svi zadaci moraju koristiti checker temeljen na testlibu; npr. kad zadatak traži ispis nekoliko cijelih brojeva, koristi se ugrađeni testlib checker ncmp, pa natjecatelj može proizvoljno ispisivati bjeline (razmake ili nove redove).

Checker se obično piše pomoću testliba. Budući da checker mora obraditi najrazličitije neispravne izlaze i treba biti iznimno robustan, bez testliba je vrlo teško napisati dobar checker.

Pri pisanju checkera treba paziti na dvoje:

1.  Morate obraditi razne neispravne izlaze, pa provjerite je li svaka učitana varijabla u dopuštenom rasponu (`readInt(minvalue, maxvalue)`). Na primjer: pri učitavanju varijable koja se tijekom provjere koristi kao indeks niza obavezno provjerite raspon, inače može doći do prekoračenja granica niza, što ponekad uzrokuje RE, a ponekad može dati presudu AC.
2.  Načelno checker ne smije provjeravati bjeline (tj. ne smije koristiti `readSpace()`, `readEoln()`, `readEof()`; vrijedi spomenuti da testlib automatski provjerava ima li suvišnog ispisa).

## Službeno rješenje (editorial)

Cilj je službenog rješenja da ga razumiju svi koji bi mogli sudjelovati na natjecanju. Zato su zahtjevi za detaljnost službenog rješenja veći nego kod običnog rješenja.

### O djelomičnim bodovima

Kod zadataka s djelomičnim bodovima u rješenju se mogu opisati i rješenja za djelomične bodove.

### O potrebnim znanjima

Znanja upotrijebljena u rješenju treba jasno navesti. Za znanja čija je težina usporediva s težinom zadatka najbolje je dati materijale za učenje (npr. adresu bloga).

### O definicijama

U rješenju se pojmovi ne smiju pojavljivati niotkuda.

Na primjer: rješenje DP zadatka mora jasno objasniti definiciju stanja.

### O detaljima

Ako su konkretni detalji implementacije domišljati, najbolje ih je napisati; inače je prihvatljivo i „vidi kod”. Ako pišete „vidi kod”, najbolje je u kod dodati određene komentare.

### Službeni kod

Iz službenog koda najbolje je ukloniti suvišne dijelove. Na primjer, neka rješenja zadržavaju cijeli predložak s define-ima (radi brzine rješavanja sadrži mnogo define-a i često korištenih funkcija, uobičajen na online natjecanjima poput CF-a), od kojih velik dio nije upotrijebljen; to nije dobro.

Ako postoje detalji implementacije koji u rješenju nisu detaljno objašnjeni, najbolje je dodati primjerenu količinu komentara.

## Natjecanje

### Težina zadataka u najavi natjecanja mora biti istinita

> Remember that authors tend to underestimate the difficulty of their problems.
>
> — podsjetnik na stranici PROPOSE A PROBLEM na Codeforcesu

Autor zadataka vrlo vjerojatno pogrešno procjenjuje težinu zadataka, pa ako u najavi natjecanja želite navesti težinu, pažljivo razmislite i najbolje unaprijed zamolite nekoga da zadatke testira i procijeni.

### Raspodjela težine zadataka

Na probnim natjecanjima nalik kineskom OI-ju obično je dovoljno da ukupna težina triju zadataka odgovara težini natjecanja.

Na online natjecanjima nalik CF/ATC-u treba nastojati da težina raste (iako se zbog pogrešne procjene težine to često ne postigne) i izbjegavati velike skokove u težini (difficulty gap). Skok u težini može se smanjiti dijeljenjem zadatka na laku i tešku inačicu (dva subtaska), ali dijeljenje na subtaskove treba pažljivo razmotriti, jer mnogi ne vole subtaskove u CF formatu ([Are subtasks evil?](https://codeforces.com/blog/entry/71700)), iz razloga koji uključuju, ali nisu ograničeni na:

-   zbog formata natjecanja može biti povoljnije najprije riješiti easy version pa hard version, uz manji penal i veći ukupni rezultat
-   bodovanje subtaskova često nije razmjerno težini zadatka
-   easy version često nije valjan zadatak (nije zanimljiv)
-   rješenje easy versiona često ne pomaže u razmišljanju o točnom rješenju hard versiona

### Raspodjela tema zadataka

Natjecanje bi trebalo pokriti što širi raspon tema (osim, naravno, tematskih treninga).

Klasičan protuprimjer: CTS2019, koji je pokrio dinamičko programiranje, očekivanja, kombinatorno prebrojavanje, princip uključivanja-isključivanja, polinome i druge teme.

> Moram odabrati šest zadataka od pet, što da radim.
>
> — razlog koji je naveo sastavljač CTS2019: nije primljeno dovoljno prijedloga zadataka

## Platforme za sastavljanje zadataka

### Polygon

Polygon je vrlo moćna platforma za suradničko sastavljanje zadataka; može biti prvi izbor za suradničko sastavljanje za bilo koju stranicu (funkcijom package izvozi se na stranice koje ne podržavaju Polygon), a vrlo je dobar izbor i za samostalno sastavljanje (osobito na više uređaja). Upute vidi u [Uvodu u Polygon](../tools/polygon.md).

### Codeforces

Codeforces je jedna od najpoznatijih svjetskih stranica za algoritamska natjecanja, s visokom kvalitetom zadataka, vrlo prikladna za autore koji već imaju iskustva, žele dodatno unaprijediti vještinu sastavljanja i sastaviti kvalitetan skup zadataka. Nedostatak je sporo recenziranje (obično nekoliko mjeseci), ali pripremu zadataka možete započeti već tijekom recenzije (uz rizik da zadatak bude odbijen i priprema propadne).

#### Uvjeti za sastavljanje zadataka

-   plavi rejting i sudjelovanje na barem 25 ocjenjivanih (rated) natjecanja;
-   ljubičasti rejting i sudjelovanje na barem 15 ocjenjivanih natjecanja;
-   narančasti rejting i sudjelovanje na barem 5 ocjenjivanih natjecanja;
-   crveni ili crno-crveni rejting.

#### Podnošenje prijave natjecanja

Kad steknete uvjete, u bočnoj traci vidjet ćete gumb [Propose a contest/problems](http://codeforces.com/proposals/new-contest).

Nakon što ga otvorite, najprije napišite contest proposal (u PROPOSE A CONTEST), a zatim problem proposale i dodajte ih u natjecanje.

Kad su zadaci odlučeni, contest proposal možete otvoriti za recenziju (open to review).

#### Priprema zadataka na Polygonu

Vidi [Uvod u Polygon](../tools/polygon.md).

#### Komunikacija s koordinatorima

Komunikacija s koordinatorima ima dvije svrhe:

1.  Ubrzati recenziju.
2.  Nakon ulaska u fazu pripreme koordinatori daju savjete i pomoć.

Službeni je način komunikacije podnošenje prijave u obliku proposala u proposal systemu; nakon što koordinator započne recenziju, rasprava se vodi komentarima ispod proposala.

U praksi, ako proposal dugo ne prolazi recenziju, možete razmotriti privatnu poruku koordinatoru (na CF-u doduše piše "Don't send private messages or emails to coordinators", ali je 300iq u [komentaru](http://codeforces.com/blog/entry/64077#comment-478933) rekao da mu se može pisati privatno).

### Comet OJ

[Poveznica na Comet OJ](https://www.cometoj.com/)

Više nije aktivan (do studenoga 2021. posljednje je natjecanje bilo u siječnju 2020.).

Prijava za sastavljanje zadataka: <https://info.cometoj.com/contests/Questionnaire_IssuerInfo/>

### CodeChef

Indijska platforma za algoritamska natjecanja s tri formata: Long Challenge od 10 dana s challenge zadatkom, Cook-Off od 2,5 h nalik ICPC-u i LunchTime od 3 h nalik IOI-ju.

FAQ za autore: <https://www.codechef.com/wiki/faq-problem-setters>

Vodič za sastavljanje: <https://www.codechef.com/problemsetting>

### AtCoder

Japanska platforma za algoritamska natjecanja; kontakt za sastavljanje zadataka: `contest@atcoder.jp`.

### UOJ & LOJ

Kineski OJ-evi s malo natjecanja.

### Luogu

Sudionici u sastavljanju zadataka moraju imati određenu razinu potvrđenih nagrada; nakon stvaranja natjecanja odgovorna osoba podnosi zahtjev u [sustavu zahtjeva](https://www.luogu.com.cn/ticket).

Pravila javnih natjecanja: <https://help.luogu.com.cn/rules/academic/opencontest-standard>

## Reference

1.  [vfk, „UOJ 精神之源流” (Izvor duha UOJ-a)][1]

2.  [王天懿, „论偏题的危害” (O štetnosti neuobičajenih zadataka)][2]

3.  [Upute za autore zadataka na CF-u][3] ([inačica u obliku slike dostupna u Kini](https://github.com/OI-wiki/libs/blob/master/topic/rules.jpg))

4.  [Samousavršavanje autora zadataka na CF-u][4]

Ovaj je tekst autor prenio iz [ouuanovih pravila za sastavljanje zadataka](https://ouuan.github.io/post/ouuan-的出题规范/) uz izmjene i dopune.

[1]: https://vfleaking.blog.uoj.ac/blog/909 "vfk《UOJ 精神之源流》"

[2]: https://github.com/OI-wiki/libs/blob/master/topic/7-%E7%8E%8B%E5%A4%A9%E6%87%BF-%E8%AE%BA%E5%81%8F%E9%A2%98%E7%9A%84%E5%8D%B1%E5%AE%B3.ppt "王天懿《论偏题的危害》"

[3]: https://docs.google.com/document/d/e/2PACX-1vRhazTXxSdj7JEIC7dp-nOWcUFiY8bXi9lLju-k6vVMKf4IiBmweJoOAMI-ZEZxatXF08I9wMOQpMqC/pub "CF 出题人须知"

[4]: https://github.com/OI-wiki/libs/blob/master/topic/CF%E5%87%BA%E9%A2%98%E4%BA%BA%E7%9A%84%E8%87%AA%E6%88%91%E4%BF%AE%E5%85%BB.md "CF 出题人的自我修养"
