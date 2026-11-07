---
title: Simbolička metoda
---

Simbolička metoda (symbolic method) način je brzog prevođenja kombinatornih objekata u funkcije izvodnice: promatramo određene operacije definirane na skupovima, a zatim izvodimo odgovarajuće operacije nad njihovim funkcijama izvodnicama.

Kombinatornom klasom (ili kraće klasom) nazivamo par $(\mathcal{A},\lvert \cdot \rvert)$, gdje je $\mathcal{A}$ skup kombinatornih objekata, a funkcija $\lvert \cdot \rvert$ svakom kombinatornom objektu pridružuje nenegativan cijeli broj; obično je zovemo funkcijom veličine. Valja uočiti da taj nenegativan cijeli broj ne smije biti beskonačan. Primjerice, za nizove znakova nad abecedom $\lbrace 0,1\rbrace$ kao funkciju veličine možemo uzeti duljinu niza; za stabla ili grafove kao funkciju veličine možemo uzeti broj čvorova. To, međutim, nije obvezno – nekim posebnim čvorovima može se, recimo, dodijeliti veličina $0$ i slično.

Ovaj je članak pojednostavljena verzija prvog poglavlja knjige Analytic Combinatorics.

## Neoznačeni svijet

U neoznačenom svijetu koristimo obične funkcije izvodnice (OGF). Skupu $\mathcal{A}$ pridružujemo OGF

$$
A(z)=\sum_{\alpha\in\mathcal{A}}z^{\lvert \alpha \rvert}=\sum_{n\geq 0}a_nz^n
$$

Dogovorno istom skupinom slova označavamo istu klasu i njezinu funkciju izvodnicu itd.; primjerice, $a_n$ označava $\lbrack z^n\rbrack A(z)$, tj. koeficijent uz $z^n$ u $A(z)$, a $\mathcal{A}_n$ označava skup objekata iz $\mathcal{A}$ čija je veličina $n$ (pa je $a_n=\operatorname{card}(\mathcal{A}_n)$, gdje $\operatorname{card}$ označava kardinalnost).

U ovom članku nećemo raspravljati o dopustivosti (admissibility); čitatelj se može poslužiti literaturom.

Uvodimo dvije posebne kombinatorne klase i dva posebna kombinatorna objekta:

-   Neka je $\epsilon$ neutralni objekt (neutral object), a $\mathcal{E}=\lbrace \epsilon \rbrace$ neutralna klasa (neutral class); veličina neutralnog objekta je $0$, a OGF neutralne klase je $E(z)=1$.
-   Neka je $\circ$ ili $\bullet$ atom (atom object), a $\mathcal{Z}_{\circ}=\lbrace \circ\rbrace$ ili $\mathcal{Z}_{\bullet}=\lbrace \bullet\rbrace$, kraće $\mathcal{Z}$, atomska klasa (atom class); veličina atoma je $1$, a OGF atomske klase je $Z(z)=z$.

Za dvije kombinatorne klase $\mathcal{A}$ i $\mathcal{B}$ koje su izomorfne u kombinatornom smislu pišemo $\mathcal{A}=\mathcal{B}$ ili $\mathcal{A}\cong\mathcal{B}$, no drugu oznaku koristimo samo kad izomorfizam nije trivijalan.

Vrijedi

$$
\mathcal{A}\cong\mathcal{E}\times \mathcal{A}\cong\mathcal{A}\times\mathcal{E}
$$

gdje je $\times$ binarna operacija koja označava Kartezijev produkt skupova.

### Konstrukcija (disjunktne) unije skupova

Uniju klasa $\mathcal{A}$ i $\mathcal{B}$ označavamo s

$$
\mathcal{A}+\mathcal{B}=(\mathcal{E}_{1}\times\mathcal{A})+(\mathcal{E}_2\times\mathcal{B})
$$

Ovakva definicija ne krši zahtjev teorije skupova da skupovi budu disjunktni; možemo zamisliti da smo objekte iz $\mathcal{A}$ obojili crveno, a objekte iz $\mathcal{B}$ plavo.

Odgovarajući OGF je

$$
A(z)+B(z)
$$

Promotrimo

$$
A(z)+B(z)=\sum _ {\alpha\in\mathcal{A}}z^{\lvert \alpha\rvert} + \sum _ {\beta\in\mathcal{B}}z^{\lvert \beta\rvert}=\sum_{n\geq 0}(a_n+b_n)z^n
$$

što odgovara zbrajanju formalnih redova potencija.

### Konstrukcija Kartezijeva produkta skupova

Kartezijev produkt klasa $\mathcal{A}$ i $\mathcal{B}$ označavamo s

$$
\mathcal{A}\times \mathcal{B}=\left\lbrace (\alpha, \beta)\mid \alpha \in \mathcal{A},\beta\in\mathcal{B}\right\rbrace
$$

Odgovarajući OGF je

$$
A(z)\cdot B(z)
$$

Veličinu para $(\alpha,\beta)$ definiramo kao zbroj veličina njegovih sastavnica, pa očito vrijedi i

$$
\gamma =(\alpha_1,\alpha_2,\dots ,\alpha_n)\implies \lvert \gamma\rvert =\lvert \alpha_1\rvert +\lvert \alpha_2\rvert +\cdots +\lvert \alpha_n\rvert
$$

Stoga je

$$
A(z)\cdot B(z)=\left(\sum _ {\alpha\in\mathcal{A}}z^{\lvert \alpha\rvert}\right)\left(\sum _ {\beta\in\mathcal{B}}z^{\lvert \beta\rvert}\right)=\sum _ {(\alpha, \beta)\in(\mathcal{A}\times \mathcal{B})}z^{\lvert \alpha\rvert +\lvert \beta\rvert}=\sum_{n\geq 0}\sum_{i+j=n}a_ib_jz^n
$$

što odgovara množenju formalnih redova potencija.

### Konstrukcija Sequence (niza) nad skupom

Konstrukcija Sequence generira sve moguće kombinacije.

???+ note "Primjer"
    $$
    \begin{aligned}
    \operatorname{SEQ}(\lbrace a\rbrace)&=\lbrace \epsilon\rbrace +\lbrace a\rbrace +\lbrace (a,a)\rbrace +\lbrace (a,a,a)\rbrace +\cdots\\
    \operatorname{SEQ}(\lbrace a,b\rbrace)&=\lbrace \epsilon\rbrace +\lbrace a,b\rbrace +\lbrace (a,b)\rbrace + \lbrace(b,a)\rbrace +\lbrace (a,a)\rbrace +\lbrace (b,b)\rbrace\\
    &+\lbrace (a,b,a)\rbrace +\lbrace (a,b,b)\rbrace +\lbrace (a,a,b)\rbrace\\
    &+\lbrace (b,b,a)\rbrace +\lbrace (b,a,b)\rbrace +\lbrace (b,b,b)\rbrace +\lbrace (a,a,a)\rbrace +\lbrace (b,a,a)\rbrace\\
    &+\cdots
    \end{aligned}
    $$
    
    Vidimo da se generiraju i elementi poput $\lbrace (a,b)\rbrace ,\lbrace (b,a)\rbrace$, koji se razlikuju samo po redoslijedu sastavnica; možemo reći da konstrukcija Sequence generira uređene kombinacije.

Definiramo

$$
\operatorname{SEQ}(\mathcal{A})=\mathcal{E}+\mathcal{A}+(\mathcal{A}\times \mathcal{A})+(\mathcal{A}\times \mathcal{A}\times \mathcal{A})+\cdots
$$

uz zahtjev $\mathcal{A}_0=\varnothing$, tj. u $\mathcal{A}$ nema objekata veličine $0$.

Odgovarajući OGF je

$$
Q(A(z))=1+A(z)+A(z)^2+A(z)^3+\cdots =\frac{1}{1-A(z)}
$$

gdje je $Q$ Pólyina kvaziinverzija (quasi-inversion).

???+ note "Primjer: uređeno korijensko stablo (ordered rooted tree)"
    Konstrukcijom Sequence možemo definirati uređena korijenska stabla, tj. korijenska stabla u kojima je redoslijed djece bitan. Neka je ta kombinatorna klasa $\mathcal{T}$; stablo se sastoji od korijena i niza (Sequence) stabala, tj.
    
    $$
    \mathcal{T}=\lbrace \bullet\rbrace\times\operatorname{SEQ}(\mathcal{T})
    $$
    
    Odgovarajući OGF je
    
    $$
    T(z)=\frac{z}{1-T(z)}
    $$
    
    Prvih nekoliko koeficijenata je `0 1 1 2 5 14 42 132 429 1430 4862 16796`; zanemarimo li slobodni član, to je OEIS [A000108](http://oeis.org/A000108).

### Konstrukcija Multiset (multiskupa) nad skupom

Konstrukcija Multiset generira sve moguće kombinacije, ali ne razlikuje redoslijed elemenata među sastavnicama.

???+ note "Primjer"
    $$
    \begin{aligned}
    \operatorname{MSET}(\lbrace a\rbrace)&=\lbrace \epsilon\rbrace +\lbrace a\rbrace +\lbrace (a,a)\rbrace +\lbrace (a,a,a)\rbrace +\cdots\\
    \operatorname{MSET}(\lbrace a,b\rbrace)&=\lbrace \epsilon\rbrace +\lbrace a\rbrace +\lbrace (a,a)\rbrace +\lbrace (a,a,a)\rbrace +\cdots\\
    &+\lbrace b\rbrace +\lbrace (a,b)\rbrace +\lbrace (a,a,b)\rbrace +\cdots \\
    &+\lbrace (b,b)\rbrace + \lbrace (a,b,b)\rbrace +\lbrace (a,a,b,b)\rbrace + \cdots\\
    &+\cdots
    \end{aligned}
    $$
    
    Uočimo da se $\lbrace (b,a)\rbrace,\lbrace (a,b,a)\rbrace$ pojavljuju u $\operatorname{SEQ}(\lbrace a,b\rbrace)$, ali ne i u $\operatorname{MSET}(\lbrace a,b\rbrace)$; možemo reći da Multiset generira neuređene kombinacije.

Rekurzivno je definiramo kao

$$
\operatorname{MSET}(\lbrace \alpha_0,\alpha_1,\dots, \alpha_n\rbrace)=\operatorname{MSET}(\lbrace \alpha_0,\alpha_1,\dots, \alpha_{n-1}\rbrace)\times \operatorname{SEQ}(\lbrace \alpha_n\rbrace)
$$

tj.

$$
\operatorname{MSET}(\mathcal{A})=\prod _ {\alpha\in\mathcal{A}}\operatorname{SEQ}(\lbrace \alpha\rbrace)
$$

uz zahtjev $\mathcal{A}_0=\varnothing$. Ekvivalentno možemo zapisati

$$
\operatorname{MSET}(\mathcal{A})=\operatorname{SEQ}(\mathcal{A})/\mathbf{R}
$$

gdje je $\mathbf{R}$ relacija ekvivalencije: kažemo da vrijedi $(\alpha_1,\dots,\alpha_n)\mathbf{R}(\beta_1,\dots,\beta_n)$ ako i samo ako postoji neka permutacija $\sigma$ takva da za sve $j$ vrijedi $\beta_{j}=\alpha_{\sigma(j)}$.

Odgovarajući OGF je

$$
\operatorname{Exp}(A(z))=\prod _ {\alpha \in\mathcal{A}}\left(1-z^{\lvert \alpha \rvert}\right)^{-1}=\prod _ {n\geq 1}\left(1-z^n\right)^{-a_n}
$$

Uočimo da je

$$
\ln(1+z)=\frac{z}{1}-\frac{z^2}{2}+\frac{z^3}{3}-\cdots =\sum_{n\geq 1}\frac{(-1)^{n-1}z^n}{n}
$$

i $A(z)=\exp(\ln(A(z)))$, pa je

$$
\begin{aligned}
\operatorname{Exp}(A(z))&=\exp\left(\sum _ {n\geq 1}-a_n\cdot \ln\left(1-z^n\right)\right)\\
&=\exp\left(\sum _ {n\geq 1}-a_n\cdot \sum _ {m\geq 1}\frac{-z^{nm}}{m}\right)\\
&=\exp\left(\frac{A(z)}{1}+\frac{A(z^2)}{2}+\frac{A(z^3)}{3}+\cdots \right)
\end{aligned}
$$

gdje je $\operatorname{Exp}$ Pólyin eksponencijal, poznat i kao Eulerova transformacija.

???+ note "Primjer zadatka [LOJ 6268. 分拆数 (Particijski brojevi)](https://loj.ac/p/6268)"
    **Zadatak**: Neka $f(n)$ označava broj particija broja $n$. Izračunajte $f(1),f(2),\dots,f(10^5)$ modulo $998244353$.
    
    **Rješenje**: Neka je $\mathcal{I}$ klasa svih pozitivnih cijelih brojeva; tada je $\mathcal{I}=\operatorname{SEQ}_{\geq 1}(\mathcal{Z})=\mathcal{Z}\times \operatorname{SEQ}(\mathcal{Z})$ (indeks $\geq 1$ označava ograničenu konstrukciju, v. dalje u tekstu). Traženo je upravo
    
    $$
    \operatorname{MSET}(\mathcal{I})
    $$
    
    Prvih nekoliko koeficijenata odgovarajućeg OGF-a je `1 2 3 5 7 11 15 22 30 42` (bez slobodnog člana), tj. OEIS [A000041](https://oeis.org/A000041).

???+ note "Primjer zadatka [Luogu P4389 付公主的背包 (Ruksak princeze Fu)](https://www.luogu.com.cn/problem/P4389)"
    **Zadatak**: Zadano je $n$ vrsta predmeta s volumenima $v_1,\dots ,v_n$ i pozitivan cijeli broj $m$. Za svaki volumen $1,2,\dots,m$ izračunajte broj načina da se ruksak tog volumena potpuno napuni (broj predmeta svake vrste nije ograničen; različite vrste mogu imati jednak volumen), modulo $998244353$. Vrijedi $1\leq n,m\leq 10^5$ i $1\leq v_i\leq m$.
    
    **Rješenje**: Neka je $\mathcal{A}$ kombinatorna klasa predmeta; traženi su koeficijenti OGF-a koji odgovara $\operatorname{MSET}(\mathcal{A})$.

???+ note "Primjer zadatka [Luogu P5900 无标号无根树计数 (Prebrojavanje neoznačenih nekorijenskih stabala)](https://www.luogu.com.cn/problem/P5900)"
    **Zadatak**: Izračunajte broj neoznačenih nekorijenskih stabala s $n$ čvorova modulo $998244353$. Vrijedi $1\leq n\leq 2\times 10^5$.
    
    **Rješenje**: Neka je $\mathcal{T}$ kombinatorna klasa neoznačenih korijenskih stabala; tada je
    
    $$
    \mathcal{T}=\lbrace \bullet\rbrace\times\operatorname{MSET}(\mathcal{T})
    $$
    
    Prema radu Richarda Ottera [The Number of Trees](https://users.math.msu.edu/users/magyarp/Math482/Otter-Trees.pdf), OGF odgovarajućih nekorijenskih stabala je
    
    $$
    T(z)-\frac{1}{2}T^2(z)+\frac{1}{2}T(z^2)
    $$
    
    Prvih nekoliko koeficijenata je `1 1 1 2 3 6 11 23 47 106` (bez slobodnog člana), tj. OEIS [A000055](https://oeis.org/A000055).

### Konstrukcija Powerset (partitivnog skupa) nad skupom

Konstrukcija Powerset generira sve podskupove.

???+ note "Primjer"
    $$
    \begin{aligned}
    \operatorname{PSET}(\lbrace a\rbrace)&=\lbrace \epsilon\rbrace +\lbrace a\rbrace \\
    \operatorname{PSET}(\lbrace a,b\rbrace)&=\lbrace \epsilon\rbrace +\lbrace a\rbrace +\lbrace b\rbrace +\lbrace (a,b)\rbrace \\
    \operatorname{PSET}(\lbrace a,b,c\rbrace)&=\lbrace \epsilon\rbrace +\lbrace a\rbrace +\lbrace b\rbrace +\lbrace (a,b)\rbrace +\lbrace c\rbrace +\lbrace (a,c)\rbrace +\lbrace (b,c)\rbrace +\lbrace (a,b,c)\rbrace\\
    \end{aligned}
    $$

Rekurzivno je definiramo kao

$$
\operatorname{PSET}(\lbrace \alpha_0,\alpha_1,\dots, \alpha_n\rbrace)=\operatorname{PSET}(\lbrace \alpha_0,\alpha_1,\dots, \alpha_{n-1}\rbrace)\times (\lbrace \epsilon\rbrace +\lbrace \alpha_n\rbrace)
$$

tj.

$$
\operatorname{PSET}(\mathcal{A})\cong \prod _ {\alpha\in\mathcal{A}}\left(\lbrace \epsilon \rbrace +\lbrace \alpha\rbrace\right)
$$

uz zahtjev $\mathcal{A}_0=\varnothing$.

Odgovarajući OGF je

$$
\begin{aligned}
\overline{\operatorname{Exp}}(A(z))&=\prod _ {\alpha\in\mathcal{A}}\left(1+z^{\lvert \alpha \rvert}\right)=\prod _ {n\geq 1}\left(1+z^n\right)^{a_n}\\
&=\exp\left(\sum _ {n\geq 1}a_n\cdot \ln\left(1+z^n\right)\right)\\
&=\exp\left(\sum _ {n\geq 1}a_n\cdot \sum _ {m\geq 1}\frac{(-1)^{m-1}z^{nm}}{m}\right)\\
&=\exp\left(\frac{A(z)}{1}-\frac{A(z^2)}{2}+\frac{A(z^3)}{3}-\cdots \right)
\end{aligned}
$$

gdje je $\overline{\operatorname{Exp}}$ modificirani Pólyin eksponencijal.

Lako se vidi da je $\operatorname{PSET}(\mathcal{A})\subset \operatorname{MSET}(\mathcal{A})$.

### Konstrukcija Cycle (ciklusa) nad skupom

Konstrukcija Cycle generira sve moguće kombinacije, ali ne razlikuje kombinacije koje se razlikuju samo za cikličko pomicanje.

Definiramo je kao

$$
\operatorname{CYC}(\mathcal{A})=\left(\operatorname{SEQ}(\mathcal{A})\setminus\lbrace \epsilon\rbrace\right)/\mathbf{S}
$$

gdje je $\mathbf{S}$ relacija ekvivalencije: kažemo da vrijedi $(\alpha_1,\dots,\alpha_n)\mathbf{S}(\beta_1,\dots,\beta_n)$ ako i samo ako postoji neki ciklički pomak $\tau$ takav da za sve $j$ vrijedi $\beta_j=\alpha_{\tau(j)}$.

???+ note "Primjer"
    Radi jednostavnosti neka su $\texttt{a},\texttt{b}$ znakovi veličine $1$; ovdje navodimo samo nizove veličine $3$ i $4$:
    
    $$
    \operatorname{CYC}(\lbrace \texttt{a},\texttt{b}\rbrace)_3=\lbrace \texttt{aaa}\rbrace +\lbrace \texttt{aab}\rbrace+\lbrace \texttt{abb}\rbrace+\lbrace \texttt{bbb}\rbrace
    $$
    
    pri čemu od $\texttt{aab}\mathbf{S}\texttt{baa}\mathbf{S}\texttt{aba}$ zadržavamo samo jedan, a jednako tako od $\texttt{abb}\mathbf{S}\texttt{bab}\mathbf{S}\texttt{bba}$ zadržavamo samo jedan.
    
    $$
    \operatorname{CYC}(\lbrace \texttt{a},\texttt{b}\rbrace)_4=\lbrace \texttt{aaaa}\rbrace +\lbrace \texttt{aaab}\rbrace+\lbrace \texttt{aabb}\rbrace+\lbrace \texttt{abbb}\rbrace+\lbrace \texttt{bbbb}\rbrace +\lbrace \texttt{abab}\rbrace
    $$
    
    pri čemu je $\texttt{aaab}\mathbf{S}\texttt{baaa}\mathbf{S}\texttt{abaa}\mathbf{S}\texttt{aaba}$, $\texttt{aabb}\mathbf{S}\texttt{baab}\mathbf{S}\texttt{bbaa}\mathbf{S}\texttt{abba}$, $\texttt{abbb}\mathbf{S}\texttt{babb}\mathbf{S}\texttt{bbab}\mathbf{S}\texttt{bbba}$ i $\texttt{abab}\mathbf{S}\texttt{baba}$.

Odgovarajući OGF je

$$
\operatorname{Log}(A(z))=\sum _ {n\geq 1}\frac{\varphi(n)}{n}\ln\frac{1}{1-A(z^n)}
$$

gdje je $\varphi$ Eulerova funkcija, a $\operatorname{Log}$ Pólyin logaritam.

Budući da je dokaz složen, čitatelj se može poslužiti Flajoletovim radom [The Cycle Construction](https://epubs.siam.org/doi/10.1137/0404006) ili dodatkom knjige Analytic Combinatorics.

### Ograničene konstrukcije

Ni u jednoj od gornjih konstrukcija nismo ograničavali broj „sastavnica”. Ako u indeks od $\operatorname{SEQ}$ stavimo predikat nad cijelim brojevima koji ograničava broj sastavnica, npr.

$$
\operatorname{SEQ}_{=k}(\mathcal{B}),\quad \operatorname{SEQ}_{\geq k}(\mathcal{B}),\quad \operatorname{SEQ}_{1..k}(\mathcal{B})
$$

pri čemu se $\operatorname{SEQ}_{=k}(\mathcal{B})$ često kraće piše $\operatorname{SEQ}_k(\mathcal{B})$, a $\operatorname{SEQ}_{1..k}(\mathcal{B})$ označava interval $\lbrack 1..k\rbrack$.

Neka je $\mathfrak{K}$ bilo koja od gornjih konstrukcija $\operatorname{SEQ},\operatorname{PSET},\operatorname{MSET},\operatorname{CYC}$ i neka je

$$
\mathcal{A}=\mathfrak{K}_k(\mathcal{B})
$$

tj. za $\alpha\in\mathcal{A}$ zahtijevamo

$$
\alpha =\lbrace (\beta_1,\beta_2,\dots ,\beta_k)\mid \beta\in\mathcal{B}\rbrace
$$

Neka funkcija $\chi$ kombinatornom objektu pridružuje broj njegovih sastavnica; želimo, dakle, $\chi(\alpha)=k$, pa je prirodno uvesti dodatnu varijablu koja „prati” broj sastavnica.

Neka je

$$
A _ {n,k}=\operatorname{card}\left\lbrace \alpha\in\mathcal{A}\mid \lvert \alpha\rvert =n,\chi(\alpha)=k\right\rbrace
$$

Tada je

$$
A(z,u)=\sum _ {n,k}A _ {n,k}u^kz^n=\sum _ {\alpha\in\mathcal{A}}z^{\lvert \alpha\rvert}u^{\chi(\alpha)}
$$

Zatim je dovoljno izdvojiti koeficijent uz $u^k$ da bismo dobili odgovarajući izraz; primjerice, za $\mathcal{A}=\operatorname{SEQ}_k(\mathcal{B})$ izravno dobivamo

$$
\begin{aligned}
&{}A(z,u)=\sum _ {k\geq 0}u^kB(z)^k=\frac{1}{1-uB(z)}\\
\implies &{}A(z)=B(z)^k
\end{aligned}
$$

Očito vrijedi i

$$
\mathcal{A}=\operatorname{SEQ}_{\geq k}(\mathcal{B})\implies A(z)=\frac{B(z)^k}{1-B(z)}
$$

a za $\operatorname{MSET} _ k(\mathcal{B})$ i $\operatorname{PSET} _ k(\mathcal{B})$ već imamo

$$
\begin{aligned}
&{}A(z,u)=\prod_n\left(1-uz^n\right)^{-b_n}\\
\implies &{}A(z)=\lbrack u^k\rbrack \exp\left(\frac{u}{1}B(z)+\frac{u^2}{2}B(z^2)+\frac{u^3}{3}B(z^3)+\cdots\right)
\end{aligned}
$$

i

$$
\begin{aligned}
&{}A(z,u)=\prod_n\left(1+uz^n\right)^{b_n}\\
\implies &{}A(z)=\lbrack u^k\rbrack \exp\left(\frac{u}{1}B(z)-\frac{u^2}{2}B(z^2)+\frac{u^3}{3}B(z^3)-\cdots\right)
\end{aligned}
$$

Za $\operatorname{CYC}_k(\mathcal{B})$ vrijedi analogno.

??? note "Izračun OGF-a za $\operatorname{MSET}_3(\mathcal{B})$ i $\operatorname{MSET}_4(\mathcal{B})$ pomoću gornjih formula"
    Pokušajmo izračunati $\mathcal{A}=\operatorname{MSET}_3(\mathcal{B})$:
    
    $$
    \begin{aligned}
    \lbrack u^3\rbrack A(z,u)&= \frac{1}{0!}\left(\lbrack u^3\rbrack 1\right)+\frac{1}{1!}\left(\lbrack u^3\rbrack \left(\frac{u}{1}B(z)+\frac{u^2}{2}B(z^2)+\frac{u^3}{3}B(z^3)+\cdots \right)\right)\\
    &+\frac{1}{2!}\left(\lbrack u^3\rbrack \left(\frac{u}{1}B(z)+\frac{u^2}{2}B(z^2)+\cdots \right)^2\right)\\
    &+\frac{1}{3!}\left(\lbrack u^3\rbrack \left(\frac{u}{1}B(z)+\cdots \right)^3\right)\\
    &=\frac{B(z)^3}{6}+\frac{B(z)B(z^2)}{2}+\frac{B(z)^3}{3}
    \end{aligned}
    $$
    
    Pokušajmo izračunati $\mathcal{A}=\operatorname{MSET}_4(\mathcal{B})$:
    
    $$
    \begin{aligned}
    \lbrack u^4\rbrack A(z,u)&= \frac{1}{0!}\left(\lbrack u^4\rbrack 1\right)+\frac{1}{1!}\left(\lbrack u^4\rbrack \left(\frac{u}{1}B(z)+\frac{u^2}{2}B(z^2)+\frac{u^3}{3}B(z^3)+\frac{u^4}{4}B(z^4)+\cdots \right)\right)\\
    &+\frac{1}{2!}\left(\lbrack u^4\rbrack \left(\frac{u}{1}B(z)+\frac{u^2}{2}B(z^2)+\frac{u^3}{3}B(z^3)+\cdots \right)^2\right)\\
    &+\frac{1}{3!}\left(\lbrack u^4\rbrack \left(\frac{u}{1}B(z)+\frac{u^2}{2}B(z^2)+\cdots \right)^3\right)\\
    &+\frac{1}{4!}\left(\lbrack u^4\rbrack \left(\frac{u}{1}B(z)+\cdots \right)^4\right)\\
    &=\frac{B(z^4)}{4}+\frac{1}{2!}\left(\frac{B(z^2)^2}{4}+\frac{2B(z)B(z^3)}{3}\right)+\frac{1}{3!}\left(\frac{3B(z)^2B(z^2)}{2}\right)+\frac{B(z)^4}{4!}\\
    &=\frac{B(z)^4}{24}+\frac{B(z)^2B(z^2)}{4}+\frac{B(z)B(z^3)}{3}+\frac{B(z^2)^2}{8}+\frac{B(z^4)}{4}
    \end{aligned}
    $$

Vidimo da je za $\mathcal{A}=\mathfrak{K}_k(\mathcal{B})$ funkcija $A(z)$ izraz u $B(z),B(z^2),\dots ,B(z^k)$.

Valja napomenuti da ograničena konstrukcija $\mathfrak{K}_k(\mathcal{B})$ ne zahtijeva $\mathcal{B}_0=\varnothing$.

???+ note "Često korištene ograničene konstrukcije"
    $$
    \begin{aligned}
    \operatorname{PSET} _ {2}(\mathcal{A})&:\quad \frac{A(z)^2}{2}-\frac{A(z^2)}{2}\\
    \operatorname{MSET} _ {2}(\mathcal{A})&:\quad \frac{A(z)^2}{2}+\frac{A(z^2)}{2}\\
    \operatorname{CYC} _ {2}(\mathcal{A})&:\quad \frac{A(z)^2}{2}+\frac{A(z^2)}{2}
    \end{aligned}
    $$
    
    $$
    \begin{aligned}
    \operatorname{PSET} _ {3}(\mathcal{A})&:\quad \frac{A(z)^3}{6}-\frac{A(z)A(z^2)}{2}+\frac{A(z^3)}{3}\\
    \operatorname{MSET} _ {3}(\mathcal{A})&:\quad \frac{A(z)^3}{6}+\frac{A(z)A(z^2)}{2}+\frac{A(z^3)}{3}\\
    \operatorname{CYC} _ {3}(\mathcal{A})&:\quad \frac{A(z)^3}{3}+\frac{2A(z^3)}{3}\\
    \end{aligned}
    $$
    
    $$
    \begin{aligned}
    \operatorname{PSET} _ {4}(\mathcal{A})&:\quad \frac{A(z)^4}{24}-\frac{A(z)^2A(z^2)}{4}+\frac{A(z)A(z^3)}{3}+\frac{A(z^2)^2}{8}-\frac{A(z^4)}{4}\\
    \operatorname{MSET} _ {4}(\mathcal{A})&:\quad \frac{A(z)^4}{24}+\frac{A(z)^2A(z^2)}{4}+\frac{A(z)A(z^3)}{3}+\frac{A(z^2)^2}{8}+\frac{A(z^4)}{4}\\
    \operatorname{CYC} _ {4}(\mathcal{A})&:\quad \frac{A(z)^4}{4}+\frac{A(z^2)^2}{4}+\frac{A(z^4)}{2}\\
    \end{aligned}
    $$

Gornji postupak računanja jest učinkovit, ali prilično mukotrpan; čitatelj može pročitati članke [Pólya Enumeration Theorem](https://mathworld.wolfram.com/PolyaEnumerationTheorem.html) i [Cycle Index](https://mathworld.wolfram.com/CycleIndex.html) na stranicama Wolfram MathWorld i srodne materijale. Potonji, ciklički indeks (Cycle Index), često se pojavljuje i u izrazima za funkcije izvodnice na OEIS-u.

???+ note "Primjer zadatka [LOJ 6538. 烷基计数 加强版 加强版 (Prebrojavanje alkilnih skupina, pojačana verzija, pojačana verzija)](https://loj.ac/p/6538)"
    **Zadatak**: Izračunajte broj neuređenih korijenskih stabala s $n$ čvorova u kojima stupanj korijena nije veći od $3$, a stupanj svakog drugog čvora nije veći od $4$, modulo $998244353$. Vrijedi $1\leq n\leq 10^5$.
    
    **Rješenje**: Neka je $\mathcal{T}$ ta kombinatorna klasa; tada je
    
    $$
    \mathcal{T}=\lbrace \bullet\rbrace\times\operatorname{MSET}_{0,1,2,3}(\mathcal{T})
    $$
    
    Ili, uvedemo li kombinatornu klasu $\hat{\mathcal{T}}=\mathcal{T}+\lbrace \epsilon\rbrace$, tada je
    
    $$
    \hat{\mathcal{T}}=\lbrace \epsilon\rbrace +\lbrace \bullet\rbrace\times\operatorname{MSET}_{3}(\hat{\mathcal{T}})
    $$
    
    što daje isti rezultat.

## Literatura

-   Philippe Flajolet and Robert Sedgewick. [Analytic Combinatorics](http://algo.inria.fr/flajolet/Publications/books.html).
