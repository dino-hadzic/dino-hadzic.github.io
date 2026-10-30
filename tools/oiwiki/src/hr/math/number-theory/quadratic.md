---
title: Kvadratna polja
---

Ovaj članak kratko predstavlja pojmove povezane s kvadratnim poljima. Dva važna primjera s njima u vezi su Gaussovi cijeli brojevi i Eisensteinovi cijeli brojevi, koji se mogu upotrijebiti za rješavanje nekih problema iz teorije brojeva.

## Osnovni pojmovi

U ovom odjeljku najprije uvodimo niz osnovnih pojmova. Kvadratna polja i prsteni kvadratnih cijelih brojeva posebni su slučajevi općenitijih pojmova algebarskog proširenja polja i prstena algebarskih cijelih brojeva, pa se gotovo sve definicije i rezultati ovog odjeljka mogu na odgovarajući način poopćiti na opći slučaj. Rasprava u ovom odjeljku bit će ograničena na poseban slučaj kvadratnih polja, bez uvođenja previše sadržaja iz algebarske teorije brojeva.

### Kvadratno polje

Elementi kvadratnog polja su kvadratni algebarski brojevi.

**Kvadratni algebarski broj** (quadratic algebraic number) kompleksan je broj koji se može prikazati kao rješenje kvadratne jednadžbe s cjelobrojnim koeficijentima. Iz formule za rješenja kvadratne jednadžbe slijedi da se svaki kvadratni algebarski broj može prikazati u obliku

$$
a+b\sqrt{d}
$$

gdje su $a$ i $b$ racionalni brojevi, a $d$ je cijeli broj bez kvadratnih faktora. Svaki broj tog oblika također je kvadratni algebarski broj. Kvadratni algebarski brojevi dijele se na racionalne brojeve i **kvadratne iracionalne brojeve** (quadratic irrational number). Očito je prikaz kvadratnog iracionalnog broja u gornjem obliku jedinstven.

Za svaki cijeli broj $d\neq 0,1$ bez kvadratnih faktora može se provjeriti da je skup $\mathbf Q(\sqrt{d})=\{a+b\sqrt{d}:a,b\in\mathbf Q\}$ zatvoren na zbrajanje, oduzimanje, množenje i dijeljenje. Budući da se skup zatvoren na četiri osnovne računske operacije naziva [poljem](../algebra/basic.md#域), skup $\mathbf Q(\sqrt{d})$ naziva se **kvadratnim poljem** (quadratic field). Svako kvadratno polje sadrži sve racionalne brojeve, pa su sva ona [kvadratna proširenja](../algebra/field-theory.md#域的扩张) polja racionalnih brojeva $\mathbf Q$. Kad je $d>0$, svi brojevi u kvadratnom polju $\mathbf Q(\sqrt{d})$ su realni; tada se $\mathbf Q(\sqrt{d})$ naziva realnim kvadratnim poljem. Kad je $d<0$, u kvadratnom polju nijedan broj osim racionalnih nije realan; tada se $\mathbf Q(\sqrt{d})$ naziva imaginarnim kvadratnim poljem.

### Konjugat i norma

**Konjugat** (conjugate) kvadratnog iracionalnog broja $a+b\sqrt{d}$ definira se kao $a-b\sqrt{d}$. Konjugirani kvadratni iracionalni brojevi dva su različita korijena iste kvadratne jednadžbe s cjelobrojnim koeficijentima. U realnom kvadratnom polju konjugat kvadratnog iracionalnog broja ne podudara se s njegovim konjugatom kao kompleksnog broja; u imaginarnom kvadratnom polju konjugat kvadratnog iracionalnog broja upravo je njegov konjugat kao kompleksnog broja. Naposljetku, konjugat racionalnog broja definira se kao on sam. Time je pojam konjugata definiran za sve kvadratne algebarske brojeve.

U svakom kvadratnom polju jednakosti dobivene zbrajanjem, oduzimanjem, množenjem i dijeljenjem ne mogu razlikovati konjugirane elemente. Drugim riječima, zamijenimo li u jednakosti svaki broj njegovim konjugatom, tj. promijenimo li predznak svakog kvadratnog korijena, jednakost i dalje vrijedi.

Pomoću konjugata može se konstruirati nekoliko preslikavanja s kvadratnih algebarskih brojeva u racionalne brojeve, kojima se rasprava o kvadratnim algebarskim brojevima prevodi u raspravu o racionalnim brojevima. Jednostavniji je **trag** (trace) kvadratnog algebarskog broja $\alpha$, tj. zbroj broja i njegova konjugata, u oznaci $\operatorname{tr}(\alpha)$. Budući da je to zapravo samo $2$ puta njegov racionalni dio, ne pruža mnogo informacija.

Korisnija je norma kvadratnog algebarskog broja. Umnožak kvadratnog algebarskog broja i njegova konjugata naziva se njegovom **normom** (norm):

$$
N(a+b\sqrt{d})=a^2-db^2
$$

Očito se u imaginarnom kvadratnom polju pojam norme podudara s pojmom kvadrata modula kompleksnog broja; u realnom kvadratnom polju, međutim, ta se dva pojma ne podudaraju.

Norma ima dobra svojstva. Prvo, budući da $d$ nema kvadratnih faktora, pa ne može biti potpun kvadrat, samo $0$ ima normu $0$. Drugo, norma čuva množenje i dijeljenje:

$$
N(a_1+b_1\sqrt{d})N(a_2+b_2\sqrt{d})=N((a_1+b_1\sqrt{d})(a_2+b_2\sqrt{d})),
$$

$$
\frac{N(a_1+b_1\sqrt{d})}{N(a_2+b_2\sqrt{d})}=N\left(\frac{a_1+b_1\sqrt{d}}{a_2+b_2\sqrt{d}}\right).
$$

Osim toga, recipročna vrijednost kvadratnog algebarskog broja upravo je omjer njegova konjugata i njegove norme:

$$
\dfrac{1}{a+b\sqrt{d}}=\frac{a-b\sqrt{d}}{N(a+b\sqrt{d})}.
$$

Prema Vièteovim formulama, kvadratni algebarski broj $\alpha$ zapravo je korijen jednadžbe

$$
x^2-\operatorname{tr}(\alpha)x+N(\alpha)=0
$$

Diskriminanta te jednadžbe naziva se i **diskriminantom** (discriminant) tog kvadratnog algebarskog broja, u oznaci $\operatorname{disc}(\alpha)$, a iznosi $4db^2$.

???+ note "Matrični prikaz"
    Slično kompleksnim brojevima, i kvadratni algebarski brojevi mogu se prikazati matricama. Neka je $d\neq 0,1$ cijeli broj bez kvadratnih faktora, a $a,b$ racionalni brojevi; tada se $a+b\sqrt{d}$ može prikazati matricom
    
    $$
    \begin{pmatrix}a & b \\ db & a\end{pmatrix}.
    $$
    
    Može se provjeriti da rezultati zbrajanja, oduzimanja, množenja i dijeljenja tih matrica odgovaraju rezultatima računanja s kvadratnim algebarskim brojevima. Trag i determinanta te matrice odgovaraju redom tragu i normi kvadratnog algebarskog broja, a diskriminanta karakterističnog polinoma te matrice upravo je diskriminanta kvadratnog algebarskog broja. Adjungirana matrica odgovara konjugatu kvadratnog algebarskog broja.

### Prsten kvadratnih cijelih brojeva

Među kvadratnim algebarskim brojevima posebni su kvadratni cijeli brojevi. **Kvadratni cijeli broj** (quadratic integer) kompleksan je broj koji se može prikazati kao rješenje kvadratne jednadžbe s cjelobrojnim koeficijentima i vodećim koeficijentom jedan. Jedina razlika u odnosu na kvadratne algebarske brojeve jest ograničenje na vodeći koeficijent. Prema formuli za rješenja, dva korijena kvadratne jednadžbe $x^2+px+q=0$ su

$$
\frac{-p\pm\sqrt{p^2-4q}}{2}.
$$

Ako je $p$ paran, tj. $p=2k$, dva se korijena mogu zapisati kao $-k\pm\sqrt{k^2-q}$; ako je $p$ neparan, tj. $p=2k+1$, dva se korijena mogu zapisati kao $-k-\dfrac{1\pm\sqrt{4(k^2+k-q)+1}}{2}$. Iz tih dvaju slučajeva može se zaključiti da se kvadratni cijeli brojevi u $\mathbf Q(\sqrt{d})$ nužno mogu zapisati u obliku

$$
a+b\omega
$$

gdje su $a$ i $b$ cijeli brojevi, a

$$
\omega=\begin{cases}
\dfrac{1+\sqrt{d}}{2}, & d\equiv 1\pmod 4,\\
\sqrt{d}, & d\equiv 2,3\pmod 4.
\end{cases}
$$

Obrnuto, svaki kompleksan broj tog oblika je kvadratni cijeli broj. Prikaz svakog neracionalnog kvadratnog cijelog broja u tom obliku je jedinstven.

Skup svih kvadratnih cijelih brojeva u kvadratnom polju $\mathbf Q(\sqrt{d})$ označava se $\mathbf Z[\omega]$. Budući da je taj skup zatvoren na zbrajanje, oduzimanje i množenje, naziva se i **prstenom kvadratnih cijelih brojeva** (quadratic integer ring). Racionalni brojevi u prstenu kvadratnih cijelih brojeva upravo su svi cijeli brojevi. Promotrimo li skup svih omjera kvadratnih cijelih brojeva iz $\mathbf Z[\omega]$, dobivamo odgovarajuće kvadratno polje $\mathbf Q(\sqrt{d})$.

Trag, norma i diskriminanta kvadratnog cijelog broja su cijeli brojevi. Diskriminanta s najmanjom apsolutnom vrijednošću među diskriminantama svih kvadratnih iracionalnih brojeva u prstenu kvadratnih cijelih brojeva $\mathbf Z[\omega]$ naziva se i diskriminantom odgovarajućeg kvadratnog polja $\mathbf Q(\sqrt{d})$. Kad je $d\equiv 1\pmod 4$, diskriminanta je $d$; kad je $d\equiv 2,3\pmod 4$, diskriminanta je $4d$.

### Djeljivost, asociranost i jedinice

Slično kao za cijele brojeve, i za kvadratne cijele brojeve može se izgraditi teorija djeljivosti. Naravno, rasprava se mora voditi unutar istog prstena kvadratnih cijelih brojeva.

Za kvadratne cijele brojeve $\alpha$ i $\beta$ iz prstena kvadratnih cijelih brojeva $\mathbf Z[\omega]$, ako postoji kvadratni cijeli broj $\gamma$ iz istog prstena takav da vrijedi $\beta=\alpha\gamma$, kažemo da $\alpha$ dijeli $\beta$ i pišemo $\alpha\mid\beta$. Relacija djeljivosti je relacija [preduređaja](../order-theory.md#二元关系) na prstenu kvadratnih cijelih brojeva. Ako istodobno vrijedi $\alpha\mid\beta$ i $\beta\mid\alpha$, tada se $\alpha$ i $\beta$ u proučavanju teorije djeljivosti mogu smatrati istim brojem; oni se nazivaju **asociranima** (associate). Relacija asociranosti je relacija ekvivalencije na prstenu kvadratnih cijelih brojeva.

U analogiji s teorijom djeljivosti cijelih brojeva, asociranost odgovara tome da su brojevi suprotni. U teoriji djeljivosti obično je dovoljno promatrati samo prirodne brojeve, bez razmatranja negativnih brojeva. Za kvadratne cijele brojeve relacija asociranosti može biti nešto složenija. Ako su kvadratni cijeli brojevi $\alpha$ i $\beta$ asocirani, tada postoje kvadratni cijeli brojevi $\gamma$ i $\delta$ takvi da vrijedi $\beta=\alpha\gamma$ i $\alpha=\beta\delta$. Stoga omjer $\gamma$ brojeva $\beta$ i $\alpha$ nužno mora biti poseban kvadratni cijeli broj, tj. takav da postoji kvadratni cijeli broj $\delta$ s $\gamma\delta=1$. Takav kvadratni cijeli broj $\gamma$ naziva se **jedinicom** (unit), a također i invertibilnim elementom. Dva su kvadratna cijela broja asocirana ako i samo ako je njihov omjer jedinica. Stoga, da bismo razumjeli relaciju asociranosti na prstenu kvadratnih cijelih brojeva, moramo razumjeti strukturu njegovih jedinica.

Budući da norma čuva množenje, a norma kvadratnog cijelog broja uvijek je cijeli broj, pomoću norme se relacija djeljivosti kvadratnih cijelih brojeva može prevesti u relaciju djeljivosti cijelih brojeva. Drugim riječima, ako je $\alpha\mid\beta$, nužno vrijedi $N(\alpha)\mid N(\beta)$. Jednako tako, kvadratni cijeli broj $\alpha$ je jedinica ako i samo ako je njegova norma $N(\alpha)=\pm 1$. Stoga, da bismo dobili sve jedinice prstena kvadratnih cijelih brojeva $\mathbf Z[\omega]$, dovoljno je riješiti diofantsku jednadžbu:

$$
N(a+b\omega)=\pm 1,
$$

gdje je izraz za normu

$$
N(a+b\omega)=\begin{cases}
a^2+ab+\dfrac{1-d}{4}b^2, & d\equiv 1\pmod 4,\\
a^2-db^2, & d\equiv 2,3\pmod 4.
\end{cases}
$$

Za imaginarne prstene kvadratnih cijelih brojeva, tj. kad je $d<0$, budući da je norma nužno nenegativan cijeli broj, lako se provjerava da za sve negativne $d\neq -1,-3$ bez kvadratnih faktora rješenja su samo $(a,b)=(\pm 1,0)$; tj. osim u $\mathbf Z[\sqrt{-1}]$ i $\mathbf Z[\frac{1+\sqrt{-3}}{2}]$, jedinice imaginarnih prstena kvadratnih cijelih brojeva su samo $\pm 1$. Označimo $\mathrm{i}=\sqrt{-1}$; tada se prsten kvadratnih cijelih brojeva $\mathbf Z[\mathrm{i}]$ naziva i prstenom Gaussovih cijelih brojeva, a skup njegovih jedinica je $\{\pm 1,\pm\mathrm{i}\}$. Označimo $\omega=\frac{1+\sqrt{-3}}{2}$; tada se prsten kvadratnih cijelih brojeva $\mathbf Z[\omega]$ naziva i prstenom Eisensteinovih cijelih brojeva, a skup njegovih jedinica je $\{\pm 1,\pm\omega,\pm\omega^2\}$.

Za realne prstene kvadratnih cijelih brojeva, tj. kad je $d>0$, situacija je složenija i može se svesti na raspravu o odgovarajućoj [Pellovoj jednadžbi](./pell-equation.md). Iz rezultata o Pellovoj jednadžbi slijedi da se tada skup svih jedinica može zapisati kao $\{\pm u^k:k\in\mathbf Z\}$, gdje se $u$ naziva **fundamentalnom jedinicom** (fundamental unit). Fundamentalna jedinica može se odrediti rješavanjem odgovarajuće Pellove jednadžbe. Fundamentalna jedinica nije jedinstvena: ako je $u$ fundamentalna jedinica, tada su i njezin konjugat $\bar u$ te $-u$ i $-\bar u$ fundamentalne jedinice.

Struktura jedinica prstena kvadratnih cijelih brojeva može se poopćiti na opće [prstene algebarskih cijelih brojeva](../algebra/field-theory.md#代数扩张). [Dirichletov teorem o jedinicama](https://en.wikipedia.org/wiki/Dirichlet%27s_unit_theorem) iz algebarske teorije brojeva kaže da sve jedinice bilo kojeg prstena algebarskih cijelih brojeva tvore [konačno generiranu Abelovu grupu](../algebra/group-theory.md#有限生成-abel-群), a taj teorem ujedno daje i rang te grupe.

Sadržaji teorije djeljivosti cijelih brojeva poput najvećeg zajedničkog djelitelja, dijeljenja s ostatkom, Bézoutova teorema i teorema o jedinstvenoj faktorizaciji mogu se poopćiti na neke ili na sve prstene kvadratnih cijelih brojeva. Može li se takvo poopćenje provesti na nekom prstenu kvadratnih cijelih brojeva zapravo odražava jesu li svojstva tog prstena dovoljno bliska svojstvima prstena cijelih brojeva. Teorem o jedinstvenoj faktorizaciji ne vrijedi u svim prstenima kvadratnih cijelih brojeva; među prstenima kvadratnih cijelih brojeva u kojima vrijedi teorem o jedinstvenoj faktorizaciji, dijeljenje s ostatkom moguće je samo u nekima. Za raspravu o tim sadržajima vidi odjeljak [Prsteni kvadratnih cijelih brojeva](../algebra/ring-theory.md#例子二次整数环) u dijelu o teoriji prstena ili odgovarajuće knjige.

### Jedinstvena faktorizacija

Ako se teorem o jedinstvenoj faktorizaciji cijelih brojeva može poopćiti na prsten kvadratnih cijelih brojeva, trebao bi imati ovakav oblik: svaki kvadratni cijeli broj u prstenu $\mathbf Z[\omega]$ može se zapisati kao umnožak nekoliko ireducibilnih elemenata, a ta je faktorizacija jedinstvena do na asociranost i poredak. Pri tome je [ireducibilni element](../algebra/ring-theory.md#整除关系) kvadratni cijeli broj koji se ne može dalje rastaviti na umnožak elemenata koji nisu jedinice, slično prostim brojevima u teoremu o jedinstvenoj faktorizaciji cijelih brojeva. Kao što je već spomenuto, teorem o jedinstvenoj faktorizaciji ne vrijedi u svim prstenima kvadratnih cijelih brojeva.

Na primjer, u $\mathbf Z[\sqrt{-5}]$ postoji faktorizacija $9=3\times 3=(2+\sqrt{-5})\times(2-\sqrt{-5})$, no $3$ i $2\pm\sqrt{-5}$ već su ireducibilni elementi, pa faktorizacija nije jedinstvena. Da bismo pokazali da su sva tri broja ireducibilni elementi, možemo promotriti njihove norme: sve su im norme jednake $9$, pa kad bi se mogli rastaviti na umnožak elemenata koji nisu jedinice, norme dobivenih faktora mogle bi biti samo $3$, ali u $\mathbf Z[\sqrt{-5}]$ ne postoji kvadratni cijeli broj s normom $3$.

Glavni razlog zašto u općem prstenu kvadratnih cijelih brojeva teorem o jedinstvenoj faktorizaciji ne vrijedi jest to što faktorizacija koja koristi samo kvadratne cijele brojeve nije dovoljno fina. Na primjer, ako treba rastaviti umnožak $abcd$, a dostupni osnovni elementi su samo $\{ab,cd,ac,bd\}$, dobivena faktorizacija prirodno nije jedinstvena; da bismo dobili teorem o jedinstvenoj faktorizaciji, moramo dodatno razmotriti $\{a,b,c,d\}$. U prstenu kvadratnih cijelih brojeva struktura finija od kvadratnih cijelih brojeva su [ideali](../algebra/ring-theory.md#理想) prstena kvadratnih cijelih brojeva; preslikavanjem kvadratnog cijelog broja u njemu pripadni glavni ideal njegova se klasa asociranosti ulaže u skup ideala, pa je faktorizacija brojeva samo poseban slučaj faktorizacije ideala. Promatramo li faktorizaciju ideala u prstenu kvadratnih cijelih brojeva, može se dokazati da se ideali svakog prstena kvadratnih cijelih brojeva mogu jedinstveno rastaviti na umnožak nekoliko prostih ideala. To znači da su svi prsteni kvadratnih cijelih brojeva [Dedekindove domene](https://en.wikipedia.org/wiki/Dedekind_domain). Općenitije, svi prsteni algebarskih cijelih brojeva su Dedekindove domene.

Ako u nekom prstenu kvadratnih cijelih brojeva vrijedi teorem o jedinstvenoj faktorizaciji, tada njegovi prosti ideali i ireducibilni elementi (klase ekvivalencije do na asociranost) stoje u bijektivnoj korespondenciji, pa je za takve prstene kvadratnih cijelih brojeva faktorizacija ideala na proste ideale ekvivalentna faktorizaciji kvadratnih cijelih brojeva na ireducibilne elemente. Štoviše, ireducibilni elementi tada se nazivaju i [prostim elementima](../algebra/ring-theory.md#整除关系) i odgovaraju pojmu prostog broja među cijelim brojevima. Rasprava u nastavku koristit će proste ideale i srodne pojmove; čitatelji koji nisu upoznati s tim pojmom mogu ih doslovno zamijeniti prostim elementima, i tada su te tvrdnje točne u slučaju kad vrijedi teorem o jedinstvenoj faktorizaciji.

Da bismo potpuno razumjeli jedinstvenu faktorizaciju u općem prstenu kvadratnih cijelih brojeva $\mathbf Z[\omega]$, moramo znati koji su prosti ideali u $\mathbf Z[\omega]$. Prvo, svaki prosti ideal u $\mathbf Z[\omega]$ dijeli (glavni ideal) svoje norme. Rastavimo li njegovu normu unutar cijelih brojeva na umnožak nekoliko prostih brojeva, prema teoremu o jedinstvenoj faktorizaciji taj prosti ideal nužno dijeli (glavni ideal) nekog od tih prostih faktora. Stoga prosti ideali u $\mathbf Z[\omega]$ nužno nastaju daljnjim rastavljanjem prostih brojeva iz cijelih brojeva. Da bismo nabrojali sve proste ideale u $\mathbf Z[\omega]$, dovoljno je dati jedinstvenu faktorizaciju (glavnog ideala) prostog broja $p$ iz $\mathbf Z$ u $\mathbf Z[\omega]$. Budući da je norma (glavnog ideala) prostog broja $p$ u $\mathbf Z[\omega]$ jednaka $p^2$, a njegova faktorizacija na proste ideale znači da norme tih prostih ideala moraju biti djelitelji $p^2$, one mogu biti samo $p$ ili $p^2$. To pokazuje da postoje samo sljedeće tri mogućnosti:

1.  $p$ je u $\mathbf Z[\omega]$ **inertan** (inert), tj. $(p)$ je u $\mathbf Z[\omega]$ i dalje prosti ideal;
2.  $p$ se u $\mathbf Z[\omega]$ **cijepa** (split), tj. $(p)$ se u $\mathbf Z[\omega]$ može zapisati kao umnožak dvaju različitih konjugiranih prostih ideala;
3.  $p$ se u $\mathbf Z[\omega]$ **grana** (ramify), tj. $(p)$ se u $\mathbf Z[\omega]$ može zapisati kao kvadrat nekog prostog ideala.

Dalje se može dokazati da je za određivanje u koji od tih triju slučajeva pada neki prosti broj $p$ dovoljno izračunati [Kroneckerov simbol](https://en.wikipedia.org/wiki/Kronecker_symbol) $\left(\dfrac{D}{p}\right)$ za diskriminantu $D$ kvadratnog polja kojem pripada $\mathbf Z[\omega]$ i taj prosti broj $p$. Ta tri slučaja odgovaraju redom trima vrijednostima Kroneckerova simbola: $-1$, $+1$ i $0$. Kad je $p$ neparan prost broj, Kroneckerov simbol upravo je [Legendreov simbol](./quad-residue.md#legendre-符号), pa ta tri slučaja odgovaraju redom tome da je $D$ [kvadratni neostatak](./quad-residue.md) modulo $p$, da je $D$ [kvadratni ostatak](./quad-residue.md) modulo $p$ te da $p$ dijeli $D$. Kad je $p=2$, ta tri slučaja odgovaraju redom $D\equiv \pm 3\pmod 8$, $D\equiv \pm 1\pmod 8$ i tome da $2$ dijeli $D$.

## Gaussovi cijeli brojevi

U ovom odjeljku neka $\mathrm{i}=\sqrt{-1}$ označava imaginarnu jedinicu. Kvadratno polje $\mathbf Q(\mathrm{i})$ naziva se i Gaussovim poljem; ono je ujedno četvrto [ciklotomsko polje](../algebra/field-theory.md#分圆域). Odgovarajući prsten kvadratnih cijelih brojeva $\mathbf Z[\mathrm{i}]$ naziva se i prstenom Gaussovih cijelih brojeva, a njegovi elementi nazivaju se **Gaussovim cijelim brojevima** (Gaussian integer). Gaussovi cijeli brojevi imaju ukupno četiri jedinice, naime $\pm 1$ i $\pm\mathrm{i}$, pa svaki Gaussov cijeli broj različit od nule ima četiri asocirana elementa (uključujući sebe). U kompleksnoj ravnini Gaussovi cijeli brojevi predstavljaju sve cjelobrojne točke, a norma Gaussova cijelog broja $N(a+b\mathrm{i})=a^2+b^2$ upravo je norma u kompleksnoj ravnini.

![](./images/gaussian-integer.svg)

Na Gaussovim cijelim brojevima može se provoditi dijeljenje s ostatkom: za Gaussove cijele brojeve $a$ i $b\neq 0$ uvijek postoje Gaussovi cijeli brojevi $q$ i $r$ takvi da vrijedi $a=bq+r$ i $N(r)<N(b)$. Da bismo izračunali takvo dijeljenje s ostatkom, možemo najprije u $\mathbf Q(\mathrm{i})$ izračunati $\dfrac{a}{b}$, zatim u kompleksnoj ravnini pronaći najbližu cjelobrojnu točku i uzeti je za $q$, pa izračunati $r=a-bq$; tako dobiveni ostatak uvijek zadovoljava $N(r)\le\dfrac{1}{2}N(b)$. Pomoću dijeljenja s ostatkom na Gaussove cijele brojeve mogu se prenijeti Euklidov algoritam, Bézoutov teorem i slično, a zatim i izgraditi teorem o jedinstvenoj faktorizaciji.

### Gaussovi prosti brojevi

Pomoću rezultata prethodnog odjeljka mogu se odrediti prosti elementi među Gaussovim cijelim brojevima (nazivaju se i Gaussovim prostim brojevima). Budući da je diskriminanta prstena Gaussovih cijelih brojeva $-4$, a Kroneckerov simbol $\left(\dfrac{-4}{n}\right)$ za paran $n$ ima vrijednost $0$, a za neparan $n$ vrijednost jednaku $\left(\dfrac{-1}{n}\right)=(-1)^{(n-1)/2}$, vrijedi

$$
\left(\dfrac{-4}{n}\right) = \begin{cases}
+1,& n\equiv 1\pmod 4,\\
-1,& n\equiv 3\pmod 4,\\
0,& 2\mid n.
\end{cases}
$$

Stoga Gaussovih prostih brojeva ima ukupno tri vrste:

1.  prosti brojevi oblika $4k+3$ među cijelim brojevima;
2.  dva konjugirana Gaussova prosta faktora prostog broja oblika $4k+1$ među cijelim brojevima;
3.  faktor $1+\mathrm{i}$ prostog broja $2$, čiji je konjugat s njim asociran.

Na primjer, u $\mathbf Z[\mathrm{i}]$ postoji faktorizacija $60=2^2\times 3\times 5=-(1+\mathrm{i})^4\times 3\times(2+\mathrm{i})\times(2-\mathrm{i})$.

Rasprava o tome može li se prosti broj $p$ dalje rastaviti u $\mathbf Z[\mathrm{i}]$ zapravo je ekvivalentna raspravi o tome može li se prosti broj $p$ zapisati kao zbroj kvadrata cijelih brojeva $a^2+b^2$. Stoga iz ovdje dobivenog rezultata slijedi da se prosti broj $p$ može zapisati kao zbroj dvaju kvadrata ako i samo ako je $p=2$ ili $p\equiv 1\pmod 4$. To je [Fermatov teorem o zbroju dvaju kvadrata](https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares).

### Problem cjelobrojnih točaka na kružnici

U kompleksnoj ravnini Gaussovi cijeli brojevi predstavljaju sve cjelobrojne točke. Norma Gaussova cijelog broja upravo je kvadrat euklidske udaljenosti točke rešetke od ishodišta. Stoga kvadratni cijeli brojevi s istom normom odgovaraju cjelobrojnim točkama na kružnici sa središtem u ishodištu kompleksne ravnine. Drugim riječima, broj cjelobrojnih točaka na kružnici $x^2+y^2=n$ jednak je broju Gaussovih cijelih brojeva $x+y\mathrm{i}$ s normom $n$.

Da bismo riješili jednadžbu $N(x+y\mathrm{i})=n$, možemo promotriti faktorizaciju Gaussova cijelog broja $x+y\mathrm{i}$ na proste faktore; umnožak normi tih prostih faktora jednak je $n$. Stoga, dobijemo li najprije faktorizaciju broja $n$, iz prostih faktora broja $n$ možemo odrediti koje proste faktore $x+y\mathrm{i}$ može imati. Neka je faktorizacija cijelog broja $n$ na proste faktore

$$
n=2^kp_1^{r_1}\cdots p_\ell^{r_\ell}q_1^{s_1}\cdots q_{m}^{s_m},
$$

gdje su $p_1,\cdots,p_\ell$ prosti faktori oblika $4k+1$, a $q_1,\cdots,q_m$ prosti faktori oblika $4k+3$.

Prvo, jednadžba $N(x+y\mathrm{i})=n$ ima rješenje ako i samo ako su eksponenti $s_1,\cdots,s_m$ prostih faktora oblika $4k+3$ broja $n$ svi parni; to je zato što su $q_1,\cdots,q_m$ također Gaussovi prosti brojevi čija je norma jednaka njihovu kvadratu, pa se u faktorizaciji norme na proste faktore nužno pojavljuju u parovima.

Pretpostavimo sada da jednadžba ima rješenje. Tada rješenje jednadžbe nužno ima oblik

$$
u(1+\mathrm{i})^k(a_1+b_1\mathrm{i})^{r_{1}^+}(a_1-b_1\mathrm{i})^{r_{1}^-}\cdots(a_\ell+ b_\ell\mathrm{i})^{r_\ell^+}(a_\ell-b_\ell\mathrm{i})^{r_\ell^-}q_1^{s_1/2}\cdots q_{m}^{s_m/2},
$$

gdje je $u$ jedinica, $a_j\pm b_j\mathrm{i}$ su konjugirani prosti faktori broja $p_j$ u prstenu Gaussovih cijelih brojeva, a $r_j^++r_j^-=r_j$. Stoga je broj rješenja jednadžbe jednak

$$
4(1+r_1)\cdots(1+r_\ell).
$$

Neka $f(n)$ označava broj cjelobrojnih rješenja jednadžbe $x^2+y^2=n$. Kad ona ima rješenje, $f(n)$ je dan gornjim izrazom; inače je $f(n)=0$. Lako se provjerava da je $\dfrac14f(n)$ [multiplikativna funkcija](./basic.md#积性函数). Vrijednosti multiplikativne funkcije određene su njezinim vrijednostima na potencijama prostih brojeva. Iz izraza za $f(n)$ može se odrediti da su vrijednosti $\dfrac14f(n)$ na potencijama prostih brojeva $p^k$ sljedeće:

1.  ako je $p$ prost broj oblika $4k+3$, tada je $\dfrac14f(1)=1,\dfrac14f(p)=0,\dfrac14f(p^2)=1,\dfrac14f(p^3)=0,\cdots$;
2.  ako je $p$ prost broj oblika $4k+1$, tada je $\dfrac14f(p^k)=k+1$;
3.  ako je $p=2$, tada je $\dfrac14f(2^k)=1$.

Lako se provjerava da se sva tri slučaja mogu zapisati kao

$$
\dfrac14f(p^k) = \sum_{j=0}^k\left(\dfrac{-4}{p}\right)^j = \sum_{j=0}^k\left(\dfrac{-4}{p^j}\right) = \sum_{d\mid p^k}\left(\dfrac{-4}{d}\right).
$$

Budući da je Kroneckerov simbol $\left(\dfrac{-4}{n}\right)$ potpuno multiplikativna funkcija, dobivamo

$$
f(n) = 4\sum_{d\mid n}\left(\dfrac{-4}{d}\right)=4\sum_{d\mid n}\chi_{4,3}(d).
$$

Oznaka u sumi krajnje desno koristi činjenicu da je Kroneckerov simbol $\left(\dfrac{-4}{n}\right)$ realni [Dirichletov karakter](https://en.wikipedia.org/wiki/Dirichlet_character) modulo $4$.

### Pitagorina jednadžba

Pomoću Gaussovih cijelih brojeva može se odrediti opće rješenje Pitagorine jednadžbe. Pitagorina jednadžba je sljedeća kvadratna diofantska jednadžba:

$$
x^2+y^2=z^2.
$$

Usporedbom sa sadržajem prethodnog odjeljka vidimo da je to isto što i rješavanje jednadžbe $N(x+y\mathrm{i})=z^2$. Neka $z$ u $\mathbf Z$ ima faktorizaciju na proste faktore

$$
z=2^kp_1^{r_1}\cdots p_\ell^{r_\ell}q_1^{s_1}\cdots q_{m}^{s_m},
$$

pa njezino rješenje $x+y\mathrm{i}$ u $\mathbf Z[\mathrm{i}]$ ima faktorizaciju na proste faktore

$$
x+y\mathrm{i} = u(1+\mathrm{i})^{2k}(a_1+b_1\mathrm{i})^{r_{1}^+}(a_1-b_1\mathrm{i})^{r_{1}^-}\cdots(a_\ell+ b_\ell\mathrm{i})^{r_\ell^+}(a_\ell-b_\ell\mathrm{i})^{r_\ell^-}q_1^{s_1}\cdots q_{m}^{s_m}
$$

uz $r_j^++r_j^-=2r_j$. Možemo izračunati najveći zajednički djelitelj brojeva $x+y\mathrm{i}$ i $z$ i dobiti sljedeći cijeli broj:

$$
\kappa = 2^kp_1^{\min\{r_1^+,r_1^-\}}\cdots p_\ell^{\min\{r_\ell^+,r_\ell^-\}}q_1^{s_1}\cdots q_m^{s_m}.
$$

Uklonimo li taj zajednički faktor, $\kappa^{-1}(x+y\mathrm{i})$ sadrži samo proste faktore oblika $a_j\pm b_j\mathrm{i}$, konjugirani faktori ne pojavljuju se u parovima, a eksponenti $|r_j^+-r_j^-|$ tih faktora nužno su parni (jer je njihov zbroj $2r_j$ paran). Stoga je $\kappa^{-1}(x+y\mathrm{i})$ kvadrat nekog kvadratnog cijelog broja $u+v\mathrm{i}$. Odatle dobivamo sljedeće jednadžbe:

$$
x+y\mathrm{i} = \kappa(u+v\mathrm{i})^2,\ z=\kappa N(u+v\mathrm{i}).
$$

Unutar cijelih brojeva $\mathbf Z$ to odgovara sljedećem sustavu jednadžbi:

$$
x = \kappa(u^2-v^2),\ y = 2\kappa uv,\ z = \kappa(u^2+v^2).
$$

Obrnuto, za bilo koje cijele brojeve $u$ i $v$ trojka $(x,y,z)$ dobivena gornjim izrazima zadovoljava Pitagorinu jednadžbu. Stoga je to opće rješenje Pitagorine jednadžbe.

Iz gornjeg postupka vidi se da su u primitivnoj Pitagorinoj trojci $(x,y,z)$ (tj. takvoj da je zajednički djelitelj brojeva $x,y,z$ jednak jedan) brojevi $x,y$ nužno jedan neparan i jedan paran, a $z$ je neparan i sadrži samo proste faktore oblika $4k+1$.

Sličnom metodom može se dobiti i opće rješenje jednadžbe $x^2+y^2=z^3$ ili dokazati da jednadžba $x^4+y^4=z^4$ nema rješenja. Naravno, pomoću općeg rješenja Pitagorine jednadžbe i metode beskonačnog spusta može se dokazati i jača tvrdnja, naime da jednadžba $x^4+y^4=z^2$ nema rješenja.

## Eisensteinovi cijeli brojevi

U ovom odjeljku neka je $\omega=\dfrac{-1+\sqrt{3}\mathrm{i}}{2}=e^{2\pi\mathrm{i}/3}$.[^omega] Kvadratno polje $\mathbf Q(\sqrt{3}\mathrm{i})$ je treće i šesto [ciklotomsko polje](../algebra/field-theory.md#分圆域), a algebarski cijeli brojevi u njemu nazivaju se Eisensteinovim cijelim brojevima. Prsten $\mathbf Z[\omega]$ svih Eisensteinovih cijelih brojeva naziva se prstenom Eisensteinovih cijelih brojeva. Prsten Eisensteinovih cijelih brojeva ima ukupno šest jedinica, a to su $\pm 1$, $\pm\omega$ i $\pm\omega^2$. U kompleksnoj ravnini svi Eisensteinovi cijeli brojevi tvore trokutastu rešetku. Za razliku od Gaussovih cijelih brojeva, ovdje točke rešetke općenito nisu cjelobrojne točke.

![](./images/eisenstein-integer.svg)

Norma Eisensteinova cijelog broja je

$$
N(a+b\omega) = a^2-ab+b^2,
$$

a to je ujedno kvadrat udaljenosti navedene točke rešetke u kompleksnoj ravnini od ishodišta.

Eisensteinovi cijeli brojevi vrlo su slični Gaussovim cijelim brojevima. I na Eisensteinovim cijelim brojevima može se pomoću norme $N(\cdot)$ definirati dijeljenje s ostatkom te izgraditi Euklidov algoritam, Bézoutov teorem, teorem o jedinstvenoj faktorizaciji i druge rezultate. Slično kao gore, mogu se izvesti faktori prostih brojeva u prstenu Eisensteinovih cijelih brojeva. U tu svrhu uočimo da je diskriminanta $\mathbf Z[\omega]$ jednaka $-3$, a Kroneckerov simbol je

$$
\left(\dfrac{-3}{n}\right) = \begin{cases}
+1, & n\equiv 1\pmod 3,\\
-1, & n\equiv 2\pmod 3,\\
0,  & 3\mid n,
\end{cases}
$$

pa prosti elementi u prstenu Eisensteinovih cijelih brojeva, tj. Eisensteinovi prosti brojevi, dolaze u sljedeće tri vrste:

1.  prosti brojevi oblika $3k+2$ među cijelim brojevima, tj. $2$ i prosti brojevi oblika $6k+5$;
2.  dva konjugirana Eisensteinova prosta faktora prostog broja oblika $3k+1$ (tj. prostog broja oblika $6k+1$) među cijelim brojevima;
3.  faktor $(3+\sqrt{3}\mathrm{i})/2$ prostog broja $3$, čiji je konjugat s njim asociran.

Metodom prethodnog odjeljka može se odrediti broj Eisensteinovih cijelih brojeva s normom $n$. Označimo taj broj s $f(n)$; tada je on jednak

$$
f(n)=6\sum_{d\mid n}\left(\dfrac{-3}{d}\right)=6\sum_{d\mid n}\chi_{3,2}(d). 
$$

Pri tome je $\chi_{3,2}(n)=\left(\dfrac{-3}{n}\right)$ realni Dirichletov karakter modulo $3$. Taj izraz pokazuje da takav Eisensteinov cijeli broj postoji ako i samo ako su eksponenti svih prostih faktora oblika $3k+2$ broja $n$ parni.

Prema ranijoj formuli za normu, $f(n)$ je ujedno broj cjelobrojnih rješenja diofantske jednadžbe $x^2-xy+y^2=n$ ili diofantske jednadžbe $x^2+xy+y^2=n$. Njegovo geometrijsko značenje je broj cjelobrojnih točaka na nagnutoj elipsi $x^2\pm xy+y^2=n$.

S tim jednadžbama usko je povezana još jedna diofantska jednadžba, $x^2+3y^2=n$, čija cjelobrojna rješenja odgovaraju cjelobrojnim točkama na elipsi u standardnom položaju. Zamjenom varijabli $x=(u+v)/2$ i $y=(u-v)/2$ ona se može svesti na već riješenu jednadžbu $u^2-uv+v^2=n$. Međutim, iako cjelobrojna rješenja jednadžbe $x^2+3y^2=n$ uvijek odgovaraju cjelobrojnim rješenjima jednadžbe $u^2-uv+v^2=n$, obrat ne mora vrijediti. Ako je $n$ paran, tada su $u$ i $v$ nužno oba parni, što znači da su $x$ i $y$ nužno cijeli brojevi, pa je broj cjelobrojnih rješenja jednadžbe $x^2+3y^2=n$ i dalje $f(n)$. No ako je $n$ neparan, $u$ i $v$ mogu biti jedan neparan i jedan paran, a mogu biti i oba neparni, pa odgovarajući $x$ i $y$ mogu biti oba polucijeli brojevi ili oba cijeli brojevi. Taj slučaj zahtijeva pažljiviju raspravu.

Kad je poznato jedno cjelobrojno rješenje $(u,v)$ jednadžbe $u^2-uv+v^2=n$, cjelobrojna rješenja koja odgovaraju Eisensteinovim cijelim brojevima asociranim s $u+v\omega$ (uključujući njega samog) su redom

$$
(u,v),(u-v,u),(-v,u-v),(-u,-v),(v-u,-u),(v,v-u).
$$

Budući da tri cijela broja $u,v,u-v$, ako nisu svi parni, nužno čine dva neparna i jedan paran broj, među tih šest cjelobrojnih rješenja nužno su dva sastavljena samo od neparnih brojeva, a četiri od jednog neparnog i jednog parnog. To znači da je, kad je $n$ neparan, samo $\dfrac13$ cjelobrojnih rješenja jednadžbe $u^2-uv+v^2=n$ sastavljeno samo od neparnih brojeva, a samo tada ona odgovaraju cjelobrojnim rješenjima jednadžbe $x^2+3y^2=n$. Stoga je, kad je $n$ neparan, broj cjelobrojnih rješenja jednadžbe $x^2+3y^2=n$ jednak $\dfrac13f(n)$.

Naposljetku, slično metodi rješavanja Pitagorine jednadžbe, pomoću Eisensteinovih cijelih brojeva mogu se riješiti sljedeće diofantske jednadžbe:

$$
x^2-xy+y^2=z^2
$$

$$
x^2+xy+y^2=z^2
$$

$$
x^2+3y^2=z^2
$$

$$
x^2+3y^2=z^3
$$

Njihova opća rješenja ovdje ne navodimo. Sličnom metodom može se dokazati i da $x^3+y^3=z^3$ nema rješenja.

## Literatura i napomene

-   [Quadratic field - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_field)
-   [Quadratic integer - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_integer)
-   [Gaussian integer - Wikipedia](https://en.wikipedia.org/wiki/Gaussian_integer)
-   [Eisenstein integer - Wikipedia](https://en.wikipedia.org/wiki/Eisenstein_integer)
-   [Kronecker symbol - Wolfram MathWorld](https://mathworld.wolfram.com/KroneckerSymbol.html)
-   [Dirichlet character - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_character)
-   [Theodorus J. Dekker's Notes on Primes in Quadratic Fields](https://staff.science.uva.nl/t.j.dekker/PrimesPaper/Primes.pdf)
-   [Franz Lemmermeyer's Notes on Ideals in Quadratic Number Fields](http://www.fen.bilkent.edu.tr/~franz/ant/ant02.pdf)
-   [J.S. Milne - Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT301.pdf)

[^omega]: Napomena: izbor $\omega$ ovdje nije isti kao gore. Prema uobičajenoj konvenciji, pri raspravi o općim prstenima kvadratnih cijelih brojeva obično se uzima $\omega=(1+\sqrt{d})/2$ (kad je $d\equiv 1\pmod4$), dok se za prsten Eisensteinovih cijelih brojeva često uzima $\omega=(-1+\sqrt{-3})/2$. Ta razlika nema nikakvog suštinskog utjecaja, ali može promijeniti oblik nekih izraza. Napomena: prsten Eisensteinovih cijelih brojeva ne smije se zapisivati kao $\mathbf Z[\sqrt{-3}]$.
