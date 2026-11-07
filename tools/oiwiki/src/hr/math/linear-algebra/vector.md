---
title: Vektori
---

Prije samog teksta posebno napominjemo nešto o prijevodu. Iz povijesnih razloga matematika i fizika različito prevode riječ „vector” na kineski.

U fizici se obično prevodi kao „矢量” (shǐliàng, „strelična veličina”), nasuprot pojmu „标量” (skalar). U matematici se obično prevodi kao „向量” (xiàngliàng, „usmjerena veličina”). Slične razlike u prijevodu postoje i između „本征” i „特征” (za „eigen-”), „幺正” i „酉” (za „unitaran”) itd.

Budući da je **OI Wiki** namijenjen prvenstveno računarstvu i srodnim inženjerskim disciplinama, koje su bliže matematici, koristi se riječ „向量”.

## Definicija i srodni pojmovi

**Vektor**: veličina koja ima i iznos i smjer zove se vektor. U matematici se proučavaju **slobodni vektori**, tj. vektori kojima se početna i završna točka mogu proizvoljno paralelno pomicati dok god se ne mijenjaju njihov iznos i smjer. Označava se $\vec a$ ili $\boldsymbol{a}$.

**Usmjerena dužina**: dužina kojoj je pridružen smjer zove se usmjerena dužina. Usmjerena dužina ima tri elementa: **početnu točku, smjer i duljinu**; kad su ta tri elementa poznata, završna je točka jednoznačno određena. Vektori se obično prikazuju usmjerenim dužinama.

**Modul vektora**: duljina usmjerene dužine $\overrightarrow{AB}$ zove se modul vektora, tj. iznos tog vektora. Označava se $|\overrightarrow{AB}|$ ili $|\boldsymbol{a}|$.

**Nulvektor**: vektor modula $0$. Smjer nulvektora je proizvoljan. Označava se $\vec 0$ ili $\boldsymbol{0}$.

**Jedinični vektor**: vektor modula $1$ zove se jedinični vektor tog smjera. Obično se označava $\vec e$ ili $\boldsymbol{e}$.

**Paralelni vektori**: dva **nenul** vektora istog ili suprotnog smjera. Označava se $\boldsymbol a\parallel \boldsymbol b$. Za više međusobno paralelnih vektora može se povući bilo koji pravac paralelan s tim vektorima, pa se svaka skupina paralelnih vektora može translatirati na isti pravac; zato se paralelni vektori zovu i **kolinearni vektori**.

**Jednaki vektori**: vektori jednakog modula i istog smjera.

**Suprotni vektori**: vektori jednakog modula i suprotnog smjera.

**Kut između vektora**: za dva nenul vektora $\boldsymbol a,\boldsymbol b$ nanesimo $\overrightarrow{OA}=\boldsymbol a,\overrightarrow{OB}=\boldsymbol b$; tada je $\theta=\angle AOB$ kut između vektora $\boldsymbol a$ i vektora $\boldsymbol b$. Označava se $\langle \boldsymbol a,\boldsymbol b\rangle$. Očito, za $\theta=0$ vektori su istog smjera, za $\theta=\pi$ suprotnog smjera, a za $\theta=\frac{\pi}{2}$ okomiti su, što se označava $\boldsymbol a\perp \boldsymbol b$; pritom se dogovorno uzima $\theta \in [0,\pi]$.

Uočimo da ravninski vektori imaju smjer, pa se dva vektora ne mogu uspoređivati po veličini (mogu se uspoređivati samo njihovi moduli). Dva vektora ipak mogu biti jednaka.

## Linearne operacije s vektorima

### Zbrajanje i oduzimanje vektora

Nakon što se definira neka veličina, želimo s njom i računati. Operacije s vektorima mogu se uvesti po analogiji s operacijama s brojevima, a mogu se proučavati i s gledišta fizike.

Po analogiji s pojmom pomaka u fizici: ako osoba iz $A$ preko $B$ dođe u $C$, njezin je pomak $\overrightarrow{AB}+\overrightarrow{BC}$, što je zapravo isto kao da je izravno otišla iz $A$ u $C$, tj. $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$.

Uočimo da se i pravilo za slaganje sila – pravilo paralelograma – također može promatrati kao zbrajanje nekih vektora.

Sažmimo pravila zbrajanja vektora:

1.  **Pravilo trokuta za zbrajanje vektora**: ako se vektori koje zbrajamo redom nadovezuju jedan na drugi (kraj jednoga je početak sljedećega), njihov je zbroj vektor od početne točke prvog vektora do završne točke posljednjeg;
2.  **Pravilo paralelograma za zbrajanje vektora**: ako dva vektora koja zbrajamo imaju **zajedničku početnu točku**, njihov je zbroj dijagonala paralelograma kojemu su ta dva vektora susjedne stranice, s početkom u zajedničkoj početnoj točki i smjerom duž dijagonale paralelograma.

Time zbrajanje vektora dobiva geometrijsko značenje. Može se i provjeriti da zbrajanje vektora zadovoljava **komutativnost i asocijativnost**.

Budući da se oduzimanje realnih brojeva može zapisati kao zbrajanje suprotnog broja, i oduzimanje vektora zapisujemo na isti način, tj.: $\boldsymbol a-\boldsymbol b=\boldsymbol a+(-\boldsymbol b)$.

Promotrimo li vektore sa zajedničkom početnom točkom i konstruiramo njihovu razliku po pravilu paralelograma, nakon translacije vidimo da je **„vektor razlike vektora sa zajedničkom početnom točkom” usmjerena dužina od „umanjitelja” prema „umanjeniku”**. To je geometrijsko značenje oduzimanja vektora.

Katkad su zadane dvije točke $A,B$ i želimo znati $\overrightarrow{AB}$; možemo ga dobiti oduzimanjem $\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}$.

### Množenje vektora skalarom

„Umnožak realnog broja $\lambda$ i vektora $\boldsymbol a$” definira se kao vektor; ta se operacija zove **množenje vektora skalarom**, označava se $\lambda \boldsymbol a$, a njegova duljina i smjer definirani su ovako:

1.  $|\lambda \boldsymbol a|=|\lambda||\boldsymbol a|$;
2.  za $\lambda >0$ vektor $\lambda\boldsymbol a$ ima isti smjer kao $\boldsymbol a$, za $\lambda =0$ je $\lambda \boldsymbol a=\boldsymbol 0$, a za $\lambda<0$ vektor $\lambda \boldsymbol a$ ima smjer suprotan od $\boldsymbol a$.

Prema definiciji množenja skalarom može se provjeriti da vrijede sljedeća računska pravila:

$$
\begin{aligned}
\lambda(\mu \boldsymbol a)&=(\lambda \mu)\boldsymbol a\\
(\lambda+\mu)\boldsymbol a&=\lambda \boldsymbol a+\mu \boldsymbol a\\
\lambda(\boldsymbol a+\boldsymbol b)&=\lambda \boldsymbol a+\lambda \boldsymbol b
\end{aligned}
$$

Posebno:

$$
\begin{gathered}
(-\lambda)\boldsymbol a=-(\lambda \boldsymbol a)=-\lambda(\boldsymbol a)\\
\lambda(\boldsymbol a-\boldsymbol b)=\lambda \boldsymbol a-\lambda \boldsymbol b
\end{gathered}
$$

### Kriterij kolinearnosti dvaju vektora

Dva **nenul** vektora $\boldsymbol a$ i $\boldsymbol b$ kolinearna su $\iff$ postoji jedinstven realan broj $\lambda$ takav da je $\boldsymbol b=\lambda \boldsymbol a$.

Dokaz: prema definiciji množenja skalarom, za **nenul** vektor $\boldsymbol a$, ako postoji realan broj $\lambda$ takav da je $\boldsymbol b=\lambda \boldsymbol a$, tada je $\boldsymbol a \parallel \boldsymbol b$.

Obratno, ako je $\boldsymbol a\parallel \boldsymbol b$, $\boldsymbol a \not = \boldsymbol 0$ i $|\boldsymbol b|=\mu |\boldsymbol a|$, tada je $\boldsymbol b=\mu \boldsymbol a$ kad su $\boldsymbol a$ i $\boldsymbol b$ istog smjera, a $\boldsymbol b=-\mu \boldsymbol a$ kad su suprotnog smjera.

Na kraju, zbrajanje, oduzimanje i množenje skalarom zajednički se zovu linearne operacije s vektorima.

## Osnovni teorem o ravninskim vektorima i koordinatni prikaz

### Osnovni teorem o ravninskim vektorima

Iskaz teorema: ako dva vektora $\boldsymbol{e_1},\boldsymbol{e_2}$ nisu kolinearna, tada za svaki vektor $\boldsymbol p$ komplanaran s $\boldsymbol{e_1},\boldsymbol{e_2}$ postoji jedinstven par realnih brojeva $(x,y)$ takav da je $\mathbf p=x\boldsymbol{e_1}+y\boldsymbol{e_2}$.

Ravninskih vektora ima tako mnogo – kako sa što manje veličina prikazati sve ravninske vektore?

Jednim vektorom očito nije moguće prikazati sve vektore; najviše se mogu prikazati vektori na jednom pravcu.

Dodamo li još jedan vektor i prikažemo vektore pomoću dva **nekolinearna** vektora (dva kolinearna vektora ovdje se mogu smatrati istim vektorom), tada se svaki ravninski vektor može rastaviti u smjerovima tih dvaju vektora.

Dva nekolinearna vektora u istoj ravnini zovu se **baza**. Ako su vektori baze međusobno okomiti, rastav vektora je **ortogonalni rastav**.

### Koordinatni prikaz ravninskih vektora

Uzmemo li kao bazu jedinične vektore $i,j$ u smjeru osi apscisa i osi ordinata, prema osnovnom teoremu o ravninskim vektorima svi su ravninski vektori u obostrano jednoznačnoj korespondenciji s uređenim parovima realnih brojeva $(x,y)$.

Uređeni parovi realnih brojeva $(x,y)$ pak su u obostrano jednoznačnoj korespondenciji s točkama pravokutnog koordinatnog sustava u ravnini, pa ako nanesemo $\overrightarrow{OP}=\boldsymbol p$, završna točka $P(x,y)$ također je jednoznačno određena. Budući da proučavamo slobodne vektore, početna se točka može slobodno translatirati, pa se tako u pravokutnom koordinatnom sustavu u ravnini svaki vektor može jednoznačno prikazati uređenim parom realnih brojeva.

## Računanje s koordinatama ravninskih vektora

### Linearne operacije s ravninskim vektorima

Iz linearnih operacija s ravninskim vektorima mogu se izvesti operacije s koordinatama; glavni je postupak sve koordinate zapisati pomoću baze, zatim sve sažeti pomoću računskih pravila i na kraju zapisati koordinatni oblik rezultata.

Ako su $\boldsymbol a=(m,n)$, $\boldsymbol b=(p,q)$ dva vektora, tada:

$$
\begin{aligned}
\boldsymbol a+\boldsymbol b&=(m+p,n+q)\\
\boldsymbol a-\boldsymbol b&=(m-p,n-q)\\
k\boldsymbol a&=(km,kn)
\end{aligned}
$$

### Određivanje koordinatnog prikaza vektora

Za zadane dvije točke $A(a,b),B(c,d)$ lako se dokazuje $\overrightarrow{AB}=(c-a,d-b)$.

### Translacija točke

Katkad je točku $P$ potrebno translatirati u određenom smjeru za određeni broj jedinica duljine; tada smjer i udaljenost translacije objedinimo u jedan vektor i, prema pravilu trokuta za zbrajanje vektora, pribrojimo taj vektor vektoru $\overrightarrow{OP}$; završna točka dobivenog vektora upravo je translatirana točka.

### Kriterij kolinearnosti triju točaka

Ako su tri točke $A,B,C$ kolinearne, tada je $\overrightarrow{OB}=\lambda \overrightarrow{OA}+(1-\lambda)\overrightarrow{OC}$.

### Proširenje kriterija kolinearnosti triju točaka

Ako je u trokutu $ABC$ točka $D$ jedna od točaka koje dijele $BC$ na $n$ jednakih dijelova ($n\ BD=k\ DC$), tada vrijedi: $\overrightarrow{AD}=\frac{n}{k+n}\overrightarrow{AB}+\frac{k}{k+n}\overrightarrow{AC}$

## Proširenje na trodimenzionalni prostor (stereometrija / prostorni vektori)

U prostoru vrijedi sve što je rečeno u prethodnim odjeljcima. Štoviše:

### Osnovni teorem o prostornim vektorima

Iskaz teorema: ako tri vektora $\boldsymbol{e_1},\boldsymbol{e_2},\boldsymbol{e_3}$ nisu komplanarna, tada za svaki vektor $\boldsymbol p$ u prostoru postoji jedinstvena trojka realnih brojeva $(x,y,z)$ takva da je $\mathbf p=x\boldsymbol{e_1}+y\boldsymbol{e_2}+z\boldsymbol{e_3}$.
Prema osnovnom teoremu o prostornim vektorima jednako tako možemo uzeti tri međusobno okomita vektora baze $\boldsymbol{e_1},\boldsymbol{e_2},\boldsymbol{e_3}$ kao ortogonalnu bazu, uvesti **pravokutni koordinatni sustav u prostoru** i prostorne vektore prikazivati uređenom trojkom $(x,y,z)$ kao koordinatama.

### Osnovni teorem o komplanarnim vektorima

Ako postoje dva nekolinearna vektora $\boldsymbol{x},\boldsymbol{y}$, tada je vektor $\boldsymbol{p}$ komplanaran s $\boldsymbol{x},\boldsymbol{y}$ ako i samo ako postoji jedinstven par realnih brojeva $(a,b)$ takav da je $\boldsymbol{p}=a\boldsymbol{x}+b\boldsymbol{y}$.

### Vektor smjera

Smjer pravca u prostoru prikazuje se nenul vektorom paralelnim s tim pravcem; takav se vektor zove vektor smjera tog pravca. Položaj pravca u prostoru **potpuno je određen** jednom točkom prostora kroz koju prolazi i jednim njegovim vektorom smjera.

Napomenimo da i pravci u ravnini imaju vektor smjera.

Za pravac u **prostoru** vektor smjera može se odrediti na sljedeće načine:

-   Ako su zadane točke $A(x_1,y_1,z_1),B(x_2,y_2,z_2)$, tada je jedan vektor smjera pravca $AB$ vektor $\boldsymbol{s}=(x_2-x_1,y_2-y_1,z_2-z_1)$.

-   Ako je poznata ravnina **okomita** na traženi pravac, s općom jednadžbom $ax+by+cz+d=0$, tada je jedan vektor smjera pravca okomitog na tu ravninu $\boldsymbol{s}=(a,b,c)$; taj je vektor smjera ujedno i **jedan vektor normale** te ravnine.

### Vektor normale

Za ravninu (plohu) $ABCD$ njezin je vektor normale $\boldsymbol{n}$ okomit na tu ravninu.

Način računanja: uzmemo bilo koja dva vektora u toj ravnini, $\overrightarrow{AB},\overrightarrow{AD}$, tako da vrijedi $\overrightarrow{AB} \cdot \boldsymbol{n}=\boldsymbol{0}$ i $\overrightarrow{AD} \cdot \boldsymbol{n}=\boldsymbol{0}$, pa ga izračunamo koordinatnom metodom.

## Vektori i matrice

U linearnoj algebri linearna preslikavanja (linearne transformacije) mogu se prikazati matricama. Neka $T$ označava linearno preslikavanje koje $\mathbf R^n$ preslikava u $\mathbf R^m$, a $\mathbf x$ $n$-dimenzionalni stupčani vektor; tada postoji matrica $A$ tipa $m\times n$ takva da je

$$
T(\mathbf x)=A\mathbf x.
$$

Matrica $A$ zove se matrica preslikavanja (matrica transformacije) $T$. U algoritamskim zadacima linearna se preslikavanja u pravilu provode unutar iste dimenzije, pa je $A$ kvadratna matrica. Tako se problem linearnog preslikavanja vektora može svesti na problem množenja matrica.

U nastavku razmatramo tri transformacije česte na natjecanjima i njihove matrice: skaliranje (matrica transformacije označava se $S$), rotaciju (matrica transformacije označava se $R$) i translaciju (matrica transformacije označava se $T$).

### Skaliranje

Za $n$-dimenzionalni stupčani vektor $\boldsymbol a$ svaku njegovu komponentu skaliramo redom faktorima $v_1,v_2,\ldots,v_n$. Lako se vidi da je matrica transformacije skaliranja $R$ dijagonalna matrica tipa $n\times n$, tj. $S=\operatorname{diag}\{v_1,v_2,\ldots,v_n\}$.

### Rotacija

Rotacija vektora razmjerno je složena operacija; ograničit ćemo se na dvodimenzionalni i trodimenzionalni slučaj.

#### Rotacija vektora oko točke

Pod rotacijom vektora oko točke obično se misli na rotaciju vektora oko ishodišta. Za rotaciju neke točke oko druge točke $P$ možemo translacijom dovesti točku $P$ u ishodište, rotirati vektor i zatim koordinatni sustav translatirati natrag u prvotni položaj. Označimo li matricu translacije s $T$, a matricu rotacije oko ishodišta s $R$, matrica cijelog postupka je $TRT^{-1}$. Prema geometrijskom značenju, $T^{-1}$ sigurno postoji.

U dvodimenzionalnom prostoru neka je $\boldsymbol a=(x,y)$, s kutom nagiba $\theta$ i duljinom $l=\sqrt{x^2+y^2}$. Tada je $x=l\cos \theta,y=l\sin\theta$. Zarotiramo li ga oko ishodišta za kut $\alpha$ u smjeru suprotnom od kazaljke na satu, dobivamo vektor $\boldsymbol b=(l\cos(\theta+\alpha),l\sin(\theta+\alpha))$.

![](./images/vector-rotation.svg)

Prema trigonometrijskim identitetima,

$$
\boldsymbol{b}=(l(\cos\theta\cos\alpha-\sin\theta\sin\alpha),l(\sin\theta\cos\alpha+\cos\theta\sin\alpha))
$$

Pojednostavljeno,

$$
\boldsymbol b=(l\cos\theta\cos\alpha-l\sin\theta\sin\alpha,l\sin\theta\cos\alpha+l\cos\theta\sin\alpha)
$$

Uvrstimo li natrag gornje $x,y$, dobivamo

$$
\boldsymbol b=(x\cos\alpha-y\sin\alpha,y\cos\alpha+x\sin\alpha)
$$

Stoga je u dvodimenzionalnom prostoru matrica transformacije $R$

$$
R=
\begin{bmatrix}
\cos\alpha & -\sin\alpha\\
\sin\alpha & \cos\alpha
\end{bmatrix}.
$$

U trodimenzionalnom prostoru rotacija vektora zahtijeva dva kutna parametra, tj. kut rotacije zenitnog kuta i kut rotacije azimuta, a rotacija se može provesti pomoću [sfernog koordinatnog sustava u prostoru](../coordinate.md#sferni-koordinatni-sustav).

#### Rotacija vektora oko pravca

Za trodimenzionalne vektore češća je rotacija oko nekog pravca. Radi jednostavnosti i ovdje pretpostavljamo da pravac prolazi ishodištem. Ako pravac ne prolazi ishodištem, i dalje se možemo svesti na taj slučaj translacijom koordinatnog sustava.

Uzmimo vektor smjera pravca $\boldsymbol u=(u_x,u_y,u_z)$ i neka se trodimenzionalni vektor rotira oko njega za kut $\theta$ u smjeru suprotnom od kazaljke na satu. Tada je pripadna matrica transformacije $R$[^note1]

$$
R=
\begin{bmatrix}
u_x^2 \left(1-\cos \theta\right) + \cos \theta & u_x u_y \left(1-\cos \theta\right) - u_z \sin \theta & u_x u_z \left(1-\cos \theta\right) + u_y \sin \theta \\ 
u_x u_y \left(1-\cos \theta\right) + u_z \sin \theta & u_y^2\left(1-\cos \theta\right) + \cos \theta & u_y u_z \left(1-\cos \theta\right) - u_x \sin \theta \\ 
u_x u_z \left(1-\cos \theta\right) - u_y \sin \theta & u_y u_z \left(1-\cos \theta\right) + u_x \sin \theta & u_z^2\left(1-\cos \theta\right) + \cos \theta
\end{bmatrix}.
$$

### Translacija

Translacija nije linearno preslikavanje, nego afino preslikavanje. Međutim, afino preslikavanje u $\mathbf R^n$ i dalje se može prikazati linearnim preslikavanjem u $\mathbf R^{n+1}$.

Promotrimo $n$-dimenzionalni vektor $\boldsymbol a=(a_1,a_2, \ldots , a_n)$ koji želimo translatirati za vektor $\boldsymbol t=(t_1, t_2, \ldots , t_n)$. Stupčanom vektoru $\boldsymbol a$ dodamo još jednu komponentu i postavimo je na $1$, čime dobivamo novi stupčani vektor $\boldsymbol a'=(a_1, a_2, \ldots , a_n, 1)$. Tada se matrica transformacije $T$ može zapisati kao

$$
T=
\begin{bmatrix}
1 &   &        &   & t_1    \\
  & 1 &        &   & t_2    \\
  &   & \ddots &   & \vdots \\
  &   &        & 1 & t_n    \\
  &   &        &   & 1      \\
\end{bmatrix}.
$$

Za ostale matrice linearnih preslikavanja dodamo matrici jedan stupac i jedan redak, pri čemu je element u donjem desnom kutu $1$, a ostala su nova mjesta popunjena s $0$; na taj se način sve matrice linearnih preslikavanja mogu pretvoriti u matrice afinih preslikavanja. Primjerice, za rotaciju dvodimenzionalnog vektora matrica transformacije postaje

$$
R'=
\begin{bmatrix}
\cos\alpha & -\sin\alpha & 0\\
\sin\alpha & \cos\alpha & 0\\
0 & 0 & 1
\end{bmatrix}.
$$

## Stroža definicija vektora

U prethodnom tekstu vektor je definiran kao usmjerena dužina u prostoru. Strogo gledano, međutim, vektori nisu samo usmjerene dužine. Da bi se vektor strože definirao, najprije treba definirati [vektorski (linearni) prostor](./vector-space.md); pojedinosti potražite na stranici [Vektorski prostor](./vector-space.md).

[^note1]: Vidi [Rotation matrix from axis and angle - Wikipedia](https://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle)
