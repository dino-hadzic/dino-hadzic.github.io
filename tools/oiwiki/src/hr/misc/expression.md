---
title: Izračunavanje vrijednosti izraza
---

Problem koji rješava izračunavanje vrijednosti izraza obično glasi: na ulazu je izraz zadan kao znakovni niz, a treba ispisati njegovu vrijednost. Naravno, postoje i varijante, npr. sadrži li izraz zagrade, potenciranje, koliko varijabli sadrži, treba li provjeriti jesu li više izraza ekvivalentni itd.

Izraz obično treba najprije sintaksno analizirati (grammar parsing), a zatim izračunati; može se i računati tijekom analize. Uloga sintaksne analize jest provjeriti je li ulazni znakovni niz valjan izraz, a obično se rješava sintaksnim analizatorom (parserom).

Izraz sadrži dvije vrste znakova: operande i operatore. Za izraz duljine $n$, uz prikladnu metodu analize, analiza i izračunavanje mogu se obaviti u vremenskoj složenosti $O(n)$.

## Stablo izraza i obrnuta poljska notacija

Jedna metoda rekurzivne analize izraza jest da se izraz analizira kao obično gramatičko pravilo, nakon analize rastavi u stablo izraza prikazano na slici, a zatim se na strukturi stabla računa odozdo prema gore.![](./images/bet.png)

[Obilaskom stabla](../graph/tree-basic.md#obilazak-stabla) izraza mogu se dobiti različite vrste izraza. Aritmetički izrazi dijele se na tri vrste: prefiksne, infiksne i postfiksne izraze. Infiksni izraz najčešće se koristi u svakodnevnom životu; postfiksni izraz računalo lako razumije.

-   Preorder obilazak odgovara prefiksnom izrazu (poljska notacija)
-   Inorder obilazak odgovara infiksnom izrazu
-   Postorder obilazak odgovara postfiksnom izrazu (obrnuta poljska notacija)

Obrnuta poljska notacija (postfiksni izraz) oblik je zapisa matematičkih izraza u kojem operator stoji iza svojih operanada. Primjerice, sljedeći izraz:

$$
a+b*c*d+(e-f)*(g*h+i)
$$

može se zapisati u obrnutoj poljskoj notaciji ovako:

$$
abc*d*+ef-gh*i+*+
$$

Dakle, izrazi u obrnutoj poljskoj notaciji i stabla izraza međusobno si jednoznačno odgovaraju. Obrnuta poljska notacija ne treba zagrade; njezin je redoslijed računanja jednoznačno određen.

Pogodnost obrnute poljske notacije jest u tome što se vrlo lako računa u linearnom vremenu. Primjer: u izrazu $3~2~*~1~-$ u obrnutoj poljskoj notaciji najprije se računa $3 \times 2 = 6$ (koristi se posljednji operator, tj. operator na vrhu stoga), a zatim $6 - 1 = 5$. Vidimo: za izraz u obrnutoj poljskoj notaciji dovoljno je **održavati stog brojeva; svaki put kad naiđemo na operator, skinemo dva elementa s vrha stoga i rezultat operacije ponovno stavimo na stog**. Na kraju je jedini element na stogu rezultat tog izraza u obrnutoj poljskoj notaciji. Taj algoritam ima vremensku složenost $O(n)$.

Hoće li rekurzivna analiza izraza uspjeti ovisi o tome jesu li gramatička pravila razumno osmišljena, tj. može li se uspješno dobiti zadano stablo izraza. Primjerice:

$$
a+b*c
$$

Zbog različitog prioriteta zbrajanja i množenja taj se infiksni izraz može pretvoriti u dva različita stabla izraza. Vidimo da osmišljavanje gramatičkih pravila uvelike ovisi o prioritetu operatora. Osmisliti odgovarajuća rekurzivna gramatička pravila na temelju prioriteta operatora zapravo nije lak posao.

Metoda opisana u nastavku promatra operator i njegov prioritet kao cjelinu te nerekurzivno analizira i računa izraz izravno prema prioritetima operatora.

## Izrazi sa zagradama koji sadrže samo lijevo asocijativne binarne operatore

Promotrimo pojednostavljeni problem. Pretpostavimo da su svi operatori binarni: svaki operator ima dva argumenta. Također, svi su operatori lijevo asocijativni: ako su prioriteti operatora jednaki, izvršavaju se slijeva nadesno. Zagrade su dopuštene.

Za izračunavanje infiksnog izraza ovog tipa možemo ga pretvoriti u postfiksni izraz i zatim izračunati. Definiramo dva [stoga](../ds/stack.md) koji zasebno pohranjuju operatore i operande; svaki put kad naiđemo na broj, izravno ga stavljamo na stog operanada. Svaki blok operatora odgovara jednom paru zagrada, a stog operatora monoton je samo unutar bloka operatora. Svaki put kad naiđemo na operator, treba pogledati elemente najgornjeg bloka operatora na stogu operatora i unutar tog bloka prikladnim skidanjem sa stoga održavati operatore u padajućem redoslijedu prioriteta, pri čemu se pri skidanju računa vrijednost odgovarajućeg podizraza.

U nastavku „ispis” označava ispis u postfiksni izraz, tj. stavljanje broja na stog operanada, odnosno skidanje operatora i dvaju operanada, računanje i vraćanje rezultata na stog operanada. Infiksni izraz prolazimo slijeva nadesno:

1.  Ako naiđemo na broj, izravno ga ispišemo.
2.  Ako naiđemo na lijevu zagradu, stavimo je na stog operatora.
3.  Ako naiđemo na desnu zagradu, neprestano ispisujemo element s vrha stoga dok ne naiđemo na lijevu zagradu, a nju skinemo sa stoga. Drugim riječima, izvršimo sve operatore unutar jednog para zagrada.
4.  Ako naiđemo na neki drugi operator, neprestano ispisujemo sve operatore čiji je prioritet veći ili jednak prioritetu trenutnog operatora. Na kraju novi operator stavimo na stog operatora.
5.  Nakon obrade cijelog niza neki operatori mogu još biti na stogu, pa preostale simbole sa stoga redom ispišemo; pretvorba izraza time je završena.

Slijedi implementacija ove metode za četiri operatora $+$, $-$, $*$, $/$:

??? note "Primjer koda"
    ```cpp
    
    bool delim(char c) { return c == ' '; }
    
    bool is_op(char c) { return c == '+' || c == '-' || c == '*' || c == '/'; }
    
    int priority(char op) {
      if (op == '+' || op == '-') return 1;
      if (op == '*' || op == '/') return 2;
      return -1;
    }
    
    void process_op(stack<int>& st, char op) {  // može se koristiti i za računanje postfiksnog izraza
      int r = st.top();                         // skidamo elemente s vrha stoga, pazimo na redoslijed
      st.pop();
      int l = st.top();
      st.pop();
      switch (op) {
        case '+':
          st.push(l + r);
          break;
        case '-':
          st.push(l - r);
          break;
        case '*':
          st.push(l * r);
          break;
        case '/':
          st.push(l / r);
          break;
      }
    }
    
    int evaluate(string& s) {  // može se preraditi i u pretvorbu infiksnog izraza u postfiksni
      stack<int> st;
      stack<char> op;
      for (int i = 0; i < (int)s.size(); i++) {
        if (delim(s[i])) continue;
    
        if (s[i] == '(') {
          op.push('(');  // 2. ako naiđemo na lijevu zagradu, stavimo je na stog operatora
        } else if (s[i] == ')') {  // 3. ako naiđemo na desnu zagradu, izvršimo sve operatore unutar para zagrada
          while (op.top() != '(') {
            process_op(st, op.top());
            op.pop();  // neprestano ispisujemo vrh stoga dok ne naiđemo na lijevu zagradu
          }
          op.pop();                // lijevu zagradu skidamo sa stoga
        } else if (is_op(s[i])) {  // 4. ako naiđemo na neki drugi operator
          char cur_op = s[i];
          while (!op.empty() && priority(op.top()) >= priority(cur_op)) {
            process_op(st, op.top());
            op.pop();  // neprestano ispisujemo sve operatore s prioritetom većim ili jednakim prioritetu trenutnog
          }
          op.push(cur_op);  // novi operator stavljamo na stog operatora
        } else {            // 1. ako naiđemo na broj, izravno ga ispišemo
          int number = 0;
          while (i < (int)s.size() && isalnum(s[i]))
            number = number * 10 + s[i++] - '0';
          --i;
          st.push(number);
        }
      }
    
      while (!op.empty()) {
        process_op(st, op.top());
        op.pop();
      }
      return st.top();
    }
    
    ```

Vremenska složenost ovog algoritma, koji za izračunavanje vrijednosti izraza implicitno koristi obrnutu poljsku notaciju, iznosi $O(n)$. Malom izmjenom gornje implementacije može se dobiti i izraz u obrnutoj poljskoj notaciji u eksplicitnom obliku.

### Unarni operatori i desno asocijativni operatori

Pretpostavimo sada da izraz sadrži i unarne operatore, tj. operatore sa samo jednim argumentom. Unarni plus i unarni minus česti su primjeri unarnih operatora.

Jedna je razlika u ovom slučaju to što treba odrediti je li trenutni operator unaran ili binaran.

Uočimo da ispred unarnog operatora obično stoji drugi operator ili otvorena zagrada, osim ako je unarni operator na samom početku izraza. Ispred binarnog operatora uvijek stoji operand ili desna zagrada. Stoga možemo označavati može li sljedeći operator biti unaran.

Osim toga, unarne i binarne operatore treba izvršavati na različit način, a prioritet unarnih operatora treba biti viši od prioriteta svih binarnih operatora. Treba napomenuti da su neki unarni operatori, npr. unarni plus i unarni minus, zapravo desno asocijativni.

Desna asocijativnost znači da se pri jednakom prioritetu operatori moraju računati zdesna nalijevo.

Kao što je rečeno, unarni su operatori obično desno asocijativni. Drugi primjer desno asocijativnog operatora jest potenciranje. Izraz $a \wedge b \wedge c$ obično se tumači kao $a^{b^c}$, a ne kao $(a^b)^c$.

Da bismo ispravno obradili takve operatore, odgovarajuća je izmjena ta da se pri jednakom prioritetu skidanje operatora sa stoga odgodi.

Kôd koji treba izmijeniti je sljedeći. Umjesto:

```cpp

while (!op.empty() && priority(op.top()) >= priority(cur_op)) 
```

pišemo

```cpp

while (!op.empty() &&
       ((left_assoc(cur_op) && priority(op.top()) >= priority(cur_op)) ||
        (!left_assoc(cur_op) && priority(op.top()) > priority(cur_op))))

```

pri čemu je left\_assoc funkcija koja određuje je li operator lijevo asocijativan.

Slijedi implementacija za binarne operatore $+$, $-$, $*$, $/$ te unarne operatore $+$ i $-$:

??? note "Primjer koda"
    ```cpp
    
    bool delim(char c) { return c == ' '; }
    
    bool is_op(char c) { return c == '+' || c == '-' || c == '*' || c == '/'; }
    
    bool is_unary(char c) { return c == '+' || c == '-'; }
    
    int priority(char op) {
      if (op < 0)  // unary operator
        return 3;
      if (op == '+' || op == '-') return 1;
      if (op == '*' || op == '/') return 2;
      return -1;
    }
    
    void process_op(stack<int>& st, char op) {
      if (op < 0) {
        int l = st.top();
        st.pop();
        switch (-op) {
          case '+':
            st.push(l);
            break;
          case '-':
            st.push(-l);
            break;
        }
      } else {  // skidamo elemente s vrha stoga, pazimo na redoslijed
        int r = st.top();
        st.pop();
        int l = st.top();
        st.pop();
        switch (op) {
          case '+':
            st.push(l + r);
            break;
          case '-':
            st.push(l - r);
            break;
          case '*':
            st.push(l * r);
            break;
          case '/':
            st.push(l / r);
            break;
        }
      }
    }
    
    int evaluate(string& s) {
      stack<int> st;
      stack<char> op;
      bool may_be_unary = true;
      for (int i = 0; i < (int)s.size(); i++) {
        if (delim(s[i])) continue;
    
        if (s[i] == '(') {
          op.push('(');  // 2. ako naiđemo na lijevu zagradu, stavimo je na stog operatora
          may_be_unary = true;
        } else if (s[i] == ')') {  // 3. ako naiđemo na desnu zagradu, izvršimo sve operatore unutar para zagrada
          while (op.top() != '(') {
            process_op(st, op.top());
            op.pop();  // neprestano ispisujemo vrh stoga dok ne naiđemo na lijevu zagradu
          }
          op.pop();  // lijevu zagradu skidamo sa stoga
          may_be_unary = false;
        } else if (is_op(s[i])) {  // 4. ako naiđemo na neki drugi operator
          char cur_op = s[i];
          if (may_be_unary && is_unary(cur_op)) cur_op = -cur_op;
          while (!op.empty() &&
                 ((cur_op >= 0 && priority(op.top()) >= priority(cur_op)) ||
                  (cur_op < 0 && priority(op.top()) > priority(cur_op)))) {
            process_op(st, op.top());
            op.pop();  // neprestano ispisujemo sve operatore s prioritetom većim ili jednakim prioritetu trenutnog
          }
          op.push(cur_op);  // novi operator stavljamo na stog operatora
          may_be_unary = true;
        } else {  // 1. ako naiđemo na broj, izravno ga ispišemo
          int number = 0;
          while (i < (int)s.size() && isalnum(s[i]))
            number = number * 10 + s[i++] - '0';
          --i;
          st.push(number);
          may_be_unary = false;
        }
      }
    
      while (!op.empty()) {
        process_op(st, op.top());
        op.pop();
      }
      return st.top();
    }
    
    ```

## Literatura

**Ova je stranica većim dijelom prevedena prema blogu [Разбор выражений. Обратная польская нотация](https://e-maxx.ru/algo/expressions_parsing) i njegovu engleskom prijevodu [Expression parsing](https://cp-algorithms.com/string/expression_parsing.html). Ruska je inačica pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0.**

## Dodatna literatura

1.  [Operator-precedence\_parser](https://en.wikipedia.org/wiki/Operator-precedence_parser)
2.  [Shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)

## Zadaci za vježbu

1.  [NOIP2013 普及组 表达式求值 (NOIP 2013, juniorska skupina: Izračunavanje vrijednosti izraza)](https://www.luogu.com.cn/problem/P1981)
2.  [后缀表达式 (Postfiksni izraz)](https://www.luogu.com.cn/problem/P1449)
3.  [Transform the Expression](https://www.spoj.com/problems/ONP/)
