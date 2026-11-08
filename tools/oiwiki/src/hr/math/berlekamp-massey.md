---
title: Berlekamp–Masseyjev algoritam
---

Berlekamp–Masseyjev algoritam je algoritam za nalaženje najkraće linearne rekurzije niza. Za zadani niz duljine $n$, ako je red njegove najkraće rekurzije $m$, Berlekamp–Masseyjev algoritam u vremenu $O(nm)$ pronalazi najkraću rekurziju svakog prefiksa niza. U najgorem slučaju je $m = O(n)$, pa je složenost algoritma u najgorem slučaju $O(n^2)$.

### Definicija

Rekurzijom niza $\{a_0 \dots a_{n - 1} \}$ nazivamo niz $\{r_0\dots r_m\}$ koji zadovoljava

$\sum_{j = 0} ^ m r_j a_{i - j} = 0, \forall i \ge m$

pri čemu je $r_0 = 1$. Broj $m$ nazivamo **redom** te rekurzije.

Najkraća rekurzija niza $\{a_i\}$ je rekurzija najmanjeg reda.

### Postupak

Malo drugačije od gornje definicije, ovdje definiramo nove rekurzivne koeficijente $\{f_0 \dots f_{m - 1}\}$ koji zadovoljavaju:

$a_i = \sum_{j = 0} ^ {m - 1} f_j a_{i - j - 1}, \forall i \ge m$

Lako se vidi da je $f_i = -r_{i + 1}$, a red $m$ isti je kao u prethodnoj definiciji.

Rekurziju možemo tražiti inkrementalno: redom razmatramo članove niza $\{a_i\}$ i, kad rekurzija da pogrešan rezultat, prilagođavamo rekurzivne koeficijente $\{f_i\}$. Radi jednostavnosti, najkraću rekurziju prvih $i$ članova označavat ćemo $F_i = \{f_{i, j}\}$.

Očito je na početku $F_0 = \{\}$. Pretpostavimo da rekurzivni koeficijenti $F_{i - 1}$ vrijede za prvih $i - 1$ članova niza $\{a_i\}$; za $i$-ti član tada postoje dva slučaja:

1.  Rekurzivni koeficijenti vrijede i za $a_i$; tada nije potrebna nikakva prilagodba, jednostavno stavimo $F_i = F_{i - 1}$.
2.  Rekurzivni koeficijenti ne vrijede za $a_i$; tada treba prilagoditi $F_{i - 1}$ i dobiti novi $F_i$.

Neka je $\Delta_i = a_i - \sum_{j = 0} ^ m f_{i - 1, j} a_{i - j - 1}$, tj. razlika između $a_i$ i rezultata rekurzije $F_{i - 1}$.

Ako je ovo prva izmjena rekurzivnih koeficijenata, onda je $a_i$ prvi član niza različit od nule. Tada jednostavno stavimo da je $F_i$ niz od $i$ vrijednosti $0$; očito je to valjana najkraća rekurzija.

Inače, neka je $k$ broj članova niza $\{a_i\}$ koji su bili razmotreni pri posljednjoj izmjeni rekurzivnih koeficijenata. Ako postoji niz $G = \{g_0 \dots g_{m' - 1}\}$ takav da

$\sum_{j = 0} ^ {m' - 1} g_j a_{i' - j - 1} = 0, \forall i' \in [m', i)$

i $\sum_{j = 0} ^ {m' - 1} g_j a_{i - j - 1} = \Delta_i$, onda nije teško uočiti da zbrajanjem $F_k$ i $G$ član po član dobivamo valjane rekurzivne koeficijente $F_i$.

Razmotrimo kako konstruirati $G$. Jedna moguća konstrukcija je

$G = \{0, 0, \dots, 0, \frac{\Delta_i}{\Delta_k}, -\frac{\Delta_i}{\Delta_k}F_{k-1}\}$

gdje je na početku ukupno $i - k - 1$ vrijednosti $0$, a završni $-\frac{\Delta_i}{\Delta_k} F_{k-1}$ označava da se svaki član od $F_{k-1}$ pomnoži s $-\frac{\Delta_i}{\Delta_k}$ i nadoveže na kraj niza.

Lako se provjeri da je tada $\sum_{j = 0} ^ {m' - 1} g_j a_{i - j - 1} = \Delta_k \frac{\Delta_i}{\Delta_k} = \Delta_i$, pa je ovako konstruiran $G$ valjan. Dovoljno je $F_i$ postaviti na zbroj $F_k$ i $G$ član po član.

Ako se traži rekurzija $\{r_i\}$ u skladu s početnom definicijom, dovoljno je svim $\{f_j\}$ promijeniti predznak i na početak umetnuti $r_0 = 1$.

Iz opisanog tijeka algoritma vidi se da je, ako je red najkraće rekurzije niza $m$, složenost algoritma $O(nm)$. U najgorem slučaju je $m = O(n)$, pa je složenost algoritma u najgorem slučaju $O(n^2)$.

Pri implementaciji, budući da se pri svakoj prilagodbi rekurzivnih koeficijenata koriste samo rekurzivni koeficijenti $F_k$ iz prethodne prilagodbe, ako nam je potrebna samo najkraća rekurzija cijelog niza, možemo pamtiti samo trenutačne rekurzivne koeficijente i one iz posljednje prilagodbe, uz prostornu složenost $O(n)$.

??? note "Referentna implementacija"
    ```cpp
    vector<int> berlekamp_massey(const vector<int> &a) {
      vector<int> v, last;  // v is the answer, 0-based, p is the module
      int k = -1, delta = 0;
    
      for (int i = 0; i < (int)a.size(); i++) {
        int tmp = 0;
        for (int j = 0; j < (int)v.size(); j++)
          tmp = (tmp + (long long)a[i - j - 1] * v[j]) % p;
    
        if (a[i] == tmp) continue;
    
        if (k < 0) {
          k = i;
          delta = (a[i] - tmp + p) % p;
          v = vector<int>(i + 1);
    
          continue;
        }
    
        vector<int> u = v;
        int val = (long long)(a[i] - tmp + p) * power(delta, p - 2) % p;
    
        if (v.size() < last.size() + i - k) v.resize(last.size() + i - k);
    
        (v[i - k - 1] += val) %= p;
    
        for (int j = 0; j < (int)last.size(); j++) {
          v[i - k + j] = (v[i - k + j] - (long long)val * last[j]) % p;
          if (v[i - k + j] < 0) v[i - k + j] += p;
        }
    
        if ((int)u.size() - i < (int)last.size() - k) {
          last = u;
          k = i;
          delta = a[i] - tmp;
          if (delta < 0) delta += p;
        }
      }
    
      for (auto &x : v) x = (p - x) % p;
      v.insert(v.begin(), 1);
    
      return v;  // $\forall i, \sum_{j = 0} ^ m a_{i - j} v_j = 0$
    }
    ```

Osnovni Berlekamp–Masseyjev algoritam pronalazi najkraću rekurziju niza s konačno mnogo članova. Ako niz čiju rekurziju tražimo ima beskonačno mnogo članova, ali je poznata gornja međa reda najkraće rekurzije, dovoljno je uzeti prvih $2m$ članova niza da bismo dobili najkraću rekurziju cijelog niza. (Dokaz izostavljen.)

### Primjene

Budući da je Berlekamp–Masseyjev algoritam numerički prilično nestabilan, rijetko se koristi za probleme s realnim brojevima. Radi jednostavnosti izlaganja, u nastavku pretpostavljamo da se računa u sustavu ostataka modulo neki prost broj $p$.

#### Najkraća rekurzija niza vektora ili niza matrica

Ako tražimo najkraću rekurziju niza vektora $\boldsymbol{v}_i$, neka je dimenzija vektora $n$; možemo nasumično odabrati $n$-dimenzionalni redni vektor $\mathbf u^T$ i izračunati najkraću rekurziju skalarnog niza $\{\boldsymbol{u}^T\boldsymbol{v}_i\}$. Prema Schwartz–Zippelovoj lemi, najkraće rekurzije tih dvaju nizova podudaraju se s vjerojatnošću barem $1 - \frac n p$.

Slično je i s najkraćom rekurzijom niza matrica $\{A_i\}$: ako su matrice veličine $n \times m$, dovoljno je nasumično odabrati redni vektor $\mathbf u^T$ veličine $1 \times n$ i stupčani vektor $\boldsymbol{v}$ veličine $m \times 1$ te izračunati najkraću rekurziju skalarnog niza $\{\boldsymbol{u}^T A_i \boldsymbol{v}\}$. Prema Schwartz–Zippelovoj lemi analogno se dobiva da je vjerojatnost podudaranja barem $1 - \frac{n + m} p$.

#### Ubrzavanje brzog potenciranja matrica

Neka je $\boldsymbol{f}_i$ stupčani vektor dimenzije $n$ i neka prijelaz zadovoljava $\boldsymbol{f}_i = A \boldsymbol{f}_{i - 1}$. Tada je $\{\boldsymbol{f}_i\}$ linearno rekurzivan niz vektora reda najviše $n$. (Dokaz izostavljen.)

Možemo izravno, grubom silom, izračunati $\boldsymbol{f}_0 \dots \boldsymbol{f}_{2n - 1}$, zatim gore opisanim postupkom pronaći najkraću rekurziju niza $\{\boldsymbol{f}_i\}$ i na kraju primijeniti [homogenu linearnu rekurziju s konstantnim koeficijentima](./poly/linear-recurrence.md).

Ako tražimo vektor $\boldsymbol{f}_m$, složenost algoritma je $O(n^3 + n\log n \log m)$. Ako je $A$ rijetka matrica sa samo $k$ elemenata različitih od nule, složenost se može smanjiti na $O(nk + n\log n \log m)$. No budući da algoritam ionako treba barem $O(nk)$ vremena za pretprocesiranje, kad ograničenja nisu stroga može se koristiti i algoritam za linearnu rekurziju složenosti $O(n^2 \log m)$, čija je složenost također prihvatljiva.

#### Minimalni polinom matrice

Minimalni polinom kvadratne matrice $A$ je polinom $f$ najmanjeg stupnja koji zadovoljava $f(A) = 0$.

Minimalni polinom zapravo je najkraća rekurzija niza $\{A^i\}$, pa je dovoljno izravno primijeniti Berlekamp–Masseyjev algoritam. Ako je $A$ kvadratna matrica reda $n$, očito je stupanj minimalnog polinoma najviše $n$.

Usko grlo je računanje $A^i$, jer bi izravno množenje matrica u svakom koraku dalo složenost $O(n^4)$. No kad tražimo najkraću rekurziju niza matrica, zapravo tražimo najkraću rekurziju niza $\{\boldsymbol{u}^T A^i \boldsymbol{v}\}$, pa je dovoljno izračunati $A^i \boldsymbol{v}$.

Ako $A$ ima $k$ elemenata različitih od nule, složenost je $O(kn + n^2)$.

#### Determinanta rijetke matrice

Ako možemo izračunati karakteristični polinom kvadratne matrice $A$, njegov slobodni član pomnožen s $(-1)^n$ je determinanta. Međutim, minimalni polinom nije nužno jednak karakterističnom polinomu.

Zapravo, ako $A$ pomnožimo nasumičnom dijagonalnom matricom $B$, minimalni polinom od $AB$ je s vjerojatnošću barem $1 - \frac {2n^2 - n} p$ jednak karakterističnom polinomu. Na kraju samo još podijelimo s $\text{det}\;B$.

Ako je $A$ kvadratna matrica reda $n$ s $k$ elemenata različitih od nule, složenost je $O(kn + n ^ 2)$.

#### Rang rijetke matrice

Neka je $A$ matrica veličine $n\times m$. Najprije nasumično odaberemo dijagonalnu matricu $P$ veličine $n\times n$ i dijagonalnu matricu $Q$ veličine $m\times m$, a zatim izračunamo minimalni polinom matrice $Q A P A^T Q$.

Zapravo nije potrebno množiti matrice: pri računanju minimalnog polinoma matricu $Q A P A^T Q$ množimo vektorom, pa jednostavno te matrice redom množimo s vektorom. Odgovor je stupanj minimalnog polinoma nakon što iz njega izbacimo sve faktore $x$.

Ako $A$ ima $k$ elemenata različitih od nule i $n \le m$, složenost je $O(kn + n ^ 2)$.

#### Rješavanje rijetkih sustava jednadžbi

**Problem**: zadano je $A \mathbf x = \mathbf b$, gdje je $A$ rijetka matrica veličine $n \times n$ **punog ranga**, a $\mathbf b$ i $\mathbf x$ su stupčani vektori veličine $1\times n$. Poznati su $A, \mathbf b$; treba izračunati $x$ u složenosti manjoj od $n^\omega$.

**Postupak**: očito je $\mathbf x = A^{-1} \mathbf b$. Ako možemo izračunati najkraću rekurziju $\{r_0 \dots r_{m - 1}\}$ ($m \le n$) niza $\{A^i \mathbf b\}$ ($i \ge 0$), onda vrijedi

$A^{-1} \mathbf b = -\frac 1 {r_{m - 1}} \sum_{i = 0} ^ {m - 2} A^i \mathbf b r_{m - 2 - i}$

(Dokaz izostavljen.)

Budući da je $A$ rijetka matrica, $\mathbf b \dots A^{2n - 1} \mathbf b$ računamo izravno po definiciji.

Jednako tako, ako $A$ ima $k$ elemenata različitih od nule, složenost je $O(kn + n^2)$.

??? note "Referentna implementacija"
    ```cpp
    vector<int> solve_sparse_equations(const vector<tuple<int, int, int>> &A,
                                       const vector<int> &b) {
      int n = (int)b.size();  // 0-based
    
      vector<vector<int>> f({b});
    
      for (int i = 1; i < 2 * n; i++) {
        vector<int> v(n);
        auto &u = f.back();
    
        for (auto [x, y, z] : A)  // [x, y, value]
          v[x] = (v[x] + (long long)u[y] * z) % p;
    
        f.push_back(v);
      }
    
      vector<int> w(n);
      mt19937 gen;
      for (auto &x : w) x = uniform_int_distribution<int>(1, p - 1)(gen);
    
      vector<int> a(2 * n);
      for (int i = 0; i < 2 * n; i++)
        for (int j = 0; j < n; j++) a[i] = (a[i] + (long long)f[i][j] * w[j]) % p;
    
      auto c = berlekamp_massey(a);
      int m = (int)c.size();
    
      vector<int> ans(n);
    
      for (int i = 0; i < m - 1; i++)
        for (int j = 0; j < n; j++)
          ans[j] = (ans[j] + (long long)c[m - 2 - i] * f[i][j]) % p;
    
      int inv = power(p - c[m - 1], p - 2);
    
      for (int i = 0; i < n; i++) ans[i] = (long long)ans[i] * inv % p;
    
      return ans;
    }
    ```

### Primjeri zadataka

1.  [LibreOJ #163. 高斯消元 2 (Gaussova eliminacija 2)](https://loj.ac/p/163)
2.  [ICPC 2021 Taipei, Gym 103443E. Composition with Large Red Plane, Yellow, Black, Gray, and Blue](https://codeforces.com/gym/103443/problem/E)
