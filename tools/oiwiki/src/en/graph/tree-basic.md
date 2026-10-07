---
title: Tree basics
---

## Introduction

A tree in graph theory looks like a tree in real life, except that when solving problems we are used to putting the root at the top. This data structure looks like an upside-down tree, hence the name.

## Definition

A tree without a fixed root node is called an **unrooted tree**. An unrooted tree has several equivalent formal definitions:

-   a connected undirected graph with $n$ nodes and $n-1$ edges

-   an undirected acyclic connected graph

-   an undirected graph in which there is exactly one simple path between any two nodes

-   a connected graph in which every edge is a bridge

-   a graph without cycles in which adding an edge between any two distinct nodes yields a graph with exactly one cycle

If, on top of an unrooted tree, we designate one node as the **root**, we obtain a **rooted tree**. A rooted tree is still often represented as an undirected graph; it is just that a parent-child relationship between the nodes is specified, as detailed below.

## Definitions related to trees

### Applicable to both unrooted and rooted trees

-   **Forest**: a graph in which every connected component is a tree. By definition, a single tree is also a forest.

-   **Spanning tree**: a spanning subgraph of a connected undirected graph that is also a tree. In other words, choose $n - 1$ edges from the edge set of the graph so that all vertices are connected.

-   **Leaf node of an unrooted tree**: a node whose degree is at most $1$.

    ???+ question "Why not degree exactly $1$?"
        Consider $n = 1$.

-   **Leaf node of a rooted tree**: a node with no children.

### Applicable only to rooted trees

-   **Parent node**: for every node other than the root, the second node on the path from that node to the root.  
    The root node has no parent.
-   **Ancestor**: the nodes on the path from a node to the root, excluding the node itself.  
    The set of ancestors of the root is empty.
-   **Child node**: if $u$ is the parent of $v$, then $v$ is a child of $u$.  
    The order of the children is usually not distinguished; binary trees are an exception.
-   **Depth of a node**: the number of edges on the path to the root.
-   **Height of a tree**: the maximum depth over all nodes.
-   **Sibling**: children of the same parent are siblings of each other.
-   **Descendant**: the children and the descendants of the children.  
    Or, equivalently: if $u$ is an ancestor of $v$, then $v$ is a descendant of $u$.

![tree-definition.svg](images/tree-definition.svg)

-   **Subtree**: the subgraph containing the node after the edge to its parent is removed.

    ![tree-definition-subtree.svg](images/tree-definition-subtree.svg)

## Special trees

-   **Chain/path graph**: a tree in which every node is incident to at most $2$ edges.

-   **Star**: a tree in which there exists a node $u$ such that all nodes other than $u$ are connected to $u$.

-   **Rooted binary tree**: a rooted tree in which every node has at most two children. The order of the two children is often distinguished; they are called the left child and the right child.  
    In most cases the term **binary tree** refers to a rooted binary tree.

-   **Full/proper binary tree**: a binary tree in which every node has either 0 or 2 children. In other words, every node is either a leaf or has both a non-empty left and a non-empty right subtree.

    ![](images/tree-binary-proper.svg)

-   **Complete binary tree**: only the nodes on the bottom two levels may have degree less than 2, and the nodes on the bottom level occupy consecutive positions at the far left of that level.

    ![](images/tree-binary-complete.svg)

-   **Perfect binary tree**: a binary tree in which all leaves have the same depth and every non-leaf node has exactly 2 children.

    ![](images/tree-binary-perfect.svg)

???+ warning "Warning"
    The Chinese translation of "proper binary tree" is not fixed, and the definitions of complete and full binary trees differ between textbooks, so when encountering them you need to judge from the context.

When competitive programmers say "full binary tree" (满二叉树), they usually mean a perfect binary tree.

## Storage

### Storing only the parent

Use an array `parent[N]` to record the parent of every node.

This way little information is available and it is inconvenient for top-down traversal. It is often used in bottom-up recurrence problems.

### Adjacency list

-   For an unrooted tree: open a linear list for every node and record all nodes connected to it.
    ```cpp
    std::vector<int> adj[N];
    ```
-   For a rooted tree:
    -   Method one: if an undirected graph is given, it can still be stored in the above form. How to tell the parent-child relationship between the nodes is described below.
    -   Method two: if the input data guarantees the parent-child relationship between the nodes, this information can be used. Open a linear list for every node and record all of its children; if needed, also record its parent in another array.
        ```cpp
        std::vector<int> children[N];
        int parent[N];
        ```
        Of course, `std::vector` can be replaced by other means (such as a linked list).

### Left-child right-sibling representation

#### Process

For rooted trees there is a simple representation.

First, fix an arbitrary order of the children of every node.

Then, for every node record two values: its **first child** `child[u]` and its **next sibling** `sib[u]`. If there are no children, `child[u]` is empty; if the node is the last child of its parent, `sib[u]` is empty.

#### Implementation

Iterating over all children of a node can be implemented as follows.

```cpp
int v = child[u];  // start from the first child
while (v != EMPTY_NODE) {
  // ...
  // process child v
  // ...
  v = sib[v];  // move to the next child, i.e. a sibling of v
}
```

It can also be written in the following short form.

```cpp
for (int v = child[u]; v != EMPTY_NODE; v = sib[v]) {
  // ...
  // process child v
  // ...
}
```

### Binary tree

The left and right children of every node need to be recorded.

???+ note "Implementation"
    ```cpp
    int parent[N];
    int lch[N], rch[N];
    // -- or --
    int child[N][2];
    ```

## Tree traversal

### DFS on a tree

DFS on a tree is the following process: first visit the root, then visit the subtree of every child of the root in turn.

It can be used to compute the depth, parent and other information of every node.

### DFS traversals of a binary tree

#### Preorder traversal

![preorder](images/tree-basic-preorder.svg)

Traverse the binary tree in the order **root, left, right**.

???+ note "Implementation"
    ```cpp
    void preorder(BiTree* root) {
      if (root) {
        cout << root->key << " ";
        preorder(root->left);
        preorder(root->right);
      }
    }
    ```

#### Inorder traversal

![inorder](images/tree-basic-inorder.svg)

Traverse the binary tree in the order **left, root, right**.

???+ note "Implementation"
    ```cpp
    void inorder(BiTree* root) {
      if (root) {
        inorder(root->left);
        cout << root->key << " ";
        inorder(root->right);
      }
    }
    ```

#### Postorder traversal

![postorder](images/tree-basic-postorder.svg)

Traverse the binary tree in the order **left, right, root**.

???+ note "Implementation"
    ```cpp
    void postorder(BiTree* root) {
      if (root) {
        postorder(root->left);
        postorder(root->right);
        cout << root->key << " ";
      }
    }
    ```

#### Reconstruction

Given the inorder sequence and one other sequence, the third sequence can be determined.

![reverse](images/tree-basic-reverse.svg)

1.  The first element of the preorder sequence is `root`, and the last element of the postorder sequence is `root`.
2.  First determine the root, then according to the inorder sequence, what is to the left of the root is the left subtree and what is to the right is the right subtree.
3.  Every subtree can be viewed as a brand new tree that still follows the rules above.

### BFS on a tree

Starting from the root, visit the nodes strictly level by level.

During the BFS the depth and parent of every node can also be computed along the way.

#### Level-order traversal of a tree

Level-order traversal means traversing the nodes horizontally, level by level, following the hierarchy from the root down to the leaves. By the definition of BFS, the order produced by BFS is a level-order traversal. However, level-order traversal requires the different levels to be distinguished, so its result is usually represented as a two-dimensional array.

For example, the level-order traversal of the tree in the figure below is `[[1], [2, 3, 4], [5, 6]]` (each level from left to right).

![tree-basic-levelOrder](images/tree-basic-levelOrder.svg)

???+ note "Implementation"
    ```cpp
    vector<vector<int>> levelOrder(Node* root) {
      if (!root) {
        return {};
      }
      vector<vector<int>> res;
      queue<Node*> q;
      q.push(root);
      while (!q.empty()) {
        int currentLevelSize = q.size();  // number of nodes on the current level
        res.push_back(vector<int>());
        for (int i = 0; i < currentLevelSize; ++i) {
          Node* cur = q.front();
          q.pop();
          res.back().push_back(cur->val);
          for (Node* child : cur->children) {  // push all the children
            q.push(child);
          }
        }
      }
      return res;
    }
    ```

### Morris traversal of a binary tree

The central problem of binary tree traversal is how to return to the current node and continue the traversal after its children have been traversed. Both the recursive and the non-recursive methods of traversing a binary tree use a stack to record the return path and thus move from a lower level to an upper one. Its space complexity is $O(\log n)$ in the best case and $O(n)$ in the worst case (when the binary tree is a chain).

The essence of the Morris traversal is to avoid using a stack: the idle `right` pointers of the bottom nodes are used to point back to some node of an upper level, thereby moving from a lower level to an upper one.

#### Process of the Morris traversal

Suppose we are at the current node `cur`; at the beginning this is the root.

1.  If `cur` is empty, the traversal stops; otherwise perform the following.
2.  If `cur` has no left subtree, `cur` moves right (`cur = cur->right`).
3.  If `cur` has a left subtree, find the rightmost node of the left subtree, denoted `mostRight`.
    -   If the `right` pointer of `mostRight` points to null, make it point to `cur`, then `cur` moves left (`cur = cur->left`).
    -   If the `right` pointer of `mostRight` points to `cur`, reset it to `null`, then `cur` moves right (`cur = cur->right`).

For example, `cur` starts visiting from node 1.

![tree-basic-morris-1](images/tree-basic-morris-1.svg)

When `cur` visits node 2 for the first time, it finds the rightmost node of the left subtree, node 4, and sets the `right` pointer of 4 to `cur` (node 2).

![tree-basic-morris-2](images/tree-basic-morris-2.svg)

`cur` returns to the upper level through the `right` pointer of 4; when it visits node 2 for the second time, it finds the rightmost node of the left subtree, node 4, resets the `right` pointer of 4 to `null`, and then continues visiting the right subtree. The rest of the process is omitted.

![tree-basic-morris-1](images/tree-basic-morris-1.svg)

The visiting order of the whole tree is `1242513637`. We can see that nodes with a left subtree are visited twice, while nodes without a left subtree are visited only once.

???+ note "Implementation"
    ```cpp
    void morris(TreeNode* root) {
      TreeNode* cur = root;
      while (cur) {
        if (!cur->left) {
          // if the current node has no left child, print its value and enter the right subtree
          std::cout << cur->val << " ";
          cur = cur->right;
          continue;
        }
        // find the rightmost node of the left subtree of the current node
        TreeNode* mostRight = cur->left;
        while (mostRight->right && mostRight->right != cur) {
          mostRight = mostRight->right;
        }
        if (!mostRight->right) {
          // if the right pointer of the rightmost node is null, point it to the current node and enter the left subtree
          mostRight->right = cur;
          cur = cur->left;
        } else {
          // if the right pointer of the rightmost node points to the current node, the left subtree has been traversed; print the value of the current node and enter the right subtree
          mostRight->right = nullptr;
          std::cout << cur->val << " ";
          cur = cur->right;
        }
      }
    }
    ```

### Unrooted tree

#### Process

A tree is usually traversed depth-first, and the thing to pay the most attention to in this process is avoiding visiting a node twice.

Since a tree is an acyclic graph, it suffices to record from which node the current node was reached, and then enter all adjacent nodes except that one; this avoids repeated visits.

???+ note "Implementation"
    ```cpp
    void dfs(int u, int from) {
      // recursively enter all children except from
      // for the start node, from is empty, so all adjacent nodes are visited, as expected
      for (int v : adj[u])
        if (v != from) {
          dfs(v, u);
        }
    }
    
    // when starting the traversal
    int EMPTY_NODE = -1;  // a non-existent index
    int root = 0;         // pick an arbitrary node as the start
    dfs(root, EMPTY_NODE);
    ```

### Rooted tree

For a rooted tree, the parent-child relationship between the nodes needs to be distinguished.

Looking at the traversal above: if the traversal starts from the root, then the value of `from` when visiting a node is exactly the index of its parent.

In this way, from an undirected input we can determine the parent of every node as well as the lists of children.

**Part of the content of this page is quoted from the blog post [二叉树：前序遍历、中序遍历、后续遍历](https://blog.csdn.net/weixin_43357638/article/details/99730284) (Binary tree: preorder, inorder and postorder traversal), under the CC 4.0 BY-SA license.**
