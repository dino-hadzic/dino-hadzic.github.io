---
title: Digit DP
---

This page briefly introduces digit DP.

## Introduction

Digits are what we get when we split a number place by place into ones, tens, hundreds, thousands and so on, and look at the digit in each place. If we split a decimal number, each digit is 0\~9; other bases are analogous.

Digit DP is used to solve a specific class of problems that are fairly easy to recognize; they usually have these features:

1.  we must count the numbers satisfying certain conditions (i.e. the ultimate goal is counting);

2.  after some transformation these conditions can be understood and checked with the idea of "digits";

3.  the input provides an interval of numbers (sometimes only an upper bound) as the restriction for counting;

4.  the upper bound is large (e.g. $10^{18}$), so brute-force enumeration would time out.

The basic principle of digit DP:

Consider how humans count: the most naive way is to start from small and add one at a time. But we notice that for numbers with many digits, this process contains a lot of repetition. For example, counting from 7000 to 7999, from 8000 to 8999 and from 9000 to 9999 is very similar: in all of them the last three digits go from 000 to 999, and the only difference is the thousands digit. So we can merge these processes and store the counting answers produced in them in a common array. The states of this array are set according to the specific requirements of the problem, and transitions are done by recurrence or DP.

Digit DP usually uses the standard techniques of counting problems, e.g. splitting the answer for an interval into the difference of two parts (i.e. $\mathit{ans}_{[l, r]} = \mathit{ans}_{[0, r]}-\mathit{ans}_{[0, l - 1]}$)

Once we have the common answer array, the next step is counting the answer. This can be done with memoized search or with iterative recurrence. To count all answers not exceeding the upper bound without repetition or omission, we enumerate each digit from high to low, consider which digits can be placed in each position, and finally count the answer using the common answer array.

Let us look at several concrete problems.

## Example 1

???+ note "Example 1 [Luogu P2602 Digit Counting](https://www.luogu.com.cn/problem/P2602)"
    Problem summary: given two positive integers $a,b$, for all integers in $[a,b]$ find how many times each digit appears.

### Method 1

#### Explanation

We observe that for full $\mathit{i}$-digit numbers, every digit appears the same number of times, so let the array $\mathit{dp}_i$ be the number of occurrences of each digit among full $i$-digit numbers; leading zeros are not handled for now. Then $\mathit{dp}_i=10 \times \mathit{dp}_{i−1}+10^{i−1}$; the first part is the contribution of the first $i-1$ digits, and the second is the contribution of the $i$-th digit.

With the $\mathit{dp}$ array, let us consider how to count the answer. Split the upper bound into digits and enumerate from high to low; when not tight against the upper bound, the remaining digits can take any value. When tight against the upper bound, the remaining digits can only go from $0$ to the upper bound; compute the contributions of the two parts separately. Finally consider leading zeros: when the $i$-th digit is a leading $0$, digits $1$ through $\mathit{i-1}$ are also $0$, so we have overcounted the answers for filling $i-1$ digits, which must be subtracted.

#### Implementation

???+ note "Sample code"
    ```cpp
    #include <cstdio>
    using namespace std;
    constexpr int N = 15;
    using ll = long long;
    ll l, r, dp[N], mi[N];
    ll ans1[N], ans2[N];
    int a[N];
    
    void solve(ll n, ll *ans) {
      ll tmp = n;
      int len = 0;
      while (n) a[++len] = n % 10, n /= 10;
      for (int i = len; i >= 1; --i) {
        for (int j = 0; j < 10; j++) ans[j] += dp[i - 1] * a[i];
        for (int j = 0; j < a[i]; j++) ans[j] += mi[i - 1];
        tmp -= mi[i - 1] * a[i], ans[a[i]] += tmp + 1;
        ans[0] -= mi[i - 1];
      }
    }
    
    int main() {
      scanf("%lld%lld", &l, &r);
      mi[0] = 1ll;
      for (int i = 1; i <= 13; ++i) {
        dp[i] = dp[i - 1] * 10 + mi[i - 1];
        mi[i] = 10ll * mi[i - 1];
      }
      solve(r, ans1), solve(l - 1, ans2);
      for (int i = 0; i < 10; ++i) printf("%lld ", ans1[i] - ans2[i]);
      return 0;
    }
    ```

### Method 2

#### Explanation

This problem can also be solved with memoized search. $\mathit{dp}_i$ is the answer for $i$ digits when not tight against the upper bound and without leading zeros.

See the code comments for details.

#### Procedure

???+ note "Sample code"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    using namespace std;
    using ll = long long;
    constexpr int N = 50005;
    ll a, b;
    ll f[15], ksm[15], p[15], now[15];
    
    ll dfs(int u, int x, bool f0,
           bool lim) {  // u is the number of digits, f0 whether there are leading zeros, lim whether we are tight against the upper bound
      if (!u) {
        if (f0) f0 = false;
        return 0;
      }
      if (!lim && !f0 && (~f[u])) return f[u];
      ll cnt = 0;
      int lst = lim ? p[u] : 9;
      for (int i = 0; i <= lst; i++) {  // enumerate the digit to place in this position
        if (f0 && i == 0)
          cnt += dfs(u - 1, x, 1, lim && i == lst);  // handle leading zeros
        else if (i == x && lim && i == lst)
          cnt += now[u - 1] + 1 +
                 dfs(u - 1, x, 0,
                     lim && i == lst);  // all digits chosen so far are tight against the given upper bound.
        else if (i == x)
          cnt += ksm[u - 1] + dfs(u - 1, x, 0, lim && i == lst);
        else
          cnt += dfs(u - 1, x, 0, lim && i == lst);
      }
      if ((!lim) && (!f0)) f[u] = cnt;  // memoize only when not tight against the bound and without leading zeros
      return cnt;
    }
    
    ll gans(ll d, int dig) {
      int len = 0;
      memset(f, -1, sizeof(f));
      while (d) {
        p[++len] = d % 10;
        d /= 10;
        now[len] = now[len - 1] + p[len] * ksm[len - 1];
      }
      return dfs(len, dig, 1, 1);
    }
    
    int main() {
      scanf("%lld%lld", &a, &b);
      ksm[0] = 1;
      for (int i = 1; i <= 12; i++) ksm[i] = ksm[i - 1] * 10ll;
      for (int i = 0; i < 9; i++) printf("%lld ", gans(b, i) - gans(a - 1, i));
      printf("%lld\n", gans(b, 9) - gans(a - 1, 9));
      return 0;
    }
    ```

## Example 2

???+ note "Example 2 [HDU 2089 No 62](https://acm.hdu.edu.cn/showproblem.php?pid=2089)"
    Problem summary: count the numbers in an interval whose digits contain neither a 4 nor a consecutive 62.

### Explanation

For the "no 4" condition, just check during enumeration: by never enumerating 4 the state stays valid, so this constraint does not need memoization. For 62, two digits are involved; the counts differ depending on whether the previous digit is 6 or not, so the state must record the different counts. $\mathit{dp}_{\mathit{pos},\mathit{sta}}$ denotes the current position $\mathit{pos}$ and whether the previous digit is 6; here $\mathit{sta}$ only needs the two states 0 and 1, and all non-6 cases can be treated as the same since they do not affect the count.

### Implementation

???+ note "Sample code"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    using namespace std;
    int x, y, dp[15][3], p[50];
    
    void pre() {
      memset(dp, 0, sizeof(dp));
      dp[0][0] = 1;
      for (int i = 1; i <= 10; i++) {
        dp[i][0] = dp[i - 1][0] * 9 - dp[i - 1][1];
        dp[i][1] = dp[i - 1][0];
        dp[i][2] = dp[i - 1][2] * 10 + dp[i - 1][1] + dp[i - 1][0];
      }
    }
    
    int cal(int x) {
      int cnt = 0, ans = 0, tmp = x;
      while (x) {
        p[++cnt] = x % 10;
        x /= 10;
      }
      bool flag = false;
      p[cnt + 1] = 0;
      for (int i = cnt; i; i--) {  // enumerate the digits from high to low
        ans += p[i] * dp[i - 1][2];
        if (flag)
          ans += p[i] * dp[i - 1][0];
        else {
          if (p[i] > 4) ans += dp[i - 1][0];
          if (p[i] > 6) ans += dp[i - 1][1];
          if (p[i] > 2 && p[i + 1] == 6) ans += dp[i][1];
          if (p[i] == 4 || (p[i] == 2 && p[i + 1] == 6)) flag = true;
        }
      }
      return tmp - ans;
    }
    
    int main() {
      pre();
      while (~scanf("%d%d", &x, &y)) {
        if (!x && !y) break;
        if (x > y) swap(x, y);
        printf("%d\n", cal(y + 1) - cal(x));
      }
      return 0;
    }
    ```

## Example 3

???+ note "Example 3 [SCOI2009 Windy Numbers](https://loj.ac/problem/10165)"
    Problem summary: given an interval $[l,r]$, count the numbers in it satisfying **no leading $0$ and every two adjacent digits differ by at least $2$**.

### Explanation

First we transform the problem into a simpler form. Let $\mathit{ans}_i$ be the number of numbers in $[1,i]$ satisfying the condition; the required answer is $\mathit{ans}_r-\mathit{ans}_{l-1}$.

For a number smaller than $n$, going from high to low there is certainly some position where its digit is smaller than the corresponding digit of $n$, while all previous digits equal those of $n$.

With this property we can define $f(i,st,op)$ as the number of numbers when the position about to be considered is the $i$-th from the top, the current prefix state is $st$, and the relation between the prefix and the number being solved is $op$ ($op=1$ means equal, $op=0$ means smaller). In this problem the prefix state is the value of the previous digit, because which digits the current position may not take depends only on the previous digit. In other problems this value can be: the digit sum of the prefix, the $\gcd$ of all digits of the prefix, the remainder of the prefix modulo some number, or a combination of two or more of these.

Write the **state transition equation**: $f(i,st,op)=\sum_{k=1}^{\mathit{maxx}} f(i+1,k,op=1~ \operatorname{and}~ k=\mathit{maxx} )\quad (|\mathit{st}-k|\ge 2)$

Here $k$ is the value of the next digit being enumerated, and $\mathit{maxx}$ is the largest digit currently allowed. Because if $\mathit{op}=1$, the value taken at this position must not exceed the corresponding digit of the number being solved; otherwise there is no restriction.

We find that even when the prefix chosen differs, as long as the three parameters of $f$ are the same, the answer is the same. To prevent this answer from being computed multiple times, we can implement it with [memoized search](./memo.md).

### Implementation

???+ note "Sample code"
    ```cpp
    int dfs(int x, int st, int op)  // op=1 =; op=0 <
    {
      if (!x) return 1;
      if (!op && ~f[x][st]) return f[x][st];
      int maxx = op ? dim[x] : 9, ret = 0;
      for (int i = 0; i <= maxx; i++) {
        if (abs(st - i) < 2) continue;
        if (st == 11 && i == 0)
          ret += dfs(x - 1, 11, op & (i == maxx));
        else
          ret += dfs(x - 1, i, op & (i == maxx));
      }
      if (!op) f[x][st] = ret;
      return ret;
    }
    
    int solve(int x) {
      memset(f, -1, sizeof f);
      dim.clear();
      dim.push_back(-1);
      int t = x;
      while (x) {
        dim.push_back(x % 10);
        x /= 10;
      }
      return dfs(dim.size() - 1, 11, 1);
    }
    ```

## Example 4

???+ note "Example 4. [SPOJMYQ10](https://www.spoj.com/problems/MYQ10/en/)"
    Problem summary: if we write down by hand all integers in $[n,m]$, how many of them look exactly the same in a mirror? ($n,m<10^{44}, T<10^5$)

### Explanation

Note: considering mirroring, only $0,1,8$ are their own mirror images. So "exactly the same" here is not a palindrome in the traditional sense, but a palindrome containing only $0,1,8$.

First, in the digit DP process, obviously only $0,1,8$ can be chosen.

Second, since the values exceed the long long range, $[n,m]=[1,m]-[1,n-1]$ no longer applies (big-integer arithmetic is tedious); instead we need to check whether $n$ is valid, obtaining: $[n,m]=[1,m]-[1,n]+\mathrm{check}(n)$.

Mirroring is solved; how to check for palindromes?

We use a small array to record the previous values. Before passing half the length, it suffices to stay within the upper bound; after passing half, we must also check whether the digit equals its "mirror-symmetric" digit.

Note in particular that the memoization part of this problem cannot use `memset`, otherwise it will time out.

### Implementation

???+ note "Sample code"
    ```cpp
    int check(char cc[]) {  // special check for n
      int strc = strlen(cc);
      for (int i = 0; i < strc; ++i) {
        if (!(cc[i] == cc[strc - i - 1] &&
              (cc[i] == '1' || cc[i] == '8' || cc[i] == '0')))
          return 0ll;
      }
      return 1ll;
    }
    
    // now: current position, eff: number of effective positions, fulc: whether tight against the bound everywhere, ful0: whether all zeros
    int dfs(int now, int eff, bool ful0, bool fulc) {
      if (now == 0) return 1ll;
      if (!fulc && f[now][eff][ful0] != -1)  // memoization
        return f[now][eff][ful0];
    
      int res = 0, maxk = fulc ? dig[now] : 9;
      for (int i = 0; i <= maxk; ++i) {
        if (i != 0 && i != 1 && i != 8) continue;
        b[now] = i;
        if (ful0 && i == 0)  // all leading zeros
          res += dfs(now - 1, eff - 1, 1, 0);
        else if (now > eff / 2)                                  // not past the halfway point
          res += dfs(now - 1, eff, 0, fulc && (dig[now] == i));  // past the halfway point
        else if (b[now] == b[eff - now + 1])
          res += dfs(now - 1, eff, 0, fulc && (dig[now] == i));
      }
      if (!fulc) f[now][eff][ful0] = res;
      return res;
    }
    
    char cc1[100], cc2[100];
    int strc, ansm, ansn;
    
    int get(char cc[]) {  // processing wrapper
      strc = strlen(cc);
      for (int i = 0; i < strc; ++i) dig[strc - i] = cc[i] - '0';
      return dfs(strc, strc, 1, 1);
    }
    
    scanf("%s%s", cc1, cc2);
    printf("%lld\n", get(cc2) - get(cc1) + check(cc1));
    ```

## Example 5

???+ note "Example 5. [P3311 Counting](https://www.luogu.com.cn/problem/P3311)"
    Problem: a positive integer $x$ is called lucky if and only if its decimal representation does not contain any element of the set of digit strings $S$ as a substring. For example, when $S = \{22, 333, 0233\}$, $233233$ is lucky, while $23332333$, $2023320233$, $32233223$ are not. Given $n$ and $S$, compute the number of lucky numbers not exceeding $n$. The answer is taken modulo $10^9 + 7$.
    
    $1 \leq n<10^{1201}，1 \leq m \leq 100，1 \leq \sum_{i = 1}^m |s_i| \leq 1500，\min_{i = 1}^m |s_i| \geq 1$, where $|s_i|$ is the length of the string $s_i$. $n$ has no leading $0$, but $s_i$ may have leading $0$s.

### Explanation

Reading the statement, if we view numbers as strings, this is a multi-pattern matching task, which naturally suggests the Aho–Corasick automaton. In ordinary digit DP we first enumerate the positions from high to low, then what to fill in each position; in this problem this naturally becomes enumerating the number of positions already filled, then which node of the AC automaton we are currently at, and then transitioning from the current node to its child in the AC automaton.

Let $f(i,j,0/1)$ denote that $i$ digits have been filled from high to low (i.e. we have walked $i$ edges in the AC automaton), we are currently at the node labeled $j$, and whether we are currently exactly tight against the upper bound.

As for the "does not contain" condition, just mark the end node of every pattern in the AC automaton and skip these end nodes whenever they are encountered during the DP.

The transition is easy to come up with; see the main function of the code for details.

### Implementation

???+ note "Sample code"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <queue>
    using namespace std;
    using ll = long long;
    constexpr int N = 1505;
    constexpr int mod = 1000000007;
    int n, m;
    char s[N], c[N];
    int ch[N][10], fail[N], ed[N], tot, len;
    
    void insert() {
      int now = 0;
      int L = strlen(s);
      for (int i = 0; i < L; ++i) {
        if (!ch[now][s[i] - '0']) ch[now][s[i] - '0'] = ++tot;
        now = ch[now][s[i] - '0'];
      }
      ed[now] = 1;
    }
    
    queue<int> q;
    
    void build() {
      for (int i = 0; i < 10; ++i)
        if (ch[0][i]) q.push(ch[0][i]);
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i = 0; i < 10; ++i) {
          if (ch[u][i]) {
            fail[ch[u][i]] = ch[fail[u]][i], q.push(ch[u][i]),
            ed[ch[u][i]] |= ed[fail[ch[u][i]]];
          } else
            ch[u][i] = ch[fail[u]][i];
        }
      }
      ch[0][0] = 0;
    }
    
    ll f[N][N][2], ans;
    
    void add(ll &x, ll y) { x = (x + y) % mod; }
    
    int main() {
      scanf("%s", c);
      n = strlen(c);
      scanf("%d", &m);
      for (int i = 1; i <= m; ++i) scanf("%s", s), insert();
      build();
      f[0][0][1] = 1;
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= tot; ++j) {
          if (ed[j]) continue;
          for (int k = 0; k < 10; ++k) {
            if (ed[ch[j][k]]) continue;
            add(f[i + 1][ch[j][k]][0], f[i][j][0]);
            if (k < c[i] - '0') add(f[i + 1][ch[j][k]][0], f[i][j][1]);
            if (k == c[i] - '0') add(f[i + 1][ch[j][k]][1], f[i][j][1]);
          }
        }
      }
      for (int j = 0; j <= tot; ++j) {
        if (ed[j]) continue;
        add(ans, f[n][j][0]);
        add(ans, f[n][j][1]);
      }
      printf("%lld\n", ans - 1);
      return 0;
    }
    ```

This problem is very helpful for understanding the principle of digit DP.

## Exercises

[Ahoi2009 self Same-Class Distribution](https://www.luogu.com.cn/problem/P4127)

[Luogu P3413 SAC#1 - Cute Numbers](https://www.luogu.com.cn/problem/P3413)

[HDU 6148 Valley Number](https://acm.hdu.edu.cn/showproblem.php?pid=6148)

[CF55D Beautiful numbers](http://codeforces.com/problemset/problem/55/D)

[CF628D Magic Numbers](http://codeforces.com/problemset/problem/628/D)
