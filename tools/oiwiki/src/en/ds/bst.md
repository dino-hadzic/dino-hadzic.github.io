---
title: Binary search tree & balanced trees
---

## Definition

A binary search tree (BST) is a tree data structure in the form of a binary tree, defined as follows:

1.  The empty tree is a binary search tree.

2.  If the left subtree of a binary search tree is not empty, the values of all nodes in its left subtree are smaller than the value of its root.

3.  If the right subtree of a binary search tree is not empty, the values of all nodes in its right subtree are greater than the value of its root.

4.  The left and right subtrees of a binary search tree are both binary search trees.

The time spent on the basic operations of a binary search tree is proportional to the height of the tree. For a binary search tree with $n$ nodes, the best-case time complexity of these operations is $O(\log n)$ and the worst case is $O(n)$. The expected height of a randomly built binary search tree is $O(\log n)$.

## Procedure

### Definition of a binary search tree node

???+ note "Implementation"
    ```cpp
    struct TreeNode {
      int key;
      TreeNode* left;
      TreeNode* right;
      // maintain other information, such as height, number of nodes, etc.
      int size;   // size of the subtree rooted at this node
      int count;  // number of duplicates of this node's value
    
      TreeNode(int value)
          : key(value), size(1), count(1), left(nullptr), right(nullptr) {}
    };
    ```

### Traversing a binary search tree

From the recursive definition of a binary search tree it follows that the sequence of values obtained by an inorder traversal is non-decreasing. The time complexity is $O(n)$.

The code for traversing a binary search tree:

???+ note "Implementation"
    ```cpp
    void inorderTraversal(TreeNode* root) {
      if (root == nullptr) {
        return;
      }
      inorderTraversal(root->left);
      std::cout << root->key << " ";
      inorderTraversal(root->right);
    }
    ```

### Finding the minimum/maximum

From the properties of a binary search tree it follows that the minimum of the tree is the end node of its left chain, and the maximum is the end node of its right chain. The time complexity is $O(h)$.

???+ note "Implementation"
    ```cpp
    int findMin(TreeNode* root) {
      if (root == nullptr) {
        return -1;
      }
      while (root->left != nullptr) {
        root = root->left;
      }
      return root->key;
    }
    
    int findMax(TreeNode* root) {
      if (root == nullptr) {
        return -1;
      }
      while (root->right != nullptr) {
        root = root->right;
      }
      return root->key;
    }
    ```

### Searching for an element

In the binary search tree rooted at `root`, search for a node with value `value`.

Case analysis:

-   If `root` is empty, return `false`.
-   If the value of `root` equals `value`, return `true`.
-   If the value of `root` is greater than `value`, continue searching in the left subtree of `root`.
-   If the value of `root` is smaller than `value`, continue searching in the right subtree of `root`.

The time complexity is $O(h)$.

???+ note "Implementation"
    ```cpp
    bool search(TreeNode* root, int target) {
      if (root == nullptr) {
        return false;
      }
      if (root->key == target) {
        return true;
      } else if (target < root->key) {
        return search(root->left, target);
      } else {
        return search(root->right, target);
      }
    }
    ```

Insertion, deletion and modification all require searching in the binary search tree first.

### Inserting an element

Insert a node with value `value` into the binary search tree rooted at `root`.

Case analysis:

-   If `root` is empty, directly return a new node with value `value`.

-   If the value of `root` equals `value`, increase the occurrence count of this value stored in the node's extra field by $1$.

-   If the value of `root` is greater than `value`, insert a node with value `value` into the left subtree of `root`.

-   If the value of `root` is smaller than `value`, insert a node with value `value` into the right subtree of `root`.

The time complexity is $O(h)$.

???+ note "Implementation"
    ```cpp
    TreeNode* insert(TreeNode* root, int value) {
      if (root == nullptr) {
        return new TreeNode(value);
      }
      if (value < root->key) {
        root->left = insert(root->left, value);
      } else if (value > root->key) {
        root->right = insert(root->right, value);
      } else {
        root->count++;  // equal values, increase the duplicate count
      }
      root->size = root->count + (root->left ? root->left->size : 0) +
                   (root->right ? root->right->size : 0);  // update the node's subtree size
      return root;
    }
    ```

### Deleting an element

Delete a node with value `value` from the binary search tree rooted at `root`.

First search the binary search tree for the node with value `value`, then do a case analysis:

-   If the extra field `count` of this node is greater than $1$, just decrease `count`.

-   If the `count` of this node is $1$:

    -   If `root` is a leaf, simply delete the node.

    -   If `root` is a chain node, i.e. a node with only one child, return that child.

    -   If `root` has two non-empty children, it is usually replaced by the maximum of its left subtree (the rightmost node of the left subtree) or the minimum of its right subtree (the leftmost node of the right subtree), and then that node is deleted.

Time complexity $O(h)$.

???+ note "Implementation"
    The call `root = remove(root, 1)` deletes the node with value 1 from the tree rooted at `root` and returns the new root.
    
    ```cpp
    // the return value is the new root after deleting value
    TreeNode* remove(TreeNode* root, int value) {
      if (root == nullptr) {
        return root;
      }
      if (value < root->key) {
        root->left = remove(root->left, value);
      } else if (value > root->key) {
        root->right = remove(root->right, value);
      } else {
        if (root->count > 1) {
          root->count--;  // duplicate count greater than 1, decrease it
        } else {
          if (root->left == nullptr) {
            TreeNode* temp = root->right;
            delete root;
            return temp;
          } else if (root->right == nullptr) {
            TreeNode* temp = root->left;
            delete root;
            return temp;
          } else {
            TreeNode* successor = findMinNode(root->right);
            root->key = successor->key;
            root->count = successor->count;  // update the duplicate count
            // when successor->count > 1, that node should also be deleted,
            // otherwise the subsequent removal would only decrease the duplicate count
            successor->count = 1;
            root->right = remove(root->right, successor->key);
          }
        }
      }
      // keep maintaining size; we do not write --root->size;
      // because value may not be in the tree, so no deletion may have happened
      root->size = root->count + (root->left ? root->left->size : 0) +
                   (root->right ? root->right->size : 0);
      return root;
    }
    
    // here we take the minimum of the right subtree as an example
    TreeNode* findMinNode(TreeNode* root) {
      while (root->left != nullptr) {
        root = root->left;
      }
      return root;
    }
    ```

### Rank of an element

The rank is defined as the number of elements before the first equal element after sorting the array in ascending order, plus one.

To find the rank of an element, start from the root and walk to this element; whenever we go right, add to the answer the number of nodes in the left child plus the duplicate count of the current node; finally add the size of the left subtree of the destination plus one.

Time complexity $O(h)$.

???+ note "Implementation"
    ```cpp
    int queryRank(TreeNode* root, int v) {
      if (root == nullptr) return 0;
      if (root->key == v) return (root->left ? root->left->size : 0) + 1;
      if (root->key > v) return queryRank(root->left, v);
      return queryRank(root->right, v) + (root->left ? root->left->size : 0) +
             root->count;
    }
    ```

### Finding the element of rank k

In a subtree, the rank of the root depends on the size of its left subtree.

-   If the size of its left subtree is at least $k$, the element is in the left subtree;

-   if the size of its left subtree lies in the interval $[k-\textit{count},k-1]$ (`count` is the occurrence count of the current node's value), the element is the root of the subtree;

-   if the size of its left subtree is smaller than $k-\textit{count}$, the element is in the right subtree.

Time complexity $O(h)$.

???+ note "Implementation"
    ```cpp
    int querykth(TreeNode* root, int k) {
      if (root == nullptr) return -1;  // or return another suitable value as needed
      if (root->left) {
        if (root->left->size >= k) return querykth(root->left, k);
        if (root->left->size + root->count >= k) return root->key;
      } else {
        if (k <= root->count) return root->key;
      }
      return querykth(root->right,
                      k - (root->left ? root->left->size : 0) - root->count);
    }
    ```

## Introduction to balanced trees

One purpose of using a search tree is to shorten the time of inserting, deleting, modifying and searching for nodes (insertion, deletion and modification all include a search).

Regarding search efficiency, if a tree has height $h$, in the worst case searching for a key requires $h$ comparisons, so the search time complexity (also the average search length, ASL) does not exceed $O(h)$. In an ideal binary search tree the time of all operations can be shortened to $O(\log n)$ ($n$ is the total number of nodes).

However, the $O(\log n)$ time complexity holds only in the ideal case. In the worst case a search tree may degenerate into a linked list. Imagine a binary search tree in which every node has only a right child: its properties are the same as those of a linked list, and all operations (insert, delete, modify, search) take $O(n)$.

We see that the complexity of the operations depends on the height $h$ of the tree. This leads to balanced trees, which maintain the height of the tree (its balance) through certain operations to reduce the complexity of the operations.

### Definition of balance

Different balanced trees define "**balanced**" differently. For example, in a binary search tree rooted at T, if the heights of the left and right subtrees differ greatly, or the number of nodes in the left subtree is far larger than in the right subtree, the tree is obviously not balanced.

For binary search trees, the common definition of balance is: in the tree rooted at T, the heights of the left and right subtrees of every node differ by at most 1.

-   In a [Splay tree](splay.md), every access operation on a node (search, insertion or deletion) moves the accessed node to the root of the tree.

-   In an [AVL tree](avl.md), every node N maintains the height of the tree rooted at N. The AVL tree's definition of balance: T is an AVL tree if and only if its left and right subtrees are also AVL trees and $|height(T->left) - height(T->right)| \leq 1$.

-   In a [Size Balanced Tree](sbt.md), every node N maintains the number of nodes `size` of the tree rooted at N. The definition of balance: the `size` of any node is not smaller than the `size` of any child (Nephew) of its sibling (Sibling).

Moreover, for search trees with the same set of element values, the balanced state may not be unique. That is, two different search trees may contain the same set of values and both be balanced.

### The rebalancing procedure

Adjusting a search tree that does not satisfy the balance condition can make the unbalanced search tree balanced again.

For binary balanced trees, the rebalancing operations are the **left rotation (Left Rotate or zag)** and the **right rotation (Right Rotate or zig)**. Since the inorder traversal sequence must remain unchanged when adjusting a binary balanced tree, neither of these two operations changes the inorder sequence.

We first introduce the right rotation, also called the "single right rotation" or "LL rotation". The right rotation of node $A$ means: the left child $B$ of $A$ is rotated up to the right and replaces $A$ as the root, node $A$ is rotated down to the right and becomes the root of the right subtree of $B$, and the former right subtree of $B$ becomes the left subtree of $A$.

![bst-rotate](images/bst-rotate.svg)

The right rotation changes only three node links, which amounts to a cyclic permutation of three edges; therefore one node must be stored temporarily before performing the cyclic update.

The usual update order for the right rotation is: temporarily store node $B$ (the new root), point the left child of $A$ to the right subtree $T2$ of $B$, then point the right child pointer of $B$ to $A$, and finally point the parent of $A$ to the stored $B$.

Completely analogously, there is the corresponding left rotation, also called the "single left rotation" or "RR rotation". The left and right rotations are mirror images of each other.

The code for the left and right rotations follows.

???+ note "Implementation"
    ```cpp
    TreeNode* rotateLeft(TreeNode* root) {
      TreeNode* newRoot = root->right;
      root->right = newRoot->left;
      newRoot->left = root;
      // update the information of the affected nodes
      updateHeight(root);
      updateHeight(newRoot);
      return newRoot;  // return the new root
    }
    
    TreeNode* rotateRight(TreeNode* root) {
      TreeNode* newRoot = root->left;
      root->left = newRoot->right;
      newRoot->right = root;
      updateHeight(root);
      updateHeight(newRoot);
      return newRoot;
    }
    ```

For this sample code, the parent `pre` of `root` must be saved when calling. The function returns a pointer to the new root; it suffices to point `pre` to the new root.

#### The four cases of broken balance

Although the definitions of different binary balanced trees differ, the differences lie only in the information maintained at the nodes and in how that information is updated after a rotation. The balance of a binary balanced tree can be broken in only the following four ways, and the rebalancing operations consist only of left and right rotations. We first introduce the four cases and then compare the different binary balanced trees.

LL type: the left subtree of the left child of T is too long, breaking the balance.

Adjustment: right-rotate node T.

![bst-LL](images/bst-LL.svg)

RR type: similar to the LL type, the right subtree of the right child of T is too long, breaking the balance.

Adjustment: left-rotate node T.

![bst-RR](images/bst-RR.svg)

LR type: the right subtree of the left child of T is too long, breaking the balance.

Adjustment: first left-rotate node L, turning it into the LL type, then right-rotate node T.

![bst-LR](images/bst-LR.svg)

RL type: similar to the LR type, the left subtree of the right child of T is too long, breaking the balance.

Adjustment: first right-rotate node R, turning it into the RR type, then left-rotate node T.

![bst-RL](images/bst-RL.svg)
