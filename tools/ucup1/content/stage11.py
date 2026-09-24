# -*- coding: utf-8 -*-
STAGE = {
    'no': 11,
    'name': 'Stage 11: Shanghai',
    'source_name': 'The 2022 ICPC Asia East Continent Final Contest, EC-Final 2022',
    'source_html': r'''
<p>Prijevod službenog kratkog rješenja sudačkog tima EC-Final 2022 (EC Final 2022 裁判组): <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1197&amp;r=2">Tutorial (zh-cn)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1197&amp;r=1">engleskim tekstovima zadataka</a>. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1197">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Coloring', 'title_hr': 'Bojanje', 'slug': 'A_coloring',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je $n$ elemenata numeriranih od $1$ do $n$. Element $i$ ima vrijednost $w_i$ i boju $c_i$, a osim toga ima i pokazivač $a_i$ na neki drugi element ($a_i \ne i$).</p>
<p>Na početku je boja elementa $s$ jednaka $1$, a boja svih ostalih elemenata je $0$. Operaciju</p>
<ul>
    <li>postavi $c_i \leftarrow c_{a_i}$ uz cijenu $p_i$</li>
</ul>
<p>smiješ izvesti proizvoljno mnogo puta, za bilo koje $i$. Tvoj rezultat jednak je zbroju vrijednosti svih elemenata koji na kraju imaju boju $1$, umanjenom za zbroj cijena svih izvedenih operacija. Odredi najveći mogući rezultat.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži cijele brojeve $n$ i $s$ ($1 \le s \le n \le 5 \cdot 10^3$). Drugi redak sadrži $w_1, \dots, w_n$ ($-10^9 \le w_i \le 10^9$), treći $p_1, \dots, p_n$ ($0 \le p_i \le 10^9$), a četvrti $a_1, \dots, a_n$ ($1 \le a_i \le n$, $a_i \ne i$).</p>
<h3>Izlaz</h3>
<p>Ispiši jedan cijeli broj — najveći mogući rezultat.</p>
<h3>Primjer</h3>
<p>Za $n = 3$, $s = 1$, $w = [-1, -1, 2]$, $p = [1, 0, 0]$, $a = [3, 1, 2]$ odgovor je $1$: redom izvedemo operacije na elementima $2, 1, 3, 2$ i dobijemo $c = [0, 0, 1]$ uz ukupnu cijenu $p_2 + p_1 + p_3 + p_2 = 1$, pa je rezultat $w_3 - 1 = 1$.</p>
''',
    'hints': [
        r'''<p>Svaki element ima točno jedan izlazni brid $i \to a_i$, pa graf pokazivača čini <em>funkcijski graf</em>: svaka komponenta je ciklus na koji su „nakačena” stabla. Boja se kroz operacije širi samo u smjeru suprotnom od pokazivača — od $a_i$ prema $i$.</p>''',
        r'''<p>Promatraj kako se boje mijenjaju duž ciklusa u vremenu: boja $1$ počinje u $s$ i može putovati oko ciklusa, a iza nje po želji „gasimo” elemente natrag na $0$. Tako svaki element ciklusa doživi niz izmjena $0 \to 1 \to 0 \to 1 \dots$; broj takvih izmjena je ključan parametar.</p>''',
        r'''<p>U podstablu koje visi na čvoru ciklusa svaki čvor može preuzeti boju roditelja u trenutku kad mu odgovara. Ako podstablo želi iskoristiti $k$ „slojeva” izmjena (npr. neki potomci boje $1$, neki $0$, pa opet $1$ …), ciklus se na tom mjestu mora promijeniti barem $k$ puta. Definiraj DP po podstablima: najbolji rezultat uz najviše $k$ izmjena.</p>''',
    ],
    'coach': [
        ('Opažanje: struktura grafa', r'''
<p>Bridovi $i \to a_i$ s uvjetom $a_i \ne i$ daju svakom čvoru točno jedan izlazni brid, dakle svaka slaba komponenta je <em>ciklus s pridruženim stablima</em> (基环树). Boja se prenosi iz $a_i$ u $i$, tj. s ciklusa prema listovima i oko ciklusa. Samo komponenta koja sadrži $s$ ikad može dobiti boju $1$.</p>'''),
        ('Redukcija: što se događa na ciklusu', r'''
<p>U svakom trenutku ciklus se sastoji od jednog susjednog bloka jedinica i bloka nula (ili je jednobojan). Operacije na ciklusu pomiču granice tih blokova. Ako pratimo fiksni čvor ciklusa kroz vrijeme, on prolazi kroz niz izmjena boje; svaka izmjena na svakom čvoru košta $p_i$. Neka je $k$ ukupan broj „prolazaka” bloka jedinica oko ciklusa.</p>
<p>Podstablo koje visi na čvoru $v$ ciklusa vidi boju $v$ kao vremenski niz $0, 1, 0, 1, \dots$; svaki čvor podstabla može u bilo kojem trenutku preuzeti <em>trenutnu</em> boju svog roditelja, pa raspored boja u podstablu na kraju odgovara podjeli podstabla na „slojeve” po vremenu izmjene.</p>'''),
        ('Algoritam: DP po podstablima, pa DP po ciklusu', r'''
<p><strong>Podstabla.</strong> Za svaki čvor $v$ izvan ciklusa izračunaj $f_v[k]$ — najbolji doprinos podstabla čvora $v$ (vrijednosti čvorova boje $1$ minus cijene operacija) ako roditelj čvora $v$ tijekom vremena promijeni boju najviše $k$ puta. Dijete može ili ignorirati roditelja (ostaje $0$, doprinos $0$ i ne treba mu nijedna izmjena) ili preuzeti boju u nekom od $k$ trenutaka; spajanje djece je zbrajanje po $k$, ukupno $O(n^2)$ stanja jer je $k \le n$.</p>
<p><strong>Ciklus.</strong> Fiksiraj broj izmjena $k$ na ciklusu i položaj bloka jedinica na kraju (koji susjedni segment ciklusa ostaje obojen); doprinos čvora ciklusa je zbroj $f$-vrijednosti njegovog podstabla uz odgovarajući broj izmjena minus cijena vlastitih izmjena. Enumeraciju završnog segmenta ubrzaj prefiksnim zbrojevima ili jednostavnim DP-om duž ciklusa.</p>'''),
        ('Složenost', r'''<p>DP po podstablima s $O(n)$ vrijednosti $k$ po čvoru i enumeracija na ciklusu daju ukupno $O(n^2)$, što je za $n \le 5000$ sasvim dovoljno.</p>'''),
    ],
    'solution': r'''
<p>Graf u kojem svaki element pokazuje na točno jedan drugi element je funkcijski graf: svaka komponenta je jedan ciklus na koji su pridružena stabla (<em>ciklus sa stablima</em>). Boja se operacijom $c_i \leftarrow c_{a_i}$ prenosi s elementa $a_i$ na element $i$, dakle iz smjera ciklusa prema listovima, odnosno oko ciklusa.</p>
<p>Promotrimo ciklus. Nakon svake operacije ciklus se sastoji od jednog neprekinutog bloka jedinica i jednog bloka nula; operacije pomiču granice tih blokova, pa svaki čvor ciklusa kroz vrijeme doživljava niz izmjena boje $0 \to 1 \to 0 \to \dots$. Kako se blok jedinica vrti oko ciklusa, i podstabla „nakačena” na čvorove ciklusa postaju slojevita: čvor podstabla preuzima boju roditelja u trenutku koji mu odgovara, pa se podstablo dijeli na slojeve prema tome u kojoj je izmjeni koji čvor preuzeo boju.</p>
<p>Ako podstablo neki čvora ciklusa iskorištava najviše $k$ slojeva (izmjena), tada se boja tog čvora ciklusa mora promijeniti barem $k$ puta. Zato najprije napravimo <strong>DP po podstablima</strong>: za svaki čvor izvan ciklusa pamtimo najbolji doprinos podstabla za svaki dopušteni broj izmjena boje roditelja, uzimajući u obzir vrijednosti $w$ čvorova koji završe s bojom $1$ i cijene $p$ svih izvedenih operacija.</p>
<p>Zatim promatramo ciklus: enumeriramo koji susjedni segment ciklusa na kraju ostaje obojen jedinicom i koliko se puta boja oko ciklusa izmijenila; svaki čvor ciklusa doprinosi vrijednošću svog podstabla za taj broj izmjena umanjenom za cijenu vlastitih izmjena. Dio u kojem enumeriramo završni segment jedinica ubrzamo prefiksnim zbrojevima ili DP-om duž ciklusa.</p>
<p>Ukupna složenost je $O(n^2)$.</p>
''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Binary String', 'title_hr': 'Binarni niz', 'slug': 'B_binary_string',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je binarni niz $a_0 a_1 \dots a_{n-1}$ raspoređen u krug. Svake sekunde istodobno se svaki par $01$ zamijeni u $10$: ako je $a_i = 0$ i $a_{(i+1) \bmod n} = 1$, ta se dva znaka zamijene. Primjerice, $100101110$ prelazi u $001010111$.</p>
<p>Koliko će se različitih nizova pojaviti tijekom beskonačno mnogo sekundi (uključujući početni)? Odgovor ispiši modulo $998244353$. Nizovi se uspoređuju po pozicijama, pa ciklički pomaci niza mogu biti međusobno različiti nizovi.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 10^6$). Svaki testni primjer je jedan binarni niz. Zbroj duljina svih nizova ne prelazi $10^7$.</p>
<h3>Izlaz</h3>
<p>Za svaki testni primjer ispiši traženi broj u zasebnom retku.</p>
<h3>Primjer</h3>
<p>Za nizove $1$, $001001$ i $0001111$ odgovori su redom $1$, $3$ i $9$.</p>
''',
    'hints': [
        r'''<p>Umjesto pojedinačnih znakova promatraj <em>blokove</em> jednakih znakova. Što se u jednoj sekundi dogodi s blokom nula duljine $\ge 2$ okruženim izmjeničnim $0101\dots$? A s blokom jedinica?</p>''',
        r'''<p>Blok nula putuje ulijevo, blok jedinica udesno, a kad se sudare oba se skrate za $1$. Proces se stabilizira kad više nema blokova duljine $\ge 2$ jednog od znakova; nakon toga se niz samo ciklički pomiče. Odgovor je (broj koraka do stabilizacije) + (najmanji period završnog niza).</p>''',
        r'''<p>Pretpostavi da jedinica ima barem koliko i nula. Kao u zadatku o balansiranim zagradama, postoji početna točka kruga od koje u svakom prefiksu jedinica ima barem koliko i nula — od nje se za svaki blok nula može izračunati kad nestaje (stog).</p>''',
    ],
    'coach': [
        ('Opažanje: dinamika blokova', r'''
<p>Uzmi blok nula duljine $\ge 2$ u okruženju $\dots 0101\,000000\,101 \dots$. Nakon jedne sekunde dobivamo $\dots 1010\,000000\,1010 \dots$: cijeli se blok pomaknuo za jedno mjesto ulijevo, a izmjenični dio oko njega samo se „prebacio”. Simetrično, blok jedinica pomiče se udesno.</p>
<p>Ako su blok jedinica i blok nula susjedni, npr. $\dots 0\,1111\,0000\,1 \dots \to \dots 1\,0111\,0001\,0\dots$, oni se „sudare” i oba se skrate za jedan znak.</p>'''),
        ('Redukcija: kad proces postaje periodičan', r'''
<p>Sudari se ponavljaju sve dok postoje i blokovi nula i blokovi jedinica duljine barem $2$. Kad nestanu svi blokovi jednog od znakova (recimo nula, ako je jedinica barem toliko koliko i nula), niz se u svakoj sljedećoj sekundi samo ciklički pomiče. Odgovor je zato: broj različitih nizova tijekom faze sudara plus najmanji period završnog niza (broj različitih cikličkih pomaka).</p>'''),
        ('Algoritam', r'''
<p>Neka jedinica ima barem koliko i nula (inače zamijeni uloge simetrično). Pronađi početnu točku kruga takvu da u svakom prefiksu blokovi jedinica imaju ukupnu duljinu barem toliku kao blokovi nula — postoji po istom argumentu kao za ciklički pomak niza zagrada. Krenuvši od nje, stogom uparuj blokove nula s blokovima jedinica koji ih „gutaju” i izračunaj trenutak nestanka svakog bloka nula; maksimum tih trenutaka je trajanje prve faze. Iz istog postupka dobiješ konačni niz nakon nestanka svih blokova nula. Njegov najmanji period izračunaj KMP-om (prefiksna funkcija) ili Z-algoritmom.</p>'''),
        ('Složenost', r'''<p>Sve je linearno: $O(n)$ po testnom primjeru, ukupno $O(\sum n)$ uz brzo čitanje ulaza (do $10^7$ znakova).</p>'''),
    ],
    'solution': r'''
<p>Promotrimo neprekinuti blok nula duljine veće od $1$, primjerice $\dots 0101000000101 \dots$. Nakon jedne sekunde on prelazi u $\dots 1010000001010 \dots$, što znači da se cijeli blok nula pomaknuo za jedno mjesto ulijevo. Analogno se blok jedinica duljine veće od $1$ pomiče za jedno mjesto udesno.</p>
<p>Ako su blok jedinica i blok nula susjedni, npr. $\dots 0111100001 \dots \to \dots 1011100010 \dots$, dva bloka se sudaraju i svakom se duljina smanji za $1$.</p>
<p>Taj se proces nastavlja dok postoje i blokovi nula i blokovi jedinica (duljine barem $2$). Bez smanjenja općenitosti pretpostavimo da je ukupna duljina blokova jedinica barem tolika kao ukupna duljina blokova nula. Tada postoji početna pozicija na krugu takva da u svakom prefiksu ukupna duljina blokova jedinica nije manja od ukupne duljine blokova nula. Krenuvši od te pozicije možemo za svaki blok nula izračunati u kojem trenutku nestaje, a time i niz koji nastaje nakon što nestanu svi blokovi nula. Od tog trenutka niz se samo ciklički pomiče, pa je preostalo izračunati najmanji period završnog niza: broj različitih nizova jednak je broju sekundi do stabilizacije uvećanom za taj najmanji period.</p>
<p>Vremenska složenost je $O(n)$.</p>
''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Best Carry Player 2', 'title_hr': 'Najbolji igrač s prijenosom 2', 'slug': 'C_best_carry_player_2',
    'tl': '4 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dan je pozitivan cijeli broj $x$. Pronađi najmanji pozitivan cijeli broj $y$ takav da pri pisanom zbrajanju $x + y$ u dekadskom sustavu (znamenku po znamenku, kao u osnovnoj školi) nastane točno $k$ prijenosa.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 10^5$). Svaki testni primjer sadrži dva cijela broja $x$ i $k$ ($1 \le x < 10^{18}$, $0 \le k \le 18$).</p>
<h3>Izlaz</h3>
<p>Za svaki testni primjer ispiši traženi $y$, ili $-1$ ako rješenje ne postoji.</p>
<h3>Primjer</h3>
<p>Za $x = 12345678$ i $k = 0, 5, 18$ odgovori su $1$, $54322$ i $999999999987654322$; za $x = 990099$, $k = 5$ odgovor je $9910$.</p>
''',
    'hints': [
        r'''<p>Prijenos na nekoj poziciji ovisi samo o znamenkama $x$ i $y$ na toj poziciji i o tome je li došao prijenos s niže pozicije. To je klasična postavka za <em>DP po znamenkama</em>.</p>''',
        r'''<p>Najmanji $y$ znači: što manje znamenki, a zatim leksikografski najmanje od najviše znamenke. Za svako stanje (pozicija, broj dosad ostvarenih prijenosa, dolazi li prijenos) pamti najmanju vrijednost sufiksa $y$ koja ga ostvaruje.</p>''',
        r'''<p>Pazi na rubne slučajeve: $y$ mora biti pozitivan (poseban slučaj $k = 0$ kad $x$ završava nizom devetki), a odgovor može premašiti $10^{18}$ — npr. $x = 10^{17}$, $k = 18$. Ukloni završne nule iz $x$ ili koristi 128-bitne cijele brojeve.</p>''',
    ],
    'coach': [
        ('Opažanje: lokalnost prijenosa', r'''<p>Na poziciji $i$ prijenos nastaje ako je $x_i + y_i + c_{\text{in}} \ge 10$. Odluka za znamenku $y_i$ utječe na ostale pozicije samo preko jednog bita — prijenosa prema višoj poziciji. Ukupan broj prijenosa je zbroj po pozicijama, pa je prirodno stanje DP-a: (pozicija, dosad ostvareni prijenosi, ulazni prijenos).</p>'''),
        ('Redukcija: minimizacija po znamenkama', r'''<p>Broj $y$ je najmanji ako ima najmanji mogući broj znamenki i zatim najmanje znamenke gledano od najviše. Ako DP radimo od najviše prema najnižoj poziciji (ili od najniže i pamtimo najmanji sufiks), za svako stanje pamtimo najmanji broj koji ga ostvaruje; na svakoj poziciji biramo hoće li se dogoditi prijenos i pritom uzimamo najmanju znamenku koja to postiže (npr. $0$ za „bez prijenosa”, odnosno $10 - x_i - c_{\text{in}}$ za „s prijenosom”).</p>'''),
        ('Algoritam', r'''<p>$dp[i][j][c]$ = najmanji sufiks $y$ na pozicijama $\lt i$ koji je do pozicije $i$ ostvario $j$ prijenosa i šalje prijenos $c \in \{0, 1\}$ prema poziciji $i$. Prijelaz razmatra sljedeću poziciju i obje mogućnosti (prijenos / bez prijenosa). Pozicija iznad najviše znamenke $x$ ima znamenku $0$ u $x$; prijenosi se mogu nastavljati kroz niz devetki, pa treba pokriti do $19$ pozicija.</p>'''),
        ('Rubni slučajevi i složenost', r'''<p>Za $k = 0$ traži se najmanji pozitivan $y$ bez prijenosa: $y = 10^t$ gdje je $t$ prva pozicija na kojoj $x$ nema znamenku $9$. Kad $x$ završava nulama, one same nikad ne stvaraju prijenos s $y_i = 0$, ali odgovor može imati više od $18$ znamenki, pa ih je najjednostavnije ukloniti prije DP-a i na kraju dopisati. Složenost je $O(\log^2 x)$ po upitu.</p>'''),
    ],
    'solution': r'''
<p>Zadatak rješavamo dinamičkim programiranjem po znamenkama, od više znamenke prema nižoj: $dp[i][j][c]$ označava stanje u kojem smo obradili pozicije do $i$-te, ukupno je nastalo $j$ prijenosa, a $c$ kaže dolazi li s nižih pozicija prijenos na trenutnu poziciju. U svakom koraku odlučujemo hoće li na sljedećoj poziciji nastati prijenos ili ne, i u oba slučaja upisujemo najmanju znamenku $y$ koja to postiže (bez prijenosa to je $0$, s prijenosom $10 - x_i - c$; ako je $x_i + c \ge 10$, prijenos nastaje neovisno o znamenci). Za svako stanje pamtimo najmanji dosad izgrađeni broj.</p>
<p>Vremenska složenost je $O(\log^2 x)$ po testnom primjeru.</p>
<p>Treba paziti na nekoliko rubnih slučajeva:</p>
<ul>
    <li>$y$ mora biti pozitivan, pa slučaj $k = 0$ zahtijeva jednostavnu posebnu obradu (najmanja potencija broja $10$ na čijoj poziciji $x$ nema znamenku $9$);</li>
    <li>odgovor može premašiti $10^{18}$, npr. za $x = 10^{17}$ i $k = 18$. To rješavamo tako da prije računanja uklonimo sve završne nule broja $x$ (one nikad ne sudjeluju u prijenosu) i na kraju ih ponovno dopišemo, ili jednostavno koristimo 128-bitne cijele brojeve.</li>
</ul>
''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Minimum Suffix', 'title_hr': 'Najmanji sufiks', 'slug': 'D_minimum_suffix',
    'tl': '3 s', 'ml': '1024 MB',
    'statement': r'''
<p>Za niz $s$ duljine $n$ definiramo $p_j = x$ ako je $s[x \dots j]$ najmanji sufiks prefiksa $s[1 \dots j]$, za sve $j = 1, \dots, n$. (Sufiks je najmanji ako je leksikografski manji od svih ostalih sufiksa tog niza.)</p>
<p>Iz zadanih $p_1, \dots, p_n$ rekonstruiraj $s$. Ako postoji više rješenja, ispiši leksikografski najmanje. Znakovi niza $s$ prikazuju se pozitivnim cijelim brojevima; manji broj znači manji znak.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži broj testnih primjera $T$ ($1 \le T \le 10^5$). Svaki testni primjer sadrži $n$ ($1 \le n \le 3 \cdot 10^6$) i zatim $p_1, \dots, p_n$ ($1 \le p_i \le i$). Zbroj svih $n$ ne prelazi $3 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki testni primjer ispiši $-1$ ako rješenje ne postoji, inače leksikografski najmanji $s$. Preporučuje se brzo čitanje i pisanje.</p>
<h3>Primjer</h3>
<p>Za $p = [1, 1, 1]$ odgovor je $1\ 2\ 2$; za $p = [1, 1, 2]$ odgovor je $-1$; za $p = [1, 2, 3]$ odgovor je $1\ 1\ 1$.</p>
''',
    'hints': [
        r'''<p>Izravan problem (dan $s$, traži se $p$) rješava se <em>Lyndonovom faktorizacijom</em> i Duvalovim algoritmom u linearnom vremenu. Razmisli što Duvalov algoritam radi s vrijednostima $p_j$: kada je $p_j$ jednak nekom ranijem $p$, a kada „skoči”?</p>''',
        r'''<p>Niz $p$ zapravo opisuje Lyndonovu faktorizaciju svakog prefiksa: $p_j = p_{j-1}$ znači da se trenutni Lyndonov faktor nastavlja, a $p_j = j$ znači da počinje novi faktor. Iz toga se dobivaju relacije oblika „$s[a] = s[b]$” i „$s[a] < s[b]$” među znakovima.</p>''',
        r'''<p>Unutar jednog Lyndonovog faktora sve relacije idu „prema naprijed” (uspoređuju se pozicije s početkom faktora), pa se faktor može puniti greedy slijeva nadesno. Između faktora vrijedi da je svaki faktor $\ge$ sljedećeg — obradi ih zdesna nalijevo.</p>''',
    ],
    'coach': [
        ('Opažanje: veza s Lyndonovom faktorizacijom', r'''<p>Najmanji sufiks prefiksa $s[1..j]$ počinje na početku posljednjeg Lyndonovog faktora u faktorizaciji tog prefiksa. Duvalov algoritam gradi faktorizaciju inkrementalno i pritom u svakom koraku uspoređuje $s[j]$ s odgovarajućim znakom perioda trenutnog faktora: ako su jednaki, period se nastavlja; ako je $s[j]$ veći, cijeli se dio spaja u novi veći Lyndonov faktor; ako je manji, faktor se zatvara.</p>'''),
        ('Redukcija: relacije među znakovima', r'''<p>Iz danog $p$ možemo rekonstruirati tok Duvalova algoritma: znamo kad se faktor nastavlja (dobivamo jednakosti $s[j] = s[j - \text{period}]$), kad počinje novi (nejednakost „manje” prema početku) i kad se spajaju (nejednakost „veće”). Primjer: $p = [1, 2, 1, 4, 1]$ daje $s_1 = s_2 < s_3$ i $s_1 = s_4 < s_5$. Ako relacije proturječe (npr. traže $s[j] < s[j]$), odgovor je $-1$.</p>'''),
        ('Algoritam: greedy u dva smjera', r'''<p>Unutar Lyndonovog faktora sve nejednakosti pokazuju od početka faktora prema kasnijim pozicijama, pa greedy slijeva nadesno daje najmanje znakove: kopiraj znak iz perioda kad relacija kaže „jednako”, uzmi najmanji dopušteni veći znak kad kaže „veće”. Između faktora vrijedi $\text{faktor}_1 \ge \text{faktor}_2 \ge \dots$; obradi ih zdesna nalijevo i za svaki faktor odaberi leksikografski najmanji niz koji je $\ge$ od sljedećeg faktora (što se zbog strukture Lyndonovih riječi također može odrediti znak po znak).</p>'''),
        ('Složenost', r'''<p>Sve faze su linearne: $O(n)$ po testu, ukupno $O(\sum n) = O(3 \cdot 10^6)$ uz brzi ulaz/izlaz.</p>'''),
    ],
    'solution': r'''
<p>Razmotrimo najprije izravan problem: za dani niz odrediti najmanji sufiks svakog prefiksa. To se rješava teorijom <strong>Lyndonove faktorizacije</strong>: niz se rastavlja na Lyndonove riječi (riječi koje su strogo manje od svih svojih netrivijalnih cikličkih pomaka) tako da je svaka riječ veća ili jednaka sljedećoj, a Duvalov algoritam faktorizaciju računa u linearnom vremenu. Najmanji sufiks prefiksa uvijek počinje na početku njegova posljednjeg Lyndonovog faktora.</p>
<p>U našem je zadatku dano rješenje izravnog problema. Prateći korake Duvalova algoritma prema zadanim vrijednostima $p$, niz možemo prikazati kao slijed Lyndonovih riječi, pri čemu unutar svake riječi dobivamo relacije jednakosti i stroge nejednakosti među znakovima. Primjerice, za $p = [1, 2, 1, 4, 1]$ dobivamo $s_1 = s_2 < s_3$ i $s_1 = s_4 < s_5$. Između susjednih riječi vrijedi da je prethodna riječ veća ili jednaka sljedećoj. Ako je skup relacija proturječan, rješenje ne postoji.</p>
<p>Budući da tražimo leksikografski najmanji niz, unutar svake riječi znakove biramo greedy slijeva nadesno, a između riječi greedy zdesna nalijevo: za svaku riječ odabiremo najmanji niz koji je leksikografski veći ili jednak sljedećoj riječi. Zbog strukture Lyndonovih riječi sve relacije „manje” usmjerene su prema naprijed, pa se i ovdje znakovi mogu određivati jedan po jedan.</p>
<p>Vremenska složenost je $O(n)$.</p>
''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Map', 'title_hr': 'Karta', 'slug': 'E_map',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Park $P$ je pravokutnik. Karta parka $M$ je manji (ili jednak) sličan pravokutnik položen unutar parka, zajedno s bijekcijom $f : M \to P$ koja je sličnost s koeficijentom $r$: $|f(a) - f(b)| = r\,|a - b|$ za sve $a, b \in M$. Karta može biti položena i „naopako” (zrcalno).</p>
<p>Mio se može teleportirati pomoću karte: kad je u točki $x$ na karti (uključujući rub), može se teleportirati u točku $f(x)$ parka; kad je u točki $y$ parka, može se teleportirati u točku $f^{-1}(y)$ na karti. Budući da je karta unutar parka, Mio koja stoji na karti istodobno je i u parku, pa se može teleportirati u oba smjera. Teleportirati se može najviše $n$ puta, svaki teleport traje $k$ sekundi, a hoda brzinom $1$.</p>
<p>Za dane točke $s$ i $t$ odredi najmanje vrijeme potrebno da Mio od $s$ dođe do $t$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 100$). Svaki testni primjer: četiri vrha parka (redom po obodu), četiri vrha karte (i-ti vrh karte odgovara i-tom vrhu parka, čime je određena i eventualna zrcalnost), točke $s$ i $t$ te cijeli brojevi $k$ i $n$ ($0 \le k \le 2 \cdot 10^6$, $0 \le n \le 100$). Sve su koordinate cijeli brojevi apsolutne vrijednosti do $2 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test ispiši najmanje vrijeme; prihvaća se apsolutna ili relativna greška do $10^{-9}$.</p>
''',
    'hints': [
        r'''<p>Teleport iz parka na kartu ($f^{-1}$) skuplja udaljenosti faktorom $1/r$, teleport s karte u park ($f$) ih množi s $r$. Kad se isplati hodati — kad su udaljenosti male ili velike?</p>''',
        r'''<p>Pokaži zamjenom redoslijeda da je optimalno: najprije se iz $s$ teleportirati $i$ puta „u kartu” (smanjivanje), zatim hodati, pa se $j$ puta teleportirati „iz karte” (uvećavanje) do $t$. Hodanje u sredini jednako je hodanju $f^{-i}(s) \to f^{-j}(t)$.</p>''',
        r'''<p>Sličnost ravnine najlakše je zapisati kompleksnim brojevima: $f(z) = Az + b$ (uz očuvanu orijentaciju) ili $f(z) = A\bar z + b$ (zrcalna). Iz para odgovarajućih vrhova odredi $A$ i $b$.</p>''',
    ],
    'coach': [
        ('Opažanje: teleport skalira udaljenosti', r'''<p>Ako Mio stoji u $x$ i želi u $y$, a obje točke preslikamo s $f^{-1}$ (u kartu), udaljenost se smanji $r$ puta. Zato teleporti „u kartu” prije hodanja skraćuju put, ali svaki košta $k$ sekundi; teleporti „iz karte” na kraju vraćaju nas u prave koordinate cilja.</p>'''),
        ('Redukcija: oblik optimalnog puta', r'''<p>Neka je optimalni put niz teleporta i hodanja. Ako se neko hodanje odvija između dvaju teleporta, možemo ga „odgoditi” na kraj (preslikavajući ga svim kasnijim teleportima) i time ga samo skratiti ili ostaviti jednakim, jer naknadni teleporti u smjeru $f$ množe duljinu s $r \ge 1$, a u smjeru $f^{-1}$ ionako ne bismo hodali prije njih. Rezultat: optimalan put je $s \xrightarrow{f^{-1}\times i} s' \xrightarrow{\text{hod}} t' \xrightarrow{f \times j} t$, gdje je $t' = f^{-j}(t)$, uz $i + j \le n$.</p>'''),
        ('Algoritam', r'''<p>Izračunaj $s_i = f^{-i}(s)$ za $i = 0..n$ i $t_j = f^{-j}(t)$ za $j = 0..n$ te uzmi $\min_{i+j \le n} \left( (i + j)\,k + |s_i - t_j| \right)$. Točke izvan karte se nakon $f^{-1}$ ne mogu koristiti — no formalno sve točke parka jesu domena $f^{-1}$, a rezultat je uvijek na karti, pa je sve dobro definirano. Sličnost odredi kompleksnom aritmetikom: $f(z) = Az + b$ ili $f(z) = A\bar z + b$, gdje $A$ i $b$ dobiješ iz dvaju parova odgovarajućih vrhova, a zrcalnost iz orijentacije (predznaka vektorskog produkta) obaju četverokuta.</p>'''),
        ('Složenost', r'''<p>$O(n^2)$ po testu uz $n \le 100$, dakle zanemarivo; treba paziti samo na preciznost realnih brojeva.</p>'''),
    ],
    'solution': r'''
<p>Može se pokazati da je optimalan put uvijek ovog oblika: najprije se iz $s$ nekoliko puta teleportiramo „iz velikog u malo” (parka na kartu), zatim hodamo, a onda se nekoliko puta teleportiramo „iz malog u veliko” (s karte u park) i stignemo u $t$. Naime, ako bismo hodali negdje usred niza teleporta, taj bismo dio hodanja mogli premjestiti na kraj i to nikad ne bi bilo lošije.</p>
<p>Zadatak se tako svodi na sljedeće: iz $s$ se $i$ puta teleportiramo prema karti i dođemo u $s'$, iz $t$ se $j$ puta (unatrag) teleportiramo prema karti i dođemo u $t'$, te hodamo od $s'$ do $t'$; ukupno vrijeme je $(i + j)\,k + |s' - t'|$. Budući da je ograničenje na broj teleporta malo ($n \le 100$), sve parove $(i, j)$ s $i + j \le n$ možemo isprobati u $O(n^2)$.</p>
<p>Što se tiče računanja same sličnosti, najjednostavnije je koristiti kompleksne brojeve: svaka se sličnost ravnine može zapisati kao $f(z) = Az + b$ ili, ako mijenja orijentaciju, kao $f(z) = A\bar{z} + b$, pri čemu koeficijente $A$ i $b$ odredimo iz odgovarajućih vrhova karte i parka.</p>
''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Inversion', 'title_hr': 'Inverzija', 'slug': 'F_inversion',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': r'''
<p><em>Interaktivni zadatak.</em> Skrivena je permutacija $p_1, \dots, p_n$ skupa $\{1, \dots, n\}$. Upitom „? $l$ $r$” dobivaš parnost broja inverzija podniza $p_l, \dots, p_r$, tj. $\left(\sum_{l \le i < j \le r} [p_i > p_j]\right) \bmod 2$.</p>
<p>Odredi permutaciju s najviše $4 \cdot 10^4$ upita i ispiši je u obliku „! $p_1$ $p_2$ $\dots$ $p_n$”.</p>
<h3>Protokol</h3>
<p>Najprije pročitaj $n$ ($1 \le n \le 2000$). Nakon svakog upita pročitaj odgovor ($0$ ili $1$). Nakon svakog ispisa isprazni izlazni međuspremnik. Permutacija je unaprijed fiksirana.</p>
<h3>Primjer</h3>
<p>Za $n = 3$ i skrivenu permutaciju $2\ 3\ 1$: upiti „? 1 2”, „? 1 3”, „? 2 3” daju odgovore $0$, $0$, $1$.</p>
''',
    'hints': [
        r'''<p>Označi $f(l, r)$ = odgovor na upit. Izrazi $[p_l > p_r]$ preko $f$ na četiri intervala (princip uključivanja–isključivanja po inverzijama koje uključuju obje krajnje točke).</p>''',
        r'''<p>Usporedba dvaju elemenata košta do četiri upita; obično sortiranje ($n \log n$ usporedbi) time premašuje limit. Koristi <em>sortiranje umetanjem s binarnim pretraživanjem</em>: kad umećeš $p_i$, prefiks $p_1..p_{i-1}$ već je poznat, pa neke vrijednosti $f$ možeš izračunati sam.</p>''',
        r'''<p>Pri usporedbi $p_j$ s $p_i$ (za $j < i$) vrijednosti $f(j, i-1)$ i $f(j+1, i-1)$ računaš iz poznatog prefiksa, a $f(j, i)$ i $f(j+1, i)$ pitaš — dva upita po usporedbi, ukupno $\approx 2 n \log_2 n \le 4 \cdot 10^4$.</p>''',
    ],
    'coach': [
        ('Opažanje: usporedba iz parnosti', r'''<p>Broj inverzija na $[l, r]$ sastoji se od inverzija unutar $[l+1, r]$, unutar $[l, r-1]$, minus dvostruko brojanih unutar $[l+1, r-1]$, plus inverzija para $(l, r)$. Dakle $[p_l > p_r] \equiv f(l,r) - f(l+1,r) - f(l,r-1) + f(l+1,r-1) \pmod 2$. Svaki par elemenata možemo usporediti s najviše četiri upita.</p>'''),
        ('Redukcija: koliko upita si smijemo dopustiti', r'''<p>Sortiranje usporedbama treba oko $n \log_2 n \approx 22000$ usporedbi za $n = 2000$; s četiri upita po usporedbi to je previše. Trebamo smanjiti broj upita po usporedbi na dva. Binarno pretraživanje u sortiranju umetanjem treba $\lceil \log_2 i \rceil$ usporedbi za $i$-ti element, ukupno $\sum_i \lceil\log_2 i\rceil \approx 19\,000$ usporedbi za $n = 2000$, tj. oko $38\,000$ upita — unutar limita.</p>'''),
        ('Algoritam: sortiranje umetanjem', r'''<p>Obrađuj $i = 1, 2, \dots, n$ i održavaj relativni poredak prefiksa $p_1..p_{i-1}$ (kao sortiranu listu indeksa). Za usporedbu $p_j$ s $p_i$ trebamo $f(j, i)$, $f(j+1, i)$ (dva upita) te $f(j, i-1)$, $f(j+1, i-1)$ — parnosti inverzija unutar već poznatog prefiksa, koje izračunamo sami (npr. $O(n)$ po vrijednosti, ili unaprijed održavajući tablicu parnosti za sve $l$ pri fiksnom desnom kraju $i-1$). Binarnim pretraživanjem nađi mjesto $p_i$ u poretku. Na kraju poredak pretvori u vrijednosti permutacije.</p>'''),
        ('Složenost', r'''<p>Broj upita je $\approx 2 n \log_2 n \le 4 \cdot 10^4$, a lokalno računanje $O(n^2)$ — za $n \le 2000$ sasvim dovoljno.</p>'''),
    ],
    'solution': r'''
<p>Označimo s $f(l, r)$ odgovor na upit za interval $[l, r]$. Lako se vidi da vrijedi</p>
<p>$$[p_l > p_r] \equiv f(l, r) - f(l+1, r) - f(l, r-1) + f(l+1, r-1) \pmod 2,$$</p>
<p>jer se u razlici ponište sve inverzije koje ne uključuju istodobno pozicije $l$ i $r$.</p>
<p>Kad bismo permutaciju jednostavno sortirali usporedbama pomoću te formule, trebali bismo oko $4 n \log n$ upita, što je previše. Umjesto toga koristimo <strong>sortiranje umetanjem</strong>: elemente obrađujemo redom i za svaki novi element binarnim pretraživanjem tražimo njegovo mjesto među već obrađenima. Kad umećemo $p_i$, relativni poredak elemenata $p_1, \dots, p_{i-1}$ već je poznat, pa vrijednosti $f(j, i-1)$ i $f(j+1, i-1)$ možemo izračunati sami, bez upita; dovoljna su dva upita po usporedbi, $f(j, i)$ i $f(j+1, i)$.</p>
<p>Ukupan broj upita je približno $2 n \log n$, a vremenska složenost $O(n^2)$.</p>
''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Rectangle', 'title_hr': 'Pravokutnik', 'slug': 'G_rectangle',
    'tl': '8 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je $n$ pravokutnika s cjelobrojnim koordinatama; $i$-ti ima donji lijevi vrh $(x_{i,1}, y_{i,1})$ i gornji desni $(x_{i,2}, y_{i,2})$. Pravokutnici se mogu preklapati.</p>
<p>Treba odabrati tri međusobno različita pravca oblika $x = a$ ili $y = a$, gdje je $a$ cijeli broj iz $[1, 10^9]$, tako da svaki pravokutnik dodiruje barem jedan pravac (pravac dodiruje pravokutnik ako siječe njegovu unutrašnjost ili rub). Izračunaj broj takvih neuređenih trojki pravaca modulo $998244353$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 10^5$). Svaki testni primjer sadrži $n$ ($1 \le n \le 10^5$) i zatim $n$ redaka s $x_{i,1}, y_{i,1}, x_{i,2}, y_{i,2}$ ($1 \le x_{i,1} < x_{i,2} \le 10^9$, $1 \le y_{i,1} < y_{i,2} \le 10^9$). Zbroj svih $n$ ne prelazi $2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki testni primjer ispiši odgovor u zasebnom retku.</p>
''',
    'hints': [
        r'''<p>Podijeli po tipu trojke: tri okomita pravca, tri vodoravna, dva okomita + jedan vodoravni, jedan okomiti + dva vodoravna. Slučajevi su simetrični (zamjena osi), pa treba riješiti samo dva.</p>''',
        r'''<p>Tri paralelna pravca: to je jednodimenzionalan problem na projekcijama (intervalima). Enumeriraj položaj srednjeg pravca; lijevi pravac mora pokriti sve intervale lijevo od srednjeg koje on ne dodiruje, a desni sve takve desno — svaki od ta dva uvjeta određuje interval dopuštenih položaja (presjek intervala).</p>''',
        r'''<p>Jedan vodoravni + dva okomita: sweep line po vodoravnom pravcu. Pravokutnici koje vodoravni pravac dodiruje nestaju; za preostale intervale $[l_i, r_i]$ trebaš broj parova točaka $(L, R)$ koje ih sve pokrivaju. Za fiksirano $L$ gornja granica za $R$ je $\min\{r_i : l_i > L\}$ — sufiksni minimum koji se mijenja pri dodavanju/brisanju intervala.</p>''',
        r'''<p>Zbroj „sufiksnih minimuma” nad dinamičkim skupom ograničenja održava se segmentnim stablom uz tehniku poznatu kao „楼房重建” (rekonstrukcija zgrada): u svakom čvoru pamtimo minimum i doprinos uz spajanje u $O(\log n)$ po čvoru.</p>''',
    ],
    'coach': [
        ('Opažanje: podjela na slučajeve', r'''<p>Trojka pravaca je jedan od tipova $\{3H\}, \{3V\}, \{2V + 1H\}, \{1V + 2H\}$. Zamjena koordinatnih osi pretvara $3H$ u $3V$ i $2V+1H$ u $1V+2H$, pa je dovoljno riješiti „tri paralelna” i „jedan poprečni + dva paralelna”, te postupak ponoviti s zamijenjenim koordinatama.</p>'''),
        ('Redukcija 1: tri paralelna pravca', r'''<p>Vodoravni pravci ovise samo o $y$-projekcijama $[y_{i,1}, y_{i,2}]$. Sortiraj intervale; fiksiraj srednji pravac $y = m$ (dovoljno je razmatrati intervale između uzastopnih „događaja”, jer se skup dodirnutih pravokutnika mijenja samo u krajnjim točkama). Nedodirnuti intervali potpuno ispod $m$ moraju biti pokriveni donjim pravcem: on leži u presjeku tih intervala, tj. u $[\max l, \min r]$ (računa se prefiksnim maksimumom lijevih i prefiksnim minimumom desnih krajeva). Analogno gornji. Broj načina je umnožak duljina dvaju dopuštenih intervala, presječen s $[1, 10^9]$ i s uvjetom da su pravci strogo ispod / iznad $m$.</p>'''),
        ('Redukcija 2: jedan vodoravni + dva okomita', r'''<p>Pomiči vodoravni pravac $y = h$ sweep lineom po događajima. Skup $S$ pravokutnika koje $h$ ne dodiruje mijenja se umetanjem i brisanjem; svaki iz $S$ daje $x$-interval $[l_i, r_i]$ koji jedan od dva okomita pravca mora pogoditi. Za lijevi pravac $L$ i desni $R$ ($L < R$) uvjet je: svaki interval s $l_i > L$ mora sadržavati $R$, i svaki s $r_i < R$ mora sadržavati $L$. Ekvivalentno, $L \le \min r_i$, $R \ge \max l_i$, i $R \le g(L) := \min\{ r_i : l_i > L\}$. Uz $\max l_i \le R \le g(L)$ i $L$ manji od svih $l$-ova koje nije pokrio, broj parova je $\sum_L \max(0, g(L) - \max(l) + 1)$ (uz odgovarajuću korekciju za $L$-ove koji dodiruju neke intervale).</p>'''),
        ('Algoritam: segmentno stablo za sufiksni minimum', r'''<p>Funkcija $g(L)$ je nerastuća stepenasta funkcija određena ograničenjima „za sve $L < l_i$ vrijedi $R \le r_i$” — svako ograničenje je prefiksni minimum. Kako ograničenja i nestaju, ne možemo ih samo „prekriti”; u segmentnom stablu nad koordinatama $l$ držimo u listu $l_i$ vrijednost $r_i$ (minimum ako ih je više — multiset po listu), a u svakom čvoru minimum i zbroj $\sum_L g(L)$ nad njegovim segmentom računat spajanjem u $O(\log n)$ (klasična tehnika „楼房重建”: doprinos lijevog djeteta ovisi o minimumu desnog). Ukupno $O(n \log^2 n)$, uz komprimirane koordinate i množenje duljina praznih raspona.</p>'''),
        ('Složenost', r'''<p>$O(n \log^2 n)$ po testu; s ukupno $2 \cdot 10^5$ pravokutnika i limitom od $8$ sekundi to prolazi, ali implementacija je zahtjevna — pažljivo s rubovima intervala i modularnim zbrajanjem.</p>'''),
    ],
    'solution': r'''
<p>Razlikujemo slučajeve prema tipovima pravaca: tri vodoravna pravca, jedan vodoravni i dva okomita, te simetrični slučajevi (tri okomita, dva vodoravna i jedan okomiti), koje dobijemo zamjenom koordinata.</p>
<p><strong>Tri vodoravna pravca.</strong> Rješenje ovisi samo o $y$-koordinatama, tj. o intervalima $[y_{i,1}, y_{i,2}]$, pa je problem jednodimenzionalan. Enumeriramo položaj srednjeg pravca; gornji pravac tada mora ležati u presjeku svih intervala iznad srednjeg koje on ne pokriva, a donji u presjeku svih nepokrivenih intervala ispod. Ti se presjeci računaju prefiksnim/sufiksnim minimumima i maksimumima, a broj načina je umnožak duljina dopuštenih raspona.</p>
<p><strong>Jedan vodoravni i dva okomita pravca.</strong> Vodoravni pravac pomičemo sweep lineom. Pri tome se skup pravokutnika koje vodoravni pravac dodiruje mijenja, pa trebamo podržati brisanje i umetanje intervala $[l_i, r_i]$ (njihovih $x$-projekcija) i odgovoriti na pitanje: na koliko načina dvije točke $L$ i $R$ pokrivaju sve preostale intervale?</p>
<p>Neka su preostali intervali $[l_i, r_i]$. Za lijevu točku vrijedi $L \le \min r_i$, a za desnu $R \ge \max l_i$. Definirajmo $f(L)$ kao gornju granicu za $R$ ako je lijeva točka u $L$. Svaki umetnuti interval $[l, r]$ daje ograničenje: ako je $L < l$, onda mora biti $R \le r$. Dakle na prefiksu položaja $L$ imamo ograničenje „$\le r$”. Budući da se ograničenja moraju moći i brisati, ne možemo ih jednostavno prepisivati.</p>
<p>Umjesto toga ograničenja pohranimo u segmentno stablo i u njemu održavamo <em>sufiksne minimume</em> ograničenja i njihov zbroj. To je tehnika koja se u kineskoj literaturi obično naziva „楼房重建” (rekonstrukcija zgrada): u svakom čvoru pamtimo minimum na segmentu i zbroj sufiksnih minimuma, a pri spajanju djece doprinos lijevog djeteta preračunavamo silaskom u $O(\log n)$ ovisno o minimumu desnog djeteta.</p>
<p>Ukupna vremenska složenost je $O(n \log^2 n)$.</p>
''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Chinese Checker', 'title_hr': 'Kineska dama', 'slug': 'H_chinese_checker',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Prof. Pang igra kinesku damu na standardnoj šesterokrakoj ploči (zvijezda sa $121$ poljem). Na ploči je $n$ figura. Jedan <em>potez</em> sastoji se od jednog ili više koraka: najprije se odabere figura $a$ koja se pomiče (ista tijekom cijelog poteza), a u svakom koraku odabere se druga figura $b$ kao „stožer” i $a$ se premjesti na položaj simetričan s obzirom na $b$, pri čemu:</p>
<ul>
    <li>spojnica $a$ i $b$ mora biti paralelna jednoj od triju osi šesterokutne ploče (susjednost nije nužna);</li>
    <li>na spojnici od $a$ do njezina simetričnog položaja ne smije biti drugih figura osim $b$;</li>
    <li>simetrični položaj mora biti na ploči i slobodan;</li>
    <li>korak koji vraća $a$ na njezin početni položaj (prije poteza) nije dopušten.</li>
</ul>
<p>Potez može stati nakon bilo kojeg koraka. Koliko različitih poteza postoji? Dva su poteza različita ako se skupovi zauzetih polja nakon njih razlikuju (figure su nerazlučive).</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 100$). Svaki test sadrži $n$ ($1 \le n \le 121$) i zatim $n$ redaka s parom (redak, položaj u retku), brojeći od vrha prema dnu i slijeva nadesno od $1$. Položaji su različiti.</p>
<h3>Izlaz</h3>
<p>Za svaki test ispiši broj različitih poteza.</p>
''',
    'hints': [
        r'''<p>Ploča ima samo $121$ polje; za svaku figuru koja se pomiče skup dostižnih polja u jednom potezu je malen. Kako bi izgledao BFS po položajima figure $a$?</p>''',
        r'''<p>Najveći dio posla je geometrija ploče: prikaži šesterokutnu mrežu u koordinatama u kojima su tri osi jednostavni pomaci (npr. „aksijalne” koordinate $(q, r)$ s smjerovima $(1,0)$, $(0,1)$, $(1,-1)$) i unaprijed izgradi skup valjanih polja.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Skupovi zauzetih polja nakon poteza razlikuju se točno onda kad se razlikuje par (pomaknuta figura, njezino završno polje). Zato je odgovor $\sum_a |\{$polja dostižna figurom $a$ u $\ge 1$ koraka$\} \setminus \{$početno polje$\}|$.</p>'''),
        ('Redukcija', r'''<p>Za fiksiranu figuru $a$ poteza je BFS po poljima: iz trenutnog polja u svakom od šest smjerova nađi prvu figuru $b$ na toj zraci, provjeri da je simetrično polje na ploči, slobodno i da između $b$ i njega nema figura, pa ga dodaj u red. Zabranjeno je samo završiti na početnom polju (ono je zauzeto figurom $a$ „u mislima” — dovoljno je ne brojati ga).</p>'''),
        ('Algoritam i složenost', r'''<p>Izgradi model ploče: zvijezda se dobiva kao unija središnjeg šesterokuta i šest trokuta; najlakše je ručno izgenerirati koordinate iz opisa redaka (dužine redaka $1,2,3,4,13,12,11,10,9,10,11,12,13,4,3,2,1$) i preslikati ih u aksijalne koordinate. Za svaki test i svaku figuru radimo BFS nad najviše $121$ poljem s $6$ smjerova i skeniranjem zrake — ukupno $O(T \cdot n \cdot 121 \cdot 6 \cdot 17)$, zanemarivo.</p>'''),
    ],
    'solution': r'''
<p>Enumeriramo koja se figura pomiče, a zatim prema pravilima zadatka napravimo BFS po poljima ploče: iz trenutnog polja u svakom od šest smjerova potražimo prvu figuru $b$, provjerimo da je simetrično polje na ploči i slobodno te da između $b$ i tog polja nema drugih figura, i to polje dodamo u red. Početno polje figure ne brojimo. Odgovor je zbroj broja posjećenih polja po svim figurama.</p>
<p>Glavni je posao točno modelirati šesterokutnu ploču (zvijezdu sa $121$ poljem) u koordinatama u kojima su tri osi jednostavni pomaci; zatim je sam algoritam trivijalan.</p>
''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Chase Game', 'title_hr': 'Igra potjere', 'slug': 'I_chase_game',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Prof. Shou bježi od prof. Panga na neusmjerenom, netežinskom, jednostavnom povezanom grafu. Shou je u vrhu $1$ i želi do vrha $n$; Pang je u vrhu $k$ i ima domet napada $d$.</p>
<p>Svake sekunde Shou prijeđe u susjedni vrh, a zatim ga Pang napadne: šteta je $d - dis$, gdje je $dis$ udaljenost (broj bridova na najkraćem putu) između njih. Ako je $dis \ge d$, Pang se umjesto toga teleportira u Shouov vrh i nanese štetu $d$ (kad je $dis < d$, Pang ostaje na mjestu). Shou prima napad i pri dolasku u vrh $n$.</p>
<p>Odredi najmanju ukupnu štetu koju Shou mora primiti.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n, m, k, d$ ($2 \le n \le 10^5$, $n - 1 \le m \le 2 \cdot 10^5$, $1 \le k \le n$, $1 \le d \le 2 \cdot 10^5$). Slijedi $m$ bridova $a\ b$. Graf je povezan.</p>
<h3>Izlaz</h3>
<p>Ispiši najmanju ukupnu štetu.</p>
''',
    'hints': [
        r'''<p>Što se dogodi nakon što Pang teleportira u Shouov vrh? Od tog trenutka Pang je uvijek na udaljenosti $1$ (ili se ponovno teleportira ako je $d = 1$), pa je šteta po koraku konstantna i optimalno je ići najkraćim putem do $n$.</p>''',
        r'''<p>Dok Pang stoji u $k$, šteta u vrhu $v$ ovisi samo o $\mathrm{dist}(k, v)$. Dakle stanje je samo trenutni vrh i „je li se teleport već dogodio” — a nakon teleporta odgovor je zatvorena formula.</p>''',
        r'''<p>Napravi BFS iz $k$ i iz $n$, zatim Dijkstra iz $1$ s težinom vrha $v$ jednakom $d - \mathrm{dist}(k, v)$ ako je to $\gt 0$; ulazak u vrh s $\mathrm{dist}(k, v) \ge d$ znači teleport, pa dodaj $d$ plus (preostali koraci do $n$) $\cdot$ (šteta po koraku) i ne nastavljaj dalje.</p>''',
    ],
    'coach': [
        ('Opažanje: stanje nakon teleporta', r'''<p>Nakon teleporta Pang je u Shouovom vrhu. U sljedećem koraku Shou se pomakne na susjedni vrh: udaljenost je $1$, pa je šteta $d - 1$ ako je $d > 1$ (Pang ostaje), a ako je $d = 1$ udaljenost $1 \ge d$ znači novi teleport i štetu $d = 1$. U oba slučaja svaki daljnji korak košta konstantno: $c = d - 1$ za $d \ge 2$, odnosno $c = 1$ za $d = 1$. Od tog je trenutka optimalno ići najkraćim putem, ukupno $d + c \cdot \mathrm{dist}(v, n)$.</p>'''),
        ('Redukcija', r'''<p>Ostaje samo prva faza, dok Pang miruje u $k$. Šteta pri ulasku u vrh $v$ iznosi $d - \mathrm{dist}(k, v)$ ako je $\mathrm{dist}(k, v) < d$; inače dolazi do teleporta i cijena ostatka puta je poznata formula. Stanje je samo trenutni vrh — $O(n)$ stanja.</p>'''),
        ('Algoritam', r'''<p>BFS iz $k$ daje $\mathrm{dist}(k, \cdot)$, BFS iz $n$ daje $\mathrm{dist}(\cdot, n)$. Zatim Dijkstra iz vrha $1$: prijelaz $u \to v$ košta $d - \mathrm{dist}(k, v)$ ako je $\mathrm{dist}(k, v) < d$; ako je $\mathrm{dist}(k, v) \ge d$, kandidat za odgovor je $D[u] + d + c \cdot \mathrm{dist}(v, n)$ i iz $v$ ne nastavljamo. Odgovor je minimum od $D[n]$ (ako je dostignut bez teleporta) i svih kandidata.</p>'''),
        ('Složenost', r'''<p>Dva BFS-a i jedan Dijkstra: $O((n + m) \log n)$.</p>'''),
    ],
    'solution': r'''
<p>Najprije uočimo: ako se Pang teleportira u Shouov vrh, od tog trenutka udaljenost među njima je uvijek $1$ (ili se, za $d = 1$, teleport ponavlja svaki korak), pa je šteta po koraku konstantna i Shou najbolje ide najkraćim putem do $n$. Dakle nakon teleporta odgovor možemo izračunati izravno formulom.</p>
<p>Zato treba razmatrati samo početni dio puta, dok se Pang još nije pomaknuo iz $k$. Šteta pri ulasku u vrh $v$ tada ovisi samo o $\mathrm{dist}(k, v)$, pa je broj korisnih stanja $O(n)$. Nakon što BFS-om izračunamo najkraće udaljenosti od $k$ i od $n$ do svih vrhova, pokrenemo Dijkstrin algoritam iz vrha $1$ s težinama $d - \mathrm{dist}(k, v)$; ulazak u vrh s $\mathrm{dist}(k, v) \ge d$ znači teleport i završava se formulom za ostatak puta.</p>
<p>Vremenska složenost je $O((n + m) \log n)$.</p>
''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Chase Game 2', 'title_hr': 'Igra potjere 2', 'slug': 'J_chase_game_2',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Karta igre je stablo s $n$ soba. Pang je u sobi $u$, Shou u sobi $v$ ($u \ne v$); igraju naizmjence, Shou prvi. U svom potezu igrač (znajući oba položaja) ostaje ili prelazi u susjednu sobu. Shou je uhvaćen kad su u istoj sobi. Pang želi uhvatiti Shoua u konačno mnogo poteza, Shou to želi izbjeći; oba igraju optimalno.</p>
<p>Prof. Fei će dodati što manje novih hodnika (bridova) tako da za <em>svaki</em> par početnih soba $(u, v)$ Pang ne može uhvatiti Shoua. Odredi najmanji broj dodanih hodnika ili $-1$ ako to nije moguće.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 10^4$). Svaki test sadrži $n$ ($2 \le n \le 10^5$) i $n - 1$ bridova stabla. Zbroj svih $n$ ne prelazi $2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test ispiši najmanji broj dodanih hodnika ili $-1$.</p>
<h3>Primjer</h3>
<p>Za put od $4$ vrha odgovor je $1$; za zvijezdu s $3$ lista odgovor je $-1$; za stablo s bridovima $1\!-\!2, 2\!-\!3, 3\!-\!4, 3\!-\!5$ odgovor je $2$.</p>
''',
    'hints': [
        r'''<p>Kada Pang sigurno hvata Shoua na grafu? Ako je Shou u listu (vrh stupnja $1$) a Pang u njegovu susjedu, Shou je uhvaćen odmah. Dakle svaki list mora dobiti barem jedan novi brid.</p>''',
        r'''<p>Nije dovoljno spojiti list samo s njegovim „bratom” (listom istog roditelja): Pang u roditelju i dalje hvata. Iz toga slijedi da zvijezda nema rješenja. Što s ostalim stablima?</p>''',
        r'''<p>Neka je $s$ broj listova, a $mx$ najveći broj listova s istim roditeljem. Donja granica je $\max\!\left(\lceil s/2 \rceil, mx\right)$ — i može se dostići uparivanjem listova različitih roditelja.</p>''',
    ],
    'coach': [
        ('Opažanje: listovi su ranjivi', r'''<p>Ako Shou stoji u listu $\ell$ a Pang u njegovom jedinom susjedu $p$, Shou na potezu može samo ostati ili ući u $p$ — u oba slučaja je uhvaćen. Zato svaki list mora dobiti barem jedan dodatni brid. Nakon dodavanja brid $\ell$–$w$ pomaže samo ako $w$ nije susjed $p$-a niti $p$ sam; posebno, list se ne smije spojiti samo sa svojim bratom (list istog roditelja), jer Pang u roditelju pokriva oba.</p>'''),
        ('Redukcija: donja granica', r'''<p>Neka je $s$ ukupan broj listova i $mx$ najveći broj listova koji dijele istog roditelja. Svaki novi brid „popravlja” najviše dva lista, dakle treba barem $\lceil s/2 \rceil$ bridova. Listovi istog roditelja ne mogu se popravljati međusobno, pa je potrebno barem $mx$ bridova. Ako je stablo zvijezda ($mx = s = n - 1$ i nema drugih vrhova), nikakvo dodavanje ne pomaže: Pang u središtu uvijek hvata — odgovor je $-1$. Za $n = 2$ isto vrijedi (jedini brid, oba vrha listovi).</p>'''),
        ('Algoritam: dostizanje granice', r'''<p>Tvrdnja: za stablo koje nije zvijezda odgovor je točno $\max(\lceil s/2 \rceil, mx)$. Konstrukcija: listove grupiraj po roditelju, sortiraj grupe po veličini i uparuj list iz najveće grupe s listom iz neke druge grupe (kao pri rasporedu u parove bez ponavljanja boja); kad je $mx$ velik, preostale listove najveće grupe spoji s bilo kojim ne-susjednim vrhom stabla (postoji jer stablo nije zvijezda). Nakon toga svaki vrh ima „izlaz” koji Pang ne može istodobno blokirati, pa Shou uvijek bježi. Zadatak traži samo broj, pa je dovoljno izračunati $s$ i $mx$.</p>'''),
        ('Složenost', r'''<p>$O(n)$ po testu — brojanje stupnjeva i listova po roditelju.</p>'''),
    ],
    'solution': r'''
<p>Najprije, za svaki list nužno je dodati barem jedan brid: ako je Shou u listu a Pang u njegovu roditelju, Shou je odmah uhvaćen. Nadalje, list se ne može „spasiti” tako da ga spojimo samo s njegovim bratom (drugim listom istog roditelja), jer Pang u roditelju i dalje pokriva oba. Iz toga slijedi da za zvijezdu rješenje ne postoji: odgovor je $-1$.</p>
<p>U suprotnom, neka je $s$ ukupan broj listova, a $mx$ najveći broj listova koji imaju zajedničkog roditelja. Odgovor ne može biti manji od $\max\!\left(\lceil s/2 \rceil, mx\right)$: svaki dodani brid popravlja najviše dva lista, a listovi istog roditelja ne mogu se popravljati međusobno.</p>
<p>Nije teško dokazati da se ta donja granica može dostići: listove uparujemo tako da uparujemo listove različitih roditelja (uvijek uzimajući list iz trenutačno najveće grupe), a preostale listove najveće grupe spajamo s drugim, ne-susjednim vrhovima stabla, kojih ima jer stablo nije zvijezda. Dakle odgovor je $\max\!\left(\lceil s/2 \rceil, mx\right)$, a složenost $O(n)$.</p>
''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Magic', 'title_hr': 'Čarolija', 'slug': 'K_magic',
    'tl': '3 s', 'ml': '16 MB',
    'statement': r'''
<p><em>Upozorenje: neobično memorijsko ograničenje!</em></p>
<p>Dan je niz $a_0, \dots, a_{2n}$, na početku sve nule, i $n$ operacija; $i$-ta operacija zadana je brojevima $l_i, r_i$ ($1 \le l_i < r_i \le 2n$) i postavlja $a_{l_i}, \dots, a_{r_i - 1}$ na vrijednost $i$. Svi brojevi $l_1, \dots, l_n, r_1, \dots, r_n$ su međusobno različiti.</p>
<p>Svaku operaciju treba izvesti točno jednom, u proizvoljnom redoslijedu. Maksimiziraj broj indeksa $i$ ($0 \le i < 2n$) za koje je na kraju $a_i \ne a_{i+1}$.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n$ ($1 \le n \le 5 \cdot 10^3$); slijedi $n$ redaka s $l_i, r_i$.</p>
<h3>Izlaz</h3>
<p>Ispiši najveći mogući broj takvih indeksa.</p>
<h3>Primjer</h3>
<p>Za intervale $[2,3], [6,7], [1,9], [5,10], [4,8]$ odgovor je $9$.</p>
''',
    'hints': [
        r'''<p>Promijeni perspektivu: granica $a_i \ne a_{i+1}$ može nastati samo na krajnjoj točki nekog intervala ($i = l_j$ ili $i = r_j$), i to samo ako je taj kraj „vidljiv” na kraju — interval $j$ je izveden nakon svih intervala koji tu točku pokrivaju iznutra. Koje skupove krajnjih točaka možemo istodobno učiniti vidljivima?</p>''',
        r'''<p>Ako se intervali $[l_1, r_1]$ i $[l_2, r_2]$ križaju ($l_1 < l_2 < r_1 < r_2$), vidljivost točke $l_2$ zahtijeva „$1$ prije $2$”, a vidljivost $r_1$ zahtijeva „$2$ prije $1$”. Dakle $r_1$ i $l_2$ su nekompatibilni — spoji ih bridom. Odabrani skup mora biti nezavisan skup u tom grafu.</p>''',
        r'''<p>Graf je bipartitan (bridovi idu samo između lijevih i desnih krajeva). Pokaži da nezavisnost dovoljna (poredak koji ostvaruje sve zahtjeve nema ciklus). Najveći nezavisan skup u bipartitnom grafu $= 2n - $ najveće sparivanje. Pazi na memoriju od $16$ MB — graf može imati $\Theta(n^2)$ bridova!</p>''',
    ],
    'coach': [
        ('Opažanje: što doprinosi odgovoru', r'''<p>Nakon svih operacija vrijednost $a$ mijenja se samo u točkama koje su krajevi intervala. Krajnja točka $x$ intervala $j$ doprinosi točno onda kad je $j$ izveden nakon svih intervala koji strogo sadrže $x$ u unutrašnjosti (inače je taj prijelaz „prebojan”). Zadatak: odaberi što više krajnjih točaka tako da postoji poredak izvođenja koji sve odabrane čini vidljivima.</p>'''),
        ('Redukcija: uvjet kompatibilnosti', r'''<p>Za dva intervala koji se križaju, $l_1 < l_2 < r_1 < r_2$: odabir $l_2$ zahtijeva da $[l_1, r_1]$ bude izveden prije $[l_2, r_2]$; odabir $r_1$ zahtijeva suprotno. Zato $r_1$ i $l_2$ ne mogu biti odabrani zajedno. Ugniježđeni i disjunktni parovi ne stvaraju konflikte (kod ugniježđenja unutarnji ide poslije, i njegovi krajevi su vidljivi; krajevi vanjskog nisu pokriveni unutarnjim). Skup odabranih točaka mora biti <em>nezavisan skup</em> u grafu s bridovima $r_1$—$l_2$ za svaki križajući par.</p>'''),
        ('Dokaz dovoljnosti', r'''<p>Nezavisan skup zadaje relacije „prije” među intervalima. Kad bi one tvorile ciklus, gledajmo brid ciklusa koji dolazi od odabranog desnog kraja $r$ intervala $[l, r]$ i tjera ga poslije nekog $[l', r']$ s $l < l' < r < r'$. Kako $l'$ nije odabran (konflikt), sljedeći brid ciklusa mora dolaziti od odabranog $r'$, koji je veći od $r$. Desni krajevi duž lanca strogo rastu, pa ciklus nije moguć — svaki nezavisan skup je ostvariv.</p>'''),
        ('Algoritam: bipartitno sparivanje uz malo memorije', r'''<p>Graf je bipartitan (lijevi krajevi vs. desni krajevi), a najveći nezavisan skup ima $2n - \nu$ elemenata, gdje je $\nu$ najveće sparivanje (Kőnigov teorem). Bridova može biti $\Theta(n^2) \approx 1.25 \cdot 10^7$, što u $16$ MB ne stane kao lista susjedstva; no brid je definiran implicitno uvjetom $l_1 < l_2 < r_1 < r_2$, pa susjede računamo u letu. Mogućnosti: Kuhnov (mađarski) algoritam s bitsetom, $O(n^3 / w)$; Dinic s implicitnim grafom preko perzistentnog segmentnog stabla, $O(n^2 \log n)$; Hopcroft–Karp uz segmentno stablo za pronalaženje neposjećenih susjeda, $O(n^{1.5} \log n)$. Sve tri prolaze; memorijski limit sprječava samo intervalni DP s $O(n^2)$ memorije.</p>'''),
    ],
    'solution': r'''
<p>Promijenimo način gledanja: odabiremo skup krajnjih točaka intervala koje će na kraju doprinijeti odgovoru (biti mjesta promjene vrijednosti), i želimo da taj skup bude što veći, a da postoji redoslijed operacija koji sve odabrane točke doista čini vidljivima.</p>
<p>Za intervale $[l_1, r_1]$ i $[l_2, r_2]$ s $l_1 < l_2 < r_1 < r_2$ vrijedi: ako odaberemo $l_2$, interval $[l_1, r_1]$ mora biti izveden prije $[l_2, r_2]$; ako odaberemo $r_1$, interval $[l_2, r_2]$ mora biti izveden prije $[l_1, r_1]$. Zato $r_1$ i $l_2$ ne mogu biti odabrani istodobno — spojimo ih bridom neusmjerenog grafa. Odabrani skup mora biti <strong>nezavisan skup</strong> u tom grafu.</p>
<p>Pokažimo da je to i dovoljno, tj. da relacije „prije” koje zadaje nezavisan skup ne stvaraju ciklus. Pretpostavimo da ciklus postoji i da u njemu neki brid dolazi od odabranog desnog kraja $r$ intervala $[l, r]$, što zahtijeva da taj interval bude izveden nakon nekog $[l', r']$ s $l < l' < r < r'$. Kako $l'$ nije odabran, sljedeći brid ciklusa nastaje zbog odabira $r'$; nastavljajući tako, desni krajevi duž lanca strogo rastu, pa se lanac ne može zatvoriti u ciklus. Dakle uvjet nezavisnosti je dovoljan.</p>
<p>Problem se time sveo na najveći nezavisan skup. Kako bridovi spajaju samo lijeve krajeve s desnima, graf je bipartitan, pa je najveći nezavisan skup jednak $2n$ minus veličina najvećeg sparivanja. Moguće implementacije:</p>
<ul>
    <li>mađarski (Kuhnov) algoritam ubrzan bitsetom: $O(n^3 / w)$;</li>
    <li>Dinic nad grafom izgrađenim perzistentnim segmentnim stablom: $O(n^2 \log n)$;</li>
    <li>Hopcroft–Karp uz segmentno stablo: $O(n^{1.5} \log n)$.</li>
</ul>
<p>Sva tri pristupa prolaze. Memorijsko ograničenje od $16$ MB postavljeno je kako bi se onemogućila optimizirana intervalna dinamička programiranja; uobičajene implementacije gornjih algoritama sparivanja nemaju problema s memorijom.</p>
''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Aqre', 'title_hr': 'Aqre', 'slug': 'L_aqre',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Matricu $n \times m$ treba ispuniti nulama i jedinicama tako da:</p>
<ul>
    <li>ne postoje četiri uzastopne ćelije u istom retku ili stupcu ispunjene istim brojem;</li>
    <li>ćelije s jedinicama čine (bridno) povezano područje.</li>
</ul>
<p>Konstruiraj matricu s najvećim mogućim brojem jedinica; ispiši taj broj i matricu.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $T$ ($1 \le T \le 10^3$). Svaki test sadrži $n, m$ ($2 \le n, m \le 10^3$). Zbroj svih $n \cdot m$ ne prelazi $10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test ispiši najveći broj jedinica i zatim matricu ($n$ redaka); bilo koje optimalno rješenje se prihvaća.</p>
<h3>Primjer</h3>
<p>Za $2 \times 2$ odgovor je $4$; za $3 \times 4$ odgovor je $9$ (npr. tri retka $1110$); za $3 \times 8$ odgovor je $18$.</p>
''',
    'hints': [
        r'''<p>Gornja granica: ako se ploča može podijeliti na disjunktne pravokutnike $1 \times 4$ (vodoravne ili okomite), svaki mora sadržavati barem jednu nulu. Oboji ćelije s $(i + j) \bmod 4$ — svaki $1 \times 4$ pokriva po jednu ćeliju svake od četiri „boje”.</p>''',
        r'''<p>Za $n, m \ge 4$ granica $nm - \min_c |\{(i,j): (i+j) \bmod 4 = c\}|$ je dostižna, i to periodičnim uzorkom $4 \times 4$. Ne moraš ga pogađati: isprobaj sve uzorke $4 \times 4$ s točno četiri nule i lokalno provjeri povezanost i valjanost za nekoliko dimenzija.</p>''',
        r'''<p>Za $n \le 3$ (ili $m \le 3$) okomitih $1 \times 4$ nema, pa argument ne prolazi doslovno; potrebna je zasebna analiza. Posebno je slučaj $3 \times (4k + 3)$ — tu treba posebna konstrukcija.</p>''',
    ],
    'coach': [
        ('Opažanje: donja granica na broj nula', r'''<p>Svaki pravokutnik $1 \times 4$ (u retku ili stupcu) mora sadržavati barem jednu nulu. Označimo ćeliju $(i, j)$ bojom $(i + j) \bmod 4$; svaki $1 \times 4$ pokriva po jednu ćeliju svake boje. Ako ćelije boje $c$ imamo $k_c$ komada i uspijemo ploču popločati $1 \times 4$ pravokutnicima koji zajedno pokrivaju sve ćelije neke boje… jednostavnije: broj disjunktnih $1 \times 4$ ne prelazi $\min_c k_c$, a za $n, m \ge 4$ postoji popločavanje koje ih ima točno toliko. Dakle nula je barem $\min_c k_c$, tj. jedinica najviše $nm - \min_c k_c$.</p>'''),
        ('Redukcija: periodičan uzorak', r'''<p>Postavljanje nula upravo na ćelije jedne boje $(i + j) \bmod 4 = c$ daje dijagonalni uzorak koji zadovoljava uvjet o četiri uzastopne ćelije, ali jedinice tada nisu povezane (dijagonale nula presijecaju ploču). Treba uzorak $4 \times 4$ s četno četiri nule, po jednoj u svakom retku i stupcu, čije periodično ponavljanje daje povezane jedinice — npr. nule u pozicijama $(0,0), (1,2), (2,1), (3,3)$ (ili slično). Umjesto ručne potrage, enumeriraj sve $\binom{16}{4}$ uzorka i provjeri programski.</p>'''),
        ('Algoritam', r'''<p>Za $n, m \ge 4$: ponovi pronađeni uzorak $4 \times 4$ periodično (obrezan na $n \times m$); ako neka od četiri „faza” daje veći broj jedinica (zbog obrezivanja), izaberi najbolju od pomaka. Za $\min(n, m) \le 3$ obradi zasebno: za $2 \times m$ i $3 \times m$ maksimum se dobiva uzorcima u kojima svaki redak ima nulu na svakom četvrtom mjestu, poravnatim tako da su jedinice povezane; jedini izuzetak je $3 \times (4k + 3)$, kod kojega naivna podjela na $1 \times 4$ ostavlja nepovezane blokove $3 \times 3$, pa treba posebna konstrukcija s jednom nulom više nego što daje gruba granica. Uvijek lokalno provjeri konstrukciju BFS-om prije ispisa.</p>'''),
        ('Složenost', r'''<p>$O(nm)$ po testu za ispis i provjeru; ukupno $O(\sum nm) = O(10^6)$.</p>'''),
    ],
    'solution': r'''
<p>Ako ploču možemo podijeliti na pravokutnike $1 \times 4$, svaki od njih mora sadržavati barem jednu nulu. Označimo ćelije brojem $(i + j) \bmod 4$; svaki pravokutnik $1 \times 4$ sadrži po jednu ćeliju s oznakama $0, 1, 2, 3$, pa broj disjunktnih pravokutnika $1 \times 4$ ne može premašiti najmanji broj ćelija neke oznake, a za $n, m \ge 4$ ta se granica i dostiže. Time dobivamo gornju granicu za broj jedinica: $nm$ minus najmanji broj ćelija jedne oznake.</p>
<p>Isprobavanjem se može uočiti da se ta gornja granica dostiže periodičnom konstrukcijom s uzorkom $4 \times 4$. Stoga možemo enumerirati sve načine na koje se uzorak $4 \times 4$ može ispuniti i lokalno (programom) provjeriti povezanost te dostiže li se maksimum, a zatim ispisati bilo koje rješenje koje zadovoljava uvjete.</p>
<p>Za $n \le 3$ (ili simetrično $m \le 3$) gornji dokaz ne prolazi: ploču ne možemo rezati okomito na pravokutnike $1 \times 4$, pa se granica temeljena na oznakama $0, 1, 2, 3$ ne dostiže. Također, zbog povezanosti, npr. ploču $3 \times 7$ možemo podijeliti samo na $6$ pravokutnika $1 \times 4$, a kad bismo htjeli dostići tu granicu, ostala bi dva nepovezana bloka $3 \times 3$, što nije dopušteno. Nakon analize ispada da samo slučaj $3 \times (4k + 3)$ zahtijeva posebnu konstrukciju; u svim ostalim slučajevima prethodna metoda i dalje daje optimalno rješenje.</p>
''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Dining Professors', 'title_hr': 'Profesori na večeri', 'slug': 'M_dining_professors',
    'tl': '1 s', 'ml': '256 MB',
    'statement': r'''
<p>Za okruglim stolom sjedi $n$ profesora; profesor $i$ susjedan je profesorima $(i \bmod n) + 1$ i $((i + n - 2) \bmod n) + 1$. Na stolu je $n$ pozicija, pozicija $i$ ispred profesora $i$; profesor $i$ doseže jela na pozicijama $i$ i dvije susjedne. Na svaku poziciju stavlja se točno jedno od $n$ jela, od kojih je $a$ ljutih i $n - a$ neljutih.</p>
<p>Neki profesori ne jedu ljuto. Zadovoljstvo profesora koji jede ljuto jednako je broju jela koja doseže (dakle $3$), a zadovoljstvo profesora koji ne jede ljuto jednako je broju neljutih jela koja doseže. Rasporedi jela tako da zbroj zadovoljstava bude najveći i ispiši taj zbroj.</p>
<h3>Ulaz</h3>
<p>Prvi redak sadrži $n, a$ ($3 \le n \le 10^5$, $0 \le a \le n$). Drugi redak sadrži $b_1, \dots, b_n \in \{0, 1\}$; $b_i = 1$ znači da profesor $i$ jede ljuto.</p>
<h3>Izlaz</h3>
<p>Ispiši najveći mogući zbroj zadovoljstava.</p>
<h3>Primjer</h3>
<p>Za $n = 5$, $a = 2$, $b = [1, 0, 1, 0, 1]$ odgovor je $13$.</p>
''',
    'hints': [
        r'''<p>Zamijeni perspektivu: umjesto po profesorima, računaj doprinos svakog <em>jela</em>. Neljuto jelo na poziciji $i$ zadovoljava sva tri profesora koji ga dosežu; ljuto jelo zadovoljava samo one među njima koji jedu ljuto.</p>''',
        r'''<p>Doprinosi pozicija su neovisni, a broj ljutih jela je fiksan ($a$). Greedy: ljuta jela stavi na $a$ pozicija na kojima najviše od trojice dosežućih profesora jede ljuto.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Zbroj zadovoljstava $= \sum_{\text{pozicije } i} (\text{broj profesora među } i-1, i, i+1 \text{ koji smiju jesti jelo na } i)$. Neljuto jelo daje uvijek $3$; ljuto jelo na poziciji $i$ daje $c_i = b_{i-1} + b_i + b_{i+1}$.</p>'''),
        ('Redukcija', r'''<p>Odgovor je $3(n - a) + \sum_{i \in S} c_i$, gdje je $S$ skup od točno $a$ pozicija s ljutim jelima. Pozicije su neovisne, pa je optimalno uzeti $a$ najvećih $c_i$.</p>'''),
        ('Algoritam i složenost', r'''<p>Izračunaj $c_i$ ciklički, sortiraj silazno (ili prebroji koliko je pozicija s $c_i = 3, 2, 1, 0$) i zbroji $a$ najvećih. Složenost $O(n)$ uz brojanje, odnosno $O(n \log n)$ sa sortiranjem.</p>'''),
    ],
    'solution': r'''
<p>Za svako jelo razmotrimo koliko ga profesora može jesti ako je ljuto, odnosno ako nije. Neljuto jelo mogu jesti sva tri profesora koji ga dosežu, a ljuto jelo na poziciji $i$ samo oni među profesorima $i-1$, $i$, $i+1$ (ciklički) koji jedu ljuto.</p>
<p>Želimo da što više profesora može jesti, pa jela raspoređujemo greedy: za svaku poziciju izračunamo koliko bi profesora moglo jesti ljuto jelo na njoj, te ljuta jela stavimo na $a$ pozicija s najvećim tim brojem. Odgovor je $3(n - a)$ plus zbroj odabranih vrijednosti.</p>
<p>Vremenska složenost je $O(n)$.</p>
''',
},
]
