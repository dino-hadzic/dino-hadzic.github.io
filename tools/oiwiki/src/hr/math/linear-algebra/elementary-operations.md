---
title: Elementarne transformacije
---

## Elementarne matrice

Sljedeće tri vrste kvadratnih matrica nazivaju se elementarnim matricama.

### Matrica množenja

Matrica množenja (scaling matrix) posebna je dijagonalna matrica.

$$
D_i(k)=\operatorname{diag}\{1,\cdots,1,k,1,\cdots,1\}
$$

Označava dijagonalnu matricu kojoj je $i$-ti element na glavnoj dijagonali jednak $k$, pri čemu se zahtijeva da $k$ nije $0$, a svi ostali elementi jednaki su $1$.

Posebno, kad je $k$ jednak $1$, $D_i(1)$ upravo je jedinična matrica $I$.

### Matrica zamjene

Matrica zamjene (switching matrix) posebna je simetrična matrica.

$$
P_{ij}=\begin{pmatrix}
I_{i-1} &  &  &  & \\
 & 0 &  & 1 & \\
 &  & I_{j-i-1} &  & \\
 & 1 &  & 0 & \\
 &  &  &  & I_{n-j}\\
\end{pmatrix}
$$

Svi elementi matrice zamjene jesu $1$ ili $0$; na glavnoj dijagonali svi su ostali elementi $1$, samo su $i$-ti i $j$-ti element jednaki $0$, a dva elementa u $i$-tom retku i $j$-tom stupcu te u $j$-tom retku i $i$-tom stupcu jednaka su $1$.

Za matricu zamjene zahtijeva se da $i$ i $j$ nisu jednaki.

### Matrica dodavanja

Matrica dodavanja (addition matrix) dobiva se iz jedinične matrice $I$ tako da se element u $i$-tom retku i $j$-tom stupcu postavi na $k$.

$$
T_{ij}(k)=\begin{pmatrix}
1 &  &  &  &  &  & \\
 & \ddots &  &  &  &  & \\
 &  & 1 & \cdots & k &  & \\
 &  &  & \ddots & \vdots &  & \\
 &  &  &  & 1 &  & \\
 &  &  &  &  & \ddots & \\
 &  &  &  &  &  & 1\\
\end{pmatrix}
$$

Za matricu dodavanja zahtijeva se da $i$ i $j$ nisu jednaki. Ako je $k$ jednak $0$, $T_{ij}(0)$ degenerira u jediničnu matricu $I$.

Matrica dodavanja gornja je ili donja trokutasta matrica.

### Determinante elementarnih matrica

Tri vrste elementarnih matrica imaju determinante:

$$
|D_i(k)|=k
$$

$$
|P_{ij}|=-1
$$

$$
|T_{ij}(k)|=1
$$

Budući da je determinanta umnoška kvadratnih matrica jednaka umnošku determinanti, uz ekvivalenciju elementarnih transformacija i množenja matrica opisanu u nastavku, ovo se svojstvo elementarnih matrica može iskoristiti za računanje determinanti.

## Elementarne transformacije

Ne samo na kvadratnim matricama nego i na općoj matrici $A$ mogu se izvoditi elementarne transformacije redaka i elementarne transformacije stupaca, zajedničkim imenom elementarne transformacije.

Elementarnih transformacija redaka, kao i elementarnih transformacija stupaca, ima 3 vrste: množenje (multiplication), zamjena (switching) i dodavanje (addition). Najprije opisujemo elementarne transformacije redaka:

-   $i$-ti redak množi se brojem $k$ različitim od nule: $B\mapsto D_i(k)B$.
-   $i$-ti i $j$-ti redak zamjenjuju mjesta: $B\mapsto P_{ij}B$.
-   $j$-ti redak pomnožen s $k$ dodaje se $i$-tom retku: $B\mapsto T_{ij}(k)B$.

Zamijenimo li u gornjim operacijama retke stupcima, dobivamo elementarne transformacije stupaca.

Među elementarnim transformacijama zamjena se može ostvariti množenjem i dodavanjem. Očito se dodavanje ne može ostvariti množenjem i zamjenom. Uz znanje o determinantama i ekvivalenciju elementarnih transformacija i množenja matrica iz nastavka može se pokazati i da se množenje ne može ostvariti dodavanjem i zamjenom.

Stoga su, u usporedbi sa zamjenom, množenje i dodavanje bitnije operacije. Zamjena je pomoćna operacija uvedena zato da bi se u metodi eliminacije osigurao uredan redoslijed eliminiranja.

## Elementarne transformacije i množenje matrica

Može se primijetiti da se sve tri vrste elementarnih matrica dobivaju tako da se na jediničnoj matrici $I$ izvede jedna odgovarajuća transformacija. U kasnijem odjeljku o linearnim preslikavanjima istaknut će se da između linearnih preslikavanja i matrica postoji korespondencija slična ovoj ovdje.

Bez obzira na to je li matrica $A$ kvadratna, elementarna transformacija redaka matrice $A$ ekvivalentna je množenju matrice $A$ elementarnom matricom slijeva. Elementarna transformacija stupaca matrice $A$ ekvivalentna je množenju matrice $A$ elementarnom matricom zdesna.

### Operacija množenja

Množenje slijeva matricom množenja $D_i(k)$ ekvivalentno je množenju $i$-tog retka s $k$. Množenje zdesna matricom množenja $D_i(k)$ ekvivalentno je množenju $i$-tog stupca s $k$.

Umnožak dijagonalnih matrica opet je dijagonalna matrica; pri množenju dijagonalnih matrica množe se odgovarajući elementi na glavnoj dijagonali. Budući da je jedinična matrica posebna matrica množenja, a matrica množenja zahtijeva da $k$ nije $0$, vidimo da se dijagonalna matrica može rastaviti na umnožak matrica množenja čim su svi njezini elementi na glavnoj dijagonali različiti od $0$.

Za opću dijagonalnu matricu, bez obzira na to jesu li neki elementi $0$, vrijedi odgovarajući zaključak. Množenje slijeva dijagonalnom matricom ekvivalentno je množenju odgovarajućih redaka nekim faktorom, a faktor je upravo odgovarajući element na glavnoj dijagonali dijagonalne matrice. Množenje zdesna dijagonalnom matricom ista je operacija na odgovarajućim stupcima.

Budući da je determinanta matrice množenja $D_i(k)$ jednaka $k$, nakon operacije množenja na retku ili stupcu kvadratne matrice njezina determinanta postaje $k$ puta veća. Determinanta dijagonalne matrice umnožak je elemenata na glavnoj dijagonali.

Množenje matrica množenja je komutativno, a komutativno je i množenje dijagonalnih matrica; kad se u umnošku pojavljuju samo dijagonalne matrice, redoslijed može biti proizvoljan.

Operacija množenja koja odgovara jediničnoj matrici ostavlja matricu $A$ nepromijenjenom; u praksi se takva operacija ne izvodi.

### Operacija zamjene

Množenje slijeva matricom zamjene $P_{ij}$ ekvivalentno je zamjeni $i$-tog i $j$-tog retka. Množenje zdesna matricom zamjene $P_{ij}$ ekvivalentno je zamjeni $i$-tog i $j$-tog stupca.

Slično odnosu između matrica množenja i dijagonalnih matrica, ovdje uvodimo pojam permutacijske matrice. Permutacijska matrica kvadratna je matrica koja u svakom retku i svakom stupcu ima točno jednu $1$, a na ostalim mjestima $0$. Jedinična matrica $I$ također je posebna permutacijska matrica.

Permutacijska matrica odgovara permutiranju redaka jedinične matrice $I$, a jednako tako i permutiranju stupaca jedinične matrice $I$. Sama jedinična matrica $I$ odgovara identičkom preslikavanju.

Množenje slijeva permutacijskom matricom ekvivalentno je permutiranju redaka izvorne matrice, a množenje zdesna permutacijskom matricom ekvivalentno je permutiranju stupaca izvorne matrice; pripadna permutacija jednaka je onoj kojom su permutirani retci odnosno stupci jedinične matrice $I$.

Permutacijske matrice u potpunoj su korespondenciji s permutacijama; multiplikativna grupa permutacijskih matrica izomorfna je grupi permutacija. Prema poznatom teoremu, ako se identičko preslikavanje smatra umnoškom nula transpozicija, svaka se permutacija može rastaviti na umnožak transpozicija, pa se stoga i svaka permutacijska matrica može rastaviti na umnožak matrica zamjene.

Budući da je determinanta matrice zamjene $-1$, nakon operacije zamjene na retcima ili stupcima kvadratne matrice njezina se determinanta množi s $-1$.

Množenje matrica zamjene nije komutativno, a ni množenje permutacijskih matrica nije komutativno.

Determinanta permutacijske matrice jednaka je ${(-1)}^p$, gdje je $p$ broj inverzija permutacije koja odgovara permutacijskoj matrici, tj. broj transpozicija u rastavu permutacije na umnožak transpozicija.

### Operacija dodavanja

Množenje slijeva matricom dodavanja $T_{ij}(k)$ ekvivalentno je dodavanju $k$-terostrukog $j$-tog retka $i$-tom retku. Množenje zdesna matricom dodavanja $T_{ij}(k)$ ekvivalentno je dodavanju $k$-terostrukog $i$-tog stupca $j$-tom stupcu.

Ako je to teško zapamtiti, može se pogledati koja je operacija na jediničnoj matrici $I$ dala matricu dodavanja $T_{ij}(k)$; te dvije stvari odgovaraju jedna drugoj: množenje slijeva operacija je na retcima, množenje zdesna operacija je na stupcima, u skladu s mnemonikom „lijevo redak, desno stupac”.

Budući da je determinanta matrice dodavanja $1$, nakon operacije dodavanja na kvadratnoj matrici njezina se determinanta ne mijenja.

Množenje matrica dodavanja nije komutativno.

Operacija dodavanja koja odgovara jediničnoj matrici ostavlja matricu $A$ nepromijenjenom; u praksi se takva operacija ne izvodi.

#### Gornja trokutasta matrica

Matrica dodavanja gornja je ili donja trokutasta matrica. Budući da su te dvije vrste matrica simetrične s obzirom na glavnu dijagonalu, ovdje razmatramo gornje trokutaste matrice. Zapravo su u ovom primjeru potrebne samo elementarne transformacije redaka, a ne i transformacije stupaca.

Ako su svi elementi na glavnoj dijagonali gornje trokutaste matrice jednaki $1$, ona se može rastaviti na umnožak niza matrica dodavanja. Redoslijed rastavljanja je sljedeći: najprije se operacija dodavanja izvodi na prvom retku jedinične matrice $I$, zatim na drugom retku jedinične matrice $I$, i tako dalje, dok se ne obradi svaki redak.

Budući da množenje matrica dodavanja nije komutativno, redoslijed gornjih operacija ne smije se mijenjati.

Ako su svi elementi na glavnoj dijagonali gornje trokutaste matrice različiti od $0$, ona se može rastaviti na umnožak niza matrica dodavanja i matrica množenja. Pri obradi svakog retka jedinične matrice $I$ najprije se na tom retku izvede operacija množenja, čime element na glavnoj dijagonali postaje zadana vrijednost različita od nule.

Ako na glavnoj dijagonali gornje trokutaste matrice postoji $0$, ona se ne može rastaviti na umnožak niza elementarnih matrica.

Bez obzira na to ima li na glavnoj dijagonali gornje trokutaste matrice $0$, determinanta gornje trokutaste matrice jednaka je umnošku elemenata na glavnoj dijagonali, jednako kao kod dijagonalnih matrica.

#### Pretvaranje kvadratne matrice u dijagonalnu operacijama dodavanja

Samo operacijama dodavanja svaka se kvadratna matrica može pretvoriti u dijagonalnu; u ovom su primjeru potrebne i elementarne transformacije redaka i elementarne transformacije stupaca.

Ako u prvom retku i prvom stupcu kvadratne matrice postoji element različit od nule, operacijom dodavanja možemo element u gornjem lijevom kutu učiniti različitim od nule, a zatim elementarnim transformacijama redaka i stupaca sve elemente prvog retka i prvog stupca, osim onog u gornjem lijevom kutu, pretvoriti u $0$.

Ako su prvi redak i prvi stupac kvadratne matrice već u cijelosti $0$, izravno prelazimo na drugi redak i drugi stupac.

Ovim se postupkom čak može postići da se svi elementi dijagonalne matrice različiti od nule nalaze u gornjem lijevom kutu.

Ako su prvi redak i prvi stupac kvadratne matrice već u cijelosti $0$, provjeravamo ima li u preostalim retcima i stupcima elemenata različitih od nule; čim ih ima, operacijom dodavanja neki element prvog retka i prvog stupca možemo učiniti različitim od $0$ i tako se svesti na početnu situaciju u kojoj je element u gornjem lijevom kutu različit od $0$.

Jedino kad ni u preostalim retcima i stupcima nema elemenata različitih od nule, element u gornjem lijevom kutu ne može se učiniti različitim od nule; tada je preostala kvadratna matrica već nul-matrica.

#### Matrica u normalnom obliku

Elementarnim transformacijama svaka se matrica, bez obzira na oblik, može svesti na matricu u normalnom obliku.

Matrica u normalnom obliku ima jediničnu matricu $I$ kao podmatricu u gornjem lijevom kutu, a svi ostali elementi jednaki su $0$. Postupak svođenja sličan je pretvaranju kvadratne matrice u dijagonalnu, a dodatno se operacijama množenja elementi različiti od nule u gornjem lijevom kutu pretvaraju u $1$.

Nakon svođenja matrice na normalni oblik broj elemenata jednakih $1$ upravo je rang matrice.

## Invertibilne matrice

Neka je $A$ matrica $n$-tog reda. Ako postoji matrica $B$ $n$-tog reda takva da je $AB=BA=I$, matrica $A$ naziva se invertibilnom (regularnom) ili nesingularnom matricom, a $B$ se naziva inverznom matricom matrice $A$ i označava s $A^{-1}$.

Ako je matrica $A$ invertibilna, inverzna matrica od $A$ jednoznačno je određena matricom $A$.

Inverz $A^{-1}$ invertibilne matrice $A$ također je invertibilan, a inverz od $A^{-1}$ upravo je $A$.

Umnožak $AB$ dviju invertibilnih matrica $A$ i $B$ također je invertibilan, a njegov je inverz $B^{-1}A^{-1}$.

Transponirana matrica $A^T$ invertibilne matrice $A$ također je invertibilna, a inverz transponirane matrice jednak je transponiranoj matrici inverza.

### Inverzi elementarnih matrica

Sve su elementarne matrice invertibilne, a inverz je elementarna matrica iste vrste:

$$
{D_i(k)}^{-1}=D_i\left(\frac{1}{k}\right)
$$

$$
P_{ij}^{-1}=P_{ij}
$$

$$
T_{ij}(k)^{-1}=T_{ij}(-k)
$$

Očito je jedinična matrica $I$ invertibilna, a njezin je inverz opet $I$.

Elementarne transformacije čuvaju invertibilnost matrice: matrice prije i poslije transformacije ili su obje invertibilne ili su obje neinvertibilne.

Matrica $A$ invertibilna je ako i samo ako se može zapisati kao umnožak elementarnih matrica, tj. ako se $A$ elementarnim transformacijama može pretvoriti u jediničnu matricu $I$.

Nakon uvođenja determinanti znat ćemo:

Matrica $A$ invertibilna je ako i samo ako je rang matrice $A$ jednak $n$, ako i samo ako je determinanta matrice $A$ različita od $0$.

Jednostavan zapis: označimo s $E_{ij}$ matricu tipa $n\times n$ kojoj je element u $i$-tom retku i $j$-tom stupcu jednak $1$, a ostali su nula; tada je

-   $D_i(k)=I_n+(k-1)E_{ii}$
-   $P_{ij}=I_n-E_{ii}-E_{jj}+E_{ij}+E_{ji}$
-   $T_{ij}(k)=I_n+kE_{ij}$

Taj se zapis može primijeniti i na njihove inverzne matrice.

## Primjene

### Rješavanje sustava linearnih jednadžbi

Za sustav linearnih jednadžbi koeficijenti uz nepoznanice čine matricu sustava (matricu koeficijenata); dopišemo li s desne strane matrice sustava slobodne članove sustava, dobivamo proširenu matricu sustava.

Primjenom elementarnih transformacija redaka proširena matrica sustava linearnih jednadžbi može se najprije svesti na retčani ešelonski oblik (row echelon form), zatim na reducirani retčani ešelonski oblik (reduced row echelon form), čime je sustav riješen. Ta se metoda naziva rješavanjem sustava linearnih jednadžbi eliminacijom, a Gauss–Jordanova eliminacija opisana kasnije algoritam je eliminacije koji se provodi u određenom redoslijedu.

### Računanje determinante

Budući da je determinanta umnoška kvadratnih matrica jednaka umnošku njihovih determinanti, determinante elementarnih matrica lako se računaju, a elementarne transformacije ekvivalentne su množenju elementarnim matricama, elementarne se transformacije koriste i pri računanju determinanti.

Budući da je elementarne transformacije koje se provode u određenom redoslijedu lakše programirati, za računanje determinante može se upotrijebiti i Gauss–Jordanova eliminacija opisana kasnije.
