---
title: Perzistentni trie
---

## Uvod

Perzistentni trie (persistent trie) gradi se na isti način kao i perzistentni segment tree: pri svakoj promjeni mijenjaju se samo čvorovi koji su dodani ili čija se vrijednost promijenila, dok se nepromijenjeni čvorovi zadržavaju i na njih se povezujemo iz prethodne verzije, tako da je trie do kojeg se dolazi iz korijena svake verzije potpun i sadrži sve informacije.

U većini zadataka s perzistentnim triejem trie se pojavljuje u obliku [01-trieja](../string/trie.md#održavanje-ekstrema-xor-a).

??? note "Primjer zadatka [Najveći XOR](https://www.luogu.com.cn/problem/P4735)"
    Za niz $a$ duljine $n$ treba podržati sljedeće operacije:
    
    1.  Na kraj niza dodaj broj $x$; duljina niza $n$ poveća se za $1$.
    2.  Za zadani interval $[l,r]$ i vrijednost $k$ nađi najveću vrijednost $k \oplus \bigoplus^{n}_{i=p} a_i$ uz $l\le p\le r$.

## Postupak

Traženu vrijednost nije sasvim jednostavno izračunati. Uobičajenim trikom za XOR uzastopnih elemenata označimo $s_x=\bigoplus_{i=1}^x a_i$; tada je izvorni izraz jednak $s_{p-1}\oplus s_n\oplus k$. Primijetimo da je $s_n \oplus k$ tijekom upita fiksan, pa se upit svodi na traženje najveće vrijednosti XOR-a s fiksnom konstantom ($s_n\oplus k$) na intervalu $[l-1,r-1]$.

Nastavimo razmišljati kao kod perzistentnog segment treea i promotrimo slučaj u kojem svaki upit obuhvaća cijeli interval. Tada je dovoljno nad tim intervalom izgraditi trie, u njega ubaciti svaki broj iz intervala i pri upitu, kad god je moguće, skretati prema bitu suprotnom od trenutnog.

Za upit na intervalu koristimo ideju prefiksnih suma i razlike: trie intervala dobivamo „oduzimanjem” dvaju prefiksnih trieja (tj. dviju povijesnih verzija nastalih dodavanjem brojeva redom). Uz to, u duhu dinamičkog stvaranja čvorova, ne dodajemo čvorove koji nikad nisu bili izračunati, čime smanjujemo utrošak memorije.

```cpp
--8<-- "docs/ds/code/persistent-trie/persistent-trie_1.cpp"
```
