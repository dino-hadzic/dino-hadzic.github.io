---
title: Brza Fourierova transformacija
---

Predznanje: [Kompleksni brojevi](../complex.md).

Ovaj članak predstavlja algoritam koji omogućuje računanje produkta dvaju polinoma stupnja $n$ u vremenu $O(n\log n)$, učinkovitije od naivnog algoritma složenosti $O(n^2)$. Budući da se i množenje dvaju cijelih brojeva može promatrati kao množenje polinoma, ovaj algoritam može poslužiti i za ubrzavanje množenja velikih cijelih brojeva.

## Uvod

Uvedimo dva polinoma $A$ i $B$:

$$
\begin{aligned}
A ={}& 5x^2 + 3x + 7 \\
B ={}& 7x^2 + 2x + 1 \\
\end{aligned}
$$

Produkt dvaju polinoma $C = A \times B$ možemo izračunati u vremenskoj složenosti $O(n^2)$ (ovdje je $n$ stupanj polinoma $A$ odnosno $B$):

$$
\begin{aligned}
C ={}& A \times B \\
  ={}& 35x^4 + 31x^3 + 60x^2 + 17x + 7
\end{aligned}
$$

Očito koeficijenti $c_i$ polinoma $C$ zadovoljavaju $c_i = \sum_{j = 0}^i a_j b_{i - j}$. Kod tog naivnog algoritma računanje svakog člana ima vremensku složenost $O(n)$, a članova ima $O(n)$, pa je vremenska složenost $O(n^2)$.

Može li se to ubrzati tako da se vremenska složenost smanji? Upotrijebimo li brzu Fourierovu transformaciju, složenost možemo smanjiti na $O(n \log n)$.

## Fourierova transformacija

Fourierova transformacija (Fourier Transform) metoda je analize signala: može analizirati sastavnice signala, a od tih sastavnica može i sintetizirati signal. Mnogi valni oblici mogu poslužiti kao sastavnice signala; Fourierova transformacija kao sastavnice koristi sinusne valove.

Neka je $f(t)$ funkcija vremena $t$; tada Fourierova transformacija može otkriti u kojoj se mjeri period frekvencije $\omega$ pojavljuje u $f(t)$:

$$
F(\omega)=\mathbb{F}[f(t)]=\int_{-\infty}^{\infty}f(t)\mathrm{e}^{-\mathrm{i}{\omega}t}dt
$$

Njezina inverzna transformacija jest

$$
f(t)=\mathbb{F}^{-1}[F(\omega)]=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(\omega)\mathrm{e}^{\mathrm{i}{\omega}t}d\omega
$$

Oblik inverzne transformacije vrlo je sličan obliku direktne; nazivnik $2\pi$ upravo je period eksponencijalne funkcije.

Fourierova transformacija odgovara kontinuiranom skalarnom produktu funkcije u vremenskoj domeni s kompleksnom eksponencijalnom funkcijom perioda $2\pi$. Inverzna transformacija također je skalarni produkt.

Fourierova transformacija ima odgovarajući teorem o konvoluciji: konvolucija u vremenskoj domeni može se pretvoriti u produkt u frekvencijskoj domeni, a konvolucija u frekvencijskoj domeni u produkt u vremenskoj domeni.

## Diskretna Fourierova transformacija

**Diskretna Fourierova transformacija** (Discrete Fourier transform, DFT) oblik je Fourierove transformacije koji je diskretan i u vremenskoj i u frekvencijskoj domeni; uzorke signala u vremenskoj domeni pretvara u uzorke njegove DTFT (discrete-time Fourier transform) u frekvencijskoj domeni.

Fourierova transformacija kontinuirani je skalarni produkt funkcija u obliku integrala, a diskretna Fourierova transformacija skalarni je produkt u obliku sume.

Neka je $\{x_n\}_{n=0}^{N-1}$ niz koji zadovoljava uvjet konačnosti; njegova diskretna Fourierova transformacija (DFT) jest:

$$
X_k=\sum_{n=0}^{N-1}x_n\mathrm{e}^{-\mathrm{i}\frac{2\pi}{N}kn}
$$

gdje je $\mathrm{e}$ baza prirodnog logaritma, a $i$ imaginarna jedinica. Transformacija se obično označava simbolom $\mathcal {F}$, tj.

$$
\hat{x}=\mathcal{F}x
$$

Slično integralnom obliku, njezina **inverzna diskretna Fourierova transformacija** (IDFT) jest:

$$
x_n=\frac{1}{N}\sum_{k=0}^{N-1}X_k\mathrm{e}^{\mathrm{i}\frac{2\pi}{N}kn}
$$

što se može zapisati kao:

$$
x=\mathcal{F}^{-1}\hat{x}
$$

Zapravo normalizacijski koeficijenti ispred suma u formulama DFT-a i IDFT-a nisu bitni. U gornjoj definiciji koeficijenti ispred DFT-a i IDFT-a su $1$ odnosno $\frac {1}{N}$. Ponekad oba koeficijenta zamjenjujemo s $\frac{1}{{\sqrt{N}}}$.

Diskretna Fourierova transformacija i dalje je transformacija iz vremenske u frekvencijsku domenu. Zbog posebnosti oblika sume moguća su i drukčija tumačenja.

Promatramo li niz $x_n$ kao koeficijente uz $x^n$ polinoma $f(x)$, izračunati $X_k$ upravo je vrijednost $f(\mathrm{e}^{\frac{-2\pi \mathrm{i}k}{N}})$ polinoma $f(x)$ u korijenu jedinice $\mathrm{e}^{\frac{-2\pi \mathrm{i}k}{N}}$.

To daje drugo tumačenje teorema o konvoluciji, naime kao posebne evaluacije polinoma. Diskretna Fourierova transformacija upravo je evaluacija polinoma u korijenima jedinice.

Na primjer, izračunajmo:

$$
\dbinom{n}{3}+\dbinom{n}{7}+\dbinom{n}{11}+\dbinom{n}{15}+\ldots
$$

Definirajmo funkciju $f(x)$ kao:

$$
f(x)={(1+x)}^n=\dbinom{n}{0}x^0+\dbinom{n}{1}x^1+\dbinom{n}{2}x^2+\dbinom{n}{3}x^3+\ldots
$$

Zatim primijetimo da uvrštavanje četvrtog korijena jedinice, $f(\mathrm{i})$, daje ovakav niz:

$$
f(\mathrm{i})={(1+\mathrm{i})}^n=\dbinom{n}{0}+\dbinom{n}{1}\mathrm{i}-\dbinom{n}{2}-\dbinom{n}{3}\mathrm{i}+\ldots
$$

Pa sljedeća suma upravo poništava sve ostale članove:

$$
f(1)+\mathrm{i}f(\mathrm{i})-f(-1)-\mathrm{i}f(-\mathrm{i})=4\dbinom{n}{3}+4\dbinom{n}{7}+4\dbinom{n}{11}+4\dbinom{n}{15}+\ldots
$$

Stoga je odgovor na ovaj matematički zadatak:

$$
\dbinom{n}{3}+\dbinom{n}{7}+\dbinom{n}{11}+\dbinom{n}{15}+\ldots=\frac{2^n+\mathrm{i}(1+\mathrm{i})^n-\mathrm{i}(1-\mathrm{i})^n}{4}
$$

Ovaj zadatak evaluira polinom u korijenima jedinice, što upravo čini diskretnu Fourierovu transformaciju.

### Matrična formula

Budući da je diskretna Fourierova transformacija **linearan** operator, može se opisati množenjem matrica. U matričnom zapisu diskretna Fourierova transformacija izgleda ovako:

$$
\begin{bmatrix}
    X_{0}  \\
    X_{1}  \\
    X_{2}  \\
    \vdots \\
    X_{N-1}
\end{bmatrix}
=
\begin{bmatrix}
    1      & 1            & 1               & \cdots & 1                   \\
    1      & \alpha       & \alpha^{2}      & \cdots & \alpha^{N-1}        \\
    1      & \alpha^{2}   & \alpha^{4}      & \cdots & \alpha^{2(N-1)}     \\
    \vdots & \vdots       & \vdots          & \ddots & \vdots              \\
    1      & \alpha^{N-1} & \alpha^{2(N-1)} & \cdots & \alpha^{(N-1)(N-1)}
\end{bmatrix}
\begin{bmatrix}
    x_{0}  \\
    x_{1}  \\
    x_{2}  \\
    \vdots \\
    x_{N-1}
\end{bmatrix}
$$

gdje je $\alpha = \mathrm{e}^{-\mathrm{i}\frac{2\pi}{N}}$.

## Brza Fourierova transformacija

FFT je učinkovit algoritam za izvođenje DFT-a, nazvan brza Fourierova transformacija (Fast Fourier Transform, FFT). Ne donosi nova otkrića u teoriji Fourierove transformacije, ali za primjenu diskretne Fourierove transformacije u računalnim, odnosno digitalnim sustavima predstavlja velik korak naprijed. Brza teorijsko-brojevna transformacija (NTT) implementacija je brze Fourierove transformacije (FFT) na teorijsko-brojevnoj osnovi.

Godine 1965. Cooley i Tukey objavili su algoritam brze Fourierove transformacije. Zapravo je FFT bio otkriven i mnogo ranije, ali tada moderna računala još nisu postojala i ljudi nisu bili svjesni važnosti FFT-a. Neki istraživači smatraju da su FFT otkrili Runge i König 1924. No zapravo je Gauss taj algoritam izumio još 1805., ali ga nikada nije objavio.

### Implementacija metodom „podijeli pa vladaj”

Osnovna ideja algoritma FFT jest podijeli pa vladaj (divide and conquer). Za DFT on podjelom računa vrijednost $f(x)$ za $x=\omega_n^k$. Ideja podjele u FFT-u s bazom 2 (radix-2) očituje se u razdvajanju polinoma na članove neparnog i parnog stupnja.

Na primjer, za polinom s ukupno $8$ članova:

$$
f(x) = a_0 + a_1x + a_2x^2+a_3x^3+a_4x^4+a_5x^5+a_6x^6+a_7x^7
$$

Podijelimo ga u dvije skupine prema parnosti stupnja, a zatim iz desne izlučimo $x$:

$$
\begin{aligned}
f(x) &= (a_0+a_2x^2+a_4x^4+a_6x^6) + (a_1x+a_3x^3+a_5x^5+a_7x^7)\\
     &= (a_0+a_2x^2+a_4x^4+a_6x^6) + x(a_1+a_3x^2+a_5x^4+a_7x^6)
\end{aligned}
$$

Od koeficijenata parnih odnosno neparnih članova zasebno gradimo nove funkcije:

$$
\begin{aligned}
G(x) &= a_0+a_2x+a_4x^2+a_6x^3\\
H(x) &= a_1+a_3x+a_5x^2+a_7x^3
\end{aligned}
$$

Tada se izvorni $f(x)$ pomoću novih funkcija zapisuje kao:

$$
f(x)=G\left(x^2\right) + x  \times  H\left(x^2\right)
$$

Koristeći svojstvo korijena jedinice parnog reda $\omega^i_n = -\omega^{i + n/2}_n$ te činjenicu da su $G\left(x^2\right)$ i $H\left(x^2\right)$ parne funkcije, znamo da u kompleksnoj ravnini $\omega^i_n$ i $\omega^{i+n/2}_n$ daju jednake vrijednosti za $G(x^2)$ i $H(x^2)$. Dobivamo:

$$
\begin{aligned}
f(\omega_n^k) &= G((\omega_n^k)^2) + \omega_n^k  \times H((\omega_n^k)^2) \\
              &= G(\omega_n^{2k}) + \omega_n^k  \times H(\omega_n^{2k}) \\
              &= G(\omega_{n/2}^k) + \omega_n^k  \times H(\omega_{n/2}^k)
\end{aligned}
$$

i:

$$
\begin{aligned}
f(\omega_n^{k+n/2}) &= G(\omega_n^{2k+n}) + \omega_n^{k+n/2}  \times H(\omega_n^{2k+n}) \\
                    &= G(\omega_n^{2k}) - \omega_n^k  \times H(\omega_n^{2k}) \\
                    &= G(\omega_{n/2}^k) - \omega_n^k  \times H(\omega_{n/2}^k)
\end{aligned}
$$

Dakle, nakon što izračunamo $G(\omega_{n/2}^k)$ i $H(\omega_{n/2}^k)$, možemo istodobno dobiti $f(\omega_n^k)$ i $f(\omega_n^{k+n/2})$. Stoga je dovoljno rekurzivno provesti DFT nad $G$ i $H$.

Imajući na umu da duljina polinoma koju DFT s podjelom može obraditi može biti samo $2^m(m \in \mathbf{N}^ \ast )$ — inače bi pri podjeli lijeva i desna strana bile različitih duljina i desnoj bi nedostajali koeficijenti — prije prvog DFT-a niz treba nadopuniti do duljine $2^m(m \in \mathbf{N}^\ast )$ (koeficijenti visokih stupnjeva dopune se s $0$), tj. do polinoma najvišeg stupnja $2^m-1$.

Pri uvrštavanju vrijednosti, budući da treba uvrstiti $n$ različitih vrijednosti, uvrštavamo $\omega_n^0,\omega_n^1,\omega_n^2,\cdots, \omega_n^{n-1} (n=2^m(m \in \mathbf{N}^ \ast ))$, ukupno $2^m$ različitih vrijednosti.

Što se tiče implementacije, STL nudi predložak za kompleksne brojeve, a naravno može se implementirati i ručno. Razlika je u tome što se uz STL-ov `complex` može pozvati funkcija `exp` za računanje $\omega_n$. No zapravo je računanje $\omega_n$ pomoću imaginarnih brojeva dobivenih Eulerovom formulom ekvivalentno.

To je bio prikaz DFT-a u algoritmu FFT: on polinom iz prikaza koeficijentima pretvara u prikaz vrijednostima u točkama.

Vrijedi napomenuti da, budući da je riječ o kompleksnim korijenima jedinice, polinom s $n$ članova moramo na visokim mjestima nadopuniti nulama tako da je $n = 2 ^ k, k \in \mathbf{N}^ \ast$.

???+ note "Rekurzivni FFT"
    ```cpp
    #include <cmath>
    #include <complex>
    
    using Comp = std::complex<double>;  // STL complex
    
    constexpr Comp I(0, 1);  // i
    constexpr int MAX_N = 1 << 20;
    
    Comp tmp[MAX_N];
    
    // rev=1, DFT; rev=-1, IDFT
    // nakon primjene ove funkcije treba pripaziti na normalizacijski koeficijent
    void DFT(Comp* f, int n, int rev) {
      if (n == 1) return;
      for (int i = 0; i < n; ++i) tmp[i] = f[i];
      // parni idu lijevo, neparni desno
      for (int i = 0; i < n; ++i) {
        if (i & 1)
          f[n / 2 + i / 2] = tmp[i];
        else
          f[i / 2] = tmp[i];
      }
      Comp *g = f, *h = f + n / 2;
      // rekurzivni DFT
      DFT(g, n / 2, rev), DFT(h, n / 2, rev);
      // cur je trenutni kompleksni korijen jedinice; za k = 0 pripadni korijen jedinice je omega^0_n = 1.
      // step je razlika dvaju korijena jedinice, tj. vrijedi omega^k_n = step*omega^{k-1}*n,
      // definicija je ekvivalentna exp(I*(-2*M_PI/n*rev))
      Comp cur(1, 0), step(cos(2 * M_PI / n), sin(-2 * M_PI * rev / n));
      for (int k = 0; k < n / 2;
           ++k) {  // F(omega^k_n) = G(omega^k*{n/2}) + omega^k*n\*H(omega^k*{n/2})
        tmp[k] = g[k] + cur * h[k];
        // F(omega^{k+n/2}*n) = G(omega^k*{n/2}) - omega^k_n*H(omega^k\_{n/2})
        tmp[k + n / 2] = g[k] - cur * h[k];
        cur *= step;
      }
      for (int i = 0; i < n; ++i) f[i] = tmp[i];
    }
    ```

Vremenska složenost je $O(n\log n)$.

### Implementacija udvostručavanjem

Ovaj se algoritam može dodatno optimizirati sa stajališta „podjele”. Kod FFT-a s bazom 2 svaki put razdvajamo koeficijente neparnih i parnih članova cijelog polinoma, sve dok ne ostane samo jedan koeficijent. Međutim, taj rekurzivni postupak zahtijeva više memorije. Zato možemo najprije, „oponašajući rekurziju”, te koeficijente „razdvojiti” u izvornom polju, a zatim „udvostručavanjem” spajati izračunate vrijednosti.

Za „razdvajanje” može se upotrijebiti permutacija obrnutim poretkom bitova.

Za „spajanje” se optimizacijom leptir-operacijom može postići da je potrebno samo $O(1)$ dodatnog prostora.

#### Permutacija obrnutim poretkom bitova

Na primjeru polinoma s $8$ članova simulirajmo postupak razdvajanja:

-   Početni niz je $\{x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7\}$
-   Nakon jedne podjele $\{x_0, x_2, x_4, x_6\},\{x_1, x_3, x_5, x_7 \}$
-   Nakon dviju podjela $\{x_0,x_4\} \{x_2, x_6\},\{x_1, x_5\},\{x_3, x_7 \}$
-   Nakon triju podjela $\{x_0\}\{x_4\}\{x_2\}\{x_6\}\{x_1\}\{x_5\}\{x_3\}\{x_7 \}$

Pravilnost: to je zapravo izvorni niz u kojem svaki broj zapišemo binarno, a zatim binarni zapis zrcalno obrnemo — to je indeks konačnog položaja. Na primjer, $x_1$ je 001, obrnuto je 100, tj. 4, i konačni položaj doista je 4. Tu transformaciju zovemo permutacijom obrnutim poretkom bitova (bit-reversal permutation); dokaz prepuštamo čitatelju.

Prema definiciji rezultat transformacije za svaki broj možemo izračunati u vremenu $O(n)$:

???+ note "Implementacija permutacije obrnutim poretkom bitova ($O(n)$)"
    ```cpp
    /*
     * Permutacija koja prethodi FFT-u i IFFT-u
     * Položaj i zamjenjuje se s položajem dobivenim obrtanjem binarnog zapisa od i
     * len mora biti potencija broja 2
     */
    void change(Complex y[], int len) {
      // Na početku je i = 0...01, a j = 10...0, binarno su zrcalno simetrični.
      // Zatim i raste za jedan, a j ostaje zrcalno simetričan prema i, sve do i = 1...11.
      for (int i = 1, j = len / 2, k; i < len - 1; i++) {
        // Zamijeni elemente čiji su indeksi međusobno obrnuti; i < j jamči da se zamjena obavi jednom
        if (i < j) swap(y[i], y[j]);
        // i se uvećava normalno za 1, a j se uvećava za 1 „obrnuto”, tako da i i j uvijek ostaju obrnuti jedan drugome.
        // Ovdje k predstavlja najviši bit na kojem se pojavljuje 0. j najprije oduzima više bitove koji su svi 1,
        // dok ne naiđe na 0, a zatim je dovoljno dodati.
        // Promotrimo broj obrtanja bitova u j: najviši bit obrnut će se n puta,
        // drugi najviši n/2 puta itd., pa je vremenska složenost:
        // T(n) = n + n/2 + n/4 + ... = O(n)
        k = len / 2;
        while (j >= k) {
          j = j - k;
          k = k / 2;
        }
        j += k;
      }
    }
    ```

Permutacija obrnutim poretkom bitova može se u $O(n)$ izračunati i rekurzijom od manjih prema većima: neka je $len=2^k$, gdje $k$ označava duljinu binarnog zapisa, i neka $R(x)$ označava broj dobiven obrtanjem binarnog zapisa duljine $k$ broja $x$ (visoka mjesta dopunjena s $0$). Tražimo $R(0),R(1),\cdots,R(n-1)$.

Najprije, $R(0)=0$.

$R(x)$ računamo od manjih prema većima. Stoga je pri računanju $R(x)$ vrijednost $R\left(\left\lfloor \dfrac{x}{2} \right\rfloor\right)$ već poznata. Dakle, pomaknemo $x$ za jedno mjesto udesno (podijelimo s $2$), obrnemo, pa opet pomaknemo za jedno mjesto udesno, i dobili smo rezultat obrtanja svih bitova od $x$ **osim (binarne) znamenke jedinica**.

Razmotrimo obrtanje znamenke jedinica: ako je ona $0$, nakon obrtanja najviši bit je $0$. Ako je $1$, nakon obrtanja najviši bit je $1$, pa treba još dodati $\dfrac{len}{2}=2^{k-1}$. Ukupno

$$
R(x)=\left\lfloor \frac{R\left(\left\lfloor \frac{x}{2} \right\rfloor\right)}{2} \right\rfloor + (x\bmod 2)\times \frac{len}{2}
$$

Primjer: neka je $k=5$, $len=(100000)_2$. Da bismo obrnuli $(11001)_2$:

1.  Promotrimo $(1100)_2$; znamo da je $R((1100)_2)=R((01100)_2)=(00110)_2$, a nakon još jednog pomaka udesno dobivamo $(00011)_2$.
2.  Promotrimo znamenku jedinica: ako je $1$, mora se obrnuti na najviše mjesto broja, tj. obrnutom broju dodajemo $(10000)_2=2^{k-1}$; ako je $0$, ne mijenjamo ništa.

???+ note "Implementacija permutacije obrnutim poretkom bitova ($O(n)$)"
    ```cpp
    // Također treba osigurati da je len potencija broja 2
    // Neka je rev[i] vrijednost i nakon obrtanja
    void change(Complex y[], int len) {
      for (int i = 0; i < len; ++i) {
        rev[i] = rev[i >> 1] >> 1;
        if (i & 1) {  // ako je zadnji bit 1, obrće se u len/2
          rev[i] |= len >> 1;
        }
      }
      for (int i = 0; i < len; ++i) {
        if (i < rev[i]) {  // jamči da se svaki par zamijeni samo jednom
          swap(y[i], y[rev[i]]);
        }
      }
      return;
    }
    ```

#### Optimizacija leptir-operacijom

Kad znamo $G(\omega_{n/2}^k)$ i $H(\omega_{n/2}^k)$, pomoću sljedećih dviju formula treba izračunati $f(\omega_n^k)$ i $f(\omega_n^{k+n/2})$:

$$
\begin{aligned}
    f(\omega_n^k)       & = G(\omega_{n/2}^k) + \omega_n^k \times H(\omega_{n/2}^k) \\
    f(\omega_n^{k+n/2}) & = G(\omega_{n/2}^k) - \omega_n^k \times H(\omega_{n/2}^k)
\end{aligned}
$$

Nakon permutacije obrnutim poretkom bitova, za zadane $n, k$:

-   Vrijednost $G(\omega_{n/2}^k)$ pohranjena je na indeksu $k$ polja, a vrijednost $H(\omega_{n/2}^k)$ na indeksu $k + \dfrac{n}{2}$.
-   Vrijednost $f(\omega_n^k)$ bit će pohranjena na indeksu $k$ polja, a vrijednost $f(\omega_n^{k+n/2})$ na indeksu $k + \dfrac{n}{2}$.

Stoga možemo izravno prepisati vrijednosti na indeksima $k$ i $k + \frac{n}{2}$ polja, bez otvaranja dodatnog polja za pohranu vrijednosti. Ta se metoda zove **leptir-operacija** (butterfly), ili preciznije leptir-operacija s bazom 2.

Objasnimo još detaljnije kako leptir-operacijom obaviti sva spajanja segmenata duljine $\frac{n}{2}$:

1.  Neka je duljina segmenta $s = \frac{n}{2}$;
2.  Istodobno nabrajamo lijeve krajeve $l_g = 0, 2s, 4s, \cdots, N-2s$ niza $\{G(\omega_{n/2}^k)\}$ i lijeve krajeve $l_h = s, 3s, 5s, \cdots, N-s$ niza $\{H(\omega_{n/2}^k)\}$;
3.  Pri spajanju dvaju segmenata nabrajamo $k = 0, 1, 2, \cdots, s-1$; tada je $G(\omega_{n/2}^k)$ pohranjen na indeksu $l_g + k$ polja, a $H(\omega_{n/2}^k)$ na indeksu $l_h + k$;
4.  Leptir-operacijom izračunamo $f(\omega_n^k)$ i $f(\omega_n^{k+n/2})$ te ih izravno prepišemo na izvorna mjesta.

## Inverzna brza Fourierova transformacija

Inverzna Fourierova transformacija može se izraziti Fourierovom transformacijom. To možemo shvatiti na dva načina.

### Sa stajališta linearne algebre

Uloga IDFT-a (inverzne Fourierove transformacije) jest pretvoriti prikaz ciljnog polinoma vrijednostima u točkama u prikaz koeficijentima. A sam DFT linearna je transformacija: može se shvatiti tako da ciljni polinom promatramo kao vektor i množimo ga slijeva matricom da bismo dobili transformirani vektor, čime simuliramo uvrštavanje kompleksnih korijena jedinice u polinom:

$$
\begin{bmatrix}y_0 \\ y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_{n-1} \end{bmatrix}
=
\begin{bmatrix}1 & 1 & 1 & 1 & \cdots & 1 \\
1 & \omega_n^1 & \omega_n^2 & \omega_n^3 & \cdots & \omega_n^{n-1} \\
1 & \omega_n^2 & \omega_n^4 & \omega_n^6 & \cdots & \omega_n^{2(n-1)} \\
1 & \omega_n^3 & \omega_n^6 & \omega_n^9 & \cdots & \omega_n^{3(n-1)} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \omega_n^{n-1} & \omega_n^{2(n-1)} & \omega_n^{3(n-1)} & \cdots & \omega_n^{(n-1)^2} \end{bmatrix}
\begin{bmatrix} a_0 \\ a_1 \\ a_2 \\ a_3 \\ \vdots \\ a_{n-1} \end{bmatrix}
$$

Sada već imamo rezultat na krajnjoj lijevoj strani, a vrijednosti $x$ u sredini također odgovaraju jedna po jedna prikazu ciljnog polinoma vrijednostima u točkama, pa je prema osnovnom znanju o matricama dovoljno obje strane jednakosti slijeva pomnožiti inverzom one velike matrice u sredini.

Budući da su elementi te matrice vrlo posebni, i njezina inverzna matrica ima posebno svojstvo: dovoljno je svaki element **zamijeniti recipročnom vrijednošću** i zatim **podijeliti duljinom transformacije $n$** da bismo dobili inverznu matricu.

Napomena: duljina Fourierove transformacije nije duljina polinoma; duljina transformacije mora biti veća od duljine polinoma produkta. Polinomi koje množimo nisu dovoljno dugi pa ih na visokim stupnjevima treba dopuniti s $0$.

Da bi rezultat računanja bio recipročna vrijednost izvornog, prema Eulerovoj formuli dobivamo

$$
\frac{1}{\omega_k}=\omega_k^{-1}=\mathrm{e}^{-\frac{2\pi \mathrm{i}}{k}}=\cos\left(\frac{2\pi}{k}\right)+\mathrm{i} \sin\left(-\frac{2\pi}{k}\right)
$$

Stoga možemo pokušati korijen jedinice $\omega_k$ uzeti kao $\mathrm{e}^{-\frac{2\pi \mathrm{i}}{k}}$; tako rezultat računanja postaje recipročna vrijednost izvornog, a jedina dodatna operacija nakon toga jest još **podijeliti njegovom duljinom $n$**, dok je ostatak postupka potpuno jednak DFT-u. Možemo definirati jednu funkciju i dodati joj parametar $1$ ili $-1$ kojim množimo $\pi$. Proslijedimo li $1$, to je DFT, a proslijedimo li $-1$, IDFT.

### Periodičnost kompleksnih korijena jedinice

Odnos IDFT-a i DFT-a može se razumjeti i pomoću periodičnosti kompleksnih korijena jedinice.

Neka je izvorni polinom $f(x)=a_0+a_1x+a_2x^2+\cdots+a_{n-1}x^{n-1}=\sum_{i=0}^{n-1}a_ix^i$. IDFT vraća prikaz vrijednostima u točkama natrag u prikaz koeficijentima.

Razmotrimo **konstruktivnu metodu**. Znamo $y_i=f\left( \omega_n^i \right),i\in\{0,1,\cdots,n-1\}$ i tražimo $\{a_0,a_1,\cdots,a_{n-1}\}$. Konstruiramo polinom

$$
A(x)=\sum_{i=0}^{n-1}y_ix^i
$$

što odgovara tome da $\{y_0,y_1,y_2,\cdots,y_{n-1}\}$ promatramo kao prikaz polinoma $A$ koeficijentima.

Sada imamo dva načina izvođenja, koji odgovaraju dvjema metodama implementacije.

#### Prva metoda

Neka je $b_i=\omega_n^{-i}$; tada je prikaz polinoma $A$ vrijednostima u točkama $x=b_0,b_1,\cdots,b_{n-1}$ jednak $\left\{ A(b_0),A(b_1),\cdots,A(b_{n-1}) \right\}$.

Preoblikovanjem definicije od $A(x)$ možemo $A(b_k)$ izraziti kao

$$
\begin{aligned}
A(b_k)&=\sum_{i=0}^{n-1}f(\omega_n^i)\omega_n^{-ik}=\sum_{i=0}^{n-1}\omega_n^{-ik}\sum_{j=0}^{n-1}a_j(\omega_n^i)^{j}\\
&=\sum_{i=0}^{n-1}\sum_{j=0}^{n-1}a_j\omega_n^{i(j-k)}=\sum_{j=0}^{n-1}a_j\sum_{i=0}^{n-1}\left(\omega_n^{j-k}\right)^i\\
\end{aligned}
$$

Označimo $S\left(\omega_n^a\right)=\sum_{i=0}^{n-1}\left(\omega_n^a\right)^i$.

Kad je $a=0 \pmod{n}$, vrijedi $S\left(\omega_n^a\right)=n$.

Kad je $a\neq 0 \pmod{n}$, oduzimamo uz pomak

$$
\begin{aligned}
S\left(\omega_n^a\right)&=\sum_{i=0}^{n-1}\left(\omega_n^a\right)^i\\
\omega_n^a S\left(\omega_n^a\right)&=\sum_{i=1}^{n}\left(\omega_n^a\right)^i\\
S\left(\omega_n^a\right)&=\frac{\left(\omega_n^a\right)^n-\left(\omega_n^a\right)^0}{\omega_n^a-1}=0\\
\end{aligned}
$$

Drugim riječima

$$
S\left(\omega_n^a\right)=
\begin{cases}
n,&a=0\\
0,&a\neq 0
\end{cases}
$$

Uvrstimo natrag u izvorni izraz

$$
A(b_k)=\sum_{j=0}^{n-1}a_jS\left(\omega_n^{j-k}\right)=a_k\cdot n
$$

Dakle, za zadane točke $b_i=\omega_n^{-i}$ prikaz polinoma $A$ vrijednostima u točkama jest

$$
\begin{aligned}
&\left\{ (b_0,A(b_0)),(b_1,A(b_1)),\cdots,(b_{n-1},A(b_{n-1})) \right\}\\
=&\left\{ (b_0,a_0\cdot n),(b_1,a_1\cdot n),\cdots,(b_{n-1},a_{n-1}\cdot n) \right\}
\end{aligned}
$$

Zaključno, uzmemo korijen jedinice kao njegovu recipročnu vrijednost, nad $\{y_0,y_1,y_2,\cdots,y_{n-1}\}$ provedemo FFT i zatim podijelimo s $n$ — tako dobivamo prikaz $f(x)$ koeficijentima.

#### Druga metoda

Izravno uvrstimo $\omega_n^i$ u $A(x)$.

Izvod je gotovo jednak onom u prvoj metodi; na kraju dobivamo $A(\omega_n^k) = \sum_{j=0}^{n-1}a_jS\left(\omega_n^{j+k}\right)$.

$S\left(\omega_n^{j+k}\right) = n$ vrijedi ako i samo ako je $j+k=0 \pmod{n}$, a inače je $0$. Stoga je $A(\omega_n^k) = a_{n-k}\cdot n$.

To znači da nad $\{y_0,y_1,y_2,\cdots,y_{n-1}\}$ provedemo DFT, podijelimo s $n$, pa obrnemo zadnjih $n - 1$ elemenata; tako također možemo vratiti prikaz $f(x)$ koeficijentima.

### Implementacija

Dakle, naša funkcija FFT može objediniti DFT i IDFT. Implementacija je sljedeća:

???+ note "Nerekurzivni FFT (odgovara prvoj metodi)"
    ```cpp
    /*
     * Izvodi FFT
     * len mora biti oblika 2^k
     * on == 1 znači DFT, on == -1 znači IDFT
     */
    void fft(Complex y[], int len, int on) {
      // permutacija obrnutim poretkom bitova
      change(y, len);
      // Simulira postupak spajanja: na početku se spaja s duljine jedan na duljinu dva, i tako sve do duljine len.
      for (int h = 2; h <= len; h <<= 1) {
        // wn: korak trenutnog kompleksnog korijena jedinice: w^1_h
        Complex wn(cos(2 * PI / h), sin(on * 2 * PI / h));
        // spajanje, ukupno len / h puta.
        for (int j = 0; j < len; j += h) {
          // Računa trenutni kompleksni korijen jedinice; na početku je 1 = w^0_n, zatim raste s korakom wn: w^1_n
          // ...
          Complex w(1, 0);
          for (int k = j; k < j + h / 2; k++) {
            // lijevi i desni dio su rješenja potproblema
            Complex u = y[k];
            Complex t = w * y[k + h / 2];
            // ovdje zbrajamo rezultate dvaju dijelova podjele
            y[k] = u + t;
            y[k + h / 2] = u - t;
            // ω u drugoj polovici „koraka” sigurno je suprotan onom u „prvoj polovici”
            // točka na „crvenoj kružnici” nakon punog kruga „vraća se natrag”, a nakon pola kruga postaje upravo suprotna
            // kvadrat suprotnog broja jednak je kvadratu samog broja
            w = w * wn;
          }
        }
      }
      // Ako je IDFT, svaki element inverzne matrice nije samo recipročna vrijednost izvornog elementa, nego ga treba i podijeliti duljinom len.
      if (on == -1) {
        for (int i = 0; i < len; i++) {
          y[i].x /= len;
          y[i].y /= len;
        }
      }
    }
    ```

???+ note "Nerekurzivni FFT (odgovara drugoj metodi)"
    ```cpp
    /*
     * Izvodi FFT
     * len mora biti oblika 2^k
     * on == 1 znači DFT, on == -1 znači IDFT
     */
    void fft(Complex y[], int len, int on) {
      change(y, len);
      for (int h = 2; h <= len; h <<= 1) {             // simulira postupak spajanja
        Complex wn(cos(2 * PI / h), sin(2 * PI / h));  // računa trenutni kompleksni korijen jedinice
        for (int j = 0; j < len; j += h) {
          Complex w(1, 0);  // računa trenutni kompleksni korijen jedinice
          for (int k = j; k < j + h / 2; k++) {
            Complex u = y[k];
            Complex t = w * y[k + h / 2];
            y[k] = u + t;  // ovdje zbrajamo rezultate dvaju dijelova podjele
            y[k + h / 2] = u - t;
            // ω u drugoj polovici „koraka” sigurno je suprotan onom u „prvoj polovici”
            // točka na „crvenoj kružnici” nakon punog kruga „vraća se natrag”, a nakon pola kruga postaje upravo suprotna
            // kvadrat suprotnog broja jednak je kvadratu samog broja
            w = w * wn;
          }
        }
      }
      if (on == -1) {
        reverse(y + 1, y + len);
        for (int i = 0; i < len; i++) {
          y[i].x /= len;
          y[i].y /= len;
        }
      }
    }
    ```

??? note "Predložak FFT-a ([HDU 1402 - A * B Problem Plus](http://acm.hdu.edu.cn/showproblem.php?pid=1402))"
    ```cpp
    --8<-- "docs/math/code/poly/fft/fft_3.cpp"
    ```

## Literatura

1.  [桃酱的算法笔记 (Algoritamske bilješke Taojiang)](https://zhuanlan.zhihu.com/p/41867199).
