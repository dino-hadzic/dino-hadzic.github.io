---
title: Radijani i koordinatni sustavi
---

## Definicija kuta

U osnovnoj školi učili smo **statičku definiciju** kuta: kut je lik koji čine dvije zrake sa zajedničkim početkom.

Ta definicija, međutim, ograničava veličinu kuta na $[0, 360^\circ]$, što otežava dublje proučavanje, a neke se stvari njome ne mogu objasniti, npr.: što znači rotacija za $720^\circ$?

U srednjoškolskoj matematici uvodi se **dinamička definicija** kuta: kut je lik koji nastaje kad se zraka u ravnini rotira oko svog početka iz jednog položaja u drugi.

Početni položaj zove se **početni krak**, a završni **završni krak**. Pritom dogovorno vrijedi:

-   kut nastao rotacijom u smjeru **suprotnom od kazaljke na satu** zove se **pozitivni kut** i njegova je mjera pozitivna;
-   kut nastao rotacijom u smjeru **kazaljke na satu** zove se **negativni kut** i njegova je mjera negativna;
-   kut čiji završni krak nije uopće rotiran u odnosu na početni zove se **nul-kut** i njegova je mjera $0^\circ$.

Time se pojam kuta proširuje na **proizvoljan kut**.

???+ note "Napomena"
    Početni i završni krak nul-kuta se podudaraju, ali nije svaki kut kojemu se početni i završni krak podudaraju nul-kut, npr. kutovi koji su višekratnici od $360^\circ$.

## Radijanska mjera

U praktičnim primjenama kutove često treba pretvarati u razne druge parametre, a opisivanje kutova u radijanima smanjuje broj potrebnih koeficijenata. Zato sada uvodimo **radijansku mjeru**:

Središnji kut kojemu pripada luk duljine jednake polumjeru zove se kut od $1$ radijana; označava se simbolom $\text{rad}$ i čita „radijan”.

Prema prethodnom dogovoru, radijanska mjera pozitivnog kuta je pozitivna, negativnog negativna, a nul-kuta $0$. Ako središnjem kutu $\alpha$ kružnice polumjera $r$ pripada luk duljine $l$, onda je:

$$
|\alpha|=\dfrac{l}{r}
$$

Pomoću te formule mogu se zapisati i formule za duljinu luka i površinu kružnog isječka, što ovdje preskačemo.

Dakle, kut od $360^\circ$ ima radijansku mjeru $2\pi$; s tom se korespondencijom može pretvarati između stupnjeva i radijana:

$$
k \operatorname{rad} = \frac{\pi}{180^\circ} n^\circ
$$

Promotrimo neki kut i zarotirajmo njegov završni krak za još jedan puni krug, ili čak više njih, dok početni krak ostaje na mjestu: položaj završnog kraka uvijek je isti. Takve kutove zovemo kutovima s istim završnim krakom.

Skup kutova s istim završnim krakom kao kut $\alpha$ lako se dobije: to je $\{\varphi \mid \varphi = \alpha + 2k\pi, k \in \mathbf{Z}\}$.

Možemo to shvatiti ovako: kraku kuta neprestano dodajemo pune krugove, a položaj završnog kraka se ne mijenja.

???+ note "Dvije matematičke konstante: $\pi$ i $\tau$"
    U zapadnom matematičkom svijetu danas postoje mišljenja da bi „prava konstanta kružnice” trebala biti $2\pi$, a ta se vrijednost označava grčkim slovom $\tau$. Pristaše nove konstante kružnice „pravi” dan broja pi slave 28. lipnja.
    
    Primjerice, u radijanskoj mjeri puni kut iznosi $2\pi$, pa se dijeljenjem $2\pi$ na jednake dijelove izravno dobiju jednaki dijelovi punog kuta. Također, u kompleksnoj analizi vrlo se često pojavljuje kombinacija $2\pi$ itd.
    
    Da bismo slijedili ustaljenu konvenciju u svim dijelovima Kine, na **OI Wikiju** za konstantu kružnice koristimo $\pi$.

???+ note "Uobičajen zapis broja pi u programiranju"
    U jezicima C/C++ za $\pi$ se obično uzima `acos(-1)`; samo je ta vrijednost broj s pomičnim zarezom najbliži $\pi$. Vrijednost $\pi$ zapisana pomoću `acos(-1)` ili `4 * atan(1)` iznosi $3.14159265358979310000$.
    
    Ako se uzmu druge vrijednosti, npr. `acos(-1.0/2.0)`, `acos(1.0/2.0)`, `asin(1.0/2.0)` itd., dobiveni $\pi$ iznosi $3.14159265358979360000$, a to više nije broj s pomičnim zarezom najbliži $\pi$.
    
    Ako ga znate napamet, možete izravno napisati i $3.1415926535897932$.

## Pravokutni koordinatni sustav u ravnini

Dvije međusobno okomite brojevne osi u istoj ravnini sa zajedničkim ishodištem čine pravokutni (Kartezijev) koordinatni sustav u ravnini (rectangular coordinates).

Obično se jedna os postavlja vodoravno, a druga okomito, pri čemu se smjer udesno odnosno prema gore uzima za pozitivan smjer osi. Vodoravna os zove se os $x$ (x-axis) ili apscisna os, okomita os zove se os $y$ (y-axis) ili ordinatna os; osi $x$ i $y$ zajedno zovu se koordinatne osi, a njihovo zajedničko ishodište $O$ zove se ishodište (origin) pravokutnog koordinatnog sustava. Pravokutni koordinatni sustav s ishodištem u točki $O$ označava se $xOy$.

Osi $x$ i $y$ dijele koordinatnu ravninu na četiri kvadranta (quadrant): dio gore desno zove se prvi kvadrant, a ostala tri dijela redom u smjeru suprotnom od kazaljke na satu drugi, treći i četvrti kvadrant. Kvadranti su omeđeni osima; točke na apscisnoj i ordinatnoj osi te ishodište ne pripadaju nijednom kvadrantu. Osi $x$ i $y$ obično imaju istu jediničnu duljinu, ali u posebnim slučajevima mogu imati i različite.

### Opis položaja u pravokutnom koordinatnom sustavu

U pravokutnom koordinatnom sustavu svakoj točki ravnine odgovara jedinstven uređeni par brojeva (koordinate točke, coordinates); obrnuto, svakom uređenom paru brojeva odgovara jedinstvena točka ravnine.

Za proizvoljnu točku $C$ ravnine spustimo iz $C$ okomice na os $x$ i na os $y$; brojevi $a, b$ koji na osima $x$ odnosno $y$ odgovaraju nožištima okomica zovu se apscisa odnosno ordinata točke $C$, a uređeni par (ordered pair) $(a, b)$ zove se pravokutne koordinate točke $C$. Točke u različitim kvadrantima ili na koordinatnim osima imaju različite koordinate.

## Polarni koordinatni sustav u ravnini

Razmotrimo stvarnu situaciju, npr. navigaciju na moru: kaže se „točka $B$ je od točke $A$ u smjeru $30^\circ$ istočno od sjevera, na udaljenosti $100$ metara”, a ne „postavimo pravokutni koordinatni sustav s ishodištem u $A$, tada je $B(50,50\sqrt 3)$”.

Zato:

1.  u ravnini odaberemo čvrstu točku $O$ koju zovemo **pol**;
2.  iz pola povučemo zraku $Ox$ koju zovemo **polarna os**;
3.  odaberemo jediničnu duljinu (u matematičkim problemima obično $1$), jedinicu za kut (obično radijan) i njegov pozitivan smjer (obično smjer suprotan od kazaljke na satu);

čime je uspostavljen **polarni koordinatni sustav**.

### Opis položaja u polarnom koordinatnom sustavu

Neka je $A$ točka ravnine.

-   Udaljenost $|OA|$ između pola $O$ i točke $A$ zove se **polarni radijus** i označava $\rho$;
-   kut $\angle xOA$ s početnim krakom na polarnoj osi i završnim krakom $OA$ zove se **polarni kut** i označava $\varphi$;

tada je uređeni par $(\rho,\varphi)$ **polarne koordinate** točke $A$.

Iz definicije kutova s istim završnim krakom slijedi da $(\rho,\varphi)$ i $(\rho,\varphi + 2k\pi)\ (k\in \mathbf{Z})$ zapravo predstavljaju istu točku. Posebno, polarne koordinate pola su $(0,\varphi)\ (\varphi \in \mathbf{R})$, pa točka ravnine ima beskonačno mnogo zapisa u polarnim koordinatama.

Ako zahtijevamo $\rho \ge 0,0 \le \varphi < 2\pi$, onda se svaka točka ravnine osim pola može prikazati jedinstvenim uređenim parom $(\rho,\varphi)$, a točka koju predstavljaju polarne koordinate $(\rho,\varphi)$ jednoznačno je određena.

### Pretvorba između pravokutnog i polarnog koordinatnog sustava

Naravno, proučavanje likova u polarnom koordinatnom sustavu katkad je nezgodno. Za prelazak u pravokutni koordinatni sustav postoje formule pretvorbe. Pravokutne koordinate $(x,y)$ točke $A(\rho,\varphi)$ mogu se izraziti ovako:

$$
\begin{aligned}
x &= \rho \cos \varphi \\
y &= \rho \sin \varphi
\end{aligned}
$$

Odatle slijedi:

$$
\begin{aligned}
\rho^2 &= x^2 + y^2\\
\tan \varphi &= \frac{y}{x}\ \ \ \ (x\not =0)
\end{aligned}
$$

Dakle $\rho = \sqrt{x^2+y^2}$.

Međutim, za isti $\dfrac{y}{x}$, tj. isti $\tan\varphi$, postoje dvije moguće vrijednosti $\varphi$, pa smjer treba odrediti još i prema vrijednostima $x, y$. Konkretno, definiramo funkciju:

$$
\operatorname{atan2}(y, x) = \begin{cases}
\arctan(\frac{y}{x}) & \text{if } x > 0 \\
\arctan(\frac{y}{x}) + \pi & \text{if } y \ge 0, x < 0 \\
\arctan(\frac{y}{x}) - \pi & \text{if } y < 0, x < 0 \\
\pi/2 & \text{if } y > 0, x = 0 \\
-\pi/2 & \text{if } y < 0, x = 0 \\
\text{any} & \text{if } y = 0, x = 0
\end{cases}
$$

Tada je $\varphi = \operatorname{atan2}(y, x)$. Uočite da je skup vrijednosti gornje funkcije $(-\pi, \pi]$.

U jezicima C/C++ [ta je funkcija](https://en.cppreference.com/w/cpp/numeric/math/atan2) definirana u biblioteci `<math.h>` odnosno `<cmath>`; dovoljno je pozvati `atan2(y, x)`.

## Pravokutni koordinatni sustav u prostoru

Pravokutni koordinatni sustav u prostoru uspostavlja se ovako:

1.  u prostoru odaberemo točku $O$;
2.  kroz točku $O$ povučemo tri međusobno okomite brojevne osi $\overrightarrow{Ox}, \overrightarrow{Oy}, \overrightarrow{Oz}$, koje redom zovemo os $x$ (apscisna os), os $y$ (ordinatna os) i os $z$ (aplikatna os), a zajedno koordinatne osi; njihovi pozitivni smjerovi slijede pravilo desne ruke: ako desnom rukom obuhvatimo os $z$ tako da se četiri prsta savijaju od pozitivnog smjera osi $x$ prema pozitivnom smjeru osi $y$, palac pokazuje pozitivan smjer osi $z$;
3.  odredimo jediničnu duljinu na svakoj osi, obično $1$.

Time je uspostavljen pravokutni koordinatni sustav u prostoru, koji označavamo $O-xyz$. Čvrsta točka $O$ zove se ishodište tog koordinatnog sustava.

Svake dvije koordinatne osi određuju ravninu, pa su tako određene tri međusobno okomite ravnine koje zajedno zovemo koordinatne ravnine. Koordinatna ravnina određena osima $x$ i $y$ zove se ravnina $xOy$, a analogno postoje ravnine $yOz$ i $zOx$. Tri koordinatne ravnine dijele prostor na osam dijelova, a svaki se dio zove oktant.

### Opis položaja u pravokutnom koordinatnom sustavu u prostoru

Nakon što odaberemo pravokutni koordinatni sustav $O-xyz$ u prostoru, možemo uspostaviti bijekciju između točaka prostora i uređenih trojki.

Neka je $M$ točka prostora; kroz $M$ povučemo ravnine okomite redom na os $x$, os $y$ i os $z$. Neka su sjecišta tih triju ravnina s osima $x$, $y$ i $z$ redom $P, Q, R$; točke $P, Q, R$ zovu se projekcije točke $M$ na os $x$, os $y$ odnosno os $z$. Neka su koordinate točaka $P, Q, R$ na osima $x$, $y$ i $z$ redom $x, y, z$; tako točka $M$ određuje uređenu trojku $(x, y, z)$.

Obrnuto, ako je zadana uređena trojka $(x, y, z)$, na osi $x$ uzmemo točku $P$ s koordinatom $x$, na osi $y$ točku $Q$ s koordinatom $y$, a na osi $z$ točku $R$ s koordinatom $z$; zatim kroz točke $P, Q, R$ povučemo tri ravnine okomite redom na os $x$, os $y$ i os $z$. One se sijeku u jednoj točki $M$ prostora i upravo je $M$ točka određena uređenom trojkom $(x, y, z)$.

Tako je uspostavljena bijekcija između točaka $M$ prostora i uređenih trojki $(x, y, z)$. Uređena trojka $(x, y, z)$ zove se koordinate točke $M$ i piše se $M(x, y, z)$, pri čemu se $x$ zove apscisa, $y$ ordinata, a $z$ aplikata.

## Cilindrični koordinatni sustav

Cilindrični koordinatni sustav proširenje je polarnih koordinata na tri dimenzije: krenemo od polarnog koordinatnog sustava koji se koristi u ravnini i zatim kroz pol $O$ dodamo os $z$ okomitu na tu ravninu, usmjerenu prema gore.

Da bismo pronašli točku opisanu cilindričnim koordinatama $(\rho, \varphi, z)$, najprije obradimo $\rho$ i $\varphi$ u polarnom koordinatnom sustavu, a zatim se prema koordinati $z$ pomaknemo duž osi $z$ „gore” ili „dolje”.

### Pretvorba između cilindričnog i pravokutnog koordinatnog sustava u prostoru

Vrijednost $z$ jednaka je u oba sustava.

Za pretvorbu između $(x,y)$ i $(\rho, \varphi)$ vidi gore [Pretvorba između pravokutnog i polarnog koordinatnog sustava](#pretvorba-između-pravokutnog-i-polarnog-koordinatnog-sustava).

## Sferni koordinatni sustav

Sferne koordinate mogu se odrediti ovako:

1.  stanemo u ishodište, okrenuti u smjeru vodoravne polarne osi; okomita os pokazuje od stopala prema glavi;
2.  ruku podignemo uvis, u smjeru okomite polarne osi;
3.  zarotiramo se za kut $\varphi$ u smjeru suprotnom od kazaljke na satu;
4.  ruku spustimo za kut $\vartheta$; ruka tada pokazuje u smjeru zadanom kutovima $\varphi$ i $\vartheta$;
5.  pomaknemo se iz ishodišta u tom smjeru za udaljenost $r$.

Tako dolazimo do točke opisane sfernim koordinatama $(r,\vartheta,\varphi)$. Pritom se $\vartheta$ zove **zenitni kut**, a $\varphi$ **azimutni kut**.

???+ warning "Upozorenje"
    Iz raznih razloga negdje se za zenitni kut koristi $\phi$, a za azimutni $\theta$. Kad u člancima naiđete na sferni koordinatni sustav, obvezno obratite pozornost na to.
    
    Isto tako, ako u vlastitom tekstu koristite sferni koordinatni sustav, preporučujemo da unaprijed jasno navedete kojim simbolima označavate zenitni i azimutni kut.

### Pretvorba između cilindričnog i sfernog koordinatnog sustava

Vrijednost $\varphi$ jednaka je u oba sustava.

Iz cilindričnog u sferni koordinatni sustav:

$$
\begin{aligned}
r &= \sqrt{\rho^2 + z^2} \\
\vartheta &= \begin{cases}
\arctan\left(\frac{\rho}{z}\right) & \text{if }z > 0 \\
\pi/2 & \text{if }z = 0, \rho \not= 0 \\
\arctan\left(\frac{\rho}{z}\right) + \pi & \text{if }z < 0 \\
\end{cases}
\end{aligned}
$$

Uočite da za točku $(0,0,0)$ u cilindričnim koordinatama sferna koordinata $\vartheta$ nije jednoznačno određena.

Iz sfernog u cilindrični koordinatni sustav:

$$
\begin{aligned}
\rho &= r \sin \vartheta \\
z &= r \cos \vartheta
\end{aligned}
$$

### Pretvorba između pravokutnog koordinatnog sustava u prostoru i sfernog koordinatnog sustava

Mogu se zajedno upotrijebiti gornji odjeljci [Pretvorba između pravokutnog i polarnog koordinatnog sustava](#pretvorba-između-pravokutnog-i-polarnog-koordinatnog-sustava) i [Pretvorba između cilindričnog i sfernog koordinatnog sustava](#pretvorba-između-cilindričnog-i-sfernog-koordinatnog-sustava), ili se izravno koriste sljedeće formule:

Iz pravokutnog koordinatnog sustava u prostoru u sferni koordinatni sustav:

$$
\begin{aligned}
r &= \sqrt{x^2 + y^2 + z^2} \\
\vartheta &= \arccos\left(\frac{z}{\sqrt{x^2 + y^2 + z^2}}\right) \\
\varphi &= \operatorname{atan2}(y, x)
\end{aligned}
$$

pri čemu je definicija funkcije $\operatorname{atan2}$ dana u odjeljku [Pretvorba između pravokutnog i polarnog koordinatnog sustava](#pretvorba-između-pravokutnog-i-polarnog-koordinatnog-sustava).

Uočite da za točku $(0,0,0)$ u pravokutnim koordinatama u prostoru sferne koordinate $\vartheta$ i $\varphi$ nisu jednoznačno određene.

Iz sfernog koordinatnog sustava u pravokutni koordinatni sustav u prostoru:

$$
\begin{aligned}
x &= r \sin \vartheta \cos \varphi \\
y &= r \sin \vartheta \sin \varphi \\
z &= r \cos \vartheta
\end{aligned}
$$
