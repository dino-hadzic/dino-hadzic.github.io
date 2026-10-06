---
title: Common tricks
---

This page lists some small tricks useful in contests.

## Exploit locality

Locality means that a program tends to access data items that are close to recently accessed items, or the recently accessed items themselves. Locality is divided into temporal locality and spatial locality.

See [Loop Unroll](../lang/optimizations.md#循环展开-loop-unroll), [Code Layout Optimizations](../lang/optimizations.md#代码布局优化-code-layout-optimizations) and related sections for details.

## Loop macros

The following code can be simplified with a macro:

```cpp
for (int i = 0; i < N; i++) {
  // loop body omitted
}

// Simplify with a macro
#define f(x, y, z) for (int x = (y), __ = (z); x < __; ++x)

// The loop can then be written as `f(i, 0, N)`. For example:
// a is a STL container
f(i, 0, a.size()) { ... }
```

Another useful macro:

```cpp
#define _rep(i, a, b) for (int i = (a); i <= (b); ++i)
```

## Make good use of namespaces

Using namespaces makes a program more readable and easier to debug.

??? note "Example: NOI 2018 屠龙勇士"
    ```cpp
    // NOI 2018 屠龙勇士 – code for 40% partial score
    #include <algorithm>
    #include <cmath>
    #include <cstring>
    #include <iostream>
    using namespace std;
    long long n, m, a[100005], p[100005], aw[100005], atk[100005];
    
    namespace one_game {
    // variables can be declared inside a namespace too
    void solve() {
      for (int y = 0;; y++)
        if ((a[1] + p[1] * y) % atk[1] == 0) {
          cout << (a[1] + p[1] * y) / atk[1] << endl;
          return;
        }
    }
    }  // namespace one_game
    
    namespace p_1 {
    void solve() {
      if (atk[1] == 1) {  // solve 1-2
        sort(a + 1, a + n + 1);
        cout << a[n] << endl;
        return;
      } else if (m == 1) {  // solve 3-4
        long long k = atk[1], kt = ceil(a[1] * 1.0 / k);
        for (int i = 2; i <= n; i++)
          k = aw[i - 1], kt = max(kt, (long long)ceil(a[i] * 1.0 / k));
        cout << k << endl;
      }
    }
    }  // namespace p_1
    
    int main() {
      int T;
      cin >> T;
      while (T--) {
        memset(a, 0, sizeof(a));
        memset(p, 0, sizeof(p));
        memset(aw, 0, sizeof(aw));
        memset(atk, 0, sizeof(atk));
        cin >> n >> m;
        for (int i = 1; i <= n; i++) cin >> a[i];
        for (int i = 1; i <= n; i++) cin >> p[i];
        for (int i = 1; i <= n; i++) cin >> aw[i];
        for (int i = 1; i <= m; i++) cin >> atk[i];
        if (n == 1 && m == 1)
          one_game::solve();  // solve 8-13
        else if (p[1] == 1)
          p_1::solve();  // solve 1-4 or 14-15
        else
          cout << -1 << endl;
      }
      return 0;
    }
    ```

## Debugging with macros

When testing locally, programmers often add debugging statements. When submitting to an OJ, they all have to be removed so that their output does not affect the judging of the program's output, which takes time. Defining macros saves time here. The rough program structure is:

```cpp
#define DEBUG
#ifdef DEBUG
// do something when DEBUG is defined
#endif
// or
#ifndef DEBUG
// do something when DEBUG isn't defined
#endif
```

`#ifdef` checks whether the corresponding identifier has been defined with `#define` in the program; if so, the following statements are compiled. `#ifndef` compiles the following statements when the identifier is not defined.

So it suffices to put the debugging code inside `#ifdef DEBUG` and the real submission code inside `#ifndef DEBUG`, making local testing easy. When submitting, just comment out the `#define DEBUG` line. Alternatively, do not define the identifier in the program but pass the `-DDEBUG` compiler option to define `DEBUG` at compile time; then the program needs no changes at all when submitting.

Many OJs compile with the `-DONLINE_JUDGE` option; using this feature well saves a lot of time.

## Stress testing (对拍)

Stress testing is a way of checking or debugging that verifies a program's correctness by comparing the outputs of two programs. You can compare the output of your own program with that of another program to judge whether yours is correct.

The process has to be repeated many times, so it should be automated with a batch script.

Specifically, stress testing needs a [test generator](../tools/testlib/generator.md) and two programs whose outputs are to be compared.

Each run of the generator writes the generated data to the input file; using redirection, both programs read the data and write their output to given files; finally the files are compared with the `fc` command on Windows (`diff` on Linux) to check correctness. If a bug is found, the data just generated can be used directly for debugging.

A rough stress-testing program:

```cpp
#include <cstdio>
#include <cstdlib>

int main() {
  // For Windows
  // do not use file I/O while stress testing
  // of course, this program can also be rewritten as a batch script
  while (true) {
    system("gen > test.in");  // the generator writes data to the input file
    system("test1.exe < test.in > a.out");  // get the output of program 1
    system("test2.exe < test.in > b.out");  // get the output of program 2
    if (system("fc a.out b.out")) {
      // this line compares the outputs
      // fc returns 0 when the outputs match, otherwise there is a difference
      system("pause");  // so the differences can be inspected
      return 0;
      // the input data is stored in test.in and can be used directly for debugging
    }
  }
}
```

## Memory pool

With dynamic allocation, frequent use of `new`/`malloc` costs a lot of time and space and may even fragment memory, degrading performance, so that an otherwise correct program gets TLE/MLE.

This is where the "memory pool" technique helps: before actually using memory, allocate a certain amount in advance as a reserve. When dynamic allocation is needed, simply take a block from the reserve.

In most OI problems, the maximum memory needed can be computed in advance and allocated all at once.

Example:

```cpp
// dynamically allocate an array of 32-bit signed integers:
int* newarr(int sz) {
  static int pool[MAXN], *allocp = pool;
  return allocp += sz, allocp - sz;
}

// dynamic node creation for a segment tree:
Node* newnode() {
  static Node pool[MAXN << 1], *allocp = pool - 1;
  return ++allocp;
}
```

## References

[洛谷日报 #86 (Chinese)](https://studyingfather.blog.luogu.org/some-coding-tips-for-oiers)

《算法竞赛入门经典 习题与解答》
