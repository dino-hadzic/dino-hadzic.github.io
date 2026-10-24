---
title: Simulirano kaljenje
---

## Uvod

Simulirano kaljenje (simulated annealing) randomizirani je algoritam. Kad je broj mogućih rješenja problema golem (ili čak beskonačan), a funkcija nije unimodalna, često ga rješavamo simuliranim kaljenjem.

## Objašnjenje

Promatrajući tijek [hill climbinga](./hill-climbing.md), uočavamo: neoptimalno rješenje u blizini trenutačnog optimuma hill climbing jednostavno odbacuje. A u mnogim slučajevima moramo prihvatiti to neoptimalno rješenje kako bismo iskočili iz lokalnog optimuma – to je upravo algoritam simuliranog kaljenja.

??? note "Što je kaljenje? (iz [Baidu Baike](https://baike.baidu.com/item/%E9%80%80%E7%81%AB/1039313))"
    Kaljenje (ovdje točnije: žarenje, engl. annealing) postupak je toplinske obrade metala: metal se polagano zagrijava do određene temperature, drži se na njoj dovoljno dugo i zatim hladi prikladnom brzinom. Cilj je smanjiti tvrdoću i poboljšati obradivost rezanjem; ukloniti zaostala naprezanja, stabilizirati dimenzije te smanjiti sklonost deformacijama i pukotinama; usitniti zrna, prilagoditi strukturu i ukloniti strukturne nedostatke. Točnije rečeno, kaljenje je postupak toplinske obrade materijala, i metalnih i nemetalnih. Osim toga, svrha kaljenja novih materijala djelomično se podudara s tradicionalnim kaljenjem metala, a djelomično se od njega razlikuje.

Budući da zakonitosti kaljenja uvode više slučajnih čimbenika, vjerojatnost da dobijemo optimalno rješenje znatno raste. Stoga možemo simulirati taj proces, uzimajući ciljnu funkciju kao funkciju energije.

### Postupak

Jednom rečenicom: ako je rješenje u novom stanju bolje, ažuriramo odgovor, a inače novo stanje prihvaćamo s određenom vjerojatnošću.

Neka je trenutačna temperatura $T$, a razlika energije (vrijednosti) između novog stanja $S'$ i poznatog stanja $S$ (novo se stanje dobiva iz poznatog na slučajan način) neka je $\Delta E$ ($\Delta E\geqslant 0$); tada je vjerojatnost prijelaza stanja (promjene optimalnog rješenja)

$$
P(\Delta E)=
\begin{cases}
1,                              & S' \text{ is better than } S,\\
\mathrm{e}^\frac{-\Delta E}{T}, & \text{otherwise}.
\end{cases}
$$

**Napomena**: ponekad, kako bi dobiveno rješenje bilo kvalitetnije, nakon završetka simuliranog kaljenja pri trenutačnoj temperaturi više puta slučajno biramo stanja u blizini dobivenog rješenja i pokušavamo pronaći bolje (postupak je sličan simuliranom kaljenju).

### Kako kaliti (hladiti)

Pri simuliranom kaljenju imamo tri parametra: početnu temperaturu $T_0$, koeficijent hlađenja $d$ i završnu temperaturu $T_k$. Pri tome je $T_0$ razmjerno velik broj, $d$ je broj vrlo blizu $1$, ali manji od $1$, a $T_k$ je pozitivan broj blizu $0$.

Najprije postavimo temperaturu $T=T_0$, zatim prema gornjim koracima napravimo jedan pokušaj prijelaza, pa postavimo $T=d\cdot T$. Kad je $T<T_k$, proces simuliranog kaljenja završava, a trenutačno optimalno rješenje konačno je optimalno rješenje.

Napomena: kako bi rješenje bilo točnije, obično za odgovor ne uzimamo izravno trenutačno rješenje, nego tijekom kaljenja održavamo najbolju vrijednost među svim rješenjima na koja smo naišli.

Navodimo sliku sa stranice [Simulated annealing - Wikipedia](https://en.wikipedia.org/wiki/Simulated_annealing) (sa snižavanjem temperature skokovi su sve manje slučajni, a optimalno je rješenje sve stabilnije).

![](./images/simulated-annealing.gif)

## Implementacija

Kôd ovdje za primjer uzima zadatak [「BZOJ 3680」吊打 XXX (Premlatiti XXX-a)](https://hydro.ac/p/bzoj-P3680) (traži se težinska Fermatova točka za $n$ točaka).

```cpp
--8<-- "docs/misc/code/simulated-annealing/simulated-annealing_1.cpp"
```

## Neki trikovi

### Simulirano kaljenje po blokovima

Ponekad funkcija ima mnogo vrhova i simulirano kaljenje teško dolazi do optimalnog rješenja.

Tada cijelu domenu možemo podijeliti na nekoliko dijelova, na svakom pokrenuti simulirano kaljenje, a zatim uzeti najbolje rješenje.

### Iskorištavanje vremenskog ograničenja

Postoji funkcija `clock()` koja vraća vrijeme izvođenja programa.

U glavnom programu `simulateAnneal();` možemo zamijeniti s `while ((double)clock()/CLOCKS_PER_SEC < MAX_TIME) simulateAnneal();`. Tako će se simulirano kaljenje izvoditi sve dok se utrošeno vrijeme ne približi vremenskom ograničenju.

Ovdje je `MAX_TIME` proizvoljno odabran broj malo manji od vremenskog ograničenja (u sekundama).

## Zadaci za vježbu

-   [「BZOJ 3680」吊打 XXX (Premlatiti XXX-a)](https://hydro.ac/p/bzoj-P3680)
-   [「JSOI 2016」炸弹攻击 (Bombaški napad)](https://loj.ac/problem/2076)
-   [「HAOI 2006」均分数据 (Ravnomjerna podjela podataka)](https://www.luogu.com.cn/problem/P2503)
