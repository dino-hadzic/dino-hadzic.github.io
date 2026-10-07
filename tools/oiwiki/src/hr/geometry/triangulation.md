---
title: Triangulacija
---

U geometriji triangulacija je podjela ravninskog objekta na trokute, a poopćeno – podjela višedimenzionalnog geometrijskog objekta na simplekse.
Za zadani skup točaka postoji mnogo triangulacija, npr.:

![Tri triangulacije](./images/triangulation-0.svg)

Ova stranica predstavlja dvodimenzionalnu Delaunayjevu triangulaciju (kraće DT) i algoritam njezine konstrukcije metodom podijeli pa vladaj.

## Delaunayjeva triangulacija

### Definicija

U matematici i računskoj geometriji, za zadani diskretan skup točaka $P$ u ravnini njegova Delaunayjeva triangulacija DT($P$) zadovoljava:

1.  Svojstvo prazne kružnice: DT($P$) je **jedinstvena** (ako nikoje četiri točke ne leže na istoj kružnici) i u DT($P$) unutar opisane kružnice **bilo kojeg** trokuta nema drugih točaka.
2.  Maksimizacija najmanjeg kuta: među svim triangulacijama skupa $P$, trokuti DT($P$) imaju najveći najmanji kut. U tom smislu DT($P$) je triangulacija **najbliža pravilnoj**. Konkretno, ako dva susjedna trokuta čine konveksan četverokut, zamjenom njegove dijagonale najmanji od unutarnjih kutova tih dvaju trokuta više se ne povećava.

![Delaunayjeva triangulacija s prikazanim opisanim kružnicama](./images/triangulation-1.svg)

### Svojstva

1.  Najbliže točke: trokute čine međusobno najbliže tri točke, a dužine (stranice trokuta) se međusobno ne sijeku.
2.  Jedinstvenost: bez obzira na to iz kojeg dijela područja počnemo konstrukciju, na kraju dobivamo isti rezultat (ako nikoje četiri točke skupa ne leže na istoj kružnici).
3.  Optimalnost: ako se dijagonala konveksnog četverokuta kojeg čine bilo koja dva susjedna trokuta može zamijeniti, najmanji od šest unutarnjih kutova tih dvaju trokuta neće se promijeniti.
4.  Najpravilnija: ako najmanje kutove svih trokuta triangulacije poredamo uzlazno, niz dobiven za Delaunayjevu triangulaciju ima najveće vrijednosti.
5.  Lokalnost: dodavanje, brisanje ili pomicanje jednog vrha utječe samo na susjedne trokute.
6.  Konveksna ljuska: vanjski rub triangulacije čini konveksan mnogokut (konveksnu ljusku).

## Algoritam podijeli pa vladaj za konstrukciju DT

Postoji više algoritama za konstrukciju DT; ovdje predstavljamo algoritam podijeli pa vladaj vremenske složenosti $O(n \log n)$.

Prvi korak konstrukcije DT metodom podijeli pa vladaj jest sortirati zadani skup točaka **uzlazno** po koordinati $x$, a pri jednakom $x$ uzlazno po koordinati $y$, te ukloniti točke koje se podudaraju. Na slici je sortirani skup od $10$ točaka.

![Sortirani skup od 10 točaka](./images/triangulation-2.svg)

Ako je točaka manje od $2$, ne treba povlačiti bridove. Inače sortirani skup uzastopno dijelimo po sredini na dva dijela dok podskupovi ne budu veličine $2$ ili $3$. Dvije točke spajamo bridom, tri nekolinearne točke trokutom, a od tri kolinearne točke spajamo samo dva para točaka susjednih u sortiranom poretku.

![Podjela na podskupove od 2 ili 3 točke](./images/triangulation-3.svg)

Zatim pri povratku iz rekurzije redom spajamo triangulacije lijevog i desnog podskupa. Bridovi nakon spajanja dijele se na LL-bridove (bridovi unutar lijevog podskupa), RR-bridove (bridovi unutar desnog podskupa) i LR-bridove (bridovi koji spajaju lijevi i desni podskup); na slici su redom sivi, crveni i plavi. Da bi se očuvala svojstva DT, pri spajanju **može** biti potrebno obrisati neke LL- i RR-bridove, ali se te dvije vrste bridova **nikad** ne dodaju.

![Tri vrste bridova nakon spajanja](./images/triangulation-4.svg)

Prvi korak spajanja lijeve i desne triangulacije jest pronaći donju zajedničku tangentu dviju konveksnih ljuski i umetnuti odgovarajući osnovni (base) LR-brid. Rekurzija vraća rubne bridove lijeve i desne ljuske; krećemo od najdesnije točke lijeve ljuske i najljevije točke desne ljuske te se pomičemo duž rubova ljuski dok nijedna točka ne bude desno od usmjerenog pravca od lijevog prema desnom krajištu.

![Spajanje lijeve i desne triangulacije](./images/triangulation-5.svg)

Zatim trebamo odrediti sljedeći LR-brid, onaj **neposredno iznad** osnovnog LR-brida. Primjerice, za desni skup točaka mogući (desni) krajevi sljedećeg LR-brida su drugi krajevi RR-bridova spojenih s desnim krajem osnovnog LR-brida (točke $6, 7, 9$), a lijevi kraj je točka $2$.

![Sljedeći LR-brid](./images/triangulation-6.svg)

Uzmimo za primjer desni kraj. Počevši od zrake prema lijevom kraju osnovnog LR-brida, u smjeru kazaljke na satu provjeravamo RR-bridove spojene s desnim krajem:

1.  Valjani kandidati su samo krajevi koji leže strogo iznad osnovnog LR-brida, tj. lijevo od usmjerenog pravca od lijevog prema desnom kraju osnovnog brida. Odgovarajući kut zakreta u smjeru kazaljke na satu mora biti u $(0^\circ,180^\circ)$.
2.  Neka je trenutni kandidat $c$, a sljedeći susjed u istom smjeru $d$. Ako $d$ leži strogo unutar kružnice opisane dvama krajevima osnovnog LR-brida i točki $c$, brišemo RR-brid prema $c$ i nastavljamo s provjerom brida prema $d$.
3.  Inače zadržavamo trenutnog kandidata i prekidamo provjeru na toj strani. Budući da je ta strana već Delaunayjeva triangulacija, dovoljno je uspoređivati susjedne kandidate u kružnom poretku.

![Provjera valjanih kandidata](./images/triangulation-7.svg)

Kao na slici, redom provjeravamo točke $6,7,9$. Zelena kružnica koja odgovara točki $6$ sadrži sljedećeg susjeda $7$, pa brišemo RR-brid prema $6$; ljubičasta kružnica koja odgovara točki $7$ ne sadrži sljedećeg susjeda $9$, pa zadržavamo $7$ kao desnog kandidata. Nakon toga ga još treba usporediti s lijevim kandidatom da bi se odredio sljedeći LR-brid.

Za lijevi skup točaka postupak je zrcalan: počinjemo od zrake prema desnom kraju osnovnog LR-brida i provjeravamo u smjeru suprotnom od kazaljke na satu.

![Provjera valjanih kandidata s lijeve strane](./images/triangulation-8.svg)

Kad ni lijeva ni desna strana nemaju valjanog kandidata, trenutni osnovni LR-brid je gornja zajednička tangenta i spajanje je gotovo. Ako samo jedna strana ima valjanog kandidata, spajamo ga s drugim krajem osnovnog LR-brida i dobivamo novi LR-brid.

Kad obje strane imaju valjanog kandidata: ako desni kandidat leži strogo unutar kružnice određene lijevim kandidatom i dvama krajevima osnovnog brida, biramo desnog kandidata; inače biramo lijevog. Odabranog kandidata spajamo s krajem osnovnog brida na suprotnoj strani i dobivamo novi LR-brid. Ako četiri točke leže na istoj kružnici, oba su izbora dobra.

![Sljedeći LR-brid](./images/triangulation-9.svg)

Kad je taj LR-brid dodan, uzimamo ga kao osnovni LR-brid i ponavljamo gornje korake, dodajući sljedeći, dok spajanje ne završi.

![Spajanje](./images/triangulation-10.svg)

### Implementacija

Ako bridove čuvamo samo u neuređenim listama susjedstva i pri svakom dodavanju LR-brida pregledavamo sve susjedne bridove obaju krajeva, vremenska je složenost $O(n^2)$, jer jedan kraj može uzastopno tvoriti više LR-bridova, pa se njegova lista susjedstva pregledava iznova i iznova.

Referentna implementacija koristi strukturu quad-edge[^quad-edge] za održavanje kružnog poretka bridova. Svaki neusmjereni brid zapisan je s četiri usmjerena brida: dva predstavljaju dva smjera u izvornom grafu, a druga dva predstavljaju dva smjera u dualnom grafu. Ta su četiri zapisa pohranjena uzastopno, pa je dovoljno za svaki usmjereni brid čuvati njegov početak i sljedeći brid s istim početkom u smjeru suprotnom od kazaljke na satu, čime se sljedeće operacije izvode u vremenu $O(1)$:

| Operacija       | Značenje                                                                   |
| --------------- | -------------------------------------------------------------------------- |
| `rev(e)`        | suprotno usmjereni brid                                                    |
| `onext(e)`      | sljedeći brid s istim početkom, u smjeru suprotnom od kazaljke na satu     |
| `oprev(e)`      | prethodni brid s istim početkom, u smjeru suprotnom od kazaljke na satu    |
| `lnext(e)`      | pomak za jedan brid naprijed duž ruba lijeve strane                        |
| `onext(rev(e))` | pomak za jedan brid natrag duž ruba desne strane                           |

`splice(a, b)` istodobno mijenja kružne odnose u izvornom i u dualnom grafu; služi za spajanje ili razdvajanje prstenova kojima pripadaju dva brida. `connect(a, b)` unutar iste strane spaja kraj brida `a` s početkom brida `b`. Pri brisanju brida njegova se dva smjera uklanjaju iz odgovarajućih prstenova. Te topološke operacije mijenjaju samo konstantan broj zapisa; referentna implementacija dodjeljuje i reciklira bridove pomoću dinamičkog polja, uz amortizirano vrijeme $O(1)$.

U kodu je `base` usmjeren od desnog skupa točaka prema lijevom, pa točke „iznad” osnovnog LR-brida na slikama leže desno od usmjerenog brida `base`. Lijevi kandidat je `onext(rev(base))`, a desni `oprev(base)`; nakon brisanja kandidata dovoljno je nastaviti duž kružnog poretka na toj strani.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/geometry/code/triangulation/triangulation_1.cpp:delaunay"
    ```

### Složenost

Neka jedno spajanje obuhvaća $k$ točaka. Pri traženju donje zajedničke tangente svaki pomak napreduje duž ruba ljuske na jednoj od strana, ukupno $O(k)$ puta. Pri izboru kandidata svaka daljnja provjera prati brisanje jednog LL- ili RR-brida, a dvije podtriangulacije zajedno imaju samo $O(k)$ bridova. Glavna petlja spajanja, osim tih brisanja, u svakom koraku obavi konstantan broj provjera i doda jedan LR-brid; novododani LR-bridovi se u ovom spajanju više ne brišu, pa ih je također $O(k)$. Ukupno vrijeme jednog spajanja stoga je $O(k)$.

Početno sortiranje traje $O(n \log n)$, rekurzija zadovoljava $T(n)=T(\lfloor n/2 \rfloor)+T(\lceil n/2 \rceil)+O(n)$, pa je ukupna vremenska složenost $O(n \log n)$. U svakom trenutku zadržano je $O(n)$ bridova, a kod reciklira mjesta obrisanih bridova umjesto da čuva sve bridove iz povijesti, pa je prostorna složenost $O(n)$.

## Voronoijev dijagram

Zadano je $n\ge 1$ međusobno različitih točaka (sjedišta) u ravnini. Voronoijeva regija svakog sjedišta sastoji se od svih točaka čija udaljenost do tog sjedišta nije veća od udaljenosti do bilo kojeg drugog sjedišta. Te su regije konveksna, moguće neograničena područja; njihove se unutrašnjosti ne sijeku i zajedno pokrivaju cijelu ravninu, a zajednička granica dviju susjednih regija leži na simetrali dužine koja spaja odgovarajuća dva sjedišta.

Za skup točaka koje nisu sve kolinearne i u kojem nikoje četiri točke ne leže na istoj kružnici, Voronoijev dijagram i Delaunayjeva triangulacija međusobno su dualni: svakom trokutu odgovara središte njegove opisane kružnice, svakom unutarnjem bridu dužina koja spaja središta opisanih kružnica dvaju susjednih trokuta, a svakom bridu konveksne ljuske zraka iz središta opisane kružnice pripadnog trokuta, okomita na taj brid i usmjerena prema van iz ljuske. Ako četiri točke leže na istoj kružnici, nakon konstrukcije treba spojiti podudarna središta i ukloniti dualne bridove duljine nula. Ako su sve točke kolinearne, Voronoijevi bridovi su simetrale dužina između točaka susjednih u sortiranom poretku; ako je točka samo jedna, njezina regija je cijela ravnina.

![Dualnost Voronoijeva dijagrama i Delaunayjeve triangulacije](./images/triangulation-11.svg)

Na slici su pune točke $P_i$ sjedišta, a prazne točke $O_i$ središta opisanih kružnica trokuta; plave pune linije čine Voronoijev dijagram, a narančaste isprekidane linije Delaunayjevu triangulaciju. Boje pozadine razlikuju pojedine Voronoijeve regije, strelice označavaju neograničene bridove; prikazan je samo dio unutar konačnog prozora.

Nakon konstrukcije DT, koristeći postojeći kružni poredak bridova za nabrajanje strana i bridova, gornja se pretvorba obavlja u vremenu $O(n)$, pa je ukupna vremenska složenost konstrukcije Voronoijeva dijagrama $O(n \log n)$.

## Zadaci

[Luogu P6362 Euklidsko minimalno razapinjuće stablo u ravnini](https://www.luogu.com.cn/problem/P6362) klasična primjena triangulacije

[SGU 383 Caravans](https://codeforces.com/problemsets/acmsguru/problem/99999/383) triangulacija + binary lifting

[ContestHunter. Beskrajno uništenje](http://noi-test.zzstep.com/contest/Beta%20Round%20%EF%BC%832%20%28%E6%96%B0%E7%96%86%E7%9C%81%E9%98%9F%E4%BA%92%E6%B5%8BWeek1-Day2%29/%E6%97%A0%E5%B0%BD%E7%9A%84%E6%AF%81%E7%81%AD) triangulacija, pa dualni graf za konstrukciju Voronoijeva dijagrama

[Codeforces Gym 103485M. Constellation collection](https://codeforces.com/gym/103485/problem/M) nakon triangulacije izgraditi graf i provesti flood fill

## Literatura i daljnje čitanje

1.  [Wikipedia - Triangulation (geometry)](https://en.wikipedia.org/wiki/Triangulation_%28geometry%29)
2.  [Wikipedia - Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation)
3.  [Samuel Peterson - Computing Constrained Delaunay Triangulations in 2-D (1997-98)](http://www.geom.uiuc.edu/~samuelp/del_project.html)

[^quad-edge]: Leonidas Guibas, Jorge Stolfi. [Primitives for the Manipulation of General Subdivisions and the Computation of Voronoi Diagrams](https://people.eecs.berkeley.edu/~jrs/meshpapers/GuibasStolfi.pdf). ACM Transactions on Graphics, 4(2), 1985, 74–123.
