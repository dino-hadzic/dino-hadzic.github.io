---
title: Uvod u perzistentne strukture podataka
---

author: morris821028

## Uvod

Perzistentna struktura podataka (Persistent data structure) čuva sve prethodne verzije i podržava nepromjenjivost (immutability) pri izvođenju operacija.

## Vrste perzistentnosti

### Djelomična perzistentnost (Partially Persistent)

Svim se verzijama može pristupiti, ali mijenjati se može samo najnovija.

### Potpuna perzistentnost (Fully Persistent)

Svim se verzijama može pristupiti i sve se mogu mijenjati.

Ako je podržano i spajanje dviju prethodnih verzija, govorimo o konfluentnoj perzistentnosti (Confluently Persistent).

## Primjene

### Računalna geometrija

U računalnoj geometriji postoje brojni offline algoritmi, primjerice algoritam pomičnog pravca (sweep line), koji jednim prolaskom odgovara na sve upite i ima izvrsnu vremensku složenost. Međutim, ako se upiti moraju obrađivati online, novi prolazak za svaki upit pogoršava složenost upita s logaritamske na linearnu. Perzistentnost nudi drukčiji pristup: vremensku os prolaska uzmemo kao osnovu promjena i povezane strukture učinimo perzistentnima. Ako se za potrebe upita možemo kretati po toj vremenskoj osi u logaritamskom vremenu, prethodni problem možemo riješiti dinamički.

### Obrada znakovnih nizova

Perzistentnost omogućuje vrlo učinkovito spajanje i sprječava pad performansi uzrokovan stvaranjem velikog broja ponovljenih znakovnih nizova, pa se razne operacije mogu izvoditi znatno brže od linearnog vremena. Primjerice, C++ rope perzistentna je struktura podataka. Primjena nije ograničena na znakovne nizove: perzistentnost može biti korisna kad god obrađeni podaci sadrže mnogo ponavljanja.

### Povratak na prethodne verzije

To u praksi odgovara naredbama redo/undo u većini aplikacija. Ako baza podataka ili promjene stanja koriste složene strukture radi učinkovitosti (za razliku od struktura hash i set, u kojima poništavanje operacije traje konstantno ili logaritamsko vrijeme), perzistentne strukture omogućuju brz povratak promjena smanjivanjem troška operacija redo/undo.

Sama baza podataka može vratiti promjenu u konstantnom vremenu tako da bilježi samo promijenjene dijelove. Na aplikacijskom sloju većina implementacija odbacuje predmemoriju i ponovno izračunava cijelu strukturu. Ako je veličina promjene koju vraćamo m, a ponovni izračun strukture košta n+m, velika razlika između n i m može učiniti uzastopno poništavanje promjena vrlo sporim za korisnika.

### Funkcijsko programiranje

Funkcijsko programiranje zahtijeva posebne strukture podataka koje odgovaraju svojstvima jezika. Nepromjenjivost je pritom posebno važna za paralelna okruženja i otklanjanje pogrešaka. Primjerice, objektno orijentirana Java od verzije 8 uvodi klasu stream, koja podržava pisanje funkcijskim stilom i pruža posebne mogućnosti poput lijenog izračunavanja i beskonačnih domena vrijednosti.

## Literatura

-   <https://en.wikipedia.org/wiki/Persistent_data_structure>
-   Kolegij MIT-a <https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-854j-advanced-algorithms-fall-2005/lecture-notes/persistent.pdf>
