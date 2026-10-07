---
title: AA tree
---

An AA tree is a balanced tree structure for efficiently storing and retrieving ordered data. Professor Arne Andersson introduced it in his 1993 paper "Balanced search trees made simple", aiming to reduce the number of cases considered by red-black trees. An AA tree supports search, insertion, and deletion in $O(\log N)$ time. An example is shown below.

![aa-tree-1](images/aa-tree-1.jpg)

An AA tree is a variant of a red-black tree, but its red nodes can only be right children. As a result, it simulates a 2-3 tree rather than a 2-3-4 tree, greatly simplifying maintenance. Red-black tree maintenance algorithms must consider seven different cases to balance the tree correctly.

![red-black tree](images/aa-tree-2.svg)

Because red nodes can only be right children, an AA tree only needs to consider two cases.

![aa-tree](images/aa-tree-3.svg)

## Definition

An AA tree follows the same rules as a red-black tree, with one additional rule: **red nodes cannot be left children**.

1.  Every node can be red or black.
2.  The root is always black.
3.  Leaves (NULL) are always black.
4.  Both children of a red node must be black; there are no two adjacent red nodes.
5.  Every path from the root to a NULL node has the same number of black nodes.
6.  Red nodes can only be right children.

## Maintaining balance

Each AA tree node maintains a **level** field, similar to the color field ("RED" or "BLACK") in a red-black tree. The levels satisfy the following 5 conditions:

1. The level of every leaf is 1.

2. The level of every left child is one less than its parent's level.

3. The level of every right child equals its parent's level or is one less.

4. The level of every right grandchild is strictly less than its grandparent's level.

5. Every node with a level greater than 1 has two children.

![aa-tree-4](images/aa-tree-4.jpg)

### Horizontal link (Horizontal Link)

A link whose child has the same level as its parent is called a **horizontal link**, similar to a red link in a red-black tree. A single right horizontal link is allowed, but consecutive right horizontal links are not; left horizontal links are forbidden. These restrictions are stricter than those of a red-black tree, making AA tree balancing much simpler to implement.

![aa-tree-5](images/aa-tree-5.jpg)

Insertion and deletion may temporarily unbalance an AA tree (violate its invariants). Restoring balance requires only two operations: **skew** and **split**. Skew performs a right rotation on a subtree with a left horizontal link, replacing it with a subtree with a right horizontal link. Split performs a left rotation and increases the level, replacing a subtree with two or more consecutive right horizontal links with one having two fewer consecutive right horizontal links. Insertion and deletion are further simplified by letting skew and split modify the tree only when needed, rather than having the caller decide whether to perform them.

### split (left rotation)

A chain of consecutive right horizontal links occurs (three consecutive nodes to the right have the same level, and nodes R and X are red).

Rotate node *T* to the left, treating nodes at or below this level as a subtree.

1.  The right child of the subtree root becomes the new subtree root;
2.  The old subtree root becomes the left child of the new root;
3.  The new subtree root's level increases by 1.

![aa-tree-split](images/aa-tree-split.svg)

???+ note "Pseudocode implementation"
    $$
    \begin{array}{ll}
    1 & \textbf{function } \text{split}(\text{root}) \\
    2 & \qquad \textbf{if } \text{root}\rightarrow\text{right}\rightarrow\text{right}\rightarrow\text{level} == \text{root}\rightarrow\text{level} \\
    3 & \qquad\qquad \text{rotate\_left}(\text{root}) \\
    4 & \textbf{end function}
    \end{array}
    $$

### skew (right rotation)

A left horizontal link occurs (two consecutive nodes to the left have the same level).

Rotate node *T* to the right, treating nodes at or below this level as a subtree.

1.  The left child of the subtree root becomes the new subtree root;
2.  The old subtree root becomes the right child of the new root.

![aa-tree-skew](images/aa-tree-skew.svg)

???+ note "Pseudocode implementation"
    $$
    \begin{array}{ll}
    1 & \textbf{function } \text{skew}(\text{root}) \\
    2 & \qquad \textbf{if } \text{root}\rightarrow\text{left}\rightarrow\text{level} == \text{root}\rightarrow\text{level} \\
    3 & \qquad\qquad \text{rotate\_right}(\text{root}) \\
    4 & \textbf{end function}
    \end{array}
    $$

## AA tree operations

An AA tree is itself a binary search tree, so searching is the same as in other binary search trees. Insertion and deletion are the same as in an *AVL* tree: first insert or delete the key, then retrace the search path to the root, restructuring the tree along the way.

### Insertion

???+ note "Pseudocode implementation"
    $$
    \begin{array}{ll}
    1 & \textbf{function } \text{insert}(\text{root}, \text{add}) \\
    2 & \qquad \textbf{if } \text{root} == \text{NULL} \\
    3 & \qquad\qquad \text{root} \gets \text{add} \\
    4 & \qquad \textbf{else if } \text{add}\rightarrow\text{key} < \text{root}\rightarrow\text{key} \qquad //If duplicates are allowed<= \\ 
    5 & \qquad\qquad \text{insert}(\text{root}\rightarrow\text{left}, \text{add}) \\
    6 & \qquad \textbf{else if } \text{add}\rightarrow\text{key} > \text{root}\rightarrow\text{key} \\
    7 & \qquad\qquad \text{insert}(\text{root}\rightarrow\text{right}, \text{add}) \\
    8 & \qquad \textbf{end if} \\
    9 & \qquad \text{//If duplicates are not allowed, perform skew and split at every level} \\
    10 & \qquad \text{skew}(\text{root}); \\
    11 & \qquad \text{split}(\text{root}); \\
    12 & \textbf{end function}
    \end{array}
    $$

### Deletion

Deletion is similar to deletion in other balanced binary trees: first reduce deleting an internal node to deleting a leaf. Replace the internal node with its closest predecessor or successor. Since every AA tree node with a level greater than 1 has two children, the predecessor or successor will be at level 1, where deletion is simpler.

???+ note "Pseudocode implementation"
    $$
    \begin{array}{ll}
    1 &  \text{//To rebalance the tree} \\
    2 &  \textbf{if} \ \text{root->left->level} < \text{root->level} -1 \ \textbf{or} \ \text{root->right->level} < \text{root->level} -1 \\
    3 &  \{ \\
    4 & \qquad \textbf{if} \ \text{root->right->level} > \text{--root->level} \\
    5 & \qquad \{ \\
    6 & \qquad\qquad \text{root->right->level} \gets \text{root->level} \\
    7 & \qquad \} \\
    8 & \qquad \text{skew}(\text{root}) \\
    9 & \qquad \text{skew}(\text{root->right}) \\
    10 & \qquad \text{skew}(\text{root->right->right}) \\
    11 & \qquad \text{split}(\text{root}) \\
    12 & \qquad \text{split}(\text{root->right}) \\
    13 &  \} \\
    \end{array}
    $$

## Performance

AA trees perform comparably to red-black trees. Although AA trees perform more rotations, their algorithms are simpler, resulting in similar overall performance. Red-black trees perform more consistently across different situations, while AA trees tend to be flatter, giving them slightly faster searches.

## References

1.  [AA tree - Wikipedia](https://en.wikipedia.org/wiki/AA_tree)
2.  [Introduction to AA trees](https://iq.opengenus.org/aa-trees/)
3.  [AA tree - Visualization](https://kubokovac.eu/gnarley-trees/AAtree.html)
4.  [CMSC 420 Lecture 6: 2-3, Red-black, and AA trees](https://www.cs.umd.edu/class/fall2019/cmsc420-0201/Lects/lect06-aa.pdf)
