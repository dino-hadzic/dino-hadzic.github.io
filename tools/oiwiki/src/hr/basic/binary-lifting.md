---
title: Binary lifting
---

Ova stranica kratko predstavlja binary lifting (metodu udvostručavanja).

## Definicija

**Binary lifting** (metoda udvostručavanja), kako i ime kaže, znači „rast udvostručavanjem”. Kad pri rekurzivnom računanju prostor stanja postane prevelik da bi obično linearno računanje zadovoljilo zahtjeve na vremensku i prostornu složenost, možemo udvostručavanjem računati samo vrijednosti u onim stanjima koja su na položajima cjelobrojnih potencija broja $k$, kao predstavnike. Kad trebamo vrijednost na nekom drugom položaju, koristimo svojstvo da se „svaki cijeli broj može prikazati kao zbroj nekoliko potencija broja $k$” i iz već izračunatih predstavnika slažemo traženu vrijednost. Stoga primjena udvostručavanja zahtijeva da se prostor stanja problema može podijeliti po potencijama broja $k$. Obično se uzima $k = 2$.[^ref1]

Metoda se primjenjuje u mnogim algoritmima; najčešće za problem RMQ i za pronalaženje [LCA (najnižeg zajedničkog pretka)](../graph/lca.md).

## Primjene

### Problem RMQ

Vidi: [RMQ](../topic/rmq.md).

RMQ je kratica za Range Maximum/Minimum Query – upit za maksimum (minimum) na intervalu. Rješenje problema RMQ koje koristi ideju udvostručavanja je [sparse table (ST tablica)](../ds/sparse-table.md).

### LCA na stablu udvostručavanjem

Vidi: [Najniži zajednički predak](../graph/lca.md).

## Primjeri

### Primjer 1

???+ note "Primjer"
    Kako sa što manje utega izvagati sve težine iz $[0,31]$? (Utezi se smiju stavljati samo na jednu stranu vage.)

??? note "Ideja rješenja"
    Odgovor je: s pet utega 1 2 4 8 16 mogu se izvagati sve težine iz $[0,31]$. Isto tako, za sve težine iz $[0,127]$ dovoljno je sedam utega 1 2 4 8 16 32 64. Kad za težine utega svaki put biramo nenegativne cjelobrojne potencije broja 2, s vrlo malo utega možemo izvagati bilo koju potrebnu težinu.
    
    Primjerice, za sve težine iz $[0,1023]$ treba samo 10 utega, a za sve iz $[0,1048575]$ samo 20. Ako se ciljna težina udvostruči, broj utega poraste samo za 1. To se zove „logaritamski” rast, jer je potreban broj utega proporcionalan logaritmu raspona ciljne težine.

### Primjer 2

???+ note "Primjer"
    Zadan je ciklus duljine $n$ i konstanta $k$; iz $i$-tog vrha svaki put skačemo u vrh $(i+k)\bmod n+1$, ukupno $m$ puta. Svaki vrh ima težinu $a_i$. Izračunajte zbroj težina početnih vrhova svih $m$ skokova modulo $10^9+7$.
    
    Ograničenja: $1\leq n\leq 10^6$, $1\leq m\leq 10^{18}$, $1\leq k\leq n$, $0\le a_i\le 10^9$.

??? note "Ideja rješenja"
    Očito ne možemo grubom silom simulirati $m$ skokova, jer $m$ može biti reda $10^{18}$ i vremenski to ne bi prošlo.
    
    Zato treba predobrada: unaprijed objediniti neke informacije kako bi se pri upitu brže došlo do rezultata. Kad bismo zapisali rezultat za svaki mogući broj skokova, ni vremenski ni prostorno ne bismo izdržali.
    
    Kako onda napraviti predobradu? Pogledajte prvi primjer. Imate li ideju?
    
    Vratimo se zadatku. Želimo unaprijed izračunati neke informacije, a zatim iz njih što brže sastaviti odgovor; pritom tih informacija ne smije biti previše. Možemo zato unaprijed izračunati informacije u jedinicama nenegativnih potencija broja 2: tako u predobradi obrađujemo malo podataka, a ni sastavljanje odgovora ne zahtijeva mnogo posla.
    
    U ovom zadatku to znači da za svaki vrh unaprijed izračunamo rezultat skoka za 1, 2, 4, 8 … koraka (vrh u kojem završavamo i zbroj težina). Ako zatim treba skočiti 13 koraka, dovoljno je skočiti 1+4+8 koraka: iz početnog vrha skočimo 1 korak, iz dobivenog vrha 4 koraka, pa 8 koraka, usput zbrajajući unaprijed izračunate zbrojeve težina, i dobijemo zbroj težina za 13 koraka.
    
    Za svaki vrh i $2^i$ koraka čuvamo `go[i][x]` – vrh u kojem završava skok od $2^i$ koraka iz $x$-tog vrha, i `sum[i][x]` – zbroj težina koji se pri tome skupi. U predobradi koristimo dvostruku petlju: skok od $2^i$ koraka možemo gledati kao skok od $2^{i-1}$ koraka pa još $2^{i-1}$ koraka, jer je očito $2^{i-1}+2^{i-1}=2^i$. Dakle `sum[i][x] = sum[i-1][x]+sum[i-1][go[i-1][x]]` i `go[i][x] = go[i-1][go[i-1][x]]`.
    
    Postoje i detalji implementacije na koje treba paziti. Da pri zbrajanju ništa ne izostavimo niti udvostručimo, obično unaprijed računamo zbrojeve težina „zatvoreno slijeva, otvoreno zdesna”. To znači: za skok od 1 koraka bilježimo samo težinu tog vrha; za skok od 2 koraka težinu tog vrha i sljedećeg. Dakle težinu završnog vrha nikad ne uključujemo u `sum`. Tada u predobradi zbrojeve dvaju dijelova jednostavno zbrojimo i ne moramo se brinuti da bi se kraj prvog dijela i početak drugog brojali dvaput.
    
    Iako $m\leq 10^{18}$ izgleda zastrašujuće, dovoljno je unaprijed izračunati razine od $0$ do $59$ i zadatak se lako rješava, mnogo brže od grube sile. Stručnim rječnikom, [vremenska složenost](./complexity.md) ovog postupka je $\Theta(n\log m)$ za predobradu i $\Theta(\log m)$ po upitu.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/basic/code/binary-lifting/binary-lifting_1.cpp"
    ```

## Literatura i bilješke

[^ref1]: Prema Li Yudong, *Algorithm Competition Advanced Guide* (《算法竞赛进阶指南》), odjeljak 0x06 „Udvostručavanje”.
