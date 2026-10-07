---
title: Particijsko stablo
---

## Uvod

Particijsko stablo (dividing tree) struktura je podataka za rješavanje problema $K$-tog najvećeg elementa intervala; ima znatno manju konstantu i lakše se razumije od perzistentnog segment treea (tzv. „chairman tree”). Istodobno je particijsko stablo usko vezano uz „$K$-ti najveći”, pa je to struktura podataka temeljena na sortiranju.

Preduvjeti: [perzistentni segment tree](persistent-seg.md#主席树)

## Postupak

### Izgradnja stabla

Izgradnja particijskog stabla relativno je jednostavna, ali u usporedbi s drugim stablima složenija.

![](./images/dividing-1.svg)

Kao na slici, svaka razina ima naizgled neuređen niz. Zapravo je svaki crveno označeni broj onaj **koji ide u lijevo dijete**. A koje je pravilo raspodjele? Uspoređuje se s **medijanom te razine**: ako je manji ili jednak medijanu, ide lijevo, inače desno. Ali pazite: nije strogo **„manji ili jednak ide lijevo, inače desno”**, jer medijan može imati jednake kopije, a stvar ovisi i o parnosti od $N$. Kod u nastavku to vješto rješava, pogledajte ga.

Ne možemo svaku razinu svaki put sortirati; ne samo zbog konstante, nego ni teorijska složenost ne bi prošla. Razmislimo: za nalaženje medijana dovoljno je jedno sortiranje. Zašto? Primjerice, medijan od $l,r$ upravo je `num[mid]` nakon sortiranja.

Dva ključna niza:

tree\[log(N),N]: samo stablo; treba pohraniti sve vrijednosti, prostorna složenost $O(n\log n)$.
toleft\[log(N),n]: broj elemenata među 1\~i na svakoj razini koji idu u lijevo dijete; ovo treba razumjeti – to je prefiksna suma.

???+ note "Implementacija"
    ```pascal
    procedure Build(left,right,deep:longint); // left,right su krajevi intervala, deep je razina
    var
      i,mid,same,ls,rs,flag:longint; // flag služi za uravnoteženje broja elemenata lijevo i desno
    begin
      if left=right then exit; // došli smo do dna
      mid:=(left+right) >> 1;
      same:=mid-left+1;
      for i:=left to right do 
        if tree[deep,i]<num[mid] then
          dec(same);
      
      ls:=left; // pokazivač na prvo mjesto u lijevom djetetu
      rs:=mid+1; // pokazivač na prvo mjesto u desnom djetetu
      for i:=left to right do
      begin
        flag:=0;
        if (tree[deep,i]<num[mid])or((tree[deep,i]=num[mid])and(same>0)) then // uvjet za odlazak lijevo
        begin
          flag:=1; tree[deep+1,ls]:=tree[deep,i]; inc(ls);
          if tree[deep,i]=num[mid] then // uravnoteži broj lijevo i desno
            dec(same);
        end
        else
        begin
          tree[deep+1,rs]:=tree[deep,i]; inc(rs);
        end;
        toleft[deep,i]:=toleft[deep,i-1]+flag;
      end;
      Build(left,mid,deep+1); // nastavi
      Build(mid+1,right,deep+1);
    end;
    ```

### Upit

Prvo se kratko vratimo na perzistentni segment tree. Kad njime tražimo $K$-ti najmanji element intervala, orijentiramo se prema $K$: ako idemo lijevo, idemo lijevo; ako idemo desno, oduzmemo broj elemenata koji idu lijevo. U particijskom stablu je isto.

Ono što je teško razumjeti kod upita jest **sužavanje intervala**. Na slici dolje upit je od $3$ do $7$, pa na sljedećoj razini treba pitati samo od $2$ do $3$. Dakako, definiramo $[\text{left},\text{right}]$ kao suženi interval (ciljni interval), a $[l,r]$ ostaje interval čvora u kojem se nalazimo. Zašto označavati ciljni interval? Zato što je on **osnova za odluku je li odgovor lijevo ili desno**.

![](./images/dividing-2.svg)

???+ note "Implementacija"
    ```pascal
    function Query(left,right,k,l,r,deep:longint):longint;
    var
      mid,x,y,cnt,rx,ry:longint;
    begin
      if left=right then // može i l=r, jer ciljni interval sigurno sadrži odgovor
        exit(tree[deep,left]);
      mid:=(l+r) >> 1;
      x:=toleft[deep,left-1]-toleft[deep,l-1]; // broj elemenata od l do left koji idu u lijevo dijete
      y:=toleft[deep,right]-toleft[deep,l-1]; // broj elemenata od l do right koji idu u lijevo dijete
      ry:=right-l-y; rx:=left-l-x; // ry je broj elemenata od l do right koji idu desno, rx od l do left koji idu desno
      cnt:=y-x; // broj elemenata od left do right koji idu u lijevo dijete
      if cnt>=k then // standardno kao kod perzistentnog segment treea
        Query:=Query(l+x,l+y-1,k,l,mid,deep+1) // l+x sužava lijevu granicu, l+y-1 desnu. Na slici gore to znači da odbacujemo čvorove 1 i 2.
      else
        Query:=Query(mid+rx+1,mid+ry+1,k-cnt,mid+1,r,deep+1); // isto sužavanje intervala, samo na desnoj strani. Pazi da od k oduzmeš cnt.
    end;
    ```

## Svojstva

Vremenska složenost: jedan upit treba samo $O(\log n)$, pa je $m$ upita $O(m\log n)$.

Prostorna složenost: treba pohraniti samo $O(n\log n)$ brojeva.

Rezultati vlastitog mjerenja: perzistentni segment tree: $1482 \text{ms}$, particijsko stablo: $889 \text{ms}$. (Nerekurzivno, s manjom konstantom.)

## Primjena particijskog stabla

Primjer zadatka: [Luogu P3157\[CQOI2011\] 动态逆序对](https://www.luogu.com.cn/problem/P3157)

> Sažetak zadatka: zadana je permutacija od $n$ elemenata ($n\leq 10^5$) i $m$ upita ($m\leq 5\times 10^4$); svaki upit briše jedan broj iz permutacije, a treba izračunati broj inverzija permutacije nakon brisanja.

Zadatak se može riješiti CDQ divide and conquerom u vremenu $\Theta(n\log^2n)$ i prostoru $\Theta(n)$, a CDQ ima i vrlo dobru konstantu.

Kad bi zadatak bio prisilno online, obično bi se rješavao ugniježđenim stablom „Fenwick tree + perzistentni segment tree”, s vremenskom složenošću $\Theta(n\log^2n)$ i prostornom $\Theta(n\log^2n)$; konstanta je malo veća, ali i to prolazi.

Particijskim stablom zadatak se može riješiti online u vremenu $\Theta(n\log^2n)$ i prostoru $\Theta(n\log n)$, a konstanta je znatno manja nego kod ugniježđenih stabala (približno jednaka CDQ-u).

???+ warning "Napomena"
    Radi lakše implementacije u ovom se tekstu veliki niz dijeli na dva mala niza prema sredini položaja, tj. particijsko stablo u nastavku odgovara postupku merge sorta, a ne quick sorta. Najviša je razina sortirani niz, a najniža izvorni niz.

Čvor particijskog stabla zovemo desnim čvorom ako i samo ako na sljedećoj razini odlazi u desno dijete, tj. ako je to jedan od brojeva koji se u izvornom nizu nalaze dalje; analogno definiramo lijevi čvor. Ako se pri izgradnji najviša razina sortira, slično računanju inverzija merge sortom, vidi se da je broj inverzija niza jednak zbroju broja desnih čvorova ispred svakog lijevog čvora.

Promotrimo zatim brisanje. Brisanje lijevog čvora smanjuje broj inverzija cijelog niza za broj desnih čvorova ispred njega, a brisanje desnog čvora za broj lijevih čvorova iza njega. Stoga možemo dinamički održavati „broj desnih čvorova ispred svakog lijevog čvora” i „broj lijevih čvorova iza svakog desnog čvora”. To se jednostavno održava Fenwick treeom.

Treba paziti da se pri održavanju Fenwick treeom smije računati samo doprinos unutar istog bloka particijskog stabla, bez izlaska iz bloka. Za Fenwick tree postoji prilično elegantan način.

Uočimo da je raspon indeksa svakog bloka particijskog stabla nužno oblika $[c\times 2^k+1,(c+1)\times 2^k]$; popis je sljedeći (budući da se u kodu ne obrađuje najniža razina particijskog stabla, navodimo samo do predzadnje razine):

    [0001 0010] [0011 0100] [0101 0110] [0111 1000] [1001 1010] [1011 1100] [1101 1110] [1111 10000]  lev=1
    [0001 0010 0011 0100]   [0101 0110 0111 1000]   [1001 1010 1011 1100]   [1101 1110 1111 10000]    lev=2
    [0001 0010 0011 0100 0101 0110 0111 1000]       [1001 1010 1011 1100 1101 1110 1111 10000]        lev=3
    [0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 10000]                lev=4

Prisjetimo se načela Fenwick treea: pri skoku prema gore svaki put radimo `x += lowbit(x)`. Ako pri skakanju prema gore možemo jamčiti da ne izlazimo iz bloka, jamčimo i da utječemo samo na vrijednosti elemenata unutar bloka. Upit prema gore je sličan.

Da pri skakanju prema gore ne izađemo iz bloka, dovoljno je jamčiti da pri skoku vrijedi $lowbit(x)<2^{lev}$.

Skok prema dolje obrađuje se potpuno drugačije. Ako indekse svakog bloka zapišemo 0-indeksirano, oni su oblika $[c\times 2^k,(c+1)\times 2^k)$. Tada je dovoljno vrijednost indeksa pomaknuti udesno za k bitova da bismo saznali u kojem je bloku. Pri skakanju prema dolje stalno provjeravamo jesmo li izašli iz bloka.

Treba napomenuti da Fenwick tree implementiran na ovaj način pristupa najvećem indeksu jednakom potenciji dvojke najbližoj n, pa niz ne smije biti veličine samo n.

Budući da treba mijenjati na $\log n$ razina, a izmjena na $k$-toj razini ima vremensku složenost $\Theta(k)$, ukupna je vremenska složenost $\Theta(n\log n+m\log^2n)$.

Kod:

```cpp
--8<-- "docs/ds/code/dividing/dividing_1.cpp"
```

## Pogovor

Referentni blog: [poveznica](https://blog.csdn.net/littlewhite520/article/details/70250722).
