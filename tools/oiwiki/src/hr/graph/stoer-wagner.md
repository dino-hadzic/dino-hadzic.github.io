---
title: Stoer–Wagnerov algoritam
---

## Definicije

Budući da smo napustili definiciju **izvora i ponora**, moramo iznova definirati pojam **reza**.

(Zapravo se definicija reza iz poglavlja o tokovima ne podudara s onom na Wikipediji; samo zato što su rezovi s kojima se obično susrećemo „problem minimalnog reza s izvorom i ponorom”, taj se pojam ustalio.)

### Rez

Skup bridova čijim uklanjanjem mreža prestaje biti povezana (tj. raspada se na dva podgrafa) zove se rez grafa.

Formalno: u neusmjerenom grafu $G = (V, E)$ neka je $C$ skup nekih lukova grafa $G$; ako brisanjem svih lukova iz $C$ graf $G$ prestaje biti povezan, $C$ zovemo rezom grafa $G$.

### Problem minimalnog reza s izvorom i ponorom

Jednako kao definicija u [Minimalni rez](./flow/min-cut.md).

### Problem minimalnog reza bez izvora i ponora

Rez čiji je zbroj težina lukova najmanji. Zove se i **globalni minimalni rez**.

Očito, složenost izravnog pokretanja algoritma za tok ovdje nije prihvatljiva.

***

## Stoer–Wagnerov algoritam

### Uvod

Stoer–Wagnerov algoritam predložili su 1995. *Mechthild Stoer* i *Frank Wagner*; to je algoritam koji **rekurzivno** rješava problem globalnog minimalnog reza na **neusmjerenim grafovima s pozitivnim težinama**.

### Svojstva

Složenost algoritma je $O(|V||E| + |V|^{2}\log|V|)$, što se obično približno smatra $O(|V|^3)$.

Implementacija se temelji na sljedećoj osnovnoj činjenici: neka su $S, T$ bilo koja dva vrha grafa $G$. Tada za svaki rez $C$ grafa $G$ vrijedi ili da su $S, T$ u istoj komponenti povezanosti, ili da je $C$ jedan ${S-T}$ rez.

### Postupak

1.  U grafu $G$ proizvoljno odaberemo dva vrha $s, t$, uzmemo ih kao izvor i ponor te izračunamo $S-T$ minimalni rez grafa $G$ (nazovimo ga *cut of phase*) i ažuriramo trenutni odgovor.
2.  „Spojimo” vrhove $s, t$; ako je $|V|$ u grafu $G$ veći od $1$, vratimo se na prvi korak.
3.  Ispišemo najmanji od svih *cut of phase*.

Spajanje vrhova $s, t$: brišemo brid $(s, t)$ između $s$ i $t$; za svaki vrh $k$ iz $G \setminus \{s, t\}$ brišemo $(t, k)$ i njegovu težinu $d(t, k)$ pribrajamo težini $d(s, k)$.

Objašnjenje: ako su $s, t$ u istoj komponenti, tada za vrh $k$ iz $G \setminus \{s, t\}$, ako je $(k, s) \in C_{\min}$, nužno vrijedi i $(k, t) \in C_{\min}$; inače bi, jer su $s, t$ povezani i $k, t$ povezani, $s, k$ bili u istoj komponenti, pa bi $C = C_{\min} \setminus \{(t, k)\}$ bio bolji od $C_{\min}$. Vrijedi i obrnuto. Stoga $s, t$ možemo promatrati kao jedan vrh.

Korak 1 pokriva slučaj kad $s,t$ nisu u istoj komponenti, a korak 2 preostale slučajeve. Budući da svako izvođenje koraka 2 smanjuje $|V|$ za $1$, algoritam završava nakon $|V| - 1$ koraka.

### Računanje S-T minimalnog reza

(Očito ne tokom.)

Pretpostavimo da je nakon nekoliko spajanja trenutni graf $G'=(V', E')$ i izvodimo korak 1.

Gradimo skup $A$; na početku $A = \varnothing$.

U svakom koraku u $A$ dodajemo onaj vrh iz $V'$ koji zadovoljava $i \notin A$ i ima najveću vrijednost težinske funkcije $w(A, i)$, sve dok $|A| = |V'|$.

Pritom je težinska funkcija definirana kao:

$w(A, i) = \sum_{j \in A} d(i, j)$

(ako $(i, j) \notin E'$, onda $d(i, j) = 0$).

Lako se vidi da je redoslijed dodavanja vrhova u $A$ jednoznačan; neka $\operatorname{ord}(i)$ označava $i$-ti vrh dodan u $A$, $t = \operatorname{ord}(|V'|)$; a $\operatorname{pos}(v)$ veličinu $|A|$ nakon dodavanja $v$ u $A$, tj. redni broj dodavanja vrha $v$.

Tada je za bilo koji vrh $s$ jedan rez između $s$ i $t$ upravo $w(t)$.

### Dokaz

Kažemo da je vrh $v$ aktiviran ako i samo ako u trenutku dodavanja $v$ u $A$ posljednji vrh $u$ koji je tada u $A$ dodan ranije od $v$ i u grafu $G'' = (V', E'/C)$ $u$ i $v$ nisu u istoj komponenti.

![Stoer-Wagner1](./images/Stoer-Wagner1.png)

Na slici plavo i žuto područje dvije su različite komponente, a brojevi u uglatim zagradama redoslijed dodavanja u $A$. Sivi su vrhovi aktivni, a bijeli nisu.

Definiramo $A_v = \{u \mid \operatorname{pos}(u) < \operatorname{pos}(v)\}$, tj. vrhove dodane u $A$ strogo prije $v$, i neka je $E_v$ skup bridova induciranog podgrafa od $E'$ (sa skupom vrhova $A_v \cup\{v\}$). (Uočite da uključuje vrh $v$.)

Definiramo inducirani rez $C_v$ kao $C \cap E_v$. $w(C_v) = \sum_{(i,j) \in C_v} d(i, j)$.

???+ note "Lema 1"
    Za svaki aktivirani vrh $v$ vrijedi $w(A_v, v) \le w(C_v)$.
    
    Dokaz: matematičkom indukcijom.
    
    Za prvi aktivirani vrh $v_0$ po definiciji vrijedi $w(A_{v_0}, v_0) = w(C_{v_0})$.
    
    Za dva kasnija aktivirana vrha $u, v$, uz pretpostavku $\operatorname{pos}(v) < \operatorname{pos}(u)$, vrijedi:
    
    $w(A_u, u) = w(A_v, u) + w(A_u - A_v, u)$
    
    Nadalje, znamo:
    
    $w(A_v, u) \le w(A_v, v)$ i $w(A_v, v) \le w(C_v)$, pa zajedno dobivamo:
    
    $w(A_u, u) \le w(C_v) + w(A_u - A_v, u)$
    
    Budući da $w(A_u - A_v, u)$ doprinosi $w(C_u)$, a ne doprinosi $w(C_v)$, uz pozitivne težine svih bridova slijedi:
    
    $w(A_u,u) \le w(C_u)$
    
    Čime je indukcija dovršena.

Budući da je $\operatorname{pos}(s) < \operatorname{pos}(t)$ i da $s, t$ nisu u istoj komponenti, $t$ će biti aktiviran, odakle slijedi $w(A_t, t) \le w(C_t) = w(C)$.

??? note "[P5632 [Predložak] Stoer–Wagnerov algoritam](https://www.luogu.com.cn/problem/P5632)"
    ```cpp
    --8<-- "docs/graph/code/stoer-wagner/stoer-wagner_1.cpp"
    ```

***

### Analiza složenosti i optimizacije

Složenost operacije *contract* je $O(|E| + |V|\log|V|)$.

Ukupno se izvodi $O(|V|)$ operacija *contract*, pa je ukupna složenost $O(|E||V| + |V|^2\log|V|)$.

Prema iskustvu s [najkraćim putovima](./shortest-path.md), usko grlo algoritma je pronalaženje vrha s najvećom težinom.

U jednom *contract* treba $|V|$ puta dohvatiti vrh gomile (heap) i $|E|$ puta povećati težinu.

Fibonaccijeva gomila može obaviti dohvat vrha u $O(\log|V|)$ i povećanje težine u $O(1)$, pa teorijska složenost može dosegnuti $O(|E| + |V|\log|V|)$; no zbog velike konstante i količine koda Fibonaccijeve gomile njezina je praktična vrijednost mala.

(U stvarnim testovima treba uključiti O2 i još imati sreće s fluktuacijama ocjenjivača da bi prošlo.)
