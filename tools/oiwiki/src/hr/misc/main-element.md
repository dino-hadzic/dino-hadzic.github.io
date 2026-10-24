---
title: Problem većinskog elementa
---

## Opis problema

Zadan je niz od $n$ elemenata za koji je zajamčeno da postoji element $a$ koji se pojavljuje **strogo više** od $n/2$ puta; pronađite taj element.

## Rješenja

### Offline algoritam

Ako od početka znamo cijeli niz, prirodna je ideja prebrojati pojavljivanja svakog elementa u nizu; onaj koji se pojavljuje više od $n/2$ puta većinski je element. Možemo napraviti bucket (polje brojača) za brojanje pojavljivanja svake vrijednosti i ispisati element s više od $n/2$ pojavljivanja.

No gornje rješenje za brojanje uvodi bucket i nije prostorno učinkovito. Očito, ako u nizu postoji većinski element, onda je nakon sortiranja element niza na položaju $\lfloor n/2\rfloor+1$ sigurno većinski element, a pomoću [`nth_element`](https://en.cppreference.com/w/cpp/algorithm/nth_element.html) možemo ga pronaći. Tako većinski element dobivamo u linearnoj vremenskoj složenosti bez uvođenja dodatnog prostora.

### Online algoritam

U nekim situacijama podatke moramo obrađivati online, kao tok (stream); tada nam treba algoritam koji ne zahtijeva poznavanje svih podataka unaprijed, nego odgovor postupno izračunava samo iz dosad zadanih podataka. **Algoritam većinskog glasanja** (Boyer–Mooreov algoritam) [^ref1] jedan je takav algoritam koji problem većinskog elementa rješava online.

Budući da se većinski element pojavljuje više od $n/2$ puta, ako iz cijelog niza neprestano poništavamo par koji čine jedan većinski element i jedan element različit od njega, na kraju nužno preostaje većinski element. Na temelju tog zapažanja možemo oblikovati online algoritam koji provodi takvo poništavanje. Neka varijable `val` i `cnt` redom označavaju trenutačnog kandidata za većinski element i koliko bi primjeraka tog kandidata preostalo kad bismo proveli opisano poništavanje. Na početku je `cnt` postavljen na $0$. Svaki put iz toka uzmemo jedan element; ako je trenutačni `cnt` jednak $0$, kandidat je u potpunosti poništen i trenutačno zabilježeni `val` sigurno nije većinski element, pa trenutačni element postavimo za kandidata. Zatim provjerimo je li trenutačni element jednak kandidatu: ako jest, `cnt` uvećamo za $1$, a ako nije, taj se element poništava zajedno s jednim kandidatom pa `cnt` umanjimo za $1$. Ponavljamo dok ne pročitamo cijeli tok; `val` je tada većinski element.

???+ warning "Napomena"
    Kad u izvornim podacima ne postoji većinski element, rezultat ovog algoritma je pogrešan. Ako treba provjeriti postoji li u nizu većinski element, tok podataka treba pročitati još jednom, prebrojati pojavljivanja vrijednosti `val` i provjeriti prelazi li broj $n/2$.
    
    Za ponovno čitanje toka možemo vratiti pokazivač položaja ulaza, npr. bibliotečnim funkcijama [`std::basic_istream<CharT,Traits>::seekg`](https://en.cppreference.com/w/cpp/io/basic_istream/seekg) (ulaz preko tokova) ili [`rewind`](https://en.cppreference.com/w/c/io/rewind), [`fseek`](https://en.cppreference.com/w/c/io/fseek) (ulaz u stilu C-a).

## Primjeri zadataka

???+ example "[Luogu P2397 yyy loves Maths VI (mode)](https://www.luogu.com.cn/problem/P2397)"
    Odredite većinski element zadanog niza.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/main-element/main-element_1.cpp"
    ```

???+ example "[LeetCode 229. Majority Element II](https://leetcode.cn/problems/majority-element-ii)"
    Zadan je niz od $n$ cijelih brojeva; pronađite sve elemente koji se pojavljuju više od $\lfloor n/3\rfloor$ puta.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/main-element/main-element_2.cpp:core"
    ```

## Literatura

[^ref1]: [Boyer–Moore majority vote algorithm - Wikipedia](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
