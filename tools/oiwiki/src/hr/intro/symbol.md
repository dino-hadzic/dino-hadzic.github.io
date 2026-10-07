---
title: Tablica matematičkih simbola
---

Ovaj dokument propisuje preporučeni način pisanja matematičkih simbola na **OI Wikiju** i daje nekoliko primjera primjene.

Pri sastavljanju su kao predložak poslužile tablice simbola iz [GB/T 3102.11-1993](https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=3DE79450D562E62D41CB6E79FF411054), [ISO 80000-2:2019](https://www.iso.org/standard/64973.html) i „Konkretne matematike”, pa je dokument u osnovi usklađen sa sustavom oznaka uobičajenih kineskih udžbenika i s oznakama uvriježenima u OI-ju.

LaTeX zapis simbola potražite u [izvornom kodu ovog članka](https://github.com/OI-wiki/OI-wiki/blob/master/docs/intro/symbol.md?plain=1)

## Matematička logika

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n1.1">n1.1</span> | $p \land q$ | konjunkcija $p$ i $q$ | $p$ i $q$. |
| <span id="n1.2">n1.2</span> | $p \lor q$ | disjunkcija $p$ i $q$ | $p$ ili $q$;<br>„ili” je ovdje uključivo, tj. ako je barem jedna od tvrdnji $p$, $q$ istinita, onda je $p \lor q$ istinito. |
| <span id="n1.3">n1.3</span> | $\lnot p$ | negacija $p$ | ne $p$. |
| <span id="n1.4">n1.4</span> | $p \implies q$ | $p$ povlači $q$;<br>ako je $p$ istinito, onda je $q$ istinito | $q \impliedby p$ i $p \implies q$ znače isto. |
| <span id="n1.5">n1.5</span> | $p \iff q$ | $p$ je ekvivalentno s $q$ | $(p \implies q) \land (q \implies p)$ i $p \iff q$ znače isto. |
| <span id="n1.6">n1.6</span> | $(\forall~x \in A)~~p(x)$ | za sve $x$ iz $A$ tvrdnja $p(x)$ je istinita | Ako je iz konteksta jasno o kojem je skupu $A$ riječ, može se pisati $(\forall~x)~~p(x)$.<br>$\forall$ zove se univerzalni kvantifikator.<br>Značenje $x \in A$ vidi u [n2.1](#n2.1). |
| <span id="n1.7">n1.7</span> | $(\exists~x \in A)~~p(x)$ | postoji $x$ iz $A$ takav da je $p(x)$ istinito | Ako je iz konteksta jasno o kojem je skupu $A$ riječ, može se pisati $(\exists~x)~~p(x)$.<br>$\exists$ zove se egzistencijalni kvantifikator.<br>Značenje $x \in A$ vidi u [n2.1](#n2.1).<br>$(\exists!~x)~~p(x)$ (kvantifikator jedinstvenosti) označava da postoji točno jedan $x$ takav da je $p(x)$ istinito.<br>$\exists!$ može se pisati i $\exists^1$. |

## Teorija skupova

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n2.1">n2.1</span> | $x \in A$ | $x$ pripada $A$, $x$ je element skupa $A$ | $A \ni x$ i $x \in A$ znače isto. |
| <span id="n2.2">n2.2</span> | $y \notin A$ | $y$ ne pripada $A$, $y$ nije element skupa $A$ | |
| <span id="n2.3">n2.3</span> | $\{x_1, x_2, \dots, x_n\}$ | skup s elementima $x_1, x_2, \dots, x_n$ | Može se pisati i $\{x_i ~\vert~ i \in I\}$, gdje je $I$ skup indeksa. |
| <span id="n2.4">n2.4</span> | $\{x \in A ~\vert~ p(x)\}$ | skup svih elemenata iz $A$ za koje je tvrdnja $p(x)$ istinita | Na primjer $\{x \in \textbf{R} ~\vert~ x \geq 5\}$;<br>ako je iz konteksta jasno o kojem je skupu $A$ riječ, može se pisati $\{x ~\vert~ p(x)\}$ (npr. kad se promatra samo skup realnih brojeva, može se pisati $\{x ~\vert~ x \geq 5\}$)<br>$\vert$ se može zamijeniti dvotočkom, npr. $\{x \in A : p(x)\}$. |
| <span id="n2.5">n2.5</span> | $\operatorname{card} A$;<br>$\vert A\vert$;<br>$\# A$ | broj elemenata skupa $A$, kardinalnost skupa $A$ | |
| <span id="n2.6">n2.6</span> | $\varnothing$ | prazan skup | Ne treba koristiti $\emptyset$. |
| <span id="n2.7">n2.7</span> | $B \subseteq A$ | $B$ je sadržan u $A$, $B$ je podskup od $A$ | Svaki element od $B$ pripada $A$.<br>I $\subset$ se može koristiti u tom značenju, ali vidi napomenu uz [n2.8](#n2.8).<br>$A \supseteq B$ i $B \subseteq A$ znače isto. |
| <span id="n2.8">n2.8</span> | $B \subset A$ | $B$ je strogo sadržan u $A$, $B$ je pravi podskup od $A$ | Svaki element od $B$ pripada $A$ i barem jedan element od $A$ ne pripada $B$.<br>Ako $\subset$ ima značenje iz [n2.7](#n2.7), onda za [n2.8](#n2.8) treba koristiti simbol $\subsetneq$.<br>$A \supset B$ i $B \subset A$ znače isto. |
| <span id="n2.9">n2.9</span> | $A \cup B$ | unija skupova $A$ i $B$ | $A \cup B := \{x ~\vert~ x \in A \lor x \in B\}$;<br>definiciju $:=$ vidi u [n4.3](#n4.3) |
| <span id="n2.10">n2.10</span> | $A \cap B$ | presjek skupova $A$ i $B$ | $A \cap B := \{x ~\vert~ x \in A \land x \in B\}$;<br>definiciju $:=$ vidi u [n4.3](#n4.3) |
| <span id="n2.11">n2.11</span> | $\displaystyle \bigcup\limits_{i=1}^n A_i$ | unija skupova $A_1, A_2, \dots, A_n$ | $\displaystyle \bigcup\limits_{i=1}^n A_i=A_1\cup A_2\cup \dots \cup A_n$;<br>može se koristiti i $\displaystyle \bigcup\nolimits_{i=1}^n$, $\displaystyle \bigcup\limits_{i\in I}$, $\displaystyle \bigcup\nolimits_{i\in I}$, gdje je $I$ skup indeksa;<br>nadalje, ako je $P(i)$ neka tvrdnja o $i$, s $\displaystyle \bigcup_{P(i)} A_i$ označava se unija svih $A_i$ za one $i$ za koje je $P(i)$ istinito |
| <span id="n2.12">n2.12</span> | $\displaystyle \bigcap\limits_{i=1}^n A_i$ | presjek skupova $A_1, A_2, \dots, A_n$ | $\displaystyle \bigcap\limits_{i=1}^n A_i=A_1\cap A_2\cap \dots \cap A_n$;<br>može se koristiti i $\displaystyle \bigcap\nolimits_{i=1}^n$, $\displaystyle \bigcap\limits_{i\in I}$, $\displaystyle \bigcap\nolimits_{i\in I}$, gdje je $I$ skup indeksa;<br>nadalje, ako je $P(i)$ neka tvrdnja o $i$, s $\displaystyle \bigcap_{P(i)} A_i$ označava se presjek svih $A_i$ za one $i$ za koje je $P(i)$ istinito |
| <span id="n2.13">n2.13</span> | $A \setminus B$ | razlika skupova $A$ i $B$ | $A \setminus B = \{x ~\vert~ x \in A \land x \notin B\}$;<br>ne treba koristiti $A - B$;<br>kad je $B$ podskup od $A$, može se koristiti i $\complement_A B$, a ako je iz konteksta jasno o kojem je skupu $A$ riječ, $A$ se može izostaviti.<br>Ako nema opasnosti od zabune, komplement skupa $B$ može se označiti i s $\overline{B}$. |
| <span id="n2.14">n2.14</span> | $(a, b)$ | uređeni par $a$, $b$;<br>uređena dvojka $a$, $b$ | $(a, b) = (c, d)$ ako i samo ako je $a = c$ i $b = d$. |
| <span id="n2.15">n2.15</span> | $(a_1, a_2, \dots, a_n)$ | uređena $n$-torka | Vidi [n2.14](#n2.14). |
| <span id="n2.16">n2.16</span> | $A \times B$ | Kartezijev produkt skupova $A$ i $B$ | $A \times B = \{(x, y) ~\vert~ x \in A \land y \in B\}$. |
| <span id="n2.17">n2.17</span> | $\displaystyle \prod\limits_{i=1}^{n} A_i$ | Kartezijev produkt skupova $A_1, A_2, \dots, A_n$ | $\displaystyle \prod\limits_{i=1}^{n} A_i=\{(x_1, x_2, \dots, x_n) ~\vert~ x_1 \in A_1, x_2 \in A_2, \dots, x_n \in A_n\}$;<br>$A \times A \times \dots \times A$ piše se $A^n$, gdje je $n$ broj faktora u produktu;<br>drugu upotrebu ovog simbola vidi u [n6.8](#n6.8) |
| <span id="n2.18">n2.18</span> | $\mathrm{id}_A$ | dijagonala skupa $A\times A$ | $\mathrm{id}_A=\{(x, x)~\vert~x\in A\}$;<br>ako je iz konteksta jasno o kojem je skupu $A$ riječ, $A$ se može izostaviti. |
| <span id="n2.19">n2.19</span> | $\mathbf{1}_A$ | indikatorska funkcija | $\mathbf{1}_A(a)=[a\in A]$, definiciju $[\cdot]$ vidi u [n6.24](#n6.24). |
| <span id="n2.20">n2.20</span> | $\mathcal{P}(A)$;<br>$2^A$ | partitivni skup | $\mathcal{P}(A)=\{S:S\subseteq A\}$ |

## Standardni skupovi brojeva i intervali

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n3.1">n3.1</span> | $\mathbf{N}$ | skup prirodnih brojeva | $\mathbf{N} = \{0, 1, 2, 3, \dots\}$;<br>$\mathbf{N}^* = \mathbf{N}_+ = \{1, 2, 3, \dots\}$;<br>dodatna ograničenja mogu se dodati ovako: $\mathbf{N}_{> 5} = \{n \in \mathbf{N} ~\vert~ n > 5\}$;<br>može se koristiti i $\mathbb{N}$. |
| <span id="n3.2">n3.2</span> | $\mathbf{Z}$ | skup cijelih brojeva | $\mathbf{Z}^* = \mathbf{Z}_+ = \{n \in \mathbf{Z} ~\vert~ n \ne 0\}$;<br>dodatna ograničenja mogu se dodati ovako: $\mathbf{Z}_{> -3} = \{n \in \mathbf{Z} ~\vert~ n > -3\}$;<br>može se koristiti i $\mathbb{Z}$. |
| <span id="n3.3">n3.3</span> | $\mathbf{Q}$ | skup racionalnih brojeva | $\mathbf{Q}^* = \mathbf{Q}_+ = \{r \in \mathbf{Q} ~\vert~ r \ne 0\}$;<br>dodatna ograničenja mogu se dodati ovako: $\mathbf{Q}_{< 0} = \{r \in \mathbf{Q} ~\vert~ r < 0\}$;<br>može se koristiti i $\mathbb{Q}$. |
| <span id="n3.4">n3.4</span> | $\mathbf{R}$ | skup realnih brojeva | $\mathbf{R}^* = \mathbf{R}_+ = \{x \in \mathbf{R} ~\vert~ x \ne 0\}$;<br>dodatna ograničenja mogu se dodati ovako: $\mathbf{R}_{> 0} = \{x \in \mathbf{R} ~\vert~ x > 0\}$;<br>može se koristiti i $\mathbb{R}$. |
| <span id="n3.5">n3.5</span> | $\mathbf{C}$ | skup kompleksnih brojeva | $\mathbf{C}^* = \mathbf{C}_+ = \{z \in \mathbf{C} ~\vert~ z \ne 0\}$;<br>može se koristiti i $\mathbb{C}$. |
| <span id="n3.6">n3.6</span> | $\mathbf{P}$ | skup (pozitivnih) prostih brojeva | $\mathbf{P} = \{2, 3, 5, 7, 11, 13, 17, \dots\}$;<br>može se koristiti i $\mathbb{P}$. |
| <span id="n3.7">n3.7</span> | $[a, b]$ | zatvoreni interval od $a$ do $b$ | $[a, b] = \{x \in \mathbf{R} ~\vert~ a \leq x \leq b\}$. |
| <span id="n3.8">n3.8</span> | $(a, b]$ | interval od $a$ do $b$ otvoren slijeva i zatvoren zdesna | $(a, b] = \{x \in \mathbf{R} ~\vert~ a < x \leq b\}$;<br>$(-\infty, b] = \{x \in \mathbf{R} ~\vert~ x \leq b\}$. |
| <span id="n3.9">n3.9</span> | $[a, b)$ | interval od $a$ do $b$ zatvoren slijeva i otvoren zdesna | $[a, b) = \{x \in \mathbf{R} ~\vert~ a \leq x < b\}$;<br>$[a, +\infty) = \{x \in \mathbf{R} ~\vert~ a \leq x\}$. |
| <span id="n3.10">n3.10</span> | $(a, b)$ | otvoreni interval od $a$ do $b$ | $(a, b) = \{x \in \mathbf{R} ~\vert~ a < x < b\}$;<br>$(-\infty, b) = \{x \in \mathbf{R} ~\vert~ x < b\}$;<br>$(a, +\infty) = \{x \in \mathbf{R} ~\vert~ a < x\}$. |

## Relacije

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n4.1">n4.1</span> | $a = b$ | $a$ je jednako $b$ | $\equiv$ se koristi da se naglasi da je neka jednakost identitet<br>drugo značenje ovog simbola vidi u [n4.18](#n4.18). |
| <span id="n4.2">n4.2</span> | $a \ne b$ | $a$ nije jednako $b$ | |
| <span id="n4.3">n4.3</span> | $a := b$ | $a$ se definira kao $b$ | Vidi [n2.9](#n2.9),[n2.10](#n2.10) |
| <span id="n4.4">n4.4</span> | $a \approx b$ | $a$ je približno jednako $b$ | Jednakost nije isključena. |
| <span id="n4.5">n4.5</span> | $a \simeq b$ | $a$ je asimptotski jednako $b$ | Na primjer:<br>kad $x\to a$, $\dfrac{1}{\sin(x-a)} \simeq \dfrac{1}{x-a}$;<br>značenje $x \to a$ vidi u [n4.15](#n4.15). |
| <span id="n4.6">n4.6</span> | $a \propto b$ | $a$ je proporcionalno s $b$ | Može se koristiti i $a \sim b$.<br>$\sim$ se koristi i za relacije ekvivalencije. |
| <span id="n4.7">n4.7</span> | $M \cong N$ | $M$ je sukladno s $N$ | Kad su $M$ i $N$ skupovi točaka (geometrijski likovi).<br>Ovaj se simbol koristi i za izomorfizam algebarskih struktura. |
| <span id="n4.8">n4.8</span> | $a < b$ | $a$ je manje od $b$ | |
| <span id="n4.9">n4.9</span> | $b > a$ | $b$ je veće od $a$ | |
| <span id="n4.10">n4.10</span> | $a \leq b$ | $a$ je manje ili jednako $b$ | |
| <span id="n4.11">n4.11</span> | $b \geq a$ | $b$ je veće ili jednako $a$ | |
| <span id="n4.12">n4.12</span> | $a \ll b$ | $a$ je mnogo manje od $b$ | |
| <span id="n4.13">n4.13</span> | $b \gg a$ | $b$ je mnogo veće od $a$ | |
| <span id="n4.14">n4.14</span> | $\infty$ | beskonačnost | Ovaj simbol **nije** broj.<br>Mogu se koristiti i $+\infty$, $-\infty$. |
| <span id="n4.15">n4.15</span> | $x \to a$ | $x$ teži prema $a$ | Obično se pojavljuje u izrazima s limesom.<br>$a$ može biti i $\infty$, $+\infty$, $-\infty$. |
| <span id="n4.16">n4.16</span> | $m \mid n$ | $m$ dijeli $n$ | Za cijele brojeve $m$, $n$:<br>$(\exists~k \in \mathbf{Z})~~m\cdot k = n$. |
| <span id="n4.17">n4.17</span> | $m \perp n$ | $m$ i $n$ su relativno prosti | Za cijele brojeve $m$, $n$:<br>$(\nexists~k \in \mathbf{Z}_{>1})~~(k \mid m) \land (k \mid n)$;<br>drugu upotrebu ovog simbola vidi u [n5.2](#n5.2) |
| <span id="n4.18">n4.18</span> | $n \equiv k \pmod m$ | $n$ je kongruentno $k$ modulo $m$ | Za cijele brojeve $n$, $k$, $m$:<br>$m \mid (n - k)$;<br>ne miješati sa značenjem iz [n4.1](#n4.1). |

## Elementarna geometrija

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n5.1">n5.1</span> | $\parallel$ | paralelno | |
| <span id="n5.2">n5.2</span> | $\perp$ | okomito | drugu upotrebu ovog simbola vidi u [n4.17](#n4.17) |
| <span id="n5.3">n5.3</span> | $\angle$ | (ravninski) kut | |
| <span id="n5.4">n5.4</span> | $\overline{\mathrm{AB}}$ | dužina $\mathrm{AB}$ | |
| <span id="n5.5">n5.5</span> | $\overrightarrow{\mathrm{AB}}$ | usmjerena dužina $\mathrm{AB}$ | |
| <span id="n5.6">n5.6</span> | $d(\mathrm{A}, \mathrm{B})$ | udaljenost između točaka $\mathrm{A}$ i $\mathrm{B}$ | tj. duljina dužine $\overline{\mathrm{AB}}$. |

## Operacije

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n6.1">n6.1</span> | $a + b$ | $a$ plus $b$ | |
| <span id="n6.2">n6.2</span> | $a - b$ | $a$ minus $b$ | |
| <span id="n6.3">n6.3</span> | $a \pm b$ | $a$ plus ili minus $b$ | |
| <span id="n6.4">n6.4</span> | $a \mp b$ | $a$ minus ili plus $b$ | $-(a \pm b) = -a \mp b$. |
| <span id="n6.5">n6.5</span> | $a \cdot b$;<br>$a \times b$;<br>$ab$ | $a$ puta $b$ | Ako se pojavljuje decimalna točka, treba koristiti samo $\times$;<br>neke primjere upotrebe vidi u [n2.16](#n2.16),[n2.17](#n2.17),[n14.11](#n14.11),[n14.12](#n14.12) |
| <span id="n6.6">n6.6</span> | $\dfrac{a}{b}$;<br>$a/b$;<br>$a:b$ | $a$ podijeljeno s $b$ | $\dfrac{a}{b}=a\cdot b^{-1}$;<br>$:$ se može koristiti za omjer brojčanih vrijednosti iste dimenzije.<br>Ne treba koristiti $÷$. |
| <span id="n6.7">n6.7</span> | $\displaystyle \sum\limits_{i=1}^n a_i$ | $a_1 + a_2 + \dots + a_n$ | Može se koristiti i $\displaystyle \sum\nolimits_{i=1}^n a_i$, $\displaystyle \sum\limits_i a_i$, $\displaystyle \sum\nolimits_i a_i$, $\displaystyle \sum a_i$;<br>ako je $P(i)$ neka tvrdnja o $i$, s $\displaystyle \sum_{P(i)} a_i$ označava se zbroj svih $a_i$ za one $i$ za koje je $P(i)$ istinito. |
| <span id="n6.8">n6.8</span> | $\displaystyle \prod\limits_{i=1}^n a_i$ | $a_1 \cdot a_2 \cdot \dots \cdot a_n$ | Može se koristiti i $\displaystyle \prod\nolimits_{i=1}^n a_i$, $\displaystyle \prod\limits_i a_i$, $\displaystyle \prod\nolimits_i a_i$, $\displaystyle \prod a_i$;<br>ako je $P(i)$ neka tvrdnja o $i$, s $\displaystyle \prod_{P(i)} a_i$ označava se umnožak svih $a_i$ za one $i$ za koje je $P(i)$ istinito;<br>drugu upotrebu ovog simbola vidi u [n2.17](#n2.17) |
| <span id="n6.9">n6.9</span> | $a^p$ | $p$-ta potencija od $a$ | |
| <span id="n6.10">n6.10</span> | $a^{1/2}$;<br>$\sqrt{a}$ | $a$ na $1/2$, drugi korijen iz $a$ | Treba izbjegavati $\sqrt{}a$. |
| <span id="n6.11">n6.11</span> | $a^{1/n}$;<br>$\sqrt[n]{a}$ | $a$ na $1/n$, $n$-ti korijen iz $a$ | Treba izbjegavati $\sqrt[n]{}a$. |
| <span id="n6.12">n6.12</span> | $\bar{x}$;<br>$\bar{x}_a$ | aritmetička sredina od $x$ | Ostale sredine:<br>harmonijska sredina $\bar{x}_h$;<br>geometrijska sredina $\bar{x}_g$;<br>kvadratna sredina / korijen srednjeg kvadrata $\bar{x}_q$ ili $\bar{x}_{rms}$.<br>$\bar{x}$ označava i konjugirano kompleksni broj od $x$, vidi [n11.6](#n11.6). |
| <span id="n6.13">n6.13</span> | $\operatorname{sgn} a$ | funkcija predznaka od $a$ | Za realan broj $a$:<br>$\operatorname{sgn} a=1\quad (a>0)$;<br>$\operatorname{sgn} a=-1\quad (a<0)$;<br>$\operatorname{sgn} 0=0$;<br>vidi [n11.7](#n11.7). |
| <span id="n6.14">n6.14</span> | $\inf M$ | infimum skupa $M$ | Najveća donja međa nepraznog skupa $M$. |
| <span id="n6.15">n6.15</span> | $\sup M$ | supremum skupa $M$ | Najmanja gornja međa nepraznog skupa $M$. |
| <span id="n6.16">n6.16</span> | $\lvert a\rvert$ | apsolutna vrijednost od $a$ | Može se koristiti i $\operatorname{abs} a$. |
| <span id="n6.17">n6.17</span> | $\lfloor a\rfloor$ | zaokruživanje nadolje (pod)<br>najveći cijeli broj manji ili jednak realnom broju $a$ | Na primjer:<br>$\lfloor 2.4\rfloor = 2$;<br>$\lfloor -2.4\rfloor = -3$. |
| <span id="n6.18">n6.18</span> | $\lceil a\rceil$ | zaokruživanje nagore (strop)<br>najmanji cijeli broj veći ili jednak realnom broju $a$ | Na primjer:<br>$\lceil 2.4\rceil = 3$;<br>$\lceil -2.4\rceil = -2$. |
| <span id="n6.19">n6.19</span> | $\min(a, b)$;<br>$\min\{a, b\}$ | minimum od $a$ i $b$ | Može se poopćiti na konačne skupove.<br>Za minimum beskonačnog skupa preporučuje se $\inf$, vidi [n6.14](#n6.14) |
| <span id="n6.20">n6.20</span> | $\max(a, b)$;<br>$\max\{a, b\}$ | maksimum od $a$ i $b$ | Može se poopćiti na konačne skupove.<br>Za maksimum beskonačnog skupa preporučuje se $\sup$, vidi [n6.15](#n6.15) |
| <span id="n6.21">n6.21</span> | $n \bmod m$ | ostatak pri dijeljenju $n$ s $m$ | Za pozitivne cijele brojeve $n$, $m$:<br>$(\exists~q\in\mathbf{N}, r\in[0, m))~~n=qm+r$;<br>pri čemu je $r=n \bmod m$. |
| <span id="n6.22">n6.22</span> | $\gcd(a, b)$;<br>$\gcd\{a, b\}$ | najveći zajednički djelitelj cijelih brojeva $a$ i $b$ | Može se poopćiti na konačne skupove. Ako nema opasnosti od zabune, može se pisati $(a, b)$. |
| <span id="n6.23">n6.23</span> | $\operatorname{lcm}(a, b)$;<br>$\operatorname{lcm}\{a, b\}$ | najmanji zajednički višekratnik cijelih brojeva $a$ i $b$ | Može se poopćiti na konačne skupove. Ako nema opasnosti od zabune, može se pisati $[a, b]$;<br>$(a, b)[a, b]=\lvert ab\rvert$. |
| <span id="n6.24">n6.24</span> | $[P]$ | Iversonova zagrada | Ako je tvrdnja $P$ istinita, onda je $[P]=1$, inače je $[P]=0$. |
| <span id="n6.25">n6.25</span> | $a\uparrow b$;<br>$a\uparrow^{n} b$ | Knuthova strelica | Za nenegativne cijele brojeve $a,b,n$:<br>$a\uparrow^{n} b=a~\underbrace{\uparrow\dots\uparrow}_{n \text{ times}}~b$;<br>$a\uparrow^{0} b=ab$;<br>$a\uparrow^{1} b=a\uparrow b=a^b$;<br>$a\uparrow^{n} 0=1\quad(n>0)$;<br>$a\uparrow^{n}b=a\uparrow^{n-1}(a\uparrow^{n}(b-1))$. |
| <span id="n6.26">n6.26</span> | $[x^n]f(x)$ | koeficijent uz $x^n$ u polinomu / formalnom redu potencija / formalnom Laurentovom redu $f(x)$ | Ako je $\displaystyle f(x)=\sum_{i} a_ix^i$, onda je $[x^n]f(x)=a_n$;<br>može se poopćiti na više varijabli, npr. ako je $\displaystyle f(x,y)=\sum_{i,j}a_{i,j}x^iy^j$, onda je $[x^ny^m]f(x,y)=a_{n,m}$. |

## Kombinatorika

U ovom odjeljku $n$ i $k$ su prirodni brojevi, $a$ je kompleksan broj i $k\leq n$.

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n7.1">n7.1</span> | $n!$ | faktorijel | $n!=\prod_{k=1}^n k=1\cdot 2\cdot 3\cdot \dots \cdot n\quad (n>0)$;<br>$0!=1$. |
| <span id="n7.2">n7.2</span> | $a^{\underline{k}}$;<br>$(a)_{-k}$ | padajuća faktorijelna potencija | $a^{\underline{k}}=a\cdot(a-1)\cdot \dots \cdot(a-k+1)\quad (k>0)$;<br>$a^{\underline{0}}=1$;<br>$n^{\underline{k}}=\dfrac{n!}{(n-k)!}$. |
| <span id="n7.3">n7.3</span> | $a^{\overline{k}}$;<br>$(a)_{+k}$ | rastuća faktorijelna potencija | $a^{\overline{k}}=a\cdot(a+1)\cdot \dots \cdot(a+k-1)\quad (k>0)$;<br>$a^{\overline{0}}=1$;<br>$n^{\overline{k}}=\dfrac{(n+k-1)!}{(n-1)!}$. |
| <span id="n7.4">n7.4</span> | $\dbinom{n}{k}$ | binomni koeficijent | $\dbinom{n}{k}=\dfrac{n!}{k!(n-k)!}$. |
| <span id="n7.5">n7.5</span> | $\displaystyle{n\brack k}$ | Stirlingov broj prve vrste | $\displaystyle{n+1\brack k}=n{n\brack k}+{n\brack k-1}$;<br>$\displaystyle x^{\overline{n}}=\sum_{k=0}^n{n\brack k}x^k$. |
| <span id="n7.6">n7.6</span> | $\displaystyle{n\brace k}$ | Stirlingov broj druge vrste | $\displaystyle{n\brace k}=\frac{1}{k!}\sum_{i=0}^k(-1)^i\binom{k}{i}(k-i)^n$;<br>$\displaystyle\sum_{k=0}^n{n\brace k}x^{\underline{k}}=x^n$. |

## Funkcije

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n8.1">n8.1</span> | $f$ | funkcija | |
| <span id="n8.2">n8.2</span> | $f(x)$, $f(x_1, \dots, x_n)$ | vrijednost funkcije $f$ u $x$<br>vrijednost funkcije $f$ u $(x_1, \dots, x_n)$ | |
| <span id="n8.3">n8.3</span> | $\operatorname{dom} f$ | domena od $f$ | Može se koristiti i $\mathrm{D}(f)$. |
| <span id="n8.4">n8.4</span> | $\operatorname{ran} f$ | slika (skup vrijednosti) od $f$ | Može se koristiti i $\mathrm{R}(f)$. |
| <span id="n8.5">n8.5</span> | $f:A\to B$ | $f$ je preslikavanje iz $A$ u $B$ | $\operatorname{dom} f=A$ i $(\forall~x \in\operatorname{dom} f)~~ f(x) \in B$. |
| <span id="n8.6">n8.6</span> | $x\mapsto T(x), x\in A$ | funkcija koja svaki $x\in A$ preslikava u $T(x)$ | $T(x)$ služi samo za definiciju i označava vrijednost neke funkcije s argumentom $x\in A$. Ako je ta funkcija $f$, onda za sve $x\in A$ vrijedi $f(x)=T(x)$. Stoga se $T(x)$ obično koristi za definiranje funkcije $f$.<br>Na primjer:<br>$x\mapsto 3x^2y, x\in[0, 2]$;<br>to je kvadratna funkcija od $x$ definirana izrazom $3x^2y$. Ako nije uveden simbol funkcije, funkcija se označava s $3x^2y$ |
| <span id="n8.7">n8.7</span> | $f^{-1}$ | inverzna funkcija od $f$ | Inverzna funkcija $f^{-1}$ funkcije $f$ definirana je ako i samo ako je $f$ injekcija.<br>Ako je $f$ injekcija, onda je $\operatorname{dom}\left(f^{-1}\right) = \operatorname{ran} f$, $\operatorname{ran}\left(f^{-1}\right) = \operatorname{dom} f$ i $(\forall~x\in\operatorname{dom} f)~~f^{-1}(f(x)) = x$.<br>Ne miješati s recipročnom vrijednošću funkcije $f(x)^{-1}$. |
| <span id="n8.8">n8.8</span> | $g\circ f$ | kompozicija funkcija $f$ i $g$ | $(g\circ f)(x)=g(f(x))$. |
| <span id="n8.9">n8.9</span> | $f:x\mapsto y$ | $f(x)=y$, $f$ preslikava $x$ u $y$ | |
| <span id="n8.10">n8.10</span> | $f\vert_a^b$;<br>$f(\dots, u, \dots)\vert_{u=a}^{u=b}$ | $f(b)-f(a)$;<br>$f(\dots, b, \dots)-f(\dots, a, \dots)$ | Koristi se uglavnom pri računanju određenih integrala. |
| <span id="n8.11">n8.11</span> | $\displaystyle \lim\limits_{x\to a}f(x)$;<br>$\lim\nolimits_{x\to a}f(x)$ | limes od $f(x)$ kad $x$ teži prema $a$ | $\lim\nolimits_{x\to a}f(x)=b$ može se pisati $f(x)\to b\quad (x \to a)$.<br>Oznake za desni i lijevi limes su redom $\lim\nolimits_{x\to a+}f(x)$ i<br>$\lim\nolimits_{x\to a-}f(x)$. |
| <span id="n8.12">n8.12</span> | $f(x) = O(g(x))$ | $\lvert f(x)/g(x)\rvert$ je ograničeno u granicama koje podrazumijeva kontekst, red od $f(x)$ nije viši od reda od $g(x)$ | Kad su i $f/g$ i $g/f$ ograničeni, kaže se da su $f$ i $g$ istog reda.<br>Simbol „$=$” koristi se iz povijesnih razloga; ovdje ne označava ekvivalenciju jer nije tranzitivan.<br>Na primjer:<br>$\sin x=O(x)\quad (x\to 0)$. |
| <span id="n8.13">n8.13</span> | $f(x) = o(g(x))$ | u granicama koje podrazumijeva kontekst vrijedi $f(x)/g(x)\to 0$, red od $f(x)$ viši je od reda od $g(x)$ | Simbol „$=$” koristi se iz povijesnih razloga; ovdje ne označava ekvivalenciju jer nije tranzitivan.<br>Na primjer:<br>$\cos x=1+o(x)\quad (x\to 0)$. |
| <span id="n8.14">n8.14</span> | $\Delta f$ | konačni prirast od $f$ | Razlika dviju vrijednosti funkcije koje podrazumijeva kontekst. Na primjer:<br>$\Delta x=x_2-x_1$;<br>$\Delta f(x)=f(x_2)-f(x_1)$. |
| <span id="n8.15">n8.15</span> | $\dfrac{\mathrm{d}f}{\mathrm{d}x}$;<br>$f'$ | derivacija od $f$ po $x$ | Samo za funkcije jedne varijable.<br>Nezavisna varijabla može se izričito navesti, npr. $\dfrac{\mathrm{d}f(x)}{\mathrm{d}x}$, $f'(x)$. |
| <span id="n8.16">n8.16</span> | $\left(\dfrac{\mathrm{d}f}{\mathrm{d}x}\right)_{x=a}$;<br>$f'(a)$ | vrijednost derivacije od $f$ u $a$ | Vidi [n8.15](#n8.15) |
| <span id="n8.17">n8.17</span> | $\dfrac{\mathrm{d}^n f}{\mathrm{d}x^n}$;<br>$f^{(n)}$ | $n$-ta derivacija od $f$ po $x$ | Samo za funkcije jedne varijable.<br>Nezavisna varijabla može se izričito navesti, npr. $\dfrac{\mathrm{d}^n f(x)}{\mathrm{d}x^n}$, $f^{(n)}(x)$.<br>$f''$ i $f'''$ mogu se koristiti za $f^{(2)}$ odnosno $f^{(3)}$. |
| <span id="n8.18">n8.18</span> | $\dfrac{\partial f}{\partial x}$;<br>$f_x$ | parcijalna derivacija od $f$ po $x$ | Samo za funkcije više varijabli.<br>Nezavisna varijabla može se izričito navesti, npr. $\dfrac{\partial f(x, y, \dots)}{\partial x}$, $f_x(x, y, \dots)$.<br>Može se proširiti na više redove, npr. $f_{xx}=\dfrac{\partial^2 f}{\partial x^2}=\dfrac{\partial}{\partial x}\left(\dfrac{\partial f}{\partial x}\right)$;<br>$f_{xy}=\dfrac{\partial^2 f}{\partial y\partial x}=\dfrac{\partial}{\partial y}\left(\dfrac{\partial f}{\partial x}\right)$. |
| <span id="n8.19">n8.19</span> | $\dfrac{\partial(f_1, \dots, f_m)}{\partial(x_1, \dots, x_n)}$ | Jacobijeva matrica | *vidi*[^n8.19-ref1] |
| <span id="n8.20">n8.20</span> | $\mathrm{d}f$ | totalni diferencijal od $f$ | $\mathrm{d}f(x, y, \dots)=\dfrac{\partial f}{\partial x}\mathrm{d}x+\dfrac{\partial f}{\partial y}\mathrm{d}y+\dots$. |
| <span id="n8.21">n8.21</span> | $\delta f$ | (infinitezimalna) varijacija od $f$ | |
| <span id="n8.22">n8.22</span> | $\displaystyle \int f(x)\mathrm{d}x$ | neodređeni integral od $f$ | |
| <span id="n8.23">n8.23</span> | $\displaystyle \int\limits_a^b f(x)\mathrm{d}x$ | određeni integral od $f$ od $a$ do $b$ | Može se koristiti i $\displaystyle \int\nolimits_a^b f(x)\mathrm{d}x$;<br>određeni integral može se definirati i na općenitijim područjima. Npr. $\displaystyle\int\limits_C$, $\displaystyle\int\limits_S$, $\displaystyle\int\limits_V$, $\displaystyle\oint$ označavaju redom određeni integral po krivulji $C$, plohi $S$, trodimenzionalnom području $V$ te po zatvorenoj krivulji ili plohi.<br>Višestruki integrali mogu se pisati $\displaystyle\iint$, $\displaystyle\iiint$ itd. |
| <span id="n8.24">n8.24</span> | $f*g$ | konvolucija funkcija $f$ i $g$ | $\displaystyle (f*g)(x)=\int\limits_{-\infty}^{\infty}f(y)g(x-y)\mathrm{d}y$. |

[^n8.19-ref1]: $\dfrac{\partial(f_1, \dots, f_m)}{\partial(x_1, \dots, x_n)}=\begin{pmatrix}\dfrac{\partial f_1}{\partial x_1}&\cdots&\dfrac{\partial f_1}{\partial x_n}\\\vdots&\ddots&\vdots\\\dfrac{\partial f_m}{\partial x_1}&\cdots&\dfrac{\partial f_m}{\partial x_n}\end{pmatrix}$; definiciju matrice vidi u [n12.1](#n12.1)

## Eksponencijalne i logaritamske funkcije

$x$ može biti kompleksan broj.

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n9.1">n9.1</span> | $\mathrm{e}$ | baza prirodnog logaritma | $\displaystyle \mathrm{e}=\lim\limits_{n\to\infty}\left(1+\frac{1}{n}\right)^n=2.718~281~8\dots$;<br>ne pisati $e$. |
| <span id="n9.2">n9.2</span> | $a^x$ | eksponencijalna funkcija od $x$ (s bazom $a$) | Vidi [n6.9](#n6.9). |
| <span id="n9.3">n9.3</span> | $\mathrm{e}^x$;<br>$\exp x$ | eksponencijalna funkcija od $x$ (s bazom $\mathrm{e}$) | |
| <span id="n9.4">n9.4</span> | $\log_a x$ | logaritam od $x$ po bazi $a$ | Kad bazu nije potrebno navesti, može se koristiti $\log x$.<br>$\log x$ ne treba koristiti umjesto bilo kojeg od $\ln x$, $\lg x$, $\operatorname{lb} x$. |
| <span id="n9.5">n9.5</span> | $\ln x$ | prirodni logaritam od $x$ | $\ln x = \log_{\mathrm{e}} x$;<br>vidi [n9.4](#n9.4). |
| <span id="n9.6">n9.6</span> | $\lg x$ | dekadski logaritam od $x$ | $\lg x = \log_{10} x$;<br>vidi [n9.4](#n9.4). |
| <span id="n9.7">n9.7</span> | $\operatorname{lb} x$ | logaritam od $x$ po bazi $2$ | $\operatorname{lb} x = \log_2 x$;<br>vidi [n9.4](#n9.4). |

## Trigonometrijske i hiperboličke funkcije

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n10.1">n10.1</span> | $\pi$ | broj pi (omjer opsega i promjera kruga) | $\pi = 3.141~592~6\dots$. |
| <span id="n10.2">n10.2</span> | $\sin x$ | sinus od $x$ | $\sin x=\dfrac{\mathrm{e}^{\mathrm{i}x}-\mathrm{e}^{-\mathrm{i}x}}{2\mathrm{i}}$;<br>$(\sin x)^n$, $(\cos x)^n$($n\geq 2$) itd. obično se pišu $\sin^n x$, $\cos^n x$ itd. |
| <span id="n10.3">n10.3</span> | $\cos x$ | kosinus od $x$ | $\cos x = \sin(x + \pi/2)$. |
| <span id="n10.4">n10.4</span> | $\tan x$ | tangens od $x$ | $\tan x = \sin x/\cos x$;<br>ne smije se koristiti $\operatorname{tg} x$. |
| <span id="n10.5">n10.5</span> | $\cot x$ | kotangens od $x$ | $\cot x = 1/\tan x$;<br>ne smije se koristiti $\operatorname{ctg} x$. |
| <span id="n10.6">n10.6</span> | $\sec x$ | sekans od $x$ | $\sec x = 1/\cos x$. |
| <span id="n10.7">n10.7</span> | $\csc x$ | kosekans od $x$ | $\csc x = 1/\sin x$;<br>ne smije se koristiti $\operatorname{cosec} x$. |
| <span id="n10.8">n10.8</span> | $\arcsin x$ | arkus sinus od $x$ | $y = \arcsin x \iff x = \sin y\quad (-\pi/2 \leq y \leq \pi/2)$. |
| <span id="n10.9">n10.9</span> | $\arccos x$ | arkus kosinus od $x$ | $y = \arccos x \iff x = \cos y\quad (0 \leq y \leq \pi)$. |
| <span id="n10.10">n10.10</span> | $\arctan x$ | arkus tangens od $x$ | $y = \arctan x \iff x = \tan y\quad (-\pi/2 \leq y \leq \pi/2)$;<br>ne smije se koristiti $\operatorname{arctg} x$. |
| <span id="n10.11">n10.11</span> | $\operatorname{arccot} x$ | arkus kotangens od $x$ | $y = \operatorname{arccot} x \iff x = \cot y\quad (0 \leq y \leq \pi)$;<br>ne smije se koristiti $\operatorname{arcctg} x$. |
| <span id="n10.12">n10.12</span> | $\operatorname{arcsec} x$ | arkus sekans od $x$ | $y = \operatorname{arcsec} x \iff x = \sec y\quad (0\leq y \leq \pi, y\ne \pi/2)$. |
| <span id="n10.13">n10.13</span> | $\operatorname{arccsc} x$ | arkus kosekans od $x$ | $y = \operatorname{arccsc} x \iff x = \csc y\quad (-\pi/2 \leq y \leq \pi/2, y\ne 0)$;<br>ne smije se koristiti $\operatorname{arccosec} x$. |
| <span id="n10.14">n10.14</span> | $\sinh x$ | hiperbolni sinus od $x$ | $\sinh x=\dfrac{\mathrm{e}^x-\mathrm{e}^{-x}}{2}$;<br>ne smije se koristiti $\operatorname{sh} x$. |
| <span id="n10.15">n10.15</span> | $\cosh x$ | hiperbolni kosinus od $x$ | $\cosh^2 x = \sinh^2 x + 1$;<br>ne smije se koristiti $\operatorname{ch} x$. |
| <span id="n10.16">n10.16</span> | $\tanh x$ | hiperbolni tangens od $x$ | $\tanh x = \sinh x/\cosh x$;<br>ne smije se koristiti $\operatorname{th} x$. |
| <span id="n10.17">n10.17</span> | $\coth x$ | hiperbolni kotangens od $x$ | $\coth x = 1/\tanh x$. |
| <span id="n10.18">n10.18</span> | $\operatorname{sech} x$ | hiperbolni sekans od $x$ | $\operatorname{sech} x = 1/\cosh x$. |
| <span id="n10.19">n10.19</span> | $\operatorname{csch} x$ | hiperbolni kosekans od $x$ | $\operatorname{csch} x = 1/\sinh x$;<br>ne smije se koristiti $\operatorname{cosech} x$. |
| <span id="n10.20">n10.20</span> | $\operatorname{arsinh} x$ | inverzni hiperbolni sinus od $x$ | $y = \operatorname{arsinh} x \iff x = \sinh y$;<br>ne smije se koristiti $\operatorname{arsh} x$. |
| <span id="n10.21">n10.21</span> | $\operatorname{arcosh} x$ | inverzni hiperbolni kosinus od $x$ | $y = \operatorname{arcosh} x \iff x = \cosh y\quad (y \geq 0)$;<br>ne smije se koristiti $\operatorname{arch} x$. |
| <span id="n10.22">n10.22</span> | $\operatorname{artanh} x$ | inverzni hiperbolni tangens od $x$ | $y = \operatorname{artanh} x \iff x = \tanh y$;<br>ne smije se koristiti $\operatorname{arth} x$. |
| <span id="n10.23">n10.23</span> | $\operatorname{arcoth} x$ | inverzni hiperbolni kotangens od $x$ | $y = \operatorname{arcoth} x \iff x = \coth y\quad (y \ne 0)$. |
| <span id="n10.24">n10.24</span> | $\operatorname{arsech} x$ | inverzni hiperbolni sekans od $x$ | $y = \operatorname{arsech} x \iff x = \operatorname{sech} y\quad (y \geq 0)$. |
| <span id="n10.25">n10.25</span> | $\operatorname{arcsch} x$ | inverzni hiperbolni kosekans od $x$ | $y = \operatorname{arcsch} x \iff x = \operatorname{csch} y\quad (y \geq 0)$;<br>ne smije se koristiti $\operatorname{arcosech} x$. |

## Kompleksni brojevi

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n11.1">n11.1</span> | $\mathrm{i}$ | imaginarna jedinica | $\mathrm{i}^2 = -1$;<br>ne smije se koristiti $i$ ni `i` |
| <span id="n11.2">n11.2</span> | $\operatorname{Re} z$ | realni dio od $z$ | Vidi [n11.3](#n11.3). |
| <span id="n11.3">n11.3</span> | $\operatorname{Im} z$ | imaginarni dio od $z$ | Ako je $z = x + \mathrm{i} y\quad (x, y\in\mathbf{R})$, onda je $x = \operatorname{Re} z$, $y = \operatorname{Im} z$. |
| <span id="n11.4">n11.4</span> | $\lvert z\rvert$ | modul od $z$ | $\lvert z\rvert=\sqrt{(\operatorname{Re} z)^2+(\operatorname{Im} z)^2}$. |
| <span id="n11.5">n11.5</span> | $\arg z$ | argument od $z$ | Ako je $z = r \mathrm{e}^{\mathrm{i}\varphi}$, gdje je $r = \lvert z\rvert$ i $-\pi < \varphi \leq \pi$, onda je $\varphi = \arg z$.<br>$\operatorname{Re} z = r \cos \varphi$, $\operatorname{Im} z = r \sin \varphi$. |
| <span id="n11.6">n11.6</span> | $\bar{z}$;<br>$z^*$ | kompleksno konjugirani broj od $z$ | $\bar{z}=\operatorname{Re}z-\mathrm{i}\operatorname{Im}z$. |
| <span id="n11.7">n11.7</span> | $\operatorname{sgn} z$ | funkcija jediničnog modula od $z$ | $\operatorname{sgn} z =z / \lvert z\rvert = \exp(\mathrm{i} \arg z)\quad (z \ne 0)$;<br>$\operatorname{sgn} 0 = 0$;<br>vidi [n6.13](#n6.13). |

## Matrice

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n12.1">n12.1</span> | $A$;<br>*vidi*[^n12.1-ref1] | matrica $A$ tipa $m\times n$ | $a_{ij} = (A)_{ij}$;<br>može se koristiti i $A = (a_{ij})$. Pritom je $m$ broj redaka, a $n$ broj stupaca<br>kad je $m=n$, matrica se zove kvadratna<br>umjesto okruglih zagrada mogu se koristiti uglate. |
| <span id="n12.2">n12.2</span> | $A + B$ | zbroj matrica $A$ i $B$ | $(A + B)_{ij} = (A)_{ij} + (B)_{ij}$;<br>matrice $A$ i $B$ moraju imati jednak broj redaka i jednak broj stupaca. |
| <span id="n12.3">n12.3</span> | $x A$ | umnožak skalara $x$ i matrice $A$ | $(x A)_{ij} = x (A)_{ij}$. |
| <span id="n12.4">n12.4</span> | $AB$ | umnožak matrica $A$ i $B$ | $\displaystyle(AB)_{ik} = \sum\limits_{j}(A)_{ij}(B)_{jk}$;<br>broj stupaca matrice $A$ mora biti jednak broju redaka matrice $B$. |
| <span id="n12.5">n12.5</span> | $I$;<br>$E$ | jedinična matrica | $(I)_{ik} = \delta_{ik}$;<br>definiciju $\delta_{ik}$ vidi u [n14.9](#n14.9). |
| <span id="n12.6">n12.6</span> | $A^{-1}$ | inverz kvadratne matrice $A$ | $AA^{-1} = A^{-1}A = I\quad (\det A \ne 0)$.<br>Definiciju $\det A$ vidi u [n12.10](#n12.10). |
| <span id="n12.7">n12.7</span> | $A^{\mathrm{T}}$;<br>$A'$ | transponirana matrica od $A$ | $(A^{\mathrm{T}})_{ik} = (A)_{ki}$. |
| <span id="n12.8">n12.8</span> | $\overline{A}$;<br>$A^*$ | kompleksno konjugirana matrica od $A$ | $\left(\overline{A}\right)_{ik}=\overline{(A)_{ik}}$. |
| <span id="n12.9">n12.9</span> | $A^{\mathrm{H}}$;<br>$A^{\dagger}$ | hermitski konjugirana matrica od $A$ | $A^{\mathrm{H}} = \left(\overline{A}\right)^{\mathrm{T}}$. |
| <span id="n12.10">n12.10</span> | $\det A$;<br>*vidi*[^n12.10-ref1] | determinanta kvadratne matrice $A$ | Može se koristiti i $\lvert A\rvert$. |
| <span id="n12.11">n12.11</span> | $\operatorname{rank}A$ | rang matrice $A$ | |
| <span id="n12.12">n12.12</span> | $\operatorname{tr}A$ | trag kvadratne matrice $A$ | $\displaystyle\operatorname{tr}A=\sum\limits_{i}(A)_{ii}$. |
| <span id="n12.13">n12.13</span> | $\lVert A\rVert$ | norma matrice $A$ | Zadovoljava nejednakost trokuta: ako je $A + B = C$, onda je $\lVert A\rVert+\lVert B\rVert \geq \lVert C\rVert$. |

[^n12.1-ref1]: $\begin{pmatrix}a_{11}&\cdots&a_{1n}\\\vdots&\ddots&\vdots\\a_{m1}&\cdots&a_{mn}\end{pmatrix}$

[^n12.10-ref1]: $\begin{vmatrix}a_{11}&\cdots&a_{1n}\\\vdots& &\vdots\\a_{n1}&\cdots&a_{nn}\end{vmatrix}$

## Koordinatni sustavi

U ovom odjeljku razmatraju se neki koordinatni sustavi u trodimenzionalnom prostoru. Točka $\mathrm{O}$ je **ishodište** koordinatnog sustava. Svaka točka $\mathrm{P}$ određena je **vektorom položaja** od ishodišta $\mathrm{O}$ do točke $\mathrm{P}$.

| Br. | Koordinate | Vektor položaja i njegov diferencijal | Naziv koordinata | Napomene |
| --- | --- | --- | --- | --- |
| <span id="n13.1">n13.1</span> | $x$, $y$, $z$ | $\boldsymbol{r} = x \boldsymbol{e}_x + y \boldsymbol{e}_y + z \boldsymbol{e}_z$;<br>$\mathrm{d}\boldsymbol{r} = \mathrm{d}x~\boldsymbol{e}_x + \mathrm{d}y~\boldsymbol{e}_y + \mathrm{d}z~\boldsymbol{e}_z$ | Kartezijeve koordinate | Bazni vektori $\boldsymbol{e}_x$, $\boldsymbol{e}_y$, $\boldsymbol{e}_z$ čine desni ortogonalni sustav, vidi [sliku 1](#slika-1) i [sliku 4](#slika-4).<br>Bazni vektori mogu se označiti i s $\boldsymbol{e}_1$, $\boldsymbol{e}_2$, $\boldsymbol{e}_3$ ili $\boldsymbol{i}$, $\boldsymbol{j}$, $\boldsymbol{k}$, a koordinate s $x_1$, $x_2$, $x_3$ ili $i$, $j$, $k$. |
| <span id="n13.2">n13.2</span> | $\rho$, $\varphi$, $z$ | $\boldsymbol{r} = \rho~\boldsymbol{e}_{\rho} + z~\boldsymbol{e}_z$;<br>$\mathrm{d}\boldsymbol{r} = \mathrm{d}\rho~\boldsymbol{e}_{\rho} +\rho~\mathrm{d}\varphi~\boldsymbol{e}_{\varphi} + \mathrm{d}z~\boldsymbol{e}_z$ | cilindrične koordinate | $\boldsymbol{e}_{\rho}(\varphi)$, $\boldsymbol{e}_{\varphi}(\varphi)$, $\boldsymbol{e}_z$ čine desni ortogonalni sustav, vidi [sliku 2](#slika-2).<br>Ako je $z = 0$, onda su $\rho$ i $\varphi$ polarne koordinate u ravnini. |
| <span id="n13.3">n13.3</span> | $r$, $\vartheta$, $\varphi$ | $\boldsymbol{r} = r \boldsymbol{e}_r$;<br>$\mathrm{d}\boldsymbol{r} = \mathrm{d}r~\boldsymbol{e}_r + r~\mathrm{d}\vartheta~\boldsymbol{e}_{\vartheta} + r~\sin\vartheta~\mathrm{\mathrm{d}}\varphi~\boldsymbol{e}_{\varphi}$ | sferne koordinate | $\boldsymbol{e}_r(\vartheta, \varphi)$, $\boldsymbol{e}_{\vartheta}(\vartheta, \varphi)$, $\boldsymbol{e}_{\varphi}(\varphi)$ čine desni ortogonalni sustav, vidi [sliku 3](#slika-3). |

Ako se umjesto [desnog koordinatnog sustava](#slika-4) koristi [lijevi koordinatni sustav](#slika-5), to treba unaprijed jasno naglasiti kako ne bi došlo do pogrešne upotrebe simbola.

![](./images/symbol-1.svg)

<span id="slika-1">**Slika 1**</span> Desni Kartezijev koordinatni sustav

![](./images/symbol-2.svg)

<span id="slika-2">**Slika 2**</span> Desni cilindrični koordinatni sustav

![](./images/symbol-3.svg)

<span id="slika-3">**Slika 3**</span> Desni sferni koordinatni sustav

![](./images/symbol-4.svg)

<span id="slika-4">**Slika 4**</span> Desni koordinatni sustav

![](./images/symbol-5.svg)

<span id="slika-5">**Slika 5**</span> Lijevi koordinatni sustav

## Skalari i vektori

U ovom odjeljku bazni vektori označavaju se s $\boldsymbol{e}_1$, $\boldsymbol{e}_2$, $\boldsymbol{e}_3$. Mnogi pojmovi iz ovog odjeljka mogu se poopćiti na $n$-dimenzionalni prostor.

Skalari i vektori sami po sebi ne ovise o izboru koordinatnog sustava, dok skalarne komponente vektora ovise o izboru koordinatnog sustava.

Za bazne vektore $\boldsymbol{e}_1$, $\boldsymbol{e}_2$, $\boldsymbol{e}_3$ svaki se vektor $\boldsymbol{a}$ može zapisati kao $\boldsymbol{a}=a_1\boldsymbol{e}_1+a_2\boldsymbol{e}_2+a_3\boldsymbol{e}_3$, gdje su $a_1$, $a_2$ i $a_3$ jednoznačno određeni skalari koji se zovu „koordinate” vektora u odnosu na tu bazu, a $a_1\boldsymbol{e}_1$, $a_2\boldsymbol{e}_2$ i $a_3\boldsymbol{e}_3$ zovu se komponentni vektori u odnosu na tu bazu.

U ovom odjeljku razmatraju se samo Kartezijeve (ortogonalne) koordinate običnog prostora. Kartezijeve koordinate označavaju se s $x$, $y$, $z$ ili $a_1$, $a_2$, $a_3$ ili $x_1$, $x_2$, $x_3$.

Svi indeksi $i$, $j$, $k$ u ovom odjeljku idu od $1$ do $3$.

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n14.1">n14.1</span> | $\boldsymbol{a}$;<br>$\vec{a}$ | vektor $\boldsymbol{a}$ | |
| <span id="n14.2">n14.2</span> | $\boldsymbol{a} + \boldsymbol{b}$ | zbroj vektora $\boldsymbol{a}$ i $\boldsymbol{b}$ | $(\boldsymbol{a} + \boldsymbol{b})_i = a_i + b_i$. |
| <span id="n14.3">n14.3</span> | $x\boldsymbol{a}$ | umnožak skalara $x$ i vektora $\boldsymbol{a}$ | $(x\boldsymbol{a})_i = xa_i$. |
| <span id="n14.4">n14.4</span> | $\lvert \boldsymbol{a}\rvert$ | duljina vektora $\boldsymbol{a}$, norma vektora $\boldsymbol{a}$ | $\lvert \boldsymbol{a}\rvert=\sqrt{a_x^2+a_y^2+a_z^2}$;<br>može se koristiti i $\lVert a\rVert$. |
| <span id="n14.5">n14.5</span> | $\boldsymbol{0}$;<br>$\vec{0}$ | nulvektor | Duljina nulvektora je $0$. |
| <span id="n14.6">n14.6</span> | $\boldsymbol{e_a}$ | jedinični vektor u smjeru $\boldsymbol{a}$ | $\boldsymbol{e_a} = \boldsymbol{a}/\lvert\boldsymbol{a}\rvert\quad (\boldsymbol{a}\ne \boldsymbol{0})$. |
| <span id="n14.7">n14.7</span> | $\boldsymbol{e}_x$, $\boldsymbol{e}_y$, $\boldsymbol{e}_z$;<br>$\boldsymbol{e}_1$, $\boldsymbol{e}_2$, $\boldsymbol{e}_3$ | jedinični vektori u smjeru Kartezijevih koordinatnih osi | Mogu se koristiti i $\boldsymbol{i}$, $\boldsymbol{j}$, $\boldsymbol{k}$. |
| <span id="n14.8">n14.8</span> | $a_x$, $a_y$, $a_z$;<br>$a_i$ | Kartezijeve komponente vektora $\boldsymbol{a}$ | $\boldsymbol{a} = a_x \boldsymbol{e}_x + a_y \boldsymbol{e}_y + a_z \boldsymbol{e}_z$;<br>ako su bazni vektori određeni kontekstom, vektor se može pisati $\boldsymbol{a} = (a_x, a_y, a_z)$.<br>$a_x = \boldsymbol{a}\cdot \boldsymbol{e}_x$, $a_y = \boldsymbol{a}\cdot \boldsymbol{e}_y$, $a_z = \boldsymbol{a}\cdot \boldsymbol{e}_z$;<br>$\boldsymbol{r} = x\boldsymbol{e}_x + y\boldsymbol{e}_y + z\boldsymbol{e}_z$ je vektor položaja s koordinatama $x$, $y$, $z$. |
| <span id="n14.9">n14.9</span> | $\delta_{ik}$ | Kroneckerov delta-simbol | $\delta_{ik}=[i=k]$, pri čemu definiciju $[\cdot]$ vidi u [n6.24](#n6.24), tj.:<br>$\delta_{ik}=1\quad (i=k)$;<br>$\delta_{ik}=0\quad (i\ne k)$. |
| <span id="n14.10">n14.10</span> | $\varepsilon_{ijk}$ | Levi-Civitin simbol | $\varepsilon_{123} = \varepsilon_{231} = \varepsilon_{312} = 1$;<br>$\varepsilon_{132} = \varepsilon_{321} = \varepsilon_{213} = -1$;<br>svi ostali $\varepsilon_{ijk}$ jednaki su $0$. |
| <span id="n14.11">n14.11</span> | $\boldsymbol{a}\cdot\boldsymbol{b}$ | skalarni/unutarnji produkt vektora $\boldsymbol{a}$ i $\boldsymbol{b}$ | $\displaystyle\boldsymbol{a}\cdot\boldsymbol{b}=\sum\limits_i a_ib_i$. |
| <span id="n14.12">n14.12</span> | $\boldsymbol{a}\times\boldsymbol{b}$ | vektorski/vanjski produkt vektora $\boldsymbol{a}$ i $\boldsymbol{b}$ | U desnom Kartezijevom koordinatnom sustavu $\displaystyle (\boldsymbol{a}\times\boldsymbol{b})_i = \sum\limits_j\sum\limits_k\varepsilon_{ijk}a_jb_k$;<br>definiciju $\varepsilon_{ijk}$ vidi u [n14.10](#n14.10). |
| <span id="n14.13">n14.13</span> | $\mathbf{\nabla}$ | operator nabla | $\displaystyle \mathbf{\nabla} = \boldsymbol{e}_x\frac{\partial}{\partial x}+\boldsymbol{e}_y\frac{\partial}{\partial y}+\boldsymbol{e}_z\frac{\partial}{\partial z}=\sum\limits_i\boldsymbol{e}_i\frac{\partial}{\partial x_i}$. |
| <span id="n14.14">n14.14</span> | $\mathbf{\nabla}\varphi$;<br>$\operatorname{\mathbf{grad}}\varphi$ | gradijent od $\varphi$ | $\displaystyle \mathbf{\nabla}\varphi=\sum\limits_i\boldsymbol{e}_i\frac{\partial\varphi}{\partial x_i}$;<br>za $\operatorname{\mathbf{grad}}$ treba koristiti `\operatorname{\mathbf{grad}}`. |
| <span id="n14.15">n14.15</span> | $\mathbf{\nabla}\cdot\boldsymbol{a}$;<br>$\operatorname{\mathbf{div}}\boldsymbol{a}$ | divergencija od $\boldsymbol{a}$ | $\displaystyle \mathbf{\nabla}\cdot\boldsymbol{a}=\sum\limits_i\frac{\partial a_i}{\partial x_i}$;<br>za $\operatorname{\mathbf{div}}$ treba koristiti `\operatorname{\mathbf{div}}`. |
| <span id="n14.16">n14.16</span> | $\mathbf{\nabla}\times\boldsymbol{a}$;<br>$\operatorname{\mathbf{rot}}\boldsymbol{a}$ | rotacija od $\boldsymbol{a}$ | $\displaystyle (\mathbf{\nabla}\times\boldsymbol{a})_i=\sum\limits_j\sum\limits_k\varepsilon_{ijk}\frac{\partial a_k}{\partial x_j}$;<br>za $\operatorname{\mathbf{rot}}$ treba koristiti `\operatorname{\mathbf{rot}}`.<br>Ne treba koristiti $\operatorname{\mathbf{curl}}$.<br>Definiciju $\varepsilon_{ijk}$ vidi u [n14.10](#n14.10). |
| <span id="n14.17">n14.17</span> | $\mathbf{\nabla}^2$;<br>$\Delta$ | Laplaceov operator | $\mathbf{\nabla}^2=\dfrac{\partial^2}{\partial x^2}+\dfrac{\partial^2}{\partial y^2}+\dfrac{\partial^2}{\partial z^2}$. |

## Specijalne funkcije

U ovom odjeljku $z$, $w$ su kompleksni brojevi, $k$, $n$ su prirodni brojevi i $k\leq n$.

| Br. | Simbol, izraz | Značenje, istovjetni izrazi | Napomene i primjeri |
| --- | --- | --- | --- |
| <span id="n15.1">n15.1</span> | $\gamma$ | Euler–Mascheronijeva konstanta | $\displaystyle \gamma=\lim\limits_{n\to\infty}\left(\sum\limits_{k=1}^n\frac{1}{k}-\ln n\right)= 0.577~215~6 \dots$. |
| <span id="n15.2">n15.2</span> | $\Gamma(z)$ | gama-funkcija | $\displaystyle\Gamma(z)=\int\limits_0^{\infty}t^{z-1}\mathrm{e}^{-t}\mathrm{d}t\quad (\operatorname{Re}z>0)$;<br>$\Gamma(n+1)=n!$. |
| <span id="n15.3">n15.3</span> | $\zeta(z)$ | Riemannova zeta-funkcija | $\displaystyle\zeta(z)=\sum\limits_{n=1}^{\infty}\frac{1}{n^z}\quad (\operatorname{Re}z>1)$. |
| <span id="n15.4">n15.4</span> | $\operatorname{B}(z, w)$ | beta-funkcija | $\displaystyle\operatorname{B}(z, w)=\int\limits_0^1 t^{z-1}(1-t)^{w-1}\mathrm{d}t\quad (\operatorname{Re} z>0$, $\operatorname{Re} w>0)$;<br>$\operatorname{B}(z, w)=\dfrac{\Gamma(z)\Gamma(w)}{\Gamma(z+w)}$;<br>$\dfrac{1}{(n+1)\operatorname{B}(k+1, n-k+1)}=\dbinom{n}{k}$. |
