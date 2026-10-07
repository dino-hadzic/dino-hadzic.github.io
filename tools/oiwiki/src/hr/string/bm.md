---
title: Boyer–Mooreov algoritam
---

Predznanje: [Prefiksna funkcija i KMP algoritam](./kmp.md).

KMP algoritam do krajnjih granica iskorištava informacije o podudaranju prefiksa,

dok je osnovna ideja BM algoritma da podudaranjem sufiksa dobije više informacija nego podudaranjem prefiksa i time postigne brže skokove po znakovima.

## Uvod

Zamislimo da je naš uzorak $pat$ postavljen na lijevi početak teksta $string$, tako da su im prvi znakovi poravnati.

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\texttt{EXAMPLE} \\
\textit{string}:\qquad\quad &\texttt{HERE IS A SIMPLE EXAMPLE} \dots \\
&\qquad\ \ \ \, \, \Uparrow
\end{aligned}
$$

Ovdje uvodimo definicije koje dalje nećemo ponavljati:

duljina $pat$ je $patlen$; posebno, za stringove indeksirane od 0 definiramo $patlastpos=patlen-1$ kao poziciju posljednjeg znaka u $pat$;

duljina $string$ je $stringlen$, $stringlastpos = stringlen-1$.

Pretpostavimo da znamo $patlen$-ti znak $char$ teksta $string$ (poravnat s posljednjim znakom $pat$). Razmotrimo koje informacije iz toga možemo dobiti:

### Opažanje 1

Ako znamo da se znak $char$ ne pojavljuje u $pat$, ne trebamo razmatrati pojavljivanja $pat$ koja počinju na $1.$, $2.$, …, $patlen$-tom znaku teksta $string$, nego $pat$ možemo izravno pomaknuti za $patlen$ znakova.

### Opažanje 2

Općenitije, **ako je pozicija posljednjeg (tj. najdesnijeg) pojavljivanja znaka $char$ u $pat$ udaljena $delta_1$ znakova od kraja**,

onda bez podudaranja možemo $pat$ izravno pomaknuti za $delta_1$ znakova: ako bi pomak bio manji od $delta_1$, već se sam znak $char$ ne bi mogao podudariti, pa se ne bi podudario ni uzorak $pat$.

Dakle, osim ako se znak $char$ podudara s posljednjim znakom $pat$, u $string$ treba preskočiti $delta_1$ znakova (što odgovara pomaku $pat$ za $delta_1$ znakova). Tako dobivamo funkciju $delta_1(char)$ za računanje $delta_1$:

$$
\begin{array}{ll}
\textbf{int}\ delta1(\textbf{char}\ char) \\
\qquad \textbf{if}\ \text{char nije u pat || char je posljednji znak u pat} \\
\qquad\qquad\textbf{return}\ patlen \\
\qquad \textbf{else} \\
\qquad\qquad\textbf{return}\ patlastpos-i\quad\textbf{//}\ \text{i je pozicija najdesnijeg pojavljivanja char u pat, tj. pat[i]=char}
\end{array}
$$

Uočimo da ovu tablicu očito treba izračunati samo do pozicije $patlastpos-1$.

Pretpostavimo sada da se $char$ podudario s posljednjim znakom $pat$; tada provjeravamo podudara li se znak ispred $char$ s pretposljednjim znakom $pat$:

ako da, nastavljamo unatrag dok se cijeli uzorak $pat$ ne podudari (tada smo u $string$ uspješno pronašli pojavljivanje $pat$);

ili se može dogoditi da se, nakon što smo podudarili posljednjih $m$ znakova $pat$, na $(m+1)$-om znaku od kraja dogodi nepodudaranje. Tada želimo $pat$ pomaknuti na sljedeću poziciju na kojoj bi se podudaranje moglo ostvariti, i naravno želimo pomak što veći.

### Opažanje 3(a)

U **Opažanju 2** rečeno je da, kad se nakon podudaranja posljednjih $m$ znakova $pat$ dogodi nepodudaranje na $(m+1)$-om znaku od kraja, da bi se nepodudareni znak u $string$ poravnao s odgovarajućim znakom u $pat$,

treba $pat$ pomaknuti za $k$ znakova, tj. pozornost trebamo usmjeriti na znak $k+m$ mjesta dalje (tj. na znak u $string$ koji je nakon pomaka $pat$ za k poravnat s krajem $pat$).

A $k=delta_1-m$,

pa pozornost duž $string$ trebamo pomaknuti za $delta_1-m+m = delta_1$ znakova.

No imamo priliku preskočiti još više znakova; čitajte dalje.

### Opažanje 3(b)

Ako znamo da se sljedećih $m$ znakova $string$ podudara s posljednjih $m$ znakova $pat$, nazovimo taj podstring $subpat$.

Znamo i da se iza nepodudarenog znaka $char$ u $string$ nalazi podstring koji se podudara sa $subpat$; ako u $pat$ ispred znaka koji odgovara nepodudarenom znaku postoji $subpat$, možemo $pat$ pomaknuti za određenu udaljenost,

tako da se $subpat$ koji se u $pat$ pojavljuje ispred znaka koji odgovara nepodudarenom znaku $char$ (plausible reoccurrence – „vjerodostojno ponovno pojavljivanje”, u nastavku skraćeno pr) poravna sa $subpat$ u $string$. Ako u $pat$ ima više $subpat$, prema redoslijedu sufiksnog podudaranja zdesna nalijevo uzimamo prvi (rightmost plausible reoccurrence, u nastavku skraćeno rpr).

Pretpostavimo da se $pat$ pritom pomiče za $k$ znakova (tj. udaljenost između $subpat$ na kraju $pat$ i njegova najdesnijeg vjerodostojnog ponovnog pojavljivanja); tada pozornost duž $string$ trebamo pomaknuti za $k+m$ znakova. Tu udaljenost zovemo $delta_2(j)$:

Neka je $rpr(j)$ pozicija najdesnijeg vjerodostojnog ponovnog pojavljivanja $subpat=pat[j+1\dots patlastpos]$ pri nepodudaranju na $pat[j]$, $rpr(j) < j$ (ovdje dajemo samo jednostavnu definiciju; preciznija rasprava slijedi u odjeljku o dizajnu algoritma). Tada je očito $k=j-rpr(j),\ m=patlastpos-j$.

Stoga imamo:

$$
\begin{array}{ll}
\textbf{int}\ delta2(\textbf{int}\ j) \quad\textbf{//}\ \text{j je pozicija znaka u pat koji odgovara nepodudarenom znaku} \\
\qquad\qquad\textbf{return}\ patlastpos-rpr(j) \\
\end{array}
$$

Dakle, pri nepodudaranju pozornost na $string$ možemo pomaknuti za $\max(delta_1,delta_2)$ znakova.

## Postupak

Strelica pokazuje na nepodudareni znak $char$:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \, \, \Uparrow
\end{aligned}
$$

$\texttt{F}$ se ne pojavljuje u $pat$, pa prema **Opažanju 1** $pat$ izravno pomičemo za $patlen$ znakova, tj. 7 znakova:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\quad\ \ \, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \, \, \qquad\quad\ \ \ \Uparrow
\end{aligned}
$$

Prema **Opažanju 2** $pat$ trebamo pomaknuti za 4 znaka da bi se crtice poravnale:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\qquad\quad\ \ \, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \; \qquad\qquad\qquad \Uparrow
\end{aligned}
$$

Sada se *char*:$\texttt{T}$ podudario; pokazivač na $string$ pomičemo za jedan korak ulijevo i nastavljamo podudaranje:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\qquad\quad\ \ \, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \; \qquad\qquad\quad\ \, \Uparrow
\end{aligned}
$$

Prema **Opažanju 3(a)** $\texttt{L}$ se ne podudara; budući da $\texttt{L}$ nije u $pat$, $pat$ pomičemo za $k=delta_1-m=7-1=6$ znakova, a pokazivač na $string$ za $delta_1=7$ znakova:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\qquad\qquad\qquad\ \ \,\, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \; \qquad\qquad\qquad\qquad\ \ \ \, \, \Uparrow
\end{aligned}
$$

Sada se $char$ opet podudario s posljednjim znakom $pat$, $\texttt{T}$; pokazivač na $string$ ide ulijevo, podudara $\texttt{A}$, nastavlja ulijevo i otkriva nepodudaranje na znaku $\texttt{-}$:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\qquad\qquad\qquad\ \ \,\, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \; \qquad\qquad\qquad\quad\ \ \ \,\, \Uparrow
\end{aligned}
$$

Intuitivno je očito da, prema **Opažanju 3(b)**, $pat$ pomičemo za $k=5$ znakova tako da se sufiks $\texttt{AT}$ poravna; taj pomak daje najveći pomak pokazivača na $string$, pri čemu je $delta_2=k+patlastpos-j=5+6-4=7$, tj. pokazivač na $string$ pomičemo za 7 znakova.

Formalno gledano, ovdje je $delta_1=7-1-2=4,\ delta_2=7, \max(delta_1,delta_2)= 7$,
što formalno potvrđuje skok iz **Opažanja 3(b)**:

$$
\begin{aligned}
\textit{pat}:\qquad\qquad &\qquad\qquad\qquad\qquad\qquad\quad \;\, \texttt{AT-THAT} \\
\textit{string}:\ \ \ \dots\ &\texttt{WHICH-FINALLY-HALTS.--AT-THAT-POINT} \dots \\
&\qquad\ \ \ \; \qquad\qquad\qquad\qquad\qquad\quad \ \ \; \Uparrow
\end{aligned}
$$

Sada vidimo da je svaki znak $pat$ jednak odgovarajućem znaku $string$: pronašli smo pojavljivanje $pat$ u $string$. Pritom smo potrošili samo 14 pristupa $string$, od kojih je 7 nužnih usporedbi za uspješno podudaranje ($patlen=7$), a ostalih 7 omogućilo nam je preskakanje 22 znaka.

## Dizajn algoritma

### Izvorni algoritam podudaranja

#### Objašnjenje

Promotrimo sljedeći algoritam podudaranja stringova koji koristi $delta_1$ i $delta_2$:

$$
\begin{array}{ll}
i \gets patlastpos. \\
j \gets patlastpos. \\
\textbf{loop}\\
\qquad \textbf{if}\ j < 0 \\
\qquad \qquad \textbf{return}\ i+1 \\
\\
\qquad \textbf{if}\ string[i]=pat[j] \\
\qquad \qquad j \gets j-1 \\
\qquad \qquad i \gets i-1 \\
\qquad \qquad \textbf{continue} \\
\\
\qquad i \gets i+max(delta_1(string[i]), delta_2(j)) \\
\\
\qquad \textbf{if}\ i > stringlastpos \\
\qquad \qquad \textbf{return}\ false \\
\qquad j \gets patlastpos \\
\end{array}
$$

Ako gornji algoritam vrati $\textbf{return}\ false$, $pat$ nije u $string$; ako vrati broj, to je pozicija prvog pojavljivanja $pat$ u $string$ slijeva.

Opišimo sada preciznije funkciju $rpr(j)$ na koju se oslanja računanje $delta_2$.

Prema ranijoj definiciji, $rpr(j)$ je pozicija najdesnijeg vjerodostojnog ponovnog pojavljivanja podstringa $subpat=pat[j+1\dots patlastpos]$ kad se nepodudaranje dogodi na $pat[j]$.

Drugim riječima, treba pronaći najbolji $k$ takav da je $pat[k\dots k+patlastpos-j-1]=pat[j+1\dots patlastpos]$, uz dva posebna slučaja:

1.  Kad je $k<0$, to odgovara dodavanju virtualnog prefiksa ispred $pat$, što je zapravo u skladu s načelom skoka $delta_2$.
2.  Kad je $k>0$, ako je $pat[k-1]=pat[j]$, tada $pat[k\dots k+patlastpos-j-1]$ ne može biti vjerodostojno ponovno pojavljivanje $subpat$.
    Razlog je što je $pat[j]$ sam nepodudareni znak, pa bi se nakon pomaka $pat$ za $k$ znakova pri sufiksnom podudaranju opet dogodilo nepodudaranje na $pat[k-1]$.

Treba paziti i na dva ograničenja:

1.  $k < j$. Jer kad je $k=j$, vrijedi $pat[k]=pat[j]$, pa bi se znak koji se ne podudara na $pat[j]$ ne bi podudario ni na $pat[k]$.
2.  Budući da je $delta_2(patlastpos)= 0$, definiramo $rpr(patlastpos) = patlastpos$.

#### Postupak

Budući da je razumijevanje $rpr(j)$ srž implementacije Boyer–Mooreova algoritma, detaljno ga objašnjavamo na sljedeća dva primjera:

$$
\begin{aligned}
\textit{j}:\qquad\qquad\quad\ \ &\texttt{0 1 2 3 4 5 6 7 8} \\
\textit{pat}:\qquad\qquad\ \  &\texttt{A B C X X X A B C} \\
\textit{rpr(j)}:\qquad\quad\  \  &\texttt{5 4 3 2 1 0 2 1 8} \\
\textit{sgn}:\qquad\qquad\ \   &\texttt{- - - - - - - - +}
\end{aligned}
$$

Za $rpr(0)$, $subpat$ je $\texttt{BCXXXABC}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[0]$ može biti samo $\texttt{[(BCXXX)ABC]XXXABC}$, tj. pozicija najdesnijeg vjerodostojnog ponovnog pojavljivanja je -5, dakle $rpr(j)=-5$;

za $rpr(1)$, $subpat$ je $\texttt{CXXXABC}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[1]$ je $\texttt{[(CXXX)ABC]XXXABC}$, pa je $rpr(j)=-4$;

za $rpr(2)$, $subpat$ je $\texttt{XXXABC}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[2]$ je $\texttt{[(XXX)ABC]XXXABC}$, pa je $rpr(j)=-3$;

za $rpr(3)$, $subpat$ je $\texttt{XXABC}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[3]$ je $\texttt{[(XX)ABC]XXXABC}$, pa je $rpr(j)=-2$;

za $rpr(4)$, $subpat$ je $\texttt{XABC}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[4]$ je $\texttt{[(X)ABC]XXXABC}$, pa je $rpr(j)=-1$;

za $rpr(5)$, $subpat$ je $\texttt{ABC}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[5]$ je $\texttt{[ABC]XXXABC}$, pa je $rpr(j)=0$;

za $rpr(6)$, $subpat$ je $\texttt{BC}$; budući da je $string[0]=string[6]$, tj. $string[0]$ jednak je nepodudarenom znaku $string[6]$, $string[0\dots 2]$ nije valjano vjerodostojno ponovno pojavljivanje $subpat$, pa je najdesnije vjerodostojno ponovno pojavljivanje $\texttt{[(BC)]ABCXXXABC}$, dakle $rpr(j)=-2$;

za $rpr(7)$, $subpat$ je $\texttt{C}$; slično, budući da je $string[7]=string[1]$, $string[1\dots 2]$ nije valjano vjerodostojno ponovno pojavljivanje $subpat$, pa je najdesnije vjerodostojno ponovno pojavljivanje $\texttt{[(C)]ABCXXXABC}$, dakle $rpr(j)=-1$;

za $rpr(8)$, prema definiciji $delta_2$, $rpr(patlastpos)=patlastpos$, pa je $rpr(8)=8$.

Pogledajmo sada još jedan primjer:

$$
\begin{aligned}
\textit{j}:\qquad\qquad\quad\ \ &\texttt{0 1 2 3 4 5 6 7 8} \\
\textit{pat}:\qquad\qquad\ \ &\texttt{A B Y X C D E Y X} \\
\textit{rpr(j)}:\qquad\quad\  \  &\texttt{8 7 6 5 4 3 2 1 8} \\
\textit{sgn}:\qquad\qquad\ \   &\texttt{- - - - - - + - +}
\end{aligned}
$$

Za $rpr(0)$, $subpat$ je $\texttt{BYXCDEYX}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[0]$ može biti samo $\texttt{[(BYXCDEYX)]ABYXCDEYX}$, tj. pozicija najdesnijeg vjerodostojnog ponovnog pojavljivanja je -8, dakle $rpr(j)=-8$;

za $rpr(1)$, $subpat$ je $\texttt{YXCDEYX}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[1]$ može biti samo $\texttt{[(YXCDEYX)]ABYXCDEYX}$, $rpr(j)=-7$;

za $rpr(2)$, $subpat$ je $\texttt{XCDEYX}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[2]$ može biti samo $\texttt{[(XCDEYX)]ABYXCDEYX}$, $rpr(j)=-6$;

za $rpr(3)$, $subpat$ je $\texttt{CDEYX}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[3]$ može biti samo $\texttt{[(CDEYX)]ABYXCDEYX}$, $rpr(j)=-5$;

za $rpr(4)$, $subpat$ je $\texttt{DEYX}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[4]$ može biti samo $\texttt{[(DEYX)]ABYXCDEYX}$, $rpr(j)=-4$;

za $rpr(5)$, $subpat$ je $\texttt{EYX}$; najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[5]$ može biti samo $\texttt{[(EYX)]ABYXCDEYX}$, $rpr(j)=-3$;

za $rpr(6)$, $subpat$ je $\texttt{YX}$; budući da je $string[2\dots 3]=string[7\dots 8]$ i $string[6]\neq string[1]$, najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[6]$ je $\texttt{AB[YX]CDEYX}$, $rpr(j)=2$;

za $rpr(7)$, $subpat$ je $\texttt{X}$; iako je $string[3]=string[8]$, budući da je $string[2] = string[7]$, najdesnije vjerodostojno ponovno pojavljivanje ispred $pat[7]$ je $\texttt{[X]ABYXCDEYX}$, $rpr(j)=-1$;

za $rpr(8)$, prema definiciji $delta_2$, $rpr(patlastpos)=patlastpos$, pa je $rpr(8)=8$.

### Poboljšanje algoritma podudaranja

Naposljetku, u praksi se procjenjuje da se oko 80 % vremena pretraživanja troši na skokove iz **Opažanja 1**, tj. na slučaj kad se $string[i]$ i $pat[patlastpos]$ ne podudaraju i zatim preskačemo cijeli $patlen$ do sljedećeg podudaranja.

Stoga za to možemo napraviti posebnu optimizaciju:

definiramo $delta0$:

$$
\begin{array}{ll}
\textbf{int}\ delta0(\textbf{char}\ char) \\
\qquad \textbf{if}\ char=pat[patlastpos] \\
\qquad\qquad \textbf{return}\ large\ \ \text{// large je cijeli broj koji zadovoljava large>stringlastpos+patlen} \\
\qquad \textbf{return}\ delta1(char)
\end{array}
$$

Zamjenom $delta_1$ s $delta0$ dobivamo poboljšani algoritam podudaranja:

$$
\begin{array}{ll}
i \gets patlastpos \\
\textbf{loop} \\
\qquad\textbf{if} \ i > stringlastpos \\
\qquad\qquad\textbf{return}\ false\\
\\
\qquad\textbf{while}\ i < stringlen \\
\qquad\qquad i \gets i+delta0(string(i)) \ \ \text{// osim ako se string[i] podudara s posljednjim znakom pat, pomak je najviše patlen }\\\
\qquad\textbf{if}\ i \leqslant\ large \qquad\qquad\qquad\qquad \text{// to znači da se nijedan znak u string ne podudara s posljednjim znakom pat}\ \\
\qquad\qquad\textbf{return}\ false\\
\\
\qquad i \gets i-large \\
\qquad j \gets patlastpos. \\
\qquad\textbf{while}\ j \geqslant\ 0 \ and \  string[i]=pat[j]\\
\qquad \qquad j \gets j-1 \\
\qquad \qquad i \gets i-1 \\
\\
\qquad \textbf{if}\ j < 0 \\
\qquad \qquad \textbf{return}\ i+1 \\
\qquad i \gets i+max(delta_1(string[i]), delta_2(j)) \\
\\
\end{array}
$$

Pritom $large$ ima više uloga: prvo, omogućuje brze skokove po lošem znaku slično Horspoolovu algoritmu opisanom dalje; drugo, pomaže pri provjeri je li pretraživanje stringa završeno.

Nakon poboljšanja, u odnosu na izvorni algoritam, pri skokovima iz **Opažanja 1** više ne treba svaki put suvišno računati $delta_2$, čime se performanse pretraživanja nad uobičajenim abecedama znatno poboljšavaju.

## Detalji izgradnje delta2

### Uvod

U listopadu 1977. u *Communications of the ACM* Boyer i Moore u svom radu[^bm] opisali su samo statičku tablicu $delta_2$,

a rasprava o konkretnoj implementaciji izgradnje $delta_2$ pojavila se u lipnju 1977. u radu o KMP algoritmu[^kmp] koji su Knuth, Morris i Pratt zajednički objavili u *SIAM Journal on Computing*.

### Naivni algoritam

Prije opisa Knuthova algoritma za izgradnju $delta_2$, prema definiciji imamo naivni algoritam prikladan za male probleme:

1.  Za svaku poziciju `i` u intervalu `[0, patlen)`, prema duljini `subpat` odredimo interval mogućih pozicija ponovnog pojavljivanja, tj. `[-subpatlen, i]`;
2.  moguće pozicije ponovnog pojavljivanja uspoređujemo znak po znak zdesna nalijevo i tražimo najdesniju poziciju ponovnog pojavljivanja $subpat$ koja zadovoljava zahtjeve $delta_2$;
3.  na kraju ne zaboravimo postaviti $delta_2(lastpos)= 0$.

???+ note "Implementacija"
    ```Rust
    use std::cmp::PartialEq;
    
    pub fn build_delta_2_table_naive(p: &[impl PartialEq]) -> Vec<usize> {
        let patlen = p.len();
        let lastpos = patlen - 1;
        let mut delta_2 = vec![];
        
        for i in 0..patlen {
            let subpatlen = (lastpos - i) as isize;
            
            if subpatlen == 0 {
                delta_2.push(0);
                break;
            }
            
            for j in (-subpatlen..(i + 1) as isize).rev() {
                // podudaranje subpat
                if (j..j + subpatlen)
                .zip(i + 1..patlen)
                .all(|(rpr_index, subpat_index)| {
                    if rpr_index < 0 {
                        return true;
                    }
                    
                    if p[rpr_index as usize] == p[subpat_index] {
                        return true;
                    }
                    
                    false
                })
                && (j <= 0 || p[(j - 1) as usize] != p[i])
                {
                    delta_2.push((lastpos as isize - j) as usize);
                    break;
                }
            }
        }
        
        delta_2
    }
    ```

Posebno, dajemo nužna objašnjenja značajki jezika Rust, koja dalje nećemo ponavljati:

-   `usize` i `isize` su neoznačeni i označeni cijeli brojevi iste širine kao memorijski pokazivač; na 32-bitnim strojevima odgovaraju `u32` i `i32`, a na 64-bitnim `u64` i `i64`.
-   Pri indeksiranju polja, vektora i odsječaka koriste se brojevi tipa `usize` (jer se radi o nasumičnom pristupu memoriji i indeks ne može biti negativan); stoga, ako treba raditi s negativnim vrijednostima, koristi se `isize`, a pri indeksiranju opet `usize`, pa se ključnom riječju `as` vrši eksplicitna pretvorba među njima.
-   `impl PartialEq` služi samo kao generički tip koji istodobno podržava `char` u kodiranju `Unicode` i binarni `u8`.

Očito je vremenska složenost ovog naivnog algoritma $O(n^3)$.

### Učinkoviti algoritam

U nastavku opisujemo učinkoviti algoritam vremenske složenosti $O(n)$, koji međutim zahtijeva dodatnih $O(n)$ prostora.

Iako je Knuth 1977. predložio ovu metodu izgradnje, njegova izvorna verzija ima nedostatak: za neke $pat$ zapravo ne daje $delta_2$ u skladu s definicijom.

Rytter je 1980. u članku[^rytter] u *SIAM Journal on Computing* predložio ispravak; slijedi algoritam izgradnje $delta_2$:

Najprije, budući da je definicija $delta_2$ razmjerno složena, klasificiramo slučajeve prema poziciji ponovnog pojavljivanja $subpat$ i svaku klasu obrađujemo zasebno; to je ključna ideja učinkovite implementacije.

Prema poziciji ponovnog pojavljivanja od najdalje do najbliže, tj. prema pomaku od najvećeg do najmanjeg, razlikujemo sljedeće klase:

1.  Cijelo ponovno pojavljivanje $subpat$ nalazi se potpuno lijevo od $pat$, npr. $\texttt{[(EYX)]ABYXCDEYX}$; tada je $delta_2(j) = patlastpos\times 2 - j$;

2.  ponovno pojavljivanje $subpat$ dijelom je lijevo od $pat$, a dijelom je početak $pat$, npr. $\texttt{[(XX)ABC]XXXABC}$; tada je $patlastpos < delta_2(j) < patlastpos\times 2 - j$;
    ovamo ubrajamo i rubni slučaj kad je $subpat$ u cijelosti početak $pat$ (ovisno o implementaciji može se svrstati i u sljedeću klasu), npr. $\texttt{[ABC]XXXABC}$; tada je $patlastpos = delta_2(j)$;

3.  ponovno pojavljivanje $subpat$ u cijelosti je unutar $pat$, npr. $\texttt{AB[YX]CDEYX}$; tada je $delta_2(j) < patlastpos$.

Razmotrimo sada kako učinkovito izračunati ova tri slučaja:

#### Prvi slučaj

To je najjednostavniji slučaj: dovoljan je jedan prolaz, kojim usput možemo inicijalizirati $delta_2$.

#### Drugi slučaj

Promotrimo kada se događa da je ponovno pojavljivanje $subpat$ dijelom lijevo od $pat$, a dijelom početak $pat$. To je kad je neki sufiks $subpat$ jednak nekom prefiksu $pat$,

npr. u ranijem primjeru:

$$
\begin{aligned}
\textit{j}:\qquad\qquad\quad\ \ &\texttt{0 1 2 3 4 5 6 7 8} \\
\textit{pat}:\qquad\qquad\ \  &\texttt{A B C X X X A B C} \\
\end{aligned}
$$

ponovno pojavljivanje za $delta_2(3)$ je $\texttt{[(XX)ABC]XXXABC}$; među sufiksima $subpat$ $\texttt{XXABC}$ i prefiksima pat postoji jednak par, $\texttt{ABC}$.

Zapravo je za računanje drugog i trećeg slučaja ključno računanje i primjena prefiksne funkcije.

Dakle, kad god $j$ poprimi vrijednost takvu da $subpat$ sadrži taj jednaki sufiks, dobivamo ponovno pojavljivanje $subpat$ drugog slučaja; u primjeru treba samo $j \leqslant 5$,

a kad je $j = 5$, imamo rubni slučaj u kojem je $subpat$ u cijelosti početak $pat$.

Izračunajmo tada $delta_2(j)$:

neka je duljina tog para jednakih prefiksa i sufiksa $\textit{prefixlen}$; znamo $subpatlen = patlastpos - j$, pa je duljina dijela lijevo od $pat$ jednaka $subpatlen-\textit{prefixlen}$,

a $rpr(j) = -(subpatlen-\textit{prefixlen})$, pa dobivamo $delta_2(j) = patlastpos - rpr(j) = patlastpos \times 2 - j - \textit{prefixlen}$.

Nakon toga može postojati više parova jednakih prefiksa i sufiksa, npr.:

$$
\begin{aligned}
\textit{j}:\qquad\qquad\quad\ \ &\texttt{0 1 2 3 4 5 6 7 8 9} \\
\textit{pat}:\qquad\qquad\ \  &\texttt{A B A A B A A B A A} \\
\end{aligned}
$$

Za $j\leq2$ imamo $\texttt{ABAABAA}$, za $2< j \leq 5$ imamo $\texttt{ABAA}$, a za $5<j\leq8$ imamo $\texttt{A}$.

Nedostatak Knuthova algoritma jest što razmatra samo najdulji par, a zapravo treba razmotriti sve slučajeve u kojima je sufiks $subpat$ jednak prefiksu $pat$, što je ekvivalentno računanju svih jednakih pravih sufiksa i pravih prefiksa $pat$ te, po duljini od najveće do najmanje, računanju različitih $delta_2(j)$ po intervalima $j$.

Pomoću prefiksne funkcije i obrnute primjene jednadžbe prijelaza stanja za računanje prefiksne funkcije, $j^{(n)} = \pi[j^{(n-1)}-1]$, dobivamo duljine svih jednakih pravih prefiksa i pravih sufiksa $pat$. Krećemo od $\pi[patlastpos]$ kao duljine najduljeg para, a zatim obrnutom primjenom jednadžbe prijelaza stanja dobivamo duljinu sljedećeg najduljeg para jednakih pravih prefiksa i sufiksa.

Time je računanje $delta_2$ za drugi slučaj dovršeno.

#### Treći slučaj

Ponovno pojavljivanje $subpat$ nalazi se upravo unutar $pat$ (ne uključujući početak $pat$), tj. tražimo $subpat$ u $pat[0\dots patlastpos-1]$ zdesna nalijevo.

Ako to rješavamo BM algoritmom, dobivamo rekurzivnu BM implementaciju trećeg slučaja, s uvjetom zaustavljanja $patlen \leqslant  2$.

Osim toga, prema definiciji $delta_2$, sljedeći (tj. lijevi) znak pronađenog ponovnog pojavljivanja $subpat$ ne smije biti jednak sljedećem znaku $subpat$ koji je sufiks $pat$.

To nas lijepo navodi na to da treći slučaj možemo izračunati postupkom sličnim računanju prefiksne funkcije, samo s prefiksnom funkcijom u kojoj su lijevo i desno zamijenjeni:

-   dva pokazivača pokazuju redom na lijevi kraj podstringa i na poziciju „prefiksa” najduljeg zajedničkog prefiksa-sufiksa podstringa; pomiču se zdesna nalijevo, a kad su znakovi na koje pokazuju jednaki, nastavljaju se pomicati, što odgovara povećanju „prefiksa”;
-   kad dva znaka nisu jednaka, prethodno jednaki dio zadovoljava zahtjev $delta_2$ za ponovno pojavljivanje, a pokazivač na poziciju „prefiksa” vraćamo unatrag dok se ne uspostavi nova jednakost znakova ili dok ne izađe izvan granica.

Kao i kod prefiksne funkcije, potrebno je pomoćno polje za vraćanje unatrag; može se iskoristiti prostor prefiksnog polja generiranog pri računanju drugog slučaja.

### Implementacija

??? note "Implementacija gore opisanog"
    ```rust
    use std::cmp::PartialEq;
    use std::cmp::min;
    
    pub fn build_delta_2_table_improved_minghu6(p: &[impl PartialEq]) -> Vec<usize> {
        let patlen = p.len();
        let lastpos = patlen - 1;
        let mut delta_2 = Vec::with_capacity(patlen);
        
        // prvi slučaj
        // delta_2[j] = lastpos * 2 - j
        for i in 0..patlen {
            delta_2.push(lastpos * 2 - i);
        }
        
        // drugi slučaj
        // lastpos <= delata2[j] = lastpos * 2 - j
        let pi = compute_pi(p);  // računanje prefiksne funkcije
        let mut i = lastpos;
        let mut last_i = lastpos; // samo radi inicijalizacije
        while pi[i] > 0 {
            let start;
            let end;
            
            if i == lastpos {
                start = 0;
            } else {
                start = patlen - pi[last_i];
            }
            
            end = patlen - pi[i];
            
            for j in start..end {
                delta_2[j] = lastpos * 2 - j - pi[i];
            }
            
            last_i = i;
            i = pi[i] - 1;
        }
        
        // treći slučaj
        // delata2[j] < lastpos
        let mut j = lastpos;
        let mut t = patlen;
        let mut f = pi;
        loop {
            f[j] = t;
            while t < patlen && p[j] != p[t] {
                // funkcijom min osiguravamo da kasnije moguće vraćanje unatrag ne prepiše ranije podatke
                delta_2[t] = min(delta_2[t], lastpos - 1 - j);
                t = f[t];
            }
            
            t -= 1;
            if j == 0 {
                break;
            }
            j -= 1;
        }
        
        // nema stvarnog značenja, samo radi potpune definicije
        delta_2[lastpos] = 0;
        
        delta_2
    }
    ```

## Galilovo pravilo i poboljšanje najgoreg slučaja pri višestrukom podudaranju

### Problem višestrukog podudaranja kod algoritama sufiksnog podudaranja

Prethodni algoritam pretraživanja odnosi se samo na pronalaženje prvog pojavljivanja $pat$ u $string$, dok za pronalaženje svih pojavljivanja $pat$ u $string$ postoji mnogo različitih algoritamskih pristupa. Središnje je pitanje ovog problema: kako iskoristiti informacije o prethodno uspješno podudarenim znakovima da bi se vremenska složenost u najgorem slučaju svela na linearnu.

Ako nakon uspješnog podudaranja jednostavno pomaknemo pokazivač na $string$ za $patlen$ i ponovno započnemo sufiksno podudaranje, u najgorem se slučaju vraćamo na složenost $O(mn)$ (prema uobičajenoj konvenciji $m$ je $patlen$, a $n$ je $stringlen$; isto vrijedi dalje).

Na primjer, ekstreman slučaj: $pat$: $\texttt{AAA}$, $string$: $\texttt{AAAAA}\dots$.

Knuth je za to predložio metodu koja „konačnim” skupom stanja bilježi znakove duljine $patlen$; taj algoritam jamči da se svaki znak u $string$ uspoređuje najviše jednom, ali po cijenu toga da taj „konačni” skup stanja može biti prilično velik: za $pat$ čiji su znakovi međusobno različiti potrebno je $\dfrac{1}{2}m^{2}+m$ stanja.

U nastavku opisujemo jednostavan pristup koji ne zahtijeva dodatnu pretprocesiranje — Galilov algoritam[^galil-rule].

### Galilovo pravilo

Pretpostavimo da je $pat$ prefiks stringa $UUUU\dots$ nastalog ponavljanjem nekog podstringa $U$ n puta; tada $U$ zovemo periodom od $pat$.

Na primjer, $pat: \texttt{ABCABCAB}$ prefiks je ponavljanja $\texttt{ABCABCABC}$ stringa $\texttt{ABC}$, pa je duljina $\texttt{ABC}$, $3$, duljina perioda ovog $pat$, tj. $pat$ zadovoljava $pat[i] = pat[i+3]$.

$pat$ ima barem jedan period duljine jednake vlastitoj duljini; najkraći period označimo s $k$, $k\leq patlen$.

Ako tijekom pretraživanja naš $pat$ uspješno dovrši jedno podudaranje, onda prema svojstvima perioda zapravo trebamo pomaknuti $string$ samo za $k$ znakova i usporediti jesu li tih $k$ znakova redom jednaki da bismo izravno utvrdili postoji li još jedno pojavljivanje $pat$.

Za računanje duljine najkraćeg perioda pretpostavimo da znamo par jednakih prefiks-sufiks od $pat$ duljine $\textit{prefixlen}$; tada vrijedi $pat[i] = pat[i+(patlen-\textit{prefixlen})]$. Time dobivamo period duljine $patlen-\textit{prefixlen}$,

a kad znamo najdulji par jednakih prefiks-sufiks od $pat$, dobivamo najkraći period od $pat$.

Duljinu najduljeg jednakog prefiksa-sufiksa, $\pi[patlastpos]$, već imamo iz postupka računanja $delta_2$, pa zapravo bez dodatnog vremena i prostora pretprocesiranja vremensku složenost algoritma sufiksnog podudaranja u najgorem slučaju možemo poboljšati na linearnu.

??? note "Konačna implementacija BM algoritma pretraživanja s gornjim optimizacijama"
    ```rust
    #[cfg(target_pointer_width = "64")]
    const LARGE: usize = 10_000_000_000_000_000_000;
    
    #[cfg(not(target_pointer_width = "64"))]
    const LARGE: usize = 2_000_000_000;
    
    pub struct BMPattern<'a> {
        pat_bytes: &'a [u8],
        delta_1: [usize; 256],
        delta_2: Vec<usize>,
        k: usize  // duljina najkraćeg perioda pat
    }
    
    impl<'a> BMPattern<'a> {
        // ...
        
        pub fn find_all(&self, string: &str) -> Vec<usize> {
            let mut result = vec![];
            let string_bytes = string.as_bytes();
            let stringlen = string_bytes.len();
            let patlen = self.pat_bytes.len();
            let pat_last_pos = patlen - 1;
            let mut string_index = pat_last_pos;
            let mut pat_index;
            let l0 =  patlen - self.k;
            let mut l = 0;
            
            while string_index < stringlen {
                let old_string_index = string_index;
                
                while string_index < stringlen {
                    string_index += self.delta0(string_bytes[string_index]);
                }
                if string_index < LARGE {
                    break;
                }
                
                string_index -= LARGE;
                
                // Ako se string_index pomaknuo, od posljednjeg uspješnog podudaranja dogodilo se barem jedno neuspješno podudaranje.
                // Tada pomak ponovnog podudaranja po Galilovu pravilu treba vratiti na nulu.
                if old_string_index < string_index {
                    l = 0;
                }
                
                pat_index = pat_last_pos;
                
                while pat_index > l && string_bytes[string_index] == self.pat_bytes[pat_index] {
                    string_index -= 1;
                    pat_index -= 1;
                }
                
                if pat_index == l && string_bytes[string_index] == self.pat_bytes[pat_index] {
                    result.push(string_index - l);
                    
                    string_index += pat_last_pos - l + self.k;
                    l = l0;
                } else {
                    l = 0;
                    string_index += max(
                        self.delta_1[string_bytes[string_index] as usize],
                        self.delta_2[pat_index],
                    );
                }
            }
            
            result
        }
    }
    ```

### Utjecaj najgoreg slučaja na performanse u praksi

S praktičnog stajališta, teorijski najgori slučaj ne utječe lako na performanse; čak i na testovima s nasumičnim tekstom nad vrlo malom abecedom od samo 4 znaka utjecaj tog najgoreg slučaja premalen je da bi se primijetio.

Zato, ako nije dobro dizajnirano, Galilovo pravilo može malo usporiti prosječne performanse, ali za neke ekstremno posebne $pat$ i $string$, poput primjera $pat$: $\texttt{AAA}$, $string$: $\texttt{AAAAA}\dots$, primjena Galilova pravila doista poboljšava performanse višestruko.

## Poboljšani algoritmi

### Simplified Boyer–Moore algoritam

Najsloženiji dio BM algoritma izgradnja je tablice $delta_2$ (tj. tablice dobrog sufiksa), a u praksi se pokazalo da performanse podudaranja nad uobičajenim abecedama uglavnom ovise o tablici $delta_1$ (tj. tablici lošeg znaka). Tako je nastala pojednostavnjena verzija BM algoritma koja koristi samo tablicu $delta_1$, a čije se performanse obično vrlo malo razlikuju od izvorne.

### Boyer–Moore–Horspol algoritam

Horspolov algoritam također se temelji na pravilu lošeg znaka: primjenjuje $delta_1$ na znak poravnat s krajem $pat$. Učinak je sličan poboljšanju izvornog algoritma podudaranja, a performanse su obično bolje od izvorne verzije.

???+ note "Implementacija"
    ```rust
    pub struct HorspoolPattern<'a> {
        pat_bytes: &'a [u8],
        bm_bc: [usize; 256],
    }
    
    impl<'a> HorspoolPattern<'a> {
        // ...
        pub fn find_all(&self, string: &str) -> Vec<usize> {
            let mut result = vec![];
            let string_bytes = string.as_bytes();
            let stringlen = string_bytes.len();
            let pat_last_pos = self.pat_bytes.len() - 1;
            let mut string_index = pat_last_pos;
            
            while string_index < stringlen {
                if &string_bytes[string_index-pat_last_pos..string_index+1] == self.pat_bytes {
                    result.push(string_index-pat_last_pos);
                }
                
                string_index += self.bm_bc[string_bytes[string_index] as usize];
            }
            
            result
        }
    }
    ```

### Boyer–Moore–Sunday algoritam

Sundayev algoritam također koristi pravilo lošeg znaka, samo što u odnosu na Horspool ide korak dalje: izravno promatra znak koji slijedi iza znaka poravnatog s krajem $pat$.

Za implementaciju je dovoljno malo izmijeniti tablicu $delta_1$, što odgovara izgradnji nad $pat$ duljine $patlen+1$.

Sundayev algoritam obično se smatra jednim od praktičnih algoritama koji su u općem slučaju najjednostavniji za implementaciju i s najboljim prosječnim performansama; obično je nešto brži od Horspoola i BM-a.

???+ note "Implementacija"
    ```rust
    pub struct SundayPattern<'a> {
        pat_bytes: &'a [u8],
        sunday_bc: [usize; 256],
    }
    
    impl<'a> SundayPattern<'a> {
        // ...
        fn build_sunday_bc(p: &'a [u8]) -> [usize; 256] {
            let mut sunday_bc_table = [p.len() + 1; 256];
            
            for i in 0..p.len() {
                sunday_bc_table[p[i] as usize] = p.len() - i;
            }
            
            sunday_bc_table
        }
        
        pub fn find_all(&self, string: &str) -> Vec<usize> {
            let mut result = vec![];
            let string_bytes = string.as_bytes();
            let pat_last_pos = self.pat_bytes.len() - 1;
            let stringlen = string_bytes.len();
            let mut string_index = pat_last_pos;
            
            while string_index < stringlen {
                if &string_bytes[string_index - pat_last_pos..string_index+1] == self.pat_bytes {
                    result.push(string_index - pat_last_pos);
                }
                
                if string_index + 1 == stringlen {
                    break;
                }
                
                string_index += self.sunday_bc[string_bytes[string_index + 1] as usize];
            }
            
            result
        }
    }
    ```

### Algoritam BMHBNFS

Ovaj algoritam kombinira Horspool i Sunday; to je algoritam `find` koji CPython koristi u implementaciji modula `stringlib`[^b5s], u nastavku skraćeno B5S.

Osnovna ideja B5S-a:

1.  Prema ideji sufiksnog podudaranja najprije usporedimo jesu li znakovi na poziciji $patlastpos$ jednaki; ako jesu, usporedimo jesu li znakovi na pozicijama $0\dots patlastpos-1$ jednaki; ako su i dalje jednaki, pronašli smo podudaranje;

2.  ako u bilo kojoj fazi dođe do nepodudaranja, prelazimo u fazu skoka;

3.  u fazi skoka najprije promatramo je li znak koji slijedi iza pozicije $patlastpos$ u $pat$; ako nije, izravno se pomičemo udesno za $patlen+1$, što je maksimalno iskorištenje Sundayeva algoritma;

    ako taj znak jest u $pat$, na znak na poziciji $patlastpos$ primjenjujemo Horspoolov skok pomoću $delta_1$.

Ovisno o tome je li primarni cilj ušteda vremena ili ušteda prostora, implementacije algoritma uvelike se razlikuju.

#### Verzija koja štedi vrijeme

???+ note "Implementacija"
    ```rust
    pub struct B5STimePattern<'a> {
        pat_bytes: &'a [u8],
        alphabet: [bool;256],
        bm_bc: [usize;256],
        k: usize
    }
    
    impl<'a> B5STimePattern<'a> {
        pub fn new(pat: &'a str) -> Self {
            assert_ne!(pat.len(), 0);
            
            let pat_bytes = pat.as_bytes();
            let (alphabet, bm_bc, k) = B5STimePattern::build(pat_bytes);
            
            B5STimePattern { pat_bytes, alphabet, bm_bc, k }
        }
        
        fn build(p: &'a [u8]) -> ([bool;256], [usize;256], usize)  {
            let mut alphabet = [false;256];
            let mut bm_bc = [p.len(); 256];
            let lastpos = p.len() - 1;
            
            for i in 0..lastpos {
                alphabet[p[i] as usize] = true;
                bm_bc[p[i] as usize] = lastpos - i;
            }
            
            alphabet[p[lastpos] as usize] = true;
            
            (alphabet, bm_bc, compute_k(p))
        }
        
        pub fn find_all(&self, string: &str) -> Vec<usize> {
            let mut result = vec![];
            let string_bytes = string.as_bytes();
            let pat_last_pos = self.pat_bytes.len() - 1;
            let patlen = self.pat_bytes.len();
            let stringlen = string_bytes.len();
            let mut string_index = pat_last_pos;
            let mut offset = pat_last_pos;
            let offset0 = self.k - 1;
            
            while string_index < stringlen {
                if string_bytes[string_index] == self.pat_bytes[pat_last_pos] {
                    if &string_bytes[string_index-offset..string_index] == &self.pat_bytes[pat_last_pos-offset..pat_last_pos] {
                        result.push(string_index-pat_last_pos);
                        
                        offset = offset0;
                        
                        // Galil rule
                        string_index += self.k;
                        continue;
                    }
                }
                
                if string_index + 1 == stringlen {
                    break;
                }
                
                offset = pat_last_pos;
                
                if !self.alphabet[string_bytes[string_index+1] as usize] {
                    string_index += patlen + 1;  // sunday
                } else {
                    string_index += self.bm_bc[string_bytes[string_index] as usize];  // horspool
                }
            }
            
            result
        }
    }
    ```

Performanse ove verzije B5S-a vrlo su dobre; među dosad opisanim algoritmima sufiksnog podudaranja u uobičajenim je slučajevima najbrža.

#### Verzija koja štedi prostor

Također implementirana u CPythonovu `stringlib`; dva cijela broja približno zamjenjuju tablicu znakova i $delta_1$, čime se iznimno štedi prostor:

1.  Jednostavan Bloomov filtar zamjenjuje tablicu znakova (alphabet)

    ???+ note "Implementacija"
        ```rust
        pub struct BytesBloomFilter {
            mask: u64,
        }
        
        impl BytesBloomFilter {
            pub fn new() -> Self {
                SimpleBloomFilter {
                    mask: 0,
                }
            }
            
            fn insert(&mut self, byte: &u8) {
                (self.mask) |= 1u64 << (byte & 63);
            }
            
            fn contains(&self, char: &u8) -> bool {
                (self.mask & (1u64 << (byte & 63))) != 0
            }
        }
        ```

    Bloomov filtar je struktura podataka tipa `Set` dizajnirana tako da žrtvovanjem točnosti (a zapravo i vremena izvođenja) iznimno štedi prostor; njegova je značajka da element koji nije u skupu može pogrešno proglasiti prisutnim (False Positives, skraćeno FP), ali element koji jest u skupu nikad neće proglasiti odsutnim (False Negatives, skraćeno FN). Stoga njegovom uporabom zbog FP-a možda nećemo dobiti najveći skok po znakovima, ali zbog FN-a nećemo preskočiti znakove koji bi se trebali podudariti.

    Teorijska analiza pokazuje da gornja implementacija „Bloomova filtra” za $pat$ duljine 50 bajtova ima vjerojatnost FP-a oko 0,5, a za $pat$ duljine 10 bajtova oko 0,15.

    Iako to nije standardni Bloomov filtar — prije svega ne koristi pravu hash funkciju, nego je zapravo samo preslikavanje znakova koje bajt 0–255 preslikava u broj sastavljen od njegovih donjih šest bitova —

    s obzirom na to da pretražujemo znakove u memoriji, to je pojednostavnjenje vrlo važno: čak i najbrži trenutno poznati nekriptografski hash algoritam [xxHash](https://cyan4973.github.io/xxHash/) treba za računanje red veličine više vremena.

    Osim toga, kad je pat kraći od 30 bajtova, za optimalnu vjerojatnost FP-a trebalo bi više od jedne hash funkcije. No to nema mnogo smisla, jer se već poljem s dva broja `u128` može izgraditi tablica znakova za cijelu abecedu.

2.  Umjesto cijelog $delta_1$ koristi se $delta_1(pat[patlastpos])$

    Promotrimo $delta_1$: najčešće se koristi kad se pri sufiksnom podudaranju već prvi znak ne podudara, što je najčešći slučaj nepodudaranja; stoga postavimo `skip = delta1(pat[patlastpos])`.

    Pri nepodudaranju u prvoj fazi izravno se pomičemo za `skip` znakova; no pri nepodudaranju u drugoj fazi, zbog nedostatka informacija cijelog $delta_1$, možemo se pomaknuti samo za jedan znak.

    ???+ note "Implementacija"
        ```rust
        pub struct B5SSpacePattern<'a> {
            pat_bytes: &'a [u8],
            alphabet: BytesBloomFilter,
            skip: usize,
        }
        
        impl<'a> B5SSpacePattern<'a> {
            pub fn new(pat: &'a str) -> Self {
                assert_ne!(pat.len(), 0);
                
                let pat_bytes = pat.as_bytes();
                let (alphabet, skip) = B5SSpacePattern::build(pat_bytes);
                
                B5SSpacePattern { pat_bytes, alphabet, skip}
            }
            
            fn build(p: &'a [u8]) -> (BytesBloomFilter, usize)  {
                let mut alphabet = BytesBloomFilter::new();
                let lastpos = p.len() - 1;
                let mut skip = p.len();
                
                for i in 0..p.len()-1 {
                    alphabet.insert(&p[i]);
                    
                    if p[i] == p[lastpos] {
                        skip = lastpos - i;
                    }
                }
                
                alphabet.insert(&p[lastpos]);
                
                (alphabet, skip)
            }
            
            pub fn find_all(&self, string: &'a str) -> Vec<usize> {
                let mut result = vec![];
                let string_bytes = string.as_bytes();
                let pat_last_pos = self.pat_bytes.len() - 1;
                let patlen = self.pat_bytes.len();
                let stringlen = string_bytes.len();
                let mut string_index = pat_last_pos;
                
                while string_index < stringlen {
                    if string_bytes[string_index] == self.pat_bytes[pat_last_pos] {
                        if &string_bytes[string_index-pat_last_pos..string_index] == &self.pat_bytes[..patlen-1] {
                            result.push(string_index-pat_last_pos);
                        }
                        
                        if string_index + 1 == stringlen {
                            break;
                        }
                        
                        if !self.alphabet.contains(&string_bytes[string_index+1]) {
                            string_index += patlen + 1;  // sunday
                        } else {
                            string_index += self.skip;  // horspool
                        }
                    } else {
                        if string_index + 1 == stringlen {
                            break;
                        }
                        
                        if !self.alphabet.contains(&string_bytes[string_index+1]) {
                            string_index += patlen + 1;  // sunday
                        } else {
                            string_index += 1;
                        }
                    }
                
                }
                
                result
            }
        }
        ```

    Ova verzija algoritma nije tako brza kao prethodni algoritmi sufiksnog podudaranja, ali razlika nije velika, a performanse su i dalje bolje od KMP-a, zahvaljujući izvrsnoj prostornoj složenosti od najviše dva cijela broja `u64`.

## Teorijska analiza

Slijede performanse pojedinih algoritama nad uobičajenom abecedom; ordinata je nalik trošku izvođenja (cost je trošak pri nepodudaranju nakon uspješnog podudaranja m znakova, a skip vjerojatnost pomaka za k znakova pri nepodudaranju) — što manje, to bolje. Apscisa je duljina uzorka pat:

![Usporedba performansi algoritama pretraživanja stringova](./images/BM/plot256.svg)

Performanse nad manjom abecedom (DNA, sekvence parova baza {A, C, T, G}):

![Usporedba performansi algoritama pretraživanja stringova nad malom abecedom](./images/BM/plot4.svg)

Ukratko, nad većim abecedama, npr. pri svakodnevnom pretraživanju, algoritmi iz obitelji Boyer–Moore imaju izvrsne performanse, pri čemu se skokovi po znakovima uglavnom oslanjaju na tablicu $delta_1$;

s druge strane, nad manjim abecedama uloga $delta_1$ slabi, a dolazi do izražaja uloga $delta_2$.

Ako ima nešto slobodnog prostora, potpuni Boyer–Mooreov algoritam prostorne složenosti $O(m)$ općenitiji je i ima najbolje ukupne performanse.

## Literatura i napomene

[^bm]: [Rad o Boyer–Mooreovu algoritmu iz 1977.](https://dl.acm.org/doi/10.1145/359842.359859)

[^kmp]: [Rad o KMP algoritmu iz 1977.](https://epubs.siam.org/doi/abs/10.1137/0206024)

[^rytter]: [Rytterov rad iz 1980. koji ispravlja Knutha](https://epubs.siam.org/doi/10.1137/0209037)

[^galil-rule]: [Rad iz 1979. koji predstavlja Galilov algoritam](https://doi.org/10.1145%2F359146.359148)

[^b5s]: [Opis algoritma B5S](http://effbot.org/zone/stringlib.htm#BMHBNFS)
