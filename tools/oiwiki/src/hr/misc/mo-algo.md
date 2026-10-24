---
title: Običan Mo algoritam
---

## Oblik

Pretpostavimo $n=m$. Tada, ako se za problem s upitima nad intervalima niza odgovor za $[l,r]$ može u $O(1)$ proširiti na odgovor za $[l-1,r],[l+1,r],[l,r+1],[l,r-1]$ (tj. za intervale susjedne intervalu $[l,r]$), odgovori na sve upite mogu se izračunati u složenosti $O(n\sqrt{n})$.

## Objašnjenje

Upiti se offline sortiraju, obrađuju redom, a odgovor se grubom silom prenosi s prethodnog intervala na sljedeći (dovoljno je pomicati se korak po korak).

## Način sortiranja

Intervali $[l,r]$ sortiraju se uzlazno s indeksom bloka u kojem se nalazi $l$ kao prvim ključem i $r$ kao drugim ključem.

## Implementacija

```cpp
void move(int pos, int sign) {
  // ažuriraj nowAns
}

void solve() {
  BLOCK_SIZE = int(ceil(pow(n, 0.5)));
  sort(querys, querys + m);
  for (int i = 0; i < m; ++i) {
    const query &q = querys[i];
    while (l > q.l) move(--l, 1);
    while (r < q.r) move(++r, 1);
    while (l < q.l) move(l++, -1);
    while (r > q.r) move(r--, -1);
    ans[q.id] = nowAns;
  }
}
```

## Analiza složenosti

Sljedeće razmatramo uz pretpostavku da su $n$ i $m$ istog reda veličine.

Prvi je korak podjela na blokove; vremenska složenost tog koraka je $O(\sqrt{n}\cdot\sqrt{n}\log\sqrt{n}+n\log n)=O(n\log n)$.

Zatim dolazi srž Mo algoritma; u nastavku jednostavnom, srednjoškolskom metodom dokazujemo da je njegova vremenska složenost $O(n\sqrt{n})$.

???+ note "Dokaz"
    Dokaz: neka su najveće vrijednosti $L$ u pojedinim blokovima $\max_1,\max_2,\max_3, \cdots , \max_{\lceil\sqrt{n}\rceil}$.
    
    Iz prvog sortiranja slijedi $\max_1 \le \max_2 \le \cdots \le \max_{\lceil\sqrt{n}\rceil}$.
    
    Očito je vremenska složenost izračuna prvog upita svakog bloka grubom silom $O(n)$.
    
    Razmotrimo najgori slučaj: u svakom je bloku najveća vrijednost $R$ jednaka $n$, a svaka operacija izmjene mora $L$ promijeniti iz $\max_{i - 1}$ u $\max_i$ ili iz $\max_i$ u $\max_{i - 1}$.
    
    Razmotrimo $R$: budući da je $R$ unutar bloka već sortiran, vremenska složenost svih njegovih izmjena unutar jednog bloka je $O(n)$. Za sve blokove to je $O(n\sqrt{n})$.
    
    Ključna je analiza $L$: budući da je vremenska složenost svake promjene $O(\max_i-\max_{i-1})$, vremenska složenost unutar jednog bloka je $O(\sqrt{n}\cdot(\max_i-\max_{i-1}))$.
    
    Zbrojimo li vremenske složenosti $L$ svih blokova, dobivamo:
    
    Ukupna vremenska složenost za $L$ je
    
    $$
    \begin{aligned}
    & O(\sqrt{n}(\max{}_1-1)+\sqrt{n}(\max{}_2-\max{}_1)+\sqrt{n}(\max{}_3-\max{}_2)+\cdots+\sqrt{n}(\max{}_{\lceil\sqrt{n}\rceil}-\max{}_{\lceil\sqrt{n}\rceil-1))} \\
    = \phantom{} & O(\sqrt{n}\cdot(\max{}_1-1+\max{}_2-\max{}_1+\max{}_3-\max{}_2+\cdots+\max{}_{\lceil\sqrt{n}\rceil-1}-\max{}_{\lceil\sqrt{n}\rceil-2}+\max{}_{\lceil\sqrt{n}\rceil}-\max{}_{\lceil\sqrt{n}\rceil-1)}) \\
    = \phantom{} & O(\sqrt{n}\cdot(\max{}_{\lceil\sqrt{n}\rceil}-1))\\
    \end{aligned}
    $$
    
    (teleskopski zbroj)
    
    Prema zadatku je $\max_{\lceil\sqrt{n}\rceil}$ najviše $n$, pa je ukupna vremenska složenost za $L$ u najgorem slučaju $O(n\sqrt{n})$.

Zaključno, vremenska složenost Mo algoritma je $O(n\sqrt{n})$.

Međutim, za druge vrijednosti $m$, npr. $m<n$, način podjele na blokove treba promijeniti da bi bio bolji.

Kako podijeliti na blokove?

Neka je duljina bloka $S$. Tada je za proizvoljno mnogo upita unutar istog bloka ukupna udaljenost pomicanja $n$, blokova je ukupno $\displaystyle \frac{n}{S}$, pa je ukupan broj pomaka $\displaystyle \frac{n^2}{S}$; pomaci mogu prelaziti preko blokova, pa treba dodati još složenost $mS$, a ukupna je složenost $\displaystyle O\left(\frac{n^2}{S}+mS\right)$. Želimo da ta vrijednost bude što manja, pa ta dva člana trebaju biti što bliže jednaka; vidimo da je optimalno uzeti $S$ jednako $\displaystyle \frac{n}{\sqrt{m}}$, a složenost je tada $\displaystyle O\left(\frac{n^2}{\displaystyle \frac{n}{\sqrt{m}}}+m\left(\frac{n}{\sqrt{m}}\right)\right)=O(n\sqrt{m})$.

Zapravo, ako duljina bloka nije točno postavljena, vremenska složenost Mo algoritma znatno trpi. Primjerice, ako je $m$ istog reda veličine kao $\sqrt n$, a duljina bloka pogrešno postavljena na $\sqrt n$, lako se konstruira skup podataka na kojem je vremenska složenost $O(n \sqrt n)$ umjesto ispravne $O(n^{5/4})$.

Mo algoritam izgleda vrlo „grubo”, uvelike zato što njegov način sortiranja po blokovima izgleda vrlo grubo. Došli bismo na pomisao da sve intervale sortiramo nekom naizgled profinjenijom metodom. Jedna je mogućnost da sve intervale $[l, r]$ promatramo kao točke $(l, r)$ u ravnini, nad svim točkama izgradimo Manhattan minimalno razapinjuće stablo i odgovore među upitima prenosimo duž bridova tog stabla. Čini se da to može poboljšati vremensku složenost Mo algoritma, ali gornja granica vremenske složenosti metode sortiranja upita po blokovima zapravo je već optimalna.

Pretpostavimo da su $n, m$ istog reda veličine i da je $n$ potpun kvadrat. Promotrimo intervale oblika $[a \sqrt n, b \sqrt n](1 \le a, b \le \sqrt n)$; takvih je intervala ukupno $n$. Ako sve intervale promatramo kao točke u ravnini, Manhattan udaljenost dviju točaka upravo je cijena prijelaza između dvaju intervala, a najmanja Manhattan udaljenost između bilo kojih dvaju intervala je $\sqrt n$, pa je vremenska složenost obrade svih upita najmanje $O(n \sqrt n)$. Konstrukcija podataka u ostalim slučajevima je slična.

Mo algoritam ima još jedno svojstvo: kad je $n$ nepromijenjen, što je $m$ veći, prosječna cijena prijelaza po upitu je manja. I neki drugi offline algoritmi imaju isto svojstvo (npr. Tarjanov algoritam za LCA), ali kod Mo algoritma prosječna cijena prijelaza najizraženije ovisi o $m$.

## Primjer i kod

???+ note "Primjer [「国家集训队」小 Z 的袜子 (Čarape malog Z-a)](https://www.luogu.com.cn/problem/P1494)"
    Sažetak zadatka:
    
    Zadan je niz $\{c_i\}$ duljine $n$. Zadano je $m$ upita; u svakom su zadana dva broja $l,r$ i među brojevima s indeksima od $l$ do $r$ nasumično se biraju dva različita; odredite vjerojatnost da su ta dva broja jednaka.

### Postupak

Ideja: školski primjer Mo algoritma.

Intervali $[l,r]$ sortiraju se uzlazno s indeksom bloka u kojem se nalazi $l$ kao prvim ključem i $r$ kao drugim ključem.

Zatim se odgovori računaju počevši od prvog upita niza; prvi se upit izračuna izravno grubom silom, u složenosti $O(n)$, a odgovori na kasnije upite dobivaju se na temelju prethodnog upita.

Konkretan postupak:

Za interval $[i,i]$, budući da ima samo jedan element, odgovor lako znamo. Zatim se korak po korak od trenutačnog intervala (s poznatim odgovorom) približavamo sljedećem intervalu.

Neka $col[i]$ označava koliko se puta trenutačno pojavljuje boja $i$, a $ans$ koliko trenutačno ima mogućih parova (na koliko se načina može izabrati par čarapa iste boje). Zatim pri svakom pomaku ažuriramo odgovor: neka je trenutačna boja $k$; ako se interval proširuje, $ans$ se uveća za $\dbinom{col[k]+1}{2}-\dbinom{col[k]}{2}$; ako se skraćuje, $ans$ se umanji za $\dbinom{col[k]}{2}-\dbinom{col[k]-1}{2}$. Odgovor na upit je $\displaystyle \frac{ans}{\dbinom{r-l+1}{2}}$.

Tu postoji optimizacija: $\displaystyle \dbinom{a}{2}=\frac{a (a-1)}{2}$.

Stoga je $\displaystyle \dbinom{a+1}{2}-\dbinom{a}{2}=\frac{(a+1) a}{2}-\frac{a (a-1)}{2}=\frac{a}{2}\cdot (a+1-a+1)=\frac{a}{2}\cdot 2=a$.

Dakle $\dbinom{col[k]+1}{2}-\dbinom{col[k]}{2}=col[k]$.

Ukupna složenost algoritma: $O(n\sqrt{n} )$

U kodu u nastavku `deno` označava nazivnik odgovora (denominator), `nume` brojnik (numerator), `sqn` veličinu bloka $\sqrt{n}$, `arr` je ulazni niz, `node` je struktura koja pohranjuje upit, `tab` je niz upita (nakon sortiranja), a `col` je kao gore opisano.

**Napomena: zbog `++l` i `--r` položaj četiriju while-petlji za pomicanje intervala u kodu u nastavku vrlo je važan i njihov se međusobni redoslijed ne smije proizvoljno mijenjati.**

??? note "Rasprava o redoslijedu četiriju petlji"
    Pomicanje intervala u Mo algoritmu ekvivalentno je dodavanju elemenata iz $[1,r]$ i brisanju elemenata iz $[1,l-1]$. Stoga:
    
    -   U slučaju $l\le r$ elementi iz $[1,l-1]$ jednom su dodani i jednom izbrisani, elementi iz $[l,r]$ dodani su jednom, a elementi iz $[r+1,+\infty)$ nisu dodani. Taj je interval valjan.
    -   U slučaju $l=r+1$ elementi iz $[1,r]$ jednom su dodani i jednom izbrisani, a elementi iz $[r+1,+\infty)$ nisu dodani. Taj interval tada predstavlja prazan interval.
    -   U slučaju $l>r+1$ elementi iz $[r+1,l-1]$ (taj interval nije prazan) jednom su izbrisani, ali nisu dodani, pa je broj dodavanja tih elemenata negativan.
    
    Dakle, ako u nekom trenutku nastupi $l>r+1$, postojat će element čiji je broj dodavanja negativan. U nekim zadacima to stvara probleme; primjerice, ako sve brojeve u intervalu održavamo u `set`-u, pojavit će se problem „brisanja elementa koji ne postoji u `set`-u”.
    
    Četiri while-petlje u kodu mogu se poredati na ukupno $4!=24$ načina. Bez smanjenja općenitosti neka prva petlja radi s lijevim krajem; tada postoji sljedećih $12$ poredaka (ostalih je $12$ simetrično). Tablica u nastavku navodi ispravnost tih 12 zapisa i daje kontraprimjere za pogrešne zapise.
    
    | Redoslijed petlji     | Ispravnost | Kontraprimjer ili napomena |
    | ----------------- | --- | ----------- |
    | `l--,l++,r--,r++` | pogrešno  | $l<r<l'<r'$ |
    | `l--,l++,r++,r--` | pogrešno  | $l<r<l'<r'$ |
    | `l--,r--,l++,r++` | pogrešno  | $l<r<l'<r'$ |
    | `l--,r--,r++,l++` | ispravno  | dokaz je razmjerno složen       |
    | `l--,r++,l++,r--` | ispravno  |             |
    | `l--,r++,r--,l++` | ispravno  |             |
    | `l++,l--,r--,r++` | pogrešno  | $l<r<l'<r'$ |
    | `l++,l--,r++,r--` | pogrešno  | $l<r<l'<r'$ |
    | `l++,r++,l--,r--` | pogrešno  | $l<r<l'<r'$ |
    | `l++,r++,r--,l--` | pogrešno  | $l<r<l'<r'$ |
    | `l++,r--,l--,r++` | pogrešno  | $l<r<l'<r'$ |
    | `l++,r--,r++,l--` | pogrešno  | $l<r<l'<r'$ |
    
    Od svih 24 poredaka samo je 6 ispravnih, od kojih je za 2 dokaz razmjerno složen; ovdje dajemo dokaz samo za 4 od njih.
    
    Zajedničko je obilježje tih 4 ispravna zapisa da prva dva koraka prvo proširuju interval (`l--` ili `r++`), a druga ga dva koraka zatim sužavaju (`l++` ili `r--`). Tako napisano, prva dva koraka proširuju interval i mogu održati $l\le r+1$; nakon izvršenja prvih dvaju koraka sigurno vrijedi $l\le l'\le r'\le r$, a izvršenje drugih dvaju koraka samo sužava interval na $[l',r']$, pa i dalje vrijedi $l\le r+1$; stoga je takav zapis ispravan.

### Implementacija

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/misc/code/mo-algo/mo-algo_1.cpp"
    ```

## Optimizacija običnog Mo algoritma

### Postupak

Pogledajmo sljedeći skup podataka

```text
// neka je veličina bloka 2 (pretpostavka)
1 1
2 100
3 1
4 100
```

Ručnom simulacijom vidi se da se pokazivač r pomakne otprilike 300 puta; nakon što obradimo prvi blok, $l = 2, r = 100$, i tada bi bila dovoljna dva pomaka pokazivača l da dobijemo odgovor na četvrti upit, ali mi umjesto toga pomičemo pokazivač r na 1 da dobijemo odgovor na treći upit i zatim ga pomičemo na 100 da dobijemo odgovor na četvrti upit, što je devedesetak pomaka pokazivača više. Kako to optimizirati? Tu upotrebljavamo parno-neparno sortiranje.

Što je parno-neparno sortiranje? Parno-neparno sortiranje znači da se za upite koji pripadaju neparnim blokovima r sortira uzlazno, a za upite koji pripadaju parnim blokovima r sortira silazno; tako naš pokazivač r, nakon što obradi upite neparnog bloka, na povratku obrađuje upite parnog bloka, a zatim se opet pomiče prema n obrađujući upite sljedećeg neparnog bloka, čime je optimiziran broj pomaka pokazivača r. U pravilu ta optimizacija ubrzava program za oko 30 %.

### Implementacija

Kod za sortiranje:

=== "Sažeto"
    ```cpp
    // clang-format off
    // ovdje postoji jedan mali detalj o kojem ćemo govoriti u nastavku
    int unit; // veličina bloka
    struct node {
      int l, r, id;
      bool operator < (const node &x) const {
        return l / unit == x.l / unit ? (r == x.r ? 0 : ((l / unit) & 1) ^ (r < x.r)) : l < x.l;
      }
    };
    ```

=== "Rašireno"
    ```cpp
    struct node {
      int l, r, id;
    
      bool operator<(const node &x) const {
        if (l / unit != x.l / unit) return l < x.l;
        // pazite: u sljedećim dvama redcima ne smije se pisati manje (veće) ili jednako, inače nastaje greška (vidi mali detalj u nastavku)
        if ((l / unit) & 1) return r < x.r;
        return r > x.r;
      }
    };
    ```

???+ warning "Mali detalj"
    Ako se `sort` upotrebljava za usporedbu dviju struktura, ne smije se dogoditi da su $a < b$ i $b < a$ istodobno istiniti, inače nastaje greška pri izvođenju; vidi [Uobičajene greške](../contest/common-mistakes.md#greške-koje-dovode-do-re).

Kod sažete inačice, ako nema posebne provjere `r == x.r`, kad l pripada istom neparnom bloku i r su jednaki, nastaje problem opisan u gornjem malom detalju (simulirajte sami ručno); kod raširene inačice isti problem nastaje ako se napiše manje (veće) ili jednako.

## Literatura

-   [莫队算法学习笔记 (Bilješke o učenju Mo algoritma) | Sengxian's Blog](https://blog.sengxian.com/algorithms/mo-s-algorithm)
