# -*- coding: utf-8 -*-
STAGE = {
    'no': 14,
    'name': 'Stage 14: Ranoa',
    'source_name': 'Osijek Competitive Programming Camp Winter 2023, Day 9: Magical Story of LaLa',
    'source_html': r'''
<p>Autor zadataka i rješenja: Aeren. Prijevod službenog rješenja: <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1214&amp;r=1">Tutorial (en)</a>. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1214&amp;r=0">engleskim tekstovima zadataka</a> (slike i pseudokod iz izvornika nisu reproducirani). Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1214">Universal Cup Judging System</a>.</p>
''',
}

FLIP = r'''
<p>Magični krug jednostavan je poligon; <em>upotrebljiv</em> je ako je konveksan. Alat radi ovako: ako krug nije upotrebljiv, odabire dvije različite točke $u$ i $v$ na rubu konveksne ljuske kruga takve da nijedna druga točka na rubnom putu od $u$ do $v$ (u pozitivnom smjeru) ne leži na rubu konveksne ljuske, te taj put zarotira za $\pi$ oko polovišta $\overline{uv}$: svaka točka $w$ puta prelazi u $u + v - w$ (<em>flipturn</em>). Rezultat je opet jednostavan poligon.</p>
'''

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'LaLa and Magic Circle (LiLi Version)', 'title_hr': 'LaLa i magični krug (LiLi verzija)', 'slug': 'A_lala_and_magic_circle_lili_version',
    'tl': '10 s', 'ml': '1024 MB',
    'statement': r'''
<p><em>Zadatak samo s izlazom (output-only).</em></p>
''' + FLIP + r'''
<p>LiLi želi podvaliti krug za koji alat treba puno koraka. Ispiši jednostavan poligon s $3 \le N \le 1000$ vrhova (cjelobrojne koordinate u $[0, 10^9]$, u pozitivnom smjeru) i valjan niz od $Q$ operacija alata, $120\,000 \le Q \le 1\,000\,000$, opisanih parovima točaka $(a_i, b_i) \to (c_i, d_i)$ (pozitivno orijentirani put od prve do druge), nakon kojih je krug upotrebljiv. Uzastopne stranice smiju činiti kut $\pi$; ništa nije potrebno minimizirati.</p>
<h3>Izlaz</h3>
<p>$N$, koordinate vrhova, $Q$, zatim $Q$ redaka $a_i\ b_i\ c_i\ d_i$.</p>
''',
    'hints': [
        r'''<p>Traži se poligon na kojem flipturn postupak može trajati $\Omega(N^2)$ koraka. Takve su konstrukcije poznate iz literature (Biedl, „Polygons Needing Many Flipturns”). Prvo shvati što flipturn radi s <em>vektorima stranica</em> na zarotiranom putu.</p>''',
        r'''<p>Flipturn ne mijenja vektore stranica, samo im obrće redoslijed. Džep od točno dvije stranice zato samo <em>zamijeni</em> te dvije stranice — kao jedan korak bubble sorta. Želimo poligon u kojem jedna stranica mora proći kroz $\Theta(N)$ takvih zamjena, i to $\Theta(N)$ puta.</p>''',
        r'''<p>Ideja: jedna „strma” skupina stranica sa strogo rastućim nagibima (konveksni lanac) i skupina vodoravnih stranica koje se jedna po jedna „spuštaju” kroz cijeli lanac — svako spuštanje kroz $N/2 - 1$ stranica traje $N/2 - 1$ koraka. Ne ispisuj korake „na slijepo”: simuliraj postupak s eksplicitnom ljuskom.</p>''',
    ],
    'coach': [
        ('Što flipturn zapravo napravi sa stranicama zarotiranog puta?',
         r'''<p>Rotacija za $\pi$ oko polovišta $\overline{uv}$ svaki vektor stranice pomnoži s $-1$, ali zarotirani put ide od $v$ do $u$, a mi rub i dalje obilazimo od $u$ do $v$ — pa ga čitamo unatrag i vektori se još jednom pomnože s $-1$. Neto učinak: <em>isti multiskup vektora stranica, obrnut redoslijed na putu</em>. Posebno, džep od dvije stranice $d_a, d_b$ postaje $d_b, d_a$ (zamjena susjeda), a džep $s, s, \dots, s, h$ s kolinearnim $s$ postaje $h, s, \dots, s$ (jedna stranica „preskoči” blok). Konačni konveksni poligon ima stranice sortirane po kutu, pa je postupak neka vrsta sortiranja zamjenama — i mi želimo da to sortiranje bude što gore, poput bubble sorta na obrnuto sortiranom nizu.</p>'''),
        ('Kako natjerati alat da jednu stranicu pomiče samo za jedno mjesto po koraku?',
         r'''<p>Stavimo konveksni lanac stranica s nagibima $1, 2, \dots, N/2 - 1$ (vektori $(i+1, (i+1)^2)$) i odmah iza njega vodoravnu stranicu $(1, 0)$. Vrh između zadnje stranice lanca (nagib $N/2-1$) i vodoravne stranice je refleksan (nagib pada), a susjedni vrhovi leže na ljusci, pa je džep točno te dvije stranice. Nakon zamjene vodoravna stranica stoji iza stranice nagiba $N/2 - 2$ — opet refleksan vrh, opet džep od dvije stranice. Tako se $(1, 0)$ „spušta” jedno mjesto po koraku kroz cijeli lanac: $N/2 - 1$ koraka.</p>'''),
        ('Zašto ne bismo mogli staviti samo jednu vodoravnu stranicu i kako slažemo ostale?',
         r'''<p>Jedna stranica daje samo $\Theta(N)$ koraka; treba ih $\Theta(N)$ komada, svaka s vlastitim „spuštanjem”. Iza lanca zato naizmjence stavljamo vodoravne stranice (skupina 2) i vrlo strme stranice $(N/2, (N/2)^2)$ (skupina 3), a zadnja stranica zatvara poligon. Strme stranice drže ostatak ruba daleko od lanca, pa džepovi ostaju mali. Kad se $k$-ta vodoravna stranica treba pomaknuti, ispred nje stoji $k - 1$ kolinearnih strmih stranica: <em>jedan</em> flipturn puta $s, \dots, s, h$ preskoči cijeli blok, a zatim slijedi $N/2 - 1$ zamjena kroz lanac. Ukupno $\tfrac{N}{4}\left(\tfrac{N}{2} - 1\right) + \left(\tfrac{N}{4} - 1\right) = \tfrac{N^2}{8} - 1$, za $N = 1000$ točno $124\,999 \ge 120\,000$.</p>'''),
        ('Zašto se isplati simulirati postupak umjesto samo ispisati unaprijed izračunane parove?',
         r'''<p>Zadatak zahtijeva da je svaki korak valjan: oba kraja na rubu ljuske, nijedna druga točka puta na rubu ljuske. To je lako pogrešno pretpostaviti, a program koji <em>simulira</em> alat (održava poligon i njegovu konveksnu ljusku, uvijek bira prvi džep u poretku obilaska i zrcali put) ispisuje samo ono što je stvarno napravio. Ljusku ne treba računati iznova: flipturn ne miče vrhove izvan puta, pa stara ljuska ostaje ljuska tih vrhova, a zrcaljene vrhove puta samo <em>umetnemo</em> u nju standardnim inkrementalnim postupkom (uklonimo bridove vidljive iz nove točke) i pritom ažuriramo oznake „vrh je na rubu ljuske”. Po koraku je to $O(N)$, ukupno $O(N^3/8) \approx 1.25 \cdot 10^8$ jednostavnih operacija — daleko ispod 10 s.</p>'''),
    ],
    'tips': [
        r'''Kod „konstruiraj loš slučaj” zadataka prvo nađi <strong>invarijantu</strong> postupka (ovdje: multiskup vektora stranica) — ona kaže što se ne može ubrzati i sugerira sortiranje kao model, a poznati najgori slučajevi sortiranja (bubble sort) daju konstrukciju.''',
        r'''Za output-only zadatke napiši <strong>neovisni validator</strong> koji provjerava sve uvjete iz teksta (format, raspone, jednostavnost, valjanost svakog koraka, konačni uvjet). Konstrukcija koja „izgleda točno” često pada na detalju poput kolinearnih vrhova ili točke na rubu ljuske.''',
        r'''Kad geometrijski postupak samo <em>proširuje</em> objekt (ljuska raste), ažuriraj strukturu inkrementalno umjesto iznova — često pretvori $O(N \log N)$ po koraku u $O(N)$ ili manje, a kod ostaje jednostavan.''',
    ],
    'solution': r'''
<p>Evo jedne moguće konstrukcije. Neka je $N$ pozitivan cijeli broj djeljiv s $4$ i neka je $d_i$ vektor smjera $i$-te stranice u pozitivnom smjeru.</p>
<ul>
<li>(Skupina 1) Za svaki $0 \le i \le N/2 - 2$: $d_i = (i + 1, (i + 1)^2)$.</li>
<li>(Skupina 2) Za svaki neparan $i$ s $N/2 - 1 \le i \le N - 2$: $d_i = (1, 0)$.</li>
<li>(Skupina 3) Za svaki paran $i$ s $N/2 - 1 \le i \le N - 2$: $d_i = (N/2, (N/2)^2)$.</li>
</ul>
<p>Spuštanje prve stranice skupine 2 kroz svih $N/2 - 1$ stranica skupine 1, a zatim spuštanje preostalih $N/4 - 1$ stranica skupine 2 jedne po jedne redom daje niz operacija duljine $N^2/8 - 1$, što za $N = 1000$ iznosi $124\,999$.</p>
<p>Zasluge za konstrukciju pripadaju radu „Polygons Needing Many Flipturns” Therese Biedl (ilustracije konstrukcije nalaze se u izvornom rješenju).</p>
''',
    'detailed': r'''
<h3>1. Što flipturn radi s vektorima stranica</h3>
<p>Neka je put od $u$ do $v$ (u pozitivnom smjeru) sastavljen od stranica s vektorima $d_1, d_2, \dots, d_k$, pa je $v = u + d_1 + \dots + d_k$. Točkasta refleksija $w \mapsto u + v - w$ oko polovišta $\overline{uv}$ preslikava vrh $u + d_1 + \dots + d_j$ u $v - d_1 - \dots - d_j$. Zarotirani put, čitan od $u$ prema $v$ (tako ga obilazimo nakon operacije), prolazi vrhove $u,\; v - d_1 - \dots - d_{k-1},\; \dots,\; v - d_1,\; v$; razlike susjednih vrhova su redom $d_k, d_{k-1}, \dots, d_1$.</p>
<p>Dakle: <strong>flipturn ne mijenja multiskup vektora stranica poligona, samo obrće njihov redoslijed na zarotiranom putu.</strong> Dvije posljedice koje ćemo koristiti:</p>
<ul>
<li>džep od točno dvije stranice $d_a, d_b$ nakon flipturna glasi $d_b, d_a$ — operacija je <em>zamjena susjeda</em>;</li>
<li>džep $s, s, \dots, s, h$ (blok od $k - 1$ jednakih stranica pa jedna druga) postaje $h, s, \dots, s$ — stranica $h$ preskoči cijeli blok u jednom koraku.</li>
</ul>
<p>Konačni krug je konveksan poligon s istim vektorima stranica, dakle s tim vektorima <em>sortiranima po kutu</em>. Postupak je zato neka vrsta sortiranja zamjenama, a mi tražimo ulaz na kojem ono traje $\Omega(N^2)$ — kao bubble sort na obrnuto sortiranom nizu. Površina se svakim flipturnom strogo povećava (poligonu se dodaju džep i njegova zrcalna slika), pa postupak uvijek završava; ne treba nas brinuti mogućnost beskonačne petlje.</p>
<h3>2. Konstrukcija</h3>
<p>Neka je $N$ djeljiv s $4$ i neka $d_i$ označava vektor $i$-te stranice u pozitivnom smjeru ($0 \le i \le N - 2$; stranica $N - 1$ zatvara poligon i jednaka je $-\sum_{i < N-1} d_i$).</p>
<ul>
<li><strong>Skupina 1 (lanac):</strong> $d_i = (i + 1, (i + 1)^2)$ za $0 \le i \le N/2 - 2$. Nagibi su $1, 2, \dots, N/2 - 1$, strogo rastu, pa je to konveksan lanac koji skreće lijevo u svakom vrhu.</li>
<li><strong>Skupina 2 (vodoravne):</strong> $d_i = (1, 0)$ za neparne $i$ s $N/2 - 1 \le i \le N - 2$. Ima ih $N/4$.</li>
<li><strong>Skupina 3 (strme):</strong> $d_i = (N/2, (N/2)^2)$ za parne takve $i$. Ima ih $N/4$, sve su jednake (kolinearne) i nagiba $N/2$, strmije od svake stranice lanca.</li>
</ul>
<p>Budući da je $N/2$ paran, prvi indeks $N/2 - 1$ je neparan: iza lanca dolazi vodoravna stranica, zatim naizmjence strma, vodoravna, strma, …, a niz završava strmom stranicom $d_{N-2}$. Vrh između stranice nagiba $N/2 - 1$ i vodoravne stranice je refleksan (nagib padne s $N/2 - 1$ na $0$), kao i svaki vrh „strma $\to$ vodoravna”. Vrhovi „vodoravna $\to$ strma” su konveksni.</p>
<p>Početni vrh stavimo u $(2 \cdot 10^8, 2 \cdot 10^8)$. Ukupni pomak po $x$ je $\sum_{i=1}^{N/2-1} i + \tfrac{N}{4} \cdot 1 + \tfrac{N}{4} \cdot \tfrac{N}{2} \approx 2.5 \cdot 10^5$, a po $y$ oko $\sum_{i=1}^{N/2-1} i^2 + \tfrac{N}{4} \cdot \tfrac{N^2}{4} \approx 1.05 \cdot 10^8$ za $N = 1000$. Refleksije $w \mapsto u + v - w$ pomiču vrhove najviše za dimenzije trenutne ljuske, pa uz pomak od $2 \cdot 10^8$ sve koordinate cijelo vrijeme ostaju u $[0, 10^9]$ (validator to i provjerava za svaki korak).</p>
<h3>3. Zašto postupak traje $N^2/8 - 1$ koraka</h3>
<p>Alat smije birati bilo koji džep; mi kao „alat” uvijek biramo <em>prvi</em> džep u poretku obilaska od vrha $0$. Pratimo što se događa.</p>
<ol>
<li><strong>Prva vodoravna stranica</strong> $h_1 = d_{N/2-1}$ stoji odmah iza zadnje stranice lanca. Vrh između njih je refleksan, a oba susjedna vrha leže na ljusci, pa je džep točno $\{d_{N/2-2}, h_1\}$ i flipturn ih zamijeni. Sada $h_1$ stoji iza stranice nagiba $N/2 - 2$: opet refleksan vrh, opet džep od dvije stranice. Nakon $N/2 - 1$ zamjena $h_1$ je ispred cijelog lanca (nagib $0$ je najmanji, vrh je konveksan) i više se ne miče.</li>
<li><strong>$k$-ta vodoravna stranica</strong> ($k \ge 2$): ispred nje su sada, redom, lanac i $k - 1$ kolinearnih strmih stranica $s$ (one koje su bile između prvih $k$ vodoravnih). Vrhovi između kolinearnih stranica su ravni (kut $\pi$) i nisu na rubu ljuske, pa je prvi džep u obilasku put $s, \dots, s, h_k$ od početka prve strme stranice do kraja $h_k$. Jedan flipturn ga obrne u $h_k, s, \dots, s$: $h_k$ je preskočila blok i sada stoji iza zadnje stranice lanca. Slijedi $N/2 - 1$ zamjena kroz lanac, kao za $h_1$.</li>
</ol>
<p>Nakon što svih $N/4$ vodoravnih stranica dođe ispred lanca, poligon glasi: $N/4$ vodoravnih, lanac, $N/4$ strmih, zatvarajuća stranica — nagibi rastu, svi su vrhovi konveksni, krug je upotrebljiv. Broj koraka je
$$\frac{N}{4}\left(\frac{N}{2} - 1\right) + \left(\frac{N}{4} - 1\right) = \frac{N^2}{8} - \frac{N}{4} + \frac{N}{4} - 1 = \frac{N^2}{8} - 1,$$
što za $N = 1000$ daje $124\,999$, unutar traženog $[120\,000, 10^6]$. Za $N = 8$ to je $7$ koraka, što se lako provjeri ručno.</p>
<p>Gornji opis džepova ovisi o tome koji su vrhovi na ljusci — a to nije očito (Biedl to dokazuje u radu). Zato se u rješenju <em>ne oslanjamo</em> na taj opis: program stvarno simulira alat.</p>
<h3>4. Simulacija</h3>
<ol>
<li>Izgradi početni poligon i njegovu konveksnu ljusku (monotoni lanac). Za svaki vrh zapamti je li na <em>rubu</em> ljuske (uključivo točke na bridovima ljuske — takve po definiciji nisu unutrašnje točke džepa).</li>
<li>Dok postoji vrh koji nije na rubu ljuske: nađi prvi vrh $u$ (u poretku indeksa) koji je na rubu, a sljedeći nije; put nastavi do prvog vrha $v$ koji je opet na rubu. To je džep: krajevi na ljusci, unutrašnjost strogo unutra. Zapiši korak $(u, v)$.</li>
<li>Vrhove između $u$ i $v$ obrni i zrcali: $w \mapsto u + v - w$.</li>
<li>Svaki zrcaljeni vrh umetni u ljusku inkrementalno: nađi ciklički interval bridova ljuske iz kojih je točka vidljiva, ukloni ih i zamijeni dvama novim bridovima. Vrhovi koji su ležali na uklonjenim bridovima gube oznaku „na rubu”, vrhovi na novim bridovima je dobivaju. Vrhovi izvan puta se ne miču, pa je stara ljuska i dalje ljuska preostalih vrhova, a umetanje novih točaka daje točnu novu ljusku.</li>
</ol>
<p>Jedan korak košta $O(N)$ (pretraga džepa i umetanje), pa je ukupno $O(N \cdot N^2/8) \approx 1.25 \cdot 10^8$ elementarnih operacija; program radi ispod $1.5$ s.</p>
<h3>5. Zamke</h3>
<ul>
<li><strong>Kolinearni vrhovi.</strong> Nakon flipturna susjedne stranice smiju činiti kut $\pi$ (tekst to dopušta), ali takav vrh <em>nije</em> vrh ljuske. Ako ga pogrešno označimo kao „na ljusci”, džep se skrati i korak postane nevaljan. Zato oznaku računamo kao „leži na nekom bridu ljuske”, a ne „jest vrh ljuske”.</li>
<li><strong>Vektorski produkti.</strong> Koordinate su do $10^9$, pa produkti razlika idu do $\sim 10^{18}$: obavezno 64-bitni cijeli brojevi; uz pomak $2 \cdot 10^8$ i dimenzije ljuske $\sim 10^8$ nema prelijevanja.</li>
<li><strong>Ispis.</strong> Ispisuje se <em>početni</em> poligon (ne konačni) i $Q$ redaka s koordinatama krajeva puta u trenutku operacije. Ispis od $125\,000$ redaka radimo jednim <code>fwrite</code>.</li>
<li><strong>Provjera.</strong> Neovisni validator (<code>check.py</code>) provjerava raspone, različitost vrhova, jednostavnost i orijentaciju poligona te za svaki korak da su krajevi na rubu trenutne ljuske i da nijedan unutrašnji vrh puta nije na njemu; za male $N$ ljusku računa iznova nakon svakog koraka. Na kraju traži da su svi vrhovi na ljusci i svi zavoji lijevi ili ravni.</li>
</ul>
''',
    'verified': r'''Zadatak je output-only, pa nema brute forcea: neovisni validator <code>check.py</code> (format, rasponi, jednostavan CCW poligon, valjanost svakog flipturna uz ljusku računanu iznova za $N \le 120$, konačna konveksnost) prihvatio je 300 slučajnih konstrukcija s $N \in \{8, 12, \dots, 200\}$ i 3 puna izlaza za $N = 1000$ ($124\,999$ koraka, najviše 1.45 s).''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'LaLa and Magic Circle (LaLa Version)', 'title_hr': 'LaLa i magični krug (LaLa verzija)', 'slug': 'B_lala_and_magic_circle_lala_version',
    'tl': '2 s', 'ml': '1024 MB',
    'statement': FLIP + r'''
<p>LaLa je uočila: (1) krug u konačno mnogo koraka postaje upotrebljiv; (2) konačni krug ne ovisi o redoslijedu koraka. Za dani jednostavan poligon s $N$ vrhova izračunaj konačni konveksni poligon.</p>
<h3>Ulaz</h3>
<p>$N$ ($3 \le N \le 100\,000$) i vrhovi $(x_i, y_i)$, $0 \le x_i, y_i \le 300\,000$, u pozitivnom smjeru, bez samopresjeka.</p>
<h3>Izlaz</h3>
<p>$M$ i vrhovi konačnog konveksnog poligona u pozitivnom smjeru, počevši od leksikografski najmanjeg, bez triju kolinearnih uzastopnih vrhova. Rješenje je jedinstveno.</p>
<h3>Primjer</h3>
<p>Za poligon $(1,0),(4,0),(6,0),(3,1),(5,2),(2,1),(6,3),(0,2)$ odgovor je $(0,2),(1,0),(6,0),(12,3),(9,4),(3,3)$.</p>
''',
    'hints': [
        r'''<p>Što flipturn čuva? Multiskup nagiba (i duljina) usmjerenih stranica — samo se njihov redoslijed mijenja. Dakle <em>oblik</em> konačnog konveksnog poligona je poznat: sortiraj stranice po kutu. Ostaje odrediti <em>položaj</em>.</p>''',
        r'''<p>Traži invarijantu za položaj: dekomponiraj vanjsko područje poligona vodoravnim rezovima na trapeze, označi konačne trapeze kao „gore”/„dolje” ovisno o tome kamo treba ići do beskonačnog područja. Zbroj visina „gore” trapeza + najveća $y$-koordinata ne mijenja se flipturnom.</p>''',
    ],
    'coach': [
        ('Što se pri flipturnu sigurno ne mijenja, a što se sigurno mijenja?',
         r'''<p>Točkasta refleksija oko polovišta $\overline{uv}$ množi vektore stranica puta s $-1$, ali put se nakon toga obilazi u suprotnom smjeru, pa vektori ostaju isti — samo im se obrne redoslijed. Multiskup <em>usmjerenih</em> vektora stranica je invarijanta. S druge strane, površina strogo raste: novi poligon je stari plus džep plus njegova zrcalna slika. Zato postupak završava, a konačni poligon je konveksan poligon sastavljen od istih vektora — a konveksan poligon s danim vektorima stranica jedinstven je do na translaciju (vektori moraju biti sortirani po kutu). Oblik je, dakle, poznat odmah.</p>'''),
        ('Ako znamo oblik, zašto položaj nije trivijalan?',
         r'''<p>Svaki flipturn pomiče dio poligona „prema van”, a koji se džep kada okreće ne znamo (i tekst kaže da rezultat ne ovisi o tome). Treba nam veličina koja ovisi o položaju, ne mijenja se nijednim flipturnom i na konveksnom poligonu se lako pročita. Prirodni kandidati su najveća $x$- i $y$-koordinata — ali one se mijenjaju. Ideja: popraviti ih nekom mjerom „koliko se poligon još mora proširiti” u tom smjeru.</p>'''),
        ('Koja mjera „nedovršenosti” daje točno tu invarijantu?',
         r'''<p>Razreži vanjštinu poligona vodoravnim pravcima kroz vrhove na trapeze. Ograničeni trapezi leže samo u džepovima (izvan ljuske svaka vodoravna zraka odlazi u beskonačnost). Svaki takav trapez označi „gore” ili „dolje” prema tome kamo se iz njega mora ići (bez prelaska ruba) do beskonačnosti. Neka je $U$ zbroj visina „gore” trapeza, $Y$ najveća $y$-koordinata. Tvrdnja (rad „Flipturning Polygons”): $U + Y$ se ne mijenja flipturnom. Intuitivno, „gore” trapezi su upravo praznine koje će se, kad se džepovi izokrenu, pretvoriti u visinu iznad sadašnjeg vrha. Konveksan poligon nema ograničenih trapeza, pa je $Y_{\text{kon}} = Y_0 + U_0$; isto s okomitim rezovima (zarotiraj koordinate za $90^\circ$) daje $X_{\text{kon}}$.</p>'''),
        ('Kako izračunati $U$ u $O(N \log N)$ i kako odlučiti je li trapez „gore”?',
         r'''<p>Klasični sweep po $y$: događaji su različite $y$-koordinate vrhova, aktivne su nevodoravne stranice koje sijeku trenutnu razinu, poredane po $x$ u uravnoteženom stablu (<code>std::set</code>). Kod pozitivno orijentiranog poligona unutrašnjost je lijevo od smjera obilaska, pa je stranica koja ide <em>gore</em> lijevi zid vanjskog trapeza, a stranica koja ide <em>dolje</em> desni zid. Krenimo obilazak od najnižeg (leksikografski najmanjeg) vrha, koji je sigurno na ljusci. Ako se desni zid $f$ (ide dolje) u obilasku pojavljuje <em>prije</em> lijevog zida $e$ (ide gore), dio ruba između njih spaja donje krajeve zidova i zatvara trapez odozdo, pa je izlaz prema gore; inače rub spaja gornje krajeve i trapez je „dolje”. Između dva događaja svaki susjedni par (gore-stranica, dolje-stranica) s tim svojstvom pridonosi visinu sloja; broj takvih parova održavamo pri umetanju i brisanju iz skupa.</p>'''),
        ('Kako od vektora i dviju koordinata složiti ispis?',
         r'''<p>Sortiraj vektore stranica po kutu (polovina ravnine pa vektorski produkt, bez trigonometrije), spoji uzastopne kolinearne istog smjera, prefiksnim zbrojevima dobij vrhove, translatiraj tako da najveći $x$ bude $X_{\text{kon}}$ i najveći $y$ bude $Y_{\text{kon}}$, pa ispis rotiraj na leksikografski najmanji vrh. Ukupno $O(N \log N)$.</p>'''),
    ],
    'tips': [
        r'''Za procese koji „nešto preslaguju” (rotacije, refleksije, zamjene) prvo popiši <strong>invarijante</strong>: multiskup dijelova koji se ne mijenja obično fiksira oblik odgovora, a monotona veličina (površina, potencijal) dokazuje završavanje.''',
        r'''Kad je rezultat određen do na translaciju, dovoljno je naći <strong>jednu koordinatu po osi</strong> — traži invarijantu oblika „trenutna vrijednost + mjera nedovršenosti”, kao potencijalnu funkciju.''',
        r'''U sweepu po $y$ stranice se međusobno ne sijeku, pa se mogu uspoređivati po $x$ na <em>sredini zajedničkog raspona visina</em>; formulu pomnoži nazivnicima i uspoređuj cijele brojeve u 64 bita umjesto razlomaka ili <code>double</code>.''',
        r'''Sortiranje vektora po kutu radi bez <code>atan2</code>: prvo po polovini ravnine ($y > 0$ ili $y = 0, x > 0$ u prvu), zatim po znaku vektorskog produkta.''',
    ],
    'solution': r'''
<p>Dokazivanje tvrdnji iz teksta zadatka daje i algoritam.</p>
<p>Konačni „oblik” je fiksiran, jer površina uvijek raste, a multiskup nagiba usmjerenih stranica se ne mijenja.</p>
<p>Za položaj promotrimo vodoravnu trapezoidnu dekompoziciju vanjskog područja poligona. Svako konačno područje označimo s „gore” ili „dolje”, ovisno o smjeru u kojem se treba kretati da bi se došlo do nekog beskonačnog područja. Neka je $U$ zbroj visina „gore” područja, a $Y$ najveća $y$-koordinata. Tada je $U + Y$ invarijantno tijekom operacija. Budući da je $U = 0$ za konačni konveksni poligon, taj zbroj odmah daje najveću $y$-koordinatu konačnog poligona.</p>
<p>Isti postupak s okomitom trapezoidnom dekompozicijom daje najveću $x$-koordinatu.</p>
<p>Referentni rad: „Flipturning Polygons”.</p>
''',
    'detailed': r'''
<h3>1. Oblik konačnog poligona</h3>
<p>Neka flipturn zarotira put od $u$ do $v$ s vektorima stranica $d_1, \dots, d_k$. Točkasta refleksija $w \mapsto u + v - w$ preslika vrh $u + d_1 + \dots + d_j$ u $v - d_1 - \dots - d_j$. Novi rub obilazimo od $u$ do $v$ preko točaka $u,\ v - d_1 - \dots - d_{k-1},\ \dots,\ v - d_1,\ v$, čije su razlike redom $d_k, d_{k-1}, \dots, d_1$. Dakle <strong>multiskup vektora stranica se ne mijenja</strong>, samo im se obrne redoslijed na putu. Stranice izvan puta netaknute su.</p>
<p>Novi poligon sadrži stari, džep (područje između puta i tetive $\overline{uv}$) i njegovu zrcalnu sliku, pa površina strogo raste; kako je vektora stranica konačno mnogo, a svaka konfiguracija (redoslijed i položaj) ima određenu površinu, postupak završava (to je tvrdnja (1) iz teksta). Završava upravo kad nema džepa — kad je poligon konveksan. Konveksan poligon s danim multiskupom vektora stranica jedinstven je do na translaciju: obilazeći ga u pozitivnom smjeru kutovi stranica strogo rastu, pa je jedini mogući redoslijed sortirani, a kolinearni istosmjerni vektori spajaju se u jednu stranicu. <em>Oblik</em> je time određen; ostaje <em>položaj</em>, tj. jedna $x$- i jedna $y$-koordinata.</p>
<h3>2. Vodoravna trapezoidna dekompozicija vanjštine</h3>
<p>Kroz svaki vrh povucimo vodoravni pravac i vanjštinu poligona razrežimo na trake; unutar trake vanjština se raspada na trapeze (ili trokute) čiji su bočni zidovi stranice poligona. Trapez koji se prostire u beskonačnost zovemo neograničenim. <strong>Ograničeni trapezi leže samo u džepovima:</strong> ako je točka izvan konveksne ljuske, vodoravni presjek ljuske na njezinoj visini je interval, a točka je lijevo ili desno od njega, pa vodoravna zraka u smjeru od ljuske nikad više ne dotakne poligon.</p>
<p>Poligon je pozitivno orijentiran, pa je unutrašnjost lijevo od smjera obilaska. Stranica koja ide <em>gore</em> ima vanjštinu desno od sebe — ona je <em>lijevi</em> zid vanjskog trapeza; stranica koja ide <em>dolje</em> je <em>desni</em> zid. Svaki ograničeni trapez stoga ima lijevi zid $e$ (gore) i desni zid $f$ (dolje).</p>
<p>Iz ograničenog trapeza do beskonačnosti se stiže (bez prelaska ruba) kroz susjedne trapeze preko vodoravnih rezova, tj. gore ili dolje; trapez označimo <strong>„gore”</strong> ako se mora ići gore, inače „dolje”. Neka je $U$ zbroj visina „gore” trapeza, a $Y$ najveća $y$-koordinata poligona.</p>
<h3>3. Invarijanta $U + Y$</h3>
<p><strong>Tvrdnja.</strong> Flipturn ne mijenja $U + Y$. Ovo je rezultat rada „Flipturning Polygons” (Aichholzer i dr.), gdje je dan potpuni dokaz; tu ćemo ga učiniti uvjerljivim i provjeriti na primjerima.</p>
<p><em>Ideja.</em> Neka flipturn okreće džep $R$ s tetivom $\overline{uv}$. Trapezi izvan $R$ ne mijenjaju se: njihovi zidovi su stranice izvan puta, a vodoravna dužina unutar drugog džepa ne može ući u $R$ (morala bi izaći iz ljuske i vratiti se). Sve promjene događaju se u $R$ i u njegovoj zrcalnoj slici $R'$. Točkasta refleksija oko polovišta preslikava „gore” u „dolje” i obrnuto te čuva visine; nakon okreta $R$ je unutrašnjost, a u $R'$ nastaju novi džepovi između zrcaljenog puta i nove ljuske. Pažljivim prebrojavanjem (rad) izlazi da su visine „gore” trapeza koje su nestale u $R$ točno nadoknađene porastom $Y$ (kad je džep bio na vrhu) odnosno novim „gore” trapezima u $R'$ — i jednako za „dolje” trapeze u zrcalnoj verziji tvrdnje. Kako flipturnovi komutiraju u smislu konačnog rezultata, dovoljno je vjerovati tvrdnji za jedan korak.</p>
<p><em>Primjer.</em> Pravokutnik s urezom: $(0,0), (4,0), (4,2), (3,2), (2,1), (1,2), (0,2)$. Jedini ograničeni trapez je urez: lijevi zid $(2,1) \to (1,2)$ ide gore, desni zid $(3,2) \to (2,1)$ ide dolje, iz njega se izlazi gore; visina $1$. Dakle $U = 1$, $Y = 2$, predviđeno $Y_{\text{kon}} = 3$. Flipturn puta $(3,2), (2,1), (1,2)$ oko točke $(2,2)$ daje $(3,2), (2,3), (1,2)$: sada je $Y = 3$, a dva mala džepa uz $(3,2)$ i $(1,2)$ ne sadrže ograničene trapeze (vodoravne zrake iz njih odlaze u beskonačnost), pa je $U = 0$ i zbroj je opet $3$. Dva daljnja flipturna daju konveksni poligon $(0,0), (4,0), (4,2), (3,3), (1,3), (0,2)$ s najvišim $y = 3$. Točno.</p>
<p><em>Primjer iz zadatka.</em> Za poligon $(1,0), (4,0), (6,0), (3,1), (5,2), (2,1), (6,3), (0,2)$ je $Y_0 = 3$ i konačni vrh ima $y = 4$, pa je $U_0 = 1$ (vodoravno); okomito je $X_0 = 6$, konačno $12$, pa okomiti $U_0 = 6$. Konačni poligon $(0,2), (1,0), (6,0), (12,3), (9,4), (3,3)$ upravo je sortiranjem vektora stranica pomaknut tako da mu je najveći $x$ jednak $12$ i najveći $y$ jednak $4$.</p>
<p>Za konveksan poligon nema ograničenih trapeza, $U = 0$, pa je $Y_{\text{kon}} = Y_0 + U_0$. Rotacijom koordinata za $90^\circ$, $(x, y) \mapsto (-y, x)$ (čuva orijentaciju), najveći $x$ postaje najveći $y$ i isti postupak daje $X_{\text{kon}}$.</p>
<h3>4. Računanje $U$ sweepom</h3>
<p>Rub obilazimo od leksikografski najmanjeg vrha $s$ (najmanji $x$, pa $y$); on je vrh ljuske, dakle nije unutar nijednog džepa. Svakoj stranici dodijelimo redni broj u tom obilasku.</p>
<p><strong>Kako odlučiti „gore”/„dolje”?</strong> Neka trapez $T$ ima lijevi zid $e$ (gore) i desni zid $f$ (dolje). Dio ruba između $f$ i $e$ (u smjeru obilaska) ne siječe $T$. Ako $f$ dolazi prije $e$, taj dio ruba kreće od donjeg kraja $f$ (obilazimo ga prema dolje) i završava u donjem kraju $e$ (ulazimo u njega odozdo), pa obilazi $T$ <em>ispod</em> — izlaz prema gore. Ako $e$ dolazi prije $f$, dio ruba između njih spaja gornje krajeve i zatvara $T$ odozgo — izlaz prema dolje. Preostali dio ruba prolazi kroz $s$, koji je na ljusci, i ne može zatvoriti $T$ i s druge strane, jer bi tada $T$ bio potpuno ograđen rubom, a ne dio vanjštine povezane s beskonačnošću preko džepova. Dakle: <strong>trapez je „gore” točno kad njegov desni zid ima manji redni broj od lijevog.</strong></p>
<p><strong>Sweep.</strong> Događaji su različite $y$-koordinate vrhova, sortirane. Nevodoravne stranice zapišemo s donjim i gornjim krajem, oznakom smjera (gore/dolje) i rednim brojem; vodoravne preskačemo (ne omeđuju trapeze bočno). U <code>std::set</code> držimo aktivne stranice poredane po $x$. Na razini $y_k$ najprije izbrišemo stranice koje tu završavaju, zatim umetnemo one koje tu počinju, pa sloju $[y_k, y_{k+1}]$ dodamo visinu $(y_{k+1} - y_k) \cdot c$, gdje je $c$ broj susjednih parova (lijevo $e$ ide gore, desno $f$ ide dolje, redni broj $f$ manji od $e$) u skupu. Vrijednost $c$ održavamo pri svakom umetanju/brisanju: oduzmemo doprinos parova koji se razdvajaju, dodamo doprinos novih susjednih parova — $O(1)$ provjera po događaju. Između dviju razina skup se ne mijenja, pa je doprinos sloja točan.</p>
<p><strong>Usporedba stranica.</strong> Stranice jednostavnog poligona ne sijeku se, pa je poredak po $x$ dobro definiran na cijelom zajedničkom rasponu visina $[\text{lo}, \text{hi}]$; uspoređujemo $x$ na sredini $y_m = (\text{lo} + \text{hi})/2$. Za stranicu od $(l_x, l_y)$ do $(h_x, h_y)$ je $x(y_m) = l_x + (y_m - l_y)\frac{h_x - l_x}{h_y - l_y}$; pomnožimo s $2(h_y - l_y)$ obje stranice i uspoređujemo cijele brojeve. Koordinate su $\le 3 \cdot 10^5$, pa su produkti tri faktora reda $10^{17}$ — stanu u 64 bita. Kod stranica koje se dodiruju u vrhu sredina zajedničkog raspona je strogo unutar oba raspona (dijele barem cijelu traku), pa je i tada usporedba stroga; jednakost razriješimo rednim brojem.</p>
<h3>5. Ispis konačnog poligona</h3>
<ol>
<li>Vektore stranica $d_i = P_{i+1} - P_i$ sortiramo po kutu bez trigonometrije: prvo polovina ravnine ($y > 0$ ili $y = 0, x > 0$ prije ostalih), zatim po znaku vektorskog produkta. Rezultat počinje vektorom najmanjeg kuta u $[0, 2\pi)$.</li>
<li>Uzastopne kolinearne istosmjerne vektore spojimo (zbroj) — time nema triju kolinearnih uzastopnih vrhova.</li>
<li>Prefiksnim zbrojevima od $(0,0)$ dobijemo vrhove; zbroj svih vektora je $0$, pa se poligon zatvara. Vrhovi su u pozitivnom smjeru jer kutovi rastu.</li>
<li>Translatiramo za $(X_{\text{kon}} - \max x,\ Y_{\text{kon}} - \max y)$ i ispis rotiramo tako da počinje leksikografski najmanjim vrhom.</li>
</ol>
<h3>6. Složenost i zamke</h3>
<ul>
<li>Sortiranje događaja, sweep i sortiranje vektora: $O(N \log N)$ za $N \le 10^5$, oko $0.2$ s uključujući velike testove.</li>
<li>$U$ može biti do $\sim N \cdot 3 \cdot 10^5 \cdot$ (broj parova), sve u <code>long long</code>; koordinate konačnog poligona u praksi ostaju reda $10^6$–$10^7$, ali ispis radimo u 64 bita.</li>
<li>Stranice koje počinju i završavaju na istoj razini (vodoravne) ne ulaze u sweep; vrhovi lokalnih minimuma i maksimuma dodaju odnosno brišu dvije stranice odjednom — redoslijed „prvo brisanje, zatim umetanje” jamči da se stranice koje se samo dodiruju u vrhu ne uspoređuju.</li>
<li>Za okomitu verziju koristimo rotaciju $(x, y) \mapsto (-y, x)$, a ne zrcaljenje — zrcaljenje bi promijenilo orijentaciju i pravilo lijevi/desni zid.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 (u ranijem pokretanju i 1500) slučajnih malih jednostavnih poligona s $N \le 9$ i koordinatama $\le 12$ protiv brute forcea koji doslovno simulira flipturnove (ljuska iznova, prvi džep, zrcaljenje) do konveksnosti; 3 velika testa s $N = 10^5$ (zvjezdasti i cik-cak „češalj” s mnogo džepova, najviše 0.17 s).''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'LaLa and Lamp', 'title_hr': 'LaLa i lampa', 'slug': 'C_lala_and_lamp',
    'tl': '3 s', 'ml': '1024 MB',
    'statement': r'''
<p>Lampa je trokutasta mreža sa stranicom $N$: $i$-ti redak ($0 \le i < N$) ima $i + 1$ žarulja, svaka upaljena ili ugašena. Jednim potezom LaLa bira jedan od tri smjera paralelna stranicama trokuta i jedan „redak” u tom smjeru te invertira stanje svih žarulja u njemu. Može li ugasiti sve žarulje?</p>
<h3>Ulaz</h3>
<p>$N$ ($2 \le N \le 2000$) i $N$ binarnih nizova $S_i$ duljine $i + 1$.</p>
<h3>Izlaz</h3>
<p><code>Yes</code> ili <code>No</code>.</p>
<h3>Primjer</h3>
<p>Za $N = 6$ i retke <code>0, 00, 000, 0110, 00100, 000000</code> odgovor je <code>Yes</code>.</p>
''',
    'hints': [
        r'''<p>Operacije komutiraju i svaka je sama sebi inverz — bitno je samo koje se od $3N$ linija invertiraju (skup, ne niz). To je linearni sustav nad $\mathbb{Z}_2$ s $3N$ nepoznanica; Gauss bi bio prespor za $N^2/2$ jednadžbi.</p>''',
        r'''<p>Većina nepoznanica je forsirana: kad fiksiraš dva najdulja retka u jednom smjeru i najdulji redak u drugom, sve ostale linije jednoznačno se određuju ćeliju po ćeliju.</p>''',
    ],
    'coach': [
        ('Zašto redoslijed poteza nije bitan i što onda zapravo biramo?',
         r'''<p>Svaki potez invertira fiksan skup žarulja, a inverzija je zbrajanje $1$ modulo $2$ — komutativno i asocijativno. Dva ista poteza zbroje $2 \equiv 0$, dakle se ponište. Rezultat zato ovisi samo o tome koje su linije invertirane <em>neparan</em> broj puta: biramo podskup od $3N$ linija ($N$ redaka, $N$ „stupaca”, $N$ dijagonala). Stanje ćelije $(i, j)$ na kraju je $s_{ij} \oplus r_i \oplus c_j \oplus d_{i-j}$, pa tražimo $r, c, d \in \{0,1\}^N$ s $r_i \oplus c_j \oplus d_{i-j} = s_{ij}$ za sve ćelije. To je linearni sustav nad $\mathbb{Z}_2$: $3N$ nepoznanica, $N(N+1)/2$ jednadžbi.</p>'''),
        ('Zašto ne Gaussova eliminacija?',
         r'''<p>Sustav ima $\sim 2 \cdot 10^6$ jednadžbi i $6000$ nepoznanica; eliminacija bi koštala $O(N^2 \cdot 3N / 64)$ operacija na bitsetima — reda $10^8$–$10^9$ — a i memorija bi bila problem. No sustav je vrlo posebnog oblika: svaka jednadžba ima točno tri nepoznanice, jednu iz svakog smjera, i svaka ćelija leži na točno jednoj liniji svakog smjera. Ako su dvije od triju nepoznanica ćelije poznate, treća je forsirana. Pitanje je samo od koliko „slobodnih” nepoznanica krenuti.</p>'''),
        ('Koje nepoznanice fiksirati da sve ostale budu forsirane?',
         r'''<p>Zadnji redak $i = N - 1$ sadrži ćelije $(N-1, j)$ za sve $j$: ako znamo $r_{N-1}$, dobivamo $c_j \oplus d_{N-1-j} = a_j := s_{N-1,j} \oplus r_{N-1}$ za svaki $j$. Predzadnji redak daje $c_j \oplus d_{N-2-j} = b_j$ za $j \le N - 2$. XOR tih dviju jednakosti eliminira $c_j$: $d_{N-1-j} \oplus d_{N-2-j} = a_j \oplus b_j$ — susjedne dijagonale su vezane, pa je iz jedne poznate ($d_{N-1}$, koja slijedi iz ćelije $(N-1, 0)$ kad znamo još $c_0$) poznat cijeli $d$. Zatim $c_j = a_j \oplus d_{N-1-j}$ i $r_i = s_{i0} \oplus c_0 \oplus d_i$ iz prvog stupca. Dakle tri bita $r_{N-1}, r_{N-2}, c_0$ određuju sve.</p>'''),
        ('Kako iz forsiranja zaključiti odgovor i zašto su 8 pokušaja dovoljna?',
         r'''<p>Ako rješenje postoji, ono ima neke vrijednosti tih triju bitova; za tu kombinaciju propagacija <em>mora</em> reproducirati upravo to rješenje (svaki korak je bio forsiran), pa završna provjera svih ćelija prolazi. Obratno, ako provjera prođe, imamo rješenje. Dakle: za svaku od $8$ kombinacija propagiraj u $O(N)$ i provjeri svih $N(N+1)/2$ ćelija u $O(N^2)$; odgovor je <code>Yes</code> ako bilo koja prođe. Ukupno $O(8 N^2) \approx 1.6 \cdot 10^7$ operacija.</p>'''),
    ],
    'tips': [
        r'''Operacije „invertiraj skup” koje komutiraju i same su sebi inverz uvijek su <strong>linearni sustav nad $\mathbb{Z}_2$</strong>; prije Gaussa pogledaj strukturu — kad svaka jednadžba veže malo nepoznanica, često se sve forsira iz nekoliko slobodnih bitova (propagacija umjesto eliminacije).''',
        r'''Traži „rubne” jednadžbe s <em>dvije</em> nepoznanice iz iste skupine (ovdje dva najdulja retka): njihov XOR eliminira zajedničku nepoznanicu i daje rekurziju po indeksu.''',
        r'''Nakon propagacije <strong>uvijek provjeri sve jednadžbe</strong> — propagacija koristi samo podskup jednadžbi, a ostale mogu biti proturječne (to je upravo slučaj <code>No</code>).''',
    ],
    'solution': r'''
<ul>
<li>Operacije komutiraju: redoslijed nije bitan.</li>
<li>Dvije iste operacije se poništavaju.</li>
<li>Fiksiranje dvaju najduljih redaka u jednom smjeru i najduljeg retka u drugom smjeru jednoznačno određuje sve ostale.</li>
</ul>
<p>Vremenska složenost: $O(N^2)$.</p>
''',
    'detailed': r'''
<h3>1. Model: linearni sustav nad $\mathbb{Z}_2$</h3>
<p>Označimo ćelije trokuta s $(i, j)$, $0 \le j \le i < N$ ($i$-ti redak, $j$-ta žarulja). Tri smjera linija su:</p>
<ul>
<li><strong>redak</strong> $i$: ćelije $(i, j)$ za $0 \le j \le i$ — ukupno $N$ redaka, indikator $r_i$;</li>
<li><strong>„stupac”</strong> $j$: ćelije $(i, j)$ za $j \le i < N$ (linija paralelna lijevoj stranici) — indikator $c_j$;</li>
<li><strong>dijagonala</strong> $k = i - j$: ćelije $(i, i - k)$ za $k \le i < N$ (paralelna desnoj stranici) — indikator $d_k$.</li>
</ul>
<p>Svaka ćelija leži na točno jednoj liniji svakog smjera, a linije istog smjera su disjunktne. Potez invertira sve žarulje jedne linije. Inverzija je zbrajanje $1$ u $\mathbb{Z}_2$, pa potezi komutiraju i dva ista se ponište; rezultat ovisi samo o skupu linija invertiranih neparan broj puta. Sve žarulje ugašene znači
$$ r_i \oplus c_j \oplus d_{i-j} = s_{ij} \quad \text{za sve } 0 \le j \le i < N, $$
gdje je $s_{ij}$ početno stanje. To je sustav od $N(N+1)/2$ linearnih jednadžbi nad $\mathbb{Z}_2$ s $3N$ nepoznanica. Pitanje zadatka: je li sustav rješiv?</p>
<h3>2. Zašto ne izravna eliminacija</h3>
<p>Gaussova eliminacija s bitsetima košta oko $\text{(broj jednadžbi)} \cdot \text{(rang)} \cdot 3N/64 \approx 2 \cdot 10^6 \cdot 6000 \cdot 94$ — daleko previše, a i samo zapisivanje matrice $2 \cdot 10^6 \times 6000$ bita je $1.5$ GB. Trebamo iskoristiti strukturu: svaka jednadžba ima točno tri nepoznanice, po jednu iz svakog smjera.</p>
<h3>3. Forsiranje iz tri bita</h3>
<p>Ključno opažanje: <em>ako su dvije od triju nepoznanica neke ćelije poznate, treća je forsirana.</em> Trebamo početni skup poznatih nepoznanica iz kojeg lančano forsiramo sve. Fiksirajmo $r_{N-1}$, $r_{N-2}$ i $c_0$ (osam kombinacija).</p>
<ol>
<li>Zadnji redak sadrži ćelije $(N-1, j)$ za <em>sve</em> $j$, pa za svaki $j$ vrijedi $c_j \oplus d_{N-1-j} = a_j$, gdje je $a_j = s_{N-1,j} \oplus r_{N-1}$ poznato.</li>
<li>Predzadnji redak daje $c_j \oplus d_{N-2-j} = b_j$, $b_j = s_{N-2,j} \oplus r_{N-2}$, za $0 \le j \le N-2$.</li>
<li>XOR (1) i (2): $d_{N-1-j} \oplus d_{N-2-j} = a_j \oplus b_j$. Uz $k = N - 1 - j$: $d_{k-1} = d_k \oplus a_{N-1-k} \oplus b_{N-1-k}$ za $k = N-1, \dots, 1$. Poznamo li $d_{N-1}$, poznajemo sve dijagonale.</li>
<li>$d_{N-1}$ dolazi iz ćelije $(N-1, 0)$: $d_{N-1} = s_{N-1,0} \oplus r_{N-1} \oplus c_0$ — zato nam treba i $c_0$.</li>
<li>Sad su svi $d$ poznati, pa iz (1) slijedi $c_j = a_j \oplus d_{N-1-j}$ za svaki $j$.</li>
<li>Napokon, ćelija $(i, 0)$ daje $r_i = s_{i0} \oplus c_0 \oplus d_i$ za svaki $i$.</li>
</ol>
<p>Svaki korak koristi samo jednu jednadžbu sustava, pa je propagacija $O(N)$ po kombinaciji.</p>
<h3>4. Ispravnost</h3>
<p><em>Potpunost.</em> Neka sustav ima rješenje $(r, c, d)$. Ono ima neke vrijednosti $r_{N-1}, r_{N-2}, c_0$; u toj kombinaciji svaki korak propagacije izvodi vrijednost koju rješenje <em>mora</em> imati (jer koristi jednadžbu koju rješenje zadovoljava), pa propagacija reproducira točno to rješenje i završna provjera prolazi. <em>Ispravnost.</em> Ako provjera svih $N(N+1)/2$ jednadžbi prođe, dobiveni vektor jest rješenje. Dakle odgovor je <code>Yes</code> točno kad barem jedna od osam kombinacija prođe provjeru.</p>
<p><em>Napomena o jezgri.</em> Propagacija pokazuje da je preslikavanje $(r, c, d) \mapsto$ stanje ćelija injektivno na skupu vektora s fiksiranim $(r_{N-1}, r_{N-2}, c_0)$, pa jezgra ima dimenziju najviše $3$. Ona ima i najmanje tri nezavisna elementa: „svi retci $+$ svi stupci”, „svi retci $+$ sve dijagonale” i „retci $i$ s $N-1-i$ parnim, dijagonale $k$ s $N-1-k$ parnim, stupci $j$ s $j$ neparnim” (za ćeliju $(i, j)$ tri indikatora su $[N-1-i \text{ paran}]$, $[j \text{ neparan}]$, $[N-1-i+j \text{ paran}]$, čiji je XOR uvijek $0$). Dakle za $N \ge 2$ jezgra ima točno dimenziju $3$, skup rješenja je (ako je neprazan) afin prostor dimenzije $3$ i <em>svaka</em> od osam kombinacija daje rješenje — dovoljno bi bilo probati jednu. Osam pokušaja je jeftin dodatak koji ne zahtijeva tu analizu.</p>
<h3>5. Primjer</h3>
<p>Za $N = 6$ upaljene su žarulje $(3,1), (3,2), (4,2)$. Propagacija s $r_5 = r_4 = c_0 = 0$: zadnji redak je ugašen, pa je $a_j = 0$ za sve $j$; u predzadnjem je upaljena samo $(4,2)$, pa je $b_2 = 1$ i ostali $b_j = 0$. Iz ćelije $(5,0)$: $d_5 = 0$. Rekurzija $d_{k-1} = d_k \oplus a_{5-k} \oplus b_{5-k}$ daje $d_4 = 0$, $d_3 = 0$, $d_2 = d_3 \oplus b_2 = 1$, $d_1 = 1$, $d_0 = 1$. Zatim $c_j = a_j \oplus d_{5-j}$: $c = (0,0,0,1,1,1)$, i $r_i = s_{i0} \oplus c_0 \oplus d_i = d_i$: $r = (1,1,1,0,0,0)$. Dakle invertiramo retke $0,1,2$, stupce $3,4,5$ i dijagonale $0,1,2$. Provjera: $(3,1)$ dobiva $r_3 \oplus c_1 \oplus d_2 = 0 \oplus 0 \oplus 1 = 1$, $(3,2)$ dobiva $0 \oplus 0 \oplus d_1 = 1$, $(4,2)$ dobiva $0 \oplus 0 \oplus d_2 = 1$, a npr. $(0,0)$ dobiva $r_0 \oplus c_0 \oplus d_0 = 1 \oplus 0 \oplus 1 = 0$ i $(4,1)$ dobiva $0 \oplus 0 \oplus d_3 = 0$ — sve se slaže s ulazom, odgovor <code>Yes</code>. (Prema napomeni iz odjeljka 4 i ostalih sedam kombinacija daje rješenja, npr. „retci, stupci i dijagonale $1$ i $4$”.) Suprotno, ako su upaljene samo $(0,0)$ i $(1,0)$, nijedna kombinacija ne prolazi provjeru: <code>No</code>.</p>
<h3>6. Složenost i implementacija</h3>
<ul>
<li>Vrijeme $O(8 \cdot N^2) \approx 1.6 \cdot 10^7$ jednostavnih operacija; memorija $O(N^2)$ za ulaz (nizovi znakova), $4$ MB.</li>
<li>Ulaz čitamo redak po redak kao nizove; ćelija $(i, j)$ je $j$-ti znak $i$-tog niza. Pazi na indeks dijagonale $i - j \ge 0$.</li>
<li>Za $N = 2$ su „zadnja dva retka” ujedno i svi retci — propagacija i dalje radi (retci $1$ i $0$, jedna dijagonalna rekurzija).</li>
<li>Bitovi se mogu držati u <code>int</code>/<code>char</code>; nema aritmetike osim XOR-a, pa nema prelijevanja ni modula.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova ($N \le 5$, pola generirano kao XOR slučajnih linija, dakle rješivo, pola s pokvarenim ćelijama) protiv brute forcea koji iscrpno probava svih $2^{3N}$ podskupova linija; 3 velika testa s $N = 2000$ (najviše 0.01 s).''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'LaLa and Magic Stone', 'title_hr': 'LaLa i magični kamen', 'slug': 'D_lala_and_magic_stone',
    'tl': '1 s', 'ml': '1024 MB',
    'statement': r'''
<p>Ploča ima $N \times M$ ćelija; neke su nekompatibilne. Traženi komad je U-oblik od $7$ ćelija ($3 \times 3$ kvadrat bez gornje srednje i središnje ćelije; rotacije dopuštene kako je prikazano u izvorniku). Prebroji, modulo $998244353$, načine da se sve kompatibilne ćelije razrežu na takve komade (bez ostatka i bez lijepljenja).</p>
<h3>Ulaz</h3>
<p>$N, M$ ($3 \le N, M \le 1000$) i $N$ binarnih nizova duljine $M$ (<code>1</code> = nekompatibilna ćelija).</p>
<h3>Izlaz</h3>
<p>Broj načina modulo $998244353$.</p>
<h3>Primjer</h3>
<p>Za $4 \times 4$ ploču s nekompatibilnim ćelijama $(0,3)$ i $(3,0)$ odgovor je $2$.</p>
''',
    'hints': [
        r'''<p>Dva U-komada koji se „isprepliću” (jedan okrenut prema dolje umetnut u drugi) čine jedinstveno spojivi blok. Ključno: ako particija postoji, gotovo je uvijek jednoznačna — odgovor je malen broj i računa se konstruktivno, ne DP-om.</p>''',
        r'''<p>Uzmi leksikografski najmanju nepokrivenu ćeliju $(i, j)$. Ako se može pokriti na točno jedan način, pokrij je i ponovi. Inače je oko nje forsiran $3 \times 3$ blok i analiza malog broja slučajeva odlučuje koja je konfiguracija ispravna (ili da postoje dvije valjane).</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Spajanje dvaju isprepletenih komada daje jedinstvenu strategiju particioniranja ako ona postoji („spojeni komad”). Dokaz te tvrdnje izravno daje algoritam.</p>'''),
        ('Redukcija: pohlepno od leksikografski najmanje ćelije', r'''<p>Neka je $(i, j)$ leksikografski najmanja slobodna ćelija. Ona je gornji-lijevi kut svog komada (sve iznad i lijevo je pokriveno). Ako je pokrivanje jedinstveno, pokrij i nastavi. Inače mora biti slobodno $8$ određenih ćelija oko nje.</p>'''),
        ('Algoritam: analiza slučajeva', r'''<p><b>Slučaj 1</b>, $(i+1, j+1)$ slobodna: komad koji pokriva $(i, j)$ mora biti spojeni komad, u jednoj od dvije konfiguracije A/B. Ako se u $3 \times 3$ kvadrat s gornjim-lijevim kutom $(i+1, j-3)$ ne može smjestiti komad, forsirana je B; inače je pokrivanje $(i, j+3)$ uz B jedinstveno, a A na njemu ne radi — biraj A ili B prema dostupnosti te particije. <b>Slučaj 2</b>, $(i+1, j+1)$ zauzeta: četiri načina L, BL, R, BR pokrivanja $3 \times 3$ kvadrata s kutom $(i, j)$. Ako je točno jedan valjan, uzmi ga. L i BL (odn. R i BR) ne mogu biti oba valjana; kombinacije L&amp;R, L&amp;BR, R&amp;BL vode na nepokrivljive ćelije ($(i+1, j+3)$ i $(i+2, j+4)$, odn. $(i+1, j-1)$ i $(i+2, j-2)$), pa su nemoguće. Ostaje BL&amp;BR: ako je $(i+1, j-1)$ slobodna, forsiran je BR; inače odluči kao u slučaju A/B. Odgovor je $0$, $1$ ili (u slučaju sample 1) $2$ zbog jedinstvenosti nakon prvog izbora.</p>'''),
        ('Složenost', r'''<p>Svaka ćelija obrađuje se $O(1)$ puta: $O(NM)$.</p>'''),
    ],
    'solution': r'''
<p>Ključno opažanje: spajanje dvaju isprepletenih komada daje jedinstvenu strategiju particioniranja, ako postoji. Takav par zovemo <em>spojeni komad</em>. Dokaz te tvrdnje prirodno daje algoritam za rješavanje zadatka.</p>
<p>Pretpostavimo da postoji valjana particija i slobodna ćelija; neka je $(i, j)$ leksikografski najmanja slobodna ćelija. Ako postoji točno jedan način da se $(i, j)$ pokrije, pokrijemo je i vratimo se na početak. Inače sljedećih $8$ ćelija (prikazanih u izvorniku) mora biti slobodno.</p>
<p><b>Slučaj 1:</b> $(i+1, j+1)$ je slobodna. Komad koji pokriva $(i, j)$ mora biti spojeni komad; postoje dva načina na koje ga može pokrivati — konfiguracije A (lijeva) i B (desna). Ako je jedna od njih nevaljana, slučaj je trivijalan; pretpostavimo da su obje valjane. Ako se u $3 \times 3$ kvadrat s gornjim-lijevim kutom $(i+1, j-3)$ ne može smjestiti komad, prisiljeni smo odabrati B i vraćamo se na početak. Inače je jedini način pokrivanja $(i, j+3)$ uz konfiguraciju B onaj prikazan u izvorniku, a lako se provjeri da A na njemu ne radi. Stoga biramo A ili B ovisno o dostupnosti te particije.</p>
<p><b>Slučaj 2:</b> $(i+1, j+1)$ nije slobodna. Postoje $4$ načina da se pokriju sve ćelije $3 \times 3$ kvadrata s gornjim-lijevim kutom $(i, j)$: konfiguracije L, BL, R i BR. Ako je točno jedna valjana, koristimo je i vraćamo se na početak. Pretpostavimo da su barem dvije valjane. L i BL ne mogu biti obje valjane, kao ni R i BR, pa ostaju $4$ slučaja.</p>
<ul>
<li>L i R valjane: ako odaberemo L, nemoguće je istodobno pokriti $(i+1, j+3)$ i $(i+2, j+4)$; slično za R. Slučaj je nemoguć.</li>
<li>L i BR valjane: ako odaberemo L, opet je nemoguće pokriti $(i+1, j+3)$ i $(i+2, j+4)$; ako odaberemo R, ne mogu se pokriti $(i+1, j-1)$ i $(i+2, j-2)$. Slučaj je nemoguć.</li>
<li>R i BL valjane: nemoguće sličnim argumentom.</li>
<li>BL i BR valjane: ako je $(i+1, j-1)$ slobodna, mora se odabrati BR. Inače, argumentom sličnim onome za A i B, biramo BL ili BR ovisno o dostupnosti odgovarajuće particije.</li>
</ul>
''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'LaLa and Monster Hunting (Part 1)', 'title_hr': 'LaLa i lov na čudovište (1. dio)', 'slug': 'E_lala_and_monster_hunting_part_1',
    'tl': '5 s', 'ml': '1024 MB',
    'statement': r'''
<p>Dano je $N$ kružnica sa središtima $(x_i, y_i)$ i polumjerima $r_i$. Odredi sadrži li konveksna ljuska kružnica ishodište $(0, 0)$.</p>
<h3>Ulaz</h3>
<p>$N$ ($1 \le N \le 10^6$), zatim $x_i, y_i, r_i$ ($|x_i|, |y_i| \le 10^6$, $0 \le r_i \le 10^6$). Udaljenost ishodišta od ruba konveksne ljuske je barem $1$.</p>
<h3>Izlaz</h3>
<p><code>Yes</code> ili <code>No</code>.</p>
<h3>Primjer</h3>
<p>Kružnice $(-3,0,1), (0,0,3), (3,0,1)$: <code>Yes</code>. Jedna kružnica $(3,3,1)$: <code>No</code>.</p>
''',
    'hints': [
        r'''<p>Ako neka kružnica sadrži ishodište (uključivo rub), odgovor je odmah <code>Yes</code>. Inače iz ishodišta prema svakoj kružnici idu dvije tangente.</p>''',
        r'''<p>Ishodište je izvan konveksne ljuske ako i samo ako postoji poluravnina (kroz ishodište) koja sadrži sve kružnice, tj. sve $2N$ tangencijalnih zraka. Sortiraj kutove zraka i provjeri postoji li praznina $\ge \pi$.</p>''',
    ],
    'coach': [
        ('Zašto ne bismo gradili konveksnu ljusku kružnica?',
         r'''<p>Ljuska diskova postoji (Rappaportov algoritam u $O(N \log N)$), ali je puna posebnih slučajeva (lukovi, zajedničke tangente, ugniježđeni diskovi) — za $N = 10^6$ to je puno koda i puno mjesta za grešku. Pitanje zadatka je samo <em>je li jedna točka u ljusci</em>, a za to postoji jednostavnija karakterizacija: točka je izvan zatvorenog konveksnog skupa ako i samo ako je od njega odvaja pravac. Dakle: ishodište je izvan ljuske $\iff$ postoji poluravnina čiji rub prolazi kroz ishodište i koja sadrži sve diskove.</p>'''),
        ('Kako „disk je u poluravnini kroz ishodište” prevesti u kutove?',
         r'''<p>Ako neki disk sadrži ishodište ($x^2 + y^2 \le r^2$), nijedna poluravnina kroz ishodište ga ne sadrži cijelog (osim ako je $r = 0$ i disk je točka u ishodištu — i tada je ishodište u ljusci), pa je odgovor odmah <code>Yes</code>. Inače disk vidimo iz ishodišta pod kutnim intervalom $[\theta - \alpha, \theta + \alpha]$, gdje je $\theta = \operatorname{atan2}(y, x)$ smjer središta, a $\alpha = \arcsin(r/d) < \pi/2$ polovina vidnog kuta ($d$ je udaljenost središta). Poluravnina kroz ishodište je skup smjerova u zatvorenom polukrugu $[\varphi, \varphi + \pi]$; disk (bez ishodišta) leži u njoj točno kad je njegov kutni interval unutar tog polukruga.</p>'''),
        ('Zašto je dovoljno gledati samo krajeve intervala, tj. $2N$ tangencijalnih zraka?',
         r'''<p>Interval duljine $2\alpha < \pi$ čija su oba kraja u zatvorenom polukrugu ili je cijeli u njemu, ili je cijeli u njemu njegov komplement — a komplement ima duljinu $> \pi$ i ne stane. Dakle „svi intervali u polukrugu” $\iff$ „svih $2N$ krajeva u polukrugu”. Konačan skup točaka na kružnici stane u zatvoreni polukrug točno kad je najveća praznina između kutno susjednih točaka (uključujući onu preko $2\pi$) barem $\pi$: polukrug koji sve sadrži počinje na prvoj točki iza praznine.</p>'''),
        ('Je li računanje u <code>double</code> sigurno i kako proći $N = 10^6$?',
         r'''<p>Tekst jamči da je ishodište barem $1$ udaljeno od ruba ljuske, pa granični slučaj (praznina točno $\pi$, ishodište na tangenti) ne postoji; udaljenosti su $\le 1.5 \cdot 10^6$, pa se praznina od $\pi$ razlikuje za barem reda $10^{-7}$, a greška <code>double</code> aritmetike u <code>atan2</code>/<code>asin</code> je reda $10^{-15}$. Ulaz od $3 \cdot 10^6$ brojeva čitamo brzim čitačem (<code>fread</code>), sortiramo $2 \cdot 10^6$ realnih brojeva ($O(N \log N)$, oko $0.2$ s) i prođemo ih jednom.</p>'''),
    ],
    'tips': [
        r'''Za pitanje „je li točka u konveksnoj ljusci skupa” ne treba graditi ljusku: koristi <strong>teorem o separaciji</strong> — točka je izvan ako i samo ako postoji pravac kroz nju s cijelim skupom na jednoj strani. To svodi 2D problem na 1D problem na kružnici smjerova.''',
        r'''„Skup točaka na kružnici stane u polukrug (luk duljine $L$)” $\iff$ „najveća praznina između sortiranih kutova je $\ge 2\pi - L$” — standardni trik, ne zaboravi prazninu koja prelazi preko $2\pi$.''',
        r'''Kad tekst obeća „udaljenost od granice barem $\varepsilon$”, to je signal da je <code>double</code> dovoljan i da graničnih slučajeva nema; ipak provjeri uvjet $d > r$ prije <code>asin(r/d)</code>.''',
        r'''Za ulaze reda $10^6$ brojeva koristi vlastiti čitač (<code>fread</code> u međuspremnik) — <code>cin</code> bez <code>sync_with_stdio(false)</code> ili <code>scanf</code> mogu potrošiti više vremena od samog algoritma.''',
    ],
    'solution': r'''
<ul>
<li>Ako neka kružnica sadrži ishodište u unutrašnjosti ili na rubu, odgovor je „Yes”.</li>
<li>Inače svaka kružnica ima $2$ tangencijalne zrake iz ishodišta. Odgovor je „Yes” ako i samo ako nijedna poluravnina ne sadrži svih $2N$ zraka.</li>
<li>Zbog uvjeta o udaljenosti sigurno je računati u tipu <code>double</code>.</li>
</ul>
<p>Vremenska složenost: $O(N \log N)$ zbog sortiranja zraka.</p>
<p><b>Alternativno rješenje.</b> Postoji $O(N \log N)$ algoritam za konveksnu ljusku $N$ kružnica (D. Rappaport, „A convex hull algorithm for discs, and applications”). Konstruiraj ljusku i za svaku rubnu dužinu i luk, usmjerene pozitivno, provjeri da ishodište leži slijeva.</p>
''',
    'detailed': r'''
<h3>1. Separacija umjesto ljuske</h3>
<p>Konveksna ljuska $K$ unije diskova je zatvoren konveksan skup. Za zatvoren konveksan skup i točku $p$ vrijedi teorem o separaciji: $p \notin K$ ako i samo ako postoji pravac kroz $p$ takav da je $K$ cijeli (strogo) na jednoj strani. Za $K$ generiran diskovima dovoljno je da su svi <em>diskovi</em> na jednoj strani, jer je poluravnina konveksna i sadrži tada i njihovu ljusku. Dakle:</p>
<p style="text-align:center">ishodište je izvan ljuske $\iff$ postoji zatvorena poluravnina s rubom kroz ishodište koja sadrži sve diskove.</p>
<p>(Uz uvjet iz zadatka da je ishodište barem $1$ udaljeno od ruba ljuske, razlika između otvorene i zatvorene poluravnine ne igra ulogu.)</p>
<h3>2. Disk u poluravnini kroz ishodište</h3>
<p>Neka disk ima središte na udaljenosti $d = \sqrt{x^2 + y^2}$ i polumjer $r$.</p>
<ul>
<li>Ako je $d \le r$, disk sadrži ishodište; tada je ishodište u ljusci i odgovor je <code>Yes</code>. (Za $d = r$ ishodište je na rubu diska, dakle u $K$; uvjet o udaljenosti $\ge 1$ takav ulaz zapravo isključuje, ali provjera $x^2 + y^2 \le r^2$ u cijelim brojevima ništa ne košta.)</li>
<li>Inače je $r/d < 1$ i iz ishodišta vidimo disk pod kutnim intervalom $I = [\theta - \alpha, \theta + \alpha]$, gdje je $\theta = \operatorname{atan2}(y, x)$ i $\alpha = \arcsin(r/d) \in [0, \pi/2)$; krajevi intervala su smjerovi dviju tangenata iz ishodišta. Disk je unija dužina od ishodišta u smjerovima iz $I$ (odsječenih diskom), pa disk leži u zatvorenoj poluravnini $H_\varphi = \{$smjerovi u $[\varphi, \varphi + \pi]\}$ točno kad je $I \subseteq [\varphi, \varphi + \pi]$.</li>
</ul>
<h3>3. Od intervala do točaka</h3>
<p>Tvrdnja: <em>svi intervali $I_i$ leže u nekom zatvorenom polukrugu $\iff$ svih $2N$ krajeva $\theta_i \pm \alpha_i$ leži u nekom zatvorenom polukrugu.</em> Smjer $\Rightarrow$ je trivijalan. Za $\Leftarrow$: neka su oba kraja intervala $I$ u polukrugu $P$. Kružnica minus dva kraja raspada se na dva luka: $I$ (duljine $2\alpha < \pi$) i njegov komplement (duljine $> \pi$). Polukrug $P$ je povezan luk koji sadrži oba kraja, pa sadrži jedan od tih dvaju lukova; komplement je predug, dakle $P \supseteq I$.</p>
<p>Konačan skup točaka na kružnici leži u nekom zatvorenom polukrugu točno kad je <strong>najveća praznina</strong> između kutno susjednih točaka (nakon sortiranja, uključujući prazninu $2\pi - (\text{max} - \text{min})$ koja prelazi preko $2\pi$) barem $\pi$: ako je praznina $\ge \pi$, polukrug koji počinje na točki iza praznine sadrži sve; obratno, ako sve točke leže u $[\varphi, \varphi + \pi]$, luk $(\varphi + \pi, \varphi + 2\pi)$ nema točaka, pa je neka praznina $\ge \pi$.</p>
<h3>4. Algoritam</h3>
<ol>
<li>Pročitaj ulaz brzim čitačem. Za svaki disk provjeri $x^2 + y^2 \le r^2$ u 64-bitnim cijelim brojevima; ako vrijedi, ispiši <code>Yes</code>.</li>
<li>Inače izračunaj $\theta$ i $\alpha$ te dodaj kutove $\theta - \alpha$ i $\theta + \alpha$ (normalizirane u $[0, 2\pi)$) u niz.</li>
<li>Sortiraj $2N$ kutova, izračunaj najveću razliku susjeda i prazninu preko $2\pi$.</li>
<li>Ako je najveća praznina $\ge \pi$, ishodište je izvan ljuske: <code>No</code>; inače <code>Yes</code>.</li>
</ol>
<p>Složenost $O(N \log N)$ zbog sortiranja $2 \cdot 10^6$ brojeva; program radi oko $0.2$ s za $N = 10^6$.</p>
<h3>5. Primjeri</h3>
<ul>
<li>Diskovi $(-3,0,1), (0,0,3), (3,0,1)$: drugi disk sadrži ishodište, odmah <code>Yes</code>.</li>
<li>Jedan disk $(3,3,1)$: $d = 3\sqrt2 \approx 4.24$, $\alpha = \arcsin(1/4.24) \approx 0.238$, $\theta = \pi/4$; dva kuta $\approx 0.547$ i $1.024$, praznina preko $2\pi$ je $\approx 5.81 \ge \pi$: <code>No</code>. Općenito, jedan disk koji ne sadrži ishodište uvijek daje <code>No</code>.</li>
<li>Dva diska $(-3,0,1)$ i $(3,0,1)$: kutovi $\approx \pi \pm 0.34$ i $\pm 0.34$; praznine su $\approx 2.46$, $0.68$, $2.46$, $0.68$, sve $< \pi$: <code>Yes</code> — ishodište je na spojnici središta, unutar ljuske.</li>
</ul>
<h3>6. Preciznost i zamke</h3>
<ul>
<li><strong>Granični slučaj ne postoji.</strong> Praznina točno $\pi$ značila bi da ishodište leži na zajedničkoj tangenti dvaju diskova, tj. na rubu ljuske — što je isključeno uvjetom udaljenosti $\ge 1$. Uz $d \le 1.5 \cdot 10^6$ pomak ruba ljuske za $1$ mijenja kut tangente za barem reda $10^{-7}$, a <code>atan2</code> i <code>asin</code> u <code>double</code> griješe reda $10^{-15}$; sigurna margina.</li>
<li><code>asin(r/d)</code> zahtijeva $r < d$; to je osigurano prethodnom cjelobrojnom provjerom (kvadrati do $2 \cdot 10^{12}$ stanu u 64 bita, ne u 32).</li>
<li>Kutovi se normaliziraju u $[0, 2\pi)$; praznina koja prelazi preko $2\pi$ lako se zaboravi.</li>
<li>$r = 0$ (točke) radi bez posebnog slučaja: $\alpha = 0$, dvije jednake zrake.</li>
<li>Brzi ulaz je nužan: $3 \cdot 10^6$ brojeva s predznacima.</li>
</ul>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih testova ($N \le 6$, mali koordinatni raspon, generator odbacuje ulaze s marginom $< 1.2$ od ruba ljuske) protiv brute forcea koji ljusku aproksimira konveksnom ljuskom $720$ točaka po kružnici i egzaktno provjerava pripadnost; 3 velika testa s $N = 10^6$ (najviše 0.21 s).''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'LaLa and Monster Hunting (Part 2)', 'title_hr': 'LaLa i lov na čudovište (2. dio)', 'slug': 'F_lala_and_monster_hunting_part_2',
    'tl': '6 s', 'ml': '1024 MB',
    'statement': r'''
<p>Čudovište je graf $G$ sa $6$ vrhova prikazan u izvorniku: trokut s pridruženim „repom” — putem duljine $3$ (ukupno $6$ bridova). Mreža grana je jednostavan graf $H$. Prebroji, modulo $998244353$, podgrafe grafa $H$ izomorfne grafu $G$ (podgraf: izbriši neke bridove, zatim izolirane vrhove).</p>
<h3>Ulaz</h3>
<p>$N, M$ ($2 \le N \le 10^5$, $0 \le M \le 10^5$) i $M$ bridova $u_i < v_i$, bez ponavljanja. Graf nije nužno povezan.</p>
<h3>Izlaz</h3>
<p>Broj kandidata modulo $998244353$.</p>
<h3>Primjer</h3>
<p>Dva trokuta $\{0,1,2\}$, $\{3,4,5\}$ spojena bridom $(2,3)$: odgovor $4$. Za $K_6$ odgovor je $360$.</p>
''',
    'hints': [
        r'''<p>Brojanje trokuta kroz svaki vrh i kroz svaki brid u $O(M\sqrt{M})$ je standard (orijentacija po stupnju). Rep duljine $3$ broji se dinamičkim programiranjem po duljini repa, ali treba paziti da se vrhovi repa ne vraćaju u trokut ili u sam rep.</p>''',
        r'''<p>Uključivanje–isključivanje za „loše” repove svodi se na brojanje malih podgrafa: kvadrat s dijagonalom (4 vrha, 5 bridova) i „kuća” od 5 vrhova i 6 bridova. Oba se broje po usmjerenim bridovima u $O(M\sqrt{M})$.</p>''',
    ],
    'coach': [
        ('Što točno brojimo — kako izbjeći višestruko brojanje istog podgrafa?',
         r'''<p>$G$ je trokut $\{a, b, c\}$ s repom $c - d - e - f$. Podgraf od $H$ izomorfan $G$ jednoznačno određuje: svoj trokut (neuređen), vrh $c$ trokuta na koji je rep spojen i uređeni put $c, d, e, f$ (rep se čita od trokuta). Jedina simetrija $G$ je zamjena $a \leftrightarrow b$, koja ništa od toga ne mijenja. Dakle broj kandidata je $\sum_{\text{trokut}} \sum_{c \in \text{trokut}} (\text{broj jednostavnih puteva } c\,d\,e\,f \text{ s } d, e, f \notin \{a, b\})$ — svaki podgraf se broji točno jednom.</p>'''),
        ('Kako prebrojati jednostavne puteve duljine $3$ iz vrha, a ne šetnje?',
         r'''<p>Šetnje $c, d, e, f$ s $d \sim c$, $e \sim d$, $f \sim e$ lako se broje po stupnjevima, ali treba isključiti povratke: $e \ne c$ i $f \notin \{c, d\}$. Brojimo izravno: za $d \sim c$ i $e \sim d$, $e \ne c$, vrh $f$ je bilo koji susjed od $e$ osim $d$ i osim $c$ ako je $c \sim e$. Zbrajanjem po $e$ dobivamo $P(c) = \sum_{d \sim c} \bigl( Q(d) - (\deg c - 1) - \mathrm{tri}(cd) \bigr)$, gdje je $Q(d) = \sum_{e \sim d} (\deg e - 1)$, a $\mathrm{tri}(cd)$ broj zajedničkih susjeda od $c$ i $d$ (trokuta na bridu $cd$). Sve su to lokalne veličine — računaju se u $O(M)$ odnosno $O(M\sqrt{M})$ za trokute po bridu.</p>'''),
        ('Kako isključiti puteve koji prolaze kroz $a$ ili $b$ — uključivanje–isključivanje?',
         r'''<p>Traženi broj je $P(c) - |\text{kroz } a| - |\text{kroz } b| + |\text{kroz oba}|$. Put prolazi kroz $a$ na točno jednom od mjesta $d, e, f$: (i) $d = a$: put $a, e, f$ iz $a$ koji izbjegava $c$ — ista formula kao $P$, ali za susjeda $a$ od $c$: $Q(a) - (\deg c - 1) - \mathrm{tri}(ca)$; (ii) $e = a$: $d$ je zajednički susjed $c$ i $a$, $f$ susjed od $a$ različit od $c, d$: $\mathrm{tri}(ca)\,(\deg a - 2)$; (iii) $f = a$: put $c, d, e, a$ zatvara 4-ciklus koji sadrži brid $ca$: $\mathrm{c4}(ca)$, broj 4-ciklusa na bridu. Za oba vrha slično: $(d,e) = (a,b)$ daje $\deg b - 2$, $(d,f) = (a,b)$ daje $\mathrm{tri}(ab) - 1$, $(e,f) = (a,b)$ daje $\mathrm{tri}(ca) - 1$, i simetrično sa zamijenjenim ulogama.</p>'''),
        ('Kako u $O(M\sqrt{M})$ dobiti trokute i 4-cikluse po bridu?',
         r'''<p>Orijentiraj svaki brid od vrha manjeg ranga (stupanj, pa indeks) prema većem; tada je izlazni stupanj svakog vrha $O(\sqrt{M})$. Trokuti: za svaki $u$ označi izlazne susjede, za $v$ izlazni susjed od $u$ i $w$ izlazni od $v$ provjeri oznaku — svaki trokut nađen točno jednom (u poretku ranga), $O(M\sqrt{M})$. 4-ciklusi na bridu: za svaki $u$ kao vrh najvećeg ranga u ciklusu prebroji puteve $u - v - w$ sa $v, w$ manjeg ranga, grupirano po $w$ u <code>cnt[w]</code>; svaki par takvih puteva do istog $w$ je 4-ciklus $u\,v\,w\,v'$, pa brid $uv$ (i $vw$) leži u $\mathrm{cnt}[w] - 1$ ciklusa s vrhom $u$; svaki 4-ciklus obrađen je točno jednom (kod svog vrha najvećeg ranga). Zbroj po svim $(u,v,w)$ je $O(M\sqrt{M})$.</p>'''),
        ('Kako složiti konačni odgovor i što s prelijevanjem?',
         r'''<p>Za svaki trokut $\{a,b,c\}$ i svaki od tri izbora vrha $c$ izračunaj $P(c)$ minus kroz-$a$ minus kroz-$b$ plus kroz-oba i dodaj modulo $998244353$. Pojedinačne veličine su najviše reda $M \cdot \max\deg \le 10^{10}$, pa ih držimo u <code>long long</code> i modul primjenjujemo tek na zbroj; trokuta je najviše $O(M\sqrt{M}) \approx 1.5 \cdot 10^7$ (gotovo potpun graf na $450$ vrhova), pa je i to $O(M\sqrt{M})$.</p>'''),
    ],
    'tips': [
        r'''Kod brojanja malih podgrafa prvo odredi <strong>što jednoznačno određuje kopiju</strong> (koji su vrhovi razlikovani, koji su automorfizmi) — tako se brojanje svodi na zbroj lokalnih veličina bez korekcije faktorom, ili s jasnim faktorom.''',
        r'''Orijentacija bridova <strong>po stupnju</strong> (od manjeg prema većem) daje izlazni stupanj $O(\sqrt{M})$ i standardno $O(M\sqrt{M})$ brojanje trokuta i 4-ciklusa; 4-cikluse broji „od vrha najvećeg ranga” grupiranjem puteva duljine $2$ po krajnjem vrhu.''',
        r'''„Jednostavni putevi” = „šetnje minus povratci”: za kratke puteve povratci su malobrojni i svi se izražavaju stupnjevima, trokutima po bridu i 4-ciklusima po bridu — <strong>uključivanje–isključivanje</strong> po mjestu na kojem se zabranjeni vrh pojavljuje.''',
        r'''Na malim testovima uvijek imaj brute force koji doslovno nabraja injekcije vrhova i dijeli brojem automorfizama — to je najbrži način da uhvatiš pogrešan faktor $2$ ili zaboravljeni slučaj.''',
    ],
    'solution': r'''
<p>Modelno rješenje uzastopno računa sljedeće vrijednosti:</p>
<ol>
<li>Za svaki vrh $u$, broj $3$-ciklusa koji prolaze kroz $u$.</li>
<li>Za svaki neusmjereni brid $e$, broj $3$-ciklusa koji prolaze kroz $e$.</li>
<li>Za svaki usmjereni brid $e = (u, v)$, broj podgrafa s $4$ vrha $0, 1, 2, 3$ i $5$ bridova $(0,1), (1,2), (2,3), (3,0), (1,3)$ takvih da $u$ i $v$ odgovaraju vrhovima $0$ i $1$.</li>
<li>Za svaki usmjereni brid $e = (u, v)$, broj podgrafa s $5$ vrhova $0, 1, 2, 3, 4$ i $6$ bridova $(0,1), (1,2), (2,3), (3,0), (1,4), (4,2)$ takvih da $u$ i $v$ odgovaraju vrhovima $0$ i $1$.</li>
<li>Za svaki vrh $u$, broj kandidata s repom duljine $1$, $2$ i $3$ takvih da $u$ leži na kraju repa.</li>
</ol>
<p>Vremenska složenost: $O(n + m\sqrt{m})$.</p>
''',
    'detailed': r'''
<p><em>Napomena.</em> Službeno rješenje gradi rep dinamički po duljini i oduzima „kuće” i „kvadrate s dijagonalom”. Ovdje je opisan ekvivalentan, ali izravniji put: prebroji sve jednostavne puteve duljine $3$ iz vrha trokuta i uključivanjem–isključivanjem izbaci one koji dotiču druga dva vrha trokuta. Sve potrebne veličine su lokalne (stupnjevi, trokuti po bridu, 4-ciklusi po bridu).</p>
<h3>1. Što jednoznačno određuje jednog kandidata</h3>
<p>Čudovište $G$ je trokut $\{a, b, c\}$ s repom $c - d - e - f$: $6$ vrhova, $6$ bridova. Podgraf $S$ grafa $H$ izomorfan $G$ ima točno jedan trokut, točno jedan vrh trokuta stupnja $3$ u $S$ (to je $c$) i točno jedan put duljine $3$ koji iz $c$ vodi izvan trokuta; taj put čitamo od $c$: $(d, e, f)$. Automorfizmi $G$ su samo identiteta i zamjena $a \leftrightarrow b$, i oboje čuvaju $c$ i $(d,e,f)$. Zato je</p>
<p style="text-align:center">$\#\text{kandidata} = \sum_{\{a,b,c\} \text{ trokut}} \ \sum_{c \in \{a,b,c\}} \#\{\text{jednostavni putevi } c\,d\,e\,f \text{ u } H:\ d, e, f \notin \{a, b\}\}$,</p>
<p>i svaki podgraf $S$ pribrojen je točno jednom (kod svog trokuta, svog $c$ i svog repa). Provjera na $K_6$: trokuta je $\binom63 = 20$, za svaki od $3$ izbora $c$ rep je permutacija preostala $3$ vrha: $20 \cdot 3 \cdot 3! = 360$ — kao u primjeru.</p>
<h3>2. Jednostavni putevi duljine $3$ iz vrha</h3>
<p>Za vrh $c$ tražimo $P(c)$, broj nizova $(d, e, f)$ različitih vrhova, različitih od $c$, s $c \sim d \sim e \sim f$. Biramo $d \sim c$, zatim $e \sim d$, $e \ne c$; $f$ je susjed od $e$ osim $d$ i osim $c$ (ako je $c \sim e$). Dakle</p>
<p style="text-align:center">$P(c) = \sum_{d \sim c} \ \sum_{e \sim d,\ e \ne c} \bigl(\deg e - 1 - [c \sim e]\bigr) = \sum_{d \sim c} \Bigl( Q(d) - (\deg c - 1) - \mathrm{tri}(cd) \Bigr)$,</p>
<p>gdje je $Q(d) = \sum_{e \sim d} (\deg e - 1)$ (iz čega izbacujemo član $e = c$ vrijednosti $\deg c - 1$), a $\mathrm{tri}(cd) = \#\{e : e \sim c, e \sim d\}$ je broj trokuta na bridu $cd$ — točno broj $e \sim d$ sa svojstvom $c \sim e$. $Q$ se računa u $O(M)$, $P$ u $O(M)$ kad znamo $\mathrm{tri}$ po bridu.</p>
<h3>3. Izbacivanje puteva koji dotiču $a$ ili $b$</h3>
<p>Neka je $T = \{a, b, c\}$ trokut i $c$ izabran. Traženi broj je, po uključivanju–isključivanju, $P(c) - A - B + AB$, gdje je $A$ broj puteva kroz $a$, $B$ kroz $b$, $AB$ kroz oba. Vrh $a$ može u putu $(d,e,f)$ zauzeti točno jedno mjesto, pa je $A$ zbroj triju disjunktnih slučajeva:</p>
<ul>
<li>$d = a$: preostaje jednostavan put $a, e, f$ koji izbjegava $c$. Ista formula kao za $P$, samo za jednog konkretnog susjeda: $Q(a) - (\deg c - 1) - \mathrm{tri}(ca)$.</li>
<li>$e = a$: $d$ je zajednički susjed $c$ i $a$ (ima ih $\mathrm{tri}(ca)$), a $f$ je susjed od $a$ različit od $c$ i $d$: ukupno $\mathrm{tri}(ca) \cdot (\deg a - 2)$.</li>
<li>$f = a$: put $c, d, e, a$ s $d, e \notin \{c, a\}$, $d \ne e$, zajedno s bridom $ac$ čini 4-ciklus koji sadrži brid $ca$; obratno, svaki takav 4-ciklus daje točno jedan put. Broj je $\mathrm{c4}(ca)$, broj 4-ciklusa na bridu $ca$.</li>
</ul>
<p>$B$ je isto s $b$. Za $AB$ vrhovi $a$ i $b$ zauzimaju dva od tri mjesta; treće je slobodno:</p>
<ul>
<li>$(d, e) = (a, b)$: put $c, a, b, f$, $f \sim b$, $f \notin \{c, a\}$: $\deg b - 2$; simetrično $(d,e) = (b,a)$: $\deg a - 2$.</li>
<li>$(d, f) = (a, b)$: put $c, a, e, b$, $e$ zajednički susjed od $a$ i $b$ različit od $c$: $\mathrm{tri}(ab) - 1$; i simetrično još $\mathrm{tri}(ab) - 1$.</li>
<li>$(e, f) = (a, b)$: put $c, d, a, b$, $d$ zajednički susjed od $c$ i $a$ različit od $b$: $\mathrm{tri}(ca) - 1$; simetrično $(e,f) = (b,a)$: $\mathrm{tri}(cb) - 1$.</li>
</ul>
<p>Sve su to $O(1)$ izrazi po trokutu, pa je zbrajanje $O(\#\text{trokuta})$.</p>
<h3>4. Trokuti i 4-ciklusi po bridu u $O(M\sqrt{M})$</h3>
<p><strong>Rang.</strong> Poredaj vrhove po stupnju (pa po indeksu) i orijentiraj svaki brid od manjeg ranga prema većem. Izlazni stupanj svakog vrha je $O(\sqrt{M})$: ako $u$ ima $k$ izlaznih susjeda, svi imaju stupanj $\ge \deg u \ge k$, pa je $k^2 \le \sum \deg \le 2M$.</p>
<p><strong>Trokuti.</strong> Za svaki $u$ označi izlazne susjede; za svaki izlazni $v$ i svaki izlazni $w$ od $v$ s oznakom, $\{u, v, w\}$ je trokut s $\mathrm{rang}(u) < \mathrm{rang}(v) < \mathrm{rang}(w)$ — nađen točno jednom. Za svaki uvećaj $\mathrm{tri}$ triju bridova i zapamti trokut. Cijena $\sum_u \sum_{v \in \mathrm{out}(u)} |\mathrm{out}(v)| = O(M\sqrt{M})$.</p>
<p><strong>4-ciklusi na bridu.</strong> Svaki 4-ciklus obrađujemo kod svog vrha $u$ najvećeg ranga. Za fiksni $u$ prođi puteve $u - v - w$ sa $\mathrm{rang}(v), \mathrm{rang}(w) < \mathrm{rang}(u)$ i broji ih po $w$ u $\mathrm{cnt}[w]$. Dva različita takva puta $u\,v\,w$ i $u\,v'\,w$ čine 4-ciklus $u\,v\,w\,v'$ (svi 4-ciklusi s maksimumom $u$ i vrhom $w$ nasuprot $u$ nastaju tako, svaki jednom). Brid $uv$ leži u $\mathrm{cnt}[w] - 1$ takvih ciklusa (uparen sa svakim drugim putom do istog $w$), a isto i brid $vw$; bridovi $uv'$ i $v'w$ dobivaju svoje kad obradimo put $u\,v'\,w$. Nakon obrade $u$ poništi $\mathrm{cnt}$ samo za dirane $w$. Broj trojki $(u, v, w)$ ograničen je zbrojem $\min(\deg u, \deg v)$ po bridovima, što je $O(M\sqrt{M})$.</p>
<h3>5. Algoritam i složenost</h3>
<ol>
<li>Učitaj graf, izračunaj stupnjeve, rang, liste susjeda i izlazne liste.</li>
<li>$Q(v)$ za sve vrhove — $O(M)$.</li>
<li>Trokuti: $\mathrm{tri}$ po bridu i popis trokuta — $O(M\sqrt{M})$.</li>
<li>$\mathrm{c4}$ po bridu — $O(M\sqrt{M})$.</li>
<li>$P(c)$ za sve vrhove — $O(M)$.</li>
<li>Za svaki trokut i svaki od tri izbora $c$: $P(c) - A - B + AB$, zbroj modulo $998244353$.</li>
</ol>
<p>Ukupno $O(N + M\sqrt{M})$; najgori slučaj (gotovo potpun graf na $\approx 450$ vrhova s $10^5$ bridova) ima $\approx 1.5 \cdot 10^7$ trokuta i radi oko $1$ s, uz $\approx 360$ MB za popis trokuta (unutar $1024$ MB; moglo bi se i bez pamćenja, računajući odgovor odmah pri pronalasku trokuta).</p>
<h3>6. Prelijevanje, indeksi, primjer</h3>
<ul>
<li>$Q(d) \le \deg d \cdot 10^5 \le 10^{10}$, $P(c) \le 10^{15}$ — sve u <code>long long</code>, bez modula do konačnog zbrajanja; izraz $P - A - B + AB$ je nenegativan (broji nešto), pa modulo primjenjujemo tek na zbroj.</li>
<li>Ulaz je $0$-indeksiran, bridovi bez ponavljanja; $M = 0$ ili graf bez trokuta daje $0$.</li>
<li>Primjer: dva trokuta $\{0,1,2\}$, $\{3,4,5\}$ i brid $(2,3)$. Za trokut $\{0,1,2\}$ i $c = 2$: $P(2)$ broji puteve iz $2$: $2,3,4,5$ i $2,3,5,4$ te puteve kroz $0$ ili $1$ (npr. $2,0,1,\cdot$ — nema nastavka; $2,1,0,\cdot$ — nema), pa je $P(2) = 2$, $A = B = AB = 0$ i doprinos je $2$; za $c = 0$ ili $1$ nema puteva izvan trokuta. Simetrično drugi trokut daje $2$; ukupno $4$.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih grafova ($N \le 8$, sve gustoće) protiv brute forcea koji nabraja sve uređene šestorke različitih vrhova s traženim bridovima uz $a < b$ (automorfizam $a \leftrightarrow b$); 3 velika testa s $M = 10^5$ (gotovo potpun graf na $450$ vrhova s $\approx 1.5 \cdot 10^7$ trokuta, rijedak graf na $10^5$ vrhova, srednji na $2 \cdot 10^4$; najviše 1.07 s).''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'LaLa and Divination Magic', 'title_hr': 'LaLa i proročanska magija', 'slug': 'G_lala_and_divination_magic',
    'tl': '4 s', 'ml': '1024 MB',
    'statement': r'''
<p>Postoji $M$ događaja, svaki završava katastrofom ili spasom. Jedno proročanstvo je klauzula oblika „$E_i$ je katastrofa/spas ili $E_j$ je katastrofa/spas” (četiri tipa, $t \in \{1,2,3,4\}$). Rezultat prognoze skup je svih $M$-torki ishoda konzistentnih sa svim proročanstvima. Dan je skup od $N$ različitih binarnih nizova duljine $M$ (<code>1</code> = spas). Postoji li skup proročanstava čiji je rezultat točno taj skup? Ako da, ispiši jedan takav s $K \le 2M^2$ klauzula; inače $-1$.</p>
<h3>Ulaz</h3>
<p>$N, M$ ($1 \le N, M \le 2000$) i $N$ različitih binarnih nizova duljine $M$.</p>
<h3>Izlaz</h3>
<p>$-1$ ili $K$ i $K$ redaka $I\ J\ t$.</p>
<h3>Primjer</h3>
<p>Za $N = 2$, $M = 1$, nizovi <code>1</code> i <code>0</code>: $K = 0$ (bez klauzula sve je moguće).</p>
''',
    'hints': [
        r'''<p>Zadatak je: rekonstruiraj 2-SAT formulu iz skupa njezinih rješenja. Klauzula $L \lor M$ je „dopuštena” ako je ne krši nijedno zadano rješenje. Dodaj <em>sve</em> dopuštene klauzule — ako formula postoji, sigurno su sve njezine klauzule među njima, a dodatne ne isključuju nijedno zadano rješenje.</p>''',
        r'''<p>Ostaje provjeriti ima li dobivena formula $F$ <em>točno</em> $N$ rješenja. Nabroji rješenja 2-SAT-a implikacijskim grafom: grananje na neodređenoj varijabli, propagacija zatvorenja bitsetima (relacija „$\mathrm{rows}(L) \subseteq \mathrm{rows}(K)$” je već tranzitivna) — svaki list rekurzije je jedno rješenje, pa prekini kad ih prebrojiš više od $N$.</p>''',
    ],
    'coach': [
        ('Što je zadatak u jeziku logike i koje klauzule uopće smijemo upotrijebiti?',
         r'''<p>Događaj $E_j$ je Booleova varijabla ($1$ = spas), proročanstvo je klauzula s dva literala, a „rezultat prognoze” je skup rješenja 2-SAT formule. Treba pronaći 2-SAT formulu čiji je skup rješenja <em>točno</em> zadani skup $S$ od $N$ redaka. Klauzulu koju neki redak iz $S$ krši ne smijemo upotrijebiti — ona bi taj redak izbacila. Zovimo klauzulu <em>dopuštenom</em> ako je zadovoljavaju svi retci iz $S$.</p>'''),
        ('Zašto je dovoljno uzeti sve dopuštene klauzule odjednom?',
         r'''<p>Neka je $F$ konjunkcija svih dopuštenih klauzula. Svaki redak iz $S$ zadovoljava svaku dopuštenu klauzulu, pa je $S \subseteq \mathrm{sol}(F)$. Ako postoji tražena formula $F^\ast$ sa $\mathrm{sol}(F^\ast) = S$, sve su njezine klauzule dopuštene, dakle $F$ sadrži $F^\ast$ i $\mathrm{sol}(F) \subseteq \mathrm{sol}(F^\ast) = S$. Zaključak: tražena formula postoji ako i samo ako $\mathrm{sol}(F) = S$, a zbog $S \subseteq \mathrm{sol}(F)$ to znači: ako i samo ako $F$ ima točno $N$ rješenja. Nema što pogađati — $F$ je jedini kandidat koji treba provjeriti.</p>'''),
        ('Kako brzo odrediti koje su klauzule dopuštene?',
         r'''<p>Klauzula $A \lor B$ je isto što i implikacija $\lnot A \to B$. Za literal $L$ neka je $\mathrm{rows}(L)$ skup redaka u kojima je $L$ istinit (bitset duljine $N$). Implikacija $L \to K$ vrijedi u svim retcima točno kad $\mathrm{rows}(L) \subseteq \mathrm{rows}(K)$, tj. $\mathrm{rows}(L)\,\&\,\lnot\mathrm{rows}(K) = 0$. Za sve $(2M)^2$ parova literala to je $O(M^2 N / w)$ operacija na riječima, oko $5 \cdot 10^8$ za $M = N = 2000$ — prolazi u pola sekunde. Rezultat spremamo kao bitset $\mathrm{imp}[L]$ (duljine $2M$) svih literala koje $L$ implicira.</p>'''),
        ('Kako prebrojati rješenja formule $F$ bez eksplozije, a da svaki list rekurzije bude rješenje?',
         r'''<p>Relacija „podskup” je tranzitivna, pa je $\mathrm{imp}[L]$ ujedno i tranzitivno zatvorenje — skup svih literala koje istinitost $L$ forsira. Držimo skup $T$ istinitih literala koji je konzistentan (ne sadrži $K$ i $\lnot K$) i zatvoren na implikacije, i granamo na prvoj varijabli koju $T$ ne određuje: $x$ je dopušten izbor ako $\mathrm{imp}[x]$ ne sadrži $\lnot x$ ni negaciju ničega iz $T$; tada je $T \cup \mathrm{imp}[x]$ opet konzistentan i zatvoren. Ključno: za neodređenu varijablu <em>barem jedan</em> od izbora $x$, $\lnot x$ je dopušten, pa se svaki konzistentan zatvoren $T$ proširuje do rješenja i broj listova je točno broj rješenja. Prekidamo čim listova bude više od $N$.</p>'''),
        ('Zašto barem jedna grana uvijek prolazi i koliko sve to košta?',
         r'''<p>Implikacije su simetrične na kontrapoziciju: $\mathrm{rows}(x) \subseteq \mathrm{rows}(\lnot y) \iff \mathrm{rows}(y) \subseteq \mathrm{rows}(\lnot x)$. Da $x$ forsira $\lnot y$ za neki $y \in T$, onda bi $y$ forsirao $\lnot x$, pa bi zbog zatvorenosti $\lnot x$ već bio u $T$ — a $x$ je neodređen. Dakle $x$ može propasti jedino ako $x \to \lnot x$, tj. $\mathrm{rows}(x) = \emptyset$; oba literala ne mogu imati prazan skup redaka jer je $N \ge 1$. Svaki čvor rekurzije ima ispod sebe barem jedno rješenje, čvorova je najviše $(N+1) \cdot M$, svaki košta $O(M/w)$: ukupno $O(N M^2 / w) \approx 1.3 \cdot 10^8$.</p>'''),
    ],
    'tips': [
        r'''Kad treba <strong>rekonstruirati ograničenja iz skupa rješenja</strong> („postoji li formula/skup pravila čiji su ovo točno svi ishodi”), uzmi <em>sva</em> ograničenja koja nijedno rješenje ne krši: to je najjači kandidat, i tražena formula postoji ako i samo ako on ne dopušta ništa dodatno.''',
        r'''Klauzula $A \lor B$ je implikacija $\lnot A \to B$; „implikacija vrijedi na svim redcima” = <strong>podskup bitsetova</strong> $\mathrm{rows}(\lnot A) \subseteq \mathrm{rows}(B)$. Provjera podskupa je jedna AND-NOT petlja, a relacija podskupa je automatski tranzitivno zatvorena.''',
        r'''Nabrajanje rješenja 2-SAT-a grananjem je linearno u broju rješenja ako svaki djelomični izbor proširiš njegovim zatvorenjem i provjeriš konzistentnost — tada nema mrtvih grana (dokaz preko kontrapozicije), pa možeš sigurno prekinuti nakon $N+1$ pronađenih rješenja.''',
        r'''Konstanta varijabla u svim redcima (npr. uvijek spas) izražava se <em>jediničnom</em> klauzulom $E_j \lor E_j$ — provjeri u tekstu smije li $I = J$ (ovdje smije, vidi službeni primjer).''',
    ],
    'solution': r'''
<p>Literal 2-SAT formule je varijabla ili negacija varijable. Svaki literal $L$ ima pridruženu varijablu $V(L)$ i pridruženu vrijednost $E(L)$ — istinu ili laž, ovisno o tome je li literal pozitivan ili negativan.</p>
<p>Kažemo da literal $L$ <em>implicira</em> literal $M$ ako je u svakom rješenju u kojem je $V(L)$ postavljena na $E(L)$ također $V(M)$ postavljena na $E(M)$.</p>
<p>Neka je $F$ 2-SAT formula u koju smo dodali svaku klauzulu oblika $\lnot L \lor M$ za sve takve parove. Ako odgovarajuća 2-SAT formula postoji, uključili smo sve njezine klauzule; dodatne klauzule ne stvaraju proturječje. Stoga 2-SAT formula postoji ako i samo ako je skup rješenja formule $F$ jednak ulazu.</p>
<p><b>Nabrajanje svih rješenja 2-SAT formule.</b></p>
<ol>
<li>Neka je $G$ usmjereni graf čiji su vrhovi literali, a za svaku klauzulu $L \lor M$ postoje bridovi $\lnot L \to M$ i $\lnot M \to L$.</li>
<li>Ako postoji literal $L$ takav da su $L$ i $\lnot L$ u istoj komponenti jake povezanosti, nema rješenja.</li>
<li>Svako pridruživanje u kojem nema puta iz istinitog u lažni literal je valjano.</li>
<li>Prolazi literale $L$ u topološkom poretku; ako je literal nepridružen, postavi ga na istinu odnosno na laž i rekurzivno nastavi u oba slučaja.</li>
<li>Ako je postavljen na istinu, svi literali dosežni iz njega također moraju biti istiniti.</li>
</ol>
<p>Vremenska složenost: $O(N \cdot M^2 / w)$.</p>
''',
    'detailed': r'''
<h3>1. Prijevod u 2-SAT</h3>
<p>Događaj $E_j$ je Booleova varijabla $x_j$ ($1$ = spas). Literal je $x_j$ („$E_j$ je spas”) ili $\lnot x_j$ („$E_j$ je katastrofa”); označimo ih brojevima $2j$ i $2j+1$, tako da je negacija literala $\ell$ upravo $\ell \oplus 1$. Četiri tipa proročanstva $(i, j, t)$ su četiri klauzule $\lnot x_i \lor \lnot x_j$, $x_i \lor \lnot x_j$, $\lnot x_i \lor x_j$, $x_i \lor x_j$ ($t = 1, 2, 3, 4$). Skup proročanstava je 2-SAT formula, a „rezultat prognoze” je skup njezinih rješenja. Zadatak: postoji li 2-SAT formula čiji je skup rješenja točno zadani skup $S$ od $N$ različitih redaka, i ako da, ispiši jednu.</p>
<h3>2. Najjača dopuštena formula</h3>
<p>Klauzulu zovemo <em>dopuštenom</em> ako je zadovoljava svaki redak iz $S$. Neka je $F$ konjunkcija svih dopuštenih klauzula.</p>
<ul>
<li>$S \subseteq \mathrm{sol}(F)$: svaki redak iz $S$ po definiciji zadovoljava svaku klauzulu iz $F$.</li>
<li>Ako postoji formula $F^\ast$ sa $\mathrm{sol}(F^\ast) = S$, svaka njezina klauzula je dopuštena (inače bi neki redak iz $S$ ne bio rješenje), pa $F$ sadrži sve klauzule od $F^\ast$ i zato $\mathrm{sol}(F) \subseteq \mathrm{sol}(F^\ast) = S$.</li>
</ul>
<p>Dakle: <strong>tražena formula postoji ako i samo ako $\mathrm{sol}(F) = S$</strong>, i tada je $F$ jedno valjano rješenje. Budući da $S \subseteq \mathrm{sol}(F)$ uvijek vrijedi, uvjet je ekvivalentan s $|\mathrm{sol}(F)| = N$. Cijeli zadatak svodi se na: (a) odrediti dopuštene klauzule, (b) prebrojati rješenja formule $F$ (dovoljno do $N + 1$).</p>
<h3>3. Dopuštene klauzule kao podskupovi bitsetova</h3>
<p>Klauzula $A \lor B$ je logički ista kao implikacija $\lnot A \to B$. Za literal $\ell$ neka je $\mathrm{rows}(\ell) \subseteq \{0, \dots, N-1\}$ skup redaka u kojima je $\ell$ istinit; to je bitset duljine $N$ ($\mathrm{rows}(2j)$ je $j$-ti stupac ulaza, $\mathrm{rows}(2j+1)$ njegov komplement). Implikacija $\ell \to k$ vrijedi u svim redcima točno kad</p>
<p style="text-align:center">$\mathrm{rows}(\ell) \subseteq \mathrm{rows}(k) \iff \mathrm{rows}(\ell)\ \&\ \lnot\mathrm{rows}(k) = 0$.</p>
<p>Za svih $(2M)^2 = 1.6 \cdot 10^7$ uređenih parova literala provjera podskupa košta $\lceil N/64 \rceil \le 32$ riječi, ukupno $\approx 5 \cdot 10^8$ jednostavnih operacija — oko $0.3$ s. Rezultat pamtimo kao bitset $\mathrm{imp}[\ell]$ duljine $2M$: bit $k$ je postavljen ako $\ell \to k$. Memorija $4000 \cdot 4000$ bita $= 2$ MB.</p>
<p>Dva svojstva relacije $\mathrm{imp}$ koja će nam trebati:</p>
<ul>
<li><em>Tranzitivnost.</em> $\mathrm{rows}(\ell) \subseteq \mathrm{rows}(k) \subseteq \mathrm{rows}(m)$ povlači $\ell \to m$. Zato je $\mathrm{imp}[\ell]$ već tranzitivno zatvorenje: skup svih literala koje istinitost $\ell$ (uz formulu $F$) forsira. Ne trebamo SCC-ove ni topološki poredak.</li>
<li><em>Kontrapozicija.</em> $\mathrm{rows}(\ell) \subseteq \mathrm{rows}(\lnot k) \iff \mathrm{rows}(k) \subseteq \mathrm{rows}(\lnot \ell)$ (komplementiranje obje strane), tj. $\ell \to \lnot k \iff k \to \lnot \ell$.</li>
</ul>
<p>Poseban slučaj: ako je $\mathrm{rows}(\ell) = \emptyset$ (varijabla je u svim redcima konstantna), $\ell$ implicira <em>sve</em>, uključujući $\lnot \ell$ — to je jedinična klauzula $\lnot\ell \lor \lnot\ell$ koja varijablu fiksira.</p>
<h3>4. Nabrajanje rješenja formule $F$</h3>
<p>Držimo skup $T$ literala proglašenih istinitima (bitset duljine $2M$) s invarijantom: $T$ je <em>konzistentan</em> (ne sadrži $k$ i $\lnot k$) i <em>zatvoren</em> ($\ell \in T$ i $\ell \to k$ povlače $k \in T$). Rekurzija:</p>
<ol>
<li>Nađi prvu varijablu $j$ za koju ni $2j$ ni $2j+1$ nije u $T$. Ako je nema, $T$ određuje sve varijable i predstavlja jedno rješenje: povećaj brojač; ako je brojač $> N$, prekini sve.</li>
<li>Za $\ell \in \{2j, 2j+1\}$: izbor $\ell$ je <em>dopušten</em> ako $\lnot\ell \notin \mathrm{imp}[\ell]$ i $\mathrm{imp}[\ell] \cap \lnot T = \emptyset$, gdje je $\lnot T$ skup negacija literala iz $T$ (bitset $T$ sa zamijenjenim susjednim bitovima — jedna maska $0x5555\ldots$ i pomaci). Ako je dopušten, rekurzivno nastavi s $T' = T \cup \mathrm{imp}[\ell]$.</li>
</ol>
<p><strong>$T'$ zadovoljava invarijantu.</strong> Zatvorenost: $T$ je zatvoren, a $\mathrm{imp}[\ell]$ je zatvoren po tranzitivnosti. Konzistentnost: par $k, \lnot k$ ne može biti unutar $T$ (pretpostavka), ni s jednim članom u $T$ i drugim u $\mathrm{imp}[\ell]$ (provjereno presjekom s $\lnot T$), ni unutar $\mathrm{imp}[\ell]$: tada bi $\mathrm{rows}(\ell) \subseteq \mathrm{rows}(k) \cap \mathrm{rows}(\lnot k) = \emptyset$, pa bi $\lnot \ell \in \mathrm{imp}[\ell]$, što je isključeno.</p>
<p><strong>Svaki list je rješenje, svako rješenje je točno jedan list.</strong> $T$ koji određuje sve varijable zadovoljava svaku klauzulu $\lnot a \lor b$ iz $F$: ako je $a \in T$, zbog zatvorenosti je $b \in T$; inače je $\lnot a \in T$ i klauzula je zadovoljena. Obratno, svako rješenje $\sigma$ formule $F$ prati točno jednu granu: u svakom čvoru grana se na varijabli $j$ i $\sigma$ bira točno jedan od literala $2j$, $2j+1$; taj izbor je dopušten jer $\sigma$ (koje zadovoljava $F$, dakle sve implikacije) sadrži $\mathrm{imp}[\ell]$ i cijeli $T \subseteq \sigma$, pa u $\sigma$ nema proturječja. Stoga je broj listova jednak $|\mathrm{sol}(F)|$.</p>
<p><strong>Nema mrtvih grana.</strong> Tvrdimo da je za neodređenu varijablu $j$ barem jedan od izbora dopušten. Neka $\ell = 2j$ nije dopušten. Ako je razlog $\lnot k \in \mathrm{imp}[\ell]$ za neki $k \in T$, kontrapozicija daje $k \to \lnot \ell$, pa je po zatvorenosti $\lnot \ell \in T$ — proturječje s neodređenošću $j$. Dakle jedini mogući razlog je $\lnot \ell \in \mathrm{imp}[\ell]$, tj. $\mathrm{rows}(\ell) = \emptyset$. Za oba literala to ne može vrijediti, jer je $\mathrm{rows}(2j) \cup \mathrm{rows}(2j+1)$ skup svih $N \ge 1$ redaka. Prema tome svaki čvor rekurzije ima ispod sebe barem jedan list (rješenje).</p>
<p><strong>Složenost.</strong> Dubina rekurzije je najviše $M$, svaki čvor ima ispod sebe barem jedno od najviše $N + 1$ prebrojanih rješenja, pa je čvorova $O((N+1) M)$; u svakom radimo $O(M / w)$ operacija na riječima. Ukupno $O(N M^2 / w) \approx 1.3 \cdot 10^8$. Bitsetove $T$ po dubini držimo u unaprijed alociranom stogu (nema alokacija u rekurziji); dubina $2000$ je sigurna za sistemski stog.</p>
<h3>5. Ispis</h3>
<p>Ako je broj rješenja različit od $N$ (ili prekoračen), ispiši $-1$. Inače je $\mathrm{sol}(F) = S$ i ispisujemo $F$: za svaki par $a \ne b$ s $a \to b$ klauzulu $\lnot a \lor b$, tj. neuređeni par literala $\{a \oplus 1, b\}$. Tautologije $\{p, \lnot p\}$ preskačemo (uvijek istinite, ne mijenjaju skup rješenja), duplikate uklanjamo sortiranjem. Klauzula $\{p, q\}$ s $p \le q$ prevodi se u $(I, J, t) = (\lfloor p/2 \rfloor, \lfloor q/2 \rfloor, t)$, gdje $t$ ovisi o paritetima: $p$ paran znači „$E_I$ spas”, pa je $t = 4$ za (paran, paran), $2$ za (paran, neparan), $3$ za (neparan, paran), $1$ za (neparan, neparan). Jedinične klauzule imaju $I = J$ — dopušteno, kao u službenom primjeru (<code>2 2 4</code>).</p>
<p><em>Broj klauzula.</em> Neuređenih parova $\{p, q\}$ s $p \le q$ među $2M$ literala je $2M^2 + M$; $M$ od njih su tautologije, pa je $K \le 2M^2$ — točno granica iz zadatka.</p>
<h3>6. Primjer</h3>
<p>Drugi službeni primjer: $M = 3$, $S = \{101, 011, 111\}$. $\mathrm{rows}(x_2) = $ svi, $\mathrm{rows}(\lnot x_2) = \emptyset$, pa $\lnot x_2$ implicira sve — dobivamo jediničnu klauzulu $x_2 \lor x_2$ (<code>2 2 4</code>) i klauzule $x_2 \lor \cdot$. Nadalje $\mathrm{rows}(\lnot x_0) = \{011\} \subseteq \mathrm{rows}(x_1)$, dakle $\lnot x_0 \to x_1$, klauzula $x_0 \lor x_1$ (<code>0 1 4</code>); simetrično $\lnot x_1 \to x_0$ daje istu klauzulu. Formula $F$ ima rješenja točno one nizove s $x_2 = 1$ i $(x_0, x_1) \ne (0, 0)$: $101, 011, 111$ — tri rješenja $= N$, odgovor postoji. Tautologije ($x_0 \lor \lnot x_0$ i sl.) preskačemo; ispis je <code>0 1 4</code>, <code>0 2 4</code>, <code>0 2 3</code>, <code>1 2 4</code>, <code>1 2 3</code>, <code>2 2 4</code> — isti skup od $6$ klauzula kao u službenom izlazu (prihvaća se, dakako, svaki valjan skup).</p>
<p>Prvi primjer: $M = 1$, $S = \{1, 0\}$. $\mathrm{rows}(x_0) = \{0\}$, $\mathrm{rows}(\lnot x_0) = \{1\}$; nijedan pravi podskup, jedine implikacije su $\ell \to \ell$ — nema klauzula, $K = 0$, a formula bez klauzula ima $2 = N$ rješenja.</p>
<h3>7. Zamke</h3>
<ul>
<li>Bez provjere „točno $N$ rješenja” lako je ispisati formulu koja dopušta više redaka nego što ih je zadano; npr. $S = \{00, 11\}$ daje implikacije $x_0 \leftrightarrow x_1$ i točno $2$ rješenja (odgovor postoji), ali za $S = \{000, 011, 101\}$ dopuštene su samo implikacije $x_0 \to x_2$, $x_1 \to x_2$, $x_0 \to \lnot x_1$ (i kontrapozicije), a ta formula dopušta i redak $001$ — četiri rješenja, pa je odgovor $-1$.</li>
<li>Prekini nabrajanje odmah nakon $N + 1$ rješenja — bez toga formula bez klauzula ima $2^M$ rješenja.</li>
<li>Negacija bitseta $T$ (zamjena susjednih bitova) mora se raditi na razini riječi; provjeri da $2M$ literala stane u $W = \lceil 2M/64 \rceil$ riječi i da su viši bitovi zadnje riječi nula.</li>
<li>Ispis do $8 \cdot 10^6$ brojeva — koristi jedan veliki međuspremnik i <code>fwrite</code>.</li>
</ul>
''',
    'verified': r'''uzorci 2/2 (preko <code>check.py</code>, jer je valjanih ispisa više); 300 slučajnih testova ($M \le 8$, $60\,\%$ generirano kao skup rješenja slučajne 2-SAT formule, ostatak slučajni skupovi redaka) — brute force iscrpno nabraja $2^M$ rješenja formule svih dopuštenih klauzula, a validator provjerava $K \le 2M^2$ i da je skup rješenja ispisane formule točno zadani skup; 3 velika testa s $N, M \approx 2000$ (lanac s $M+1$ rješenja, isti lanac s izbačenim retkom $\Rightarrow -1$, $2000$ slučajnih redaka; najviše 0.54 s).''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'LaLa and Harvesting', 'title_hr': 'LaLa i žetva', 'slug': 'H_lala_and_harvesting',
    'tl': '4 s', 'ml': '1024 MB',
    'statement': r'''
<p>Graf usjeva s vrhovima $0..N-1$ (težine $T_u$) nastaje u tri faze: (1) kaktus (povezan jednostavan graf u kojem svaki brid leži na najviše jednom ciklusu) s $M$ bridova; (2) uzmi DFS-stablo kaktusa iz vrha $0$ (susjedi u redoslijedu ulaza), neka su $c_0, \dots, c_{l-1}$ listovi DFS-stabla u DFS-poretku — dodaju se bridovi ciklusa $(c_0, c_1), \dots, (c_{l-1}, c_0)$; (3) dodaje se još $K$ bridova koji čine stablo u kojem svaki vrh stupnja $> 1$ ima stupanj $\ge 12$. Nađi nezavisan skup najveće ukupne težine i ispiši ga.</p>
<h3>Ulaz</h3>
<p>$N, M$ ($2 \le N \le 500$, $N - 1 \le M \le 2N$), težine $T_u \le 200\,000$, $M$ bridova kaktusa, $K$ ($1 \le K \le \min(N-1, 100)$) i $K$ bridova treće faze. Mogu postojati višestruki bridovi.</p>
<h3>Izlaz</h3>
<p>$W$, $L$ i rastući popis odabranih vrhova.</p>
''',
    'hints': [
        r'''<p>Bez treće faze, kaktus (ili stablo) s ciklusom kroz listove DFS-stabla je (generalizirani) Halinov graf — poznato je da ima malu širinu stabla (treewidth). Nezavisan skup najveće težine na grafu ograničene širine stabla rješava se DP-om po dekompoziciji.</p>''',
        r'''<p>Stablo iz treće faze ima vrhovni pokrivač veličine $\max(1, (K-1)/11)$ (nelistovi stupnja $\ge 12$). Dodavanje grafa s vrhovnim pokrivačem $B$ grafu širine $A$ daje širinu $\le A + B$: ubaci pokrivač u svaku vreću.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Da nema treće faze i da je prva faza stablo, graf bi bio Halinov graf — širina stabla $\le 3$. Za kaktus u prvoj fazi: u dekompoziciju Halinova grafa (po DFS-stablu) u svaku vreću ubaci korijen DFS-stabla relevantnih ciklusa; širina postaje $\le 4$.</p>'''),
        ('Redukcija', r'''<p>Spoj grafa širine stabla $\le A$ i grafa s vrhovnim pokrivačem $\le B$ ima širinu $\le A + B$ (pokrivač dodaj u sve vreće). Stablo treće faze s $K$ bridova, u kojem svi nelistovi imaju stupanj $\ge 12$, ima vrhovni pokrivač veličine $\max(1, (K-1)/11)$ (uzmi sve nelistove — svaki pokriva $\ge 12$ bridova, a bridova je $K$; ili, za zvijezdu, jedan vrh). Dakle ulazni graf ima dekompoziciju širine $\le 4 + 9 = 13$.</p>'''),
        ('Algoritam i složenost', r'''<p>Konstruiraj dekompoziciju eksplicitno (DFS-stablo kaktusa, vreće Halinova grafa uz korijene ciklusa, plus fiksnih $\le 9$ vrhova pokrivača). DP za nezavisan skup najveće težine po vrećama: stanje je podskup vreće; pamti odabire za rekonstrukciju. Vrijeme $O\!\left(N \cdot 2^{5 + (K-1)/11} \cdot (5 + (K-1)/11)\right)$.</p>'''),
    ],
    'solution': r'''
<ul>
<li>Da nema treće faze i da je graf iz prve faze stablo, ovaj graf bio bi poznat kao Halinov graf, koji ima širinu stabla $\le 3$.</li>
<li>Da nema treće faze, u svaku vreću dekompozicije Halinova grafa ubacimo korijen DFS-stabla relevantnih ciklusa. Dobivena dekompozicija ima širinu $\le 4$.</li>
<li>Spajanje grafa širine stabla $\le A$ s grafom čiji je vrhovni pokrivač $\le B$ daje graf širine stabla $\le A + B$.</li>
<li>Budući da stablo iz treće faze ima vrhovni pokrivač veličine $\max(1, (K-1)/11)$, možemo konstruirati dekompoziciju ulaznog grafa širine $\le 13$. Odgovor se tada nalazi u $O\!\left(N \cdot 2^{5 + (K-1)/11} \cdot (5 + (K-1)/11)\right)$.</li>
</ul>
''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'LaLa and Spirit Summoning', 'title_hr': 'LaLa i prizivanje duha', 'slug': 'I_lala_and_spirit_summoning',
    'tl': '3 s', 'ml': '1024 MB',
    'statement': r'''
<p>Duh ima $N$ zglobova i $M$ šipki u boji; šipka spaja dva zgloba i ima proizvoljnu (fiksiranu) duljinu. LaLa uklanja neke šipke tako da (1) ne ostanu dvije šipke iste boje i (2) <em>stupanj slobode</em> preostalog mehanizma bude najmanji mogući. Stupanj slobode je (intuitivno) broj neovisnih smjerova gibanja u ravnini koji čuvaju duljine šipki, maksimiziran po svim smještajima (generički smještaj). Ispiši taj najmanji stupanj slobode.</p>
<h3>Ulaz</h3>
<p>$N, M$ ($2 \le N \le 200$, $0 \le M \le 1000$) i šipke $u_i\ v_i\ c_i$ ($0 \le c_i < M$). Višestruke šipke su moguće.</p>
<h3>Izlaz</h3>
<p>Stupanj slobode.</p>
<h3>Primjer</h3>
<p>Trokut čije su sve tri šipke boje $0$: $5$ (ostaje jedna šipka: $2 \cdot 3 - 1$). Trokut s tri različite boje: $3$. Četverokut s četiri boje: $4$. Put s $4$ šipke na $5$ zglobova: $6$.</p>
''',
    'hints': [
        r'''<p>Svaka šipka generički smanjuje stupanj slobode za $1$ ili za $0$; skup šipki koje ga smanjuju čini matroid — <em>matroid krutosti</em> (rigidity matroid) u ravnini. Stupanj slobode $= 2N - \operatorname{rank}$.</p>''',
        r'''<p>Uvjet „bez dvije iste boje” je particijski matroid. Traži se najveći zajednički nezavisan skup: presjek matroida. Za orakul nezavisnosti matroida krutosti koristi Lamanov uvjet ($|E(S)| \le 2|V(S)| - 3$ za sve podskupove) provjeren igrom kamenčićima (pebble game).</p>''',
    ],
    'coach': [
        ('Što je stupanj slobode u jeziku linearne algebre i zašto je „generički” ključna riječ?',
         r'''<p>Smještaj je točka $p \in \mathbb{R}^{2N}$. Šipka $(u, v)$ nameće uvjet $|p_u - p_v|^2 = \text{konst}$; brzine koje čuvaju sve duljine čine jezgru <em>matrice krutosti</em> $R(p)$ (jedan redak $(p_u - p_v, -(p_u - p_v))$ po šipki). Stupanj slobode je $\dim \ker R(p) = 2N - \operatorname{rank} R(p)$, a maksimum po smještajima postiže se za generički $p$, gdje je rang najveći mogući. Skupovi šipki čiji su retci linearno nezavisni za generički $p$ čine <strong>matroid</strong> (linearni matroid redaka), tzv. generički matroid krutosti ravnine. Dakle stupanj slobode $= 2N - r(S)$, gdje je $r$ rang u tom matroidu; broji i $3$ trivijalna gibanja (translacije i rotacija).</p>'''),
        ('Kako prepoznati koji su skupovi šipki nezavisni bez računanja s realnim brojevima?',
         r'''<p>Nužan uvjet: ako je $T$ nezavisan, svaki neprazan $T' \subseteq T$ ima $|T'| \le 2|V(T')| - 3$, jer skup vrhova $V(T')$ sam ima najviše $2|V(T')| - 3$ neovisnih ograničenja (od $2|V(T')|$ koordinata $3$ uvijek ostaju za kruta gibanja). <strong>Lamanov teorem</strong> (1970.) kaže da je taj uvjet i dovoljan u ravnini. Time je matroid krutosti čisto kombinatorni — $(2,3)$-rijetki matroid — i možemo ga ispitivati bez geometrije. Napomena: dvije paralelne šipke $u$–$v$ čine skup s $2 > 2 \cdot 2 - 3$, dakle su ovisne (višestruke šipke su dopuštene u ulazu!).</p>'''),
        ('Koje dvije strukture se ovdje sijeku i koji je standardni algoritam?',
         r'''<p>„Bez dvije šipke iste boje” = nezavisan skup <em>particijskog matroida</em>. Tražimo najveći skup nezavisan u oba matroida: <strong>presjek matroida</strong>. Standardni algoritam: kreni od $I = \emptyset$ i ponavljaj augmentaciju najkraćim putem u grafu zamjena — izvori su $y \notin I$ koje smijemo dodati u prvi matroid, ponori $y \notin I$ koje smijemo dodati u drugi, lukovi $x \to y$ ($x \in I$) kad je $I - x + y$ nezavisan u prvom, $y \to x$ kad je nezavisan u drugom. Najkraći put od izvora do ponora daje simetričnu razliku $I \,\triangle\, P$ koja je zajednički nezavisan skup veličine $|I| + 1$; kad puta nema, $I$ je maksimalan (dokaz preko min–max teorema Edmondsa). Augmentacija je najviše $r \le 2N - 3$.</p>'''),
        ('Kako brzo odgovarati na pitanje „je li $I + y$ (odnosno $I - x + y$) Lamanov”?',
         r'''<p>Provjera svih podskupova je eksponencijalna; koristi se <strong>igra kamenčićima</strong> (pebble game, Jacobs–Hendrickson, Lee–Streinu). Svaki vrh dobiva $2$ kamenčića. Umetanje brida $uv$: pokušaj skupiti $4$ kamenčića na $\{u, v\}$ premještanjem po usmjerenim putevima (kamenčić s vrha $w$ dostupnog iz $u$ preseli se na $u$ okretanjem puta), zatim jedan kamenčić s $u$ „plati” brid, koji se usmjeri $u \to v$. Invarijanta: kamenčića na skupu $V'$ je $2|V'| - (\text{bridovi s početkom u } V')$. Skupljanje $4$ kamenčića uspijeva ako i samo ako je $I + uv$ Lamanov: ako ne uspije, skup $\mathrm{Reach}(u,v)$ ima točno $3$ kamenčića i sve njegove bridove unutra, dakle točno $2|V'| - 3$ bridova — dodavanje $uv$ krši uvjet. Obratno, ako uvjet ne bi bio prekršen ni za jedan podskup, moglo bi se pokazati da $4$ kamenčića postoje (Lee–Streinu).</p>'''),
        ('Kako iz neuspjelog umetanja dobiti cijeli fundamentalni krug, a ne samo „ne”?',
         r'''<p>Ako $I + y$ nije nezavisan, $I - x + y$ je nezavisan točno za $x$ iz jedinstvenog kruga $C \subseteq I + y$. Tvrdnja: $C - y$ su točno bridovi iz $I$ s oba kraja u $\mathrm{Reach}(u, v)$. Dokaz: $V' = \mathrm{Reach}$ je tijesan ($2|V'| - 3$ bridova) i sadrži $u, v$, pa $E_I(V') + y$ krši uvjet i $C \subseteq E_I(V') + y$. S druge strane, $V(C)$ je također tijesan skup koji sadrži $u, v$, pa ima najviše $3$ kamenčića; sva $3$ preostala kamenčića sjede na $u, v \in V(C)$, što znači da nijedan brid ne napušta $V(C)$ i da $\mathrm{Reach} \subseteq V(C)$. Zato $V' = V(C)$ i $C = E_I(V') + y$. Jedan DFS daje sve lukove $y \to x$ grafa zamjena.</p>'''),
        ('Koliko sve to košta?',
         r'''<p>Po augmentaciji: izgradnja igre za $I$ ($|I| \le 2N - 3$ umetanja, svako nekoliko DFS-ova po $O(N + |I|)$), zatim za svaki $y \notin I$ jedno skupljanje i jedan DFS dosežnosti — $O(M (N + M))$; BFS po grafu zamjena je $O(M + \text{broj lukova}) = O(M \cdot N)$. Ukupno $O(r \cdot M \cdot (N + M))$, s $r \le 2N$, $N = 200$, $M = 1000$ oko $10^8$ jednostavnih koraka u najgorem slučaju — u praksi daleko manje (0.3 s).</p>'''),
    ],
    'tips': [
        r'''„Broj neovisnih ograničenja / stupanj slobode u generičkom položaju” gotovo uvijek znači <strong>rang u matroidu</strong> — a čim se traži najveći skup koji je nezavisan u dva matroida (ovdje krutost + „različite boje”), to je <strong>presjek matroida</strong>, ne pohlepni algoritam.''',
        r'''Ravninska krutost je kombinatorna: <strong>Lamanov uvjet</strong> $|E'| \le 2|V'| - 3$ za sve podskupove; provjerava se u polinomnom vremenu <strong>igrom kamenčićima</strong> (2 kamenčića po vrhu, skupi 4 na krajevima novog brida). Neuspjeli pokušaj besplatno daje fundamentalni krug: $\mathrm{Reach}(u, v)$.''',
        r'''U presjeku matroida je za particijski matroid graf zamjena trivijalan (zamjena unutar iste boje); sav rad ide na orakul drugog matroida — ne zaboravi da $I - x + y$ treba provjeriti samo za $x$ u fundamentalnom krugu $y$-a.''',
        r'''Brute force za matroidne zadatke: iscrpno po podskupovima uz doslovnu definiciju (ovdje Lamanov uvjet za svaki podskup) — sporo, ali očito točno; testiraj i s višestrukim bridovima i s jednom bojom.''',
    ],
    'solution': r'''
<ul>
<li>Svaka šipka doprinosi stupnju slobode s $-1$ ili $0$, a šipke koje doprinose $-1$ čine matroid (matroid krutosti).</li>
<li>Skup bridova je nezavisan ako i samo ako svaki podgraf $S$ zadovoljava $2|V| - 3 \ge |E|$ (Lamanov teorem).</li>
<li>Orakul nezavisnosti gradi se provjerom postoji li i dalje $2$-prema-$1$ sparivanje između vrhova i bridova nakon učetverostručenja novog brida (algoritam igre kamenčićima, pebble game).</li>
<li>Algoritam presjeka matroida + orakul krutosti igrom kamenčićima daje rješenje složenosti $O(N^2 \cdot M)$.</li>
</ul>
''',
    'detailed': r'''
<h3>1. Stupanj slobode kao rang matroida</h3>
<p>Smještaj mehanizma je vektor položaja zglobova $p = (p_0, \dots, p_{N-1}) \in \mathbb{R}^{2N}$. Šipka $(u, v)$ zahtijeva $|p_u - p_v|^2 = \text{konst}$; deriviranjem po vremenu, dopuštene brzine $\dot p$ zadovoljavaju $(p_u - p_v) \cdot (\dot p_u - \dot p_v) = 0$ za svaku šipku. To je homogeni linearni sustav $R(p)\,\dot p = 0$ s <em>matricom krutosti</em> $R(p)$ (redak po šipki), pa je (infinitezimalni) stupanj slobode $2N - \operatorname{rank} R(p)$. Rang je funkcija od $p$ koja postiže svoj maksimum na otvorenom gustom skupu (generički smještaji); zadatak traži upravo taj maksimum. Skupovi šipki čiji su retci od $R(p)$ nezavisni za generički $p$ čine matroid (matroid stupaca/redaka matrice nad poljem racionalnih funkcija) — <strong>generički matroid krutosti</strong> $\mathcal{R}_2$. Zato:</p>
<p style="text-align:center">stupanj slobode skupa šipki $S$ $= 2N - r_{\mathcal{R}_2}(S)$,</p>
<p>i minimizirati stupanj slobode znači maksimizirati rang odabranog skupa. Primjer: jedna šipka na tri zgloba ima rang $1$, stupanj slobode $5$; trokut ima rang $3$, stupanj $3$ (samo translacije i rotacija); put s $4$ šipke na $5$ zglobova ima rang $4$, stupanj $6$.</p>
<h3>2. Lamanov teorem: krutost je kombinatorna</h3>
<p>Za svaki neprazan skup šipki $T'$, redaka matrice $R$ koji pripadaju $T'$ ima $|T'|$ i oni žive u koordinatama vrhova $V(T')$, tj. u $\mathbb{R}^{2|V(T')|}$; kako tri smjera (dvije translacije i rotacija) uvijek leže u jezgri, rang je najviše $2|V(T')| - 3$. Dakle nezavisan skup nužno zadovoljava</p>
<p style="text-align:center">$|T'| \le 2\,|V(T')| - 3$ za svaki neprazan $T' \subseteq T$. $\quad(\ast)$</p>
<p><strong>Lamanov teorem</strong>: u ravnini je $(\ast)$ i dovoljan. Time je $\mathcal{R}_2$ jednak $(2,3)$-rijetkom matroidu na bridovima grafa i sve se može raditi cjelobrojno, bez ijedne koordinate. Posljedice: dvije paralelne šipke ($2 > 2 \cdot 2 - 3$) su ovisne — u ulazu su višestruke šipke dopuštene; rang cijelog grafa je najviše $2N - 3$, pa je stupanj slobode $\ge 3$ (za $N \ge 2$).</p>
<h3>3. Presjek matroida</h3>
<p>Uvjet „nema dvije šipke iste boje” opisuje <em>particijski matroid</em> $\mathcal{P}$ (najviše jedna šipka po boji). Traži se $\max\{|I| : I \in \mathcal{P} \cap \mathcal{R}_2\}$ — <strong>presjek dvaju matroida</strong>, standardno rješiv Edmondsovim algoritmom augmentirajućih puteva:</p>
<ol>
<li>$I \leftarrow \emptyset$.</li>
<li>Izgradi <em>graf zamjena</em>: vrhovi su sve šipke. Izvori $X_1 = \{y \notin I : I + y \in \mathcal{P}\}$ (boja od $y$ nije u $I$), ponori $X_2 = \{y \notin I : I + y \in \mathcal{R}_2\}$. Lukovi: $x \to y$ za $x \in I$, $y \notin I$ ako $I - x + y \in \mathcal{P}$ (tj. $y$ ima boju kao $x$); $y \to x$ ako $I - x + y \in \mathcal{R}_2$.</li>
<li>Nađi <em>najkraći</em> put $P$ od $X_1$ do $X_2$ (BFS). Ako ga nema, $I$ je najveći. Inače $I \leftarrow I \,\triangle\, P$ i natrag na 2.</li>
</ol>
<p>Ispravnost je klasična (Edmonds, 1970.): najkraći put nema „prečaca”, pa lema o jedinstvenim zamjenama jamči da je $I \triangle P$ nezavisan u oba matroida i za jedan veći; a nepostojanje puta daje skup $U$ (nedosežni vrhovi) s $|I| = r_{\mathcal{P}}(U) + r_{\mathcal{R}_2}(\bar U)$, što je gornja ograda za svaki zajednički nezavisan skup. Augmentacija je najviše $r \le 2N - 3 \le 397$.</p>
<p>Za $\mathcal{P}$ je sve trivijalno: $X_1$ i lukovi $x \to y$ čitaju se iz boja. Sav pravi rad je orakul za $\mathcal{R}_2$: za svaki $y \notin I$ treba znati je li $I + y$ nezavisan i, ako nije, za koje $x \in I$ je $I - x + y$ nezavisan — a to su točno elementi jedinstvenog <em>fundamentalnog kruga</em> $C(I, y)$ bez $y$.</p>
<h3>4. Igra kamenčićima kao orakul</h3>
<p>$(2,3)$-igra kamenčićima (Jacobs–Hendrickson 1997., Lee–Streinu 2008.) održava za nezavisan skup $I$ usmjerenje bridova i raspodjelu kamenčića: na početku svaki vrh ima $2$ kamenčića; brid $uv$ se umeće tako da se na $\{u, v\}$ skupe $4$ kamenčića, jedan se s $u$ „potroši” i brid usmjeri $u \to v$. Kamenčić se dovlači po usmjerenom putu: DFS iz $u$ po lukovima nađe vrh $w \ne u, v$ s kamenčićem, kamenčić se preseli na $u$ i svi lukovi puta okrenu (svaki vrh puta izgubi jedan ulazni i dobije jedan izlazni luk, pa broj kamenčića + broj izlaznih lukova ostaje $2$ za sve vrhove osim $u$ i $w$).</p>
<p><em>Invarijanta.</em> Za svaki vrh $w$: $\mathrm{peb}(w) + \mathrm{outdeg}(w) = 2$. Za skup $V'$: $\sum_{w \in V'} \mathrm{peb}(w) = 2|V'| - \#\{\text{lukovi s početkom u } V'\} \le 2|V'| - |E_I(V')|$.</p>
<p><em>Neuspjeh skupljanja $\Rightarrow$ ovisnost.</em> Ako se za $y = uv$ ne mogu skupiti $4$ kamenčića, neka je $V' = \mathrm{Reach}(u, v)$ skup vrhova dosežnih iz $\{u, v\}$ lukovima. Svi kamenčići u $V'$ su na $u, v$ (inače bismo ih dovukli) i ima ih $\le 3$; lukovi iz $V'$ ostaju u $V'$ (zatvorenost), pa je $\sum_{V'} \mathrm{peb} = 2|V'| - |E_I(V')|$. Kako je $I$ nezavisan, $|E_I(V')| \le 2|V'| - 3$, pa je kamenčića točno $3$ i $|E_I(V')| = 2|V'| - 3$: $V'$ je <em>tijesan</em>. Dodavanje $y$ (oba kraja u $V'$) prekršilo bi $(\ast)$.</p>
<p><em>Uspjeh $\Rightarrow$ nezavisnost.</em> Neka su na $\{u, v\}$ skupljena $4$ kamenčića (prije plaćanja). Za svaki $V''$ koji sadrži $u$ i $v$ tada je $\sum_{V''} \mathrm{peb} \ge 4$, pa iz invarijante $|E_I(V'')| \le \#\{\text{lukovi iz } V''\} = 2|V''| - \sum_{V''}\mathrm{peb} \le 2|V''| - 4$, dakle $|E_{I+y}(V'')| \le 2|V''| - 3$. Za $V''$ koji ne sadrži oba kraja $y$ vrijedi $E_{I+y}(V'') = E_I(V'')$ i $(\ast)$ slijedi iz nezavisnosti $I$. Prema tome $I + y$ zadovoljava $(\ast)$ i po Lamanu je nezavisan. Zajedno: <strong>skupljanje $4$ kamenčića uspijeva ako i samo ako je $I + y$ nezavisan</strong> — bez obzira na redoslijed umetanja i na to kako su se kamenčići prije premještali.</p>
<p><em>Fundamentalni krug.</em> Tvrdnja: ako je umetanje $y = uv$ odbijeno, tada je $C(I, y) - y = E_I(V')$ za $V' = \mathrm{Reach}(u,v)$. Dokaz. $E_I(V') + y$ krši $(\ast)$, pa jedinstveni krug $C \subseteq E_I(V') + y$, tj. $V(C) \subseteq V'$. S druge strane $V(C)$ je tijesan ($|C| - 1 = 2|V(C)| - 3$, jer je $C - y$ nezavisan, a $C$ nije) i sadrži $u, v$; po invarijanti ima najviše $3$ kamenčića, a $3$ ih već sjedi na $u, v \in V(C)$ — dakle svi lukovi s početkom u $V(C)$ završavaju u $V(C)$ (inače bi ih bilo više od $|E_I(V(C))|$ i kamenčića manje od $3$). Zato DFS iz $\{u, v\}$ ne napušta $V(C)$: $V' \subseteq V(C)$. Slijedi $V' = V(C)$, a onda $|C| - 1 = 2|V'| - 3 = |E_I(V')|$ daje $C - y = E_I(V')$. Dakle $I - x + y \in \mathcal{R}_2 \iff$ oba kraja od $x$ leže u $\mathrm{Reach}(u, v)$ — jedan DFS daje sve lukove $y \to x$.</p>
<h3>5. Algoritam u cjelini</h3>
<ol>
<li>Dok postoji augmentirajući put:
  <ol>
  <li>Izgradi igru kamenčićima za trenutačni $I$ (umetni bridove redom; sva su umetanja uspješna jer je $I$ nezavisan).</li>
  <li>Za svaki $y \notin I$: pokušaj skupiti $4$ kamenčića na krajevima; uspjeh $\Rightarrow$ $y \in X_2$. Neuspjeh $\Rightarrow$ izračunaj $\mathrm{Reach}$ i dodaj lukove $y \to x$ za sve $x \in I$ s oba kraja u $\mathrm{Reach}$. (Premještanja kamenčića pri neuspješnom pokušaju ne kvare stanje — ona su valjani potezi igre.)</li>
  <li>BFS iz $X_1$ (šipke slobodne boje) naizmjence po lukovima $y \to x$ (krug krutosti) i $x \to y$ (ista boja) do prvog $y \in X_2$; $I \leftarrow I \triangle P$.</li>
  </ol></li>
<li>Ispiši $2N - |I|$.</li>
</ol>
<p><strong>Složenost.</strong> Jedna iteracija: izgradnja $O(|I| \cdot (N + |I|))$, orakul za sve $y$: $O(M (N + M))$, BFS $O(M + |I| \cdot M)$; iteracija je $\le 2N - 3$. Ukupno $O(N \cdot M \cdot (N + M)) \approx 2 \cdot 10^8$ elementarnih koraka u najgorem slučaju, u praksi puno manje (0.3 s za $N = 200$, $M = 1000$).</p>
<h3>6. Primjeri i zamke</h3>
<ul>
<li>Trokut s tri iste boje: $\mathcal{P}$ dopušta jednu šipku, $r = 1$, odgovor $5$. Tri različite boje: $r = 3$, odgovor $3$. Četverokut s četiri boje: $4$ šipke na $4$ vrha, $4 \le 5$, sve nezavisne, odgovor $8 - 4 = 4$. Put s $4$ šipke: $10 - 4 = 6$.</li>
<li>$M = 0$: odgovor $2N$. Višestruke šipke između istih zglobova: druga je uvijek ovisna (sam par krši $(\ast)$) — igra to hvata jer nakon prve šipke par $\{u, v\}$ ima točno $3$ kamenčića.</li>
<li>Ne zaboravi da $y$ može biti izvor <em>i</em> ponor istodobno (put duljine $0$).</li>
<li>Pri okretanju puta u DFS-u pamti brid (a ne samo roditelja) — višestruki bridovi u $I$ nisu mogući, ali paralelni bridovi između $I$ i kandidata jesu.</li>
</ul>
''',
    'verified': r'''uzorci 4/4; 300 slučajnih testova ($N \le 7$, $M \le 9$, slučajan broj boja, s višestrukim šipkama) protiv brute forcea koji iscrpno prolazi podskupove šipki i doslovno provjerava različite boje i Lamanov uvjet za svaki podskup; 3 velika testa s $N = 200$, $M = 1000$ ($1000$, $400$ i $150$ boja; najviše 0.34 s).''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'LaLa and Magical Beast Summoning', 'title_hr': 'LaLa i prizivanje magične zvijeri', 'slug': 'J_lala_and_magical_beast_summoning',
    'tl': '5 s', 'ml': '1024 MB',
    'statement': r'''
<p>Polje prizivanja $F(M, E, V)$ ima prost modul $M$ ($9 \cdot 10^8 \le M \le 10^9$) i konstante $E, V \le 100$. Ćelija $C(L, A, I)$ je u <em>nul-stanju</em> ako je $L = 0$, inače je pozitivna s <em>gustoćom</em> $(A \cdot I) / L^2$. Valjanost ćelije i operacija $\mathrm{Combine}_F(C_0, C_1)$ (nekomutativna i neasocijativna; rezultat je opet valjana ćelija) definirane su pseudokodom u izvornom tekstu (uz priloženu sporu C++ implementaciju). $\mathrm{Combine}$ više ćelija računa se slijeva: $\mathrm{Combine}(C_0, \dots, C_{K-1}) = \mathrm{Combine}(\mathrm{Combine}(C_0, \dots, C_{K-2}), C_{K-1})$.</p>
<p>Dan je niz od $N$ valjanih ćelija. Obradi $Q$ upita: <code>1 i L A I</code> — postavi $C_i$; <code>2 l r</code> — neka je $R = \mathrm{Combine}(C_l, \dots, C_{r-1})$; ispiši $-1$ ako je $R$ u nul-stanju, inače gustoću $R$ modulo $M$.</p>
<h3>Ulaz</h3>
<p>$M, E, V$; $N$ ($1 \le N \le 10^5$) ćelija; $Q$ ($1 \le Q \le 10^5$) upita.</p>
<h3>Izlaz</h3>
<p>Odgovor za svaki upit tipa 2.</p>
''',
    'hints': [
        r'''<p>Operacija nije asocijativna, pa segmentno stablo ne može izravno raditi. No traži se samo <em>gustoća</em> — pronađi ekvivalenciju ćelija (skaliranje) koja čuva gustoću i pod kojom operacija <em>postaje</em> asocijativna „do na skalar”.</p>''',
        r'''<p>Uvedi $-C(L, A, I) = C(L, I, A)$, $C_0 + C_1 = \mathrm{Combine}(C_0, -C_1)$ i neutralni element $e = C(0, 3, -3)$. Algebrom se pokaže da je $+$ asocijativna do na množenje skalarom $k$, $0 < k < M$, a skaliranje ne mijenja gustoću.</p>''',
    ],
    'coach': [
        ('Što uvjet valjanosti zapravo opisuje — možemo li ga pročitati kao poznatu jednadžbu?',
         r'''<p>Uvjet iz pseudokoda je kubni polinom u $L, A, I$ koji mora biti $0$ modulo $M$. Simetrija u $A$ i $I$ sugerira supstituciju $X = A + I$, $Y = A - I$, $Z = L$: tada se svih deset članova sabere u $X^3 + E X Z^2 + V Z^3 - Y^2 Z$. Dakle valjana ćelija je točka $(X : Y : Z)$ na <strong>eliptičkoj krivulji</strong> $Y^2 Z = X^3 + E X Z^2 + V Z^3$ u projektivnim koordinatama nad $\mathbb{Z}_M$, a nul-stanje ($L = 0$, $A + I \equiv 0$, $A \ne I$) je točka u beskonačnosti $O = (0 : 1 : 0)$.</p>'''),
        ('Zašto se gustoća ne mijenja pri skaliranju i što to znači za nekomutativnu operaciju?',
         r'''<p>$A = (X + Y)/2$, $I = (X - Y)/2$, pa je gustoća $\dfrac{AI}{L^2} = \dfrac{X^2 - Y^2}{4 Z^2}$ — homogena stupnja $0$, dakle ovisi samo o projektivnoj točki, ne o reprezentantu. Zato smijemo ćelije promatrati „do na skalar” i pitati se: što je $\mathrm{Combine}$ kao operacija na <em>točkama</em> krivulje? Formule u pseudokodu (nazivnici $B = X_0 Z_1 - X_1 Z_0$, $C = Y_0 Z_1 + Y_1 Z_0$, poseban slučaj udvostručenja s $3X^2 + EZ^2$ i $2YZ$) točno su formule tangente i sekante za zbrajanje na krivulji — s $-C_1$ umjesto $C_1$, jer se koristi $I_1 - A_1 = -Y_1$.</p>'''),
        ('Ako je Combine oduzimanje u grupi, kako izgleda lijevo asocirani rezultat?',
         r'''<p>$\mathrm{Combine}(C_0, C_1) = P_0 - P_1$ (provjera rubnih grana: $L_1 = 0 \Rightarrow P_0 - O = P_0$; $L_0 = 0 \Rightarrow O - P_1 = -P_1$, što je zamjena $A \leftrightarrow I$ jer negacija mijenja predznak $Y$; jednake točke $\Rightarrow O = C(0, 3, -3)$). Grupa je komutativna i asocijativna, pa je $(\cdots((P_l - P_{l+1}) - P_{l+2}) \cdots) - P_{r-1} = P_l - (P_{l+1} + \dots + P_{r-1})$. Nekomutativnost i neasocijativnost $\mathrm{Combine}$ bile su samo maska za oduzimanje.</p>'''),
        ('Koja struktura podataka podržava točkovnu promjenu i zbroj po intervalu za asocijativnu operaciju?',
         r'''<p>Segmentno stablo nad grupnim zbrajanjem $+$ s neutralnim elementom $O$: list čuva točku $P_i$, unutarnji čvor zbroj djece. Upit $[l, r)$: $S = P_{l+1} + \dots + P_{r-1}$ iz stabla, zatim $R = P_l + (-S)$; ako je $Z_R = 0$ ispiši $-1$, inače $(X_R^2 - Y_R^2) \cdot (4 Z_R^2)^{-1} \bmod M$ Fermatovim inverzom. Sve u projektivnim koordinatama, bez ijednog dijeljenja u stablu.</p>'''),
        ('Gdje mogu zapeti formule zbrajanja i zašto je krivulja „dobra”?',
         r'''<p>Slučajevi: jedan od operanada $O$; jednake $x$-koordinate ($X_0 Z_1 = X_1 Z_0$) s $Y_0 Z_1 = -Y_1 Z_0$ (rezultat $O$) ili $Y_0 Z_1 = Y_1 Z_0$ (udvostručenje). Krivulja je nesingularna jer je $4E^3 + 27V^2 \le 4.3 \cdot 10^6 < M$, dakle $\ne 0 \bmod M$, pa grupni zakon vrijedi za sve točke. Brojevi su $< 10^9$, umnošci $< 10^{18}$ stanu u 64 bita; negativne razlike normaliziraj. Složenost $O((N + Q) \log N)$ uz dvadesetak modularnih množenja po zbrajanju.</p>'''),
    ],
    'tips': [
        r'''Kad zadatak daje „čudnu” nekomutativnu/neasocijativnu operaciju s dugačkim pseudokodom, traži <strong>skrivenu algebarsku strukturu</strong>: supstituiraj simetrične kombinacije varijabli ($A + I$, $A - I$), pogledaj homogenost i rubne slučajeve ($L = 0$). Kubna jednadžba s $Y^2 = X^3 + \dots$ je eliptička krivulja, a formule s $3x^2 + a$ i $2y$ su formule udvostručenja.''',
        r'''Lijevo asocirani lanac $((a - b) - c) - d$ u komutativnoj grupi jednak je $a - (b + c + d)$ — nekomutativna operacija iz zadatka često je samo <strong>oduzimanje</strong> u komutativnoj grupi, koje se svodi na asocijativno zbrajanje pogodno za segmentno stablo.''',
        r'''Radi u <strong>projektivnim koordinatama</strong> (bez inverza u unutrašnjosti strukture) i normaliziraj tek pri ispisu; homogene veličine stupnja $0$ (kao $\frac{X^2 - Y^2}{4Z^2}$) ne ovise o reprezentantu, pa nije važno koji skalar formule vrate.''',
        r'''Kad dobiješ sporu referentnu implementaciju, iskoristi je kao brute force: doslovno je prepiši i stresiraj svoje rješenje protiv nje na malim $N$ i $Q$ — svaka greška u predznaku ili posebnoj grani odmah ispliva.''',
    ],
    'solution': r'''
<p>Pretpostavimo da sve ćelije leže u polju prizivanja $F(M, E, V)$. Definiramo:</p>
<ul>
<li>$-C(L, A, I) = C(L, I, A)$,</li>
<li>$C(L_0, A_0, I_0) + C(L_1, A_1, I_1) = \mathrm{Combine}\big(C(L_0, A_0, I_0), -C(L_1, A_1, I_1)\big)$, i</li>
<li>$e = C(0, 3, -3)$, koja je valjana.</li>
</ul>
<p>Nešto algebre pokazuje da vrijedi:</p>
<ol>
<li>$k_0 * C(L_0, A_0, I_0) + k_1 * C(L_1, A_1, I_1) = k_2 * \big(C(L_0, A_0, I_0) + C(L_1, A_1, I_1)\big)$ za neki cijeli $0 < k_2 < M$,</li>
<li>$C_0 + (C_1 + C_2) = k * \big((C_0 + C_1) + C_2\big)$ za neki cijeli $0 < k < M$,</li>
<li>$e + C(L, A, I) = k_0 * (C(L, A, I) + e) = k_1 * C(L, A, I)$ za neke cijele $0 < k_0, k_1 < M$, i</li>
<li>$C(L, A, I) + (-C(L, A, I)) = k * e$ za neki cijeli $0 < k < M$.</li>
</ol>
<p>Uočimo da je gustoća $C(L, A, I)$ jednaka gustoći $k * C(L, A, I)$ za svaki cijeli $0 < k < M$.</p>
<p>Za dane $l$ i $r$ cilj je naći gustoću ćelije</p>
<p>$$(\cdots((C_l - C_{l+1}) - C_{l+2}) - \cdots) - C_{r-1} = k * \big(C_l - (C_{l+1} + \dots + C_{r-1})\big)$$</p>
<p>za neki cijeli $0 < k < M$, što je jednako gustoći $C_l - (C_{l+1} + \dots + C_{r-1})$.</p>
<p>Drugo svojstvo osigurava da će upit na segmentnom stablu naći rezultat $C_{l+1} + \dots + C_{r-1}$ pomnožen nekom nenul konstantom, a prvo svojstvo osigurava da će oduzimanje toga od $C_l$ dati traženi rezultat pomnožen nekom nenul konstantom.</p>
<p>Vremenska složenost: $O(N + Q \log N)$ za izgradnju i upite segmentnog stabla.</p>
''',
    'detailed': r'''
<p>Službeno rješenje navodi četiri svojstva „do na skalar” koja se dokazuju „nešto algebre”. Ovdje pokazujemo <em>odakle</em> ta svojstva dolaze: iza pseudokoda skriva se grupa točaka eliptičke krivulje, a $\mathrm{Combine}$ je oduzimanje u toj grupi. Time sva četiri svojstva postaju očita, a implementacija je klasično segmentno stablo.</p>
<h3>1. Što je „valjana ćelija”</h3>
<p>Pseudokod za <code>valid</code> zahtijeva $0 \le L, A, I < M$, za $L = 0$ još $A + I \equiv 0$ i $A \ne I$, te da polinom</p>
<p>$$A^3 - A^2 L + 3A^2 I + E A L^2 + V L^3 + 2ALI + E L^2 I + 3AI^2 - L I^2 + I^3$$</p>
<p>bude $\equiv 0 \pmod M$. (U tiskanom pseudokodu stoji „$\ne 0$”, ali službeni primjer pokazuje da su valjane ćelije upravo one s vrijednošću $0$; priložena C++ implementacija i naš brute force to potvrđuju.) Polinom je simetričan u $A$ i $I$ osim u članovima s $L$, što poziva na supstituciju</p>
<p style="text-align:center">$X = A + I, \quad Y = A - I, \quad Z = L.$</p>
<p>Provjera: $X^3 = A^3 + 3A^2I + 3AI^2 + I^3$, $E X Z^2 = EAL^2 + EIL^2$, $V Z^3 = VL^3$, $-Y^2 Z = -A^2L + 2ALI - LI^2$; zbroj je točno gornji polinom. Dakle</p>
<p style="text-align:center">ćelija je valjana $\iff$ $Y^2 Z = X^3 + E X Z^2 + V Z^3$,</p>
<p>a to je homogena (projektivna) Weierstrassova jednadžba eliptičke krivulje $y^2 = x^3 + Ex + V$ nad $\mathbb{Z}_M$. Ćelija je <em>projektivna točka</em> $(X : Y : Z)$; za $L = 0$ uvjeti $A + I \equiv 0$, $A \ne I$ znače $X = 0$, $Y \ne 0$ — jedina točka s $Z = 0$, tj. točka u beskonačnosti $O = (0 : 1 : 0)$. Krivulja je nesingularna jer je diskriminanta $-16(4E^3 + 27V^2)$ različita od nule: $1 \le 4E^3 + 27V^2 \le 4\,270\,000 < M$.</p>
<h3>2. Gustoća je funkcija točke, ne reprezentanta</h3>
<p>Iz $A = (X + Y)/2$, $I = (X - Y)/2$ slijedi</p>
<p>$$\frac{A \cdot I}{L^2} = \frac{X^2 - Y^2}{4 Z^2}.$$</p>
<p>Brojnik i nazivnik su homogeni stupnja $2$, pa množenje $(X, Y, Z)$ skalarom $k \ne 0$ ne mijenja vrijednost — to je službeno „gustoća $C$ jednaka je gustoći $k * C$”. Zaključak: smijemo raditi s bilo kojim reprezentantom točke i normalizirati tek pri ispisu. (Nazivnik $4Z^2$ je invertibilan jer je $M$ prost i $Z \ne 0$ za pozitivno stanje.)</p>
<h3>3. Combine je oduzimanje na krivulji</h3>
<p>Pročitajmo pseudokod <code>combine</code> u novim koordinatama. Neka su $P_0 = (X_0 : Y_0 : Z_0)$, $P_1 = (X_1 : Y_1 : Z_1)$.</p>
<ul>
<li>$L_1 = 0$: vraća $C_0$, tj. $P_0$.</li>
<li>$L_0 = 0$: vraća $(L_1, I_1, A_1)$ — zamjena $A \leftrightarrow I$ ostavlja $X$ i $Z$, a mijenja predznak $Y$: to je $-P_1$ (negacija na krivulji je $(X : -Y : Z)$).</li>
<li>Inače računa $B_0 = X_0 Z_1$, $B_1 = X_1 Z_0$ (usporedba $x$-koordinata $X_0/Z_0$ i $X_1/Z_1$ bez dijeljenja) i $C_0 = Y_0 Z_1$, $C_1 = (I_1 - A_1) Z_0 = -Y_1 Z_0$ — dakle $y$-koordinatu <em>negirane</em> točke $-P_1$.
  <ul>
  <li>$B_0 = B_1$ i $C_0 + C_1 = 0$, tj. $Y_0/Z_0 = Y_1/Z_1$: točke su jednake, rezultat $C(0, 3, -3) = (0 : 6 : 0) = O$. To je $P_0 - P_0 = O$.</li>
  <li>$B_0 = B_1$, $C_0 + C_1 \ne 0$: $-P_1 = P_0$, formula s $B = 3X_0^2 + E Z_0^2$ i $C = 2 Y_0 Z_0$ (nagib tangente $\lambda = (3x^2 + E)/(2y)$) je <em>udvostručenje</em> $2P_0 = P_0 + (-P_1)$.</li>
  <li>$B_0 \ne B_1$: $B = B_0 - B_1$, $C = C_0 - C_1 = Y_0 Z_1 + Y_1 Z_0$ su brojnik i nazivnik nagiba sekante kroz $P_0$ i $-P_1$; formule $E' = C^2 D - B^2 (B_0 + B_1)$, $X_2 = B \cdot E'$, $Y_2 = C(B_0 B^2 - E') - C_0 B^3$, $Z_2 = B^3 D$ (s $D = Z_0 Z_1$) upravo su standardne projektivne formule zbrajanja $P_0 + (-P_1)$ — svaka koordinata pomnožena istim skalarom, što ne smeta.</li>
  </ul></li>
</ul>
<p>Rezultat se vraća kao $(L_2, A_2, I_2) = (2Z_2, X_2 + Y_2, X_2 - Y_2)$, što je reprezentant $(2X_2 : 2Y_2 : 2Z_2)$ iste točke. <strong>Zaključak: $\mathrm{Combine}(C_0, C_1) = P_0 - P_1$ u grupi krivulje.</strong> Sad su službena svojstva očita: $-C$ je negacija, $C_0 + C_1 := \mathrm{Combine}(C_0, -C_1) = P_0 + P_1$ je grupno zbrajanje (asocijativno i komutativno), $e = O$ je neutralni element, $C + (-C) = O$. Skalari $k$ u tim svojstvima samo su različiti reprezentanti iste točke.</p>
<h3>4. Lijevo asocirani Combine</h3>
<p>Po definiciji $\mathrm{Combine}(C_l, \dots, C_{r-1}) = (\cdots((P_l - P_{l+1}) - P_{l+2}) \cdots) - P_{r-1}$. U komutativnoj grupi je to</p>
<p>$$P_l - (P_{l+1} + P_{l+2} + \dots + P_{r-1}).$$</p>
<p>Prividna nekomutativnost i neasocijativnost operacije nestaju: potreban nam je zbroj točaka na intervalu $[l+1, r)$ i jedno oduzimanje.</p>
<h3>5. Algoritam</h3>
<ol>
<li>Ćeliju pretvori u točku: $L = 0 \mapsto O$, inače $(A + I \bmod M,\ A - I \bmod M,\ L)$.</li>
<li>Implementiraj $\mathrm{add}(P, Q)$ u projektivnim koordinatama (bez inverza): slučajevi $P = O$, $Q = O$, $x_P = x_Q$ s $y_P = -y_Q$ ($\Rightarrow O$), $x_P = x_Q$ s $y_P = y_Q$ (udvostručenje), opći slučaj. Negacija $(X : -Y : Z)$.</li>
<li>Segmentno stablo nad $\mathrm{add}$ s neutralnim $O$: točkovna promjena mijenja list i ponovno računa $O(\log N)$ predaka; upit vraća $S = P_{l+1} + \dots + P_{r-1}$ (za $r = l + 1$ je $S = O$).</li>
<li>$R = \mathrm{add}(P_l, -S)$. Ako je $Z_R = 0$, ispiši $-1$; inače $(X_R^2 - Y_R^2) \cdot (4 Z_R^2)^{M-2} \bmod M$.</li>
</ol>
<p><strong>Ispravnost</strong>: segmentno stablo vraća reprezentant točke $S$ (asocijativnost grupe), a gustoća ovisi samo o točki $R$. <strong>Složenost</strong>: $O((N + Q) \log N)$ zbrajanja, svako s dvadesetak modularnih množenja; za $N = Q = 10^5$ oko $0.2$ s.</p>
<h3>6. Primjer</h3>
<p>$M = 998244353$, $E = 1$, $V = 2$. $C_0 = C(2, M-1, 3)$: $X = 2$, $Y = -4$, $Z = 2$ — afina točka $(1, -2)$; provjera: $(-2)^2 = 4 = 1 + 1 + 2$. $C_1 = C(4, M-2, 6)$: $X = 4$, $Y = -8$, $Z = 4$ — <em>ista</em> točka $(1, -2)$. $C_2 = C(4, 929561374, 68682991)$ je afina točka $(3, 464780684)$.</p>
<ul>
<li>Upit <code>2 0 2</code>: $P_0 - P_1 = O$ $\Rightarrow$ $-1$, kao u službenom izlazu.</li>
<li>Upit <code>2 0 3</code>: $P_0 - (P_1 + P_2) = -P_2$, gustoća jednaka gustoći $C_2$: $929561374 \cdot 68682991 \cdot 16^{-1} \equiv 748683259$ — drugi redak službenog izlaza.</li>
<li>Upit <code>2 1 3</code>: $P_1 - P_2$, opći slučaj sekante; rezultat $156877648$.</li>
</ul>
<h3>7. Zamke</h3>
<ul>
<li>Umnošci dvaju brojeva $< 10^9$ stanu u 64 bita, ali $3 \cdot X^2$ ili $B_0 + B_1$ prije redukcije treba držati u <code>long long</code> i reducirati; razlike normaliziraj na $[0, M)$.</li>
<li>Ne zaboravi granu „jednake točke” (rezultat $O$) — dogodi se i za točku reda $2$ ($Y = 0$), gdje bi formula udvostručenja dala $Z = 0$ s neispravnim $X, Y$.</li>
<li>Ispis $-1$ samo kad je $Z_R = 0$; točka s $X_R^2 = Y_R^2$ ima gustoću $0$, što je valjan odgovor $0$, ne $-1$.</li>
<li>Upit $r = l + 1$ (jedna ćelija) vraća gustoću same ćelije $C_l$.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih testova (slučajan prost $M$, $N \le 7$, $Q \le 10$; ćelije su slučajno skalirani reprezentanti iz malog bazena točaka krivulje, njihove negacije i nul-stanja, pa se često pogađaju grane „jednake točke” i „udvostručenje”) protiv brute forcea koji doslovno prepisuje pseudokod <code>valid</code>/<code>combine</code> i lijevo asocirano spaja $C_l, \dots, C_{r-1}$; 3 velika testa s $N = Q = 10^5$ (najviše 0.18 s).''',
},
]
