---
title: Greedy algoritmi
---

Ova stranica kratko predstavlja greedy (pohlepne) algoritme.

## Uvod

**Greedy algoritam** (pohlepni algoritam) računalom simulira kako „pohlepna” osoba donosi odluke. Ta je osoba vrlo pohlepna: u svakom koraku bira operaciju koja je prema nekom kriteriju najbolja. Uz to je i kratkovidna: gleda samo ono što je pred njom i ne razmišlja o posljedicama koje bi kasnije mogle nastati.

Jasno je da greedy pristup ne daje uvijek optimalno rješenje, pa pri njegovoj upotrebi u pravilu treba znati dokazati njegovu ispravnost.

## Objašnjenje

### Područje primjene

Greedy algoritmi osobito su učinkoviti u problemima s optimalnom podstrukturom. Optimalna podstruktura znači da se problem može rastaviti na potprobleme, a optimalna rješenja potproblema vode do optimalnog rješenja cijelog problema.[^ref1]

### Dokaz

Uobičajene tehnike dokaza su argument zamjene i matematička indukcija; mogu se i kombinirati.

1.  Argument zamjene (exchange argument): krenemo od proizvoljnog optimalnog rješenja i konačnim brojem zamjena koje čuvaju dopustivost i ne pogoršavaju vrijednost cilja pretvorimo ga u rješenje koje daje greedy algoritam, čime pokazujemo da je i greedy rješenje optimalno. Dokaz se često piše kao dokaz kontradikcijom.
2.  Indukcija: najprije izračunamo optimalno rješenje $F_1$ graničnog slučaja (npr. $n = 1$), a zatim dokažemo da se za svaki $n$ rješenje $F_{n+1}$ može izvesti iz $F_{n}$.

## Ključne točke

### Česti tipovi zadataka

U zadacima do razine „提高组” (NOIP senior) najčešće su dvije vrste greedy pristupa.

-   Sortiraj XXX po nekom redoslijedu, a zatim biraj u nekom redoslijedu (npr. od najmanjeg prema najvećem).
-   Svaki put uzmi najveći/najmanji element iz XXX i ažuriraj XXX. (Ponekad se uzimanje maksimuma/minimuma može ubrzati, npr. prioritetnim redom.)

Razlika je u tome što je prvi pristup uvijek offline – prvo se obradi, pa bira; drugi može biti online – treba birati tijekom obrade.

### Rješavanje sortiranjem

Metoda sortiranja / zamjene susjednih elemenata obično se javlja kad je ulaz niz s nekoliko (najčešće jedne ili dvije) težine, a optimum se dobiva sortiranjem pa simuliranim prolazom.

???+ note "Primjer [NOIP 2012 Kraljeva igra](https://www.luogu.com.cn/problem/P1080)"
    Za Dan državnosti zemlje H kralj poziva $n$ ministara da igraju igru s nagradama. Najprije svaki ministar na lijevu i desnu ruku napiše po jedan cijeli broj, a i kralj na svaku ruku napiše po jedan cijeli broj. Zatim se $n$ ministara postavi u red, a kralj stoji na čelu reda. Nakon postavljanja svaki ministar dobiva od kralja nagradu u zlatnicima: umnožak brojeva na lijevim rukama svih osoba ispred njega podijeljen brojem na njegovoj desnoj ruci, zaokružen prema dolje.
    
    Kralj ne želi da neki ministar dobije posebno veliku nagradu, pa te moli da preurediš redoslijed u redu tako da ministar s najvećom nagradom dobije što manje. Kralj je uvijek na čelu reda.

??? note "Ideja rješenja"
    Neka $i$-ti ministar u trenutnom poretku ima na lijevoj i desnoj ruci brojeve $a_i, b_i$. Greedy strategiju izvodimo metodom zamjene susjednih elemenata.
    
    Zanemarimo najprije zaokruživanje i označimo sa $s$ umnožak $a_i$ svih osoba ispred $i$-tog ministra. Prije zamjene najveća nagrada među tim dvama ministrima je
    
    $$
    \dfrac{s}{b_i b_{i+1}}\max(b_{i+1},a_i b_i),\tag{1}
    $$
    
    a nakon zamjene
    
    $$
    \dfrac{s}{b_i b_{i+1}}\max(b_i,a_{i+1}b_{i+1}).\tag{2}
    $$
    
    Ako je $a_i b_i\le a_{i+1}b_{i+1}$, zbog $b_{i+1}\le a_{i+1}b_{i+1}$ izraz $(1)$ nije veći od izraza $(2)$. Zaokruživanje prema dolje je monotono i vrijedi $\max(\lfloor u\rfloor,\lfloor v\rfloor)=\lfloor\max(u,v)\rfloor$, pa se zamjenom redoslijeda tih dvoje najveća nagrada ne smanjuje. Stoga je optimalno sortirati uzlazno po $a_i b_i$.
    
    U implementaciji dva ulazna broja spremamo u strukturu i preopterećujemo operator:
    
    ```cpp
    struct uv {
      int a, b;
    
      bool operator<(const uv& x) const { return 1LL * a * b < 1LL * x.a * x.b; }
    };
    ```

### Rješavanje „žaljenjem”

Ideja: novu opciju privremeno prihvatimo; ako dođe do sukoba s ograničenjima, iz već odabranog skupa poništimo opciju koja je prema greedy kriteriju najlošija. I za ovu strategiju treba dokazati ispravnost.

???+ note "Primjer [„USACO09OPEN” Work Scheduling](https://www.luogu.com.cn/problem/P2949)"
    Johnov radni dan počinje u trenutku $0$ i traje $10^9$ jedinica vremena. U svakoj jedinici vremena može odraditi bilo koji od $N(1 \leq N \leq 10^5)$ poslova označenih brojevima $1$ do $N$. Posao $i$ ima rok $D_i(1 \leq D_i \leq 10^9)$ i donosi zaradu $P_i( 1\leq P_i\leq 10^9 )$. Uz zadane zarade i rokove, odredi najveću zaradu koju John može ostvariti.

??? note "Ideja rješenja"
    1.  Pretpostavimo najprije da radimo svaki posao; poslove sortiramo po roku i stavljamo u red;
    2.  pri odluci radimo li `i`-ti posao, ako mu rok dopušta, usporedimo ga s elementom u redu koji ima najmanju zaradu; ako `i`-ti posao donosi više (žaljenje), tada `ans += a[i].p - q.top()`.  
        Prioritetnim redom (min-hrpom) održavamo minimum na vrhu.
    3.  Uvjet `a[i].d<=q.size()` tumačimo ovako: u razdoblju od 0 do `a[i].d` može se odraditi najviše `a[i].d` poslova; ako je `q.size()>=a[i].d`, vrijeme potrebno za `q.size()` poslova veće je ili jednako `a[i].d`, pa kad `i`-ti posao donosi veću zaradu, najmanji posao treba izbaciti iz prioritetnog reda.

??? note "Primjer rješenja"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/greedy/greedy_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/greedy/greedy_1.py"
        ```

??? note "Analiza složenosti"
    -   Prostorna složenost: za $n$ poslova koristimo $n$ elemenata niza $a$, a prioritetni red u najgorem slučaju sadrži $n$ elemenata, pa je prostorna složenost $O(n)$.
    -   Vremenska složenost: `std::sort` ima složenost $O(n\log n)$, održavanje prioritetnog reda također $O(n\log n)$; ukupno $O(n\log n)$.

## Razlika prema dinamičkom programiranju

Uobičajeni greedy oslanja se na lokalne izbore za koje se može dokazati da su sigurni; dinamičko programiranje održava optimalnu vrijednost svakog stanja i uspoređuje moguće prijelaze.

## Zadaci za vježbu

-   [„USACO1.3” Barn Repair](https://www.luogu.com.cn/problem/P1209)
-   [Luogu P2123 Kraljičina igra](https://www.luogu.com.cn/problem/P2123)
-   [Zadaci s oznakom „greedy” na LeetCodeu](https://leetcode-cn.com/tag/greedy/)

## Literatura i bilješke

[^ref1]: [Greedy algorithm – Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)
