---
title: Sqrt Tree
---

## Uvod

Zadan je niz duljine n, ${\left\langle a_i\right\rangle}_{i=1}^n$, i asocijativna operacija $\circ$ (primjerice, $\gcd,\min,\max,+,\operatorname{and},\operatorname{or},\operatorname{xor}$ sve su asocijativne); za svaki intervalni upit $[l,r]$ treba izračunati $a_l\circ a_{l+1}\circ\dotsb\circ a_{r}$.

Sqrt Tree može se predobraditi u vremenu $O(n\log\log n)$ i odgovarati na upite u vremenu $O(1)$.

## Objašnjenje

### Podjela niza na blokove

Najprije cijeli niz podijelimo na $O(\sqrt{n})$ blokova, svaki veličine $O(\sqrt{n})$. Za svaki blok izračunamo:

1.  $P_i$ – prefiksne intervalne upite unutar bloka
2.  $S_i$ – sufiksne intervalne upite unutar bloka
3.  održavamo dodatni niz $\left\langle B_{i,j}\right\rangle$ koji označava odgovor za interval od $i$-tog do $j$-tog bloka.

Primjerice, neka $\circ$ označava zbrajanje $+$, a niz neka je $\{1,2,3,4,5,6,7,8,9\}$.

Najprije niz podijelimo na tri bloka, pa dobijemo $\{1,2,3\},\{4,5,6\},\{7,8,9\}$.

Tada su prefiksni i sufiksni intervalni odgovori svakog bloka redom

$$
\begin{aligned}
&P_1=\{1,3,6\},S_1=\{6,5,3\}\\
&P_2=\{4,9,15\},S_2=\{15,11,6\}\\
&P_3=\{7,15,24\},S_3=\{24,17,9\}\\
\end{aligned}
$$

Niz $B$ je:

$$
B=\begin{bmatrix}
6 & 21 & 45\\
0 & 15 & 39\\
0 & 0 & 24\\
\end{bmatrix}
$$

(Za nevaljane slučajeve $i>j$ pretpostavljamo da je odgovor 0.)

Očito te vrijednosti možemo predobraditi u vremenu $O(n)$, a prostorna je složenost također $O(n)$. Nakon toga pomoću njih možemo u vremenu $O(1)$ odgovarati na upite koji prelaze granice blokova. No upite čiji je cijeli interval unutar jednog bloka još ne možemo obraditi, pa moramo pripremiti još nešto.

### Izgradnja stabla

Lako se dosjetiti da unutar svakog bloka rekurzivno izgradimo gornju strukturu kako bismo podržali upite unutar bloka. Za blokove veličine $1$ na upit možemo odgovoriti u $O(1)$. Tako smo izgradili stablo u kojem svaki čvor predstavlja jedan interval niza. Intervali listova imaju duljinu $1$ ili $2$. Čvor veličine $k$ ima $O(\sqrt{k})$ djece, pa je visina cijelog stabla $O(\log\log n)$, a ukupna duljina intervala na svakoj razini je $O(n)$; stoga je složenost izgradnje stabla $O(n\log\log n)$.

??? note "Dokaz visine stabla"
    Prema definiciji, neka je $T(n)$ visina podstabla čvora koji „kontrolira” $n$ elemenata; možemo zapisati rekurziju:
    
    $$
    T(n)=T(\sqrt n)+1
    $$
    
    Supstitucijom $n=2^m$ dobivamo
    
    $$
    T(2^m)=T(2^{\frac m2})+1
    $$
    
    Definiramo li još $S(m)=T(2^m)$ i uvrstimo, imamo
    
    $$
    S(m)=S(\dfrac m2)+1
    $$
    
    Prema glavnom teoremu, $S(m)=O(\log m)$, pa je $T(n)=S(\log n)=O(\log\log n)$.

Sada na upite možemo odgovarati u vremenu $O(\log\log n)$. Za upit $[l,r]$ trebamo samo brzo pronaći čvor $u$ s najmanjim intervalom koji sadrži $[l,r]$; tada $[l,r]$ u blokovnoj podjeli čvora $u$ sigurno prelazi granicu bloka, pa odgovor možemo izračunati u $O(1)$. Ukupna složenost jednog upita je $O(\log\log n)$, jer je visina stabla $O(\log\log n)$. Taj postupak ipak još možemo optimizirati.

### Optimizacija složenosti upita

Lako se dosjetiti binarnog pretraživanja po visini, uz provjeru valjanosti u $O(1)$. Time složenost postaje $O(\log\log\log n)$. No postupak možemo dodatno ubrzati.

Pretpostavimo:

1.  veličina svakog bloka je cjelobrojna potencija broja $2$;
2.  veličine blokova na istoj razini su jednake.

Zato na kraj niza moramo dodati nekoliko elemenata $0$ kako bi mu duljina postala cjelobrojna potencija broja $2$. Iako neki blokovi mogu postati dvostruko veći nego prije, to je i dalje $O(\sqrt{k})$, pa složenost predobrade blokova ostaje $O(n)$.

Sada lako možemo utvrditi je li upitni interval u cijelosti sadržan u jednom bloku. Za interval $[l,r]$ (indeksiran od 0) zapišemo krajeve u binarnom obliku. Primjerice, za $k=4, l=39, r=46$ binarni je zapis

$$
l = 39_{10} = 100111_2,
r = 46_{10} = 101110_2
$$

Znamo da su duljine intervala na jednoj razini jednake, a jednake su i veličine blokova (u gornjem primjeru $2^k=2^4=16$). Ti blokovi potpuno pokrivaju cijeli niz, pa prvi blok predstavlja elemente $[0,15]$ (binarno $[000000_2,001111_2]$), drugi blok predstavlja interval elemenata $[16,31]$ (binarno $[010000_2,011111_2]$) i tako dalje. Primjećujemo da se položaji elemenata unutar istog bloka u binarnom zapisu razlikuju samo u zadnjih $k$ bitova (u gornjem primjeru $k=4$). I $l,r$ iz primjera razlikuju se samo u zadnjih $k$ bitova, pa su u istom bloku.

Dakle, trebamo provjeriti razlikuju li se krajevi intervala samo u zadnjih $k$ bitova, tj. je li $l\oplus r\le 2^k-1$. Tako možemo brzo pronaći razinu na kojoj je interval odgovora:

1.  za svaki $i\in [1,n]$ nađemo najviši bit $1$ u $i$;
2.  sada za upit $[l,r]$ izračunamo najviši bit od $l\oplus r$ i time brzo odredimo razinu na kojoj je interval odgovora.

Tako na upite možemo odgovarati u vremenu $O(1)$.

## Postupak ažuriranja elemenata

Elemente u Sqrt Treeu možemo ažurirati; podržane su i izmjene u točki i izmjene na intervalu.

### Izmjena u točki

Razmotrimo pridruživanje u točki $a_x=val$; želimo učinkovito ažurirati informacije nakon te operacije.

#### Naivna implementacija

Pogledajmo najprije kako Sqrt Tree izgleda nakon jedne izmjene u točki.

Promotrimo čvor duljine $l$ i pripadne nizove: $\left\langle P_i\right\rangle,\left\langle S_i\right\rangle,\left\langle B_{i,j}\right\rangle$. Lako je vidjeti da se u $\left\langle P_i\right\rangle$ i $\left\langle S_i \right\rangle$ mijenja samo $O(\sqrt{l})$ elemenata. U $\left\langle B_{i,j}\right\rangle$ se pak mijenja $O(l)$ elemenata. Dakle, u čvoru stabla ažurira se $O(l)$ elemenata. Stoga je složenost izmjene u točki u Sqrt Treeu $O(n+\sqrt{n}+\sqrt{\sqrt{n}}+\dotsb)=O(n)$.

#### Zamjena niza B Sqrt Treeom

Primjećujemo da je usko grlo izmjene u točki ažuriranje $\left\langle B_{i,j}\right\rangle$ korijena. Zato pokušajmo $\left\langle B_{i,j}\right\rangle$ korijena zamijeniti drugim Sqrt Treeom, koji nazivamo $index$. Njegova je uloga ista kao i izvornog dvodimenzionalnog niza: održava odgovore na upite za cijele blokove. Ostali čvorovi, osim korijena, i dalje koriste $\left\langle B_{i,j}\right\rangle$. Napomena: ako korijen Sqrt Treea ima strukturu $index$, kažemo da Sqrt Tree **ima indeks**; ako korijen Sqrt Treea ima strukturu $\left\langle B_{i,j}\right\rangle$, kažemo da je **bez indeksa**. Samo stablo $index$ nema indeks.

Stablo $index$ stoga ažuriramo ovako:

1.  U vremenu $O(\sqrt{n})$ ažuriramo $\left\langle P_i\right\rangle$ i $\left\langle S_i\right\rangle$.
2.  Ažuriramo $index$; njegova je duljina $O(n)$, ali trebamo ažurirati samo jedan njegov element (onaj koji predstavlja promijenjeni blok); složenost ovog koraka je $O(\sqrt{n})$ (naivnim algoritmom).
3.  Spustimo se u dijete u kojem je nastala promjena i naivnim algoritmom ažuriramo informacije u vremenu $O(\sqrt{n})$.

Napomena: složenost upita ostaje $O(1)$, jer stablo $index$ koristimo najviše jednom. Složenost izmjene u točki tako je $O(\sqrt{n})$.

### Ažuriranje intervala

Sqrt Tree podržava i operaciju pridruživanja na intervalu $\operatorname{Update}(l,r,x)$, koja sve brojeve na intervalu $[l,r]$ postavlja na $x$. Za to imamo dvije implementacije: jedna ažurira informacije u $O(\sqrt{n}\log\log n)$ i odgovara na upite u $O(1)$; druga ažurira u $O(\sqrt{n})$, ali vrijeme upita raste na $O(\log\log n)$.

Na Sqrt Treeu možemo, kao i na segment treeu, koristiti lijene oznake (lazy tags). No kod Sqrt Treea postoji jedna razlika. Budući da spuštanje lijene oznake jednog čvora može stajati $O(\sqrt{n})$, oznake ne spuštamo pri upitu, nego provjeravamo ima li roditelj oznaku i, ako ima, spuštamo je.

#### Prva implementacija

U prvoj implementaciji lijene oznake stavljamo samo na čvorove razine $1$ (čvorove s intervalom duljine $O(\sqrt{n})$), a pri spuštanju oznake izravno ažuriramo cijelo podstablo, složenosti $O(\sqrt{n}\log\log n)$. Postupak je sljedeći:

1.  Promotrimo čvorove razine $1$; onima koji su u cijelosti sadržani u intervalu izmjene stavimo lijenu oznaku;

2.  Dva su bloka samo djelomično pokrivena; njih izravno **ponovno izgradimo** u vremenu $O(\sqrt{n}\log\log n)$. Ako blok sam nosi lijenu oznaku iz prethodne izmjene, pri ponovnoj izgradnji usput spustimo oznaku;

3.  Ažuriramo $\left\langle P_i\right\rangle$ i $\left\langle S_i\right\rangle$ korijena, složenost $O(\sqrt{n})$;

4.  Ponovno izgradimo stablo $index$, složenost $O(\sqrt{n}\log\log n)$.

Sada možemo učinkovito izvoditi izmjene na intervalu. A kako uz lijene oznake odgovaramo na upite? Postupak je sljedeći:

1.  Ako je upit sadržan u bloku s lijenom oznakom, odgovor možemo izračunati pomoću lijene oznake;

2.  Ako upit obuhvaća više blokova, zanimaju nas samo odgovori krajnjeg lijevog i krajnjeg desnog nepotpunog bloka. Odgovor za blokove u sredini možemo dohvatiti iz stabla $index$ (jer se stablo $index$ nakon svake izmjene ponovno izgrađuje), složenosti $O(1)$.

Složenost upita stoga ostaje $O(1)$.

#### Druga implementacija

U ovoj implementaciji lijenu oznaku može nositi svaki čvor. Zato pri obradi upita moramo uzeti u obzir lijene oznake predaka, pa složenost upita postaje $O(\log\log n)$. No ažuriranje informacija postaje brže. Postupak je sljedeći:

1.  Blokovima koji su u cijelosti sadržani u intervalu izmjene dodamo lijenu oznaku, složenost $O(\sqrt{n})$;
2.  Blokovima koje interval izmjene djelomično pokriva ažuriramo $\left\langle P_i\right\rangle$ i $\left\langle S_i\right\rangle$, složenost $O(\sqrt{n})$ (jer su samo dva bloka izmijenjena);
3.  Ažuriramo stablo $index$, složenost $O(\sqrt{n})$ (istim algoritmom ažuriranja);
4.  Podstablima bez indeksa ažuriramo $\left\langle B_{i,j}\right\rangle$;
5.  Rekurzivno ažuriramo dva intervala koja nisu u cijelosti pokrivena.

Vremenska je složenost $O(\sqrt{n}+\sqrt{\sqrt{n}}+\dotsb)=O(\sqrt{n})$.

## Implementacija

Sljedeća implementacija gradi stablo u vremenu $O(n\log\log n)$, odgovara na upite u $O(1)$ i izvodi izmjene u točki u $O(\sqrt{n})$.

```cpp
SqrtTreeItem op(const SqrtTreeItem &a, const SqrtTreeItem &b);

int log2Up(int n) {
  int res = 0;
  while ((1 << res) < n) {
    res++;
  }
  return res;
}

class SqrtTree {
 private:
  int n, lg, indexSz;
  vector<SqrtTreeItem> v;
  vector<int> clz, layers, onLayer;
  vector<vector<SqrtTreeItem>> pref, suf, between;

  void buildBlock(int layer, int l, int r) {
    pref[layer][l] = v[l];
    for (int i = l + 1; i < r; i++) {
      pref[layer][i] = op(pref[layer][i - 1], v[i]);
    }
    suf[layer][r - 1] = v[r - 1];
    for (int i = r - 2; i >= l; i--) {
      suf[layer][i] = op(v[i], suf[layer][i + 1]);
    }
  }

  void buildBetween(int layer, int lBound, int rBound, int betweenOffs) {
    int bSzLog = (layers[layer] + 1) >> 1;
    int bCntLog = layers[layer] >> 1;
    int bSz = 1 << bSzLog;
    int bCnt = (rBound - lBound + bSz - 1) >> bSzLog;
    for (int i = 0; i < bCnt; i++) {
      SqrtTreeItem ans;
      for (int j = i; j < bCnt; j++) {
        SqrtTreeItem add = suf[layer][lBound + (j << bSzLog)];
        ans = (i == j) ? add : op(ans, add);
        between[layer - 1][betweenOffs + lBound + (i << bCntLog) + j] = ans;
      }
    }
  }

  void buildBetweenZero() {
    int bSzLog = (lg + 1) >> 1;
    for (int i = 0; i < indexSz; i++) {
      v[n + i] = suf[0][i << bSzLog];
    }
    build(1, n, n + indexSz, (1 << lg) - n);
  }

  void updateBetweenZero(int bid) {
    int bSzLog = (lg + 1) >> 1;
    v[n + bid] = suf[0][bid << bSzLog];
    update(1, n, n + indexSz, (1 << lg) - n, n + bid);
  }

  void build(int layer, int lBound, int rBound, int betweenOffs) {
    if (layer >= (int)layers.size()) {
      return;
    }
    int bSz = 1 << ((layers[layer] + 1) >> 1);
    for (int l = lBound; l < rBound; l += bSz) {
      int r = min(l + bSz, rBound);
      buildBlock(layer, l, r);
      build(layer + 1, l, r, betweenOffs);
    }
    if (layer == 0) {
      buildBetweenZero();
    } else {
      buildBetween(layer, lBound, rBound, betweenOffs);
    }
  }

  void update(int layer, int lBound, int rBound, int betweenOffs, int x) {
    if (layer >= (int)layers.size()) {
      return;
    }
    int bSzLog = (layers[layer] + 1) >> 1;
    int bSz = 1 << bSzLog;
    int blockIdx = (x - lBound) >> bSzLog;
    int l = lBound + (blockIdx << bSzLog);
    int r = min(l + bSz, rBound);
    buildBlock(layer, l, r);
    if (layer == 0) {
      updateBetweenZero(blockIdx);
    } else {
      buildBetween(layer, lBound, rBound, betweenOffs);
    }
    update(layer + 1, l, r, betweenOffs, x);
  }

  SqrtTreeItem query(int l, int r, int betweenOffs, int base) {
    if (l == r) {
      return v[l];
    }
    if (l + 1 == r) {
      return op(v[l], v[r]);
    }
    int layer = onLayer[clz[(l - base) ^ (r - base)]];
    int bSzLog = (layers[layer] + 1) >> 1;
    int bCntLog = layers[layer] >> 1;
    int lBound = (((l - base) >> layers[layer]) << layers[layer]) + base;
    int lBlock = ((l - lBound) >> bSzLog) + 1;
    int rBlock = ((r - lBound) >> bSzLog) - 1;
    SqrtTreeItem ans = suf[layer][l];
    if (lBlock <= rBlock) {
      SqrtTreeItem add =
          (layer == 0) ? (query(n + lBlock, n + rBlock, (1 << lg) - n, n))
                       : (between[layer - 1][betweenOffs + lBound +
                                             (lBlock << bCntLog) + rBlock]);
      ans = op(ans, add);
    }
    ans = op(ans, pref[layer][r]);
    return ans;
  }

 public:
  SqrtTreeItem query(int l, int r) { return query(l, r, 0, 0); }

  void update(int x, const SqrtTreeItem &item) {
    v[x] = item;
    update(0, 0, n, 0, x);
  }

  SqrtTree(const vector<SqrtTreeItem> &a)
      : n((int)a.size()), lg(log2Up(n)), v(a), clz(1 << lg), onLayer(lg + 1) {
    clz[0] = 0;
    for (int i = 1; i < (int)clz.size(); i++) {
      clz[i] = clz[i >> 1] + 1;
    }
    int tlg = lg;
    while (tlg > 1) {
      onLayer[tlg] = (int)layers.size();
      layers.push_back(tlg);
      tlg = (tlg + 1) >> 1;
    }
    for (int i = lg - 1; i >= 0; i--) {
      onLayer[i] = max(onLayer[i], onLayer[i + 1]);
    }
    int betweenLayers = max(0, (int)layers.size() - 1);
    int bSzLog = (lg + 1) >> 1;
    int bSz = 1 << bSzLog;
    indexSz = (n + bSz - 1) >> bSzLog;
    v.resize(n + indexSz);
    pref.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
    suf.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
    between.assign(betweenLayers, vector<SqrtTreeItem>((1 << lg) + bSz));
    build(0, 0, n, 0);
  }
};
```

## Zadaci za vježbu

[CodeChef - SEGPROD](https://www.codechef.com/NOV17/problems/SEGPROD)

**Ova je stranica uglavnom prevedena prema [Sqrt Tree - Algorithms for Competitive Programming](https://cp-algorithms.com/data_structures/sqrt-tree.html), pod licencijom CC-BY-SA 4.0.**
