---
title: Mo's algorithm on trees
---

## Mo's algorithm on trees via the bracket sequence

Ordinary Mo's algorithm can only handle linear problems, so we have to forcibly flatten the tree into a sequence.

We can compute the bracket sequence of the tree, split the bracket sequence into blocks and run Mo's algorithm on it.

How exactly do we do that?

### Process

We build the bracket sequence of the tree with a DFS (when entering node $x$ we append $x$ to the sequence, and when leaving node $x$ we append $x$ to the sequence again; the total length of the sequence is $2N$).

Let $st_x$ be the time we enter $x$ and $ed_x$ the time we leave $x$.

By the properties of the bracket sequence, for a tree path $u \to v$ (without loss of generality assume $st_u \le st_v$):

-   If $\text{LCA}(u, v) = u$, the nodes on the path appear exactly once in the interval $[st_u, st_v]$, while nodes not on the path appear 0 or 2 times.
-   If $\text{LCA}(u, v) \neq u$, the nodes on the path other than $\text{LCA}(u, v)$ appear exactly once in the interval $[ed_u, st_v]$, while nodes not on the path appear 0 or 2 times. Note that $\text{LCA}(u, v)$ needs special consideration: it appears 0 times.

Therefore, while running Mo's algorithm, no matter whether the node we encounter is being pushed or popped, what essentially happens is that the number of occurrences of that node in the current interval changes. We only need to maintain how many times each node $x$ has appeared: nodes with 0 or 2 occurrences are not in the node set of the path we currently maintain, and nodes with 1 occurrence are. Hence, when the pointers of Mo's algorithm reach $[st_u, st_v]$, we have almost exactly the node set of the tree path $u \to v$.

In an actual implementation we can maintain the number of occurrences of each node $x$ modulo 2, which indicates whether node $x$ is present or not. Then, when moving the pointers, every update, whether an insertion or a deletion, amounts to flipping the presence state of that node $x$.

Note that when handling a query with $\text{LCA} \neq u$, after the pointers of Mo's algorithm have moved into place we must temporarily add $\text{LCA}(u, v)$ to the set by hand (flip its state), compute and record the answer to this query, and then remove $\text{LCA}(u, v)$ from the set again (flip it once more), so that it does not interfere with the subsequent pointer moves.

### Example problem

???+ note "Example problem [「WC2013」糖果公园 (Candy Park)](https://uoj.ac/problem/58)"
    Statement: you are given a tree in which the $i$-th node has color $c_i$; each query gives a path $u_i$, $v_i$ and asks, for this path, for
    
    $\sum_{c}val_c\sum_{i=1}^{cnt_c}w_i$
    
    where $val$ is the value of the color, $cnt$ is the number of occurrences of the color, and $w$ is the value the color yields when it appears for the $i$-th time.

#### Process

First turn the tree into a sequence; then, every time a node is added/removed, its contribution to the answer can be obtained in $O(1)$ time, namely $val_c\times w_{cnt_{c+1}}$.

We notice that this also sweeps over the subtree of the starting node, producing extra contributions. What can we do?

Since the nodes in the subtree of the starting node are certainly swept twice during the process, their contribution is 0.

So we can keep an array $vis$, and every time we sweep over a node x we XOR $vis_x$ with 1.

If $vis_x=0$, the contribution of this node can be ignored.

Hence the problem can be solved with Mo's algorithm on trees.

For modifications, just add a time dimension, turning it into Mo's algorithm on trees with updates.

Then, since the covered interval may not contain the LCA, in that case the extra contribution has to be removed, and that is all.

#### Implementation

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cmath>
    #include <cstdio>
    using namespace std;
    
    constexpr int MAXN = 200010;
    
    int f[MAXN], g[MAXN], id[MAXN], head[MAXN], cnt, last[MAXN], dep[MAXN],
        fa[MAXN][22], v[MAXN], w[MAXN];
    int block, index, n, m, q;
    int pos[MAXN], col[MAXN], app[MAXN];
    bool vis[MAXN];
    long long ans[MAXN], cur;
    
    struct edge {
      int to, nxt;
    } e[MAXN];
    
    int cnt1 = 0, cnt2 = 0;  // timestamps
    
    struct query {
      int l, r, t, id;
    
      bool operator<(const query &b) const {
        return (pos[l] < pos[b.l]) || (pos[l] == pos[b.l] && pos[r] < pos[b.r]) ||
               (pos[l] == pos[b.l] && pos[r] == pos[b.r] && t < b.t);
      }
    } a[MAXN], b[MAXN];
    
    void addedge(int x, int y) {
      e[++cnt] = edge{y, head[x]};
      head[x] = cnt;
    }
    
    void dfs(int x) {
      id[f[x] = ++index] = x;
      for (int i = head[x]; i; i = e[i].nxt) {
        if (e[i].to != fa[x][0]) {
          fa[e[i].to][0] = x;
          dep[e[i].to] = dep[x] + 1;
          dfs(e[i].to);
        }
      }
      id[g[x] = ++index] = x;  // bracket sequence
    }
    
    int lca(int x, int y) {
      if (dep[x] < dep[y]) swap(x, y);
      if (dep[x] != dep[y]) {  // climb to the same depth
        int dis = dep[x] - dep[y];
        for (int i = 20; i >= 0; i--)
          if (dis >= (1 << i)) dis -= 1 << i, x = fa[x][i];
      }
      if (x == y) return x;
      for (int i = 20; i >= 0; i--) {
        if (fa[x][i] != fa[y][i]) x = fa[x][i], y = fa[y][i];
      }
      return fa[x][0];
    }
    
    void add(int x) {
      if (vis[x])
        cur -= (long long)v[col[x]] * w[app[col[x]]--];
      else
        cur += (long long)v[col[x]] * w[++app[col[x]]];
      vis[x] ^= 1;
    }
    
    // move along the time dimension
    void modify(int x, int t) {
      if (vis[x]) {
        add(x);
        col[x] = t;
        add(x);
      } else
        col[x] = t;
    }
    
    int main() {
      scanf("%d%d%d", &n, &m, &q);
      for (int i = 1; i <= m; i++) scanf("%d", &v[i]);
      for (int i = 1; i <= n; i++) scanf("%d", &w[i]);
      for (int i = 1; i < n; i++) {
        int x, y;
        scanf("%d%d", &x, &y);
        addedge(x, y);
        addedge(y, x);
      }
      for (int i = 1; i <= n; i++) {
        scanf("%d", &last[i]);
        col[i] = last[i];
      }
      dfs(1);
      for (int j = 1; j <= 20; j++)
        for (int i = 1; i <= n; i++)
          fa[i][j] = fa[fa[i][j - 1]][j - 1];  // precompute ancestors
      int block = pow(index, 2.0 / 3);
      for (int i = 1; i <= index; i++) {
        pos[i] = (i - 1) / block;
      }
      while (q--) {
        int opt, x, y;
        scanf("%d%d%d", &opt, &x, &y);
        if (opt == 0) {
          b[++cnt2].l = x;
          b[cnt2].r = last[x];
          last[x] = b[cnt2].t = y;
        } else {
          if (f[x] > f[y]) swap(x, y);
          a[++cnt1] = query{lca(x, y) == x ? f[x] : g[x], f[y], cnt2, cnt1};
        }
      }
      sort(a + 1, a + cnt1 + 1);
      int L, R, T;  // pointer positions
      L = R = 0;
      T = 1;
      for (int i = 1; i <= cnt1; i++) {
        while (T <= a[i].t) {
          modify(b[T].l, b[T].t);
          T++;
        }
        while (T > a[i].t) {
          modify(b[T].l, b[T].r);
          T--;
        }
        while (L > a[i].l) {
          L--;
          add(id[L]);
        }
        while (L < a[i].l) {
          add(id[L]);
          L++;
        }
        while (R > a[i].r) {
          add(id[R]);
          R--;
        }
        while (R < a[i].r) {
          R++;
          add(id[R]);
        }
        int x = id[L], y = id[R];
        int llca = lca(x, y);
        if (x != llca && y != llca) {
          add(llca);
          ans[a[i].id] = cur;
          add(llca);
        } else
          ans[a[i].id] = cur;
      }
      for (int i = 1; i <= cnt1; i++) {
        printf("%lld\n", ans[i]);
      }
      return 0;
    }
    ```

## The real Mo's algorithm on trees

The Mo's algorithm on trees above merely turns the tree into a chain; what follows is the real Mo's algorithm on trees.

Since problems related to Mo's algorithm are all template problems, the implementation part is not explained in much detail.

### Sorting the queries

First, we know that Mo's algorithm is based on block decomposition, so we need to find a way of splitting a tree into blocks that guarantees the time complexity.

Conditions:

-   the distance between nodes belonging to the same block does not exceed the given block size;
-   each block contains neither too many nor too few nodes;
-   every node must belong to some block;
-   the distance between blocks with adjacent indices must not be too large.

Having understood these conditions, let us look at this problem: [「SCOI2005」王室联邦 (Royal Federation)](https://loj.ac/problem/2152).

Building on that problem, we only need to additionally guarantee the last condition to solve the block decomposition problem.

??? note "Idea"
    Let lim be the desired block size. First DFS the whole tree; whenever the size of a subtree exceeds lim, put those nodes into one block. It is easy to see that some nodes may remain at the root, so put them into the last block.

Method: use a stack to maintain the nodes while the current node, acting as a parent, visits its children; when the distance from the top of the stack to the parent exceeds the desired block size, pop that part of the elements and make them one block; whatever remains at the end forms a block by itself.

The final sorting method: if the timestamp of the first dimension is greater than that of the second, swap them; sort with the block of the first dimension as the first key and the timestamp of the second dimension as the second key.

### Moving the pointers

#### Process

It is easy to think of the following: we can mark the nodes counted in the answer, move the pointer straight toward its target and flip the nodes on the path along the way.

However, there is a problem: if both pointers start at x, then x is obviously marked; when both pointers move toward the same child (and in many other situations), x should not be marked, but in reality x is marked, because each of the two pointers marked it once and the two cancel out.

How do we solve this?

There is an obvious property: these nodes must be some LCAs, because only at an LCA can a repeated undo cause the undo to fail.

So we never mark the LCA while moving; we mark the LCA only when the answer to the query is needed, and then undo it.

#### Implementation

```cpp
// flip all nodes on the path except the LCA
void move(int x, int y) {
  if (dp[x] < dp[y]) swap(x, y);
  while (dp[x] > dp[y]) update(x), x = fa[x];
  while (x != y) update(x), update(y), x = fa[x], y = fa[y];
  // x!=y guarantees that the LCA is not flipped
}
```

To find the LCA we can use heavy-light decomposition (HLD); then we can put the block decomposition step into the first DFS of HLD, and the timestamps can simply be the DFS order of the second DFS.

```cpp
int bl[100002], bls = 0;  // block the node belongs to, number of blocks
unsigned step;            // block size
int fa[100002], dp[100002], hs[100002] = {0}, sz[100002] = {0};
// parent, depth, heavy child, size
stack<int> sta;

void dfs1(int x) {
  sz[x] = 1;
  unsigned ss = sta.size();
  for (int i = head[x]; i; i = nxt[i])
    if (ver[i] != fa[x]) {
      fa[ver[i]] = x;
      dp[ver[i]] = dp[x] + 1;
      dfs1(ver[i]);
      sz[x] += sz[ver[i]];
      if (sz[ver[i]] > sz[hs[x]]) hs[x] = ver[i];
      if (sta.size() - ss >= step) {
        bls++;
        while (sta.size() != ss) bl[sta.top()] = bls, sta.pop();
      }
    }
  sta.push(x);
}

// main
if (!sta.empty()) {
  bls++;  // this line is optional
  while (!sta.empty()) bl[sta.top()] = bls, sta.pop();
}
```

### Time complexity

Here comes the key point: it concerns the choice of the block size.

Let the block size be $unit$:

-   For the pointer x: since the distance between nodes within a block is about $unit$, in each block the pointer x moves $unit^2$ times ($unit\times dis_{\max}$), for a total of $n\times unit$ times ($unit^2 \times (\frac{n}{unit})$);
-   For the pointer y: in each block it moves at most $O(n)$ times, for a total of $\frac{n^2}{unit}$ times ($n \times (\frac{n}{unit})$).

The sum attains its minimum roughly at the square root (since the block size of Mo's algorithm on trees is not fixed, this need not be followed strictly).

### Example problem 「WC2013」糖果公园

Because of the extra time dimension, a block size of about $n^{0.6}$ is good enough.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cmath>
    #include <cstdio>
    #include <stack>
    using namespace std;
    
    int gi() {
      int x, c, op = 1;
      while (c = getchar(), c < '0' || c > '9')
        if (c == '-') op = -op;
      x = c ^ 48;
      while (c = getchar(), c >= '0' && c <= '9')
        x = (x << 3) + (x << 1) + (c ^ 48);
      return x * op;
    }
    
    int head[100002], nxt[200004], ver[200004], tot = 0;
    
    void add(int x, int y) {
      ver[++tot] = y, nxt[tot] = head[x], head[x] = tot;
      ver[++tot] = x, nxt[tot] = head[y], head[y] = tot;
    }
    
    int bl[100002], bls = 0;
    unsigned step;
    int fa[100002], dp[100002], hs[100002] = {0}, sz[100002] = {0}, top[100002],
                                id[100002];
    stack<int> sta;
    
    void dfs1(int x) {
      sz[x] = 1;
      unsigned ss = sta.size();
      for (int i = head[x]; i; i = nxt[i])
        if (ver[i] != fa[x]) {
          fa[ver[i]] = x, dp[ver[i]] = dp[x] + 1;
          dfs1(ver[i]);
          sz[x] += sz[ver[i]];
          if (sz[ver[i]] > sz[hs[x]]) hs[x] = ver[i];
          if (sta.size() - ss >= step) {
            bls++;
            while (sta.size() != ss) bl[sta.top()] = bls, sta.pop();
          }
        }
      sta.push(x);
    }
    
    int cnt = 0;
    
    void dfs2(int x, int hf) {
      top[x] = hf, id[x] = ++cnt;
      if (!hs[x]) return;
      dfs2(hs[x], hf);
      for (int i = head[x]; i; i = nxt[i])
        if (ver[i] != fa[x] && ver[i] != hs[x]) dfs2(ver[i], ver[i]);
    }
    
    int lca(int x, int y) {
      while (top[x] != top[y]) {
        if (dp[top[x]] < dp[top[y]]) swap(x, y);
        x = fa[top[x]];
      }
      return dp[x] < dp[y] ? x : y;
    }
    
    struct qu {
      int x, y, t, id;
    
      bool operator<(const qu a) const {
        return bl[x] == bl[a.x] ? (bl[y] == bl[a.y] ? t < a.t : bl[y] < bl[a.y])
                                : bl[x] < bl[a.x];
      }
    } q[100001];
    
    int qs = 0;
    
    struct ch {
      int x, y, b;
    } upd[100001];
    
    int ups = 0;
    long long ans[100001];
    int b[100001] = {0};
    int a[100001];
    long long w[100001];
    long long v[100001];
    long long now = 0;
    bool vis[100001] = {false};
    
    void back(int t) {
      if (vis[upd[t].x]) {
        now -= w[b[upd[t].y]--] * v[upd[t].y];
        now += w[++b[upd[t].b]] * v[upd[t].b];
      }
      a[upd[t].x] = upd[t].b;
    }
    
    void change(int t) {
      if (vis[upd[t].x]) {
        now -= w[b[upd[t].b]--] * v[upd[t].b];
        now += w[++b[upd[t].y]] * v[upd[t].y];
      }
      a[upd[t].x] = upd[t].y;
    }
    
    void update(int x) {
      if (vis[x])
        now -= w[b[a[x]]--] * v[a[x]];
      else
        now += w[++b[a[x]]] * v[a[x]];
      vis[x] ^= 1;
    }
    
    void move(int x, int y) {
      if (dp[x] < dp[y]) swap(x, y);
      while (dp[x] > dp[y]) update(x), x = fa[x];
      while (x != y) update(x), update(y), x = fa[x], y = fa[y];
    }
    
    int main() {
      int n = gi(), m = gi(), k = gi();
      step = (int)pow(n, 0.6);
      for (int i = 1; i <= m; i++) v[i] = gi();
      for (int i = 1; i <= n; i++) w[i] = gi();
      for (int i = 1; i < n; i++) add(gi(), gi());
      for (int i = 1; i <= n; i++) a[i] = gi();
      for (int i = 1; i <= k; i++)
        if (gi())
          q[++qs].x = gi(), q[qs].y = gi(), q[qs].t = ups, q[qs].id = qs;
        else
          upd[++ups].x = gi(), upd[ups].y = gi();
      for (int i = 1; i <= ups; i++) upd[i].b = a[upd[i].x], a[upd[i].x] = upd[i].y;
      for (int i = ups; i; i--) back(i);
      fa[1] = 1;
      dfs1(1), dfs2(1, 1);
      if (!sta.empty()) {
        bls++;
        while (!sta.empty()) bl[sta.top()] = bls, sta.pop();
      }
      for (int i = 1; i <= n; i++)
        if (id[q[i].x] > id[q[i].y]) swap(q[i].x, q[i].y);
      sort(q + 1, q + qs + 1);
      int x = 1, y = 1, t = 0;
      for (int i = 1; i <= qs; i++) {
        if (x != q[i].x) move(x, q[i].x), x = q[i].x;
        if (y != q[i].y) move(y, q[i].y), y = q[i].y;
        int f = lca(x, y);
        update(f);
        while (t < q[i].t) change(++t);
        while (t > q[i].t) back(t--);
        ans[q[i].id] = now;
        update(f);
      }
      for (int i = 1; i <= qs; i++) printf("%lld\n", ans[i]);
      return 0;
    }
    ```
