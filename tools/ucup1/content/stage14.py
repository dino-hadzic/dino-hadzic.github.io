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
        r'''<p>Traži se poligon na kojem flipturn postupak može trajati $\Omega(N^2)$ koraka. Takve su konstrukcije poznate iz literature (Biedl, „Polygons Needing Many Flipturns”).</p>''',
        r'''<p>Ideja: jedna „strma” skupina stranica sa strogo rastućim nagibima i jedna skupina vodoravnih stranica koje se jedna po jedna „spuštaju” kroz cijelu strmu skupinu — svako spuštanje kroz $N/2$ stranica traje $N/2$ koraka.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Flipturn puta između dva „džepa” ljuske mijenja samo redoslijed (i smjer) stranica; multiskup nagiba usmjerenih stranica je invarijanta. Da bi postupak dugo trajao, treba puno džepova kroz koje jedna stranica prolazi jedna po jedna.</p>'''),
        ('Konstrukcija', r'''<p>Neka je $N$ djeljiv s $4$, $d_i$ vektor smjera $i$-te stranice u pozitivnom smjeru. Skupina 1: za $0 \le i \le N/2 - 2$, $d_i = (i + 1, (i + 1)^2)$. Skupina 2: za neparne $i$ s $N/2 - 1 \le i \le N - 2$, $d_i = (1, 0)$. Skupina 3: za parne takve $i$, $d_i = (N/2, (N/2)^2)$. Posljednja stranica zatvara poligon.</p>'''),
        ('Redoslijed operacija', r'''<p>Prvu stranicu skupine 2 „spusti” flipturnima kroz svih $N/2 - 1$ stranica skupine 1, a zatim redom svaku od preostalih $N/4 - 1$ stranica skupine 2. Duljina niza je $N^2/8 - 1$, što je za $N = 1000$ jednako $124\,999 \ge 120\,000$. Provjeri simulacijom da su svi izabrani putovi valjani (oba kraja na ljusci, ostatak strogo unutra) i da su koordinate u dopuštenom rasponu.</p>'''),
        ('Složenost', r'''<p>Simulacija s $O(N)$ po koraku: $O(N^3) \approx 10^8$ operacija, unutar 10 s.</p>'''),
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
        ('Opažanje: oblik', r'''<p>Flipturn zarotira dio ruba za $\pi$: svaka stranica na putu zadržava nagib i duljinu, mijenja se samo redoslijed stranica (i orijentacija dijela puta se uskladi tako da poligon ostane pozitivno orijentiran). Površina strogo raste, pa postupak završava. Konačni konveksni poligon ima iste usmjerene stranice, sortirane po kutu — oblik je fiksiran.</p>'''),
        ('Redukcija: invarijanta za položaj', r'''<p>Promotri vodoravnu trapezoidnu dekompoziciju vanjskog područja poligona. Svako konačno područje označi kao „gore” ili „dolje” ovisno o smjeru u kojem se iz njega dolazi do beskonačnog područja. Neka je $U$ zbroj visina „gore” područja, a $Y$ najveća $y$-koordinata poligona. Tada je $U + Y$ invarijanta postupka. Za konačni konveksni poligon je $U = 0$, pa je $Y_{\text{final}} = U_0 + Y_0$.</p>'''),
        ('Algoritam', r'''<p>Izračunaj $U_0$ za ulazni poligon: vodoravni sweep po događajima vrhova (sortiranje), s uravnoteženom strukturom za aktivne stranice — $O(N \log N)$. Isto napravi s okomitom dekompozicijom da dobiješ najveću $x$-koordinatu. Zatim složi stranice po kutu; s poznatim maksimalnim $x$ i $y$ položaj konveksnog poligona je jednoznačan. Spoji kolinearne uzastopne stranice i rotiraj ispis na leksikografski najmanji vrh.</p>'''),
        ('Složenost', r'''<p>$O(N \log N)$. Referenca: „Flipturning Polygons”.</p>'''),
    ],
    'solution': r'''
<p>Dokazivanje tvrdnji iz teksta zadatka daje i algoritam.</p>
<p>Konačni „oblik” je fiksiran, jer površina uvijek raste, a multiskup nagiba usmjerenih stranica se ne mijenja.</p>
<p>Za položaj promotrimo vodoravnu trapezoidnu dekompoziciju vanjskog područja poligona. Svako konačno područje označimo s „gore” ili „dolje”, ovisno o smjeru u kojem se treba kretati da bi se došlo do nekog beskonačnog područja. Neka je $U$ zbroj visina „gore” područja, a $Y$ najveća $y$-koordinata. Tada je $U + Y$ invarijantno tijekom operacija. Budući da je $U = 0$ za konačni konveksni poligon, taj zbroj odmah daje najveću $y$-koordinatu konačnog poligona.</p>
<p>Isti postupak s okomitom trapezoidnom dekompozicijom daje najveću $x$-koordinatu.</p>
<p>Referentni rad: „Flipturning Polygons”.</p>
''',
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
        ('Opažanje', r'''<p>Redoslijed poteza ne utječe na rezultat, a dva ista poteza se poništavaju — stanje ćelije je XOR početnog stanja i indikatora triju linija koje kroz nju prolaze. Tražimo podskup od $3N$ linija.</p>'''),
        ('Redukcija', r'''<p>Ćelija leži na točno jednoj liniji svakog smjera. Ako su izbori za dvije od tri linije kroz ćeliju poznati, treća je forsirana. Fiksiranjem dvaju najduljih redaka u jednom smjeru i najduljeg u drugom (najviše $2^3 = 8$ kombinacija) sve ostale linije određene su jedinstveno: krećući od ruba, svaka nova linija prolazi kroz ćeliju čije su druge dvije linije već odlučene.</p>'''),
        ('Algoritam i složenost', r'''<p>Za svaku od 8 kombinacija propagiraj odluke i na kraju provjeri sve $N(N+1)/2$ ćelija. $O(N^2)$.</p>'''),
    ],
    'solution': r'''
<ul>
<li>Operacije komutiraju: redoslijed nije bitan.</li>
<li>Dvije iste operacije se poništavaju.</li>
<li>Fiksiranje dvaju najduljih redaka u jednom smjeru i najduljeg retka u drugom smjeru jednoznačno određuje sve ostale.</li>
</ul>
<p>Vremenska složenost: $O(N^2)$.</p>
''',
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
        ('Opažanje', r'''<p>Točka je izvan konveksnog skupa ako i samo ako je od njega odvaja pravac. Za skup kružnica to znači: postoji poluravnina s rubom kroz ishodište koja sadrži sve kružnice.</p>'''),
        ('Redukcija', r'''<p>Ako neka kružnica sadrži ishodište ($x_i^2 + y_i^2 \le r_i^2$), odgovor je <code>Yes</code>. Inače svaka kružnica „pokriva” kutni interval iz ishodišta između svoje dvije tangente: središnji kut $\theta_i = \operatorname{atan2}(y_i, x_i)$, poluširina $\alpha_i = \arcsin(r_i / \sqrt{x_i^2 + y_i^2})$. Sve kružnice leže u nekoj poluravnini kroz ishodište ako i samo ako se svih $2N$ zraka (kutovi $\theta_i \pm \alpha_i$) nalazi unutar kutnog intervala duljine $\le \pi$.</p>'''),
        ('Algoritam i složenost', r'''<p>Sortiraj $2N$ kutova, izračunaj najveću kružnu prazninu; ako je $\ge \pi$, ispiši <code>No</code>, inače <code>Yes</code>. Zbog uvjeta da je ishodište barem $1$ udaljeno od ruba ljuske, računanje u <code>double</code> je sigurno. $O(N \log N)$ zbog sortiranja. Alternativa: konveksna ljuska diskova u $O(N \log N)$ (Rappaport) i provjera da je ishodište lijevo od svakog ruba.</p>'''),
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
        ('Opažanje', r'''<p>$G$ je trokut $\{a, b, c\}$ s repom $c - d - e - f$. Kandidat se broji jednom po svakoj injektivnoj ulozi vrhova modulo automorfizmi (samo zamjena $a \leftrightarrow b$). Naivno: za svaki vrh $c$ pomnoži broj trokuta kroz $c$ s brojem šetnji duljine $3$ iz $c$, pa oduzmi šetnje koje ponovno posjete trokut ili same sebe.</p>'''),
        ('Redukcija: niz pomoćnih veličina', r'''<p>Modelno rješenje redom računa: (1) za svaki vrh $u$ broj trokuta kroz $u$; (2) za svaki neusmjereni brid broj trokuta kroz njega; (3) za svaki usmjereni brid $(u, v)$ broj podgrafa s $4$ vrha $0,1,2,3$ i $5$ bridova $(0,1),(1,2),(2,3),(3,0),(1,3)$ u kojima $u, v$ odgovaraju $0, 1$; (4) za svaki usmjereni brid $(u, v)$ broj podgrafa s $5$ vrhova i $6$ bridova $(0,1),(1,2),(2,3),(3,0),(1,4),(4,2)$ u kojima $u, v$ odgovaraju $0, 1$; (5) za svaki vrh $u$ broj kandidata s repom duljine $1, 2, 3$ kojima je $u$ kraj repa.</p>'''),
        ('Algoritam i složenost', r'''<p>Trokuti kroz vrhove/bridove: orijentacija po stupnju, $O(M\sqrt{M})$. Veličine (3) i (4) opisuju točno one konfiguracije u kojima se rep „zatvori” natrag u trokut i moraju se oduzeti pri prelasku s repa duljine $k$ na $k+1$ u koraku (5). Ukupno $O(N + M\sqrt{M})$.</p>'''),
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
        r'''<p>Ostaje provjeriti ima li dobivena formula $F$ <em>točno</em> $N$ rješenja. Nabroji rješenja 2-SAT-a implikacijskim grafom: obradi literale u topološkom poretku SCC-ova, grananje na neodređenima, propagacija bitsetima — svaki list rekurzije je jedno rješenje, pa prekini kad ih prebrojiš više od $N$.</p>''',
    ],
    'coach': [
        ('Opažanje', r'''<p>Literal $L$ ima varijablu $V(L)$ i vrijednost $E(L)$. Reci da $L$ <em>implicira</em> $M$ ako u svakom zadanom rješenju u kojem je $V(L) = E(L)$ vrijedi i $V(M) = E(M)$. Za svaki takav par dodaj klauzulu $\lnot L \lor M$ (jedan od 4 tipa); to se provjerava bitsetima po stupcima ulaza u $O(M^2 N / w)$.</p>'''),
        ('Redukcija', r'''<p>Neka je $F$ formula sa svim tim klauzulama. Ako tražena formula postoji, sve su njezine klauzule u $F$ (svaka klauzula formule je implikacija koja vrijedi na svim rješenjima), a dodane klauzule ne isključuju nijedno zadano rješenje. Dakle: formula postoji ako i samo ako je skup rješenja $F$ jednak ulazu — dovoljno je provjeriti da $F$ nema drugih rješenja, tj. da ih ima točno $N$.</p>'''),
        ('Algoritam: nabrajanje rješenja 2-SAT-a', r'''<p>(1) Implikacijski graf: za $L \lor M$ bridovi $\lnot L \to M$, $\lnot M \to L$. (2) Ako su $L$ i $\lnot L$ u istom SCC-u, nema rješenja. (3) Pridruživanje je valjano ako nema puta iz istinitog u lažni literal. (4) Prolazi literale u topološkom poretku; ako je neodređen, grananje: postavi ga na istinu odnosno laž i rekurzivno nastavi. (5) Postavljanje na istinu forsira istinu svih dosežnih literala (bitset dosežnosti). Svaka grana vodi do barem jednog rješenja, pa prebroji rješenja i prekini ako premaši $N$.</p>'''),
        ('Složenost', r'''<p>$O(N \cdot M^2 / w)$. Broj klauzula je $\le 2M^2$ (najviše $4$ po paru varijabli, ali dovoljno je ispisati po jednu klauzulu za svaku implikaciju — $\le (2M)^2 / 2$).</p>'''),
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
        ('Opažanje', r'''<p>U generičkom smještaju svaka šipka nameće jedno ograničenje koje je ili neovisno (smanjuje stupanj slobode za $1$) ili redundantno ($0$). Neovisni skupovi šipki čine matroid krutosti; stupanj slobode je $2N - r$, gdje je $r$ rang odabranog skupa šipki. Minimizirati stupanj slobode $\Leftrightarrow$ maksimizirati rang uz uvjet različitih boja.</p>'''),
        ('Redukcija: presjek matroida', r'''<p>Skup šipki s različitim bojama je nezavisan skup particijskog matroida. Traži se najveći skup nezavisan u oba matroida — algoritam presjeka matroida (augmentirajući putovi u grafu razmjene), s $O(r)$ augmentacija i $O(M^2)$ poziva orakula po augmentaciji u naivnoj izvedbi.</p>'''),
        ('Algoritam: orakul krutosti', r'''<p>Lamanov teorem: skup bridova je nezavisan u matroidu krutosti ravnine ako i samo ako svaki podgraf $S$ zadovoljava $|E(S)| \le 2|V(S)| - 3$. Provjera igrom kamenčićima: održavaj $2$-prema-$1$ sparivanje (svaki brid usmjeren prema jednom kraju, svaki vrh prima najviše $2$ brida); novi brid $e$ je nezavisan ako i samo ako se sparivanje može proširiti kad se $e$ učetverostruči (4 kopije). To je nekoliko DFS-ova po usmjerenom grafu — $O(N)$ do $O(N + M)$ po upitu.</p>'''),
        ('Složenost', r'''<p>$O(N^2 \cdot M)$ prema službenom rješenju. Odgovor: $2N - |\text{najveći zajednički nezavisan skup}|$.</p>'''),
    ],
    'solution': r'''
<ul>
<li>Svaka šipka doprinosi stupnju slobode s $-1$ ili $0$, a šipke koje doprinose $-1$ čine matroid (matroid krutosti).</li>
<li>Skup bridova je nezavisan ako i samo ako svaki podgraf $S$ zadovoljava $2|V| - 3 \ge |E|$ (Lamanov teorem).</li>
<li>Orakul nezavisnosti gradi se provjerom postoji li i dalje $2$-prema-$1$ sparivanje između vrhova i bridova nakon učetverostručenja novog brida (algoritam igre kamenčićima, pebble game).</li>
<li>Algoritam presjeka matroida + orakul krutosti igrom kamenčićima daje rješenje složenosti $O(N^2 \cdot M)$.</li>
</ul>
''',
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
        ('Opažanje', r'''<p>Gustoća $C(L, A, I)$ jednaka je gustoći $k * C(L, A, I)$ za svaki cijeli $0 < k < M$. Dakle ćelije smijemo promatrati do na skalar.</p>'''),
        ('Redukcija: algebarska struktura', r'''<p>Definiraj $-C(L, A, I) = C(L, I, A)$, $C_0 + C_1 = \mathrm{Combine}(C_0, -C_1)$ i $e = C(0, 3, -3)$ (valjana ćelija). Pokazuje se: (1) $k_0 C_0 + k_1 C_1 = k_2 (C_0 + C_1)$ za neki $0 < k_2 < M$; (2) $C_0 + (C_1 + C_2) = k\,((C_0 + C_1) + C_2)$; (3) $e + C = k_0 (C + e) = k_1 C$; (4) $C + (-C) = k e$. Dakle $+$ je asocijativna i ima neutralni element do na skalar.</p>'''),
        ('Algoritam', r'''<p>Traženi rezultat $(\cdots((C_l - C_{l+1}) - C_{l+2}) \cdots) - C_{r-1}$ jednak je $k * \big(C_l - (C_{l+1} + \dots + C_{r-1})\big)$ za neki $0 < k < M$, pa ima istu gustoću kao $C_l - (C_{l+1} + \dots + C_{r-1})$. Svojstvo (2) osigurava da segmentno stablo s operacijom $+$ vrati $C_{l+1} + \dots + C_{r-1}$ pomnoženo nekom nenul konstantom, a svojstvo (1) da oduzimanje od $C_l$ daje traženi rezultat do na nenul konstantu. Točkovna promjena je obično ažuriranje lista.</p>'''),
        ('Složenost', r'''<p>$O(N + Q \log N)$ za izgradnju i upite segmentnog stabla.</p>'''),
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
},
]
