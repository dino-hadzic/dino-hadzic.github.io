---
title: Standard library
---

## C standard library

The C standard library works with character arrays `char[]`/`const char*`.

See also: [fprintf](https://en.cppreference.com/w/c/io/fprintf), [fscanf](https://en.cppreference.com/w/c/io/fscanf), [null-terminated byte strings](https://en.cppreference.com/w/c/string/byte)

-   `printf("%s", s)`: use `%s` to print a string (character array).
-   `scanf("%s", &s)`: use `%s` to read a string (character array).
-   `sscanf(const char *__source, const char *__format, ...)`: reads variables from the string `__source`, e.g. `sscanf(str,"%d",&a)`.
-   `sprintf(char *__stream, const char *__format, ...)`: writes the contents of the format string `__format` into `__stream`, e.g. `sprintf(str,"%d",i)`.
-   `strlen(const char *str)`: returns the number of characters from `str[0]` up to `'\0'`. Note that without O2 optimization this operation has complexity $\Theta(N)$ when written in a loop condition.
-   `strcmp(const char *str1, const char *str2)`: compares `str1 str2` lexicographically; returns a negative value if `str1` is lexicographically smaller, `0` if they are equal, and a positive value if `str1` is lexicographically larger. Do not assume that the only possible return values are `0`, `1` and `-1`: on different platforms the sign is always correct, but the values are not necessarily `0`, `1`, `-1`.
-   `strcpy(char *str, const char *src)`: copies the characters of `src` into `str`; both `str` and `src` are pointers to the beginning of character arrays, and the return value is `str`, including the null terminator `'\0'`.
-   `strncpy(char *str, const char *src, int cnt)`: copies at most `cnt` characters into `str`; if `src` ends before `cnt` characters are copied, null characters are written into `str` until a total of `cnt` characters have been written.
-   `strcat(char *str1, const char *str2)`: appends `str2` to the end of `str1`, replacing the terminating `'\0'` of `str1` with `*str2`; returns `str1`.
-   `strstr(char *str1, const char *str2)`: if `str2` is a substring of `str1`, returns the address of the first occurrence of `str2` in `str1`; if `str2` is not a substring of `str1`, returns `NULL`.
-   `strchr(const char *str, int c)`: finds the first occurrence of the character `c` in the string `str` and returns the address of that position. Returns `NULL` if the character is not found.
-   `strrchr(const char *str, int c)`: finds the last occurrence of the character `c` in the string `str` and returns the address of that position. Returns `NULL` if the character is not found.

## C++ standard library

The C++ standard library works with string objects of type [`std::string`](../lang/csl/string.md), while also remaining compatible with character arrays.

See also: [std::basic\_string](https://en.cppreference.com/w/cpp/string/basic_string), [std::basic\_string\_view](https://en.cppreference.com/w/cpp/string/basic_string_view)

-   The operator `+` is overloaded: when both sides of `+` are of type `string/char/char[]/const char*`, it concatenates the two operands and returns the concatenated string (`string`).
-   The right-hand side of the assignment operator `=` may be `const string/string/const char*/char*`.
-   The access operator `[cur]` returns a reference to position `cur`.
-   The access functions `data()/c_str()` return a `const char*` pointer whose contents are the same as the `string`.
-   The capacity function `size()` returns the number of characters in the string.
-   `find(ch, start = 0)` finds and returns the position of the character `ch` starting from `start`; `rfind(ch)` searches from the end and returns the position of the first `ch` found (both counted from `0`) (returns `-1` if not found).
-   `substr(start, len)` extracts a substring of length `len` starting at position `start` (counted from `0`) (if `len` is omitted, it extracts up to the end of the string).
-   `append(s)` appends `s` to the end of the string.
-   `append(s, pos, n)` appends the `n` characters of the string `s` starting from `pos` to the end of the current string.
-   `replace(pos, n, s)` erases `n` characters starting from `pos`, then inserts the string `s` at `pos`.
-   `erase(pos, n)` erases `n` characters starting from `pos`.
-   `insert(pos, s)` inserts the string `s` at position `pos`.
-   `std::string` overloads the comparison operators, with complexity $\Theta(N)$.
