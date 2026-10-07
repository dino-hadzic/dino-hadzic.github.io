---
title: Standardna biblioteka
---

## Standardna biblioteka jezika C

Standardna biblioteka jezika C radi s poljima znakova `char[]`/`const char*`.

Vidi i: [fprintf](https://en.cppreference.com/w/c/io/fprintf), [fscanf](https://en.cppreference.com/w/c/io/fscanf), [stringovi bajtova završeni nulom](https://en.cppreference.com/w/c/string/byte)

-   `printf("%s", s)`: pomoću `%s` ispisuje string (polje znakova).
-   `scanf("%s", &s)`: pomoću `%s` učitava string (polje znakova).
-   `sscanf(const char *__source, const char *__format, ...)`: čita varijable iz stringa `__source`, npr. `sscanf(str,"%d",&a)`.
-   `sprintf(char *__stream, const char *__format, ...)`: ispisuje sadržaj formatnog stringa `__format` u `__stream`, npr. `sprintf(str,"%d",i)`.
-   `strlen(const char *str)`: vraća broj znakova od `str[0]` do `'\0'`. Oprez: bez uključene optimizacije O2 ova operacija u uvjetu petlje ima složenost $\Theta(N)$.
-   `strcmp(const char *str1, const char *str2)`: leksikografski uspoređuje `str1 str2`; ako je `str1` leksikografski manji vraća negativnu vrijednost, ako su jednaki vraća `0`, a ako je `str1` leksikografski veći vraća pozitivnu vrijednost. Nemojte pretpostavljati da su jedine moguće povratne vrijednosti `0`, `1` i `-1`: na različitim platformama predznak je uvijek ispravan, ali vrijednosti nisu nužno `0`, `1`, `-1`.
-   `strcpy(char *str, const char *src)`: kopira znakove iz `src` u `str`; `str` i `src` pokazivači su na početak polja znakova, a povratna vrijednost je `str`, uključujući završnu nulu `'\0'`.
-   `strncpy(char *str, const char *src, int cnt)`: kopira najviše `cnt` znakova u `str`; ako `src` završi prije nego što se dosegne `cnt`, u `str` se upisuju prazni znakovi dok ukupno ne bude upisano `cnt` znakova.
-   `strcat(char *str1, const char *str2)`: nadovezuje `str2` na kraj `str1`, pri čemu `*str2` zamjenjuje završni `'\0'` stringa `str1`; vraća `str1`.
-   `strstr(char *str1, const char *str2)`: ako je `str2` podstring stringa `str1`, vraća adresu prvog pojavljivanja `str2` u `str1`; ako `str2` nije podstring stringa `str1`, vraća `NULL`.
-   `strchr(const char *str, int c)`: pronalazi prvo pojavljivanje znaka `c` u stringu `str` i vraća adresu tog položaja. Ako znak nije pronađen, vraća `NULL`.
-   `strrchr(const char *str, int c)`: pronalazi posljednje pojavljivanje znaka `c` u stringu `str` i vraća adresu tog položaja. Ako znak nije pronađen, vraća `NULL`.

## Standardna biblioteka jezika C++

Standardna biblioteka jezika C++ radi s objektima tipa [`std::string`](../lang/csl/string.md), a ujedno je kompatibilna s poljima znakova.

Vidi i: [std::basic\_string](https://en.cppreference.com/w/cpp/string/basic_string), [std::basic\_string\_view](https://en.cppreference.com/w/cpp/string/basic_string_view)

-   Preopterećen je operator `+`: kad su s obje strane `+` vrijednosti tipa `string/char/char[]/const char*`, nadovezuje ih i vraća spojeni string (`string`).
-   Na desnoj strani operatora pridruživanja `=` može stajati `const string/string/const char*/char*`.
-   Operator pristupa `[cur]` vraća referencu na položaj `cur`.
-   Pristupne funkcije `data()/c_str()` vraćaju pokazivač `const char*` čiji je sadržaj jednak sadržaju tog `string`-a.
-   Funkcija `size()` vraća broj znakova u stringu.
-   `find(ch, start = 0)` traži i vraća položaj znaka `ch` počevši od `start`; `rfind(ch)` traži od kraja i vraća položaj prvog pronađenog znaka `ch` (oba broje od `0`) (ako znak nije pronađen, vraća `-1`).
-   `substr(start, len)` izdvaja iz stringa podstring duljine `len` koji počinje na položaju `start` (broji se od `0`) (ako se `len` izostavi, izdvaja do kraja stringa).
-   `append(s)` dodaje `s` na kraj stringa.
-   `append(s, pos, n)` nadovezuje `n` znakova stringa `s` počevši od `pos` na kraj trenutnog stringa.
-   `replace(pos, n, s)` briše `n` znakova počevši od `pos`, a zatim na položaj `pos` umeće string `s`.
-   `erase(pos, n)` briše `n` znakova počevši od `pos`.
-   `insert(pos, s)` umeće string `s` na položaj `pos`.
-   `std::string` ima preopterećene operatore usporedbe, složenosti $\Theta(N)$.
