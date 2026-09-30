# -*- coding: utf-8 -*-
STAGE = {
    'no': 22,
    'name': 'Stage 22: Shaanxi',
    'source_name': 'Jul 1st, 2023',
    'no_editorial': True,
    'community': True,
    'source_html': r'''
<p>Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1287&amp;r=0">engleskim tekstovima zadataka</a>. Organizatori nisu objavili službena rješenja. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1287">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Moniphant Sleep', 'title_hr': 'Monifantov san', 'slug': 'A_moniphant_sleep',
    'tl': '3 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Monifant putuje kroz razine sna; na svakoj razini je jedan Mofunfun. Četiri operacije:</p>
<ol>
<li><em>Spavaj</em>: silazi na sljedeću (za jedan dublju) razinu.</li>
<li><em>Probudi se</em>: vraća se na prethodnu (za jedan pliću) razinu.</li>
<li><em>Uvreda</em>: Mofunfun na trenutnoj razini postaje ljut.</li>
<li><em>Odmazda</em>: ako postoji ljuti Mofunfun, Monifant se vraća na najmanju razinu na kojoj je Mofunfun ljut i taj Mofunfun prestaje biti ljut; inače se ništa ne događa.</li>
</ol>
<p>Kad se Monifant vrati na manju razinu, Mofunfuni dubljih razina nestaju (zajedno sa svojom ljutnjom). Dan je niz od $n$ Monifanata; svaki je prije početka izveo operaciju <em>Spavaj</em> $5 \cdot 10^5$ puta. Treba izvršavati operacije $1$–$4$ nad svim Monifantima s indeksima u $[l, r]$ ili (operacija $5$, $l = r$) ispisati razinu sna $l$-tog Monifanta.</p>
<h3>Ulaz</h3>
<p>$1 \le n, q \le 5 \cdot 10^5$; zatim $q$ redaka <code>op l r</code>, $op \in \{1,\dots,5\}$, $1 \le l \le r \le n$.</p>
<h3>Izlaz</h3>
<p>Za svaku operaciju $5$ jedan broj.</p>
<h3>Primjer</h3>
<p>$n = 1$: operacije <code>1</code>, <code>1</code>, <code>1</code>, <code>3</code>, <code>2</code>, <code>1</code>, <code>1</code>, <code>4</code>, <code>5</code> (sve na $[1,1]$) daju $500004$. $n = 3$: <code>2 1 3</code>, <code>3 1 3</code>, <code>1 1 3</code>, <code>1 1 3</code>, <code>5 1 1</code>, <code>4 1 3</code>, <code>5 1 1</code> daju $500001$, $499999$.</p>
''',
    'hints': [
        r'''
<p>Što od cijelog skupa ljutih razina jednog Monifanta uopće utječe na budućnost? Razmisli što se događa s ljutim Mofunfunima nakon <em>Odmazde</em> i nakon <em>Buđenja</em>.</p>
''',
        r'''
<p>Dovoljno je stanje $(L, m)$: razina $L$ i najmanja ljuta razina $m \le L$ (ili $\bot$ ako ljutih nema). Operacije: $1$: $L{+}{+}$; $2$: $L{-}{-}$, a ako je bilo $m = L$, onda $m := \bot$; $3$: ako je $\bot$, $m := L$; $4$: ako nije $\bot$, $L := m$, $m := \bot$.</p>
''',
        r'''
<p>Sve operacije su invarijantne na pomak $(L, m) \mapsto (L + t, m + t)$, a ovise o $\delta = L - m$. Kompozicija niza operacija zapisiva je kao oznaka s tri grane ($\bot$ / „umrli” s $\delta \lt K$ / „preživjeli” s $\delta \ge K$) fiksne veličine – lijeno segmentno stablo s kompozicijom oznaka u $O(1)$.</p>
''',
    ],
    'coach': [
        (r'Skup ljutih razina može biti velik. Što od njega stvarno treba pamtiti?',
         r'''
<p>Ljuti Mofunfuni su uvijek na razinama $\le L$ (dublji nestaju pri povratku). <em>Odmazda</em> vraća Monifanta na najmanju ljutu razinu $m$, smiruje tog Mofunfuna, a svi dublji (dakle svi ostali ljuti) nestaju – nakon nje ljutih nema. <em>Buđenje</em> uklanja samo Mofunfuna razine $L$; minimum $m$ preživi osim ako je $m = L$, a tada nestaju svi. <em>Uvreda</em> dodaje $L \ge m$ i ne mijenja minimum ako on postoji. Dakle o skupu treba znati samo njegov minimum: stanje je $(L, m)$ ili $(L, \bot)$, s invarijantom $m \le L$.</p>
'''),
        (r'Zašto se kompozicija operacija ne može zapisati kao obična funkcija „po komponentama”, i što ju ipak čini malom?',
         r'''
<p>Operacija $2$ grana se po $\delta = L - m$: element s $\delta = 0$ gubi $m$ („umire”), ostali samo pomaknu $L$. Kroz niz operacija bez odmazde $\delta$ se mijenja za neto pomak $s$ operacija $1$/$2$; element umire pri prvom buđenju u trenutku kad je $\delta + s = 0$. Postoji prag $K$ takav da umiru točno elementi s $\delta \lt K$, jer $\delta + s$ prolazi kroz $0$ točno kad je $\delta \lt \max_t(-s_t)$ po buđenjima $t$. Ključna lema: <strong>svi elementi koji umru prije prve odmazde završe u istom stanju</strong> (relativno prema $L$).</p>
'''),
        (r'Zašto vrijedi lema o umrlima?',
         r'''
<p>Neka element $1$ umre prije elementa $2$ (dakle $\delta_1 \lt \delta_2$). U trenutku smrti oba imaju isti $L$ (isti početni $L$ plus isti pomak). Element $2$ umire prvi put kad pomak $s$ padne na $-\delta_2$ buđenjem. Do tog trenutka $s \ge -\delta_2$. Element $1$ između svoje i njegove smrti može uvredom dobiti novo $m = L$ pri pomaku $s_3 \ge -\delta_2$; ako je $s_3 \gt -\delta_2$, pomak mora buđenjem proći $s_3 \to s_3 - 1$ prije nego dođe do $-\delta_2$, pa element $1$ opet umre; ako je $s_3 = -\delta_2$, umre istim buđenjem kao element $2$. U trenutku smrti elementa $2$ oba su $\bot$ s istim $L$, a dalje se razvijaju jednako. Odmazda je jedina operacija koja to kvari – zato ju oznaka bilježi posebno.</p>
'''),
        (r'Kako onda izgleda oznaka (lijena operacija) i kako se dvije komponiraju?',
         r'''
<p>Oznaka opisuje što niz operacija radi trima klasama ulaznih stanja: (i) $\bot$: $L' = L + a$, $m' = L + b$ ili $\bot$; (ii) živi s $\delta \lt K$ (umiru): $L' = L + c$, $m' = L + d$ ili $\bot$; (iii) živi s $\delta \ge K$: bez odmazde $L' = L + e$, $m' = m$; s odmazdom $L' = m + e$, $m' = m + f$ ili $\bot$ (nakon odmazde svi preživjeli su u istom stanju <em>relativno prema $m$</em>). Kompozicija $t_1$ pa $t_2$: granu (i) i granu (ii) od $t_1$ provučemo simbolički kroz $t_2$; prag postaje $K = \max(K_1, K_2 - e_1)$ – ako je $K_2 - e_1 \gt K_1$, novi umrli dolaze iz $t_2$ i po lemi svi umrli dijele stanje $t_2$-ovih umrlih; preživjeli se slažu po tome ima li $t_1$ ili $t_2$ odmazdu. Sve su to $O(1)$ operacije nad desetak brojeva.</p>
'''),
        (r'Kako iz oznaka dobiti odgovor na upit $5$?',
         r'''
<p>Segmentno stablo nad Monifantima čuva u svakom čvoru oznaku koja još nije spuštena djeci; pri djelomičnom preklapanju oznaku spustimo (komponiramo u djecu). Upit za poziciju $l$ krene od početnog stanja $(500000, \bot)$ i primijeni oznake na putu od lista prema korijenu (dublje oznake su starije). Sve zajedno $O((n + q) \log n)$.</p>
'''),
    ],
    'tips': [
        r'''Kad je stanje složeno (skup), prvo dokaži da je dovoljan sažetak (ovdje minimum) – tek onda traži lijenu strukturu. Sažetak mora biti zatvoren na sve operacije.''',
        r'''Za lijeno segmentno stablo nije nužno da operacije budu linearne: dovoljno je da se <em>kompozicija</em> proizvoljnog niza operacija zapiše u ograničeno mnogo parametara. Traži klase ulaza koje niz obrađuje jednako (ovdje $\bot$, umrli, preživjeli).''',
        r'''Ovakve „simboličke” oznake nužno testiraj protiv doslovne simulacije na malim $n$ i puno kratkih nizova operacija – greške u kompoziciji se ne vide na primjerima.''',
        r'''Upit u točki može se riješiti bez spuštanja: skupi oznake na putu i primijeni ih od lista prema korijenu (starije prvo).''',
    ],
    'solution': r'''
<p>Vlastita izvedba (organizatori nisu objavili rješenja), potvrđena brute forceom koji doslovno simulira skup ljutih razina. Stanje jednog Monifanta sažima se na $(L, m)$: razinu $L$ i najmanju ljutu razinu $m \le L$ ili $\bot$ – <em>Odmazda</em> vraća na $m$ i briše sve ljute, <em>Buđenje</em> briše $m$ samo ako je $m = L$ (i tada sve), <em>Uvreda</em> ne mijenja postojeći minimum. Operacije su invarijantne na pomak i granaju se samo po $\delta = L - m$: kroz niz operacija bez odmazde „umiru” (gube $m$) točno elementi s $\delta \lt K$ za neki prag $K$, a lema kaže da svi umrli završe u istom stanju relativno prema $L$. Zato se kompozicija bilo kojeg niza operacija zapisuje oznakom s tri grane ($\bot$ / umrli / preživjeli, uz zastavicu odmazde nakon koje su preživjeli u istom stanju relativno prema $m$) i komponira u $O(1)$. Lijeno segmentno stablo s tim oznakama daje operacije na intervalu i upit u točki u $O(\log n)$; ukupno $O((n+q)\log n)$.</p>
''',
    'detailed': r'''
<h3>1. Sažimanje stanja jednog Monifanta</h3>
<p>Neka je $L$ trenutna razina i $A$ skup razina s ljutim Mofunfunom. Kad se Monifant vrati na manju razinu, dublji Mofunfuni nestaju, pa je uvijek $A \subseteq \{0, \dots, L\}$. Promotrimo operacije:</p>
<ul>
<li><em>Spavaj</em>: $L := L + 1$, $A$ nepromijenjen.</li>
<li><em>Probudi se</em>: $L := L - 1$, $A := A \setminus \{L_{\text{staro}}\}$.</li>
<li><em>Uvreda</em>: $A := A \cup \{L\}$.</li>
<li><em>Odmazda</em>: ako $A \ne \emptyset$, $L := \min A$ i svi Mofunfuni dublji od $\min A$ nestaju, a onaj na $\min A$ se smiri – dakle $A := \emptyset$.</li>
</ul>
<p><strong>Lema 1.</strong> Ponašanje ovisi samo o $(L, m)$, $m = \min A$ (ili $\bot$ za $A = \emptyset$). <em>Dokaz.</em> Odmazda koristi samo $m$ i briše sve. Buđenje briše iz $A$ element $L$; kako je $m \le L$, novi minimum je $m$ ako je $m \lt L$, a ako je $m = L$ onda je $A = \{L\}$ (svi elementi su u $[m, L]$) i postaje $\bot$. Uvreda dodaje $L \ge m$, pa minimum ostaje $m$ (ili postaje $L$ ako je bilo $\bot$). Spavanje ne mijenja $A$. $\square$</p>
<p>Prijelazi na $(L, m)$: $1$: $L{+}{+}$. $2$: $L{-}{-}$; ako je bilo $m = L$, $m := \bot$. $3$: ako $\bot$, $m := L$. $4$: ako nije $\bot$, $L := m$, $m := \bot$. Početno stanje svakog Monifanta je $(500000, \bot)$; odgovor na upit $5$ je $L$.</p>
<h3>2. Invarijantnost na pomak i prag umiranja</h3>
<p>Sve četiri operacije komutiraju s pomakom $(L, m) \mapsto (L+t, m+t)$, a jedino grananje (u operaciji $2$ i $4$) ovisi o $\delta = L - m \ge 0$ odnosno o tome je li stanje $\bot$. Promotrimo niz operacija $\sigma$ <em>bez odmazde</em> primijenjen na živo stanje. Neka je $s_t$ neto pomak razine (broj operacija $1$ minus broj operacija $2$) prije $t$-te operacije. Dok element živi, njegov $\delta$ u trenutku $t$ iznosi $\delta + s_t$; umire (postaje $\bot$) pri prvom buđenju $t$ s $\delta + s_t = 0$.</p>
<p><strong>Lema 2.</strong> Postoji $K \ge 0$ takav da u $\sigma$ umiru točno elementi s $\delta \lt K$; $K = \max(0, \max_{t \text{ buđenje}} (-s_t))$. <em>Dokaz.</em> Element s $\delta$ umire ako postoji buđenje $t$ s $s_t = -\delta$. Pomak se mijenja za $\pm 1$, kreće od $0$ i element s $\delta \ge 0$ ima $\delta + s_t \ge 0$ dok živi; ako je $\delta \lt K$, postoji buđenje s $-s_t \gt \delta$, a prije njega (jer pomak pada po $1$ i svaki pad je buđenje) postoji buđenje s $-s_t = \delta$. Ako je $\delta \ge K$, nikad $s_t = -\delta$ pri buđenju. $\square$</p>
<h3>3. Lema o umrlima</h3>
<p><strong>Lema 3.</strong> Neka dva živa elementa s istim $L$ i $\delta_1 \lt \delta_2 \lt K$ prođu kroz $\sigma$ (bez odmazde). Od trenutka smrti elementa $2$ nadalje njihova su stanja jednaka.</p>
<p><em>Dokaz.</em> Bez odmazde vrijedi $L = L_0 + s_t$ za oba elementa u svakom trenutku, neovisno o $m$. Element $2$ umire pri prvom buđenju $t_2$ s $s_{t_2} = -\delta_2$; prije toga je $s_t \ge -\delta_2$ (pomak pada po $1$ i svaki pad je buđenje). Element $1$ umire ranije, u $t_1 \lt t_2$; nakon toga je $\bot$ i može uvredom u trenutku $t_3 \in (t_1, t_2)$ dobiti $m = L_0 + s_{t_3}$, gdje je $s_{t_3} \ge -\delta_2$. Ako je $s_{t_3} \gt -\delta_2$, pomak prije $t_2$ mora buđenjem prijeći sa $s_{t_3}$ na $s_{t_3} - 1$, a u tom trenutku element $1$ ima $\delta = 0$ i umire; postupak se ponavlja. Ako je $s_{t_3} = -\delta_2$, element $1$ u trenutku $t_2$ ima $\delta = 0$ i umire istim buđenjem. U svakom slučaju neposredno nakon $t_2$ oba su elementa $\bot$ s $L = L_0 + s_{t_2} - 1$, a od tada primaju iste operacije. $\square$</p>
<p>Posljedica: za niz bez odmazde svi umrli elementi završavaju u istom stanju oblika $(L + c,\ L + d \text{ ili } \bot)$ – ovisnom samo o $L$. Preživjeli ($\delta \ge K$) završavaju u $(L + e, m)$. Ako niz sadrži odmazdu, preživjeli do prve odmazde postaju $(m, \bot)$ – svi u istom stanju <em>relativno prema $m$</em> – i dalje se razvijaju jednako; a umrli prije odmazde i dalje dijele stanje (odmazda na $\bot$ ne radi ništa, a ako su u međuvremenu dobili $m$, dobili su ga isti).</p>
<h3>4. Oznaka i njezina kompozicija</h3>
<p>Oznaka $T$ opisuje djelovanje niza operacija na tri klase ulaznih stanja (sve relativno, pa je pomak besplatan):</p>
<ul>
<li>$\bot$ stanja: $L' = L + a$, $m' = L + b$ ako je $b_m$, inače $\bot$.</li>
<li>živa s $\delta \lt K$: $L' = L + c$, $m' = L + d$ ako je $b_d$, inače $\bot$.</li>
<li>živa s $\delta \ge K$: ako niz nema odmazde ($\mathit{op4} = 0$): $L' = L + e$, $m' = m$; inače $L' = m + e$, $m' = m + f$ ako je $b_f$, inače $\bot$.</li>
</ul>
<p>Pojedine operacije: $1$: $a = e = 1$. $2$: $a = -1$, $K = 1$, $c = -1$, $e = -1$ ($\delta = 0$ umire). $3$: $b_m = 1$, $b = 0$ (samo $\bot$ dobiva $m = L$). $4$: $\mathit{op4} = 1$, $e = f = 0$, $b_f = 0$.</p>
<p><strong>Kompozicija</strong> $T = T_1 \circ T_2$ (prvo $T_1$): simboličko stanje $(\text{pomak } L, \text{ima } m, \text{pomak } m)$ relativno prema bazi provučemo kroz $T_2$ funkcijom <code>sym_apply</code> koja grananje radi po simboličkom $\delta$ (razlika pomaka). Grana $\bot$: primijeni $T_2$ na $(a_1, b_{m1}, b_1)$. Ako $T_1$ ima odmazdu: $K = K_1$; umrli iz $T_1$ provuku se kroz $T_2$; preživjeli (relativno prema $m$) provuku se kroz $T_2$ i $\mathit{op4} = 1$. Ako $T_1$ nema odmazde: preživjeli iz $T_1$ ulaze u $T_2$ s $\delta + e_1$, pa umiru u $T_2$ ako je $\delta \lt K_2 - e_1$; novi prag je $K = \max(K_1, K_2 - e_1)$. Ako je $K_2 - e_1 \gt K_1$, po Lemi 3 svi umrli dijele stanje umrlih iz $T_2$ pomaknuto za $e_1$: $c = e_1 + c_2$, $d = e_1 + d_2$, $b_d = b_{d2}$; inače se umrli iz $T_1$ provuku kroz $T_2$. Preživjeli: bez odmazde u $T_2$: $e = e_1 + e_2$; s odmazdom: $\mathit{op4} = 1$, $(e, f, b_f) = (e_2, f_2, b_{f2})$ (nakon odmazde stanje ovisi samo o $m$, koji $T_1$ nije mijenjao). Sve je $O(1)$.</p>
<h3>5. Segmentno stablo i upit</h3>
<p>Čvor čuva oznaku primijenjenu na cijeli svoj interval, još nespuštenu djeci. Operacija na $[l, r]$: potpuno pokriven čvor dobiva <code>tag = compose(tag, op)</code>; djelomično pokriven prvo spusti svoju oznaku u djecu (<code>compose(child, tag)</code>) pa se spušta. Upit $5$ za poziciju $l$: krenemo od $(500000, \bot)$ i primijenimo oznake na putu <em>od lista prema korijenu</em> – dublje oznake su starije, jer se pri spuštanju roditeljska oznaka komponira <em>nakon</em> dječje. Složenost $O((n + q)\log n)$, memorija $O(n)$ oznaka (svaka je desetak 64-bitnih brojeva).</p>
<h3>6. Zamke</h3>
<ul>
<li>Vrijednosti $b$, $d$, $f$ su relevantne samo uz pripadnu zastavicu; u kompoziciji ih ne smiješ čitati kad je zastavica $0$ (u kodu ih <code>sym_apply</code> ipak računa, ali se ne koriste).</li>
<li>Prag $K$ i pomaci su do $\pm q = 5 \cdot 10^5$, ali kompozicija ih zbraja – koristi 64-bitne brojeve.</li>
<li>Kad je $K_1 = 0$ (nitko nije umro u $T_1$), grana umrlih iz $T_1$ je prazna; tada se ne smije „provlačiti” smeće – koristi se isključivo grana iz $T_2$.</li>
</ul>
''',
    'verified': r'''uzorci 2/2, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 0.90 s).''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Click the Circle', 'title_hr': 'Klikni krug', 'slug': 'B_click_the_circle',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Izmijenjena verzija igre osu!. Dva tipa objekata, svi krugovi imaju polumjer $r$:</p>
<ol>
<li><em>Krug</em> $(c_x, c_y, t)$: središte $(c_x, c_y)$, prisutan u vremenu $[t - d, t + d]$.</li>
<li><em>Klizač</em> $(s_x, s_y, t_x, t_y, u, v)$: sastoji se od dva zasebna objekta — pokretnog kruga i okvira koji drži putanju. U trenutku $u - d$ krug i okvir se pojavljuju sa središtem kruga u $(s_x, s_y)$; od $u$ do $v$ središte se jednoliko giba do $(t_x, t_y)$; nakon $v + d$ oboje nestaju.</li>
</ol>
<p>Dva objekta se sijeku ako u nekom trenutku oba postoje i njihovi se oblici preklapaju (uključivo rubovi). Prebroji parove objekata koji se sijeku.</p>
<h3>Ulaz</h3>
<p>$1 \le n, r, d \le 10^3$; zatim $n$ objekata: <code>1 cx cy t</code> ili <code>2 sx sy tx ty u v</code>; koordinate u $[1, 10^4]$, $1 \le t, u, v \le 10^3$, $u \lt v$.</p>
<h3>Izlaz</h3>
<p>Broj parova.</p>
<h3>Primjer</h3>
<p>$r = d = 1$: krugovi $(1,1,2)$ i $(2,2,3)$: $1$; krugovi $(1,1,2)$ i $(3,2,3)$: $0$; krug $(3,3,2)$ i klizač $(5,5,5,1,2,4)$: $3$; klizači $(1,1,1,5,2,4)$ i $(5,5,5,1,2,4)$: $2$; klizači $(10,1,10,20,2,4)$ i $(1,10,20,10,2,4)$: $6$.</p>
''',
    'hints': [
        r'''
<p>Objekata je najviše $2n \le 2000$, pa se smiju provjeriti svi parovi – teškoća je u tome da se svaki par provjeri točno, u cijelim brojevima. Koje vrste parova postoje?</p>
''',
        r'''
<p>Okvir klizača je „kapsula” polumjera $r$ oko segmenta $ST$; dva kruga polumjera $r$ se sijeku kad su im središta na udaljenosti $\le 2r$. Svaka provjera svodi se na udaljenost točka–segment, segment–segment ili na pitanje: postiže li $|P + w s|$ vrijednost $\le R$ za neki $s \in [0, \ell]$?</p>
''',
        r'''
<p>Za pokretne krugove gledaj samo presjek vremenskih intervala: u njemu središte prijeđe pod-segment putanje (prije $u$ stoji u $S$, poslije $v$ u $T$). Za dva pokretna kruga relativno gibanje je po dijelovima linearno – razdvoji ga u trenucima $u_1, v_1, u_2, v_2$ i skaliraj s $(v_1 - u_1)(v_2 - u_2)$ da ostaneš u cijelim brojevima (<code>__int128</code>).</p>
''',
    ],
    'coach': [
        (r'Koji su objekti u igri i kad se dva „preklapaju”?',
         r'''
<p>Tri vrste: krug (točka $c$, prisutan na $[t-d, t+d]$), okvir klizača (kapsula polumjera $r$ oko segmenta $ST$, prisutan na $[u-d, v+d]$) i pokretni krug klizača (središte $p(t)$: $S$ za $t \le u$, jednoliko od $S$ do $T$ na $[u, v]$, $T$ za $t \ge v$; prisutan na $[u-d, v+d]$). Krug i okvir istog klizača su zasebni objekti i također tvore par (uvijek se sijeku). Dva objekta se sijeku ako u nekom zajedničkom trenutku njihovi oblici imaju zajedničku točku – za krug polumjera $r$ i kapsulu polumjera $r$ to je: udaljenost jezgri (točka/segment) $\le 2r$.</p>
'''),
        (r'Kako svaki od šest tipova parova svesti na cjelobrojnu provjeru?',
         r'''
<p>Ako se vremenski intervali ne presijecaju, par se ne siječe. Inače: krug–krug: $|c_1 - c_2|^2 \le (2r)^2$. Krug–okvir: udaljenost točke od segmenta $\le 2r$. Okvir–okvir: udaljenost segmenata $\le 2r$ – segmenti se sijeku ili je neki kraj jednog blizu drugog. Statični objekt–pokretni krug: u presjeku vremena $[lo, hi]$ središte prijeđe segment $p(lo)\,p(hi)$ (stegnuto na $[u,v]$), pa je to ponovno točka–segment odnosno segment–segment. Pokretni–pokretni: relativni položaj $p_1(t) - p_2(t)$ je po dijelovima linearan.</p>
'''),
        (r'Kako točno odgovoriti „postoji li $s \in [0, \ell]$ s $|P + w s| \le R$” bez realnih brojeva?',
         r'''
<p>$f(s) = |P + ws|^2 = A s^2 + B s + C$ s $A = w \cdot w$, $B = 2 P \cdot w$, $C = P \cdot P$. Provjerimo krajeve $f(0) \le R^2$ i $f(\ell) \le R^2$. Ako oba ne prolaze, minimum je unutar intervala samo ako je $B \lt 0$ i $-B \lt 2A\ell$ (tjeme $s^* = -B/(2A) \in (0, \ell)$); tada je $f(s^*) = C - B^2/(4A) \le R^2 \iff B^2 \ge 4A(C - R^2)$. Sve su veličine cijeli brojevi; kad položaje skaliramo s $D = v - u$ (ili s $D_1 D_2$), koordinate su do $10^{10}$, a umnošci do $\sim 10^{35}$ – stane u <code>__int128</code>.</p>
'''),
        (r'Zašto skaliranje s $D = v-u$ i kako se ponaša udaljenost točke od segmenta?',
         r'''
<p>Položaj $p(t) = S + (T - S)\frac{t-u}{v-u}$ nije cjelobrojan; pomnožen s $D = v-u$ jest: $D\,p(t) = SD + (T-S)(t-u)$. Uvjet „udaljenost $\le 2r$” skaliramo isto: $\le 2rD$. Udaljenost točke $P$ od segmenta $AB$ je $\min_{s\in[0,1]} |A - P + (B - A)s|$ – isti kvadratni test s $\ell = 1$. Za dva pokretna kruga skaliramo s $D_1 D_2$: $P = p_1 D_2 - p_2 D_1$, $w = (T_1 - S_1)D_2$ ako se prvi giba, minus $(T_2 - S_2)D_1$ ako se drugi giba, na svakom dijelu $[t_0, t_1]$ između točaka prekida.</p>
'''),
    ],
    'tips': [
        r'''Geometriju s krugovima jednakih polumjera svedi na udaljenosti jezgri (točaka/segmenata) i prag $2r$ – kapsula je Minkowskijev zbroj segmenta i kruga.''',
        r'''Jednoliko gibanje na intervalu s racionalnom brzinom skaliraj nazivnikom da sve ostane cjelobrojno; prije toga procijeni najveće međurezultate i po potrebi uzmi <code>__int128</code>.''',
        r'''Minimum kvadratne funkcije na segmentu: provjeri krajeve, pa tjeme samo ako je unutra – i to bez dijeljenja, uspoređivanjem $B^2$ i $4A(C-R^2)$.''',
        r'''Kad je sve „uključivo”, brute force mora biti egzaktan (racionalna aritmetika ili gusto uzorkovanje s točnim testom u cijelim brojevima); usporedba s približnim floatovima može lažno prijaviti razliku.''',
    ],
    'solution': r'''
<p>Vlastita izvedba (organizatori nisu objavili rješenja), potvrđena neovisnom implementacijom u točnoj racionalnoj aritmetici. Objekata je $\le 2n \le 2000$ (krug, okvir klizača, pokretni krug klizača), pa provjeravamo sve parove u $O(n^2)$. Krug i okvir su „jezgra” (točka, segment) proširena za $r$, pa se dva objekta sijeku točno kad su im vremenski intervali presječeni i jezgre na udaljenosti $\le 2r$. Za pokretni krug gledamo samo presjek vremena $[lo, hi]$, u kojem središte prijeđe pod-segment putanje; za dva pokretna kruga relativno gibanje je po dijelovima linearno (prekidi u $u_1, v_1, u_2, v_2$). Sve se svodi na test „$\exists s \in [0,\ell]$: $|P + ws|^2 \le R^2$” (krajevi i tjeme kvadratne funkcije, bez dijeljenja) te na udaljenost segment–segment; položaje skaliramo nazivnicima $v-u$ (odnosno $(v_1-u_1)(v_2-u_2)$) i računamo u <code>__int128</code>, s uključivim granicama.</p>
''',
    'detailed': r'''
<h3>1. Model</h3>
<p>Svaki objekt ima <em>jezgru</em> i <em>vremenski interval</em>:</p>
<ul>
<li>krug: jezgra točka $c$, interval $[t-d, t+d]$;</li>
<li>okvir klizača: jezgra segment $ST$, interval $[u-d, v+d]$;</li>
<li>pokretni krug klizača: jezgra točka $p(t)$ s $p(t) = S$ za $t \le u$, $p(t) = S + (T-S)\frac{t-u}{v-u}$ na $[u,v]$, $p(t) = T$ za $t \ge v$; interval $[u-d, v+d]$.</li>
</ul>
<p>Oblik objekta u trenutku $t$ je jezgra proširena za $r$ (krug, odnosno kapsula). Dva takva oblika imaju zajedničku točku točno kad je udaljenost jezgri $\le 2r$ (Minkowskijev zbroj). Objekti se sijeku ako postoji $t$ u presjeku intervala s tim svojstvom. Klizač daje <strong>dva</strong> objekta, pa je ukupno $N \le 2n \le 2000$ objekata i $\binom{N}{2} \lt 2 \cdot 10^6$ parova – dovoljno je svaki par provjeriti u $O(1)$.</p>
<h3>2. Osnovni test: točka blizu ishodišta na pravcu</h3>
<p><code>near_origin(P, w, ℓ, R)</code> odgovara na: postoji li $s \in [0, \ell]$ s $|P + ws|^2 \le R^2$? Neka je $f(s) = As^2 + Bs + C$, $A = w\cdot w$, $B = 2P\cdot w$, $C = P \cdot P$. Ako je $f(0) \le R^2$ ili $f(\ell) \le R^2$, da. Inače je $C \gt R^2$; ako je $A = 0$ ili $\ell = 0$, ne. Minimum na $(0,\ell)$ postoji samo ako je tjeme $s^* = -B/(2A)$ unutra: $B \lt 0$ i $-B \lt 2A\ell$. Tada je $f(s^*) = C - \frac{B^2}{4A} \le R^2 \iff B^2 \ge 4A(C - R^2)$. Nema dijeljenja, sve u cijelim brojevima. <em>Udaljenost točke $P$ od segmenta $AB$ je $\le R$</em> ⟺ <code>near_origin(A - P, B - A, 1, R)</code>.</p>
<h3>3. Udaljenost segment–segment</h3>
<p>Segmenti $AB$ i $CD$ su na udaljenosti $\le R$ ako se sijeku (standardni test s orijentacijama i kolinearnim slučajevima; degenerirani segmenti dopušteni) ili je neki od krajeva jednog na udaljenosti $\le R$ od drugog segmenta (kad se ne sijeku, najbliži par točaka uključuje kraj jednog od segmenata).</p>
<h3>4. Parovi</h3>
<p>Neka je $[lo, hi]$ presjek intervala; ako je prazan, par se ne siječe. Uredimo par tako da je tip prvog $\le$ tipu drugog (krug $\lt$ okvir $\lt$ pokretni).</p>
<ul>
<li>krug–krug: $|c_1 - c_2|^2 \le (2r)^2$;</li>
<li>krug–okvir: točka–segment s $R = 2r$;</li>
<li>okvir–okvir: segment–segment s $R = 2r$;</li>
<li>statični–pokretni: u $[lo, hi]$ središte prijeđe segment od $p(lo)$ do $p(hi)$ (funkcija $p$ je stegnuta na $[u,v]$, pa je i mirovanje u $S$ ili $T$ pokriveno). Skaliramo s $D = v - u$: $Dp(t) = SD + (T-S)(t - u)$ je cjelobrojno, prag postaje $2rD$, a statičnu jezgru množimo s $D$. Krug: <code>near_origin(P1 - cD, P2 - P1, 1, 2rD)</code>; okvir: segment–segment.</li>
<li>pokretni–pokretni: relativni položaj $p_1(t) - p_2(t)$ je linearan na svakom dijelu između točaka prekida $\{lo, hi\} \cup (\{u_1, v_1, u_2, v_2\} \cap (lo, hi))$. Skaliramo s $D = D_1 D_2$: na dijelu $[t_0, t_1]$ je $P = \tilde p_1(t_0) D_2 - \tilde p_2(t_0) D_1$ gdje je $\tilde p_i = D_i p_i$, brzina $w = (T_1 - S_1)D_2\,[u_1 \le t_0 \lt v_1] - (T_2 - S_2)D_1\,[u_2 \le t_0 \lt v_2]$, $\ell = t_1 - t_0$, $R = 2rD$. Ako je $lo = hi$, provjeri se samo trenutak $lo$.</li>
</ul>
<h3>5. Veličine brojeva</h3>
<p>Koordinate $\le 10^4$, $D_i \le 10^3$, pa su skalirani položaji $\le 10^{10}$ i $C = P\cdot P \le 2 \cdot 10^{20}$; $A \le 2\cdot 10^{14}$, $B \le 4 \cdot 10^{17}$, $B^2 \le 1.6 \cdot 10^{35}$, $4A(C - R^2) \le 2 \cdot 10^{35}$ – ispod $1.7 \cdot 10^{38}$, granice <code>__int128</code>. Zato su sve točke i skalarni produkti u <code>__int128</code>.</p>
<h3>6. Složenost i zamke</h3>
<ul>
<li>$O(N^2)$ parova s $O(1)$ radom (pokretni–pokretni najviše $5$ dijelova): trenutno.</li>
<li>Sve granice su uključive: presjek intervala $lo \le hi$, udaljenost $\le 2r$, dodir u jednoj točki se broji.</li>
<li>Presjek vremena može biti jedan trenutak ($lo = hi$) – tada je $\ell = 0$ i provjeravaju se samo položaji.</li>
<li>U primjeru krug $(3,3,2)$ i klizač $(5,5)\to(5,1)$ daju $3$ para: krug–okvir, krug–pokretni krug i okvir–pokretni krug istog klizača.</li>
</ul>
''',
    'verified': r'''uzorci 5/5, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 0.08 s).''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Tree', 'title_hr': 'Stablo', 'slug': 'C_tree',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Stablo s $n$ vrhova; vrh $i$ ima boju $a_i$, a $i$-ti brid spaja $fa_i$ i $i + 1$, ima boju $fc_i$ i duljinu $fw_i$. Jednostavan put je <em>dobar</em> ako svi vrhovi na njemu imaju istu boju i svi bridovi na njemu imaju istu boju (boja vrhova i boja bridova mogu se razlikovati).</p>
<p>$q$ operacija: boja vrha $x_i$ postaje $c_i$. Na početku i nakon svake operacije ispiši najveću duljinu dobrog puta.</p>
<h3>Ulaz</h3>
<p>$1 \le n, q \le 2 \cdot 10^5$; $a_1..a_n$ ($1 \le a_i \le n$); $fa_2..fa_n$ ($1 \le fa_i \lt i$); $fc_2..fc_n$ ($1 \le fc_i \le n$); $fw_2..fw_n$ ($0 \le fw_i \le 10^9$); $q$ redaka $x_i\ c_i$.</p>
<h3>Izlaz</h3>
<p>$q + 1$ redaka.</p>
<h3>Primjer</h3>
<p>$n = 5$, $a = (5,4,3,4,5)$, $fa = (1,2,3,1)$, $fc = (2,2,2,2)$, $fw = (4,9,2,6)$, operacije $(2,5), (4,5), (5,4), (3,5), (2,1)$: izlaz $6, 10, 10, 4, 15, 2$.</p>
''',
    'hints': [
        r'''
<p>Dobar put koristi samo bridove $(u, p(u))$ s $a_u = a_{p(u)}$ i svi su iste boje. Definiraj $D[v]$ = najdulji dobar put od $v$ prema dolje čiji bridovi imaju boju $fc_v$ (boju brida prema roditelju). Kako se $D[v]$ računa iz djece, i kako izgleda najbolji put s vrhom u $v$?</p>
''',
        r'''
<p>Statički: $D[v] = \max(0, \max\{ fw_u + D[u] : u \text{ dijete}, a_u = a_v, fc_u = fc_v\})$, a odgovor u $v$ je zbroj dva najveća $fw_u + D[u]$ među djecom iste boje vrha i <em>iste boje brida</em>. Promjena boje vrha $x$ mijenja $D$ na cijelom putu do korijena – treba dinamički DP.</p>
''',
        r'''
<p>Heavy-light dekompozicija: lagana djeca svakog vrha grupirana su po ključu (boja vrha, boja brida) u multisete; teški lanac je u segmentnom stablu s $(\max, +)$ funkcijama $y \mapsto \max(y + \alpha, \beta)$ i najboljim odgovorom. Promjena košta $O(\log^2 n)$.</p>
''',
    ],
    'coach': [
        (r'Kako izgleda statički DP za najdulji dobar put?',
         r'''
<p>Brid $(u, p(u))$ je <em>uporabljiv</em> ako je $a_u = a_{p(u)}$. Za vrh $v$ neka je $D[v]$ najdulji dobar put od $v$ prema dolje koji koristi samo bridove boje $fc_v$ (boja brida $v$–roditelj): $D[v] = \max(0, \max\{ fw_u + D[u] \})$ po djeci $u$ s $a_u = a_v$ i $fc_u = fc_v$. Put s najvišim vrhom $v$ i bojom bridova $c$ sastoji se od najviše dva „kraka” u djecu $u$ s $a_u = a_v$, $fc_u = c$; njegova duljina je zbroj dva najveća $fw_u + D[u]$ (ili jedan krak, ili $0$). Odgovor je maksimum po svim $v$ i $c$.</p>
'''),
        (r'Zašto obično prebrojavanje ne prolazi i što HLD daje?',
         r'''
<p>Promjena $a_x$ mijenja $D$ na svim precima do korijena – $O(n)$ po upitu. Heavy-light dekompozicija: svaki vrh ima najviše jedno teško dijete, a put do korijena prolazi $O(\log n)$ lanaca. Doprinos <em>laganih</em> djece držimo u strukturama u roditelju; doprinos teškog djeteta ne držimo eksplicitno, nego lanac opisujemo funkcijom „što lanac daje roditelju kao funkcija vrijednosti koja dolazi s dna”.</p>
'''),
        (r'Što točno pamti vrh $v$ o laganoj djeci?',
         r'''
<p>Za ključ $(\text{boja vrha } col, \text{boja brida } c)$ multiset vrijednosti $fw_u + D[u]$ laganih djece $u$ s $a_u = col$, $fc_u = c$; uz to po boji vrha $col$ multiset „zbroja para” (dva najveća) svake grupe te boje. Iz toga u $O(\log n)$ čitamo: $L = $ najbolje lagano dijete s ključem $(a_v, fc_v)$ (nastavak prema gore), $L_2$ s ključem $(a_v, fc_h)$ (partner teškog djeteta $h$ po boji njegova brida) i $\gamma_0 = $ najbolji par laganih djece boje $a_v$ s jednakom bojom brida.</p>
'''),
        (r'Kako lanac opisati elementom segmentnog stabla koji se može spajati?',
         r'''
<p>Za vrh $v$ neka $y = fw_h + D[h]$ dolazi od teškog djeteta $h$. Tada $fw_v + D[v] = \max(y + \alpha_v, \beta_v)$ gdje je $\alpha_v = fw_v$ ako $h$ smije nastaviti kroz $v$ prema gore ($a_h = a_v$ i $fc_h = fc_v$), inače $-\infty$, a $\beta_v = fw_v + L$. Najbolji put kroz $v$ koji koristi teško dijete je $y + \delta_v$, $\delta_v = L_2$ ako $a_h = a_v$ (i tada bridovi imaju boju $fc_h$), inače $-\infty$; $\gamma_v = \gamma_0$ je najbolji odgovor bez teškog djeteta. Segment lanca (gornji dio $U$ iznad donjeg $Lo$) spaja se: $\alpha = \alpha_{Lo} + \alpha_U$, $\beta = \max(\beta_U, \beta_{Lo} + \alpha_U)$, $\delta = \max(\delta_{Lo}, \alpha_{Lo} + \delta_U)$, $\gamma = \max(\gamma_{Lo}, \gamma_U, \beta_{Lo} + \delta_U)$ – to je asocijativno, pa ide u segmentno stablo.</p>
'''),
        (r'Što se sve mijenja pri promjeni boje vrha $x$?',
         r'''
<p>List za $x$ (ovisi o $a_x$) i list za roditelja ako je $x$ teško dijete (ovisi o $a_h$). Zatim za lanac koji sadrži $x$: ponovno pročitaj cijeli lanac iz segmentnog stabla – njegov $\gamma$ ide u globalni multiset odgovora, a njegov $\beta$ (vrijednost koju vrh lanca $t$ daje roditelju $p$) zamjenjuje staru vrijednost u grupama od $p$ pod ključem $(a_t, fc_t)$; onda osvježi list od $p$ i nastavi s lancem od $p$. $O(\log n)$ lanaca, svaki s $O(\log n)$ rada: $O(\log^2 n)$ po upitu.</p>
'''),
    ],
    'tips': [
        r'''Dinamički DP na stablu = HLD + segmentno stablo nad lancem s $(\max,+)$ matricama/funkcijama koje su zatvorene na kompoziciju; lagana djeca idu u multisete u roditelju.''',
        r'''Kad odgovor može biti „kroz vrh” (dva kraka), u element segmentnog stabla dodaj polja za „najbolji zatvoren odgovor” ($\gamma$) i „otvoren prema dolje” ($\delta$) – spoj je tada $\beta_{Lo} + \delta_U$.''',
        r'''Držanje „zbroja para” po grupi u drugom multisetu daje $\max$ po svim grupama iste boje bez obilaska grupa.''',
        r'''Razdvoji uvjete „dijete se smije spojiti s $v$” (boja vrha) i „put smije nastaviti prema roditelju” (i boja brida) – to su različiti uvjeti i miješanje ih je čest izvor grešaka.''',
    ],
    'solution': r'''
<p>Vlastita izvedba (organizatori nisu objavili rješenja), potvrđena brute forceom koji nakon svake operacije iscrpno traži najdulji dobar put. Brid $(u,p(u))$ je uporabljiv samo ako $a_u = a_{p(u)}$; $D[v]$ = najdulji dobar put od $v$ prema dolje s bridovima boje $fc_v$: $D[v] = \max(0, \max_{u: a_u=a_v, fc_u=fc_v} fw_u + D[u])$, a odgovor u $v$ je zbroj dva najveća kraka među djecima iste boje vrha i iste boje brida. Promjenu boje vrha obrađujemo dinamičkim DP-om nad HLD-om: lagana djeca su u roditelju grupirana po ključu (boja vrha, boja brida) u multisete (uz multiset zbrojeva dva najveća po boji vrha), a teški lanac je u segmentnom stablu čiji element čuva $(\max,+)$ funkciju $y \mapsto \max(y + \alpha, \beta)$ (što lanac daje roditelju kao funkcija vrijednosti teškog djeteta), najbolji zatvoreni odgovor $\gamma$ i „otvoreni” $\delta$. Promjena osvježava $O(\log n)$ lanaca, svaki u $O(\log n)$; odgovor je maksimum multiseta $\gamma$-vrijednosti lanaca. Ukupno $O((n + q)\log^2 n)$.</p>
''',
    'detailed': r'''
<h3>1. Struktura dobrog puta i statički DP</h3>
<p>Na dobrom putu svi vrhovi imaju istu boju, pa je svaki brid $(u, p(u))$ na njemu <em>uporabljiv</em>: $a_u = a_{p(u)}$; i svi bridovi imaju istu boju $c$. Put ima najviši vrh $v$ (LCA) i najviše dva kraka prema dolje. Definiramo za svaki vrh $v$</p>
<p>$$D[v] = \max\Big(0,\ \max\{ fw_u + D[u] : u \text{ dijete od } v,\ a_u = a_v,\ fc_u = fc_v \}\Big),$$</p>
<p>najdulji dobar put od $v$ prema dolje čiji bridovi imaju boju $fc_v$ – to je jedina boja bridova koja se od $v$ može nastaviti prema roditelju. Najbolji put s vrhom u $v$ i bojom bridova $c$ je zbroj dva najveća $fw_u + D[u]$ po djeci $u$ s $a_u = a_v$, $fc_u = c$ (ili jedan takav, ili $0$); primijeti da je za krak boje $c$ potrebno upravo $D[u]$, jer je $fc_u = c$. Odgovor je maksimum po $v$ i $c$. Ispravnost: svaki dobar put je oblika „dva kraka iz LCA” i obrnuto, a $D[u]$ je maksimum po definiciji.</p>
<h3>2. Heavy-light dekompozicija</h3>
<p>Uz $fa_i \lt i$ veličine podstabala i teško dijete <code>heavy[v]</code> (najveće podstablo) računamo jednim prolazom. Lanci dobivaju uzastopne pozicije; <code>top[v]</code> je vrh lanca, <code>bottom[t]</code> njegovo dno. Put od bilo kojeg vrha do korijena mijenja lanac $O(\log n)$ puta.</p>
<h3>3. Lagana djeca: grupe i zbrojevi parova</h3>
<p>U vrhu $v$ držimo <code>groups[v][(col, c)]</code> – multiset vrijednosti $fw_u + D[u]$ laganih djece $u$ s $a_u = col$ i $fc_u = c$ – te <code>pairsums[v][col]</code>, multiset „zbroja para” (najveći $+$ drugi najveći ili $0$) svake grupe $(col, \cdot)$. Iz njih čitamo u $O(\log n)$:</p>
<ul>
<li>$L = \max(0, \max \text{groups}[v][(a_v, fc_v)])$ – najbolji lagani krak koji se može nastaviti prema roditelju;</li>
<li>$L_2 = \max(0, \max \text{groups}[v][(a_v, fc_h)])$ – najbolji lagani partner teškog djeteta $h$ (isti $c = fc_h$);</li>
<li>$\gamma_0 = \max(0, \max \text{pairsums}[v][a_v])$ – najbolji put kroz $v$ samo iz laganih krakova.</li>
</ul>
<p>Vrijednost koju lagano dijete $u$ unosi pamtimo u <code>storedVal[u]</code>, <code>storedKey[u]</code> (boja pod kojom je uneseno) da bismo ju znali izbrisati.</p>
<h3>4. Element segmentnog stabla</h3>
<p>Za vrh $v$ s teškim djetetom $h$ neka je $y = fw_h + D[h]$. Tada:</p>
<ul>
<li>$fw_v + D[v] = \max(y + \alpha_v, \beta_v)$, gdje je $\alpha_v = fw_v$ ako $a_h = a_v$ i $fc_h = fc_v$ (krak kroz $h$ smije nastaviti u $v$ i dalje gore), inače $-\infty$; $\beta_v = fw_v + L$;</li>
<li>najbolji zatvoreni odgovor u $v$ bez teškog djeteta: $\gamma_v = \gamma_0$;</li>
<li>najbolji odgovor u $v$ koji koristi teški krak: $y + \delta_v$, gdje je $\delta_v = L_2$ ako $a_h = a_v$ (bridovi tada moraju imati boju $fc_h$, a uvjet $fc_h = fc_v$ nije potreban – put završava u $v$), inače $-\infty$.</li>
</ul>
<p>Spajanje gornjeg dijela $U$ i donjeg $Lo$ (u $Lo$ ulazi $y$ s dna, iz $Lo$ izlazi $y' = \max(y + \alpha_{Lo}, \beta_{Lo})$ u $U$):</p>
<p>$$\alpha = \alpha_{Lo} + \alpha_U,\quad \beta = \max(\beta_U,\ \beta_{Lo} + \alpha_U),\quad \delta = \max(\delta_{Lo},\ \alpha_{Lo} + \delta_U),\quad \gamma = \max(\gamma_{Lo},\ \gamma_U,\ \beta_{Lo} + \delta_U).$$</p>
<p>Obrazloženje: $\max(y' + \alpha_U, \beta_U) = \max(y + \alpha_{Lo} + \alpha_U,\ \beta_{Lo} + \alpha_U,\ \beta_U)$; „otvoreni” odgovor kroz $U$ s ulazom $y'$ je $y' + \delta_U$, što se s $y$ raspiše u $y + \alpha_{Lo} + \delta_U$ (ostaje otvoren) i $\beta_{Lo} + \delta_U$ (zatvoren). Dno lanca ima $y = -\infty$, pa je za cijeli lanac $fw_t + D[t] = \beta$ i najbolji odgovor $\gamma$ (svi otvoreni članovi propadaju). Zbrajanja s $-\infty$ štitimo funkcijom <code>add</code> koja rezultat steže odozdo.</p>
<h3>5. Obrada operacije $a_x := c$</h3>
<ol>
<li>Osvježi list $x$ (ovisi o $a_x$) i list roditelja ako je $x$ teško dijete (ovisi o $a_h$).</li>
<li>Za lanac s vrhom $t$ koji sadrži $x$: pročitaj $(\alpha,\beta,\gamma,\delta)$ cijelog lanca; zamijeni stari $\gamma$ lanca u globalnom multisetu <code>answers</code>; ako $t$ ima roditelja $p$: izbriši staru vrijednost iz <code>groups[p][(storedKey[t], fc_t)]</code>, unesi $\beta$ pod $(a_t, fc_t)$, osvježi list $p$ i ponovi za lanac od $p$.</li>
<li>Odgovor je najveći element <code>answers</code>.</li>
</ol>
<p>Početno stanje gradimo naivnim DP-om (djeca imaju veće indekse od roditelja) i punjenjem svih struktura.</p>
<h3>6. Složenost</h3>
<p>Po upitu $O(\log n)$ lanaca; za svaki: upit segmentnog stabla $O(\log n)$, operacije na multisetima $O(\log n)$, dvije točkaste izmjene $O(\log n)$. Ukupno $O((n+q)\log^2 n)$ s $n, q \le 2\cdot10^5$ – oko $1$ s na velikim testovima. Memorija $O(n)$ (svaki vrh je u točno jednom multisetu roditelja).</p>
<h3>7. Zamke</h3>
<ul>
<li>Uvjet za $\delta_v$ je samo $a_h = a_v$, a za $\alpha_v$ još i $fc_h = fc_v$ – zamjena tih uvjeta daje pogrešne odgovore koje primjeri ne otkrivaju.</li>
<li>Pri brisanju iz grupe koristi zapamćeni ključ (stara boja vrha lanca), ne trenutni $a_t$.</li>
<li>Duljine do $10^9 \cdot 2\cdot 10^5$ – <code>long long</code>; $-\infty$ mora biti dovoljno negativan da zbrojevi ne prelijevaju (<code>add</code>).</li>
<li>Vrh bez teškog djeteta: $\alpha = \delta = -\infty$, $L_2 = 0$.</li>
</ul>
''',
    'verified': r'''uzorci 1/1, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 1.01 s).''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Alice and Bob', 'title_hr': 'Alice i Bob', 'slug': 'D_alice_and_bob',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Alice i Bob naizmjence (Alice prva) izvode operaciju nad permutacijom $p$: preslože elemente $p_1, \dots, p_{p_1}$ u proizvoljan redoslijed. Igrač koji izvede dvije operacije s istom vrijednošću $p_1$ gubi. Oba igraju optimalno.</p>
<p>Koliko permutacija veličine $n$ Bob dobiva? Odgovor modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 10^7$.</p>
<h3>Izlaz</h3>
<p>Jedan broj.</p>
<h3>Primjer</h3>
<p>$n = 1 \to 1$; $n = 2 \to 1$; $n = 10 \to 997920$; $n = 100 \to 188898954$.</p>
''',
    'hints': [
        r'''
<p>Alice je prisiljena odigrati potez s $p_1$. Pogledaj što se događa ako je $p_1$ <em>najmanji</em> element među $p_1, \dots, p_{p_1}$: može li Alice tada išta pametno napraviti, ili joj Bob može „vratiti” istu permutaciju?</p>
''',
        r'''
<p>Ako u prefiksu $p_1, \dots, p_{p_1}$ postoji $u \lt p_1$, Alice može najmanji takav $u$ staviti na prvo mjesto i iza njega poredati $u - 1$ elemenata većih od $u$ (i pri tome izbjeći vrijednost $p_1$ koju je već potrošila). Tko je sad u problemu?</p>
''',
        r'''
<p>Bob dobiva točno permutacije u kojima je $p_1 = \min(p_1, \dots, p_{p_1})$. Prebroji ih po vrijednosti $i = p_1$: pozicije $2, \dots, i$ pune se elementima iz $\{i+1, \dots, n\}$, a ostatak proizvoljno.</p>
''',
    ],
    'coach': [
        (r'Prvi potez je prisilan: Alice mora odigrati s $p_1 = v$. Što ako je $v$ najmanji element prefiksa $p_1, \dots, p_v$?',
         r'''
<p>Alice preslaže samo pozicije $1, \dots, v$ i dobiva neku permutaciju s $p_1 = x \ge v$ (svi elementi prefiksa su $\ge v$). Bob tada smije preslagati pozicije $1, \dots, x \supseteq 1, \dots, v$, pa može <strong>vratiti početnu permutaciju</strong>. Alice je opet pred $p_1 = v$, a $v$ je već potrošila – gubi odmah. Bob je potrošio samo jednu vrijednost, pa mu ništa ne prijeti.</p>
'''),
        (r'Što ako prefiks $p_1, \dots, p_v$ sadrži element manji od $v$? Zašto Alice bira baš najmanji takav?',
         r'''
<p>Neka je $u = \min(p_1, \dots, p_v) \lt v$. Alice stavi $u$ na prvo mjesto i na pozicije $2, \dots, u$ stavi $u - 1$ elemenata prefiksa koji su veći od $u$, ali <em>različiti od $v$</em>: takvih ima $v - 2 \ge u - 1$, jer je $u$ minimum. Sada je Bob u „zatvorenoj” poziciji: $p_1 = u$ je minimum svog prefiksa, a prefiks duljine $u$ ne sadrži $v$.</p>
'''),
        (r'Zašto Bob iz te pozicije gubi, tj. zašto Alice može primijeniti isti argument vraćanja?',
         r'''
<p>Bob preslaže pozicije $1, \dots, u$ i dobiva $p_1 = x$ iz tog prefiksa, dakle $x \ne v$. Alice smije odigrati s $x$ (potrošila je samo $v$) i vratiti Bobovu permutaciju natrag. Bob je opet pred $p_1 = u$ koje je već potrošio – gubi. Posebno, za $u = 1$ nema što preslagati: Bob troši $1$, Alice troši $1$, Bob mora ponovno igrati s $1$.</p>
'''),
        (r'Kako prebrojiti permutacije u kojima je $p_1$ minimum prefiksa $p_1, \dots, p_{p_1}$?',
         r'''
<p>Fiksiramo $p_1 = i$. Pozicije $2, \dots, i$ moraju sadržavati $i - 1$ različitih vrijednosti iz $\{i+1, \dots, n\}$ (ima ih $n - i$, pa treba $i - 1 \le n - i$, tj. $2i - 1 \le n$), u proizvoljnom redoslijedu: $\binom{n-i}{i-1}(i-1)!$ načina. Preostalih $n - i$ vrijednosti proizvoljno popunjava ostatak: $(n-i)!$. Ukupno $\frac{(n-i)!\,(n-i)!}{(n-2i+1)!}$; zbrajamo po svim $i$ s $2i - 1 \le n$ uz predračun faktorijela i inverznih faktorijela do $n = 10^7$.</p>
'''),
    ],
    'tips': [
        r'''<strong>Strategija vraćanja (mirroring).</strong> Kad protivnik smije mijenjati samo podskup pozicija koji je sadržan u onome što ti smiješ mijenjati, često možeš „poništiti” njegov potez – a pravilo o ponavljanju tada kažnjava njega, ne tebe.''',
        r'''Za igre na permutacijama prvo napiši brute force nad cijelim stanjem (permutacija + iskorištene vrijednosti oba igrača + tko je na potezu) za $n \le 6$ i pogodi karakterizaciju dobitnih pozicija; formulu zatim dokaži.''',
        r'''Predračun faktorijela do $10^7$ modulo prost broj: jedan niz <code>fact</code>, jedan niz inverznih faktorijela izračunat unatrag iz $\mathrm{fact}[n]^{-1}$ – bez posebnog inverza po članu.''',
    ],
    'solution': r'''
<p>Vlastita izvedba (organizatori nisu objavili rješenja; javne analize postoje na blogu sheauhaw.com i u raspravi na QOJ-u); karakterizacija dobitnih permutacija provjerena je brute forceom nad cijelim stanjem igre. Neka je $v = p_1$. Ako je $v$ najmanji element prefiksa $p_1, \dots, p_v$, Bob pobjeđuje: što god Alice napravi s pozicijama $1, \dots, v$, novi $p_1 = x \ge v$ dopušta Bobu da preslaže pozicije $1, \dots, x \supseteq 1, \dots, v$ i vrati početnu permutaciju, pa Alice mora drugi put igrati s $v$. Inače Alice uzme $u = \min(p_1, \dots, p_v) \lt v$, stavi ga na prvo mjesto, iza njega poreda $u - 1$ elemenata većih od $u$ i različitih od $v$, i istim argumentom vraćanja pobjeđuje. Bob dobiva točno permutacije s $p_1 = \min(p_1, \dots, p_{p_1})$; za $p_1 = i$ ih je $\binom{n-i}{i-1}(i-1)!\,(n-i)! = \frac{(n-i)!^2}{(n-2i+1)!}$, pa je odgovor $\sum_{2i-1 \le n} \frac{(n-i)!^2}{(n-2i+1)!} \bmod 998244353$, u $O(n)$ s predračunatim faktorijelima.</p>
''',
    'detailed': r'''
<h3>1. Pravila igre u jednoj rečenici</h3>
<p>Igrač na potezu čita $v = p_1$; ako je s tom vrijednošću već igrao, gubi; inače je zapisuje kao iskorištenu i proizvoljno preslaguje pozicije $1, \dots, v$. Bitno je da je skup iskorištenih vrijednosti <em>osoban</em> – Alicine potrošene vrijednosti ne smetaju Bobu.</p>
<h3>2. „Zatvorene” pozicije: $p_1$ je minimum svog prefiksa</h3>
<p>Neka je $v = p_1 = \min(p_1, \dots, p_v)$ i Alice na potezu. Ona preslaguje pozicije $1, \dots, v$; svi elementi tog prefiksa su $\ge v$, pa je nakon poteza $p_1 = x \ge v$. Bob smije preslagati pozicije $1, \dots, x$, a to uključuje sve pozicije koje je Alice dirala. Bob jednostavno <strong>vrati početnu permutaciju</strong>. Alice je ponovno pred $p_1 = v$, ali $v$ je već potrošila – gubi odmah. Bob je pri tome potrošio jednu vrijednost ($x$), što mu ne može škoditi jer igra završava. Dakle: <em>igrač na potezu u zatvorenoj poziciji gubi</em> (uz uvjet da protivnik još nije potrošio vrijednost $x$ – to ćemo osigurati u sljedećem koraku).</p>
<h3>3. „Otvorene” pozicije: prefiks sadrži manji element</h3>
<p>Neka prefiks $p_1, \dots, p_v$ sadrži element manji od $v$ i neka je $u$ najmanji element prefiksa. Alice potroši $v$ i složi prefiks ovako: $u$ na poziciju $1$, a na pozicije $2, \dots, u$ bilo kojih $u - 1$ elemenata prefiksa koji su veći od $u$ i različiti od $v$. Takvih elemenata ima $v - 2$ (svi osim $u$ i $v$, a svi su $> u$ jer je $u$ minimum), i $v - 2 \ge u - 1$ zbog $u \le v - 1$. Ostatak prefiksa složi proizvoljno.</p>
<p>Bob je sad u zatvorenoj poziciji s $p_1 = u$: preslaguje pozicije $1, \dots, u$, čiji elementi su svi $\ge u$ i <em>nijedan nije $v$</em>. Novi $p_1 = x$ dolazi iz tog prefiksa, pa je $x \ne v$ i Alice ga smije odigrati (potrošila je samo $v$). Alice vrati Bobovu permutaciju; Bob je ponovno pred $p_1 = u$ koje je potrošio – gubi. Rubni slučaj $u = 1$: prefiks duljine $1$ ne može se mijenjati, Bob troši $1$, Alice troši $1$, Bob mora ponovno igrati s $1$ i gubi – isti zaključak.</p>
<p>Zaključak: <strong>Bob pobjeđuje točno kada je $p_1 = \min(p_1, \dots, p_{p_1})$.</strong> Provjera na primjerima: $n = 1$ ($p = (1)$) i $n = 2$ (samo $(1, 2)$; u $(2, 1)$ Alice napravi $(1, 2)$ i pobjeđuje) daju $1$, kako treba.</p>
<h3>4. Prebrojavanje</h3>
<p>Fiksiramo $p_1 = i$. Pozicije $2, \dots, i$ moraju sadržavati $i - 1$ različitih vrijednosti iz $\{i+1, \dots, n\}$; tih vrijednosti ima $n - i$, pa mora biti $i - 1 \le n - i$, tj. $2i - 1 \le n$. Biramo ih i poredamo na $\binom{n-i}{i-1}(i-1)!$ načina, a preostalih $n - i$ vrijednosti popunjava pozicije $i+1, \dots, n$ na $(n-i)!$ načina. Ukupno</p>
<p>$$\binom{n-i}{i-1}(i-1)!\,(n-i)! = \frac{(n-i)!}{(n-2i+1)!}\,(n-i)! = \frac{(n-i)!^2}{(n-2i+1)!},$$</p>
<p>a odgovor je $\sum_{i \ge 1,\ 2i-1 \le n} \frac{(n-i)!^2}{(n-2i+1)!} \bmod 998244353$. Za $n = 2$: samo $i = 1$ daje $\frac{1!^2}{1!} = 1$. Za $n = 10$ formula daje $997920$, kao u primjeru.</p>
<h3>5. Implementacija i složenost</h3>
<p>Predračunamo $\mathrm{fact}[0..n]$ i inverzne faktorijele (jedan modularni inverz $\mathrm{fact}[n]^{-1}$ brzim potenciranjem, pa unatrag $\mathrm{inv}[i-1] = \mathrm{inv}[i] \cdot i$). Petlja po $i$ ima $\lfloor (n+1)/2 \rfloor$ članova. Vrijeme $O(n)$, memorija dva niza od $n + 1$ <code>int</code>-ova ($\approx 80$ MB za $n = 10^7$, unutar $1024$ MiB). Množenja radimo u 64-bitnoj aritmetici jer su faktori $\lt 2^{30}$.</p>
''',
    'verified': r'''uzorci 4/4, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 0.13 s).''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Neighbourhood', 'title_hr': 'Susjedstvo', 'slug': 'E_neighbourhood',
    'tl': '10 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Stablo s $n$ vrhova i težinskim bridovima $w_i$. $q$ operacija:</p>
<ul>
<li><code>1 i c</code> — $w_i := c$;</li>
<li><code>2 x d</code> — prebroji vrhove $y$ za koje je udaljenost od $x$ do $y$ najviše $d$.</li>
</ul>
<h3>Ulaz</h3>
<p>$2 \le n \le 2 \cdot 10^5$, $1 \le q \le 2 \cdot 10^5$; $n - 1$ bridova $x_i\ y_i\ w_i$ ($1 \le w_i \le 10^9$); operacije s $1 \le i \le n - 1$, $1 \le c \le 10^9$, $0 \le d \le 2 \cdot 10^{14}$.</p>
<h3>Izlaz</h3>
<p>Za svaku operaciju tipa 2 jedan broj.</p>
<h3>Primjer</h3>
<p>Bridovi $(1,2,3), (2,3,1)$; operacije <code>2 2 1</code>, <code>2 1 3</code>, <code>2 3 4</code>, <code>1 1 1</code>, <code>2 2 1</code>, <code>2 1 0</code>, <code>2 3 1</code>: izlaz $2, 2, 3, 3, 1, 2$.</p>
''',
    'hints': [
        r'''
<p>Bez promjena težina zadatak je klasičan: centroidna dekompozicija i za svaki centroidni predak $c$ od $x$ prebroji $y$ u komponenti od $c$ s $\mathrm{dist}(c,y) \le d - \mathrm{dist}(c,x)$ (sortirane udaljenosti + binarno pretraživanje), oduzimajući ono što se dvaput broji.</p>
''',
        r'''
<p>Promjena težine brida $e$ mijenja $\mathrm{dist}(c, y)$ za točno one $y$ koji su u komponenti centroida $c$ „ispod” $e$ – u DFS poretku iz $c$ to je jedan <em>interval</em>. Dakle po centroidu treba niz s operacijama „dodaj konstantu na interval” i „prebroji elemente $\le T$ na intervalu”.</p>
''',
        r'''
<p>Sqrt-dekompozicija po blokovima: svaki blok ima sortiranu kopiju i lijeni pomak; dodavanje na cijeli blok je $O(1)$, na dio bloka se sortirana kopija popravlja spajanjem (merge) u $O(S)$; upit je binarno pretraživanje po blokovima. Veličine komponenata se po razinama polove, pa je ukupno $O((n+q)\sqrt{n}\log n)$ – u granici $10$ s.</p>
''',
    ],
    'coach': [
        (r'Kako bi zadatak riješio bez operacija tipa 1?',
         r'''
<p>Centroidnom dekompozicijom. Svaki vrh $x$ ima $O(\log n)$ centroidnih predaka $c$; za par $(x, y)$ postoji jedinstveni „najviši” centroid $c$ koji je na putu $x \to y$ (najbliži zajednički predak u centroidnom stablu), i za njega vrijedi $\mathrm{dist}(x,y) = \mathrm{dist}(x,c) + \mathrm{dist}(c,y)$. Za svaki centroid pamtimo udaljenosti do svih vrhova njegove komponente; upit $(x, d)$ za svaki predak $c$ broji $y$ s $\mathrm{dist}(c,y) \le d - \mathrm{dist}(c,x)$ u komponenti od $c$, i <em>oduzima</em> isti broj u pod-komponenti (dijelu nakon uklanjanja $c$) koja sadrži $x$ – ti su $y$ pogrešno prebrojeni (put $x \to y$ ne ide kroz $c$) i točno se broje na dubljim razinama.</p>
'''),
        (r'Zašto je „oduzimanje pod-komponente” točno?',
         r'''
<p>Fiksirajmo $y$. Neka je $c^*$ najviši centroid na putu $x \to y$ – to je LCA od $x$ i $y$ u centroidnom stablu. Za pretka $c$ od $x$ strogo iznad $c^*$ vrh $y$ je u istoj pod-komponenti kao $x$, pa ga zbrajanje i oduzimanje ponište – ali samo ako u obje sume koristimo <em>isti</em> prag. Prag je $d - \mathrm{dist}(c, x)$ u oba slučaja, pa se poništavaju. Za $c = c^*$ je $y$ u drugoj pod-komponenti (ili $y = c^*$), broji se jednom, i to s ispravnim uvjetom $\mathrm{dist}(c^*, x) + \mathrm{dist}(c^*, y) = \mathrm{dist}(x,y) \le d$. Za pretke ispod $c^*$ (dublje) $y$ nije u komponenti – ne broji se. Ukupno točno jedan doprinos po $y$.</p>
'''),
        (r'Što se dogodi s tim udaljenostima kad se promijeni težina brida $e = (u, v)$ za $\Delta$?',
         r'''
<p>Za centroid $c$ čija komponenta sadrži $e$: $\mathrm{dist}(c, y)$ poraste za $\Delta$ točno za $y$ u podstablu (unutar komponente, korijenjene u $c$) ispod dubljeg kraja $e$. Ako udaljenosti po komponenti zapišemo u DFS poretku iz $c$, to je interval $[\mathrm{tin}, \mathrm{tout}]$ toga kraja. Brid pripada $O(\log n)$ komponentama (po jednoj na svakoj razini dok ga neki centroid ne razdvoji), pa za svaki brid pamtimo popis (struktura, interval).</p>
'''),
        (r'Koja struktura podržava „dodaj na interval” i „prebroji $\le T$ na intervalu” dovoljno brzo?',
         r'''
<p>Blokovi veličine $S \approx \sqrt m$. Za svaki blok: sortirana kopija vrijednosti (s indeksima) i lijeni pomak <code>lazy</code>. Dodavanje na interval: rubne blokove popravimo – izdvojimo pogođene elemente (već sortirane), dodamo im $\Delta$, i spojimo (merge) natrag s nepogođenima u $O(S)$; unutarnjim blokovima samo <code>lazy += Δ</code>. Prebrojavanje $\le T$: rubni blokovi linearno, unutarnji binarnim pretraživanjem s pragom $T - \text{lazy}$. Obje operacije $O(\sqrt m \log m)$ za niz duljine $m$.</p>
'''),
        (r'Kako iz toga izlazi ukupna složenost i stane li u $10$ s?',
         r'''
<p>Komponente na razini $i$ imaju veličinu $\le n/2^i$, pa upit i promjena obrađuju $O(\log n)$ struktura s ukupnim troškom $\sum_i O(\sqrt{n/2^i}\log n) = O(\sqrt n \log n)$ – geometrijski niz. Ukupno $O((n + q)\sqrt n \log n) \approx 4\cdot10^5 \cdot 450 \cdot 18 \approx 3\cdot10^9$ vrlo jednostavnih operacija na gornjoj granici, u praksi ispod $5$ s uz $O(n \log n)$ memorije (oko $280$ MB, ispod $1024$ MiB). Gradnju radimo iterativno (eksplicitni stog) zbog dubine.</p>
'''),
    ],
    'tips': [
        r'''Centroidna dekompozicija za upite oblika „koliko $y$ ima $\mathrm{dist}(x,y) \le d$”: zbroji po centroidnim precima, oduzmi pod-komponentu s $x$ – isti prag u obje sume jamči da se svaki $y$ broji točno jednom.''',
        r'''DFS poredak iz centroida pretvara „podstablo” u interval, pa se promjena brida pretvara u dodavanje na interval – i to na svakoj od $O(\log n)$ razina kojima brid pripada.''',
        r'''Kad treba i dodavanje na interval i prebrojavanje po pragu, sqrt-dekompozicija sa sortiranim kopijama blokova je jednostavna i brza (merge umjesto ponovnog sortiranja); zbroj $\sqrt{n/2^i}$ po razinama je geometrijski.''',
        r'''Prije upita provjeri $\mathrm{dist}(c, x) \gt d$ – tada preskoči cijelu razinu (prag bi bio negativan).''',
    ],
    'solution': r'''
<p>Prema javnoj analizi (blog LJC00118 na cnblogs, centroidna dekompozicija s blokovnim nizovima) i vlastitoj izvedbi, potvrđeno brute forceom (Dijkstra/DFS po upitu). Centroidna dekompozicija: za svaki centroid $c$ pamtimo $\mathrm{dist}(c, y)$ svih vrhova njegove komponente u DFS poretku iz $c$. Upit $(x, d)$ za svaki centroidni predak $c$ od $x$ (za koji je $\mathrm{dist}(c,x) \le d$) zbraja broj $y$ u komponenti s $\mathrm{dist}(c,y) \le d - \mathrm{dist}(c,x)$ i oduzima isti broj unutar pod-komponente koja sadrži $x$ (ti se $y$ broje na dubljoj razini); svaki $y$ se tako broji točno jednom – na LCA-u od $x$ i $y$ u centroidnom stablu. Promjena težine brida za $\Delta$ dodaje $\Delta$ na interval DFS poretka (podstablo ispod brida) u svakoj od $O(\log n)$ komponenata koje brid sadrže. Niz s operacijama „dodaj na interval” i „prebroji $\le T$ na intervalu” držimo sqrt-dekompozicijom: blokovi sa sortiranom kopijom i lijenim pomakom, rubni blokovi se popravljaju spajanjem u $O(S)$, unutarnji binarnim pretraživanjem. Kako se veličine komponenata polove, po operaciji je $O(\sqrt n \log n)$; ukupno $O((n+q)\sqrt n\log n)$, oko $4$–$5$ s i $280$ MB na najvećim testovima.</p>
''',
    'detailed': r'''
<h3>1. Centroidna dekompozicija i prebrojavanje bez promjena</h3>
<p>Centroid komponente je vrh čijim uklanjanjem sve preostale komponente imaju $\le$ pola vrhova; rekurzivnim uklanjanjem centroida nastaje <em>centroidno stablo</em> dubine $O(\log n)$. Za centroid $c$ neka je $C(c)$ komponenta u kojoj je $c$ postao centroid.</p>
<p><strong>Lema 1.</strong> Za vrhove $x, y$ neka je $c^*$ njihov LCA u centroidnom stablu. Tada je $c^*$ na putu $x \to y$ u stablu, pa $\mathrm{dist}(x,y) = \mathrm{dist}(x, c^*) + \mathrm{dist}(c^*, y)$. <em>Dokaz.</em> $x, y \in C(c^*)$, a nakon uklanjanja $c^*$ su u različitim pod-komponentama (ili je jedan od njih $c^*$); povezani put unutar $C(c^*)$ stoga prolazi kroz $c^*$. $\square$</p>
<p>Upit $(x, d)$: za svaki centroidni predak $c$ od $x$ (uključivo $x$) s $\mathrm{dist}(c,x) \le d$ neka je $T = d - \mathrm{dist}(c,x)$;</p>
<p>$$\text{odgovor} = \sum_{c} \Big( \#\{y \in C(c) : \mathrm{dist}(c,y) \le T\} - \#\{y \in P_c(x) : \mathrm{dist}(c,y) \le T\} \Big),$$</p>
<p>gdje je $P_c(x)$ pod-komponenta od $C(c) \setminus \{c\}$ koja sadrži $x$ (prazna za $c = x$).</p>
<p><strong>Lema 2.</strong> Formula broji svaki $y$ s $\mathrm{dist}(x,y) \le d$ točno jednom, a ostale nijednom. <em>Dokaz.</em> Fiksirajmo $y$ i $c^* = \mathrm{LCA}(x,y)$. Predak $c$ strogo iznad $c^*$: $y \in P_c(x)$ (jer $x, y$ ostaju zajedno do $c^*$), pa je $y$ u obje sume s <em>istim</em> pragom $T$ i doprinos je $0$. Predak $c = c^*$: $y \in C(c^*) \setminus P_{c^*}(x)$, doprinos $[\mathrm{dist}(c^*,y) \le d - \mathrm{dist}(c^*,x)] = [\mathrm{dist}(x,y) \le d]$ po Lemi 1. Ako je $\mathrm{dist}(c^*, x) \gt d$, razinu preskačemo, što je u skladu jer je tada i $\mathrm{dist}(x,y) \gt d$. Preci ispod $c^*$: $y \notin C(c)$, doprinos $0$. $\square$</p>
<h3>2. Promjena težine brida</h3>
<p>Za centroid $c$ udaljenosti $\mathrm{dist}(c, y)$, $y \in C(c)$, zapišemo u niz u DFS poretku iz $c$ (DFS unutar $C(c)$). Podstablo svakog vrha $v \ne c$ (u korijenjenju iz $c$) je interval $[\mathrm{tin}_v, \mathrm{tout}_v]$. Brid $e = (v, \mathrm{par}(v))$ u $C(c)$ mijenja $\mathrm{dist}(c, y)$ za $\Delta$ točno za $y$ u podstablu od $v$: <em>dodavanje $\Delta$ na interval</em>. Brid pripada komponentama $C(c)$ za centroide $c$ na putu od korijena centroidnog stabla do LCA-a njegovih krajeva – $O(\log n)$ komponenata; te parove (struktura, interval) spremamo u <code>edgeRanges[e]</code> pri gradnji. Za svaki vrh $x$ i svaki njegov centroidni predak spremamo <code>anc[x]</code>: strukturu, poziciju $x$ (za čitanje $\mathrm{dist}(c,x)$ – i ona se mijenja!) i interval pod-komponente $P_c(x)$ (podstablo djeteta od $c$ na putu do $x$).</p>
<h3>3. Struktura: dodaj na interval, prebroji $\le T$ na intervalu</h3>
<p>Niz duljine $m$ dijelimo u blokove veličine $S = \lfloor\sqrt m\rfloor + 1$. Za svaki blok držimo: vrijednosti $a$, sortiranu kopiju <code>sv</code> s pripadnim indeksima <code>sidx</code>, i lijeni pomak <code>lazy</code> (stvarna vrijednost je $a_i + \text{lazy}_{b(i)}$).</p>
<ul>
<li><strong>Dodaj $\Delta$ na $[l, r]$:</strong> unutarnji blokovi: <code>lazy += Δ</code>. Rubni blok: $a_i += \Delta$ za $i \in [l,r]$; sortiranu kopiju rastavimo na pogođene (kojima dodamo $\Delta$ – ostaju sortirani među sobom) i nepogođene, pa ih spojimo (merge) u $O(S)$. Ukupno $O(S + m/S) = O(\sqrt m)$.</li>
<li><strong>Prebroji $\le T$ na $[l, r]$:</strong> rubni blokovi linearno ($a_i + \text{lazy} \le T$), unutarnji blokovi <code>upper_bound</code> po <code>sv</code> s pragom $T - \text{lazy}$: $O(S + (m/S)\log S) = O(\sqrt m \log m)$.</li>
</ul>
<h3>4. Algoritam</h3>
<ol>
<li>Gradnja (iterativno, eksplicitnim stogom – dubina stabla može biti $2\cdot10^5$): za komponentu nađi centroid (veličine podstabala iz proizvoljnog korijena, spusti se u dijete s $sz \gt$ pola), DFS iz centroida s $\mathrm{tin}/\mathrm{tout}$, udaljenostima i „vršnim djetetom” (dijete od $c$ na putu), izgradi blokovnu strukturu, upiši <code>edgeRanges</code> i <code>anc</code>, ukloni $c$ i nastavi po pod-komponentama.</li>
<li>Tip 1: $\Delta = c - w_i$; za svaki $(sid, l, r) \in$ <code>edgeRanges[i]</code> pozovi <code>range_add</code>.</li>
<li>Tip 2: za svaki $(sid, pos, subL, subR) \in$ <code>anc[x]</code>: $d_x = $ <code>get(pos)</code>; ako $d_x \gt d$ preskoči; inače dodaj <code>count_le(0, m-1, d - d_x)</code> i oduzmi <code>count_le(subL, subR, d - d_x)</code> ako pod-komponenta postoji.</li>
</ol>
<h3>5. Složenost i memorija</h3>
<p>Komponente na razini $i$ imaju $\le n/2^i$ vrhova, pa je trošak jedne operacije $\sum_i O(\sqrt{n/2^i}\log n) = O(\sqrt n\log n)$ (geometrijski niz). Ukupno $O((n+q)\sqrt n\log n)$; s $n = q = 2\cdot10^5$ izmjereno oko $4$–$5$ s na najgorim generiranim testovima (dugačke „gusjenice”, zvijezde, slučajna stabla; polovica upita promjene), unutar $10$ s. Memorija: svaki vrh je u $O(\log n)$ komponenata, po zapisu nekoliko 64-bitnih brojeva – oko $280$ MB, ispod $1024$ MiB.</p>
<h3>6. Zamke</h3>
<ul>
<li>$\mathrm{dist}(c, x)$ se mijenja promjenama bridova – čitaj ju iz strukture (<code>get</code>), ne iz statičke tablice.</li>
<li>Udaljenosti do $2\cdot10^5 \cdot 10^9 = 2\cdot10^{14}$ i $d \le 2\cdot10^{14}$: <code>long long</code>.</li>
<li>Rubni blokovi pri <code>range_add</code> kad su $l$ i $r$ u istom bloku: jedan <code>partial_add</code>, ne dva.</li>
<li>Rekurzivni DFS na stablu dubine $2\cdot10^5$ može srušiti stog – zato iterativno.</li>
</ul>
''',
    'verified': r'''uzorci 1/1, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 5.28 s).''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Cover', 'title_hr': 'Pokrivanje', 'slug': 'F_cover',
    'tl': '5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Stablo s $n$ vrhova, stupanj svakog vrha najviše $k$. Dano je $m$ putova $(a_i, b_i)$ s težinama $w_i$; put pokriva brid $e$ ako uklanjanje $e$ razdvaja $a_i$ i $b_i$. Odaberi podskup $S$ putova tako da je svaki brid pokriven najviše jednim putem iz $S$ i $\sum_{i \in S} w_i$ bude najveći.</p>
<h3>Ulaz</h3>
<p>$2 \le n \le 10^5$, $0 \le m \le 5 \cdot 10^5$, $1 \le k \le 12$; $n - 1$ bridova; $m$ redaka $a_i\ b_i\ w_i$ ($a_i \ne b_i$, $0 \le w_i \le 10^9$).</p>
<h3>Izlaz</h3>
<p>Najveći zbroj.</p>
<h3>Primjer</h3>
<p>$n = 5$, bridovi $1\text{-}2, 1\text{-}3, 2\text{-}4, 2\text{-}5$; putovi $(3,2,8), (5,4,10), (3,1,2), (1,2,7), (2,1,2), (1,2,1), (5,2,3)$: $19$.</p>
''',
    'hints': [
        r'''
<p>Korijeni stablo i putove grupiraj po LCA-u. Put s LCA-om $v$ zauzima jedan ili dva brida od $v$ prema djeci; kako putovi s istim LCA-om ne smiju dijeliti bridove, u $v$ se bira <em>uparivanje</em> djece – stupanj je $\le 12$, pa se to može DP-om po podskupovima.</p>
''',
        r'''
<p>Definiraj $F[v]$ = najbolji zbroj putova čiji je LCA u podstablu $v$. Put s LCA-om $v$ i krajem $a$ zauzima cijeli lanac $v \to a$: u svakom vrhu $x$ lanca je zabranjen jedan brid prema djetetu. Cijena „rezervacije” u $x$ je $e_x(c) = \max_{\text{maska} \not\ni c} dp[x][\text{maska}] - F[c]$, neovisna o putu – može se prefiksno zbrajati po dubini.</p>
''',
        r'''
<p>Obradi vrhove od listova prema korijenu; kad je $F[x]$ gotov, dodaj $e_x(c)$ na cijelo podstablo djeteta $c$ (Fenwick nad Eulerovim poretkom). Vrijednost puta $(a,b,w)$ s LCA-om $v$ tada je $w + F[a] + \text{fen}(a) + F[b] + \text{fen}(b)$.</p>
''',
    ],
    'coach': [
        (r'Zašto grupiranje po LCA-u i što se točno odlučuje u vrhu $v$?',
         r'''
<p>Bridovi koje put pokriva su bridovi na putu $a \to b$; taj put ima najviši vrh $\mathrm{LCA}(a,b) = v$ i silazi u najviše dvoje djece od $v$. Različiti putovi s LCA-om $v$ ne smiju dijeliti brid, posebno ne brid $(v, \text{dijete})$; dakle skup odabranih putova s LCA-om $v$ određuje <em>disjunktne</em> podskupove djece veličine 1 ili 2 – uparivanje na $\le 12$ djece. Za svaku masku $M$ djece neka je $P[M]$ najbolji jedan put s LCA-om $v$ koji koristi točno bridove prema djeci iz $M$; $g[M]$ = najbolji zbroj putova koji točno pokrivaju $M$ (DP po podskupovima: uzmi najniži bit $i \in M$ i uparuj ga sam ili s nekim $j$).</p>
'''),
        (r'Put s LCA-om $v$ silazi do $a$. Što to znači za vrhove između $v$ i $a$, i kako izbjeći $O(\text{dubina})$ po putu?',
         r'''
<p>Za svaki vrh $x$ na lancu strogo ispod $v$ i iznad $a$, brid $(x, x')$ prema sljedećem vrhu lanca je zauzet, pa putovi s LCA-om $x$ ne smiju koristiti to dijete: vrijednost podstabla $x$ je tada $\max_{M \not\ni x'} dp[x][M]$ umjesto $F[x]$, gdje $dp[x][M] = g[M] + \sum_{c \notin M} F[c]$. Ključ: ta vrijednost <strong>ne ovisi o putu</strong>, samo o paru $(x, x')$. Definiramo $e_{x'} = \max_{M \not\ni x'} dp[x][M] - F[x']$ – „koliko podstablo $x$ vrijedi bez doprinosa $F[x']$, uz zabranjen brid $(x,x')$”. Vrijednost lanca do $a$ je onda $F[a] + \sum_{x' \text{ na lancu ispod } v} e_{x'}$, jer teleskopski $F[a]$ ulazi u $e$ svog roditelja, itd.</p>
'''),
        (r'Kako zbroj $e$ duž lanca dobiti u $O(\log n)$?',
         r'''
<p>Obrađujemo vrhove od listova prema korijenu (obrnuti preorder). Kad je $F[x]$ izračunat, za svako dijete $c$ dodamo $e_c$ na cijelo podstablo od $c$ (interval $[\mathrm{tin}_c, \mathrm{tout}_c]$, Fenwick s dodavanjem na interval i upitom u točki). Kad kasnije obrađujemo $v$, <code>fen(a)</code> je zbroj $e$ po svim precima od $a$ koji su <em>već obrađeni</em> – to su točno vrhovi lanca ispod $v$ (preci iznad $v$ još nisu obrađeni, drugi vrhovi ne pokrivaju $\mathrm{tin}_a$).</p>
'''),
        (r'Koja je ukupna složenost i zašto stane u limit?',
         r'''
<p>Za vrh s $d$ djece: $P$ iz putova ($O(1)$ po putu, uz $O(\log n)$ za LCA i skok do djeteta), $g$ u $O(2^d d)$, $dp$ i najbolje po isključenom djetetu u $O(2^d d)$. Broj vrhova s $d$ djece je $\le 2n/(d+1)$, pa je $\sum 2^{d} d \le n \cdot 2^{11}$ za $k = 12$ (ne-korijen ima $\le 11$ djece) – oko $2\cdot10^8$ jednostavnih operacija; s $m \le 5\cdot10^5$ putova i $O(m\log n)$ za LCA sve zajedno ispod $0.5$ s.</p>
'''),
    ],
    'tips': [
        r'''Zadaci s putovima koji se ne smiju preklapati na stablu: grupiraj po LCA-u, u LCA-u odluči koje bridove prema djeci putovi zauzimaju; mali stupanj $\Rightarrow$ DP po maskama djece (uparivanje).''',
        r'''Kad odabir u pretku „rezervira” nešto u potomcima, izrazi cijenu rezervacije kao razliku (vrijednost s ograničenjem $-$ vrijednost bez), pa je zbroj cijena duž lanca teleskopski i može se držati prefiksno (Fenwick nad Eulerovim poretkom).''',
        r'''Obrada u obrnutom preorderu daje „djeca prije roditelja” bez rekurzije; Fenwick tada automatski sadrži samo doprinose već obrađenih (dubljih) vrhova.''',
        r'''$-\infty$ predstavi kao <code>LLONG_MIN/4</code> i provjeravaj ga prije zbrajanja – zbrojevi težina do $5\cdot10^{14}$ stanu u <code>long long</code>.''',
    ],
    'solution': r'''
<p>Vlastita izvedba (organizatori nisu objavili rješenja), potvrđena brute forceom po podskupovima putova. Korijenimo stablo i grupiramo putove po LCA-u. $F[v]$ = najbolji zbroj putova s LCA-om u podstablu $v$. Put s LCA-om $v$ zauzima 1–2 brida prema djeci i cijele lance do krajeva; za vrh $x$ lanca s rezerviranim bridom prema djetetu $x'$ vrijednost podstabla je $\max_{M \not\ni x'} dp[x][M]$, gdje je $dp[x][M] = g[M] + \sum_{c \notin M} F[c]$ i $g$ je DP po podskupovima djece (uparivanje djece putovima, $O(2^d d)$, $d \le 11$). Cijena rezervacije $e_{x'} = \max_{M\not\ni x'} dp[x][M] - F[x']$ ne ovisi o putu, pa ju nakon obrade $x$ dodamo na podstablo od $x'$ (Fenwick nad Eulerovim poretkom); vrijednost puta $(a,b,w)$ s LCA-om $v$ je $w + F[a] + \text{fen}(a) + F[b] + \text{fen}(b)$ (član za kraj jednak $v$ izostaje). Vrhove obrađujemo od listova prema korijenu; odgovor je $F[\text{korijen}]$. Složenost $O(\sum_v 2^{d_v} d_v + m\log n)$.</p>
''',
    'detailed': r'''
<h3>1. Postavka</h3>
<p>Korijenimo stablo u $1$. Put $(a, b)$ pokriva bridove na jedinstvenom putu $a \to b$, čiji je najviši vrh $v = \mathrm{LCA}(a,b)$; put silazi u $v$ u najviše dvoje djece ($s_a$ = dijete od $v$ prema $a$ ako $a \ne v$, $s_b$ analogno). Uvjet „svaki brid pokriven najviše jednom” treba vrijediti za sve bridove, ne samo one uz LCA.</p>
<h3>2. Stanja</h3>
<p>Za vrh $v$ s djecom $c_0, \dots, c_{d-1}$ ($d \le 11$ za $v \ne 1$, jer je $\deg \le k \le 12$ i jedan brid vodi roditelju; $d \le 12$ za korijen) definiramo:</p>
<ul>
<li>$F[v]$ – najveći zbroj odabranih putova s LCA-om u podstablu $v$ (oni koriste samo bridove unutar podstabla), bez vanjskih ograničenja;</li>
<li>$dp[v][M]$ za masku djece $M$ – isto, ali uz zahtjev da odabrani putovi s LCA-om $v$ koriste <em>točno</em> bridove $(v, c_i)$, $i \in M$;</li>
<li>$e_{c}$ za dijete $c$ od $v$ – cijena rezervacije brida $(v,c)$: $e_c = \max_{M \not\ni c} dp[v][M] - F[c]$.</li>
</ul>
<p>Očito $F[v] = \max_M dp[v][M]$.</p>
<h3>3. Vrijednost jednog puta s LCA-om $v$</h3>
<p><strong>Lema 1.</strong> Ako je put $(a, b, w)$ s LCA-om $v$ odabran, najbolji ukupni zbroj putova s LCA-om <em>strogo unutar</em> podstabla djeteta $s_a$ (uz uvjet da nijedan ne pokriva brid lanca $v \to a$) iznosi $F[a] + \sum_{x'} e_{x'}$, gdje $x'$ prolazi vrhove lanca strogo ispod $v$ do $a$ uključivo (svaki $x'$ s roditeljem $x$ na lancu).</p>
<p><em>Dokaz.</em> Neka su vrhovi lanca $v = x_0, x_1, \dots, x_t = a$. Podstabla vrhova $x_i$ dijele se na podstablo $x_{i+1}$ i ostatak. Putovi s LCA-om $x_i$ ($1 \le i \lt t$) ne smiju koristiti brid $(x_i, x_{i+1})$, a ostala podstabla djece $c \ne x_{i+1}$ su slobodna (vrijednost $F[c]$, jer njihovi putovi ne dodiruju lanac): najbolje je $\max_{M \not\ni x_{i+1}} dp[x_i][M]$, u čemu je uključen $F[x_{i+1}]$ kao slobodan – no podstablo $x_{i+1}$ nije slobodno. Zato definiramo $V(x_i)$ = optimum podstabla $x_i$ uz lanac; $V(a) = F[a]$ (ispod $a$ nema ograničenja) i $V(x_i) = \big(\max_{M \not\ni x_{i+1}} dp[x_i][M] - F[x_{i+1}]\big) + V(x_{i+1}) = e_{x_{i+1}} + V(x_{i+1})$: izbor u $x_i$ i izbor u podstablu $x_{i+1}$ su neovisni jer se tiču disjunktnih skupova bridova, pa je optimum zbroj. Teleskopski $V(x_1) = F[a] + \sum_{i=1}^{t} e_{x_i}$. $\square$</p>
<p>Vrijednost puta: $P(a,b,w) = w + [a \ne v]\,V_a + [b \ne v]\,V_b$ i $P[M]$ = maksimum po putovima s LCA-om $v$ i maskom $M = \{s_a, s_b\}$ (jedan ili dva bita).</p>
<h3>4. DP po podskupovima u $v$</h3>
<p>$g[M]$ = najbolji zbroj vrijednosti $P$ disjunktnih putova čije maske točno pokrivaju $M$: $g[\emptyset] = 0$; za $M \ne \emptyset$ s najnižim bitom $i$: $g[M] = \max\big(g[M \setminus i] + P[\{i\}],\ \max_{j \in M \setminus i} g[M \setminus \{i,j\}] + P[\{i,j\}]\big)$ (bit $i$ mora biti pokriven nekim putem – samo njim ili u paru). Zatim $dp[v][M] = g[M] + \sum_{c \notin M} F[c]$ (djeca izvan $M$ su slobodna), $F[v] = \max_M dp[v][M]$ i $e_{c_i} = \max_{M \not\ni i} dp[v][M] - F[c_i]$. Sve u $O(2^d d)$.</p>
<h3>5. Zbroj $e$ duž lanca u $O(\log n)$</h3>
<p>Vrhove obrađujemo u obrnutom preorderu (djeca prije roditelja). Nakon obrade $v$ dodamo $e_c$ na interval $[\mathrm{tin}_c, \mathrm{tout}_c]$ za svako dijete $c$ (Fenwick s dodavanjem na interval, upit u točki). Pri obradi $v$ vrijednost <code>fen(tin_a)</code> je zbroj $e_{x'}$ po svim već obrađenim vrhovima $x'$ koji su preci od $a$ (uključivo $a$). Preci iznad $v$ (i $v$ sam, čije $e$ još nije dodano) nisu obrađeni, a $e$ vrhova koji nisu preci od $a$ ne pokrivaju $\mathrm{tin}_a$. Dakle <code>fen(tin_a)</code> $= \sum_{i=1}^{t} e_{x_i}$ – točno zbroj iz Leme 1. Zato je $V_a = F[a] + \text{fen}(\mathrm{tin}_a)$.</p>
<h3>6. Ispravnost odgovora</h3>
<p>$F[1]$ je optimum s LCA-om u cijelom stablu – svi putovi. Indukcijom po podstablima: svaki dopustiv izbor putova u podstablu $v$ razlaže se na putove s LCA-om $v$ (disjunktne maske, dakle jedan sažetak $g$), lance (Lema 1) i slobodna podstabla ($F$); obratno, svaka kombinacija u DP-u je dopustiva jer su skupovi bridova disjunktni.</p>
<h3>7. Složenost i zamke</h3>
<ul>
<li>$O(\sum_v 2^{d_v} d_v)$: vrhova s $d$ djece je $\le n/d$, pa je zbroj $\le n \cdot 2^{11} \approx 2\cdot10^8$; LCA binarnim dizanjem $O(m\log n)$. Izmjereno $\lt 0.5$ s.</li>
<li>Skok „dijete od $v$ prema $a$” je predak od $a$ na dubini $\mathrm{dep}_v + 1$ (binarno dizanje).</li>
<li>$m = 0$: odgovor $0$ ($g[\emptyset] = 0$, sve $F = 0$).</li>
<li>Putovi s $a = v$ ili $b = v$ imaju masku od jednog bita; $a \ne b$ jamči neprazan skup bridova.</li>
<li>Rekurziju izbjegavamo (dubina do $10^5$): iterativni DFS za preorder/roditelje.</li>
</ul>
''',
    'verified': r'''uzorci 1/1, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 0.42 s).''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Teleport', 'title_hr': 'Teleport', 'slug': 'G_teleport',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Mreža $n \times n$ točaka $(x, y)$, $1 \le x, y \le n$; neke su neprohodne (<code>*</code>), ostale prohodne (<code>.</code>). Iz $(x, y)$ se u jednoj sekundi može teleportirati u $(x \pm 1, y)$, $(x, y \pm 1)$ ili $f_i(x, y)$ za bilo koji $0 \le i \le k$, gdje je $f_0(x, y) = (x, y)$ i $f_i(x, y) = f_{i-1}(y + 1, x)$. Cilj izvan mreže ili neprohodan nije dopušten.</p>
<p>Nađi najkraće vrijeme od $(1,1)$ do $(n,n)$ ili $-1$.</p>
<h3>Ulaz</h3>
<p>$1 \le n, k \le 5000$; $n$ redaka po $n$ znakova; $(1,1)$ i $(n,n)$ su prohodne.</p>
<h3>Izlaz</h3>
<p>Jedan broj.</p>
<h3>Primjer</h3>
<p>Mreža <code>.*.</code>/<code>.*.</code>/<code>...</code>: za $k = 2$ odgovor je $3$, za $k = 3$ odgovor je $2$.</p>
''',
    'hints': [
        r'''
<p>Raspiši $f_1, f_2, f_3, f_4$ iz definicije $f_i(x, y) = f_{i-1}(y + 1, x)$. Uočavaš li dvije dijagonale?</p>
''',
        r'''
<p>$f_{2j}(x, y) = (x + j, y + j)$ i $f_{2j+1}(x, y) = (y + j + 1, x + j)$: ciljevi teleporta su prefiksi dviju dijagonala – one kroz $(x, y)$ i one kroz $(y+1, x)$. BFS s $O(k)$ prijelaza po ćeliji bio bi $O(n^2 k)$ – prespor.</p>
''',
        r'''
<p>U BFS-u svaku ćeliju treba posjetiti samo prvi put. Po svakoj dijagonali drži strukturu „sljedeća neposjećena ćelija” (union-find s kompresijom putova) i preskači posjećene – ukupno $O(n^2 \alpha(n^2))$.</p>
''',
    ],
    'coach': [
        (r'Kamo vodi $f_i$? Kako iz rekurzije $f_i(x,y) = f_{i-1}(y+1, x)$ dobiti zatvorenu formulu?',
         r'''
<p>$f_1(x,y) = (y+1, x)$; $f_2(x,y) = f_1(y+1, x) = (x+1, y+1)$; $f_3(x,y) = f_2(y+1, x) = (y+2, x+1)$. Indukcijom: ako je $f_{2j}(x,y) = (x+j, y+j)$, onda je $f_{2j+1}(x,y) = f_{2j}(y+1, x) = (y+1+j, x+j)$ i $f_{2j+2}(x,y) = f_{2j+1}(y+1, x) = (x+1+j, y+1+j)$. Parni indeksi klize po glavnoj dijagonali kroz $(x,y)$ za $j = 1, \dots, \lfloor k/2 \rfloor$; neparni po dijagonali kroz $(y+1, x)$ za $j = 0, \dots, \lfloor (k-1)/2 \rfloor$. Sve su to ćelije na dvije dijagonale smjera $(+1, +1)$, i to <em>uzastopne</em>.</p>
'''),
        (r'Zašto obični BFS s popisom svih $k+1$ teleporta nije dovoljan?',
         r'''
<p>Za $n = k = 5000$ ima $2.5 \cdot 10^7$ ćelija i po $5000$ prijelaza – $10^{11}$ operacija. No BFS nikad ne treba dvaput obraditi istu ćeliju: kad iz $(x,y)$ „pometemo” odsječak dijagonale, zanimaju nas samo <strong>još neposjećene</strong> ćelije u njemu; posjećene (i neprohodne) treba preskočiti u $O(1)$ amortizirano.</p>
'''),
        (r'Kako preskakati posjećene ćelije na dijagonali?',
         r'''
<p>Svaku dijagonalu $d = x - y + n - 1$ linearno indeksiramo i držimo niz <code>nxt[p]</code> s union-find semantikom: <code>find(p)</code> vraća prvu neposjećenu poziciju $\ge p$ (na kraju svake dijagonale stoji stražar). Kad ćelija postane posjećena (ili je neprohodna od početka), postavimo <code>nxt[p] = p + 1</code>. Pometanje odsječka $[t_1, t_2]$: $p = \text{find}(t_1)$; dok je $p \le t_2$ posjeti ćeliju, stavi u red i skoči na $\text{find}(p+1)$. Svaka ćelija ulazi u red najviše jednom, a s kompresijom putova ukupni je trošak $O(n^2 \alpha)$.</p>
'''),
        (r'Što još treba paziti da BFS bude ispravan i dovoljno brz?',
         r'''
<p>Četiri susjeda obrađujemo obično (provjera granica i polja <code>vis</code>). Odsječke dijagonala stegnemo na dio unutar mreže; za neparne teleporte ishodište je $(y+1, x)$ pa zahtijeva $y + 1 \le n$. Neprohodne ćelije i početnu ćeliju označimo posjećenima prije BFS-a. Red je jedan niz od $n^2$ <code>int</code>-ova, <code>vis</code> je $n^2$ bajtova, <code>nxt</code> ima $n^2 + 2n$ zapisa – ukupno oko $225$ MB za $n = 5000$, unutar $1024$ MiB.</p>
'''),
    ],
    'tips': [
        r'''Rekurzivno zadane funkcije oblika $f_i = f_{i-1} \circ g$ raspiši za nekoliko $i$ i traži period: zamjena koordinata s pomakom ima period $2$, pa $f_{2j}$ i $f_{2j+1}$ imaju zatvorene formule.''',
        r'''<strong>BFS s intervalnim prijelazima:</strong> kad iz stanja vodi prijelaz u cijeli interval stanja, koristi „sljedeći neposjećeni” (DSU/pokazivače) po tom intervalu – svako stanje se otvara jednom, pa je ukupno $O(\text{stanja} \cdot \alpha)$.''',
        r'''Za $n^2 = 2.5 \cdot 10^7$ ćelija koristi plošne nizove (<code>vector&lt;char&gt;</code>, <code>vector&lt;int&gt;</code>) s ručno izračunatim indeksom, ne <code>vector&lt;vector&lt;…&gt;&gt;</code> ili <code>std::queue</code> parova.''',
    ],
    'solution': r'''
<p>Vlastita izvedba, potvrđena brute forceom koji doslovno iterira definiciju $f_i$. Iz $f_i(x,y) = f_{i-1}(y+1, x)$ indukcijom slijedi $f_{2j}(x,y) = (x+j, y+j)$ i $f_{2j+1}(x,y) = (y+j+1, x+j)$, pa su ciljevi teleporta iz $(x,y)$ uzastopne ćelije dviju dijagonala smjera $(+1,+1)$: one kroz $(x,y)$ (pomaci $1..\lfloor k/2 \rfloor$) i one kroz $(y+1, x)$ (pomaci $0..\lfloor (k-1)/2 \rfloor$). Radimo BFS po vremenu; da ne obilazimo $O(k)$ ciljeva po ćeliji, po svakoj dijagonali držimo union-find „sljedeća neposjećena ćelija” i pri pometanju odsječka skačemo samo po neposjećenim ćelijama (posjećene i neprohodne su preskočene). Svaka ćelija uđe u red jednom: $O(n^2 \alpha(n^2))$ vremena i $O(n^2)$ memorije.</p>
''',
    'detailed': r'''
<h3>1. Zatvorena formula za $f_i$</h3>
<p><strong>Lema.</strong> Za $j \ge 0$: $f_{2j}(x, y) = (x + j, y + j)$ i $f_{2j+1}(x, y) = (y + j + 1, x + j)$. <em>Dokaz</em> indukcijom po $i$. $f_0 = \mathrm{id}$. Ako je $f_{2j}(x,y) = (x+j, y+j)$, onda je $f_{2j+1}(x, y) = f_{2j}(y+1, x) = (y + 1 + j, x + j)$ i $f_{2j+2}(x, y) = f_{2j+1}(y+1, x) = (x + j + 1, y + 1 + j)$. $\square$</p>
<p>Dakle iz $(x, y)$ u jednoj sekundi možemo u: četiri susjeda; $(x+j, y+j)$ za $1 \le j \le \lfloor k/2 \rfloor$ – prefiks <em>glavne</em> dijagonale kroz $(x,y)$; $(y+1+j, x+j)$ za $0 \le j \le \lfloor (k-1)/2 \rfloor$ – prefiks dijagonale kroz <em>zrcalnu</em> točku $(y+1, x)$. Obje su dijagonale smjera $(+1, +1)$, pa je svaka dijagonala $d = x - y + n - 1 \in [0, 2n-2]$ jedan niz ćelija poredanih po $\min(x, y)$. Ciljevi su uzastopni odsječci takvih nizova; cilj izvan mreže ili neprohodan se odbacuje (odsječak stegnemo na mrežu, a neprohodne ćelije preskačemo isto kao posjećene).</p>
<h3>2. BFS i problem $O(n^2 k)$</h3>
<p>Sve operacije traju $1$ s, pa najkraće vrijeme daje BFS od $(1,1)$ do $(n,n)$. Naivno bismo za svaku ćeliju prošli $O(k)$ teleporta: $O(n^2 k) \approx 10^{11}$. Ključno opažanje: BFS ćeliju obrađuje samo kad je <em>prvi put</em> dosegne; pri pometanju odsječka dijagonale sve već posjećene ćelije su beskorisne. Trebamo dakle brzo naći „sljedeću neposjećenu ćeliju na dijagonali od pozicije $p$”.</p>
<h3>3. Union-find „sljedeća neposjećena”</h3>
<p>Sve dijagonale spojimo u jedan niz pozicija (dijagonala $d$ počinje na <code>base[d]</code>, iza njezinih $\ell_d = n - |d - (n-1)|$ ćelija stoji stražar). Niz <code>nxt[p]</code> inicijalno je <code>nxt[p] = p</code> (neposjećeno). Kad ćelija na poziciji $p$ postane posjećena – ili je neprohodna od početka – postavimo <code>nxt[p] = p + 1</code>. Funkcija <code>find(p)</code> slijedi pokazivače do prve pozicije $r$ s <code>nxt[r] = r</code> i putem sažima staze; stražar je uvijek „neposjećen”, pa se pretraga zaustavlja unutar dijagonale.</p>
<p>Pometanje odsječka $[t_1, t_2]$ dijagonale $d$: $p = \text{find}(\text{base}[d] + t_1)$; dok je $p \le \text{base}[d] + t_2$: ćeliju označi posjećenom (<code>vis</code> i <code>nxt[p] = p+1</code>), stavi u red, $p = \text{find}(p + 1)$. Svaki uspješan korak petlje posjećuje novu ćeliju, pa je ukupan broj koraka $\le n^2$; svaki <code>find</code> je amortizirano $O(\alpha(n^2))$ uz kompresiju putova (spajamo uvijek s desnim susjedom, pa struktura ostaje linearna – to je klasična „pointer-jumping” varijanta DSU-a). Ukupno $O(n^2 \alpha(n^2))$.</p>
<h3>4. Tijek algoritma</h3>
<ol>
<li>Učitaj mrežu u <code>vis</code> (neprohodno $=$ posjećeno); za neprohodne postavi i <code>nxt</code>.</li>
<li>Posjeti $(1,1)$, stavi u red. Obrada po slojevima (razina $=$ vrijeme).</li>
<li>Za ćeliju $(x,y)$: četiri susjeda uz provjeru <code>vis</code>; ako je $k \ge 2$, pometi glavnu dijagonalu na pomacima $[t+1, t+\lfloor k/2 \rfloor]$ gdje je $t = \min(x,y) - 1$; ako je $k \ge 1$ i $y + 1 \le n$, pometi dijagonalu kroz $(y+1, x)$ na pomacima $[t', t' + \lfloor (k-1)/2 \rfloor]$, $t' = \min(y+1, x) - 1$.</li>
<li>Kad izvadimo $(n,n)$, ispiši razinu; ako se red isprazni, $-1$.</li>
</ol>
<p>Primjeri: u mreži $3 \times 3$ s neprohodnim srednjim stupcem u prva dva retka i $k = 2$ optimalno je $(1,1) \xrightarrow{f_1} (2,1) \xrightarrow{f_2} (3,2) \to (3,3)$, ukupno $3$; za $k = 3$ je $(1,1) \xrightarrow{f_3} (3,2) \to (3,3)$, ukupno $2$ – oba u skladu s izlazima primjera.</p>
<h3>5. Složenost, memorija i zamke</h3>
<ul>
<li>Vrijeme $O(n^2 \alpha)$; za $n = 5000$ mjerenja na najgorim generiranim testovima (prazna mreža, veliki $k$) daju ispod $1$ s.</li>
<li>Memorija: <code>vis</code> $n^2$ bajtova ($25$ MB), <code>nxt</code> $\approx n^2$ <code>int</code>-ova ($100$ MB), red $n^2$ <code>int</code>-ova ($100$ MB) – oko $225$ MB, ispod $1024$ MiB. Za red koristimo jedan <code>vector&lt;int&gt;</code> s indeksom glave, ne <code>std::queue</code>.</li>
<li>Ne zaboravi $k = 0$ (nema teleporta) i $k = 1$ (samo $f_1(x,y) = (y+1, x)$, pomak $j = 0$).</li>
<li>Neprohodne ćelije moraju biti u <code>nxt</code> označene kao posjećene, inače bi pometanje stalo na njima.</li>
</ul>
''',
    'verified': r'''uzorci 2/2, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 0.70 s).''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Function', 'title_hr': 'Funkcija', 'slug': 'H_function',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Funkcija $f$ zadana je s $f(x) = 0$ za $x \gt n$ i $f(x) = 1 + \sum_{k=2}^{20210926} f(kx)$ inače. Izračunaj $f(1) \bmod 998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$1 \le n \le 10^9$.</p>
<h3>Izlaz</h3>
<p>Jedan broj.</p>
<h3>Primjer</h3>
<p>$n = 1 \to 1$; $n = 2 \to 2$; $n = 100 \to 949$.</p>
''',
    'hints': [
        r'''
<p>$f(x)$ ovisi o $x$ samo preko toga koliko višekratnika $kx$ stane u $n$. Pokušaj $f(x)$ izraziti kao funkciju od $m = \lfloor n / x \rfloor$.</p>
''',
        r'''
<p>Vrijedi $\lfloor \lfloor n/x \rfloor / k \rfloor = \lfloor n/(kx) \rfloor$, pa je $g(m) = 1 + \sum_{k=2}^{\min(m, A)} g(\lfloor m/k \rfloor)$ s $g(0) = 0$ i $A = 20210926$. Koliko različitih argumenata $g$ uopće treba?</p>
''',
        r'''
<p>Svi potrebni argumenti su oblika $\lfloor n/d \rfloor$ – ima ih $O(\sqrt n)$. Sumu po $k$ računaj po blokovima jednakih kvocijenata $\lfloor m/k \rfloor$; ukupno $O(n^{3/4})$.</p>
''',
    ],
    'coach': [
        (r'Definicija je $f(x) = 1 + \sum_{k=2}^{A} f(kx)$ uz $f(x) = 0$ za $x \gt n$. O čemu $f(x)$ zapravo ovisi?',
         r'''
<p>Član $f(kx)$ je nenul samo za $kx \le n$, tj. $k \le \lfloor n/x \rfloor =: m$. Nadalje, $f(kx)$ na isti način ovisi o $\lfloor n/(kx) \rfloor = \lfloor m/k \rfloor$ (standardni identitet za ugniježđena cjelobrojna dijeljenja). Dakle $f(x) = g(\lfloor n/x \rfloor)$ gdje je $g(0) = 0$ i $g(m) = 1 + \sum_{k=2}^{\min(m, A)} g(\lfloor m/k \rfloor)$; traži se $g(n)$.</p>
'''),
        (r'Koliko različitih vrijednosti $g$ se pojavljuje u rekurziji i zašto?',
         r'''
<p>Krenemo od $m = n$; djeca su $\lfloor n/k \rfloor$, a njihova djeca $\lfloor \lfloor n/k \rfloor / k' \rfloor = \lfloor n/(kk') \rfloor$ – opet oblik $\lfloor n/d \rfloor$. Skup $\{\lfloor n/d \rfloor : d \ge 1\}$ ima najviše $2\sqrt n$ elemenata: za $d \le \sqrt n$ ima ih $\sqrt n$, a za $d \gt \sqrt n$ kvocijent je $\lt \sqrt n$. Memoiziramo ih u dva niza: po vrijednosti $m$ kad je $m \le \sqrt n$, inače po $d = \lfloor n/m \rfloor$ (tada je $m = \lfloor n/d \rfloor$).</p>
'''),
        (r'Kako izračunati $\sum_{k=2}^{\min(m,A)} g(\lfloor m/k \rfloor)$ brže nego u $O(m)$?',
         r'''
<p>Kvocijent $q = \lfloor m/k \rfloor$ konstantan je za $k \in [k, \lfloor m/q \rfloor]$, pa sumu računamo po blokovima: $(k_2 - k + 1) \cdot g(q)$, gdje je $k_2 = \min(\lfloor m/q \rfloor, \min(m, A))$. Blokova je $O(\sqrt m)$. Gornja granica $A = 20210926$ bitna je samo za $m \gt A$, tj. za $m = \lfloor n/d \rfloor$ s $d \le 49$.</p>
'''),
        (r'Kolika je ukupna složenost?',
         r'''
<p>Za argumente $m \le \sqrt n$ trošimo $\sum_{m \le \sqrt n} \sqrt m = O(n^{3/4})$; za $m = \lfloor n/d \rfloor \gt \sqrt n$ trošimo $\sum_{d \le \sqrt n} \sqrt{n/d} = O(n^{3/4})$. Za $n = 10^9$ to je reda $10^7$ operacija, a rekurzija je duboka najviše $O(\log n)$.</p>
'''),
    ],
    'tips': [
        r'''Kad se funkcija poziva na $\lfloor n/x \rfloor$, $\lfloor n/(kx) \rfloor, \dots$, gotovo uvijek pomaže identitet $\lfloor \lfloor n/a \rfloor / b \rfloor = \lfloor n/(ab) \rfloor$: sve vrijednosti žive u skupu $\{\lfloor n/d \rfloor\}$ veličine $O(\sqrt n)$.''',
        r'''Memoizacija „po $\lfloor n/d \rfloor$” u dva niza (mali argumenti izravno, veliki preko $d$) izbjegava <code>unordered_map</code> i njegove konstante.''',
        r'''Blokovi jednakih kvocijenata: za $k$ postavi $k_2 = \lfloor m / \lfloor m/k \rfloor \rfloor$ i preskoči na $k_2 + 1$; množitelj $(k_2 - k + 1)$ reduciraj modulo $p$ prije množenja.''',
    ],
    'solution': r'''
<p>Vlastita izvedba, potvrđena brute forceom po definiciji. Član $f(kx)$ je nenul samo za $k \le \lfloor n/x \rfloor$, a zbog $\lfloor \lfloor n/x \rfloor / k \rfloor = \lfloor n/(kx) \rfloor$ vrijednost $f(x)$ ovisi samo o $m = \lfloor n/x \rfloor$: $f(x) = g(m)$, gdje je $g(0) = 0$ i $g(m) = 1 + \sum_{k=2}^{\min(m, A)} g(\lfloor m/k \rfloor)$, $A = 20210926$. Traženi $f(1) = g(n)$. Svi argumenti koji se pojave su oblika $\lfloor n/d \rfloor$, pa ih je $O(\sqrt n)$; memoiziramo ih (mali po vrijednosti, veliki po $d$) i svaku sumu računamo po blokovima jednakih kvocijenata u $O(\sqrt m)$. Ukupno $O(n^{3/4})$, modulo $998244353$.</p>
''',
    'detailed': r'''
<h3>1. Redukcija na jednu varijablu</h3>
<p>Definicija glasi $f(x) = 1 + \sum_{k=2}^{A} f(kx)$ za $x \le n$ i $f(x) = 0$ za $x \gt n$, $A = 20210926$. Član $f(kx)$ je različit od nule samo kad je $kx \le n$, tj. $k \le \lfloor n/x \rfloor$. Uvedimo $m(x) = \lfloor n/x \rfloor$. Tvrdimo da $f(x)$ ovisi samo o $m(x)$.</p>
<p><strong>Lema.</strong> Za prirodne $n, a, b$ vrijedi $\lfloor \lfloor n/a \rfloor / b \rfloor = \lfloor n/(ab) \rfloor$. <em>Dokaz.</em> Neka je $q = \lfloor n/(ab) \rfloor$, dakle $qab \le n \lt (q+1)ab$. Tada $qb \le n/a$, pa $qb \le \lfloor n/a \rfloor$, dakle $\lfloor \lfloor n/a \rfloor / b \rfloor \ge q$. S druge strane $\lfloor n/a \rfloor \le n/a \lt (q+1)b$, pa je $\lfloor n/a \rfloor / b \lt q + 1$. $\square$</p>
<p>Po lemi je $m(kx) = \lfloor m(x) / k \rfloor$. Indukcijom po $m$ (od manjih prema većima) slijedi da je $f(x) = g(m(x))$, gdje je</p>
<p>$$g(0) = 0, \qquad g(m) = 1 + \sum_{k=2}^{\min(m, A)} g\!\left(\lfloor m/k \rfloor\right) \quad (m \ge 1).$$</p>
<p>Gornja granica $\min(m, A)$: za $k \gt m$ je $\lfloor m/k \rfloor = 0$ i član otpada; za $k \gt A$ članova nema po definiciji. Traži se $f(1) = g(n)$. Provjera: $g(1) = 1$, $g(2) = 1 + g(1) = 2$ – primjeri $n = 1, 2$.</p>
<h3>2. Koje argumente $g$ treba</h3>
<p>Iz $m = n$ rekurzija ide u $\lfloor n/k \rfloor$, zatim u $\lfloor \lfloor n/k \rfloor / k' \rfloor = \lfloor n/(kk') \rfloor$ itd. – po lemi svi argumenti pripadaju skupu $Q = \{\lfloor n/d \rfloor : 1 \le d \le n\}$. Skup $Q$ ima najviše $2\sqrt n$ elemenata: za $d \le \sqrt n$ najviše $\sqrt n$ različitih vrijednosti, a za $d \gt \sqrt n$ je $\lfloor n/d \rfloor \lt \sqrt n$, pa opet najviše $\sqrt n$ vrijednosti.</p>
<p>Memoizacija u dva niza: ako je $m \le S = \lfloor \sqrt n \rfloor$, pamtimo $g$ pod indeksom $m$; inače pod indeksom $d = \lfloor n/m \rfloor$, jer za $m \in Q$, $m \gt S$, vrijedi $m = \lfloor n/d \rfloor$ (i takav $d$ je $\le n/(S+1) \lt \sqrt n + 1$). Time izbjegavamo hash-tablicu.</p>
<h3>3. Suma po blokovima jednakih kvocijenata</h3>
<p>Za fiksni $m$ kvocijent $q = \lfloor m/k \rfloor$ ostaje isti za sve $k$ iz intervala $[k, \lfloor m/q \rfloor]$. Zato sumu računamo skokovima: na položaju $k$ izračunamo $q$, postavimo $k_2 = \min(\lfloor m/q \rfloor, \min(m, A))$, dodamo $(k_2 - k + 1) \cdot g(q)$ i nastavimo od $k_2 + 1$. Broj blokova je $O(\sqrt m)$ (različitih kvocijenata $\lfloor m/k \rfloor$ ima najviše $2\sqrt m$). Ograničenje $A$ utječe samo kad je $m \gt A$, što se za $n \le 10^9$ događa za $m = \lfloor n/d \rfloor$, $d \le 49$.</p>
<h3>4. Složenost</h3>
<p>Za male argumente $m \le \sqrt n$: $\sum_{m \le \sqrt n} O(\sqrt m) = O(n^{3/4})$. Za velike $m = \lfloor n/d \rfloor$, $d \le \sqrt n$: $\sum_{d \le \sqrt n} O(\sqrt{n/d}) = O(\sqrt n \cdot n^{1/4}) = O(n^{3/4})$. Za $n = 10^9$ to je nekoliko puta $10^7$ jednostavnih operacija, daleko unutar 1 s. Dubina rekurzije je $O(\log n)$ jer se argument barem polovi. Memorija: dva niza duljine $O(\sqrt n)$.</p>
<h3>5. Zamke</h3>
<ul>
<li>Množitelj $k_2 - k + 1$ može biti do $\approx 2 \cdot 10^7$ – reduciraj ga modulo $p$ prije množenja s $g(q) \lt p$, da umnožak ostane u 64 bita.</li>
<li>$\lfloor \sqrt n \rfloor$ računaj cjelobrojno (korekcija nakon <code>sqrtl</code>), jer o $S$ ovisi u koji niz ide koji argument.</li>
<li>$g(0) = 0$ mora biti obrađen izričito ($f(x) = 0$ za $x \gt n$), inače bi „$1 +$” pokvario odgovor.</li>
</ul>
''',
    'verified': r'''uzorci 3/3, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 0.25 s).''',
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Digit', 'title_hr': 'Znamenka', 'slug': 'I_digit',
    'tl': '2.5 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dan je pozitivan $n$. U svakom koraku: uniformno slučajno odaberi znamenku $d$ dekadskog zapisa $n$ i postavi $n := n \cdot (d + 1)$. Izračunaj očekivani broj koraka dok $n$ ne prijeđe $N$, modulo $998\,244\,353$.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 200$ testova; $1 \le n \le N \le 10^{18}$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan broj; dokazivo odgovor uvijek postoji.</p>
<h3>Primjer</h3>
<p>$(1, 10) \to 3$; $(1, 100) \to 4$; $(1, 1000) \to 942786340$.</p>
''',
    'hints': [
        r'''
<p>Napiši očekivanje po prvom koraku: $E(n) = 1 + \frac{1}{k}\sum_{d} E(n(d+1))$, gdje $d$ prolazi po $k$ znamenki broja $n$ i $E(m) = 0$ za $m \gt N$. Što s znamenkom $0$?</p>
''',
        r'''
<p>Znamenka $0$ ostavlja $n$ nepromijenjen, pa se $E(n)$ pojavljuje na obje strane. Ako $n$ ima $k$ znamenki od kojih $z$ nula: $E(n) = \dfrac{k + \sum_{d \ne 0} E(n(d+1))}{k - z}$; nazivnik je $\ge 1$ jer vodeća znamenka nije nula.</p>
''',
        r'''
<p>Sva dostižna stanja su oblika $n \cdot 2^a 3^b 5^c 7^d \le N$ (množitelji $d + 1 \in \{2, \dots, 10\}$ su 7-glatki). Takvih brojeva do $10^{18}$ ima nekoliko desetaka tisuća – memoiziraj po $(a, b, c, d)$.</p>
''',
    ],
    'coach': [
        (r'Kako postaviti jednadžbu za očekivani broj poteza $E(n)$?',
         r'''
<p>Uvjetujemo po prvom potezu. Ako $n$ ima $k$ znamenki, svaka se bira s vjerojatnošću $1/k$ (znamenke se biraju po pozicijama, jednake znamenke se broje višestruko), pa je $E(n) = 1 + \frac{1}{k}\sum_{\text{pozicije}} E(n(d+1))$, uz $E(m) = 0$ za $m \gt N$ (proces je već završio). Za $n = 1$, $N = 10$: $E(1) = 1 + E(2)$, $E(2) = 1 + E(3)$, …, $E(9) = 1 + E(10)$, $E(10) = ?$ – tu ulazi znamenka $0$.</p>
'''),
        (r'Znamenka $0$ vraća isti $n$. Kako se riješiti $E(n)$ na desnoj strani?',
         r'''
<p>Ako je $z$ znamenki jednako $0$, jednadžba glasi $E(n) = 1 + \frac{z}{k}E(n) + \frac{1}{k}\sum_{d \ne 0} E(n(d+1))$. Prebacimo: $E(n)\,(1 - z/k) = 1 + \frac1k \sum_{d\ne0} E(n(d+1))$, tj. $E(n) = \dfrac{k + \sum_{d \ne 0} E(n(d+1))}{k - z}$. Nazivnik $k - z \ge 1$ jer vodeća znamenka nije $0$. Modulo $998244353$ dijeljenje je množenje inverzom od $k - z \le 19$. Provjera na primjeru $n = 1$, $N = 10$: $E(6) = (1 + E(42))/1 = 1$, $E(3) = 1 + E(12) = 1$, $E(2) = 1 + E(6) = 2$, $E(1) = 1 + E(2) = 3$, kako i piše u primjeru.</p>
'''),
        (r'Koliko stanja rekurzija posjećuje i kako ih memoizirati bez hash-tablice?',
         r'''
<p>Svaki potez množi $n$ s $d + 1 \in \{2, 3, 4, 5, 6, 7, 8, 9, 10\}$, a to su brojevi oblika $2^a 3^b 5^c 7^d$. Zato je svako stanje $n \cdot 2^a 3^b 5^c 7^d \le N \le 10^{18}$, s $a \le 59$, $b \le 37$, $c \le 25$, $d \le 21$. Različitih 7-glatkih brojeva do $10^{18}$ ima nekoliko desetaka tisuća, a stanje je jednoznačno određeno četvorkom $(a,b,c,d)$ – memoiziramo u 4D polju s „pečatom” broja testa (bez brisanja između $T \le 200$ testova).</p>
'''),
        (r'Kako ostati u 64 bita i koliko sve to traje?',
         r'''
<p>Prije množenja $n \cdot (d+1)$ provjeri $n \gt N / (d+1)$ – tada je umnožak $\gt N$ i $E = 0$, bez prelijevanja (<code>unsigned long long</code>). Po stanju radimo $O(19)$ operacija (znamenke i rekurzivni pozivi), pa je ukupno $O(T \cdot \#\text{stanja} \cdot 19)$, u praksi ispod $0.5$ s za $T = 200$ najgorih testova ($n = 1$, $N = 10^{18}$).</p>
'''),
    ],
    'tips': [
        r'''Očekivanja s „prijelazom u samog sebe” (znamenka $0$, promašaj, ponavljanje) rješavaj algebarski: $E = 1 + pE + \dots \Rightarrow E = \frac{1 + \dots}{1 - p}$; modulo prost broj to je množenje inverzom.''',
        r'''Kad su prijelazi množenja malim brojevima, prostor stanja su glatki brojevi – prebroji ih (ovdje 7-glatki do $10^{18}$) prije nego se uplašiš granice $10^{18}$; memoizacija po eksponentima je brža i sigurnija od <code>unordered_map</code>.''',
        r'''Za više testova s istim poljem memoizacije koristi „pečat” (broj testa) umjesto <code>memset</code>-a polja od milijuna zapisa po testu.''',
    ],
    'solution': r'''
<p>Vlastita izvedba, potvrđena brute forceom u točnoj aritmetici (razlomci). Neka $n$ ima $k$ znamenki od kojih $z$ nula. Uvjetovanjem po prvom potezu $E(n) = 1 + \frac{1}{k}\sum_{\text{znamenke } d} E(n(d+1))$, uz $E(m) = 0$ za $m \gt N$; znamenka $0$ vraća $n$, pa se rješavanjem po $E(n)$ dobiva $E(n) = \frac{k + \sum_{d \ne 0} E(n(d+1))}{k - z}$, gdje je $k - z \ge 1$ (vodeća znamenka). Svako dostižno stanje je $n \cdot 2^a 3^b 5^c 7^d \le N$ jer su množitelji $d+1 \le 10$ 7-glatki; takvih stanja ima nekoliko desetaka tisuća, pa ih memoiziramo u 4D polju po $(a,b,c,d)$ s pečatom testa. Dijeljenje je množenje inverzom modulo $998244353$; prelijevanje izbjegavamo provjerom $n \gt N/(d+1)$. Ukupno $O(T \cdot \#\text{stanja} \cdot 19)$.</p>
''',
    'detailed': r'''
<h3>1. Jednadžba očekivanja</h3>
<p>Neka $n \le N$ ima $k$ dekadskih znamenki, od kojih je $z$ jednako $0$. U jednom potezu biramo poziciju znamenke uniformno (vjerojatnost $1/k$ po poziciji; jednake znamenke doprinose više puta) i prelazimo u $n(d+1)$. Uvjetujemo po prvom potezu:</p>
<p>$$E(n) = 1 + \frac{1}{k}\sum_{\text{pozicije } d} E\big(n(d+1)\big), \qquad E(m) = 0 \text{ za } m \gt N.$$</p>
<p>Za $d = 0$ prijelaz vodi u $n \cdot 1 = n$, dakle $E(n)$ se pojavljuje i desno, $z$ puta. Prebacivanjem: $E(n)\left(1 - \frac{z}{k}\right) = 1 + \frac{1}{k}\sum_{d \ne 0} E(n(d+1))$, pa</p>
<p>$$E(n) = \frac{k + \sum_{d \ne 0} E\big(n(d+1)\big)}{k - z}.$$</p>
<p>Nazivnik je $\ge 1$ jer vodeća znamenka nije nula, pa je $E(n)$ dobro definiran (i to je razlog zašto „odgovor uvijek postoji”). Za $d \ne 0$ je $n(d+1) \ge 2n \gt n$, pa rekurzija strogo raste i završava kad prijeđe $N$ – rekurzija je dobro utemeljena.</p>
<p>Provjera na primjeru $n = 1$, $N = 10$: $E(6) = (1 + E(42))/1 = 1$; $E(3) = 1 + E(12) = 1$; $E(2) = 1 + E(6) = 2$; $E(1) = 1 + E(2) = 3$, u skladu s primjerom.</p>
<h3>2. Prostor stanja</h3>
<p>Množitelji su $d + 1 \in \{2, \dots, 10\}$, a svi su oblika $2^a 3^b 5^c 7^d$ ($2, 3, 2^2, 5, 2\cdot3, 7, 2^3, 3^2, 2\cdot5$). Dakle svako dostižno stanje je $n \cdot 2^a 3^b 5^c 7^d \le N$, i različita stanja imaju različite četvorke $(a, b, c, d)$ (jedinstvena faktorizacija). Granice: $2^a \le 10^{18} \Rightarrow a \le 59$, slično $b \le 37$, $c \le 25$, $d \le 21$. Broj 7-glatkih brojeva do $10^{18}$ je reda nekoliko desetaka tisuća, pa i broj stanja po testu. Memoiziramo u statičkom polju <code>memo[60][38][26][22]</code> uz polje pečata (indeks testa), čime izbjegavamo brisanje polja između $T \le 200$ testova.</p>
<h3>3. Algoritam</h3>
<ol>
<li>Predračunaj inverze brojeva $1..19$ modulo $p = 998244353$.</li>
<li>$E(n, a, b, c, d)$: ako je stanje memoizirano za tekući test, vrati ga. Prođi znamenke od $n$: broji $k$ i $z$; za znamenku $d \ne 0$, ako je $n \le \lfloor N/(d+1) \rfloor$, dodaj $E(n(d+1), \dots)$ s ažuriranim eksponentima, inače dodaj $0$.</li>
<li>Rezultat $(k + \text{suma}) \cdot \mathrm{inv}[k - z] \bmod p$, spremi i vrati.</li>
</ol>
<h3>4. Složenost i implementacijske zamke</h3>
<ul>
<li>Po stanju $O(\text{broj znamenki}) \le 19$ operacija; ukupno $O(T \cdot S \cdot 19)$ gdje je $S$ broj stanja – za $T = 200$ najgorih testova ($n = 1$, $N = 10^{18}$) izmjereno ispod $0.5$ s.</li>
<li>$n \le 10^{18}$ i $n(d+1) \le 10^{19}$ mogu prijeći <code>long long</code>; koristimo <code>unsigned long long</code> i provjeru $n \gt N/(d+1)$ <em>prije</em> množenja.</li>
<li>Znamenke se broje po pozicijama: broj $n = 100$ ima $k = 3$, $z = 2$, $E(100) = (3 + E(200))/1$.</li>
<li>Dubina rekurzije je $\le \log_2 (N/n) \le 60$.</li>
</ul>
''',
    'verified': r'''uzorci 1/1, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 0.40 s).''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Leaves', 'title_hr': 'Listovi', 'slug': 'J_leaves',
    'tl': '2 s', 'ml': '64 MiB',
    'statement': r'''
<p>Binarno stablo s $n$ vrhova (svaki unutarnji vrh ima točno dva djeteta), listovi imaju oznake $a_u$. Obilazak stabla (lijevo dijete pa desno) daje niz oznaka listova. Točno $m$ puta: odaberi unutarnji vrh i zamijeni mu lijevo i desno dijete. Odredi leksikografski najmanji niz koji se može dobiti.</p>
<h3>Ulaz</h3>
<p>$n \le 1000$ neparan, $0 \le m \le \frac{n-1}{2}$; zatim $n$ redaka: <code>1 l r</code> (djeca vrha $i$, $l, r \gt i$) ili <code>2 a</code> (list s oznakom $1 \le a \le 10^9$).</p>
<h3>Izlaz</h3>
<p>$\frac{n+1}{2}$ brojeva.</p>
<h3>Primjer</h3>
<p>$n = 3$, $m = 0$, listovi $1, 2$: <code>1 2</code>. $n = 7$, vrh $1$ ima djecu $2,3$; $2$ ima $4,5$; $3$ ima $6,7$; listovi $4,2,3,1$: za $m = 1$ izlaz <code>2 4 3 1</code>, za $m = 2$ izlaz <code>1 3 4 2</code>.</p>
''',
    'hints': [
        r'''
<p>Dvije zamjene u istom vrhu se poništavaju. Koje konačne konfiguracije („skup zamijenjenih vrhova” $F$) su dostižne s <em>točno</em> $m$ zamjena?</p>
''',
        r'''
<p>Dostižne su točno $F$ s $|F| \le m$ i $|F| \equiv m \pmod 2$ (višak zamjena potrošimo u parovima na bilo kojem unutarnjem vrhu). Za fiksni $F$ niz listova je konkatenacija nizova podstabala – razmišljaj o DP-u po podstablima.</p>
''',
        r'''
<p>$S[v][j]$ = leksikografski najmanji niz listova podstabla $v$ s točno $j$ zamjena u podstablu. Sve varijante podstabla imaju istu duljinu, pa je za fiksnu raspodjelu zamjena među djecu najbolja konkatenacija najboljih dijelova; za vrh $v$ isprobaj i redoslijed s zamjenom i bez nje.</p>
''',
    ],
    'coach': [
        (r'Zamjene se izvode točno $m$ puta. Što je zapravo bitno na kraju?',
         r'''
<p>Konačni raspored listova ovisi samo o tome koji su unutarnji vrhovi zamijenjeni <em>neparan</em> broj puta – skup $F$. Skup $F$ je dostižan s točno $m$ zamjena ako i samo ako je $|F| \le m$ i $m - |F|$ paran: preostale $m - |F|$ zamjene odigramo u parovima na bilo kojem unutarnjem vrhu (postoji, jer $m \ge 1$ povlači $n \ge 3$). Obrat: svaka zamjena mijenja parnost ukupnog broja, pa je $|F| \equiv m$, a $|F| \le m$ očito.</p>
'''),
        (r'Zašto se problem razbija po podstablima i što točno pamtimo?',
         r'''
<p>Niz listova podstabla $v$ je konkatenacija nizova lijevog i desnog djeteta (u zamijenjenom redoslijedu ako je $v \in F$). Pamtimo $S[v][j]$ = leksikografski najmanji niz listova podstabla $v$ koji se može dobiti s točno $j$ zamijenjenih vrhova <em>unutar</em> podstabla, za $0 \le j \le \min(\text{broj unutarnjih vrhova}, m)$.</p>
'''),
        (r'Zašto smijemo uzeti „najbolji lijevi dio ++ najbolji desni dio” umjesto da gledamo sve kombinacije?',
         r'''
<p>Svi nizovi podstabla $l$ imaju istu duljinu (broj listova podstabla je fiksan). Leksikografska usporedba dviju konkatenacija $A \,{+}{+}\, B$ i $A' \,{+}{+}\, B'$ s $|A| = |A'|$ najprije uspoređuje $A$ i $A'$, a tek pri jednakosti $B$ i $B'$. Zato je za fiksni $a$ najbolji izbor $S[l][a] \,{+}{+}\, S[r][j-a]$ (bez zamjene u $v$) odnosno $S[r][a] \,{+}{+}\, S[l][j-1-a]$ (sa zamjenom u $v$); $S[v][j]$ je minimum tih kandidata po svim $a$.</p>
'''),
        (r'Koliko to košta i kako stati u 64 MiB?',
         r'''
<p>Za vrh $v$ s $L_v$ listova i $I_v$ unutarnjih vrhova tablica $S[v]$ ima $\min(I_v, m) + 1$ nizova duljine $L_v$; gradnja košta $O(m \cdot \min(I_v, m) \cdot L_v)$. Za $n \le 1000$ ($\le 500$ listova, $m \le 499$) najgori slučajevi (dugačka „gusjenica” ili puno stablo) ostaju daleko ispod $10^9$ jednostavnih operacija, a mjerenja daju $\lt 0.1$ s. Memorija: tablice djece brišemo čim je roditelj izračunat, pa istodobno živi tek $O(\text{dubina})$ tablica – ukupno nekoliko MB.</p>
'''),
    ],
    'tips': [
        r'''Kad se operacija poništava sama sa sobom (zamjena, XOR), „točno $m$ puta” znači „najviše $m$ puta uz istu parnost” – provjeri postoji li mjesto na kojem se višak može potrošiti.''',
        r'''Leksikografski minimum konkatenacije dijelova <em>fiksnih duljina</em> je konkatenacija minimuma dijelova; kad duljine nisu fiksne, ta tvrdnja pada.''',
        r'''Uz strogo memorijsko ograničenje pusti tablice djece van dosega odmah nakon spajanja (lokalne varijable u rekurziji) i vraćaj rezultate premještanjem (<code>std::move</code>), ne kopiranjem.''',
    ],
    'solution': r'''
<p>Vlastita izvedba, potvrđena brute forceom s doslovno $m$ zamjena (javnu analizu ovog zadatka objavio je i blog sheauhaw.com, 2023). Zamjena je involucija, pa je konačni raspored određen skupom $F$ vrhova zamijenjenih neparan broj puta; $F$ je dostižan s točno $m$ zamjena točno kad je $|F| \le m$ i $|F| \equiv m \pmod 2$ (višak trošimo u parovima). Dinamičko programiranje po podstablima: $S[v][j]$ je leksikografski najmanji niz listova podstabla $v$ s točno $j$ zamijenjenih vrhova u podstablu. Kako svi nizovi jednog podstabla imaju istu duljinu, $S[v][j] = \min\big(\min_a S[l][a] \,{+}{+}\, S[r][j-a],\ \min_a S[r][a] \,{+}{+}\, S[l][j-1-a]\big)$. Odgovor je $\min\{S[1][j] : j \le m,\ j \equiv m \pmod 2\}$. Nizove čuvamo eksplicitno i oslobađamo tablice djece odmah nakon spajanja; $O(m^2 \cdot n)$ u najgorem slučaju, u praksi trenutno.</p>
''',
    'detailed': r'''
<h3>1. Što točno $m$ zamjena može proizvesti</h3>
<p>Zamjena djece u vrhu $v$ je involucija: dvije zamjene u istom vrhu poništavaju se, a zamjene u različitim vrhovima komutiraju (svaka mijenja samo redoslijed dvoje djece svog vrha). Konačni raspored stoga ovisi samo o skupu $F$ vrhova zamijenjenih <em>neparan</em> broj puta.</p>
<p><strong>Lema.</strong> Skup $F$ unutarnjih vrhova dostižan je s točno $m$ zamjena ako i samo ako je $|F| \le m$ i $|F| \equiv m \pmod 2$. <em>Dokaz.</em> ($\Rightarrow$) Svaki vrh iz $F$ zamijenjen je barem jednom, pa $|F| \le m$; zbroj svih brojeva zamjena je $m$, a vrhovi izvan $F$ pridonose parno, oni iz $F$ neparno, pa je $m \equiv |F|$. ($\Leftarrow$) Zamijenimo svaki vrh iz $F$ jednom, a preostalih $m - |F|$ (paran broj) zamjena odigramo u parovima na proizvoljnom unutarnjem vrhu; unutarnji vrh postoji kad je $m \ge 1$ jer $m \le (n-1)/2$ povlači $n \ge 3$. $\square$</p>
<h3>2. Dinamičko programiranje po podstablima</h3>
<p>Za vrh $v$ neka je $L_v$ broj listova i $I_v$ broj unutarnjih vrhova u podstablu. Definiramo $S[v][j]$, $0 \le j \le \min(I_v, m)$, kao leksikografski najmanji niz listova podstabla $v$ ostvariv skupom $F$ s točno $j$ vrhova <em>unutar podstabla $v$</em>. List: $S[v][0] = (a_v)$. Unutarnji vrh $v$ s djecom $l, r$:</p>
<p>$$S[v][j] = \min\Big( \min_{a} S[l][a] \,{+}{+}\, S[r][j-a],\ \ \min_{a} S[r][a] \,{+}{+}\, S[l][j-1-a] \Big),$$</p>
<p>gdje prvi minimum odgovara $v \notin F$, drugi $v \in F$ (djeca zamijenjena, jedna zamjena potrošena), a $a$ prolazi vrijednosti za koje su oba indeksa unutar dopuštenih raspona.</p>
<p><strong>Zašto je to točno.</strong> Svi nizovi podstabla $l$ imaju duljinu $L_l$, a podstabla $r$ duljinu $L_r$. Za fiksni redoslijed djece i fiksnu raspodjelu $(a, j-a)$ svaka ostvariva konkatenacija ima oblik $A \,{+}{+}\, B$ s $A$ iz skupa nizova od $l$ (s $a$ zamjena) i $B$ iz skupa nizova od $r$. Za nizove jednake duljine $A \,{+}{+}\, B \lt A' \,{+}{+}\, B'$ vrijedi točno kad je $A \lt A'$, ili $A = A'$ i $B \lt B'$; zato je minimum upravo $\min A \,{+}{+}\, \min B = S[l][a] \,{+}{+}\, S[r][j-a]$. Skup svih ostvarivih nizova podstabla $v$ s $j$ zamjena je unija tih skupova po redoslijedu i raspodjeli, pa je $S[v][j]$ minimum kandidata. $\square$</p>
<h3>3. Odgovor</h3>
<p>Po Lemi je odgovor $\min\{S[1][j] : 0 \le j \le \min(I_1, m),\ j \equiv m \pmod 2\}$. Za $m = 0$ to je $S[1][0]$ – izvorni niz (prvi primjer). U drugom primjeru ($m = 1$) najbolje je zamijeniti korijen: $2\,4\,3\,1$; u trećem ($m = 2$) zamjena korijena i njegova (novog) drugog djeteta daje $1\,3\,4\,2$.</p>
<h3>4. Složenost i memorija</h3>
<p>Gradnja $S[v]$: za svaki $j$ ima $O(\min(I_l, I_r, j))$ kandidata, svaki se izgradi i usporedi u $O(L_v)$; ukupno po vrhu $O(\min(I_v, m) \cdot \min(I_l, I_r, m) \cdot L_v)$. Za $n \le 1000$ (najviše $500$ listova, $m \le 499$) i najgore oblike (gusjenica: $L_v$ velik ali $\min(I_l, I_r)$ malen; puno stablo: obrnuto) to je najviše nekoliko puta $10^7$ elementarnih operacija – izmjereno $\lt 0.1$ s.</p>
<p>Memorijsko ograničenje je $64$ MiB. Tablica $S[v]$ ima $(\min(I_v, m) + 1) \cdot L_v$ brojeva – za korijen do $500 \cdot 500 \cdot 4$ B $= 1$ MB. Bitno je da tablice djece oslobodimo odmah nakon spajanja (u rekurziji su lokalne i izlaze iz dosega), pa istodobno živi samo po jedna tablica na svakoj razini trenutnog puta rekurzije; ukupno nekoliko MB. Rezultate vraćamo premještanjem, ne kopiranjem.</p>
<h3>5. Zamke</h3>
<ul>
<li>Za list je $I_v = 0$ i tablica ima samo $j = 0$; raspon $a$ u spajanju ograniči s $\max(0, j - I_r) \le a \le \min(j, I_l)$ (bez zamjene) i $\max(0, j-1-I_l) \le a \le \min(j-1, I_r)$ (sa zamjenom).</li>
<li>Parnost provjeravaj na $m - j$, ne na $j$.</li>
<li>Oznake listova su do $10^9$ – <code>int</code> dostaje, ali usporedba mora biti leksikografska po vektorima, ne po zbroju ili duljini.</li>
</ul>
''',
    'verified': r'''uzorci 3/3, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 0.05 s).''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'water235', 'title_hr': 'water235', 'slug': 'K_water235',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Matrica $N \times M$. Po pravilima Minecrafta, prazno polje s barem dva susjedna (po bridu) polja ispunjena vodom i samo se ispuni vodom; postupak se ponavlja dok je moguće. Odaberi najmanji broj polja koja početno ispuniš vodom tako da na kraju sva polja budu ispunjena.</p>
<h3>Ulaz</h3>
<p>$N$ i $M$, $1 \le N \cdot M \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Najmanji broj jedinica, zatim $N$ redaka matrice $0/1$ ($1$ = početno ispunjeno). Bilo koje optimalno rješenje se prihvaća.</p>
<h3>Primjer</h3>
<p>$2 \times 1$: $2$, matrica <code>1</code>/<code>1</code>. $3 \times 3$: $3$, npr. <code>1 0 1</code>/<code>0 0 0</code>/<code>0 1 0</code>.</p>
''',
    'hints': [
        r'''
<p>Promatraj <em>opseg</em> skupa punih ćelija (broj bridova između pune i prazne ćelije ili ruba). Kako se opseg mijenja kad se napuni ćelija koja ima barem dva puna susjeda?</p>
''',
        r'''
<p>Opseg nikad ne raste, na kraju iznosi $2(N + M)$, a na početku je najviše $4c$. Dakle $c \ge \lceil (N+M)/2 \rceil$. Sad tu granicu treba dostići.</p>
''',
        r'''
<p>Dijagonala kvadrata $s \times s$ ($s = \min(N, M)$) napuni cijeli kvadrat. Preostali „rep” pokrij tako da u zadnjem retku (ili stupcu) napuniš svaku drugu ćeliju, počevši od kraja.</p>
''',
    ],
    'coach': [
        (r'Koja se veličina lijepo ponaša pod pravilom „ćelija s barem dva puna susjeda se puni”?',
         r'''
<p>Opseg $P$ skupa punih ćelija: broj parova (puna ćelija, njezin brid) kojima je na drugoj strani prazna ćelija ili rub matrice. Kad se napuni ćelija s $t \ge 2$ punih susjeda, ona donosi $4 - t$ novih rubnih bridova, a poništava $t$ starih, pa je $\Delta P = 4 - 2t \le 0$. Opseg <strong>nikad ne raste</strong>.</p>
'''),
        (r'Kako iz toga dobiti donju granicu za broj početnih ćelija $c$?',
         r'''
<p>Na početku je $P \le 4c$ (svaka ćelija ima $4$ brida). Na kraju je puna cijela matrica, pa je $P = 2(N + M)$. Iz monotonosti $2(N+M) \le 4c$, tj. $c \ge (N+M)/2$, dakle $c \ge \lceil (N+M)/2 \rceil$ jer je $c$ cijeli broj.</p>
'''),
        (r'Kako dijagonala puni kvadrat, i zašto je to dobra baza konstrukcije?',
         r'''
<p>U kvadratu $s \times s$ napunimo $(i, i)$ za $i = 0, \dots, s-1$. Ćelija $(i, j)$ s $|i - j| = t \ge 1$ ima susjede $(i, j \mp 1)$ i $(i \pm 1, j)$ (prema dijagonali) na udaljenosti $t - 1$ od dijagonale; indukcijom po $t$ oni su puni, pa se puni i $(i, j)$. Dijagonala troši $s$ ćelija za kvadrat čija je „polovica opsega” $s$ – točno onoliko koliko donja granica dopušta.</p>
'''),
        (r'Kako riješiti ostatak kad je $N \ne M$, a da ukupno bude točno $\lceil (N+M)/2 \rceil$?',
         r'''
<p>Neka je $N \le M$, $s = N$. U zadnjem retku napunimo stupce $M-1, M-3, \dots$ dok su $\ge s$. Stupac $s - 1$ je pun (kvadrat). Ćelija zadnjeg retka u stupcu $j \ge s$ koja nije početna ima oba horizontalna susjeda puna (početna ili iz kvadrata), pa se cijeli zadnji redak napuni; zatim se stupci $s, s+1, \dots$ pune odozdo prema gore jer ćelija $(i, j)$ ima puna $(i+1, j)$ i $(i, j-1)$. Broj početnih ćelija je $s + \lceil (M - s)/2 \rceil = \lceil (N+M)/2 \rceil$. Za $N \gt M$ simetrično u zadnjem stupcu.</p>
'''),
    ],
    'tips': [
        r'''<strong>Monotona veličina = donja granica.</strong> Za procese širenja u mreži (perkolacija, „bootstrap” punjenje) potraži veličinu koja pod pravilom ne raste – opseg, broj komponenata, zbroj po rubu – i usporedi početnu i konačnu vrijednost.''',
        r'''Konstrukciju provjeri simulacijom (checker) na svim malim dimenzijama i usporedi broj s iscrpnom pretragom; za velike matrice ispis složi u jedan <code>string</code> i ispiši odjednom ($N \cdot M \le 10^6$).''',
        r'''Kad matrica nije kvadratna, riješi kvadratni dio optimalnom bazom, a ostatak pokrij uzorkom koji „strši” svaku drugu ćeliju – oba dijela troše točno pola svog doprinosa opsegu.''',
    ],
    'solution': r'''
<p>Vlastita izvedba, potvrđena iscrpnom pretragom za $N \cdot M \le 16$ i checkerom koji simulira punjenje. Opseg skupa punih ćelija nikad ne raste: ćelija s $t \ge 2$ punih susjeda mijenja opseg za $4 - 2t \le 0$. Na kraju je opseg $2(N+M)$, na početku najviše $4c$, pa je $c \ge \lceil (N+M)/2 \rceil$. Granica se dostiže: za $s = \min(N, M)$ napunimo dijagonalu $(i, i)$, $i \lt s$ (ona indukcijom po udaljenosti od dijagonale napuni cijeli kvadrat $s \times s$), a u zadnjem retku (ako $N \le M$; inače zadnjem stupcu) svaku drugu ćeliju počevši od kraja, u stupcima $\ge s$. Zadnji redak se napuni jer svaka nepočetna ćelija ima puna oba horizontalna susjeda, a zatim se preostali stupci pune odozdo. Ukupno $s + \lceil (\max(N,M) - s)/2 \rceil = \lceil (N+M)/2 \rceil$ ćelija, $O(NM)$.</p>
''',
    'detailed': r'''
<h3>1. Donja granica preko opsega</h3>
<p>Za skup punih ćelija $F$ definiramo <em>opseg</em> $P(F)$ kao broj parova $(\text{ćelija iz } F, \text{brid})$ kojima je s druge strane brida prazna ćelija ili rub matrice. Za $|F| = c$ očito je $P(F) \le 4c$.</p>
<p><strong>Lema.</strong> Punjenje ćelije $x \notin F$ koja ima $t \ge 2$ susjeda u $F$ ne povećava opseg. <em>Dokaz.</em> Bridovi koji spajaju $x$ s njezinim $t$ punim susjedima bili su rubni (za susjeda) i prestaju to biti: $-t$. Preostala $4 - t$ brida ćelije $x$ postaju rubni: $+(4-t)$. Ukupno $\Delta P = 4 - 2t \le 0$. $\square$</p>
<p>Proces završava kad je puna cijela matrica (tražimo da se sve napuni), a tada je $P = 2(N + M)$ (samo vanjski rub). Zbog monotonosti $2(N+M) \le P(F_0) \le 4c$, dakle $c \ge (N+M)/2$, tj. $c \ge \lceil (N+M)/2 \rceil$.</p>
<h3>2. Dijagonala puni kvadrat</h3>
<p>U kvadratu $s \times s$ (indeksi $0..s-1$) napunimo $(i, i)$ za sve $i$. Tvrdimo da se napuni sve. Neka je $t = |i - j|$; dokazujemo indukcijom po $t \ge 1$ da se ćelija $(i, j)$ napuni. Za $i \lt j$ njezini susjedi $(i, j-1)$ i $(i+1, j)$ imaju $|i - j| = t - 1$ (i unutar su kvadrata jer $i + 1 \le j \le s - 1$), pa su po pretpostavci puni – dva puna susjeda, ćelija se puni. Slučaj $i \gt j$ je simetričan. $\square$ Dijagonala troši $s$ ćelija, a $s \times s$ kvadrat sam po sebi traži $\lceil 2s/2 \rceil = s$ – konstrukcija je za kvadrat optimalna.</p>
<h3>3. Rep za $N \ne M$</h3>
<p>Neka je $N \le M$ i $s = N$ (slučaj $N \gt M$ je simetričan: umjesto zadnjeg retka koristimo zadnji stupac). Uz dijagonalu, u zadnjem retku $N - 1$ napunimo stupce $M-1, M-3, M-5, \dots$ sve dok su $\ge s$; to su stupci $j \in [s, M-1]$ s $j \equiv M - 1 \pmod 2$.</p>
<p><em>Zadnji redak se napuni.</em> Kvadrat je pun, posebno $(N-1, s-1)$. Neka je $j \ge s$ stupac koji nije početan; tada je $j \le M - 2$ (jer $M - 1$ jest početan) i $j - 1 \ge s - 1$. Susjed $(N-1, j+1)$ je početan (prava parnost, $\le M-1$), a susjed $(N-1, j-1)$ je početan ili iz kvadrata ($j - 1 = s - 1$). Dva puna susjeda – ćelija se puni. Time su puni svi stupci zadnjeg retka.</p>
<p><em>Stupci se pune odozdo.</em> Indukcijom po $j = s, s+1, \dots, M-1$ i po retku $i = N-2, N-3, \dots, 0$: ćelija $(i, j)$ ima pune susjede $(i+1, j)$ (redak ispod, već pun) i $(i, j-1)$ (stupac lijevo: kvadrat ili prethodno napunjen). $\square$</p>
<p>Broj početnih ćelija: $s$ na dijagonali plus broj $j \in [s, M-1]$ prave parnosti, tj. $\lfloor (M - 1 - s)/2 \rfloor + 1 = \lceil (M - s)/2 \rceil$ (za $s = M$ nula). Ukupno $s + \lceil (M-s)/2 \rceil = \lceil (M + s)/2 \rceil = \lceil (N+M)/2 \rceil$ – točno donja granica.</p>
<h3>4. Rubni slučajevi</h3>
<ul>
<li>$N = M$: samo dijagonala, $N$ ćelija.</li>
<li>$N = 1$: $s = 1$, dijagonala je ćelija $(0,0)$, a u „zadnjem retku” (jedinom) pune se stupci $M-1, M-3, \dots \ge 1$: uzorak $1\,0\,1\,0\,1\dots$ ili $1\,1\,0\,1\,0\dots$ s $\lceil (M+1)/2 \rceil$ jedinica; svaka nula ima dva puna susjeda. Primjer $2 \times 1$: obje ćelije, $2 = \lceil 3/2 \rceil$.</li>
<li>Primjer $3 \times 3$: dijagonala, $3$ ćelije (službeni izlaz koristi drugi optimalni raspored – svaki valjani je prihvaćen).</li>
</ul>
<h3>5. Složenost i ispis</h3>
<p>Konstrukcija i ispis su $O(NM)$, $NM \le 10^6$. Ispis od $2NM$ znakova složimo u jedan <code>string</code> i ispišemo jednim <code>fwrite</code>; s $10^6$ poziva <code>printf</code> lako bi se prekoračilo 1 s.</p>
''',
    'verified': r'''uzorci 2/2, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 0.02 s).''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Square', 'title_hr': 'Kvadrat', 'slug': 'L_square',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Pozitivan cijeli broj $x$ u jednoj operaciji možeš pretvoriti u $x - 1$ ili u $x + \left\lfloor \sqrt{2x} + 1.5 \right\rfloor$. Nađi najmanji broj operacija da od $x$ dobiješ $y$.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 10^5$ testova; $1 \le x, y \le 10^{18}$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan broj.</p>
<h3>Primjer</h3>
<p>$5 \to 1$: $4$; $1 \to 5$: $3$.</p>
''',
    'hints': [
        r'''
<p>Poredaj prirodne brojeve u trokut: $1$; $2, 3$; $4, 5, 6$; … Redak $r$ sadrži brojeve $\frac{(r-1)r}{2} + 1, \dots, \frac{r(r+1)}{2}$. Što operacija $x \mapsto x + \lfloor \sqrt{2x} + 1.5 \rfloor$ radi u tom trokutu?</p>
''',
        r'''
<p>Za $x$ u retku $r$ vrijedi $\lfloor \sqrt{2x} + 1.5 \rfloor = r + 1$, pa skok vodi iz $(r, c)$ u $(r+1, c+1)$ – po dijagonali, razlika $c - r$ se čuva. Operacija $x - 1$ ide ulijevo u retku, a s početka retka na kraj prethodnog.</p>
''',
        r'''
<p>Za $y \le x$ odgovor je $x - y$. Za $y \gt x$ usporedi $u_x = c_x - r_x$ i $u_y = c_y - r_y$: ako je $u_x \ge u_y$, skoči do retka $r_y$ i spusti se u retku; inače prvo siđi na kraj prethodnog retka (dijagonala $u = 0$), pa skoči i spusti se.</p>
''',
    ],
    'coach': [
        (r'Kako „ukrotiti” operaciju $x \mapsto x + \lfloor \sqrt{2x} + 1.5 \rfloor$?',
         r'''
<p>Poredamo brojeve u trokut: redak $r$ čine brojevi $T(r-1) + 1, \dots, T(r)$, $T(r) = \frac{r(r+1)}{2}$; broj $x = T(r-1) + c$ ima redak $r$ i stupac $c \in [1, r]$. Za takav $x$ je $r^2 - r + 2 \le 2x \le r^2 + r$, a $(r - 0.5)^2 = r^2 - r + 0.25$ i $(r + 0.5)^2 = r^2 + r + 0.25$, pa je $r - 0.5 \le \sqrt{2x} \lt r + 0.5$, tj. $\lfloor \sqrt{2x} + 1.5 \rfloor = r + 1$. Skok vodi u $x + r + 1 = T(r) + c + 1$, dakle iz $(r, c)$ u $(r+1, c+1)$: <em>jedan redak niže, ista dijagonala</em> $u = c - r$.</p>
'''),
        (r'A operacija $x - 1$? Što se događa s retkom i dijagonalom?',
         r'''
<p>Iz $(r, c)$ s $c \gt 1$ idemo u $(r, c-1)$: redak isti, $u$ se smanji za $1$. Iz $(r, 1)$ idemo u $T(r-1) = (r-1, r-1)$: redak se smanji za $1$, a $u$ skoči s $1 - r$ na $0$ („omotavanje”). Skok povećava redak za $1$ i čuva $u$; dekrement čuva redak ili ga smanjuje za $1$. Zato je za put od $x$ do $y$ broj skokova $J$ i broj omotavanja $W$ vezan s $J - W = r_y - r_x$.</p>
'''),
        (r'Zašto je za $y \le x$ odgovor $x - y$, a za $y \gt x$ i $u_x \ge u_y$ odgovor $2(r_y - r_x) + (c_x - c_y)$?',
         r'''
<p>Za $y \le x$ svaki skok samo povećava vrijednost, pa treba barem $x - y$ dekremenata; toliko i dostaje. Za $y \gt x$ neka put ima $J$ skokova i $D$ dekremenata, od čega $W$ omotavanja. Dijagonala se mijenja samo dekrementima: običan je smanji za $1$, omotavanje u retku $r'$ poveća je za $r' - 1 \ge 1$. Dakle $D = (u_x - u_y) + W + \sum (\text{dobici}) \ge (u_x - u_y) + 2W$, a ukupno $J + D \ge (r_y - r_x) + (u_x - u_y) + 3W$. Minimum je za $W = 0$: $(r_y - r_x) + (u_x - u_y) = 2(r_y - r_x) + c_x - c_y$, a postiže se s $r_y - r_x$ skokova pa $c_x + (r_y - r_x) - c_y \ge 0$ dekremenata unutar retka $r_y$.</p>
'''),
        (r'Što kad je $u_x \lt u_y$, tj. $y$ je na dijagonali „desno” od $x$?',
         r'''
<p>Dijagonalu možemo povećati samo omotavanjem, pa je $W \ge 1$. Prvo omotavanje događa se u nekom retku $r_1 \ge r_x$ (prije njega redak samo raste), s dobitkom $r_1 - 1 \ge r_x - 1$. Iz ocjene $J + D = (r_y - r_x) + (u_x - u_y) + 2W + \sum(\text{dobici})$ dobivamo $J + D \ge (r_y - r_x) + (u_x - u_y) + 2 + (r_x - 1) = c_x + (r_y - r_x + 1) + (r_y - c_y)$, uz jednakost za $W = 1$ i $r_1 = r_x$. Taj put postoji: $c_x - 1$ dekremenata do $(r_x, 1)$, jedno omotavanje na $(r_x - 1, r_x - 1)$, $r_y - r_x + 1$ skokova do $(r_y, r_y)$ i $r_y - c_y$ dekremenata. (Ovdje je $c_x \lt r_x$, pa je $r_x \ge 2$ i omotavanje ne izlazi iz prirodnih brojeva.)</p>
'''),
    ],
    'tips': [
        r'''Operacije s $\lfloor \sqrt{\cdot} \rfloor$ često imaju skrivenu strukturu trokutnih brojeva: provjeri kamo operacija vodi brojeve $T(r-1)+1, \dots, T(r)$ i traži invarijantu (ovdje dijagonala $c - r$).''',
        r'''Donje granice u ovakvim „najmanji broj operacija” zadacima dokazuj knjigovodstvom: izrazi ukupni pomak dvaju parametara (redak, dijagonala) preko broja operacija svake vrste i minimiziraj.''',
        r'''Za $x \le 10^{18}$ redak računaj s <code>sqrtl</code> pa korigiraj cjelobrojno (dok $T(r-1) \ge x$ smanjuj, dok $T(r) \lt x$ povećavaj) – zaokruživanje u pomičnom zarezu inače griješi za $\pm 1$.''',
    ],
    'solution': r'''
<p>Vlastita izvedba, potvrđena brute forceom (BFS po doslovnim operacijama). Poredamo brojeve u trokut: redak $r$ sadrži $T(r-1) + 1, \dots, T(r)$ s $T(r) = r(r+1)/2$, a $x = T(r-1) + c$ ima koordinate $(r, c)$. Za takav $x$ je $\lfloor \sqrt{2x} + 1.5 \rfloor = r + 1$, pa skok vodi iz $(r, c)$ u $(r + 1, c + 1)$ – čuva dijagonalu $u = c - r$; dekrement ide u $(r, c - 1)$, a iz $(r, 1)$ „omotava” na $(r-1, r-1)$ (dijagonala $0$). Za $y \le x$ odgovor je $x - y$. Za $y \gt x$: ako je $u_x \ge u_y$, odgovor je $2(r_y - r_x) + (c_x - c_y)$ (skokovi do retka $r_y$, pa dekrementi); inače je $c_x + (r_y - r_x + 1) + (r_y - c_y)$ (dekrementi do kraja prethodnog retka, skokovi do $(r_y, r_y)$, dekrementi). Optimalnost slijedi iz knjigovodstva: $J - W = r_y - r_x$ i $D = (u_x - u_y) + W + \sum(\text{dobici omotavanja})$, gdje je dobitak $\ge 1$, a prvog omotavanja $\ge r_x - 1$. Po upitu $O(1)$.</p>
''',
    'detailed': r'''
<h3>1. Trokutni raspored i djelovanje operacija</h3>
<p>Neka je $T(r) = r(r+1)/2$. Redak $r \ge 1$ trokuta sadrži brojeve $T(r-1) + 1, \dots, T(r)$; broj $x = T(r-1) + c$, $1 \le c \le r$, ima <em>redak</em> $r$, <em>stupac</em> $c$ i <em>dijagonalu</em> $u = c - r \in [1 - r, 0]$.</p>
<p><strong>Lema 1.</strong> Za $x$ u retku $r$ je $\lfloor \sqrt{2x} + 1.5 \rfloor = r + 1$. <em>Dokaz.</em> $2x \in [2T(r-1) + 2, 2T(r)] = [r^2 - r + 2, r^2 + r]$. Kako je $(r - \tfrac12)^2 = r^2 - r + \tfrac14 \lt r^2 - r + 2$ i $(r + \tfrac12)^2 = r^2 + r + \tfrac14 \gt r^2 + r$, vrijedi $r - \tfrac12 \lt \sqrt{2x} \lt r + \tfrac12$, pa $\sqrt{2x} + 1.5 \in (r + 1, r + 2)$. $\square$</p>
<p>Dakle skok vodi $x \mapsto x + r + 1 = T(r) + (c + 1)$, tj. $(r, c) \mapsto (r+1, c+1)$: redak $+1$, dijagonala nepromijenjena. Dekrement: za $c \gt 1$ ide $(r, c) \mapsto (r, c-1)$ (redak isti, $u$ manji za $1$); za $c = 1$ ide $x = T(r-1) + 1 \mapsto T(r-1) = (r-1, r-1)$ – nazovimo to <em>omotavanje</em>: redak $-1$, dijagonala s $1 - r$ na $0$, dakle <em>dobitak</em> $r - 1 \ge 1$ (omotavanje iz retka $1$ vodilo bi u $0$, što nije dopušteno).</p>
<h3>2. Knjigovodstvo puta</h3>
<p>Promotrimo bilo koji niz operacija od $x$ do $y$ s $J$ skokova i $D$ dekremenata, među kojima je $W$ omotavanja (u redcima $r_1, r_2, \dots, r_W$). Redak: svaki skok $+1$, svako omotavanje $-1$, obični dekrementi $0$, pa je $J - W = r_y - r_x$. Dijagonala: skokovi $0$, obični dekrementi $-1$, omotavanje u retku $r'$ daje $+(r' - 1)$, pa je $u_y = u_x - (D - W) + \sum_i (r_i - 1)$, tj.</p>
<p>$$D = (u_x - u_y) + W + \sum_{i=1}^{W} (r_i - 1), \qquad J + D = (r_y - r_x) + (u_x - u_y) + 2W + \sum_{i=1}^{W}(r_i - 1).$$</p>
<h3>3. Slučaj $y \le x$</h3>
<p>Skokovi samo povećavaju vrijednost, pa je $x - y \le D \le J + D$; niz od $x - y$ dekremenata to postiže. Odgovor $x - y$.</p>
<h3>4. Slučaj $y \gt x$, $u_x \ge u_y$</h3>
<p>Svi članovi $r_i - 1$ su $\ge 1$, pa je $J + D \ge (r_y - r_x) + (u_x - u_y) + 3W \ge (r_y - r_x) + (u_x - u_y)$, a to je $2(r_y - r_x) + (c_x - c_y)$. Put koji to postiže: $r_y - r_x$ skokova (redak $r_x \le r_y$ jer je $x \lt y$) dovodi u $(r_y, c_x + r_y - r_x)$, gdje je $c_x + r_y - r_x \ge c_y$ upravo zbog $u_x \ge u_y$; zatim $c_x + r_y - r_x - c_y$ običnih dekremenata unutar retka $r_y$. Primjer $x = 1, y = 5$: $(1,1) \to (3, 2)$, $u_x = 0 \ge u_y = -1$, odgovor $2 \cdot 2 - 1 = 3$ ($1 \to 3 \to 6 \to 5$).</p>
<h3>5. Slučaj $y \gt x$, $u_x \lt u_y$</h3>
<p>Dijagonalu povećava samo omotavanje, pa je $W \ge 1$. Prije prvog omotavanja put nema omotavanja, pa redak ne pada: $r_1 \ge r_x$, dakle $r_1 - 1 \ge r_x - 1$. Ostali članovi su $\ge 1$, pa $J + D \ge (r_y - r_x) + (u_x - u_y) + 2 + (r_x - 1) = c_x + (r_y - r_x + 1) + (r_y - c_y)$, s jednakošću samo za $W = 1$, $r_1 = r_x$. Konstrukcija: $c_x - 1$ dekremenata do $(r_x, 1)$, omotavanje na $(r_x - 1, r_x - 1)$ (dijagonala $0$), zatim $r_y - r_x + 1$ skokova do $(r_y, r_y) = T(r_y)$ i $r_y - c_y$ dekremenata do $y$. Uvjet $u_x \lt u_y \le 0$ daje $c_x \lt r_x$, pa je $r_x \ge 2$ i omotavanje vodi u $T(r_x - 1) \ge 1$. Primjer $x = 2 = (2,1)$, $y = 3 = (2,2)$: $1 + 1 + 0 = 2$ ($2 \to 1 \to 3$).</p>
<h3>6. Implementacija</h3>
<p>Redak broja $v$ je najmanji $r$ s $T(r) \ge v$. Za $v \le 10^{18}$ krenemo od $\lfloor \sqrt{2v} \rfloor$ (u <code>long double</code>) i korigiramo cjelobrojno: dok je $T(r-1) \ge v$ smanjuj $r$, dok je $T(r) \lt v$ povećavaj. $T(r)$ za $r \approx 1.5 \cdot 10^9$ stane u 64 bita. Stupac je $c = v - T(r-1)$. Po upitu $O(1)$; sve formule su u <code>long long</code> (odgovor je $\le 2 \cdot 10^{18}$ jer je $\le x - y$ ili $\le 3 r_y + c_x$).</p>
''',
    'verified': r'''uzorci 1/1, 300 slučajnih malih testova protiv brute forcea, 3 velikih testova (najviše 0.03 s).''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Delete the Tree', 'title_hr': 'Izbriši stablo', 'slug': 'M_delete_the_tree',
    'tl': '1 s', 'ml': '1024 MiB',
    'statement': r'''
<p>Dano je stablo s $n$ vrhova. Operacija: odaberi skup postojećih vrhova među kojima nema bridova; za svaki odabrani vrh $v$ dodaj brid između svakog para trenutnih susjeda od $v$, zatim izbriši $v$ i sve njegove bridove (redoslijed unutar jedne operacije ne utječe na rezultat; mogu nastati višestruki bridovi).</p>
<p>U najviše $10$ operacija izbriši sve vrhove. Rješenje sigurno postoji; ispiši bilo koje.</p>
<h3>Ulaz</h3>
<p>$3 \le n \le 500$; $n - 1$ različitih bridova $x_i \lt y_i$.</p>
<h3>Izlaz</h3>
<p>Broj operacija $m$ ($0 \le m \le 10$), zatim $m$ redaka: $k$ i $k$ različitih odabranih vrhova.</p>
<h3>Primjer</h3>
<p>Bridovi $1\text{-}2, 1\text{-}3, 1\text{-}4, 4\text{-}5$: npr. $4$ operacije — $\{1, 5\}$, $\{2\}$, $\{4\}$, $\{3\}$.</p>
''',
    'hints': [
        r'''
<p>Kad izbrišeš vrh $v$ i spojiš sve parove njegovih susjeda, koji su vrhovi nakon toga spojeni bridom? Pokušaj to opisati preko <em>puta u izvornom stablu</em>.</p>
''',
        r'''
<p>Nakon brisanja skupa $S$, vrhovi $x$ i $y$ su susjedni točno kad su svi unutarnji vrhovi puta $x \to y$ u stablu izbrisani. Skup koji brišeš u jednoj operaciji stoga smije sadržavati $x, y$ samo ako na putu između njih postoji još neizbrisan vrh.</p>
''',
        r'''
<p>Centroidna dekompozicija daje svakom vrhu razinu (dubinu u centroidnom stablu), najviše $\lfloor \log_2 500 \rfloor + 1 = 9$ razina. Briši razine od najdublje prema korijenu: dva vrha iste razine razdvaja centroid manje razine koji je još prisutan.</p>
''',
    ],
    'coach': [
        (r'Što operacija radi s grafom? Kako opisati bridove nakon brisanja skupa $S$?',
         r'''
<p>Tvrdnja: nakon brisanja skupa $S$ (u bilo kojem broju operacija), preostali vrhovi $x \ne y$ su susjedni točno kad su <em>svi unutarnji vrhovi puta $x \to y$ u izvornom stablu</em> u $S$. Dokaz indukcijom po broju izbrisanih vrhova: brisanjem $v$ novi brid $x$–$y$ nastaje samo za susjede $x, y$ od $v$, tj. kad su putovi $x \to v$ i $v \to y$ imali sve unutarnje vrhove izbrisane – tada i put $x \to y$ (koji u stablu prolazi kroz $v$, jer je $v$ jedini novi izbrisani vrh na spoju) ima sve unutarnje vrhove izbrisane. Obrat je isti argument unatrag; višestruki bridovi ne mijenjaju susjedstvo.</p>
'''),
        (r'Koji je uvjet da skup vrhova smijemo izbrisati u istoj operaciji?',
         r'''
<p>Odabrani vrhovi moraju biti međusobno nesusjedni u <em>trenutnom</em> grafu, tj. za svaka dva odabrana $x, y$ na putu $x \to y$ u stablu mora postojati vrh koji <strong>još nije izbrisan</strong>. Pri tome brisanje unutar iste operacije ne smeta (zadatak jamči da redoslijed u operaciji nije bitan – nesusjednost se provjerava prije operacije).</p>
'''),
        (r'Zašto centroidna dekompozicija daje dobar redoslijed, i zašto stane u 10 operacija?',
         r'''
<p>Centroid $c$ dijeli komponentu na dijelove veličine $\le n/2$; rekurzivno svaki vrh dobiva razinu $=$ dubina u centroidnom stablu. Za $n \le 500$ veličine komponenata su $500, 250, 125, 62, 31, 15, 7, 3, 1$, dakle najviše $9$ razina $\le 10$. Ako su $x, y$ iste razine $\ell$, u centroidnom stablu imaju najbližeg zajedničkog pretka $c$ razine $\lt \ell$; $x$ i $y$ su bili u komponenti od $c$ i razdvojilo ih je uklanjanje $c$, pa $c$ leži na putu $x \to y$ u stablu. Brišemo razine od najveće prema $0$: kad brišemo razinu $\ell$, vrh $c$ (razina $\lt \ell$) još postoji, pa $x$ i $y$ nisu susjedni.</p>
'''),
        (r'Kako to izgleda u kodu?',
         r'''
<p>Standardna centroidna dekompozicija u $O(n \log n)$ (za $n \le 500$ i naivno $O(n^2)$ prolazi): izračunaj veličine podstabala, nađi centroid (vrh čije su sve „strane” $\le n/2$), zapiši mu razinu, označi ga uklonjenim i rekurzivno obradi susjedne komponente s razinom $+1$. Ispiši broj razina $L$, pa za $\ell = L-1, \dots, 0$ popis vrhova razine $\ell$.</p>
'''),
    ],
    'tips': [
        r'''Operacija „izbriši vrh i spoji mu susjede” (eliminacija vrha) uvijek ima opis preko puteva: $x$ i $y$ su spojeni kad su svi vrhovi između njih eliminirani. Isti argument stoji iza eliminacijskih stabala, treewidth-a i Gaussove eliminacije na grafovima.''',
        r'''Kad zadatak traži $O(\log n)$ „rundi” na stablu, prvo pomisli na centroidnu dekompoziciju: dubina centroidnog stabla je $\le \lfloor \log_2 n \rfloor + 1$.''',
        r'''Za konstruktivne zadatke napiši checker koji doslovno simulira operacije (postojanje vrhova, nesusjednost, spajanje susjeda) – to je jedina poštena provjera kad je ispravnih izlaza mnogo.''',
    ],
    'solution': r'''
<p>Vlastita izvedba (klasična primjena centroidne dekompozicije), provjerena checkerom koji simulira operacije. Nakon brisanja skupa $S$ vrhovi $x, y$ su susjedni točno kad su svi unutarnji vrhovi puta $x \to y$ u stablu izbrisani (indukcija po brisanjima). Centroidnom dekompozicijom svaki vrh dobiva razinu $=$ dubina u centroidnom stablu; za $n \le 500$ ima najviše $9$ razina. Brišemo razine od najdublje prema korijenu, sve vrhove jedne razine u jednoj operaciji: dva vrha iste razine razdvaja njihov najbliži zajednički centroidni predak, koji je manje razine, leži na putu među njima i još nije izbrisan – pa su nesusjedni. Ukupno $\le 9 \le 10$ operacija, $O(n \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Što operacija čini s grafom</h3>
<p>Nazovimo vrh <em>eliminiranim</em> kad je izbrisan. Za skup eliminiranih vrhova $S$ tvrdimo:</p>
<p><strong>Lema 1.</strong> U trenutnom grafu su preostali vrhovi $x \ne y$ susjedni ako i samo ako su svi unutarnji vrhovi (jedinstvenog) puta $x \to y$ u izvornom stablu u $S$.</p>
<p><em>Dokaz</em> indukcijom po $|S|$. Za $S = \emptyset$ to su bridovi stabla. Neka tvrdnja vrijedi prije brisanja vrha $v$ i neka su $x, y \ne v$ preostali. Postojeći bridovi se ne brišu, a put $x \to y$ ne dobiva nove neeliminirane unutarnje vrhove, pa stari bridovi i dalje zadovoljavaju tvrdnju. Novi brid nastaje samo između susjeda $x, y$ od $v$: po pretpostavci su svi unutarnji vrhovi puteva $x \to v$ i $v \to y$ u $S$. Spoj tih dvaju puteva je šetnja od $x$ do $y$ kroz $v$; put $x \to y$ u stablu dobiva se iz nje izbacivanjem ponovljenog dijela, pa su svi njegovi unutarnji vrhovi među unutarnjim vrhovima te šetnje, dakle u $S \cup \{v\}$. Obrat: neka su svi unutarnji vrhovi puta $x \to y$ u $S \cup \{v\}$. Ako $v$ nije na putu, $x$ i $y$ su bili susjedni već prije. Ako jest, dijelovi $x \to v$ i $v \to y$ imaju sve unutarnje vrhove u $S$, pa su $x$ i $y$ susjedi od $v$ i operacija ih spaja. Višestruki bridovi ne utječu na relaciju susjedstva. $\square$</p>
<p>Zadatak također jamči da redoslijed brisanja unutar jedne operacije nije bitan – u skladu s lemom, jer ona ovisi samo o skupu $S$.</p>
<h3>2. Uvjet valjanosti jedne operacije</h3>
<p>Odabrani vrhovi moraju biti nesusjedni u trenutnom grafu. Po Lemi 1: za svaka dva odabrana $x, y$ na putu $x \to y$ u stablu mora postojati vrh koji <em>još nije izbrisan</em> (prije te operacije).</p>
<h3>3. Centroidna dekompozicija i razine</h3>
<p>Centroid komponente veličine $t$ je vrh čijim uklanjanjem sve preostale komponente imaju veličinu $\le t/2$ (uvijek postoji: krećemo od bilo kojeg vrha i spuštamo se u dijete s podstablom $\gt t/2$ dok takvog ima). Rekurzivno: centroid $c$ cijelog stabla dobiva razinu $0$, uklonimo ga i svaku nastalu komponentu obradimo s razinom $+1$. Dobivamo <em>centroidno stablo</em>; razina vrha je njegova dubina u njemu. Kako se veličina komponente barem polovi, razina je $\le \lfloor \log_2 n \rfloor$; za $n \le 500$ niz veličina je $500 \to 250 \to 125 \to 62 \to 31 \to 15 \to 7 \to 3 \to 1$, dakle najviše $9$ razina ($0..8$).</p>
<p><strong>Lema 2.</strong> Ako su $x \ne y$ iste razine $\ell$, postoji vrh razine $\lt \ell$ na putu $x \to y$. <em>Dokaz.</em> Neka je $c$ najbliži zajednički predak $x$ i $y$ u centroidnom stablu; $c \ne x, y$ (inače bi im razine bile različite), pa je razina $c$ manja od $\ell$. Kad je $c$ postao centroid, $x$ i $y$ bili su u njegovoj komponenti (povezanom podstablu), a nakon uklanjanja $c$ završili su u različitim komponentama. Put $x \to y$ unutar te komponente stoga prolazi kroz $c$. $\square$</p>
<h3>4. Redoslijed operacija</h3>
<p>Operacija $i$ briše sve vrhove razine $L - i$ ($i = 1..L$, $L$ = broj razina). Kad brišemo razinu $\ell$, izbrisani su samo vrhovi razina $\gt \ell$; po Lemi 2 između svaka dva vrha razine $\ell$ leži vrh manje razine koji je prisutan, pa po Lemi 1 nisu susjedni – operacija je valjana. Nakon $L \le 9 \le 10$ operacija svi su vrhovi izbrisani. Primjer iz zadatka ima $n = 5$: centroid je $1$ (razina $0$), zatim $4$ (razina $1$) i $5$ (razina $2$) te $2, 3$ (razina $1$); izlaz s $3$ operacije $\{5\}, \{4, 2, 3\}, \{1\}$ je valjan (službeni primjer koristi drugi valjani niz).</p>
<h3>5. Složenost i provjera</h3>
<p>Dekompozicija je $O(n \log n)$ (u kodu se veličine računaju iznova po komponenti, što je i za $n = 500$ trenutno). Ispravnost izlaza provjerava se checkerom koji simulira operacije: vrhovi postoje i različiti su, nijedan par nije susjedan, brisanje spaja sve susjede, na kraju nema vrhova i operacija je $\le 10$.</p>
''',
    'verified': r'''uzorci 1/1, 300 slučajnih testova provjereno checkerom, 3 velikih testova (najviše 0.00 s).''',
},
]
