# -*- coding: utf-8 -*-
STAGE = {
    'no': 9,
    'name': 'Stage 9: Qingdao',
    'source_name': 'March 25-26, 2023',
    'no_editorial': True,
    'community': True,
    'source_html': r'''
<p>Zadaci potječu s natjecanja The 2018 ICPC Asia Qingdao Regional Contest. Tekst zadatka preveden je prema službenim <a href="https://contest.ucup.ac/download.php?type=attachments&amp;id=1187&amp;r=1">engleskim tekstovima zadataka</a>. Organizatori nisu objavili službena rješenja. Zadatak je dostupan na <a href="https://contest.ucup.ac/contest/1187">Universal Cup Judging System</a>.</p>
''',
}

PROBLEMS = [
# ---------------------------------------------------------------- A
{
    'letter': 'A', 'title': 'Sequence and Sequence', 'title_hr': 'Niz i niz', 'slug': 'A_sequence_and_sequence',
    'tl': '10 s', 'ml': '256 MiB',
    'statement': r'''
<p>Niz $P$ je sortiran niz u kojem se svaki pozitivan cijeli broj $k$ pojavljuje točno $k + 1$ puta: $P = \{1, 1, 2, 2, 2, 3, 3, 3, 3, 4, \dots\}$. Niz $Q$ zadan je s $Q(1) = 1$ i $Q(i) = Q(i-1) + Q(P(i))$ za $i \gt 1$: $Q = \{1, 2, 4, 6, 8, 12, 16, 20, 24, 30, 36, 42, 48, 54, 62, \dots\}$.</p>
<p>Za dani $n$ izračunaj $Q(n)$.</p>
<h3>Ulaz</h3>
<p>$T \approx 10^4$ testova; u svakom jedan broj $n$, $1 \le n \le 10^{40}$.</p>
<h3>Izlaz</h3>
<p>Za svaki test $Q(n)$.</p>
<h3>Primjer</h3>
<p>$Q(10) = 30$, $Q(100) = 2522$, $Q(1000) = 244274$, $Q(987654321123456789) = 235139898689017607381017686096176798$.</p>
''',
    'hints': [
        r'''
<p>Zapiši $Q(n) = \sum_{i=1}^{n} Q(P(i))$ i grupiraj pribrojnike po vrijednosti $P(i) = k$: to su indeksi $i \in [T_k, T_{k+1} - 1]$, $T_k = \frac{k(k+1)}{2}$. Koliko je $P(n)$ u odnosu na $n$?</p>
''',
        r'''
<p>$P(n) \approx \sqrt{2n}$, pa se već nakon četiri „skoka” $n \le 10^{40}$ smanji na $\approx 600$. Poopći: $g(f, n) = \sum_{i \le n} f(i)\, Q(P(i))$ za polinom $f$ i primijeni Abelovu (parcijalnu) sumaciju da dobiješ $g(f, n) = F(n)\, Q(P(n)) - g(f', P(n))$ s novim polinomom $f'$.</p>
''',
        r'''
<p>$F(x) = \sum_{i \le x} f(i)$ je polinom stupnja $\deg f + 1$, a $f'(k) = F(T_k - 1)$ polinom stupnja $2\deg F$. Stupnjevi su $1, 3, 7, 15, 31$ – mali. Evaluiraj polinome Lagrangeovom interpolacijom iz vrijednosti u $0..\deg$ u točnoj velikoj aritmetici.</p>
''',
    ],
    'coach': [
        ('Kako se rekurzija za $Q$ pretvara u zbroj i zašto $P(n)$ tako brzo pada?',
         r'''
<p>Iz $Q(i) - Q(i-1) = Q(P(i))$ i $Q(1) = 1 = Q(P(1))$ slijedi $Q(n) = \sum_{i=1}^{n} Q(P(i))$. $P(n)$ je najveći $k$ s $T_k = \frac{k(k+1)}{2} \le n$, dakle $P(n) \approx \sqrt{2n}$: iz $10^{40}$ dobivamo $\approx 1.4 \cdot 10^{20}$, pa $1.7 \cdot 10^{10}$, pa $1.8 \cdot 10^5$, pa $\approx 600$. Cilj je izraziti $Q(n)$ preko vrijednosti u $P(n)$, i tako dalje do malih argumenata koje predračunamo.</p>
'''),
        ('Kako Abelova sumacija svodi $g(f, n) = \\sum_{i \\le n} f(i) Q(P(i))$ na $P(n)$?',
         r'''
<p>Neka je $K = P(n)$, $F(x) = \sum_{i=1}^{x} f(i)$ i $h(k) = F(T_k - 1)$. Grupiranjem po $P(i) = k$: $g(f, n) = \sum_{k=1}^{K-1} Q(k)\,[h(k+1) - h(k)] + Q(K)\,[F(n) - h(K)]$. Parcijalnom sumacijom ($\sum Q(k)(h(k+1) - h(k)) = Q(K-1)h(K) - Q(1)h(1) - \sum_{k=2}^{K-1} (Q(k) - Q(k-1)) h(k)$, uz $h(1) = F(0) = 0$ i $Q(k) - Q(k-1) = Q(P(k))$) dobivamo $$g(f, n) = F(n)\, Q(K) - \sum_{k=1}^{K} h(k)\, Q(P(k)) = F(n)\, g(1, K) - g(h, K).$$ Dakle $g$ s težinom $f$ na $n$ izražava se preko $g$ s težinama $1$ i $h$ na $K = P(n)$.</p>
'''),
        ('Zašto su sve težine polinomi malog stupnja i kako ih evaluirati u točkama do $10^{40}$?',
         r'''
<p>Krenemo s $f^{(0)} = 1$. Prefiksna suma polinoma stupnja $d$ je polinom stupnja $d + 1$ (Faulhaber), a $f^{(d+1)}(k) = F^{(d)}(T_k - 1)$ je kompozicija s kvadratnim polinomom: stupanj se udvostručuje. Stupnjevi $F^{(d)}$ su $1, 3, 7, 15, 31, \dots$ ($2^{d+1} - 1$). Polinom stupnja $D$ s cjelobrojnim vrijednostima zadajemo vrijednostima u $0, 1, \dots, D$ i evaluiramo Lagrangeovom formulom $F(x) = \frac{1}{D!} \sum_{i} (-1)^{D-i} \binom{D}{i} y_i \prod_{j \ne i} (x - j)$; sve je cjelobrojno, pa radimo u vlastitoj velikoj aritmetici (brojevi imaju do $\approx 40 \cdot 31$ znamenki).</p>
'''),
        ('Kako izgleda cijeli postupak za jedan upit i zašto je dovoljno brz?',
         r'''
<p>Izgradimo lanac $n_0 = n$, $n_{l+1} = P(n_l)$ dok $n_L \le 2000$ ($L \le 4$). Za $n \le 2000$ predračunamo tablice $S_d(n) = g(f^{(d)}, n)$ za $d \le 5$. Zatim od dna prema vrhu: $G_d(n_l) = F^{(d)}(n_l)\, G_0(n_{l+1}) - G_{d+1}(n_{l+1})$ za $d = 0..l$; odgovor je $G_0(n_0)$. Po upitu je to $O(L^2)$ evaluacija polinoma stupnja $\le 15$ na brojevima od $\approx 40$ znamenki plus računanje $P$ (procjena korijenom u <code>long double</code> i korekcija za $\pm$ nekoliko): $10^4$ upita prolazi u dijelu sekunde.</p>
'''),
    ],
    'tips': [
        r'''Rekurzije oblika $Q(n) = \sum_{i \le n} Q(P(i))$ s $P(n) \ll n$ rješavaj „skokovima”: izrazi vrijednost u $n$ preko vrijednosti u $P(n)$ pa nastavi – broj skokova je logaritamski ili bolji.''',
        r'''Abelova (parcijalna) sumacija $\sum a_k (h_{k+1} - h_k) = a_K h_K - \sum (a_k - a_{k-1}) h_k$ pretvara težinu iz „razlike” u „prirast” niza – ovdje $Q(k) - Q(k-1) = Q(P(k))$ vraća isti oblik zbroja.''',
        r'''Polinom s cjelobrojnim vrijednostima čuvaj kao vrijednosti u $0..D$; Lagrangeova formula s nazivnikom $D!$ daje egzaktnu cjelobrojnu evaluaciju bez racionalnih brojeva.''',
        r'''Kad su ulazi do $10^{40}$, napiši mali razred za velike brojeve (baza $10^9$, zbrajanje, množenje, dijeljenje malim brojem) i testiraj ga zasebno na Pythonu.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi): $Q(n) = \sum_{i \le n} Q(P(i))$, a $P(n) \approx \sqrt{2n}$. Za polinomsku težinu $f$ definiramo $g(f, n) = \sum_{i \le n} f(i)\, Q(P(i))$; grupiranjem po $P(i) = k$ i Abelovom sumacijom slijedi $g(f, n) = F(n)\, g(1, P(n)) - g(f', P(n))$, gdje je $F$ prefiksna suma od $f$ i $f'(k) = F\!\left(\frac{k(k+1)}{2} - 1\right)$. Težine $f^{(0)} = 1, f^{(1)}, \dots$ su polinomi stupnja $0, 2, 6, 14, 30$ ($F^{(d)}$ stupnja $2^{d+1}-1$); lanac $n \to P(n) \to \dots$ nakon $\le 4$ koraka padne pod $2000$, gdje su $g(f^{(d)}, n)$ predračunati. Polinome čuvamo kao vrijednosti u $0..\deg$ i evaluiramo Lagrangeom u točnoj velikoj aritmetici. Složenost po upitu $O(L^2 \cdot \deg \cdot M)$ s $L \le 4$, gdje je $M$ cijena operacije na velikim brojevima.</p>
''',
    'detailed': r'''
<h3>1. Oblik zbroja i brzina opadanja</h3>
<p>Niz $P$ sadrži $k$ točno $k + 1$ puta, pa je $P(i) = k$ za $i \in [T_k, T_{k+1} - 1]$, $T_k = \frac{k(k+1)}{2}$; dakle $P(n)$ je najveći $k$ s $T_k \le n$, $P(n) = \lfloor (\sqrt{8n + 1} - 1)/2 \rfloor \approx \sqrt{2n}$. Iz rekurzije $Q(i) = Q(i-1) + Q(P(i))$ i $Q(1) = 1 = Q(P(1))$ slijedi teleskopiranjem $$Q(n) = \sum_{i=1}^{n} Q(P(i)).$$ Za $n \le 10^{40}$ lanac $n, P(n), P(P(n)), \dots$ glasi približno $10^{40} \to 1.4 \cdot 10^{20} \to 1.7 \cdot 10^{10} \to 1.8 \cdot 10^{5} \to 6 \cdot 10^{2}$, dakle nakon četiri koraka ulazimo u područje koje možemo predračunati.</p>
<h3>2. Poopćeni zbroj i Abelova sumacija</h3>
<p>Za funkciju $f$ na pozitivnim cijelim brojevima definiramo $g(f, n) = \sum_{i=1}^{n} f(i)\, Q(P(i))$, tako da je $Q(n) = g(1, n)$. Neka je $K = P(n)$, $F(x) = \sum_{i=1}^{x} f(i)$ ($F(0) = 0$) i $h(k) = F(T_k - 1)$ (zbroj $f$ po svim indeksima s $P(i) < k$). Grupiranjem po vrijednosti $P(i) = k$:</p>
<p>$$g(f, n) = \sum_{k=1}^{K-1} Q(k)\,\big[h(k+1) - h(k)\big] + Q(K)\,\big[F(n) - h(K)\big].$$</p>
<p><strong>Lema (Abelova sumacija).</strong> $\sum_{k=1}^{K-1} Q(k)\,[h(k+1) - h(k)] = Q(K-1)\,h(K) - Q(1)\,h(1) - \sum_{k=2}^{K-1} [Q(k) - Q(k-1)]\, h(k)$. <em>Dokaz.</em> Raspišemo $\sum_{k=1}^{K-1} Q(k)h(k+1) = \sum_{k=2}^{K} Q(k-1)h(k)$ i oduzmemo $\sum_{k=1}^{K-1} Q(k)h(k)$; članovi za $k = 2..K-1$ daju $-(Q(k) - Q(k-1))h(k)$, a rubni članovi $Q(K-1)h(K)$ i $-Q(1)h(1)$. $\square$</p>
<p>Uvrstimo $h(1) = F(T_1 - 1) = F(0) = 0$ i $Q(k) - Q(k-1) = Q(P(k))$, te dodamo posljednji pribrojnik $Q(K)F(n) - Q(K)h(K)$: $Q(K-1)h(K) - Q(K)h(K) = -Q(P(K))h(K)$, pa je</p>
<p>$$g(f, n) = F(n)\, Q(K) - \sum_{k=1}^{K} h(k)\, Q(P(k)) = F(n)\, g(1, K) - g(h, K)$$</p>
<p>(član $k = 1$ u zbroju je $h(1)Q(P(1)) = 0$, pa ga smijemo uključiti). Ovo je ključna redukcija: vrijednost s argumentom $n$ izražena je preko dviju vrijednosti s argumentom $K = P(n) \approx \sqrt{2n}$.</p>
<h3>3. Familija težina</h3>
<p>Definiramo $f^{(0)} = 1$, $F^{(d)}(x) = \sum_{i=1}^{x} f^{(d)}(i)$ i $f^{(d+1)}(k) = F^{(d)}(T_k - 1)$. Tada za $g_d(n) := g(f^{(d)}, n)$ vrijedi</p>
<p>$$g_d(n) = F^{(d)}(n)\, g_0(P(n)) - g_{d+1}(P(n)).$$</p>
<p><strong>Tvrdnja.</strong> $f^{(d)}$ i $F^{(d)}$ su polinomi s cjelobrojnim vrijednostima, $\deg F^{(d)} = 2^{d+1} - 1$. <em>Dokaz</em> indukcijom: prefiksna suma polinoma stupnja $e$ je polinom stupnja $e + 1$ (Faulhaberove formule; slijedi iz toga što je operator diferencije $\Delta F = f$ invertibilan na polinomima uz $F(0) = 0$), a kompozicija s $T_k - 1$ (stupanj $2$) udvostručuje stupanj. Iz $\deg f^{(0)} = 0$: $\deg F^{(0)} = 1$, $\deg f^{(1)} = 2$, $\deg F^{(1)} = 3$, $\deg f^{(2)} = 6$, $\deg F^{(2)} = 7$, $\deg F^{(3)} = 15$, $\deg F^{(4)} = 31$. Cjelobrojnost vrijednosti u cijelim točkama očita je iz definicija kao zbrojeva i kompozicija. Polinom stupnja $D$ koji je polinom i za negativne cijele argumente $T_k - 1$ (npr. $T_0 - 1 = -1$) i dalje daje cijele vrijednosti jer je $D$-ta razlika konstantna. $\square$</p>
<h3>4. Predstavljanje i evaluacija polinoma</h3>
<p>Polinom $F^{(d)}$ stupnja $D$ čuvamo vrijednostima $y_0, \dots, y_D$ u točkama $0, \dots, D$ (dobivenima izravnim zbrajanjem $f^{(d)}(i)$, a $f^{(d)}(i)$ evaluacijom prethodnog $F^{(d-1)}$ u $T_i - 1$). Evaluacija u velikom $x$ Lagrangeovom formulom s čvorovima $0..D$: $\prod_{j \ne i}(i - j) = i!\,(D-i)!\,(-1)^{D-i}$, pa je</p>
<p>$$F(x) = \frac{1}{D!} \sum_{i=0}^{D} (-1)^{D-i} \binom{D}{i}\, y_i \prod_{j \ne i} (x - j),$$</p>
<p>gdje umnoške $\prod_{j<i}(x-j)$ i $\prod_{j>i}(x-j)$ uzimamo iz prefiksnih i sufiksnih umnožaka. Zbroj je cijeli broj djeljiv s $D!$ (jer je $F(x)$ cijeli), pa dijelimo redom malim brojevima $2, \dots, D$ – točno, bez racionalnih brojeva. Sve radimo u vlastitom razredu velikih cijelih brojeva s predznakom (baza $10^9$: zbrajanje, oduzimanje, množenje $O(\ell_1 \ell_2)$, dijeljenje malim brojem). Veličina: $F^{(3)}(n)$ za $n \approx 10^{40}$ ima $\approx 600$ znamenki, umnošci u Lagrangeu $\approx 40 \cdot 16$ znamenki – zanemarivo.</p>
<h3>5. Računanje $P(n)$ za velike $n$</h3>
<p>Procijenimo $k \approx \sqrt{2n}$ u <code>long double</code> (relativna greška $\approx 10^{-19}$, dakle apsolutna $\lesssim 20$ za $k \approx 10^{20}$) i zatim korigiramo petljama „dok $T_k > n$: $k{-}{-}$” i „dok $T_{k+1} \le n$: $k{+}{+}$” u velikoj aritmetici. Broj korekcija je malen.</p>
<h3>6. Cijeli algoritam</h3>
<ol>
<li><em>Predračun.</em> $Q(i)$ i $P(i)$ za $i \le N_0 = 2000$; za $d = 0..5$: vrijednosti $f^{(d)}(i)$, tablica $F^{(d)}$ u $0..\deg$, i $S_d(n) = g_d(n) = \sum_{i \le n} f^{(d)}(i) Q(P(i))$ za $n \le N_0$.</li>
<li><em>Upit.</em> Lanac $n_0 = n$, $n_{l+1} = P(n_l)$ dok $n_L \le N_0$ ($L \le 4$). Postavi $G_d = S_d(n_L)$ za $d \le L$. Za $l = L-1, \dots, 0$: novi $G'_d = F^{(d)}(n_l)\, G_0 - G_{d+1}$ za $d = 0..l$. Odgovor $G_0$ na razini $0$.</li>
</ol>
<p>Na razini $l$ trebaju nam $g_d(n_l)$ za $d \le l$ (jer $g_0(n_0)$ traži $g_0, g_1$ na $n_1$, ti traže $g_0, g_1, g_2$ na $n_2$, itd.), pa je najveći potreban $d$ jednak $L \le 4$ i najveći evaluirani polinom $F^{(3)}$ (stupanj 15) na $n_0$; tablice do $d = 5$ daju rezervu. Za $n \le N_0$ odgovor je izravno $S_0(n)$.</p>
<h3>7. Složenost</h3>
<p>Predračun: $O(N_0 \cdot D_{\max} \cdot M)$, gdje je $M$ cijena operacije na brojevima s nekoliko stotina znamenki – trenutno. Po upitu: $\le 4$ računanja $P$ i $\le 10$ evaluacija polinoma stupnja $\le 15$, svaka $O(D)$ velikih množenja: ukupno za $10^4$ upita ispod $0.5$ s.</p>
<h3>8. Zamke</h3>
<ul>
<li>$P(1) = 1$ (jer $T_1 = 1 \le 1$), pa je $Q(n) = \sum_{i \le n} Q(P(i))$ točno i za $i = 1$.</li>
<li>Vrijednosti $F^{(d)}(T_k - 1)$ za $k = 0$ traže evaluaciju u $-1$: polinomska formula vrijedi, ali <em>ne</em> smije se koristiti „zbroj do $-1$”.</li>
<li>Predznaci u Lagrangeu i u redukciji ($-g_{d+1}$) zahtijevaju velike brojeve s predznakom; završno dijeljenje s $D!$ mora biti egzaktno – dobra samoprovjera je ostatak $0$.</li>
<li>Granicu tablice ($N_0$) treba uskladiti s dubinom: uz $N_0 = 2000$ i $n \le 10^{40}$ dubina je $\le 4$; implementaciju vrijedi testirati i s umjetno malom granicom (npr. $12$) da se rekurzija dublje „istrese” na malim $n$ usporedivima s brute forceom.</li>
</ul>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n \le 2 \cdot 10^5$) protiv brute forcea koji izravno računa niz $Q$ (Python); 3 velika testa s $T = 10^4$ i $n$ do $10^{40}$ (najviše $0.39$ s); dodatno ista C++ implementacija prevedena s tablicom smanjenom na $12$ (lanac $P$ ide u dubinu do $5$, pa se koriste i polinomi $F^{(4)}$) uspoređena s brute forceom na $n \le 2 \cdot 10^5$ i s običnom verzijom na 300 slučajnih $n \le 10^{40}$.''',
},
# ---------------------------------------------------------------- B
{
    'letter': 'B', 'title': 'Kawa Exam', 'title_hr': 'Ispit iz Kawe', 'slug': 'B_kawa_exam',
    'tl': '3 s', 'ml': '512 MiB',
    'statement': r'''
<p>Ispit ima $n$ pitanja s jednim točnim odgovorom $a_i$ (od $10^5$ ponuđenih). Sustav ima $m$ grešaka; $i$-ta greška $(u_i, v_i)$ znači da BaoBao na pitanja $u_i$ i $v_i$ mora dati isti odgovor (i kad je pogrešan). Programeri stignu popraviti samo jednu grešku.</p>
<p>Za svaku grešku $i = 1..m$ odredi najveći broj pitanja koje BaoBao može točno odgovoriti ako se popravi upravo $i$-ta greška (ostale ostaju na snazi).</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n, m \le 10^5$, $1 \le a_i \le 10^5$, zatim $m$ parova $u_i, v_i$ (mogu se ponavljati, može $u_i = v_i$); $\sum n, \sum m \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test jedan redak s $m$ brojeva $c_1, \dots, c_m$ razdvojenih razmakom (bez razmaka na kraju).</p>
<h3>Primjer</h3>
<p>$a = (1, 2, 1, 2, 1, 2, 1)$, greške $(1,2), (1,3), (2,4), (5,6), (5,7)$: <code>6 5 5 5 4</code>. $a = (1, 2, 3)$, greške $(1,2), (1,3), (2,3)$: <code>1 1 1</code>. $a = (12345, 54321)$, greške $(1,2), (1,2)$: <code>1 1</code> — popravkom jedne kopije greške druga i dalje vrijedi.</p>
''',
    'hints': [
        r'''
<p>Greške su bridovi grafa na pitanjima. Sva pitanja iste komponente povezanosti moraju dobiti isti odgovor, pa komponenta pridonosi točno onoliko koliko puta se u njoj pojavljuje najčešća vrijednost (mod).</p>
''',
        r'''
<p>Uklanjanje brida mijenja komponente samo ako je brid <em>most</em>. Za most koji u DFS stablu vodi u dijete $v$ komponenta se raspada na podstablo od $v$ i ostatak. Trebaju ti modovi svih podstabala i svih „komplemenata podstabla unutar komponente”.</p>
''',
        r'''
<p>Modove podstabala računaj tehnikom DSU na stablu (sack): u jednom prolazu održavaj multiskup podstabla i istodobno multiskup komplementa (sve što dodaš u prvi, makni iz drugog). Mod se održava u $O(1)$ brojačem „koliko vrijednosti ima brojnost $c$”.</p>
''',
    ],
    'coach': [
        ('Koliko pitanja BaoBao može točno odgovoriti uz fiksan skup grešaka?',
         r'''
<p>Uvjet „isti odgovor na $u$ i $v$” je tranzitivan preko lanaca grešaka, pa sva pitanja u istoj komponenti povezanosti grafa grešaka dobivaju isti odgovor $x$. Točnih je u komponenti onoliko koliko pitanja ima $a_i = x$, što je najveće kad je $x$ najčešća vrijednost: doprinos komponente je njezin mod (brojnost najčešće vrijednosti). Odgovor je zbroj modova komponenata; nazovimo ga $B$.</p>
'''),
        ('Koji bridovi uopće mijenjaju $B$ kad ih uklonimo?',
         r'''
<p>Ako brid nije most, njegovo uklanjanje ne mijenja komponente (krajevi ostaju povezani drugim putem), pa je $c_i = B$. To pokriva i višestruke bridove i petlje $u = v$. Ako je most, njegova komponenta $K$ raspada se na dva dijela $K_1, K_2$ i $c_i = B - \mathrm{mod}(K) + \mathrm{mod}(K_1) + \mathrm{mod}(K_2)$. Mostove nalazimo Tarjanovim algoritmom ($\mathrm{low}[v] > \mathrm{tin}[u]$ za stablasti brid $u \to v$), pri čemu preskačemo <em>brid</em> prema roditelju po identifikatoru, a ne roditeljski vrh, kako bi paralelni bridovi bili ispravno prepoznati kao ne-mostovi.</p>
'''),
        ('Kako izgledaju $K_1$ i $K_2$ i kako izračunati modove svih takvih parova?',
         r'''
<p>Most je uvijek brid DFS stabla; ako vodi od roditelja u dijete $v$, tada je $K_1 = $ podstablo od $v$ (u DFS stablu), a $K_2 = K \setminus K_1$. Modovi podstabala standardno se dobivaju tehnikom DSU na stablu (sack): za vrh $v$ prvo obradimo laku djecu i ispraznimo strukturu, zatim teško dijete čiji sadržaj zadržimo, pa dodamo $v$ i cijela podstabla lake djece. Svaki se vrh dodaje $O(\log n)$ puta (jednom po lakom bridu na putu do korijena). Trik za komplemente: držimo dvije strukture, $S_1$ (trenutno podstablo) i $S_2$ (komponenta bez $S_1$); svaka operacija „dodaj u $S_1$” prati se s „makni iz $S_2$” i obrnuto, pa je u trenutku kad $S_1$ = podstablo od $v$ automatski $S_2 = K \setminus \text{podstablo}(v)$.</p>
'''),
        ('Kako održavati mod multiskupa uz umetanje i brisanje u $O(1)$?',
         r'''
<p>Osim brojača $\mathrm{cnt}[x]$ držimo $\mathrm{freq}[c]$ = broj vrijednosti s brojnošću točno $c$. Pri umetanju $x$ brojnost raste s $c$ na $c+1$ i mod postaje $\max(\mathrm{mod}, c+1)$. Pri brisanju brojnost pada s $c$ na $c-1$; ako je $c$ bio mod i $\mathrm{freq}[c]$ postane $0$, mod pada na $c - 1$ (ne može pasti više jer se mod mijenja za najviše $1$ po operaciji). Ukupno $O((n + m) \log n)$ po testu, što uz $\sum n, \sum m \le 10^6$ prolazi u limitu.</p>
'''),
    ],
    'tips': [
        r'''„Za svaki brid: što ako ga uklonimo?” – prvo provjeri je li most; ne-mostovi ne mijenjaju povezanost, a mostovi su bridovi DFS stabla pa dijele komponentu na podstablo i ostatak.''',
        r'''DSU na stablu (sack) daje odgovore za sva podstabla u $O(n \log n)$; za komplemente drži drugu, „zrcalnu” strukturu koja uvijek sadrži ostatak komponente.''',
        r'''Mod (najčešća brojnost) održava se u $O(1)$ po operaciji brojačem $\mathrm{freq}[c]$, jer se mod mijenja za najviše $1$.''',
        r'''Za $n$ do $10^5$ i puno testova piši Tarjana i sack iterativno (ili povećaj stog) – rekurzija po lancu od $10^5$ vrhova zna srušiti program.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi): greške su bridovi, sva pitanja iste komponente dobivaju isti odgovor, pa je osnovni rezultat $B = \sum$ modova komponenata (mod = brojnost najčešće vrijednosti). Uklanjanje brida koji nije most ne mijenja ništa ($c_i = B$); most $u \to v$ u DFS stablu dijeli komponentu $K$ na podstablo $v$ i ostatak, pa je $c_i = B - \mathrm{mod}(K) + \mathrm{mod}(\text{sub}(v)) + \mathrm{mod}(K \setminus \text{sub}(v))$. Mostove nađemo Tarjanom, a modove svih podstabala i komplemenata jednim prolazom DSU na stablu (sack) s dvije zrcalne strukture (podstablo / ostatak komponente) uz $O(1)$ održavanje moda brojačem $\mathrm{freq}[c]$. Složenost $O((n + m)\log n)$.</p>
''',
    'detailed': r'''
<h3>1. Osnovni odgovor</h3>
<p>Napravimo graf s vrhovima $1..n$ (pitanja) i bridovima $(u_i, v_i)$. Ako su $u$ i $v$ povezani putem grešaka, indukcijom po duljini puta imaju isti odgovor; obratno, pitanja u različitim komponentama su nezavisna. Za komponentu $K$ s odabranim odgovorom $x$ točno je $|\{i \in K : a_i = x\}|$ pitanja, maksimalno za najčešći $x$: $\mathrm{mod}(K)$. Dakle bez ikakvih popravaka najveći rezultat je $B = \sum_K \mathrm{mod}(K)$.</p>
<h3>2. Uklanjanje jednog brida</h3>
<p><strong>Tvrdnja.</strong> Ako brid $e$ nije most, uklanjanje ne mijenja skup komponenata, pa je $c_e = B$. Ako je most, njegova komponenta $K$ raspada se na točno dvije komponente $K_1, K_2$ i $c_e = B - \mathrm{mod}(K) + \mathrm{mod}(K_1) + \mathrm{mod}(K_2)$. To je po definiciji mosta. Petlje ($u = v$) i paralelni bridovi nisu mostovi.</p>
<p>Mostove nalazimo Tarjanovim algoritmom: DFS s vremenima ulaska $\mathrm{tin}$ i $\mathrm{low}[v] = \min$ od $\mathrm{tin}$ vrhova dosegnutih iz podstabla $v$ jednim povratnim bridom; stablasti brid $u \to v$ je most točno kad $\mathrm{low}[v] > \mathrm{tin}[u]$. Da paralelni bridovi budu ispravno tretirani, pri obilasku preskačemo samo brid s istim <em>identifikatorom</em> kao roditeljski, a ne sve bridove prema roditelju. Petlja $v \to v$ daje $\mathrm{low}[v] \le \mathrm{tin}[v]$, što ništa ne mijenja.</p>
<h3>3. Što su $K_1$ i $K_2$</h3>
<p>Most je nužno brid DFS stabla (povratni brid zatvara ciklus). Ako most vodi od roditelja $u$ u dijete $v$, uklanjanjem se odvaja podstablo $\text{sub}(v)$: svi vrhovi iz $\text{sub}(v)$ ostaju povezani stablastim bridovima, a nijedan povratni brid ne izlazi iz $\text{sub}(v)$ iznad $u$ (inače $\mathrm{low}[v] \le \mathrm{tin}[u]$). Dakle $K_1 = \text{sub}(v)$, $K_2 = K \setminus \text{sub}(v)$. Treba nam $\mathrm{mod}(\text{sub}(v))$ i $\mathrm{mod}(K \setminus \text{sub}(v))$ za svaki vrh $v$ koji nije korijen.</p>
<h3>4. Multiskup s modom u $O(1)$</h3>
<p>Struktura drži $\mathrm{cnt}[x]$ (brojnost vrijednosti $x$), $\mathrm{freq}[c]$ (koliko vrijednosti ima brojnost $c$) i $\mathrm{mod}$. Umetanje $x$: $\mathrm{freq}[c]{-}{-}$, $\mathrm{cnt}[x] = c + 1$, $\mathrm{freq}[c+1]{+}{+}$, $\mathrm{mod} = \max(\mathrm{mod}, c+1)$. Brisanje: simetrično, i ako je $c = \mathrm{mod}$ te $\mathrm{freq}[c]$ postane $0$, onda $\mathrm{mod} \leftarrow c - 1$. Ispravnost: brisanje jednog elementa smanjuje najveću brojnost za najviše $1$, a $\mathrm{freq}[c] = 0$ znači da više nitko nema brojnost $c$ (veće brojnosti od moda ne postoje).</p>
<h3>5. DSU na stablu s dvije zrcalne strukture</h3>
<p>Za korijen komponente $r$ napunimo $S_2$ svim vrijednostima iz $K$, a $S_1$ je prazan. Definiramo <code>dodaj(x)</code> = ($S_1$.umetni $x$, $S_2$.izbriši $x$) i <code>makni(x)</code> obrnuto; tako je uvijek $S_1 \uplus S_2 = K$. Sack obilazak vrha $v$:</p>
<ol>
<li>za svako <em>lako</em> dijete $c$: obradi $c$ rekurzivno, zatim <code>makni</code> sve vrhove iz $\text{sub}(c)$ (raspon u Eulerovom poretku);</li>
<li>obradi <em>teško</em> dijete (najvećeg podstabla) i <em>zadrži</em> njegov sadržaj;</li>
<li><code>dodaj</code>($a_v$) i <code>dodaj</code> sva podstabla lake djece; sada je $S_1 = \text{sub}(v)$ i $S_2 = K \setminus \text{sub}(v)$, pa zapiši $\mathrm{modSub}[v] = S_1.\mathrm{mod}$, $\mathrm{modComp}[v] = S_2.\mathrm{mod}$.</li>
</ol>
<p><strong>Složenost.</strong> Vrh $w$ se dodaje/miče u koracima 1 i 3 samo za pretke $v$ takve da $w$ leži u lakom podstablu djeteta od $v$; na putu od $w$ do korijena ima $O(\log n)$ lakih bridova (svaki bar udvostručuje veličinu podstabla), pa je ukupno $O(n \log n)$ operacija po $O(1)$.</p>
<h3>6. Sastavljanje odgovora</h3>
<p>$B = \sum_r \mathrm{modSub}[r]$ po korijenima. Za brid $i$: ako nije most, $c_i = B$; ako je most s djetetom $v$ u komponenti s korijenom $r$, $c_i = B - \mathrm{modSub}[r] + \mathrm{modSub}[v] + \mathrm{modComp}[v]$. Primjer 1: $a = (1,2,1,2,1,2,1)$, greške $(1,2),(1,3),(2,4),(5,6),(5,7)$: komponente $\{1,2,3,4\}$ (mod $2$) i $\{5,6,7\}$ (mod $2$), $B = 4$. Sve su greške mostovi; uklanjanje $(1,2)$ daje $\{1,3\}$ (mod 2), $\{2,4\}$ (mod 2): $4 - 2 + 4 = 6$. Ostali daju $5, 5, 5, 4$.</p>
<h3>7. Zamke i implementacija</h3>
<ul>
<li>Rekurzivni DFS po lancu od $10^5$ vrhova može prepuniti stog: Tarjan i sack pišemo iterativno, s eksplicitnim okvirima (faza obrade).</li>
<li>Roditeljski brid preskačemo po identifikatoru (paralelni bridovi nisu mostovi).</li>
<li>Vrijednosti $a_i \le 10^5$: $\mathrm{cnt}$ je niz, ne mapa; $\mathrm{freq}$ mora imati veličinu $n + 2$ i početno $\mathrm{freq}[0]$ = „mnogo” da dekrement pri prvom umetanju ne ode u minus (brojnost $0$ se ne koristi za mod).</li>
<li>Nakon svake komponente očisti obje strukture (ukloni vrijednosti), da sljedeća komponenta ili sljedeći test krenu od praznog stanja.</li>
<li>Izlaz: $m$ brojeva u retku bez razmaka na kraju; skupljaj u string.</li>
</ul>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n \le 7$, $m \le 8$, vrijednosti $\le 3$, s petljama i višestrukim bridovima) protiv brute forcea koji za svaki brid zasebno računa komponente i modove; 3 velika testa s $n = m = 10^5$ (dugi lanac, slučajno stablo s dodatnim bridovima, potpuno slučajan graf; najviše $0.05$ s).''',
},
# ---------------------------------------------------------------- C
{
    'letter': 'C', 'title': 'Flippy Sequence', 'title_hr': 'Preokretni niz', 'slug': 'C_flippy_sequence',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Dani su binarni nizovi $s$ i $t$ duljine $n$. Operacija: odaberi $1 \le l \le r \le n$ i invertiraj $s_l, \dots, s_r$. Operaciju treba izvesti <em>točno dvaput</em> tako da nakon toga bude $s = t$.</p>
<p>Prebroji uređene četvorke $(a_1, a_2, a_3, a_4)$ — prva operacija $[a_1, a_2]$, druga $[a_3, a_4]$ — koje to postižu; četvorke su različite ako se razlikuju u bilo kojoj komponenti.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^6$ i stringovi $s$, $t$; $\sum n \le 10^7$.</p>
<h3>Izlaz</h3>
<p>Za svaki test broj načina.</p>
<h3>Primjer</h3>
<p>$s = 1, t = 0 \to 0$. $s = 00, t = 11 \to 2$ (četvorke $(1,1,2,2)$ i $(2,2,1,1)$). $s = 01010, t = 00111 \to 6$.</p>
''',
    'hints': [
        r'''
<p>Operacija „preokreni interval” djeluje na oba niza jednako pa promatraj samo razliku $d_i = s_i \oplus t_i$. Cilj je dvama preokretima $d$ pretvoriti u sve nule. Kako izgleda skup pozicija koje promijene vrijednost kad se dva intervala preokrenu?</p>
''',
        r'''
<p>Simetrična razlika dvaju intervala sastoji se od najviše dva bloka jedinica. Dakle, ako $d$ ima tri ili više maksimalnih blokova jedinica, odgovor je $0$. Preostaje prebrojati slučajeve $0$, $1$ i $2$ bloka.</p>
''',
        r'''
<p>Za nula blokova oba intervala moraju biti jednaka. Za jedan blok $[l, r]$ intervali su ili dva susjedna komada bloka, ili jedan sadrži drugi i dijele točno jedan rub. Za dva bloka postoje samo tri para intervala, svaki u dva poretka.</p>
''',
    ],
    'coach': [
        ('Zašto možemo zaboraviti $s$ i $t$ i gledati samo jedan niz?',
         r'''
<p>Preokretanje intervala u $s$ mijenja $s_i$ u $1 - s_i$, a to na razliku $d_i = s_i \oplus t_i$ djeluje jednako kao da smo preokrenuli isti interval u $d$. Uvjet „$s = t$ nakon operacija” glasi „$d$ je sve nule nakon operacija”. Dva preokreta intervala $[a_1, a_2]$ i $[a_3, a_4]$ na $d$ zapravo XOR-aju $d$ s karakterističnim vektorom simetrične razlike tih intervala, pa je uvjet: simetrična razlika $[a_1,a_2] \triangle [a_3,a_4]$ mora biti točno skup pozicija gdje je $d_i = 1$.</p>
'''),
        ('Kako izgleda simetrična razlika dvaju intervala?',
         r'''
<p>Ako su intervali disjunktni, razlika je njihova unija: dva bloka (ili jedan ako se dodiruju). Ako se preklapaju, razlika je unija dva „viška” lijevo i desno od presjeka: opet najviše dva bloka, a ako dijele rub onda jedan blok; jednaki intervali daju prazan skup. Dakle skup jedinica u $d$ mora imati $0$, $1$ ili $2$ maksimalna bloka, inače je odgovor $0$.</p>
'''),
        ('Koliko uređenih parova daje prazan skup, a koliko točno jedan blok $[l, r]$?',
         r'''
<p>Prazan skup nastaje jedino kad su intervali jednaki: $\frac{n(n+1)}{2}$ izbora. Za jedan blok $[l, r]$: ili su intervali dva susjedna komada $[l, k]$ i $[k+1, r]$ ($r - l$ rezova, po $2$ poretka), ili jedan interval pokriva blok i „viri” ulijevo pa drugi je taj višak $[l', l-1]$ ($l - 1$ izbora, $2$ poretka), ili simetrično udesno ($n - r$ izbora, $2$ poretka). Ukupno $2(r - l) + 2(l - 1) + 2(n - r) = 2(n - 1)$, neovisno o položaju bloka.</p>
'''),
        ('Zašto je za dva bloka odgovor uvijek $6$?',
         r'''
<p>Neka su blokovi $[l_1, r_1]$ i $[l_2, r_2]$ s $r_1 < l_2 - 1$. Rubovi simetrične razlike su točno rubovi intervala, pa su krajnje točke oba intervala među $l_1, r_1, l_2, r_2$. Mogućnosti kao neuređeni par: $\{[l_1, r_1], [l_2, r_2]\}$ (disjunktni), $\{[l_1, r_2], [r_1 + 1, l_2 - 1]\}$ (veliki i rupa), $\{[l_1, l_2 - 1], [r_1 + 1, r_2]\}$ (preklapanje točno na rupi). Svaki u $2$ poretka: $6$ načina.</p>
'''),
    ],
    'tips': [
        r'''Kad se ista operacija primjenjuje na dva objekta koje treba izjednačiti, promatraj njihovu <strong>razliku</strong> (XOR, oduzimanje) i cilj postaje „svedi na nulu”.''',
        r'''Dva preokreta intervala = XOR s simetričnom razlikom; ona ima najviše dva bloka, što odmah odbacuje sve ulaze s puno blokova.''',
        r'''Kad se broje uređeni parovi $(a_1,a_2,a_3,a_4)$, prebroj neuređene parove intervala pa pomnoži s $2$ – ali pazi da jednaki intervali daju samo jedan uređeni par.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi), rješenje je čista kombinatorika. Neka je $d_i = s_i \oplus t_i$; oba preokreta zajedno XOR-aju $d$ s simetričnom razlikom dvaju intervala, koja ima najviše dva bloka jedinica. Prebroji maksimalne blokove jedinica u $d$: $0$ blokova $\Rightarrow \frac{n(n+1)}{2}$ (intervali jednaki), $1$ blok $\Rightarrow 2(n-1)$, $2$ bloka $\Rightarrow 6$, $\ge 3$ bloka $\Rightarrow 0$. Složenost $O(n)$ po testu.</p>
''',
    'detailed': r'''
<h3>1. Svođenje na jedan niz</h3>
<p>Preokretanje intervala $[a, b]$ u $s$ mijenja $s_i \mapsto 1 - s_i$ za $i \in [a, b]$. Za razliku $d_i = s_i \oplus t_i$ to znači $d_i \mapsto 1 - d_i$ na istom intervalu, a preokret u $t$ djeluje na $d$ identično. Zato je pitanje „postaju li $s$ i $t$ jednaki” isto što i „postaje li $d$ nul-niz”. Neka je $\chi(I)$ karakteristični vektor intervala $I$. Nakon dviju operacija imamo $d \oplus \chi(I_1) \oplus \chi(I_2)$, a $\chi(I_1) \oplus \chi(I_2) = \chi(I_1 \triangle I_2)$ (simetrična razlika). Uvjet je dakle</p>
<p>$$I_1 \triangle I_2 = D := \{ i : d_i = 1 \}.$$</p>
<h3>2. Oblik simetrične razlike</h3>
<p><strong>Tvrdnja.</strong> Simetrična razlika dvaju intervala ima najviše dva maksimalna bloka uzastopnih pozicija. <em>Dokaz.</em> Ako su $I_1, I_2$ disjunktni, $I_1 \triangle I_2 = I_1 \cup I_2$: dva bloka, ili jedan ako se dodiruju. Ako se sijeku, neka je $J = I_1 \cap I_2$ interval; tada je $I_1 \triangle I_2 = (I_1 \cup I_2) \setminus J$, a izbacivanje intervala iz intervala ostavlja najviše dva komada (lijevo i desno od $J$). $\square$</p>
<p>Posljedica: ako $D$ ima tri ili više blokova, odgovor je $0$. Preostaje prebrojati uređene parove $(I_1, I_2)$ za $0$, $1$ i $2$ bloka. Primijetimo da su svi rubovi blokova skupa $I_1 \triangle I_2$ ujedno rubovi intervala $I_1$ ili $I_2$ (rub bloka je mjesto gdje se mijenja pripadnost, a to se može dogoditi samo na rubu nekog intervala).</p>
<h3>3. Nula blokova</h3>
<p>$I_1 \triangle I_2 = \emptyset$ točno kad je $I_1 = I_2$. Intervala ima $\frac{n(n+1)}{2}$, a svaki daje jedan uređeni par $(I, I)$. Odgovor: $\frac{n(n+1)}{2}$.</p>
<h3>4. Jedan blok $[l, r]$</h3>
<p>Razlikujemo dva slučaja prema tome sijeku li se intervali.</p>
<ul>
<li><em>Disjunktni.</em> Unija mora biti točno $[l, r]$, pa su intervali $[l, k]$ i $[k + 1, r]$ za neki $l \le k < r$: $r - l$ neuređenih parova.</li>
<li><em>Sijeku se.</em> Tada $(I_1 \cup I_2) \setminus (I_1 \cap I_2)$ mora biti jedan blok, pa je jedan od dva „viška” prazan: intervali dijele jedan rub, a $[l, r]$ je onaj višak. Ako dijele lijevi rub $l'$: intervali su $[l', l - 1]$ i $[l', r]$, uz $1 \le l' \le l - 1$: $l - 1$ parova. Ako dijele desni rub $r'$: $[l, r']$ i $[r + 1, r']$, uz $r + 1 \le r' \le n$: $n - r$ parova.</li>
</ul>
<p>Svaki neuređeni par čine dva različita intervala pa daje $2$ uređena para. Ukupno $2\,(r - l) + 2\,(l - 1) + 2\,(n - r) = 2(n - 1)$. Zanimljivo je da rezultat ne ovisi o položaju ni duljini bloka; primjer iz zadatka ($n = 2$, $d = 11$) daje $2$.</p>
<h3>5. Dva bloka $[l_1, r_1]$ i $[l_2, r_2]$, $r_1 + 1 < l_2$</h3>
<p>Skup $I_1 \triangle I_2$ ima četiri ruba, a rubova intervala ukupno je četiri, pa se moraju točno poklopiti: lijevi rubovi intervala su $\{l_1, l_2\}$ ili $\{l_1, r_1 + 1\}$, a desni $\{r_1, r_2\}$ ili $\{l_2 - 1, r_2\}$. Provjerom svih kombinacija ostaju tri neuređena para:</p>
<ul>
<li>$[l_1, r_1]$ i $[l_2, r_2]$ – disjunktni, unija je $D$;</li>
<li>$[l_1, r_2]$ i $[r_1 + 1, l_2 - 1]$ – veliki interval i „rupa”, razlika je $D$;</li>
<li>$[l_1, l_2 - 1]$ i $[r_1 + 1, r_2]$ – preklapaju se točno na rupi, razlika je $D$.</li>
</ul>
<p>Svaki u dva poretka: odgovor $6$, što potvrđuje treći primjer ($d = 01101$, blokovi $[2,3]$ i $[5,5]$).</p>
<h3>6. Algoritam i složenost</h3>
<p>Za svaki test prođi $i = 1..n$ i broji pozicije gdje je $s_i \ne t_i$, a $s_{i-1} = t_{i-1}$ (početak bloka). Zatim ispiši vrijednost prema broju blokova. Vrijeme $O(n)$, ukupno $O(\sum n) = O(10^7)$; memorija $O(n)$ za nizove.</p>
<h3>7. Zamke</h3>
<p>Odgovor za nula blokova ($\approx 5 \cdot 10^{11}$ za $n = 10^6$) ne stane u 32 bita. Nizovi su dugi do $10^6$ pa čitaj znak po znak ili u statički spremnik, a ne <code>cin &gt;&gt; string</code> bez isključene sinkronizacije.</p>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n \le 8$, $t$ nastaje iz $s$ s 0–3 promjene ili posve slučajno) protiv brute forcea koji nabraja sve četvorke $(a_1,a_2,a_3,a_4)$; 3 velika testa s $T = 10$, $n = 10^6$ (najviše $0.06$ s).''',
},
# ---------------------------------------------------------------- D
{
    'letter': 'D', 'title': 'Magic Multiplication', 'title_hr': 'Čarobno množenje', 'slug': 'D_magic_multiplication',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Za $A = a_1 a_2 \dots a_n$ i $B = b_1 b_2 \dots b_m$ (znamenke) definiramo $A \otimes B$ kao <em>konkatenaciju</em> stringova $a_i b_j$ (dekadski zapis umnoška, bez vodećih nula; $0$ se piše kao jedna nula) redom za $i = 1..n$, $j = 1..m$. Npr. $23 \otimes 45 = 8101215$.</p>
<p>Dani su $n$, $m$ i rezultat $C$. Rekonstruiraj $A$ i $B$ (pozitivni, bez vodećih nula, točno $n$ odnosno $m$ znamenaka); ako ima više rješenja, ono s najmanjim $A$, pa najmanjim $B$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n, m \le 2 \cdot 10^5$; $C$ bez vodećih nula duljine najviše $2 \cdot 10^5$; $\sum |C| \le 2 \cdot 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test <code>A B</code> ili <code>Impossible</code>.</p>
<h3>Primjer</h3>
<p>$n = m = 2$, $C = 8101215 \to$ <code>23 45</code>. $n = 3, m = 4$, $C = 100000001000 \to$ <code>101 1000</code>. $n = m = 2$, $C = 80101215 \to$ <code>Impossible</code>. $n = 3, m = 4$, $C = 1000000010000 \to$ <code>Impossible</code>.</p>
''',
    'hints': [
        r'''
<p>Sve o $C$ određeno je prvom znamenkom $a_1$: ako je znaš, umnošci $a_1 b_1, a_1 b_2, \dots$ stoje na početku $C$ redom. Probaj svih $9$ mogućnosti za $a_1$.</p>
''',
        r'''
<p>Kad je $a_1$ poznat, svaki sljedeći umnožak „odgrizi” s početka: ako je znamenka $0$, umnožak je $0$; ako je jedna znamenka djeljiva s $a_1$, to je umnožak; inače uzmi dvije znamenke. Dokaži da je taj izbor jednoznačan.</p>
''',
        r'''
<p>Kad je cijeli $B$ rekonstruiran, znamenka $b_1$ na isti način daje svaki $a_i$ iz početka $i$-tog bloka, a ostatak bloka samo provjeravaš. Najmanji $a_1$ koji uspije daje najmanji $A$, a $B$ je tada jedinstven.</p>
''',
    ],
    'coach': [
        ('Zašto se sve vrti oko prve znamenke $a_1$?',
         r'''
<p>$C$ počinje umnošcima $a_1 b_1, a_1 b_2, \dots, a_1 b_m$ (prvi „redak”). Ako znamo $a_1$, iz tih umnožaka čitamo cijeli $B$. Kad znamo $B$ (posebno $b_1 \ge 1$), svaki daljnji redak počinje umnoškom $a_i b_1$ koji određuje $a_i$, a ostatak retka je provjera. Dakle za fiksan $a_1$ postoji najviše jedno rješenje, i ukupno ima najviše $9$ kandidata.</p>
'''),
        ('Kako iz početka niza jednoznačno pročitati umnožak $d \\cdot y$ kad znamo $d \\ge 1$, a $y \\in \\{0,\\dots,9\\}$?',
         r'''
<p>Umnožak ima jednu znamenku ($< 10$) ili dvije ($10..81$, bez vodeće nule). Pogledajmo prvu znamenku $x$. Ako je $x = 0$, umnožak je $0$ (dvoznamenkasti nema vodeću nulu), pa $y = 0$. Ako je $x \ne 0$ i $d \mid x$, tada je $y = x/d$ jednoznamenkasto rješenje – a dvoznamenkasto $10x + x'$ ne može biti umnožak jer $10x + x' \ge 10x \ge 10d > 9d$. Ako $d \nmid x$, jednoznamenkasti ne postoji, pa mora biti dvoznamenkasti $10x + x'$: provjeri $d \mid 10x + x'$ i $(10x+x')/d \le 9$, inače neuspjeh. Svaki korak je dakle prisiljen.</p>
'''),
        ('Zašto najmanji uspješni $a_1$ daje leksikografski najmanji par $(A, B)$?',
         r'''
<p>$A$ i $B$ imaju fiksne duljine $n$ i $m$, pa je „najmanji” isto što i numerički najmanji. Za dani $a_1$ postoji najviše jedan par $(A, B)$, i njegov $A$ počinje s $a_1$. Rješenje s manjim $a_1$ ima manji $A$. Prvi $a_1 \in \{1..9\}$ za koji rekonstrukcija uspije i potroši točno cijeli $C$ daje odgovor; ako nijedan ne uspije: <code>Impossible</code>.</p>
'''),
        ('Što treba provjeriti da se ne bi prihvatilo pogrešno rješenje?',
         r'''
<p>Da $b_1 \ne 0$ (inače $B$ ima vodeću nulu i ne može odrediti $a_i$), da svaki odgriz ne izlazi izvan $C$, da se ostali umnošci $a_i b_j$ ($j \ge 2$) doslovno podudaraju s odgovarajućim znamenkama (npr. umnožak $12$ ne smije se podudariti s „1” pa „2” drukčije), i da se na kraju potroši točno $|C|$ znamenki. Složenost je $O(9 |C|)$ po testu, ukupno $O(\sum |C|)$.</p>
'''),
    ],
    'tips': [
        r'''Kad izlaz ovisi o malom broju „ključnih” nepoznanica (ovdje jedna znamenka), isprobaj sve njihove vrijednosti i za svaku napravi deterministično parsiranje.''',
        r'''Prije parsiranja dokaži jednoznačnost (ovdje: jednoznamenkasti i dvoznamenkasti kandidat ne mogu istodobno biti valjani); tako izbjegavaš backtracking.''',
        r'''Duljine $A$ i $B$ su zadane, pa su leksikografski i numerički poredak isti – najmanji $a_1$ znači najmanji $A$.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi): $C$ počinje umnošcima $a_1 b_j$, pa za svaki kandidat $a_1 \in \{1..9\}$ (od najmanjeg) deterministički rekonstruiramo $B$: umnožak $a_1 b_j$ „odgrizemo” s početka – znamenka $0$ znači $b_j = 0$; jedna znamenka $x$ djeljiva s $a_1$ znači $b_j = x/a_1$ (dvoznamenkasti kandidat je tada nemoguć jer $10x > 9a_1$); inače dvije znamenke $10x + x'$ moraju biti djeljive s $a_1$ s kvocijentom $\le 9$. Zatim iz početka svakog sljedećeg retka jednako pročitamo $a_i$ pomoću $b_1 \ne 0$, a ostale umnoške samo usporedimo. Prvi $a_1$ za koji sve prođe i potroši točno $|C|$ znamenki daje odgovor, inače <code>Impossible</code>. Složenost $O(9|C|)$.</p>
''',
    'detailed': r'''
<h3>1. Struktura niza $C$</h3>
<p>$C$ je konkatenacija umnožaka $a_i b_j$ u redoslijedu $(i, j) = (1,1), (1,2), \dots, (1,m), (2,1), \dots, (n,m)$, svaki zapisan bez vodećih nula ($0$ kao „0”). Umnožak dviju znamenki je između $0$ i $81$: jedna znamenka ako je $< 10$, inače dvije. Dakle $|C|$ je između $nm$ i $2nm$; ako to ne vrijedi, odgovor je odmah <code>Impossible</code> (naš postupak to otkrije i sam).</p>
<h3>2. Lema o jednoznačnom odgrizu</h3>
<p><strong>Lema.</strong> Neka je $d \in \{1..9\}$ poznat i neka niz znamenki počinje umnoškom $d \cdot y$ za neki nepoznati $y \in \{0..9\}$. Tada je duljina tog umnoška (1 ili 2 znamenke) i vrijednost $y$ jednoznačno određena prvim dvjema znamenkama. <em>Dokaz.</em> Neka je $x$ prva znamenka. (a) $x = 0$: dvoznamenkasti zapis nema vodeću nulu, pa je umnožak $0$ i $y = 0$. (b) $x \ne 0$ i $d \mid x$: kandidat je $y = x/d$ ($\le 9$ jer $x \le 9$). Dvoznamenkasti kandidat $10x + x'$ zahtijevao bi $10x + x' = d y'$ s $y' \le 9$, ali $10x + x' \ge 10x \ge 10d > 9d \ge d y'$ – nemoguće. (c) $x \ne 0$ i $d \nmid x$: jednoznamenkasti kandidat ne postoji, pa umnožak mora biti dvoznamenkast $10x + x'$; on je valjan točno ako $d \mid 10x + x'$ i $(10x + x')/d \le 9$. $\square$</p>
<h3>3. Rekonstrukcija za fiksan $a_1$</h3>
<ol>
<li>Postavi pokazivač $p = 0$. Za $j = 1..m$ odgrizi umnožak $a_1 b_j$ pomoću leme (s $d = a_1$) i tako dobij $b_j$; ako odgriz nije moguć ili izlazi iz $C$, kandidat pada. Ako je $b_1 = 0$, kandidat pada ($B$ nema vodeću nulu).</li>
<li>Za $i = 2..n$: odgrizi umnožak $a_i b_1$ s $d = b_1$ i dobij $a_i$; zatim za $j = 2..m$ izračunaj $a_i b_j$, zapiši ga kao string i provjeri da se doslovno podudara s idućim znamenkama $C$ (pomakni $p$ za duljinu zapisa).</li>
<li>Kandidat uspijeva ako je na kraju $p = |C|$.</li>
</ol>
<p><strong>Ispravnost.</strong> Ako par $(A, B)$ s prvom znamenkom $a_1$ generira $C$, lema jamči da koraci 1 i 2 rekonstruiraju upravo $B$ i $A$ (svaki korak je prisiljen), pa postupak uspijeva i vraća taj par. Obratno, ako postupak uspije, dobiveni $A, B$ imaju $a_1, b_1 \ne 0$ i njihovi umnošci konkateniraju se točno u $C$ (koraci 1 i 2 su upravo ta usporedba) – dakle su valjano rješenje. Za fiksan $a_1$ postoji najviše jedno rješenje.</p>
<h3>4. Minimalnost</h3>
<p>Duljine $n$ i $m$ su zadane, pa je poredak po $A$ pa po $B$ numerički. Sva rješenja s istim $a_1$ su identična (jedinstvenost), a rješenje s manjim $a_1$ ima manji $A$. Zato isprobavamo $a_1 = 1, 2, \dots, 9$ i prvo uspješno je odgovor; ako nijedno ne uspije, ispisujemo <code>Impossible</code>.</p>
<h3>5. Složenost i zamke</h3>
<p>Za svaki od $9$ kandidata radimo jedan prolaz kroz $C$: $O(9 |C|)$ po testu, $O(\sum |C|) = O(2 \cdot 10^6)$ ukupno. Zamke: čitanje izvan kraja $C$ pri dvoznamenkastom odgrizu; usporedba umnoška kao stringa (npr. „12” vs. „1”,„2”); provjera $b_1 \ne 0$; provjera da je $C$ do kraja potrošen (treći primjer: <code>80101215</code> s $n = m = 2$ ostaje neobjašnjen višak). Četvrti primjer <code>1000000010000</code> pada jer bi za $a_1 = 1$ trebalo $b = (1,0,0,0)$, a onda drugi redak počinje s $0$, pa je $a_2 = 0$, treći redak nema dovoljno znamenki – i tako za svaki $a_1$.</p>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n, m \le 3$; $C$ ispravan ili nasumično oštećen/produljen/skraćen) protiv brute forcea koji nabraja sve $A$ i $B$; 3 velika testa s $nm = 10^5$ (najviše $0.01$ s).''',
},
# ---------------------------------------------------------------- E
{
    'letter': 'E', 'title': 'Plants vs. Zombies', 'title_hr': 'Biljke protiv zombija', 'slug': 'E_plants_vs_zombies',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>$n$ biljaka u nizu; $i$-ta je $i$ metara istočno od kuće, ima obranu $d_i = 0$ i brzinu rasta $a_i$. Robot kreće iz kuće (pozicija $0$); u jednom koraku pomakne se točno $1$ m istočno ili zapadno, a ako se nakon pomaka nalazi na biljci $i$, zalije je: $d_i \mathrel{+}= a_i$. Dopušteno je najviše $m$ koraka (robot smije otići i istočno od $n$ ili zapadno od kuće).</p>
<p>Maksimiziraj obranu vrta $\min_i d_i$.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $2 \le n \le 10^5$, $0 \le m \le 10^{12}$, $1 \le a_i \le 10^5$; $\sum n \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najveća moguća obrana vrta.</p>
<h3>Primjer</h3>
<p>$n = 4, m = 8$, $a = (3, 2, 6, 6) \to 6$ (npr. EEWEEWEE daje $d = (6, 6, 12, 6)$). $n = 3, m = 9$, $a = (10, 10, 1) \to 4$.</p>
''',
    'hints': [
        r'''
<p>Zadatak „maksimiziraj minimum” s monotonim uvjetom: ako je moguće postići da su sve obrane $\ge x$, moguće je i za svaki manji $x$. Binarno pretraži $x$ i napiši provjeru <code>moguce(x)</code>.</p>
''',
        r'''
<p>U provjeri idi slijeva nadesno: biljku $i$ moraš zaliti $t_i = \lceil (x - d_i)/a_i \rceil$ puta, gdje je $d_i$ obrana koju je već skupila. Prvo zalijevanje dobiva kad na nju stupiš; svako sljedeće košta dva koraka (korak na $i+1$ i natrag) i pritom jednom zalije biljku $i+1$.</p>
''',
        r'''
<p>Ne vraćaj se ulijevo nikad i prekini provjeru čim broj koraka premaši $m$ (inače prijeti prelijevanje). Gornja granica za $x$ je $\max a_i \cdot m \le 10^{17}$.</p>
''',
    ],
    'coach': [
        ('Zašto se odgovor traži binarnim pretraživanjem, a ne izravno?',
         r'''
<p>Izravno optimiranje puta je teško, ali je predikat „u $m$ koraka može se postići $\min_i d_i \ge x$” monoton u $x$: ako put radi za $x$, radi i za svaki manji $x$. Zato je dovoljno napisati provjeru za fiksan $x$ i binarno pretražiti najveći $x$ za koji uspijeva. Granice: $0$ (uvijek moguće) i $m \cdot \max a_i$ (jedna biljka ne može dobiti više).</p>
'''),
        ('Kako izgleda optimalan put za fiksan $x$ i zašto se nikad ne vraćamo ulijevo?',
         r'''
<p>Svaki posjet biljci $i$ osim prvog zahtijeva da s nje odemo i vratimo se – to su barem dva koraka. Odlazak ulijevo zalijeva biljku $i-1$, koja je već zadovoljena kad obrađujemo redom slijeva, dok odlazak udesno zalijeva biljku $i+1$ koja će nam tek trebati. Dakle svaki par koraka „$i \to i-1 \to i$” možemo zamijeniti parom „$i \to i+1 \to i$” bez štete: broj koraka je isti, biljka $i$ dobiva isto, a umjesto nepotrebne obrane biljke $i-1$ dobiva korisnu obranu biljka $i+1$. Zato promatramo samo puteve oblika: kreni s položaja $0$, na svakoj biljci napravi potreban broj šetnji $i \to i+1 \to i$, pa prijeđi dalje.</p>
'''),
        ('Koliko koraka pohlepa troši na biljci $i$ i što daruje biljci $i+1$?',
         r'''
<p>Kad stupimo na $i$ (1 korak) ona ima obranu $d_i$ (od ranijih posjeta s biljke $i-1$) uvećanu za $a_i$. Treba joj $t_i = \lceil (x - d_i)/a_i \rceil$ zalijevanja ukupno, pa je potrebno $t_i - 1$ dodatnih šetnji, svaka po 2 koraka: ukupno $2t_i - 1$ koraka. Svaka šetnja stupa i na $i+1$, pa $d_{i+1}$ raste za $(t_i - 1) a_{i+1}$. Ako je $d_i \ge x$ već pri dolasku, dovoljno je stupiti na nju (1 korak) samo ako dalje ima posla; ako nema, možemo stati. Zato broj koraka uspoređujemo s $m$ samo kad neka biljka zaista zahtijeva zalijevanje.</p>
'''),
        ('Kako izbjeći prelijevanje i koliko je sve zajedno brzo?',
         r'''
<p>$t_i$ može biti do $\approx 10^{17}$ pa $2t_i - 1$ stane u 64 bita, ali $(t_i - 1) a_{i+1}$ ne bi stalo ($10^{17} \cdot 10^5$). Rješenje: prvo dodaj korake i prekini ako su premašili $m$; tek tada je $t_i - 1 \le m/2 \le 5 \cdot 10^{11}$, pa je $(t_i - 1) a_{i+1} \le 5 \cdot 10^{16}$ sigurno. Binarno pretraživanje ima $\log_2 10^{17} \approx 57$ iteracija, svaka $O(n)$: $O(n \log(m \max a))$.</p>
'''),
    ],
    'tips': [
        r'''„Maksimiziraj minimum” + monoton uvjet = binarno pretraživanje po odgovoru; sav trud ide u brzu provjeru za fiksan prag.''',
        r'''U pohlepnim provjerama s velikim brojevima prvo provjeri prekoračenje budžeta, pa tek onda množi – tako ograničiš veličinu brojeva bez <code>__int128</code>.''',
        r'''Kad se kretanje odvija na pravcu s početkom na jednom kraju, obično je optimalno nikad se ne vraćati „iza” već obrađenog dijela; dokaz zamjenom koraka.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi): binarno pretraži najveću vrijednost $x$ za koju se u najviše $m$ koraka svaka biljka može dovesti na obranu $\ge x$. Provjera je pohlepna slijeva nadesno: kad stupimo na biljku $i$ s već skupljenom obranom $d_i$, treba joj $t_i = \lceil (x - d_i)/a_i \rceil$ zalijevanja; prvo dobiva dolaskom, svako sljedeće šetnjom $i \to i+1 \to i$ (2 koraka) koja ujedno zalije biljku $i+1$. Trošak je $2t_i - 1$ koraka i $d_{i+1}$ raste za $(t_i - 1)a_{i+1}$; biljku koja već ima $\ge x$ samo prekoračimo. Prekini čim koraci premaše $m$. Složenost $O(n \log(m \cdot \max a_i))$.</p>
''',
    'detailed': r'''
<h3>1. Monotonost i binarno pretraživanje</h3>
<p>Neka je $\mathrm{ok}(x)$ tvrdnja „postoji niz od najviše $m$ koraka nakon kojeg svaka biljka ima obranu $\ge x$”. Ako put radi za $x$, isti put radi i za svaki $x' < x$, pa je $\mathrm{ok}$ monoton i odgovor je najveći $x$ s $\mathrm{ok}(x)$. Granice: $\mathrm{ok}(0)$ vrijedi (ne mičemo se), a $x > m \cdot \max_i a_i$ nije moguće jer se svaka biljka zalije najviše $m$ puta. Binarno pretraživanje treba $\approx 57$ evaluacija predikata.</p>
<h3>2. Oblik optimalnog puta</h3>
<p>Za fiksan $x$ zanimaju nas samo brojevi $c_i$ = koliko puta smo stupili na biljku $i$ (obrana je $c_i a_i$). <strong>Tvrdnja.</strong> Ako neki put duljine $L$ postiže $c_i a_i \ge x$ za sve $i$, onda i put sljedećeg oblika postiže isto s najviše $L$ koraka: kreni s pozicije $0$; na biljci $i$ napravi $t_i - 1$ šetnji $i \to i+1 \to i$, zatim prijeđi na $i+1$; nikad ne idi ulijevo (osim unutar šetnje, koja se vraća na $i$).</p>
<p><em>Dokaz.</em> Uzmimo bilo koji uspješan put i promatrajmo prvi trenutak u kojem stupi na biljku $i$ (za svaki $i$ redom). Broj posjeta biljci $i$ nakon prvog stupanja jednak je broju „odlazaka” s nje, a svaki odlazak i povratak košta 2 koraka; odlazak ulijevo zalijeva $i-1$, udesno $i+1$. Zamjenom svakog odlaska ulijevo odlaskom udesno (isti broj koraka, isti posjeti biljci $i$) biljka $i-1$ gubi posjete, ali samo one koji su se dogodili <em>nakon</em> što je prvi put napuštena udesno; te posjete možemo nadoknaditi tako da ih izvedemo ranije, dok smo još bili na $i-1$, kao šetnje $i-1 \to i \to i-1$ – one biljki $i$ daju iste posjete koje bi joj dao povratak s desna. Ponavljanjem od najljevije biljke dobivamo put pohlepnog oblika s istim vektorom posjeta i ne većim brojem koraka. Za pohlepni oblik broj posjeta biljci $i$ određen je s $t_i$: manje posjeta ne zadovoljava prag, a više posjeta nema smisla jer bi trošili korake koje možemo uštedjeti (svaki dodatni posjet biljci $i+1$ koji bismo time dobili može se dobiti i šetnjom s biljke $i+1$ po istoj cijeni od 2 koraka). $\square$</p>
<h3>3. Provjera $\mathrm{ok}(x)$</h3>
<p>Držimo $d_i$ = obrana biljke $i$ skupljena šetnjama s biljke $i-1$ (početno $0$) i broj koraka $s = 0$. Za $i = 1..n$:</p>
<ul>
<li>ako je $d_i \ge x$: $s \leftarrow s + 1$ (samo prekoračimo; ako je to zadnja biljka ili nijedna sljedeća ne treba vodu, taj korak zapravo nije nužan, ali ne utječe na rezultat jer provjeru $s > m$ radimo samo kad neka biljka zahtijeva zalijevanje);</li>
<li>inače $t = \lceil (x - d_i)/a_i \rceil \ge 1$, $s \leftarrow s + 2t - 1$; ako je $s > m$ vrati <code>false</code>; inače $d_{i+1} \leftarrow d_{i+1} + (t - 1) a_{i+1}$ (za $i < n$; za $i = n$ šetnja ide na položaj $n+1$ i ne zalijeva ništa, ali je dopuštena).</li>
</ul>
<p>Na kraju vrati <code>true</code>. Napomena: kad je $d_i \ge x$ pri dolasku, obrana je $d_i$, a stupanje na biljku dodaje još $a_i$ – to ne smeta jer nam treba samo $\ge x$.</p>
<h3>4. Složenost i granice tipova</h3>
<p>Svaka provjera je $O(n)$, pretraživanje ima $O(\log(m \max a_i)) \approx 57$ koraka: ukupno $O(n \log(m \max a_i))$, uz $\sum n \le 10^6$ oko $6 \cdot 10^7$ operacija. Brojevi: $x \le 10^{17}$, $t \le 10^{17}$, $s \le 2 \cdot 10^{17} + m$ – sve u 64 bita. Množenje $(t - 1) a_{i+1}$ radimo <em>tek nakon</em> provjere $s \le m$, kad je $t - 1 \le m / 2 \le 5 \cdot 10^{11}$, pa je umnožak $\le 5 \cdot 10^{16}$.</p>
<h3>5. Rubni slučajevi</h3>
<p>$m = 0$: odgovor $0$ ($\mathrm{ok}(1)$ pada jer prva biljka traži barem 1 korak). $m < n$: neka biljka ostaje nezalivena, odgovor $0$ – provjera to prirodno otkrije. Primjer $n = 3$, $m = 9$, $a = (10, 10, 1)$: za $x = 4$ treba $t = (1, 1, 4)$, koraci $1 + 1 + 7 = 9$; za $x = 5$ treba $9 + 2 = 11 > 9$. Odgovor $4$.</p>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n \le 4$, $m \le 9$, $a_i \le 6$) protiv brute forcea koji nabraja sve nizove poteza lijevo/desno duljine $\le m$; 3 velika testa s $n = 10^5$, $m$ do $10^{12}$, $a_i \le 10^5$ (najviše $0.04$ s).''',
},
# ---------------------------------------------------------------- F
{
    'letter': 'F', 'title': 'Tournament', 'title_hr': 'Turnir', 'slug': 'F_tournament',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>$n$ vitezova, $k$ kola. U svakom kolu svaki vitez ima točno jedan dvoboj; svaki par vitezova bori se najviše jednom u svih $k$ kola. Dodatno, za različita kola $i \ne j$ i četiri različita viteza $a, b, c, d$: ako se u kolu $i$ bore $a$–$b$ i $c$–$d$, a u kolu $j$ $a$–$c$, tada se u kolu $j$ moraju boriti $b$–$d$.</p>
<p>Napravi raspored svih dvoboja.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n, k \le 1000$; $\sum n, \sum k \le 5000$.</p>
<h3>Izlaz</h3>
<p>Ako je moguće, $k$ redaka; u $i$-tom $n$ brojeva $c_{i,1}, \dots, c_{i,n}$ — u kolu $i$ vitez $j$ bori se protiv $c_{i,j}$. Od svih valjanih rasporeda ispiši leksikografski najmanji (uspoređuje se redak po redak, pa broj po broj). Inače <code>Impossible</code>. Bez razmaka na kraju retka.</p>
<h3>Primjer</h3>
<p>$n = 3, k = 1 \to$ <code>Impossible</code>. $n = 4, k = 3 \to$ <code>2 1 4 3</code> / <code>3 4 1 2</code> / <code>4 3 2 1</code>.</p>
''',
    'hints': [
        r'''
<p>Zapiši $i$-tu rundu kao permutaciju $\sigma_i$ bez fiksnih točaka reda $2$ (savršeno sparivanje). Prevedi uvjet „$a$–$b$ i $c$–$d$ u rundi $i$, $a$–$c$ u rundi $j$ $\Rightarrow$ $b$–$d$ u rundi $j$” u jednakost koja uključuje $\sigma_i \circ \sigma_j$.</p>
''',
        r'''
<p>Uvjet je točno $\sigma_i \sigma_j = \sigma_j \sigma_i$ za sve $i \ne j$. Skup svih kompozicija tvori komutativnu grupu u kojoj je svaki element sam sebi inverz – što to govori o veličini orbite jednog viteza?</p>
''',
        r'''
<p>Orbite imaju veličinu potenciju broja $2$, a svaka mora sadržavati $k + 1$ različitih vitezova (vitez i njegovih $k$ protivnika). Zato je nužno $k < \mathrm{lowbit}(n)$. Za konstrukciju probaj protivnika $j \oplus i$ (XOR, indeksi od $0$) i uvjeri se da je to leksikografski najmanje.</p>
''',
    ],
    'coach': [
        ('Kako uvjet zadatka izgleda u jeziku permutacija?',
         r'''
<p>Runda $i$ je involucija bez fiksnih točaka $\sigma_i$ ($\sigma_i(a) = b \Leftrightarrow$ $a$ i $b$ se bore). Uvjet kaže: ako je $\sigma_i(a) = b$, $\sigma_i(c) = d$ i $\sigma_j(a) = c$, tada $\sigma_j(b) = d$, tj. $\sigma_j(\sigma_i(a)) = \sigma_i(\sigma_j(a))$. Uvjet „$a, b, c, d$ različiti” automatski vrijedi: $b \ne a$, $c \ne a$ (nema fiksnih točaka), $b \ne c$ (par se bori najviše jednom, pa $\sigma_i(a) \ne \sigma_j(a)$), $d \ne c$, $d \ne a$ (inače $\sigma_i(a) = c = \sigma_j(a)$), $d \ne b$ (inače $c = a$). Dakle uvjet je točno $\sigma_i \sigma_j = \sigma_j \sigma_i$ za svaki par rundi, uz to da su sva sparivanja po parovima „disjunktna”.</p>
'''),
        ('Zašto su orbite veličine $2^s$ i zašto svaka ima barem $k + 1$ elemenata?',
         r'''
<p>Neka je $G$ grupa generirana svim $\sigma_i$. Generatori komutiraju i involucije su, pa je $G$ komutativna i svaki element $g$ zadovoljava $g^2 = \mathrm{id}$: $G$ je vektorski prostor nad $\mathbb{Z}_2$, $|G| = 2^r$. Orbita viteza $a$ je $\{g(a) : g \in G\}$; preslikavanje $g \mapsto g(a)$ je konstantno na klasama podgrupe stabilizatora $H_a$ i različito na različitim klasama, pa je $|\text{orbita}| = |G|/|H_a|$ – potencija broja 2. Nadalje, $a, \sigma_1(a), \dots, \sigma_k(a)$ su $k + 1$ različitih vitezova (protivnici su različiti) i svi su u orbiti od $a$. Dakle svaka orbita ima veličinu $2^s \ge k + 1$.</p>
'''),
        ('Kako iz toga slijedi nužan uvjet $k < \\mathrm{lowbit}(n)$?',
         r'''
<p>Orbite particioniraju vitezove, pa je $n$ zbroj potencija broja $2$ od kojih je svaka $\ge 2^s$, gdje je $2^s$ najmanja orbita. Sve su potencije $\ge 2^s$ višekratnici od $2^s$, pa $2^s \mid n$, dakle $2^s \le \mathrm{lowbit}(n)$ (najveća potencija dvojke koja dijeli $n$). Zajedno s $k + 1 \le 2^s$ dobivamo $k + 1 \le \mathrm{lowbit}(n)$. Za $k \ge \mathrm{lowbit}(n)$ odgovor je <code>Impossible</code>.</p>
'''),
        ('Zašto XOR-konstrukcija radi i zašto je leksikografski najmanja?',
         r'''
<p>Neka je $L = \mathrm{lowbit}(n)$ i vitezovi indeksirani $0..n-1$. U rundi $i$ ($1 \le i \le k < L$) protivnik viteza $j$ je $j \oplus i$. Kako je $i < L$ i $L \mid n$, $j \oplus i$ ostaje u istom bloku od $L$ uzastopnih indeksa, dakle unutar $[0, n)$. Preslikavanje je involucija bez fiksnih točaka, različite runde daju različite protivnike ($j \oplus i \ne j \oplus i'$), a XOR-ovi komutiraju. Leksikografska minimalnost: indukcijom po rundama, ako su runde $1..i-1$ XOR-runde, grupa koju generiraju je $\{x \mapsto x \oplus t : t < 2^p\}$ za najmanji $2^p \ge i$. Vitez $0$ već se borio s $1, \dots, i-1$, pa je najmanji dopušteni protivnik $i$; komutiranje s $x \mapsto x \oplus t$ tada <em>prisiljava</em> $\sigma_i(t) = i \oplus t$ za sve $t < 2^p$. Sljedeći još nesparen vitez je početak idućeg bloka i argument se ponavlja. Svaki je zapis dakle najmanji mogući, a raspored se može dovršiti (XOR radi za sve $k < L$).</p>
'''),
    ],
    'tips': [
        r'''Uvjete oblika „ako se $a$–$b$, $c$–$d$ i $a$–$c$ bore, onda i $b$–$d$” pokušaj zapisati kao <strong>komutiranje permutacija</strong>; time se kombinatorni uvjet pretvara u algebarski.''',
        r'''Komutativna grupa u kojoj je svaki element involucija ima red $2^r$, a njezine orbite također – česta prečica za dokaz „mora biti potencija dvojke”.''',
        r'''Za leksikografski najmanje konstrukcije: dokaži da je pohlepni izbor na svakom mjestu prisiljen (ovdje komutiranjem s prethodnim rundama) i da se pohlepni prefiks uvijek može dovršiti.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi) uvjet znači da sva sparivanja $\sigma_1, \dots, \sigma_k$ (involucije bez fiksnih točaka) međusobno komutiraju. Grupa koju generiraju je komutativna s $g^2 = \mathrm{id}$, pa su orbite vitezova veličine $2^s$; svaka orbita sadrži viteza i njegovih $k$ protivnika, dakle $2^s \ge k + 1$, a $2^s \mid n$ daje $k < \mathrm{lowbit}(n)$. Ako je $k \ge \mathrm{lowbit}(n)$: <code>Impossible</code>. Inače je leksikografski najmanji raspored: u rundi $i$ vitez $j$ (indeksi od $0$) bori se s $j \oplus i$; ispis $+1$. Složenost $O(nk)$.</p>
''',
    'detailed': r'''
<h3>1. Prijevod u permutacije</h3>
<p>Rundu $i$ zapišimo kao $\sigma_i$: $\sigma_i(a)$ je protivnik viteza $a$. Tada je $\sigma_i$ involucija ($\sigma_i^2 = \mathrm{id}$) bez fiksnih točaka. Uvjet da se svaki par bori najviše jednom glasi $\sigma_i(a) \ne \sigma_j(a)$ za $i \ne j$. Uvjet zadatka: iz $\sigma_i(a) = b$, $\sigma_i(c) = d$, $\sigma_j(a) = c$ slijedi $\sigma_j(b) = d$, tj.</p>
<p>$$\sigma_j(\sigma_i(a)) = \sigma_i(\sigma_j(a)) \quad \text{za sve } a, \text{ sve } i \ne j.$$</p>
<p>Pretpostavka „$a, b, c, d$ različiti” u zadatku ne sužava ništa: $b \ne a$ i $c \ne a$ (nema fiksnih točaka), $b \ne c$ (jer $\sigma_i(a) \ne \sigma_j(a)$), $d \ne c$, $d \ne a$ (inače bi $\sigma_i(a) = c = \sigma_j(a)$), $d \ne b$ (inače $\sigma_i(c) = \sigma_i(a)$, pa $c = a$). Dakle: <strong>raspored je valjan točno kad su $\sigma_1, \dots, \sigma_k$ komutirajuće involucije bez fiksnih točaka s $\sigma_i(a) \ne \sigma_j(a)$.</strong></p>
<h3>2. Struktura grupe i orbite</h3>
<p>Neka je $G = \langle \sigma_1, \dots, \sigma_k \rangle$. Generatori komutiraju, pa je $G$ komutativna; svaki element je produkt generatora, a kvadrat produkta komutirajućih involucija je identiteta. Grupa u kojoj svaki element zadovoljava $g^2 = \mathrm{id}$ i koja je komutativna jest vektorski prostor nad $\mathbb{Z}_2$ (zbrajanje = kompozicija), pa je $|G| = 2^r$.</p>
<p>Orbita viteza $a$ je $O(a) = \{g(a) : g \in G\}$. Skup $H_a = \{g : g(a) = a\}$ je podgrupa (stabilizator), a $g(a) = g'(a) \Leftrightarrow g^{-1}g' \in H_a$, pa je $|O(a)| = |G| / |H_a|$ – potencija broja $2$ (Lagrangeov teorem: red podgrupe dijeli red grupe). Orbite particioniraju skup vitezova.</p>
<p>U orbiti od $a$ leže $a, \sigma_1(a), \dots, \sigma_k(a)$, međusobno različiti (protivnici su različiti i različiti od $a$). Dakle svaka orbita ima barem $k + 1$ elemenata.</p>
<h3>3. Nužan uvjet</h3>
<p>Neka je $2^s$ veličina najmanje orbite. Sve orbite imaju veličinu $2^{s'}$ s $s' \ge s$, dakle djeljivu s $2^s$, pa je i $n$ (zbroj veličina) djeljiv s $2^s$: $2^s \le \mathrm{lowbit}(n)$, gdje je $\mathrm{lowbit}(n)$ najveća potencija dvojke koja dijeli $n$. Uz $k + 1 \le 2^s$ dobivamo</p>
<p>$$k \le \mathrm{lowbit}(n) - 1.$$</p>
<p>Posebno, za neparan $n$ nema rješenja ni za $k = 1$ (nemoguće sparivanje), što je konzistentno.</p>
<h3>4. Konstrukcija: XOR</h3>
<p>Neka je $L = \mathrm{lowbit}(n)$ i $k < L$. Indeksirajmo vitezove $0, \dots, n-1$ i stavimo $\sigma_i(j) = j \oplus i$ za $1 \le i \le k$. Kako je $i < L$, XOR s $i$ mijenja samo bitove ispod pozicije $\log_2 L$, pa $j \oplus i$ ostaje u istom bloku $[tL, (t+1)L)$; budući da $L \mid n$, blokovi točno pokrivaju $[0, n)$. Svojstva: $\sigma_i$ je involucija bez fiksnih točaka ($i \ne 0$); $j \oplus i \ne j \oplus i'$ za $i \ne i'$; $\sigma_i \sigma_j = \sigma_j \sigma_i$ jer je XOR komutativan i asocijativan. Prema 1. raspored je valjan.</p>
<h3>5. Leksikografska minimalnost</h3>
<p>Ispis se uspoređuje redak po redak (runda po runda), unutar retka vitez po vitez. Dokazujemo indukcijom da je XOR-raspored najmanji mogući u svakom zapisu.</p>
<p>Runda $1$: najmanji mogući protivnik viteza $0$ je $1$, zatim za viteza $2$ je $3$, itd. – to je točno $j \oplus 1$. Pretpostavimo da su runde $1, \dots, i-1$ XOR-runde. Grupa $G_{i-1}$ koju generiraju je $\{x \mapsto x \oplus t : t \in \mathrm{span}\{1, \dots, i-1\}\} = \{x \mapsto x \oplus t : t < 2^p\}$, gdje je $2^p$ najmanja potencija dvojke $\ge i$ (brojevi $1, \dots, i-1$ generiraju XOR-om sve brojeve s bitovima ispod pozicije $p$). Za rundu $i$: vitez $0$ već se borio s $1, \dots, i-1$, pa mu je najmanji dopušteni protivnik $i$. Komutiranje $\sigma_i$ s $x \mapsto x \oplus t$ daje $\sigma_i(t) = \sigma_i(0 \oplus t) = \sigma_i(0) \oplus t = i \oplus t$ za sve $t < 2^p$ – time je prvi blok od $2^p$ vitezova (i njihovi protivnici) određen bez ikakva izbora. Sljedeći nesparen vitez je $j = $ početak idućeg bloka (višekratnik od $2^p$, a ako je $i = 2^p$, višekratnik od $2^{p+1}$ jer je prvi blok otišao u drugi); njegovi već korišteni protivnici su $j \oplus 1, \dots, j \oplus (i-1) = j+1, \dots, j+i-1$, pa mu je najmanji dopušteni protivnik $j + i = j \oplus i$, i opet komutiranje određuje cijeli blok. Svaki je zapis dakle najmanji koji dopuštaju prethodne runde, a XOR-raspored se doista može dovršiti do $k$ rundi. Zato je globalno leksikografski najmanji. $\square$</p>
<h3>6. Algoritam, složenost, zamke</h3>
<p>Izračunaj $L = n \,\&\, (-n)$. Ako je $k \ge L$, ispiši <code>Impossible</code>; inače za $i = 1..k$ ispiši $(j \oplus i) + 1$ za $j = 0..n-1$. Složenost $O(nk)$, a $\sum n, \sum k \le 5000$ pa je izlaz najviše $\approx 2.5 \cdot 10^7$ brojeva – koristi brz ispis (skupljanje u spremnik). Ne zaboravi pretvorbu indeksa $0 \leftrightarrow 1$.</p>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n \in \{2,4,6,8\}$, $k \le 4$) protiv brute forcea koji backtrackingom gradi leksikografski najmanji valjan raspored (ili dokazuje da ne postoji); 3 velika testa s $n$ do $4096$ i slučajnim $k$ (najviše $0.11$ s).''',
},
# ---------------------------------------------------------------- G
{
    'letter': 'G', 'title': 'Repair the Artwork', 'title_hr': 'Popravi umjetničko djelo', 'slug': 'G_repair_the_artwork',
    'tl': '6 s', 'ml': '256 MiB',
    'statement': r'''
<p>Papirna traka s $n$ polja; $a_i = 0$ prazno, $a_i = 1$ DreamGridov uzorak, $a_i = 2$ BaoBaoov uzorak. Operacija: odaberi $1 \le l \le r \le n$ takve da nijedno polje u $[l, r]$ ne sadrži DreamGridov uzorak i isprazni sva polja $[l, r]$.</p>
<p>Na koliko načina (nizovi od $m$ uređenih parova $(l, r)$) se točno $m$ operacija može izvesti tako da na kraju nema BaoBaoovih uzoraka? Odgovor modulo $10^9 + 7$.</p>
<h3>Ulaz</h3>
<p>$1 \le T \le 1000$ testova; $1 \le n \le 100$, $1 \le m \le 10^9$, $a_i \in \{0, 1, 2\}$; najviše $50$ testova ima $n \gt 50$.</p>
<h3>Izlaz</h3>
<p>Za svaki test broj načina modulo $10^9 + 7$.</p>
<h3>Primjer</h3>
<p>$a = (2, 0)$, $m = 2 \to 8$. $a = (2, 1, 0)$, $m = 2 \to 3$. $a = (2, 1, 0)$, $m = 1 \to 1$.</p>
''',
    'hints': [
        r'''
<p>Kad bi niz sadržavao samo $0$ i $1$, odgovor bi bio $k^m$, gdje je $k$ broj intervala bez jedinica. Dvojke smetaju jer <em>moraju</em> biti pokrivene. Kako se uvjet „mora biti pokrivena” izražava preko „smije biti pokrivena” i „ne smije biti pokrivena”?</p>
''',
        r'''
<p>Uključivanje–isključivanje: za svaki podskup $S$ dvojki koje proglasimo „zabranjenima” (tretiramo kao $1$) i ostale dvojke tretiramo kao $0$, doprinos je $(-1)^{|S|} k(S)^m$. Vrijednost ovisi samo o parnosti $|S|$ i broju intervala $k(S)$ – to je stanje DP-a.</p>
''',
        r'''
<p>Broj intervala bez jedinica je zbroj $\frac{g(g+1)}{2}$ po prazninama duljine $g$ između blokiranih pozicija. DP po posljednjoj blokiranoj poziciji: $f(i, j, p)$ = broj podskupova s posljednjom blokadom na $i$, $j$ intervala, parnost $p$; prijelaz preskače samo nule i dvojke do sljedeće blokade.</p>
''',
    ],
    'coach': [
        ('Kako riješiti zadatak bez dvojki?',
         r'''
<p>Ako su samo $0$ i $1$, svaka operacija bira jedan od $k$ intervala koji ne sadrže jedinicu, neovisno o prethodnima, i nema što pokrivati: točno $k^m$ nizova. Intervali bez jedinica su podintervali maksimalnih blokova nula; blok duljine $g$ daje $\frac{g(g+1)}{2}$ intervala.</p>
'''),
        ('Kako se uvjet „svaka dvojka mora biti pokrivena” pretvara u zbroj lakših zadataka?',
         r'''
<p>Za jednu dvojku: (mora biti pokrivena) $=$ (smije biti pokrivena, tj. ponaša se kao $0$) $-$ (nije pokrivena, tj. nijedan interval ne smije sadržavati tu poziciju: ponaša se kao $1$). Za više dvojki primjenom istog identiteta po svakoj dobivamo uključivanje–isključivanje: $$\text{odg} = \sum_{S \subseteq \text{dvojke}} (-1)^{|S|}\, k(S)^m,$$ gdje $k(S)$ = broj intervala koji ne sadrže nijednu jedinicu ni poziciju iz $S$. To je točno formula „broj nizova koji pokrivaju sve” = $\sum_S (-1)^{|S|} \cdot$ (broj nizova koji izbjegavaju $S$).</p>
'''),
        ('Podskupova je $2^{\\#2}$ – kako ih ne nabrajati?',
         r'''
<p>Pribrojnik ovisi samo o parnosti $|S|$ i o $k(S)$. Nazovimo <em>blokiranima</em> jedinice i pozicije iz $S$; $k(S)$ je zbroj $\frac{g(g+1)}{2}$ po prazninama duljine $g$ između uzastopnih blokiranih pozicija (uz rubne blokade $a_0 = a_{n+1} = 1$). Zato je prirodan DP po blokiranim pozicijama: $f(i, j, p)$ = broj izbora $S$ među dvojkama na pozicijama $\le i$, takvih da je $i$ blokirana, ukupno $j$ intervala lijevo od $i$ i $|S| \equiv p \pmod 2$. Prijelaz: sljedeća blokirana pozicija $i' > i$, između njih samo nule i dvojke (koje nisu u $S$); ako je $a_{i'} = 1$, parnost ostaje, ako je $a_{i'} = 2$, parnost se mijenja; $j$ raste za $\frac{g(g+1)}{2}$, $g = i' - i - 1$. Preko jedinice se ne može preskočiti.</p>
'''),
        ('Kolika je složenost i kako se računa konačni odgovor?',
         r'''
<p>Stanja: $i \le n + 1$, $j \le \frac{n(n+1)}{2} \approx 5050$, $p \in \{0,1\}$; prijelaza po stanju do $n$. Ali do pozicije $i$ broj intervala je najviše $\frac{i(i+1)}{2}$, pa je ukupni rad $\sum_i (n - i) \cdot \frac{i^2}{2} \approx \frac{n^4}{24} \approx 4 \cdot 10^6$ za $n = 100$ – daleko ispod granice, čak i za $50$ velikih testova. Odgovor je $\sum_j \big(f(n+1, j, 0) - f(n+1, j, 1)\big) \cdot j^m \bmod (10^9 + 7)$, s $j^m$ brzim potenciranjem; pripazi da razlika bude nenegativna prije množenja.</p>
'''),
    ],
    'tips': [
        r'''„Svaki element skupa $X$ mora biti pokriven” $\Rightarrow$ uključivanje–isključivanje po podskupu $S \subseteq X$ nepokrivenih: $\sum_S (-1)^{|S|}\cdot$(broj načina koji izbjegavaju $S$).''',
        r'''Kad pribrojnik u uključivanju–isključivanju ovisi samo o nekoliko sažetih veličina (parnost, broj intervala), zamijeni nabrajanje podskupova dinamičkim programiranjem po tim veličinama.''',
        r'''Rubne „blokade” ($a_0 = a_{n+1} = 1$) pojednostavnjuju prijelaze i uklanjaju posebne slučajeve na krajevima niza.''',
        r'''Za $O(n^4)$ DP procijeni pravu konstantu (ovdje $\approx n^4/24$) prije nego odbaciš pristup.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi): bez dvojki odgovor je $k^m$ ($k$ = broj intervala bez jedinica). Uvjet „svaka dvojka pokrivena” rješava se uključivanjem–isključivanjem: $\text{odg} = \sum_{S} (-1)^{|S|} k(S)^m$ po podskupovima $S$ dvojki koje proglasimo blokiranima (kao $1$), dok se ostale dvojke ponašaju kao $0$. Pribrojnik ovisi samo o parnosti $|S|$ i o $k(S)$, pa DP $f(i, j, p)$ (posljednja blokirana pozicija $i$, $j$ intervala, parnost $p$) prelazi na sljedeću blokiranu poziciju $i'$ preskačući samo nule i dvojke, uz $j \mathrel{+}= \frac{g(g+1)}{2}$ za prazninu $g = i' - i - 1$; $a_0 = a_{n+1} = 1$. Odgovor $\sum_j (f(n{+}1, j, 0) - f(n{+}1, j, 1))\, j^m$. Složenost $\approx n^4/24$ po testu.</p>
''',
    'detailed': r'''
<h3>1. Slučaj bez dvojki</h3>
<p>Operacija smije birati bilo koji interval koji ne sadrži jedinicu; izbori su međusobno neovisni jer brisanje ne mijenja skup dopuštenih intervala (prazno ostaje prazno). Ako je $k$ broj takvih intervala, nizova od $m$ operacija je $k^m$. Intervali bez jedinica su točno podintervali maksimalnih blokova ne-jedinica; blok duljine $g$ sadrži $\frac{g(g+1)}{2}$ intervala.</p>
<h3>2. Uključivanje–isključivanje po dvojkama</h3>
<p>Neka je $X$ skup pozicija s $a_i = 2$. Tražimo broj nizova operacija (svaka bira interval bez jedinica) čija unija pokriva cijeli $X$. Za $S \subseteq X$ neka je $N(S)$ broj nizova koji <em>ne pokrivaju nijednu</em> poziciju iz $S$; to je broj nizova u kojima svaki interval izbjegava $S$ i jedinice, dakle $N(S) = k(S)^m$ gdje je $k(S)$ broj intervala bez jedinica i bez pozicija iz $S$ (pozicije iz $S$ ponašaju se kao jedinice, ostale dvojke kao nule). Po principu uključivanja–isključivanja broj nizova koji pokrivaju sve iz $X$ je</p>
<p>$$\text{odg} = \sum_{S \subseteq X} (-1)^{|S|} N(S) = \sum_{S \subseteq X} (-1)^{|S|} k(S)^m.$$</p>
<p>(Dokaz: niz koji ne pokriva točno skup $U \subseteq X$ pribraja se sa $\sum_{S \subseteq U} (-1)^{|S|} = [U = \emptyset]$.)</p>
<h3>3. Sažimanje stanja</h3>
<p>Pribrojnik ovisi samo o parnosti $|S|$ i o $k(S)$. Nazovimo <em>blokiranima</em> pozicije s $a_i = 1$ i pozicije iz $S$; dodajmo rubne blokade $a_0 = a_{n+1} = 1$ (ne mijenjaju odgovor jer intervali žive u $[1, n]$). Ako su blokirane pozicije $0 = i_0 < i_1 < \dots < i_r = n+1$, tada je</p>
<p>$$k(S) = \sum_{t=1}^{r} \frac{g_t (g_t + 1)}{2}, \qquad g_t = i_t - i_{t-1} - 1.$$</p>
<p>Definirajmo $f(i, j, p)$ = broj podskupova $S$ dvojki s pozicija $< i$ (uz uvjet da su sve jedinice s pozicija $< i$ „preskočene” korektno) takvih da je pozicija $i$ blokirana (tj. $a_i = 1$, ili $a_i = 2$ i $i \in S$), zbroj intervala u prazninama lijevo od $i$ iznosi $j$, i $|S \cap [1, i]| \equiv p \pmod 2$. Početno $f(0, 0, 0) = 1$.</p>
<h3>4. Prijelazi</h3>
<p>Iz stanja $(i, j, p)$ biramo sljedeću blokiranu poziciju $i' \in (i, n+1]$. Sve pozicije strogo između moraju biti neblokirane: nule ili dvojke izvan $S$; posebno, ako je $a_{i'} = 1$ za neki $i''$ između, prijelaz nije moguć – zato petlju po $i'$ prekidamo nakon prve jedinice. Praznina $g = i' - i - 1$ donosi $\Delta = \frac{g(g+1)}{2}$ intervala.</p>
<ul>
<li>$a_{i'} = 1$ (uključujući $i' = n+1$): $f(i', j + \Delta, p) \mathrel{+}= f(i, j, p)$, zatim prekid petlje.</li>
<li>$a_{i'} = 2$: pozicija ulazi u $S$: $f(i', j + \Delta, 1 - p) \mathrel{+}= f(i, j, p)$; petlja nastavlja (dvojka može i ostati izvan $S$).</li>
<li>$a_{i'} = 0$: ne može biti blokirana, petlja nastavlja.</li>
</ul>
<p>Svaki podskup $S$ odgovara točno jednom putu kroz DP (niz blokiranih pozicija određuje $S$ i obrnuto), pa je $\sum_{S} (-1)^{|S|} [k(S) = j] = f(n{+}1, j, 0) - f(n{+}1, j, 1)$ i</p>
<p>$$\text{odg} = \sum_{j} \big(f(n{+}1, j, 0) - f(n{+}1, j, 1)\big)\, j^m \pmod{10^9 + 7}.$$</p>
<p>Napomena: parnost $p$ broji samo elemente $S$ (dvojke), ne prave jedinice, pa nije potrebna nikakva korekcija predznaka.</p>
<h3>5. Složenost</h3>
<p>Do pozicije $i$ broj intervala je $\le \frac{i(i+1)}{2}$, pa u stanju $i$ petlju po $j$ vodimo do te granice. Rad je $\sum_{i=0}^{n} (n + 1 - i) \cdot \frac{i(i+1)}{2} \cdot 2 \approx \frac{n^4}{12}$ operacija zbrajanja, za $n = 100$ oko $8 \cdot 10^6$, uz preskakanje nultih stanja još manje; s najviše $50$ testova $n > 50$ ukupno je ispod $10^9$ jednostavnih operacija u limitu od 6 s. Memorija: $(n+2) \cdot 2 \cdot \frac{n(n+1)}{2}$ 64-bitnih brojeva $\approx 8$ MB. Potencije $j^m$ za $j \le 5050$ brzim potenciranjem: $O(n^2 \log m)$.</p>
<h3>6. Zamke</h3>
<ul>
<li>Razlika $f(\cdot, 0) - f(\cdot, 1)$ može biti negativna modulo – dodaj modul prije množenja.</li>
<li>$0^m = 0$ za $m \ge 1$: pribrojnik za $j = 0$ otpada (npr. treći primjer <code>2 1 0</code>, $m = 1$: jedini interval koji pokriva dvojku je $[1,1]$; odgovor $1$).</li>
<li>Ne zaboravi prekid petlje po $i'$ na pravoj jedinici – preskakanje jedinice dalo bi pogrešna stanja.</li>
</ul>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n \le 5$, $m \le 3$) protiv brute forcea koji nabraja sve nizove od $m$ dopuštenih intervala i provjerava pokrivenost dvojki; 3 velika testa s $T = 60$, $n = 100$, $m$ do $10^9$ (najviše $0.21$ s).''',
},
# ---------------------------------------------------------------- H
{
    'letter': 'H', 'title': 'Mirror', 'title_hr': 'Zrcalo', 'slug': 'H_mirror',
    'tl': '15 s', 'ml': '1024 MiB',
    'statement': r'''
<p>U ravnini su neprozirna trokutasta prepreka i jednostrano zrcalo — usmjerena dužina od $(x_{m,1}, y_{m,1})$ do $(x_{m,2}, y_{m,2})$ čija je desna strana reflektirajuća. U točki $(x_1, y_1)$ je $m$ kamenova koje DreamGrid nosi jedan po jedan do $(x_2, y_2)$; kamen koji podigne smije spustiti samo u cilju. U svakoj točki svog puta mora vidjeti sve kamenove — izravno ili preko zrcala.</p>
<p>Pravila: linija vida koja prolazi unutrašnjošću prepreke ne vrijedi (dodirivanje vrha ili brida je dopušteno); ako linija vida prolazi krajnjom točkom zrcala, vidi i „u zrcalu” i „kroz zrcalo”; refleksija po zakonu odbijanja (upadni i odbijeni zrak u istoj poluravnini); linija vida paralelna zrcalu ne reflektira se i zrcalo tada nije prepreka; DreamGrid se ne smije kretati unutrašnjošću prepreke (smije po bridovima i vrhovima) ni prolaziti kroz zrcalo (smije hodati po njemu, ali s unutrašnjosti zrcala vidi samo stranu s koje je došao).</p>
<p>Odredi najkraći ukupni put za prijenos svih kamenova.</p>
<h3>Ulaz</h3>
<p>$T \approx 100$ testova; $1 \le m \le 10^6$; $x_1, y_1, x_2, y_2$; koordinate zrcala; tri vrha prepreke. Sve koordinate su cijeli brojevi s $|{\cdot}| \le 100$; početak i cilj su izvan prepreke i zrcala; zrcalo i prepreka nemaju zajedničkih točaka; nikoje tri točke nisu kolinearne.</p>
<h3>Izlaz</h3>
<p>Za svaki test realan broj (apsolutna ili relativna greška $\lt 10^{-6}$) ili $-1$ ako je nemoguće.</p>
<h3>Primjer</h3>
<p>$m = 2$, $A = (-2, 0)$, $B = (2, 0)$, zrcalo $(-3, 3) \to (3, 3)$, trokut $(0, 1), (-3, -2), (3, -2)$: $13.416407864999$ (put $A \to C \to B \to C \to A \to C \to B$). Isto, ali zrcalo $(-3, 3) \to (-1, 3)$: $-1$ jer se $A$ ne vidi iz $B$.</p>
''',
    'solution': None,
},
# ---------------------------------------------------------------- I
{
    'letter': 'I', 'title': 'Soldier Game', 'title_hr': 'Igra vojnika', 'slug': 'I_soldier_game',
    'tl': '4 s', 'ml': '256 MiB',
    'statement': r'''
<p>$n$ vojnika sa snagom $a_i$ treba podijeliti u timove od $1$ ili $2$ vojnika; tim od dvojice mora činiti susjedne vojnike ($|i - j| = 1$). Snaga tima je zbroj snaga članova.</p>
<p>Minimiziraj razliku između najveće i najmanje snage tima.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^5$, $-10^9 \le a_i \le 10^9$; $\sum n \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test najmanja razlika.</p>
<h3>Primjer</h3>
<p>$a = (-1, 4, 2, 1, 1) \to 1$ (podjela $[-1, 4], [2], [1, 1]$). $a = (1, 3, 2, 4) \to 2$. $a = (7) \to 0$.</p>
''',
    'hints': [
        r'''
<p>Kandidata za snagu najslabijeg tima ima samo $2n - 1$: vrijednosti $a_i$ i $a_i + a_{i+1}$. Fiksiraj donju granicu $v$ i pitaj: koliki je najmanji mogući maksimum podjele u kojoj su svi timovi $\ge v$?</p>
''',
        r'''
<p>Za fiksan $v$ zadatak je DP po nizu s dva stanja (je li vojnik $i$ vezan s $i+1$). Kad $v$ raste, samo se pojedini timovi „zabrane” – to su točkaste promjene koje segmentno stablo obrađuje u $O(\log n)$.</p>
''',
        r'''
<p>Čvor segmentnog stabla čuva $2 \times 2$ tablicu $f[l][r]$: najmanji maksimum podjele segmenta, gdje $l$ (odnosno $r$) kaže je li lijevi (desni) rubni vojnik u timu koji izlazi iz segmenta. Spajanje: $f[i][j] = \min_k \max(L[i][k], R[k][j])$ – (min, max)-umnožak matrica.</p>
''',
    ],
    'coach': [
        ('Zašto je dovoljno promatrati samo $2n - 1$ vrijednosti donje granice?',
         r'''
<p>U svakoj podjeli najslabiji tim ima snagu iz skupa $V = \{a_i\} \cup \{a_i + a_{i+1}\}$. Za $v \in V$ neka je $M(v)$ najmanji mogući maksimum među podjelama u kojima je svaki tim $\ge v$ ($\infty$ ako nema takve). Optimalna podjela s minimumom $v^*$ i maksimumom $\mu$ daje $M(v^*) \le \mu$, pa je $M(v^*) - v^* \le \mu - v^* = \text{opt}$. Obratno, podjela koja postiže $M(v)$ ima minimum $\ge v$, dakle razliku $\le M(v) - v$, pa je $\text{opt} \le M(v) - v$ za svaki $v$. Zato je $\text{opt} = \min_{v \in V} (M(v) - v)$.</p>
'''),
        ('Kako izračunati $M(v)$ za jedan fiksan $v$?',
         r'''
<p>Dinamičkim programiranjem slijeva: $\mathrm{dp}[i]$ = najmanji maksimum podjele prvih $i$ vojnika; $\mathrm{dp}[i] = \min(\max(\mathrm{dp}[i-1], a_i),\ \max(\mathrm{dp}[i-2], a_{i-1} + a_i))$, uz zabranu timova sa snagom $< v$ (tretiramo ih kao $+\infty$). To je $O(n)$ po $v$, ukupno $O(n^2)$ – previše. No kad $v$ prijeđe na sljedeći kandidat, promijeni se (zabrani) samo tim čija je snaga jednaka prethodnom kandidatu: jedna točkasta promjena.</p>
'''),
        ('Kako DP po nizu pretvoriti u strukturu koja podržava točkaste promjene?',
         r'''
<p>Segmentno stablo nad pozicijama. Za segment $[l, r]$ čuvamo $f[p][q]$, $p, q \in \{0, 1\}$: najmanji maksimum podjele vojnika $l..r$ pri čemu $p = 1$ znači da je vojnik $l$ desni član para $(l-1, l)$ (trošak tog para plaćen je lijevo), a $q = 1$ da je vojnik $r$ lijevi član para $(r, r+1)$ (trošak plaćen ovdje). List $i$: $f[0][0] = a_i$ (sam), $f[0][1] = a_i + a_{i+1}$ (par počinje), $f[1][0] = -\infty$ (član para plaćenog lijevo – neutralno za $\max$), $f[1][1] = +\infty$ (nemoguće). Spajanje lijevog $L$ i desnog $R$: $f[p][q] = \min_{k} \max(L[p][k], R[k][q])$, gdje $k = 1$ znači da par prelazi granicu. To je asocijativan (min, max)-umnožak $2 \times 2$ matrica, pa stablo radi; identitet ima $-\infty$ na dijagonali i $+\infty$ izvan nje (za prazne listove). $M(v) = f_{\text{korijen}}[0][0]$.</p>
'''),
        ('Kako sve zajedno teče i kolika je složenost?',
         r'''
<p>Sortiraj kandidate $(v, \text{list}, \text{tip})$. Za svaki različiti $v$ rastuće: pročitaj $M(v)$ iz korijena i ažuriraj odgovor $M(v) - v$; zatim za svaki tim snage točno $v$ postavi njegovu vrijednost u listu na $+\infty$ i prepravi put do korijena. Ukupno $2n - 1$ ažuriranja po $O(\log n)$, plus sortiranje: $O(n \log n)$. Ako je $M(v) = \infty$ (nema podjele bez slabih timova), preskoči. Snage do $2 \cdot 10^9$ po apsolutnoj vrijednosti: 64-bitni tip, a $\infty$ neka bude npr. $\mathrm{LLONG\_MAX}/4$ da zbrajanja ne preliju.</p>
'''),
    ],
    'tips': [
        r'''„Minimiziraj (max − min)” često se rješava fiksiranjem minimuma (ili maksimuma) iz malog skupa kandidata i optimiranjem druge veličine.''',
        r'''DP po nizu s konstantno mnogo stanja može se ubaciti u segmentno stablo kao umnožak malih matrica u (min, max) ili (min, +) polugrupi – time točkaste promjene ulaza koštaju $O(\log n)$.''',
        r'''Kad zabranjivanje elemenata ide monotono (rastući prag), sve promjene su „jednosmjerne” i njihov je broj linearan – idealno za offline obradu sortiranih kandidata.''',
        r'''Za $-\infty/+\infty$ u (min, max)-algebri koristi vrijednosti reda $\pm\mathrm{LLONG\_MAX}/4$ i nikad ih ne zbrajaj.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi): najslabiji tim ima snagu iz skupa od $2n - 1$ kandidata $\{a_i\} \cup \{a_i + a_{i+1}\}$. Za rastući prag $v$ zabranjujemo timove snage $< v$ i tražimo $M(v)$ = najmanji mogući maksimum podjele; odgovor je $\min_v (M(v) - v)$. $M(v)$ daje segmentno stablo čiji čvor čuva $2 \times 2$ tablicu $f[l][r]$ (najmanji maksimum podjele segmenta, $l$/$r$ = rubni vojnik pripada paru koji prelazi granicu), spajanje $f[i][j] = \min_k \max(L[i][k], R[k][j])$; prelazak na sljedeći kandidat je točkasto ažuriranje lista (tim $\to +\infty$). Složenost $O(n \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Fiksiranje minimuma</h3>
<p>Neka je $V = \{a_i : 1 \le i \le n\} \cup \{a_i + a_{i+1} : 1 \le i < n\}$, $|V| \le 2n - 1$; snaga svakog tima u bilo kojoj podjeli je element od $V$. Za $v \in V$ definiramo $M(v) = \min\{\max(\text{podjela}) : \text{svi timovi} \ge v\}$ (ili $\infty$).</p>
<p><strong>Tvrdnja.</strong> $\text{opt} = \min_{v \in V} \big(M(v) - v\big)$. <em>Dokaz.</em> ($\le$) Podjela koja postiže $M(v)$ ima sve timove u $[v, M(v)]$, pa joj je razlika $\le M(v) - v$. ($\ge$) Neka optimalna podjela ima minimum $v^* \in V$ i maksimum $\mu$; ona je dopuštena za prag $v^*$, pa $M(v^*) \le \mu$ i $M(v^*) - v^* \le \mu - v^* = \text{opt}$. $\square$</p>
<h3>2. DP za fiksan prag i zašto ga treba ubrzati</h3>
<p>Za fiksan $v$: $\mathrm{dp}[i] = \min\big(\max(\mathrm{dp}[i-1], w(i)),\ \max(\mathrm{dp}[i-2], w(i-1, i))\big)$, gdje su $w(i) = a_i$ i $w(i-1,i) = a_{i-1} + a_i$ snage timova, s tim da se snaga $< v$ zamijeni s $+\infty$. Izravno je to $O(n)$ po pragu, $O(n^2)$ ukupno – preko $10^{10}$ za $n = 10^5$. Ključno: kad $v$ raste na sljedeći kandidat, zabrane se samo timovi snage jednake prethodnom kandidatu. Ukupno je $2n - 1$ točkastih promjena, pa želimo strukturu koja nakon točkaste promjene vraća $\mathrm{dp}[n]$ u $O(\log n)$.</p>
<h3>3. Segmentno stablo s $2 \times 2$ tablicama</h3>
<p>Za segment vojnika $[l, r]$ definiramo $f[p][q]$ ($p, q \in \{0,1\}$) kao najmanji mogući maksimum troškova timova „pripisanih” segmentu, uz rubne uvjete: $p = 1$ znači da je vojnik $l$ desni član para $(l-1, l)$ čiji je trošak pripisan segmentu lijevo; $q = 1$ znači da je vojnik $r$ lijevi član para $(r, r+1)$ čiji trošak $a_r + a_{r+1}$ pripisujemo ovom segmentu. Trošak para uvijek pripisujemo segmentu koji sadrži njegov lijevi član.</p>
<p><em>Listovi.</em> Za vojnika $i$: $f[0][0] = w(i)$, $f[0][1] = w(i, i+1)$ (za $i = n$: $+\infty$), $f[1][0] = -\infty$ (vojnik je u paru koji je već plaćen; ništa se ne pripisuje, a $-\infty$ je neutralni element za $\max$), $f[1][1] = +\infty$ (vojnik ne može biti u dva para).</p>
<p><em>Spajanje.</em> Za lijevi segment $L$ i desni $R$ koji se dodiruju: $$f[p][q] = \min_{k \in \{0,1\}} \max\big(L[p][k],\ R[k][q]\big),$$ gdje $k = 1$ znači da posljednji vojnik od $L$ i prvi od $R$ čine par (trošak plaćen u $L$). Ispravnost: svaka podjela segmenta $[l, r]$ s rubnim stanjima $(p, q)$ jednoznačno se rastavlja na podjelu lijeve polovice s rubovima $(p, k)$ i desne s $(k, q)$, a maksimum unije troškova je maksimum maksimuma; minimiziranje po svim podjelama = minimiziranje po $k$ i po podjelama polovica. Operacija je asocijativna (to je umnožak matrica u polugrupi $(\min, \max)$), pa segmentno stablo daje ispravan rezultat za korijen. Za veličinu stabla koja je potencija dvojke prazni listovi dobivaju identitet: $-\infty$ na dijagonali, $+\infty$ izvan nje.</p>
<p>Tada je $M(v) = f_{\text{korijen}}[0][0]$ (nijedan par ne prelazi rubove cijelog niza).</p>
<h3>4. Cijeli algoritam</h3>
<ol>
<li>Izgradi stablo sa svim timovima dopuštenima.</li>
<li>Sastavi listu kandidata $(v, i, \text{tip})$: $(a_i, i, \text{sam})$ i $(a_i + a_{i+1}, i, \text{par})$; sortiraj po $v$.</li>
<li>Za svaku različitu vrijednost $v$ rastuće: $M = f_{\text{korijen}}[0][0]$; ako je $M < \infty$, $\text{ans} = \min(\text{ans}, M - v)$. Zatim za sve kandidate sa snagom točno $v$ postavi odgovarajući element lista ($f[0][0]$ ili $f[0][1]$) na $+\infty$ i prepravi pretke.</li>
</ol>
<p>Nakon što zabranimo sve timove snage $\le v$, korijen daje $M(v')$ za sljedeći kandidat $v'$ – upravo ono što treba. Prvi primjer $a = (-1, 4, 2, 1, 1)$: za $v = 2$ (timovi $\ge 2$: $[-1,4] = 3$, $[4] = 4$, $[2] = 2$, $[2,1] = 3$, $[1,1] = 2$, $[4,2] = 6$) najmanji maksimum je $3$ (podjela $[-1,4],[2],[1,1]$), razlika $1$; za ostale $v$ razlika nije manja.</p>
<h3>5. Složenost i zamke</h3>
<p>Izgradnja $O(n)$, sortiranje $O(n \log n)$, $2n - 1$ ažuriranja po $O(\log n)$: ukupno $O(n \log n)$ po testu, uz $\sum n \le 10^6$ oko $4 \cdot 10^7$ spajanja $2 \times 2$ tablica. Snage do $\pm 2 \cdot 10^9$ pa je nužan 64-bitni tip; $\pm\infty$ biraj kao $\pm\mathrm{LLONG\_MAX}/4$ (nikad se ne zbrajaju, samo uspoređuju). Za $n = 1$ jedina podjela je $[a_1]$, odgovor $0$. Pazi da $M = \infty$ (nema valjane podjele) ne uđe u odgovor.</p>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n \le 9$, $|a_i| \le 6$) protiv brute forcea koji nabraja sve $2^{n-1}$ podjele na timove; 3 velika testa s $T = 2$, $n = 10^5$, $|a_i| \le 10^9$ (najviše $0.20$ s).''',
},
# ---------------------------------------------------------------- J
{
    'letter': 'J', 'title': 'Books', 'title_hr': 'Knjige', 'slug': 'J_books',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>U knjižari je $n$ knjiga s cijenama $a_i$. DreamGrid ih pregledava redom $1..n$; ako ima dovoljno novca (barem cijena knjige), kupuje je i novac mu se smanji za cijenu, inače je preskače. Poznato je da je kupio točno $m$ knjiga.</p>
<p>Odredi najveću moguću početnu količinu novca (nenegativan cijeli broj).</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^5$, $0 \le m \le n$, $0 \le a_i \le 10^9$; $\sum n \le 10^6$.</p>
<h3>Izlaz</h3>
<p><code>Impossible</code> ako ni za koju početnu količinu ne kupuje točno $m$ knjiga; <code>Richman</code> ako novac može biti neograničen; inače najveća količina.</p>
<h3>Primjer</h3>
<p>$a = (1, 2, 4, 8)$, $m = 2 \to 6$. $a = (100, 99, 98, 97)$, $m = 0 \to 96$. $a = (10000, 10000)$, $m = 2 \to$ <code>Richman</code>. $a = (0, 0, 0, 0, 1)$, $m = 3 \to$ <code>Impossible</code>.</p>
''',
    'hints': [
        r'''
<p>Knjige cijene $0$ kupuju se uvijek, bez obzira na novac. Što to znači ako je $m$ manji od broja nula, a što ako je $m = n$?</p>
''',
        r'''
<p>Ako je poznato koliko će knjiga s pozitivnom cijenom biti kupljeno, koje točno će to biti? Razmisli o tome da se knjige obilaze redom i da novac samo pada.</p>
''',
        r'''
<p>Kad je skup kupljenih knjiga fiksiran, najviše novca je „zbroj kupljenih plus najjeftinija nekupljena minus jedan”. Zašto točno tako, i zašto postoji nekupljena knjiga?</p>
''',
    ],
    'coach': [
        ('Koje knjige BaoBao kupuje bez obzira na iznos novca i što to odmah rješava?',
         r'''
<p>Knjige cijene $0$: uvjet „novac $\ge$ cijena” uvijek vrijedi. Neka ih je $z$. Ako je $m < z$, nemoguće je kupiti samo $m$ knjiga: <code>Impossible</code>. Ako je $m = n$, novac možemo uzeti beskonačno velik: <code>Richman</code>. Inače $m < n$ i $m \ge z$.</p>
'''),
        ('Ako znamo da će se kupiti točno $k = m - z$ knjiga pozitivne cijene, koje su to?',
         r'''
<p>Uvijek prvih $k$ pozitivnih knjiga u redoslijedu obilaska. Naime, pretpostavimo da je s nekim iznosom kupljena pozitivna knjiga $j$, a preskočena pozitivna knjiga $i < j$. U trenutku $i$ novac je bio barem toliki kao u trenutku $j$ (novac samo pada), a ipak $a_i >$ novac $\ge a_j$. To je moguće, ali tada postoji strogo bolji iznos? Ne trebamo to; dovoljno je primijetiti sljedeće: skup kupljenih knjiga jednoznačno je određen iznosom, a mi tražimo <em>najveći</em> iznos s točno $m$ kupljenih. Za najveći iznos tvrdimo da se kupuje baš prvih $k$ pozitivnih: idući korak pokazuje da je iznos $S + p - 1$ ostvariv s prvih $k$ knjiga, a svaki iznos $\ge S + p$ kupuje barem $k + 1$ pozitivnih knjiga (kupuje sve prve $k$ jer je novac u trenutku svake od njih barem $S + p - (\text{zbroj prethodnih}) \ge$ njena cijena, i još stigne do knjige cijene $p$ s barem $p$ novca).</p>
'''),
        ('Zašto je odgovor $S + p - 1$, gdje je $S$ zbroj prvih $k$ pozitivnih knjiga, a $p$ najmanja cijena među preostalim pozitivnim knjigama?',
         r'''
<p>S iznosom $S + p - 1$: kad dođemo do $i$-te od prvih $k$ pozitivnih knjiga, imamo $S + p - 1 - (\text{zbroj prethodnih}) \ge a_i + p - 1 \ge a_i$, pa je kupujemo; nakon svih $k$ ostaje $p - 1$, što je manje od svake preostale cijene (sve su $\ge p$), pa ne kupujemo više ništa. Točno $m$ knjiga. S iznosom $S + p$ ili većim kupili bismo i knjigu cijene $p$ (pokazano u prethodnom koraku), dakle više od $m$. Zato je $S + p - 1$ maksimum.</p>
'''),
        ('Zašto uvijek postoji „najjeftinija preostala” knjiga i na što paziti pri računanju?',
         r'''
<p>Jer je $m < n$: kupujemo $z$ nula i $k = m - z$ pozitivnih, dakle $n - m \ge 1$ pozitivnih ostaje. Zbroj $S$ može biti do $10^5 \cdot 10^9 = 10^{14}$, pa treba 64-bitni tip. Redoslijed provjera: prvo $m = n$ (<code>Richman</code>), zatim $m < z$ (<code>Impossible</code>).</p>
'''),
    ],
    'tips': [
        r'''Pohlepni proces koji ovisi o parametru („novac”) je monoton: veći iznos kupuje nadskup knjiga. Traženi ekstrem tada je „točka prije prve promjene”, ovdje $S + p - 1$.''',
        r'''Elemente koji se biraju bez obzira na parametar (cijena $0$) izdvoji odmah – oni određuju rubne slučajeve <code>Impossible</code>/<code>Richman</code>.''',
        r'''Kad zadatak ima posebne izlaze, prvo napiši te grane pa tek onda glavnu formulu; lako je zaboraviti da se <code>Richman</code> odnosi i na slučaj $m = n$ sa svim nulama.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi): knjige cijene $0$ (ima ih $z$) kupuju se uvijek. Ako je $m = n$, ispiši <code>Richman</code>; ako je $m < z$, <code>Impossible</code>. Inače se kupuje prvih $k = m - z$ knjiga pozitivne cijene (u redoslijedu obilaska), zbroja $S$; neka je $p$ najmanja cijena među preostalim pozitivnim knjigama (postoji jer $m < n$). Odgovor je $S + p - 1$: s tim iznosom kupimo točno tih $k$ knjiga i ostane $p - 1 < p$, a sa $S + p$ kupili bismo i knjigu cijene $p$. Složenost $O(n)$.</p>
''',
    'detailed': r'''
<h3>1. Proces je monoton u novcu</h3>
<p>Za iznos $x$ označimo $K(x)$ skup kupljenih knjiga (obilazak redom, kupi ako je novac $\ge$ cijena). <strong>Tvrdnja.</strong> $x \le y \Rightarrow K(x) \subseteq K(y)$. <em>Dokaz</em> indukcijom po pozicijama: neka je nakon prvih $i - 1$ knjiga preostali novac $x_i$ odnosno $y_i$ i vrijedi $K$-inkluzija na prefiksu te $y_i - x_i \ge \sum_{j \in K(y) \setminus K(x),\, j < i} a_j \ge 0$. Ako $x$ kupi knjigu $i$ ($x_i \ge a_i$), onda i $y_i \ge x_i \ge a_i$ pa je kupi i $y$; razlika $y_{i+1} - x_{i+1} = y_i - x_i$. Ako $x$ ne kupi, a $y$ kupi, razlika se smanji za $a_i$ ali ostaje $\ge 0$ jer $y_i \ge a_i$; ako nitko ne kupi, ništa se ne mijenja. $\square$</p>
<p>Posljedica: $|K(x)|$ je neopadajuća funkcija od $x$, pa je skup iznosa s $|K(x)| = m$ (ako nije prazan) interval $[x_{\min}, x_{\max}]$, eventualno neograničen odozgo. Tražimo $x_{\max}$.</p>
<h3>2. Rubni slučajevi</h3>
<p>Knjige cijene $0$ kupuju se za svaki $x \ge 0$; neka ih je $z$. Ako je $m < z$, $|K(x)| \ge z > m$ za sve $x$: <code>Impossible</code>. Ako je $m = n$, za $x \ge \sum a_i$ kupujemo sve, pa $x_{\max}$ ne postoji: <code>Richman</code>. Inače je $z \le m < n$.</p>
<h3>3. Koje se knjige kupuju za $x_{\max}$</h3>
<p>Neka su pozitivne knjige (cijena $> 0$) u redoslijedu obilaska $b_1, b_2, \dots, b_{n-z}$ i $k = m - z \ge 0$ broj pozitivnih koje treba kupiti. Neka je $S = \sum_{i \le k} b_i$ i $p = \min_{i > k} b_i$ (skup nije prazan jer $n - z > k \Leftrightarrow n > m$).</p>
<p><strong>Tvrdnja.</strong> $|K(S + p - 1)| = m$ i $|K(y)| > m$ za svaki $y \ge S + p$. <em>Dokaz.</em> S iznosom $S + p - 1$, pri dolasku na $b_i$ ($i \le k$) preostali je novac $S + p - 1 - \sum_{j < i} b_j = b_i + \sum_{i < j \le k} b_j + p - 1 \ge b_i$, pa je kupujemo; nule se kupuju uvijek. Nakon $b_k$ ostaje $p - 1$, a svaka daljnja pozitivna cijena je $\ge p$, pa se više ništa ne kupuje: točno $z + k = m$ knjiga. S iznosom $y \ge S + p$: istim računom kupujemo $b_1, \dots, b_k$ (novac je čak veći), a nakon njih ostaje $\ge p$; na knjizi cijene $p$ (nalazi se iza $b_k$) novac je još uvijek $\ge p$ jer između nje i $b_k$ nismo kupili ništa što bi ga smanjilo ispod $p$ – ako smo nešto kupili, već imamo $m + 1$ knjiga; ako nismo, kupimo nju. U oba slučaja $|K(y)| \ge m + 1$. $\square$</p>
<p>Iz monotonosti slijedi $x_{\max} = S + p - 1$.</p>
<h3>4. Algoritam</h3>
<ol>
<li>Pročitaj $n, m, a$. Ako je $m = n$: <code>Richman</code>.</li>
<li>Prebroji nule $z$. Ako je $m < z$: <code>Impossible</code>.</li>
<li>Prođi niz; prvih $m - z$ pozitivnih cijena zbroji u $S$, od ostalih pozitivnih uzmi minimum $p$.</li>
<li>Ispiši $S + p - 1$.</li>
</ol>
<p>Složenost $O(n)$ vremena i $O(1)$ dodatne memorije po testu.</p>
<h3>5. Zamke</h3>
<p>$S$ do $10^{14}$: 64-bitni tip. Slučaj $k = 0$ (sve kupljene knjige su nule) daje $S = 0$ i odgovor $p - 1$, npr. drugi primjer $m = 0$, $a = (100, 99, 98, 97)$ daje $96$. Provjera $m = n$ mora doći prije provjere s nulama (npr. $n = m = 2$, $a = (0, 0)$ je <code>Richman</code>).</p>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n \le 7$, cijene $0..6$, svi $m$) protiv brute forcea koji simulira kupnju za svaki iznos do $\sum a + 1$; 3 velika testa s $n = 10^5$ i cijenama do $10^9$ (najviše $0.07$ s).''',
},
# ---------------------------------------------------------------- K
{
    'letter': 'K', 'title': 'Airdrop', 'title_hr': 'Zračna pošiljka', 'slug': 'K_airdrop',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>Pošiljka je pala u $(x_0, y_0)$; $n$ igrača kreće iz $(x_i, y_i)$. U svakoj jedinici vremena igrač koji nije u $(x_0, y_0)$ prelazi u onu od točaka $(x, y-1), (x, y+1), (x-1, y), (x+1, y)$ koja je Manhattan udaljenošću najbliža pošiljci; pri izjednačenju prioritet je tim redom. Igrač na pošiljci ostaje tamo. Ako se dva ili više igrača nađu u istoj točki različitoj od $(x_0, y_0)$, svi oni ginu.</p>
<p>Poznat je $y_0$, ali ne $x_0$. Po svim cijelim $x_0$ odredi najmanji i najveći mogući broj igrača koji stignu do pošiljke.</p>
<h3>Ulaz</h3>
<p>$T$ testova; $1 \le n \le 10^5$, $1 \le y_0 \le 10^5$, $1 \le x_i, y_i \le 10^5$, sve početne pozicije različite; $\sum n \le 10^6$.</p>
<h3>Izlaz</h3>
<p>Za svaki test <code>p_min p_max</code>.</p>
<h3>Primjer</h3>
<p>$y_0 = 2$, igrači $(1,2), (2,1), (3,5)$: <code>1 3</code> ($x_0 = 3$ daje $1$: prva dva se sudaraju u $(2,2)$; $x_0 = 2$ daje $3$). $y_0 = 3$, igrači $(2,1), (2,5), (4,3)$: <code>0 3</code>. $y_0 = 3$, igrači $(1,3), (4,3)$: <code>2 2</code>.</p>
''',
    'hints': [
        r'''
<p>Zbog prioriteta smjerova igrač se najprije giba okomito do reda $y_0$, a tek zatim vodoravno. Kad se dva igrača mogu naći u istoj točki u istom trenutku?</p>
''',
        r'''
<p>Igrači s različitih strana od $x_0$ mogu se sresti samo u samoj pošiljci, a igrači u stupcu $x_0$ nikad ne ginu. Dva igrača lijevo od $x_0$ sudaraju se točno kad imaju jednaku udaljenost $d = |y_i - y_0| + (x_0 - x_i)$, tj. jednak $k = |y_i - y_0| - x_i$, što ne ovisi o $x_0$!</p>
''',
        r'''
<p>Za lijevu stranu obrađuj stupce rastuće po $x$: skupina žive klase $k$ stiže u stupac $x$ točno kad ondje „slijeću” novi igrači klase $k$; klasa preživi točno ako je (živi + novi) $= 1$. Isto zdesna padajuće. Vrijednost ovisi o $x_0$ samo kroz to koji su stupci lijevo/desno – kandidati $x_i - 1, x_i, x_i + 1$.</p>
''',
    ],
    'coach': [
        ('Kako se točno giba jedan igrač?',
         r'''
<p>Dok je $y \ne y_0$, jedan od poteza $(x, y \mp 1)$ smanjuje Manhattan udaljenost, a oni imaju prioritet pred vodoravnima: igrač ide okomito do reda $y_0$, za $|y_i - y_0|$ koraka, i stiže u $(x_i, y_0)$ u trenutku $\delta_i = |y_i - y_0|$. Zatim ide vodoravno prema $x_0$ i stiže u trenutku $d_i = \delta_i + |x_i - x_0|$. Ako je $x_i = x_0$, igrač je već na cilju nakon okomitog dijela.</p>
'''),
        ('Koji se parovi igrača mogu sudariti?',
         r'''
<p>Sudar je ista točka u istom trenutku, izvan pošiljke. Igrač lijevo od $x_0$ u trenutku $t \ge \delta_i$ nalazi se u $(x_0 - (d_i - t), y_0)$, dakle strogo lijevo od $x_0$ do dolaska; igrač desno je strogo desno; igrač u stupcu $x_0$ je na okomici $x = x_0$ izvan reda $y_0$ ili na cilju. Zato se igrači s <em>različitih</em> strana ne mogu sresti izvan cilja, a igrači stupca $x_0$ ne ginu nikad (dva igrača u istom stupcu s iste strane reda $y_0$ zadržavaju razmak, s različitih strana sreću se samo u $(x_0, y_0)$, tj. na cilju). Dva igrača lijevo od $x_0$: u vodoravnoj fazi oba su u $x_0 - (d_i - t)$, pa se preklapaju točno ako $d_i = d_j$, tj. $\delta_i - x_i = \delta_j - x_j$. Ako je $d_i = d_j$, doista se sretnu: onaj s manjim $x$ ima manji $\delta$, stiže u red ranije i u trenutku $\delta_j$ nalazi se točno u $(x_j, y_0)$ – gdje igrač $j$ upravo silazi. (Sudar u okomitoj fazi, isti stupac i različite strane reda, isti je slučaj: $d_i = d_j$.)</p>
'''),
        ('Kako prebrojati preživjele s jedne strane za zadani $x_0$?',
         r'''
<p>Za lijevu stranu klasa igrača je $k_i = \delta_i - x_i$; svi u klasi imaju istu udaljenost $d = k + x_0$ i putuju kao jedna „skupina” po redu $y_0$. Skupina stiže u stupac $x$ točno u trenutku kad igrači klase $k$ iz stupca $x$ silaze u red. Ako je u tom trenutku u točki $(x, y_0)$ više od jednog igrača (živi u skupini + novi iz stupca), svi ginu; ako je točno jedan, on nastavlja. Dakle obrađujemo stupce lijevo od $x_0$ redom rastuće po $x$ i za svaku klasu držimo indikator „skupina živa”: $\text{živa}' = [\text{živa} + \text{novi} = 1]$. Broj živih klasa nakon svih stupaca $< x_0$ je broj preživjelih slijeva. Zdesna simetrično s $k_i = \delta_i + x_i$ i stupcima padajuće.</p>
'''),
        ('Kako obraditi sve $x_0$ odjednom i zašto su dovoljni kandidati $x_i \\pm 1$, $x_i$?',
         r'''
<p>Lijeva strana ovisi o $x_0$ samo kroz skup stupaca $x < x_0$; obrađujemo ih rastuće i broj živih klasa prati se inkrementalno („sweep” po $x_0$). Desna strana ovisi o stupcima $x > x_0$: obradimo ih unaprijed padajuće i spremimo broj živih klasa nakon svakog stupca (sufiksne vrijednosti). Igrači sa $x_i = x_0$ svi prežive. Odgovor za $x_0$ je zbroj tih triju veličina. Kao funkcija od $x_0$ vrijednost se može mijenjati samo kad $x_0$ prijeđe neki stupac, pa je konstantna na intervalima između susjednih stupaca; kandidati $x_i - 1$, $x_i$, $x_i + 1$ pokrivaju svaki takav interval i svaki stupac. Složenost $O(n \log n)$ zbog sortiranja (ili $O(n + 10^5)$ s brojanjem), s nizovima indeksiranima pomaknutim ključem $k + 10^5$.</p>
'''),
    ],
    'tips': [
        r'''Prvo ručno izvedi trajektoriju jednog igrača iz pravila prioriteta; često se cijela simulacija svede na zatvorenu formulu (okomito pa vodoravno).''',
        r'''Za sudare pronađi invarijantu para koja ne ovisi o nepoznatom parametru (ovdje $\delta_i - x_i$ za lijevu stranu) – time se isti predračun koristi za sve $x_0$.''',
        r'''Kad odgovor ovisi o parametru samo kroz „koji su elementi lijevo/desno”, radi sweep: prefiks slijeva inkrementalno, sufiks zdesna predračunat.''',
        r'''Kandidate za cjelobrojni parametar biraj kao sve točke prekida $\pm 1$; time se pokriva i svaki otvoreni interval između njih.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi): zbog prioriteta smjerova igrač ide okomito do reda $y_0$ (za $\delta_i = |y_i - y_0|$ koraka), pa vodoravno. Igrači s različitih strana od $x_0$ sreću se samo na cilju, igrači u stupcu $x_0$ uvijek prežive, a dva igrača lijevo od $x_0$ sudaraju se točno kad imaju istu udaljenost, tj. istu klasu $k = \delta_i - x_i$ (neovisno o $x_0$). Klasa putuje kao skupina: obradimo stupce rastuće po $x$ i klasa je živa nakon stupca točno ako je (živi + novi u stupcu) $= 1$; zdesna simetrično ($k = \delta_i + x_i$, stupci padajuće, sufiksne vrijednosti predračunate). Sweep po kandidatima $x_0 \in \{x_i - 1, x_i, x_i + 1\}$ zbraja lijeve žive klase, igrače u stupcu $x_0$ i desni sufiks; složenost $O(n \log n)$.</p>
''',
    'detailed': r'''
<h3>1. Putanja igrača</h3>
<p>Neka je $\delta_i = |y_i - y_0|$. Dok je $y \ne y_0$, jedan od okomitih poteza smanjuje Manhattan udaljenost za $1$, a ni jedan potez ne može smanjiti više; okomiti potezi imaju prioritet, pa igrač $\delta_i$ koraka ide okomito i u trenutku $\delta_i$ nalazi se u $(x_i, y_0)$. Nakon toga, ako je $x_i \ne x_0$, svaki korak ide vodoravno prema $x_0$ i stiže u trenutku $d_i = \delta_i + |x_i - x_0|$. Položaj u trenutku $t$: za $t \le \delta_i$ točka $(x_i, y_i \pm t)$; za $\delta_i \le t \le d_i$ točka $(x_0 \mp (d_i - t), y_0)$ (minus za igrača lijevo, plus desno).</p>
<h3>2. Tko se može sudariti</h3>
<p><strong>Lema 1.</strong> Igrači s različitih strana od $x_0$ (jedan s $x_i < x_0$, drugi s $x_j > x_0$) ne sudaraju se. <em>Dokaz.</em> Igrač $i$ je u svakom trenutku prije dolaska u točki s $x < x_0$ (okomita faza: $x = x_i$; vodoravna: $x_0 - (d_i - t) < x_0$), igrač $j$ u točki s $x > x_0$. $\square$</p>
<p><strong>Lema 2.</strong> Igrač s $x_i = x_0$ nikad ne gine. <em>Dokaz.</em> Do dolaska je u $(x_0, y)$ s $y \ne y_0$. Igrači drugih stupaca su u okomitoj fazi u svom stupcu, a u vodoravnoj fazi u redu $y_0$ – nikad u $(x_0, y)$, $y \ne y_0$. Drugi igrač iz stupca $x_0$: ako je s iste strane reda $y_0$, razmak im je konstantan; ako je s druge strane, susreću se samo u $(x_0, y_0)$, a to je pošiljka. $\square$</p>
<p><strong>Lema 3.</strong> Dva igrača lijevo od $x_0$ sudaraju se točno ako je $d_i = d_j$, tj. $\delta_i - x_i = \delta_j - x_j$. <em>Dokaz.</em> U okomitoj fazi igrač je u svom stupcu; dva igrača u istom stupcu ($x_i = x_j$) sreću se prije reda $y_0$ samo ako su s različitih strana reda i $\delta_i = \delta_j$ (tada se sretnu točno u $(x_i, y_0)$) – to je slučaj $d_i = d_j$. Okomiti igrač u $(x_i, y)$, $y \ne y_0$, ne može sresti vodoravnog (u redu $y_0$). U vodoravnoj fazi položaji su $x_0 - (d_i - t)$ i $x_0 - (d_j - t)$: jednaki za neki $t$ točno ako $d_i = d_j$. Ako je $d_i = d_j$ i, recimo, $x_i < x_j$, tada je $\delta_i = \delta_j - (x_j - x_i) < \delta_j$, pa igrač $i$ ulazi u red ranije i u trenutku $\delta_j$ nalazi se u $x_0 - (d - \delta_j) = x_j$: točno gdje igrač $j$ ulazi u red. Sudar se dogodi (osim ako je $x_j = x_0$, što je isključeno). $\square$</p>
<h3>3. Klase i skupine</h3>
<p>Za lijevu stranu definiramo klasu $k_i = \delta_i - x_i$; $d_i = k_i + x_0$, pa je klasa ista stvar kao udaljenost, ali <em>ne ovisi o $x_0$</em>. Svi živi igrači klase $k$ u vodoravnoj fazi nalaze se u istoj točki i gibaju se kao skupina; skupina je u stupcu $x$ u trenutku $k + x$, upravo kad igrači klase $k$ iz stupca $x$ (za njih $\delta = k + x$) ulaze u red. Tada se u točki $(x, y_0)$ nađe (broj živih u skupini) $+$ (broj novih iz stupca $x$ s klasom $k$) igrača; ako ih je $\ge 2$ svi ginu (skupina postaje prazna), ako je točno $1$ on nastavlja. Broj živih u skupini uvijek je $0$ ili $1$. Obradom stupaca $x < x_0$ rastuće dobivamo za svaku klasu je li živa nakon zadnjeg stupca; zbroj živih klasa je broj preživjelih slijeva.</p>
<p>Desna strana je zrcalna: klasa $k_i = \delta_i + x_i$, stupci $x > x_0$ obrađuju se padajuće.</p>
<h3>4. Svi $x_0$ odjednom</h3>
<p>Neka su različiti stupci $x^{(1)} < \dots < x^{(C)}$. Odgovor za $x_0$ je $$\mathrm{Ans}(x_0) = \mathrm{L}(\{c : x^{(c)} < x_0\}) + |\{i : x_i = x_0\}| + \mathrm{R}(\{c : x^{(c)} > x_0\}),$$ gdje su $L$, $R$ brojevi živih klasa nakon obrade navedenih stupaca. $R$ za svaki sufiks stupaca predračunamo jednim prolazom padajuće (sprem $R_c$ = živih nakon obrade stupaca $c..C$). $L$ računamo inkrementalno dok $x_0$ raste (sweep), obrađujući stupce $x^{(c)} < x_0$ kad ih $x_0$ prijeđe.</p>
<p>Za $x_0$ strogo između dva susjedna stupca ili izvan svih, vrijednost ovisi samo o tome koji su stupci lijevo/desno, pa je konstantna na tim intervalima; zato su kandidati $x^{(c)} - 1$, $x^{(c)}$, $x^{(c)} + 1$ dovoljni (pokrivaju svaki stupac i svaki interval između, uključujući $x_0 < x^{(1)}$ i $x_0 > x^{(C)}$). Zadatak dopušta bilo koji cijeli $x_0$ (i izvan $[1, 10^5]$), što ovi kandidati također pokrivaju.</p>
<h3>5. Složenost i implementacija</h3>
<p>Sortiranje po $x$: $O(n \log n)$; sve ostalo linearno. Ključevi klasa su u $[-10^5, 2 \cdot 10^5]$, pa koristimo nizove s pomakom umjesto mape; nizove „živa klasa” i „novi u stupcu” treba očistiti nakon svakog prolaza (samo dirane ključeve, zbog $\sum n \le 10^6$). U stupcu s više igrača iste klase obradu radimo jednom po klasi (zato brojimo <em>nove</em> pa tek onda odlučujemo). Primjer 1 ($y_0 = 2$; $(1,2), (2,1), (3,5)$): za $x_0 = 3$ igrači $(1,2)$ i $(2,1)$ imaju lijeve klase $0 - 1 = -1$ i $1 - 2 = -1$ – ista klasa, sudar u $(2,2)$; preživi samo $(3,5)$ (stupac $x_0$): $1$. Za $x_0 = 2$: $(1,2)$ lijevo sam, $(2,1)$ u stupcu, $(3,5)$ desno sam: $3$.</p>
<h3>6. Zamke</h3>
<ul>
<li>Igrači u stupcu $x_0$ uvijek prežive – ne stavljaj ih ni u lijevu ni u desnu obradu.</li>
<li>Sudar u okomitoj fazi (isti stupac, različite strane reda, ista $\delta$) već je obuhvaćen jednakošću klasa, ne treba ga posebno.</li>
<li>Kandidati moraju uključivati $x^{(1)} - 1$ i $x^{(C)} + 1$ (svi igrači s iste strane). U drugom primjeru ($y_0 = 3$; $(2,1), (2,5), (4,3)$) minimum $0$ postiže se za $x_0 \le 1$: svi su desno, s desnim klasama $\delta + x = 4, 4, 4$; stupac $4$ daje jednog živog, a u stupcu $2$ skupina (1 živi) susreće 2 nova pa svi ginu. Brute force koji doslovno simulira pravila neprocjenjiv je za provjeru ovakvih slučajeva.</li>
</ul>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n \le 6$, koordinate $\le 6$) protiv brute forcea koji doslovno simulira kretanje po pravilima za svaki $x_0$ u širokom rasponu; 3 velika testa s $n = 10^5$ (gusti i rijetki rasporedi; najviše $0.05$ s).''',
},
# ---------------------------------------------------------------- L
{
    'letter': 'L', 'title': 'Sub-cycle Graph', 'title_hr': 'Podciklički graf', 'slug': 'L_sub_cycle_graph',
    'tl': '2 s', 'ml': '512 MiB',
    'statement': r'''
<p>Jednostavan neusmjeren graf s $n \ge 3$ označenih vrhova i $m$ bridova je <em>podciklički</em> ako mu se dodavanjem nenegativnog broja bridova može dobiti točno jedan jednostavan ciklus na svih $n$ vrhova (povezan graf, svaki vrh stupnja $2$).</p>
<p>Za dane $n$ i $m$ prebroji podcikličke grafove (grafovi su različiti ako imaju različite skupove bridova), modulo $10^9 + 7$.</p>
<h3>Ulaz</h3>
<p>$T \approx 2 \cdot 10^4$ testova; $3 \le n \le 10^5$, $0 \le m \le \frac{n(n-1)}{2}$; $\sum n \le 3 \cdot 10^7$.</p>
<h3>Izlaz</h3>
<p>Za svaki test broj grafova modulo $10^9 + 7$.</p>
<h3>Primjer</h3>
<p>$(4, 2) \to 15$; $(4, 3) \to 12$; $(5, 3) \to 90$.</p>
''',
    'hints': [
        r'''
<p>Kad je graf s $m$ bridova podgraf nekog ciklusa na svim $n$ vrhovima? Razmisli o stupnjevima i o tome što se dogodi ako graf sadrži ciklus, a $m < n$.</p>
''',
        r'''
<p>Za $m < n$ graf mora biti unija $n - m$ vršno disjunktnih puteva (izolirani vrh je put s jednim vrhom). Prebroji takve grafove tako da fiksiraš broj $j$ puteva s barem dva vrha.</p>
''',
        r'''
<p>Rasporedi $i$ vrhova u niz ($i!$), reži ga na $j$ komada duljine $\ge 2$ (kompozicije: $\binom{i-j-1}{j-1}$), pa podijeli s $2^j j!$ zbog smjera i poretka puteva. Slučaj $m = n$ je Hamiltonov ciklus: $(n-1)!/2$.</p>
''',
    ],
    'coach': [
        ('Kako izgleda graf koji je podgraf ciklusa kroz sve vrhove?',
         r'''
<p>Ciklus kroz sve vrhove ima svaki stupanj $2$, pa podgraf ima stupnjeve $\le 2$. Ako podgraf sadrži ciklus, taj ciklus je dio Hamiltonova ciklusa, a jedini ciklus sadržan u ciklusu je on sam: podgraf je cijeli Hamiltonov ciklus i $m = n$. Ako je $m > n$, odgovor je $0$. Za $m < n$ graf je acikličan sa stupnjevima $\le 2$: disjunktna unija puteva, i to točno $n - m$ puteva (svako stablo sa $v$ vrhova ima $v - 1$ bridova, pa je broj komponenata $n - m$). Obrat: svaki takav skup puteva može se spojiti u ciklus (poveži krajeve puteva redom), pa su to točno podciklički grafovi.</p>
'''),
        ('Kako prebrojati particije na $k = n - m$ puteva?',
         r'''
<p>Razdvojimo puteve s jednim vrhom (izolirani) od onih s barem dva. Neka ih je $j$ „pravih”; izoliranih je $k - j$ i biramo ih na $\binom{n}{k-j}$ načina. Preostaje $i = n - (k - j)$ vrhova rasporediti u $j$ puteva s po $\ge 2$ vrha. Poredajmo tih $i$ vrhova u niz na $i!$ načina i režimo ga na $j$ uzastopnih komada duljine $\ge 2$: to je kompozicija broja $i$ na $j$ dijelova $\ge 2$, tj. kompozicija broja $i - j$ na $j$ pozitivnih dijelova, kojih je $\binom{i-j-1}{j-1}$. Svaki skup puteva tako je prebrojan $2^j j!$ puta (svaki put u dva smjera, putevi u $j!$ poredaka).</p>
'''),
        ('Kako sve zajedno izgleda kao formula i kolika je složenost?',
         r'''
<p>$$\text{odg} = \sum_{j=0}^{k} \binom{n}{k-j} \cdot \frac{(n-k+j)!}{2^j\, j!} \cdot \binom{n-k-1}{j-1},$$ uz $i = n - k + j \ge 2j$ i uz dogovor da je za $j = 0$ pribrojnik $1$ ako je $i = 0$ (svi vrhovi izolirani, $m = 0$), inače $0$. Za $m = n$ odgovor je $(n-1)!/2$ (Hamiltonovi ciklusi), za $m > n$ nula. Uz predračun faktorijela, inverza i potencija od $2^{-1}$ svaki test je $O(k) = O(n)$, a $\sum n \le 3 \cdot 10^7$.</p>
'''),
        ('Zašto je izraz $\x08inom{n-k-1}{j-1}$ neovisan o $j$ u gornjem indeksu i što s $j = 0$?',
         r'''
<p>Jer $i - j - 1 = (n - k + j) - j - 1 = n - k - 1 = m - 1$: broj kompozicija ovisi samo o broju bridova. Za $j = 0$ nema pravih puteva, pa moraju svi vrhovi biti izolirani ($m = 0$): tada je $\binom{n}{k}=1$ i pribrojnik je $1$; za $m > 0$ i $j = 0$ pribrojnik je $0$ (nemoguće). Modularno: koristi $\binom{a}{b} = 0$ za $b < 0$ ili $b > a$, pa formula sama daje ispravne nule za $m = 0$, $j \ge 1$.</p>
'''),
    ],
    'tips': [
        r'''„Podgraf ciklusa/puta/stabla” najprije opiši strukturno (stupnjevi, acikličnost, broj komponenata) – prebrojavanje tada postane standardna kombinatorika.''',
        r'''Za prebrojavanje skupova puteva koristi „poredaj pa reži”: $i!$ poredaka, kompozicije za rezove, pa podijeli simetrijama ($2$ po putu, $j!$ za poredak puteva).''',
        r'''Kompozicije broja $i$ na $j$ dijelova $\ge 2$: $\binom{i-j-1}{j-1}$ (oduzmi $1$ od svakog dijela).''',
        r'''Uz $\sum n \le 3 \cdot 10^7$ i puno testova predračunaj sve tablice jednom, a po testu radi samo $O(n)$ množenja bez potenciranja.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi): graf s $m$ bridova je podciklički točno kad je za $m = n$ Hamiltonov ciklus ($(n-1)!/2$ načina), za $m > n$ nikad, a za $m < n$ kad je disjunktna unija $k = n - m$ puteva (izolirani vrh je put). Fiksiraj broj $j$ puteva s $\ge 2$ vrha: izoliranih je $k - j$ ($\binom{n}{k-j}$ izbora), preostalih $i = n - k + j$ vrhova poredaj ($i!$), reži na $j$ komada duljine $\ge 2$ ($\binom{i-j-1}{j-1} = \binom{m-1}{j-1}$ kompozicija) i podijeli s $2^j j!$ (smjer i poredak puteva). Zbroji po $j$; uz predračunate faktorijele i inverze složenost je $O(n)$ po testu.</p>
''',
    'detailed': r'''
<h3>1. Karakterizacija podcikličkih grafova</h3>
<p>Graf $H$ na $n$ vrhova je podgraf nekog ciklusa $C$ na istim vrhovima (Hamiltonovog). <strong>Tvrdnja.</strong> $H$ je podciklički $\Leftrightarrow$ ($m = n$ i $H$ je Hamiltonov ciklus) ili ($m < n$, svi stupnjevi $\le 2$ i $H$ je acikličan). <em>Dokaz.</em> ($\Rightarrow$) Stupnjevi u $C$ su $2$, dakle u $H$ su $\le 2$. Ako $H$ sadrži ciklus $Z$, onda $Z \subseteq C$; ciklus je 2-regularan i povezan pa jedini ciklus unutar ciklusa $C$ je $C$ sam. Tada $H \supseteq C$, a uz $|E(H)| \le |E(C)| = n$ slijedi $H = C$ i $m = n$. Inače je $H$ acikličan, pa $m \le n - 1$. ($\Leftarrow$) Hamiltonov ciklus je očito podciklički. Acikličan graf sa stupnjevima $\le 2$ je disjunktna unija puteva $P_1, \dots, P_k$ (komponente stabla s maksimalnim stupnjem $2$); spojimo kraj $P_t$ s početkom $P_{t+1}$ i kraj $P_k$ s početkom $P_1$ i dobivamo Hamiltonov ciklus koji sadrži $H$ (za $k = 1$ i $n \ge 3$ spajamo dva kraja puta; $n \ge 3$ je zadano). $\square$</p>
<p>Broj komponenata šume s $n$ vrhova i $m$ bridova je $k = n - m$. Dakle za $m < n$ brojimo načine da se $n$ označenih vrhova rastavi na $k$ vršno disjunktnih puteva (put s jednim vrhom dopušten).</p>
<h3>2. Prebrojavanje skupova puteva</h3>
<p>Neka je $j$ broj puteva s barem dva vrha, $0 \le j \le k$. Izoliranih vrhova je $k - j$, biramo ih na $\binom{n}{k-j}$ načina. Ostaje $i = n - (k - j) = m + j$ vrhova koje treba podijeliti u $j$ puteva duljine (broja vrhova) $\ge 2$, dakle nužno $i \ge 2j$, tj. $j \le m$.</p>
<p><strong>Lema.</strong> Broj načina da se $i$ označenih vrhova podijeli na $j$ neoznačenih puteva s po $\ge 2$ vrha jednak je $\dfrac{i!}{2^j\, j!} \binom{i-j-1}{j-1}$. <em>Dokaz.</em> Brojimo uređene parove (permutacija $\pi$ od $i$ vrhova, rez na $j$ uzastopnih blokova duljina $\ell_1, \dots, \ell_j \ge 2$). Permutacija ima $i!$; rezovi odgovaraju kompozicijama $i = \ell_1 + \dots + \ell_j$ s $\ell_t \ge 2$, a zamjenom $\ell_t' = \ell_t - 1 \ge 1$ kompozicijama broja $i - j$ na $j$ pozitivnih dijelova, kojih je $\binom{i-j-1}{j-1}$. Svaki par određuje skup puteva (blokovi su putevi u redoslijedu čitanja). Obratno, dani skup od $j$ puteva nastaje iz točno $j! \cdot 2^j$ parova: biramo poredak puteva i za svaki smjer čitanja; duljine blokova su tada određene. $\square$</p>
<p>Primijetimo $i - j - 1 = m - 1$, pa je binomni koeficijent $\binom{m-1}{j-1}$. Za $j = 0$: mora biti $i = 0$, tj. $m = 0$, i tada je pribrojnik $\binom{n}{n} \cdot 1 = 1$ (prazan graf); za $m > 0$ pribrojnik je $0$.</p>
<h3>3. Formula</h3>
<p>Za $m < n$:</p>
<p>$$\text{odg}(n, m) = \sum_{j=0}^{\min(k, m)} \binom{n}{k-j} \cdot \frac{(m+j)!}{2^j\, j!} \cdot \binom{m-1}{j-1}, \qquad k = n - m,$$</p>
<p>s dogovorom da je za $j = 0$ pribrojnik $[m = 0]$. Za $m = n$: $\dfrac{(n-1)!}{2}$ (cikličkih poredaka $n$ vrhova je $(n-1)!$, svaki ciklus nastaje iz dva smjera). Za $m > n$: $0$.</p>
<p>Provjera na primjeru $n = 4$, $m = 2$ ($k = 2$): $j = 1$: $\binom{4}{1} \cdot \frac{3!}{2} \cdot \binom{1}{0} = 4 \cdot 3 = 12$; $j = 2$: $\binom{4}{0} \cdot \frac{4!}{4 \cdot 2} \cdot \binom{1}{1} = 3$; ukupno $15$. Za $n = 4$, $m = 3$: $j$ mora dati $i = 3 + j \le 4$, pa $j = 1$: $\binom{4}{0} \cdot \frac{4!}{2} \cdot \binom{2}{0} = 12$. Za $n = 5$, $m = 3$ ($k = 2$): $j = 1$: $\binom{5}{1} \frac{4!}{2} \binom{2}{0} = 60$; $j = 2$: $\binom{5}{0} \frac{5!}{8} \binom{2}{1} = 30$; ukupno $90$. Sve se slaže s primjerom.</p>
<h3>4. Implementacija i složenost</h3>
<p>Predračunaj $x!$, $(x!)^{-1}$ i $2^{-x}$ modulo $10^9 + 7$ do $10^5$. Po testu petlja po $j$ od $0$ do $k$ s prekidom kad $i < 2j$: $O(n)$ množenja. Uz $\sum n \le 3 \cdot 10^7$ i $T \le 2 \cdot 10^4$ to je oko $10^8$ modularnih množenja – u redu bez potenciranja u petlji (zato su inverzi predračunati). Ulaz je $m \le n(n-1)/2$, do $\approx 5 \cdot 10^9$: čitaj $m$ kao 64-bitni broj prije usporedbe s $n$.</p>
<h3>5. Zamke</h3>
<ul>
<li>$m > n$ mora dati $0$, a $m = n$ Hamiltonove cikluse, ne formulu s putevima.</li>
<li>$m = 0$: jedini graf je prazan, odgovor $1$; formula to daje samo ako se $j = 0$ obradi kako je opisano.</li>
<li>Binomni koeficijent s negativnim donjim indeksom ($j = 0$, $\binom{m-1}{-1}$) mora vratiti $0$.</li>
</ul>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova ($n \le 6$, svi $m$) protiv brute forcea koji nabraja sve skupove od $m$ bridova i provjerava stupnjeve i cikluse; 3 velika testa s $T = 300$, $n \approx 10^5$ (najviše $0.15$ s).''',
},
# ---------------------------------------------------------------- M
{
    'letter': 'M', 'title': 'Function and Function', 'title_hr': 'Funkcija i funkcija', 'slug': 'M_function_and_function',
    'tl': '1 s', 'ml': '256 MiB',
    'statement': r'''
<p>$f(x)$ je ukupan broj zatvorenih područja („rupa”) u znamenkama broja $x$: znamenke $0, 4, 6, 9$ imaju $1$ rupu, $8$ ima $2$, ostale $0$. Npr. $f(1234) = 1$, $f(5678) = 3$. Definiramo $g_0(x) = x$ i $g_k(x) = f(g_{k-1}(x))$ za $k \ge 1$.</p>
<p>Za dane $x$ i $k$ izračunaj $g_k(x)$.</p>
<h3>Ulaz</h3>
<p>$T \approx 10^5$ testova; $0 \le x, k \le 10^9$ (nula se zadaje kao jedna znamenka <code>0</code>).</p>
<h3>Izlaz</h3>
<p>Za svaki test $g_k(x)$.</p>
<h3>Primjer</h3>
<p>$g_1(123456789) = 5$; $g_1(888888888) = 18$; $g_2(888888888) = 2$; $g_{999999999}(888888888) = 0$; $g_{12345}(98640) = 0$; $g_0(10^9) = 10^9$.</p>
''',
    'hints': [
        r'''
<p>Izračunaj $f(x)$ za nekoliko velikih $x$. Koliko brzo vrijednost pada? Što je $f(0)$ i $f(1)$?</p>
''',
        r'''
<p>Za $x \ge 1$ vrijedi $f(x) \le 2 \cdot (\text{broj znamenki})$, pa već nakon dva-tri koraka vrijednost postaje jednoznamenkasta, a zatim uskoro $0$ ili $1$. Vrijednosti $0$ i $1$ tvore ciklus $f(0) = 1$, $f(1) = 0$.</p>
''',
        r'''
<p>Simuliraj dok je $k > 0$ i $x > 1$; preostalih $k$ koraka odlučuje samo parnost.</p>
''',
    ],
    'coach': [
        ('Koliko iteracija $f$ zapravo treba simulirati?',
         r'''
<p>Za $x \le 10^9$ imamo najviše $10$ znamenki, a svaka ima najviše $2$ rupe, pa je $f(x) \le 20$. Zatim $f(f(x)) \le 4$ (dvoznamenkasti broj do $20$), pa $f^3(x) \le 2$, a $f(2) = 0$. Dakle nakon najviše $4$ koraka vrijednost je $0$ ili $1$; petlja „dok je $x > 1$” završava odmah.</p>
'''),
        ('Što se događa kad vrijednost postane $0$ ili $1$?',
         r'''
<p>$f(0) = 1$ (znamenka $0$ ima jednu rupu) i $f(1) = 0$, pa se vrijednosti izmjenjuju. Ako preostaje još $k$ koraka, konačna je vrijednost $x$ za paran $k$ i $1 - x$ za neparan $k$. Zato $k \le 10^9$ ne stvara problem.</p>
'''),
        ('Zašto je važno posebno tretirati $k = 0$ i ulaz $x = 0$?',
         r'''
<p>Za $k = 0$ ne primjenjujemo ništa: odgovor je $x$ (primjer $10^9, 0 \mapsto 10^9$). Za $x = 0$ funkcija <em>ne</em> vraća $0$ nego $1$ – ako se broj rupa računa petljom „dok $x > 0$”, slučaj $x = 0$ mora se obraditi zasebno. Petlja „dok $k > 0$ i $x > 1$” prirodno staje i za $x = 0$, a parnost preostalog $k$ tada daje $0$ ili $1$.</p>
'''),
    ],
    'tips': [
        r'''Funkcije na znamenkama (zbroj znamenki, broj rupa…) drastično smanjuju broj: nakon $O(1)$ koraka ulazi se u mali ciklus. Simuliraj do ciklusa, ostatak riješi modulom duljine ciklusa.''',
        r'''Uvijek ručno provjeri rubne vrijednosti tablice ($f(0)$, $f(1)$) – upravo one čine ciklus.''',
    ],
    'solution': r'''
<p>Prema javnim analizama (SUA wiki i blogovi): $f(x)$ je zbroj rupa znamenki ($0,4,6,9 \to 1$, $8 \to 2$, ostale $0$), uz $f(0) = 1$. Za $x \le 10^9$ vrijedi $f(x) \le 20$, pa nakon najviše četiri primjene vrijednost postane $0$ ili $1$, a te se dvije vrijednosti izmjenjuju ($f(0) = 1$, $f(1) = 0$). Simuliraj dok je $k > 0$ i $x > 1$; ako je preostali $k$ neparan, zamijeni $x \leftrightarrow 1 - x$. Složenost $O(1)$ po testu.</p>
''',
    'detailed': r'''
<h3>1. Definicija i tablica rupa</h3>
<p>Broj rupa po znamenkama: $0 \to 1$, $1,2,3,5,7 \to 0$, $4 \to 1$, $6 \to 1$, $8 \to 2$, $9 \to 1$. Za $x > 0$ je $f(x)$ zbroj po znamenkama, a $f(0) = 1$ (broj $0$ zapisuje se jednom znamenkom $0$).</p>
<h3>2. Brzo opadanje</h3>
<p><strong>Tvrdnja.</strong> Za $1 \le x \le 10^9$ je $f^{(4)}(x) \in \{0, 1\}$, gdje je $f^{(j)}$ $j$-struka kompozicija. <em>Dokaz.</em> $x$ ima najviše $10$ znamenki pa je $f(x) \le 20$. Brojevi $\le 20$ imaju najviše dvije znamenke, prva je $0$ (nema je), $1$ ili $2$, druga ima do $2$ rupe: $f^{(2)}(x) \le 2 + 0 = 2$; točnije, $\max_{y \le 20} f(y) = f(8) = 2$ ili $f(18) = 2$. Dakle $f^{(2)}(x) \in \{0, 1, 2\}$. Zatim $f(2) = 0$, $f(0) = 1$, $f(1) = 0$, pa je $f^{(3)}(x) \in \{0, 1\}$ i time i $f^{(4)}(x) \in \{0,1\}$. $\square$ (Za $x = 0$ trivijalno vrijedi već od početka.)</p>
<h3>3. Ciklus duljine 2</h3>
<p>$f(0) = 1$ i $f(1) = 0$, dakle nakon što vrijednost uđe u $\{0, 1\}$ svaki daljnji korak samo zamjenjuje $0 \leftrightarrow 1$. Ako je u tom trenutku vrijednost $x \in \{0,1\}$ i preostaje $k$ koraka, rezultat je $x$ za parni $k$ i $1 - x$ za neparni $k$.</p>
<h3>4. Algoritam</h3>
<ol>
<li>Dok je $k > 0$ i $x > 1$: $x \leftarrow f(x)$, $k \leftarrow k - 1$. (Najviše 4 iteracije.)</li>
<li>Ako je $k > 0$ i $k$ neparan: $x \leftarrow 1 - x$.</li>
<li>Ispiši $x$.</li>
</ol>
<p>Ispravnost: petlja točno reproducira prve korake dok vrijednost nije u $\{0,1\}$ ili dok koraci nisu potrošeni; ostatak pokriva točka 3. Složenost $O(\text{broj znamenki})$ po testu, tj. $O(1)$; $T$ nije ograničen pa je brzi ulaz koristan.</p>
<h3>5. Zamke</h3>
<ul>
<li>$k = 0$: ne dirati $x$ (šesti primjer: $10^9 \mapsto 10^9$).</li>
<li>$f(0) = 1$: petlja koja zbraja znamenke „dok $x > 0$” daje $0$ za ulaz $0$ – pogrešno. U našem algoritmu $x = 0$ ne ulazi u petlju iz koraka 1, ali ako se $f$ zove izravno, mora vraćati $1$.</li>
<li>Peti primjer $98640, 12345$: znamenke $9,8,6,4,0$ daju $1,2,1,1,1$ rupa, dakle $f(98640) = 6$; zatim $f(6) = 1$, $f(1) = 0$. Preostaje $12345 - 3 = 12342$ koraka (paran broj) od vrijednosti $0$, pa je odgovor $0$. Tablicu rupa treba prepisati doslovno iz zadatka.</li>
</ul>
''',
    'verified': r'''uzorci 1/1; 300 slučajnih malih testova (mali i veliki $x$, brojevi sastavljeni od znamenki s rupama, $k$ od $0$ do $10^9$) protiv brute forcea koji simulira do 50 koraka pa koristi parnost; 3 velika testa s $T = 10^5$ (najviše $0.04$ s).''',
},
]
