---
title: Treap
---

Predznanje: [obično binarno stablo pretraživanja](./bst.md), [osnove gomile](./heap.md).

## Uvod

Treap (stablo‑gomila, engl. *tree* + *heap*) **slabo je balansirano** **binarno stablo pretraživanja**.

Čvorovi Treapa, osim **vrijednosti** ($\textit{val}$) koja se održava, imaju i dodatni slučajni **prioritet** ($\textit{priority}$). Vrijednosti zadovoljavaju svojstvo binarnog stabla pretraživanja, a prioriteti svojstvo gomile (min‑gomile ili max‑gomile).

Svojstvo binarnog stabla pretraživanja znači:

-   Vrijednosti ($\textit{val}$) svih čvorova lijevog podstabla manje su od vrijednosti roditelja.
-   Vrijednosti ($\textit{val}$) svih čvorova desnog podstabla veće su od vrijednosti roditelja.

Svojstvo gomile znači:

-   Prioritet ($\textit{priority}$) djeteta veći je ili manji od prioriteta roditelja (ovisno o tome je li riječ o min‑gomili ili max‑gomili).

Nije teško vidjeti da bi se, kad bismo koristili istu vrijednost, ove dvije strukture podataka nakon kombiniranja pretvorile u lanac, pa na temelju stabla pretraživanja uvodimo još jednu vrijednost za gomilu, $\textit{priority}$. Za vrijednost $\textit{val}$ održavamo svojstvo stabla pretraživanja, a za vrijednost $\textit{priority}$ održavamo svojstvo gomile. Pritom se vrijednost $\textit{priority}$ zadaje slučajno.

Na slici je primjer Treapa (ovdje se koristi min‑gomila, tj. korijen ima najmanji prioritet).

![Primjer Treapa](./images/treap-treap-example.svg)

Zašto se onda toliko trudimo da ova struktura podataka zadovoljava i svojstvo stabla i svojstvo gomile, i to sa slučajno zadanim vrijednostima za gomilu?

Da bismo to razumjeli, najprije treba razumjeti problem običnog binarnog stabla pretraživanja. Kad u obično stablo pretraživanja umećemo novi čvor, trebamo rekurzivno krenuti od korijena; ako je novi čvor manji od trenutačnog čvora, idemo lijevo, i obrnuto.

Na kraju, kad otkrijemo da trenutačni čvor nema odgovarajuće dijete, novi čvor prema svojoj vrijednosti postaje lijevo ili desno dijete trenutačnog čvora.

Ako su vrijednosti umetnutih čvorova slučajne (drugim riječima, umeću se slučajnim redoslijedom), visina takvog običnog stabla pretraživanja bit će mala (blizu $\log n$, gdje je $n$ broj čvorova), a broj čvorova na svakoj razini velik, tj. oblik će mu biti vrlo „debeo”. Treap na gornjoj slici primjer je toga. Stoga će složenost bilo koje operacije biti oko $O(\log n)$.

No to vrijedi samo za slučajan slučaj; ako u obično stablo pretraživanja umećemo čvorove ovim vrlo uređenim redoslijedom:

```plain
1 2 3 4 5
```

stablo će degenerirati u lanac, tj. postat će vrlo „tanko i dugačko” (svaki umetnuti čvor veći je od prethodnih, pa svaki završava kao desno dijete):

![Primjer degeneracije u lanac](./images/treap-search-tree-chain.svg)

Nije teško vidjeti da se složenost upita time pogoršala s $O(\log n)$ na $O(n)$.

Da bi riješio taj problem i postigao razmjerno „uravnoteženo” stanje, Treap održavanjem slučajnih prioriteta koji zadovoljavaju svojstvo gomile „izmiješa” redoslijed umetanja čvorova, čime binarno stablo pretraživanja postiže idealnu složenost i izbjegava problem degeneracije u lanac.

## Dokaz složenosti Treapa

Budući da složenost svih operacija Treapa ovisi o dubini čvora nad kojim se operira, najprije dokazujemo da je očekivana dubina svih čvorova $O(\log n)$.

### Dogovor o oznakama

Radi jednostavnijeg izražavanja dogovaramo se:

-   $n$ je broj čvorova.
-   Vrijednost u čvoru Treapa koja zadovoljava svojstvo binarnog stabla pretraživanja zovemo **vrijednost**, a onu koja zadovoljava svojstvo gomile (dakle slučajnu) zovemo **prioritet**. Bez smanjenja općenitosti neka prioriteti zadovoljavaju svojstvo min‑gomile.
-   $x_k$ označava čvor s $k$‑tom najmanjom vrijednošću.
-   $X_{i,j}$ označava skup $\{x_i,x_{i+1},\cdots,x_{j-1},x_j\}$, tj. skup čvorova od $i$‑tog do $j$‑tog nakon uzlaznog sortiranja po vrijednosti.
-   $\operatorname{dep}(x)$ označava dubinu čvora $x$. Dubina korijena je po dogovoru $0$.
-   $Y_{i,j}$ je indikatorska slučajna varijabla koja je $1$ kad je $x_i$ predak od $x_j$, a inače $0$. Posebno, $Y_{i,i}=0$.
-   $\Pr(A)$ označava vjerojatnost događaja $A$.

### Dokaz očekivane dubine čvora

Budući da je dubina čvora $x_i$ jednaka broju njegovih predaka, vrijedi

$$
\operatorname{dep}(x_i)=\sum_{k=1}^nY_{k,i}.
$$

Prema linearnosti očekivanja vrijedi

$$
E(\operatorname{dep}(x_i))=E\left(\sum_{k=1}^nY_{k,i}\right)=\sum_{k=1}^nE(Y_{k,i}).
$$

Budući da je $Y_{k,i}$ indikatorska slučajna varijabla, njezino je očekivanje jednako vjerojatnosti da bude $1$, pa je

$$
E(\operatorname{dep}(x_i))=\sum_{k=1}^n\Pr(Y_{k,i}=1).
$$

Najprije dokazujemo lemu: $Y_{i,j}=1$ ako i samo ako je prioritet od $x_i$ najmanji u $X_{i,j}$.

??? note "Dokaz leme"
    Razmotrimo slučajeve za $x_i$ i $x_j$.
    
    1.  Ako je $x_i$ korijen: budući da prioriteti zadovoljavaju svojstvo min‑gomile, $x_i$ ima najmanji prioritet i za svaki $x_j$ čvor $x_i$ je predak od $x_j$.
    2.  Ako je $x_j$ korijen: slično, $x_j$ ima najmanji prioritet, pa $x_i$ nema najmanji prioritet u $X_{i,j}$; istodobno $x_i$ nije predak od $x_j$.
    3.  Ako su $x_i$ i $x_j$ u različitim podstablima korijena (jedan u lijevom, drugi u desnom), tada je korijen $r\in X_{i,j}$. Stoga prioritet od $x_i$ ne može biti najmanji u $X_{i,j}$ (jer je korijenov manji). Istodobno, budući da $x_i$ i $x_j$ pripadaju različitim podstablima, $x_i$ nije predak od $x_j$.
    4.  Ako su $x_i$ i $x_j$ u istom podstablu korijena, to podstablo možemo zasebno promatrati kao novi Treap i rekurzivno provesti gornji dokaz.

Prema lemi, očekivanje dubine može se pretvoriti u

$$
E(\operatorname{dep}(x_i))=\sum_{k=1}^n\Pr(x_k=\min X_{i,k}\land k\neq i).
$$

Budući da su prioriteti čvorova slučajni, pretpostavljamo da svaki čvor u skupu $X_{i,j}$ s jednakom vjerojatnošću ima najmanji prioritet, pa je

$$
\begin{aligned}
E(\operatorname{dep}(x_i))&=\sum_{k=1}^n\Pr(x_k=\min X_{i,k}\land k\neq i)\\
&=\sum_{k=1}^{n}\Pr(x_k=\min X_{i,k})-1\\
&=\sum_{k=1}^n\dfrac{1}{|i-k|+1}-1\\
&=\sum_{k=1}^{i-1}\dfrac{1}{i-k+1}+\sum_{k=i+1}^n\dfrac{1}{k-i+1}\\
&=\sum_{j=2}^i\dfrac 1j+\sum_{j=2}^{n-i+1}\dfrac 1j\\
&\le 2\sum_{j=2}^n\dfrac 1j < 2\sum_{j=2}^n\int_{j-1}^j\dfrac 1x\mathrm dx\\
&=2\int_1^n\dfrac 1x\mathrm dx=2\ln n=O(\log n).
\end{aligned}
$$

Dakle, očekivana dubina svakog čvora je $O(\log n)$.

Budući da je složenost operacija običnog binarnog stabla pretraživanja $O(h)$, a složenost održavanja svojstva gomile u Treapu također $O(h)$, očekivana složenost svih operacija Treapa je $O(\log n)$.

???+ note "Intuitivno razumijevanje očekivane složenosti"
    Najprije trebamo uočiti da je atribut $\textit{priority}$ čvora izravno povezan s razinom na kojoj se čvor nalazi. Prisjetimo se svojstva gomile:
    
    -   Vrijednost ($\textit{priority}$) djeteta veća je ili manja od roditeljeve (ovisno o tome je li riječ o min‑gomili ili max‑gomili)
    
    Vidimo da čvorovi na niskoj razini, npr. korijen cijelog stabla, imaju i manji atribut $\textit{priority}$ (u min‑gomili). Osim toga, u običnom stablu pretraživanja čvorovi umetnuti ranije vjerojatnije će imati manju razinu. Atribut $\textit{priority}$ možemo povezati s redoslijedom umetanja; tako postaje jasno zašto Treap pomoću $\textit{priority}$ može izmiješati redoslijed umetanja čvorova.

Pri umetanju novog čvora u Treap treba istodobno održavati svojstvo stabla i svojstvo gomile. Svojstvo stabla pretraživanja može se održavati pri umetanju, a za održavanje svojstva gomile postoje dva pristupa: rotacija te razdvajanje i spajanje. Treapovi koji koriste ta dva pristupa zovu se redom **rotirajući Treap** i **Treap bez rotacija**.

## Rotirajući Treap

**Rotirajući Treap** ravnotežu održava rotacijama, sličnima rotacijama AVL stabla, koje se dijele na **lijevu rotaciju** i **desnu rotaciju**. Dakle, uz zadovoljavanje uvjeta binarnog stabla pretraživanja Treap se balansira prema prioritetima gomile.

Rotirajući Treap pri rješavanju zadataka s običnim balansiranim stablom ima jednu od manjih konstanti među svim balansiranim stablima.

Kod u objašnjenju u nastavku implementira rotirajući Treap pokazivačima; na kraju teksta nalazi se potpuna implementacija poljem.

???+ info "Info"
    `rank` u kodu označava prije spomenuti prioritet (atribut $\textit{priority}$), koji zadovoljava svojstvo min‑gomile.

### Struktura čvora

```cpp
struct Node {
  Node *ch[2];  // adrese dvaju djece
  int val, rank;
  int rep_cnt;  // koliko se puta trenutačna vrijednost (val) ponavlja
  int siz;      // veličina podstabla s korijenom u trenutačnom čvoru

  Node(int val) : val(val), rep_cnt(1), siz(1) {
    ch[0] = ch[1] = nullptr;
    rank = rand();
    // pazite: pri inicijalizaciji rank se zadaje slučajno
  }

  void upd_siz() {
    // ponovno računa vrijednost siz nakon rotacije i brisanja
    siz = rep_cnt;
    if (ch[0] != nullptr) siz += ch[0]->siz;
    if (ch[1] != nullptr) siz += ch[1]->siz;
  }
};
```

### Rotacija

Rotacija je vrlo važna operacija Treapa; služi uglavnom tome da se, uz očuvanje svojstva stabla, prilagode razine različitih čvorova i tako održi svojstvo gomile.

Lijevu i desnu rotaciju možda nije lako razlikovati; evo dvaju razmjerno jasnih obilježja:

Značenje rotacije:

-   Ne narušavajući svojstvo stabla pretraživanja, podstablo na strani suprotnoj smjeru rotacije postaje korijen (npr. lijeva rotacija pretvara desno podstablo u korijen)
-   Svojstvo se ne narušava, a nakon rotacije dijete na strani smjera rotacije postaje prijašnji korijen (npr. kod lijeve rotacije lijevo dijete nakon rotacije je korijen prije rotacije)

Lijeva i desna rotacija međusobno su inverzne, kao na slici.

![Rotacija](./images/treap-rotate.svg)

```cpp
enum rot_type { LF = 1, RT = 0 };

void _rotate(Node *&cur,
             rot_type dir) {  // parametar dir označava smjer rotacije: 0 je desna, 1 lijeva rotacija
  // pazite: proslijeđeni cur referenca je na pokazivač, dakle mijenjanjem ovog
  // cur mijenja se i varijabla; ako je taj cur dijete nekog drugog stabla, pri
  // dolasku preko ch također ćemo doći ovamo

  // kod u nastavku objašnjen je za slučaj lijeve rotacije
  Node *tmp = cur->ch[dir];  // neka C postane korijen;
                             // ovdje je tmp
                             // privremeni pokazivač na čvor koji postaje novi korijen

  /* lijeva rotacija: desno dijete postaje korijen
   *         A                 C
   *        / \               / \
   *       B  C    ---->     A   E
   *         / \            / \
   *        D   E          B   D
   */
  cur->ch[dir] = tmp->ch[!dir];    // neka desno dijete od A postane D
  tmp->ch[!dir] = cur;             // neka lijevo dijete od C postane A
  cur->upd_siz(), tmp->upd_siz();  // ažuriraj informacije o veličini
  cur = tmp;  // na kraju varijablu koja privremeno čuva stablo C dodijeli trenutačnom korijenu (pazite: cur je referenca)
}
```

### Umetanje

Slično umetanju u obično binarno stablo pretraživanja, ali tijekom umetanja treba rotacijama održavati svojstvo gomile za prioritete.

```cpp
void _insert(Node *&cur, int val) {
  if (cur == nullptr) {
    // ako čvora nema, jednostavno ga stvori
    cur = new Node(val);
    return;
  } else if (val == cur->val) {
    // ako postoji čvor s istom vrijednošću, povećaj broj ponavljanja za jedan
    cur->rep_cnt++;
    cur->siz++;
  } else if (val < cur->val) {
    // održavaj svojstvo stabla pretraživanja: ako je val manji od trenutačnog čvora, umetni lijevo, i obrnuto
    _insert(cur->ch[0], val);
    if (cur->ch[0]->rank < cur->rank) {
      // u min-gomili gornji čvor sigurno ima manji prioritet
      // budući da je novoumetnuto lijevo dijete manje od roditelja, lijevo dijete sada mora postati roditelj
      _rotate(cur, RT);  // pazite na prije opisano svojstvo rotacije: da bi lijevo dijete došlo gore, treba desna rotacija
    }
    cur->upd_siz();  // nakon umetanja veličina se mijenja pa je treba ažurirati
  } else {
    _insert(cur->ch[1], val);
    if (cur->ch[1]->rank < cur->rank) {
      _rotate(cur, LF);
    }
    cur->upd_siz();
  }
}
```

### Brisanje

Uglavnom je riječ o razlikovanju slučajeva; različite situacije obrađuju se različito, a nakon brisanja veličina stabla se mijenja pa je treba ažurirati. Osim toga, ako čvor koji brišemo ima i lijevo i desno podstablo, treba razmotriti tko nakon brisanja postaje roditelj (održavamo da čvor s manjim rank bude gore).

```cpp
void _del(Node *&cur, int val) {
  if (val > cur->val) {
    _del(cur->ch[1], val);
    // veća vrijednost je u desnom podstablu, i obrnuto
    cur->upd_siz();
  } else if (val < cur->val) {
    _del(cur->ch[0], val);
    cur->upd_siz();
  } else {
    if (cur->rep_cnt > 1) {
      // ako se čvor koji brišemo ponavlja, dovoljno je smanjiti broj ponavljanja
      cur->rep_cnt--, cur->siz--;
      return;
    }
    uint8_t state = 0;
    state |= (cur->ch[0] != nullptr);
    state |= ((cur->ch[1] != nullptr) << 1);
    // 00 nema nijedno, 01 ima lijevo bez desnog, 10 nema lijevo ima desno, 11 ima oba
    Node *tmp = cur;
    switch (state) {
      case 0:
        delete cur;
        cur = nullptr;
        // nema nijedno dijete, pa čvor jednostavno obriši
        break;
      case 1:  // ima lijevo, nema desno
        cur = tmp->ch[0];
        // korijen postaje lijevo dijete, a zatim se prijašnji korijen briše; pazite da je tmp
        // kopiran iz cur, a cur je referenca
        delete tmp;
        break;
      case 2:  // ima desno, nema lijevo
        cur = tmp->ch[1];
        delete tmp;
        break;
      case 3:
        rot_type dir = cur->ch[0]->rank < cur->ch[1]->rank
                           ? RT
                           : LF;  // dir je ono dijete s manjim rank
        _rotate(cur, dir);  // ova rotacija podiže dijete s manjim prioritetom; rt je 0,
                            // a lf je 1, upravo obrnuto od stvarnih indeksa podstabala
        _del(
            cur->ch[!dir],
            val);  // nakon rotacije prijašnji korijen nalazi se na strani smjera rotacije, pa
                   // treba nastaviti i obrisati taj prijašnji korijen
                   // ako je čvor koji brišemo u „gornjem sloju” cijelog stabla, ovom ga rotacijom
                   // stalno spuštamo dok ne ostane bez podstabala (ili samo s jednim), a zatim ga brišemo.
        cur->upd_siz();
        // brisanje mijenja veličinu
        break;
    }
  }
}
```

### Upit ranga prema vrijednosti

Značenje operacije: u podstablu s korijenom cur pronaći rang vrijednosti val (broj čvorova u tom podstablu manjih od val + 1)

```cpp
int _query_rank(Node *cur, int val) {
  int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
  // broj čvorova u ovom stablu manjih od val
  if (val == cur->val)
    // ako je ovaj čvor upravo onaj koji tražimo
    return less_siz + 1;
  else if (val < cur->val) {
    if (cur->ch[0] != nullptr)
      return _query_rank(cur->ch[0], val);
    else
      return 1;  // ako je lijevo podstablo prazno, vrijednost je manja i od najmanjeg čvora, pa je ona najmanja
  } else {
    if (cur->ch[1] != nullptr)
      // ako je tražena vrijednost veća od ovog čvora, lijevo podstablo ovog čvora i sam čvor sigurno su manji od tražene vrijednosti
      // pa treba dodati te dvije veličine i rezultat traženja udesno
      // (rang vrijednosti val u podstablu s korijenom u desnom djetetu)
      return less_siz + cur->rep_cnt + _query_rank(cur->ch[1], val);
    else
      return cur->siz + 1;
    // ako nema desnog podstabla, cijelo stablo + 1 jednako je less_siz + cur->rep_cnt + 1
  }
}
```

### Upit vrijednosti prema rangu

Da bismo tražili vrijednost prema rangu, najprije moramo znati kako odrediti u kojem se dijelu stabla traženi čvor nalazi:

Slijedi tablica s kriterijem odlučivanja:

| Lijevo podstablo             | Korijen/trenutačni čvor                                                           | Desno podstablo                                           |
| ---------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------- |
| rang ≤ veličina lijevog podstabla | rang > veličina lijevog podstabla i ≤ veličina lijevog podstabla + broj ponavljanja korijena | rang > veličina lijevog podstabla + broj ponavljanja korijena |

Pazite da pri rekurziji u desno podstablo treba obraditi izvorni `rank`. Rekurzija zapravo traži vrijednost s tim rangom u desnom podstablu, pa da bismo rang pretvorili u rang relativan prema desnom podstablu, od izvornog `rank` treba oduzeti veličinu lijevog podstabla i broj ponavljanja korijena.

Sve čvorove možemo zamisliti kao sortirano polje ili brojevni pravac (kao u nastavku),

    1 -> |čvorovi lijevog podstabla|korijen|čvorovi desnog podstabla| -> n
                                                 ^
                                                 traženi rang
                                           ⬇pretvorba u rang relativan prema desnom podstablu
    1 -> |čvorovi desnog podstabla| -> n
           ^
           traženi rang

Pretvorba se ovdje svodi na to da se od ranga oduzmu veličina lijevog podstabla i broj ponavljanja korijena.

```cpp
int _query_val(Node *cur, int rank) {
  // traži vrijednost čvora s rangom rank u stablu
  int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
  // less siz je veličina lijevog podstabla
  if (rank <= less_siz)
    return _query_val(cur->ch[0], rank);
  else if (rank <= less_siz + cur->rep_cnt)
    return cur->val;
  else
    return _query_val(cur->ch[1], rank - less_siz - cur->rep_cnt);  // vidi gore
}
```

### Traženje prvog čvora manjeg od val

Pazite da se ovdje koristi globalna varijabla klase, `q_prev_tmp`.

Ta se vrijednost mijenja samo kad je val veći od vrijednosti trenutačnog čvora, pa vraćanje te varijable znači vraćanje posljednje vrijednosti kod koje je val još bio veći od trenutačnog čvora; nakon toga čvorovi su manji.

```cpp
int _query_prev(Node *cur, int val) {
  if (val <= cur->val) {
    // još uvijek veće od val ili jednako, pa traži u lijevom podstablu
    if (cur->ch[0] != nullptr) return _query_prev(cur->ch[0], val);
  } else {
    // samo ulaskom u ovaj else ažurira se vrijednost q_prev_tmp
    q_prev_tmp = cur->val;
    // trenutačni čvor već je manji od val, ali nije sigurno da je najveći, pa treba nastaviti tražiti u desnom podstablu
    if (cur->ch[1] != nullptr) _query_prev(cur->ch[1], val);
    // sljedeće rekurzije možda više neće mijenjati q_prev_tmp,
    // pa jednostavno vrati tu vrijednost; u svakom slučaju vraća se cur->val
    // iz posljednjeg ulaska u ovaj else
    return q_prev_tmp;
  }
  return NIL;
}
```

### Traženje prvog čvora većeg od val

Vrlo slično prethodnom, samo su zamijenjeni znakovi veće i manje.

```cpp
int _query_nex(Node *cur, int val) {
  if (val >= cur->val) {
    if (cur->ch[1] != nullptr) return _query_nex(cur->ch[1], val);
  } else {
    q_nex_tmp = cur->val;
    if (cur->ch[0] != nullptr) _query_nex(cur->ch[0], val);
    return q_nex_tmp;
  }
  return NIL;
}
```

## Treap bez rotacija

Način rada Treapa bez rotacija čini ga prirodno pogodnim za održavanje nizova, perzistentnost i slična svojstva.

**Treap bez rotacija** zove se i Treap s razdvajanjem i spajanjem. Ima samo dvije temeljne operacije, **razdvajanje** i **spajanje**. Pomoću njih se u mnogim situacijama ostale operacije mogu implementirati jednostavnije nego kod rotirajućeg Treapa. U nastavku redom predstavljamo te dvije operacije.

???+ note "Napomena"
    Pri objašnjavanju Treapa bez rotacija valja spomenuti **FHQ‑Treap** (autor Fan Haoqiang), tj. perzistentni Treap bez rotacija koji podržava intervalne operacije. Više o tome u prezentaciji „Fan Haoqiang o strukturama podataka”.

### Razdvajanje (split)

#### Razdvajanje po vrijednosti

Postupak razdvajanja prima dva parametra: pokazivač na korijen $\textit{cur}$ i ključnu vrijednost $\textit{key}$. Rezultat je razdvajanje Treapa na koji pokazuje korijen na dva Treapa: prvi Treap sadrži sve čvorove s vrijednošću ($\textit{val}$) manjom ili jednakom $\textit{key}$, a drugi sve čvorove s vrijednošću većom od $\textit{key}$.

Postupak najprije provjerava je li $\textit{key}$ manji od vrijednosti $\textit{cur}$; ako jest, $\textit{cur}$ i cijelo njegovo desno podstablo veći su od $\textit{key}$ i pripadaju drugom Treapu. Naravno, i dio lijevog podstabla može imati vrijednosti veće od $\textit{key}$, pa treba nastaviti rekurzivno razdvajati lijevo podstablo. Dio lijevog podstabla veći od $\textit{key}$ postavljamo kao lijevo podstablo od $\textit{cur}$; tako su svi čvorovi u $\textit{cur}$ veći od $\textit{key}$.

Analogno, ako je $\textit{key}$ veći ili jednak vrijednosti $\textit{cur}$, cijelo lijevo podstablo od $\textit{cur}$ i sam $\textit{cur}$ manji su ili jednaki $\textit{key}$ i pripadaju prvom Treapu nakon razdvajanja. Osim toga, dio desnog podstabla od $\textit{cur}$ također može biti manji ili jednak $\textit{key}$, pa treba nastaviti rekurzivno razdvajati desno podstablo. Dio manji ili jednak $\textit{key}$ postavljamo kao desno podstablo od $\textit{cur}$; tako su svi čvorovi u $\textit{cur}$ manji ili jednaki $\textit{key}$.

Slika prikazuje razdvajanje po vrijednosti u slučaju kad je vrijednost $\textit{cur}$ manja ili jednaka $\textit{key}$.[^ref1]

![Razdvajanje po vrijednosti](./images/treap-none-rot-split-by-val.svg)

```cpp
pair<Node *, Node *> split(Node *cur, int key) {
  if (cur == nullptr) return {nullptr, nullptr};
  if (cur->val <= key) {
    // cur i njegovo lijevo podstablo sigurno pripadaju prvom stablu nakon razdvajanja
    auto temp = split(cur->ch[1], key);
    // ali i dio njegova desnog podstabla može biti manji od key
    cur->ch[1] = temp.first;
    // dio manji od key izdvajamo i postavljamo kao desno podstablo od cur, tako da je cijeli cur manji od
    // key; ostatak desnog podstabla postaje drugi Treap nakon razdvajanja
    cur->upd_siz();
    // nakon razdvajanja veličina stabla se mijenja pa je treba ažurirati
    return {cur, temp.second};
  } else {
    // kao gore
    auto temp = split(cur->ch[0], key);
    cur->ch[0] = temp.second;
    cur->upd_siz();
    return {temp.first, cur};
  }
}
```

#### Razdvajanje po rangu

U usporedbi s razdvajanjem po vrijednosti ova je operacija sličnija upitu vrijednosti prema rangu u rotirajućem Treapu (rang čvora je broj čvorova u stablu s vrijednošću manjom od vrijednosti tog čvora $+ 1$):

Funkcija prima dva parametra, pokazivač na čvor $\textit{cur}$ i rang $\textit{rk}$, a vraća tri Treapa nakon razdvajanja.

U prvom Treapu rang svakog čvora manji je od $\textit{rk}$, u drugom je rang jednak $\textit{rk}$ i taj drugi Treap ima samo jedan čvor (ne može ih biti više jednakih; ako ih ima, povećava se `cnt` u strukturi `Node`), a u trećem je rang veći.

Težište ove operacije jest odrediti u kojem se dijelu stabla nalazi čvor čiji je rang jednak $\textit{rk}$; to je ujedno važan dio upita vrijednosti prema rangu u rotirajućem Treapu, vrlo detaljno objašnjen ranije, pa ga ovdje ne ponavljamo.

Osim toga, rekurzivni dio ove operacije vrlo je sličan razdvajanju po vrijednosti, pa ga ne ponavljamo.

```cpp
tuple<Node *, Node *, Node *> split_by_rk(Node *cur, int rk) {
  if (cur == nullptr) return {nullptr, nullptr, nullptr};
  int ls_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
  if (rk <= ls_siz) {
    // čvor s rangom jednakim rk je u lijevom podstablu
    Node *l, *mid, *r;
    tie(l, mid, r) = split_by_rk(cur->ch[0], rk);
    cur->ch[0] = r;  // rangovi u vraćenom trećem Treapu svi su veći od rk
    // nakon što lijevo podstablo od cur postane r, rangovi svih čvorova u cur veći su od rk
    cur->upd_siz();
    return {l, mid, cur};
  } else if (rk <= ls_siz + cur->cnt) {
    // čvor s rangom jednakim rk je trenutačni čvor
    Node *lt = cur->ch[0];
    Node *rt = cur->ch[1];
    cur->ch[0] = cur->ch[1] = nullptr;
    // drugi Treap nakon razdvajanja ima samo jedan čvor, pa mu podstabla treba postaviti na prazno
    return {lt, cur, rt};
  } else {
    // čvor s rangom jednakim rk je u desnom podstablu
    // rekurzija kao gore
    Node *l, *mid, *r;
    tie(l, mid, r) = split_by_rk(cur->ch[1], rk - ls_siz - cur->cnt);
    cur->ch[1] = l;
    cur->upd_siz();
    return {cur, mid, r};
  }
}
```

### Spajanje (merge)

Postupak spajanja prima dva parametra: pokazivač na korijen lijevog Treapa $\textit{u}$ i pokazivač na korijen desnog Treapa $\textit{v}$. Mora vrijediti da su vrijednosti svih čvorova u $\textit{u}$ manje ili jednake vrijednostima svih čvorova u $\textit{v}$. Općenito, dva Treapa koja spajamo prije su razdvojena iz jednog Treapa, pa nije teško osigurati da su vrijednosti svih čvorova u $\textit{u}$ manje od onih u $\textit{v}$

U rotirajućem Treapu pomoću rotacija održavamo da $\textit{priority}$ zadovoljava svojstvo gomile, a rotacije pritom ne smiju narušiti svojstvo stabla. U Treapu bez rotacija isti učinak postižemo spajanjem.

Budući da su oba Treapa već uređena, pri spajanju trebamo razmotriti samo koje stablo „staviti gore”, a koje „staviti dolje”, tj. odrediti koje stablo postaje podstablo. Očito, prema svojstvu gomile gore stavljamo ono s manjim $\textit{priority}$ (ovdje koristimo min‑gomilu).

Istodobno moramo zadovoljiti i svojstvo stabla pretraživanja, pa ako je $\textit{priority}$ korijena od $\textit{u}$ manji od onoga od $\textit{v}$, tada $\textit{u}$ postaje novi korijen, a $\textit{v}$, čije su vrijednosti veće od $\textit{u}$, spaja se s desnim podstablom od $\textit{u}$; u suprotnom $\textit{v}$ postaje novi korijen, a budući da su vrijednosti od $u$ manje od $\textit{v}$, $u$ se spaja s lijevim podstablom od $v$.

```cpp
Node *merge(Node *u, Node *v) {
  // oba proslijeđena stabla iznutra već zadovoljavaju svojstvo stabla pretraživanja
  // i vrijednosti svih čvorova u u < vrijednosti svih čvorova u v
  // pa pri spajanju treba održavati svojstvo gomile
  // ovdje se koristi min-gomila
  if (u == nullptr && v == nullptr) return nullptr;
  if (u != nullptr && v == nullptr) return u;
  if (v != nullptr && u == nullptr) return v;

  if (u->prio < v->prio) {
    // prio od u je manji, u treba biti roditelj
    u->ch[1] = merge(u->ch[1], v);
    // budući da je v veći od u, v postaje desno podstablo od u
    u->upd_siz();
    return u;
  } else {
    // v je manji, v treba biti roditelj
    v->ch[0] = merge(u, v->ch[0]);
    // u je manji od v, pa su parametri rekurzije ovakvi
    v->upd_siz();
    return v;
  }
}
```

### Umetanje

U Treapu bez rotacija osnovne operacije poput umetanja, brisanja i upita ranga prema vrijednosti mogu se implementirati i običnim metodama binarnog stabla pretraživanja i pomoću razdvajanja i spajanja. Općenito, implementacija razdvajanjem i spajanjem sažetija je, ali nešto sporija[^ref2]. Radi boljeg razumijevanja Treapa bez rotacija, sve operacije u nastavku implementirane su razdvajanjem i spajanjem.

Pri implementaciji umetanja koristimo neka svojstva razdvajanja. Naime, čvorovi s vrijednošću manjom ili jednakom $\textit{val}$ dospijevaju u prvi Treap.

Pretpostavimo dakle da trenutačni Treap razdvojimo po $\textit{val}$. Dobivamo sljedeća dva stabla koja zadovoljavaju uvjete:

$$
\begin{aligned}
T_1 &\le val\\
T_2 &> val
\end{aligned}
$$

gdje $T_1$ označava skup svih čvorova koji nakon razdvajanja dospijevaju u prvi Treap, a $T_2$ u drugi.

Ako $T_1$ dalje razdvojimo po $\textit{val} - 1$, nastaju sljedeća dva stabla koja zadovoljavaju uvjete:

$$
\begin{gathered}
T_{1\ \text{left}} \le val - 1\\
T_{1\ \text{right}} > val - 1 \ \And \ T_{1\ \text{right}} \le val
\end{gathered}
$$

gdje $T_{1\ \text{left}}$ označava skup svih čvorova koji nakon razdvajanja $T_1$ dospijevaju u prvi Treap, a $T_{1\ \text{right}}$ u drugi. Drugi dio gornjeg izraza, $\And \ T_{1\ \text{right}} \le val$, dolazi iz uvjeta $T_1 \le val$ koji $T_1$ zadovoljava.

Nije teško vidjeti da, čim su $\textit{val}$ i vrijednosti čvorova cijeli brojevi (u većini primjena koriste se cijeli brojevi), postoji samo jedan čvor koji zadovoljava uvjet za $T_{1\ \text{right}}$, a to je čvor s vrijednošću jednakom $\textit{val}$.

Ako pri umetanju otkrijemo da čvor koji zadovoljava $T_{1\ \text{right}}$ postoji, dovoljno je povećati broj ponavljanja; inače stvaramo novi čvor.

Pazite da nakon razdvajanja stablo treba spajanjem „zalijepiti” natrag kako bi se moglo dalje koristiti. Osim toga, pazite da redoslijed parametara spajanja ima zahtjev: vrijednosti svih čvorova prvog stabla moraju biti manje od onih u drugom.

```cpp
void insert(int val) {
  auto temp = split(root, val);
  // prema vrijednosti val razdvoji cijelo stablo na dva
  // pazite na implementaciju split: podstablo jednako val je u lijevom podstablu
  auto l_tr = split(temp.first, val - 1);
  // lijevo podstablo od l_tr je <= val - 1; ako postoji čvor = val, sigurno je u desnom podstablu
  Node *new_node;
  if (l_tr.second == nullptr) {
    // ako čvora nema, stvori novi, inače samo povećaj broj ponavljanja.
    new_node = new Node(val);
  } else {
    l_tr.second->cnt++;
    l_tr.second->upd_siz();
  }
  Node *l_tr_combined =
      merge(l_tr.first, l_tr.second == nullptr ? new_node : l_tr.second);
  // spoji T_1 left i T_1 right
  root = merge(l_tr_combined, temp.second);
  // spoji T_1 i T_2
}
```

### Brisanje

Brisanje koristi metodu sličnu umetanju: pronađe se čvor s vrijednošću jednakom $\textit{val}$ i obriše.

```cpp
void del(int val) {
  auto temp = split(root, val);
  auto l_tr = split(temp.first, val - 1);
  if (l_tr.second->cnt > 1) {
    // ako je broj ponavljanja ovog čvora veći od 1, dovoljno ga je smanjiti
    l_tr.second->cnt--;
    l_tr.second->upd_siz();
    l_tr.first = merge(l_tr.first, l_tr.second);
  } else {
    if (temp.first == l_tr.second) {
      // moguće je da se cijeli T_1 sastoji samo od ovog čvora, pa i njega treba postaviti na null kao oznaku brisanja
      temp.first = nullptr;
    }
    delete l_tr.second;
    l_tr.second = nullptr;
  }
  root = merge(l_tr.first, temp.second);
}
```

### Upit ranga prema vrijednosti

Rang je broj čvorova manjih od te vrijednosti $+ 1$, pa trenutačno stablo razdvajamo po $\textit{val} - 1$; prvo stablo nakon razdvajanja zadovoljava:

$$
T_1 \le val - 1
$$

Ako su vrijednosti stabla i $\textit{val}$ cijeli brojevi, $T_1$ sadrži sve čvorove s vrijednošću manjom od $\textit{val}$.

```cpp
int qrank_by_val(Node* cur, int val) {
  auto temp = split(cur, val - 1);
  int ret = (temp.first == nullptr ? 0 : temp.first->siz) + 1;  // prema definiciji + 1
  root = merge(temp.first, temp.second);  // nakon razdvajanja zalijepi natrag
  return ret;
}
```

### Upit vrijednosti prema rangu

Nakon poziva funkcije `split_by_rk()` vraćaju se tri razdvojena Treapa, od kojih drugi sadrži samo jedan čvor čiji je rang jednak $\textit{rk}$, pa jednostavno vraćamo $\textit{val}$ tog čvora.

```cpp
int qval_by_rank(Node *cur, int rk) {
  Node *l, *mid, *r;
  tie(l, mid, r) = split_by_rk(cur, rk);
  int ret = mid->val;
  root = merge(merge(l, mid), r);
  return ret;
}
```

### Traženje prvog čvora manjeg od val

Problem možemo svesti na traženje čvora s najvećim rangom među svim čvorovima manjima od $\textit{val}$. Treap razdvojimo po $\textit{val}$; vrijednosti čvorova u vraćenom prvom Treapu sve su manje od $\textit{val}$, a zatim pozivom `qval_by_rank()` nađemo čvor s najvećom vrijednošću u tom stablu.

```cpp
int qprev(int val) {
  auto temp = split(root, val - 1);
  // temp.first je podstablo s vrijednostima manjima od val
  int ret = qval_by_rank(temp.first, temp.first->siz);
  // ovdje tražimo vrijednost najvećeg među svim čvorovima manjima od val
  root = merge(temp.first, temp.second);
  return ret;
}
```

### Traženje prvog čvora većeg od val

Slično prethodnoj operaciji, problem možemo svesti na traženje čvora s najmanjim rangom među svim čvorovima većima od $\textit{val}$. Nakon razdvajanja po $\textit{val}$ vrijednosti svih čvorova u vraćenom drugom Treapu veće su od $\textit{val}$.

Zatim u tom stablu tražimo vrijednost čvora s rangom $1$ (tj. čvora s najmanjom vrijednošću) i tako uspješno nalazimo prvi čvor veći od $\textit{val}$.

```cpp
int qnex(int val) {
  auto temp = split(root, val);
  int ret = qval_by_rank(temp.second, 1);
  // traži najmanju vrijednost u podstablu svih čvorova većih od val
  root = merge(temp.first, temp.second);
  return ret;
}
```

### Izgradnja stabla (build)

Niz $\{a_n\}$ od $n$ čvorova pretvaramo u Treap.

Možemo redom grubom silom umetati tih $n$ čvorova: pri svakom umetanju čvora s vrijednošću $v$ cijeli Treap razdvojimo po vrijednosti na dio s vrijednostima manjima ili jednakima $v$ i dio s vrijednostima većima od $v$, zatim stvorimo novi čvor s vrijednošću $v$ i oba dijela i novi čvor redom spojimo od manjeg prema većem; složenost jednog umetanja je $O(\log n)$, a ukupna vremenska složenost $O(n\log n)$.

U nekim zadacima može biti više umetanja čitavog sortiranog niza, pa je tada izgradnju stabla potrebno obaviti u vremenskoj složenosti $O(n)$.

Prvi način: tijekom rekurzivne izgradnje svaki put za korijen intervala uzmemo sredinu trenutačnog intervala i svakom čvoru dodijelimo prikladan prioritet tako da novo stablo zadovoljava svojstvo gomile. Tako je zajamčena visina stabla $O(\log n)$.

Drugi način: tijekom rekurzivne izgradnje svaki put za korijen intervala uzmemo sredinu trenutačnog intervala, a zatim svakom čvoru dodijelimo slučajan prioritet. Tako je zajamčena visina stabla $O(\log n)$, ali nije zajamčeno svojstvo gomile. I to je ispravno, jer prioriteti Treapa bez rotacija služe tome da operacija `merge` bude malo slučajnija, a ne tome da jamče visinu stabla.

Treći način: uočimo da je Treap Kartezijevo stablo, pa možemo iskoristiti $O(n)$ izgradnju Kartezijeva stabla, tj. monotonim stogom održavati desni lanac.

### Intervalne operacije Treapa bez rotacija

#### Izgradnja stabla

Velika prednost Treapa bez rotacija u odnosu na rotirajući Treap jest mogućnost implementacije raznih intervalnih operacija; u nastavku na primjeru [predloška](https://loj.ac/problem/105) za umjetničko balansirano stablo predstavljamo intervalne operacije Treapa.

> Trebate napisati strukturu podataka (vidi naslov zadatka) koja održava uređeni niz.
>
> Treba podržati sljedeću operaciju: okretanje intervala; npr. ako je izvorni uređeni niz $5\ 4\ 3\ 2\ 1$, a okreće se interval $[2,4]$, rezultat je $5\ 2\ 3\ 4\ 1$.
> Za $100\%$ podataka vrijedi $1 \le n$ (početna duljina intervala), $m$ (broj okretanja) $\le 10^5$

U ovom zadatku trebamo implementirati okretanje intervala, pa najprije trebamo razmotriti kako izgraditi stablo; izgrađeno stablo treba predstavljati početni interval.

Dovoljno je indekse intervala redom umetnuti u Treap; tako pri inorder obilasku (najprije lijevo podstablo, zatim trenutačni čvor, na kraju desno podstablo) dobivamo taj interval[^ref3].

Znamo da se u običnom binarnom stablu pretraživanja umetanjem čvorova rastućim redoslijedom dobiva dugačak lanac, a inorder obilaskom prirodno dobivamo taj interval.

<div align=center>
  <img style="width: 50%; " src="./images/treap-search-tree-chain.svg" >
</div>

Kao na gornjoj slici, umetanjem čvorova redoslijedom $1\ 2\ 3\ 4\ 5$ u obično stablo pretraživanja, inorder obilaskom također dobivamo $1\ 2\ 3\ 4\ 5$.

Ali u Treapu se nakon umetanja rastućim redoslijedom pri spajanju struktura stabla prilagođava prema $\textit{priority}$; kako u takvoj situaciji osigurati da inorder obilazak sigurno daje ispravan ispis?

Za razumijevanje ovog problema može se pogledati [izgradnja Kartezijeva stabla monotonim stogom](./cartesian-tree.md).

Neka je novoumetnuti čvor $\textit{u}$.

Najprije, budući da čvorove umećemo rastućim redoslijedom, svaki novoumetnuti čvor sigurno se spaja na desni lanac Treapa (tj. lanac čvorova kroz koje prolazimo idući od korijena stalno u desno podstablo).

Počevši od korijena, $\textit{priority}$ čvorova na desnom lancu raste (min‑gomila). Možemo dakle naći prvi čvor na desnom lancu čiji je $\textit{priority}$ veći od onoga od $\textit{u}$; nazovimo ga $\textit{v}$ i zamijenimo ga s $\textit{u}$.

Budući da je $\textit{u}$ sigurno veći od svih ostalih čvorova u stablu, $\textit{v}$ i njegovo podstablo trebamo postaviti kao lijevo podstablo od $\textit{u}$. Pritom $\textit{u}$ nema desno podstablo.

Vidimo da je pri inorder obilasku $\textit{u}$ sigurno posljednji obiđen (jer je $\textit{u}$ posljednji na desnom lancu, a pri inorder obilasku desno se podstablo obilazi posljednje).

Slika prikazuje promjenu pri umetanju čvora $5$ kad u Treap rastućim redoslijedom umećemo čvorove $1 \sim 5$; pomoću nje se može bolje razumjeti postupak umetanja rastućim redoslijedom.

![Umetanje čvora](./images/treap-none-rot-seg-build.svg)

#### Okretanje intervala

Pri okretanju intervala $[l, r]$ osnovna je ideja razdvojiti stablo na tri intervala $[1, l - 1],\ [l, r],\ [r + 1, n]$, a zatim okrenuti srednji $[l, r]$[^ref3].

Konkretno, okretanje znači zamijeniti mjesta lijevog i desnog djeteta svakog čvora podstabla u intervalu. Slika prikazuje Treap nakon okretanja intervala $[3, 4]$ i $[3, 5]$ Treapa s gornje slike.

![Okretanje intervala](./images/treap-none-rot-seg-flip-ex.svg)

Pazite: ako okrećemo na ovaj način, pri svakom okretanju intervala $[l, r]$ mjesta mijenja $r - l$ čvorova; tako česte operacije očito ne mogu zadovoljiti ograničenje $10^5$, a složenost jednog okretanja $O(n \times \log_2 n)$ čak je gora od grube sile (jer osim linearnog vremena za zamjenu čvorova trošimo još $O(\log_2 n)$ vremena da u stablu nađemo čvorove koje treba zamijeniti).

Pogledamo li ponovno zahtjeve zadatka, vidimo da treba ispisati samo konačni interval nakon svih operacija, pa zamjene ne treba doista obavljati svaki put. Stoga možemo iskoristiti lijene oznake (lazy tag), uobičajene kod segmentnog stabla, za optimizaciju složenosti. Pri zamjeni dovoljno je na roditelja staviti oznaku koja znači da svakom čvoru u tom podstablu treba zamijeniti lijevo i desno dijete.

U segmentnom stablu lijene oznake obično spuštamo pri ažuriranju i upitu. Razlog je taj što se pri ažuriranju i upitu raspon koji želimo ažurirati/ispitati ne mora podudarati s rasponom koji lijena oznaka predstavlja, pa najprije treba spustiti oznaku kako bi ispitane i ažurirane vrijednosti bile ispravne.

Isto vrijedi i u Treapu bez rotacija. Konkretno, Treap razdvajamo na tri prije spomenuta stabla, srednjem stavljamo lijenu oznaku i zatim spajamo ta tri stabla. Budući da se interval koji želimo okrenuti i interval koji lijena oznaka predstavlja ne moraju podudarati, oznaku treba spuštati pri razdvajanju. Osim toga, razdvajanje i spajanje mijenjaju svaki čvor i čvorove koje njegova lijena oznaka predstavlja, pa lijenu oznaku treba spustiti i prije spajanja.

Drugim riječima, kad se struktura stabla mijenja, tj. kad pri razdvajanju ili spajanju trebamo promijeniti informacije o lijevom i desnom djetetu nekog čvora, oznaku treba spustiti prije toga, a ne poslije, jer lijenu oznaku treba prenijeti djeci; ako nakon promjene djece oznaka još nije spuštena, ona više nema kome biti spuštena.[^ref4]

<!-- TODO: može se dodati slika koja objašnjava zašto oznake treba spuštati pri razdvajanju i spajanju -->

Slijedi objašnjenje koda; kod se oslanja na[^ref3].

Budući da je većina intervalnih operacija jednaka kao kod običnog Treapa bez rotacija, ovdje objašnjavamo samo ono što se razlikuje od običnog Treapa bez rotacija.

#### Spuštanje oznake

Pazite da lijena oznaka ovdje znači da svakom djetetu u ovom stablu treba zamijeniti mjesto. Stoga, ako i dijete trenutačnog čvora ima lijenu oznaku, dva se okretanja poništavaju. Ako dijete ne treba okretati, lijenu oznaku treba dalje spustiti na dijete.

```cpp
// pushdown je ovdje članska funkcija klase Node, a to_rev je lijena oznaka
void pushdown() {
  swap(ch[0], ch[1]);
  if (ch[0] != nullptr) ch[0]->to_rev ^= 1;
  if (ch[1] != nullptr) ch[1]->to_rev ^= 1;
  to_rev = false;
}

void check_tag() {
  if (to_rev) pushdown();
}
```

#### Razdvajanje

Pazite da u ovom zadatku, zbog okretanja, $\textit{val}$ u Treapu ne zadovoljava svojstvo binarnog stabla pretraživanja (vidi sliku u odjeljku o okretanju intervala), pa prema $\textit{val}$ ne možemo odlučiti treba li rekurzivno ići u lijevo ili desno podstablo.

Stoga je razdvajanje ovdje sličnije razdvajanju po rangu u običnom Treapu bez rotacija: prema veličini trenutačnog stabla odlučuje se ide li se rekurzivno lijevo ili desno; drugim riječima, odlučujemo prema početnom položaju čvora u stablu.

Rangovi čvorova u vraćenom prvom Treapu svi su manji ili jednaki $\textit{sz}$, a rangovi čvorova u drugom Treapu svi su veći od $\textit{sz}$.

```cpp
#define siz(_) (_ == nullptr ? 0 : _->siz)

pair<Node*, Node*> split(Node* cur, int sz) {
  // odlučuje se prema veličini stabla
  if (cur == nullptr) return {nullptr, nullptr};
  cur->check_tag();
  // prije razdvajanja najprije spusti oznaku
  if (sz <= siz(cur->ch[0])) {
    auto temp = split(cur->ch[0], sz);
    cur->ch[0] = temp.second;
    cur->upd_siz();
    return {temp.first, cur};
  } else {
    auto temp =
        split(cur->ch[1],
              sz - siz(cur->ch[0]) -
                  1);  // ova je pretvorba objašnjena u odjeljku „Upit vrijednosti prema rangu” rotirajućeg Treapa
    cur->ch[1] = temp.first;
    cur->upd_siz();
    return {cur, temp.second};
  }
}
```

#### Spajanje

Jedino na što treba paziti jest spuštanje lijene oznake prije spajanja

```cpp
Node *merge(Node *sm, Node *bg) {
  // small, big
  if (sm == nullptr && bg == nullptr) return nullptr;
  if (sm != nullptr && bg == nullptr) return sm;
  if (sm == nullptr && bg != nullptr) return bg;
  sm->check_tag(), bg->check_tag();
  if (sm->prio < bg->prio) {
    sm->ch[1] = merge(sm->ch[1], bg);
    sm->upd_siz();
    return sm;
  } else {
    bg->ch[0] = merge(sm, bg->ch[0]);
    bg->upd_siz();
    return bg;
  }
}
```

#### Okretanje intervala

Kao što je prije opisano, razdvojimo tri intervala $[1, l - 1],\ [l, r],\ [r + 1, n]$, srednjem stavimo oznaku i zatim ih spojimo.

```cpp
void seg_rev(int l, int r) {
  // less i more ovdje su relativni prema l
  auto less = split(root, l - 1);
  // svi manji ili jednaki l - 1 bit će u lijevom podstablu od less
  auto more = split(less.second, r - l + 1);
  // interval prvih r - l + 1 elemenata počevši od l
  more.first->to_rev = true;
  root = merge(less.first, merge(more.first, more.second));
}
```

#### Ispis inorder obilaskom

Pazite da pri ispisu treba spuštati oznake.

```cpp
void print(Node* cur) {
  if (cur == nullptr) return;
  cur->check_tag();
  // inorder obilazak -> najprije lijevo podstablo, zatim sam čvor, na kraju desno podstablo
  print(cur->ch[0]);
  cout << cur->val << " ";
  print(cur->ch[1]);
}
```

## Potpuni kod

### Rotirajući Treap

#### Implementacija pokazivačima

??? note "Potpuni kod"
    Slijedi potpuna verzija prije objašnjenog koda; to je predložak za obično balansirano stablo.
    
    ```cpp
    // author: (ttzytt)[ttzytt.com]
    #include <cstdint>
    #include <cstdio>
    #include <cstdlib>
    using namespace std;
    
    struct Node {
      Node *ch[2];
      int val, rank;
      int rep_cnt;
      int siz;
    
      Node(int val) : val(val), rep_cnt(1), siz(1) {
        ch[0] = ch[1] = nullptr;
        rank = rand();
      }
    
      void upd_siz() {
        siz = rep_cnt;
        if (ch[0] != nullptr) siz += ch[0]->siz;
        if (ch[1] != nullptr) siz += ch[1]->siz;
      }
    };
    
    class Treap {
     private:
      Node *root;
    
      constexpr static int NIL = -1;  // označava da tražena vrijednost ne postoji
    
      enum rot_type { LF = 1, RT = 0 };
    
      int q_prev_tmp = 0, q_nex_tmp = 0;
    
      void _rotate(Node *&cur, rot_type dir) {  // 0 je desna, 1 lijeva rotacija
        Node *tmp = cur->ch[dir];
        cur->ch[dir] = tmp->ch[!dir];
        tmp->ch[!dir] = cur;
        cur->upd_siz(), tmp->upd_siz();
        cur = tmp;
      }
    
      void _insert(Node *&cur, int val) {
        if (cur == nullptr) {
          cur = new Node(val);
          return;
        } else if (val == cur->val) {
          cur->rep_cnt++;
          cur->siz++;
        } else if (val < cur->val) {
          _insert(cur->ch[0], val);
          if (cur->ch[0]->rank < cur->rank) {
            _rotate(cur, RT);
          }
          cur->upd_siz();
        } else {
          _insert(cur->ch[1], val);
          if (cur->ch[1]->rank < cur->rank) {
            _rotate(cur, LF);
          }
          cur->upd_siz();
        }
      }
    
      void _del(Node *&cur, int val) {
        if (val > cur->val) {
          _del(cur->ch[1], val);
          cur->upd_siz();
        } else if (val < cur->val) {
          _del(cur->ch[0], val);
          cur->upd_siz();
        } else {
          if (cur->rep_cnt > 1) {
            cur->rep_cnt--, cur->siz--;
            return;
          }
          uint8_t state = 0;
          state |= (cur->ch[0] != nullptr);
          state |= ((cur->ch[1] != nullptr) << 1);
          // 00 nema nijedno, 01 ima lijevo bez desnog, 10 nema lijevo ima desno, 11 ima oba
          Node *tmp = cur;
          switch (state) {
            case 0:
              delete cur;
              cur = nullptr;
              break;
            case 1:  // ima lijevo, nema desno
              cur = tmp->ch[0];
              delete tmp;
              break;
            case 2:  // ima desno, nema lijevo
              cur = tmp->ch[1];
              delete tmp;
              break;
            case 3:
              rot_type dir = cur->ch[0]->rank < cur->ch[1]->rank ? RT : LF;
              _rotate(cur, dir);
              _del(cur->ch[!dir], val);
              cur->upd_siz();
              break;
          }
        }
      }
    
      int _query_rank(Node *cur, int val) {
        int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
        if (val == cur->val)
          return less_siz + 1;
        else if (val < cur->val) {
          if (cur->ch[0] != nullptr)
            return _query_rank(cur->ch[0], val);
          else
            return 1;
        } else {
          if (cur->ch[1] != nullptr)
            return less_siz + cur->rep_cnt + _query_rank(cur->ch[1], val);
          else
            return cur->siz + 1;
        }
      }
    
      int _query_val(Node *cur, int rank) {
        int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
        if (rank <= less_siz)
          return _query_val(cur->ch[0], rank);
        else if (rank <= less_siz + cur->rep_cnt)
          return cur->val;
        else
          return _query_val(cur->ch[1], rank - less_siz - cur->rep_cnt);
      }
    
      int _query_prev(Node *cur, int val) {
        if (val <= cur->val) {
          if (cur->ch[0] != nullptr) return _query_prev(cur->ch[0], val);
        } else {
          q_prev_tmp = cur->val;
          if (cur->ch[1] != nullptr) _query_prev(cur->ch[1], val);
          return q_prev_tmp;
        }
        return NIL;
      }
    
      int _query_nex(Node *cur, int val) {
        if (val >= cur->val) {
          if (cur->ch[1] != nullptr) return _query_nex(cur->ch[1], val);
        } else {
          q_nex_tmp = cur->val;
          if (cur->ch[0] != nullptr) _query_nex(cur->ch[0], val);
          return q_nex_tmp;
        }
        return NIL;
      }
    
     public:
      void insert(int val) { _insert(root, val); }
    
      void del(int val) { _del(root, val); }
    
      int query_rank(int val) { return _query_rank(root, val); }
    
      int query_val(int rank) { return _query_val(root, rank); }
    
      int query_prev(int val) { return _query_prev(root, val); }
    
      int query_nex(int val) { return _query_nex(root, val); }
    };
    
    Treap tr;
    
    int main() {
      srand(0);
      int t;
      scanf("%d", &t);
      while (t--) {
        int mode;
        int num;
        scanf("%d%d", &mode, &num);
        switch (mode) {
          case 1:
            tr.insert(num);
            break;
          case 2:
            tr.del(num);
            break;
          case 3:
            printf("%d\n", tr.query_rank(num));
            break;
          case 4:
            printf("%d\n", tr.query_val(num));
            break;
          case 5:
            printf("%d\n", tr.query_prev(num));
            break;
          case 6:
            printf("%d\n", tr.query_nex(num));
            break;
        }
      }
    }
    ```

#### Implementacija poljem

Slijedi predložak za obično balansirano stablo s bzoj-a, implementiran poljem.

??? note "Potpuni kod"
    ```cpp
    --8<-- "docs/ds/code/treap/treap_1.cpp"
    ```

### Treap bez rotacija

#### Implementacija pokazivačima

??? note "Potpuni kod"
    Slijedi potpuna verzija prije objašnjenog koda; to je predložak za obično balansirano stablo.
    
    ```cpp
    
    // author: (ttzytt)[ttzytt.com]
    #include <cstdio>
    #include <cstdlib>
    #include <ctime>
    #include <tuple>
    using namespace std;
    
    struct Node {
      Node *ch[2];
      int val, prio;
      int cnt;
      int siz;
    
      Node(int _val) : val(_val), cnt(1), siz(1) {
        ch[0] = ch[1] = nullptr;
        prio = rand();
      }
    
      Node(Node *_node) {
        val = _node->val, prio = _node->prio, cnt = _node->cnt, siz = _node->siz;
      }
    
      void upd_siz() {
        siz = cnt;
        if (ch[0] != nullptr) siz += ch[0]->siz;
        if (ch[1] != nullptr) siz += ch[1]->siz;
      }
    };
    
    struct none_rot_treap {
    #define _3 second.second
    #define _2 second.first
      Node *root;
    
      pair<Node *, Node *> split(Node *cur, int key) {
        if (cur == nullptr) return {nullptr, nullptr};
        if (cur->val <= key) {
          auto temp = split(cur->ch[1], key);
          cur->ch[1] = temp.first;
          cur->upd_siz();
          return {cur, temp.second};
        } else {
          auto temp = split(cur->ch[0], key);
          cur->ch[0] = temp.second;
          cur->upd_siz();
          return {temp.first, cur};
        }
      }
    
      tuple<Node *, Node *, Node *> split_by_rk(Node *cur, int rk) {
        if (cur == nullptr) return {nullptr, nullptr, nullptr};
        int ls_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
        if (rk <= ls_siz) {
          Node *l, *mid, *r;
          tie(l, mid, r) = split_by_rk(cur->ch[0], rk);
          cur->ch[0] = r;
          cur->upd_siz();
          return {l, mid, cur};
        } else if (rk <= ls_siz + cur->cnt) {
          Node *lt = cur->ch[0];
          Node *rt = cur->ch[1];
          cur->ch[0] = cur->ch[1] = nullptr;
          return {lt, cur, rt};
        } else {
          Node *l, *mid, *r;
          tie(l, mid, r) = split_by_rk(cur->ch[1], rk - ls_siz - cur->cnt);
          cur->ch[1] = l;
          cur->upd_siz();
          return {cur, mid, r};
        }
      }
    
      Node *merge(Node *u, Node *v) {
        if (u == nullptr && v == nullptr) return nullptr;
        if (u != nullptr && v == nullptr) return u;
        if (v != nullptr && u == nullptr) return v;
        if (u->prio < v->prio) {
          u->ch[1] = merge(u->ch[1], v);
          u->upd_siz();
          return u;
        } else {
          v->ch[0] = merge(u, v->ch[0]);
          v->upd_siz();
          return v;
        }
      }
    
      void insert(int val) {
        auto temp = split(root, val);
        auto l_tr = split(temp.first, val - 1);
        Node *new_node;
        if (l_tr.second == nullptr) {
          new_node = new Node(val);
        } else {
          l_tr.second->cnt++;
          l_tr.second->upd_siz();
        }
        Node *l_tr_combined =
            merge(l_tr.first, l_tr.second == nullptr ? new_node : l_tr.second);
        root = merge(l_tr_combined, temp.second);
      }
    
      void del(int val) {
        auto temp = split(root, val);
        auto l_tr = split(temp.first, val - 1);
        if (l_tr.second->cnt > 1) {
          l_tr.second->cnt--;
          l_tr.second->upd_siz();
          l_tr.first = merge(l_tr.first, l_tr.second);
        } else {
          if (temp.first == l_tr.second) {
            temp.first = nullptr;
          }
          delete l_tr.second;
          l_tr.second = nullptr;
        }
        root = merge(l_tr.first, temp.second);
      }
    
      int qrank_by_val(Node *cur, int val) {
        auto temp = split(cur, val - 1);
        int ret = (temp.first == nullptr ? 0 : temp.first->siz) + 1;
        root = merge(temp.first, temp.second);
        return ret;
      }
    
      int qval_by_rank(Node *cur, int rk) {
        Node *l, *mid, *r;
        tie(l, mid, r) = split_by_rk(cur, rk);
        int ret = mid->val;
        root = merge(merge(l, mid), r);
        return ret;
      }
    
      int qprev(int val) {
        auto temp = split(root, val - 1);
        int ret = qval_by_rank(temp.first, temp.first->siz);
        root = merge(temp.first, temp.second);
        return ret;
      }
    
      int qnex(int val) {
        auto temp = split(root, val);
        int ret = qval_by_rank(temp.second, 1);
        root = merge(temp.first, temp.second);
        return ret;
      }
    };
    
    none_rot_treap tr;
    
    int main() {
      srand(time(nullptr));
      int t;
      scanf("%d", &t);
      while (t--) {
        int mode;
        int num;
        scanf("%d%d", &mode, &num);
        switch (mode) {
          case 1:
            tr.insert(num);
            break;
          case 2:
            tr.del(num);
            break;
          case 3:
            printf("%d\n", tr.qrank_by_val(tr.root, num));
            break;
          case 4:
            printf("%d\n", tr.qval_by_rank(tr.root, num));
            break;
          case 5:
            printf("%d\n", tr.qprev(num));
            break;
          case 6:
            printf("%d\n", tr.qnex(num));
            break;
        }
      }
    }
    ```

### Intervalne operacije Treapa bez rotacija

#### Implementacija pokazivačima

??? note "Potpuni kod"
    Slijedi potpuna verzija prije objašnjenog koda; to je predložak za zadatak s umjetničkim balansiranim stablom.
    
    ```cpp
    
    // author: (ttzytt)[ttzytt.com]
    #include <cstdlib>
    #include <ctime>
    #include <iostream>
    using namespace std;
    
    // Izvor: https://www.cnblogs.com/Equinox-Flower/p/10785292.html
    struct Node {
      Node* ch[2];
      int val, prio;
      int cnt;
      int siz;
      bool to_rev = false;  // svaki čvor u ovom podstablu treba okrenuti
    
      Node(int _val) : val(_val), cnt(1), siz(1) {
        ch[0] = ch[1] = nullptr;
        prio = rand();
      }
    
      int upd_siz() {
        siz = cnt;
        if (ch[0] != nullptr) siz += ch[0]->siz;
        if (ch[1] != nullptr) siz += ch[1]->siz;
        return siz;
      }
    
      void pushdown() {
        swap(ch[0], ch[1]);
        if (ch[0] != nullptr) ch[0]->to_rev ^= 1;
        // ako i dijete treba okrenuti, dva se okretanja poništavaju; ako se dijete ne okreće, ovaj
        //  tag treba dalje spustiti na dijete
        if (ch[1] != nullptr) ch[1]->to_rev ^= 1;
        to_rev = false;
      }
    
      void check_tag() {
        if (to_rev) pushdown();
      }
    };
    
    struct Seg_treap {
      Node* root;
    #define siz(_) (_ == nullptr ? 0 : _->siz)
    
      pair<Node*, Node*> split(Node* cur, int sz) {
        // dijeli se prema veličini stabla
        if (cur == nullptr) return {nullptr, nullptr};
        cur->check_tag();
        if (sz <= siz(cur->ch[0])) {
          // dovoljno je lijevo podstablo
          auto temp = split(cur->ch[0], sz);
          // lijevo podstablo ne treba nužno cijelo; temp.second nije potreban
          cur->ch[0] = temp.second;
          cur->upd_siz();
          return {temp.first, cur};
        } else {
          // lijevo plus dio desnog (naravno, uključujući i sam ovaj čvor)
          auto temp = split(cur->ch[1], sz - siz(cur->ch[0]) - 1);
          cur->ch[1] = temp.first;
          cur->upd_siz();
          return {cur, temp.second};
        }
      }
    
      Node* merge(Node* sm, Node* bg) {
        // small, big
        if (sm == nullptr && bg == nullptr) return nullptr;
        if (sm != nullptr && bg == nullptr) return sm;
        if (sm == nullptr && bg != nullptr) return bg;
        sm->check_tag(), bg->check_tag();
        if (sm->prio < bg->prio) {
          sm->ch[1] = merge(sm->ch[1], bg);
          sm->upd_siz();
          return sm;
        } else {
          bg->ch[0] = merge(sm, bg->ch[0]);
          bg->upd_siz();
          return bg;
        }
      }
    
      void insert(int val) {
        auto temp = split(root, val);
        auto l_tr = split(temp.first, val - 1);
        Node* new_node;
        if (l_tr.second == nullptr) new_node = new Node(val);
        Node* l_tr_combined =
            merge(l_tr.first, l_tr.second == nullptr ? new_node : l_tr.second);
        root = merge(l_tr_combined, temp.second);
      }
    
      void seg_rev(int l, int r) {
        // less i more ovdje su relativni prema l
        auto less = split(root, l - 1);
        // svi manji ili jednaki l - 1 bit će na lijevoj strani od less
        auto more = split(less.second, r - l + 1);
        // izdvoji prvih r - l + 1 elemenata počevši od l
        more.first->to_rev = true;
        root = merge(less.first, merge(more.first, more.second));
      }
    
      void print(Node* cur) {
        if (cur == nullptr) return;
        cur->check_tag();
        print(cur->ch[0]);
        cout << cur->val << " ";
        print(cur->ch[1]);
      }
    };
    
    Seg_treap tr;
    
    int main() {
      srand(time(nullptr));
      int n, m;
      cin >> n >> m;
      for (int i = 1; i <= n; i++) tr.insert(i);
      while (m--) {
        int l, r;
        cin >> l >> r;
        tr.seg_rev(l, r);
      }
      tr.print(tr.root);
    }
    ```

## Zadaci za vježbu

[Obično balansirano stablo](https://loj.ac/problem/104)

[Umjetničko balansirano stablo (Splay)](https://loj.ac/problem/105)

[„ZJOI2006” Polica za knjige](https://www.luogu.com.cn/problem/P2596)

[„NOI2005” Održavanje niza](https://www.luogu.com.cn/problem/P2042)

[CF 702F T-Shirts](http://codeforces.com/problemset/problem/702/F)

## Literatura i napomene

[^ref1]: Dizajn slike oslanja se na [ilustraciju u članku o Treapu na Wikipediji](https://en.wikipedia.org/wiki/Treap)

[^ref2]: <https://charleswu.site/archives/1051>

[^ref3]: <https://www.cnblogs.com/Equinox-Flower/p/10785292.html>

[^ref4]: <https://www.luogu.com.cn/blog/85514/fhq-treap-xue-xi-bi-ji>
