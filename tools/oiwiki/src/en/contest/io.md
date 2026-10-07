---
title: Input and output optimization
---

This article describes how to optimize stream-based I/O and C-style I/O.

???+ note "Note"
    The actual speed of stream-based I/O and C-style I/O varies somewhat with the environment (such as the compiler, operating system and hardware specification). If you want a deeper analysis, rely on experimental results. Be careful, however, to control the variables in the experiment, so that the influence of several variables does not lead to wrong conclusions.

## Stream-based I/O

For stream-based I/O (such as `std::cin` and `std::cout`), the most common optimizations are turning off synchronization with the C streams and untying the input and output streams.

### Turning off synchronization

Use the [`std::ios::sync_with_stdio(false)`](https://en.cppreference.com/w/cpp/io/ios_base/sync_with_stdio) function to turn off synchronization with the C streams. For compatibility with C, that is, to make sure a program that uses both `printf` and `std::cout` does not get garbled, C++ synchronizes these two kinds of streams. Synchronized C++ streams are guaranteed to be thread-safe.

This is really a conservative measure that C++ takes for the sake of compatibility. With synchronization enabled, on every I/O operation the C++ stream immediately applies the operation to the corresponding C buffer; if the code does not involve C-style I/O at all, this operation is redundant. Therefore synchronization with the C streams can be turned off before doing I/O, but after doing so you must be careful not to use `std::cin` together with `scanf`, nor `std::cout` together with `printf`, in the rest of the code; you may, however, use `std::cin` together with `printf`, and `scanf` together with `std::cout`.

### Untying the streams

Use the [`tie()`](https://en.cppreference.com/w/cpp/io/basic_ios/tie) function to untie the input stream from the output stream.

By default `std::cin` is tied to `&std::cout`, so every formatted input calls `std::cout.flush()` to empty the output buffer, which increases the I/O load. You can untie them with `std::cin.tie(nullptr)` to speed up execution further.

???+ warning "Note"
    You must not omit the argument and write `std::cin.tie()`; this does not untie the streams but returns the output stream tied to `std::cin`. There is also no need to call `std::cout.tie(nullptr)`, because by default no other output stream is tied to `std::cout`.

### Implementation

```cpp
std::ios::sync_with_stdio(false);
std::cin.tie(nullptr);
```

???+ note "Note"
    After performing both operations above, the program must `flush` manually to make sure that what `std::cout` prints appears before `std::cin`. This is because in this situation `std::cout` does not flush its buffer automatically when `std::cin` is called. For example:
    
    ```cpp
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout << "Please input your name: "
              << std::flush;  // or: std::endl;
                              // because every call to std::endl flushes the output buffer, while \n
                              // does not.
    // If std::flush is removed, the prompt will not be shown before the name is entered
    std::cin >> name;
    ```

## C-style I/O

`scanf` and `printf` still have room for speedup; all speedup methods are based on the conversion between integers and strings.

???+ note "Note"
    The input and output optimizations described on this page all target integer data. Input and output optimization for floating-point numbers is very complex; for input see the [Bellerophon algorithm](https://dl.acm.org/doi/10.1145/93542.93557), and for output see the [Ryū algorithm](https://dl.acm.org/doi/10.1145/3192366.3192369).

### Implementation design

???+ note "Note"
    The optimizations here focus on faster I/O, while the data conversion uses naive methods that do not fully exploit hardware features. Nowadays the vast majority of x86 CPUs support the AVX2 instruction set, and SIMD can be used to speed up the conversion between integers and strings. The standard library functions do not use SIMD optimizations; for example, the libstdc++ [implementation](https://github.com/gcc-mirror/gcc/blob/releases/gcc-14.3.0/libstdc%2B%2B-v3/include/bits/charconv.h#L81) converts two consecutive digits at a time and turns them into characters via a lookup table, so optimizing the conversion process may also pay off. Within the scope of competitions, however, the optimizations mentioned in this article are sufficient for the vast majority of situations.

#### Input optimization

Every integer consists of a sign part and a digit part, and the sign always comes before the digits, so the sign part is read first. For the sign part, the `+` of positive integers is usually omitted and does not affect the value represented by the following digits, while `-` cannot be omitted, so it must be checked for. If the input contains no negative integers, this check can be omitted. The digit part contains only the digits 0 to 9, so when a character that cannot be part of an integer (usually a space) is read, we can conclude that the integer has been read completely.

Since the digits are read from left to right, Horner's method can be used for the integer conversion. The whole conversion can therefore be combined with the input.

While reading the digit part, we need to check whether the character read is a decimal digit. We can simply use the condition `ch >= '0' && ch <= '9'`, or the [`isdigit()`](https://en.cppreference.com/w/cpp/string/byte/isdigit) function.

#### Output optimization

For output, the integer must be converted into a string; usually the naive algorithm is used, that is, the digits of the integer are computed directly from the lowest to the highest, converted into characters and printed in reverse order.

### Implementation details

#### Integer overflow

The implementation must take care of integer overflow. For example, carelessly negating the number in the output optimization causes the minimum value of the integer type, after negation, to exceed the maximum value the type can represent, which may lead to wrong output. A similar overflow may occur when reading the minimum value of the type, but in that case the data read may not actually be wrong, because the value obtained by overflow may equal the actual input value.

Signed integer overflow is undefined behavior; the implementation can avoid the problem above by using the fact that in C integer division of negative numbers rounds toward zero. If, however, no negative numbers need to be read or written, or the minimum value of the type cannot appear in the input or output, this problem does not arise.

#### Making the implementation more generic

If a program uses integer variables of several types, you may need to implement several input/output functions with different types but the same logic. In that case you can use a C++ [`template`](https://en.cppreference.com/w/cpp/language/templates.html) to implement input/output optimization for all integer types. For example, under the C++11 standard you can use

```cpp
template <typename T>
typename std::enable_if<std::is_integral<T>::value &&
                        std::is_signed<T>::value>::type
read(T &x);
```

or under the C++20 standard

```cpp
template <std::signed_integral T>
void read(T &x);
```

to define the function.

For readability, the implementations below assume that only integers of type `int` need to be read; they are sufficient for the needs of most problems.

### Implementations

The mainstream implementations differ only in the input/output functions they use; the integer conversion logic is the same. They are introduced below according to the input/output functions they use.

#### Implementation with `getchar` and `putchar`

The core code is as follows.

```cpp
--8<-- "docs/contest/code/io/io_1.cpp:core"
```

#### Implementation with `fread` and `fwrite`

Faster input and output can be achieved with `fread` and `fwrite`. Their signatures are as follows.

```cpp
std::size_t fread(void* buffer, std::size_t size, std::size_t count,
                  std::FILE* stream);
std::size_t fwrite(const void* buffer, std::size_t size, std::size_t count,
                   std::FILE* stream);
```

For example, `fread(Buf, 1, SIZE, stdin)` means: read `SIZE` blocks of size 1 byte from standard input into `Buf`. The return value is the number of bytes successfully read.

Since `fread` and `fwrite` read and write whole blocks, they have a speed advantage over `getchar()` and `putchar()`. If the buffer is large enough, the whole file can be read at once. If the buffer is not large enough, several reads are needed to make sure all of the input is read. To implement this, we only need to redefine `getchar`.

```cpp
char buf[1 << 20], *p1, *p2;
#define gc()                                                               \
  (p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1 << 20, stdin), p1 == p2) \
       ? EOF                                                               \
       : *p1++)
```

Output is similar to input: the content to be printed is first put into a buffer, and at the end the contents of the buffer are written out at once with `fwrite`.

The core code is as follows.

```cpp
--8<-- "docs/contest/code/io/io_2.cpp:core"
```

When using this method, note:

-   With the debug switch off, `fread()` and `fwrite()` are used, and `fwrite()` is executed automatically by the destructor on exit. With the debug switch on, `getchar()` and `putchar()` are used, which makes debugging easier.
-   If you want to read from and write to files, add `freopen()` before all reading and writing.

#### Implementation with `mmap`

`mmap` is a Linux system call that maps a file into memory at once, similar to a memory region that can be referenced by a pointer, and is faster in some situations. Its signature is as follows:

```c
void *mmap(void addr[.length], size_t length, int prot, int flags, int fd,
           off_t offset);
```

???+ warning "Note"
    `mmap` cannot be used in a Windows environment (for example, the judging systems of Codeforces and HDU), and it is also not recommended in official contests. In fact `fread` is already fast enough, and if `mmap` is used to repeatedly read a small chunk of a file, the overhead of a memory mapping and of the kernel handling page faults is far greater than the overhead of `fread`.

First obtain the file descriptor `fd`, then get the file size with `fstat`, and then obtain the pointer `*pc` to the file mapped into memory with `mmap`. After that, `*pc++` can be used directly instead of `getchar()` to read the file.

If you need to read from standard input, `fd` can be set to `0`. **However, using mmap on standard input is extremely dangerous, and you cannot type input in a terminal; you can redirect a file to standard input instead.**

???+ note "Example: [Luogu P10815 \"Template\" Fast input](https://www.luogu.com.cn/problem/P10815)"
    Read $n$ integers in the range $[-n, n]$, sum them and print the sum, where $n \leq 10^8$. The data guarantee that for every prefix of the sequence, the sum of that prefix fits in a $32$-bit signed integer.

The reference code is as follows.

```cpp
--8<-- "docs/contest/code/io/io_3.cpp"
```

## References

[cin.tie 与 sync\_with\_stdio 加速输入输出 - 码农场 (Chinese)](https://www.hankcs.com/program/cpp/cin-tie-with-sync_with_stdio-acceleration-input-and-output.html)

[C++ 高速化 - Heavy Watal (Japanese)](https://heavywatal.github.io/cxx/speed.html)

['Re: mmap/mlock performance versus read' - MARC](https://marc.info/?l=linux-kernel&m=95496636207616&w=2)
