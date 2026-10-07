---
title: Tokovi s donjim i gornjim granicama
---

Prije čitanja ovog članka pročitajte [Maksimalni tok](./max-flow.md) i uvjerite se da dobro vladate algoritmima za maksimalni tok.

## Pregled

Tok s donjim i gornjim granicama (bounded flow) u biti znači da svaki brid mreže ima gornju granicu toka $c(u,v)$ i donju granicu toka $b(u,v)$. Drugim riječima, dopustivi tok mora zadovoljavati $b(u,v) \leq f(u,v) \leq c(u,v)$. Istodobno u svim vrhovima osim izvora i ponora mora vrijediti očuvanje toka.

Ovisno o zahtjevima zadatka, tokovima s granicama možemo rješavati razne probleme.

## Dopustivi tok bez izvora i ponora

Zadana je mreža $G$ bez izvora i ponora. Pitamo se postoji li način da svakom bridu dodijelimo tok tako da tok svakog brida zadovoljava granice i da u svakom vrhu vrijedi očuvanje toka.

Pretpostavimo da svakim bridom već teče $b(u,v)$ jedinica toka; to zovemo početnim tokom. Istodobno u novi graf dodamo brid iz $u$ u $v$ kapaciteta $c(u,v) - b(u,v)$. Na novom grafu provodimo prilagodbu.

Maksimalni tok zahtijeva da početni tok zadovoljava očuvanje (maksimalni tok možemo shvatiti kao tok s granicama u kojem je donja granica $0$), ali konstruirani početni tok vrlo vjerojatno ne zadovoljava očuvanje. Neka je za neki vrh razlika početnog ulaznog i početnog izlaznog toka jednaka $M$.

Ako je $M=0$, tok je očuvan i dodatni bridovi nisu potrebni.

Ako je $M>0$, ulazni je tok prevelik, pa uvodimo dodatni izvor $S'$ i iz $S'$ u taj vrh povlačimo dodatni brid kapaciteta $M$.

Ako je $M<0$, izlazni je tok prevelik, pa uvodimo dodatni ponor $T'$ i iz tog vrha u $T'$ povlačimo dodatni brid kapaciteta $-M$.

Ako je dodatni brid zasićen, uvjet očuvanja toka u tom vrhu može biti zadovoljen; inače nije. (Jer tek izvorni graf zajedno s dodatnim tokom zadovoljava očuvanje toka u izvornom grafu.)

Nakon izgradnje grafa izračunamo maksimalni tok od $S'$ do $T'$. Ako su svi bridovi koji izlaze iz $S'$ zasićeni, dopustivi tok postoji; inače ne postoji.

### Primjer

???+ note "[Luogu P14578 [Predložak] Dopustivi tok s granicama bez izvora i ponora](https://www.luogu.com.cn/problem/P14578)"
    Zadan je usmjereni graf $G$ s $n$ vrhova i $m$ usmjerenih bridova; svaki brid ima donju granicu toka $l_i$ i gornju granicu toka $r_i$.
    
    Konstruirajte rješenje u kojem tok $w_i$ svakog brida zadovoljava ograničenje $l_i\leq w_i\leq r_i$ i u kojem je tok očuvan u svakom vrhu, tj. ulazni tok svakog vrha jednak je izlaznom. Ili prijavite da rješenje ne postoji.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/graph/code/flow/bound/bound_1.cpp"
    ```

## Dopustivi tok s izvorom i ponorom

Zadana je mreža $G$ s izvorom i ponorom. Pitamo se postoji li način da svakom bridu dodijelimo tok tako da tok svakog brida zadovoljava granice i da u svakom vrhu osim izvora i ponora vrijedi očuvanje toka.

Neka je izvor $S$, a ponor $T$.

Tada možemo dodati brid od $T$ do $S$ s gornjom granicom $\infty$ i donjom granicom $0$ i problem svesti na dopustivi tok bez izvora i ponora.

Ako rješenje postoji, vrijednost dopustivog toka od $S$ do $T$ jednaka je toku na dodatnom bridu od $T$ do $S$.

## Maksimalni tok s izvorom i ponorom

Zadana je mreža $G$ s izvorom i ponorom. Pitamo se postoji li način da svakom bridu dodijelimo tok tako da tok svakog brida zadovoljava granice i da u svakom vrhu osim izvora i ponora vrijedi očuvanje toka. Ako postoji, pitamo se kolika je najveća vrijednost toka koja zadovoljava ta ograničenja.

Pronađemo bilo koji dopustivi tok u mreži. Ako ga nema, odmah završavamo.

Inače promatramo rezidualnu mrežu nakon brisanja svih dodatnih bridova i na njoj provodimo prilagodbu.

Na rezidualnoj mreži još jednom izračunamo maksimalni tok od $S$ do $T$; odgovor je zbroj vrijednosti dopustivog toka i tog maksimalnog toka.

??? warning "Vrlo česta pogreška"
    Maksimalni tok od $S$ do $T$ računa se izravno na rezidualnoj mreži koja ostane nakon računanja dopustivog toka s izvorom i ponorom.
    
    Nipošto ga ne smijemo računati na izvornoj mreži.

## Minimalni tok s izvorom i ponorom

Zadana je mreža $G$ s izvorom i ponorom. Pitamo se postoji li način da svakom bridu dodijelimo tok tako da tok svakog brida zadovoljava granice i da u svakom vrhu osim izvora i ponora vrijedi očuvanje toka. Ako postoji, pitamo se kolika je najmanja vrijednost toka koja zadovoljava ta ograničenja.

Slično, razmišljamo o tome kako iz rezidualne mreže „vratiti” nepotreban tok.

Pronađemo bilo koji dopustivi tok u mreži. Ako ga nema, odmah završavamo.

Inače promatramo rezidualnu mrežu nakon brisanja svih dodatnih bridova.

Na rezidualnoj mreži još jednom izračunamo maksimalni tok od $T$ do $S$; odgovor je vrijednost dopustivog toka umanjena za taj maksimalni tok.

??? note "[AHOI 2014 Sporedne priče](https://loj.ac/problem/2226)"
    Za svaki brid priče od $x$ do $y$ s cijenom $v$ postavimo gornju granicu $\infty$, a donju $1$.
    
    Za svaki vrh povučemo brid prema $T$ s cijenom $c$, gornjom granicom $\infty$ i donjom granicom $1$.
    
    Vrh $S$ je vrh broj $1$.
    
    Dovoljno je jednom izračunati dopustivi tok minimalne cijene s granicama, izvorom i ponorom.
    
    Budući da je postupak za dopustivi tok minimalne cijene sličan onome za minimalni dopustivi tok, ovdje ga ne razrađujemo.
