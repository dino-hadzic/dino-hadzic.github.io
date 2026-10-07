---
title: Common mistakes
---

This page lists some mistakes that many people often make in contests.

## Mistakes caused by differences in environment

-   Using the `%I64d` format specifier in `scanf` or `printf` may cause wrong input/output formatting on Linux.

## Mistakes that cause CE

These mistakes are mostly lexical, syntactic and semantic errors; their causes are fairly simple and they are easy to fix.

Examples:

-   Typos such as writing `int main()` as `int mian()`.

-   Forgetting the semicolon after a `struct` or `class`.

-   Arrays that are too large, using (on an OJ) disallowed functions (e.g. multithreading), or a function that is declared but not defined, cause link errors.

-   Mismatched function argument types.

    -   Example: calling the `max` function from the `<algorithm>` header with one argument of type `int` and one of type `long long`.

        ```cpp
        // query is a user-defined function returning long long
        printf("%lld\n", max(0, query(1, 1, n, l, r));

        //error    no instance of overloaded function "std::max" matches the argument list
        ```

-   Skipping the initialization of some local variables when using `goto` and `switch-case`.

## Mistakes that do not cause CE but cause a Warning

A program written with this kind of mistake compiles, but will most likely produce a wrong result. The compiler points out these mistakes when compiling with the `-W{warningtype}` option.

-   Confusing the assignment operator `=` with the comparison operator `==`.

    -   Example:

        ```cpp
        std::srand(std::time(nullptr));
        int n = std::rand();
        if (n = 1)
          printf("Yes");
        else
          printf("No");

        // whatever the random value of n, the output is always Yes
        // warning    incorrect operator: constant assignment in Boolean context. Consider using "==" instead.
        ```

    -   If you really want to use `=` in a statement where `==` would normally be used (e.g. `while (foo = bar)`) and do not want a Warning, you can use **double parentheses**: `while ((foo = bar))`.

-   Mistakes caused by operator precedence.

    -   Example:

        ```cpp
        // wrong
        // std::cout << (1 << 1 + 1);
        // correct
        std::cout << ((1 << 1) + 1);

        // warning    "<<": check operator precedence for a possible error; use parentheses to clarify precedence
        ```

-   Incorrect use of the `static` modifier.

-   Missing the address-of operator `&` when reading with `scanf`.

-   Argument types not matching the format specifiers when using `scanf` or `printf`.

-   Using bit operations together with the logical operator `==` without parentheses.
    -   Example: `(x >> j) & 3 == 2`

-   `int` literal overflow.

    -   Example: `long long x = 0x7f7f7f7f7f7f7f7f`, `1<<62`.

-   Uninitialized local variables.

    ???+ note "What happens with an uninitialized variable"
        Original: <https://loj.ac/d/3679> by @hly1204
        
        For example, if we declare `int a;` in C++ without initializing it, we may sometimes think `a` is a "random" value (it may actually not be truly random), or we may think of it as some fixed value, but in fact neither is the case.
        
        In the simple test code
        
        <https://wandbox.org/permlink/T2uiVe4n9Hg4EyWT>
        
        the code is:
        
        ```cpp
        #include <iostream>
        
        int main() {
          int a;
          std::cout << std::boolalpha << (a < 0 || a == 0 || a > 0);
          return 0;
        }
        ```
        
        On some compilers and environments, with optimizations enabled, the output is false.
        
        If you are interested, see <https://www.ralfj.de/blog/2019/07/14/uninit.html>; although the experiment is done in Rust, the essence is the same.

-   A local variable with the same name as a global one, so the global variable is accidentally shadowed. (Enabling `-Wshadow` detects this kind of mistake.)

-   Output errors caused by operator overloading.
    -   Example:

        ```cpp
        // Intent: the first << is the overloaded operator and means output; the second << is the shift operator
        // and means shifting 1 left by 1 bit. But because the parentheses were forgotten, the compiler treats the second <<
        // as the output operator too, so the output differs from what was expected. Wrong: std::cout << 1 << 1; Correct:
        std::cout << (1 << 1);
        ```

## Mistakes that cause neither CE nor a Warning

These mistakes cannot be found by the compiler; you can only find them yourself.

### Mistakes that lead to WA

-   Not clearing arrays after processing one test case and before reading the next.

-   Fast input not handling negative numbers.

-   The data type used is not wide enough, causing overflow.
    -   The situation described by the saying "three years of OI go down the drain if you don't use `long long`" (三年 OI 一场空，不开 `long long` 见祖宗). The contestant loses points because they did not use `long long` (define the integer as `long long`) in the right place, resulting in a wrong answer.

-   When storing a graph, node numbering starts at 0, but the endpoints of the edges given in the problem are numbered from 1, and the -1 is forgotten when reading.

-   Mistyped or reversed greater-than/less-than sign.

-   Mixing `scanf/printf` and `std::cin/std::cout` after `ios::sync_with_stdio(false);`, causing garbled input/output.

    -   Example:

        ```cpp
        // This example shows the consequences of mixing the two kinds of IO after turning off synchronization with stdio
        // Stepping through it is recommended to observe the effect
        #include <cstdio>
        #include <iostream>

        int main() {
          // After synchronization is turned off, cin/cout use their own buffer instead of synchronizing output
          // with the scanf/printf buffer, which reduces IO time
          std::ios::sync_with_stdio(false);
          // With cout, when '\n' is used for a newline, the content is buffered and not output immediately
          std::cout << "a\n";
          // The '\n' of printf flushes printf's buffer, so the output gets out of order
          printf("b\n");
          std::cout << "c\n";
          // cout's buffer is only output when the program ends
          return 0;
        }
        ```

-   Mistakes caused by macro expansion without parentheses.

    -   Example: this macro returns not $4^2 = 16$ but $2+2\times 2+2 = 8$.

        ```cpp
        #define square(x) x* x
        printf("%d", square(2 + 2));
        ```

-   Arithmetic errors caused by not using `unsigned` when hashing.
    -   Right-shifting a negative number fills the highest bit with 1. See: [Bitwise operators](../lang/op.md#位操作符).

-   Debug output statements not removed or commented out.

-   A stray `;`.

    -   Example:

        ```cpp
        /* clang-format off */
        while (1);
            printf("OI Wiki!\n");
        ```

-   Wrong sentinel value. For example, node `0` of a balanced tree.

-   When initializing variables with `:` in the constructor of a class or struct, the declaration order of the variables does not match the dependencies during initialization.

    -   The initialization order of member variables depends on the order in which they are declared in the class, not on the order in the initializer list. See "Initialization order" in [Constructors and member initializer lists](https://zh.cppreference.com/w/cpp/language/constructor)
    -   Example:

        ```cpp
        #include <iostream>

        class Foo {
         public:
          int a, b;

          // a will be initialized before b, and its value is indeterminate
          Foo(int x) : b(x), a(b + 1) {}
        };

        int main() {
          Foo bar(1, 2);
          std::cout << bar.a << ' ' << bar.b;
        }

        // Possible output: -858993459 1
        ```

-   When merging sets in a disjoint set union, the roots of the two elements are not merged.

    -   Example:

        ```cpp
        f[a] = b;              // wrong
        f[find(a)] = find(b);  // correct
        ```

-   Using `freopen` with `a` (append mode)
    -   CCF's judging environment does not clear the output file, so using `a` causes the previous contestant's output to be read by the judge as well, resulting in WA

#### Different newline characters

???+ warning "Warning"
    In official contests, efforts are made to ensure that the environment in which contestants solve problems is the same as the final testing environment.
    
    This section only applies to situations such as mock contests, and we also recommend that problem setters make the data conform to the [data format](problemsetting.md#data-format) as far as possible.

Different operating systems use different characters to mark a newline; here are the newline characters of several commonly used systems:

-   LF (written `\n`): `Unix` or `Unix`-compatible systems

-   CR+LF (written `\r\n`): `Windows`

-   CR (written `\r`): `Mac OS` version 9 and earlier

C/C++ uses the escape sequence `\n` for newlines, which may lead us to assume that newlines in the input are also always represented by `\n`, so we read only one character as the newline; this means we do not read the input file completely.

Solutions:

-   Call `getchar()` repeatedly until the desired character is read.

-   Read with `cin`, **which may increase the constant factor of the code**.

-   Read a string with `scanf("%s",str)` and then take `str[0]` as the character read.

-   Use `scanf(" %c",&c)` to skip all whitespace characters.

### Mistakes that lead to unpredictable results

Undefined behavior leads to unpredictable results, which may be WA, RE, etc. The compiler usually assumes that your program has no undefined behavior, so the code may behave differently with and without O2.

-   Division by 0 (computing the inverse of 0)

    ???+ warning "Example"
        ```cpp
        cout << x / 0 << endl;
        ```

-   Array (index) out of bounds

    For example:

    -   Setting the initial value of a loop incorrectly leads to accessing the element at index -1.

    -   The edge list of an undirected graph is not doubled.

    -   The segment tree is not allocated 4 times the space.

    -   Misreading the constraints, one zero short.

    -   Wrongly estimating the space complexity of the algorithm.

    -   When writing a segment tree, calling `pushup` or `pushdown` on a leaf.

        The right approach: do not go out of bounds, remember to check your code so that the index `x` being accessed is within the defined indices.

-   A function other than main with a return value reaching its end without executing any return statement

    Even if one branch returns a value but other branches do not, the result is undefined.

    You can add `-Wall` to the compile options and check whether the compiler warns about the function not returning.

-   Attempting to modify a string literal

    ???+ warning "Example"
        ```cpp
        char *p = "OI-wiki";
        p[0] = 'o';
        p[1] = 'i';
        ```

    Attempting to modify a string literal like this leads to **undefined behavior**; other **appropriate** data types such as `std::string` and `char[]` should be used.

-   Freeing a piece of memory multiple times / illegally dereferencing it

    For example:

    -   Dereferencing a pointer before initializing it.

    -   The memory the pointer points to has already been freed.

        When using `erase`, `delete` or `free`, be careful not to apply them to the same address/object more than once.

-   Attempting to free part of a block of memory allocated with `new []`

    For example:

    ```cpp
    object *pool = new object[POOL_SIZE];

    object *pointer = pool + 10;

    // error!
    delete pointer;
    ```

    This commonly happens when, after allocating a whole block of memory in advance with a memory pool, one tries to free a single object obtained from the pool with `delete` or `free()`.

-   Dereferencing a null pointer / dangling pointer

    For null pointers: check for null first, e.g. with `p == nullptr` or `!p`.

    For dangling pointers: set the pointer to `nullptr` when freeing it to avoid this.

-   Signed overflow

    For example, we have the expression `x+1 > x`.

    The normal output should be `true`, but when `x` is `INT_MAX` the output is `false`; this is called `signed integer overflow`.

    You can use a larger data type (such as `long long` or `__int128`), or check for overflow. If there are guaranteed to be no negative numbers, you can also use unsigned integers.

    Signed integer overflow may affect compiler optimizations; for example, the code:

    ```cpp
    int foo(int x) {
      if (x > x + 1) return 1;
      return 0;
    }
    ```

    may be directly optimized by the compiler into:

    ```cpp
    int foo(int x) { return 0; }
    ```

    because the compiler may assume that signed integers never overflow, so `x > x + 1` never holds.

-   Using an uninitialized variable

    ???+ warning "Example"
        ```cpp
        int foo(int a) {
          int t; /* not initialized */
          if (/* use */ t > 3) return a;
          return 0;
        }
        ```

### Mistakes that lead to RE

-   File operations not removed (on some OJs).

-   A wrong comparison function when sorting. `std::sort` requires the comparison function to be a strict weak ordering: `a<a` is `false`; if `a<b` is `true`, then `b<a` is `false`; if `a<b` is `true` and `b<c` is `true`, then `a<c` is `true`. Pay special attention to the second point.
    If these requirements are not met, sorting is very likely to RE.
    For example, when writing the odd-even sorting for Mo's algorithm, this is wrong:

    ```cpp
    bool operator<(const int a, const int b) {
      if (block[a.l] == block[b.l])
        return (block[a.l] & 1) ^ (a.r < b.r);
      else
        return block[a.l] < block[b.l];
    }
    ```

    In the code above, `(block[a.l]&1)^(a.r<b.r)` does not satisfy the second point of the requirements above.
    Changing it like this makes it correct:

    ```cpp
    bool operator<(const int a, const int b) {
      if (block[a.l] == block[b.l])
        // wrong: does not satisfy the strict weak ordering requirement
        // return (block[a.l] & 1) ^ (a.r < b.r);
        // correct
        return (block[a.l] & 1) ? (a.r < b.r) : (a.r > b.r);
      else
        return block[a.l] < block[b.l];
    }
    ```

-   On Windows, insufficient stack space leads to a stack overflow; Windows sends the program a SIGSEGV signal, and the program terminates and returns 3221225725 (i.e. 0xC00000FD, defined in NTSTATUS as `STATUS_STACK_OVERFLOW`).  
    If you use the gcc compiler, you can add `-Wl,--stack=SIZE` when compiling to specify the stack size limit, where `SIZE` is the stack size in bytes.

    On Linux, insufficient stack space leads to a stack overflow; Linux then scribbles over `head_info` in the stack/heap, which in the vast majority of cases makes the program exit immediately with a message like `segmentation fault (core dumped)`.  
    You can use `ulimit -s SIZE` in a terminal to change the stack limit of the current terminal, where `SIZE` is the stack size in kilobytes (KB).  
    **Note that if you set the stack limit too large, infinite recursion may make the recursion stack too large and crash the system.**

### Mistakes that lead to TLE

-   Missing boundary check in divide and conquer, leading to infinite recursion.

-   Infinite loops.

    -   Loop variables with the same name.

    -   Loop direction reversed.

-   Not marking whether a state has been visited in BFS.

-   Writing min/max with macros

    This mistake greatly increases the running time of the program and may even directly affect the time complexity of the code. It is especially common when beginners write segment trees.

    The common wrong way is:

    ```cpp
    #define Min(x, y) ((x) < (y) ? (x) : (y))
    #define Max(x, y) ((x) > (y) ? (x) : (y))
    ```

    Written this way there is no correctness problem, but if max is applied directly to the return values of functions, e.g. `a = Max(func1(), func2())`, and these functions take a long time to run, the performance of the program suffers greatly, because after macro expansion it becomes `a = func1() > func2() ? func1() : func2()`, which calls the functions three times, one more than a normal max function. Note that if `func1()` returns a different answer each time, this kind of `max` also gives a wrong result, e.g. when `func1()` is `return ++a;` and `a` is a global variable.

    Example: the following code can be hacked to $\Theta(n)$ per query, leading to TLE.

    ```cpp
    #define max(x, y) ((x) > (y) ? (x) : (y))

    int query(int t, int l, int r, int ql, int qr) {
      if (ql <= l && qr >= r) {
        ++ti[t];  // record the number of visits to the node for easier debugging
        return vi[t];
      }

      int mid = (l + r) >> 1;
      if (mid >= qr) return query(lt(t), l, mid, ql, qr);
      if (mid < ql) return query(rt(t), mid + 1, r, ql, qr);
      return max(query(lt(t), l, mid, ql, qr), query(rt(t), mid + 1, r, ql, qr));
    }
    ```

-   Appending a character to a `std::string` with the + operator

    This mistake creates a temporary `string` variable and assigns it to the original variable after the modification. The compiler cannot optimize this away, and with large data it may degrade the time complexity.

    The common wrong way:

    ```cpp
    std::string a;
    char b = 'c';
    a = a + b;
    ```

    When this code runs, the program first creates a temporary `string` variable, then stores the value of `a` in the temporary, then appends the value of `b` at the end, and finally stores it back into `a`.

    From the [assembly output](https://godbolt.org/z/Eo9vn7or5) we can see that `a = a + b` calls functionality of `std::__cxx11::basic_string` three times: `operator+`, `operator=` and variable creation.

    The correct way is:

    ```cpp
    std::string a;
    char b = 'c';
    a += b;
    ```

    [This way](https://godbolt.org/z/eGh33Grf3) directly appends the character `b` to the string `a`, calling `operator+=` only once. For a more detailed performance comparison, see the [Benchmark](https://quick-bench.com/q/JNDGl7HgOszNG-bo7AgVc42owv4).

-   File operations not removed (on some OJs).

-   Repeatedly executing a function whose complexity is not $O(1)$ inside a `for/while` loop. Strictly speaking, this may change the time complexity.

-   A wrong midpoint formula or termination condition in binary search.

### Mistakes that lead to MLE

-   Arrays that are too large.

    ??? note "Memory usage metrics on Linux explained"
        > TL;DR: if you declare an extremely large global static array in a CCF-series exam, be especially careful. All arrays declared by the program are fully counted toward memory usage (unlike most online judges, which only count the part actually used), and in some cases this may even cause MLE on the whole problem.
        
        -   About RSS and VSZ[^ref1][^ref2]
        
            1.  VSZ (Virtual Memory Size)[^ref3]
        
                VSZ is the **virtual memory size** of a process, i.e. the total size of the virtual address space the process can access, usually shown in KB.
        
                Virtual memory is a logical concept and is usually much larger than the actual memory usage.
        
                On Linux you can use the `top` command to view the composition of a process's memory usage; the `VIRT` column represents the virtual memory it occupies.
        
                Virtual memory generally includes address space that the process has allocated but not actually used; in short, roughly as much as was requested is the virtual memory.
        
                Note in particular that common online judges usually only count physical memory usage. But **CCF's judging environment counts virtual memory**, which means that if you declare a large global static array, it takes up a lot of space even if only a small part of it is used.
            2.  RSS (Resident Set Size)[^ref4]
        
                RSS is the **physical memory size** actually occupied by a process, i.e. the size of the page frames resident in RAM, usually shown in KB.
        
                Likewise, you can use `top` to view a process's physical memory in the `RES` column.
        
                RSS generally includes only the part actually loaded into physical memory, i.e. exactly as much as is actually used.
        -   Analysis of memory usage behavior
        
            Suppose the following array is declared:
        
            ```cpp
            const int SIZE = 1e8;
            int arr[SIZE];  // space used: 4 bytes * 100 million = 400 MB
            ```
        
            This is a static array, allocated in the global data segment. The array is not explicitly initialized, so it is usually placed in the BSS segment (if it is explicitly initialized (e.g. all zeros or other values), it is placed in the DATA segment).
        
            -   When the array is not used at all (assuming the compiler does not optimize it away)
        
                -   Physical memory: if the array is not accessed, the demand paging mechanism means the memory pages have not yet been loaded into physical memory. Physical memory does not increase, or increases only slightly (some metadata pages may be loaded).
                -   Virtual memory: the size of the array counts toward virtual memory (an increase of `400MB`), because the virtual address space of the whole array has already been allocated.
            -   When part of the array is used
        
                Suppose only a few elements of the array are used, for example:
        
                ```cpp
                arr[0] = 1;
                arr[999999] = 2;
                ```
        
                -   Virtual memory: does not change, still `400MB`.
                -   Physical memory: each time an element of the array is accessed, the corresponding virtual page is loaded into physical memory. Assuming the system page size is `4KB`, each page holds $4 \text{KB} ÷ 4 \text{B} = 1024$ `int` elements. Accessing the array twice may load 2 pages, i.e. about $2 \times 4 \text{KB} = 8 \text{KB}$ of additional physical memory.
            -   When most of the array is used
        
                Suppose the first $50,000,000$ elements of the array are assigned:
        
                ```cpp
                for (int i = 0; i < 50000000; ++i) {
                  arr[i] = i;
                }
                ```
        
                -   Virtual memory (VSZ): VSZ is still `400MB` and does not change.
                -   Physical memory (RSS): this is sequential access (the $50,000,000$ elements accessed are adjacent in memory), so the number of pages to load is $\left\lceil \dfrac{50,000,000}{1024} \right\rceil = 48,828$.
        
                    Assuming a page size of `4KB`, the total is $48,828 \times 4 \text{KB} \approx 190 \text{MB}$, so physical memory increases to about `190MB`.
        
                    Note: if the array is assigned at random indices, the physical memory usage will differ greatly from the estimate (because pages are loaded by address, so random assignment loads a large number of pages).
        
                Brief summary: as the proportion of the array that is accessed grows, physical memory approaches virtual memory (assuming no page reclamation).
-   Too many elements inserted into an STL container.

    -   Often this is an infinite loop that keeps inserting into the STL container.

    -   It is also possible that you were hacked.

### Mistakes that lead to a large constant factor

-   The modulus is not defined as a constant.

    -   Example:

        ```cpp
        // int mod = 998244353;      // wrong
        const int mod = 998244353;  // correct, lets the compiler treat it as a constant
        ```

-   Unnecessary recursion (tail recursion excluded).

-   Introducing a lot of extra computation when converting recursion into iteration.

### Mistakes that only matter when the program runs locally

-   Possible mistakes in file operations:

    -   During stress testing, calling `fp = fopen()` again without closing the file pointer with `fclose(fp)`. This leaves the process with many dangling file pointers.

    -   File names in `freopen()` without `.in`/`.out`.

-   Forgetting `delete` or `free` after using heap memory.

## References and notes

[^ref1]: [What is RSS and VSZ in Linux memory management - Stack Overflow](https://stackoverflow.com/questions/7880784/what-is-rss-and-vsz-in-linux-memory-management)

[^ref2]: [Need explanation on Resident Set Size/Virtual Size - Stack Overflow](https://unix.stackexchange.com/questions/35129/need-explanation-on-resident-set-size-virtual-size)

[^ref3]: [Virtual memory](https://en.wikipedia.org/wiki/Virtual_memory)

[^ref4]: [Resident set size](https://en.wikipedia.org/wiki/Resident_set_size)
