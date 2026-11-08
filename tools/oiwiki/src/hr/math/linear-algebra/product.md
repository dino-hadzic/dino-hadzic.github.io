---
title: Skalarni i vektorski produkt
---

U ovom se članku uvode jednostavne operacije među vektorima.

Prije samog teksta posebno napominjemo nešto o prijevodu. Iz povijesnih razloga u matematici i fizici postoje najrazličitiji kineski prijevodi dvaju pojmova „inner product” i „outer product”.

U fizici se obično prevode kao „标积” i „矢积” („skalarni produkt” i „vektorski produkt”), čime se izražava da je rezultat operacije skalar odnosno vektor. Nazivi „数量积” i „向量积” („količinski produkt” i „vektorski produkt”) iz srednjoškolskih udžbenika matematike također slijede taj način prevođenja po smislu.

U matematici se obično prevode i kao „内积” i „外积” („unutarnji produkt” i „vanjski produkt”), što je doslovan prijevod tih dvaju naziva. „点乘” i „叉乘” („množenje točkom” i „množenje križićem”) kolokvijalni su nazivi izvedeni iz znaka operacije i također su vrlo česti.

U operaciji „množenja točkom” znak točke često se izostavlja, a u linearnoj se algebri ta operacija čak izravno promatra kao množenje matrica, pa se točka ne piše.

## Skalarni produkt

Pojam skalarnog produkta **primjenjiv je na vektore bilo koje dimenzije**.

### Definicija

Skalarni produkt ima više različitih, ali ekvivalentnih definicija; u nastavku navodimo neke od njih.

#### Geometrijska definicija

U $n$-dimenzionalnom euklidskom prostoru $\mathbf{R}^n$ neka su zadana dva vektora $\boldsymbol{a}, \boldsymbol{b}$ i neka je kut među njima $\theta$. Tada je

$$
\boldsymbol{a} \cdot \boldsymbol{b} = |\boldsymbol{a}| |\boldsymbol{b}| \cos \theta
$$

**skalarni produkt** tih dvaju vektora, koji se zove i **unutarnji produkt** (inner product) ili **točkasti produkt** (dot product). Pritom se $|\boldsymbol{b}|\cos \theta$ zove projekcija vektora $\boldsymbol{b}$ na smjer vektora $\boldsymbol{a}$. Geometrijsko značenje skalarnog produkta jest: skalarni produkt $\boldsymbol{a} \cdot \boldsymbol{b}$ jednak je umnošku modula vektora $\boldsymbol{a}$ i projekcije vektora $\boldsymbol{b}$ na smjer vektora $\boldsymbol{a}$.

#### Algebarska definicija

U $n$-dimenzionalnom euklidskom prostoru $\mathbf{R}^n$ neka su zadana dva vektora $\boldsymbol{a} = (a_1, a_2, \dots, a_n), \boldsymbol{b} = (b_1, b_2, \dots, b_n)$. Tada je

$$
\boldsymbol{a} \cdot \boldsymbol{b} = \sum_{i = 1}^{n} a_i b_i
$$

**skalarni produkt** tih dvaju vektora, koji se zove i **unutarnji produkt** ili **točkasti produkt**. Geometrijska i algebarska definicija skalarnog produkta ekvivalentne su u euklidskom prostoru, a potonja je praktičnija za uporabu.

Kad ne može doći do zabune, točka skalarnog produkta može se izostaviti. Ako vektor ima gornji indeks $2$, to je skraćeni zapis skalarnog produkta vektora sa samim sobom, tj. **kvadrat modula vektora**, pri čemu se oznaka modula izostavlja. Taj gornji indeks $2$ ne smije se shvatiti kao kvadrat vektora, jer je rezultat skalarnog produkta vektora skalar, pa skalarni produkt bilo kojeg broja vektora različitog od $2$ ne postoji. Isto tako, kvadrat kvadrata modula vektora ne može se skraćeno zapisati gornjim indeksom $4$, nego se rezultat s gornjim indeksom $2$ mora promatrati kao cjelina, i tako dalje.

### Svojstva

Vidimo da je rezultat skalarnog produkta skalar; njegova je posebnost to što je riječ o bilinearnoj operaciji, linearnoj u svakom od dvaju vektora zasebno. Konkretno, skalarni produkt zadovoljava:

$$
\begin{aligned}
(\boldsymbol{a} + \boldsymbol{b}) \cdot \boldsymbol{c} &= \boldsymbol{a} \cdot \boldsymbol{c} + \boldsymbol{b} \cdot \boldsymbol{c} \\
\boldsymbol{a} \cdot (\boldsymbol{b} + \boldsymbol{c}) &= \boldsymbol{a} \cdot \boldsymbol{b} + \boldsymbol{a} \cdot \boldsymbol{c} \\
(\lambda \boldsymbol{a}) \cdot \boldsymbol{b} &= \lambda (\boldsymbol{a} \cdot \boldsymbol{b}) \\
\boldsymbol{a} \cdot (\lambda \boldsymbol{b}) &= \lambda (\boldsymbol{a} \cdot \boldsymbol{b})
\end{aligned}
$$

Skalarni produkt zadovoljava i komutativnost, tj.:

$$
\boldsymbol{a} \cdot \boldsymbol{b} = \boldsymbol{b} \cdot \boldsymbol{a}
$$

### Primjene

U nastavku navodimo neke uobičajene primjene skalarnog produkta.

1.  Provjera okomitosti dvaju vektora:

    $$
    \boldsymbol{a} \perp \boldsymbol{b} \iff \boldsymbol{a} \cdot \boldsymbol{b} = 0
    $$

    Dakle, skalarni produkt dvaju međusobno okomitih vektora jednak je $0$; skalarni produkt vektora i nulvektora jednak je $0$. Ako se kao definicija okomitosti uzme da je skalarni produkt jednak nuli, slijedi da je nulvektor okomit na svaki vektor.

2.  Provjera kolinearnosti dvaju vektora:

    $$
    \exists\lambda \in \mathbf{R} (\boldsymbol{a} = \lambda \boldsymbol{b}) \iff |\boldsymbol{a} \cdot \boldsymbol{b}| = |\boldsymbol{a}| |\boldsymbol{b}|
    $$

3.  Računanje modula vektora:

    $$
    |\boldsymbol a| = \sqrt{\boldsymbol{a} \cdot \boldsymbol{a}}
    $$

4.  Računanje kuta između dvaju vektora:

    $$
    \theta = \arccos \frac{\boldsymbol{a} \cdot \boldsymbol{b}}{|\boldsymbol a| |\boldsymbol b|}
    $$

## Determinante drugog i trećeg reda

Determinante drugog i trećeg reda mogu se posebno definirati kao jednostavniji posebni slučajevi determinante. U posljednjem dijelu matematičke analize, teoriji polja, Greenov teorem koristi determinantu drugog reda, Gaussov teorem (teorem o divergenciji) koristi skalarni produkt, a Stokesov teorem koristi determinantu trećeg reda.

Determinanta drugog reda može se promatrati kao funkcija četiriju varijabli, a definirana je kao:

$$
\begin{vmatrix}
    a & b \\
    c & d
\end{vmatrix}=ad-bc
$$

Determinanta trećeg reda može se promatrati kao funkcija devet varijabli, a definirana je kao:

$$
\begin{vmatrix}
    a & b & c \\
    d & e & f \\
    g & h & i
\end{vmatrix}=aei+dhc+gbf-ahf-dbi-gec
$$

Poseban način pamćenja jest „pravilo dijagonala” (Sarrusovo pravilo); pravilo dijagonala vrijedi samo za determinante drugog i trećeg reda.

Posebno napominjemo: razvoj determinante četvrtog reda ima ukupno 24 člana, a član na sporednoj dijagonali ima pozitivan predznak. Primijenimo li nasilno „pravilo dijagonala” za determinante trećeg reda, ne samo da ne dobivamo dovoljno članova nego je i predznak člana na sporednoj dijagonali pogrešan; stoga „pravilo dijagonala” za determinante trećeg reda ne vrijedi za determinante višeg reda, a determinante višeg reda nije prikladno računati ni izravnim razvojem.

## Vektorski produkt

Vektorski produkt operacija je **svojstvena trodimenzionalnim vektorima**.

U fizici se trodimenzionalni vektori podrazumijevano odnose na prostorni položaj i uvijek se pišu podebljano. Međutim, četverodimenzionalni vektori u teoriji relativnosti ne pišu se podebljano, nego posebnim oznakama i indeksima.

U linearnoj algebri svi se vektori pišu podebljano, a budući da je to zamorno i budući da su u linearnoj algebri operacije uglavnom među vektorima i matricama, pa teško može doći do dvosmislenosti, pri pisanju rukom oznaka vektora može se izostaviti.

### Definicija

Vektorski produkt ima više različitih, ali ekvivalentnih definicija; u nastavku navodimo neke od njih.

#### Geometrijska definicija

U trodimenzionalnom euklidskom prostoru $\mathbf{R}^3$ vektorski produkt vektora $\boldsymbol{a}, \boldsymbol{b}$ definira se kao vektor, označen $\boldsymbol{a} \times \boldsymbol{b}$, čiji su modul i smjer definirani ovako:

1.  $|\boldsymbol{a} \times \boldsymbol{b}| = |\boldsymbol{a}| |\boldsymbol{b}| \sin \langle \boldsymbol{a}, \boldsymbol{b} \rangle$;
2.  $\boldsymbol{a} \times \boldsymbol{b}$ okomit je na oba vektora $\boldsymbol{a}, \boldsymbol{b}$, a smjerovi vektora $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{a} \times \boldsymbol{b}$ zadovoljavaju pravilo desne ruke.

Promotrimo li modul vektorskog produkta i prisjetimo se formule za površinu trokuta $S=\frac{1}{2}ab\sin C$, vidimo da je geometrijsko značenje vektorskog produkta: **$|\boldsymbol{a} \times \boldsymbol{b}|$ je površina paralelograma kojemu su $\boldsymbol{a}, \boldsymbol{b}$ susjedne stranice**.

#### Algebarska definicija

U trodimenzionalnom euklidskom prostoru $\mathbf{R}^3$ vektorski produkt vektora $\boldsymbol{a} = (x_1, y_1, z_1), \boldsymbol{b} = (x_2, y_2, z_2)$ definira se kao vektor $\boldsymbol{c}$, označen $\boldsymbol{c} = \boldsymbol{a} \times \boldsymbol{b}$, a rezultat se može prikazati determinantom trećeg reda:

$$
\begin{vmatrix}
    \boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
    x_1 & y_1 & z_1  \\
    x_2 & y_2 & z_2
\end{vmatrix}
$$

pri čemu $\boldsymbol{i}, \boldsymbol{j}, \boldsymbol{k}$ označavaju jedinične vektore u smjeru koordinatnih osi $x, y, z$ i pišu se na mjestima odgovarajućih koordinata. Razvojem dobivamo

$$
\begin{aligned}
\boldsymbol{c} &= \boldsymbol{a} \times \boldsymbol{b} \\
&= (y_1z_2 - y_2z_1)\boldsymbol{i} + (z_1x_2 - z_2x_1)\boldsymbol{j} + (x_1y_2 - x_2y_1)\boldsymbol{k} \\
&= (y_1z_2 - y_2z_1, z_1x_2 - z_2x_1, x_1y_2 - x_2y_1)
\end{aligned}
$$

### Svojstva

1.  Vektorski produkt bilinearna je operacija, linearna u svakom od dvaju vektora zasebno. Konkretno, vektorski produkt zadovoljava:

    $$
    \begin{aligned}
    (\boldsymbol{a} + \boldsymbol{b}) \times \boldsymbol{c} &= \boldsymbol{a} \times \boldsymbol{c} + \boldsymbol{b} \times \boldsymbol{c} \\
    \boldsymbol{a} \times (\boldsymbol{b} + \boldsymbol{c}) &= \boldsymbol{a} \times \boldsymbol{b} + \boldsymbol{a} \times \boldsymbol{c} \\
    (\lambda \boldsymbol{a}) \times \boldsymbol{b} &= \lambda (\boldsymbol{a} \times \boldsymbol{b}) \\
    \boldsymbol{a} \times (\lambda \boldsymbol{b}) &= \lambda (\boldsymbol{a} \times \boldsymbol{b})
    \end{aligned}
    $$

    Prva dva svojstva mogu se nazvati i distributivnost, tj. vektorski produkt distributivan je prema zbrajanju vektora.

2.  Vektorski produkt zadovoljava antikomutativnost, tj.:

    $$
    \boldsymbol a \times \boldsymbol b=-\boldsymbol b \times \boldsymbol a
    $$

3.  Prema gornjim geometrijskim definicijama skalarnog i vektorskog produkta:

    $$
    \begin{aligned}
    |\boldsymbol a \times \boldsymbol b| &= |\boldsymbol a| |\boldsymbol b| \sin \langle \boldsymbol a, \boldsymbol b \rangle \\
    \boldsymbol a \cdot \boldsymbol b &= |\boldsymbol a| |\boldsymbol b| \cos \theta \\
    &= |\boldsymbol a| |\boldsymbol b| \cos \langle \boldsymbol a, \boldsymbol b\rangle
    \end{aligned}
    $$

    može se napisati identitet:

    $$
    (\boldsymbol a\times \boldsymbol b) \cdot (\boldsymbol a\times \boldsymbol b) = |\boldsymbol a|^2 |\boldsymbol b|^2-{(\boldsymbol a \cdot \boldsymbol b)}^2
    $$

4.  Vektorski produkt zadovoljava Jacobijev identitet:

    $$
    \boldsymbol a \times (\boldsymbol b \times \boldsymbol c) + \boldsymbol b \times (\boldsymbol c \times \boldsymbol a) + \boldsymbol c \times (\boldsymbol a \times \boldsymbol b) = \boldsymbol 0
    $$

### Primjene

U nastavku navodimo neke uobičajene primjene vektorskog produkta.

1.  Provjera jesu li dva vektora kolinearna:

    $$
    \exists\lambda \in \mathbf{R} (\boldsymbol{a} = \lambda \boldsymbol{b}) \iff \boldsymbol{a} \times \boldsymbol{b} = \boldsymbol{0}
    $$

    Dakle, vektorski produkt dvaju kolinearnih trodimenzionalnih vektora jednak je $\boldsymbol 0$; vektorski produkt trodimenzionalnog vektora sa samim sobom jednak je $\boldsymbol 0$; vektorski produkt trodimenzionalnog vektora i nulvektora jednak je $\boldsymbol 0$. Ako se kao definicija kolinearnosti dvaju vektora uzme da je vektorski produkt jednak nuli, slijedi da je nulvektor kolinearan sa svakim vektorom.

2.  Računanje površine paralelograma razapetog dvama vektorima:

    $$
    S \langle \boldsymbol a, \boldsymbol b \rangle = |\boldsymbol a \times \boldsymbol b|
    $$

#### Slučaj dvodimenzionalnih vektora

Za dvodimenzionalne vektore vektorski produkt nije moguće izračunati, ali se ipak može izračunati površina paralelograma razapetog dvama vektorima:

Označimo $\boldsymbol{a} = (m, n), \boldsymbol{b} = (p, q)$ i proširimo pravokutni koordinatni sustav u ravnini do pravokutnog koordinatnog sustava u prostoru tako da izvorna ravnina bude ravnina $xOy$ novog koordinatnog sustava; izvorne koordinate $(m, n)$ i $(p, q)$ postaju $(m, n, 0)$ i $(p, q, 0)$.

Tada je vektorski produkt tih dvaju vektora $(0, 0, mq - np)$, pa je površina paralelograma $|mq - np|$, što se može promatrati kao apsolutna vrijednost determinante drugog reda.

Pritom se prema pravilu desne ruke i predznaku koordinate $z$ može zaključiti kako je $\boldsymbol b$ usmjeren u odnosu na $\boldsymbol a$: ako je u smjeru suprotnom od kazaljke na satu, koordinata $z$ je pozitivna, a u protivnom negativna; skraćeno: **u smjeru kazaljke negativno, suprotno od kazaljke pozitivno**.

## Mješoviti produkt

Kao i vektorski produkt, mješoviti produkt vektora operacija je **svojstvena trodimenzionalnim vektorima**.

### Definicija

Neka su $\boldsymbol a, \boldsymbol b, \boldsymbol c$ tri vektora u trodimenzionalnom prostoru. Tada se $(\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c$ zove mješoviti produkt triju vektora $\boldsymbol a, \boldsymbol b, \boldsymbol c$ i označava $[\boldsymbol a \boldsymbol b \boldsymbol c]$ ili $(\boldsymbol a, \boldsymbol b, \boldsymbol c)$ ili $(\boldsymbol a \boldsymbol b \boldsymbol c)$ ili $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c)$. Geometrijsko značenje apsolutne vrijednosti mješovitog produkta $|(\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c|$ jest volumen paralelepipeda s bridovima $\boldsymbol a, \boldsymbol b, \boldsymbol c$.

Mješoviti produkt vektora može se prikazati determinantom trećeg reda:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c &= \det(\boldsymbol a, \boldsymbol b, \boldsymbol c) \\
&= \begin{vmatrix}
    a_x & b_x & c_x \\
    a_y & b_y & c_y \\
    a_z & b_z & c_z
\end{vmatrix} \\
&= a_x b_y c_z + a_y b_z c_x + a_z b_x c_y - a_z b_y c_x -a _y b_x c_z - a_x b_z c_y
\end{aligned}
$$

### Svojstva

1.  Mješoviti produkt linearan je u svakom od triju vektora zasebno; konkretno, vrijedi:

    $$
    \begin{aligned}
    \det(\lambda\boldsymbol{u} + \mu\boldsymbol{v}, \boldsymbol{b}, \boldsymbol{c}) &= \lambda\det(\boldsymbol{u}, \boldsymbol{b}, \boldsymbol{c}) + \mu\det(\boldsymbol{v}, \boldsymbol{b}, \boldsymbol{c}) \\
    \det(\boldsymbol{a}, \lambda\boldsymbol{u} + \mu\boldsymbol{v}, \boldsymbol{c}) &= \lambda\det(\boldsymbol{a}, \boldsymbol{u}, \boldsymbol{c}) + \mu\det(\boldsymbol{a}, \boldsymbol{v}, \boldsymbol{c}) \\
    \det(\boldsymbol{a}, \boldsymbol{b}, \lambda\boldsymbol{u} + \mu\boldsymbol{v}) &= \lambda\det(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{u}) + \mu\det(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{v})
    \end{aligned}
    $$

2.  Mješoviti produkt je antisimetričan: zamjena mjesta dvaju vektora mijenja predznak mješovitog produkta, pa vrijedi:

    $$
    \det(\boldsymbol a, \boldsymbol b, \boldsymbol c) = \det(\boldsymbol b, \boldsymbol c, \boldsymbol a) = \det(\boldsymbol c, \boldsymbol a, \boldsymbol b) = -\det(\boldsymbol b, \boldsymbol a, \boldsymbol c) = -\det(\boldsymbol a, \boldsymbol c, \boldsymbol b)= -\det(\boldsymbol c, \boldsymbol b, \boldsymbol a)
    $$

    Iz toga se može dobiti i sljedeća veza skalarnog i vektorskog produkta:

    $$
    (\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c = \boldsymbol a \cdot (\boldsymbol b \times \boldsymbol c)
    $$

### Primjene

Mješoviti produkt vektora ima sljedeće uobičajene primjene.

1.  Računanje volumena tetraedra $ABCD$:

    $$
    V=\frac{1}{6}\left|\det(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD})\right|
    $$

2.  Provjera jesu li $\boldsymbol a, \boldsymbol b, \boldsymbol c$ komplanarni;

    Tri trodimenzionalna vektora $\boldsymbol a, \boldsymbol b, \boldsymbol c$ komplanarna su ako i samo ako je $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c)=0$.

3.  Određivanje orijentacije (kiralnosti) koordinatnog sustava koji čine $\boldsymbol a, \boldsymbol b, \boldsymbol c$;

    Je li predznak mješovitog produkta $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c)$ pozitivan ili negativan ovisi o tome je li kut između $\boldsymbol a \times \boldsymbol b$ i $\boldsymbol c$ šiljast ili tup, tj. pokazuju li na istu ili na suprotnu stranu ravnine razapete vektorima $\boldsymbol a$ i $\boldsymbol b$, što je isto kao pitanje čine li vektori $\boldsymbol a, \boldsymbol b, \boldsymbol c$ u tom redoslijedu desni ili lijevi sustav. Konkretno:

    -   $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c) < 0$ ekvivalentno je tome da $\boldsymbol a, \boldsymbol b, \boldsymbol c$ u tom redoslijedu čine lijevi sustav;
    -   $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c) > 0$ ekvivalentno je tome da $\boldsymbol a, \boldsymbol b, \boldsymbol c$ u tom redoslijedu čine desni sustav.

## Dvostruki vektorski produkt

Mješoviti produkt trodimenzionalnih vektora kombinacija je skalarnog i vektorskog produkta i ima cikličku simetriju. Vektorski produkt dvaju trodimenzionalnih vektora opet je trodimenzionalni vektor; postoje li onda slični rezultati za vektorski produkt vektorskog produkta?

Najprije dokažimo jednu lemu.

$$
(\boldsymbol a \times \boldsymbol b)\times \boldsymbol a = (\boldsymbol a \cdot \boldsymbol a) \boldsymbol b - (\boldsymbol a \cdot \boldsymbol b) \boldsymbol a
$$

Dokaz: prema pravilu desne ruke, $\boldsymbol a \times \boldsymbol b$ okomit je i na $\boldsymbol a$ i na $\boldsymbol b$, a lijeva strana jednakosti koju dokazujemo okomita je na $\boldsymbol a \times \boldsymbol b$, pa je lijeva strana jednakosti komplanarna s $\boldsymbol a$ i $\boldsymbol b$.

Stoga možemo pretpostaviti:

$$
(\boldsymbol a \times \boldsymbol b)\times \boldsymbol a = \lambda \boldsymbol a + \mu \boldsymbol b
$$

Prema rezultatima o mješovitom produktu, pomnožimo li obje strane gornje jednakosti skalarno s $\boldsymbol a$ odnosno s $\boldsymbol b$, dobivamo:

$$
\begin{aligned}
\lambda (\boldsymbol a \cdot \boldsymbol a)+\mu (\boldsymbol a \cdot \boldsymbol b) &= 0 \\
\lambda (\boldsymbol a \cdot \boldsymbol b) + \mu (\boldsymbol b \cdot \boldsymbol b) &= \det(\boldsymbol b, \boldsymbol a \times \boldsymbol b, \boldsymbol a) \\
&= (\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol a \times \boldsymbol b)
\end{aligned}
$$

Prema ranije izvedenom identitetu:

$$
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol a \times \boldsymbol b) = |\boldsymbol a|^2|\boldsymbol b|^2-(\boldsymbol a \cdot \boldsymbol b)^2
$$

možemo riješiti:

$$
\begin{aligned}
\lambda &= -\boldsymbol a \cdot \boldsymbol b \\
\mu &= \boldsymbol a \cdot \boldsymbol a
\end{aligned}
$$

Time je dokaz završen.

U gornjem je dokazu spomenuto da je vektorski produkt vektora $\boldsymbol a \times \boldsymbol b$ s bilo kojim vektorom komplanaran s $\boldsymbol a$ i $\boldsymbol b$. Dokažimo sada rezultat o **dvostrukom vektorskom produktu**:

$$
(\boldsymbol a\times \boldsymbol b)\times \boldsymbol c=(\boldsymbol a \cdot \boldsymbol c)\boldsymbol b - (\boldsymbol b \cdot \boldsymbol c)\boldsymbol a
$$

Spomenuta komplanarnost pomaže pri pamćenju formule za dvostruki vektorski produkt. Vidimo da je gornja lema poseban slučaj dvostrukog vektorskog produkta.

Dokaz: dovoljno je razmotriti slučaj kad su sva tri vektora nenul i nekolinearni; ostali su posebni slučajevi očiti.

Trodimenzionalni vektori $\boldsymbol a$, $\boldsymbol b$ i $\boldsymbol a \times \boldsymbol b$ nisu komplanarni, pa možemo pretpostaviti:

$$
\boldsymbol c = \alpha \boldsymbol a + \beta \boldsymbol b + \gamma(\boldsymbol a \times \boldsymbol b)
$$

Stoga je:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol c &= (\boldsymbol a \times \boldsymbol b) \times (\alpha \boldsymbol a + \beta \boldsymbol b + \gamma(\boldsymbol a \times \boldsymbol b)) \\
&= \alpha(\boldsymbol a \times \boldsymbol b) \times \boldsymbol a + \beta(\boldsymbol a \times \boldsymbol b) \times \boldsymbol b
\end{aligned}
$$

Prema gornjoj lemi vrijedi:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol a &=(\boldsymbol a \cdot \boldsymbol a) \boldsymbol b - (\boldsymbol a \cdot \boldsymbol b) \boldsymbol a \\
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol b
&= -(\boldsymbol b \times \boldsymbol a) \times \boldsymbol b \\
&= -(\boldsymbol b \cdot \boldsymbol b)\boldsymbol a+(\boldsymbol a \cdot \boldsymbol b) \boldsymbol b
\end{aligned}
$$

Dakle:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol c &= \alpha((\boldsymbol a \cdot \boldsymbol a)\boldsymbol b - (\boldsymbol a \cdot \boldsymbol b)\boldsymbol a) + \beta((\boldsymbol a \cdot \boldsymbol b)\boldsymbol b - (\boldsymbol b \cdot \boldsymbol b)\boldsymbol a) \\
&=(\alpha(-\boldsymbol a \cdot \boldsymbol b) + \beta(-\boldsymbol b \cdot \boldsymbol b))\boldsymbol a + (\alpha \boldsymbol a \cdot \boldsymbol a + \beta \boldsymbol a \cdot \boldsymbol b)\boldsymbol b \\
&= (\boldsymbol a \cdot \boldsymbol c) \boldsymbol b - (\boldsymbol b \cdot \boldsymbol c) \boldsymbol a
\end{aligned}
$$

Time je dokaz završen.

Iz antikomutativnosti vektorskog produkta dobivaju se dvije formule za dvostruki vektorski produkt:

$$
\begin{aligned}
(\boldsymbol a\times \boldsymbol b)\times \boldsymbol c &=(\boldsymbol a \cdot \boldsymbol c)\boldsymbol b - (\boldsymbol b \cdot \boldsymbol c)\boldsymbol a \\
\boldsymbol a \times(\boldsymbol b \times \boldsymbol c) &= (\boldsymbol a \cdot \boldsymbol c)\boldsymbol b - (\boldsymbol a \cdot \boldsymbol b)\boldsymbol c
\end{aligned}
$$

Vidimo da dvostruki vektorski produkt ima stroge zahtjeve na redoslijed operacija.

Pomoću mješovitog i dvostrukog vektorskog produkta može se dokazati i Lagrangeov identitet.

$$
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol c \times \boldsymbol d)=(\boldsymbol a \cdot \boldsymbol c)(\boldsymbol b \cdot \boldsymbol d)-(\boldsymbol a \cdot \boldsymbol d)(\boldsymbol b \cdot \boldsymbol c)
$$

Dokaz:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol c \times \boldsymbol d) &= \det(\boldsymbol c, \boldsymbol d, \boldsymbol a \times \boldsymbol b) \\
&= \det(\boldsymbol a \times \boldsymbol b, \boldsymbol c, \boldsymbol d) \\
&= ((\boldsymbol a \times \boldsymbol b)\times \boldsymbol c)\cdot \boldsymbol d \\
&= (\boldsymbol b(\boldsymbol a \cdot \boldsymbol c)- \boldsymbol a(\boldsymbol b \cdot \boldsymbol c))\cdot \boldsymbol d \\
&= (\boldsymbol a \cdot \boldsymbol c)(\boldsymbol b \cdot \boldsymbol d) - (\boldsymbol a \cdot \boldsymbol d)(\boldsymbol b \cdot \boldsymbol c)
\end{aligned}
$$

Vidimo da je raniji identitet

$$
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol a \times \boldsymbol b) = |\boldsymbol a|^2|\boldsymbol b|^2 - (\boldsymbol a \cdot \boldsymbol b)^2
$$

poseban slučaj Lagrangeova identiteta.
