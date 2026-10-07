---
title: Linked list
---

This page briefly introduces linked lists.

## Introduction

A linked list is a data structure for storing data in which the elements are connected by pointers, like the links of a chain. Its characteristic is that inserting and deleting data is very convenient, but finding and reading data performs poorly.

## Difference from arrays

Both linked lists and arrays can be used to store data. Unlike a linked list, an array stores all elements one after another in order. The different storage structures give them different advantages:

Thanks to its chain-like structure, a linked list can delete and insert data conveniently in $O(1)$ operations. But for the same reason, finding and reading data is less efficient than in an array: random access takes $O(n)$ operations.

An array can find and read data conveniently, with $O(1)$ operations for random access. But deleting and inserting take $O(n)$ operations.

## Building a linked list

???+ tip "Tip"
    When building a linked list, the part involving pointers is rather abstract and may be hard to understand from text and code alone; we recommend drawing pictures to follow along.

### Singly linked list

A node of a singly linked list contains a data field and a pointer field: the data field stores the data, and the pointer field connects the current node to the next node.

![](images/list.svg)

???+ note "Implementation"
    === "C++"
        ```cpp
        struct Node {
          int value;
          Node *next;
        };
        ```
    
    === "Python"
        ```python
        class Node:
            def __init__(self, value=None, next=None):
                self.value = value
                self.next = next
        ```

### Doubly linked list

A doubly linked list also has a data field and a pointer field. The difference is that the pointer field has a left and a right (or previous and next) pointer, used to connect the previous node, the current node and the next node.

![](images/double-list.svg)

???+ note "Implementation"
    === "C++"
        ```cpp
        struct Node {
          int value;
          Node *left;
          Node *right;
        };
        ```
    
    === "Python"
        ```python
        class Node:
            def __init__(self, value=None, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right
        ```

## Inserting (writing) data into a linked list

### Singly linked list

The procedure is roughly as follows:

1.  initialize the data `node` to be inserted;
2.  point the `next` pointer of `node` to the node after `p`;
3.  point the `next` pointer of `p` to `node`.

The concrete process is shown in the following figures:

1.  ![](./images/list-insert-1.svg)
2.  ![](./images/list-insert-2.svg)
3.  ![](./images/list-insert-3.svg)

The code implementation is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void insertNode(int i, Node *p) {
          Node *node = new Node;
          node->value = i;
          node->next = p->next;
          p->next = node;
        }
        ```
    
    === "Python"
        ```python
        def insertNode(i, p):
            node = Node()
            node.value = i
            node.next = p.next
            p.next = node
        ```

### Singly linked circular list

If we connect the head and the tail of the list, it becomes a circular list. Since the head and tail are connected, when inserting data we must check whether the original list is empty: if it is, the node points to itself; otherwise the data is inserted as usual.

The procedure is roughly as follows:

1.  initialize the data `node` to be inserted;
2.  check whether the given list `p` is empty;
3.  if it is, point the `next` pointer of `node` and `p` to `node` itself;
4.  otherwise, point the `next` pointer of `node` to the node after `p`;
5.  point the `next` pointer of `p` to `node`.

The concrete process is shown in the following figures:

1.  ![](./images/list-insert-cyclic-1.svg)
2.  ![](./images/list-insert-cyclic-2.svg)
3.  ![](./images/list-insert-cyclic-3.svg)

The code implementation is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void insertNode(int i, Node *p) {
          Node *node = new Node;
          node->value = i;
          node->next = NULL;
          if (p == NULL) {
            p = node;
            node->next = node;
          } else {
            node->next = p->next;
            p->next = node;
          }
        }
        ```
    
    === "Python"
        ```python
        def insertNode(i, p):
            node = Node()
            node.value = i
            node.next = None
            if p == None:
                p = node
                node.next = node
            else:
                node.next = p.next
                p.next = node
        ```

### Doubly linked circular list

When inserting data into a doubly linked circular list, besides checking whether the given list is empty, we also have to update both the left and the right pointer.

The procedure is roughly as follows:

1.  initialize the data `node` to be inserted;
2.  check whether the given list `p` is empty;
3.  if it is, point the `left` and `right` pointers of `node`, as well as `p`, to `node` itself;
4.  otherwise, point the `left` pointer of `node` to `p`;
5.  point the `right` pointer of `node` to the right node of `p`;
6.  point the `left` pointer of the right node of `p` to `node`;
7.  point the `right` pointer of `p` to `node`.

The code implementation is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void insertNode(int i, Node *p) {
          Node *node = new Node;
          node->value = i;
          if (p == NULL) {
            p = node;
            node->left = node;
            node->right = node;
          } else {
            node->left = p;
            node->right = p->right;
            p->right->left = node;
            p->right = node;
          }
        }
        ```
    
    === "Python"
        ```python
        def insertNode(i, p):
            node = Node()
            node.value = i
            if p == None:
                p = node
                node.left = node
                node.right = node
            else:
                node.left = p
                node.right = p.right
                p.right.left = node
                p.right = node
        ```

## Deleting data from a linked list

### Singly linked (circular) list

Let `p` be the node to delete. To remove it from the list, it suffices to overwrite `p` with the value of its next node `p->next`, and at the same time update the pointer to the node after the next one.

The procedure is roughly as follows:

1.  assign the value of the node after `p` to `p`, erasing `p->value`;
2.  create a temporary node `t` holding the address of `p->next`;
3.  point the `next` pointer of `p` to the node two steps after `p`, erasing `p->next`;
4.  delete `t`. Although the address of the original node `p` is still in use and what is freed is the address of the original `p->next`, the data of `p` has been overwritten by that of `p->next`, so `p` survives in name only.

The concrete process is shown in the following figures:

1.  ![](./images/list-delete-1.svg)
2.  ![](./images/list-delete-2.svg)
3.  ![](./images/list-delete-3.svg)

The code implementation is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void deleteNode(Node *p) {
          p->value = p->next->value;
          Node *t = p->next;
          p->next = p->next->next;
          delete t;
        }
        ```
    
    === "Python"
        ```python
        def deleteNode(p):
            p.value = p.next.value
            p.next = p.next.next
        ```

### Doubly linked circular list

The procedure is roughly as follows:

1.  point the right pointer of the left node of `p` to the right node of `p`;
2.  point the left pointer of the right node of `p` to the left node of `p`;
3.  create a temporary node `t` holding the address of `p`;
4.  assign the address of the right node of `p` to `p`, so that `p` does not become a dangling pointer;
5.  delete `t`.

The code implementation is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void deleteNode(Node *&p) {
          p->left->right = p->right;
          p->right->left = p->left;
          Node *t = p;
          p = p->right;
          delete t;
        }
        ```
    
    === "Python"
        ```python
        def deleteNode(p):
            p.left.right = p.right
            p.right.left = p.left
            p = p.right
        ```

## Tricks

### XOR linked list

An XOR linked list is essentially still a **doubly linked list**, but by using bitwise XOR values it achieves the functionality of a doubly linked list with the memory of only one pointer.

In the structure `Node` we define `lr = left ^ right`, i.e. the **bitwise XOR** of the addresses of the previous and next elements. When traversing forward, XOR-ing the address of the previous element with the `lr` of the current node gives the address of the next element; when traversing backward, XOR-ing the address of the next element with the `lr` of the current node gives the address of the previous element.
This way, the same functionality as a doubly linked list is achieved with half the memory.
