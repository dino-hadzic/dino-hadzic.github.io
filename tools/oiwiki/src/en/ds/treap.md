---
title: Treap
---

Prerequisites: [plain binary search tree](./bst.md), [heap basics](./heap.md).

## Introduction

A Treap (tree + heap) is a **weakly balanced** **binary search tree**.

Besides the maintained **value** ($\textit{val}$), each node of a Treap also carries an additional random **priority** ($\textit{priority}$). The values satisfy the binary search tree property, and the priorities satisfy the heap property (min-heap or max-heap).

Here, the binary search tree property means:

-   The values ($\textit{val}$) of all nodes in the left subtree are smaller than that of the parent.
-   The values ($\textit{val}$) of all nodes in the right subtree are larger than that of the parent.

The heap property is:

-   The priority ($\textit{priority}$) of a child is larger or smaller than that of the parent (depending on whether it is a min-heap or a max-heap).

It is not hard to see that if the same value were used, the combination of these two data structures would degenerate into a chain, so on top of the search tree we introduce another value for the heap, $\textit{priority}$. For the $\textit{val}$ values we maintain the search tree property, and for the $\textit{priority}$ values we maintain the heap property. The value $\textit{priority}$ is assigned randomly.

The figure below is an example of a Treap (a min-heap is used here, i.e. the root has the smallest priority).

![An example of a Treap](./images/treap-treap-example.svg)

So why do we go to such lengths to make this data structure satisfy both the tree and heap properties, and assign the heap values randomly?

To understand this, one first needs to understand the problem with the plain binary search tree. When inserting a new node into a plain search tree, we recurse starting from the root of the tree; if the new node is smaller than the current node, we recurse to the left, and vice versa.

Finally, when we find that the current node has no child, the new node becomes the left or right child of the current node depending on its value.

If the values of the inserted nodes are random (in other words, they are inserted in random order), the height of this plain search tree is small (close to $\log n$, where $n$ is the number of nodes), and the number of nodes on each level is large, i.e. its shape is very "fat". The Treap in the figure above is an example. Hence, in this case, the complexity of any operation is about $O(\log n)$.

However, this is only the complexity in the random case; if we insert nodes into a plain search tree in the following very ordered sequence:

```plain
1 2 3 4 5
```

then the tree degenerates into a chain, i.e. it becomes very "thin and long" (every inserted node is larger than the previous ones, so all of them are placed as right children):

![Example of degeneration into a chain](./images/treap-search-tree-chain.svg)

It is not hard to see that the query complexity has also gone from $O(\log n)$ to $O(n)$.

To solve this problem and reach a relatively "balanced" state, the Treap maintains random priorities satisfying the heap property, thereby "shuffling" the insertion order of the nodes, so that the binary search tree reaches the ideal complexity and avoids the problem of degenerating into a chain.

## Proof of Treap complexity

Since the complexity of every Treap operation depends on the depth of the node being operated on, we first prove that the expected depth of every node is $O(\log n)$.

### Notation

For convenience, we agree on the following:

-   $n$ is the number of nodes.
-   In a Treap node, the quantity satisfying the binary search tree property is called the **value**, and the one satisfying the heap property (i.e. the random one) is called the **priority**. Without loss of generality, assume the priorities satisfy the min-heap property.
-   $x_k$ denotes the node with the $k$-th smallest value.
-   $X_{i,j}$ denotes the set $\{x_i,x_{i+1},\cdots,x_{j-1},x_j\}$, i.e. the set of nodes from the $i$-th to the $j$-th after sorting by value in ascending order.
-   $\operatorname{dep}(x)$ denotes the depth of node $x$. The depth of the root is defined to be $0$.
-   $Y_{i,j}$ is an indicator random variable that is $1$ when $x_i$ is an ancestor of $x_j$, and $0$ otherwise. In particular, $Y_{i,i}=0$.
-   $\Pr(A)$ denotes the probability that event $A$ occurs.

### Proof of the expected node depth

Since the depth of node $x_i$ equals the number of its ancestors, we have

$$
\operatorname{dep}(x_i)=\sum_{k=1}^nY_{k,i}.
$$

Then, by linearity of expectation,

$$
E(\operatorname{dep}(x_i))=E\left(\sum_{k=1}^nY_{k,i}\right)=\sum_{k=1}^nE(Y_{k,i}).
$$

Since $Y_{k,i}$ is an indicator random variable, its expectation equals the probability that it is $1$, so

$$
E(\operatorname{dep}(x_i))=\sum_{k=1}^n\Pr(Y_{k,i}=1).
$$

We first prove a lemma: $Y_{i,j}=1$ if and only if the priority of $x_i$ is the smallest in $X_{i,j}$.

??? note "Proof of the lemma"
    Consider the cases for $x_i$ and $x_j$.
    
    1.  If $x_i$ is the root: since the priorities satisfy the min-heap property, $x_i$ has the smallest priority, and for any $x_j$, $x_i$ is an ancestor of $x_j$.
    2.  If $x_j$ is the root: likewise, $x_j$ has the smallest priority, so $x_i$ is not the node with the smallest priority in $X_{i,j}$; at the same time, $x_i$ is not an ancestor of $x_j$.
    3.  If $x_i$ and $x_j$ are in the two different subtrees of the root (one left, one right), then the root $r\in X_{i,j}$. Therefore the priority of $x_i$ cannot be the smallest in $X_{i,j}$ (because the root's is smaller). At the same time, since $x_i$ and $x_j$ belong to two different subtrees, $x_i$ is not an ancestor of $x_j$.
    4.  If $x_i$ and $x_j$ are in the same subtree of the root, this subtree can be taken out as a new Treap on its own, and the above proof applied recursively.

By the lemma, the expected depth can be rewritten as

$$
E(\operatorname{dep}(x_i))=\sum_{k=1}^n\Pr(x_k=\min X_{i,k}\land k\neq i).
$$

Also, since the priorities of the nodes are random, we assume that every node in the set $X_{i,j}$ has the same probability of having the smallest priority, so

$$
\begin{aligned}
E(\operatorname{dep}(x_i))&=\sum_{k=1}^n\Pr(x_k=\min X_{i,k}\land k\neq i)\\
&=\sum_{k=1}^{n}\Pr(x_k=\min X_{i,k})-1\\
&=\sum_{k=1}^n\dfrac{1}{|i-k|+1}-1\\
&=\sum_{k=1}^{i-1}\dfrac{1}{i-k+1}+\sum_{k=i+1}^n\dfrac{1}{k-i+1}\\
&=\sum_{j=2}^i\dfrac 1j+\sum_{j=2}^{n-i+1}\dfrac 1j\\
&\le 2\sum_{j=2}^n\dfrac 1j < 2\sum_{j=2}^n\int_{j-1}^j\dfrac 1x\mathrm dx\\
&=2\int_1^n\dfrac 1x\mathrm dx=2\ln n=O(\log n).
\end{aligned}
$$

Therefore, the expected depth of every node is $O(\log n)$.

Since the complexity of the operations of a plain binary search tree is $O(h)$, and the complexity of maintaining the heap property in a Treap is also $O(h)$, the expected complexity of every Treap operation is $O(\log n)$.

???+ note "Intuitive understanding of the expected complexity"
    First, we need to realize that the $\textit{priority}$ attribute of a node is directly related to the level it is on. Recall the heap property:
    
    -   The value ($\textit{priority}$) of a child is larger or smaller than that of the parent (depending on whether it is a min-heap or a max-heap)
    
    We find that nodes on low levels, such as the root of the whole tree, also have a smaller $\textit{priority}$ attribute (in a min-heap). Moreover, in a plain search tree, nodes inserted earlier are also more likely to have a smaller level. We can understand the $\textit{priority}$ attribute by relating it to the insertion order; this also explains why a Treap can shuffle the insertion order of nodes via $\textit{priority}$.

When inserting a new node into a Treap, both the tree property and the heap property must be maintained. The search tree property can be maintained during insertion, while there are two approaches to maintaining the heap property: rotation, and split and merge. Treaps using these two approaches are called **rotating Treaps** and **non-rotating Treaps** respectively.

## Rotating Treap

The **rotating Treap** maintains balance by rotations, similar to the rotation operations of the AVL tree, divided into **left rotation** and **right rotation**. That is, while satisfying the binary search tree condition, the Treap is balanced according to the heap priorities.

When solving ordinary balanced tree problems, the rotating Treap has one of the smaller constant factors among all balanced trees.

The code in the explanation below implements the rotating Treap with pointers; a complete array implementation is attached at the end of the article.

???+ info "Info"
    `rank` in the code stands for the priority discussed above (the $\textit{priority}$ attribute), which satisfies the min-heap property.

### Node structure

```cpp
struct Node {
  Node *ch[2];  // addresses of the two children
  int val, rank;
  int rep_cnt;  // how many times the current value (val) occurs
  int siz;      // size of the subtree rooted at the current node

  Node(int val) : val(val), rep_cnt(1), siz(1) {
    ch[0] = ch[1] = nullptr;
    rank = rand();
    // note that at initialization, rank is given randomly
  }

  void upd_siz() {
    // used to recompute siz after rotations and deletions
    siz = rep_cnt;
    if (ch[0] != nullptr) siz += ch[0]->siz;
    if (ch[1] != nullptr) siz += ch[1]->siz;
  }
};
```

### Rotation

Rotation is a very important operation of the Treap; it is mainly used to adjust the levels of different nodes while keeping the tree property, so as to maintain the heap property.

The left and right rotations may not be particularly easy to tell apart; here are two fairly clear characteristics:

The meaning of a rotation:

-   Without affecting the search tree property, the subtree on the side opposite to the rotation direction becomes the root (e.g. a left rotation turns the right subtree into the root)
-   The property is not affected, and after the rotation, the child on the same side as the rotation direction becomes the former root (e.g. for a left rotation, the left child after rotation is the root before rotation)

The left and right rotations are inverses of each other, as shown in the figure below.

![Rotation](./images/treap-rotate.svg)

```cpp
enum rot_type { LF = 1, RT = 0 };

void _rotate(Node *&cur,
             rot_type dir) {  // the dir parameter is the rotation direction: 0 for right rotation, 1 for left rotation
  // note that the cur passed in is a reference to a pointer, i.e. modifying this
  // cur modifies the variable along with it; if this cur is a child of some other tree, when
  // reached via ch we also arrive here

  // the code below is explained for the case of a left rotation
  Node *tmp = cur->ch[dir];  // let C become the root;
                             // tmp here
                             // is a temporary node pointer pointing to the node that becomes the new root

  /* left rotation: let the right child become the root
   *         A                 C
   *        / \               / \
   *       B  C    ---->     A   E
   *         / \            / \
   *        D   E          B   D
   */
  cur->ch[dir] = tmp->ch[!dir];    // let the right child of A become D
  tmp->ch[!dir] = cur;             // let the left child of C become A
  cur->upd_siz(), tmp->upd_siz();  // update the size information
  cur = tmp;  // finally assign the variable temporarily holding tree C to the current root (note that cur is a reference)
}
```

### Insertion

Similar to insertion in a plain binary search tree, but during insertion the heap property of the priorities must be maintained by rotations.

```cpp
void _insert(Node *&cur, int val) {
  if (cur == nullptr) {
    // no such node, so simply create a new one
    cur = new Node(val);
    return;
  } else if (val == cur->val) {
    // if there is a node with the same value, increase the repetition count by one
    cur->rep_cnt++;
    cur->siz++;
  } else if (val < cur->val) {
    // maintain the search tree property: if val is smaller than the current node, insert on the left, and vice versa
    _insert(cur->ch[0], val);
    if (cur->ch[0]->rank < cur->rank) {
      // in a min-heap, the node above must have the smaller priority
      // since the newly inserted left child is smaller than the parent, the left child now needs to become the parent
      _rotate(cur, RT);  // note the rotation property above: to bring the left child up, a right rotation is needed
    }
    cur->upd_siz();  // the size changes after insertion and needs to be updated
  } else {
    _insert(cur->ch[1], val);
    if (cur->ch[1]->rank < cur->rank) {
      _rotate(cur, LF);
    }
    cur->upd_siz();
  }
}
```

### Deletion

This is mainly a case analysis; different situations are handled differently, and after deletion the size of the tree changes, so remember to update it. Also, if the node to be deleted has both a left and a right subtree, we need to consider who becomes the parent after deletion (keeping the node with the smaller rank on top).

```cpp
void _del(Node *&cur, int val) {
  if (val > cur->val) {
    _del(cur->ch[1], val);
    // a larger value is in the right subtree, and vice versa
    cur->upd_siz();
  } else if (val < cur->val) {
    _del(cur->ch[0], val);
    cur->upd_siz();
  } else {
    if (cur->rep_cnt > 1) {
      // if the node to be deleted is repeated, simply decrease the repetition count
      cur->rep_cnt--, cur->siz--;
      return;
    }
    uint8_t state = 0;
    state |= (cur->ch[0] != nullptr);
    state |= ((cur->ch[1] != nullptr) << 1);
    // 00 neither, 01 left only, 10 right only, 11 both
    Node *tmp = cur;
    switch (state) {
      case 0:
        delete cur;
        cur = nullptr;
        // no children at all, so simply delete this node
        break;
      case 1:  // left only
        cur = tmp->ch[0];
        // make the root the left child, then delete the original root; note that tmp here is
        // copied from cur, while cur is a reference
        delete tmp;
        break;
      case 2:  // right only
        cur = tmp->ch[1];
        delete tmp;
        break;
      case 3:
        rot_type dir = cur->ch[0]->rank < cur->ch[1]->rank
                           ? RT
                           : LF;  // dir is the child with the smaller rank
        _rotate(cur, dir);  // this rotation brings the child with the smaller priority up; rt is 0
                            // and lf is 1, exactly the opposite of the actual subtree indices
        _del(
            cur->ch[!dir],
            val);  // after the rotation, the original root is on the side of the rotation direction, so
                   // we need to continue and delete this original root
                   // if the node to be deleted is in the "upper layers" of the whole tree, we keep rotating it down
                   // with this rotation until it has no subtrees (or only one), and then delete it.
        cur->upd_siz();
        // deletion changes the size
        break;
    }
  }
}
```

### Querying the rank by value

Meaning of the operation: in the subtree rooted at cur, query the rank of the value val (the number of nodes in that subtree smaller than val + 1)

```cpp
int _query_rank(Node *cur, int val) {
  int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
  // the number of nodes in this tree smaller than val
  if (val == cur->val)
    // if this node is exactly the one being queried
    return less_siz + 1;
  else if (val < cur->val) {
    if (cur->ch[0] != nullptr)
      return _query_rank(cur->ch[0], val);
    else
      return 1;  // if the left subtree is empty, the value is smaller than even the smallest node, so it is the smallest
  } else {
    if (cur->ch[1] != nullptr)
      // if the queried value is larger than this node, the left subtree of this node and the node itself are surely smaller than the queried value
      // so add these two quantities, plus the result of searching to the right
      // (the rank of the value val in the subtree rooted at the right child)
      return less_siz + cur->rep_cnt + _query_rank(cur->ch[1], val);
    else
      return cur->siz + 1;
    // without a right subtree, the whole tree + 1 equals less_siz + cur->rep_cnt + 1
  }
}
```

### Querying the value by rank

To query the value by rank, we first need to know how to decide which part of the tree the queried node is in:

Below is a table of the decision rule:

| Left subtree                 | Root/current node                                                              | Right subtree                                          |
| ---------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------ |
| rank ≤ size of left subtree  | rank > size of left subtree, and ≤ size of left subtree + repetition count of root | rank > size of left subtree + repetition count of root |

Note that when recursing into the right subtree, the original `rank` must be processed. The recursion amounts to querying the value with this rank in the right subtree, so to convert the rank into one relative to the right subtree, we need to subtract the size of the left subtree and the repetition count of the root from the original `rank`.

All nodes can be imagined as a sorted array, or a number line (as below),

    1 -> |nodes of the left subtree|root|nodes of the right subtree| -> n
                                                 ^
                                                 queried rank
                                           ⬇convert to a rank relative to the right subtree
    1 -> |nodes of the right subtree| -> n
           ^
           queried rank

The conversion here is simply to subtract the size of the left subtree and the repetition count of the root from the rank.

```cpp
int _query_val(Node *cur, int rank) {
  // query the value of the node with rank rank in the tree
  int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
  // less siz is the size of the left subtree
  if (rank <= less_siz)
    return _query_val(cur->ch[0], rank);
  else if (rank <= less_siz + cur->rep_cnt)
    return cur->val;
  else
    return _query_val(cur->ch[1], rank - less_siz - cur->rep_cnt);  // see above
}
```

### Finding the first node smaller than val

Note that a class-wide variable, `q_prev_tmp`, is used here.

This value is modified only when val is larger than the value of the current node, so returning this variable means returning the value from the last time val was larger than the current node's value; after that, the nodes are smaller.

```cpp
int _query_prev(Node *cur, int val) {
  if (val <= cur->val) {
    // still larger than or equal to val, so search in the left subtree
    if (cur->ch[0] != nullptr) return _query_prev(cur->ch[0], val);
  } else {
    // the value of q_prev_tmp is updated only when we get into this else
    q_prev_tmp = cur->val;
    // the current node is already smaller than val, but it is not certain that it is the largest, so continue searching in the right subtree
    if (cur->ch[1] != nullptr) _query_prev(cur->ch[1], val);
    // the following recursion may no longer modify q_prev_tmp,
    // so simply return this value; in any case, what is returned is the cur->val
    // from the last time we entered this else
    return q_prev_tmp;
  }
  return NIL;
}
```

### Finding the first node larger than val

Very similar to the previous one, only the greater-than and less-than signs are swapped.

```cpp
int _query_nex(Node *cur, int val) {
  if (val >= cur->val) {
    if (cur->ch[1] != nullptr) return _query_nex(cur->ch[1], val);
  } else {
    q_nex_tmp = cur->val;
    if (cur->ch[0] != nullptr) _query_nex(cur->ch[0], val);
    return q_nex_tmp;
  }
  return NIL;
}
```

## Non-rotating Treap

The way the non-rotating Treap operates makes it naturally suited to maintaining sequences, persistence, and similar features.

The **non-rotating Treap** is also called the split-merge Treap. It has only two core operations, namely **split** and **merge**. Through these two operations, other operations can in many cases be implemented more conveniently than with the rotating Treap. The two operations are introduced one by one below.

???+ note "Note"
    When explaining the non-rotating Treap, the **FHQ-Treap** (by Fan Haoqiang) should be mentioned, i.e. the persistent non-rotating Treap supporting range operations. For more, refer to the slides "Fan Haoqiang on Data Structures".

### Splitting (split)

#### Splitting by value

The split procedure takes two parameters: the root pointer $\textit{cur}$ and the key value $\textit{key}$. The result is that the Treap pointed to by the root pointer is split into two Treaps: the values ($\textit{val}$) of all nodes in the first Treap are less than or equal to $\textit{key}$, and the values of all nodes in the second Treap are greater than $\textit{key}$.

The procedure first checks whether $\textit{key}$ is less than the value of $\textit{cur}$; if so, then $\textit{cur}$ and its entire right subtree are greater than $\textit{key}$ and belong to the second Treap. Of course, part of the left subtree may also have values greater than $\textit{key}$, so we need to continue splitting the left subtree recursively. The part of the left subtree greater than $\textit{key}$ is made the left subtree of $\textit{cur}$; in this way, all nodes in $\textit{cur}$ are greater than $\textit{key}$.

Correspondingly, if $\textit{key}$ is greater than or equal to the value of $\textit{cur}$, then the entire left subtree of $\textit{cur}$ and $\textit{cur}$ itself are less than or equal to $\textit{key}$ and belong to the first Treap after splitting. Also, part of the right subtree of $\textit{cur}$ may also be less than or equal to $\textit{key}$, so we need to continue splitting the right subtree recursively. The part less than or equal to $\textit{key}$ is made the right subtree of $\textit{cur}$; in this way, all nodes in $\textit{cur}$ are less than or equal to $\textit{key}$.

The figure below shows splitting by value in the case where the value of $\textit{cur}$ is less than or equal to $\textit{key}$.[^ref1]

![Splitting by value](./images/treap-none-rot-split-by-val.svg)

```cpp
pair<Node *, Node *> split(Node *cur, int key) {
  if (cur == nullptr) return {nullptr, nullptr};
  if (cur->val <= key) {
    // cur and its left subtree surely belong to the first tree after splitting
    auto temp = split(cur->ch[1], key);
    // but part of its right subtree may also be smaller than key
    cur->ch[1] = temp.first;
    // we take out the part smaller than key and make it the right subtree of cur, so that the whole cur is smaller than
    // key; the remaining part of the right subtree becomes the second Treap after splitting
    cur->upd_siz();
    // the size of the tree changes after splitting and needs to be updated
    return {cur, temp.second};
  } else {
    // same as above
    auto temp = split(cur->ch[0], key);
    cur->ch[0] = temp.second;
    cur->upd_siz();
    return {temp.first, cur};
  }
}
```

#### Splitting by rank

Compared with splitting by value, this operation is more like querying the value by rank in the rotating Treap (the rank of a node is the number of nodes in the tree whose value is smaller than this node's value $+ 1$):

This function takes two parameters, the node pointer $\textit{cur}$ and the rank $\textit{rk}$, and returns the three Treaps after splitting.

In the first Treap, the rank of every node is less than $\textit{rk}$; in the second, the rank equals $\textit{rk}$, and the second Treap has only one node (there cannot be several equal ones; if there are, `cnt` in the `Node` struct is increased); and in the third, the rank is greater.

The key point of this operation is to determine which part of the tree the node whose rank equals $\textit{rk}$ is in; this is also an important part of the query-value-by-rank operation of the rotating Treap, which was explained in great detail above, so we do not elaborate here.

Also, the recursive part of this operation is very similar to splitting by value, so we do not repeat it here.

```cpp
tuple<Node *, Node *, Node *> split_by_rk(Node *cur, int rk) {
  if (cur == nullptr) return {nullptr, nullptr, nullptr};
  int ls_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
  if (rk <= ls_siz) {
    // the node whose rank equals rk is in the left subtree
    Node *l, *mid, *r;
    tie(l, mid, r) = split_by_rk(cur->ch[0], rk);
    cur->ch[0] = r;  // the ranks in the returned third Treap are all greater than rk
    // after the left subtree of cur is set to r, the ranks of all nodes in cur are greater than rk
    cur->upd_siz();
    return {l, mid, cur};
  } else if (rk <= ls_siz + cur->cnt) {
    // the node whose rank equals rk is the current node
    Node *lt = cur->ch[0];
    Node *rt = cur->ch[1];
    cur->ch[0] = cur->ch[1] = nullptr;
    // the second Treap after splitting has only one node, so its subtrees must be set to empty
    return {lt, cur, rt};
  } else {
    // the node whose rank equals rk is in the right subtree
    // the recursion is the same as above
    Node *l, *mid, *r;
    tie(l, mid, r) = split_by_rk(cur->ch[1], rk - ls_siz - cur->cnt);
    cur->ch[1] = l;
    cur->upd_siz();
    return {cur, mid, r};
  }
}
```

### Merging (merge)

The merge procedure takes two parameters: the root pointer $\textit{u}$ of the left Treap and the root pointer $\textit{v}$ of the right Treap. It must hold that the values of all nodes in $\textit{u}$ are less than or equal to the values of all nodes in $\textit{v}$. Generally, the two Treaps we merge were originally split from one Treap, so it is not hard to satisfy that the values of all nodes in $\textit{u}$ are smaller than those in $\textit{v}$

In the rotating Treap, we rely on rotations to keep $\textit{priority}$ consistent with the heap property, while rotations must not change the tree property. In the non-rotating Treap, we use merging to achieve the same effect.

Since the two Treaps are already ordered, when merging we only need to consider which tree to "put on top" and which to "put below", i.e. decide which tree becomes the subtree. Obviously, by the heap property, we need to put the one with the smaller $\textit{priority}$ on top (a min-heap is used here).

At the same time, we also need to satisfy the search tree property, so if the $\textit{priority}$ of the root of $\textit{u}$ is smaller than that of $\textit{v}$, then $\textit{u}$ is the new root, and $\textit{v}$, whose values are larger than $\textit{u}$, should be merged with the right subtree of $\textit{u}$; otherwise, $\textit{v}$ is the new root, and since the values of $u$ are smaller than $\textit{v}$, $u$ is merged with the left subtree of $v$.

```cpp
Node *merge(Node *u, Node *v) {
  // the two trees passed in already satisfy the search tree property internally
  // and the values of all nodes in u < the values of all nodes in v
  // so when merging, the heap property needs to be maintained
  // a min-heap is used here
  if (u == nullptr && v == nullptr) return nullptr;
  if (u != nullptr && v == nullptr) return u;
  if (v != nullptr && u == nullptr) return v;

  if (u->prio < v->prio) {
    // the prio of u is smaller, so u should be the parent
    u->ch[1] = merge(u->ch[1], v);
    // since v is larger than u, make v the right subtree of u
    u->upd_siz();
    return u;
  } else {
    // v is smaller, so v should be the parent
    v->ch[0] = merge(u, v->ch[0]);
    // u is smaller than v, hence the arguments of the recursion are like this
    v->upd_siz();
    return v;
  }
}
```

### Insertion

In the non-rotating Treap, basic operations such as insertion, deletion, and querying the rank by value can be implemented either with the methods of an ordinary binary search tree or with split and merge. Generally, the implementation with split and merge is more concise, but a bit slower[^ref2]. To help understand the non-rotating Treap better, all operations below are implemented with split and merge.

When implementing the insertion operation, we make use of some properties of the split operation. Namely, nodes with values less than or equal to $\textit{val}$ are placed in the first Treap.

So suppose we split the current Treap by $\textit{val}$. We get the following two trees, satisfying the conditions:

$$
\begin{aligned}
T_1 &\le val\\
T_2 &> val
\end{aligned}
$$

where $T_1$ denotes the set of all nodes placed in the first Treap after splitting, and $T_2$ the second.

If we further split $T_1$ by $\textit{val} - 1$, the following two trees arise, satisfying the conditions:

$$
\begin{gathered}
T_{1\ \text{left}} \le val - 1\\
T_{1\ \text{right}} > val - 1 \ \And \ T_{1\ \text{right}} \le val
\end{gathered}
$$

where $T_{1\ \text{left}}$ denotes the set of all nodes placed in the first Treap after splitting $T_1$, and $T_{1\ \text{right}}$ the second. In the formula above, the latter part $\And \ T_{1\ \text{right}} \le val$ comes from the condition $T_1 \le val$ that $T_1$ satisfies.

It is not hard to see that, as long as $\textit{val}$ and the node values are integers (integers are used in most scenarios), there is only one node satisfying the condition of $T_{1\ \text{right}}$, namely the node whose value equals $\textit{val}$.

During insertion, if we find that the node satisfying $T_{1\ \text{right}}$ exists, we can simply increase the repetition count; otherwise, we create a new node.

Note that after splitting the tree, we still need to "glue" it back with the merge operation so that it can be used again next time. Also note that the order of the arguments of the merge operation matters: the values of all nodes of the first tree must be smaller than those of the second.

```cpp
void insert(int val) {
  auto temp = split(root, val);
  // split the whole tree into two according to the value val
  // note the implementation of split: the subtree equal to val is in the left subtree
  auto l_tr = split(temp.first, val - 1);
  // the left subtree of l_tr is <= val - 1; if there is a node = val, it must be in the right subtree
  Node *new_node;
  if (l_tr.second == nullptr) {
    // if there is no such node, create a new one; otherwise simply increase the repetition count.
    new_node = new Node(val);
  } else {
    l_tr.second->cnt++;
    l_tr.second->upd_siz();
  }
  Node *l_tr_combined =
      merge(l_tr.first, l_tr.second == nullptr ? new_node : l_tr.second);
  // merge T_1 left and T_1 right
  root = merge(l_tr_combined, temp.second);
  // merge T_1 and T_2
}
```

### Deletion

The deletion operation also uses a method similar to insertion: find the node whose value equals $\textit{val}$ and delete it.

```cpp
void del(int val) {
  auto temp = split(root, val);
  auto l_tr = split(temp.first, val - 1);
  if (l_tr.second->cnt > 1) {
    // if the repetition count of this node is greater than 1, simply decrease it
    l_tr.second->cnt--;
    l_tr.second->upd_siz();
    l_tr.first = merge(l_tr.first, l_tr.second);
  } else {
    if (temp.first == l_tr.second) {
      // it is possible that the whole T_1 consists only of this node, so this one also needs to be set to null to mark it as deleted
      temp.first = nullptr;
    }
    delete l_tr.second;
    l_tr.second = nullptr;
  }
  root = merge(l_tr.first, temp.second);
}
```

### Querying the rank by value

The rank is the number of nodes smaller than this value $+ 1$, so we split the current tree by $\textit{val} - 1$; then the first tree after splitting satisfies:

$$
T_1 \le val - 1
$$

If the values of the tree and $\textit{val}$ are integers, then $T_1$ contains all nodes whose value is smaller than $\textit{val}$.

```cpp
int qrank_by_val(Node* cur, int val) {
  auto temp = split(cur, val - 1);
  int ret = (temp.first == nullptr ? 0 : temp.first->siz) + 1;  // + 1 by definition
  root = merge(temp.first, temp.second);  // glue it back after splitting
  return ret;
}
```

### Querying the value by rank

After calling the `split_by_rk()` function, the three split Treaps are returned, of which the second contains only one node whose rank equals $\textit{rk}$, so we directly return the $\textit{val}$ of this node.

```cpp
int qval_by_rank(Node *cur, int rk) {
  Node *l, *mid, *r;
  tie(l, mid, r) = split_by_rk(cur, rk);
  int ret = mid->val;
  root = merge(merge(l, mid), r);
  return ret;
}
```

### Finding the first node smaller than val

This problem can be transformed into finding the node with the largest rank among all nodes smaller than $\textit{val}$. We split this Treap by $\textit{val}$; the values of the nodes in the returned first Treap are all smaller than $\textit{val}$, and then we call `qval_by_rank()` to find the node with the largest value in this tree.

```cpp
int qprev(int val) {
  auto temp = split(root, val - 1);
  // temp.first is the subtree with values smaller than val
  int ret = qval_by_rank(temp.first, temp.first->siz);
  // what is queried here is the value of the largest among all nodes smaller than val
  root = merge(temp.first, temp.second);
  return ret;
}
```

### Finding the first node larger than val

Similar to the previous operation, this problem can be transformed into finding the node with the smallest rank among all nodes larger than $\textit{val}$. Then, after splitting by $\textit{val}$, the values of all nodes in the returned second Treap are larger than $\textit{val}$.

Then we query the value of the node with rank $1$ in this tree (i.e. the node with the smallest value), and we successfully find the first node larger than $\textit{val}$.

```cpp
int qnex(int val) {
  auto temp = split(root, val);
  int ret = qval_by_rank(temp.second, 1);
  // query the smallest value in the subtree of all nodes larger than val
  root = merge(temp.first, temp.second);
  return ret;
}
```

### Building the tree (build)

Convert a sequence $\{a_n\}$ of $n$ nodes into a Treap.

We can insert these $n$ nodes one by one by brute force: each time a node with value $v$ is inserted, split the whole Treap by value into the part with values less than or equal to $v$ and the part with values greater than $v$, then create a new node with value $v$, and merge the two parts and the new node in order from small to large; a single insertion takes $O(\log n)$, for a total time complexity of $O(n\log n)$.

In some problems, there may be multiple operations inserting an entire sorted sequence, and then the tree must be built in $O(n)$ time.

Method one: during the recursive build, each time take the midpoint of the current interval as the root of that interval, and assign each node an appropriate priority so that the new tree satisfies the heap property. This guarantees a tree height of $O(\log n)$.

Method two: during the recursive build, each time take the midpoint of the current interval as the root of that interval, and then give each node a random priority. This guarantees a tree height of $O(\log n)$, but does not guarantee that it satisfies the heap property. This is also correct, because the priorities of the non-rotating Treap are used to make the `merge` operation a bit more random, not to guarantee the tree height.

Method three: observe that a Treap is a Cartesian tree, so the $O(n)$ construction of the Cartesian tree can be used, maintaining the right chain with a monotonic stack.

### Range operations of the non-rotating Treap

#### Building the tree

A major advantage of the non-rotating Treap over the rotating Treap is that various range operations can be implemented; below we take the [template problem](https://loj.ac/problem/105) of the artistic balanced tree as an example to introduce the range operations of the Treap.

> You need to write a data structure (see the problem title) to maintain an ordered sequence.
>
> The following operation must be supported: reverse an interval; for example, if the original ordered sequence is $5\ 4\ 3\ 2\ 1$ and the reversed interval is $[2,4]$, the result is $5\ 2\ 3\ 4\ 1$.
> For $100\%$ of the data, $1 \le n$ (initial interval length), $m$ (number of reversals) $\le 10^5$

In this problem, what we need to implement is interval reversal, so we first need to consider how to build the tree; the built tree must represent the initial interval.

We only need to insert the indices of the interval into the Treap one by one, so that an in-order traversal (first the left subtree, then the current node, finally the right subtree) yields this interval[^ref3].

We know that inserting nodes in increasing order into a plain binary search tree builds a long chain, and an in-order traversal naturally yields this interval.

<div align=center>
  <img style="width: 50%; " src="./images/treap-search-tree-chain.svg" >
</div>

As in the figure above, inserting nodes into a plain search tree in the order $1\ 2\ 3\ 4\ 5$, the in-order traversal also yields $1\ 2\ 3\ 4\ 5$.

But in a Treap, after inserting nodes in increasing order, the structure of the tree is also adjusted according to $\textit{priority}$ during merging; in such a case, how do we make sure the in-order traversal always produces the correct output?

One can refer to the [monotonic-stack construction of the Cartesian tree](./cartesian-tree.md) to understand this problem.

Let the newly inserted node be $\textit{u}$.

First, since the nodes are inserted in increasing order, every newly inserted node is surely attached to the right chain of the Treap (i.e. the chain formed by the nodes passed when going from the root into the right subtree all the way down).

Starting from the root, the $\textit{priority}$ of the nodes on the right chain is increasing (min-heap). So we can find the first node on the right chain whose $\textit{priority}$ is larger than that of $\textit{u}$; call this node $\textit{v}$, and replace this node with $\textit{u}$.

Since $\textit{u}$ is surely larger than all other nodes in the tree, we need to make $\textit{v}$ and its subtree the left subtree of $\textit{u}$. And at this point $\textit{u}$ has no right subtree.

One can see that in the in-order traversal, $\textit{u}$ is surely the last to be visited (because $\textit{u}$ is the last one in the right chain, and in an in-order traversal the right subtree is visited last).

The figure below shows the change when inserting node $5$ while inserting nodes $1 \sim 5$ into a Treap in increasing order; it can help to better understand the process of inserting in increasing order.

![Inserting a node](./images/treap-none-rot-seg-build.svg)

#### Range reversal

When reversing the interval $[l, r]$, the basic idea is to split the tree into the three intervals $[1, l - 1],\ [l, r],\ [r + 1, n]$, and then reverse the middle one $[l, r]$[^ref3].

Concretely, reversing means swapping the positions of the left and right children of every node of the subtree within the interval. The figure below shows the Treap after reversing the intervals $[3, 4]$ and $[3, 5]$ of the Treap in the figure above.

![Range reversal](./images/treap-none-rot-seg-flip-ex.svg)

Note that if we reverse in this way, then every time the interval $[l, r]$ is reversed, $r - l$ nodes are swapped; such frequent operations obviously cannot satisfy the constraint of $10^5$, and the $O(n \times \log_2 n)$ complexity of a single reversal is even worse than brute force (because, apart from spending linear time swapping nodes, we also need to spend $O(\log_2 n)$ time finding the nodes to swap in the tree).

Looking at the problem requirements again, we find that since only the final interval after all operations needs to be output, we do not actually need to swap every time. Thus, we can use the lazy tag commonly used in segment trees to optimize the complexity. When swapping, we only need to put a tag on the parent, meaning that every node in this subtree needs its left and right children swapped.

In a segment tree, we generally push the lazy tags down during updates and queries. This is because, during updates and queries, the range we want to update/query does not necessarily coincide with the range the lazy tag represents, so the tag must be pushed down first to make sure the queried and updated values are correct.

The same holds for the non-rotating Treap. Concretely, we split the Treap into the three trees mentioned above, put a lazy tag on the middle one, and then merge the three trees. Since the interval we want to reverse and the interval the lazy tag represents do not necessarily coincide, the tag must be pushed down during splitting. Also, the split and merge operations cause every node and the nodes its lazy tag represents to change, so the lazy tag must also be pushed down before merging.

In other words, when the structure of the tree changes, i.e. when we need to change the left/right child information of some node during a split or merge operation, the tag should be pushed down before that, not after, because the lazy tag needs to be passed down to the children; if the lazy tag has not been pushed down after the left/right child information is changed, the tag loses the target to be pushed to.[^ref4]

<!-- TODO: a figure could be added to explain why tags must be pushed down during split and merge -->

Below is the code explanation; the code is based on[^ref3].

Since most of the range operations are the same as in the ordinary non-rotating Treap, only the parts that differ from the ordinary non-rotating Treap are explained here.

#### Pushing down tags

Note that the lazy tag here means that every child in this tree needs to have its position swapped. So if the child of the current node also has a lazy tag, the two reversals cancel out. If the child does not need to be reversed, this lazy tag needs to be pushed further down to the child.

```cpp
// pushdown here is a member function of the Node class, where to_rev is the lazy tag
void pushdown() {
  swap(ch[0], ch[1]);
  if (ch[0] != nullptr) ch[0]->to_rev ^= 1;
  if (ch[1] != nullptr) ch[1]->to_rev ^= 1;
  to_rev = false;
}

void check_tag() {
  if (to_rev) pushdown();
}
```

#### Splitting

Note that in this problem, because of the reversal operation, $\textit{val}$ in the Treap does not satisfy the binary search tree property (see the figure in the range reversal section), so we cannot decide whether to recurse into the left or the right subtree based on $\textit{val}$.

So the split here is more similar to splitting by rank in the ordinary non-rotating Treap: whether to recurse into the left or right subtree is decided by the size of the current tree; in other words, we decide according to the position of this node in the tree at the beginning.

The ranks of the nodes in the returned first Treap are all less than or equal to $\textit{sz}$, while the ranks of the nodes in the second Treap are all greater than $\textit{sz}$.

```cpp
#define siz(_) (_ == nullptr ? 0 : _->siz)

pair<Node*, Node*> split(Node* cur, int sz) {
  // decide according to the tree size
  if (cur == nullptr) return {nullptr, nullptr};
  cur->check_tag();
  // push down first before splitting
  if (sz <= siz(cur->ch[0])) {
    auto temp = split(cur->ch[0], sz);
    cur->ch[0] = temp.second;
    cur->upd_siz();
    return {temp.first, cur};
  } else {
    auto temp =
        split(cur->ch[1],
              sz - siz(cur->ch[0]) -
                  1);  // this conversion is explained in "Querying the value by rank" of the rotating Treap
    cur->ch[1] = temp.first;
    cur->upd_siz();
    return {cur, temp.second};
  }
}
```

#### Merging

The only thing to note is pushing down the lazy tags before merging

```cpp
Node *merge(Node *sm, Node *bg) {
  // small, big
  if (sm == nullptr && bg == nullptr) return nullptr;
  if (sm != nullptr && bg == nullptr) return sm;
  if (sm == nullptr && bg != nullptr) return bg;
  sm->check_tag(), bg->check_tag();
  if (sm->prio < bg->prio) {
    sm->ch[1] = merge(sm->ch[1], bg);
    sm->upd_siz();
    return sm;
  } else {
    bg->ch[0] = merge(sm, bg->ch[0]);
    bg->upd_siz();
    return bg;
  }
}
```

#### Range reversal

As introduced above, split off the three intervals $[1, l - 1],\ [l, r],\ [r + 1, n]$, put a tag on the middle interval, and then merge.

```cpp
void seg_rev(int l, int r) {
  // less and more here are relative to l
  auto less = split(root, l - 1);
  // everything less than or equal to l - 1 will be in the left subtree of less
  auto more = split(less.second, r - l + 1);
  // the interval of the first r - l + 1 elements starting from l
  more.first->to_rev = true;
  root = merge(less.first, merge(more.first, more.second));
}
```

#### Printing by in-order traversal

Note that the tags must be pushed down when printing.

```cpp
void print(Node* cur) {
  if (cur == nullptr) return;
  cur->check_tag();
  // in-order traversal -> first the left subtree, then itself, finally the right subtree
  print(cur->ch[0]);
  cout << cur->val << " ";
  print(cur->ch[1]);
}
```

## Complete code

### Rotating Treap

#### Pointer implementation

??? note "Complete code"
    Below is the complete version of the code explained above; it is the template code for the ordinary balanced tree.
    
    ```cpp
    // author: (ttzytt)[ttzytt.com]
    #include <cstdint>
    #include <cstdio>
    #include <cstdlib>
    using namespace std;
    
    struct Node {
      Node *ch[2];
      int val, rank;
      int rep_cnt;
      int siz;
    
      Node(int val) : val(val), rep_cnt(1), siz(1) {
        ch[0] = ch[1] = nullptr;
        rank = rand();
      }
    
      void upd_siz() {
        siz = rep_cnt;
        if (ch[0] != nullptr) siz += ch[0]->siz;
        if (ch[1] != nullptr) siz += ch[1]->siz;
      }
    };
    
    class Treap {
     private:
      Node *root;
    
      constexpr static int NIL = -1;  // indicates that the queried value does not exist
    
      enum rot_type { LF = 1, RT = 0 };
    
      int q_prev_tmp = 0, q_nex_tmp = 0;
    
      void _rotate(Node *&cur, rot_type dir) {  // 0 is a right rotation, 1 a left rotation
        Node *tmp = cur->ch[dir];
        cur->ch[dir] = tmp->ch[!dir];
        tmp->ch[!dir] = cur;
        cur->upd_siz(), tmp->upd_siz();
        cur = tmp;
      }
    
      void _insert(Node *&cur, int val) {
        if (cur == nullptr) {
          cur = new Node(val);
          return;
        } else if (val == cur->val) {
          cur->rep_cnt++;
          cur->siz++;
        } else if (val < cur->val) {
          _insert(cur->ch[0], val);
          if (cur->ch[0]->rank < cur->rank) {
            _rotate(cur, RT);
          }
          cur->upd_siz();
        } else {
          _insert(cur->ch[1], val);
          if (cur->ch[1]->rank < cur->rank) {
            _rotate(cur, LF);
          }
          cur->upd_siz();
        }
      }
    
      void _del(Node *&cur, int val) {
        if (val > cur->val) {
          _del(cur->ch[1], val);
          cur->upd_siz();
        } else if (val < cur->val) {
          _del(cur->ch[0], val);
          cur->upd_siz();
        } else {
          if (cur->rep_cnt > 1) {
            cur->rep_cnt--, cur->siz--;
            return;
          }
          uint8_t state = 0;
          state |= (cur->ch[0] != nullptr);
          state |= ((cur->ch[1] != nullptr) << 1);
          // 00 neither, 01 left only, 10 right only, 11 both
          Node *tmp = cur;
          switch (state) {
            case 0:
              delete cur;
              cur = nullptr;
              break;
            case 1:  // left only
              cur = tmp->ch[0];
              delete tmp;
              break;
            case 2:  // right only
              cur = tmp->ch[1];
              delete tmp;
              break;
            case 3:
              rot_type dir = cur->ch[0]->rank < cur->ch[1]->rank ? RT : LF;
              _rotate(cur, dir);
              _del(cur->ch[!dir], val);
              cur->upd_siz();
              break;
          }
        }
      }
    
      int _query_rank(Node *cur, int val) {
        int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
        if (val == cur->val)
          return less_siz + 1;
        else if (val < cur->val) {
          if (cur->ch[0] != nullptr)
            return _query_rank(cur->ch[0], val);
          else
            return 1;
        } else {
          if (cur->ch[1] != nullptr)
            return less_siz + cur->rep_cnt + _query_rank(cur->ch[1], val);
          else
            return cur->siz + 1;
        }
      }
    
      int _query_val(Node *cur, int rank) {
        int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
        if (rank <= less_siz)
          return _query_val(cur->ch[0], rank);
        else if (rank <= less_siz + cur->rep_cnt)
          return cur->val;
        else
          return _query_val(cur->ch[1], rank - less_siz - cur->rep_cnt);
      }
    
      int _query_prev(Node *cur, int val) {
        if (val <= cur->val) {
          if (cur->ch[0] != nullptr) return _query_prev(cur->ch[0], val);
        } else {
          q_prev_tmp = cur->val;
          if (cur->ch[1] != nullptr) _query_prev(cur->ch[1], val);
          return q_prev_tmp;
        }
        return NIL;
      }
    
      int _query_nex(Node *cur, int val) {
        if (val >= cur->val) {
          if (cur->ch[1] != nullptr) return _query_nex(cur->ch[1], val);
        } else {
          q_nex_tmp = cur->val;
          if (cur->ch[0] != nullptr) _query_nex(cur->ch[0], val);
          return q_nex_tmp;
        }
        return NIL;
      }
    
     public:
      void insert(int val) { _insert(root, val); }
    
      void del(int val) { _del(root, val); }
    
      int query_rank(int val) { return _query_rank(root, val); }
    
      int query_val(int rank) { return _query_val(root, rank); }
    
      int query_prev(int val) { return _query_prev(root, val); }
    
      int query_nex(int val) { return _query_nex(root, val); }
    };
    
    Treap tr;
    
    int main() {
      srand(0);
      int t;
      scanf("%d", &t);
      while (t--) {
        int mode;
        int num;
        scanf("%d%d", &mode, &num);
        switch (mode) {
          case 1:
            tr.insert(num);
            break;
          case 2:
            tr.del(num);
            break;
          case 3:
            printf("%d\n", tr.query_rank(num));
            break;
          case 4:
            printf("%d\n", tr.query_val(num));
            break;
          case 5:
            printf("%d\n", tr.query_prev(num));
            break;
          case 6:
            printf("%d\n", tr.query_nex(num));
            break;
        }
      }
    }
    ```

#### Array implementation

Below is the bzoj ordinary balanced tree template code, implemented with arrays.

??? note "Complete code"
    ```cpp
    --8<-- "docs/ds/code/treap/treap_1.cpp"
    ```

### Non-rotating Treap

#### Pointer implementation

??? note "Complete code"
    Below is the complete version of the code explained above; it is the template code for the ordinary balanced tree.
    
    ```cpp
    
    // author: (ttzytt)[ttzytt.com]
    #include <cstdio>
    #include <cstdlib>
    #include <ctime>
    #include <tuple>
    using namespace std;
    
    struct Node {
      Node *ch[2];
      int val, prio;
      int cnt;
      int siz;
    
      Node(int _val) : val(_val), cnt(1), siz(1) {
        ch[0] = ch[1] = nullptr;
        prio = rand();
      }
    
      Node(Node *_node) {
        val = _node->val, prio = _node->prio, cnt = _node->cnt, siz = _node->siz;
      }
    
      void upd_siz() {
        siz = cnt;
        if (ch[0] != nullptr) siz += ch[0]->siz;
        if (ch[1] != nullptr) siz += ch[1]->siz;
      }
    };
    
    struct none_rot_treap {
    #define _3 second.second
    #define _2 second.first
      Node *root;
    
      pair<Node *, Node *> split(Node *cur, int key) {
        if (cur == nullptr) return {nullptr, nullptr};
        if (cur->val <= key) {
          auto temp = split(cur->ch[1], key);
          cur->ch[1] = temp.first;
          cur->upd_siz();
          return {cur, temp.second};
        } else {
          auto temp = split(cur->ch[0], key);
          cur->ch[0] = temp.second;
          cur->upd_siz();
          return {temp.first, cur};
        }
      }
    
      tuple<Node *, Node *, Node *> split_by_rk(Node *cur, int rk) {
        if (cur == nullptr) return {nullptr, nullptr, nullptr};
        int ls_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
        if (rk <= ls_siz) {
          Node *l, *mid, *r;
          tie(l, mid, r) = split_by_rk(cur->ch[0], rk);
          cur->ch[0] = r;
          cur->upd_siz();
          return {l, mid, cur};
        } else if (rk <= ls_siz + cur->cnt) {
          Node *lt = cur->ch[0];
          Node *rt = cur->ch[1];
          cur->ch[0] = cur->ch[1] = nullptr;
          return {lt, cur, rt};
        } else {
          Node *l, *mid, *r;
          tie(l, mid, r) = split_by_rk(cur->ch[1], rk - ls_siz - cur->cnt);
          cur->ch[1] = l;
          cur->upd_siz();
          return {cur, mid, r};
        }
      }
    
      Node *merge(Node *u, Node *v) {
        if (u == nullptr && v == nullptr) return nullptr;
        if (u != nullptr && v == nullptr) return u;
        if (v != nullptr && u == nullptr) return v;
        if (u->prio < v->prio) {
          u->ch[1] = merge(u->ch[1], v);
          u->upd_siz();
          return u;
        } else {
          v->ch[0] = merge(u, v->ch[0]);
          v->upd_siz();
          return v;
        }
      }
    
      void insert(int val) {
        auto temp = split(root, val);
        auto l_tr = split(temp.first, val - 1);
        Node *new_node;
        if (l_tr.second == nullptr) {
          new_node = new Node(val);
        } else {
          l_tr.second->cnt++;
          l_tr.second->upd_siz();
        }
        Node *l_tr_combined =
            merge(l_tr.first, l_tr.second == nullptr ? new_node : l_tr.second);
        root = merge(l_tr_combined, temp.second);
      }
    
      void del(int val) {
        auto temp = split(root, val);
        auto l_tr = split(temp.first, val - 1);
        if (l_tr.second->cnt > 1) {
          l_tr.second->cnt--;
          l_tr.second->upd_siz();
          l_tr.first = merge(l_tr.first, l_tr.second);
        } else {
          if (temp.first == l_tr.second) {
            temp.first = nullptr;
          }
          delete l_tr.second;
          l_tr.second = nullptr;
        }
        root = merge(l_tr.first, temp.second);
      }
    
      int qrank_by_val(Node *cur, int val) {
        auto temp = split(cur, val - 1);
        int ret = (temp.first == nullptr ? 0 : temp.first->siz) + 1;
        root = merge(temp.first, temp.second);
        return ret;
      }
    
      int qval_by_rank(Node *cur, int rk) {
        Node *l, *mid, *r;
        tie(l, mid, r) = split_by_rk(cur, rk);
        int ret = mid->val;
        root = merge(merge(l, mid), r);
        return ret;
      }
    
      int qprev(int val) {
        auto temp = split(root, val - 1);
        int ret = qval_by_rank(temp.first, temp.first->siz);
        root = merge(temp.first, temp.second);
        return ret;
      }
    
      int qnex(int val) {
        auto temp = split(root, val);
        int ret = qval_by_rank(temp.second, 1);
        root = merge(temp.first, temp.second);
        return ret;
      }
    };
    
    none_rot_treap tr;
    
    int main() {
      srand(time(nullptr));
      int t;
      scanf("%d", &t);
      while (t--) {
        int mode;
        int num;
        scanf("%d%d", &mode, &num);
        switch (mode) {
          case 1:
            tr.insert(num);
            break;
          case 2:
            tr.del(num);
            break;
          case 3:
            printf("%d\n", tr.qrank_by_val(tr.root, num));
            break;
          case 4:
            printf("%d\n", tr.qval_by_rank(tr.root, num));
            break;
          case 5:
            printf("%d\n", tr.qprev(num));
            break;
          case 6:
            printf("%d\n", tr.qnex(num));
            break;
        }
      }
    }
    ```

### Range operations of the non-rotating Treap

#### Pointer implementation

??? note "Complete code"
    Below is the complete version of the code explained above; it is the template code for the artistic balanced tree problem.
    
    ```cpp
    
    // author: (ttzytt)[ttzytt.com]
    #include <cstdlib>
    #include <ctime>
    #include <iostream>
    using namespace std;
    
    // Reference: https://www.cnblogs.com/Equinox-Flower/p/10785292.html
    struct Node {
      Node* ch[2];
      int val, prio;
      int cnt;
      int siz;
      bool to_rev = false;  // every node in this subtree needs to be reversed
    
      Node(int _val) : val(_val), cnt(1), siz(1) {
        ch[0] = ch[1] = nullptr;
        prio = rand();
      }
    
      int upd_siz() {
        siz = cnt;
        if (ch[0] != nullptr) siz += ch[0]->siz;
        if (ch[1] != nullptr) siz += ch[1]->siz;
        return siz;
      }
    
      void pushdown() {
        swap(ch[0], ch[1]);
        if (ch[0] != nullptr) ch[0]->to_rev ^= 1;
        // if the child also needs to be reversed, the two reversals cancel out; if the child is not reversed, this
        //  tag needs to be pushed further down to the child
        if (ch[1] != nullptr) ch[1]->to_rev ^= 1;
        to_rev = false;
      }
    
      void check_tag() {
        if (to_rev) pushdown();
      }
    };
    
    struct Seg_treap {
      Node* root;
    #define siz(_) (_ == nullptr ? 0 : _->siz)
    
      pair<Node*, Node*> split(Node* cur, int sz) {
        // split according to the tree size
        if (cur == nullptr) return {nullptr, nullptr};
        cur->check_tag();
        if (sz <= siz(cur->ch[0])) {
          // the left subtree is enough
          auto temp = split(cur->ch[0], sz);
          // not all of the left subtree is necessarily needed; temp.second is not needed
          cur->ch[0] = temp.second;
          cur->upd_siz();
          return {temp.first, cur};
        } else {
          // the left one plus part of the right one (of course including this node itself)
          auto temp = split(cur->ch[1], sz - siz(cur->ch[0]) - 1);
          cur->ch[1] = temp.first;
          cur->upd_siz();
          return {cur, temp.second};
        }
      }
    
      Node* merge(Node* sm, Node* bg) {
        // small, big
        if (sm == nullptr && bg == nullptr) return nullptr;
        if (sm != nullptr && bg == nullptr) return sm;
        if (sm == nullptr && bg != nullptr) return bg;
        sm->check_tag(), bg->check_tag();
        if (sm->prio < bg->prio) {
          sm->ch[1] = merge(sm->ch[1], bg);
          sm->upd_siz();
          return sm;
        } else {
          bg->ch[0] = merge(sm, bg->ch[0]);
          bg->upd_siz();
          return bg;
        }
      }
    
      void insert(int val) {
        auto temp = split(root, val);
        auto l_tr = split(temp.first, val - 1);
        Node* new_node;
        if (l_tr.second == nullptr) new_node = new Node(val);
        Node* l_tr_combined =
            merge(l_tr.first, l_tr.second == nullptr ? new_node : l_tr.second);
        root = merge(l_tr_combined, temp.second);
      }
    
      void seg_rev(int l, int r) {
        // less and more here are relative to l
        auto less = split(root, l - 1);
        // everything less than or equal to l - 1 will be on the left of less
        auto more = split(less.second, r - l + 1);
        // take out the first r - l + 1 elements starting from l
        more.first->to_rev = true;
        root = merge(less.first, merge(more.first, more.second));
      }
    
      void print(Node* cur) {
        if (cur == nullptr) return;
        cur->check_tag();
        print(cur->ch[0]);
        cout << cur->val << " ";
        print(cur->ch[1]);
      }
    };
    
    Seg_treap tr;
    
    int main() {
      srand(time(nullptr));
      int n, m;
      cin >> n >> m;
      for (int i = 1; i <= n; i++) tr.insert(i);
      while (m--) {
        int l, r;
        cin >> l >> r;
        tr.seg_rev(l, r);
      }
      tr.print(tr.root);
    }
    ```

## Exercises

[Ordinary balanced tree](https://loj.ac/problem/104)

[Artistic balanced tree (Splay)](https://loj.ac/problem/105)

["ZJOI2006" Bookshelf](https://www.luogu.com.cn/problem/P2596)

["NOI2005" Sequence maintenance](https://www.luogu.com.cn/problem/P2042)

[CF 702F T-Shirts](http://codeforces.com/problemset/problem/702/F)

## References and notes

[^ref1]: The design of this figure is based on the [illustration in the Wikipedia article on treaps](https://en.wikipedia.org/wiki/Treap)

[^ref2]: <https://charleswu.site/archives/1051>

[^ref3]: <https://www.cnblogs.com/Equinox-Flower/p/10785292.html>

[^ref4]: <https://www.luogu.com.cn/blog/85514/fhq-treap-xue-xi-bi-ji>
