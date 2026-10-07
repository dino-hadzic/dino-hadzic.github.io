---
title: Spajanje i razdvajanje segment treeova
---

Spajanje i razdvajanje segment treeova često su korištene tehnike, tipične za situacije u kojima segment tree nad vrijednostima održava multiskup.

Primjerice, ako se u nekim čvorovima stabla nalazi više operacija, a informacije iz djece treba odozdo prema gore prenijeti roditelju, pri čemu se informacija u jednom čvoru zgodno održava segment treeom, spajanjem segment treeova može se kontrolirati ukupna složenost.

## Spajanje segment treeova

### Postupak

Kako ime kaže, spajanje segment treeova znači izgradnju novog segment treea čiji je svaki čvor rezultat spajanja odgovarajućih čvorova dvaju izvornih segment treeova. Često se koristi za održavanje informacija na stablu ili grafu.

Očito ne možemo svaki put stvarno izgraditi cijeli novi segment tree, pa koristimo segment tree s dinamičkim stvaranjem čvorova opisan ranije.

Postupak spajanja u biti je prilično grub (brute force):

Neka su dva segment treea A i B; spajamo rekurzivno počevši od čvora 1.

Kad rekurzija dođe do nekog čvora, ako je odgovarajući čvor u stablu A ili B prazan, izravno vraćamo odgovarajući čvor drugog stabla – tu se koristi svojstvo dinamičkog stvaranja čvorova.

Ako rekurzija dođe do lista, spajamo odgovarajuće čvorove dvaju stabala.

Na kraju ažuriramo trenutni čvor iz djece i vraćamo ga.

???+ note "Složenost spajanja segment treeova"
    Očito je za dva puna segment treea složenost jednog spajanja $O(n)$. Međutim, u praksi se obično koriste segment treeovi nad vrijednostima, pa ukupan broj čvorova svih segment treeova koje treba spojiti nije mnogo veći od $n$. Osim toga, pri spajanju se isti segment tree obično ne spaja više puta, pa je ukupan broj dodanih čvorova reda veličine $n\log n$. Tako je ukupna složenost spajanja svih segment treeova $O(n\log n)$. Naravno, u nekim je situacijama spojiva hrpa (mergeable heap) možda bolji izbor.

### Implementacija

```cpp
int merge(int a, int b, int l, int r) {
  if (!a) return b;
  if (!b) return a;
  if (l == r) {
    // do something...
    return a;
  }
  int mid = (l + r) >> 1;
  tr[a].l = merge(tr[a].l, tr[b].l, l, mid);
  tr[a].r = merge(tr[a].r, tr[b].r, mid + 1, r);
  pushup(a);
  return a;
}
```

### Primjer zadatka

???+ note "[Luogu P4556 \[Vani 有约会\] 雨天的尾巴/【模板】线段树合并](https://www.luogu.com.cn/problem/P4556)"
    ??? note "Ideja rješenja"
        Predložak za spajanje segment treeova: diferencijama se izmjene na stablu pretvore u izmjene jednog elementa, a zatim se DFS-om prema gore spajaju segment treeovi i računa odgovor.
    
    ??? note "Referentni kod"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-merge.cpp"
        ```

## Razdvajanje segment treeova

### Postupak

Razdvajanje segment treea u biti je obrnut postupak od spajanja. Razdvajanje ima smisla samo za uređene nizove, za neuređene nema smisla; obično se koristi na segment treeu nad vrijednostima s dinamičkim stvaranjem čvorova.

Pazite: kad postoje i razdvajanje i spajanje, pri spajanju moramo oslobađati (reciklirati) čvorove, kako pri razdvajanju ne bi došlo do višestrukog korištenja istog čvora.

Iz segment treea nad intervalom $[1,N]$ razdvajamo $[l,r]$ i gradimo novo stablo:

Rekurzivno razdvajamo počevši od čvora 1; kad čvor ne postoji ili je njegov interval $[s,t]$ disjunktan s $[l,r]$, izravno se vraćamo.

Kad se $[s,t]$ i $[l,r]$ sijeku, treba stvoriti novi čvor.

Kad je $[s,t]$ sadržan u $[l,r]$, trenutni čvor treba izravno prikvačiti pod novo stablo i prekinuti stari brid.

???+ note "Složenost razdvajanja segment treeova"
    Lako se vidi da se prekine najviše $\log n$ bridova, pa je vremenska složenost jednog razdvajanja $O(\log⁡ n)$, jednako kao kod upita nad intervalom.

### Implementacija

```cpp
void split(int &p, int &q, int s, int t, int l, int r) {
  if (t < l || r < s) return;
  if (!p) return;
  if (l <= s && t <= r) {
    q = p;
    p = 0;
    return;
  }
  if (!q) q = New();
  int m = s + t >> 1;
  if (l <= m) split(ls[p], ls[q], s, m, l, r);
  if (m < r) split(rs[p], rs[q], m + 1, t, l, r);
  push_up(p);
  push_up(q);
}
```

### Primjer zadatka

???+ note "[P5494【模板】线段树分裂](https://www.luogu.com.cn/problem/P5494)"
    ??? note "Ideja rješenja"
        Predložak za razdvajanje segment treea: razdvoji $[x,y]$.
        
        -   Spoji stablo $t$ u stablo $p$: jedno spajanje.
        
        -   U stablo $p$ umetni $x$ komada vrijednosti $q$: izmjena jednog elementa.
        
        -   Upit za broj elemenata u $[x,y]$: zbroj intervala.
        
        -   Upit za $k$-ti najmanji element.
    
    ??? note "Referentni kod"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-split.cpp"
        ```

## Zadaci za vježbu

-   [Luogu P4556 \[Vani 有约会\] 雨天的尾巴/【模板】线段树合并](https://www.luogu.com.cn/problem/P4556)
-   [Luogu P5494【模板】线段树分裂](https://www.luogu.com.cn/problem/P5494)
-   [Luogu P1600 天天爱跑步](https://www.luogu.com.cn/problem/P1600)
-   [Luogu P4577 \[FJOI2018\] 领导集团问题](https://www.luogu.com.cn/problem/P4577)
-   [Luogu P2824 \[HEOI2016/TJOI2016\] 排序](https://www.luogu.com.cn/problem/P2824)
