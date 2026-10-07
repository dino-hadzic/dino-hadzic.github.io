---
title: Stog
---

## Uvod

![](./images/stack.svg)

Stog (stack) je linearna struktura podataka koja se često koristi u natjecateljskom programiranju. Ovaj članak govori o strukturi podataka stog, a ne o sistemskom stogu ili prostoru stoga pri izvođenju programa.

Izmjene stoga i pristup njegovim elementima slijede načelo „zadnji ušao, prvi izašao”, pa se stog često zove LIFO lista (last in, first out).

??? warning "Upozorenje"
    LIFO znači da se među elementima **trenutačno u spremniku** prvo uklanja onaj koji je posljednji umetnut.
    
    Promotrimo stog sa sljedećim operacijama:
    
    ```text
    push(1)
    pop(1)
    push(2)
    pop(2)
    ```
    
    Gledano u cjelini, 1 prvi ulazi i prvi izlazi, dok 2 posljednji ulazi i posljednji izlazi. Tako bismo dobili FIFO listu, što je očito pogrešno.
    
    Zato pri određivanju je li struktura LIFO ili FIFO treba promatrati elemente koji se trenutačno nalaze u spremniku.

## Implementacija stoga poljem

Poljem možemo jednostavno simulirati stog, kao u nastavku:

???+ note "Implementacija"
    === "C++"
        ```cpp
        int st[N];
        // Ovdje st[0] (odnosno *st) čuva broj elemenata i indeks vrha stoga
        
        // Dodavanje na stog:
        st[++*st] = var1;
        // Pristup vrhu stoga:
        int u = st[*st];
        // Uklanjanje: pazi na granice; ne uklanjaj kad je *st == 0
        if (*st) --*st;
        // Isprazni stog
        *st = 0;
        ```
    
    === "Python"
        ```python
        st = [0] * N
        # Ovdje st[0] čuva broj elemenata i indeks vrha stoga
        
        # Dodavanje na stog:
        st[st[0] + 1] = var1
        st[0] = st[0] + 1
        # Pristup vrhu stoga:
        u = st[st[0]]
        # Uklanjanje: pazi na granice; ne uklanjaj kad je *st == 0
        if st[0]:
            st[0] = st[0] - 1
        # Isprazni stog
        st[0] = 0
        ```

## Stogovi u C++ STL-u

C++ STL nudi spremnik `std::stack`. Prije korištenja treba uključiti zaglavlje `stack`.

???+ info "Definicija spremnika `stack` u STL-u"
    ```cpp
    // clang-format off
    template<
        class T,
        class Container = std::deque<T>
    > class stack;
    ```
    
    `T` je tip podataka pohranjenih u stogu.
    
    `Container` je tip temeljnog spremnika za pohranu elemenata. Mora pružati sljedeće funkcije s njihovim uobičajenim značenjem:
    
    -   `back()`
    -   `push_back()`
    -   `pop_back()`
    
    STL spremnici `std::vector`, `std::deque` i `std::list` zadovoljavaju te zahtjeve. Ako nije drukčije navedeno, zadani temeljni spremnik jest `std::deque`.

Spremnik `stack` u STL-u pruža niz članskih funkcija. Često se koriste:

-   Pristup elementima
    -   `st.top()` vraća element na vrhu stoga
-   Izmjene
    -   `st.push()` umeće predani argument na vrh stoga
    -   `st.pop()` uklanja element s vrha stoga
-   Kapacitet
    -   `st.empty()` vraća je li stog prazan
    -   `st.size()` vraća broj elemenata

Spremnik `std::stack` pruža i nekoliko operatora. Često se koristi operator pridruživanja `=`, kao u ovom primjeru:

```cpp
// Stvori dva stoga, st1 i st2
std::stack<int> st1, st2;

// Dodaj 1 na st1
st1.push(1);

// Pridruži st1 stogu st2
st2 = st1;

// Ispiši element na vrhu stoga st2
cout << st2.top() << endl;
// Ispis: 1
```

## Implementacija stoga Pythonovom listom

U Pythonu možete simulirati stog pomoću liste:

???+ note "Implementacija"
    ```python
    st = [5, 1, 4]
    
    # Dodaj elemente na vrh pomoću append()
    st.append(2)
    st.append(3)
    # >>> st
    # [5, 1, 4, 2, 3]
    
    # Ukloni element s vrha pomoću pop
    st.pop()
    # >>> st
    # [5, 1, 4, 2]
    
    # Isprazni stog pomoću clear
    st.clear()
    ```

## Literatura

1.  [std::stack - zh.cppreference.com](https://zh.cppreference.com/w/cpp/container/stack)
