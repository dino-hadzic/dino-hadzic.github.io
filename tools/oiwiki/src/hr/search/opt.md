---
title: Optimizacije
---

## Predgovor

DFS (pretraživanje u dubinu) čest je algoritam i većina se zadataka može riješiti DFS-om, ali u većini slučajeva to je samo algoritam za „hvatanje djelomičnih bodova”; rijetko je čisto brute-force pretraživanje službeno rješenje, jer je vremenska složenost DFS-a vrlo velika. (Tko još nije učio DFS, neka to najprije nadoknadi.)

Ako već ne može biti potpuno rješenje, pokušajmo barem osvojiti više bodova. Ovaj članak predstavlja nekoliko praktičnih optimizacijskih tehnika (poznatih kao „odsijecanje”, pruning).

Najprije predložak za pretraživanje u dubinu; kasniji predlošci bit će njegove izmjene.

```cpp
int ans = najgori slučaj, now;  // now je trenutno rješenje

void dfs(ulazne vrijednosti) {
  if (stigli smo do cilja) ans = bolje od trenutnog i dosadašnjeg rješenja;
  for (prođi sve mogućnosti)
    if (moguće) {
      izvedi operaciju;
      dfs(smanjeni problem);
      poništi operaciju;
    }
}
```

Pritom `ans` može biti i zapis rješenja; tada „bolje od trenutnog i dosadašnjeg rješenja” postaje ispis rješenja.

## Metode odsijecanja

Tri su najčešće vrste odsijecanja: memoizirano pretraživanje, odsijecanje po optimalnosti i odsijecanje po izvedivosti.

### Memoizirano pretraživanje

Budući da pri pretraživanju iste ulazne vrijednosti često daju isto rješenje, možemo ih pamtiti u nizu; detalje vidi u [memoizirano pretraživanje](../dp/memo.md).

**Predložak:**

```cpp
int g[MAXN];  // niz za memoizaciju
int ans = najgori slučaj, now;

void dfs f(ulazne vrijednosti) {
  if (g[veličina] != nevažeća vrijednost) return;  // ili zapamti rješenje, ovisno o situaciji
  if (stigli smo do cilja) ans = bolje od trenutnog i dosadašnjeg rješenja;  // ispiši rješenje, ovisno o situaciji
  for (prođi sve mogućnosti)
    if (moguće) {
      izvedi operaciju;
      dfs(smanjeni problem);
      poništi operaciju;
    }
}

int main() {
  // ...
  memset(g, nevažeća vrijednost, sizeof(g));  // inicijaliziraj niz za memoizaciju
  // ...
}
```

### Odsijecanje po optimalnosti

Još jedan uzrok sporosti pretraživanja jest to što nastavljamo pretraživati i kad je trenutno rješenje već lošije od dosadašnjeg. Dovoljno je, dakle, provjeriti je li trenutno rješenje već lošije od dosadašnjeg.

**Predložak:**

```cpp
int ans = najgori slučaj, now;

void dfs(ulazne vrijednosti) {
  if (now je lošije od ans) return;
  if (stigli smo do cilja) ans = bolje od trenutnog i dosadašnjeg rješenja;
  for (prođi sve mogućnosti)
    if (moguće) {
      izvedi operaciju;
      dfs(smanjeni problem);
      poništi operaciju;
    }
}
```

### Odsijecanje po izvedivosti

I nastavljanje pretraživanja kad trenutno rješenje više nije upotrebljivo uzrok je sporosti.

**Predložak:**

```cpp
int ans = najgori slučaj, now;

void dfs(ulazne vrijednosti) {
  if (trenutno rješenje više nije upotrebljivo) return;
  if (stigli smo do cilja) ans = bolje od trenutnog i dosadašnjeg rješenja;
  for (prođi sve mogućnosti)
    if (moguće) {
      izvedi operaciju;
      dfs(smanjeni problem);
      poništi operaciju;
    }
}
```

## Ideje za odsijecanje

Ideja za odsijecanje ima mnogo i većinu treba analizirati za konkretan problem; ovdje kratko predstavljamo nekoliko uobičajenih.

-   Metoda ekstrema: razmotri ekstremni slučaj; ako ni najekstremniji (najidealniji) slučaj ne zadovoljava uvjete, rezultat stvarnog pretraživanja sigurno neće biti bolji.

-   Metoda prilagodbe: usporedbom podstabala odsijeci ponovljena podstabla i podstabla koja očito nisu najviše „perspektivna”.

-   Matematičke metode: npr. u teoriji grafova pomoću komponenata povezanosti, u teoriji brojeva analizom modularnih jednadžbi, procjenom donje granice pomoću nejednakosti itd.

## Primjer

???+ note "Problem raspodjele poslova"
    Treba raspodijeliti $n$ ($1 \leq n \leq  15$) poslova među $n$ osoba tako da svaka obavi po jedan. Vrijeme koje $i$-ta osoba treba za $k$-ti posao pozitivan je cijeli broj $t_{i,k}$ ($1 \leq t_{i,k} \leq 10^4$), gdje je $1 \leq i, k \leq n$. Odredite raspodjelu kojom je ukupno vrijeme obavljanja tih $n$ poslova najmanje.

Budući da svaka osoba mora dobiti posao, možemo napraviti dvodimenzionalni niz `time[i][j]` koji označava vrijeme koje osoba $i$ treba za posao $j$. Petljom raspodjeljujemo poslove počevši od prve osobe dok ih sve ne dobiju. Pri dodjeljivanju posla $i$-toj osobi u petlji provjeravamo je li svaki posao već dodijeljen; ako nije, dodijelimo ga osobi $i$, a inače provjerimo sljedeći posao. Jednodimenzionalnim nizom `is_working[j]` označavamo je li posao $j$ već dodijeljen: ako nije, `is_working[j]=0`, inače `is_working[j]=1`. Po ideji backtrackinga, nakon završetka petlje po radnicima vraćamo se na prethodnog radnika, poništavamo dodijeljeni posao i dodjeljujemo sljedeći, dok dodjela ne uspije. Tako, vraćajući se sve do prvog radnika, dobivamo sva moguća rješenja.

Provjera raspodjele poslova zapravo je provjera da pri dobivanju mogućeg rješenja indeksi prve dimenzije dvodimenzionalnog niza budu međusobno različiti i indeksi druge dimenzije međusobno različiti. Mi pak tražimo najmanji ukupni zbroj vremena za $n$ poslova, tj. moguće rješenje s najmanjim zbrojem vremena, pa definiramo još jednu globalnu varijablu `cost_time_total_min` koja označava najmanji dosad pronađeni zbroj vremena; početno je `cost_time_total_min` zbroj `time[i][i]`, tj. zbroj vremena na dijagonali. Kad su svima dodijeljeni poslovi, usporedimo `count` i `cost_time_total_min`: ako je `count` manji od `cost_time_total_min`, pronašli smo bolje rješenje i `count` dodijelimo u `cost_time_total_min`.

Radi učinkovitosti algoritma ovdje se može napraviti još jedno odsijecanje. Pri svakom računanju djelomičnog troška `count`, ako utvrdimo da je `count` već veći od `cost_time_total_min`, nema smisla nastavljati raspodjelu, jer tako dobiveno rješenje sigurno nije optimalno.

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/search/code/opt/opt_1.cpp"
    ```
