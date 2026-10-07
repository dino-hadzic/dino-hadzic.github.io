---
title: Plug DP
---

## Definition

Some [bitmask DP](./state.md) problems require us to record connectivity information in the state; such problems are vividly called plug DP or connectivity state compression DP. Examples include counting Hamiltonian paths in grid graphs, counting black-and-white colorings of a board in which cells of the same color form a single connected component, counting spanning trees of specific graphs, and so on. These problems usually require us to encode the connectivity of the state and discuss how connectivity changes during state transitions.

## Introduction

### Domino tiling and contour-line DP

Reviewing the old helps us learn the new: before we start learning plug DP, let us recall a classic problem.

???+ note "Example [\"HDU 1400\" Mondriaan’s Dream](https://acm.hdu.edu.cn/showproblem.php?pid=1400)"
    Problem summary: tile an $N\times M$ board completely with $1\times 2$ or $2\times 1$ dominoes; find the number of ways.

When $n$ or $m$ is small, such problems can be solved with [bitmask DP](./state.md). Divide the stages row by row; let $dp(i,s)$ be the number of ways when the first $i$ rows have been considered and the state of row $i$ is $s$. Each bit of the state $s$ indicates whether that position has already been covered from the previous row.

![domino](./images/domino.svg)

Another way of dividing stages is cell-by-cell DP, also called contour-line DP. $dp(i,j,s)$ is the number of ways when we have considered cells up to row $i$, column $j$, and the state on the current contour line is $s$.

Although the state gains one more dimension in cell-by-cell DP, the time complexity of a transition drops to $O(1)$, so the total time complexity is unchanged. Let $f_0$ denote the states of the current stage, $f_1$ the states of the next stage, and $u = f_0(s)$ the function value currently being enumerated; then the state transition equation is:

```cpp
if (s >> j & 1) {       // if already covered
  f1[s ^ 1 << j] += u;  // place nothing
} else {                // if not covered
  if (j != m - 1 && (!(s >> j + 1 & 1))) f1[s ^ 1 << j + 1] += u;  // horizontal
  f1[s ^ 1 << j] += u;                                             // vertical
}
```

Observe that the equations for "place nothing" and "vertical" can be merged.

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <iostream>
    using namespace std;
    constexpr int N = 11;
    long long f[2][1 << N], *f0, *f1;
    int n, m;
    
    int main() {
      while (cin >> n >> m && n) {
        f0 = f[0];
        f1 = f[1];
        fill(f1, f1 + (1 << m), 0);
        f1[0] = 1;
        for (int i = 0; i < n; ++i) {
          for (int j = 0; j < m; ++j) {
            swap(f0, f1);
            fill(f1, f1 + (1 << m), 0);
    #define u f0[s]
            for (int s = 0; s < 1 << m; ++s)
              if (u) {
                if (j != m - 1 && (!(s >> j & 3))) f1[s ^ 1 << j + 1] += u;  // horizontal
                f1[s ^ 1 << j] += u;  // vertical or nothing
              }
          }
        }
        cout << f1[0] << endl;
      }
    }
    ```

??? note "Exercise [\"SRM 671. Div 1 900\" BearDestroys](https://archive.topcoder.com/ProblemStatement/pm/14069)"
    Problem summary: given an $n\times m$ matrix in which each cell is `E` or `S`.
    A scoring scheme is defined for a matrix. Scan the cells in row-major order; if a cell is already occupied by a domino, skip it.
    Otherwise try to place a domino. If the placement direction goes outside the matrix or is occupied by another domino, the placement fails; switch to the other option or skip.
    If the cell is `E`, prefer placing a $1\times 2$ domino;
    if it is `S`, prefer placing a $2\times 1$ domino.
    The score of a matrix is the final number of dominoes placed.
    Find the sum of the scores of all $2^{nm}$ matrices.

### Terminology

Stage: the order in which dynamic programming is executed; the results of later stages depend only on the results of earlier stages (no aftereffects). Many DP problems admit several ways of dividing stages. For example, in the knapsack problem we can usually divide stages either by items or by knapsack capacity (what the outer loop enumerates first). In the domino problem we can divide stages by rows, columns, cells, diagonals, etc.

Contour line: the boundary between decided and undecided states.

![contour line](./images/contour_line.svg)

Plug: the existence of a plug of a cell in some direction means that the cell is connected to its neighbor in that direction.

![plug](./images/plug.svg)

## Path model

### Multiple circuits

#### Example

???+ note "Example [\"HDU 1693\" Eat the Trees](https://acm.hdu.edu.cn/showproblem.php?pid=1693)"
    Problem summary: find the number of ways to cover an $N\times M$ board with several circuits; some cells are obstacles.

Strictly speaking, the multiple-circuits problem does not belong to plug DP, because, as in the domino tiling problem above, it suffices to record whether a plug exists and then merge and generate plugs in pairs.

Note that for a board of width $m$, the contour line has width $m+1$, since it contains $m$ up plugs and $1$ left plug. Note that after one row has been iterated, the rightmost left plug is usually an invalid state, and at the same time we need to add the first left plug of the next row; this requires adjusting the state of the current contour line, usually by shifting all states left. We call this operation rolling, `roll()`.

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_1.cpp"
    ```

#### Exercises

??? note "Exercise [\"ZOJ 3466\" The Hive II](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827368730)"
    Problem summary: same as the previous problem, but the cells are hexagons.

### One circuit

#### Example

???+ note "Example [\"Andrew Stankevich Contest 16 - Problem F\" Pipe Layout](https://codeforces.com/gym/100220)"
    Problem summary: find the number of ways to cover an $N\times M$ board with a single circuit.

In the state representation above, every time we merge a pair of connected plugs we generate a separate circuit; therefore in this problem we also need to distinguish the connectivity between plugs (here it comes!). This requires additional encoding of the state.

#### State encoding

The usual encoding schemes are the bracket representation and the minimal representation; here we focus on the more general minimal representation. We use an integer array of length $m+1$ to record the state of each plug on the contour line, $0$ meaning no plug, and we agree to mark connected plugs with the same number.

Then the following two encodings represent the same state:

-   `0 3 1 0 1 3`
-   `0 1 2 0 2 1`

We map all equal states to the lexicographically smallest representation; for example, in the example above `0 1 2 0 2 1` is a minimal representation.

We use the array `b[]` for the states of the plugs on the contour line. `bb[]` is the smallest number each number is mapped to during minimal-representation encoding. Note that $0$ means the plug does not exist and must not be mapped to another value.

??? note "Implementation"
    ```cpp
    int b[M + 1], bb[M + 1];
    
    int encode() {
      int s = 0;
      memset(bb, -1, sizeof(bb));
      int bn = 1;
      bb[0] = 0;
      for (int i = m; i >= 0; --i) {
    #define bi bb[b[i]]
        if (!~bi) bi = bn++;
        s <<= offset;
        s |= bi;
      }
      return s;
    }
    
    void decode(int s) {
      REP(i, m + 1) {
        b[i] = s & mask;
        s >>= offset;
      }
    }
    ```

We notice that plugs always appear in pairs and disappear in pairs. Hence a state like `0 1 2 0 1 2` is invalid. The valid states form a bracket sequence, and in practice valid states may be very sparse.

#### Hand-written hash table

In some [bitmask DP](./state.md) problems the valid states may be sparse (as in this problem); to optimize time and space complexity we can store the valid DP states in a hash table. C++ contestants can use [std::unordered\_map](http://www.cplusplus.com/reference/unordered_map/unordered_map/), or of course write one by hand, which allows flexibly encapsulating the state transition function in it as well.

???+ note "Implementation"
    ```cpp
    constexpr int MaxSZ = 16796, Prime = 9973;
    
    struct hashTable {
      int head[Prime], next[MaxSZ], sz;
      int state[MaxSZ];
      long long key[MaxSZ];
    
      void clear() {
        sz = 0;
        memset(head, -1, sizeof(head));
      }
    
      void push(int s) {
        int x = s % Prime;
        for (int i = head[x]; ~i; i = next[i]) {
          if (state[i] == s) {
            key[i] += d;
            return;
          }
        }
        state[sz] = s, key[sz] = d;
        next[sz] = head[x];
        head[x] = sz++;
      }
    
      void roll() { REP(i, sz) state[i] <<= offset; }
    } H[2], *H0, *H1;
    ```

In the code above:

-   `MaxSZ` is an upper bound on the number of valid states; it can be estimated or precomputed more precisely.
-   `Prime` is a large prime smaller than `MaxSZ`.
-   `head[]` are the pointers to the head nodes.
-   `next[]` are the pointers to the following states.
-   `state[]` is the state of a node.
-   `key[]` is the key of a node, in this problem the number of ways.
-   `clear()` is the initialization function; as with a hand-written adjacency list, we only need to initialize the head pointers.
-   `push()` is the state transition function, where `d` is a global variable (out of laziness) representing the increment brought by each state transition. If the state is found we `+=`, otherwise we create a new node with state `s` and key `d`.
-   `roll()` rolls the contour line after a whole row has been iterated.

For the complexity analysis of hash tables, and the difference between open and closed hashing, see the relevant chapters on hash tables in [Introduction to Algorithms](../contest/resources.md#书籍).

#### State transition

???+ note "Implementation"
    ```cpp
    REP(ii, H0->sz) {
      decode(H0->state[ii]);                  // fetch the state and decode it
      d = H0->key[ii];                        // get the increment delta
      int lt = b[j], up = b[j + 1];           // left plug, up plug
      bool dn = i != n - 1, rt = j != m - 1;  // down plug, right plug
      if (lt && up) {                         // if both the left and the up plug exist
        if (lt == up) {                       // from the same connected component
          if (i == n - 1 &&
              j == m - 1) {  // merging is allowed only at the last cell; it closes the circuit.
            push(j, 0, 0);
          }
        } else {  // otherwise we must merge the two components, since this problem requires a circuit cover
          REP(i, m + 1) if (b[i] == lt) b[i] = up;
          push(j, 0, 0);
        }
      } else if (lt || up) {  // if exactly one of the left and up plugs exists
        int t = lt | up;      // get that plug
        if (dn) {             // if it can extend downward
          push(j, t, 0);
        }
        if (rt) {  // if it can extend to the right
          push(j, 0, t);
        }
      } else {           // if neither the left nor the up plug exists
        if (dn && rt) {  // generate a pair of new plugs
          push(j, m, m);
        }
      }
    }
    ```

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_2.cpp"
    ```

#### Exercises

??? note "Exercise [\"Ural 1519\" Formula 1](https://acm.timus.ru/problem.aspx?space=1&num=1519)"
    Problem summary: find the number of ways to cover an $N\times M$ board with a single circuit; some cells are obstacles.

??? note "Exercise [\"USACO 5.4.4\" Betsy's Tours](https://hydro.ac/d/USACO/p/USACO544)"
    Problem summary: for an $N\times N$ square ($N\le 7$), find the total number of paths that start at the top-left corner, end at the bottom-left corner and pass through every cell. Although it is a path, since the start and end are fixed it can be converted into a one-circuit problem.

??? note "Exercise [\"POJ 1739\" Tony's Tour](http://poj.org/problem?id=1739)"
    Problem summary: for an $N\times M$ board, find the total number of paths that start at the bottom-left corner, end at the bottom-right corner and pass through every cell; some cells are obstacles.

??? note "Exercise [\"USACO 6.1.1\" Postal Vans](https://vjudge.net/problem/UVALive-2738)"
    Problem summary: find the number of ways to cover a $4\times N$ board with a single directed circuit; big integers are required.

??? note "Exercise [\"HNOI 2007\" Magical Amusement Park](https://www.luogu.com.cn/problem/P3190)"
    Problem summary: given an $n\times m$ grid with a weight in every cell, find an arbitrary circuit maximizing the sum of the weights it passes through.

??? note "Exercise [\"ProjectEuler 393\" Migrating ants](https://projecteuler.net/problem=393)"
    Problem summary: cover an $n\times n$ square with multiple circuits; each configuration with $m$ circuits contributes $2^m$ to the answer. Find the sum of the contributions of all configurations.

### One path

#### Example

???+ note "Example [\"ZOJ 3213\" Beautiful Meadow](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=22&problemSetProblemId=91827367895)"
    Problem summary: for an $N\times M$ square ($N,M\le 8$) with a weight in every cell, find a path maximizing the sum of the weights of the cells it covers.

This is a standard one-path problem. In one-path problems, the encoded state may also contain independent plugs that cannot be paired. In the state transition function we must additionally discuss the generation, merging and disappearance of independent plugs. The generation and disappearance of an independent plug corresponds to one end of the path, so such events cannot happen more than twice (one generation and one disappearance, or two generations and one merge); otherwise the final result would certainly contain several connected components.

We need to additionally record the total number of such events in the state; this information can be encoded into the state (note that extra information like this does not need to be rolled when the contour line is adjusted), or we can add a dimension outside the `hashTable` array. In the sample program below we choose the latter.

#### State transition

???+ note "Implementation"
    ```cpp
    REP(i, n) {
      REP(j, m) {
        checkMax(ans, A[i][j]);  // the single-cell case must be handled separately
        if (!A[i][j]) continue;  // if it is an obstacle, skip; note the state arrays need not be rolled then
        swap(H0, H1);
        REP(c, 3)
        H1[c].clear();  // c is the total number of generation and disappearance events, at most 2
        REP(c, 3) REP(ii, H0[c].sz) {
          decode(H0[c].state[ii]);
          d = H0[c].key[ii] + A[i][j];
          int lt = b[j], up = b[j + 1];
          bool dn = A[i + 1][j], rt = A[i][j + 1];
          if (lt && up) {
            if (lt == up) {  // in a one-path problem we cannot merge identical plugs.
              // Cannot deploy here...
            } else {  // one of the two plugs being merged may be independent, but the same code handles it
              REP(i, m + 1) if (b[i] == lt) b[i] = up;
              push(c, j, 0, 0);
            }
          } else if (lt || up) {
            int t = lt | up;
            if (dn) {
              push(c, j, t, 0);
            }
            if (rt) {
              push(c, j, 0, t);
            }
            // a plug disappears: if it is independent it vanishes; if it came from a pair this amounts to generating an independent plug;
            // either way c + 1 is needed.
            if (c < 2) {
              push(c + 1, j, 0, 0);
            }
          } else {
            d -= A[i][j];
            H1[c].push(H0[c].state[ii]);
            d += A[i][j];    // skip plug generation; this problem does not require full coverage
            if (dn && rt) {  // generate a pair of plugs
              push(c, j, m, m);
            }
            if (c < 2) {  // generate an independent plug
              if (dn) {
                push(c + 1, j, m, 0);
              }
              if (rt) {
                push(c + 1, j, 0, m);
              }
            }
          }
        }
      }
      REP(c, 3) H1[c].roll();  // end of row, adjust the contour line
    }
    ```

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_3.cpp"
    ```

#### Exercises

??? note "Exercise [\"BZOJ 2310\" ParkII](https://hydro.ac/p/bzoj-P2310)"
    Problem summary: an $m\times n$ board with a weight in every cell; find a path cover maximizing the sum of the weights of the cells the path passes through.

??? note "Exercise [\"NOI 2010 Day2\" Travel Route](https://www.luogu.com.cn/problem/P1933)"
    Problem summary: an $n\times m$ board where every cell has a 0/1 weight T\[x]\[y]; find a path cover such that:
    
    -   the i-th visited cell (x, y) satisfies T\[x]\[y]= L\[i]
    -   one end of the path lies on the boundary of the board
    
    Find the number of feasible configurations.

## Coloring model

Besides the path model there is another common model, in which we color the board and adjacent cells of the same color are considered connected. In path problems we enumerate the direction of the current path during the state transition, whereas in coloring problems we enumerate which color the current cell gets. In the coloring model, more than two cells in the state may share the same connectivity. Overall, however, things remain very similar. Let us look at a classic example.

### Example "UVa 10572" Black & White

???+ note "Example [\"UVa 10572\" Black & White](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1513)"
    Problem summary: color the uncolored cells of an $N\times M$ board black and white so that all black regions and all white regions are connected, and no $2\times 2$ sub-rectangle is monochromatic (e.g. the situation in the figure below is invalid). Find the number of valid colorings and construct one valid coloring.
    
    ![black\_and\_white1](./images/black_and_white1.svg)

### State encoding

Let us first consider the state encoding. Without connectivity this is [SGU 197. Nice Patterns Strike Back](https://codeforces.com/problemsets/acmsguru/problem/99999/197), easily solved directly with [bitmask DP](./state.md). Now we need the state to reflect both color and connectivity information; looking at the state of each position on the contour line, every `Offset` bits describe one position on the contour line. Since there are only two colors, black and white, we use the parity of the lowest bit for the color and the remaining part for connectivity.

For the cells above the first row and to the left of the first column, if we want to avoid special cases we may introduce a third color to distinguish them; here we observe that the connectivity information of these boundary states is always 0, so no extra encoding of the third color is needed.

In path problems our contour line consists of $m$ up plugs and $1$ left plug. In this problem, since we also need to check whether the $2\times 2$ sub-rectangle whose bottom-right corner is the current cell is valid, we need to record the color of the top-left cell, so the length of the contour line is still $m+1$.

This encoding scheme still keeps a lot of redundant information (connected regions must have the same color, and the top-left cell only needs color information, not connectivity), but since we already use a hash table and the minimal representation, the impact on the time complexity is small, and to reduce programming effort we do not refine it further.

In the worst case (e.g. the first row alternating black and white), the connectivity information of every plug is different, so we need $4$ bits for connectivity; adding the color information, `Offset` in this problem is $5$ bits.

???+ note "Implementation"
    ```cpp
    constexpr int Offset = 5, Mask = (1 << Offset) - 1;
    int c[N + 2];
    int b[N + 2], bb[N + 3];
    
    T_state encode() {
      T_state s = 0;
      memset(bb, -1, sizeof(bb));
      int bn = 1;
      bb[0] = 0;
      for (int i = m; i >= 0; --i) {
    #define bi bb[b[i]]
        if (!~bi) bi = bn++;
        s <<= Offset;
        s |= (bi << 1) | c[i];
      }
      return s;
    }
    
    void decode(T_state s) {
      REP(i, m + 1) {
        b[i] = s & Mask;
        c[i] = b[i] & 1;
        b[i] >>= 1;
        s >>= Offset;
      }
    }
    ```

### Hand-written hash table

Since we need to construct an arbitrary valid solution, the hash table here needs an extra field `pre[]` recording, for each state, an arbitrary predecessor from the previous stage.

???+ note "Implementation"
    ```cpp
    constexpr int Prime = 9979, MaxSZ = 1 << 20;
    
    template <class T_state, class T_key>
    struct hashTable {
      int head[Prime];
      int next[MaxSZ], sz;
      T_state state[MaxSZ];
      T_key key[MaxSZ];
      int pre[MaxSZ];
    
      void clear() {
        sz = 0;
        memset(head, -1, sizeof(head));
      }
    
      void push(T_state s, T_key d, T_state u) {
        int x = s % Prime;
        for (int i = head[x]; ~i; i = next[i]) {
          if (state[i] == s) {
            key[i] += d;
            return;
          }
        }
        state[sz] = s, key[sz] = d, pre[sz] = u;
        next[sz] = head[x], head[x] = sz++;
      }
    
      void roll() { REP(ii, sz) state[ii] <<= Offset; }
    };
    
    hashTable<T_state, T_key> _H, H[N][N], *H0, *H1;
    ```

### Constructing a solution

With the information above we can easily construct a solution. First traverse the states in the current hash table; if the number of connected components does not exceed $2$, add it to the count. If the count is not $0$, construct the solution backward using the `pre` array; note that at the end of each row, because we performed the `Roll()` operation, the color must be taken from `c[j+1]`.

???+ note "Implementation"
    ```cpp
    void print() {
      T_key z = 0;
      int u;
      REP(i, H1->sz) {
        decode(H1->state[i]);
        if (*max_element(b + 1, b + m + 1) <= 2) {
          z += H1->key[i];
          u = i;
        }
      }
      cout << z << endl;
      if (z) {
        DWN(i, n, 0) {
          B[i][m] = 0;
          DWN(j, m, 0) {
            decode(H[i][j].state[u]);
            int cc = j == m - 1 ? c[j + 1] : c[j];
            B[i][j] = cc ? 'o' : '#';
            u = H[i][j].pre[u];
          }
        }
        REP(i, n) puts(B[i]);
      }
      puts("");
    }
    ```

### State transition

We denote:

-   `cc` the color of the cell currently being colored
-   `lf` the color of the cell to the left
-   `up` the color of the cell above
-   `lu` the color of the top-left cell

We use $-1$ to indicate that a color does not exist. Now we discuss the state transition; there are three cases: merge, inherit and generate:

???+ note "State transition – code"
    ```cpp
    void trans(int i, int j, int u, int cc) {
      decode(H0->state[u]);
      int lf = j ? c[j - 1] : -1, lu = b[j] ? c[j] : -1,
          up = b[j + 1] ? c[j + 1] : -1;  // no color is also a kind of color!
      if (lf == cc && up == cc) {         // merge
        if (lu == cc) return;             // monochromatic 2x2 sub-rectangle
        int lf_b = b[j - 1], up_b = b[j + 1];
        REP(i, m + 1) if (b[i] == up_b) { b[i] = lf_b; }
        b[j] = lf_b;
      } else if (lf == cc || up == cc) {  // inherit
        if (lf == cc)
          b[j] = b[j - 1];
        else
          b[j] = b[j + 1];
      } else {                                             // generate
        if (i == n - 1 && j == m - 1 && lu == cc) return;  // special case
        b[j] = m + 2;
      }
      c[j] = cc;
      if (!ok(i, j, cc)) return;  // check whether generating a closed connected component makes the state invalid
      H1->push(encode(), H0->key[u], u);
    }
    ```

For the last case, note that if a closed connected region has already been generated, we can no longer use its color, otherwise this color would appear in two connected components. It seems we need to record this event additionally; one could follow the approach in [\"ZOJ 3213\" Beautiful Meadow](#example_2) and add another dimension to record this event. However, using the special property of this problem, we can also handle it with a special case.

???+ note "Special case – code"
    ```cpp
    bool ok(int i, int j, int cc) {
      if (cc == c[j + 1]) return true;
      int up = b[j + 1];
      if (!up) return true;
      int c1 = 0, c2 = 0;
      REP(i, m + 1) if (i != j + 1) {
        if (b[i] == b[j + 1]) {  // same connectivity, so the color must be the same
          assert(c[i] == c[j + 1]);
        }
        if (c[i] == c[j + 1] && b[i] == b[j + 1]) ++c1;
        if (c[i] == c[j + 1]) ++c2;
      }
      if (!c1) {               // if a new closed connected component would be generated
        if (c2) return false;  // if the same color still exists on the contour line
        if (i < n - 1 || j < m - 2) return false;
      }
      return true;
    }
    ```

Let us further discuss the disappearance of a connected component. Whenever we color a cell, if no other cell is connected to the cell above it, a closed connected component is formed. This event can only happen in the last two columns of the last row; otherwise, to avoid a monochromatic $2\times 2$ component later, this color would certainly appear again, except in the following situation:

    2 2
    o#
    #o

We handle this situation as a special case; thus, in this problem, we can be lazy and avoid recording whether a closed connected component has already been generated.

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_4.cpp"
    ```

### Exercises

??? note "Exercise [\"Topcoder SRM 312. Div1 Hard\" CheapestIsland](https://archive.topcoder.com/ProblemStatement/pm/6482)"
    Problem summary: given a board with a weight in every cell, find the connected component with the minimum weight sum.

??? note "Exercise [\"JLOI 2009\" Mysterious Creature](https://www.luogu.com.cn/problem/P3886)"
    Problem summary: given a board with a weight in every cell, find the connected component with the maximum weight sum.

??? note "Exercise [\"AtCoder Beginner Contest 211. Problem E\" Red Polyomino](https://atcoder.jp/contests/abc211/tasks/abc211_e)"
    Problem summary: given an $N\times N$ board where every cell is initially black or white. You choose exactly $K$ of the white cells and paint them red; how many colorings are there in which the red cells form one connected component?

## Graph model

???+ note "Example [\"NOI 2007 Day2\" Counting Spanning Trees](https://www.luogu.com.cn/problem/P2109)"
    Problem summary: count the spanning trees of a special kind of graph in which every node is connected by an edge to exactly its $k$ preceding nodes.

???+ note "Example [\"2015 ACM-ICPC Asia Shenyang Regional Contest - Problem E\" Efficient Tree](https://acm.hdu.edu.cn/showproblem.php?pid=5513)"
    Problem summary: given an $N\times M$ grid and edge weights between 4-connected adjacent cells.
    For a spanning tree, the score of each node is 1+\[there is an edge going up]+\[there is an edge going left].
    The score of a spanning tree is the product of the scores of all nodes.
    
    You must find: the edge weight sum of a minimum spanning tree, and the sum of the scores of all minimum spanning trees.
    ($n\le 800,m\le 7$)

## Practice

### Example

???+ note "Example [\"HDU 4113\" Construct the Great Wall](https://acm.hdu.edu.cn/showproblem.php?pid=4113)"
    Problem summary: on an $N\times M$ board, construct a circuit separating all the `x` from all the `o`.

There is a class of plug DP problems that require us to build walls on the board to separate certain elements of the board. Let us call them wall-building problems; they can be viewed both as a coloring model and as a path model.

![greatwall](./images/greatwall.svg)

In this problem, if viewed as a coloring model, we would need to additionally discuss the perimeter of the colored region as well as detect invalid cases of touching at a corner (figure 2). Moreover, unlike [\"UVa 10572\" Black & White](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1513), this problem requires the wall to be a simple polygon, so the following ring-shaped case is invalid here.

    3 3
    ooo
    oxo
    ooo

Therefore we use the path model and reduce it to [one circuit](#one-circuit).

We run the DP along the grid intersections (so the length and width must be increased by $1$); at every transition we must ensure that all `x` are outside the circuit and all `o` inside. Hence we also need to maintain whether the current position is inside the circuit. For this information we can add a dimension, or directly count the parity of the number of down plugs appearing on the contour line before this position (ray casting).

??? note "Example code"
    ```cpp
    #include <cstring>
    #include <iostream>
    using namespace std;
    #define REP(i, n) for (int i = 0; i < n; ++i)
    
    template <class T>
    bool checkMin(T &a, const T b) {
      return b < a ? a = b, true : false;
    }
    
    constexpr int N = 10, M = N;
    constexpr int offset = 3, mask = (1 << offset) - 1;
    int n, m;
    int d;
    constexpr int INF = 0x3f3f3f3f;
    int b[M + 1], bb[M + 1];
    
    int encode() {
      int s = 0;
      memset(bb, -1, sizeof(bb));
      int bn = 1;
      bb[0] = 0;
      for (int i = m; i >= 0; --i) {
    #define bi bb[b[i]]
        if (!~bi) bi = bn++;
        s <<= offset;
        s |= bi;
      }
      return s;
    }
    
    void decode(int s) {
      REP(i, m + 1) {
        b[i] = s & mask;
        s >>= offset;
      }
    }
    
    constexpr int MaxSZ = 16796, Prime = 9973;
    
    struct hashTable {
      int head[Prime], next[MaxSZ], sz;
      int state[MaxSZ];
      int key[MaxSZ];
    
      void clear() {
        sz = 0;
        memset(head, -1, sizeof(head));
      }
    
      void push(int s) {
        int x = s % Prime;
        for (int i = head[x]; ~i; i = next[i]) {
          if (state[i] == s) {
            checkMin(key[i], d);
            return;
          }
        }
        state[sz] = s, key[sz] = d;
        next[sz] = head[x];
        head[x] = sz++;
      }
    
      void roll() { REP(i, sz) state[i] <<= offset; }
    } H[2], *H0, *H1;
    
    char A[N + 1][M + 1];
    
    void push(int i, int j, int dn, int rt) {
      b[j] = dn;
      b[j + 1] = rt;
      if (A[i][j] != '.') {
        bool bad = A[i][j] == 'o';
        REP(jj, j + 1) if (b[jj]) bad ^= 1;
        if (bad) return;
      }
      H1->push(encode());
    }
    
    int solve() {
      cin >> n >> m;
      int ti, tj;
      REP(i, n) {
        scanf("%s", A[i]);
        REP(j, m) if (A[i][j] == 'o') ti = i, tj = j;
        A[i][m] = '.';
      }
      REP(j, m + 1) A[n][j] = '.';
      ++n, ++m, ++ti, ++tj;
      H0 = H, H1 = H + 1;
      H1->clear();
      d = 0;
      H1->push(0);
      int z = INF;
      REP(i, n) {
        REP(j, m) {
          swap(H0, H1);
          H1->clear();
          REP(ii, H0->sz) {
            decode(H0->state[ii]);
            d = H0->key[ii] + 1;
            int lt = b[j], up = b[j + 1];
            bool dn = i != n - 1, rt = j != m - 1;
            if (lt && up) {
              if (lt == up) {
                int cnt = 0;
                REP(i, m + 1) if (b[i])++ cnt;
                if (cnt == 2 && i == ti && j == tj) {
                  checkMin(z, d);
                }
              } else {
                REP(i, m + 1) if (b[i] == lt) b[i] = up;
                push(i, j, 0, 0);
              }
            } else if (lt || up) {
              int t = lt | up;
              if (dn) {
                push(i, j, t, 0);
              }
              if (rt) {
                push(i, j, 0, t);
              }
            } else {
              --d;
              push(i, j, 0, 0);
              ++d;
              if (dn && rt) {
                push(i, j, m, m);
              }
            }
          }
        }
        H1->roll();
      }
      if (z == INF) z = -1;
      return z;
    }
    
    int main() {
      int T;
      cin >> T;
      for (int Case = 1; Case <= T; ++Case) {
        printf("Case #%d: %d\n", Case, solve());
      }
    }
    ```

### Exercises

??? note "Exercise [\"SCOI 2011\" Floor](https://www.luogu.com.cn/problem/P3272)"
    Problem summary: on an $r\times c$ board some cells are obstacles; in how many ways can all obstacle-free cells be tiled with L-shaped tiles?

??? note "Exercise [\"HDU 4796\" Winter's Coming](https://acm.hdu.edu.cn/showproblem.php?pid=4796)"
    Problem summary: color the uncolored cells of an $N\times M$ board black, white and gray so that all black regions and all white regions are connected, the black region and the white region are each connected to both the top and bottom boundary of the board, and the black and white regions are not adjacent. Each cell has a cost; find a coloring minimizing the cost of the gray region.
    
    ![4796](./images/4796.jpg)

??? note "Exercise [\"ZOJ 2125\" Rocket Mania](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=11&problemSetProblemId=91827365624)"
    Problem summary: on a $9\times6$ map, every cell contains a kind of pipe (`-`,`T`,`L`,`+` shaped, or none); pipes can be rotated by 0°,90°,180°,270°. At most how many rows can have their right boundary connected through pipes to the left boundary of row X?

??? note "Exercise [\"ZOJ 2126\" Rocket Mania Plus](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=11&problemSetProblemId=91827365625)"
    Problem summary: on a $9\times6$ map, every cell contains a kind of pipe (`-`,`T`,`L`,`+` shaped, or none); pipes can be rotated by 0°,90°,180°,270°. At most how many rows can have their right boundary connected through pipes to the left boundary?

??? note "Exercise [\"World Finals 2009/2010 Harbin\" Channel](https://qoj.ac/problem/13134)"
    Problem summary: on a grid map, `.` denotes empty ground and `#` denotes rock; find the longest path such that:
    
    1.  it starts at the top-left corner and ends at the bottom-right corner;
    2.  it does not pass through rocks;
    3.  the path does not form a cycle with itself in the 8-connected sense (i.e. it must not touch itself even at corners).

??? note "Exercise [\"HDU 3958\" Tower Defence](https://acm.hdu.edu.cn/showproblem.php?pid=3958)"
    Problem summary: can be reduced to finding the longest path from $\mathit{S}$ to $\mathit{T}$ that must not touch itself, except at corners.

??? note "Exercise [\"UVa 10531\" Maze Statistics](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1472)"
    Problem summary: given an $N\times M$ grid in which each cell independently becomes an obstacle with probability $\mathit{p}$. You must go from the top-left corner of the maze to the bottom-right corner. For each cell, find the probability that it is an obstacle in a **solvable maze (i.e. start and end are 4-connected)**. ($N \le 5$, $M \le 6$)

??? note "Exercise [\"Aizu 2452\" Pipeline Plans](https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2452)"
    Problem summary: there are 12 kinds of tile patterns in total, with a given number of tiles of each kind. They must be laid on a rectangular floor that can be viewed as an $R\times C$ grid, one tile per cell, such that the center of the top-left cell and the center of the bottom-right cell are connected through the lines on the tile patterns. $(2 \le R \times C \le 15)$
    
    ![plug2](./images/plug2.png)

??? note "Exercise [\"SDOI 2014\" Circuit Board](https://www.luogu.com.cn/problem/P3314)"
    Problem summary: an $N\times M$ circuit board on which some cells are obstacles that wires cannot pass through; given $K$ pairs of cells, every pair must be connected by a wire, and wires must not cross each other (a wire may enter a cell from the top boundary and leave from the left boundary while another wire enters from the bottom boundary and leaves from the right). Treating wires as undirected edges, find the minimum total wire length satisfying the requirements and the number of such configurations.

??? note "Exercise [\"SPOJ CAKE3\" Delicious Cake](https://www.spoj.com/problems/CAKE3)"
    Problem summary: a cake that can be viewed as an $N\times M$ grid is cut along grid lines into several pieces; how many different ways of cutting are there? Two ways are the same if and only if every piece has the same shape and the same position. ($\min(N,M) \le 5, \max(N,M) \le 130$)

## Chapter notes

Plug DP problems are usually hard to code and complex to analyze, so they belong to a relatively [niche area](https://github.com/OI-wiki/libs/blob/master/topic/7-%E7%8E%8B%E5%A4%A9%E6%87%BF-%E8%AE%BA%E5%81%8F%E9%A2%98%E7%9A%84%E5%8D%B1%E5%AE%B3.ppt) of OI/ACM. The most classic reference on this topic is [Danqi Chen](https://www.cs.princeton.edu/~danqic/)'s 2008 Chinese national training team paper – [Dynamic Programming Problems Based on Connectivity State Compression](https://github.com/AngelKitty/review_the_national_post-graduate_entrance_examination/tree/master/books_and_notes/professional_courses/data_structures_and_algorithms/sources/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2008%E8%AE%BA%E6%96%87%E9%9B%86/%E9%99%88%E4%B8%B9%E7%90%A6%E3%80%8A%E5%9F%BA%E4%BA%8E%E8%BF%9E%E9%80%9A%E6%80%A7%E7%8A%B6%E6%80%81%E5%8E%8B%E7%BC%A9%E7%9A%84%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E9%97%AE%E9%A2%98%E3%80%8B). Next, notonlysuccess of HDU wrote two consecutive blog posts in 2011 on this topic, going from the basics to the advanced; they are also rare good material, but nowadays have to be dug up from the Web Archive.

-   [notonlysuccess, [Collection] Plug DP](https://web.archive.org/web/20110815044829/http://www.notonlysuccess.com/?p=625)
-   [notonlysuccess, [Complete Edition] Plug DP](https://web.archive.org/web/20111007185146/http://www.notonlysuccess.com/?p=931)

### Domino tiling

[\"HDU 1400\" Mondriaan’s Dream](https://acm.hdu.edu.cn/showproblem.php?pid=1400) also appears in the [Training Guide for Algorithm Contests](../contest/resources.md#书籍) as the example of the section "Dynamic programming on the contour line". [Domino tiling](https://en.wikipedia.org/wiki/Domino_tiling) is a very classic family of mathematical problems; slightly changing its constraints yields subproblems of different difficulty that require different algorithms.

When $m=2$ is fixed, domino tiling is equivalent to the Fibonacci sequence. [Concrete Mathematics](https://www.csie.ntu.edu.tw/~r97002/temp/Concrete%20Mathematics%202e.pdf) uses this problem to introduce the Fibonacci sequence and derives its closed form in several ways.

When $m\le 10,n\le 10^9$, the transition equation can be precomputed in matrix form and [accelerated with matrix multiplication](http://www.matrix67.com/blog/archives/276).

![domino\_v2\_transform\_matrix](./images/domino_v2_transform_matrix.svg)

When $n,m\le 100$, the number of perfect matchings of the corresponding planar graph can be computed with the [FKT algorithm](https://en.wikipedia.org/wiki/FKT_algorithm).

-   [\"51nod 1031\" Domino Tiling](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1031)
-   [\"51nod 1033\" Domino Tiling V2](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1033)|[\"Vijos 1194\" Domino](https://vijos.org/p/1194)
-   [\"51nod 1034\" Domino Tiling V3](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1034)|[\"Ural 1594\" Aztec Treasure](https://acm.timus.ru/problem.aspx?space=1&num=1594)
-   [Wolfram MathWorld, Chebyshev Polynomial of the Second Kind](https://mathworld.wolfram.com/ChebyshevPolynomialoftheSecondKind.html)

### One path

"One path" is a special case of the [Hamiltonian path](https://en.wikipedia.org/wiki/Hamiltonian_path) problem on a [grid graph](https://mathworld.wolfram.com/GridGraph.html). The decision version of the Hamiltonian path problem is an important member of the [NP-complete](https://en.wikipedia.org/wiki/NP-completeness) family.
