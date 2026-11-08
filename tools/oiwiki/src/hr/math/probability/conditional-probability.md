---
title: Uvjetna vjerojatnost i nezavisnost
---

## Uvod

Kad se neki događaj već dogodio, vjerojatnosti nekih slučajnih događaja mijenjaju se zbog povećanja poznatih informacija. Primjerice, pri izvlačenju karata u mobilnoj igri (gacha) možda smatramo da su dobivanje šestozvjezdane karte i njezino nedobivanje u jednom izvlačenju jednako vjerojatni, ali nakon što u $50$ uzastopnih izvlačenja nismo dobili nijednu šestozvjezdanu kartu, tvrdoglavo ustrajati na tome da su „dobivanje i nedobivanje šestozvjezdane karte jednako vjerojatni” više ne izgleda tako pametno.

Ukratko, nužno je proučavati vjerojatnost događaja uz neke poznate uvjete.

## Uvjetna vjerojatnost

### Definicija

Ako je poznato da se događaj $A$ dogodio, vjerojatnost da se uz taj uvjet dogodi događaj $B$ naziva se **uvjetnom vjerojatnošću** i označava $P(B|A)$.

U vjerojatnosnom prostoru $(\Omega, \mathcal{F}, P)$, ako događaj $A \in \mathcal{F}$ zadovoljava $P(A) > 0$, uvjetna vjerojatnost $P(\cdot|A)$ definira se kao

$$
P(B|A) = \frac{P(AB)}{P(A)} \quad \forall B \in \mathcal{F}
$$

Može se provjeriti da je $P(\cdot|A)$ definirana gornjom formulom funkcija vjerojatnosti na $(\Omega, \mathcal{F})$.

Iz definicije uvjetne vjerojatnosti izravno slijede sljedeće dvije jednakosti:

-   **formula množenja vjerojatnosti**: u vjerojatnosnom prostoru $(\Omega, \mathcal{F}, P)$, ako je $P(A) > 0$, onda za svaki događaj $B$ vrijedi

$$
P(AB) = P(A)P(B|A)
$$

-   **formula potpune vjerojatnosti**: u vjerojatnosnom prostoru $(\Omega, \mathcal{F}, P)$, ako su događaji $A_1, \cdots, A_n$ u parovima disjunktni i njihova je unija $\Omega$, onda za svaki događaj $B$ vrijedi

$$
P(B) = \sum_{i=1}^{n} P(A_i)P(B|A_i)
$$

### Bayesova formula

Općenito, neka su mogući uzroci događaja $B$ događaji $A_1, A_2, \cdots, A_n$; tada se, kad su poznati $P(A_i)$ i $P(B|A_i)$, vjerojatnost događaja $B$ može izračunati formulom potpune vjerojatnosti. No u mnogim slučajevima iz rezultata „događaj $B$ se dogodio” trebamo unatrag zaključiti vjerojatnosti pojedinih događaja-uzroka. Tako dobivamo

$$
P(A_i|B) = \frac{P(A_iB)}{P(B)} = \frac{P(A_i)P(B|A_i)}{\sum_{j=1}^{n} P(A_j)P(B|A_j)}
$$

Gornja je formula Bayesova formula.

## Nezavisnost događaja

Pri proučavanju uvjetne vjerojatnosti može se pojaviti slučaj $P(B|A) = P(B)$. Intuitivno, to znači da nam to je li se događaj $B$ dogodio ne daje nikakvu informaciju o događaju $A$, tj. događaj $B$ „nije povezan” s događajem $A$. Tako dolazimo do sljedeće definicije.

### Definicija

Ako događaji $A$,$B$ istog vjerojatnosnog prostora zadovoljavaju

$$
P(AB) = P(A)P(B)
$$

kažemo da su $A$,$B$ **nezavisni**. Za više događaja $A_1, A_2, \cdots, A_n$ kažemo da su nezavisni ako i samo ako za svaki izbor događaja $\{ A_{i_k} : 1 \leq i_1 < i_2 < \cdots < i_k \leq n \}$ vrijedi

$$
P( A_{i_1}A_{i_2} \cdots A_{i_r} ) = \prod_{k=1}^{r} P(A_{i_k})
$$

### Nezavisnost više događaja

Za više događaja općenito se iz nezavisnosti u parovima ne može zaključiti da su ti događaji nezavisni. Promotrimo sljedeći protuprimjer:

Imamo pravilnu tetraedarsku kockicu kojoj su tri strane obojene redom crveno, zeleno i plavo, a četvrta strana ima sve tri boje. Bacimo tu kockicu jednom i neka događaji $A$,$B$,$C$ redom označavaju da strana koja dodiruje stol sadrži crvenu, zelenu odnosno plavu boju.

Lako se izračuna $P(A) = P(B) = P(C) = \frac{1}{2}$, a $P(AB) = P(BC) = P(CA) = P(ABC) = \frac{1}{4}$.

Očito su $A, B, C$ nezavisni u parovima, ali budući da je $P(ABC) \neq P(A)P(B)P(C)$, događaji $A, B, C$ nisu nezavisni.
