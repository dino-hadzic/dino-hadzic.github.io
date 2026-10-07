# Upute za prevođenje OI Wikija (hr + en)

Izvornik: klon https://github.com/OI-wiki/OI-wiki (lokalno `/home/ubuntu/oiwiki`), stranice su `docs/<put>.md`.

## Što se piše

Za svaku stranicu `docs/<put>.md` nastaju:

- `src/hr/<put>.md` – hrvatski prijevod
- `src/en/<put>.md` – engleski prijevod
- za svaki kôd koji stranica uključuje (`--8<-- "docs/.../x.cpp"` ili `x.py:odjeljak`):
  `src/code/hr/docs/.../x.cpp` i `src/code/en/docs/.../x.cpp` – kopija izvornog koda u kojoj su
  prevedeni **samo komentari** (ništa drugo se ne smije promijeniti: ni razmaci, ni imena, ni redoslijed).
  Ako kôd nema komentara, kopira se nepromijenjen u obje mape.
- slike koje stranica koristi kopiraju se u `src/images/<put do slike kao u docs/>`,
  npr. `docs/basic/images/x.svg` → `src/images/basic/images/x.svg`.

## Oblik datoteke

```
---
title: Naslov stranice na tom jeziku
---

(prevedeni Markdown)
```

Naslov stranice dolazi iz `nav.json` (kineski naslov iz mkdocs.yml); prevedi ga u `title`.

## Pravila

1. **Struktura 1:1.** Jednak broj i redoslijed naslova (`##`, `###` …), odlomaka, popisa, okvira (`!!! note`, `??? note "…"`,
   `???+ warning "…"`), kartica (`=== "C++"`), formula i blokova koda kao u izvorniku. Hrvatska i engleska inačica
   moraju imati isti broj naslova (build to provjerava).
2. **Matematika se ne mijenja.** `$...$` i `$$...$$` prepisuju se doslovno. Smije se prevesti samo tekst unutar `\text{...}`
   ako je na kineskom; engleski `\text{}` u pseudokodu ostaje engleski u obje inačice.
3. **Kôd se ne mijenja**, prevode se samo komentari (i u datotekama u `src/code/` i u blokovima koda ugrađenima u Markdown).
   Redci `--8<-- "docs/..."` prepisuju se doslovno. Kineski tekst u stringovima programa (npr. `printf("答案")`) ostaje
   nepromijenjen.
4. **Poveznice.** Relativne poveznice na druge stranice ostaju kakve jesu (`../ds/stack.md`, `./complexity.md#...`);
   build ih sam preusmjerava na prevedenu stranicu ili na izvorni oi-wiki.org. Kotve (`#...`) iza `.md`: ako cilj još
   nije preveden, ostavi kinesku kotvu; ako je preveden, napiši kotvu kao slug prevedenog naslova (mala slova, razmaci → `-`).
   Vanjske poveznice ostaju; ako postoji engleska inačica Wikipedijina članka, koristi nju umjesto zh.wikipedia.
5. **Terminologija.** Ustaljeni nazivi algoritama i struktura ostaju u obliku koji se koristi na natjecanjima u Hrvatskoj:
   bubble sort, quick sort, merge sort, heap, segment tree, Fenwick tree (BIT), DP, BFS/DFS, LCA, trie, hash,
   prefiksne sume, binarno pretraživanje (binary search), složenost O(n log n), stabilnost, amortizirana složenost,
   greedy (pohlepni algoritam), divide and conquer (podijeli pa vladaj), backtracking, bitmask, memoizacija.
   Prvi put u stranici navedi engleski izraz u zagradi ako hrvatski nije uobičajen, npr. „prefiksne sume (prefix sums)”.
   Kineske nazive natjecanja/platformi zadrži u izvornom latiničnom obliku (NOIP, NOI, CSP-J/S, Luogu, Codeforces, AtCoder).
   Oznake zadataka kao „洛谷 P1177” pišu se „Luogu P1177”.
6. **Jezik.** Prirodan hrvatski (ijekavica, standardni pravopis, navodnici „…”), bez doslovnog prevođenja kineske sintakse.
   Engleski: jednostavan, tehnički, američki pravopis. Kineska interpunkcija (，．：「」（）) zamjenjuje se latiničnom.
7. **Ne prevodi** `--8<--` putanje, imena datoteka, HTML atribute ni identifikatore.
8. **Ništa se ne izostavlja i ne dodaje** (osim nužnog pojašnjenja kinesko-specifičnog pojma u zagradi).

## Provjera

```
OIWIKI_UPSTREAM=/home/ubuntu/oiwiki python3 tools/oiwiki/build.py
```

mora završiti s `0 grešaka` (provjerava: oba jezika postoje, naslov, kôd jednak izvorniku osim komentara,
slike i poveznice postoje, kotve postoje). Upozorenje o različitom broju naslova znači da struktura nije 1:1.
