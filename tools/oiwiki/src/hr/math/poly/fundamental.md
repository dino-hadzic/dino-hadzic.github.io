---
title: Osnovni teorem algebre
---

## Definicija

Svaka polinomna jednadžba jedne varijable stupnja $n$ s kompleksnim koeficijentima ($n$ je barem $1$) ima barem jedan korijen u polju kompleksnih brojeva.

Iz toga slijedi da polinomna jednadžba stupnja $n$ s kompleksnim koeficijentima u polju kompleksnih brojeva ima točno $n$ korijena, pri čemu se višestruki korijeni broje s kratnošću.

Ponekad se taj teorem iskazuje i ovako:

Svaki nenul polinom jedne varijable stupnja $n$ s kompleksnim koeficijentima ima točno $n$ kompleksnih korijena.

Dokaz osnovnog teorema algebre obično se oslanja na kompleksnu analizu ili modernu algebru, pa se teorem najčešće izravno primjenjuje kao dobro poznat rezultat.

Prema osnovnom teoremu algebre, polinom s kompleksnim koeficijentima $f(x)=a_nx^n+a_{n-1}x^{n-1}+\ldots+a_0$ sigurno se može na jedinstven način rastaviti kao:

$$
f(x)=a_n{(x-x_1)}^{k_1}{(x-x_2)}^{k_2}\ldots{(x-x_t)}^{k_t}
$$

gdje su svi korijeni kompleksni brojevi i $k_1+k_2+\ldots+k_t=n$.

## Teorem o parovima konjugiranih korijena

Predmet proučavanja osnovnog teorema algebre polinomi su s kompleksnim koeficijentima. Kad proučavamo polinome s realnim koeficijentima, iako se i oni mogu rastaviti na kompleksne korijene, potrebno je proširiti područje proučavanja, što nije osobito praktično.

Imaginarni korijen: korijen koji nije realan.

Teorem: kompleksno konjugirani broj korijena polinoma s realnim koeficijentima također je korijen tog polinoma.

Dokaz: izravno konjugiramo obje strane jednakosti iz osnovnog teorema algebre i dokaz je gotov.

Ako je korijen sam realan, konjugiranjem ostaje isti i ništa se ne mijenja.

Ako je korijen imaginaran, onda je i kompleksno konjugirani broj tog imaginarnog korijena korijen izvornog polinoma. Tada se dva imaginarna korijena mogu upariti.

Teorem: konjugirani imaginarni korijeni jednadžbe s realnim koeficijentima uvijek dolaze u parovima, a kratnosti konjugiranih imaginarnih korijena su jednake.

Dokaz: pretpostavimo da je jedan korijen $a+b\mathrm{i}$; tada je drugi korijen $a-b\mathrm{i}$. To znači da u rastavu postoje dva faktora:

$$
(x-a-b\mathrm{i})(x-a+b\mathrm{i})=x^2-2ax+a^2+b^2
$$

Vidimo da množenjem tih dvaju faktora svi koeficijenti postaju realni brojevi. Kvadratni polinom s realnim koeficijentima na desnoj strani te jednakosti dijeli izvorni polinom.

Stoga, podijelimo li obje strane jednakosti iz osnovnog teorema algebre tim kvadratnim trinomom, ponovno dobivamo jednakost polinoma s realnim koeficijentima. Na novoj jednakosti ponavljamo postupak; kako stupanj pada, nakon određenog broja koraka imaginarnih korijena više nema.

Dakle, kratnosti svakog para konjugiranih imaginarnih korijena su jednake. Time je dokaz završen.

Slijede posljedice teorema o parovima konjugiranih korijena:

-   Polinom neparnog stupnja s realnim koeficijentima ima barem jedan realan korijen, a ukupno ima neparan broj realnih korijena.
-   Polinom parnog stupnja s realnim koeficijentima može biti bez realnih korijena, a ukupno ima paran broj realnih korijena.

Gornji kvadratni trinom $x^2-2ax+a^2+b^2=x^2+px+q$ zovemo nesvodivim kvadratnim faktorom s realnim koeficijentima. Nesvodiv znači da se ne može rastaviti u skupu realnih brojeva.

Teorem: polinom s realnim koeficijentima uvijek je produkt nesvodivih faktora s realnim koeficijentima prvog ili drugog stupnja.

Dokaz:

Čim polinom s realnim koeficijentima ima realan korijen $c$, njemu odgovara faktor $x-c$ s realnim koeficijentima; čim ima par imaginarnih korijena $a\pm b\mathrm{i}$, njemu odgovara faktor $x^2-2ax+a^2+b^2$ s realnim koeficijentima.

Stoga je dovoljno u izvornom rastavu iz osnovnog teorema algebre upariti korijene pomoću teorema o parovima konjugiranih korijena i dokaz je gotov.

Prema teoremu o parovima konjugiranih korijena, polinom s realnim koeficijentima $f(x)=a_nx^n+a_{n-1}x^{n-1}+\ldots+a_0$ sigurno se može na jedinstven način rastaviti kao:

$$
f(x)=a_n{(x-x_1)}^{k_1}{(x-x_2)}^{k_2}\ldots{(x-x_t)}^{k_t}{(x^2+p_1x+q_1)}^{l_1}{(x^2+p_2x+q_2)}^{l_2}\ldots{(x^2+p_sx+q_s)}^{l_s}
$$

gdje su svi koeficijenti realni brojevi i $k_1+k_2+\ldots+k_t+2(l_1+l_2+\ldots+l_s)=n$.

## Linov algoritam (Lin–Bairstowova metoda)

### Uvod

Kako provesti rastav polinoma s realnim koeficijentima prema osnovnom teoremu algebre? Proširimo li skup brojeva na kompleksne, postaje vrlo složeno.

Ako rastavljamo samo u skupu realnih brojeva, možemo jamčiti jedino da, kad je stupanj veći od $2$, sigurno postoji faktor koji je kvadratni trinom s realnim koeficijentima.

Naime, ako polinom ima imaginarne korijene, izravno sastavimo par konjugiranih imaginarnih korijena. Ako polinom ima samo realne korijene, uzmemo bilo koja dva realna korijena i pomnožimo pripadne linearne faktore, čime također dobivamo faktor koji je kvadratni trinom s realnim koeficijentima.

Nakon što nađemo kvadratni trinomni faktor, iz kvadratnog izraza izuzetno je lako izračunati realne ili kompleksne korijene. Tako nastaje računska metoda koja uzastopno **pronalazi po jedan kvadratni faktor** kako bi dobila kompleksne korijene jednadžbe; ta metoda izbjegava računanje s kompleksnim brojevima.

U kolovozu 1940., kolovozu 1943. i srpnju 1947. Lin Shih-nge (林士谔) uzastopno je u časopisu „Journal of Mathematics and Physics”, koji izdaje MIT, službeno objavio 3 rada o metodi rješavanja kompleksnih korijena jednadžbi visokog stupnja[^note1], svaki put s poboljšanjima.

Ta se metoda i danas koristi za brzo računanje na suvremenim računalima; programi za traženje korijena polinoma u programskim paketima (npr. MATLAB) također se temelje na načelu ovog algoritma.

### Postupak

Da bismo pronašli faktor koji je kvadratni trinom, polinom treba rastaviti kao:

$$
f(x)=(x^2+p_1x+q_1)g(x)
$$

Budući da kvadratni trinomni faktor ne možemo pronaći odjednom, u duhu iterativnog rješavanja za početnu vrijednost imamo:

$$
f(x)=(x^2+px+q)g(x)+rx+s
$$

pri čemu kao ostatak nastaje linearni izraz. Čim je ostatak dovoljno malen, približno smo pronašli traženi faktor.

Želimo da konačno rješenje bude početna vrijednost plus korekcija pomakom:

$$
p_1=p+dp
$$

$$
q_1=q+dq
$$

Dva broja $(r, s)$ u ostatku određena su zadanim koeficijentima djelitelja $(p, q)$. Vrijedi odnos parcijalnih derivacija:

$$
dr=\frac{\partial r}{\partial p}dp+\frac{\partial r}{\partial q}dq
$$

$$
ds=\frac{\partial s}{\partial p}dp+\frac{\partial s}{\partial q}dq
$$

U početnoj jednakosti djeljenik $f(x)$ je zadan, a kvocijent $g(x)$ i ostatak $rx+s$ mijenjaju se s promjenom djelitelja $x^2+px+q$. Stoga vrijede odnosi parcijalnih derivacija

$$
0=xg(x)+\frac{\partial g(x)}{\partial p}(x^2+px+q)+\frac{\partial r}{\partial p}x+\frac{\partial s}{\partial p}
$$

$$
0=g(x)+\frac{\partial g(x)}{\partial q}(x^2+px+q)+\frac{\partial r}{\partial q}x+\frac{\partial s}{\partial q}
$$

Primijetimo da je parcijalna derivacija samo broj, neovisan o varijabli $x$. Stoga vrijede odnosi djeljivosti

$$
xg(x)=-\frac{\partial g(x)}{\partial p}(x^2+px+q)-\frac{\partial r}{\partial p}x-\frac{\partial s}{\partial p}
$$

$$
g(x)=-\frac{\partial g(x)}{\partial q}(x^2+px+q)-\frac{\partial r}{\partial q}x-\frac{\partial s}{\partial q}
$$

Zaključak je da su tražene parcijalne derivacije upravo ostatci daljnjeg dijeljenja kvocijenta. Dijeljenje polinoma zadanim kvadratnim trinomom računa se izravno. Time smo dobili četiri parcijalne derivacije.

Želimo da $s$ i $r$ nakon dodavanja pomaka $ds$ i $dr$ postanu $0$, tj. da $ds$ i $dr$ budu suprotni brojevi od $s$ i $r$. Stoga treba riješiti jednadžbe:

$$
-\frac{\partial r}{\partial p}dp-\frac{\partial r}{\partial q}dq=r
$$

$$
-\frac{\partial s}{\partial p}dp-\frac{\partial s}{\partial q}dq=s
$$

Iz gornjeg sustava jednadžbi dobivamo pomake $dp$ i $dq$ koji odgovaraju $p$ i $q$; dovoljno ga je izravno riješiti determinantom drugog reda.

### Implementacija

```C
// a je izvorni polinom, n je stupanj polinoma, p je traženi linearni koeficijent, q je traženi slobodni član
void Shie(double a[], int n, double *p, double *q) {
  // polje b je kvocijent dijeljenja polinoma a kvadratnim trinomom trenutne iteracije
  memset(b, 0, sizeof(b));
  // polje c je kvocijent dijeljenja polinoma b pomnoženog s x na kvadrat kvadratnim trinomom trenutne iteracije
  memset(c, 0, sizeof(c));
  *p = 0;
  *q = 0;
  double dp = 1;
  double dq = 1;
  while (dp > eps || dp < -eps || dq > eps || dq < -eps)  // eps odredite sami
  {
    double p0 = p;
    double q0 = q;
    b[n - 2] = a[n];
    c[n - 2] = b[n - 2];
    b[n - 3] = a[n - 1] - p0 * b[n - 2];
    c[n - 3] = b[n - 3] - p0 * b[n - 2];
    int j;
    for (j = n - 4; j >= 0; j--) {
      b[j] = a[j + 2] - p0 * b[j + 1] - q0 * b[j + 2];
      c[j] = b[j] - p0 * c[j + 1] - q0 * c[j + 2];
    }
    double r = a[1] - p0 * b[0] - q0 * b[1];
    double s = a[0] - q0 * b[0];
    double rp = c[1];
    double sp = b[0] - q0 * c[2];
    double rq = c[0];
    double sq = -q0 * c[1];
    dp = (rp * s - r * sp) / (rp * sq - rq * sp);
    dq = (r * sq - rq * s) / (rp * sq - rq * sp);
    *p += dp;
    *q += dq;
  }
}
```

## Literatura i napomene

[^note1]: [林士谔．论劈因法解高阶特征方程根值的应用问题．数学进展，1963(03):207-217. (Lin Shih-nge. O primjeni metode cijepanja faktora na rješavanje korijena karakterističnih jednadžbi visokog stupnja. Advances in Mathematics, 1963(03):207-217.)](https://cnki.net/kcms/detail/detail.aspx?filename=SXJZ196303000&dbcode=CJFD&dbname=CJFD1979)
