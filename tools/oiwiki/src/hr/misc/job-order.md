---
title: Raspoređivanje poslova na jednom stroju
---

Imate $n$ poslova i trebate pronaći redoslijed njihova izvršavanja s najmanjim troškom. Izvršavanje $i$-tog posla traje $t_i$ vremena, a čekanje $i$-tog posla u trajanju $t$ stoji $f_i(t)$.

Formalno: zadano je $n$ funkcija $f_i$ i $n$ brojeva $t_i$; treba pronaći permutaciju $p$ koja minimizira

$$
F(p)=\sum_{i=1}^nf_{p_i}\left(\sum_{j=1}^{i-1}t_{p_j}\right)
$$

## Posebne funkcije troška

### Linearna funkcija troška

Najprije razmotrimo slučaj u kojem su sve funkcije linearne, tj. $f_i(x)=c_ix+d_i$, gdje su $c_i$ nenegativni cijeli brojevi. Očito možemo unaprijed zbrojiti slobodne članove, pa funkcije poprimaju oblik $f_i(x)=c_ix$.

Promotrimo dvije permutacije $p$ i $p'$, gdje je $p'$ permutacija dobivena iz $p$ zamjenom elemenata na položajima $i$ i $i+1$. Tada je

$$
\begin{aligned}
F(p')-F(p)&=c_{p'_i}\sum_{j=1}^{i-1}t_{p'_j}+c_{p'_{i+1}}\sum_{j=1}^{i}t_{p'_j}
-\left(c_{p_i}\sum_{j=1}^{i-1}t_{p_j}+c_{p_{i+1}}\sum_{j=1}^{i}t_{p_j}\right)\\
&=c_{p_i}t_{p_{i+1}}-c_{p_{i+1}}t_{p_i}
\end{aligned}
$$

Dakle, dovoljno je sortirati strategijom „zamijeni ako je $c_{p_i}t_{p_{i+1}}-c_{p_{i+1}}t_{p_i}<0$”. Zapišemo li to u obliku $\dfrac{c_{p_i}}{t_{p_i}}<\dfrac{c_{p_{i+1}}}{t_{p_{i+1}}}$, možemo to shvatiti kao sortiranje permutacije silazno po $\dfrac{c_i}{t_i}$.

Pri rješavanju ovog problema ideja nam je promotriti što se mijenja nakon male perturbacije i pohlepno odabrati optimalno rješenje.

### Eksponencijalna funkcija troška

Razmotrimo funkciju troška oblika $f_i(x)=c_i\mathrm{e}^{ax}$, gdje je $c_i\ge 0,a>0$.

Slijedimo prethodnu ideju i promatramo promjenu troška izazvanu zamjenom elemenata na položajima $i$ i $i+1$. Konačni algoritam jest sortiranje permutacije uzlazno po $\dfrac{1-\mathrm{e}^{at_i}}{c_i}$.

### Jednaka monotono rastuća funkcija

Razmotrimo slučaj u kojem su sve $f_i(x)$ ista monotono rastuća funkcija. Tada očito samo trebamo sortirati permutaciju uzlazno po $t_i$.

## Livshits–Kladovljev teorem

Livshits–Kladovljev teorem vrijedi ako i samo ako je funkcija troška jedan od sljedećih triju slučajeva:

-   linearna funkcija: $f_i(t) = c_it + d_i$, gdje je $c_i\ge 0$;
-   eksponencijalna funkcija: $f_i(t) = c_i \mathrm{e}^{a t} + d_i$, gdje je $c_i,a>0$;
-   jednaka monotono rastuća funkcija: $f_i(t) = \phi(t)$, gdje je $\phi(t)$ monotono rastuća funkcija.

Teorem je dokazan uz pretpostavku da je funkcija troška dovoljno glatka (postoji treća derivacija). U ta tri slučaja optimalno se rješenje problema može pronaći jednostavnim sortiranjem u vremenu $O(n\log n)$.

**Ova je stranica uglavnom prevedena iz članka [Задача Джонсона с одним станком](http://e-maxx.ru/algo/johnson_problem_1) i njegova engleskog prijevoda [Scheduling jobs on one machine](https://cp-algorithms.com/schedules/schedule_one_machine.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.**
