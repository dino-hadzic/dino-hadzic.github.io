---
title: WQS binarno pretraživanje
---

## Uvod

Ovaj članak predstavlja metodu optimizacije zadataka dinamičkog programiranja pomoću WQS binarnog pretraživanja. U različitim se tekstovima ona naziva i težinskim binarnim pretraživanjem, konveksnom optimizacijom DP-a, DP-om s potpunom konveksnom monotonošću, metodom Lagrangeovih multiplikatora i sl., a izvan Kine poznata je i kao Aliens Trick. Prvi ju je sažeo Wang Qinshi u radu „浅析一类二分方法” (Kratka analiza jedne klase metoda binarnog pretraživanja).

WQS binarno pretraživanje obično se koristi za rješavanje ove klase optimizacijskih problema: imaju ograničenje na broj, pa ih je skupo rješavati izravno; no čim se to ograničenje ukloni, problem postaje znatno lakši.

Na primjer, pretpostavimo da treba od $n$ predmeta odabrati $m$ i optimizirati neku složeniju funkciju cilja. Ako s $f(i,j)$ označimo optimalnu vrijednost funkcije cilja kad od prvih $i$ predmeta odaberemo $j$, odgovor na izvorni problem je $f(n,m)$. U takvim je problemima jednadžba prijelaza stanja obično dvodimenzionalna. Izravna implementacija te jednadžbe prijelaza ima vremensku složenost $O(nm)$, što je neprihvatljivo.

Pretpostavimo nadalje da je optimizacijski problem bez ograničenja na broj lako riješiti. Međutim, optimalan broj odabranih predmeta ne mora zadovoljavati ograničenje izvornog problema. Recimo da je odabrano previše predmeta. Tada možemo pri odabiru svakom odabranom predmetu pridružiti fiksnu kaznu $k$ (to je „težina” u nazivu „težinsko binarno pretraživanje”) i i dalje rješavati optimizacijski problem bez ograničenja na broj. Ovisno o vrijednosti $k$, optimalan broj odabranih predmeta mijenjat će se; štoviše, s promjenom $k$ optimalan se broj mijenja monotono. Stoga binarnim pretraživanjem možemo naći $k$ za koji je optimalan broj odabranih predmeta točno $m$. Ako je tada optimalna vrijednost funkcije cilja $f_k(n)$, dovoljno je poništiti gubitak vrijednosti uzrokovan dodanom kaznom i dobivamo odgovor izvornog problema $f(n,m)=f_k(n)-km$. Ako je složenost jednog rješavanja problema s kaznom $O(T(n))$, ukupna se složenost algoritma smanjuje na $O(T(n)\log L)$, gdje je $O(\log L)$ broj koraka binarnog pretraživanja po $k$.

To je osnovna ideja WQS binarnog pretraživanja. No da bi ta ideja radila, preduvjet je da je $f(n,m)$ konveksna u $m$. Inače možda ne postoji kazna $k$ za koju je optimalan broj točno $m$. Zato se ova metoda optimizacije DP-a često naziva „konveksnom optimizacijom DP-a” ili „DP-om s potpunom konveksnom monotonošću”.

## Tradicionalna metoda

Neka je neprazan skup $X$ (konačan) prostor odluka, $f:X\rightarrow\mathbf R$ funkcija cilja, a $g:X\rightarrow\mathbf R^d$ dodatna funkcija kojom se nameće ograničenje. Problem koji treba riješiti možemo shvatiti kao računanje vrijednosti funkcije vrijednosti $v(y)$ sljedećeg optimizacijskog problema u nekoj točki:

$$
\begin{aligned}
v(y)=\min_{x\in X}\;&f(x)\\
\text{subject to }&g(x)=y.
\end{aligned}
$$

Na primjer, za gore spomenuti problem s ograničenjem broja, $X$ možemo shvatiti kao familiju svih podskupova skupa predmeta, $x\in X$ je jedan podskup, $f(x)$ je vrijednost tog podskupa, a $g(x)$ je broj elemenata podskupa $x$. Naravno, $g(x)$ ne mora biti samo ograničenje na broj; u nastavku su navedeni primjeri općenitijih ograničenja.

???+ info "Dogovor"
    Radi jednostavnosti izlaganja, u ovom se članku razmatraju samo problemi minimizacije funkcije cilja. Problemi maksimizacije analogni su, samo što (dolje) konveksne funkcije iz ovog članka treba zamijeniti konkavnim funkcijama (ili gore konveksnim). Alternativno, dodavanjem predznaka minus problem maksimizacije funkcije cilja može se pretvoriti u problem minimizacije njezine suprotne vrijednosti.

### Geometrijska intuicija

Budući da je većina problema s natjecanja iz kombinatorne optimizacije, prostor odluka $X$ obično nema dobru strukturu, pa umjesto njega možemo promatrati skup

$$
\mathcal D = \{(g(x),f(x))\in\mathbf R^d\times\mathbf R:x\in X\}.
$$

Tradicionalnom se metodom uglavnom rješava slučaj $d=1$, tj. slučaj s jednim ograničenjem. Donja slika prikazuje jedan mogući izgled skupa točaka $\mathcal D$ u tom slučaju.

![](../images/wqs-binary-search/wqs-f-g-space.svg)

Crvene i plave točke na slici čine skup $\mathcal D$, dobiven projekcijom svih mogućih odabira iz $X$ na ravninu $(g(x),f(x))$. Izvorni problem traži, među točkama s apscisom $y$, najmanju ordinatu $v(y)$. Kad $y$ varira, sve takve točke $(y,v(y))$ čine skup crvenih točaka na slici.

Da bismo dobili ordinatu točke $(y,v(y))$, možemo skup $\mathcal D$ „rezati” pravcem nagiba $\lambda\in\mathbf R$. Kao što slika pokazuje, kad je nagib pravca prikladno odabran, pravac kroz točku $(y,v(y))$ ima najmanji odsječak $f(x)-\lambda g(x)$ među svim pravcima nagiba $\lambda$ koji prolaze točkama skupa $\mathcal D$. Taj minimum označimo s

$$
h(\lambda) = \min_{x\in X}f(x)-\lambda g(x).
$$

Budući da $(y,v(y))$ također leži na tom pravcu, dobivamo rješenje izvornog problema

$$
v(y) = h(\lambda) + \lambda y.
$$

Pretpostavimo da je za sve $\lambda$ u razumnom rasponu gornju funkciju $h(\lambda)$ lako izračunati. Na natjecanjima to često vrijedi, jer je ograničenje izvornog problema uklonjeno. Tada su dva najvažnija pitanja:

1.  postoji li nagib pravca $\lambda$ takav da se minimum odsječka postiže upravo u točki $(y,v(y))$, i
2.  ako postoji, kako naći takav nagib $\lambda$.

Prvo je pitanje razmjerno lako. Kad se nagib $\lambda$ mijenja, skup koji svi ti pravci „izrezuju” (tj. presjek odgovarajućih gornjih poluravnina) nužno je konveksan skup. Stoga ti pravci mogu proći nekom točkom ako i samo ako ta točka leži na donjoj konveksnoj ljusci tog skupa. To je ekvivalentno tome da je funkcija $v(y)$ [konveksna](./slope-trick.md#离散点集上的凸函数).

Drugo je pitanje suptilnije. Budući da već znamo da je apscisa tražene točke $y$, prirodna je ideja pri računanju $h(\lambda)$ usput izračunati vrijednost funkcije ograničenja $g(x)$ u trenutnom optimalnom rješenju $x_\lambda$. Na primjer, u gore spomenutom primjeru, pri rješavanju problema s kaznom možemo zabilježiti broj odabranih predmeta u optimalnom rješenju funkcije cilja s kaznom. Zatim usporedimo $g(x_\lambda)$ sa željenim $y$ i u skladu s tim prilagodimo vrijednost $\lambda$ za sljedeći izračun. To je najtradicionalnija metoda WQS binarnog pretraživanja.

Ukratko, osnovni tijek tradicionalnog WQS binarnog pretraživanja je sljedeći:

1.  na početku odaberemo razuman interval za $\lambda$;
2.  u trenutnom intervalu odaberemo neki $\lambda$;
3.  riješimo problem s kaznom $h(\lambda)=\min_{x\in X}f(x)-\lambda g(x)$ i zabilježimo vrijednost $g(x_\lambda)$ funkcije $g(x)$ u njegovu optimalnom rješenju $x_\lambda$;
4.  ako je $g(x_\lambda)=y$, dobili smo optimalnu vrijednost izvornog problema $v(y)=h(\lambda)+\lambda y$ i algoritam odmah završava;
5.  inače, ovisno o odnosu $g(x_\lambda)$ i $y$, prilagodimo interval za $\lambda$ i vratimo se na korak 2.

Ovaj osnovni tijek već je dovoljan za rješavanje nekih zadataka, ali nije potpun. U nastavku razmatramo poboljšanja tog osnovnog tijeka.

### Obrada kolinearnog slučaja

Pri primjeni osnovnog tijeka prvi problem na koji nailazimo jest da se kolinearni slučaj ne obrađuje ispravno.

Ako na donjoj konveksnoj ljusci skupa točaka $\mathcal D$ postoje tri ili više kolinearnih crvenih točaka, u gornjem osnovnom tijeku možda nećemo moći ispravno odrediti odnos $g(x_\lambda)$ i $y$. Neka su, na primjer, apscise triju kolinearnih crvenih točaka $y_1,y_2,y_3$, a nagib pravca na kojem leže $\lambda^*$. Da bismo ispravno izračunali $v(y_2)$, moramo osigurati da je posljednji problem izračunat pri završetku algoritma upravo $h(\lambda^*)$, jer je $\lambda^*$ jedini nagib pravca koji pri minimizaciji odsječka može proći točkom $(y_2,v(y_2))$. No pri rješavanju $h(\lambda^*)$ zabilježeni $g(x_{\lambda^*})$ može biti bilo koji od $y_1,y_2,y_3$. Ako zabilježeni $g(x_{\lambda^*})$ nije jednak $y_2$, algoritam će pogrešno nastaviti i prilagođavati interval za $\lambda$ u smjeru suprotnom od $y_2$, što na kraju daje pogrešan rezultat.

Jedan način rješavanja kolinearnog slučaja jest da pri bilježenju $g(x_\lambda)$ za optimalno rješenje $x_\lambda$ uvijek uzimamo što veću (ili što manju) vrijednost. Istodobno, uvjet zaustavljanja binarnog pretraživanja mijenjamo iz traženja $\lambda$ za koji je točno $g(x_\lambda)=y$ u traženje najmanjeg (ili najvećeg) $\lambda$ za koji vrijedi $g(x_\lambda)\ge y$ (ili $g(x_\lambda)\le y$). U primjeru iz prethodnog odlomka to znači da pri računanju problema $h(\lambda^*)$ izlaz $g(x_{\lambda^*})$ bude $y_3$. Time je osigurano da je posljednji izračunati problem pri završetku algoritma $h(\lambda^*)$. Pri implementaciji ove metode treba paziti da se na kraju ne ispisuje $h(\lambda)+\lambda g(x_{\lambda})$ nego $h(\lambda)+\lambda y$, jer zabilježeni $g(x_\lambda)$ ne mora biti jednak stvarnom ograničenju $y$.

Drugi je način binarno pretraživanje po realnim brojevima. Ako su svi brojevi u problemu cijeli, očito je i nagib u WQS binarnom pretraživanju cijeli broj. Uvođenje realnih brojeva u binarno pretraživanje služi tome da se, ako pogrešno isključimo ispravnu opciju $\lambda^*$, pomoću decimalnog dijela možemo vratiti i na kraju približiti točnom odgovoru $\lambda^*$. Na primjer, u gornjem primjeru, ako je pri računanju problema $h(\lambda^*)$ zabilježeni $g(x_{\lambda^*})$ jednak $y_1$, što je manje od željenog $y_2$, algoritam će se prebaciti na interval $(\lambda^*,\lambda_r]$, gdje je $\lambda_r$ desni kraj intervala u kojem se nalazi $\lambda$. U cjelobrojnom slučaju taj bi interval zapravo trebalo zapisati kao $[\lambda^*+1,\lambda_r]$, čime se isključuje mogućnost da se u nastavku algoritma približimo točnom odgovoru $\lambda^*$. No pri realnom binarnom pretraživanju razmatrani je interval i dalje $(\lambda^*,\lambda_r]$, a za $\lambda$ iz tog intervala zabilježeni $g(x_\lambda)$ pri rješavanju $h(\lambda)$ uvijek je barem $y_3$, dakle strogo veći od $y_2$. Zato će algoritam, kako napreduje, stalno odbacivati desnu polovicu intervala, pa je konačni raspon za $\lambda$ zajamčeno blizu $\lambda^*$. Naravno, budući da već znamo da je traženi nagib cijeli broj, preciznost pri završetku realnog binarnog pretraživanja ne mora biti velika; dovoljno je da interval sadrži samo jedan cijeli broj, a taj je cijeli broj traženi $\lambda^*$.

Nakon ispravne obrade kolinearnog slučaja, WQS binarno pretraživanje dovoljno je za rješavanje velike većine zadataka s WQS binarnim pretraživanjem koji se pojavljuju na natjecanjima. No ta metoda i dalje ima nedostatke: ne može obraditi slučajeve u kojima je $g(x_\lambda)$ teško zabilježiti, niti slučaj višestrukih komplanarnih točaka u višedimenzionalnom WQS binarnom pretraživanju. U ovom ćemo članku dalje proučiti svojstva optimizacijskog problema $v(y)$ i predložiti općenitiji pristup.

## Dualna metoda

U ovom se odjeljku predstavlja implementacija WQS binarnog pretraživanja koja zahtijeva samo da se za sve $\lambda\in\mathbf R^d$ može učinkovito izračunati vrijednost

$$
h(\lambda) = \min_{x\in X}f(x)-\lambda\cdot g(x)
$$

te da je optimalna vrijednost izvornog problema $v(y)$ konveksna funkcija od $y\in\mathbf R^d$[^high-d-convex]. Ukratko, u ovom ćemo odjeljku dokazati da je funkcija vrijednosti izvornog problema $v(y)$ jednaka optimalnoj vrijednosti njegova dualnog problema

$$
v^\star(y) = \sup_{\lambda\in\mathbf R^d} h(\lambda)+\lambda\cdot y,
$$

a funkcija cilja dualnog problema konkavna je funkcija od $\lambda\in\mathbf R^d$, dakle unimodalna, pa se može učinkovito riješiti [ternarnim pretraživanjem](../../basic/binary.md#三分法) ili [metodom zlatnog reza](../../basic/binary.md#优化黄金分割法), uz složenost i dalje $O(T(n)\log^d L)$. Time su potpuno riješeni problemi koji se mogu pojaviti pri bilježenju vrijednosti $g(x_\lambda)$ u tradicionalnoj metodi WQS binarnog pretraživanja, a ujedno se ideja WQS binarnog pretraživanja može primijeniti na višedimenzionalni slučaj.

Osim toga, u ovom se odjeljku pokazuje da se raspon $g(x_\lambda)$ može dobiti iz $h(\lambda)$, bez dodatnog bilježenja pri rješavanju $h(\lambda)$. Na primjer, za $d=1$ i problem koji uključuje samo cijele brojeve može se dokazati da je raspon vrijednosti $g(x_\lambda)$ upravo

$$
[h(\lambda-1)-h(\lambda),h(\lambda)-h(\lambda+1)].
$$

To zapravo daje još jedan način rješavanja kolinearnog problema i za zadatke u kojima se mora koristiti gore opisani tijek binarnog pretraživanja.

U nastavku ćemo te tvrdnje dokazati teorijom konveksne analize. Za konkretne primjene ovih metoda pogledajte odjeljak [Primjeri zadataka](#primjeri-zadataka).

### Lagrangeova dualnost

Razmotrimo rješavanje problema [metodom Lagrangeovih multiplikatora](https://en.wikipedia.org/wiki/Lagrange_multiplier). Uvedemo Lagrangeov multiplikator $\lambda\in\mathbf R^d$; lagranžijan se tada može zapisati kao

$$
L(x,\lambda,y) = f(x) - \lambda\cdot g(x)+\lambda\cdot y.
$$

Budući da čim je neka komponenta od $g(x)-y$ različita od nule možemo pustiti odgovarajuću komponentu od $\lambda$ u (pozitivnu ili negativnu) beskonačnost, vrijedi

$$
\sup_{\lambda\in\mathbf R^d}L(x,\lambda,y)
= \begin{cases}
f(x),&g(x)=y,\\
+\infty,&\text{otherwise}.
\end{cases}
$$

To znači da se izvorni problem može zapisati kao

$$
\begin{aligned}
v(y) &= \min_{x\in X}\sup_{\lambda\in\mathbf R^d}L(x,\lambda,y).
\end{aligned}
$$

Zamjenom redoslijeda dviju operacija ekstrema dobivamo njegov [dualni problem](https://en.wikipedia.org/wiki/Duality_%28optimization%29):

$$
\begin{aligned}
v^\star(y)&=\sup_{\lambda\in\mathbf R^d}\min_{x\in X}L(x,\lambda,y)\\
&=\sup_{\lambda\in\mathbf R^d}h(\lambda)+\lambda\cdot y.
\end{aligned}
$$

Uskoro ćemo pokazati da uz uvjet da je $v(y)$ konveksna funkcija od $y$ vrijedi jaka dualnost (strong duality), tj. $v^\star(y)=v(y)$.

### Konveksna konjugata

Da bismo dokazali jaku dualnost, trebamo pojam konveksne konjugate.

???+ abstract "Konveksna konjugata"
    Za funkciju $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ njezina **konveksna konjugata** (convex conjugate), ili **Legendre–Fenchelova transformacija** (Legendre–Fenchel transformation), jest funkcija
    
    $$
    f^*(x^*) = \sup_{x\in\mathbf R^d}x^*\cdot x - f(x).
    $$

Gledano kao funkcija varijable $x^*$, $f^*(x^*)$ je supremum familije linearnih funkcija, pa je nužno konveksna funkcija na $\mathbf R^d$.

???+ info "„Vektor nagiba” i „odsječak” hiperravnine"
    Jednadžbe hiperravnina u vektorskom prostoru $\mathbf R^{d+1}$ koje se razmatraju u ovom članku sve su oblika
    
    $$
    y = k\cdot x + b.
    $$
    
    Drugim riječima, članak ne razmatra hiperravnine paralelne s osi $y$. Radi jednostavnosti izražavanja, u članku se $k$ nestrogo naziva „vektorom nagiba” te hiperravnine, a $b$ njezinim „odsječkom”. Zapisana u standardnijem obliku, jednadžba te hiperravnine glasi
    
    $$
    k\cdot x - y = -b.
    $$
    
    Jedan njezin vektor normale je $(k,-1)$. Dakle, takozvani vektor nagiba zapravo su prvih $d$ komponenata vektora normale hiperravnine normiranog tako da mu je posljednja komponenta jednaka $-1$.

Geometrijski gledano, konveksna konjugata funkcije $f(x)$ opisuje sljedeće: među svim hiperravninama s vektorom nagiba $x^*$ koje sijeku epigraf funkcije $f(x)$

$$
\operatorname{epi}f = \{(x,y)\in\mathbf R^d\times\mathbf R:f(x)\le y\}
$$

najmanji odsječak $f(x)-x^*\cdot x$ jednak je $-f^*(x^*)$. Drugim riječima, funkcija $f(x)$ uvijek je iznad hiperravnine $y = x^*\cdot x-f^*(x^*)$ i dodiruje je u točki $(x_0,f(x_0))$; naravno, može postojati i drugih dirališta. Takva se hiperravnina zove **potporna hiperravnina** (supporting hyperplane) funkcije $f(x)$ u $x_0$. Odsječak potporne hiperravnine funkcije $f(x)$ jednoznačno je određen njezinim vektorom nagiba, a konveksna konjugata upravo daje to preslikavanje iz vektora nagiba u odsječak.

Minimizirati $f(x)-\lambda\cdot g(x)$ na skupu $X$ ekvivalentno je minimiziranju $v(y)-\lambda\cdot y$ na skupu $\{(y,v(y))\}$:

$$
\begin{aligned}
\min_x f(x)-\lambda\cdot g(x) &= \min_{y\in g(X)}\left(\min_{x\in X:g(x)=y} f(x) - \lambda\cdot g(x)\right)\\
&= \min_{y\in g(X)}\left(\min_{x\in X:g(x)=y} f(x)\right) - \lambda\cdot y \\
&= \min_{y\in g(X)}v(y) - \lambda\cdot y.
\end{aligned}
$$

Stoga vrijedi

$$
h(\lambda) = \min_{y\in g(X)}v(y) - \lambda\cdot y = -v^*(\lambda).
$$

To pokazuje da je $h(\lambda)$ konkavna funkcija od $\lambda\in\mathbf R^d$. Nadalje,

$$
v^\star(y) = \sup_{\lambda\in\mathbf R^d}\lambda\cdot y-v^*(\lambda) = v^{**}(y).
$$

Drugim riječima, funkcija vrijednosti dualnog problema $v^{\star}(y)$ dvostruka je konveksna konjugata funkcije vrijednosti izvornog problema $v(y)$, koja se naziva i **bikonjugata** (biconjugate).

Problem se tako svodi na pitanje: koje funkcije $v(y)$ zadovoljavaju da im je bikonjugata jednaka njima samima? Odgovor daje sljedeći teorem:

???+ note "Teorem (Fenchel–Moreau)"
    Za funkciju $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ bikonjugata je jednaka njoj samoj, tj. $f^{**}=f$, ako i samo ako je ispunjen jedan od sljedeća tri uvjeta:
    
    1.  $f(x)$ je prava konveksna funkcija i [odozdo poluneprekidna](https://en.wikipedia.org/wiki/Semi-continuity),
    2.  $f(x)\equiv+\infty$, ili
    3.  $f(x)\equiv-\infty$.

??? note "Dokaz"
    Funkcija je prava (proper) ako i samo ako nikad ne poprima vrijednost $-\infty$ i nije identički jednaka $+\infty$.
    
    Za neprave funkcije lako se provjerava da su $f(x)\equiv+\infty$ i $f(x)\equiv-\infty$ međusobno konjugirane. Osim toga, čim $f(x)$ u bilo kojoj točki poprimi $-\infty$, nužno je $f^*(x^*)\equiv+\infty$. Dakle, jedine neprave funkcije koje zadovoljavaju $f^{**}=f$ jesu ta dva slučaja. Rasprava u nastavku ograničena je na prave funkcije. Za prave funkcije uvjet da je odozdo poluneprekidna i konveksna ekvivalentan je tome da joj je epigraf zatvoren konveksan skup.
    
    Nužnost uvjeta je jednostavna. Budući da je $f=f^{**}$ konveksna konjugata od $f^*$, kao supremum familije linearnih funkcija njezin je epigraf presjek familije zatvorenih konveksnih skupova, pa je nužno zatvoren konveksan skup. To pokazuje da prava funkcija koja zadovoljava $f^{**}=f$ mora biti odozdo poluneprekidna i konveksna.
    
    Obratno, ti su uvjeti i dovoljni. Kao i kod drugih teorema o jakoj dualnosti, dokaz se dijeli u dva koraka.
    
    U prvom koraku pokazujemo da vrijedi slaba dualnost, tj. $f(x)\ge f^{**}(x)$. Iz definicije konveksne konjugate slijedi da za sve $x,x^*\in\mathbf R^d$ vrijedi
    
    $$
    f^*(x^*) \ge x^*\cdot x-f(x).
    $$
    
    To znači da za sve $x,x^*\in\mathbf R^d$ vrijedi i
    
    $$
    f(x) \ge x^*\cdot x-f^*(x^*).
    $$
    
    Uzimanjem supremuma po $x^*$ na desnoj strani nejednakosti dobivamo $f(x)\ge f^{**}(x)$.
    
    U drugom koraku pomoću [teorema o separaciji hiperravninom](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem) pokazujemo $f(x)\le f^{**}(x)$. Pretpostavimo suprotno: postoji $x_0\in\mathbf R^d$ takav da je $f(x_0)>f^{**}(x_0)$. Budući da je epigraf $\operatorname{epi}(f)$ funkcije $f(x)$ zatvoren konveksan skup, a jednočlani skup $\{(x_0,f^{**}(x_0))\}$ kompaktan konveksan skup, prema teoremu o separaciji hiperravninom postoje $(\lambda,t)\in\mathbf R^d\times\mathbf R$ i $\alpha\in\mathbf R$ takvi da za sve $x\in\operatorname{dom} f:=\{x\in\mathbf R^d:f(x)<+\infty\}$ i sve $y\ge f(x)$ vrijedi
    
    $$
    \lambda\cdot x-ty <\alpha <\lambda\cdot x_0 - tf^{**}(x_0)
    $$
    
    Budući da $y$ može biti proizvoljno velik, nužno je $t\ge 0$. To se opet dijeli na dva slučaja.
    
    Najprije razmotrimo slučaj $t>0$. Tada sve dijelove nejednakosti podijelimo s $t$ i stavimo $\lambda'=t^{-1}\lambda$ i $\alpha'=t^{-1}\alpha$, pa dobivamo
    
    $$
    \lambda'\cdot x-y < \alpha'< \lambda'\cdot x_0-f^{**}(x_0).
    $$
    
    Za sve $x\in\operatorname{dom} f$ stavimo $y=f(x)$; tada vrijedi
    
    $$
    \alpha' > \lambda'\cdot x - f(x).
    $$
    
    Uzimanjem supremuma po $x$ na desnoj strani nejednakosti dobivamo
    
    $$
    \alpha' \ge \sup_{x\in\mathbf R^d}\lambda'\cdot x - f(x) = f^*(\lambda').
    $$
    
    Nadalje,
    
    $$
    f^{**}(x_0) < \lambda'\cdot x_0-f^*(\lambda') \le \sup_{x^*\in\mathbf R^d}x^*\cdot x_0-f^*(x^*) = f^{**}(x_0).
    $$
    
    Ta kontradikcija pokazuje da slučaj $t>0$ nije moguć.
    
    Na kraju razmotrimo slučaj $t=0$. Zapravo ćemo pokazati da ga se malom perturbacijom može svesti na slučaj $t>0$. Uzmimo proizvoljan $\lambda_0\in\operatorname{dom}f^*$; iz definicije konveksne konjugate slijedi da za sve $x\in\operatorname{dom}f$ i $y\ge f(x)$ vrijedi
    
    $$
    \lambda_0\cdot x-y\le f^*(\lambda_0).
    $$
    
    Stoga za svaki $\varepsilon>0$ vrijedi
    
    $$
    (\lambda+\varepsilon\lambda_0)\cdot x - \varepsilon y<\alpha+\varepsilon f^*(\lambda_0).
    $$
    
    Istodobno, budući da je $\alpha<\lambda\cdot x_0$, za dovoljno malen $\varepsilon>0$ vrijedi i
    
    $$
    \alpha+\varepsilon f^*(\lambda_0) < (\lambda+\varepsilon\lambda_0)\cdot x_0 - \varepsilon f^{**}(x_0).
    $$
    
    Dakle, ako uzmemo $\lambda'=\lambda+\varepsilon\lambda_0$, $t'=\varepsilon$ i $\alpha'=\alpha+\varepsilon f^*(\lambda_0)$, vrijedi
    
    $$
    \lambda'\cdot x-t'y <\alpha' <\lambda'\cdot x_0 - t'f^{**}(x_0).
    $$
    
    Time smo se vratili na prethodni slučaj, koji opet vodi u kontradikciju.
    
    Ta kontradikcija pokazuje da ne postoji točka $x_0\in\mathbf R^d$ sa svojstvom $f(x_0)>f^{**}(x_0)$. Dakle, uvijek vrijedi $f(x_0)\le f^{**}(x_0)$.
    
    Spajanjem rezultata obaju koraka dobivamo $f^{**}(x)=f(x)$.

Dakle, jaka dualnost vrijedi ako i samo ako je $v(y)$ konveksna funkcija od $y\in\mathbf R^d$[^other-conditions].

### Subgradijent

U prethodnom je odjeljku pokazano da je funkcija vrijednosti problema s kaznom $h(\lambda)$ suprotna vrijednost konveksne konjugate funkcije vrijednosti izvornog problema $v(y)$. Budući da je definicija konveksne konjugate zapravo optimizacijski problem s parametrom, za nju vrijedi i rezultat sličan [teoremu o ovojnici](https://en.wikipedia.org/wiki/Envelope_theorem). No kako konveksne funkcije nisu svuda diferencijabilne, najprije treba poopćiti definiciju derivacije na konveksne funkcije. To vodi do pojma subgradijenta.

???+ abstract "Subgradijent"
    Za konveksnu funkciju $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ i $x_0\in\operatorname{dom}f$, ako vektor $x^*\in\mathbf R^d$ zadovoljava da za svaki $x\in\mathbf R^d$ vrijedi
    
    $$
    f(x) \ge f(x_0)+x^*\cdot(x-x_0),
    $$
    
    onda se $x^*$ zove **subgradijent** (subgradient) funkcije $f(x)$ u $x_0$. Skup svih subgradijenata funkcije $f(x)$ u $x_0$ zove se njezin **subdiferencijal** (subdifferential) u toj točki i označava se $\partial f(x_0)$.

Geometrijski, subdiferencijal konveksne funkcije $f(x)$ u $x_0$ skup je vektora nagiba svih njezinih potpornih hiperravnina u toj točki. U jednodimenzionalnom slučaju subdiferencijal je

$$
\partial f(x_0) = [\partial_-f(x_0),\partial_+f(x_0)],
$$

gdje su $\partial_-f(x_0)$ i $\partial_+f(x_0)$ redom lijeva i desna derivacija funkcije $f(x)$ u $x_0$. Nadalje, za funkciju $\tilde f(x)$ dobivenu proširenjem konveksne funkcije $f:\mathbf Z\rightarrow\mathbf R\cup\{\pm\infty\}$ na skupu cijelih brojeva, lijeva i desna derivacija u cjelobrojnoj točki $x=k$ upravo su lijeva i desna diferencija prvog reda:

$$
\partial\tilde f(k) = [f(k)-f(k-1),f(k+1)-f(k)]. 
$$

Očito je konveksna funkcija $f(x)$ diferencijabilna u točki $x_0$ ako i samo ako je njezin subdiferencijal $\partial f(x_0)$ u toj točki jednočlan skup.

Budući da konveksna konjugata daje preslikavanje iz vektora nagiba potporne hiperravnine u njezin odsječak, pomoću nje možemo provjeriti je li vektor nagiba $x^*$ subgradijent konveksne funkcije $f(x)$ u zadanoj točki $x$.

???+ note "Teorem (konveksna konjugata i subgradijent)"
    Za pravu konveksnu funkciju $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ i proizvoljne $x,x^*\in\mathbf R^d$ vrijedi
    
    $$
    x^*\in\partial f(x) \iff x^*\cdot x = f(x) + f^*(x^*).
    $$
    
    Nadalje, ako je $f$ još i odozdo poluneprekidna, oba su uvjeta ekvivalentna s $x\in\partial f^*(x^*)$.

??? note "Dokaz"
    Prema definiciji subgradijenta, $x^*\in\partial f(x)$ ako i samo ako
    
    $$
    f(x') \ge f(x) + x^*\cdot(x'-x),~\forall x'\in\mathbf R^d.
    $$
    
    To je ekvivalentno s
    
    $$
    x^*\cdot x - f(x) \ge x^*\cdot x'-f(x'),~\forall x'\in\mathbf R^d.
    $$
    
    što je opet ekvivalentno s
    
    $$
    x^*\cdot x - f(x) \ge \sup_{x'\in\mathbf R^d}x^*\cdot x'-f(x') = f^*(x^*).
    $$
    
    No prema definiciji konveksne konjugate uvijek vrijedi
    
    $$
    x^*\cdot x - f(x) \le f^*(x^*).
    $$
    
    Stoga je znak „veće ili jednako” u prethodnoj formuli zapravo ekvivalentan jednakosti, dakle ekvivalentan sljedećoj formuli
    
    $$
    x^*\cdot x = f(x) + f^*(x^*).
    $$
    
    Time je dovršen prvi dio dokaza.
    
    U slučaju kad je $f$ odozdo poluneprekidna prava konveksna funkcija, prema Fenchel–Moreauovu teoremu vrijedi $f^{**}=f$. Stoga su ta dva uvjeta ekvivalentna s
    
    $$
    x^*\cdot x = f^*(x^*) + f^{**}(x).
    $$
    
    Ponovnom primjenom zaključka iz prvog dijela, to je ekvivalentno s $x\in\partial f^*(x^*)$.

Ovaj rezultat pokazuje da je, ako je $f^{**}=f$, subdiferencijal $\partial f^{*}(x^*)$ konveksne konjugate $f^*$ u $x^*$ upravo skup $x$-komponenata presjeka potporne hiperravnine s vektorom nagiba $x^*$ i epigrafa $\operatorname{epi}f$.

???+ note "Korolar"
    Za odozdo poluneprekidnu pravu konveksnu funkciju $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ i proizvoljne $x,x^*\in\mathbf R^d$ vrijedi
    
    $$
    \begin{aligned}
    \partial f(x) &= \arg\max_{y^*\in\mathbf R^d} x\cdot y^* - f^*(y^*),\\
    \partial f^*(x^*) &= \arg\max_{y\in\mathbf R^d} x^*\cdot y - f(y).
    \end{aligned}
    $$

??? note "Dokaz"
    Dokazujemo drugu jednakost. Dokaz prve je analogan.
    
    Prema definiciji konveksne konjugate vrijedi
    
    $$
    f^*(x^*) = \sup_{y\in\mathbf R^d} x^*\cdot y - f(y),
    $$
    
    pa
    
    $$
    x \in \arg\max_{y\in\mathbf R^d} x^*\cdot y - f(y)
    $$
    
    ako i samo ako je $f^*(x^*) = x^*\cdot x - f(x)$, a ta jednakost vrijedi ako i samo ako je $x\in\partial f^*(x^*)$. Time je dokazano da su ta dva skupa jednaka.

Primijenjen na kontekst ovog članka, ovaj rezultat pokazuje da pri rješavanju problema

$$
h(\lambda) = \min_{x\in X}f(x)-\lambda\cdot g(x) = \min_{y\in g(X)}v(y) - \lambda\cdot y
$$

skup vrijednosti funkcije ograničenja $g(x)$ na skupu optimalnih odluka upravo je $\partial(-h(\lambda))$. Za $d=1$ i problem koji uključuje samo cijele brojeve taj je skup interval

$$
[h(\lambda-1)-h(\lambda),h(\lambda)-h(\lambda+1)].
$$

Za uzastopne cijele brojeve $\lambda$ ti se intervali nadovezuju, pa je pri binarnom pretraživanju dovoljno računati samo jedan kraj.

## Dokaz konveksnosti

Preduvjet primjene WQS binarnog pretraživanja jest konveksnost funkcije vrijednosti. Na natjecanjima se konveksnost može naslutiti tabličnim računanjem, intuicijom i sl. No strogo dokazati konveksnost često nije lako. U ovom odjeljku, na primjeru sljedećeg klasičnog zadatka, predstavljamo uobičajene načine dokazivanja konveksnosti na natjecanjima.

???+ example "Problem sadnje stabala"
    Postoji $n$ jama i treba posaditi $m$ stabala. Stabla se ne smiju saditi u dvije susjedne jame. Zadan je niz $\{a_i\}$ duljine $n$ koji označava dobit od sadnje stabla u svaku jamu; dobit može biti pozitivna ili negativna. Odredi najveću moguću ukupnu dobit nakon sadnje tih $m$ stabala.
    
    Ukratko, riječ je o problemu najvećeg težinskog nezavisnog skupa veličine $m$ na lancu duljine $n$.

Te se metode grubo mogu podijeliti u četiri skupine:

-   svođenje na konveksnost funkcije vrijednosti nekog problema konveksne optimizacije (uključujući [linearno programiranje](../../math/linear-programming.md) i sl.) u ovisnosti o parametru, što uključuje izgradnju modela [toka najmanje cijene](../../graph/flow/min-cost.md) i sl.;
-   pomoću jednadžbe prijelaza stanja konveksnost se može dokazati i induktivno, pri čemu se mogu koristiti neke [transformacije koje čuvaju konveksnost](./slope-trick.md#凸函数的变换);
-   za probleme particije intervala može se provjeriti da funkcija cijene svakog intervala zadovoljava [četverokutnu nejednakost](./quadrangle.md);
-   na kraju, za posebne probleme konveksnost se može izravno pokazati argumentom zamjene.

Te su metode dokazivanja često povezane s nekim načinom rješavanja samog problema.

### Svođenje na parametarsku konveksnu optimizaciju

Razmotrimo parametarski problem konveksne optimizacije sljedećeg oblika:

$$
v(y)=\inf_{x\in\mathcal D(y)} f(x,y).
$$

Pritom je funkcija cilja $f:\mathbf R^m\times\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ za svaki $y\in\mathbf R^d$ konveksna funkcija od $x\in\mathbf R^m$, a dopustivo područje $\mathcal D:\mathbf R^d\rightarrow \mathcal P(\mathbf R^m)$ skupovna je funkcija na $\mathbf R^d$ takva da je za svaki $y\in\mathbf R^d$ skup $\mathcal D(y)$ konveksan. Ti uvjeti jamče da je za svaki parametar $y\in\mathbf R^d$ riječ o problemu konveksne optimizacije.

???+ note "Teorem"
    Pretpostavimo da gornji parametarski problem konveksne optimizacije zadovoljava sljedeće uvjete:
    
    1.  funkcija cilja $f(x,y)$ konveksna je funkcija od $(x,y)$;
    2.  graf preslikavanja dopustivog područja $y\mapsto\mathcal D(y)$, tj. $\{(x,y):x\in\mathcal D(y)\}$, konveksan je skup.
    
    Ako za svaki $y\in\mathbf R^d$ vrijedi $v(y)>-\infty$, onda je funkcija vrijednosti $v(y)$ prava konveksna funkcija od $y$.

??? note "Dokaz"
    Za proizvoljne $y_1,y_2\in\mathbf R^d$ i $\alpha\in(0,1)$ treba dokazati
    
    $$
    v(\alpha y_1+(1-\alpha)y_2) \le \alpha v(y_1) + (1-\alpha) v(y_2).
    $$
    
    Ako je $v(y_1)=+\infty$ ili $v(y_2)=+\infty$, desna je strana nejednakosti $+\infty$ i nejednakost sigurno vrijedi. Inače su $v(y_1)$ i $v(y_2)$ konačni. Za svaki $\varepsilon>0$ i $i=1,2$ postoji $x_i\in\mathcal D(y_i)$ takav da je $f(x_i,y_i)< v(y_i)+\varepsilon$. Iz konveksnosti grafa preslikavanja $\mathcal D$ slijedi
    
    $$
    \alpha x_1+(1-\alpha)x_2 \in \mathcal D(\alpha y_1+(1-\alpha)y_2).
    $$
    
    Drugim riječima, $\alpha x_1+(1-\alpha)x_2$ dopustivo je rješenje optimizacijskog problema s parametrom $\alpha y_1+(1-\alpha)y_2$. Iz optimalnosti i konveksnosti funkcije cilja slijedi
    
    $$
    \begin{aligned}
    v(\alpha y_1+(1-\alpha)y_2)
    &\le f(\alpha x_1+(1-\alpha)x_2,\alpha y_1+(1-\alpha)y_2) \\
    &\le \alpha f(x_1,y_1) + (1-\alpha)f(x_2,y_2) \\
    &< \alpha v(y_1) + (1-\alpha) v(y_2) + \varepsilon.
    \end{aligned}
    $$
    
    Budući da je $\varepsilon$ proizvoljan, puštanjem $\varepsilon\rightarrow 0$ dobivamo
    
    $$
    v(\alpha y_1+(1-\alpha)y_2) \le \alpha v(y_1) + (1-\alpha) v(y_2).
    $$
    
    Dakle, funkcija vrijednosti $v(y)$ je konveksna.

Na natjecanjima je najčešći problem konveksne optimizacije linearno programiranje.

???+ note "Korolar"
    Neka su $c\in\mathbf R^n$, $A_1\in\mathbf R^{d_1\times n}$, $A_2\in\mathbf R^{d_2\times n}$, $y_1\in\mathbf R^{d_1}$, $y_2\in\mathbf R^{d_2}$. Razmotrimo sljedeći parametarski problem linearnog programiranja:
    
    $$
    v(y_1,y_2)=\min_{x\in\mathbf R^n} c\cdot x \text{ subject to }A_1x\le y_1,A_2x=y_2,x\ge 0.
    $$
    
    Tada je funkcija vrijednosti $v(y_1,y_2)$ konveksna funkcija od $(y_1,y_2)$.

Bilo da je riječ o ograničenjima nejednakostima ili jednakostima, funkcija vrijednosti linearnog programa konveksna je funkcija parametara ograničenja.

Mnogi se problemi iz teorije grafova mogu zapisati kao problemi linearnog programiranja:

-   problemi mrežnih tokova: maksimalni tok, minimalni rez, tok najmanje cijene;
-   najkraći put bez negativnih ciklusa;
-   najveće (težinsko) sparivanje, najmanji vršni pokrivač i sl. u bipartitnim grafovima;
-   najveće (težinsko) sparivanje u općim grafovima;
-   minimalno razapinjuće stablo[^mst].

Stoga su funkcije vrijednosti tih problema konveksne (konkavne) funkcije parametara tih problema.

???+ warning "Cjelobrojna ograničenja"
    Pri modeliranju stvarnih problema grafovskim modelima obično postoje implicitna cjelobrojna ograničenja, npr. brid se može samo odabrati ili ne odabrati, tok može biti samo cjelobrojan itd. Zato se oni mogu pretvoriti samo u probleme cjelobrojnog linearnog programiranja (integer linear programming, ILP), a ne linearnog programiranja (LP). Budući da ILP nije problem konveksne optimizacije, njegova funkcija vrijednosti ne mora biti konveksna funkcija parametara problema. Relaksacijom cjelobrojnih ograničenja ILP-a dobiva se LP, ali potonji ne mora imati optimalno rješenje koje zadovoljava cjelobrojna ograničenja. Stoga optimalna vrijednost LP-a dobivenog relaksacijom cjelobrojnih ograničenja može biti strogo bolja od odgovarajućeg ILP-a, pa ta dva problema nisu nužno ekvivalentna.
    
    Gore navedeni grafovski problemi mogu se zapisati kao LP bez cjelobrojnih ograničenja; no za neke druge probleme, npr. najveći nezavisni skup u općem grafu, cjelobrojna su ograničenja nužna. Osim toga, čak i ako se neki grafovski problem može zapisati kao LP, uvođenje dodatnih linearnih ograničenja može narušiti ekvivalenciju odgovarajućih ILP i LP problema, pa se taj grafovski problem s ograničenjem više ne može zapisati kao linearno programiranje.

Na primjer, u kontekstu toka najmanje cijene vrijedi sljedeći uobičajeni rezultat:

???+ note "Korolar"
    U [modelu toka najmanje cijene](../../graph/flow/min-cost.md) najmanja cijena $v(m)$ konveksna je funkcija toka $m$.

??? note "Dokaz"
    Neka je $G=(V,E)$ usmjereni graf, brid $(i,j)$ ima kapacitet $c_{ij}$ i cijenu $w_{ij}$ po jedinici toka, a izvor i ponor su redom $s$ i $t$. Varijable odluke označimo s $\{f_{ij}\}$, gdje je $f_{ij}$ tok kroz brid $(i,j)\in E$. Tada se tok najmanje cijene može zapisati kao sljedeći problem linearnog programiranja:
    
    $$
    \begin{aligned}
    v(m)=\min_{\{f_{ij}\}}\;&\sum_{(i,j)\in E}w_{ij}f_{ij}\\
    \text{subject to }&\sum_{(j,i)\in E}f_{ji} - \sum_{(i,j)\in E}f_{ij} = 
    \begin{cases}
    -m, & i=s,\\
    m,  & i=t,\\
    0,  & \text{otherwise},
    \end{cases}
    ~\forall i\in V,\\
    &0\le f_{ij}\le c_{ij},~\forall (i,j)\in E.
    \end{aligned}
    $$
    
    Dakle, najmanja cijena $v(m)$ konveksna je funkcija parametra $m$.

Mnogi se natjecateljski problemi mogu svesti na mrežne tokove i druge grafovske probleme, pa se konveksnost funkcije vrijednosti može uspostaviti na sličan način.

Ovom metodom dobivamo prvi dokaz konveksnosti problema sadnje stabala:

??? example "Dokaz konveksnosti 1"
    Najveća dobit problema sadnje stabala zapravo se može dobiti iz sljedećeg modela maksimalnog toka najveće cijene:
    
    -   iz izvora $s$ prema čvoru $r$ povučemo brid kapaciteta $m$ i cijene $0$;
    -   iz čvora $r$ prema svakom neparnom čvoru $i=1,3,\cdots,2\lceil n/2\rceil-1$ povučemo brid kapaciteta $1$ i cijene $0$;
    -   iz svakog parnog čvora $i=0,2,\cdots,2\lfloor n/2\rfloor$ prema ponoru $t$ povučemo brid kapaciteta $1$ i cijene $0$;
    -   za svaki $i=1,\cdots,n$, od neparnog među čvorovima $i-1$ i $i$ prema parnom povučemo brid kapaciteta $1$ i cijene $a_i$.
    
    Konačni je odgovor dobivena najveća cijena. Pretvorimo li ovaj grafovski model u odgovarajući problem linearnog programiranja (vidi dokaz gornjeg korolara), ukupni tok $m$ pojavit će se u nejednakosti koja ograničava tok bridom $(s,r)$. Iz korolara slijedi da je najveća cijena $v(m)$ konkavna funkcija toka $m$.
    
    Pomoću tog modela toka problem se može riješiti simulacijom toka ili [greedy pristupom sa „žaljenjem”](../../basic/greedy.md#rješavanje-žaljenjem) u složenosti $O(n\log n)$.

### Pomoću jednadžbe prijelaza stanja

Iako jednadžba prijelaza stanja ne daje učinkovit način računanja, često se može iskoristiti za dokaz konveksnosti funkcije stanja $f(i,j)$ u parametru $j$. Konkretno, ako funkciju $f(i,\cdot)$ shvatimo kao stanje u $i$, jednadžbu prijelaza za $f(i,j)$ možemo shvatiti kao rekurziju za $f(i,\cdot)$ i tako induktivno dokazati da je svaka $f(i,\cdot)$ konveksna. Takvi su dokazi konveksnosti češći u kontekstu [optimizacije DP-a tehnikom Slope Trick](./slope-trick.md), a ta stranica raspravlja i o uobičajenim transformacijama koje čuvaju konveksnost.

Ovom se metodom također može dokazati konveksnost problema sadnje stabala:

??? example "Dokaz konveksnosti 2"
    Neka je $f(i,j)$ najveća dobit kad se u prvih $i$ jama posadi $j$ stabala. Promotrimo sljedeću jednadžbu prijelaza:
    
    $$
    f(i,j) = \max\{f(i-1,j),f(i-2,j-1)+a_i\}.
    $$
    
    Shvatimo tu jednadžbu kao rekurziju za funkciju $f(i,\cdot)$. Budući da se unutar maksimuma pojavljuju dvije različite funkcije, ne može se zapisati u obliku supremalne konvolucije. Ipak, induktivno se može dokazati da je funkcija $f(i,\cdot)$ konkavna.
    
    Zapravo treba induktivno dokazati sljedeće dvije tvrdnje:
    
    -   $f(i,j)-f(i-2,j-1)$ pada u $j$;
    -   $f(i,j)-f(i-1,j)$ raste u $j$.
    
    Baza indukcije je trivijalna. Pretpostavimo da tvrdnje vrijede za sve prirodne brojeve do uključivo $i-1$ i dokažimo ih za $i$. Dovoljno je izravno provjeriti.
    
    Prvo, prema pretpostavci indukcije,
    
    $$
    f(i-1,j) - f(i-2,j-1) = (f(i-1,j)-f(i-3,j-1)) - (f(i-2,j-1)-f(i-3,j-1))
    $$
    
    pada u $j$. Stoga
    
    $$
    f(i,j) - f(i-2,j-1) = \max\{f(i-1,j) - f(i-2,j-1), a_i\}
    $$
    
    pada u $j$, a
    
    $$
    f(i,j) - f(i-1,j) = \max\{0,a_i-(f(i-1,j) - f(i-2,j-1))\}
    $$
    
    raste u $j$. Time je indukcija dovršena.
    
    Nadalje,
    
    $$
    f(i,j) - f(i,j-1) = (f(i,j)-f(i-2,j-1)) - (f(i,j-1) - f(i-1,j-1)) - (f(i-1,j-1) - f(i-2,j-1))
    $$
    
    pada u $j$. To pokazuje da je $f(i,j)$ konkavna funkcija od $j$, pa je i funkcija vrijednosti $v(m)=f(n,m)$ konkavna funkcija od $m$.
    
    Nusproizvod ovog dokaza jest da za svaki $i$ postoji $p_i$ takav da je
    
    $$
    f(i,j) =
    \begin{cases}
    f(i-1,j), & j\le p_i,\\
    f(i-2,j-1) + a_i, & j> p_i.
    \end{cases}
    $$
    
    To znači da se niz $f(i,\cdot)$ može izravno održavati balansiranim stablom u složenosti $O(n\log^2n)$. Prednost je što se tako može obraditi opći slučaj proizvoljnog razmaka sadnje te se odjednom dobivaju sve vrijednosti $v(m)$.

### Četverokutna nejednakost

Druga česta klasa problema s konveksnošću na natjecanjima jesu [problemi particije intervala](./quadrangle.md#区间分拆问题). Na toj je stranici dokazano da, ako funkcija cijene pojedinog intervala zadovoljava četverokutnu nejednakost, najmanja cijena problema particije intervala s ograničenim brojem intervala konveksna je funkcija broja intervala. Ta stranica također daje načine provjere zadovoljava li neka funkcija $w(l,r)$ četverokutnu nejednakost. Najizravniji je način izračunati njezinu mješovitu diferenciju drugog reda:

$$
\begin{aligned}
\Delta_l \Delta_r w(l,r) &= \Delta_l(w(l,r+1)-w(l,r)) \\
&= w(l+1,r+1)-w(l+1,r)-w(l,r+1)+w(l,r).
\end{aligned}
$$

Funkcija $w(l,r)$ zadovoljava četverokutnu nejednakost ako i samo ako je $\Delta_l \Delta_r w(l,r)$ nepozitivna. Intuitivno, funkcija koja zadovoljava četverokutnu nejednakost obično znači da proširenje intervala na obje strane — tj. pomicanje lijevog kraja ulijevo i desnog udesno — ima neki sinergijski učinak.

Problem sadnje stabala također se može promatrati kao problem particije intervala i dokazati provjerom četverokutne nejednakosti.

??? example "Dokaz konveksnosti 3"
    Ispred niza dobiti sadnje dodamo $a_0$, koji može biti proizvoljan. Tada je problem sadnje ekvivalentan problemu particije intervala u kojem niz $\{a_0,a_1,\cdots,a_n\}$ dijelimo na $m$ segmenata, a funkcija dobiti svakog segmenta je
    
    $$
    w(l,r) = \max_{i\in[l+1,r]} a_i
    $$
    
    Drugim riječima, dobit svakog segmenta najveća je dobit među svim stablima osim prvog — time je osiguran razmak u sadnji.
    
    Budući da je riječ o problemu maksimizacije, treba provjeriti da je „ukršteno veće od ugniježđenog”, tj. da za sve $a<b<c<d$ vrijedi
    
    $$
    w(a,c)+w(b,d) \ge w(a,d)+w(b,c).
    $$
    
    Uvrstimo izraz za funkciju dobiti i stavimo
    
    $$
    A = \max_{i\in[a+1,b]} a_i,~ B = \max_{i\in[b+1,c]} a_i,~ C = \max_{i\in[c+1,d]}a_i,
    $$
    
    pa se nejednakost koju treba dokazati može zapisati kao
    
    $$
    \max\{A,B\} + \max\{B,C\} \ge \max\{A,B,C\} + B.
    $$
    
    Uočimo da je veći od dvaju članova $\max\{A,B\}$ i $\max\{B,C\}$ na lijevoj strani jednak $\max\{A,B,C\}$, a manji od njih uvijek je barem $B$, pa nejednakost vrijedi.
    
    Nakon pretvorbe problema sadnje u problem particije intervala dovoljno je predobraditi ekstreme intervala ST tablicom i sl., čime se cijena pojedinog intervala računa u $O(1)$, pa se algoritmom za probleme particije intervala problem rješava u vremenskoj složenosti $O(n\log n\log L)$ ili $O(n(n+m))$. Ta metoda također može obraditi proizvoljan razmak sadnje.

### Argument zamjene

U kombinatornoj optimizaciji dokazi konveksnosti funkcije vrijednosti često koriste argument zamjene (exchange argument). Konkretno, polazeći od optimalnih rješenja problema s parametrima $m-1$ i $m+1$, zamjenom dijela elemenata konstruira se dopustivo rješenje s parametrom $m$ i vrijednošću koja ne premašuje $(v(m-1)+v(m+1))/2$, pa se optimalnošću $v(m)$ dokazuje konveksnost. Za razliku od konveksne optimizacije, u kombinatornoj optimizaciji ne postoji prirodan način konstrukcije „međuoblika” dvaju rješenja, pa primjena argumenta zamjene obično zahtijeva određenu dosjetljivost.

???+ warning "„Rastući granični trošak” ne povlači nužno konveksnost"
    U kombinatornoj optimizaciji funkcije cilja često imaju svojstvo „rastućeg graničnog troška”, ali to ne povlači nužno konveksnost. Tipičan je primjer [\[IOI 2005\] Riv – Rijeke](https://www.luogu.com.cn/problem/P3354): verzija na lancu zadovoljava četverokutnu nejednakost pa je konveksna, ali za verziju na stablu postoje primjeri u kojima konveksnost ne vrijedi.
    
    Često svojstvo kojim se opisuje „rastući granični trošak” jest supermodularnost (supermodularity) funkcije. Za funkciju $f:\mathcal PX\rightarrow\mathbf R$ na familiji podskupova $\mathcal PX$ konačnog skupa $X$, ako zadovoljava jedno od sljedeća dva ekvivalentna svojstva:
    
    1.  (ukršteno manje od ugniježđenog) za sve podskupove $A,B\subseteq X$ vrijedi $f(A)+f(B) \le f(A\cup B) + f(A\cap B)$;
    2.  (rastući granični trošak) za sve podskupove $A\subseteq B\subseteq X$ i $x\in X\setminus B$ vrijedi $f(A\cup\{x\})-f(A)\le f(B\cup\{x\})-f(B)$;
    
    kažemo da je funkcija $f$ **supermodularna** (supermodular). No u optimizacijskom problemu sa supermodularnom funkcijom cilja funkcija vrijednosti
    
    $$
    v(m) = \min_{A\subseteq X} f(A) \text{ subject to }|A|=m
    $$
    
    **ne mora** biti konveksna funkcija od $m$. Razlog je taj što se iz optimalnih rješenja s veličinama podskupa $m-1$ i $m+1$ općenito ne može konstruirati dopustivo rješenje s podskupom veličine $m$ koje zadovoljava gornji odnos vrijednosti.

Argument zamjene daje još jedan dokaz konveksnosti problema sadnje stabala.

??? example "Dokaz konveksnosti 4"
    Koristimo argument zamjene. Neka su optimalni rasporedi za sadnju $m-1$ i $m+1$ stabala zadani redom s $\{x_i^{(m-1)}\}\in\{0,1\}^n$ i $\{x_i^{(m+1)}\}\in\{0,1\}^n$, gdje $1$ znači da je u jamu posađeno stablo, a $0$ da nije. Definiramo niz $\{z_i\}\in\{0,\pm 1\}^n$ s
    
    $$
    z_i = x_i^{(m+1)} - x_i^{(m-1)},~i=1,\cdots,n.
    $$
    
    Taj niz označava razlike dvaju rasporeda. Položaji s vrijednošću $0$ znače da je u toj jami u oba rasporeda posađeno stablo ili ni u jednom; položaji s vrijednošću $-1$ odnosno $+1$ znače da je stablo posađeno samo u rasporedu $x^{(m-1)}$ odnosno samo u rasporedu $x^{(m+1)}$. Budući da se ni u jednom rasporedu ne smije saditi u susjedne jame, vrijedi sljedeće:
    
    -   unutar uzastopnog podniza elemenata različitih od nule vrijednosti $z_i$ nužno se izmjenjuju između $\pm 1$;
    -   vrijednosti $0$ lijevo i desno od maksimalnog uzastopnog podniza elemenata različitih od nule nužno znače da u oba rasporeda ondje nije posađeno stablo.
    
    Dakle, ako je u nekom maksimalnom uzastopnom podnizu elemenata različitih od nule zbroj $z_i$ točno $+1$, tj. u tom je dijelu jama raspored $x^{(m+1)}$ posadio jedno stablo više od rasporeda $x^{(m-1)}$, možemo unutar tog dijela zamijeniti položaje sadnje dvaju rasporeda. Tako dobivamo dva dopustiva rasporeda, svaki s $m$ stabala. Budući da nismo promijenili ukupne položaje ni broj posađenih stabala u oba rasporeda, nego ih samo preraspodijelili, ukupna dobit ostaje $v(m-1)+v(m+1)$. No ta dva rasporeda s $m$ stabala ne moraju biti optimalna, pa dobit svakoga od njih ne premašuje $v(m)$. Time je dokazano
    
    $$
    v(m-1) + v(m+1) \le 2v(m),
    $$
    
    tj. $v(m)$ je konkavna funkcija od $m$.
    
    Preostaje samo pitanje postoji li maksimalni uzastopni podniz elemenata različitih od nule sa zbrojem točno $+1$. Budući da se zbrajaju izmjenični $\pm 1$, zbroj uzastopnog podniza elemenata različitih od nule može biti samo $0$ ili $\pm 1$. A kako je zbroj svih takvih maksimalnih podnizova jednak $2$, sigurno postoje barem dva maksimalna uzastopna podniza elemenata različitih od nule sa zbrojem točno $+1$. Time je dokaz dovršen.

## Primjeri zadataka

U ovom odjeljku predstavljamo nekoliko primjera primjene WQS binarnog pretraživanja u različitim situacijama.

### Predložak

???+ example "[Luogu P1484 Sadnja stabala](https://www.luogu.com.cn/problem/P1484)"
    Postoji $n$ jama i treba posaditi **najviše** $m$ stabala. Stabla se ne smiju saditi u dvije susjedne jame. Zadan je niz $\{a_i\}$ duljine $n$ koji označava dobit od sadnje stabla u svaku jamu; dobit može biti pozitivna ili negativna. Odredi najveću moguću ukupnu dobit.

??? note "Rješenje"
    Za razliku od ranije razmatranog problema sadnje, ovdje se traži najviše $m$ stabala, a ne točno $m$. Ako s $v(m)$ i dalje označavamo funkciju vrijednosti ranije razmatranog problema, odgovor je ovog zadatka zapravo $\tilde v(m)=\max_{k\le m}v(k)$. Budući da je $v(m)$ konkavna, dakle unimodalna funkcija, odgovor zadatka odgovara tome da zadržimo samo rastući dio $v(m)$ do vrha, nakon čega funkcija ostaje na vrhu; to je kao da zadržimo samo dio s nenegativnim nagibom tangente. Stoga je jedina razlika u odnosu na ranije razmatrani problem to što je početni raspon nagiba u WQS binarnom pretraživanju $[0,\max_ia_i]$ umjesto $[\min_ia_i,\max_ia_i]$.
    
    Nakon uklanjanja ograničenja na broj metodom WQS binarnog pretraživanja, problem se svodi na računanje najvećeg težinskog nezavisnog skupa na lancu, samo što je izvorna dobit $\{a_i\}$ zamijenjena s $\{a_i+k\}$. To je klasičan zadatak dinamičkog programiranja. Neka je $f(i,j)$ najveća dobit podproblema na prvih $i$ jama kad u $i$-tu jamu sadimo ($j=1$) odnosno ne sadimo ($j=0$). Jednadžba prijelaza tada glasi
    
    $$
    \begin{aligned}
    f(i,0) &= \max\{f(i-1,0),f(i-1,1)\},\\
    f(i,1) &= f(i-1,0) + a_i + k.
    \end{aligned}
    $$
    
    Početni su uvjeti $f(0,0)=0$ i $f(0,1)=-\infty$, a konačni je odgovor $\max\{f(n,0),f(n,1)\}$. Složenost jednog izračuna je $O(n)$, a ukupna vremenska složenost $O(n\log L)$, gdje je $L=\max_i|a_i|$.
    
    Referentna implementacija:
    
    === "Tradicionalna metoda"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/plant-tree-1.cpp"
        ```
    
    === "Dualna metoda"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/plant-tree-2.cpp"
        ```

???+ example "[Luogu P2619 \[Nacionalni trening-kamp\] Tree I](https://www.luogu.com.cn/problem/P2619)"
    Zadan je težinski neusmjereni povezani graf u kojem je svaki brid crn ili bijel. Odredi najmanju težinu razapinjućeg stabla s točno $m$ bijelih bridova.

??? note "Rješenje"
    Najprije se argumentom zamjene može dokazati da je $v(m)$ konveksna. Bez smanjenja općenitosti pretpostavimo da su sve težine bridova različite: slučajeve s dva brida jednake težine možemo malom perturbacijom pretvoriti u slučaj s različitim težinama; zatim puštanjem veličine perturbacije u nulu dokazujemo da konveksnost vrijedi i u graničnom slučaju — tj. kad postoje dva brida jednake težine. Ključ dokaza je sljedeća lema:[^edge-swap]
    
    ???+ note "Lema"
        Neka su $S$ i $T$ dva razapinjuća stabla neusmjerenog povezanog grafa $G=(V,E)$. Za svaki $e\in S\setminus T$ postoji barem jedan brid $f\in T\setminus S$ takav da su $S-e+f$ i $T-f+e$ oba razapinjuća stabla grafa $G$.
    
    ??? note "Dokaz"
        Neka je $e=(u,v)$ i neka je $P$ jedinstveni put u stablu $T$ koji spaja $u$ i $v$. Budući da je $P+e$ jedini ciklus u grafu $T+e$, brisanjem bilo kojeg brida $f$ iz $P$ dobivamo da je $T-f+e$ razapinjuće stablo. Istodobno, graf $S-e$ šuma je s dvije komponente povezanosti čije skupove vrhova označimo s $V_1$ i $V_2$; stoga, odaberemo li brid $f\in P$ takav da $f$ spaja $V_1$ i $V_2$, osiguravamo da je $S-e+f$ razapinjuće stablo. Takav brid $f$ uvijek postoji, jer $u$ i $v$ pripadaju redom $V_1$ i $V_2$, a $P$ spaja $u$ i $v$. Štoviše, $f\notin S$, jer u grafu $S-e$ skupovi $V_1$ i $V_2$ nisu povezani. Time je dokaz dovršen.
    
    Neka su $T_{m-1}$ i $T_{m+1}$ minimalna razapinjuća stabla s redom $m-1$ i $m+1$ bijelih bridova. Neka je $e$ bijeli brid iz $T_{m+1}\setminus T_{m-1}$; primjenom gornje leme postoji brid $f\in T_{m-1}\setminus T_{m+1}$ takav da su $T'=T_{m+1}-e+f$ i $T''=T_{m-1}+e-f$ oba razapinjuća stabla. Budući da je zamijenjen samo jedan par bridova, zbroj težina stabala $T'$ i $T''$ i dalje je $v(m-1)+v(m+1)$. Razlikujemo dva slučaja:
    
    -   ako je $f$ crni brid, $T'$ i $T''$ oba imaju $m$ bijelih bridova. Zbroj težina svakoga od njih nije manji od $v(m)$. Time je dokazano $2v(m)\le v(m-1)+v(m+1)$, pa je $v(m)$ konveksna u $m$;
    -   ako je $f$ bijeli brid, $T'$ i $T''$ imaju redom $m+1$ i $m-1$ bijelih bridova, pa zbrojevi njihovih težina nisu manji od $v(m+1)$ odnosno $v(m-1)$. No gore je pokazano da je zbroj njihovih težina zajedno jednak $v(m-1)+v(m+1)$. To znači da je zbroj težina stabla $T'$ jednak $v(m+1)$. Usporedbom $T'$ i $T_{m+1}$ slijedi da težine bridova $e$ i $f$ moraju biti jednake. To je u suprotnosti s pretpostavkom, pa ovaj slučaj nije moguć.
    
    Time je dokazano da je $v(m)$ konveksna funkcija od $m$.
    
    Nakon što je uspostavljena konveksnost funkcije $v(m)$, problem se može riješiti WQS binarnim pretraživanjem. Uklonimo ograničenje na broj, težinu svakog bijelog brida umanjimo za $k$ i riješimo problem minimalnog razapinjućeg stabla. Za to možemo primijeniti [Kruskalov algoritam](../../graph/mst.md#kruskal-算法). Uz održavanje povezanosti disjunktnim skupovima (DSU), složenost algoritma je $O(E\log E+E\alpha(V))$, gdje su $E$ i $V$ redom broj bridova i vrhova, a $\alpha(\cdot)$ inverzna Ackermannova funkcija. Glavni dio složenosti, $O(E\log E)$, odnosi se na sortiranje bridova, što se u ovom zadatku može dodatno optimizirati. Iako se tijekom WQS binarnog pretraživanja minimalno razapinjuće stablo računa više puta, svaki se put samo težine bijelih bridova mijenjaju za isti iznos. Zato pri predobradi možemo zasebno sortirati bijele i crne bridove, a zatim pri svakom računanju minimalnog razapinjućeg stabla samo spojiti (merge) bijele bridove s prilagođenim težinama i crne bridove. Tako se ukupna složenost smanjuje na $O(E\log E+E\alpha(V)\log L)$, gdje je $L$ duljina raspona težina bridova.
    
    Referentna implementacija:
    
    === "Tradicionalna metoda"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/black-white-mst-1.cpp"
        ```
    
    === "Dualna metoda"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/black-white-mst-2.cpp"
        ```

### Problem particije intervala

???+ example "[Luogu P6246 \[IOI 2000\] Poštanski uredi, pojačana verzija, pojačana verzija](https://www.luogu.com.cn/problem/P6246)"
    Zadan je rastući niz pozitivnih cijelih brojeva $\{a_i\}$ duljine $n$ koji označava položaje $n$ sela uz autocestu; treba izgraditi $m$ poštanskih ureda. Položaje ureda treba odabrati tako da se minimizira zbroj udaljenosti svih sela do njima najbližeg ureda. Odredi taj minimum.

??? note "Rješenje"
    Ovo je tipičan [problem particije intervala](./quadrangle.md#区间分拆问题). Detalje implementacije s binarnim redom (queue) potražite na toj stranici.
    
    Svaki ured poslužuje sela koja su mu najbliža, a ta su sela nužno uzastopna sela uz autocestu. Stoga je izgradnja $m$ ureda ekvivalentna podjeli svih sela na $m$ uzastopnih segmenata i izgradnji ureda najmanje cijene za svaki segment. Poznato je da ured treba izgraditi na položaju medijana položaja sela. Tako funkcija cijene intervala $[l,r]$ glasi
    
    $$
    w(l,r) = \sum_{i=l}^r|a_i-a_{\lfloor(l+r)/2\rfloor}|.
    $$
    
    Ona zadovoljava četverokutnu nejednakost, jer je njezina mješovita diferencija drugog reda nepozitivna:
    
    $$
    \Delta_l\Delta_r w(l,r)
    = \Delta_l(a_{r+1} - a_{\lfloor(l+r+1)/2\rfloor})
    = a_{\lfloor(l+r+1)/2\rfloor}-a_{\lfloor(l+r+2)/2\rfloor} \le 0.
    $$
    
    To znači da se problem može riješiti kombinacijom binarnog reda i WQS binarnog pretraživanja u složenosti $O(n\log n\log L)$.
    
    Referentna implementacija:
    
    === "Tradicionalna metoda"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/post-office-1.cpp"
        ```
    
    === "Dualna metoda"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/post-office-2.cpp"
        ```

### Dvodimenzionalna ograničenja

???+ example "[Codeforces 739 E. Gosha is hunting](https://codeforces.com/problemset/problem/739/E)"
    Postoji $n$ pokemona; nizovi $\{p_i\}$ i $\{q_i\}$ označavaju vjerojatnosti da se $i$-ti pokemon uhvati poke-loptom odnosno ultra-loptom. Na jednog pokemona može se baciti jedna poke-lopta, ili jedna ultra-lopta, ili po jedna od svake, ili nijedna. Na raspolaganju je $m_1$ poke-lopti i $m_2$ ultra-lopti koje treba razumno rasporediti i baciti istodobno. Odredi najveći očekivani broj uhvaćenih pokemona. Uspjeh pojedinog hvatanja neovisan je o ishodima ostalih hvatanja.
    
    Općenitije, problem se može apstrahirati ovako:
    
    Zadana su tri niza pozitivnih realnih brojeva $\{A_i\},\{B_i\},\{C_i\}$ duljine $n$, pri čemu za sve $i=1,\cdots,n$ vrijedi $C_i\le A_i+B_i$. Odredi optimalne skupove indeksa $X$ i $Y$ takve da je $|X|=m_1$ i $|Y|=m_2$ i da se maksimizira
    
    $$
    \sum_{i\in X\setminus Y}A_i + \sum_{i\in Y\setminus X}B_i + \sum_{i\in X\cap Y}C_i.
    $$

??? note "Rješenje"
    Izvorni problem može se shvatiti kao poseban slučaj ovog općenitijeg problema uz
    
    $$
    A_i = p_i,~ B_i = q_i,~ C_i = p_i+q_i-p_iq_i
    $$
    
    Stoga je dovoljno raspraviti rješenje općenitijeg problema.
    
    Neka $v(m_1,m_2)$ označava funkciju vrijednosti tog problema; treba dokazati da je konkavna funkcija od $(m_1,m_2)$. Razmotrimo sljedeći model toka:
    
    -   iz izvora $s$ povučemo po jedan brid prema čvorovima $x$ i $y$, kapaciteta redom $m_1$ i $m_2$, oba cijene $0$;
    -   za sve $i=1,\cdots,n$ povučemo iz čvorova $x$ i $y$ po jedan brid prema čvoru $i$, oba kapaciteta $1$, cijena redom $A_i$ i $B_i$;
    -   za sve $i=1,\cdots,n$ povučemo iz čvora $i$ dva brida prema ponoru $t$, oba kapaciteta $1$, cijena redom $0$ i $C_i-A_i-B_i$.
    
    Odgovor problema je maksimalni tok najveće cijene u tom modelu. Uvjet $C_i-A_i-B_i\le 0$ jamči da će tok kroz čvor $i$, kad iznosi $1$, prvo izabrati izlazni brid cijene $0$. Zapišemo li taj model toka kao problem linearnog programiranja, $m_1$ i $m_2$ pojavljuju se u nejednakostima koje ograničavaju tok bridovima $(s,x)$ i $(s,y)$. Dakle, $v(m_1,m_2)$ doista je konkavna funkcija od $(m_1,m_2)$.
    
    Za primjenu WQS binarnog pretraživanja treba razmotriti optimizacijski problem bez ograničenja na broj. Neka su $k_1$ i $k_2$ dodatne nagrade za stavljanje indeksa u skup $X$ odnosno $Y$. Bez ograničenja na broj odluka je za svaki indeks neovisna, pa je
    
    $$
    h(k_1,k_2) = \sum_{i=1}^n\max\{0,A_i+k_1,B_i+k_2,C_i+k_1+k_2\}.
    $$
    
    Odgovor izvornog problema zadan je s
    
    $$
    v(m_1,m_2) = \min_{k_1,k_2} h(k_1,k_2) - k_1m_1 - k_2m_2
    $$
    
    Ukupna vremenska složenost je $O(n\log^2L)$, gdje je $O(\log L)$ broj koraka binarnog pretraživanja po jednoj dimenziji.
    
    Referentna implementacija za problem hvatanja pokemona:
    
    ```cpp
    --8<-- "docs/dp/code/opt/wqs-binary-search/gosha-is-hunting.cpp"
    ```

### Općenitija ograničenja

???+ example "[Codeforces 1661 F. Teleporters](https://codeforces.com/problemset/problem/1661/F)"
    Zadano je $n$ dužina čije su duljine zadane nizom $\{a_i\}$. Mogu se proizvoljno rezati na dužine cjelobrojnih duljina, a cilj je minimizirati zbroj kvadrata duljina svih dužina. Odredi najmanji broj rezova potreban da taj zbroj kvadrata padne na najviše $V$.

??? note "Rješenje"
    Neka je $f(a,m)$ najmanji zbroj kvadrata koji se može dobiti rezanjem dužine duljine $a$ na $m$ mjesta. Prema nejednakosti između sredina, kad je zbroj dvaju brojeva fiksan, što je njihova razlika manja, to je manji i zbroj njihovih kvadrata. Stoga, što su dobivene dužine ujednačenije, to je ukupni zbroj kvadrata duljina manji. No zbog cjelobrojnog ograničenja najujednačeniji je slučaj dobiti $a\bmod (m+1)$ dužina duljine $\lceil a/(m+1)\rceil$ i $m+1-(a\bmod (m+1))$ dužina duljine $\lfloor a/(m+1)\rfloor$. Dakle, vrijedi
    
    $$
    \begin{aligned}
    f(a,m) &= (a\bmod (m+1))\left\lceil\dfrac{a}{m+1}\right\rceil^2 + (m+1-(a\bmod (m+1)))\left\lfloor\dfrac{a}{m+1}\right\rfloor^2 \\
    &= (a\bmod (m+1))\left(\left\lfloor\dfrac{a}{m+1}\right\rfloor+1\right)^2 + (m+1-(a\bmod (m+1)))\left\lfloor\dfrac{a}{m+1}\right\rfloor^2.
    \end{aligned}
    $$
    
    Druga jednakost vrijedi jer je $\lceil a/(m+1)\rceil \neq \lfloor a/(m+1)\rfloor + 1$ ako i samo ako je $a\bmod (m+1) = 0$.
    
    Može se dokazati da je funkcija $f(a,m)$ konveksna u $m$. Za to je treba proširiti na $m\in\mathbf R_{+}$. Kad je $\lfloor a/(m+1)\rfloor = q$, vrijedi
    
    $$
    \begin{aligned}
    f(a,m) &= (a-(m+1)q)(q+1)^2 + ((m+1)(q+1)-a)q^2 \\
    &= a(2q+1) - q(q+1)(m+1).
    \end{aligned}
    $$
    
    To je pravac nagiba $-q(q+1)$. Dakle, $f(a,m)$ je po dijelovima linearna funkcija čiji nagib raste s porastom $m$. To pokazuje da je $f(a,m)$ konveksna, pa je naravno konveksna i njezina restrikcija na cjelobrojne točke[^conv-int].
    
    Pomoću $f(\cdot,\cdot)$ najmanji zbroj kvadrata pri ukupno $m$ rezova svih dužina može se zapisati kao funkcija vrijednosti sljedećeg optimizacijskog problema:
    
    $$
    v(m) = \min_{\{m_i\}}\sum_i f(a_i,m_i)\text{ subject to }\sum_i m_i=m,~m_i\in\mathbf N.
    $$
    
    To je [infimalna konvolucija](./slope-trick.md#卷积下确界minkowski-和) nekoliko konveksnih funkcija, pa je i sama konveksna. Da zadatak traži $v(m)$, mogli bismo ga riješiti istom metodom kao prethodne primjere u vremenskoj složenosti $O(n\log^2L)$; no ovaj zadatak traži najmanji $m$ za koji je $v(m)\le V$. Pristup u kojem se $v(m)$ računa WQS binarnim pretraživanjem, a zatim se binarno pretražuje po $m$, ne prolazi, jer mu složenost doseže $O(n\log^3L)$. Za ovaj zadatak postoje sljedeća dva pristupa.
    
    **Metoda 1**: i dalje binarno pretražujemo nagib $k$, ali je kriterij pretraživanja procjena donje i gornje ograde za $v(m)$.
    
    U tradicionalnoj metodi WQS binarnog pretraživanja za zadani nagib $k$ može se izračunati raspon odgovarajućih optimalnih vrijednosti $m$. Budući da su ti $(m,v(m))$ kolinearni, time je određen i raspon vrijednosti $v(m)$. Stoga možemo izravno binarno pretraživati nagib $k$. Nakon što dobijemo nagib $k$, iz jednadžbe pravca
    
    $$
    v(m) = h(k) + km
    $$
    
    možemo izračunati najmanji $m$. Ukupna složenost je $O(n\log^2L)$.
    
    Da bismo odredili raspon $v(m)$, trebamo odrediti raspon $m$. Jedan je način pri računanju $h(k)$ zabilježiti najveće optimalno rješenje i iz njega izračunati donju ogradu za $v(m)$; drugi je način iz $h(k)-h(k-1)$ dobiti gornju ogradu za $m$, a time i donju ogradu za $v(m)$. U referentnoj implementaciji korišten je drugi način, koji ne ovisi o konkretnoj strukturi problema i ne zahtijeva posebnu obradu.
    
    **Metoda 2**: preoblikujemo optimizacijski problem tako da funkcija vrijednosti dualnog problema bude upravo rješenje zadatka.
    
    Zadatak se izravno može shvatiti kao sljedeći optimizacijski problem:
    
    $$
    m(V) = \min_{\{m_i\}} \sum_i m_i \text{ subject to }\sum_i f(a_i,m_i) \le V.
    $$
    
    Analiza iz ovog članka vrijedi i za taj problem. Stoga se traženi $m(V)$ može izračunati pomoću njegova dualnog problema:
    
    $$
    m(V) = \max_{\lambda} \sum_i\min_{m_i}(m_i - \lambda f(a_i,m_i)) + \lambda V.
    $$
    
    Ukupna je složenost algoritma i dalje $O(n\log^2L)$.
    
    Referentni kôd:
    
    === "Metoda 1"
        Kôd je samo ilustrativan; za prolaz na ograničenjima izvornog zadatka potrebni su 128-bitni cijeli brojevi i početni interval binarnog pretraživanja $[0,10^{60}]$.
        
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/teleporters-1.cpp"
        ```
    
    === "Metoda 2"
        Kôd je samo ilustrativan; zbog problema s preciznošću brojeva s pomičnim zarezom ne prolazi na ograničenjima izvornog zadatka.
        
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/teleporters-2.cpp"
        ```

## Zadaci za vježbu

Na kraju navodimo neke zadatke koji se mogu riješiti WQS binarnim pretraživanjem, za vježbu:

-   [Luogu P1484 Sadnja stabala](https://www.luogu.com.cn/problem/P1484)
-   [Luogu P1792 \[Nacionalni trening-kamp\] Sadnja stabala](https://www.luogu.com.cn/problem/P1792)
-   [Luogu P2619 \[Nacionalni trening-kamp\] Tree I](https://www.luogu.com.cn/problem/P2619)
-   [Luogu P3620 \[APIO/CTSC2007\] Sigurnosna kopija podataka](https://www.luogu.com.cn/problem/P3620)
-   [Luogu P4072 \[SDOI2016\] Pohod](https://www.luogu.com.cn/problem/P4072)
-   [Luogu P4383 \[Zajednički izbori osam pokrajina 2018\] Linkova stablo](https://www.luogu.com.cn/problem/P4383)
-   [Luogu P4983 Zaborav](https://www.luogu.com.cn/problem/P4983)
-   [Luogu P5308 \[COCI 2018/2019 #4\] Akvizna](https://www.luogu.com.cn/problem/P5308)
-   [Luogu P5633 Razapinjuće stablo s ograničenjem najmanjeg stupnja](https://www.luogu.com.cn/problem/P5633)
-   [Luogu P5896 \[IOI 2016\] aliens](https://www.luogu.com.cn/problem/P5896)
-   [Luogu P6246 \[IOI 2000\] Poštanski uredi, pojačana verzija, pojačana verzija](https://www.luogu.com.cn/problem/P6246)
-   [AtCoder Beginner Contest 218 H - Red and Blue Lamps](https://atcoder.jp/contests/abc218/tasks/abc218_h)
-   [AtCoder Beginner Contest 305 Ex - Shojin](https://atcoder.jp/contests/abc305/tasks/abc305_h)
-   [AtCoder Regular Contest 164 E - Segment-Tree Optimization](https://atcoder.jp/contests/arc164/tasks/arc164_e)
-   [Codeforces 125 E. MST Company](https://codeforces.com/problemset/problem/125/E)
-   [Codeforces 321 E. Ciel and Gondolas](https://codeforces.com/problemset/problem/321/E)
-   [Codeforces 739 E. Gosha is hunting](https://codeforces.com/problemset/problem/739/E)
-   [Codeforces 802 O. April Fools' Problem (hard)](https://codeforces.com/contest/802/problem/O)
-   [Codeforces 958 E2. Guard Duty (medium)](https://codeforces.com/problemset/problem/958/E2)
-   [Codeforces 1279 F. New Year and Handle Change](https://codeforces.com/problemset/problem/1279/F)
-   [Codeforces 1661 F. Teleporters](https://codeforces.com/problemset/problem/1661/F)
-   [Codeforces 1799 F. Halve or Subtract](https://codeforces.com/problemset/problem/1799/F)
-   [2019 Summer Petrozavodsk Camp H. Honorable Mention](https://codeforces.com/gym/102331/problem/H)

## Literatura i bilješke

-   [Wang Qinshi, „浅析一类二分方法” (Kratka analiza jedne klase metoda binarnog pretraživanja)](https://github.com/hzwer/shareOI/blob/master/%E5%9F%BA%E7%A1%80%E7%AE%97%E6%B3%95/%E6%B5%85%E6%9E%90%E4%B8%80%E7%B1%BB%E4%BA%8C%E5%88%86%E6%96%B9%E6%B3%95_%E7%8E%8B%E9%92%A6%E7%9F%B3.pdf)
-   [Theoretical grounds of lambda optimization by adamant - Codeforces blog](https://codeforces.com/blog/entry/98334)
-   [Rigorozna metoda WQS binarnog pretraživanja, YeahPotato - Luogu blog](https://www.luogu.com.cn/article/vsffwrc3)
-   [Bilješke: detaljno objašnjenje WQS binarnog pretraživanja i česte zablude, ikrvxt - CSDN blog](https://blog.csdn.net/Emm_Titan/article/details/124035796)
-   [Convex conjugate - Wikipedia](https://en.wikipedia.org/wiki/Convex_conjugate)
-   [Fenchel–Moreau theorem - Wikipedia](https://en.wikipedia.org/wiki/Fenchel%E2%80%93Moreau_theorem)
-   [Subderivative - Wikipedia](https://en.wikipedia.org/wiki/Subderivative)
-   [Boyd, Stephen P., and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004.](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
-   Papadimitriou, Christos H., and Kenneth Steiglitz. Combinatorial optimization: algorithms and complexity. Courier Corporation, 1998.
-   Conforti, Michele, Gérard Cornuéjols, and Giacomo Zambelli. Integer programming. Springer International Publishing, 2014.
-   Schrijver, Alexander. Combinatorial optimization: polyhedra and efficiency. Vol. 24, no. 2. Berlin: Springer, 2003.

[^high-d-convex]: U stvarnim problemima $y$ može poprimati samo konačno mnogo točaka rešetke u $\mathbf R^d$. Uvjet koji je ovdje zapravo potreban jest da se rješenje izvornog problema $v(y)$ može proširiti do konveksne funkcije $\tilde v:\mathbf R^d\rightarrow \mathbf R\cup\{\pm\infty\}$ na $\mathbf R^d$, tj. da je $v(y)$ **konveksno proširiva** (convex-extensible). Radi jednostavnosti, u tekstu se proširena funkcija i dalje označava s $v(y)$. Geometrijski to znači da sve točke skupa $\{(y,v(y))\}$ leže na donjoj konveksnoj ljusci svoje konveksne ljuske. U jednodimenzionalnom slučaju taj se uvjet algebarski [lako opisuje](./slope-trick.md#离散点集上的凸函数); u višedimenzionalnom je slučaju nešto složeniji, a [ova skripta](https://kzmurota.fpark.tmu.ac.jp/paper/HIMSummerSchool15Murota.pdf) daje neke jednostavne dovoljne uvjete.

[^other-conditions]: Uvjeti iz teorema na prvi pogled izgledaju jači od same konveksnosti, ali za situacije koje se susreću na natjecanjima, posebno kad je $X$ konačan skup, dovoljno je zahtijevati samo konveksnost. Funkcija $\tilde v$ dobivena proširenjem prave konveksne funkcije $v$ na diskretnom skupu nužno je odozdo poluneprekidna konveksna funkcija, jer je konveksna ljuska konačno mnogo točaka zatvoren konveksan skup, a odozdo poluneprekidna konveksna funkcija upravo je ona čiji je epigraf zatvoren konveksan skup. Što se tiče riječi „prava” u „prava konveksna funkcija”, dovoljno je da $v(y)$ bude konveksna i da u barem jednoj točki poprima konačnu vrijednost.

[^mst]: Problem minimalnog razapinjućeg stabla ima dva uobičajena [načina](https://math.arizona.edu/~glickenstein/math443f14/golari.pdf) zapisa kao linearno programiranje: model s eliminacijom podtura (subtour-elimination formulation) i model zasnovan na rezovima (cut-based formulation). Samo prvi način modeliranja jamči da je dobiveni linearni program ekvivalentan izvornom problemu.

[^edge-swap]: Ova lema vrijedi i za opće [matroide](../../math/matroid.md). Zove se **svojstvo simetrične zamjene baza** (symmetric base-exchange property); vidi [stranicu na Wikipediji](https://en.wikipedia.org/wiki/Basis_of_a_matroid). Stoga se zaključak o konveksnosti iz ovog zadatka može poopćiti na opće matroide.

[^conv-int]: Naravno, konveksne ljuske funkcije $f(a,m)$ i njezine restrikcije na cjelobrojne točke nisu iste, jer $f(a,m)$ može imati ekstreme na necjelobrojnim položajima. To znači da se $f(a,m)$ s realnom domenom ne može izravno koristiti u optimizacijskom problemu ovog zadatka.
