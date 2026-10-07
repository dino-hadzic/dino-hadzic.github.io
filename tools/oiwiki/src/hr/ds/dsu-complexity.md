---
title: Složenost union-finda
---

Ovaj je odjeljak preuzet i prilagođen iz [Vremenska složenost – kratko o analizi potencijala](https://www.luogu.com.cn/blog/Atalod/shi-jian-fu-za-du-shi-neng-fen-xi-qian-tan), uz dopuštenje izvornog autora.

## Definicije

### Ackermannova funkcija

Najprije dajemo definiciju $\alpha(n)$. Da bismo je dali, najprije definiramo $A_k(j)$.

Definiramo $A_k(j)$ kao:

$$
A_k(j)=\left\{
\begin{aligned}
&j+1& &k=0&\\
&A_{k-1}^{(j+1)}(j)& &k\geq1&
\end{aligned}
\right.
$$

To je Ackermannova funkcija.

Ovdje $f^i(x)$ označava $i$ uzastopnih primjena funkcije $f$ na $x$, tj. $f^0(x)=x$, $f^i(x)=f(f^{i-1}(x))$.

Zatim definiramo $\alpha(n)$ kao najmanji cijeli broj takav da je $A_{\alpha(n)}(1)\geq n$. Uočite da smo je ranije opisali kao $A_{\alpha(n)}(\alpha(n))\geq n$; u svakom slučaju obje rastu vrlo sporo i vrijednosti im ne prelaze 4.

### Osnovne definicije

Svaki čvor ima rank. Rank ovdje nije broj čvorova, nego dubina. Početni rank čvora je 0; pri spajanju, ako dva čvora imaju različit rank, čvor s manjim rankom spaja se na čvor s većim rankom, a rank većeg čvora se ne mijenja. Inače se nasumično jedan čvor spoji na drugi, a rank korijena poveća se za 1. Rank korijena tako daje visinu stabla. Rank čvora $x$ označavamo $rnk(x)$, a slično roditelja čvora $x$ označavamo $fa(x)$. Uvijek vrijedi $rnk(x)+1\leq rnk(fa(x))$.

Da bismo definirali funkciju potencijala, najprije definiramo pomoćnu funkciju $level(x)$, gdje je $level(x)=\max(k:rnk(fa(x))\geq A_k(rnk(x)))$. Kad je $rnk(x)\geq1$, definiramo još jednu pomoćnu funkciju $iter(x)=\max(i:rnk(fa(x))\geq A_{level(x)}^i(rnk(x))$. Za $x$ u tim definicijama vrijedi $rnk(x)>0$ i $x$ nije korijen nekog stabla.

Gornje vas definicije možda malo zbunjuju. Ponovimo: za $x$ i $fa(x)$, ako je $rnk(x)>0$, uvijek se može naći par $i,k$ takav da je $rnk(fa(x))\geq A_k^i(rnk(x))$; $level(x)=\max(k)$, a uz taj uvjet $iter(x)=\max(i)$. $level$ opisuje najveću razinu iteracije funkcije $A$, a $iter$ najveći broj iteracija na toj najvećoj razini.

Za te dvije funkcije vrijedi: $level(x)$ se tijekom operacija uvijek povećava ili ostaje isti, a ako se $level(x)$ ne poveća, $iter(x)$ se također samo povećava ili ostaje isti. Osim toga, uvijek zadovoljavaju sljedeće dvije nejednakosti:

$$
0\leq level(x)<\alpha(n)
$$

$$
1\leq iter(x)\leq rnk(x)
$$

S obzirom na definicije $level(x)$, $iter(x)$ i $A_k^j$, to je lako dokazati, pa to prepuštamo čitatelju kao vježbu za upoznavanje s definicijama.

Definiramo funkciju potencijala $\Phi(S)=\sum\limits_{x\in S}\Phi(x)$, gdje $S$ označava cijeli union-find, a $x$ čvor u njemu. Definiramo $\Phi(x)$ kao:

$$
\Phi(x)=
\begin{cases}
\alpha(n)\times \mathit{rnk}(x)& \mathit{rnk}(x)=0\ \text{ili je}\ x\ \text{korijen nekog stabla}\\
(\alpha(n)-\mathit{level}(x))\times \mathit{rnk}(x)-iter(x)& \text{inače}
\end{cases}
$$

Zatim preko promjena potencijala izazvanih operacijama dokazujemo da je amortizirana vremenska složenost $\Theta(\alpha(n))$. Uočite da operacija $union(x,y)$ koju ovdje razmatramo jamči da su $x$ i $y$ korijeni nekih stabala, pa ne treba dodatno izvoditi $find(x)$ i $find(y)$.

Vidimo da je potencijal uvijek nenegativan. Osim toga, na početku je potencijal union-finda $0$.

## Dokaz

### Operacija union(x,y)

Njezino je vrijeme $\Theta(1)$, pa razmatramo promjenu potencijala koju izaziva.

Pretpostavimo $rnk(x)\leq rnk(y)$, tj. $x$ se spaja na $y$. Tada se potencijal može povećati samo čvorovima $x$ (od korijena postaje ne-korijen), $y$ (rank se može povećati) i djeci čvora $y$ prije operacije (rank roditelja može se povećati). Najprije dokazujemo da se potencijal djeteta $c$ čvora $y$ prije operacije ne može povećati, a ako se smanji, smanji se barem za $1$.

Neka je potencijal čvora $c$ prije operacije $\Phi(c)$, a nakon operacije $\Phi(c')$; ovdje $c$ može biti bilo koji ne-korijenski čvor s $rnk(c)>0$, a operacija bilo koja operacija, uključujući operaciju find u nastavku. Razlikujemo tri slučaja.

1.  $iter(c)$ i $level(c)$ nisu se povećali. Očito $\Phi(c)=\Phi(c')$.
2.  $iter(c)$ se povećao, $level(c)$ nije. Tada se $iter(c)$ povećao barem za jedan, tj. $\Phi(c')\leq \Phi(c)-1$: funkcija potencijala se smanjila, i to barem za 1.
3.  $level(c)$ se povećao, a $iter(c)$ se možda smanjio. No zbog $0<iter(c)\leq rnk(c)$, $iter(c)$ se smanji najviše za $rnk(c)-1$, dok se $level(c)$ poveća barem za $1$. Iz definicije $\Phi(c)=(\alpha(n)-level(c))\times rnk(c)-iter(c)$ slijedi $\Phi(c')\leq\Phi(c)-1$.
4.  Ostali slučajevi. Budući da se $rnk(c)$ ne mijenja, a $rnk(fa(c))$ se ne smanjuje, oni ne postoje.

Dakle, potencijal se može povećati samo čvorovima $x$ ili $y$. Čvor $x$ od korijena postaje ne-korijen; ako je $rnk(x)=0$, uvijek vrijedi $\Phi(x)=\Phi(x')=0$. Inače sigurno vrijedi $\alpha(x)\times rnk(x)\geq(\alpha(n)-level(x))\times rnk(x)-iter(x)$, tj. $\Phi(x')\leq \Phi(x)$.

Stoga je jedini čvor kojem se potencijal može povećati $y$, a potencijal čvora $y$ poveća se najviše za $\alpha(n)$. Slijedi da je amortizirana vremenska složenost operacije $union$ jednaka $\Theta(\alpha(n))$.

### Operacija find(a)

Ako put pretraživanja sadrži $\Theta(s)$ čvorova, vremenska složenost pretraživanja očito je $\Theta(s)$. Ako zbog operacije pretraživanja nijednom čvoru ne raste potencijal, a barem $s-\alpha(n)$ čvorova potencijal smanji barem za $1$, dokazano je da je vremenska složenost operacije $find(a)$ jednaka $\Theta(\alpha(n))$. Da ne bi došlo do zabune, ovdje kao argument koristimo $a$, dok $x$ općenito označava neki čvor union-finda.

Najprije dokazujemo da se nijednom čvoru ne povećava potencijal. Očito: gore smo dokazali da se potencijal ne-korijenskih čvorova ne povećava, a $rnk$ korijena se ne mijenja, pa se nijednom čvoru potencijal ne povećava.

Zatim dokazujemo da se barem $s-\alpha(n)$ čvorova potencijal smanji barem za $1$. Gore smo dokazali da se potencijal čvora smanji barem za $1$ ako se $level(x)$ ili $iter(x)$ promijeni. Dakle, dovoljno je dokazati da se barem $s-\alpha(n)$ čvorova $level(x)$ ili $iter(x)$ promijeni.

Prisjetimo se definicije potencijala ne-korijenskog čvora, $\Phi(x)=(\alpha(n)-level(x))\times rnk(x)-iter(x)$, gdje su $level(x)$ i $iter(x)$ najveći brojevi takvi da je $rnk(fa(x))\geq A_{level(x)}^{iter(x)}(rnk(x))$.

Ako $root_x$ označava korijen stabla u kojem je $x$, dovoljno je dokazati $rnk(root_x)\geq A_{level(x)}^{iter(x)+1}(rnk(x))$. Prema definiciji $A_k^i$ vrijedi $A_{level(x)}^{iter(x)+1}(rnk(x))=A_{level(x)}(A_{level(x)}^{iter(x)}(rnk(x)))$.

Napomena: $k(x)$ može označavati $level(x)$, a $i(x)$ $iter(x)$, da izrazi ne bi bili predugi. Ovdje to znači $rnk(root_x)\geq A_{k(x)}(A_{k(x)}^{i(x)}(x))$.

Kad ovo pročitate, možda ćete pomisliti „što je sad ovo”. To znači da biste možda trebali pročitati još nekoliko puta ili preskočiti dio i vratiti mu se poslije.

Ovdje nam treba još jedan vanjski $A_{k(x)}$, što znači da možda trebamo naći još jedan čvor $y$. Neka je $y$ čvor na putu pretraživanja nakon $x$ za koji vrijedi $k(y)=k(x)$; „nakon na putu pretraživanja” znači „predak od $x$”. Očito nema svaki $x$ takav $y$. Lako se dokazuje da čvorova $x$ bez takvog $y$ ima najviše $\alpha(n)+2$, jer takav $y$ nemaju samo posljednji $x$ za svaki $k$ te $a$ i $root_a$.

Još jednom naglašavamo da $fa(x)$ označava roditelja čvora $x$ **prije** kompresije puta, a roditelja čvora $x$ **nakon** kompresije puta uvijek označavamo $root_x$. Za svaki $x$ za koji postoji $y$ uvijek vrijedi $rnk(y)\geq rnk(fa(x))$. Istodobno imamo $rnk(fa(x))\geq A_{k(x)}^{i(x)}(rnk(x))$. Budući da je $k(x)=k(y)$, oboje označavamo s $k$, tj. $rnk(fa(x))\geq A_k^{i(x)}(rnk(x))$. Trebamo konstruirati jedan $A_k$, pa se ne moramo obazirati na vrijednost $iter(y)$ i izravno koristimo oslabljenu verziju $rnk(fa(y))\geq A_k(rnk(y))$.

Ako nejednakosti spojimo, događa se nešto čarobno. Dobivamo $rnk(fa(y))\geq A_k^{i(x)+1}(rnk(x))$. Drugim riječima, iterirajući od $rnk(x)$ prema $rnk(fa(y))$, $A_k$ se može primijeniti barem $i(x)+1$ puta a da se ne premaši $rnk(fa(y))$.

Očito vrijedi $rnk(root_y)\geq rnk(fa(y))$, a $rnk(x)$ se pri kompresiji puta ne mijenja. Stoga dobivamo $rnk(root_x)\geq A_k^{i(x)+1}(rnk(x))$, tj. vrijednost $iter(x)$ povećava se barem za 1, a ako se $rnk(x)$ nije povećao, onda se sigurno povećao $level(x)$.

Dakle, $\Phi(x)$ se smanjio barem za 1. Budući da takvih čvorova $x$ ima barem $s-\alpha(n)-2$, $\Phi(S)$ se na kraju smanji barem za $s-\alpha(n)-2$, pa je amortizirana vremenska složenost $\Theta(\alpha(n)+2)=\Theta(\alpha(n))$.

## Zašto union-find može biti „srušen” posebnim testovima

Pitanje je zapravo: ako ne spajamo po ranku, koja se svojstva narušavaju tako da se vremenska složenost union-finda ne može zajamčiti kao $\Theta(m\alpha(n))$?

Ako pri spajanju čvor s većim $rnk$ spojimo na čvor s manjim $rnk$, tada $rnk$ čvora s manjim $rnk$ postavimo na $rnk$ drugog čvora uvećan za jedan. Tako jamčimo $rnk(fa(x))\geq rnk(x)+1$, pa ne dolazi do narušavanja svojstava nalik „compile erroru posvuda”.

Očito je da u tom slučaju narušavamo tvrdnju iz analize funkcije $union(x,y)$ da se „potencijal čvora $y$ poveća najviše za $\alpha(n)$”.

Postoji struktura koja vremensku složenost union-finda s kompresijom puta spušta na $\Omega(m\log_{1+\frac{m}{n}}n)$; definirana je ovako:

binomno stablo (zapravo se malo razlikuje od običnog binomnog stabla), gdje je $j$ konstanta, a $T_k$ je $T_{k-1}$ kojem je kao dijete korijena dodan $T_{k-j}$.

![Binomno stablo](./images/dsu-complexity.svg)

Rubni uvjet: $T_1$ do $T_j$ su pojedinačni čvorovi.

Neka je $rnk(T_k)=r_k$; tada je $r_k=(k-1)/j$ (dokaz izostavljen). U svakoj rundi operacija spojimo ga na jedan samostalan čvor, a zatim pretražimo $j$ čvorova na dnu. Drugim riječima, kad ga spojimo na samostalni čvor, potencijal tog čvora poraste za $(k-1)/j+1$. Za $j=\lfloor\frac{m}{n}\rfloor$, $i=\lfloor\log_{j+1}\frac{n}{2}\rfloor$, $k=ij$ porast potencijala iznosi:

$$
\alpha(n)\times((ij-1)/j+1)=\alpha(n)\times((\lfloor\log_{\lfloor\frac{m}{n}\rfloor+1}\frac{n}{2}\rfloor\times \lfloor\frac{m}{n}\rfloor-1)/\lfloor\frac{m}{n}\rfloor+1)
$$

Preoblikovanjem i uklanjanjem svih zaokruživanja dobivamo da je porast potencijala $\geq \alpha(n)\times(\log_{1+\frac{m}{n}}n-\frac{n}{m})$, što za $m$ operacija daje $\Omega(m\log_{1+\frac{m}{n}}n-n)=\Omega(m\log_{1+\frac{m}{n}}n)$.

## O heurističkom spajanju

Budući da je spajanje po ranku teže napisati od heurističkog spajanja, mnogi iskusni natjecatelji union-find pišu s heurističkim spajanjem. Konkretno, za svaki korijen održava se $size(x)$ i svaki se put manji $size$ spaja na veći.

Može li se, dakle, heurističko spajanje „srušiti”?

Najprije to možemo objasniti svojstvima ranka koja sudjeluju u dokazu. Ako $size$ može preuzeti ulogu $rnk$, heurističko spajanje može se koristiti. Ukratko, svojstva ranka koja sudjeluju u dokazu su sljedeća tri:

1.  Pri svakom spajanju rank se poveća najviše jednom čvoru, i to najviše za 1.
2.  Uvijek vrijedi $rnk(fa(x))\geq rnk(x)+1$.
3.  Rank čvora se ne smanjuje.

Drugo i treće svojstvo $siz$ očito zadovoljava, ali prvo ne: ako $x$ spojimo na $y$, $siz(y)$ se poveća za $siz(x)$.

Zato možemo razmotriti zamjenu $rnk(x)$ s $\log_2 siz(x)$.

Što se tiče prvog svojstva, budući da se $siz$ čvora najviše udvostruči, $\log_2 siz(x)$ poraste najviše za 1. Za drugo i treće svojstvo zaključak je prilično očit, pa dokaz izostavljamo.

Dakle, ako ne želite pisati spajanje po ranku, pišite heurističko spajanje; vremenska složenost i dalje je $\Theta(m\alpha(n))$.
