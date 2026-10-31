---
title: Presjek poluravnina
---

## Definicija

### Poluravnina

Pravac i jedna njegova strana. Poluravnina je skup točaka, dakle skup točaka koji čine pravac i jedna njegova strana. Ako sadrži sam pravac, zove se zatvorena poluravnina; ako ga ne sadrži, zove se otvorena poluravnina.

Analitički se obično zapisuje kao $Ax+By+C\ge 0$.

U računalnoj geometriji prikazuje se vektorom; u cijelom se zadatku za poluravninu dosljedno uzima lijeva ili desna strana vektora.

![Poluravnina](./images/hpi1.svg)

### Presjek poluravnina

Presjek poluravnina je presjek više poluravnina. Budući da su poluravnine skupovi točaka, njihov je presjek također skup točaka. U pravokutnom koordinatnom sustavu on omeđuje neko područje.

To jako nalikuje običnom problemu linearnog programiranja: dobiveni presjek poluravnina upravo je dopustivo područje iz linearnog programiranja. U pravilu je presjek poluravnina ograničen, a često se ispituje rješavanje problema poput računanja površine.

Možemo ga shvatiti kao presjek desnih strana svih vektora iz skupa vektora ili kao rješenje sljedećeg sustava nejednadžbi.

$$
\begin{cases}
A_1x+B_1y+C\ge 0\\
A_2x+B_2y+C\ge 0\\
\cdots
\end{cases}
$$

### Jezgra mnogokuta

Ako spojnica bilo koje točke nekog skupa točaka s bilo kojom točkom mnogokuta nema drugih sjecišta s mnogokutom, taj se skup točaka zove jezgra mnogokuta.

Promatramo li svaku stranicu mnogokuta kao vektor, tako da se vektori nadovezuju jedan na drugi, presjek poluravnina tih vektora usmjerenih prema unutrašnjosti mnogokuta upravo je jezgra mnogokuta.

## Rješenje – algoritam S&I

### Sortiranje po polarnom kutu

Jezik C ima bibliotečnu funkciju `atan2(double y,double x)` koja vraća $\theta\in (-\pi,\pi]$, $\theta =\arctan \frac{y}{x}$.

Pozovemo tu funkciju izravno s vektorom kao argumentom i sortiramo po povratnoj vrijednosti kao ključu; tako dobivamo novi skup bridova (vektora).

Ako pri sortiranju naiđemo na kolinearne vektore (istog smjera), uzimamo onaj bliži dopustivom području. Na primjer, ako dva vektora imaju jednak polarni kut, a tražimo lijevu poluravninu vektora, dovoljno je zadržati lijevi vektor. Provjerava se tako da se početak ili kraj jednog vektora usporedi s drugim vektorom i utvrdi je li s njegove lijeve ili desne strane.

### Održavanje monotonog reda

Budući da je presjek poluravnina konveksan mnogokut, treba održavati konveksnu ljusku. Kako kasnije dodani vektori mogu utjecati samo na prve ili na posljednje dodane bridove (ljuska je tada povezana), dovoljno je brisati elemente s početka i s kraja reda, pa koristimo monotoni red (monotonic queue).

Prolazimo kroz sortirane vektore i održavamo još jedno polje sjecišta. Čim red sadrži više od 2 elementa, među njima nastaju sjecišta.

Ako se za trenutačni vektor prethodno sjecište nalazi na **suprotnoj strani** od poluravnine koju taj vektor predstavlja, prethodni brid više nema smisla.

![Monotoni red](./images/hpi2.svg)

Kao na gornjoj slici, pretpostavimo da uzimamo lijevu poluravninu vektora. Nakon sortiranja po polarnom kutu redoslijed obilaska trebao bi biti $\vec a\to\vec b\to\vec c$. Kad $\vec a$ i $\vec b$ uđu u red, u polju sjecišta nastaje točka $D$ (polje sjecišta na istom indeksu čuva sjecište vektora iz reda s prethodnim vektorom).

Kad zatim dođemo do $\vec c$, ustanovimo da je $D$ s desne strane vektora $\vec c$. A budući da **polarni kut vektora koji je proizveo** $D$ **mora biti manji od** polarnog kuta vektora $\vec c$, vektor koji je proizveo $D$ (dakle $\vec b$) više ne utječe na presjek poluravnina.

Postoji još jedna moguća situacija: pred kraj novododani vektor može početi utjecati od početka reda.

![Utjecaj na početak reda](./images/hpi7.svg)

I dalje pretpostavimo da uzimamo lijevu poluravninu vektora. Nakon dodavanja vektora $\vec f$ prvo sjecište $G$ nalazi se s desne strane vektora $\vec f$; primijenimo li gornji kriterij u obrnutom smjeru, vidimo da tada treba izbaciti vektor $\vec a$, dakle vektor s **početka reda**.

Na kraju vektorom s početka reda uklanjamo suvišne vektore s kraja reda. Naime, vektore s početka reda ograničavaju kasniji vektori, a vektore s kraja reda ne. Oni tada zatvaraju prsten, pa vektor s početka reda može ograničiti vektore s kraja reda.

### Dobivanje presjeka poluravnina

Ako je presjek poluravnina konveksan $n$-terokut, na kraju ćemo u polju sjecišta dobiti $n$ točaka. Spojimo li ih redom u zatvoreni lanac, dobivamo $n$-terokut jedinstvene orijentacije (u smjeru kazaljke na satu ili suprotno).

Tada površinu možemo izračunati triangulacijom. (Računanje površine najosnovniji je način na koji se ovo ispituje.)

Povremeno se dogodi da presjek poluravnina ne postoji ili da mu je površina 0; pripazite na rubne slučajeve.

### Napomene

Kad se pojavi vektor koji može izbaciti sve točke iz reda (tj. sve točke u redu nalaze se s njegove desne strane), **moramo** najprije obraditi kraj reda, a tek zatim početak reda. Zato u petlji najprije obrađujemo dio s `--r;`, a zatim dio s `++l;`; samo tako nema pogreške. Razlog je sljedeći.

![](./images/hpi4.svg)

U pravilu, kad na kraj reda (redoslijed u redu je $\left\{\vec{u},\vec{v}\right\}$) dodamo brid (vektor $\vec w$), nastaje sjecište $N$ koje sužava područje iza $\vec{v}$.

![](./images/hpi5.svg)

No svaka je operacija ipak općenita, pa se može dogoditi da točka $M$ bude „istisnuta”.

![](./images/hpi6.svg)

Ako se tada pojavi vektor $\vec a$ takav da je $M$ s desne strane vektora $\vec a$, $M$ mora izaći iz reda. Ako u tom trenutku krenemo od početka reda s `++l`, očito proširujemo područje. Zapravo točku $M$ zajedno određuju $\vec u$ i $\vec v$, pa treba razmotriti utječe li na trenutačni tijek $\vec u$ ili $\vec v$. A budući da su nakon sortiranja po polarnom kutu vektori poredani u smjeru suprotnom od kazaljke na satu, utjecaj $\vec v$ je veći.

Kao na gornjoj slici, ako je $M$ zaista s desne strane vektora $\vec a$, utjecaj $\vec v$ sigurno neće ničim pridonijeti rješenju presjeka poluravnina.

Razlog zbog kojeg uklanjamo početak reda jest da je **ograničenje trenutačnog vektora jače od ograničenja vektora s početka reda**, a preduvjet tog uvjeta jest da red sadrži više od dvije dužine (vektora); inače nastaje gore opisana situacija.

Zato obavezno najprije uklanjamo s kraja reda, a tek onda s početka.

???+ note "Kod – usporedba"
    ```cpp
    friend bool operator<(seg x, seg y) {
      db t1 = atan2((x.b - x.a).y, (x.b - x.a).x);
      db t2 = atan2((y.b - y.a).y, (y.b - y.a).x);  // računanje polarnog kuta
      if (fabs(t1 - t2) > eps)                      // ako polarni kutovi nisu jednaki
        return t1 < t2;
      return (y.a - x.a) * (y.b - x.a) >
             eps;  // provjera s koje je strane vektora y vektor x; najljeviji ide na početak
    }
    ```

???+ note "Kod – inkrementalni dio"
    ```cpp
    // pnt its(seg a,seg b) računa sjecište dužina a i b
    // s[] su vektori sortirani po polarnom kutu
    // q[] je red vektora
    // t[i] je sjecište s[i-1] i s[i]
    // [Stil koda] raspon reda je (l,r]
    // Računa se poluravnina s lijeve strane vektora
    int l = 0, r = 0;
    for (int i = 1; i <= n; ++i)
      if (s[i] != s[i - 1]) {
        // Pazite: najprije treba provjeriti kraj reda
        while (r - l > 1 && (s[i].b - t[r]) * (s[i].a - t[r]) >
                                eps)  // ako je prethodno sjecište desno od vektora, izbaci s kraja reda
          --r;
        while (r - l > 1 && (s[i].b - t[l + 2]) * (s[i].a - t[l + 2]) >
                                eps)  // ako je prvo sjecište desno od vektora, izbaci s početka reda
          ++l;
        q[++r] = s[i];
        if (r - l > 1) t[r] = its(q[r], q[r - 1]);  // računanje novog sjecišta
      }
    while (r - l > 1 &&
           (q[l + 1].b - t[r]) * (q[l + 1].a - t[r]) > eps)  // pazite: brisanje suvišnih elemenata
      --r;
    t[r + 1] = its(q[l + 1], q[r]);  // zatim računamo novo sjecište
    ++r;
    // Pazite: ovdje se ++r ne smije izvesti unutar indeksa t…
    ```

## Zadaci za vježbu

[POJ 2451 Uyuw's Concert](http://poj.org/problem?id=2451) pripazite na rubne slučajeve

[POJ 1279 Art Gallery](http://poj.org/problem?id=1279) traži se jezgra mnogokuta

[「CQOI2006」凸多边形 (Konveksni mnogokut)](https://www.luogu.com.cn/problem/P4196)
