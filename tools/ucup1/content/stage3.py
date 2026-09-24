# -*- coding: utf-8 -*-
STAGE = {
    'no': 3,
    'name': 'Stage 3: Poland',
    'source_name': 'February 11-12, 2023',
    'no_editorial': True,
    'source_html': r'''
<p>Zadaci potječu s natjecanja AMPPZ 2022 (Akademickie Mistrzostwa Polski w Programowaniu Zespołowym — The 2022 ICPC Polish Collegiate Programming Contest, Kraków, 30. 10. 2022.). Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1103&amp;r=1">engleskim tekstovima zadataka</a>. Organizatori nisu objavili službena rješenja. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1103">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Aliases', 'title_hr': 'Nadimci', 'slug': 'A_aliases',
    'tl': '42 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Za $n$ natjecatelja treba napraviti korisnička imena (nadimke) po istom pravilu: prvih $a$ slova imena, zatim prvih $b$ slova prezimena i na kraju $c$ znamenaka po vlastitom izboru. Ako ime ima manje od $a$ slova (ili prezime manje od $b$), uzimaju se sva slova. Npr. za $a = b = c = 3$ James Bond može dobiti <code>jambon007</code>, a Lady Di <code>laddi123</code>.</p>
<p>Svi nadimci moraju biti međusobno različiti. Nađi nenegativne $a, b, c$ (ne sve tri nule) za koje je to moguće i za koje je $a + b + c$ najmanje moguće.</p>
<h3>Ulaz</h3>
<p>$z \le 6$ testova. U svakom $n \le 200\,000$ parova ime prezime (mala engleska slova); ukupna duljina svih imena i prezimena u testu je najviše $1\,500\,000$. Dvoje sudionika može imati isto ime i prezime (i tada moraju dobiti različite nadimke).</p>
<h3>Izlaz</h3>
<p>Za svaki test tri broja $a$, $b$, $c$ s najmanjim zbrojem. Ako ima više rješenja, ispiši bilo koje.</p>
<h3>Primjer</h3>
<p>Za $11$ sudionika (sven eriksson, erik svensson, sven svensson, erik eriksson, bjorn eriksson, bjorn svensson, bjorn bjornsson, erik bjornsson, sven bjornsson, thor odinsson, odin thorsson) odgovor je <code>1 1 0</code> — inicijali su svima različiti. Točan je i odgovor <code>1 0 1</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Bars', 'title_hr': 'Barovi', 'slug': 'B_bars',
    'tl': '6 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Kuće $n$ stanovnika ($1..n$) leže redom uz jednu ravnu cestu. Svaki stanovnik želi otvoriti bar; $i$-ti obećava porez od $p_i$ zlatnika po svakom gostu. Ti odabireš neprazan podskup stanovnika kojima daješ dozvolu.</p>
<p>Svaki stanovnik (imao bar ili ne) postaje gost dvaju barova: najbližeg <em>strogo lijevo</em> i najbližeg <em>strogo desno</em> od svoje kuće (ako postoje; vlastiti bar se ne računa). Svaki otvoreni bar donosi $p_i$ zlatnika po gostu. Npr. za $n = 5$ i otvorene barove $3$ i $5$, treći ima $4$ gosta, a peti $2$: prihod je $4 p_3 + 2 p_5$.</p>
<p>Odredi najveći mogući ukupni prihod.</p>
<h3>Ulaz</h3>
<p>$z \le 10\,000$ testova; $2 \le n \le 500\,000$, $1 \le p_i \le 10^9$; $\sum n \le 3 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najveći ukupni prihod.</p>
<h3>Primjer</h3>
<p>$p = (5, 2, 2, 6)$: otvori prvi i posljednji bar, svaki ima $3$ gosta, prihod $3 \cdot 5 + 3 \cdot 6 = 33$. $p = (1, 5, 4, 4, 1)$: otvori sve osim trećeg, prihod $1 \cdot 1 + 3 \cdot 5 + 3 \cdot 4 + 1 \cdot 1 = 29$ (svi otvoreni dali bi samo $28$).</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Ctrl+C Ctrl+V', 'title_hr': 'Ctrl+C Ctrl+V', 'slug': 'C_ctrl_c_ctrl_v',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je string $s$ malih engleskih slova (Anijina autobiografija). Odredi najmanji broj znakova koje treba promijeniti da $s$ više ne sadrži riječ <code>ania</code> kao podniz uzastopnih znakova.</p>
<h3>Ulaz</h3>
<p>$z \le 10\,000$ testova; svaki je jedan string duljine $l \le 10^6$; $\sum l \le 5\,000\,000$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najmanji broj promjena.</p>
<h3>Primjer</h3>
<p><code>aniasieurodzilaapotemnicsieniedzialo</code> $\to 1$; <code>nicciekawegouanianiagnieszkianialicji</code> $\to 2$; <code>jeszczekrotszaautobiografiaani</code> $\to 0$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Dazzling Mountain', 'title_hr': 'Blistava planina', 'slug': 'D_dazzling_mountain',
    'tl': '10 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Na planini je $n$ planinarskih domova povezanih s $n - 1$ stazom u stablo s korijenom u domu $1$ (vrh planine). Domovi s točno jednom stazom (osim doma $1$) nalaze se u podnožju. Tradicionalni uspon počinje u nekom domu u podnožju i završava na vrhu.</p>
<p>Iz doma $x$ vide se točno domovi čiji put do $1$ prolazi kroz $x$ (uključujući $x$), tj. veličina podstabla od $x$. Uprava želi izgraditi vidikovac u svakom domu iz kojeg se vidi točno $d$ domova.</p>
<p>Nađi sve vrijednosti $d$ za koje će svaki planinar, bez obzira na to iz kojeg doma u podnožju kreće, na putu do vrha proći kroz barem jedan vidikovac.</p>
<h3>Ulaz</h3>
<p>$z \le 10\,000$ testova; $2 \le n \le 1\,000\,000$, zatim $n - 1$ bridova $a_i, b_i$; $\sum n \le 3 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test dva retka: broj traženih vrijednosti $d$, pa te vrijednosti uzlazno.</p>
<h3>Primjer</h3>
<p>Stablo s $9$ vrhova i bridovima $1\text{-}2, 2\text{-}3, 3\text{-}4, 3\text{-}5, 2\text{-}6, 6\text{-}7, 7\text{-}8, 7\text{-}9$: odgovor su $4$ vrijednosti, $1\ 3\ 8\ 9$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Euclidean Algorithm', 'title_hr': 'Euklidov algoritam', 'slug': 'E_euclidean_algorithm',
    'tl': '30 s', 'ml': '8 MiB',
    'statement': r'''
<p>„Algoritam” za $\gcd(x, y)$: na ploči su brojevi $x$ i $y$. U jednom koraku odaberi bilo koja dva već napisana broja $a$ i $b$ i napiši $c = 2a - b$, uz uvjet $c \gt 0$. Rezultat za par $(x, y)$ je najmanji broj koji se može pojaviti na ploči nakon proizvoljno mnogo (možda nula) koraka.</p>
<p>Za $(10, 14)$ algoritam daje $2$ ($2 \cdot 10 - 14 = 6$, $2 \cdot 6 - 10 = 2$), što je točno; za $(10, 16)$ daje $4$, a točan je $\gcd$ jednak $2$.</p>
<p>Za dani $n$ odredi broj parova $(x, y)$, $1 \le x \lt y \le n$, za koje algoritam vraća točno $\gcd(x, y)$. (Ako je $\gcd(x, y) = x$, algoritam radi ispravno jer je $x$ već na ploči.)</p>
<h3>Ulaz</h3>
<p>$z \ge 1$ testova, svaki je jedan broj $n \ge 2$. Ulaz pripada jednoj od tri skupine: $z \le 3000, n \le 10^6$; $z = 30, n \le 10^9$; $z = 3, n \le 10^{11}$. <strong>Memorijsko ograničenje je samo 8 MB.</strong></p>
<h3>Izlaz</h3>
<p>Za svaki test broj traženih parova.</p>
<h3>Primjer</h3>
<p>$n = 2 \to 1$; $n = 5 \to 9$; $n = 14 \to 62$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Flower Garden', 'title_hr': 'Cvjetni vrt', 'slug': 'F_flower_garden',
    'tl': '30 s', 'ml': '1024 MiB',
    'statement': r'''
<p>U red od $3n$ gredica sade se ljubičice (F) i ruže (R). Kraljevski dekret ima $q$ uvjeta; $i$-ti glasi: <em>barem jedno</em> od sljedećeg vrijedi — sve gredice $a_i..b_i$ su ruže, ili sve gredice $c_i..d_i$ su ljubičice. Na raspolaganju je $2n$ ruža i $2n$ ljubičica (pa nijedne vrste ne smije biti više od $2n$).</p>
<p>Nađi raspored koji zadovoljava sve uvjete ili utvrdi da ne postoji.</p>
<h3>Ulaz</h3>
<p>$z \le 10^5$ testova; $1 \le n \le 33\,333$, $1 \le q \le 10^5$, zatim $q$ četvorki $a_i \le b_i$, $c_i \le d_i$ iz $[1, 3n]$; $\sum n \le 333\,333$, $\sum q \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test <code>TAK</code> i u sljedećem retku string duljine $3n$ od znakova <code>F</code>/<code>R</code> (najviše $2n$ svakog), ili <code>NIE</code>.</p>
<h3>Primjer</h3>
<p>$n = 1$, uvjeti $(1,1,2,2), (1,2,3,3), (1,1,3,3)$: <code>TAK</code>, <code>RFF</code>. $n = 1$, uvjeti $(1,1,2,2), (2,2,3,3), (3,3,1,1)$: <code>NIE</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Great Chase', 'title_hr': 'Velika potjera', 'slug': 'G_great_chase',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Na brojevnom pravcu razbojnik stoji u $0$, a $n$ policajaca s obje njegove strane (barem jedan na svakoj). Svaki policajac trči prema razbojniku svojom brzinom $v_i$; razbojnik bježi brzinom $v$ većom od svih $v_i$, početno udesno. Kad god razbojnik dođe do prvog policajca koji mu trči ususret, trenutno se okreće i trči u suprotnom smjeru. To se ponavlja dok se dva policajca iz suprotnih smjerova ne sretnu s razbojnikom između njih.</p>
<p>Odredi ukupni put koji razbojnik prijeđe.</p>
<h3>Ulaz</h3>
<p>$z \le 10\,000$ testova; $2 \le n \le 400\,000$, $1 \lt v \le 10^6$, zatim $n$ parova $p_i$ ($|p_i| \le 10^{12}$, $p_i \ne 0$) i $v_i$ ($1 \le v_i \lt v$); $\sum n \le 2 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test realan broj (decimalni zapis, ne znanstveni, najviše $20$ decimala); prihvaća se relativna ili apsolutna greška do $10^{-8}$, tj. $\frac{|a - b|}{\max(1, b)} \le 10^{-8}$.</p>
<h3>Primjer</h3>
<p>$v = 9$, policajci $(10, 2), (-7, 2), (-6, 1), (7, 1)$: $38.25$. $v = 8$, policajci $(-1, 7), (1, 6)$: $1.23076923$. $v = 3$, policajci $(-10^{12}, 1), (10^{12}, 1)$: $3\,000\,000\,000\,000$ (zbog relativne greške prihvaća se svaki odgovor unutar $30\,000$).</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Hyperloop', 'title_hr': 'Hyperloop', 'slug': 'H_hyperloop',
    'tl': '45 s', 'ml': '64 MiB',
    'statement': r'''
<p>Na obali otoka leži $n$ gradova $1, 2, \dots, n$ redom. Trajekti voze između $i$ i $i+1$ te između $n$ i $1$; uz to postoje Hyperloop veze između nekih parova nesusjednih gradova. Sve su veze dvosmjerne s trajanjem $d_i$ i tretiraju se jednako.</p>
<p>Traži se najkraći put od $1$ do $n$. Među najkraćim putovima preferiraju se oni s <em>najduljim</em> pojedinačnim vezama: za svaki put ispiši duljine njegovih veza (s ponavljanjima), sortiraj nerastuće i odaberi leksikografski najveći niz. (Nizovi imaju isti zbroj, pa nijedan nije prefiks drugoga.)</p>
<p><strong>Memorijsko ograničenje je samo 64 MB.</strong></p>
<h3>Ulaz</h3>
<p>$z \le 600$ testova; $3 \le n \le 100\,000$, $n \le m \le 300\,000$, zatim $m$ veza $u_i, v_i, d_i$ ($1 \le d_i \le 50\,000$), među kojima su sigurno $(1,2), (2,3), \dots, (n,1)$; između para gradova najviše jedna veza. $\sum n \le 400\,000$, $\sum m \le 800\,000$.</p>
<h3>Izlaz</h3>
<p>Za svaki test broj gradova $k$ na optimalnom putu, pa $k$ različitih gradova redom od $1$ do $n$. Ako ima više optimalnih putova, bilo koji.</p>
<h3>Primjer</h3>
<p>$n = 4$, veze $(1,2,1), (1,3,2), (2,3,1), (2,4,2), (3,4,1), (1,4,4)$: najkraća udaljenost je $3$, postižu je $1 \to 2 \to 4$, $1 \to 3 \to 4$ i $1 \to 2 \to 3 \to 4$; prva dva su bolja jer je $(2,1) \gt (1,1,1)$. Odgovor npr. <code>3</code>, <code>1 2 4</code>. U drugom primjeru ($n = 6$, $m = 11$) odgovor je <code>5</code>, <code>1 2 5 3 6</code> jer je $(9, 8, 2, 1) \gt (9, 5, 3, 2, 1)$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Investors', 'title_hr': 'Investitori', 'slug': 'I_investors',
    'tl': '8 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Financijski rezultati su niz $a_1, \dots, a_n$. Jedna operacija: odaberi neprazan uzastopni interval niza i sve njegove članove uvećaj za isti pozitivan cijeli broj (u različitim operacijama različiti brojevi). Smiješ izvesti najviše $k$ operacija.</p>
<p>Minimiziraj broj inverzija (parova $i \lt j$ s $a_i \gt a_j$) u konačnom nizu.</p>
<h3>Ulaz</h3>
<p>$z \le 400$ testova; $1 \le n \le 6000$, $0 \le k \le n$, $0 \le a_i \le 10^9$; $\sum n \le 6000$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najmanji mogući broj inverzija.</p>
<h3>Primjer</h3>
<p>$a = (4, 5, 6, 2, 2, 1)$: za $k = 1$ odgovor je $2$, za $k = 2$ odgovor je $0$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Job for a Hobbit', 'title_hr': 'Posao za hobita', 'slug': 'J_job_for_a_hobbit',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>U redu je $n$ stupova, na svakom točno $k$ obojenih prstenova (boje su brojevi). Dodana su dva prazna stupa, $0$ i $n+1$, pa ih je ukupno $n + 2$. U jednom potezu hobit skida gornji prsten s nekog stupa i stavlja ga na vrh <em>susjednog</em> stupa; nijedan stup ne smije imati više od $k$ prstenova.</p>
<p>Cilj: svaki stup jednobojan (ili prazan). Odredi je li moguće i, ako jest, ispiši plan od najviše $10^6$ poteza.</p>
<h3>Ulaz</h3>
<p>$z \le 25$ testova; $1 \le n \le 50$, $1 \le k \le 10$, zatim $n$ redaka s po $k$ brojeva $a_{i1}, \dots, a_{ik}$ ($0 \le a_{ij} \le 10^9$) — prstenovi $i$-tog stupa odozdo prema gore; $\sum n \le 50$.</p>
<h3>Izlaz</h3>
<p><code>TAK</code>, broj poteza $p \le 10^6$ i $p$ redaka $a_i\ b_i$ ($0 \le a_i, b_i \le n+1$, $|a_i - b_i| = 1$): premjesti gornji prsten sa stupa $a_i$ na stup $b_i$ (stup $a_i$ neprazan, $b_i$ ima manje od $k$ prstenova). Inače <code>NIE</code>. Bilo koji valjani plan se prihvaća.</p>
<h3>Primjer</h3>
<p>$n = 2$, $k = 2$, stupovi $(1, 2)$ i $(2, 1)$: <code>TAK</code>, $2$ poteza: <code>1 0</code>, <code>2 1</code>. $n = 1$, $k = 4$, stup $(1, 2, 3, 4)$: <code>NIE</code>.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Kooky Tic-Tac-Toe', 'title_hr': 'Otkačeni križić-kružić', 'slug': 'K_kooky_tic_tac_toe',
    'tl': '6 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Križić-kružić na ploči $n \times n$: igrači naizmjence stavljaju svoj znak (x ili o) na prazno polje; prvi potez može odigrati bilo koji igrač. Ako se nakon poteza pojavi $k$ istih znakova uzastopno u retku, stupcu, dijagonali ili antidijagonali, taj igrač pobjeđuje i igra završava. Ako nitko ne pobijedi i ploča je puna, igra je neriješena.</p>
<p>Dana je ploča s križićima, kružićima i praznim poljima. Postoji li ispravna igra (igrači ne moraju igrati optimalno, samo po pravilima) koja je <em>završila</em> upravo u ovoj poziciji?</p>
<h3>Ulaz</h3>
<p>$z \le 10\,000$ testova; $3 \le n \le 6$, $2 \le k \le n$, zatim $n$ redaka po $n$ znakova <code>.</code>, <code>x</code>, <code>o</code>.</p>
<h3>Izlaz</h3>
<p><code>TAK</code> i zatim redoslijed poteza — u $i$-tom retku $x_i\ y_i$ (redak od vrha, stupac od lijeva) polja popunjenog u $i$-tom potezu; inače <code>NIE</code>. Bilo koja valjana igra se prihvaća.</p>
<h3>Primjer</h3>
<p>Za $n = k = 3$ ploča <code>x.o / xxx / o.o</code> daje <code>TAK</code> (križić je pobijedio u posljednjem potezu). Ploča <code>xoo / oxx / xoo</code> s $k = 3$ je neriješena — <code>TAK</code>; ista ploča s $k = 2$ je <code>NIE</code> (netko bi pobijedio prije devetog poteza). <code>xox / .o. / xox</code>: <code>NIE</code> (križić je morao odigrati posljednji potez, a kružić je pobijedio). <code>xo. / ..x / xo.</code> s $k=2$: <code>NIE</code> (igra nije završena). <code>x.. / .x. / ..x</code>: <code>NIE</code> (tri križića, nijedan kružić).</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Line Replacements', 'title_hr': 'Zamjenske linije', 'slug': 'L_line_replacements',
    'tl': '15 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Tramvajska mreža je stablo s $n$ raskrižja i $n - 1$ pruga; na $p$ raskrižja nalaze se okretišta (svaki list je okretište, a mogu biti i drugdje). Byteasar je odabrao $k$ pruga i svake od sljedećih $k$ noći ukrast će jednu od njih.</p>
<p>Za svaki dan $j = 0, 1, \dots, k$ (nakon $j$ krađa) mora postojati mreža zamjenskih linija: svaka linija je jednostavan put koji počinje i završava u okretištima i vozi neki (pozitivan) broj vožnji na sat, ne prolazi ukradenim prugama, a za svaku neukradenu prugu $i$ ukupan broj vožnji svih linija kroz nju mora biti točno $c_i$.</p>
<p>Nađi redoslijed krađa za koji to vrijedi svaki dan, ili utvrdi da ne postoji (uključujući slučaj da već za $j = 0$ vrijednosti $c_i$ ne opisuju valjanu mrežu).</p>
<h3>Ulaz</h3>
<p>$z \le 15\,000$ testova; $2 \le p \le n \le 500\,000$; $p$ raskrižja s okretištima (uzlazno); $n - 1$ pruga $u_i, v_i, c_i$ ($1 \le c_i \le 10^9$), pruga $i$ je $i$-ta u ulazu; $k$ ($1 \le k \le n-1$) i $k$ različitih indeksa pruga uzlazno; $\sum n \le 2\,000\,000$.</p>
<h3>Izlaz</h3>
<p><code>TAK</code> i $k$ indeksa pruga u redoslijedu krađe (svaka od odabranih točno jednom; bilo koji valjani redoslijed), ili <code>NIE</code>.</p>
<h3>Primjer</h3>
<p>Stablo sa $7$ raskrižja, okretišta $1, 2, 3, 4, 6$, pruge $(7,1,3), (7,2,4), (7,3,4), (7,4,3), (5,3,1), (5,6,1)$. Krađa pruga $\{2, 3\}$: <code>TAK</code>, <code>2 3</code> (i <code>3 2</code> je točno). Krađa pruga $\{2, 3, 5, 6\}$: <code>NIE</code> — nakon krađe bilo koje od pruga $5$, $6$ drugu nije moguće ispravno opslužiti.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Minor Evil', 'title_hr': 'Manje zlo', 'slug': 'M_minor_evil',
    'tl': '16 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Sljedećih $k$ dana vještac Gebyte susreće po jedan par ljudi u sukobu: $i$-tog dana osobe $a_i$ i $b_i$, i ubit će $b_i$ („manje zlo”). Susret se održava samo ako su obje osobe još žive. Prije bilo kojeg susreta možeš baciti čaroliju — tada tog dana Gebyte ne ubija nikoga. Čarolija možeš baciti koliko god želiš.</p>
<p>Dan je skup od $s$ tvojih neprijatelja. Možeš li osigurati da svi oni poginu od Gebyteove ruke? Isti par se može pojaviti više puta, pa i s obrnutom odlukom.</p>
<h3>Ulaz</h3>
<p>$z \le 1000$ testova; $2 \le n \le 10^6$, $1 \le k \le 10^6$, $k$ parova $a_i \ne b_i$; $s$ i $s$ različitih neprijatelja uzlazno; $\sum n, \sum k \le 4\,000\,000$.</p>
<h3>Izlaz</h3>
<p><code>TAK</code> i string od $k$ slova <code>T</code>/<code>N</code>: <code>T</code> — $i$-tog dana pusti Gebytea da ubije $b_i$, <code>N</code> — spriječi ga. (Ako se susret ne održava, slovo nije bitno.) Prihvaća se ako nijedan neprijatelj ne preživi. Inače <code>NIE</code>.</p>
<h3>Primjer</h3>
<p>$n = 5$, susreti $(1,2), (2,1), (2,5), (2,3), (2,4), (4,2)$, neprijatelji $1, 2, 3$: <code>TAK</code>, <code>NTTTNT</code> — Gebyte ubija $1$ (2. dan), $5$ (3. dan), $3$ (4. dan) i $2$ (6. dan); točno je i <code>NTNTNT</code>. $n = 3$, susreti $(1,2), (2,3)$, neprijatelji $2, 3$: <code>NIE</code>.</p>
''',
    'solution': None,
},
]
