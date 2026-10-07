---
title: Lyndonova faktorizacija
---

author: sshwy, StudyingFather, orzAtalod

## Definicija

Najprije uvodimo pojam Lyndonove faktorizacije.

Lyndonov string: za string $s$, ako je $s$ leksikografski strogo manji od svih sufiksa stringa $s$, zovemo $s$ jednostavnim stringom ili **Lyndonovim stringom**. Primjerice, `a`, `b`, `ab`, `aab`, `abb`, `ababb` i `abcd` Lyndonovi su stringovi. Ako i samo ako je $s$ leksikografski strogo manji od svih svojih netrivijalnih cikličkih pomaka (netrivijalan znači neprazan i različit od samog stringa), $s$ je Lyndonov string.

Lyndonova faktorizacija: Lyndonovu faktorizaciju stringa $s$ zapisujemo kao $s=w_1w_2\cdots w_k$, pri čemu su svi $w_i$ jednostavni stringovi poredani leksikografski nerastuće, odnosno $w_1\ge w_2\ge\cdots\ge w_k$. Takva faktorizacija postoji i jedinstvena je.

## Duvalov algoritam

### Objašnjenje

Duvalov algoritam pronalazi Lyndonovu faktorizaciju stringa u vremenu $O(n)$.

Najprije uvodimo još jedan pojam: ako string $t$ možemo zapisati u obliku $t=ww\cdots\overline{w}$, gdje je $w$ Lyndonov string, a $\overline{w}$ prefiks stringa $w$ ($\overline{w}$ može biti i prazan), tada $t$ zovemo približno jednostavnim stringom (pre-simple), odnosno približno Lyndonovim stringom. Svaki Lyndonov string ujedno je i približno Lyndonov.

Duvalov algoritam koristi greedy pristup. Tijekom algoritma string $s$ dijelimo na tri dijela $s=s_1s_2s_3$: $s_1$ je Lyndonov string čija je Lyndonova faktorizacija već zabilježena; $s_2$ je približno Lyndonov string; $s_3$ je još neobrađeni dio.

### Postupak

Ukratko, algoritam svaki put pokušava dodati prvi znak stringa $s_3$ na kraj stringa $s_2$. Ako $s_2$ više nije približno Lyndonov string, možemo odrezati dio prefiksa stringa $s_2$ (Lyndonove faktore) i dodati ga na kraj stringa $s_1$.

Detaljnije opišimo postupak. Definiramo pokazivač $i$ na prvi znak stringa $s_2$; $i$ prolazi od $1$ do $n$ (duljine stringa). Unutar petlje definiramo pokazivač $j$ na prvi znak stringa $s_3$ i pokazivač $k$ na znak koji trenutačno promatramo u $s_2$ (znak koji odgovara poziciji $j$ u prethodnom ponavljanju u $s_2$). Želimo dodati $s[j]$ na kraj stringa $s_2$, pa uspoređujemo $s[j]$ i $s[k]$:

1.  Ako je $s[j]=s[k]$, dodavanje znaka $s[j]$ na kraj stringa $s_2$ čuva približnu jednostavnost. Dovoljno je povećati pokazivače $j,k$ (pomaknuti ih na sljedeću poziciju).
2.  Ako je $s[j]>s[k]$, tada $s_2s[j]$ postaje Lyndonov string. Povećamo $j$, a $k$ postavimo na prvi znak stringa $s_2$, pa $s_2$ postaje novi Lyndonov string s jednim ponavljanjem.
3.  Ako je $s[j]<s[k]$, tada $s_2s[j]$ nije približno jednostavan string. Iz $s_2$ moramo izdvojiti Lyndonov podstring duljine $j-k$, odnosno jedno ponavljanje. Zatim $s_2$ zamijenimo preostalim dijelom i nastavimo petlju (u ovom slučaju ne mijenjamo pokazivače $j,k$), sve dok ne odrežemo sva potpuna ponavljanja. Za ostatak se samo „vratimo” na njegov početak.

### Implementacija

Sljedeći kôd vraća Lyndonovu faktorizaciju stringa $s$.

=== "C++"
    ```cpp
    // duval_algorithm
    vector<string> duval(string const& s) {
      int n = s.size(), i = 0;
      vector<string> factorization;
      while (i < n) {
        int j = i + 1, k = i;
        while (j < n && s[k] <= s[j]) {
          if (s[k] < s[j])
            k = i;
          else
            k++;
          j++;
        }
        while (i <= k) {
          factorization.push_back(s.substr(i, j - k));
          i += j - k;
        }
      }
      return factorization;
    }
    ```

=== "Python"
    ```python
    # duval_algorithm
    def duval(s):
        n, i = len(s), 0
        factorization = []
        while i < n:
            j, k = i + 1, i
            while j < n and s[k] <= s[j]:
                if s[k] < s[j]:
                    k = i
                else:
                    k += 1
                j += 1
            while i <= k:
                factorization.append(s[i : i + j - k])
                i += j - k
        return factorization
    ```

### Analiza složenosti

Dokažimo sada složenost ovog algoritma.

Vanjska petlja izvrši se najviše $n$ puta jer se $i$ svaki put povećava. Druga unutarnja petlja također traje $O(n)$ jer samo bilježi Lyndonovu faktorizaciju. Promotrimo sada prvu unutarnju petlju. Svaki Lyndonov string pronađen u jednoj iteraciji vanjske petlje dulji je od preostalog stringa koji smo uspoređivali, pa je zbroj duljina tih ostataka manji od $n$. Zato unutarnja petlja ukupno ima najviše $O(n)$ iteracija. Zapravo, ukupan broj iteracija nije veći od $4n-3$, a vremenska složenost jest $O(n)$.

## Minimalna reprezentacija (pronalaženje najmanjeg cikličkog pomaka)

Za duljinu $n$ i string $s$ te duljine prethodnim algoritmom možemo pronaći njegovu minimalnu reprezentaciju.

Konstruiramo Lyndonovu faktorizaciju stringa $ss$, a zatim u njoj pronađemo Lyndonov string $t$ kojem je početna pozicija manja od $n$, a završna barem $n$. Svojstvima Lyndonove faktorizacije lako se dokazuje da je prvi znak podstringa $t$ ujedno prvi znak minimalne reprezentacije stringa $s$. Drugim riječima, od početka stringa $t$ uzmemo $n$ znakova, što čini minimalnu reprezentaciju stringa $s$.

Zato je tijekom faktorizacije dovoljno bilježiti početak svakog približno Lyndonova stringa.

=== "C++"
    ```cpp
    // smallest_cyclic_string
    string min_cyclic_string(string s) {
      s += s;
      int n = s.size();
      int i = 0, ans = 0;
      while (i < n / 2) {
        ans = i;
        int j = i + 1, k = i;
        while (j < n && s[k] <= s[j]) {
          if (s[k] < s[j])
            k = i;
          else
            k++;
          j++;
        }
        while (i <= k) i += j - k;
      }
      return s.substr(ans, n / 2);
    }
    ```

=== "Python"
    ```python
    # smallest_cyclic_string
    def min_cyclic_string(s):
        s += s
        n = len(s)
        i, ans = 0, 0
        while i < n / 2:
            ans = i
            j, k = i + 1, i
            while j < n and s[k] <= s[j]:
                if s[k] < s[j]:
                    k = i
                else:
                    k += 1
                j += 1
            while i <= k:
                i += j - k
        return s[ans : ans + n / 2]
    ```

## Zadaci

-   [UVa #719 - Glass Beads](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=660)

    **Ova je stranica uglavnom prevedena iz objave [Декомпозиция Линдона. Алгоритм Дюваля. Нахождение наименьшего циклического сдвига](http://e-maxx.ru/algo/duval_algorithm) i njezina engleskog prijevoda [Lyndon factorization](https://cp-algorithms.com/string/lyndon_factorization.html). Ruska inačica ima licencu Public Domain + Leave a Link, a engleska CC-BY-SA 4.0.**
