---
title: Redoslijed bajtova
---

Ova stranica kratko predstavlja pojam i vrste redoslijeda bajtova (endianness).

## Uvod

Redoslijed bajtova pravilo je pohrane programskih objekata koji se prostiru na više bajtova; opisuje način na koji su bajtovi objekta raspoređeni.

## Vrste

Postoje dva redoslijeda bajtova: little endian (mali kraj) i big endian (veliki kraj).

Radi lakšeg objašnjenja, u nastavku kao primjer uzimamo varijablu na adresi `0x100`, tipa `int`, s heksadecimalnom vrijednošću `0x01234567`. Pri tome je `0x01` najznačajniji bajt, a `0x67` najmanje značajan bajt.

### Little endian

Little endian znači da računalo objekt u memoriji pohranjuje redom od **najmanje** značajnog bajta do **najznačajnijeg** bajta.

Gore spomenuta varijabla prikazuje se ovako:

| .... | 0x100 | 0x101 | 0x102 | 0x103 | .... |
| ---- | ----- | ----- | ----- | ----- | ---- |
| .... | 67    | 45    | 23    | 01    | .... |

### Big endian

Big endian znači da računalo objekt u memoriji pohranjuje redom od **najznačajnijeg** bajta do **najmanje** značajnog bajta.

Gore spomenuta varijabla prikazuje se ovako:

| .... | 0x100 | 0x101 | 0x102 | 0x103 | .... |
| ---- | ----- | ----- | ----- | ----- | ---- |
| .... | 01    | 23    | 45    | 67    | .... |

### Razlika između dvaju redoslijeda

Zapravo ni jedan od tih dvaju redoslijeda bajtova nije bolji ni lošiji od drugoga. Njihova imena, „mali kraj” i „veliki kraj”, potječu iz knjige „Gulliverova putovanja”. U knjizi se dvije stranke u Liliputu neprekidno ratuju jer se ne mogu dogovoriti treba li jaje razbijati s malog ili s velikog kraja. Baš kao i spor o razbijanju jaja, spor o izboru redoslijeda bajtova nije tehničke naravi.

Naravno, nepodudaranje redoslijeda bajtova dovodi do toga da se binarni podaci pri prijenosu između računala različitih vrsta obrnu. Da bi se to izbjeglo, mrežne aplikacije uspostavile su standard koji jamči da se pri slanju koristi dogovoreni mrežni standard, a ne interni prikaz pojedinog računala.

## Uobičajeni izbor redoslijeda

-   Little endian: x86, ARM procesori s Androidom, iOS-om i Windowsima

-   Big endian: Sun, PPC Mac, internet
