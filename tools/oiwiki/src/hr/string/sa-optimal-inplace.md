---
title: Optimalni in-place algoritam sortiranja sufiksa
---

Ovo poglavlje predstavlja in-place algoritam sortiranja sufiksa linearne vremenske složenosti[^in-place-sa-sort] (Optimal In-Place Suffix Sorting).

???+ warning "Upozorenje"
    Ovo poglavlje **preporučujemo** čitati **samo** ako ste **vrlo, vrlo dobro** upoznati sa SA-IS-om[^nzc09a][^sa-is-intro].

## Opće postavke

Ciljni niz je $\texttt{Pat}$, sufiksno polje je $\texttt{SA}$, indeksi niza počinju od 0, a završni znak je sentinel, koji bez smanjenja općenitosti postavljamo na 0.

## Sortiranje sufiksa nad cjelobrojnom abecedom

Zapravo se ovaj dio može shvatiti kao in-place inačica algoritma SA-IS.

Budući da je to algoritam čiji su detalji u izvornom radu najjasnije opisani i čija je implementacija razmjerno jednostavna, a ujedno je temelj za razumijevanje algoritama koji slijede, on je težište ovog članka.

Načelo in-place pristupa jest da preimenovani $\texttt{Pat}$ zamjenjuje S i L buckete, a dodatnih $O(n)$ operacija zamjenjuje bucket tipova.

### Preimenovanje ciljnog niza Pat

Jednostavno rečeno, preimenovat ćemo $\texttt{Pat}$ tako da se relativni poredak sufiksa ne promijeni, a preimenovani $\texttt{Pat}$ zamijenit će dotadašnje S i L buckete i označavati početak odnosno kraj bucketa.

Preimenovanje se provodi tako da se znak tipa S u $\texttt{Pat}$ zamijeni indeksom kraja svojeg bucketa, a znak tipa L indeksom početka svojeg bucketa.

Kao na sljedećoj slici:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat}:\qquad&\texttt{ 2   1   1   3   3   1   1   3   3   1   2   1   0} \\
\texttt{Type}:\qquad&\texttt{ L   S   S   L   L   S   S   L   L   S   L   L   S} \\
\texttt{Bucket}:\qquad&\texttt{(0)}\texttt{ }\texttt{(1}\texttt{ }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 1 }\texttt{ }
\texttt{ 1) }\texttt{(2 }\texttt{ }\texttt{ 2) }\texttt{(3}\texttt{ }\texttt{ }\texttt{ 3 }\texttt{ }\texttt{ 3 }\texttt{ }\texttt{ 3)}
\end{aligned}
$$

Preimenovani $\texttt{Pat'}$ (u nastavku preimenovani $\texttt{Pat'}$ zovemo jednostavno $\texttt{Pat}$):

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat'}:\qquad&\texttt{ 7   6   6   9   9   6   6   9   9   6   7   1   0}
\end{aligned}
$$

Budući da su unutar bucketa sufiksi znakova tipa L manji i stoje na početku bucketa, a sufiksi znakova tipa S veći i stoje na kraju bucketa, relativni poredak sufiksa ostaje očuvan.

Opišimo konkretne korake preimenovanja:

1.  Kao i u SA-IS-u, prebrojimo svaki znak u $\texttt{Pat}$ i izračunamo prefiksne sume (counting sort) kako bismo izgradili S/L buckete, samo što ovdje prefiksne sume pohranjujemo u $\texttt{SA}$;
2.  Skeniramo svaki znak niza $\texttt{Pat}$ od kraja prema početku; tako je dovoljno pamtiti tip prethodnog znaka da bismo dinamički odredili tip svakog znaka, a zatim ga prema prefiksnim sumama preimenujemo.

### Sortiranje LMS znakova

Ključni je trik ovdje korištenje unutarnjeg brojača.

#### Inicijalizacija

Na početku svaki element $\texttt{SA}$ postavimo na E (EMPTY).

Skeniramo $\texttt{Pat}$ od kraja prema početku; ako naiđemo na LMS znak $\texttt{Pat[i]}$, postavljamo oznaku u $\texttt{SA[Pat[i]]}$:

ako je $\texttt{SA[Pat[i]]}$ jednako E, postavimo ga na U (UNIQUE);

ako je $\texttt{SA[Pat[i]]}$ jednako U, postavimo ga na M (MULTIPLE);

inače ne radimo ništa.

Rezultat je prikazan na sljedećoj slici:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat}:\qquad&\texttt{ 7   6   6   9   9   6   6   9   9   6   7   1   0} \\
\texttt{LMS}:\qquad&\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ ∗ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ * }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ * }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ }\texttt{ * } \\
\texttt{SA}:\qquad&\texttt{(}\underline{\color{red}{\texttt{U}}}\texttt{) }\texttt{(E)}\texttt{ }\texttt{(E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{M}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}
\end{aligned}
$$

#### Umetanje indeksa LMS znakova u SA

Skeniramo $\texttt{Pat}$ od kraja prema početku i za LMS znak $\texttt{Pat[i]}$ razlikujemo slučajeve prema oznaci u $\texttt{SA[Pat[i]]}$:

U: jednostavno postavimo $\texttt{SA[Pat[i]] = i}$

M: znači da bucket sadrži barem dva LMS znaka.

1.  Ako bucket sadrži barem tri LMS znaka:
    pretposljednju poziciju bucketa koristimo kao privremeni brojač koji bilježi broj već umetnutih LMS znakova u bucketu (posljednja pozicija bucketa je oznaka M);
    nove LMS znakove umećemo počevši od treće pozicije od kraja i privremeni brojač uvećavamo za 1;
    ako ustanovimo da je bucket pun, sve elemente bucketa od početka do treće pozicije od kraja pomaknemo za 2 mjesta udesno, a novi element umetnemo na drugu poziciju bucketa (prvu poziciju bucketa postavimo na E).

2.  Ako bucket sadrži točno 2 LMS znaka, brojač očito nije potreban; jednostavno ih umetnemo redom zdesna nalijevo.

Obična vrijednost:

    prema ranijoj raspravi, bez obzira na to sadrži li bucket dva ili više od dva LMS znaka, to znači da je $\texttt{i}$ pozicija posljednjeg LMS znaka koji treba umetnuti u bucket,

    pa je dovoljno od početka bucketa skenirati ulijevo, pronaći prvu poziciju označenu E i postaviti je na $\texttt{i}$.

Na kraju još jednom skeniramo $\texttt{SA}$ od kraja prema početku i uklonimo eventualno preostale posebne oznake M (bucket nije bio popunjen, pa M i brojač nisu prebrisani).

To radimo tako da LMS znakove u bucketu, kao u gornjem koraku, pomaknemo za 2 mjesta udesno, a oslobođene pozicije slijeva postavimo na E.

Kao na sljedećoj slici:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat}:\qquad&\texttt{ }\texttt{ 7   6   6   9   9   6   6   9   9   6   7   1   0} \\
\texttt{SA}:\qquad&\texttt{(}\underline{\color{red}{\texttt{12}}}\texttt{)}\texttt{ (E)}\texttt{ (E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ M}\texttt{) }\texttt{(E }\texttt{ }
\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}\\
\texttt{SA}:\qquad&\texttt{(12) }\texttt{(E)}\texttt{ (E }\texttt{ }\texttt{ E }\texttt{ }
\texttt{ }\underline{\color{red}{\texttt{9}}}\texttt{ }\texttt{ }{\color{red}{\texttt{ 1 }}}\texttt{ }\texttt{ }
{\color{red}{\texttt{M}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }
\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)} \\
\texttt{SA}:\qquad&\texttt{(12) }\texttt{(E)}\texttt{ (E }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{5}}}}
\texttt{ }\texttt{ }\texttt{ }{\texttt{9}}\texttt{ }\texttt{ }{\color{red}{\texttt{ 2 }}}\texttt{ }\texttt{ }
{\color{red}{\texttt{M}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }
\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}\\
\texttt{SA}:\qquad&\texttt{(12) }\texttt{(E)}\texttt{ (}\underline{\color{red}{\texttt{1}}}\texttt{ }\texttt{ }{\texttt{ 5}}\texttt{ }\texttt{ }\texttt{ }{\texttt{9}}\texttt{ }\texttt{ }{\color{red}{\texttt{ 3 }}}\texttt{ }\texttt{ }{\color{red}{\texttt{M}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}\\
\texttt{SA}:\qquad&\texttt{(12) }\texttt{(E)}\texttt{ (}\texttt{E }\texttt{ }\texttt{ E }\texttt{ }{\color{red}{\texttt{ 1 }}\texttt{ }{\texttt{ 5 }}\texttt{ }\texttt{ }{\texttt{9}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}
\end{aligned}
$$

Budući da se u ovoj fazi svaki bucket pomiče i skenira samo jednom, vremenska složenost je $O(n)$.

### Inducirano sortiranje LMS podnizova

#### Inducirano sortiranje LMS prefiksa

LMS prefikse sortiramo inducirano; kao i u SA-IS-u, taj je dio potpuno jednak kasnijem induciranom sortiranju sufiksa (koristi se ista funkcija), pa ga ovdje preskačemo.

Ovdje izravno navodimo rezultat sortiranja:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{(}\texttt{12}\texttt{)}\texttt{(11)}\texttt{ (1 }\texttt{ }\texttt{ 5 }\texttt{ }\texttt{ 9 }\texttt{ }\texttt{ 2 }\texttt{ }\texttt{ 6}\texttt{) }\texttt{(10 }\texttt{ }\texttt{ 0) }\texttt{(4}\texttt{ }\texttt{ }\texttt{ 8 }\texttt{ }\texttt{ 3 }\texttt{ }\texttt{ 7)}
\end{aligned}
$$

#### Premještanje sortiranih LMS podnizova na kraj SA

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{ }\texttt{E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }{\underline{\color{red}{\texttt{12}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{5}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{9}}}}
\end{aligned}
$$

### Izgradnja reduciranog podniza Pat1

LMS podnizove na kraju $\texttt{SA}$ skeniramo slijeva nadesno, odredimo njihov poredak („preimenovanje”) i preimenovanu vrijednost $\texttt{SA[i]}$ pohranimo u $\texttt{SA}\left[\left\lfloor\frac{\texttt{SA}[i]}{2} \right\rfloor\right]$.

Budući da LMS znakovi nisu susjedni, ne dolazi do sukoba; time preimenovane vrijednosti razmještamo prema izvornom redoslijedu podnizova koje predstavljaju u $\texttt{Pat}$:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{ }\underline{\color{red}{\texttt{1}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{1}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{2}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{0}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ 12 }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 5 }\texttt{ }\texttt{ 9 }
\end{aligned}
$$

Zatim skeniramo $\texttt{SA}$ i te preimenovane vrijednosti skupimo na početak $\texttt{SA}$:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{ }\underline{\color{red}{\texttt{1}}}\texttt{ }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{1}}}\texttt{ }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{2}}}\texttt{ }\texttt{ }\texttt{ }\underline{\color{red}{\texttt{0}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ 12 }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 5 }\texttt{ }\texttt{ 9 }
\end{aligned}
$$

### Rekurzivno rješavanje Pat1 i dovršetak sortiranja LMS sufiksa

Kao i u SA-IS-u, rekurzivno riješimo sortiranje sufiksa reduciranog niza $\texttt{Pat1}$ na početku $\texttt{SA}$, a rezultat pohranimo na kraj $\texttt{SA}$:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{ }\texttt{1 }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 2 }\texttt{ }\texttt{ 0 }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{3}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{0}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{2}}}}
\end{aligned}
$$

Premjestimo $\texttt{SA1}$ s kraja $\texttt{SA}$ na početak $\texttt{SA}$, ponovno skeniramo $\texttt{Pat}$ od kraja prema početku i LMS znakove, redoslijedom kojim se pojavljuju u $\texttt{Pat}$, stavimo na kraj $\texttt{SA}$:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{ }{\underline{\color{red}{\texttt{3}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{0}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{2}}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{5}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{9}}}}\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{12}}}}
\end{aligned}
$$

Prema „tablici preslikavanja” na kraju $\texttt{SA}$ vrijednosti $\texttt{SA1}$ na početku $\texttt{SA}$ pretvorimo natrag u indekse odgovarajućih LMS sufiksa u $\texttt{Pat}$:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&{\underline{\color{red}{\texttt{12}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{5}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{9}}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 5 }\texttt{ }\texttt{ 9 }\texttt{ 12 }
\end{aligned}
$$

Sortirane LMS sufikse s početka $\texttt{SA}$ redom stavimo u odgovarajuće buckete (popunjavajući od kraja):

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{(}{\underline{\color{red}{\texttt{12}}}}\texttt{)}\texttt{ }\texttt{(E)}\texttt{ (}\texttt{E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{1}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{5}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{9}}}}\texttt{)}\texttt{ }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}
\end{aligned}
$$

### Inducirano sortiranje svih sufiksa u Pat1

U ovom dijelu trikom unutarnjeg brojača, koji smo već koristili, provodimo in-place inačicu induciranog sortiranja.

Pretpostavimo da već imamo sortirane LMS sufikse (na krajevima bucketa) i iz njih induciramo sufikse tipa L[^induction-order]:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat}:\qquad&\texttt{ }\texttt{ 7   6   6   9   9   6   6   9   9   6   7   1   0} \\
\texttt{SA}:\qquad&\texttt{(12) }\texttt{(E)}\texttt{ (}\texttt{E }\texttt{ }\texttt{ E }\texttt{ }{\texttt{ 1 }\texttt{ }{\texttt{ 5 }}\texttt{ }\texttt{ }{\texttt{9}}}\texttt{) }\texttt{(E }\texttt{ }\texttt{ E) }\texttt{(E}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}
\end{aligned}
$$

Kao i pri sortiranju LMS znakova, najprije znakove tipa L prebrojimo posebnim oznakama:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{Pat}:\qquad&\texttt{ }\texttt{ 7   6   6   9   9   6   6   9   9   6   7   1   0} \\
\texttt{SA}:\qquad&\texttt{(}{{\texttt{12}}}\texttt{)}\texttt{ }\texttt{(}{\underline{\color{red}{\texttt{U}}}}\texttt{)}\texttt{ }\texttt{(E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ 1 }\texttt{ }\texttt{ 5 }\texttt{ }{\texttt{ 9}}\texttt{) }\texttt{(}{\underline{\color{red}{\texttt{M}}}}\texttt{ }\texttt{ }\texttt{ E) }\texttt{(}{\underline{\color{red}{\texttt{M}}}}\texttt{ }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E }\texttt{ }\texttt{ E)}
\end{aligned}
$$

Skeniramo SA slijeva nadesno, kao i pri sortiranju LMS znakova; nešto je složenije određivanje tipa $\texttt{suf[SA[i] - 1]}$, gdje treba razlikovati slučajeve (detalji u kodu):

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{(}{\overrightarrow{\color{red}{\texttt{12}}}\texttt{)}\texttt{(}{\underline{\color{red}{\texttt{11}}}}}\texttt{)}\texttt{  (E   E   1   5   9) (M   E) (M   E   E   E)}\\
\texttt{SA}:\qquad&\texttt{(}\texttt{12}\texttt{)}\texttt{(}{\overrightarrow{\color{red}{\texttt{11}}}}\texttt{)}\texttt{  (E   E   1   5   9)}\texttt{(}{\underline{\color{red}{\texttt{10}}}}\texttt{ }\texttt{ }\texttt{ E)}\texttt{ (M   E   E   E)}\\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E  }\texttt{ }\texttt{ } {\overrightarrow{\color{red}{\texttt{1}}}}\texttt{ }\texttt{  5   9)}\texttt{(10 }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{0}}}}\texttt{)}\texttt{ (M   E   E   E)}\\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E   1 }\texttt{ }\texttt{ } {\overrightarrow{\color{red}{\texttt{5}}}}\texttt{ }\texttt{  9)}\texttt{(10   0)}\texttt{ (}{\color{red}{\texttt{M   1}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{4}}}}\texttt{ }\texttt{ }\texttt{ E)}\\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E   1   5}\texttt{ }\texttt{ } {\overrightarrow{\color{red}{\texttt{9}}}}\texttt{)}\texttt{(10   0)}\texttt{ (}{\color{red}{\texttt{M   2}}}\texttt{ }\texttt{ }\texttt{ 4 }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{8}}}}\texttt{)}\\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E   1   5   9)(10   0)}\texttt{ (}{\overrightarrow{\color{red}{\texttt{4}}}}\texttt{ }\texttt{ 8 }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{3}}}}\texttt{ }\texttt{ }\texttt{ E}\texttt{)}\\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E   1   5   9)(10   0)}\texttt{ (4 }\texttt{ }\texttt{ }{\overrightarrow{\color{red}{\texttt{8}}}}\texttt{ }\texttt{ 3 }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{7}}}}\texttt{)}
\end{aligned}
$$

Za razliku od SA-IS-a, nakon induciranog sortiranja znakova jednog tipa treba očistiti LMS znakove kako ne bi smetali kasnijem in-place induciranom sortiranju:

$$
\begin{aligned}
\texttt{Index}:\qquad&\texttt{ }\texttt{ 0   1   2   3   4   5   6   7   8   9  10  11  12} \\
\texttt{SA}:\qquad&\texttt{(12)(11)}\texttt{  (E   E  }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{E}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{E}}}}\texttt{ }\texttt{ }\texttt{ }{\underline{\color{red}{\texttt{E}}}}\texttt{)}\texttt{(10   0)}\texttt{ (4   8   3   7)}
\end{aligned}
$$

Induciranje S sufiksa iz L sufiksa potpuno je simetrično induciranju L sufiksa iz LMS sufiksa, pa ga ovdje ne opisujemo zasebno.

Time je inducirano sortiranje dovršeno.

#### Implementacija

Vremenski se ne razlikuje značajno od SA-IS-a, a zauzeće memorije pada na manje od $\dfrac{1}{3}$ izvornog (uz 1 puta više koda), pa algoritam doista zaslužuje naslov izvornog rada Optimal In-Place Suffix Sorting[^in-place-sa-sort].

??? note "Referentni kôd"
    ```rust
    use std::cmp::max;
    use std::cmp::Ordering;
    use std::slice::from_raw_parts_mut;
    
    
    const LTYPE: bool = false;
    const STYPE: bool = true;
    const MAX_SA_VALUE: usize = usize::MAX / 2;
    const EMPTY: usize = MAX_SA_VALUE + 1;
    const UNIQUE: usize = MAX_SA_VALUE + 2;
    const MULTI: usize = MAX_SA_VALUE + 3;  // >= 258
    
    
    fn lms_str_cmp<E: Ord>(l1: &[E], l2: &[E]) -> Ordering {
        for (x, y) in l1.iter().zip(l2.iter()) {
            let cmp_res = x.cmp(&y);
            
            if cmp_res != Ordering::Equal { return cmp_res; }
        }
        
        Ordering::Equal
    }
    
    #[inline]
    fn pat_char_type(cur: usize, prev: usize, last_scanned_type: bool) -> bool {
        if cur < prev || cur == prev && last_scanned_type == STYPE { STYPE }
        else { LTYPE }
    }
    
    
    fn rename_pat(pat: &mut [usize], sa: &mut [usize]) {
        let patlastpos = pat.len() - 1;
        // sve postavi na bucket head
        //sa.fill(0);
        for i in 0..sa.len() { sa[i] = 0 }
        
        for i in 0..pat.len() { sa[pat[i]] += 1 }
        for i in 1..sa.len() { sa[i] += sa[i - 1] }
        
        for i in 0..pat.len() - 1 {
            pat[i] = sa[pat[i]] - 1;
        };
        // L-sufikse postavi na bucket head
        //sa.fill(0);
        for i in 0..sa.len() { sa[i] = 0 }
        
        for i in 0..pat.len() { sa[pat[i]] += 1 }
        let mut last_scanned_type = STYPE;
        pat[patlastpos] = 0;
        for i in (0..pat.len() - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == STYPE {
                last_scanned_type = STYPE;
            } else {
                pat[i] -= sa[pat[i]] - 1;
                last_scanned_type = LTYPE;
            }
        }
    
    }
    
    
    fn sort_lms_char(pat: &mut [usize], sa: &mut [usize]) -> usize {
        //sa.fill(EMPTY);
        for i in 0..sa.len() { sa[i] = EMPTY }
        
        let mut last_scanned_type = STYPE;
        for i in (0..pat.len() - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == STYPE {
                last_scanned_type = STYPE;
            } else {
                if last_scanned_type == STYPE {  // pat[i + 1] is LMS type
                    sa[pat[i + 1]] += 1;
                }
                
                last_scanned_type = LTYPE;
            }
        }
        
        let mut lms_cnt = 0;
        last_scanned_type = STYPE;
        for i in (0..pat.len() - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == STYPE {
                last_scanned_type = STYPE;
            } else {
                let e_i = i + 1;
                let e = pat[e_i];
                
                if last_scanned_type == STYPE {  // pat[i + 1] is LMS type
                    lms_cnt += 1;
                    if sa[e] == UNIQUE {
                        sa[e] = e_i;
                    } else if sa[e] >= MULTI && sa[e - 1] == EMPTY {
                        if sa[e - 2] == EMPTY {
                            sa[e - 2] = e_i;
                            sa[e - 1] = 1;  // set counter
                        } else {  // MUL = 2
                            sa[e] = e_i;
                            sa[e - 1] = EMPTY;
                        }
                    } else if sa[e] >= MULTI && sa[e - 1] != EMPTY {
                        let c = sa[e - 1];  // get counter
                        
                        if sa[e - 2 - c] == EMPTY {
                            sa[e - 2 - c] = e_i;
                            sa[e - 1] += 1;  // update counter
                        } else {
                            for j in (1..c + 1).rev() {
                                sa[e - c + j] = sa[e - 2 - c + j]
                            }
                            sa[e - c] = e_i;
                            sa[e - c - 1] = EMPTY;
                        }
                    } else if sa[e] < EMPTY {
                        for j in (0..e).rev() {
                            if sa[j] == EMPTY {
                                sa[j] = e_i;
                                break;
                            }
                        }
                    }
                }
                
                last_scanned_type = LTYPE;
            }
        }
        
        for i in (0..pat.len()).rev() {
            if sa[i] >= MULTI {
                let c = sa[i - 1];
                for j in (1..c + 1).rev() {  // obrnuti redoslijed da prednji ne prebrišu stražnje
                    sa[i - c + j] = sa[i - 2 - c + j];
                }
                sa[i - c - 1] = EMPTY;
                sa[i - c] = EMPTY;
            }
        }
        
        lms_cnt
    }
    
    
    fn sort_lms_substr(pat: &mut [usize], sa: &mut [usize]) {
        // step 1
        induced_sort(pat, sa);
        
        // step 2
        let pat_last_pos = pat.len() - 1;
        let mut lms_cnt = 0;
        let mut i = pat_last_pos;
        let mut bucket_tail_ptr = pat_last_pos + 1;  // for renamed bucket ver
        let mut bucket = EMPTY;  // može se izostaviti, ali olakšava pisanje koda
        let mut num = 0;  // S type number of bucket
        while i > 0 {
            if pat[sa[i]] != bucket {  // reach new bucket
                num = 0;
                
                let mut l = 0;
                while pat[sa[i - l]] == pat[sa[i]] {  // skeniraj bucket i prebroji S znakove u njemu; po definiciji petlja sigurno staje kad je l=i
                    let pat_i = sa[i - l];             // l < i, tj. i - l > 0, 0 <= pat_i < patlen - 1
                    if pat[pat_i] < pat[pat_i + 1] {
                        let mut k = pat_i;
                        while k > 0 && pat[k - 1] == pat[pat_i] { k -= 1 }
                        num += pat_i - k + 1;
                    } else {
                        break;   // bucket ne sadrži S znakove, kraj skeniranja
                    }
                    
                    l += 1;
                }
                
                bucket_tail_ptr = i;
                bucket = pat[sa[bucket_tail_ptr]];
            }
            
            if num > 0
            && i > bucket_tail_ptr - num
            && sa[i] > 0
            && pat[sa[i]] < pat[sa[i] - 1]  {
                sa[pat_last_pos - lms_cnt] = sa[i];
                lms_cnt += 1;
            }
            
            i -= 1;
        }
        
        sa[pat_last_pos - lms_cnt ] = sa[i];  // i = 0
        lms_cnt += 1;
        //sa[0..pat_last_pos - lms_cnt + 1].fill(EMPTY);
        for i in 0..pat_last_pos - lms_cnt + 1 { sa[i] = EMPTY }
    }
    
    
    fn construct_pat1(pat: &mut [usize], sa: &mut [usize], lms_cnt: usize) -> bool {
        let patlen = pat.len();
        
        let mut prev_lms_str_len = 1;
        let mut rank = 0;
        sa[(patlen - 1) / 2] = rank;
        let mut has_duplicated_char = false;
        for i in patlen - lms_cnt + 1..patlen {  // počni od znaka iza sentinela
            let mut j = sa[i];
            while pat[j] <= pat[j + 1] { j += 1 } // nađi prvi L znak desno od suf(sa[i]); budući da je LMS sufiks sentinela isključen, ne može se izaći izvan granica
            let mut k = j;
            while k + 1 < patlen && pat[k] >= pat[k + 1] { k += 1 }  // nađi prvi LMS znak desno od suf(sa[i])
            let cur_lms_str_len = k + 1 - sa[i];
            let cmp_res = lms_str_cmp(&pat[sa[i]..sa[i] + cur_lms_str_len], &pat[sa[i - 1]..sa[i - 1] + prev_lms_str_len]);
            
            if  cmp_res != Ordering::Equal {
                rank += 1
            }
            
            if rank == sa[sa[i - 1] / 2] {
                has_duplicated_char = true;
            }
            let rank_index = sa[i] / 2;
            sa[rank_index] = rank;  // cjelobrojno dijeljenje
            
            prev_lms_str_len = cur_lms_str_len;
        }
        
        // move to head of sa
        let mut j = 0;
        for i in 0..patlen - lms_cnt {
            if sa[i] != EMPTY {
                sa[j] = sa[i];
                if i > j {
                    sa[i] = EMPTY;
                }
                j += 1;
            }
        }
        //sa[lms_cnt..patlen].fill(EMPTY);
        for i in lms_cnt..patlen { sa[i] = EMPTY }
        
        has_duplicated_char
    }
    
    fn sort_lms_suf(pat: &mut [usize], sa: &mut [usize], lms_cnt: usize, has_duplicated_char: bool) {
        // solve T1 recursively
        let patlen = pat.len();
        let salen = sa.len();
        unsafe {
            let sa_ptr = sa.as_mut_ptr();
            let mut pat1 = from_raw_parts_mut(sa_ptr, lms_cnt);
            let mut sa1 = from_raw_parts_mut(sa_ptr.offset((patlen - lms_cnt) as isize), salen - (patlen - lms_cnt));
            
            if has_duplicated_char {
                _compute_suffix_array_16_1(&mut pat1, &mut sa1);
            } else {
                for i in 0..lms_cnt { sa1[pat1[i]] = i }
            }
        }
        
        // move SA1 to SA[0...n1-1]
        for i in 0..lms_cnt {
            sa[i] = sa[patlen- lms_cnt + i];
        }
        
        // put all LMS-suffixes in SA tail
        let mut last_scanned_type = STYPE;
        let mut j = 0;
        for i in (0..pat.len() - 1).rev() {
            if pat[i] < pat[i + 1] || pat[i] == pat[i + 1] && last_scanned_type == STYPE {
                last_scanned_type = STYPE;
            } else {
                if last_scanned_type == STYPE {
                    sa[patlen - 1 - j] = i + 1;
                    j += 1;
                }
                
                last_scanned_type = LTYPE;
            }
        }
        
        // backward map the LMS-suffixes rank
        for i in 0..lms_cnt {
            let relative_rank = sa[i];
            sa[i] = sa[patlen - lms_cnt + relative_rank];
            sa[patlen - lms_cnt + relative_rank] = EMPTY;
        }
        
        let mut tail = EMPTY;
        let mut rfp = EMPTY;
        for i in (1..lms_cnt).rev() { // sa[0] ostaje na mjestu
            if pat[sa[i]] != tail {
                tail = pat[sa[i]];
                rfp = tail;
            }
            
            sa[rfp] = sa[i];
            if rfp != i { sa[i] = EMPTY }
            rfp -= 1;
        }
    }
    
    // PASS!
    fn induced_sort(pat: &mut [usize], sa: &mut [usize]) {
        let patlen = pat.len();
        
        // place L-suff in SA
        // init
        let mut last_scanned_type = STYPE;
        for i in (0..patlen - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == LTYPE {
                sa[pat[i]] += 1;  // >= EMPTY
                last_scanned_type = LTYPE;
            } else {
                last_scanned_type = STYPE;
            }
        }
        //place
        let mut i = 0;
        while i < patlen {
            if sa[i] < EMPTY && sa[i] > 0 {
                let j = sa[i] - 1;
                let mut is_ltype = false;
                if pat[j] > pat[j + 1] {
                    is_ltype = true;
                } else if pat[j] == pat[j + 1] {  // provjeri je li sa[i] indeks L sufiksa
                    let next_i = sa[pat[sa[i]]];
                    if next_i >= MULTI {
                        is_ltype = true;
                    } else if next_i < EMPTY && pat[sa[i]] + 1 < patlen {
                        if sa[pat[sa[i]] + 1] == EMPTY {
                            is_ltype = true;
                        } else if sa[pat[sa[i]] + 1] < EMPTY {
                            if pat[sa[pat[sa[i]] + 1]] == pat[sa[i]] {
                                is_ltype = true;
                            }
                        }
                    }
                }
                
                if is_ltype {
                    if sa[pat[j]] == UNIQUE {
                        sa[pat[j]] = j;
                    } else if sa[pat[j]] >= MULTI && sa[pat[j] + 1] == EMPTY {
                        if sa[pat[j]] - EMPTY > 2 {
                            sa[pat[j] + 2] = j;
                            sa[pat[j] + 1] = 1;  // set counter
                        } else {
                            sa[pat[j]] = j;
                        }
                    } else if sa[pat[j]] >= MULTI && sa[pat[j] + 1] != EMPTY {
                        let e = pat[j];
                        let c = sa[e + 1];
                        let lfp = e + c + 2;
                        if  c + 2 < sa[pat[j]] - EMPTY {  // nije stiglo do kraja bucketa
                            sa[lfp] = j;
                            sa[e + 1] += 1;  // update counter
                        } else {
                            for k in 1..c + 1 {
                                sa[e + k - 1] = sa[e + k + 1];
                            }
                            sa[e + c] = j;
                            sa[e + c + 1] = EMPTY;
                            if i >= e + 2 && i <= e + c + 1 {
                                i -= 2;
                            }
                        }
                    } else if sa[pat[j]] < EMPTY {
                        for k in pat[j]..patlen {
                            if sa[k] == EMPTY {
                                sa[k] = j;
                                break;
                            }
                        }
                    }
                }
            } else if sa[i] >= MULTI {
                i += 1;
            }
            
            i += 1;
        }
        
        // remove LMS-suff form SA, u jednom bucketu može biti više LMS sufiksa
        last_scanned_type = STYPE;
        for i in (0..pat.len() - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == STYPE {
                last_scanned_type = STYPE;
            } else {
                if last_scanned_type == STYPE {  // pat[i + 1] is LMS type
                    if sa[pat[i + 1]] <= EMPTY {
                        sa[pat[i + 1]] = UNIQUE;
                    } else {
                        sa[pat[i + 1]] += 1;
                    }
                }
                
                last_scanned_type = LTYPE;
            }
        }
        i = patlen - 1;
        while i > 0 {
            if sa[i] > EMPTY {
                let c = sa[i] - EMPTY;
                for k in 0..c {
                    sa[i - k] = EMPTY;
                }
                i -= c - 1;
            }
            
            i -= 1;
        }
        sa[0] = pat.len() - 1;
        
        // place S-suff in SA
        // init
        let mut last_scanned_type = STYPE;
        for i in (0..patlen - 1).rev() {
            if pat_char_type(pat[i], pat[i + 1], last_scanned_type) == STYPE {
                if sa[pat[i]] >= EMPTY {
                    sa[pat[i]] += 1;
                } else {
                    sa[pat[i]] = UNIQUE;
                }
                last_scanned_type = STYPE;
            } else {
                last_scanned_type = LTYPE;
            }
        }
        i = patlen - 1;
        while i > 0 {
            if sa[i] < EMPTY && sa[i] > 0 {
                let j = sa[i] - 1;
                let mut is_stype = false;
                if pat[j] < pat[j + 1] {
                    is_stype = true;
                } else if pat[j] == pat[j + 1] {  // provjeri je li sa[i] indeks S sufiksa
                    let next_i = sa[pat[sa[i]]];
                    if next_i >= MULTI {
                        is_stype = true;
                    } else if next_i < EMPTY && pat[sa[i]] - 1 > 0 {
                        if sa[pat[sa[i]] - 1] == EMPTY {
                            is_stype = true;
                        } else if sa[pat[sa[i]] - 1] < EMPTY {
                            if pat[sa[pat[sa[i]] - 1]] == pat[sa[i]] {
                                is_stype = true;
                            }
                        }
                    }
                }
                
                if is_stype {
                    if sa[pat[j]] == UNIQUE {
                        sa[pat[j]] = j;
                    } else if sa[pat[j]] >= MULTI && sa[pat[j] - 1] == EMPTY {
                        if sa[pat[j]] - EMPTY > 2 {
                            sa[pat[j] - 2] = j;
                            sa[pat[j] - 1] = 1;  // set counter
                        } else {
                            sa[pat[j]] = j;
                        }
                    } else if sa[pat[j]] >= MULTI && sa[pat[j] - 1] != EMPTY {
                        let e = pat[j];
                        let c = sa[e - 1];
                        let num = sa[pat[j]] - EMPTY;
                        if c + 2 < num {  // nije stiglo do početka bucketa
                            let rfp = e - c - 2;
                            sa[rfp] = j;
                            sa[e - 1] += 1;
                        } else {
                            for k in 1..c + 1 {
                                sa[e - k + 1] = sa[e - k - 1];
                            }
                            sa[e - c] = j;
                            sa[e - c - 1] = EMPTY;
                            if i >= e - num + 1 && i <= e - 2 {
                                i += 2;
                            }
                        }
                    } else if sa[pat[j]] < EMPTY {
                        for k in (0..pat[j]).rev() {
                            if sa[k] == EMPTY {
                                sa[k] = j;
                                break;
                            }
                        }
                    }
                }
            } else if sa[i] >= MULTI {
                i -= 1;
            }
            i -= 1;
        }
    }
    
    fn _compute_suffix_array_16_1(pat: &mut [usize], sa: &mut [usize]) {
        rename_pat(pat, sa);
        let lms_cnt = sort_lms_char(pat, sa);
        sort_lms_substr(pat, sa);
        let has_duplicated_char = construct_pat1(pat, sa, lms_cnt);
        sort_lms_suf(pat, sa, lms_cnt, has_duplicated_char);
        induced_sort(pat, sa);
    }
    
    pub fn suffix_array_16(pat: &[u8]) -> Vec<usize> {
        let mut pat = pat.into_iter().map(|x| *x as usize).collect::<Vec<usize>>();
        pat.push(0);
        let mut sa = vec![0; max(pat.len(), 256) * 1];
        _compute_suffix_array_16_1(&mut pat[..], &mut sa[..]);
        
        sa
    }
    
    fn input() -> String {
        use std::io;
        
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        String::from(input.trim())
    }
    
    
    fn main() {
        let pat = input();
        
        let sa_16 = suffix_array_16(pat.as_bytes());
        
        for i in 1..pat.len() + 1 { print!("{} ", sa_16[i] + 1) }
    }
    ```

## Sortiranje sufiksa nad cjelobrojnom abecedom samo za čitanje

Složeni problem rješava se složenim metodama: podijeli-pa-vladaj pristupom rješava se problem ograničenog prostora.

Teškoća u implementaciji algoritma jest izgradnja BitMaps struktura[^np12] nad $\texttt{SA}$ koje zamjenjuju pozicije krajeva/početaka bucketa što ih je inače označavao preimenovani T.

BitMaps ovdje označava uređeni rječnik (multiskup) predstavljen bitnim vektorom (bit vector); riječ je o kompaktnoj strukturi podataka (compact data structure).

Zainteresirani zasad mogu samo pročitati izvorni rad i radove o BitMaps strukturama na koje se ovaj članak poziva.

## Sortiranje sufiksa nad općom abecedom samo za čitanje

Preduvjeti su merge sort i heap sort.

Budući da autor ima dvojbe oko vremenske složenosti tamošnje metode određivanja tipova znakova, ni to ovdje ne opisujemo; preporučujemo čitanje izvornog rada.

## Napomene

[^in-place-sa-sort]: Li, Zhize; Li, Jian; Huo, Hongwei (2016).*Optimal In-Place Suffix Sorting*. Proceedings of the 25th International Symposium on String Processing and Information Retrieval (SPIRE). Lecture Notes in Computer Science. 11147. Springer. pp. 268–284. arXiv:1610.08305. doi:10.1007/978-3-030-00479-8\_22. ISBN:978-3-030-00478-1.

[^nzc09a]: Ge Nong, Sen Zhang, and Wai Hong Chan. Linear suffix array construction by almost pure induced-sorting. In Data Compression Conference (DCC), pages 193–202. IEEE, 2009.

[^sa-is-intro]: Preporučujemo [blog](https://riteme.site/blog/2016-6-19/sais.html) i njegov [popis issuea](https://github.com/riteme/riteme.github.io/issues/28)

[^induction-order]: Ako se radi o LML sufiksima, najprije se induciraju sufiksi tipa S; jedina je razlika u tome što pri računanju LML sufiksa treba uračunati i sentinel.

[^np12]: Gonzalo Navarro and Eliana Providel. Fast, small, simple rank/select on bitmaps. In Proc. 11th International Symposium on Experimental Algorithms (SEA), pages 295–306, 2012.
