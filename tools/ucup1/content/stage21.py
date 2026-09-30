# -*- coding: utf-8 -*-
STAGE = {
    'no': 21,
    'name': 'Stage 21: Shandong',
    'source_name': 'Jul 1st, 2023',
    'no_editorial': True,
    'community': True,
    'source_html': r'''
<p>Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1277&amp;r=0">engleskim tekstovima zadataka</a>. Organizatori nisu objavili službena rješenja. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1277">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Colorful Segments', 'title_hr': 'Šareni segmenti', 'slug': 'A_colorful_segments',
    'tl': '4 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Na brojevnom pravcu je $n$ segmenata $[l_i, r_i]$ boje $c_i \in \{0, 1\}$ ($0$ crvena, $1$ plava). Odaberi podskup segmenata (može i prazan) tako da svaka dva odabrana segmenta koja se preklapaju imaju istu boju. Segmenti $i$ i $j$ se preklapaju ako postoji realan $x$ s $l_i \le x \le r_i$ i $l_j \le x \le r_j$.</p>
<p>Izračunaj broj načina odabira modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; u svakom $1 \le n \le 10^5$ i $n$ redaka $l_i\ r_i\ c_i$ ($1 \le l_i \le r_i \le 10^9$). Zbroj $n$ ne prelazi $5 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan broj.</p>
<h3>Primjer</h3>
<p>Segmenti $[1,5]_0, [3,6]_1, [4,7]_0$: $5$ (ne mogu se zajedno uzeti 1. i 2., ni 2. i 3.). Segmenti $[1,5]_0, [7,9]_1, [3,6]_0$: $8$.</p>
''',
    'hints': [r'''
<p>Sortiraj segmente po desnom kraju i gledaj odabrani podskup u tom redoslijedu: dijeli se na maksimalne <em>blokove</em> iste boje. Kad je prijelaz s bloka boje $1-c$ na blok boje $c$ dopušten?</p>
''', r'''
<p>Neka je $f(i)$ broj dopuštenih odabira u kojima je segment $i$ posljednji po desnom kraju. Ako je $j$ posljednji segment suprotne boje ispred $i$ (ili $j = 0$, virtualni početak), svi segmenti boje $c_i$ između $j$ i $i$ s $l \gt r_j$ mogu se uzeti ili ne uzeti slobodno: $f(i) = \sum_j f(j) \cdot 2^{\#\{\text{takvih segmenata}\}}$ po $j$ s $r_j \lt l_i$.</p>
''', r'''
<p>Po jednom segmentnom stablu za svaku boju: na poziciji $j$ drži $f(j)$ pomnoženo s $2^{(\text{broj već obrađenih segmenata suprotne boje koji ne sijeku } j)}$. Obrada $i$: zbroj prefiksa $[0, p_i]$ u stablu boje $1 - c_i$ ($p_i$ = broj segmenata s $r \lt l_i$), zatim taj prefiks pomnoži s $2$, pa upiši $f(i)$ u stablo boje $c_i$.</p>
'''],
    'coach': [
        (r'''Kako opisati dopušten podskup tako da se uvjet „preklapajući imaju istu boju” lako provjerava redom?''', r'''
<p>Poredajmo segmente po desnom kraju $r$ (ties po bilo čemu) i gledajmo odabrane u tom redoslijedu. Dva segmenta $j \lt i$ (po $r$) se ne preklapaju točno kad je $r_j \lt l_i$. Uvjet zadatka kaže: za svaka dva odabrana segmenta različite boje mora biti $r_j \lt l_i$. Podijelimo odabrani niz na maksimalne blokove iste boje; segment $i$ smije se dodati ako je $l_i \gt r_j$ za svaki odabrani $j$ suprotne boje, a kako su $r$ sortirani, dovoljno je provjeriti <em>posljednji</em> takav $j$ – on ima najveći $r$ među njima.</p>
'''),
        (r'''Kako definirati stanje DP-a da se broj načina ne broji višestruko?''', r'''
<p>$f(i)$ = broj dopuštenih odabira čiji je posljednji segment (po $r$) točno $i$; odgovor je $1 + \sum_i f(i)$ (prazan skup). Za odabir s posljednjim $i$ boje $c$ neka je $j$ posljednji odabrani segment boje $1-c$ ($j = 0$ ako ga nema). Segmenti poslije $j$ u odabiru su svi boje $c$ i svi moraju imati $l \gt r_j$; obrnuto, svaki podskup segmenata boje $c$ s indeksom u $(j, i)$ i $l \gt r_j$, zajedno s $i$, daje dopušten odabir (dva segmenta iste boje smiju se preklapati). Zato $$f(i) = \sum_{j:\, c_j \ne c_i,\ r_j \lt l_i} f(j) \cdot 2^{\,m(j, i)},\qquad m(j,i) = \#\{t \in (j, i): c_t = c_i,\ l_t \gt r_j\},$$ uz $f(0) = 1$. Svaki odabir se broji točno jednom jer je par $(i, j)$ njime jednoznačno određen.</p>
'''),
        (r'''Kako prijelaz sa faktorima $2^{m(j,i)}$ učiniti brzim?''', r'''
<p>Ključ je da $2^{m(j,i)}$ raste inkrementalno: kad obradimo novi segment $t$ boje $c$, faktor za sve $j$ suprotne boje s $r_j \lt l_t$ udvostručuje se. Zato stablo boje $x$ drži na poziciji $j$ vrijednost $f(j) \cdot 2^{(\text{broj obrađenih segmenata boje } 1-x \text{ koji ne sijeku } j)}$. Kad obrađujemo $i$ boje $c_i$: (1) $f(i) = $ zbroj prefiksa $[0, p_i]$ stabla boje $1 - c_i$, gdje su pozicije $1..p_i$ točno segmenti s $r \lt l_i$ (sortirani po $r$, pa <code>lower_bound</code>); (2) pomnoži taj isti prefiks s $2$ – segment $i$ je „slobodan” za sve te $j$; (3) upiši $f(i)$ na poziciju $i$ stabla boje $c_i$. Faktor koji stoji uz $f(j)$ u trenutku upita točno je $2^{m(j,i)}$, jer su udvostručenja primijenili upravo segmenti $t \in (j, i)$ boje $c_i$ s $l_t \gt r_j$.</p>
'''),
        (r'''Koja svojstva segmentnog stabla trebaju i kolika je složenost?''', r'''
<p>Zbroj na prefiksu, množenje prefiksa konstantom $2$ (lijeno, množenje se lijepo kompozira) i postavljanje vrijednosti u točki – standardno lijeno segmentno stablo s $O(\log n)$ po operaciji. Sortiranje i $n$ obrada daju $O(n \log n)$ po testu; zbroj $n$ je $5 \cdot 10^5$, vremensko ograničenje $4$ s je vrlo komotno.</p>
'''),
    ],
    'tips': [r'''<strong>„Posljednji element suprotne vrste”</strong> je čest DP parametar kod uvjeta oblika „elementi različitih klasa ne smiju se dodirivati”; sve između posljednjeg prijelaza i trenutnog elementa tada je slobodno ili zabranjeno po jednostavnom pravilu.''',
             r'''Faktore oblika $2^{\text{broj nečega između}}$ ne računaj za svaki par – održavaj ih inkrementalno lijenim množenjem prefiksa u segmentnom stablu.''',
             r'''Za intervale sortirane po $r$, uvjet „ne siječe $i$” za ranije segmente je prefiks ($r_j \lt l_i$): to je razlog zašto svi upiti i ažuriranja padaju na prefikse i zašto <code>lower_bound</code> daje granicu.'''],
    'solution': r'''
<p>Prema javnim analizama natjecanja SDCPC 2023. Segmente sortiramo po desnom kraju; $f(i)$ je broj dopuštenih odabira u kojima je $i$ posljednji. Ako je $j$ posljednji odabrani segment suprotne boje ($r_j \lt l_i$; ili $j = 0$), svi segmenti boje $c_i$ između $j$ i $i$ s $l \gt r_j$ biraju se slobodno, pa je $f(i) = \sum_j f(j) \cdot 2^{m(j,i)}$. Faktore održavamo inkrementalno: stablo boje $x$ na poziciji $j$ drži $f(j)$ pomnoženo s $2^{(\text{broj obrađenih segmenata boje } 1-x \text{ koji ne sijeku } j)}$; obrada $i$ je upit zbroja prefiksa $[0, p_i]$ u stablu boje $1 - c_i$ (pozicije s $r \lt l_i$), množenje tog prefiksa s $2$ i upis $f(i)$ u stablo boje $c_i$. Odgovor je $1 + \sum f(i)$, složenost $O(n \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Karakterizacija dopuštenih odabira</h3>
<p>Sortirajmo segmente po $r$ (indeksi $1..n$). Za $j \lt i$ segmenti se <em>ne</em> preklapaju točno kad $r_j \lt l_i$ (jer $r_j \le r_i$). Odabir je dopušten ako za svaki par odabranih $j \lt i$ različitih boja vrijedi $r_j \lt l_i$. Gledajući odabrani niz po indeksima, dijeli se na maksimalne blokove iste boje; uvjet se odnosi samo na parove iz različitih blokova. Ako je $i$ u bloku boje $c$ i $j$ je posljednji odabrani segment boje $1-c$ ispred $i$, onda je $r_j$ najveći desni kraj među odabranim suprotne boje ispred $i$, pa je uvjet za $i$ ekvivalentan s $r_j \lt l_i$.</p>
<h3>2. Rekurzija</h3>
<p>Neka je $f(i)$ broj dopuštenih odabira s posljednjim segmentom $i$, $f(0) = 1$ (prazan odabir, virtualni segment $0$ s $r_0 = -\infty$ i „obje boje”). Za odabir s posljednjim $i$ boje $c$ neka je $j$ posljednji odabrani segment boje $1 - c$ (ili $0$). Dio odabira do $j$ zaključno je dopušten odabir s posljednjim $j$ (broji ga $f(j)$); dio poslije $j$ sastoji se od $i$ i nekog podskupa $S$ segmenata $t$ boje $c$ s $j \lt t \lt i$. Uvjet dopuštenosti cijelog odabira: svaki $t \in S \cup \{i\}$ mora imati $l_t \gt r_j$ (prema odjeljku 1, provjera prema posljednjem suprotnom, a to je $j$ za sve njih), i ništa više – segmenti iste boje smiju se preklapati, a parovi iz dijela do $j$ već su provjereni u $f(j)$. Dakle $$f(i) = \sum_{\substack{j \lt i\\ c_j \ne c_i\\ r_j \lt l_i}} f(j)\, 2^{\,m(j,i)},\qquad m(j,i) = \#\{t : j \lt t \lt i,\ c_t = c_i,\ l_t \gt r_j\}$$ (za $j = 0$ uvjet $r_j \lt l_i$ je uvijek istinit, a $m(0,i)$ broji sve ranije segmente boje $c_i$). Odgovor je $1 + \sum_{i=1}^n f(i)$. Svaki odabir broji se jednom jer je $(i, j)$ njime određen.</p>
<h3>3. Inkrementalno održavanje faktora</h3>
<p>Za boju $x$ držimo segmentno stablo $T_x$ nad pozicijama $0..n$. Invarijanta nakon obrade segmenata $1..i-1$: na poziciji $j$ (boje $x$, ili $j = 0$) stoji $$f(j) \cdot 2^{\#\{t \le i-1:\ t \gt j,\ c_t = 1-x,\ l_t \gt r_j\}},$$ a na pozicijama još neobrađenih ili druge boje stoji $0$. Obrada segmenta $i$ boje $c$:</p>
<ol>
<li>$p_i$ = broj segmenata s $r \lt l_i$ (binarno pretraživanje u sortiranom nizu $r$); to su točno pozicije $1..p_i$. Upit: $f(i) = T_{1-c}.\mathrm{sum}(0, p_i)$. Po invarijanti sumand na poziciji $j$ je $f(j) \cdot 2^{m(j,i)}$ – eksponent broji segmente $t \in (j, i)$ boje $c$ s $l_t \gt r_j$, upravo $m(j,i)$.</li>
<li>Množenje: $T_{1-c}.\mathrm{mul}(0, p_i, 2)$ – za svaki $j$ s $r_j \lt l_i$ segment $i$ je novi „slobodni” segment boje $c$, pa se eksponent uvećava za $1$; za $j \gt p_i$ ne mijenja se.</li>
<li>Upis: $T_c.\mathrm{set}(i, f(i))$ – eksponent je $0$ jer još nema kasnijih segmenata.</li>
</ol>
<p>Pozicija $0$ upisana je s $1$ u <em>oba</em> stabla (virtualni početak je kompatibilan s obje boje).</p>
<h3>4. Struktura podataka i složenost</h3>
<p>Lijeno segmentno stablo s operacijama: zbroj intervala, množenje intervala konstantom (lijeni faktor se množi; identitet $1$), postavljanje točke. Sve $O(\log n)$; ukupno $O(n \log n)$ po testu, zbroj $n \le 5 \cdot 10^5$. Aritmetika modulo $998\,244\,353$ u 64-bitnim tipovima.</p>
<h3>5. Provjera na primjeru i zamke</h3>
<ul>
<li>Primjer $[1,5]_0, [3,6]_1, [4,7]_0$: sortirano po $r$: $A=[1,5]_0$, $B=[3,6]_1$, $C=[4,7]_0$. $f(A) = 1$; $f(B)$: samo $j = 0$, $m = 0$ ($A$ siječe $B$) → $1$; $f(C)$: $j = 0$ s $m(0, C) = 1$ ($A$ slobodan) → $2$, a $B$ ne može ($r_B = 6 \ge 4$). Ukupno $1 + 1 + 1 + 2 = 5$. ✓</li>
<li>Jednaki desni krajevi: poredak među njima nije bitan jer se takvi segmenti međusobno sijeku ($r_j = r_i \ge l_i$), pa uvjet $r_j \lt l_i$ pada u oba smjera – binarno pretraživanje s <code>lower_bound</code> po $r$ daje ispravan prefiks.</li>
<li>Ne zaboravi $+1$ za prazan odabir i upis $f(0) = 1$ u oba stabla.</li>
<li>Množenje prefiksa mora se izvesti <em>nakon</em> upita za isti $i$, a upis $f(i)$ u drugo stablo ne smije biti pomnožen.</li>
</ul>
''',
    'verified': r'''uzorci 1/1 (oba testa iz zadatka); 300 slučajnih malih testova ($n \le 12$, koordinate do $3$, $6$ ili $20$ radi mnogo preklapanja i jednakih krajeva) protiv brute forcea koji ispituje svih $2^n$ podskupova; 3 velika testa s $5$ testova po $n = 10^5$ (najviše $0.29$ s).''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Be Careful 2', 'title_hr': 'Budi oprezan 2', 'slug': 'B_be_careful_2',
    'tl': '12 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Pravokutnik s donjim lijevim kutom $(0,0)$ i gornjim desnim $(n, m)$ sadrži $k$ zabranjenih točaka $(x_i, y_i)$. Kvadrat s donjim lijevim kutom $(x, y)$ i stranicom $d$ smije se nacrtati ako su $x, y$ nenegativni cijeli, $d$ pozitivan cijeli, $x + d \le n$, $y + d \le m$ i ni za jednu zabranjenu točku ne vrijedi $x \lt x_i \lt x + d$ i $y \lt y_i \lt y + d$ (točke na rubu kvadrata su dopuštene).</p>
<p>Izračunaj zbroj površina svih dopuštenih kvadrata modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$2 \le n, m \le 10^9$, $1 \le k \le 5 \cdot 10^3$; zatim $k$ različitih točaka, $0 \lt x_i \lt n$, $0 \lt y_i \lt m$.</p>
<h3>Izlaz</h3>
<p>Jedan broj.</p>
<h3>Primjer</h3>
<p>$n = m = 3$, točka $(2,2)$: $21$ ($9$ kvadrata stranice $1$ i $3$ kvadrata stranice $2$). $n = m = 5$, točke $(2,1), (2,4)$: $126$.</p>
''',
    'hints': [r'''
<p>Uvjet „nijedna zabranjena točka strogo unutra” zapiši uključivanjem-isključivanjem: $[\text{nijedna}] = \sum_{S \subseteq \text{točke unutra}} (-1)^{|S|}$. Odgovor je tada $\sum_S (-1)^{|S|} f(S)$, gdje $f(S)$ zbraja $d^2$ po kvadratima koji strogo sadrže sve točke iz $S$.</p>
''', r'''
<p>Podskupova je previše, ali grupiraj ih po paru $(L, R)$ – točkama s najmanjim i najvećim $x$ (jednake koordinate razdvoji indeksom). Za fiksni kvadrat i fiksni par, predznaci svih $S$ s tim krajevima zbrajaju se u $[\text{nijedna „srednja” točka nije u kvadratu}]$. Ostaje $O(k^2)$ parova, a za svaki treba zbroj $d^2$ po kvadratima koji strogo sadrže $L$ i $R$ i ne sadrže nijednu točku s $x$ između njih.</p>
''', r'''
<p>Za par $(L,R)$ srednje točke ograničavaju samo $y$-raspon kvadrata: ako je neka srednja točka po $y$ između $y_L$ i $y_R$, par ne doprinosi; inače kvadrat mora ostati unutar $(Y_p, Y_q)$ – najbližih srednjih $y$ ispod i iznad. Broj položaja 1D prozora duljine $d$ je „trapezna” po dijelovima linearna funkcija od $d$; umnožak po $x$ i $y$ puta $d^2$ je po dijelovima polinom stupnja $4$, zbroji ga Faulhaberovim formulama u $O(1)$. Parove obradi za fiksni $L$ po padajućem $x_R$ uz dvostruko povezanu listu točaka po $y$.</p>
'''],
    'coach': [
        (r'''Kako se uvjet „kvadrat ne sadrži nijednu zabranjenu točku” pretvara u zbroj koji se može grupirati?''', r'''
<p>Za fiksni kvadrat $Q$ neka je $I(Q)$ skup zabranjenih točaka strogo unutra. Tada je $[I(Q) = \emptyset] = \sum_{S \subseteq I(Q)} (-1)^{|S|}$ (prazan skup daje $1$, neprazan daje $0$). Zamjenom redoslijeda sumiranja: $$\text{odgovor} = \sum_{Q} d(Q)^2 [I(Q)=\emptyset] = \sum_{S} (-1)^{|S|} f(S),\quad f(S) = \sum_{Q \supset S} d(Q)^2.$$ Za $S = \emptyset$ dobivamo zbroj po svim kvadratima; za $|S| = 1$ po kvadratima koji strogo sadrže tu točku. Problem je eksponencijalan broj $S$.</p>
'''),
        (r'''Zašto se svi podskupovi s istim krajnjim točkama $L, R$ po $x$ mogu sažeti u jedan član?''', r'''
<p>Poredajmo točke po $(x, \text{indeks})$ tako da su svi „rangovi” različiti. Svaki $S$ s $|S| \ge 2$ ima jedinstvenu točku najmanjeg ranga $L$ i najvećeg ranga $R$, a ostale točke iz $S$ – srednje, s rangom između – proizvoljan su podskup $M$ srednjih točaka. Za fiksni kvadrat $Q \supset \{L, R\}$ zbroj predznaka po svim $S$ s tim krajevima koji su u $Q$ je $\sum_{M \subseteq \text{mid}(Q)} (-1)^{2 + |M|} = [\text{mid}(Q) = \emptyset]$, gdje je $\text{mid}(Q)$ skup srednjih točaka strogo unutar $Q$. Dakle $$\text{odgovor} = \sum_Q d^2 \;-\; \sum_L f(\{L\}) \;+\; \sum_{L \lt R}\ \sum_{Q \supset \{L,R\},\ \text{mid}(Q)=\emptyset} d(Q)^2 .$$ Ostalo je $O(k^2)$ parova.</p>
'''),
        (r'''Kad kvadrat strogo sadrži $L$ i $R$, što točno znači „ne sadrži nijednu srednju točku”?''', r'''
<p>Srednja točka $p$ ima $x_L \le x_p \le x_R$, pa je po $x$ automatski strogo unutar (kvadrat strogo sadrži $x_L$ i $x_R$). Dakle $p$ je unutra točno kad je $y_p$ strogo unutar $y$-raspona kvadrata. Neka je $[y_{lo}, y_{hi}]$ raspon $y$-koordinata $L$ i $R$. Ako neka srednja točka ima $y_p \in [y_{lo}, y_{hi}]$, svaki kvadrat koji sadrži $L, R$ sadrži i $p$ – par ne doprinosi. Inače neka je $Y_p$ najveći srednji $y$ manji od $y_{lo}$ (ili $0$) i $Y_q$ najmanji veći od $y_{hi}$ (ili $m$): kvadrat s $y$-prozorom $[y, y+d]$ ne sadrži srednje točke točno kad $y \ge Y_p$ i $y + d \le Y_q$. Uvjet je dakle: $x$-prozor strogo sadrži $[x_L, x_R]$ unutar $[0, n]$, $y$-prozor strogo sadrži $[y_{lo}, y_{hi}]$ unutar $[Y_p, Y_q]$.</p>
'''),
        (r'''Kako za fiksni par zbrojiti $d^2$ po svim takvim kvadratima u $O(1)$?''', r'''
<p>Broj položaja 1D prozora duljine $d$ unutar $[A, B]$ koji strogo sadrži $[a, b]$ je $\tau(d) = \max\big(0, \min(a-1, B-d) - \max(A, b-d+1) + 1\big)$: kao funkcija od $d$ to je nula za $d \le b - a + 1$, zatim raste s nagibom $1$, onda je konstantna, pa pada s nagibom $-1$ do nule kod $d = B - A$ – najviše tri linearna dijela. Za par tražimo $\sum_d d^2 \tau_x(d)\tau_y(d)$; na presjeku dijelova umnožak je polinom stupnja $\le 4$ u $d$, pa ga zbrajamo formulama za $\sum d^2, \sum d^3, \sum d^4$ (Faulhaber) modulo $998244353$. Najviše $9$ presjeka po paru.</p>
'''),
        (r'''Kako obići sve parove i za svaki brzo znati $Y_p$, $Y_q$ i je li neka srednja točka po $y$ između?''', r'''
<p>Za fiksni $L$ (rang $\ell$) stavimo sve točke ranga $\ge \ell$ u dvostruko povezanu listu sortiranu po $(y, \text{indeks})$. Obrađujemo $R$ po padajućem rangu: u tom trenutku lista sadrži točno rangove $\ell..r$, dakle $L$, $R$ i sve srednje. Par je valjan točno kad su $L$ i $R$ susjedi u listi; tada su $Y_p$ i $Y_q$ prethodnik nižeg i sljedbenik višeg od njih. Nakon obrade $R$ ga izbacimo iz liste u $O(1)$. Po $L$ je to $O(k)$, ukupno $O(k^2)$ s malom konstantom – za $k = 5000$ oko $1.25 \cdot 10^7$ parova.</p>
'''),
    ],
    'tips': [r'''<strong>Uključivanje-isključivanje + grupiranje po krajnjim točkama.</strong> Kad su podskupovi „intervalno” određeni (krajevi po jednoj koordinati), predznaci srednjih elemenata se pokrate i ostane samo uvjet praznine – tehnika se pojavljuje u mnogim zadacima brojanja pravokutnika bez točaka.''',
             r'''Broj položaja prozora duljine $d$ je po dijelovima linearan u $d$; umnošci takvih funkcija s polinomom zbrajaju se Faulhaberovim formulama – nema potrebe za petljom po $d$ kad je $d$ do $10^9$.''',
             r'''Jednake koordinate razbij indeksom prije bilo kakvog „min/max” grupiranja; inače isti podskup dobiva više ili nula reprezentanata i predznaci se ne pokrate.''',
             r'''Kod $O(k^2)$ enumeracije s $k = 5000$ pazi da unutarnja petlja bude $O(1)$ bez alokacija; dvostruko povezana lista s brisanjem je idealna.'''],
    'solution': r'''
<p>Prema službenim skicama rješenja (SUA wiki, SDCPC 2023) i javnim analizama. Uključivanjem-isključivanjem: odgovor $= \sum_S (-1)^{|S|} f(S)$, gdje $f(S)$ zbraja $d^2$ po kvadratima koji strogo sadrže sve točke skupa $S$. Podskupove grupiramo po točkama $L, R$ najmanjeg i najvećeg $x$ (jednake koordinate razdvojene indeksom); za fiksni kvadrat predznaci srednjih točaka se pokrate, pa ostaje: (svi kvadrati) $- \sum_L f(\{L\}) + \sum_{L \lt R}$ (zbroj $d^2$ po kvadratima koji strogo sadrže $L$ i $R$, a ne sadrže nijednu točku s $x$ između). Srednje točke ograničavaju samo $y$-prozor na $[Y_p, Y_q]$ (najbliži srednji $y$ ispod/iznad), a ako je neki srednji $y$ između $y_L$ i $y_R$ par otpada. Za fiksni $L$ obrađujemo $R$ po padajućem $x$ uz dvostruko povezanu listu točaka po $y$ ($L$ i $R$ moraju biti susjedi). Broj položaja 1D prozora duljine $d$ je po dijelovima linearan, pa je zbroj $d^2\tau_x(d)\tau_y(d)$ po dijelovima polinom stupnja $4$ – Faulhaberove formule daju $O(1)$ po paru. Ukupno $O(k^2)$.</p>
''',
    'detailed': r'''
<h3>1. Uključivanje-isključivanje</h3>
<p>Neka $Q$ prolazi po svim kvadratima ($0 \le x \lt x + d \le n$, $0 \le y \lt y + d \le m$), $d(Q)$ stranica, $I(Q)$ skup zabranjenih točaka strogo unutar $Q$. Iz $[I(Q) = \emptyset] = \sum_{S \subseteq I(Q)} (-1)^{|S|}$ slijedi $$\text{odgovor} = \sum_S (-1)^{|S|} f(S),\qquad f(S) = \sum_{Q:\ S \subseteq I(Q)} d(Q)^2 .$$</p>
<h3>2. Grupiranje po krajnjim točkama</h3>
<p>Sortirajmo točke po $(x, \text{indeks})$ – „rang” po $x$ – tako da su rangovi različiti i za jednake $x$. Za $|S| \ge 2$ neka su $L, R$ točke najmanjeg i najvećeg ranga u $S$, a $\text{mid}(L,R)$ skup točaka ranga strogo između. Za fiksni kvadrat $Q$ koji strogo sadrži $L$ i $R$, podskupovi $S$ s krajevima $L, R$ i $S \subseteq I(Q)$ su točno $\{L, R\} \cup M$ za $M \subseteq \text{mid}(L,R) \cap I(Q)$, pa je zbroj njihovih predznaka $\sum_M (-1)^{|M|} = [\text{mid}(L,R) \cap I(Q) = \emptyset]$. Time $$\text{odgovor} = \underbrace{\sum_Q d(Q)^2}_{(1)} - \underbrace{\sum_L f(\{L\})}_{(2)} + \underbrace{\sum_{L \lt R}\ \sum_{\substack{Q \ni L, R\\ Q \cap \text{mid}(L,R) = \emptyset}} d(Q)^2}_{(3)} .$$ Član (1) je $\sum_{d=1}^{\min(n,m)} d^2 (n+1-d)(m+1-d)$.</p>
<h3>3. Uvjet za par $(L, R)$</h3>
<p>Srednja točka $p$ zadovoljava $x_L \le x_p \le x_R$, a $Q$ strogo sadrži $x_L$ i $x_R$, pa je $p$ po $x$ strogo unutra. Dakle $p \in I(Q)$ točno kad je $y \lt y_p \lt y + d$. Neka je $y_{lo} = \min(y_L, y_R)$, $y_{hi} = \max(y_L, y_R)$. Ako postoji srednja točka s $y_p \in [y_{lo}, y_{hi}]$, onda je u svakom $Q \ni L, R$ i par ne doprinosi. Inače neka je $Y_p = \max(\{0\} \cup \{y_p \lt y_{lo}\})$ i $Y_q = \min(\{m\} \cup \{y_p \gt y_{hi}\})$ po srednjim točkama. $Q$ izbjegava srednje točke točno kad $Y_p \le y$ i $y + d \le Y_q$. Uvjeti za $Q = [x, x+d] \times [y, y+d]$: $$0 \le x \lt x_L \le x_R \lt x + d \le n,\qquad Y_p \le y \lt y_{lo} \le y_{hi} \lt y + d \le Y_q .$$ Za fiksni $d$ broj mogućih $x$ je $\tau_x(d) = \max(0, \min(x_L - 1, n - d) - \max(0, x_R - d + 1) + 1)$, a $\tau_y(d)$ analogno s $[Y_p, Y_q]$ i $[y_{lo}, y_{hi}]$. Član (2) je isti izraz s $L = R$ i bez ograničenja srednjih točaka ($Y_p = 0$, $Y_q = m$).</p>
<h3>4. Zbroj po $d$ u $O(1)$</h3>
<p>Funkcija $\tau(d)$ za prozor $[A, B]$ i unutarnji interval $[a, b]$ ($A \lt a \le b \lt B$) ima oblik: $0$ za $d \le b - a + 1$; $d - (b - a + 1)$ dok obje granice nisu „stisnute” (do $d \lt \min(b - A + 1, B - a + 1)$); konstanta $\min(a - A, B - b)$ do $d \lt \max(\cdot)$; zatim $B - A + 1 - d$ do $d \le B - A$; potom $0$. Dakle najviše tri linearna dijela $\alpha d + \beta$ na intervalima $d$. Za par uzmemo presjeke dijelova $\tau_x$ i $\tau_y$ (najviše $9$); na presjeku $[l, r]$ je $d^2 \tau_x \tau_y = c_4 d^4 + c_3 d^3 + c_2 d^2$ s $c_4 = \alpha_x\alpha_y$, $c_3 = \alpha_x\beta_y + \beta_x\alpha_y$, $c_2 = \beta_x\beta_y$, a $\sum_{d=l}^{r} d^k$ dobivamo iz prefiksnih formula $\sum_{d \le t} d^2 = \frac{t(t+1)(2t+1)}{6}$, $\sum d^3 = \left(\frac{t(t+1)}{2}\right)^2$, $\sum d^4 = \frac{t(t+1)(2t+1)(3t^2+3t-1)}{30}$ modulo $998244353$ (inverzi od $6$ i $30$). Koeficijenti su do $10^{18}$ po apsolutnoj vrijednosti – reduciramo ih modulo prije množenja.</p>
<h3>5. Enumeracija parova</h3>
<p>Za svaki $L$ (rang $\ell$): u dvostruko povezanu listu sortiranu po $(y, \text{indeks})$ stavimo sve točke ranga $\ge \ell$. Za $R$ po padajućem rangu $r = k-1, \dots, \ell+1$: lista sadrži rangove $\ell..r$, tj. $L$, $R$ i sve srednje točke. Par je valjan točno kad su $L$ i $R$ susjedi u listi (nijedna srednja točka nema $y$ između, uz ties razriješene indeksom – srednja točka s $y_p = y_L$ koja stoji ispred $L$ daje $Y_p = y_{lo}$ i $\tau_y \equiv 0$, što je ispravno jer bi $p$ bila unutra). $Y_p$ je $y$ prethodnika nižeg od $L, R$ (ili $0$), $Y_q$ je $y$ sljedbenika višeg (ili $m$). Zatim izbacimo $R$ iz liste. Ukupno $O(k^2)$ koraka $O(1)$, plus $O(k \log k)$ za sortiranja.</p>
<h3>6. Složenost i zamke</h3>
<ul>
<li>Vrijeme $O(k^2)$ s $\le 9$ evaluacija Faulhaberovih formula po valjanom paru; za $k = 5000$ ispod $0.3$ s. Memorija $O(k)$.</li>
<li>Točke s jednakim $x$ ili $y$: rang po indeksu je nužan – bez toga isti podskup nema jedinstven par $(L, R)$.</li>
<li>Granice trapeza: vrijednost $\tau$ mora biti $\ge 1$ na svakom dijelu koji zbrajamo; odrezivanje intervala $d$ na $\tau \ge 1$ izbjegava negativne „brojeve položaja”.</li>
<li>Sve aritmetike u <code>unsigned long long</code> s redukcijom nakon svakog množenja; $t$ do $10^9$, pa $t(t+1)$ prelazi 64 bita bez prethodne redukcije.</li>
<li>Provjera: $n = m = 3$, točka $(2,2)$: svi kvadrati $1 \cdot 9 + 4 \cdot 4 + 9 \cdot 1 = 34$, kvadrati koji strogo sadrže $(2,2)$: $d = 2$: jedan ($4$), $d = 3$: jedan ($9$), ukupno $34 - 13 = 21$. ✓</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($n, m \le 9$, do $8$ točaka) protiv brute forcea koji ispituje svaki kvadrat; 3 velika testa s $k = 5000$ i $n, m \approx 10^9$ (slučajne točke, dva „sloja” u kojima je svaki par valjan, gusti raspored s jednakim koordinatama; najviše $0.19$ s), dodatno srednje veliki testovi ($k \le 60$, $n, m \le 40$) protiv brute forcea.''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Connected Intervals', 'title_hr': 'Povezani intervali', 'slug': 'C_connected_intervals',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dano je stablo s $n$ vrhova. Interval $[l, r]$ je <em>povezan</em> ako inducirani podgraf na skupu vrhova $\{v_l, \dots, v_r\}$ ima točno jednu komponentu povezanosti. Prebroji povezane intervale.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 3 \cdot 10^5$, zatim $n - 1$ bridova. Zbroj $n$ ne prelazi $3 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test broj povezanih intervala.</p>
<h3>Primjer</h3>
<p>Put $1\text{-}2\text{-}3\text{-}4$: $10$. Zvijezda s bridovima $1\text{-}2, 2\text{-}3, 2\text{-}4$: $9$ (svi osim $[3,4]$).</p>
''',
    'hints': [r'''
<p>Inducirani podgraf stabla na skupu vrhova je šuma. Koliko bridova ima šuma s $r - l + 1$ vrhova i jednom komponentom?</p>
''', r'''
<p>Interval $[l, r]$ je povezan točno kad je $e(l, r) = r - l$, gdje je $e(l,r)$ broj bridova s oba kraja u $[l, r]$. Uvijek je $e(l, r) \le r - l$, pa je $d(l) = (r - l) - e(l, r) \ge 0$ i tražimo broj nula.</p>
''', r'''
<p>Pomiči desni kraj $r$ i drži $d(l)$ za sve $l \le r$ u segmentnom stablu: prijelaz na $r+1$ dodaje $+1$ na $[1, r]$ i, za svaki brid $(u, r+1)$ s $u \lt r+1$, $-1$ na $[1, u]$. Odgovor uvećaj za broj minimuma ako je minimum $0$.</p>
'''],
    'coach': [
        (r'''Što povezanost induciranog podgrafa stabla govori o broju bridova unutar intervala?''', r'''
<p>Podgraf stabla induciran skupom vrhova nema ciklusa, dakle je šuma; šuma s $V$ vrhova i $E$ bridova ima točno $V - E$ komponenata. Za $[l, r]$ je $V = r - l + 1$, pa je podgraf povezan točno kada $E = e(l, r) = r - l$. Time se „povezanost” (svojstvo koje se teško održava) zamjenjuje čistim brojanjem bridova.</p>
'''),
        (r'''Kako iskoristiti da je $e(l, r) \le r - l$ uvijek?''', r'''
<p>Definirajmo deficit $d(l) = (r - l) - e(l, r) \ge 0$ za fiksni $r$ – broj komponenata minus $1$. Tražimo broj $l \le r$ s $d(l) = 0$; kako je $d \ge 0$, to je broj minimuma u segmentnom stablu ako je minimum jednak $0$. Segmentno stablo s operacijom „dodaj na interval” i podacima (minimum, broj minimuma) to daje u $O(\log n)$.</p>
'''),
        (r'''Kako se $d(l)$ mijenja kad desni kraj poraste s $r$ na $r + 1$?''', r'''
<p>Za sve $l \le r$ član $r - l$ raste za $1$: dodaj $+1$ na $[1, r]$. Novi bridovi unutar intervala su oni koji spajaju $r + 1$ s nekim $u \lt r + 1$; brid $(u, r+1)$ pripada $[l, r+1]$ točno za $l \le u$, pa oduzimamo $1$ na $[1, u]$. Za $l = r + 1$ vrijednost ostaje $0$ (jedan vrh, povezan). Ukupno se svaki brid obradi jednom, dakle $O(n)$ operacija na stablu.</p>
'''),
        (r'''Kako izbjeći da se u broj nula umiješaju pozicije $l \gt r$ koje još nisu „aktivne”?''', r'''
<p>Sve pozicije počinju s $0$ i pozicije $l \gt r$ nikad nisu dirane, pa imaju $d = 0$. Ili se stablo gradi samo nad $[1, r]$ (upit na prefiksu), ili se od ukupnog broja nula oduzme $n - r$. Alternativno se pozicije inicijaliziraju velikim brojem i „aktiviraju” na $0$ kad $r$ stigne do njih.</p>
'''),
    ],
    'tips': [r'''<strong>Komponente = vrhovi − bridovi</strong> u šumi. Kad god je struktura stablo ili šuma, povezanost podskupa svodi se na brojanje bridova unutar podskupa.''',
             r'''Uzorak „sweep po desnom kraju + segmentno stablo s (min, broj minimuma) i lijenim dodavanjem” rješava mnoge zadatke oblika „prebroji intervale s nekim svojstvom” kad je svojstvo izraženo brojačem koji se mijenja na prefiksima.''',
             r'''Kad je veličina koju brojiš uvijek $\ge 0$ (ili uvijek $\le 0$), broj „točno nula” je broj minimuma (maksimuma) uz provjeru vrijednosti – ne treba posebna struktura za brojanje nula.'''],
    'solution': r'''
<p>Prema javnim analizama natjecanja SDCPC 2023 (klasična tehnika). Inducirani podgraf stabla na $[l, r]$ je šuma s $r - l + 1$ vrhova, pa je povezan točno kada ima $r - l$ bridova; kako ih nikad nema više, deficit $d(l) = (r - l) - e(l, r)$ je nenegativan i interval je povezan točno kad je $d(l) = 0$. Sweep po $r$: pri prelasku na $r+1$ dodamo $+1$ na $[1, r]$ i za svaki brid $(u, r+1)$, $u \lt r+1$, dodamo $-1$ na $[1, u]$; segmentno stablo s lijenim dodavanjem čuva minimum i broj minimuma, a odgovor se uvećava za broj minimuma kad je minimum $0$ (bez još neaktivnih pozicija $l \gt r$). Složenost $O(n \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Karakterizacija povezanog intervala</h3>
<p>Neka je $e(l, r)$ broj bridova stabla s oba kraja u $\{l, \dots, r\}$. Inducirani podgraf je podgraf stabla, dakle šuma; šuma s $V$ vrhova i $E$ bridova ima $V - E$ komponenata (svaki brid smanjuje broj komponenata za točno $1$ jer nema ciklusa). Za $V = r - l + 1$: interval je povezan $\iff$ $e(l, r) = r - l$. Posljedica: $e(l, r) \le r - l$ za sve intervale, pa je $$d_r(l) = (r - l) - e(l, r) = (\text{broj komponenata}) - 1 \ge 0.$$</p>
<h3>2. Sweep po desnom kraju</h3>
<p>Fiksirajmo $r$ i promatrajmo $d_r(l)$ za $l = 1, \dots, r$. Traženi odgovor je $\sum_r \#\{l \le r : d_r(l) = 0\}$. Pri prijelazu $r \to r + 1$:</p>
<ul>
<li>$r - l$ raste za $1$ za svaki $l \le r$: $d(l) \mathrel{+}= 1$ na $[1, r]$;</li>
<li>za svaki brid $(u, r + 1)$ s $u \lt r + 1$ vrijedi: brid je unutar $[l, r+1]$ točno za $l \le u$, pa $d(l) \mathrel{-}= 1$ na $[1, u]$;</li>
<li>$d_{r+1}(r+1) = 0$ (interval od jednog vrha).</li>
</ul>
<p>Svaki brid $(u, v)$ obradi se jednom, kod $r + 1 = \max(u, v)$. Ukupno je $O(n)$ operacija „dodaj konstantu na prefiks”.</p>
<h3>3. Struktura podataka</h3>
<p>Segmentno stablo nad pozicijama $1..n$ s lijenim dodavanjem, gdje čvor čuva $\min$ i broj pozicija koje ga postižu. Nakon ažuriranja za $r$ minimum je $\ge 0$; ako je jednak $0$, broj minimuma u korijenu je broj pozicija s $d = 0$ – ali pozicije $l \gt r$ nisu nikad dirane i takođe imaju $0$, pa od broja minimuma oduzmemo $n - r$. (Ekvivalentno: upit minimuma/broja na prefiksu $[1, r]$.)</p>
<h3>4. Algoritam</h3>
<ol>
<li>Učitaj stablo u liste susjedstva; izgradi segmentno stablo s nulama.</li>
<li>Za $r = 1, \dots, n$: ako je $r \gt 1$, dodaj $+1$ na $[1, r-1]$; za svaki susjed $u \lt r$ vrha $r$ dodaj $-1$ na $[1, u]$; ako je globalni minimum $0$, odgovor $\mathrel{+}= \text{cnt} - (n - r)$.</li>
</ol>
<p>Provjera na primjeru zvijezde $1\text{-}2$, $2\text{-}3$, $2\text{-}4$: jedini nepovezani interval je $[3,4]$ (vrhovi $3$ i $4$ nisu susjedni), pa je odgovor $10 - 1 = 9$.</p>
<h3>5. Složenost i zamke</h3>
<ul>
<li>$O(n \log n)$ vremena, $O(n)$ memorije; zbroj $n$ je $3 \cdot 10^5$, ograničenje $1$ s – bez problema.</li>
<li>Odgovor je do $\frac{n(n+1)}{2} \approx 4.5 \cdot 10^{10}$: 64-bitni tip.</li>
<li>Lijeno dodavanje mora se ispravno spuštati prije rekurzije u djecu; ako čuvaš samo minimum bez broja, ne možeš izbrojiti nule.</li>
<li>$n = 1$: nema bridova, odgovor $1$.</li>
</ul>
''',
    'verified': r'''uzorak 1/1 (oba testa iz zadatka); 300 slučajnih malih testova ($n \le 9$; putovi, zvijezde, gusjenice i slučajna stabla s permutiranim oznakama) protiv brute forcea koji za svaki interval provjerava povezanost DSU-om; 3 velika testa s $n = 3 \cdot 10^5$ (najviše $0.16$ s).''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'DS Team Selection 2', 'title_hr': 'Odabir tima za strukture podataka 2', 'slug': 'D_ds_team_selection_2',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Niz $a$ duljine $n$ i $q$ upita:</p>
<ol>
<li><code>1 v</code> — svaki $a_i$ postaje $\min(a_i, v)$;</li>
<li><code>2</code> — svaki $a_i$ postaje $a_i + i$;</li>
<li><code>3 l r</code> — ispiši $\sum_{i=l}^{r} a_i$.</li>
</ol>
<h3>Ulaz</h3>
<p>$1 \le n, q \le 2 \cdot 10^5$; $0 \le a_i \le 10^{12}$; $0 \le v \le 10^{12}$; $1 \le l \le r \le n$.</p>
<h3>Izlaz</h3>
<p>Za svaki upit tipa 3 jedan broj.</p>
<h3>Primjer</h3>
<p>$a = (6, 14, 14, 6, 3, 6, 4, 13, 10, 3, 12, 5, 11)$, upiti <code>1 2</code>, <code>2</code>, <code>2</code>, <code>2</code>, <code>1 11</code>, <code>3 4 6</code>, <code>2</code>, <code>1 6</code>, <code>2</code>, <code>1 9</code>, <code>3 2 13</code>: izlaz $33$, $107$.</p>
''',
    'hints': [r'''
<p>Neka je $\mathrm{cnt}$ broj dosadašnjih operacija tipa 2 i piši $a_i = b_i + \mathrm{cnt} \cdot i$. Tip 2 samo uveća $\mathrm{cnt}$. Što tip 1 s vrijednošću $v$ radi s $b_i$?</p>
''', r'''
<p>$b_i = \min(b_i, v - \mathrm{cnt}\cdot i)$ – pravac u varijabli $i$ s nagibom $-\mathrm{cnt}$. Nagibi kasnijih pravaca su sve strmiji, pa je $b_i = \min(\text{init}_i, \mathrm{env}(i))$ gdje je $\mathrm{env}$ donja ovojnica pravaca; novi pravac postaje ovojnica na sufiksu $[p, n]$ (stog pravaca), što je „dodijeli aritmetički niz na sufiks”.</p>
''', r'''
<p>Pozicija $i$ „umire” u prvom trenutku kad $\mathrm{env}(i) \lt \text{init}_i$ i od tada $b_i = \mathrm{env}(i)$ zauvijek. Trenutke smrti izračunaj offline paralelnim binarnim pretraživanjem (na svakoj razini donja ovojnica pravaca iz intervala vremena, upiti rastućim pokazivačem). Online segmentno stablo čuva zbroj init po živima te broj, zbroj indeksa i zbroj $\mathrm{env}$ po mrtvima, uz lijenu dodjelu pravca.</p>
'''],
    'coach': [
        (r'''Kako se operacija „$a_i \mathrel{+}= i$ za sve $i$” može učiniti trivijalnom?''', r'''
<p>Zapišimo $a_i = b_i + \mathrm{cnt}\cdot i$, gdje je $\mathrm{cnt}$ broj dosad primijenjenih operacija tipa 2. Tip 2 postaje $\mathrm{cnt} \mathrel{+}= 1$ bez promjene $b$. Upit tipa 3 postaje $\sum_{i=l}^r b_i + \mathrm{cnt}\cdot\frac{(l+r)(r-l+1)}{2}$. Cijena: tip 1, $a_i = \min(a_i, v)$, u novoj varijabli glasi $b_i = \min(b_i, v - \mathrm{cnt}\cdot i)$ – oduzimamo <em>pravac</em> $\ell(i) = v - c\, i$ s $c = \mathrm{cnt}$ u trenutku upita.</p>
'''),
        (r'''Kako izgleda skup pravaca koji su dosad primijenjeni i zašto je to važno?''', r'''
<p>Nakon niza operacija $b_i = \min\big(\text{init}_i, \min_j \ell_j(i)\big) = \min(\text{init}_i, \mathrm{env}(i))$, gdje je $\mathrm{env}$ donja ovojnica svih dosadašnjih pravaca. Nagibi $-c_j$ su nerastući u vremenu (svaki novi pravac je barem toliko strm kao prethodni). Donja ovojnica pravaca s padajućim nagibima, gledana po rastućem $i$, prelazi s manje strmih na strmije: najnoviji pravac je minimum na sufiksu $[p, n]$ (možda praznom). Zato ovojnicu držimo kao <em>stog</em> pravaca s početnim pozicijama; novi pravac izbaci s vrha sve pravce čiji je početak $\ge p$ i sam uđe s početkom $p$ (sjecište s novim vrhom, cjelobrojno zaokruženo). Dodavanje pravca postaje „na $[p, n]$ dodijeli $\mathrm{env}(i) = v - c\, i$”.</p>
'''),
        (r'''Zbog čega je $\min(\text{init}_i, \mathrm{env}(i))$ problem i kako ga zaobići pojmom „smrti” pozicije?''', r'''
<p>Segmentno stablo lako održava zbroj aritmetičkog niza na intervalu, ali ne i zbroj $\min$ dviju različitih stvari. Uočimo da $\mathrm{env}(i)$ s vremenom samo pada, a $\text{init}_i$ je konstanta: postoji prvi trenutak $T_i$ (indeks operacije tipa 1) nakon kojeg je $\mathrm{env}(i) \lt \text{init}_i$ – od tada zauvijek $b_i = \mathrm{env}(i)$, a prije toga $b_i = \text{init}_i$. Ako znamo sve $T_i$ unaprijed, stablo čuva po čvoru: zbroj $\text{init}$ po živim pozicijama, broj mrtvih, zbroj indeksa mrtvih i zbroj $\mathrm{env}$ po mrtvima; lijena dodjela pravca $A + B\,i$ na čvor daje $\sum_{\text{mrtvi}} \mathrm{env} = A\cdot\#\text{mrtvih} + B\cdot\sum\text{indeksa}$. „Ubijanje” pozicije je točkasto ažuriranje.</p>
'''),
        (r'''Kako izračunati sve trenutke smrti $T_i$ offline?''', r'''
<p>Za fiksni $i$ predikat „nakon prvih $t$ pravaca vrijedi $\mathrm{env}_t(i) \lt \text{init}_i$” je monoton u $t$ – binarno pretraživanje. Za sve $i$ odjednom koristimo paralelno binarno pretraživanje: rekurzija nad intervalom vremena $[lo, hi]$ i skupom pozicija $I$ (sortiranim po $i$); izgradimo donju ovojnicu pravaca $lo..mid$ (dodaju se u redoslijedu nerastućeg nagiba – klasična konstrukcija sa stogom i provjerom sjecišta u <code>__int128</code>), zatim za $i \in I$ rastućim redom pomičemo pokazivač po ovojnici (za veće $i$ pobjeđuju strmiji pravci) i dijelimo $I$ na one koji su mrtvi do $mid$ (idu u $[lo, mid]$) i ostale ($[mid+1, hi]$). Svaka razina obradi svaki pravac i svaku poziciju jednom, ukupno $O((n + K)\log K)$ gdje je $K$ broj upita tipa 1; $T_i = K$ znači „nikad”.</p>
'''),
        (r'''Kako se sve slaže u online obradu upita?''', r'''
<p>Prolazimo upite redom. Tip 2: $\mathrm{cnt} \mathrel{+}= 1$. Tip 1 (indeks $s$): izračunaj početak $p$ pravca na stogu ovojnice (izbacujući nadvladane pravce), dodijeli $v - c\, i$ na $[p, n]$ (ako $p \le n$), zatim ubij sve pozicije s $T_i = s$ (list preuzima svoj trenutačni pravac). Tip 3: zbroj (živi $\text{init}$ + mrtvi $\mathrm{env}$) na $[l, r]$ plus $\mathrm{cnt}\cdot\sum i$. Sve u $O(\log n)$ po operaciji.</p>
'''),
    ],
    'tips': [r'''<strong>Odvoji „globalni” dio.</strong> Operacije oblika „svima dodaj $g(i)$” gotovo uvijek se izvlače u globalni brojač, a druge operacije se preformuliraju u novoj koordinati – ovdje $\min$ s konstantom postaje $\min$ s pravcem.''',
             r'''Kad nagibi pravaca dolaze monotono, donja ovojnica je stog i svaki novi pravac djeluje na sufiks – to je „Li Chao bez Li Chaoa” i daje jednostavne range-assign operacije.''',
             r'''Ako se stanje svake pozicije mijenja monotono (prvo faza A pa trajno faza B), trenutak prelaska izračunaj offline paralelnim binarnim pretraživanjem; online dio tada održava samo zbrojeve po fazama.''',
             r'''Sjecišta pravaca s vrijednostima do $10^{12}$ i nagibima do $2\cdot 10^5$ traže <code>__int128</code> u usporedbama i pažljivo cjelobrojno zaokruživanje (floor-div s negativnim brojevima).'''],
    'solution': r'''
<p>Prema službenim skicama rješenja (SUA wiki, SDCPC 2023) i javnim analizama. Pišemo $a_i = b_i + \mathrm{cnt}\cdot i$ ($\mathrm{cnt}$ = broj dosadašnjih operacija tipa 2); tip 1 postaje $b_i = \min(b_i, v - \mathrm{cnt}\cdot i)$ – pravac s nagibom $-\mathrm{cnt}$, a nagibi su u vremenu sve strmiji. Zato je $b_i = \min(\text{init}_i, \mathrm{env}(i))$, gdje je donja ovojnica $\mathrm{env}$ stog pravaca i svaki novi pravac postaje minimum na sufiksu $[p, n]$ (dodjela aritmetičkog niza). Pozicija $i$ „umire” u prvom trenutku $T_i$ kad $\mathrm{env}(i) \lt \text{init}_i$ i od tada je $b_i = \mathrm{env}(i)$; sve $T_i$ računamo offline paralelnim binarnim pretraživanjem (donja ovojnica pravaca iz intervala vremena, upiti rastućim pokazivačem). Online segmentno stablo čuva zbroj $\text{init}$ po živima te broj, zbroj indeksa i zbroj $\mathrm{env}$ po mrtvima uz lijenu dodjelu pravca; upit tipa 3 je taj zbroj plus $\mathrm{cnt}\cdot\sum i$. Složenost $O((n + q)\log q)$.</p>
''',
    'detailed': r'''
<h3>1. Nova koordinata</h3>
<p>Neka je $\mathrm{cnt}$ broj dosad primijenjenih operacija tipa 2 i definirajmo $b_i$ s $a_i = b_i + \mathrm{cnt}\cdot i$; početno $b_i = \text{init}_i = a_i$. Tip 2: $\mathrm{cnt} \mathrel{+}= 1$, $b$ nepromijenjen. Tip 3: $\sum_{i=l}^r a_i = \sum_{i=l}^r b_i + \mathrm{cnt}\cdot\frac{(l+r)(r-l+1)}{2}$. Tip 1 s vrijednošću $v$: $a_i \le v \iff b_i \le v - \mathrm{cnt}\cdot i$, pa $b_i \leftarrow \min(b_i, \ell(i))$ za pravac $\ell(i) = v - c\,i$, $c = \mathrm{cnt}$ u tom trenutku. Vrijednosti: $|b_i| \le 10^{12} + 2\cdot 10^5 \cdot 2\cdot 10^5$, zbrojevi do $\approx 2\cdot 10^{17}$ – 64-bitni tip dovoljan.</p>
<h3>2. Ovojnica kao stog</h3>
<p>Nakon $t$ pravaca $b_i = \min(\text{init}_i, \mathrm{env}_t(i))$, $\mathrm{env}_t = \min_{j \le t} \ell_j$. Nagibi $-c_j$ su nerastući u $j$ (jer $\mathrm{cnt}$ ne pada). Lema: za dva pravca $\ell_j, \ell_{j'}$ s $c_j \lt c_{j'}$ skup $\{i : \ell_{j'}(i) \lt \ell_j(i)\}$ je sufiks ($v_{j'} - c_{j'} i \lt v_j - c_j i \iff i \gt \frac{v_{j'} - v_j}{c_{j'} - c_j}$). Zato najnoviji pravac (najstrmiji) nadvladava ovojnicu točno na nekom sufiksu $[p, n]$: $p$ je najmanji $i$ na kojem je novi pravac strogo manji od trenutačne ovojnice. Ovojnicu držimo kao stog $(v_j, c_j, \text{start}_j)$ s rastućim startovima; pri dodavanju novog pravca računamo $p$ iz sjecišta s vrhom stoga ($p = \lfloor (v - v_2)/(c - c_2) \rfloor + 1$ uz floor-div), i dok je $p \le \text{start}_{\text{vrh}}$ vrh je potpuno nadvladan – izbacimo ga i ponovimo. Ako je $c = c_{\text{vrh}}$, ostaje pravac s manjim $v$. Ako $p \gt n$, pravac je beskoristan. Inače pravac ulazi u stog i na $[p, n]$ dodjeljujemo $\mathrm{env}(i) := v - c\,i$ (aritmetički niz). Amortizirano $O(1)$ operacija stoga po pravcu.</p>
<h3>3. Smrt pozicije</h3>
<p>$\mathrm{env}_t(i)$ je nerastuće u $t$, $\text{init}_i$ konstanta. Neka je $T_i$ najmanji $t$ s $\mathrm{env}_t(i) \lt \text{init}_i$ (ili $K$, broj pravaca, ako takvog nema). Za $t \lt T_i$: $b_i = \text{init}_i$; za $t \ge T_i$: $b_i = \mathrm{env}_t(i)$. Ako su $T_i$ poznati, stablo čuva po čvoru: $\text{sumAlive}$ (zbroj $\text{init}$ po živima), $\text{cntDead}$, $\text{sumIdxDead}$, $\text{sumEnvDead}$ i lijenu dodjelu pravca $(A, B)$ koja postavlja $\text{sumEnvDead} = A\cdot\text{cntDead} + B\cdot\text{sumIdxDead}$. Dodjela na sufiks je standardna lijena operacija; ubijanje pozicije $i$ je točkasto: $\text{sumAlive} = 0$, $\text{cntDead} = 1$, $\text{sumIdxDead} = i$, $\text{sumEnvDead} = A + B\,i$ iz pravca koji list trenutačno nosi (nakon spuštanja lijenih dodjela). Odgovor upita tipa 3 je $\text{sumAlive} + \text{sumEnvDead}$ na $[l, r]$ plus $\mathrm{cnt}\cdot\sum i$.</p>
<h3>4. Paralelno binarno pretraživanje za $T_i$</h3>
<p>Predikat $P_i(t) = [\mathrm{env}_t(i) \lt \text{init}_i]$ je monoton u $t$. Funkcija $\mathrm{solve}(I, lo, hi)$ za skup pozicija $I$ (rastuće) s $T_i \in [lo, hi]$: ako je $lo = hi$, gotovo. Inače $mid = \lfloor (lo+hi)/2 \rfloor$; izgradimo donju ovojnicu pravaca $\ell_{lo}, \dots, \ell_{mid}$ – to je i $\mathrm{env}_{mid}$ ograničena na te pravce, a $P_i(mid)$ za $i \in I$ ovisi samo o njima? Ne sasvim: $\mathrm{env}_{mid}$ uključuje i pravce prije $lo$. No za $i \in I$ znamo $T_i \ge lo$, tj. $\mathrm{env}_{lo-1}(i) \ge \text{init}_i$, pa $\mathrm{env}_{mid}(i) \lt \text{init}_i$ vrijedi točno kad je minimum pravaca $lo..mid$ u $i$ manji od $\text{init}_i$. Ovojnicu gradimo stogom (pravci dolaze s nerastućim nagibom; srednji pravac je nepotreban kad se vanjski sijeku lijevo ili na sjecištu lijevog para – usporedba umnožaka u <code>__int128</code>; pravce jednakog nagiba zadrži samo s najmanjim $v$). Upite $i \in I$ obrađujemo rastuće s pokazivačem koji ide naprijed dok sljedeći pravac daje manju ili jednaku vrijednost (za veći $i$ pobjeđuju strmiji pravci, koji su kasnije na stogu). Pozicije s $P_i(mid)$ istinitim idu u $\mathrm{solve}(\cdot, lo, mid)$, ostale u $\mathrm{solve}(\cdot, mid+1, hi)$. Početni poziv $\mathrm{solve}(\{1..n\}, 0, K)$ s dogovorom $T_i = K$ = „nikad” (pravci su indeksirani $0..K-1$, a $t = K$ znači da niti svi pravci ne ubijaju $i$). Na svakoj od $O(\log K)$ razina zbroj veličina intervala pravaca je $\le K$ i zbroj veličina $I$ je $n$: $O((n + K)\log K)$.</p>
<h3>5. Online obrada</h3>
<ol>
<li>Učitaj sve upite, prikupi pravce $(v, c)$ tipa 1; izračunaj $T_i$; grupiraj pozicije po $T_i$.</li>
<li>Izgradi stablo s $\text{sumAlive} = \text{init}$.</li>
<li>Za upite redom: tip 2 → $\mathrm{cnt}{+}{+}$; tip 1 (indeks $s$) → stog ovojnice, eventualna dodjela na $[p, n]$, zatim ubij sve $i$ s $T_i = s$; tip 3 → upit.</li>
</ol>
<p>Ukupno $O((n + q)\log(n + q))$ vremena i $O(n + q)$ memorije.</p>
<h3>6. Zamke</h3>
<ul>
<li>Redoslijed u tipu 1: najprije dodjela pravca, zatim ubijanje – list mora preuzeti pravac koji ga je ubio.</li>
<li>Floor-dijeljenje s negativnim brojnikom ($v - v_2$ može biti negativan): ručna korekcija, ne <code>/</code> iz C-a.</li>
<li>Pravci jednakog nagiba (uzastopni tipovi 1 bez tipa 2 između) – i u stogu ovojnice i u PBS-u zadrži samo manji $v$.</li>
<li>Test gdje $\mathrm{env}(i) = \text{init}_i$ točno: pozicija nije mrtva (stroga nejednakost), ali vrijednost je ista pa oba tumačenja daju isti zbroj; bitno je da PBS i online koriste isti kriterij.</li>
<li>Kriva orijentacija usporedbe pri gradnji ovojnice prolazi male testove i pada na većim – provjeri predikat na tri konkretna pravca.</li>
</ul>
''',
    'verified': r'''uzorak 1/1; 300 slučajnih malih testova ($n \le 7$, $q \le 10$) protiv izravne simulacije, a dodatno $2000$ malih i niz srednjih testova (vrijednosti do $10^{12}$) istim brute forceom; 3 velika testa s $n = q = 2\cdot 10^5$ i vrijednostima do $10^{12}$ (najviše $0.14$ s).''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Computational Geometry', 'title_hr': 'Računalna geometrija', 'slug': 'E_computational_geometry',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je konveksan poligon $P$ s $n$ vrhova. Odaberi tri vrha $a, b, c$ u smjeru suprotnom od kazaljke na satu tako da od $b$ do $c$ (u tom smjeru) ima točno $k$ bridova poligona ($a$ nije krajnja točka tih bridova). Neka je $Q$ poligon omeđen dužinama $ab$, $ac$ i tih $k$ bridova (ima $k + 2$ stranice; $ab$ i $ac$ se smiju poklapati s bridovima $P$).</p>
<p>Nađi najveću moguću površinu $Q$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $3 \le n \le 10^5$, $1 \le k \le n - 2$; vrhovi $(x_i, y_i)$, $|x_i|, |y_i| \le 10^9$, u pozitivnom smjeru, površina pozitivna, bez ponovljenih vrhova (tri vrha mogu biti kolinearna). Zbroj $n$ ne prelazi $10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test realan broj; dopuštena relativna ili apsolutna greška $\lt 10^{-9}$.</p>
<h3>Primjer</h3>
<p>Trokut $(0,0),(1,0),(0,1)$, $k = 1$: $0.5$. Osmerokut $(1,2),(3,1),(5,1),(7,3),(8,6),(5,8),(3,7),(1,5)$, $k = 3$: $26.5$. Sedmerokut $(3,6),(1,1),(3,1),(7,1),(8,1),(5,6),(4,6)$, $k = 2$: $20$.</p>
''',
    'hints': [r'''
<p>Za fiksne $b = p_i$ i $c = p_{i+k}$ površina $Q$ je (površina dijela poligona između $b$ i $c$ uz lanac od $k$ bridova) + (površina trokuta $abc$). Prvi dio ne ovisi o $a$ – kako ga računati u $O(1)$?</p>
''', r'''
<p>Za fiksnu tetivu $bc$ najbolji $a$ je vrh preostalog lanca $c \to b$ najudaljeniji od pravca $bc$. Na konveksnom poligonu udaljenost vrhova od pravca duž lanca prvo raste pa pada (unimodalna), pa se maksimum može tražiti pomicanjem pokazivača.</p>
''', r'''
<p>Kad se $b$ i $c$ pomaknu za jedno mjesto u pozitivnom smjeru, optimalni $a$ se također pomiče samo u pozitivnom smjeru. Jedan pokazivač za $a$ koji nikad ne ide natrag daje $O(n)$ ukupno. Računaj s dvostrukim površinama u cijelim brojevima (<code>__int128</code>).</p>
'''],
    'coach': [
        (r'''Kako rastaviti površinu $Q$ na dio koji ne ovisi o $a$ i dio koji ovisi?''', r'''
<p>$Q$ je omeđen lancem od $k$ bridova $b = p_i, p_{i+1}, \dots, p_{i+k} = c$ te dužinama $ca$ i $ab$. Po formuli pertle (shoelace) dvostruka površina je $\sum_{j=i}^{i+k-1} (p_j \times p_{j+1}) + (c \times a) + (a \times b)$. Prvi zbroj je zbroj po lancu i računa se prefiksnim sumama vektorskih produkata (nad udvostručenim nizom vrhova, da se izbjegne omatanje indeksa); drugi dio je dvostruka orijentirana površina trokuta $b, c, a$, koji je za $a$ na lancu $c \to b$ pozitivno orijentiran. Sve je u cijelim brojevima.</p>
'''),
        (r'''Zašto je za fiksne $b, c$ funkcija $a \mapsto \mathrm{area}(abc)$ unimodalna duž lanca $c, c+1, \dots, b$?''', r'''
<p>Površina trokuta $abc$ proporcionalna je udaljenosti $a$ od pravca $bc$. Vrhovi konveksnog poligona između $c$ i $b$ leže na istoj strani pravca $bc$, a udaljenost od pravca je konkavna funkcija duž konveksnog lanca: gledajući projekciju na smjer okomit na $bc$, lanac se prvo udaljava, pa (nakon vrha gdje je tangenta paralelna s $bc$) približava. Zato je niz udaljenosti najprije nerastući pa nepadajući u obrnutom smjeru – točnije, ne raste nakon što jednom počne padati, pa se maksimum nalazi pomicanjem dok sljedeći vrh nije strogo lošiji (uz kolinearne vrhove dopuštamo pomak i pri jednakosti).</p>
'''),
        (r'''Zašto se optimalni $a$ pomiče monotono kad se par $(b, c)$ pomiče u pozitivnom smjeru?''', r'''
<p>Kad $b$ i $c$ prijeđu u $p_{i+1}$, $p_{i+k+1}$, pravac $bc$ se zarotira u pozitivnom smjeru (bridovi konveksnog poligona imaju monotono rastuće kutove smjera, a tetive $p_i p_{i+k}$ također). Vrh najudaljeniji od pravca zadanog smjera je vrh na kojem je tangenta paralelna tom smjeru, a on se po konveksnom poligonu pomiče u istom (pozitivnom) smjeru kako se kut rotira. Zato pokazivač $a$ nikad ne treba vraćati; treba samo osigurati $a \ne c$ i $a \ne b$, tj. držati ga u otvorenom lancu $(c, b)$.</p>
'''),
        (r'''Kako izbjeći greške pomičnog zareza uz koordinate do $10^9$?''', r'''
<p>Dvostruka površina je cijeli broj. Vektorski produkt dviju koordinata je do $2 \cdot 10^{18}$, a zbroj po lancu do $n$ takvih članova prelazi 64 bita, pa koristimo <code>__int128</code> za prefiksne sume i trokute. Rezultat je polovina cijelog broja: ispišemo cjelobrojni dio i <code>.5</code> ili <code>.0</code> – točno, bez gubitka preciznosti.</p>
'''),
    ],
    'tips': [r'''<strong>Rotirajući pokazivači.</strong> Na konveksnom poligonu „najudaljeniji vrh od pravca” pomiče se monotono kad se pravac monotono rotira – to je isti princip kao kod rotating calipers za najdalji par.''',
             r'''Kod zbrojeva po lancu vrhova uvijek koristi udvostručeni niz ($p_{i+n} = p_i$) s prefiksnim sumama, umjesto da ručno rješavaš omatanje indeksa.''',
             r'''Kad je odgovor „realan broj” ali je struktura zadatka cjelobrojna, računaj u cijelim brojevima (dvostruka površina) i tek na ispisu pretvori – preciznost $10^{-9}$ na brojevima reda $10^{18}$ inače nije dostižna u <code>double</code>.'''],
    'solution': r'''
<p>Prema javnim analizama natjecanja SDCPC 2023. Za $b = p_i$, $c = p_{i+k}$ dvostruka površina $Q$ je zbroj vektorskih produkata duž lanca $p_i, \dots, p_{i+k}$ (prefiksne sume nad udvostručenim nizom) plus dvostruka površina trokuta $bca$, koja je najveća za vrh $a$ preostalog lanca najudaljeniji od pravca $bc$. Zbog konveksnosti je udaljenost duž lanca unimodalna, a kad se $(b, c)$ pomakne za jedan vrh u pozitivnom smjeru, optimalni $a$ se pomiče samo u pozitivnom smjeru; jedan pokazivač za $a$ daje $O(n)$. Računamo u <code>__int128</code> i ispisujemo polovinu cijelog broja točno.</p>
''',
    'detailed': r'''
<h3>1. Formula za površinu $Q$</h3>
<p>Označimo vrhove $p_0, \dots, p_{n-1}$ u pozitivnom smjeru i produžimo niz ciklički ($p_{j+n} = p_j$). Za $b = p_i$, $c = p_{i+k}$ i $a = p_j$ s $i + k \lt j \lt i + n$ poligon $Q$ je $p_i, p_{i+1}, \dots, p_{i+k}, p_j$, također pozitivno orijentiran (konveksan poligon, vrhovi u redoslijedu). Po formuli pertle $$2 \cdot \mathrm{area}(Q) = \underbrace{\sum_{t=i}^{i+k-1} p_t \times p_{t+1}}_{C(i)} + \underbrace{p_{i+k} \times p_j + p_j \times p_i}_{T(i, j)},$$ gdje je $u \times v = u_x v_y - u_y v_x$. $C(i) = \mathrm{pre}[i+k] - \mathrm{pre}[i]$ uz prefiksne sume $\mathrm{pre}$ nad $2n$ vrhova. $T(i,j)$ je dvostruka orijentirana površina trokuta $(b, c, a)$; za $a$ na preostalom lancu je $\ge 0$.</p>
<h3>2. Najbolji $a$ za fiksni $i$ – unimodalnost</h3>
<p>$T(i, j)$ jednako je $|bc| \cdot h(j)$ gdje je $h(j)$ udaljenost $p_j$ od pravca $bc$ (svi $p_j$ na lancu su s iste strane). Tvrdnja: niz $h(i+k+1), h(i+k+2), \dots, h(i+n-1)$ je unimodalan (nepadajući, pa nerastući). Dokaz: uzmimo koordinatni sustav u kojem je $bc$ os $x$; $h$ je tada $y$-koordinata. Lanac $c \to b$ ide „iznad” osi, konveksan poligon znači da smjerovi bridova rotiraju monotono; dok je $y$-komponenta smjera brida pozitivna $h$ raste, a nakon što jednom postane negativna, zbog monotonosti kutova ostaje negativna do kraja lanca – pa $h$ pada. Kolinearni vrhovi daju jednake susjedne vrijednosti, što unimodalnost ne kvari. Zato je maksimum na prvom $j$ nakon kojega vrijednost strogo pada; pomičemo pokazivač dok je $T(i, j+1) \ge T(i, j)$.</p>
<h3>3. Monotonost pokazivača po $i$</h3>
<p>Neka je $a^*(i)$ najdesniji (u smislu indeksa) maksimum za $i$. Tvrdimo $a^*(i+1) \ge a^*(i)$ (kao indeksi u udvostručenom nizu). Vrh koji maksimizira udaljenost od pravca sa smjerom $\theta$ je vrh $p_j$ u kojem se smjer bridova prelazi iz „$\lt \theta$” u „$\gt \theta$” (mjereno relativno), tj. gdje je poligon „tangentan” na smjer $\theta$. Prijelaz $i \to i+1$ rotira tetivu $p_i p_{i+k}$ u pozitivnom smjeru za kut iz $[0, \pi)$ (kutovi tetiva fiksne duljine $k$ na konveksnom poligonu monotono rastu, kao i kutovi bridova), a tangentna točka se rotacijom smjera pomiče u pozitivnom smjeru po poligonu. Uz to $a$ mora ostati u $(c, b)$: kad $c$ prijeđe pokazivač, pomaknemo $a$ na $c + 1$. Ukupno pokazivač napravi $O(n)$ pomaka.</p>
<h3>4. Algoritam</h3>
<ol>
<li>Prefiksne sume $\mathrm{pre}[t] = \sum_{s \lt t} p_s \times p_{s+1}$ za $t \le 2n$, u <code>__int128</code>.</li>
<li>$a := k + 1$. Za $i = 0, \dots, n-1$: $c := i + k$; $a := \max(a, c + 1)$; dok je $a + 1 \le i + n - 1$ i $T(i, a+1) \ge T(i, a)$: $a := a + 1$. Kandidat: $C(i) + T(i, a)$.</li>
<li>Maksimum $M$ (dvostruka površina) ispiši kao $\lfloor M/2 \rfloor$ i <code>.5</code> ako je $M$ neparan, inače <code>.0</code>.</li>
</ol>
<p>Vrijeme $O(n)$ po testu, memorija $O(n)$.</p>
<h3>5. Točnost i zamke</h3>
<ul>
<li>Koordinate do $10^9$: pojedini produkt do $2 \cdot 10^{18}$ stane u 64 bita, ali prefiksne sume i zbroj triju produkata ne moraju – <code>__int128</code> je najjednostavnije.</li>
<li>$k = n - 2$: lanac $(c, b)$ ima točno jedan vrh; petlja pokazivača ne radi ništa, $a = c + 1$.</li>
<li>Kolinearni vrhovi: uvjet $\ge$ u pomicanju pokazivača dopušta prelazak preko jednakih vrijednosti, što je nužno da pokazivač ne „zaglavi” ispred pravog maksimuma za sljedeći $i$.</li>
<li>Ispis: dopuštena greška je relativna ili apsolutna $10^{-9}$; egzaktan ispis s <code>.5</code>/<code>.0</code> uklanja svaku dvojbu.</li>
</ul>
''',
    'verified': r'''uzorci 1/1 (tri testa iz zadatka); 300 slučajnih malih testova (konveksne ljuske $3$–$12$ slučajnih točaka, koordinate do $20$ ili do $10^9$, uz kolinearne vrhove) protiv brute forcea koji isprobava sve dopuštene trojke, usporedba s tolerancijom $10^{-9}$; 3 velika testa s $n \approx 10^5$ vrhova na kružnici radijusa $10^9$ (najviše $0.01$ s).''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Puzzle: Sashigane', 'title_hr': 'Zagonetka: Sashigane', 'slug': 'F_puzzle_sashigane',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Ploča $n \times n$ ima točno jedno crno polje $(b_i, b_j)$; ostala su bijela. Pokrij sva bijela polja L-oblicima tako da je svako bijelo polje pokriveno točno jednim L-oblikom, crno nijednim, a oblici ne izlaze iz ploče.</p>
<p>L-oblik je zadan s $(r, c, h, w)$: $(r, c)$ je pregib, $h \ne 0$ i $w \ne 0$ zadaju smjer i duljinu krakova, $1 \le r + h \le n$, $1 \le c + w \le n$. Oblik sadrži polja $(i, c)$ za $i$ između $r$ i $r + h$ te polja $(r, j)$ za $j$ između $c$ i $c + w$.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 10^3$, $1 \le b_i, b_j \le n$.</p>
<h3>Izlaz</h3>
<p>Ako rješenje postoji, <code>Yes</code>, zatim broj oblika $k$ ($0 \le k \le \frac{n^2 - 1}{3}$) i $k$ redaka <code>r c h w</code>; bilo koje ispravno rješenje se prihvaća. Inače <code>No</code>.</p>
<h3>Primjer</h3>
<p>$n = 5$, crno $(3,4)$: <code>Yes</code>, npr. $6$ oblika <code>5 1 -1 3</code>, <code>1 2 1 3</code>, <code>3 1 -2 1</code>, <code>4 3 -1 -1</code>, <code>4 5 1 -1</code>, <code>2 5 1 -2</code>. $n = 1$: <code>Yes</code>, $0$.</p>
''',
    'hints': [r'''
<p>Ne pokušavaj popločiti odmah cijelu ploču. Postoji li mali kvadrat oko crnog polja koji je već „gotov”, i kako ga povećati za jedan red i jedan stupac odjednom?</p>
''', r'''
<p>Novi red i novi stupac uz kvadrat $s \times s$ imaju zajedničko kutno polje – zajedno čine točno jedan L-oblik s krakovima duljine $s$. Kvadrat $s \times s$ tako postaje $(s+1) \times (s+1)$.</p>
''', r'''
<p>Rast biraj u smjeru u kojem još ima mjesta (dolje ako $D \lt n$, inače gore; desno ako $R \lt n$, inače lijevo). Kvadrat raste u obje dimenzije za $1$ u svakom koraku, pa nakon $n-1$ koraka pokriva cijelu ploču. Odgovor je uvijek <code>Yes</code>.</p>
'''],
    'coach': [
        (r'''Kad je zadatak „pokrij sve osim jednog polja”, koji je najmanji podslučaj koji je trivijalno riješen i može li se rješenje širiti?''', r'''
<p>Najmanji riješen slučaj je kvadrat $1 \times 1$ koji se sastoji samo od crnog polja: sva njegova bijela polja (nijedno) pokrivena su. Ako uspijemo dokazati da se svaki riješeni kvadrat $s \times s$ (koji sadrži crno polje) može proširiti na riješeni kvadrat $(s+1) \times (s+1)$ unutar ploče, indukcija daje rješenje za cijelu ploču $n \times n$.</p>
'''),
        (r'''Zašto novi red i novi stupac oko kvadrata tvore točno jedan L-oblik?''', r'''
<p>Dodamo li kvadratu $[U,D] \times [L,R]$ red $r$ (ispod ili iznad) i stupac $c$ (desno ili lijevo), nova polja su $(r, j)$ za $j \in [L, R]$, $(i, c)$ za $i \in [U, D]$ i kutno polje $(r, c)$. To je upravo L-oblik s pregibom u $(r, c)$: jedan krak ide po stupcu $c$ preko starih redaka (duljina $s = D-U+1$), a drugi po retku $r$ preko starih stupaca (duljina $s$). Krakovi su neprazni jer je $s \ge 1$, pa je $h, w \ne 0$ zadovoljeno.</p>
'''),
        (r'''Kako osigurati da kvadrat nikad ne „izađe” iz ploče?''', r'''
<p>Dok je $s \lt n$, kvadrat ne može istodobno dodirivati i gornji i donji rub (imao bi $n$ redaka), pa postoji barem jedan slobodan smjer po redcima; isto za stupce. Biramo dolje ako je $D \lt n$, inače gore; desno ako je $R \lt n$, inače lijevo. Svaki korak povećava $s$ za $1$, pa nakon točno $n-1$ koraka kvadrat je cijela ploča.</p>
'''),
        (r'''Zadovoljava li konstrukcija ograničenje na broj oblika $k \le \frac{n^2-1}{3}$?''', r'''
<p>Koristimo $n-1$ oblika. Svaki L-oblik ima barem $3$ polja, a bijelih polja je $n^2 - 1$, pa svako rješenje ima najviše $\frac{n^2-1}{3}$ oblika – to je i razlog ograničenja. Za $n \ge 2$ je $n - 1 \le \frac{n^2-1}{3}$ jer je $3 \le n+1$; za $n = 1$ ispisujemo $0$ oblika.</p>
'''),
    ],
    'tips': [r'''<strong>Induktivno širenje.</strong> U konstruktivnim zadacima na mreži često je najlakše naći „jedan potez koji povećava riješeno područje za jedan red i jedan stupac” nego globalno popločavanje.''',
             r'''Kod L-oblika zapamti da negativan $h$ ili $w$ znači krak prema gore, odnosno ulijevo; provjeri na primjeru iz zadatka kako se predznaci čitaju prije nego što pišeš izlaz.''',
             r'''Za svaki konstruktivni zadatak napiši vlastiti validator (svako polje pokriveno točno jednom, oblici unutar ploče) i vrti ga na svim malim $n$ i svim položajima crnog polja – to je jedini pouzdan test.'''],
    'solution': r'''
<p>Prema javnim analizama natjecanja (SDCPC 2023) rješenje uvijek postoji i gradi se induktivno. Krenemo od kvadrata $1 \times 1$ koji sadrži crno polje. Dok je kvadrat manji od ploče, dodamo mu jedan novi red (ispod ako ima mjesta, inače iznad) i jedan novi stupac (desno ako ima mjesta, inače lijevo): novi red i stupac zajedno čine točno jedan L-oblik s pregibom u njihovom zajedničkom kutnom polju i krakovima duljine $s$ (trenutna stranica kvadrata). Nakon $n-1$ koraka kvadrat je cijela ploča, a svako bijelo polje pokriveno je točno jednom. Složenost $O(n)$, izlaz ima $n-1$ oblika.</p>
''',
    'detailed': r'''
<h3>1. Ključno opažanje: L-oblik je „okvir” kvadrata</h3>
<p>Promotrimo kvadrat $[U, D] \times [L, R]$ stranice $s = D - U + 1$ i pretpostavimo da su sva njegova bijela polja već pokrivena. Ako ploča ima još redaka ispod (ili iznad) i još stupaca desno (ili lijevo), dodajmo red $r$ i stupac $c$ koji se naslanjaju na kvadrat. Nova polja su: $(i, c)$ za $i \in [U, D]$, $(r, j)$ za $j \in [L, R]$ i kutno polje $(r, c)$. Upravo to je definicija L-oblika s pregibom $(r, c)$: krak po stupcu $c$ prema starim redcima i krak po retku $r$ prema starim stupcima. Oba kraka imaju duljinu $s \ge 1$, pa je $h \ne 0$ i $w \ne 0$. Time kvadrat stranice $s$ postaje riješen kvadrat stranice $s + 1$.</p>
<h3>2. Indukcija i izbor smjera</h3>
<p>Baza: kvadrat $1 \times 1$ koji je samo crno polje $(b_i, b_j)$ – nema bijelih polja, pa je trivijalno riješen. Korak: dok je $s \lt n$, kvadrat ne dodiruje oba horizontalna ruba (inače bi imao $n$ redaka), pa je barem jedan od smjerova „dolje” ($D \lt n$) i „gore” ($U \gt 1$) slobodan; analogno za stupce. Odaberemo dolje ako je moguće, inače gore; desno ako je moguće, inače lijevo. Nakon koraka kvadrat je i dalje unutar ploče, a $s$ je porastao za $1$. Nakon $n - 1$ koraka $s = n$, tj. kvadrat je cijela ploča i sva bijela polja su pokrivena točno jednom (svaki L pokriva samo nova polja svog koraka, a crno polje nikad nije „novo”).</p>
<h3>3. Zapis L-oblika</h3>
<p>Ako je novi red $r = D + 1$ (rast dolje), krak po stupcu mora ići prema gore preko redaka $U..D$, dakle $h = -s$; ako je $r = U - 1$, onda $h = +s$. Analogno $w = -s$ kad je $c = R + 1$, a $w = +s$ kad je $c = L - 1$. Oblik je $(r, c, h, w)$ i vrijedi $1 \le r + h \le n$, $1 \le c + w \le n$ jer su $r + h$ i $c + w$ redom suprotni rub starog kvadrata.</p>
<h3>4. Algoritam i složenost</h3>
<ol>
<li>$U = D = b_i$, $L = R = b_j$.</li>
<li>Dok je $D - U + 1 \lt n$: odredi $r$, $c$, $h$, $w$ kao gore, zapiši oblik, proširi $U/D$ i $L/R$.</li>
<li>Ispiši <code>Yes</code>, broj oblika $n - 1$ i oblike.</li>
</ol>
<p>Svaki korak je $O(1)$, ukupno $O(n)$ vremena i $O(n)$ izlaza. Ograničenje $k \le \frac{n^2-1}{3}$ zadovoljeno je jer je $n - 1 \le \frac{n^2 - 1}{3}$ za $n \ge 2$ (ekvivalentno $3 \le n + 1$), a za $n = 1$ ispisujemo $k = 0$.</p>
<h3>5. Rubni slučajevi i zamke</h3>
<ul>
<li>$n = 1$: petlja se ne izvršava, izlaz je <code>Yes</code> i $0$ – ne smije se ispisati prazan redak s oblicima krivo formatiran.</li>
<li>Crno polje u kutu: smjerovi rasta su cijelo vrijeme isti (npr. dolje-desno); crno polje u sredini: kad kvadrat dotakne rub, smjer se mijenja – provjeri da se odluka donosi u svakom koraku, ne jednom na početku.</li>
<li>Predznaci $h$ i $w$: lako ih je zamijeniti; validator koji broji pokrivenost svakog polja otkriva grešku odmah.</li>
</ul>
''',
    'verified': r'''uzorci 2/2 (uz vlastiti validator: <code>Yes</code>, oblici unutar ploče, svako bijelo polje pokriveno točno jednom, crno nijednom, $k \le (n^2-1)/3$); 300 slučajnih testova s $n \le 12$ i slučajnim položajem crnog polja kroz validator; 3 velika testa s $n = 1000$ ($\lt 0.01$ s).''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Gem Island 2', 'title_hr': 'Otok dragulja 2', 'slug': 'G_gem_island_2',
    'tl': '2 s', 'ml': '1024 MiB',
    'statement': r'''
<p>$n$ kutija u nizu, u svakoj početno jedna kuglica. Točno $d$ puta: odaberi uniformno slučajno kuglicu među svima i u njezinu kutiju dodaj još jednu (u $i$-toj operaciji svaka kuglica ima vjerojatnost $\frac{1}{n + i - 1}$). Neka su brojevi kuglica poredani nerastuće $a_1 \ge a_2 \ge \dots \ge a_n$.</p>
<p>Izračunaj očekivanje $\sum_{i=1}^{r} a_i$ modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$1 \le n, d \le 1.5 \cdot 10^7$, $1 \le r \le n$.</p>
<h3>Izlaz</h3>
<p>Jedan broj.</p>
<h3>Primjer</h3>
<p>$(2, 3, 1) \to 499122180$; $(3, 3, 2) \to 698771052$; $(5, 10, 3) \to 176512750$.</p>
''',
    'hints': [r'''
<p>Poredaj sve kuglice u red; korak „odaberi kuglicu i dodaj novu u njezinu kutiju” je isto što i „dodaj novu kuglicu odmah iza odabrane”. Koliko je vjerojatan pojedini konačni raspored $(x_1, \dots, x_n)$, $x_i \ge 1$, $\sum x_i = n + d$?</p>
''', r'''
<p>Svi rasporedi su jednako vjerojatni (Pólyina urna), ukupno $\binom{n+d-1}{n-1}$. Zbroj $r$ najvećih je $\sum_{t \ge 1} \min(r, \#\{i : x_i \ge t\})$. Za svaki par $(t, j)$ prebroj rasporede s <em>točno</em> $j$ kutija $\ge t$ binomnom inverzijom iz „zadano $j$ kutija ima $\ge t$”: $\binom{n}{j}\binom{n+d-1-j(t-1)}{n-1}$.</p>
''', r'''
<p>Zamjenom redoslijeda sumiranja koeficijent uz $\binom{n}{j} S_j$, gdje je $S_j = \sum_{t} \binom{n-1+d-j(t-1)}{n-1}$, postaje jednostavan binomni izraz; $S_j$ za sve $j$ odjednom je zbroj po višekratnicima, tj. Dirichletova sufiksna suma u $O(d \log\log d)$.</p>
'''],
    'coach': [
        (r'''Zašto su svi konačni rasporedi kuglica jednako vjerojatni?''', r'''
<p>Proces je Pólyina urna: kutija s $s$ kuglica bira se s težinom $s$. Fiksirajmo raspored $(x_1, \dots, x_n)$ i jedan konkretan redoslijed kojim kutije dobivaju svoje nove kuglice. Vjerojatnost tog redoslijeda je $\frac{\prod_k 1\cdot 2\cdots(x_k-1)}{\prod_{i=0}^{d-1}(n+i)} = \frac{\prod_k (x_k-1)!}{\prod_{i=0}^{d-1}(n+i)}$ – nazivnici su ukupni brojevi kuglica po koracima, a brojnici težine odabranih kutija, koji se samo permutiraju ako promijenimo redoslijed. Redoslijeda s istim brojevima je $\frac{d!}{\prod_k (x_k-1)!}$, pa je $P(x) = \frac{d!}{n(n+1)\cdots(n+d-1)} = \binom{n+d-1}{n-1}^{-1}$, neovisno o $x$. Vjerojatnosni zadatak postaje brojanje kompozicija.</p>
'''),
        (r'''Kako zbroj $r$ najvećih pretvoriti u brojanje?''', r'''
<p>Za nenegativne cijele $x_i$: $x_i = \sum_{t \ge 1} [x_i \ge t]$. Zbroj $r$ najvećih je stoga $\sum_{t \ge 1} \min\big(r, \#\{i : x_i \ge t\}\big)$ – na razini $t$ doprinose sve kutije s bar $t$ kuglica, ali najviše $r$ njih (najvećih). Zato je očekivanje $\frac{1}{N}\sum_{t}\sum_{j} \min(r, j) \cdot E(t, j)$, gdje je $E(t,j)$ broj rasporeda s točno $j$ kutija $\ge t$ i $N = \binom{n+d-1}{n-1}$.</p>
'''),
        (r'''Kako izbrojiti rasporede s točno $j$ kutija koje imaju bar $t$ kuglica?''', r'''
<p>Lakše je „zadano $j$ kutija ima $\ge t$”: oduzmemo im po $t - 1$ kuglica i preostaje kompozicija zbroja $n + d - j(t-1)$ na $n$ pozitivnih dijelova: $A_j(t) = \binom{n}{j}\binom{n+d-1-j(t-1)}{n-1}$. Binomna inverzija daje točno-$j$: $E(t,j) = \sum_{i \ge j} (-1)^{i-j}\binom{i}{j} A_i(t)$. Sumiranje po $t$ i $j$ i zamjena redoslijeda daje odgovor oblika $\frac{1}{N}\sum_{i} c_i \binom{n}{i} S_i$, gdje je $S_i = \sum_{t \ge 1}\binom{n-1+d-i(t-1)}{n-1}$ i $c_i = \sum_{j \le i} \min(r,j)(-1)^{i-j}\binom{i}{j}$.</p>
'''),
        (r'''Kako se koeficijent $c_i$ pojednostavljuje?''', r'''
<p>$c_i = \sum_{j=0}^{i} \min(r, j) (-1)^{i-j}\binom{i}{j}$ je $i$-ta konačna razlika niza $\min(r, j)$. Niz je linearan ($=j$) do $r$ pa konstantan; razlike višeg reda linearnog niza su $0$, pa je $c_1 = 1$ i $c_i = 0$ za $2 \le i \le r$. Za $i \gt r$ raspišemo $\min(r,j) = j - \max(0, j - r)$: prvi dio daje $0$, a $\sum_j (j - r)^+ (-1)^{i-j}\binom{i}{j} = (-1)^{i-r}\binom{i-2}{r-1}$ (konačna razlika „odrezanog” linearnog niza; provjera indukcijom ili malim brute forceom). Dakle $c_i \in \{0, \pm\binom{i-2}{r-1}\}$ – bez dodatnih suma.</p>
'''),
        (r'''Kako izračunati sve $S_i$ u vremenu bližem $O(d)$?''', r'''
<p>$S_i = \sum_{t \ge 1} h(i(t-1))$ uz $h(x) = \binom{n-1+d-x}{n-1}$ za $0 \le x \le d$ (izvan toga $0$): $S_i = h(0) + \sum_{m \ge 1,\ im \le d} h(im)$. Zbrojevi po višekratnicima za sve $i$ odjednom su Dirichletova sufiksna suma: za svaki prosti $p$ i $x$ od $\lfloor d/p \rfloor$ prema dolje: $H(x) \mathrel{+}= H(px)$. Nakon prolaza po svim prostima $H(i) = \sum_{m \ge 1} h(im)$, u $O(d \log\log d)$. Vrijednosti $h$ računamo unatrag iz $h(d) = 1$ množenjem s $\frac{n+d-x}{d-x+1}$ uz linearno predizračunate inverze.</p>
'''),
    ],
    'tips': [r'''<strong>Prepoznaj Pólyinu urnu.</strong> „Odaberi slučajnu kuglicu i dodaj još jednu iste vrste” daje uniformnu razdiobu nad kompozicijama – time se vjerojatnosni zadatak pretvara u čisto brojanje.''',
             r'''Zbroj $k$ najvećih $= \sum_t \min(k, \#\{x_i \ge t\})$ – rastavljanje po pragovima $t$ zamjenjuje sortiranje brojanjem, a „točno $j$” iz „bar $j$” dobiva se binomnom inverzijom.''',
             r'''Kad ti treba $\sum_m g(im)$ za sve $i$, to je Dirichletova (sufiksna) suma: $O(d \log\log d)$ prolazom po prostim brojevima umjesto harmonijskog $O(d \log d)$; uz $d = 1.5\cdot 10^7$ razlika je osjetna.''',
             r'''Za $1.5 \cdot 10^7$ inverza koristi linearnu formulu $\mathrm{inv}[i] = -\lfloor p/i \rfloor \cdot \mathrm{inv}[p \bmod i]$ i 32-bitne polja – memorija i vrijeme su tu kritični.'''],
    'solution': r'''
<p>Prema javnim analizama natjecanja SDCPC 2023. Nakon $d$ koraka svaki raspored $(x_1, \dots, x_n)$, $x_i \ge 1$, $\sum x_i = n + d$ jednako je vjerojatan (Pólyina urna), ukupno $N = \binom{n+d-1}{n-1}$. Zbroj $r$ najvećih je $\sum_{t \ge 1}\min(r, \#\{i : x_i \ge t\})$; broj rasporeda u kojima zadanih $j$ kutija ima $\ge t$ je $\binom{n}{j}\binom{n-1+d-j(t-1)}{n-1}$, a binomna inverzija i zamjena redoslijeda sumiranja daju $$\text{odgovor} = \frac{1}{N}\sum_{j=1}^{n} c_j \binom{n}{j} S_j,\quad S_j = \sum_{m \ge 0,\ jm \le d} \binom{n-1+d-jm}{n-1},$$ s $c_1 = 1$, $c_j = 0$ za $2 \le j \le r$ i $c_j = (-1)^{j-r}\binom{j-2}{r-1}$ za $j \gt r$. Sve $S_j$ dobivamo Dirichletovom sufiksnom sumom nad $h(x) = \binom{n-1+d-x}{n-1}$ u $O(d \log\log d)$; ukupno $O(n + d \log\log d)$.</p>
''',
    'detailed': r'''
<h3>1. Uniformnost rasporeda</h3>
<p>Proces je Pólyina urna s $n$ boja i početno jednom kuglicom svake boje. Tvrdnja: nakon $d$ koraka vjerojatnost svakog rasporeda $(x_1, \dots, x_n)$ s $x_i \ge 1$ i $\sum x_i = n+d$ jednaka je $1/N$, $N = \binom{n+d-1}{n-1}$. Dokaz: vjerojatnost da kutije redom dobiju kuglice u zadanom nizu boja (npr. najprije $x_1 - 1$ puta kutija $1$, itd.) jednaka je $\prod_i \frac{(x_i-1)!}{\,} \big/ \prod_{i=0}^{d-1}(n+i)$ – brojnik je $\prod_k 1 \cdot 2 \cdots (x_k - 1)$ jer kutija s $s$ kuglica ima težinu $s$. Bilo koji drugi redoslijed boja s istim brojevima daje isti umnožak (samo se faktori permutiraju), a takvih redoslijeda je $\frac{d!}{\prod_k (x_k-1)!}$. Ukupno $P(x) = \frac{d!}{\prod_{i=0}^{d-1}(n+i)} = \frac{d!\,(n-1)!}{(n+d-1)!} = \frac{1}{N}$, neovisno o $x$.</p>
<h3>2. Zbroj $r$ najvećih kao brojanje po pragovima</h3>
<p>Za sortirani raspored, $\sum_{i \le r} a_i = \sum_{t \ge 1} \min\big(r, \#\{i : x_i \ge t\}\big)$ jer na razini $t$ doprinos daje svaka od $r$ najvećih kutija koja ima $\ge t$ kuglica, a to je točno $\min(r, \#\{x_i \ge t\})$. Stoga $$\mathbb{E} = \frac{1}{N}\sum_{t \ge 1}\sum_{j=0}^{n} \min(r, j)\, E(t, j),$$ gdje je $E(t,j)$ broj rasporeda s točno $j$ kutija $\ge t$.</p>
<h3>3. Binomna inverzija</h3>
<p>Neka je $A_j(t) = \binom{n}{j}\binom{n-1+d-j(t-1)}{n-1}$ broj parova (skup od $j$ kutija, raspored u kojem te kutije imaju $\ge t$): oduzmemo tim kutijama po $t-1$ kuglica i preostane kompozicija broja $n+d-j(t-1)$ na $n$ pozitivnih dijelova (binom je $0$ ako je $n-1+d-j(t-1) \lt n-1$). Vrijedi $A_j(t) = \sum_{i \ge j}\binom{i}{j}E(t,i)$, pa inverzijom $E(t,j) = \sum_{i \ge j}(-1)^{i-j}\binom{i}{j}A_i(t)$. Uvrštavanjem: $$\sum_j \min(r,j) E(t,j) = \sum_i A_i(t)\underbrace{\sum_{j \le i}\min(r,j)(-1)^{i-j}\binom{i}{j}}_{c_i}.$$ Sumiranje po $t$: $\sum_t A_i(t) = \binom{n}{i} S_i$, $S_i = \sum_{t \ge 1} h\big(i(t-1)\big)$, $h(x) = \binom{n-1+d-x}{n-1}$ za $0 \le x \le d$.</p>
<h3>4. Koeficijenti $c_i$</h3>
<p>$c_i = \Delta^i \min(r, \cdot)(0)$ je $i$-ta konačna razlika niza $u_j = \min(r,j)$ u $0$. Pišemo $u_j = j - (j-r)^+$. Za linearni dio: $\Delta^1 j = 1$ u $j=0$, a $\Delta^i j = 0$ za $i \ge 2$. Za $v_j = (j-r)^+$: $v_j = 0$ za $j \le r$, pa $\Delta^i v(0) = 0$ za $i \le r$; općenito $\Delta^i v(0) = \sum_j (-1)^{i-j}\binom{i}{j}(j-r)^+$. Kako je $(j-r)^+ = \sum_{s \ge r+1}[j \ge s]$ i $\sum_j (-1)^{i-j}\binom{i}{j}[j \ge s] = (-1)^{i-s}\binom{i-1}{s-1}$ (za $1 \le s \le i$), dobivamo $\Delta^i v(0) = \sum_{s=r+1}^{i}(-1)^{i-s}\binom{i-1}{s-1} = (-1)^{i-r-1}\binom{i-2}{r-1}$ (alternirajuća suma binoma). Dakle $c_1 = 1$, $c_i = 0$ za $2 \le i \le r$, i $c_i = (-1)^{i-r}\binom{i-2}{r-1}$ za $i \gt r$. Za $r = n$ svi $c_i$ s $i \gt r$ ne postoje pa je odgovor $\frac{1}{N}\binom{n}{1}S_1 = n + d$, kao što i mora biti.</p>
<h3>5. Računanje $S_i$: Dirichletova sufiksna suma</h3>
<p>$S_i = h(0) + \sum_{m \ge 1,\ im \le d} h(im)$. Definiramo $H(x) = \sum_{m \ge 1} h(mx)$ za $1 \le x \le d$; to je „sufiksna suma po djeljivosti”. Računa se prolazom po prostim brojevima $p \le d$ (sito), za svaki $p$ i $x = \lfloor d/p \rfloor, \dots, 1$: $H(x) \mathrel{+}= H(px)$. Ispravnost: svaki višekratnik $mx$ zbroji se točno jednom, po redoslijedu prostih faktora $m$ (standardni argument za Dirichletove prefiksne/sufiksne sume, analogno višedimenzionalnim prefiksnim sumama po eksponentima prostih brojeva). Složenost $O(d \log\log d)$. Vrijednosti $h(x)$ za $x = d, d-1, \dots, 0$: $h(d) = 1$, $h(x-1) = h(x)\cdot\frac{n+d-x}{d-x+1}$, uz linearno predizračunate inverze do $\max(n,d)+2$.</p>
<h3>6. Algoritam i složenost</h3>
<ol>
<li>Linearni inverzi; $h$ unatrag; $N = h(0)$.</li>
<li>Dirichletova sufiksna suma $H$.</li>
<li>Za $j = 1..n$: održavaj $\binom{n}{j}$ i $\binom{j-2}{r-1}$ inkrementalno; $S_j = h(0) + H(j)$ (za $j \le d$, inače $h(0)$); akumuliraj $c_j\binom{n}{j}S_j$.</li>
<li>Odgovor pomnoži s $N^{-1}$.</li>
</ol>
<p>Vrijeme $O(n + d\log\log d)$, memorija tri 32-bitna polja veličine $\approx 1.5 \cdot 10^7$ (oko $180$ MB uz ograničenje $1024$ MiB).</p>
<h3>7. Zamke</h3>
<ul>
<li>$j \gt d$: $S_j = h(0)$ (samo $m = 0$).</li>
<li>$r = n$ odgovor je $n + d$; $n = 1$ isto. $d \lt n$ ne mijenja ništa u formulama.</li>
<li>Binome $\binom{j-2}{r-1}$ računaj inkrementalno ($\binom{j-2}{r-1} = \binom{j-3}{r-1}\cdot\frac{j-2}{j-1-r}$), a ne faktorijelima do $n$ – i to je $O(n)$ ali s manje memorije.</li>
<li>Koristi <code>unsigned int</code> za velika polja i pazi da $H(x) + H(px)$ ne prelije prije redukcije modulo.</li>
</ul>
''',
    'verified': r'''uzorci 3/3; 300 slučajnih malih testova ($n \le 5$, $d \le 6$) protiv brute forcea koji točnom racionalnom aritmetikom simulira cijelu razdiobu procesa; 3 velika testa s $n, d$ do $1.5 \cdot 10^7$ (najviše $0.53$ s).''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Not Another Path Query Problem', 'title_hr': 'Ne još jedan upit o putovima', 'slug': 'H_not_another_path_query_problem',
    'tl': '4 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Graf s $n$ vrhova i $m$ neusmjerenih bridova težina $w_i$. Vrijednost puta je bitovni AND težina svih bridova na njemu. Za konstantu $V$ i svaki od $q$ upita $(u, v)$ odredi postoji li put od $u$ do $v$ vrijednosti barem $V$.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 10^5$, $0 \le m \le 5 \cdot 10^5$, $1 \le q \le 5 \cdot 10^5$, $0 \le V \lt 2^{60}$; bridovi $u_i \ne v_i$, $0 \le w_i \lt 2^{60}$ (mogući višestruki bridovi); upiti $u_i \ne v_i$.</p>
<h3>Izlaz</h3>
<p>Za svaki upit <code>Yes</code> ili <code>No</code>.</p>
<h3>Primjer</h3>
<p>$n = 9$, $V = 5$, bridovi $(1,2,8), (1,3,7), (2,4,1), (3,4,14), (2,5,9), (4,5,7), (5,6,6), (3,7,15)$: upiti $(1,6), (2,7), (7,6), (1,8)$ daju <code>Yes</code>, <code>No</code>, <code>Yes</code>, <code>No</code> (npr. $1 \to 3 \to 4 \to 5 \to 6$ ima vrijednost $7 \,\&\, 14 \,\&\, 7 \,\&\, 6 = 6 \ge 5$). $n = 3$, $V = 4$, bridovi $(1,2,3), (1,2,5), (2,3,2), (2,3,6)$, upit $(1,3)$: <code>Yes</code> ($5 \,\&\, 6 = 4$).</p>
''',
    'hints': [r'''
<p>Uvjet „AND svih težina $\ge V$” razloži po bitovima: dva broja se uspoređuju po najvišem bitu na kojem se razlikuju. Koje su sve mogućnosti da rezultat bude $\ge V$?</p>
''', r'''
<p>Ili je AND jednak $V$, ili postoji bit $i$ na kojem $V$ ima $0$, AND ima $1$, a svi viši bitovi su jednaki. Za fiksni $i$ to znači da <em>svaka</em> težina na putu sadrži masku $M_i$ = (viši bitovi od $V$, bit $i$ postavljen); niži bitovi su nevažni.</p>
''', r'''
<p>Maski ima najviše $61$. Za svaku zadrži samo bridove čija težina sadrži masku i izgradi komponente povezanosti (DSU). Upit $(u, v)$ je <code>Yes</code> ako su $u$ i $v$ u istoj komponenti za bar jednu masku.</p>
'''],
    'coach': [
        (r'''Kako se uvjet $x \ge V$ za AND-vrijednost puta može svesti na uvjete o pojedinim bitovima?''', r'''
<p>Za nenegativne cijele brojeve $x \ge V$ vrijedi točno onda kad je $x = V$ ili kad na najvišem bitu $i$ na kojem se razlikuju $x$ ima $1$ a $V$ ima $0$. U drugom slučaju bitovi iznad $i$ su jednaki bitovima $V$, bit $i$ je $1$, a bitovi ispod $i$ mogu biti bilo što. Dakle $x \ge V$ je unija od najviše $61$ „uzoraka”: $x = V$ te, za svaki $i$ s $V_i = 0$, uzorak $M_i = \left(\lfloor V / 2^{i} \rfloor \,|\, 1\right) \cdot 2^{i}$ u smislu „$x$ sadrži sve bitove od $M_i$”.</p>
'''),
        (r'''Zašto je „AND puta sadrži masku $M$” ekvivalentno tome da svaki brid na putu sadrži $M$?''', r'''
<p>AND više brojeva ima bit $j$ postavljen točno onda kad ga imaju svi. Zato $(w_1 \,\&\, \dots \,\&\, w_t) \,\&\, M = M$ vrijedi točno kada $w_k \,\&\, M = M$ za svaki brid $k$. Uvjet o cijelom putu raspao se na uvjet o pojedinim bridovima – to je ključ: možemo jednostavno <em>izbaciti</em> bridove koji ne sadrže $M$ i pitati je li put uopće moguć.</p>
'''),
        (r'''Kad je uvjet po bridovima, koja struktura odgovara na $q$ upita povezanosti brzo?''', r'''
<p>Za fiksnu masku pitanje „postoji li put od $u$ do $v$ koristeći samo dopuštene bridove” je pitanje povezanosti u statičnom grafu: DSU (unija-pronađi) nad dopuštenim bridovima, a zatim je svaki upit $O(1)$ usporedbom predstavnika. S $K \le 61$ maski gradimo $K$ takvih struktura, ukupno $O(K \cdot (n + m))$, i za svaki upit provjerimo $K$ maski.</p>
'''),
        (r'''Zašto je dovoljno provjeriti maske neovisno, a ne kombinirati ih?''', r'''
<p>Put je dobar ako je njegova AND-vrijednost $x$ $\ge V$, a pokazali smo da je to unija slučajeva po masci. Ako postoji dobar put, njegova $x$ upada u bar jedan slučaj $M$, i tada su svi njegovi bridovi u grafu maske $M$, pa DSU za $M$ kaže „povezano”. Obrnuto, ako je $u$–$v$ povezano u grafu maske $M$, bilo koji put u tom grafu ima $x \supseteq M$, a svaki takav $x$ je $\ge V$ (jer se s $V$ podudara na višim bitovima i ima $1$ gdje $V$ ima $0$, ili je jednak $V$ ako je $M = V$). Nema potrebe za kombiniranjem.</p>
'''),
    ],
    'tips': [r'''<strong>Usporedba po najvišem različitom bitu.</strong> Uvjet „$f(\text{put}) \ge V$” za bitovne funkcije (AND, OR, XOR) gotovo se uvijek razbija na $O(\log V)$ neovisnih uzoraka „viši bitovi fiksni, bit $i$ zadan, niži slobodni”.''',
             r'''AND je monoton po podskupu bridova: dodavanjem bridova rezultat samo pada. Zato uvjet o cijelom putu postaje uvjet o svakom bridu, a upit povezanosti rješava DSU umjesto pretraživanja po putovima.''',
             r'''Pazi na $V = 2^{60} - 1$ i na slučaj $V = 0$: prvi ima samo masku $x = V$, drugi ima $61$ maski. Koristi <code>unsigned long long</code> i pomak <code>1ULL &lt;&lt; i</code>.'''],
    'solution': r'''
<p>Prema javnim analizama natjecanja SDCPC 2023. Vrijednost puta $x$ (AND težina) je $\ge V$ točno kada je $x = V$ ili kad postoji bit $i$ s $V_i = 0$ i $x_i = 1$, a viši bitovi su jednaki. Za svaki takav $i$ definiramo masku $M_i$ (viši bitovi od $V$, bit $i$ postavljen, niži nule); uvjet „$x \supseteq M_i$” vrijedi točno kada <em>svaki</em> brid na putu sadrži $M_i$. Za svaku od najviše $61$ maski zadržimo samo bridove koji je sadrže i izgradimo DSU; upit $(u,v)$ je <code>Yes</code> ako su $u$ i $v$ spojeni u bar jednoj od tih struktura. Složenost $O(61 \cdot (n + m + q))$.</p>
''',
    'detailed': r'''
<h3>1. Razlaganje uvjeta $x \ge V$</h3>
<p>Neka je $x$ AND težina nekog puta. Tvrdnja: $x \ge V$ točno onda kad vrijedi bar jedna od sljedećih $\le 61$ mogućnosti: (a) $x = V$; (b) za neki bit $i$ ($0 \le i \lt 60$) s $V_i = 0$: $x_i = 1$ i $x_j = V_j$ za sve $j \gt i$. Dokaz: ako $x \ne V$, promotrimo najviši bit $i$ na kojem se razlikuju; tada je $x \ge V$ točno kad je $x_i = 1$ i $V_i = 0$ (bitovi iznad su jednaki, bitovi ispod ukupno vrijede manje od $2^i$). Obrnuto, svaka mogućnost (b) daje $x \gt V$. Za svaki takav $i$ definiramo masku $$M_i = \left(\left\lfloor \tfrac{V}{2^i} \right\rfloor \,\big|\, 1\right) \cdot 2^i,$$ tj. bitovi $V$ iznad $i$, jedinica na $i$, nule ispod. Mogućnost (b) za $i$ povlači $x \,\&\, M_i = M_i$; obrnuto, ako $x \supseteq M_i$ (kao skup bitova), onda je $x \ge M_i \gt V$ jer se $M_i$ podudara s $V$ iznad $i$ i ima $1$ gdje $V$ ima $0$. Također $x \supseteq V$ povlači $x \ge V$. Dakle: <em>$x \ge V$ točno kad $x$ sadrži barem jednu masku iz skupa $\{V\} \cup \{M_i : V_i = 0\}$</em>.</p>
<h3>2. Redukcija na povezanost</h3>
<p>AND niza brojeva sadrži masku $M$ točno kada je svaki od njih sadrži (bit je u AND-u postavljen samo ako ga svi imaju). Zato „postoji put $u \to v$ s AND $\supseteq M$” znači „postoji put $u \to v$ u podgrafu $G_M$ koji sadrži samo bridove $e$ s $w_e \,\&\, M = M$”. To je čisto pitanje povezanosti u statičnom grafu, bez težina.</p>
<h3>3. Algoritam</h3>
<ol>
<li>Sastavi popis maski: $V$, te $M_i$ za svaki $i \in [0, 60)$ s $V_i = 0$. Najviše $61$ maska.</li>
<li>Za svaku masku $M$: DSU s $n$ vrhova, spoji krajeve svih bridova s $w_e \,\&\, M = M$; zapamti predstavnika svakog vrha u polje <code>comp[M][v]</code>.</li>
<li>Za upit $(u, v)$: odgovor je <code>Yes</code> ako za neku masku vrijedi <code>comp[M][u] == comp[M][v]</code>.</li>
</ol>
<p>Ispravnost: ako postoji dobar put, njegova vrijednost $x$ sadrži neku masku $M$ (korak 1), pa su svi njegovi bridovi u $G_M$ i DSU javlja povezanost. Ako DSU javlja povezanost za $M$, postoji put u $G_M$, njegova vrijednost sadrži $M$, pa je $\ge V$.</p>
<h3>4. Složenost</h3>
<p>Izgradnja: $61$ puta prolaz kroz $m$ bridova s DSU operacijama, $O(61 \cdot m \, \alpha(n))$, plus $O(61 \cdot n)$ za zapis predstavnika; za $m = 5 \cdot 10^5$ to je oko $3 \cdot 10^7$ jednostavnih operacija. Upiti: $O(61)$ svaki, ukupno $O(61 q)$. Memorija $61 \cdot n$ cijelih brojeva, oko $25$ MB za $n = 10^5$.</p>
<h3>5. Rubni slučajevi i zamke</h3>
<ul>
<li>$V = 0$: svaki put je dobar; maska $V = 0$ zadržava sve bridove, pa se odgovor svodi na obično „povezano”. $V = 2^{60} - 1$: jedina maska je $V$.</li>
<li>Težine i $V$ idu do $2^{60}$: koristi 64-bitne nepredznačene tipove i <code>1ULL &lt;&lt; i</code>; s <code>int</code> pomacima rezultat je nedefiniran.</li>
<li>Višestruki bridovi i petlje su dopušteni i ne smetaju DSU-u.</li>
<li>$u = v$ nije moguće po uvjetima zadatka, ali DSU bi ionako dao <code>Yes</code>.</li>
</ul>
''',
    'verified': r'''uzorci 2/2; 300 slučajnih malih testova ($n \le 7$, $m \le 10$, težine i $V$ s najviše $4$ bita) protiv brute forcea koji pretražuje stanja (vrh, trenutni AND); 3 velika testa s $n = 10^5$, $m = q = 5 \cdot 10^5$ i 60-bitnim težinama (najviše $0.34$ s).''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Heap', 'title_hr': 'Gomila', 'slug': 'I_heap',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Gomila (heap) veličine $n$ je niz $a_1, \dots, a_n$ u kojem za sve $2 \le i \le n$ vrijedi $a_{\lfloor i/2 \rfloor} \le a_i$ (min-gomila) ili za sve $a_{\lfloor i/2 \rfloor} \ge a_i$ (max-gomila). Umetanje vrijednosti $v$: stavi $a_n := v$, $i := n$; dok je $i \gt 1$: ako je <code>is_max</code> lažno i $a_{\lfloor i/2 \rfloor} \le a_i$, stani; ako je <code>is_max</code> istinito i $a_{\lfloor i/2 \rfloor} \ge a_i$, stani; inače zamijeni $a_{\lfloor i/2 \rfloor}$ i $a_i$ te $i := \lfloor i/2 \rfloor$.</p>
<p>BaoBao je u prazan niz redom umetao $v_1, \dots, v_n$, ali je za $i$-to umetanje vrijednost <code>is_max</code> odredio prema binarnom stringu $b$: $b_i = 0$ znači lažno, $b_i = 1$ istinito. Dani su $v$ i konačni niz $a$; rekonstruiraj leksikografski najmanji $b$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^5$; $v_1, \dots, v_n$ ($1 \le v_i \le 10^9$); $a_1, \dots, a_n$ — permutacija od $v$. Zbroj $n$ ne prelazi $10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test leksikografski najmanji $b$ ili <code>Impossible</code>.</p>
<h3>Primjer</h3>
<p>$v = (2,3,1,4)$, $a = (4,1,3,2)$: <code>0101</code> (nizovi nakon umetanja: $\{2\}, \{3,2\}, \{1,2,3\}, \{4,1,3,2\}$). $v = (4,5,1,2,3)$, $a = (3,4,1,5,2)$: <code>Impossible</code>. $v = (1,1,2)$, $a = (2,1,1)$: <code>001</code>.</p>
''',
    'hints': [r'''
<p>Razmišljaj unatrag: posljednje umetnuta vrijednost $v_n$ počela je na poziciji $n$ i penjala se prema korijenu. Gdje se sada nalazi i što se dogodilo s elementima koje je „preskočila”?</p>
''', r'''
<p>Element koji se penje zamjenjuje se samo s roditeljem koji je strogo veći (min-hrpa) odnosno strogo manji (max-hrpa); jednakost zaustavlja penjanje. Zato je $v_n$ na <em>najdubljoj</em> poziciji na putu $n \to$ korijen s vrijednošću $v_n$, a svi elementi ispod nje na putu pomaknuti su za jedno mjesto dolje.</p>
''', r'''
<p>Poništi umetanje (pomakni elemente ispod natrag gore, ukloni poziciju $n$) i provjeri koji je $b_n$ konzistentan: za <code>0</code> svi preskočeni moraju biti $\gt v_n$ i roditelj mora biti $\le v_n$; za <code>1</code> obrnuto. Stanje prije umetanja ne ovisi o izboru, pa uvijek biraj <code>0</code> ako je moguće i nastavi s $n-1$.</p>
'''],
    'coach': [
        (r'''Zašto je prirodno rekonstruirati umetanja od posljednjeg prema prvom?''', r'''
<p>Umetanje $v_i$ mijenja samo pozicije na putu od $i$ do korijena, a sve kasnije operacije dodaju nove pozicije $i+1, \dots, n$. Kad znamo konačni niz i poništimo posljednje umetanje, dobivamo točno niz nakon $n-1$ umetanja – problem se svodi na manji istog oblika. Unaprijed to ne ide, jer ne znamo kako je izgledao niz nakon svakog koraka.</p>
'''),
        (r'''Gdje je u konačnom nizu vrijednost $v_n$ i zašto je to jednoznačno?''', r'''
<p>Umetnuti element počinje na poziciji $n$ i u svakom koraku zamijeni mjesto s roditeljem; stane kad roditelj zadovolji uvjet hrpe ($\le$ za min, $\ge$ za max), što uključuje jednakost. Dakle svi elementi koje je preskočio strogo su različiti od $v_n$ (svi $\gt v_n$ ili svi $\lt v_n$), a on završava na poziciji $p$ na putu $n \to 1$. Pozicije ispod $p$ na putu sad sadrže preskočene elemente ($\ne v_n$), pa je $p$ upravo <em>najdublja</em> pozicija na putu s vrijednošću $v_n$. Ako takve pozicije nema, niz $a$ nije mogao nastati i odgovor je <code>Impossible</code>.</p>
'''),
        (r'''Koji uvjeti odlučuju je li umetanje moglo biti min-umetanje ($b_n = 0$) ili max-umetanje ($b_n = 1$)?''', r'''
<p>Za $b_n = 0$: svaki preskočeni element (na putu strogo ispod $p$) morao je biti $\gt v_n$ (inače bi penjanje stalo ranije), a roditelj pozicije $p$ (ako $p \gt 1$) mora biti $\le v_n$ (inače bi penjanje nastavilo). Za $b_n = 1$ simetrično: preskočeni $\lt v_n$, roditelj $\ge v_n$. Ta su dva skupa uvjeta sve što treba: ako vrijede, simulacija umetanja $v_n$ u poništeni niz zaista daje $a$.</p>
'''),
        (r'''Zašto smijemo pohlepno birati $b_n = 0$ kad god je moguće, bez straha da ćemo kasnije zapeti?''', r'''
<p>Poništavanje umetanja (pomak elemenata ispod $p$ za jedno mjesto gore, uklanjanje pozicije $n$) ne ovisi o tome jesmo li odabrali <code>0</code> ili <code>1</code> – niz nakon $n-1$ umetanja je isti. Dakle izbor $b_n$ ne utječe na izvedivost ostatka. Tražimo leksikografski najmanji $b$, a odlučujemo od zadnjeg indeksa prema prvom; kako je za svaki $i$ skup dopuštenih vrijednosti $b_i$ neovisan o drugim izborima, uzimanje najmanje dopuštene vrijednosti na svakom indeksu daje leksikografski minimum.</p>
'''),
        (r'''Kolika je složenost i što je s jednakim vrijednostima $v$?''', r'''
<p>Put $i \to 1$ ima $O(\log i)$ pozicija; za svaki $i$ radimo prolaz po putu, pa je ukupno $O(n \log n)$. Jednake vrijednosti pokriva pravilo „najdublja pozicija s vrijednošću $v_i$” i stroge nejednakosti za preskočene elemente; roditelj smije biti jednak $v_i$ jer jednakost zaustavlja penjanje.</p>
'''),
    ],
    'tips': [r'''<strong>Poništavaj operacije unatrag.</strong> Kad je zadan konačni rezultat niza operacija koje dodaju elemente, posljednja operacija obično je jednoznačno prepoznatljiva i njezino poništavanje vraća manji problem istog oblika.''',
             r'''U hrpi element koji se penje ostavlja trag: preskočeni elementi pomaknuti su za jedno mjesto dolje i svi su strogo na istoj strani od njega. Ta „stroga” svojstva određuju položaj čak i uz duplikate.''',
             r'''Pohlepni leksikografski izbor je siguran čim pokažeš da izbor na jednom indeksu ne mijenja skup mogućnosti na ostalima – provjeri to eksplicitno, ne pretpostavljaj.'''],
    'solution': r'''
<p>Prema javnim analizama natjecanja SDCPC 2023. Rekonstruiramo unatrag, $i = n, \dots, 1$. Umetnuti element $v_i$ krenuo je s pozicije $i$ i penjao se putem do korijena; kako jednakost zaustavlja penjanje, svi preskočeni elementi strogo su različiti od $v_i$, pa je $v_i$ na najdubljoj poziciji $p$ na putu $i \to 1$ s vrijednošću $v_i$ (nema je $\Rightarrow$ <code>Impossible</code>). $b_i = 0$ je moguće ako su svi preskočeni $\gt v_i$ i roditelj od $p$ (ako postoji) $\le v_i$; $b_i = 1$ ako su svi preskočeni $\lt v_i$ i roditelj $\ge v_i$. Poništavanje umetanja (elemente ispod $p$ na putu pomaknemo za jedno gore i uklonimo poziciju $i$) ne ovisi o izboru, pa pohlepno biramo <code>0</code> kad je moguće. Složenost $O(n \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Što posljednje umetanje ostavlja u nizu</h3>
<p>Promotrimo umetanje $v_n$ u hrpu veličine $n-1$ (bez obzira na tip). Element se postavi na poziciju $n$, a zatim, dok roditelj ne zadovoljava uvjet, zamjenjuje mjesto s roditeljem. Uvjet zaustavljanja je $a_{\lfloor i/2\rfloor} \le a_i$ (min) odnosno $\ge$ (max), dakle <em>uključuje jednakost</em>. Posljedice: (1) $v_n$ završava na nekoj poziciji $p$ na putu $P = (n, \lfloor n/2 \rfloor, \dots, 1)$; (2) elementi koji su bili na pozicijama $p, \dots$ iznad $n$ na putu pomaknuti su za jedno mjesto dolje (svaki na poziciju svog djeteta na putu); (3) svi preskočeni elementi su strogo $\gt v_n$ (min) ili strogo $\lt v_n$ (max); (4) roditelj od $p$ (ako $p \gt 1$) zadovoljava $a_{\lfloor p/2\rfloor} \le v_n$ (min) odnosno $\ge v_n$ (max), i to je jedini element iznad $p$ koji je umetanje „vidjelo”.</p>
<h3>2. Prepoznavanje pozicije $p$</h3>
<p>Po (2) i (3), pozicije na putu strogo ispod $p$ sadrže preskočene elemente, svi $\ne v_n$. Dakle $p$ je najdublja pozicija na putu $P$ s vrijednošću $v_n$. Ako na putu nema vrijednosti $v_n$, konačni niz ne može nastati zadanim umetanjima – odgovor <code>Impossible</code>. Ovo vrijedi i uz ponovljene vrijednosti u $v$: eventualne druge kopije vrijednosti $v_n$ na putu iznad $p$ nisu preskočene, a ispod $p$ ih ne može biti.</p>
<h3>3. Provjera tipa i poništavanje</h3>
<p>Neka je $S$ skup vrijednosti na pozicijama puta strogo ispod $p$ (preskočeni). Umetanje je moglo biti min-umetanje ($b_n = 0$) točno kad su svi elementi $S$ strogo $\gt v_n$ i ($p = 1$ ili $a_{\lfloor p/2\rfloor} \le v_n$). Slično za max-umetanje s obrnutim nejednakostima. Dokaz dostatnosti: krenemo od poništenog niza (opisanog dolje) i simuliramo umetanje $v_n$ – u svakom koraku roditelj je element iz $S$ koji strogo krši uvjet, pa se zamjena dogodi, a kod roditelja od $p$ uvjet vrijedi pa se staje; dobiveni niz je točno $a$. Nužnost slijedi iz (3) i (4).</p>
<p>Poništeni niz: za pozicije puta $p = P_t, P_{t-1}, \dots, P_1$ (od $p$ prema $n$) postavimo $a_{P_s} := a_{P_{s-1}}$ (vrijednost s djeteta na putu vraćamo gore), a poziciju $n$ uklonimo. Ovaj korak ne ovisi o tome je li $b_n$ bio $0$ ili $1$.</p>
<h3>4. Leksikografski minimum</h3>
<p>Za svaki $i$ (obrađujemo $i = n, n-1, \dots, 1$) skup dopuštenih vrijednosti $b_i$ ovisi samo o nizu nakon $i$ umetanja, koji je jednoznačno određen konačnim nizom (poništavanja su deterministička). Skupovi su dakle neovisni, pa je leksikografski najmanji $b$ onaj koji na svakom indeksu uzima najmanju dopuštenu vrijednost: <code>0</code> ako je min-umetanje moguće, inače <code>1</code>; ako nijedno nije moguće (ili $v_i$ nije na putu), odgovor je <code>Impossible</code>.</p>
<h3>5. Algoritam i složenost</h3>
<ol>
<li>Za $i = n$ do $1$: izgradi put $i, \lfloor i/2 \rfloor, \dots, 1$ (duljina $\lfloor \log_2 i \rfloor + 1$).</li>
<li>Nađi najdublju poziciju $p$ na putu s $a_p = v_i$; ako nema, <code>Impossible</code>.</li>
<li>Provjeri uvjete za <code>0</code> i za <code>1</code> po preskočenim elementima i roditelju od $p$; upiši $b_i$.</li>
<li>Pomakni vrijednosti ispod $p$ za jedno mjesto gore, obriši poziciju $i$.</li>
</ol>
<p>Svaki korak je $O(\log n)$, ukupno $O(n \log n)$ za $n \le 10^5$ i zbroj $n \le 10^6$ – trenutno.</p>
<h3>6. Zamke</h3>
<ul>
<li>Stroge vs. nestroge nejednakosti: preskočeni elementi su <em>strogo</em> na jednoj strani, roditelj smije biti <em>jednak</em>. Zamjena ova dva uvjeta ruši testove s duplikatima (usporedi primjer $v = (1,1,2)$, $a = (2,1,1)$, odgovor <code>001</code>).</li>
<li>Vrijednosti su do $10^9$: bez problema u 32 bita, ali koristi konzistentan tip za oznaku „prazno”.</li>
<li>Kod $i = 1$ put je samo korijen; uvjet za oba tipa je trivijalno ispunjen, pa je $b_1 = 0$.</li>
</ul>
''',
    'verified': r'''uzorci 1/1 (tri testa iz zadatka); 300 slučajnih malih testova ($n \le 9$, vrijednosti iz malog skupa radi duplikata; dio nizova $a$ nasumično permutiran) protiv brute forcea koji isprobava sve $2^n$ nizova $b$; 3 velika testa s $10$ nizova duljine $10^5$ (najviše $0.20$ s).''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Triangle City', 'title_hr': 'Trokutasti grad', 'slug': 'J_triangle_city',
    'tl': '2 s', 'ml': '256 MiB',
    'statement': r'''
<p>Grad ima $\frac{n(n+1)}{2}$ raskrižja u $n$ redova; $i$-ti red ima $i$ raskrižja $(i, 1), \dots, (i, i)$. Za sve $1 \le j \le i \lt n$ postoje ceste: $(i,j)\text{-}(i+1,j)$ duljine $a_{i,j}$, $(i,j)\text{-}(i+1,j+1)$ duljine $b_{i,j}$ i $(i+1,j)\text{-}(i+1,j+1)$ duljine $c_{i,j}$, pri čemu $a_{i,j}, b_{i,j}, c_{i,j}$ zadovoljavaju nejednakost trokuta.</p>
<p>Nađi najdulji put od $(1,1)$ do $(n,n)$ koji svaku cestu koristi najviše jednom.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $2 \le n \le 300$; zatim $n-1$ redaka s $a_{i,\cdot}$, $n-1$ redaka s $b_{i,\cdot}$ i $n-1$ redaka s $c_{i,\cdot}$ ($1 \le \cdot \le 10^9$). Zbroj $n$ ne prelazi $5 \cdot 10^3$.</p>
<h3>Izlaz</h3>
<p>Za svaki test tri retka: duljina $l$, broj raskrižja $m$ na putu i $2m$ brojeva $i_1\ j_1\ \dots\ i_m\ j_m$ redom, s $(i_1,j_1) = (1,1)$ i $(i_m,j_m) = (n,n)$. Bilo koje optimalno rješenje se prihvaća; bez suvišnih razmaka na kraju retka.</p>
<h3>Primjer</h3>
<p>$n = 2$, $a = 3$, $b = 2$, $c = 4$: $7$, put $(1,1),(2,1),(2,2)$. $n = 2$, $a = b = c = 1$: $2$, put $(1,1),(2,1),(2,2)$. $n = 3$, $a = (100; 100, 100)$, $b = (1; 100, 1)$, $c = (100; 100, 100)$: $700$, put od $8$ raskrižja $(1,1),(2,1),(3,2),(2,2),(2,1),(3,1),(3,2),(3,3)$.</p>
''',
    'hints': [r'''
<p>Izbroji stupnjeve: svaki vrh trokutastog grada ima paran stupanj ($2$, $4$ ili $6$). Što to znači za skup cesta koje staza <em>ne</em> iskoristi?</p>
''', r'''
<p>Staza od $(1,1)$ do $(n,n)$ troši neparan broj cesta u krajevima i paran u ostalim vrhovima, pa u neiskorištenom skupu $(1,1)$ i $(n,n)$ imaju neparan stupanj, a svi ostali paran – takav skup nužno sadrži put od $(1,1)$ do $(n,n)$. Neiskorištena duljina je stoga $\ge d$, gdje je $d$ najkraći put.</p>
''', r'''
<p>Ukloni bridove jednog najkraćeg puta (Dijkstra). Zbog stroge nejednakosti trokuta put koristi najviše jedan brid svakog trokuta, pa ostatak ostaje povezan; svi stupnjevi u ostatku su parni osim $(1,1)$ i $(n,n)$, pa Hierholzerov algoritam daje Eulerovu stazu duljine (ukupno $-\ d$).</p>
'''],
    'coach': [
        (r'''Zašto je odgovor ograničen odozgo s (ukupna duljina) $-$ (najkraći put)?''', r'''
<p>Prebrojimo stupnjeve: unutarnji vrh susjedan je $6$ cesta, vrh na stranici $4$, kut $2$ – svi parni. Staza od $s = (1,1)$ do $t = (n,n)$ koristi u $s$ i $t$ neparan, a u ostalim vrhovima paran broj cesta. Neiskorišteni skup $U$ ima stoga neparan stupanj točno u $s$ i $t$; komponenta od $s$ u grafu $(V, U)$ ima paran broj vrhova neparnog stupnja, pa mora sadržavati i $t$ – dakle $U$ sadrži put $s \to t$ i ukupna duljina u $U$ je $\ge d$, gdje je $d$ duljina najkraćeg puta. Staza dakle ima duljinu $\le \text{total} - d$.</p>
'''),
        (r'''Kako postići tu granicu – koje ceste izostaviti?''', r'''
<p>Izostavimo točno bridove jednog najkraćeg puta $P$ od $s$ do $t$. U grafu $G - P$ stupnjevi su parni osim u $s$ i $t$ (put mijenja paritet samo u krajevima). Ako je $G - P$ povezan (na skupu vrhova sa stupnjem $\gt 0$), Eulerova staza od $s$ do $t$ postoji i koristi sve preostale bridove – duljina točno $\text{total} - d$.</p>
'''),
        (r'''Zašto ostatak $G - P$ ostaje povezan?''', r'''
<p>Zbog <em>stroge</em> nejednakosti trokuta najkraći put nikad ne koristi dvije stranice istog trokuta: zamjena dviju stranica trećom dala bi strogo kraći put. Skup bridova $P$ dakle sadrži najviše jedan brid iz svakog trokuta. Rez u planarnom grafu odgovara ciklusu u dualnom grafu, a takav ciklus ulazi i izlazi iz svake unutarnje trokutaste plohe kroz koju prolazi – treba dva brida istog trokuta. Jedini rezovi koji koriste samo vanjsku plohu i jednu trokutastu jesu izolacije kutnih vrhova (dva rubna brida jednog trokuta), također dva brida istog trokuta. Zato $P$ ne sadrži nijedan rez i $G - P$ je povezan.</p>
'''),
        (r'''Kako konstruirati stazu i u kojoj složenosti?''', r'''
<p>Dijkstra od $s$ na $V = \frac{n(n+1)}{2}$ vrhova i $E = \frac{3n(n-1)}{2}$ bridova daje $d$ i put $P$ preko roditeljskih bridova. Bridove iz $P$ označimo iskorištenima i pokrenemo iterativni Hierholzerov algoritam od $s$ nad preostalim bridovima; jer je $s$ jedan od dva neparna vrha, staza završava u $t$. Ispis ima $E - (|P|) + 1$ vrhova. Složenost $O(E \log V)$ po testu, s $n \le 300$ to je oko $1.4 \cdot 10^5$ bridova.</p>
'''),
    ],
    'tips': [r'''<strong>Paritet stupnjeva neiskorištenih bridova</strong> je standardni donji/gornji argument za „najdulja staza” zadatke: kad su svi stupnjevi parni, izostavljeni skup mora povezivati krajeve staze.''',
             r'''Stroga nejednakost trokuta u uvjetima nije ukras – ona osigurava da najkraći put dira svaki trokut najviše jednom, što je ključ za povezanost ostatka.''',
             r'''Hierholzer piši iterativno (eksplicitni stog) i s pokazivačem po listi susjedstva; rekurzija po $10^5$ bridova može prepuniti stog.'''],
    'solution': r'''
<p>Prema javnim analizama natjecanja SDCPC 2023. Svi vrhovi imaju paran stupanj, pa skup cesta koje staza od $(1,1)$ do $(n,n)$ ne iskoristi ima neparan stupanj točno u tim dvama vrhovima i stoga sadrži put među njima – neiskorištena duljina je $\ge d$ (najkraći put). Granica se postiže: uklonimo bridove jednog najkraćeg puta (Dijkstra); zbog stroge nejednakosti trokuta put koristi najviše jedan brid svakog trokuta, pa ostatak ostaje povezan i, budući da su mu svi stupnjevi parni osim krajeva, ima Eulerovu stazu $(1,1) \to (n,n)$ (Hierholzer) duljine $\text{total} - d$. Složenost $O(n^2 \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Graf i stupnjevi</h3>
<p>Vrhovi su $(i, j)$, $1 \le j \le i \le n$; bridovi $a_{i,j}$: $(i,j)$–$(i+1,j)$, $b_{i,j}$: $(i,j)$–$(i+1,j+1)$, $c_{i,j}$: $(i+1,j)$–$(i+1,j+1)$. Svaki brid pripada jednom ili dvama trokutima, a svaki vrh ima stupanj $2$ (tri kuta), $4$ (rub) ili $6$ (unutrašnjost) – uvijek paran. Ukupno $E = \frac{3n(n-1)}{2}$ bridova, $V = \frac{n(n+1)}{2}$ vrhova.</p>
<h3>2. Gornja granica</h3>
<p>Neka staza $W$ ide od $s = (1,1)$ do $t = (n,n)$ i neka je $U$ skup bridova koje ne koristi. Za svaki vrh $v$: $\deg_U(v) = \deg_G(v) - \deg_W(v)$. Staza u unutarnjem vrhu ulazi i izlazi (paran $\deg_W$), a u $s$ i $t$ ima neparan $\deg_W$ (za $s \ne t$). Dakle $\deg_U$ je neparan točno u $s$ i $t$. U svakoj komponenti grafa $(V, U)$ zbroj stupnjeva je paran, pa je broj neparnih vrhova paran – komponenta koja sadrži $s$ sadrži i $t$, tj. $U$ sadrži put $s \to t$ i $w(U) \ge d := \mathrm{dist}(s,t)$. Stoga $w(W) = \text{total} - w(U) \le \text{total} - d$.</p>
<h3>3. Konstrukcija koja postiže granicu</h3>
<p>Neka je $P$ najkraći put $s \to t$ i $G' = G - P$. Stupnjevi u $G'$ parni su svugdje osim u $s$ i $t$. Tvrdnja: $G'$ je povezan na vrhovima pozitivnog stupnja (a $s$ i $t$ imaju pozitivan stupanj: stupanj $\ge 2$ minus jedan brid puta). Dokaz: pretpostavimo suprotno – tada $P$ sadrži rez $C \subseteq P$ grafa $G$. U planarnom grafu minimalni rez odgovara ciklusu u dualu (plohe su trokuti i vanjska ploha). Dualni ciklus prolazi kroz svaku svoju plohu ulazeći jednim i izlazeći drugim bridom; za unutarnji trokut to znači dva brida istog trokuta u $C \subseteq P$. Ciklus koji koristi samo vanjsku plohu i jedan trokut (duljina $2$) također uzima dva brida istog trokuta (to su rezovi koji izoliraju kutne vrhove). Dakle $P$ bi sadržavao dva brida istog trokuta. No zbog stroge nejednakosti trokuta ($a + b \gt c$ itd.) zamjena dviju stranica trećom skraćuje put, što proturječi minimalnosti $P$. (Duljina puta koji koristi dvije stranice trokuta nije nužno „uzastopno” – ali dvije stranice istog trokuta dijele vrh, pa put koji ih obje koristi prolazi tim vrhom i može se skratiti trećom stranicom.) Zato je $G'$ povezan i ima Eulerovu stazu od $s$ do $t$ duljine $\text{total} - d$.</p>
<h3>4. Algoritam</h3>
<ol>
<li>Indeksiraj vrhove ($\mathrm{id}(i,j) = \frac{i(i-1)}{2} + j - 1$), učitaj tri matrice, izgradi listu bridova i susjedstva, zbroji $\text{total}$.</li>
<li>Dijkstra od $s$ s pamćenjem roditeljskog brida; rekonstruiraj $P$ od $t$ i označi bridove iskorištenima.</li>
<li>Iterativni Hierholzer od $s$ preko neiskorištenih bridova (pokazivač po listi susjedstva, stog vrhova); dobiveni niz vrhova obrni.</li>
<li>Ispiši $\text{total} - d$, broj vrhova staze i vrhove.</li>
</ol>
<p>Složenost $O(E \log V) = O(n^2 \log n)$ po testu; zbroj $n^2 \le 10^6$ daje oko $1.5 \cdot 10^6$ bridova ukupno.</p>
<h3>5. Rubni slučajevi i zamke</h3>
<ul>
<li>$n = 2$: tri brida; najkraći put je $\min(b, a + c)$, staza koristi preostale bridove – npr. primjer s $a = b = c = 1$ daje $2$.</li>
<li>Duljine do $10^9$ i do $1.4 \cdot 10^5$ bridova: zbroj u 64-bitnom tipu.</li>
<li>Hierholzer mora preskakati već iskorištene bridove (uključujući one iz $P$) preko pokazivača koji se ne vraća – inače kvadratno.</li>
<li>Pretvorba $\mathrm{id} \to (i,j)$ zaokruživanjem korijena: popravi $i$ petljama da se izbjegnu greške u <code>double</code>.</li>
</ul>
''',
    'verified': r'''uzorci 1/1 (oba testa iz zadatka, kroz checker koji provjerava krajeve, susjednost, jedinstvenost cesta i optimalnost); 300 slučajnih malih testova ($n \le 4$, duljine do $3$, $10$ ili $10^9$ uz strogu nejednakost trokuta) protiv brute forcea koji pretražuje sve staze i checkera; 3 velika testa s $16$ testova po $n = 300$ (najviše $0.44$ s).''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Are you a bot?', 'title_hr': 'Jesi li ti bot?', 'slug': 'K_are_you_a_bot',
    'tl': '3 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Niz $a$ je permutacija od $1..n$. Neka je $A_i$ niz $a$ bez $i$-tog elementa. Za niz $p$ različitih elemenata, $G(p)$ je neusmjeren graf s vrhovima $1..|p|$ u kojem su $i \lt j$ spojeni bridom ako za sve $k \in [i, j]$ vrijedi $p_k \in [\min(p_i, p_j), \max(p_i, p_j)]$. $F(p)$ je duljina najkraćeg puta (broj bridova) od $1$ do $|p|$ u $G(p)$. Neka je $f(a) = [F(A_1), \dots, F(A_n)]$.</p>
<p>Za dani niz $b$ nađi bilo koju permutaciju $a$ s $f(a) = b$. Rješenje sigurno postoji.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 40\,000$ testova; $4 \le n \le 10^5$ i niz $b_1, \dots, b_n$. Zbroj $n$ ne prelazi $5 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedna permutacija.</p>
<h3>Primjer</h3>
<p>$b = (2,2,1,1) \to$ npr. $1\ 2\ 4\ 3$; $b = (2,2,2,2) \to 2\ 1\ 4\ 3$; $b = (2,1,1,2) \to 1\ 3\ 2\ 4$; $b = (5,5,4,4,4,5,5) \to 3\ 1\ 7\ 2\ 6\ 4\ 5$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Difficult Constructive Problem', 'title_hr': 'Težak konstruktivni zadatak', 'slug': 'L_difficult_constructive_problem',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je string $s_1 \dots s_n$ nad $\{0, 1, ?\}$ i broj $k$. Zamijeni svaki <code>?</code> znakom <code>0</code> ili <code>1</code> (različiti upitnici neovisno) tako da broj indeksa $1 \le i \lt n$ sa $s_i \ne s_{i+1}$ bude točno $k$. Među rješenjima ispiši leksikografski najmanje.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^5$, $0 \le k \lt n$, string $s$. Zbroj $n$ ne prelazi $10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test leksikografski najmanji popunjeni string ili <code>Impossible</code>.</p>
<h3>Primjer</h3>
<p><code>1?010??01</code>, $k = 6 \to$ <code>100100101</code>; isti string, $k = 5 \to$ <code>Impossible</code>; <code>100101101</code>, $k = 6 \to$ <code>100101101</code>; $k = 5 \to$ <code>Impossible</code>; <code>????????1</code>, $k = 3 \to$ <code>000000101</code>.</p>
''',
    'hints': [r'''
<p>Leksikografski najmanje rješenje gradi se slijeva: na svakom mjestu pokušaj staviti <code>0</code> i pitaj se može li se <em>ostatak</em> još dovršiti. Što o sufiksu trebaš znati da bi na to odgovorio u $O(1)$?</p>
''', r'''
<p>Za sufiks $s_i \dots s_n$ uz fiksan znak $s_i = j$ izračunaj najmanji $f_{i,j}$ i najveći $g_{i,j}$ mogući broj prijelaza (DP zdesna). Dostižni su svi brojevi između $f$ i $g$ – ali samo oni odgovarajućeg pariteta.</p>
''', r'''
<p>Paritet broja prijelaza u sufiksu određen je isključivo prvim i posljednjim znakom ($s_i \ne s_n$ daje neparan). Zato fiksiraj posljednji znak (ako je <code>?</code>, probaj oba i uzmi manji rezultat); tada je skup dostižnih vrijednosti točno $\{f, f+2, \dots, g\}$ i pohlepni odabir je ispravan.</p>
'''],
    'coach': [
        (r'''Kako se općenito gradi leksikografski najmanji niz i što nam za to treba znati o ostatku?''', r'''
<p>Slijeva nadesno na svako mjesto stavimo najmanji znak za koji <em>postoji</em> dovršetak ostatka. Ispravnost je standardna: bilo koje rješenje koje na mjestu $i$ ima veći znak leksikografski je veće od bilo kojeg rješenja s manjim znakom na $i$ uz isti prefiks. Dakle trebamo brzo odgovoriti: „može li sufiks $i..n$, uz $s_i = j$, imati točno $k'$ prijelaza?”, gdje je $k'$ preostali broj prijelaza.</p>
'''),
        (r'''Zašto je skup mogućih brojeva prijelaza sufiksa opisan samo minimumom, maksimumom i paritetom?''', r'''
<p>Broj prijelaza u nizu $s_i \dots s_n$ ima paritet $[s_i \ne s_n]$: svaki prijelaz mijenja znak, pa je znak na kraju jednak početnom točno kad je prijelaza paran broj. Uz fiksne $s_i$ i $s_n$ paritet je fiksan. Nadalje, ako neki popunjeni sufiks ima $t \ge f + 2$ prijelaza (gdje je $f$ minimum), možemo ga „popraviti” tako da broj prijelaza padne za točno $2$: uzmi neki blok <code>?</code>-ova koji doprinosi više nego što mora i promijeni jedan znak na rubu bloka – detaljan argument u detaljnom rješenju. Ponavljanjem dobivamo sve vrijednosti $f, f+2, \dots, g$.</p>
'''),
        (r'''Kako izračunati $f_{i,j}$ i $g_{i,j}$ za sve $i$ odjednom?''', r'''
<p>DP zdesna: $f_{n,j} = 0$ ako je $s_n$ kompatibilan s $j$, inače $\infty$; $f_{i,j} = \min_{t} \big(f_{i+1,t} + [j \ne t]\big)$ po dopuštenim $t$, i analogno $g$ s maksimumom. To je $O(n)$ i daje za svaki $i$ i svaki izbor znaka najmanji i najveći broj prijelaza sufiksa.</p>
'''),
        (r'''Zašto posljednji znak fiksiramo unaprijed i što ako je <code>?</code>?''', r'''
<p>Tvrdnja o dostižnosti $\{f, f+2, \dots, g\}$ vrijedi uz fiksan $s_n$; ako je $s_n$ slobodan, skup dostižnih vrijednosti je unija dvaju takvih skupova različitih pariteta i pohlepni test s intervalom i paritetom više ne bi bio točan. Zato ako je $s_n = $ <code>?</code>, riješimo zadatak dvaput (sa $s_n = 0$ i $s_n = 1$) i ispišemo leksikografski manji od dobivenih rezultata – to je i dalje $O(n)$.</p>
'''),
        (r'''Kako izgleda pohlepni korak i zašto je $O(1)$?''', r'''
<p>Na mjestu $i$, uz prethodni znak $p$, probamo $j = 0$ pa $j = 1$ (samo ako je kompatibilan sa $s_i$): preostali broj prijelaza za sufiks je $k' = k - [p \ne j]$, a uvjet je $f_{i,j} \le k' \le g_{i,j}$ i $k' \equiv f_{i,j} \pmod 2$. Prvi $j$ koji prolazi stavimo i nastavimo s $k := k'$. Ako nijedan ne prolazi (moguće samo na prvom mjestu), odgovor je <code>Impossible</code>.</p>
'''),
    ],
    'tips': [r'''<strong>Pohlepno + „može li se ostatak dovršiti?”</strong> Leksikografski najmanji objekt gotovo uvijek se gradi slijeva uz DP koji za svaki sufiks opisuje skup dostižnih stanja – ovdje je taj skup interval s paritetom.''',
             r'''Kad skup dostižnih vrijednosti opisuješ kao interval, uvijek provjeri postoje li „rupe”; tipično ih uklanja argument pariteta (kao ovdje) ili argument „mogu smanjiti za $1$”.''',
             r'''Ako neki rubni parametar (posljednji znak) kvari lijepo svojstvo, fiksiraj ga i pokreni algoritam za svaku vrijednost – konstanta $2$ je jeftina, a dokaz postaje čist.'''],
    'solution': r'''
<p>Prema javnim analizama natjecanja SDCPC 2023. Fiksiramo posljednji znak (ako je <code>?</code>, riješimo za oba izbora i uzmemo manji rezultat). DP-om zdesna izračunamo za svaki $i$ i znak $j$ najmanji $f_{i,j}$ i najveći $g_{i,j}$ broj prijelaza u sufiksu $s_i \dots s_n$ uz $s_i = j$. Uz fiksne krajeve sufiksa dostižni su točno svi brojevi između $f$ i $g$ istog pariteta kao $f$ (paritet je $[s_i \ne s_n]$, a broj prijelaza može se mijenjati u koracima od $2$). Zatim slijeva pohlepno stavljamo <code>0</code> kad god preostali broj prijelaza ostaje dostižan, inače <code>1</code>; ako ni jedno ni drugo ne ide, <code>Impossible</code>. Složenost $O(n)$.</p>
''',
    'detailed': r'''
<h3>1. Struktura skupa dostižnih vrijednosti</h3>
<p>Za sufiks $s_i \dots s_n$ i fiksan znak $s_i = j$ neka je $R_{i,j}$ skup svih brojeva prijelaza koje možemo dobiti popunjavanjem upitnika u sufiksu (uz fiksan $s_n$). Neka je $f_{i,j} = \min R_{i,j}$ i $g_{i,j} = \max R_{i,j}$.</p>
<p><strong>Paritet.</strong> Svaki prijelaz mijenja znak, pa je $s_n = s_i$ točno kad je broj prijelaza paran. Dakle svi elementi $R_{i,j}$ imaju paritet $[j \ne s_n]$.</p>
<p><strong>Nema rupa.</strong> Tvrdnja: $R_{i,j} = \{f, f+2, \dots, g\}$. Dokaz: uzmimo popunjavanje $x$ s $t \gt f$ prijelaza i popunjavanje $y$ s $f$ prijelaza (oba imaju iste fiksne znakove). Mijenjajmo $x$ prema $y$ mijenjajući jedan upitnik odjednom, u proizvoljnom redoslijedu. Promjena jednog znaka na mjestu $m$ mijenja samo prijelaze $(m-1,m)$ i $(m,m+1)$, dakle ukupan broj prijelaza za $-2$, $0$ ili $+2$ (paritet je fiksan pa $\pm 1$ nije moguće). Niz brojeva prijelaza tako ide od $t$ do $f$ koracima veličine $\le 2$, a svaka vrijednost pariteta $t$ između $f$ i $t$ negdje na tom putu bude pogođena – jer se od vrijednosti $\ge v + 2$ ne može „preskočiti” na $\le v - 2$ u jednom koraku. Isto vrijedi za sve $t \le g$, pa su dostižni svi brojevi iz $[f, g]$ pravog pariteta.</p>
<h3>2. Izračun $f$ i $g$</h3>
<p>Neka je $\mathrm{ok}(i, j)$ istina ako je $s_i = $ <code>?</code> ili $s_i = j$. Tada
$$f_{n,j} = \begin{cases}0 & \mathrm{ok}(n,j)\\ \infty & \text{inače}\end{cases},\qquad f_{i,j} = \min_{t \in \{0,1\}} \big(f_{i+1,t} + [j \ne t]\big)\ \text{ako } \mathrm{ok}(i,j),$$ a $g$ analogno s $\max$ (i $-\infty$ za nedopuštene). Prijelaz je $O(1)$, ukupno $O(n)$.</p>
<h3>3. Pohlepna konstrukcija</h3>
<p>Prolazimo $i = 1, \dots, n$, pamtimo prethodni znak $p$ (na početku nema prijelaza) i preostali broj prijelaza $k$. Za $j = 0$, zatim $j = 1$: ako je $\mathrm{ok}(i,j)$ i $f_{i,j} \lt \infty$, stavimo $k' = k - [p \ne j]$ i provjerimo $f_{i,j} \le k' \le g_{i,j}$ te $k' \equiv f_{i,j} \pmod 2$. Prvi $j$ koji prolazi upišemo, $k := k'$, $p := j$. Prema odjeljku 1 uvjet je točno „postoji dovršetak”, pa je izbor najmanjeg prolaznog $j$ ispravan. Ako na prvom mjestu ništa ne prolazi, rješenja nema; na kasnijim mjestima uvijek nešto prolazi (prethodni korak je to jamčio).</p>
<h3>4. Posljednji znak</h3>
<p>Argument o paritetu koristi fiksan $s_n$. Ako je $s_n = $ <code>?</code>, pokrenemo cijeli postupak za $s_n = $ <code>0</code> i za $s_n = $ <code>1</code> te ispišemo leksikografski manji od uspješnih rezultata (ili <code>Impossible</code> ako oba ne uspiju). Za $n = 1$ jedina je varijabla sam znak: odgovor je <code>0</code> ili zadani znak ako je $k = 0$, inače <code>Impossible</code> – algoritam to pokriva jer je $f = g = 0$.</p>
<h3>5. Složenost, rubni slučajevi i zamke</h3>
<ul>
<li>Vrijeme $O(n)$ po testu (najviše dva prolaza), memorija $O(n)$; zbroj $n$ je $10^6$.</li>
<li>Ne zaboravi $f = \infty$ za nedopuštene znakove – inače pohlepni test prolazi kroz „nemoguće” stanje. Koristi dovoljno velik <code>INF</code> da $f + 1$ ne prelije.</li>
<li>$k$ može biti $0$; tada rješenje mora biti konstantno – DP to vraća automatski.</li>
<li>Kad je $s_n$ upitnik, usporedba dvaju rezultata radi se kao usporedba stringova, a ne po broju jedinica.</li>
</ul>
''',
    'verified': r'''uzorak 1/1 (pet testova iz zadatka); 300 slučajnih malih testova ($n \le 11$, udio upitnika $0.3$–$1$) protiv brute forcea koji isprobava sve popune; 3 velika testa s $10$ stringova duljine $10^5$ (najviše $0.03$ s).''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Trie', 'title_hr': 'Prefiksno stablo', 'slug': 'M_trie',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Prefiksno stablo (trie) je korijensko stablo u kojem je svaki brid označen znakom; korijen predstavlja prazan string, a dijete $v$ roditelja $u$ preko brida sa znakom $c$ predstavlja $s(v) = s(u) + c$; svi predstavljeni stringovi su različiti.</p>
<p>Dano je korijensko stablo s vrhovima $0..n$ (korijen $0$) i $m$ ključnih vrhova $k_1, \dots, k_m$; svi listovi su ključni. Označi svaki brid malim engleskim slovom tako da stablo postane trie. Neka je $B$ niz stringova ključnih vrhova sortiran leksikografski uzlazno. Označi bridove tako da $B$ bude najmanji (nizovi se uspoređuju leksikografski po elementima); među takvim označavanjima ispiši leksikografski najmanji string oznaka.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le m \le n \le 2 \cdot 10^5$; roditelji $a_1, \dots, a_n$ ($0 \le a_i \lt i$, svaki vrh ima najviše $26$ djece); ključni vrhovi $k_1, \dots, k_m$ (različiti). Zbroj $n$ ne prelazi $2 \cdot 10^5$.</p>
<h3>Izlaz</h3>
<p>Za svaki test string $c_1 \dots c_n$, gdje je $c_i$ slovo na bridu $(a_i, i)$.</p>
<h3>Primjer</h3>
<p>$n = 5$, roditelji $(0,1,1,2,2)$, ključni $1,4,3,5$: <code>abaab</code> ($B = \{$<code>a</code>, <code>aa</code>, <code>aba</code>, <code>abb</code>$\}$). $n = 1$, roditelj $0$, ključni $1$: <code>a</code>.</p>
''',
    'hints': [r'''
<p>Niz stringova ključnih vrhova u podstablu vrha $x$ (gledan relativno, bez prefiksa $s(x)$) ima oblik: prazan string ako je $x$ ključan, zatim za djecu po slovima $a, b, c, \dots$ redom „slovo + niz djeteta”. Odabir slova je zapravo odabir <em>redoslijeda djece</em>.</p>
''', r'''
<p>Usporedi „dijete $u$ ispred $v$” i „$v$ ispred $u$”: razlika se vidi na prvom mjestu gdje se nizovi $u$ i $v$ razlikuju. Ako je niz od $u$ pravi prefiks niza od $v$, bolje je staviti $v$ prvo – dulji niz ide ispred kraćeg. Inače pobjeđuje leksikografski manji niz.</p>
''', r'''
<p>Nizove ne treba graditi eksplicitno: rangiraj vrhove po dubinama odozdo. Vektor vrha je $[0$ ako je ključan$]$ + sortirani rangovi djece; vektore uspoređuj leksikografski uz pravilo „pravi prefiks je veći”. Djeca sortirana po (rang, indeks) dobivaju $a, b, c, \dots$</p>
'''],
    'coach': [
        (r'''Kako izgleda sortirani niz ključnih stringova podstabla i što o njemu odlučuje označavanje bridova?''', r'''
<p>Neka je $\mathrm{seq}(x)$ sortirani niz stringova ključnih vrhova u podstablu $x$, bez zajedničkog prefiksa $s(x)$. Stringovi koji počinju manjim slovom su manji, pa je $$\mathrm{seq}(x) = [\varepsilon \text{ ako je } x \text{ ključan}] \;\Vert\; \big(\ell_1 + \mathrm{seq}(c_1)\big) \;\Vert\; \big(\ell_2 + \mathrm{seq}(c_2)\big) \;\Vert\; \dots$$ gdje su $c_1, c_2, \dots$ djeca poredana po slovima $\ell_1 \lt \ell_2 \lt \dots$ i „$\ell + \mathrm{seq}$” znači dodavanje slova ispred svakog stringa. Konkretna slova nisu bitna (uvijek ćemo koristiti $a, b, c, \dots$ redom radi minimalnog ispisa) – bitan je samo <em>redoslijed</em> djece. $B = \mathrm{seq}(\text{korijen})$.</p>
'''),
        (r'''Kako usporediti dva moguća redoslijeda djece i zašto se dobiva pravilo „pravi prefiks je veći”?''', r'''
<p>Uzmimo dvoje djece $u, v$ i usporedimo $[a + \mathrm{seq}(u)] \Vert [b + \mathrm{seq}(v)]$ s $[a + \mathrm{seq}(v)] \Vert [b + \mathrm{seq}(u)]$ element po element. Dok su $\mathrm{seq}(u)$ i $\mathrm{seq}(v)$ jednaki, elementi su jednaki. Ako se razlikuju na nekom mjestu, pobjeđuje onaj s manjim stringom – dakle manji niz ide prvi. Ako je $\mathrm{seq}(u)$ pravi prefiks od $\mathrm{seq}(v)$, na mjestu $|\mathrm{seq}(u)|$ prvi redoslijed ima string koji počinje s $b$, a drugi string koji počinje s $a$ – drugi je manji, pa <em>dulji</em> niz $v$ ide prvi. To je poredak $\prec$ na nizovima: leksikografski, ali pravi prefiks je veći. Argument se doslovno prenosi na više djece (usporedba susjednih).</p>
'''),
        (r'''Zašto je dovoljno da svaki vrh neovisno minimizira svoj $\mathrm{seq}$ u poretku $\prec$?''', r'''
<p>$\mathrm{seq}(x)$ je monoton u $\mathrm{seq}(c_i)$ s obzirom na $\prec$: ako $\mathrm{seq}(c_i)$ postane $\prec$-manji, blok $\ell_i + \mathrm{seq}(c_i)$ postane manji na prvom mjestu razlike (ili, ako je stari bio pravi prefiks novog, novi na tom mjestu ima string s $\ell_i$ umjesto $\ell_{i+1}$ – opet manji). Zato je optimalno najprije minimizirati nizove djece, a onda ih poredati po $\prec$. Na korijenu je $\prec$-minimum ujedno i običan leksikografski minimum, jer je konačni $B$ jednoznačno određen redoslijedom i samo taj redoslijed biramo.</p>
'''),
        (r'''Kako usporedbe nizova provesti efikasno, bez eksplicitnih stringova?''', r'''
<p>Rangiramo vrhove po dubini, od najdublje razine. Vektor vrha: $[0]$ ako je ključan, zatim rangovi djece sortirani uzlazno (rangovi iz prethodne, dublje razine; $0$ je manji od svakog ranga, kao što je $\varepsilon$ manji od svakog stringa). Dva vrha iste razine uspoređujemo po vektorima uz pravilo „pravi prefiks je veći”; vrhovi s jednakim vektorima dobivaju isti rang. To je vjerna usporedba $\mathrm{seq}$-ova: blokovi se poklapaju redom, a unutar bloka slovo je isto pa odlučuje $\mathrm{seq}$ djeteta – tj. njegov rang. Zbroj duljina vektora je $O(n)$, sortiranje po razinama daje $O(n \log n)$.</p>
'''),
        (r'''Kako iz rangova dobiti leksikografski najmanji ispis $c_1 \dots c_n$?''', r'''
<p>Za svaki vrh sortiramo djecu po (rang, indeks) i dodjeljujemo $a, b, c, \dots$ Rang određuje redoslijed koji minimizira $B$; djeca s jednakim rangom imaju jednake nizove, pa je njihov međusobni redoslijed za $B$ nevažan, a manjem indeksu dajemo manje slovo jer je izlazni string indeksiran vrhovima. Odluke u različitim vrhovima su neovisne.</p>
'''),
    ],
    'tips': [r'''<strong>Slova su samo redoslijed.</strong> U zadacima s označavanjem bridova trie-a slovima uvijek prvo shvati da je izbor slova ekvivalentan permutaciji djece; minimalna slova $a, b, c, \dots$ dobivaju se automatski.''',
             r'''Kad se uspoređuju „konkatenacije blokova”, pravilo za prefiks može biti obrnuto od uobičajenog – provjeri na primjeru što slijedi iza kraćeg bloka.''',
             r'''Rangiranje podstabala po razinama (kao kod kanonskih oblika stabala / AHU algoritma) zamjenjuje usporedbu nizova usporedbom kratkih vektora cijelih brojeva; ukupna veličina vektora je $O(n)$.'''],
    'solution': r'''
<p>Prema javnim analizama natjecanja SDCPC 2023. Sortirani niz ključnih stringova podstabla $x$ (relativno) jest $[\varepsilon$ ako je $x$ ključan$]$ pa redom, po slovima djece, „slovo + niz djeteta”; slova su dakle samo redoslijed djece. Usporedba dvaju redoslijeda pokazuje da dijete s $\prec$-manjim nizom ide prvo, gdje je $\prec$ leksikografski poredak nizova uz pravilo da je <em>pravi prefiks veći</em> (dulji niz ide ispred kraćeg). Nizove rangiramo po dubinama odozdo: vektor vrha je $[0$ ako ključan$]$ + sortirani rangovi djece, vektore uspoređujemo po $\prec$, jednaki dobivaju isti rang. Djeca sortirana po (rang, indeks) dobivaju $a, b, c, \dots$ Složenost $O(n \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Struktura sortiranog niza</h3>
<p>Za vrh $x$ neka je $\mathrm{seq}(x)$ sortirani niz stringova ključnih vrhova u podstablu $x$, svakome uklonjen zajednički prefiks $s(x)$. Svi stringovi iz podstabla djeteta $c$ počinju slovom $\ell(c)$ brida $(x, c)$, a različita djeca imaju različita slova, pa je $$\mathrm{seq}(x) = [\varepsilon]^{[x \text{ ključan}]} \;\Vert\; \big(\ell(c_1) + \mathrm{seq}(c_1)\big) \;\Vert\; \dots \;\Vert\; \big(\ell(c_t) + \mathrm{seq}(c_t)\big),$$ gdje su djeca poredana po slovima. Traženi $B$ je $\mathrm{seq}(0)$. Skup upotrijebljenih slova ne utječe na relativni poredak, a leksikografski najmanji ispis zahtijeva slova $a, b, c, \dots$ redom, pa je jedina odluka <em>redoslijed djece</em> u svakom vrhu.</p>
<h3>2. Poredak $\prec$ i pravilo za prefiks</h3>
<p>Definirajmo na nizovima stringova poredak $\prec$: usporedi element po element; na prvom različitom mjestu odlučuje manji string; ako je jedan niz pravi prefiks drugoga, <em>dulji je manji</em>. Tvrdnja: u optimalnom redoslijedu dijete $u$ stoji ispred $v$ kad je $\mathrm{seq}(u) \prec \mathrm{seq}(v)$ (uz jednakost redoslijed nije bitan). Dokaz: promotrimo susjednu djecu sa slovima $\ell \lt \ell'$ i usporedimo $X = [\ell + \mathrm{seq}(u)] \Vert [\ell' + \mathrm{seq}(v)] \Vert R$ s $Y = [\ell + \mathrm{seq}(v)] \Vert [\ell' + \mathrm{seq}(u)] \Vert R$ ($R$ je ostatak, jednak u oba). Dok su $\mathrm{seq}(u)_i = \mathrm{seq}(v)_i$, elementi su jednaki. Ako se razlikuju na mjestu $i$, manji od $X, Y$ je onaj s manjim $\mathrm{seq}(\cdot)_i$ na prvom mjestu. Ako je $\mathrm{seq}(u)$ pravi prefiks od $\mathrm{seq}(v)$ duljine $m$, onda je $X_m = \ell' + \mathrm{seq}(v)_0$, a $Y_m = \ell + \mathrm{seq}(v)_m$; kako je $\ell \lt \ell'$, $Y_m \lt X_m$ pa je $Y$ manji – dulji niz ide prvi. Isto vrijedi ako $u, v$ nisu susjedni (zamjena susjednih ne mijenja ostale blokove), pa je optimalni redoslijed sortiranje po $\prec$.</p>
<h3>3. Neovisnost odluka (monotonost)</h3>
<p>Ako se $\mathrm{seq}(c_i)$ zamijeni $\prec$-manjim nizom, $\mathrm{seq}(x)$ postaje $\prec$-manji: razlika se vidi unutar bloka $i$ na prvom različitom mjestu, a ako je stari niz pravi prefiks novoga, novi blok na tom mjestu ima string koji počinje s $\ell(c_i)$, dok stari niz tamo ima string sljedećeg bloka (počinje većim slovom) ili završava (pa je $\mathrm{seq}(x)$ pravi prefiks – po definiciji $\prec$ veći). Zato svaki vrh može neovisno minimizirati svoj niz: najprije djeca (rekurzivno), zatim njihov poredak po $\prec$. Na korijenu tražimo obični leksikografski minimum $B$, ali biramo samo redoslijed blokova, a taj isti argument pokazuje da je poredak blokova po $\prec$ optimalan i za običnu usporedbu (kraći blok nikad nije „posljednji”, jer iza njega slijedi sljedeći blok ili kraj u oba niza jednako).</p>
<h3>4. Rangiranje umjesto stringova</h3>
<p>Eksplicitni nizovi imali bi kvadratnu veličinu. Umjesto toga obradimo vrhove po dubini, od najdublje: vrh $v$ dobiva vektor $\mathrm{vec}(v) = [0]^{[v \text{ ključan}]} \Vert \mathrm{sort}(\mathrm{rk}(c_1), \dots, \mathrm{rk}(c_t))$, gdje su $\mathrm{rk}$ rangovi djece (svi na istoj, dubljoj razini, dakle međusobno usporedivi; rangovi su $\ge 1$, a $0$ predstavlja $\varepsilon$ koji je manji od svakog nepraznog stringa). Vektore vrhova iste razine sortiramo po $\prec$ (leksikografski, pravi prefiks veći), jednakima damo isti rang, i to je $\mathrm{rk}(v)$. Ispravnost: $\mathrm{seq}(u) \prec \mathrm{seq}(v)$ za vrhove iste razine točno kad $\mathrm{vec}(u) \prec \mathrm{vec}(v)$ – blokovi se uspoređuju redom, unutar bloka slova su ista ($a, b, \dots$ po poziciji) pa odlučuje $\prec$ na nizovima djece, tj. rang; ako je jedan vektor pravi prefiks drugoga, pripadni $\mathrm{seq}$ je pravi prefiks (jednaki blokovi, pa kraj) – veći.</p>
<h3>5. Algoritam i složenost</h3>
<ol>
<li>Učitaj roditelje, izgradi djecu i dubine; grupiraj vrhove po dubini.</li>
<li>Za dubine od najveće do $0$: izgradi vektore, sortiraj vrhove razine po $\prec$, dodijeli rangove.</li>
<li>Za svaki vrh sortiraj djecu po (rang, indeks); $i$-to dijete dobiva slovo $a + i$; ispiši $c_1 \dots c_n$.</li>
</ol>
<p>Zbroj duljina vektora je $O(n)$; svaka usporedba košta najviše duljinu kraćeg vektora, a sortiranje razine s $m$ vrhova radi $O(m \log m)$ usporedbi – ukupno $O(n \log n)$ uz uobičajene pretpostavke (u praksi usporedbe su kratke; u najgorem slučaju gornja granica je $O(n \log n \cdot 26)$ jer vektor ima najviše $27$ elemenata). Memorija $O(n)$.</p>
<h3>6. Provjera na primjeru i zamke</h3>
<ul>
<li>Primjer: roditelji $(0,1,1,2,2)$, ključni $1,4,3,5$. Razina $2$: $\mathrm{vec}(4) = \mathrm{vec}(5) = [0]$, rang $1$; $\mathrm{vec}(3) = [0]$, rang $1$. Razina $1$: $\mathrm{vec}(2) = [1, 1]$, $\mathrm{vec}(3) = [0]$; $[0] \prec [1,1]$ jer je $0 \lt 1$, dakle $\mathrm{rk}(3) = 1$, $\mathrm{rk}(2) = 2$. Korijen: dijete $1$ dobiva <code>a</code>; kod vrha $1$: dijete $3$ (rang $1$) dobiva <code>a</code>, dijete $2$ <code>b</code>; kod vrha $2$: djeca $4, 5$ jednakog ranga → <code>a</code>, <code>b</code> po indeksu. Ispis <code>abaab</code>, $B = (a, aa, aba, abb)$. ✓</li>
<li>Uobičajena greška: standardna usporedba vektora (prefiks manji). Test: vrh s djecom $u$ (jedan ključni list) i $v$ (ključan, s jednim ključnim listom) – $\mathrm{seq}(u) = [x]$, $\mathrm{seq}(v) = [\varepsilon, x]$; $v$ mora ići prvi.</li>
<li>Svi listovi su ključni, pa je svaki vektor neprazan.</li>
<li>Duplicirani rangovi na istoj razini moraju biti <em>jednaki</em> (ne uzastopni), inače se jednaki nizovi krivo razlikuju.</li>
</ul>
''',
    'verified': r'''uzorak 1/1 (oba testa iz zadatka); 300 slučajnih malih testova ($n \le 8$, do $3$ djece po vrhu, razni udjeli ključnih vrhova) protiv brute forcea koji isprobava sve permutacije djece i bira minimalni $B$ pa minimalni ispis; 3 velika testa s $n = 2 \cdot 10^5$ ($2$, $3$ ili $26$ djece po vrhu; najviše $0.07$ s).''',
},
]
