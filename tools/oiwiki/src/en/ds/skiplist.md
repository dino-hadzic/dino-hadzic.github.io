---
title: Skip list
---

A skip list is a search data structure invented by William Pugh. It supports fast lookup, insertion, and deletion of data.

The expected space complexity of a skip list is $O(n)$, and the expected time complexity of search, insertion, and deletion is $O(\log n)$.

## Basic idea

As its name suggests, a skip list is a data structure similar to a linked list. More precisely, it improves upon an ordered linked list.

For convenience, all ordered linked lists below are assumed to be sorted in **ascending order**.

Searching an ordered linked list starts at the head and compares nodes one by one until the current node's value is at least the target value. Clearly, this operation has complexity $O(n)$.

A skip list introduces **levels** on top of an ordered linked list. Each level is an ordered linked list; in particular, the bottom level is the original ordered linked list. Every node on level $i$ appears on level $i+1$ with probability $p$, where $p$ is a constant.

In a skip list with $n$ nodes, let $L(n)$ denote the level expected to contain $\frac{1}{p}$ elements. It follows that $L(n) = \log_{\frac{1}{p}}n$.

To search a skip list, start at level $L(n)$ and compare nodes horizontally until the next node is at least the target, then move down one level. Repeat until reaching the first level and no further operation is possible. If the next node is the target, the search succeeds; otherwise, the element does not exist. This skips unnecessary comparisons, making skip list searches faster than searches in an ordered linked list. The average search complexity can be proven to be $O(\log n)$.

## Complexity proof

### Space complexity

For a node, the probability that its highest level is $i$ is $p^{i-1}(1 - p)$. Thus, the expected number of levels in a skip list is $\sum_{i\ge 1} ip^{i - 1}(1-p) = \frac{1}{1 - p}$. Since $p$ is constant, the **expected space complexity** is $O(n)$.

In the worst case, the ordered linked list on every level equals the original list, so the **worst-case space complexity** is $O(n \log n)$.

### Time complexity

Analyze the search path backward. Split the process into climbing from the bottom level to level $L(n)$ and the remaining steps. Assume that a node's details are unknown until it is visited.

Suppose we are on level $i$ at node $x$. We do not know the maximum level of $x$ or of the nodes to the left of $x$, only that the maximum level of $x$ is at least $i$. If the maximum level of $x$ is greater than $i$, the next step is upward, with probability $p$; if the maximum level of $x$ equals $i$, the next step is leftward, with probability $1-p$.

Let $C(i)$ be the expected cost of climbing $i$ levels in an infinitely long skip list. Then:

$$
\begin{aligned}
C(0) & = 0 \\
C(i) & = (1-p)(1+C(i)) + p(1+C(i-1))
\end{aligned}
$$

Solving gives $C(i)=\frac{i}{p}$.

It follows that in a skip list of length $n$, the expected number of steps from the bottom level to level $L(n)$ is bounded above by $\frac{L(n) - 1}{p}$.

It remains to analyze the number of steps after reaching level $L(n)$. After reaching level $L(n)$, the number of leftward steps cannot exceed the total number of nodes at level $L(n)$ and above, whose expectation is $\frac{1}{p}$. Thus, the expected number of leftward steps after reaching level $L(n)$ is bounded above by $\frac{1}{p}$. Similarly, the expected number of upward steps after reaching level $L(n)$ is bounded above by $\frac{1}{p}$.

The expected number of search steps is therefore $\frac{L(n) - 1}{p} + \frac{2}{p}$. Since $L(n)=\log_{\frac{1}{p}}n$, the **expected time complexity** of a skip list search is $O(\log n)$.

In the worst case, the ordered list on every level equals the original list. Searching then amounts to searching the ordered list at the top level, so the **worst-case time complexity** of a skip list search is $O(n)$.

Insertion and deletion perform a search, recording the nodes that need modification along the way, and then apply the changes. At most one node needs modification on each level. Since the expected number of levels is $\log_{\frac{1}{p}}n$, the **expected time complexity** of insertion and modification is also $O(\log n)$.

## Implementation details

### Obtaining a node's maximum level

Simulate adding another level with probability $p$, then take the minimum of the result and the upper limit.

```cpp
int randomLevel() {
  int lv = 1;
  // MAXL = 32, S = 0xFFFF, PS = S * P, P = 1 / 4
  while ((rand() & S) < PS) ++lv;
  return min(MAXL, lv);
}
```

### Search

Search for a node with key `key` in the skip list. Two sentinel nodes can be used to reduce the number of boundary cases.

```cpp
V& find(const K& key) {
  SkipListNode<K, V>* p = head;

  // Find the last node on this level with key less than key, then move down
  for (int i = level; i >= 0; --i) {
    while (p->forward[i]->key < key) {
      p = p->forward[i];
    }
  }
  // The current key is still smaller, so move forward once more
  p = p->forward[0];

  // The node was found
  if (p->key == key) return p->value;

  // The node does not exist; return INVALID
  return tail->value;
}
```

### Insertion

Insert the node `(key, value)`. First perform a search, recording the nodes after which the new node should be inserted, then perform the insertion. The last node on each level with key less than `key` is the node to modify.

```cpp
void insert(const K &key, const V &value) {
  // Record the nodes that need modification
  SkipListNode<K, V> *update[MAXL + 1];

  SkipListNode<K, V> *p = head;
  for (int i = level; i >= 0; --i) {
    while (p->forward[i]->key < key) {
      p = p->forward[i];
    }
    // Node p needs modification on level i
    update[i] = p;
  }
  p = p->forward[0];

  // If the node already exists, update its value
  if (p->key == key) {
    p->value = value;
    return;
  }

  // Obtain the new node's maximum level
  int lv = randomLevel();
  if (lv > level) {
    lv = ++level;
    update[lv] = head;
  }

  // Create a new node
  SkipListNode<K, V> *newNode = new SkipListNode<K, V>(key, value, lv);
  // Insert the new node on levels 0~lv
  for (int i = lv; i >= 0; --i) {
    p = update[i];
    newNode->forward[i] = p->forward[i];
    p->forward[i] = newNode;
  }

  ++length;
}
```

### Deletion

Delete the node with key `key`. First perform a search, recording the nodes preceding the node to be deleted, then perform the deletion. The last node on each level with key less than `key` is the node to modify.

```cpp
bool erase(const K &key) {
  // Record the nodes that need modification
  SkipListNode<K, V> *update[MAXL + 1];

  SkipListNode<K, V> *p = head;
  for (int i = level; i >= 0; --i) {
    while (p->forward[i]->key < key) {
      p = p->forward[i];
    }
    // Node p needs modification on level i
    update[i] = p;
  }
  p = p->forward[0];

  // The node does not exist
  if (p->key != key) return false;

  // Start deletion from the bottom level
  for (int i = 0; i <= level; ++i) {
    // If p is absent from this level, deletion is complete
    if (update[i]->forward[i] != p) {
      break;
    }
    // Unlink p
    update[i]->forward[i] = p->forward[i];
  }

  // Reclaim memory
  delete p;

  // Deleting a node may reduce the maximum level
  while (level > 0 && head->forward[level] == tail) --level;

  // Skip list length
  --length;
  return true;
}
```

### Complete code

The following code implements a map using a skip list. It has not been thoroughly tested and is for reference only.

??? note "Reference code"
    ```cpp
    #include <cassert>
    #include <climits>
    #include <ctime>
    #include <iostream>
    #include <map>
    using namespace std;
    
    template <typename K, typename V>
    struct SkipListNode {
      int level;
      K key;
      V value;
      SkipListNode **forward;
    
      SkipListNode() {}
    
      SkipListNode(K k, V v, int l, SkipListNode *nxt = NULL) {
        key = k;
        value = v;
        level = l;
        forward = new SkipListNode *[l + 1];
        for (int i = 0; i <= l; ++i) forward[i] = nxt;
      }
    
      ~SkipListNode() {
        if (forward != NULL) delete[] forward;
      }
    };
    
    template <typename K, typename V>
    struct SkipList {
      static constexpr int MAXL = 32;
      static constexpr int P = 4;
      static constexpr int S = 0xFFFF;
      static constexpr int PS = S / P;
      static constexpr int INVALID = INT_MAX;
    
      SkipListNode<K, V> *head, *tail;
      int length;
      int level;
    
      SkipList() {
        srand(time(nullptr));
    
        level = length = 0;
        tail = new SkipListNode<K, V>(INVALID, 0, 0);
        head = new SkipListNode<K, V>(INVALID, 0, MAXL, tail);
      }
    
      ~SkipList() {
        delete head;
        delete tail;
      }
    
      int randomLevel() {
        int lv = 1;
        while ((rand() & S) < PS) ++lv;
        return MAXL > lv ? lv : MAXL;
      }
    
      void insert(const K &key, const V &value) {
        SkipListNode<K, V> *update[MAXL + 1];
    
        SkipListNode<K, V> *p = head;
        for (int i = level; i >= 0; --i) {
          while (p->forward[i]->key < key) {
            p = p->forward[i];
          }
          update[i] = p;
        }
        p = p->forward[0];
    
        if (p->key == key) {
          p->value = value;
          return;
        }
    
        int lv = randomLevel();
        if (lv > level) {
          lv = ++level;
          update[lv] = head;
        }
    
        SkipListNode<K, V> *newNode = new SkipListNode<K, V>(key, value, lv);
        for (int i = lv; i >= 0; --i) {
          p = update[i];
          newNode->forward[i] = p->forward[i];
          p->forward[i] = newNode;
        }
    
        ++length;
      }
    
      bool erase(const K &key) {
        SkipListNode<K, V> *update[MAXL + 1];
        SkipListNode<K, V> *p = head;
    
        for (int i = level; i >= 0; --i) {
          while (p->forward[i]->key < key) {
            p = p->forward[i];
          }
          update[i] = p;
        }
        p = p->forward[0];
    
        if (p->key != key) return false;
    
        for (int i = 0; i <= level; ++i) {
          if (update[i]->forward[i] != p) {
            break;
          }
          update[i]->forward[i] = p->forward[i];
        }
    
        delete p;
    
        while (level > 0 && head->forward[level] == tail) --level;
        --length;
        return true;
      }
    
      V &operator[](const K &key) {
        V v = find(key);
        if (v == tail->value) insert(key, 0);
        return find(key);
      }
    
      V &find(const K &key) {
        SkipListNode<K, V> *p = head;
        for (int i = level; i >= 0; --i) {
          while (p->forward[i]->key < key) {
            p = p->forward[i];
          }
        }
        p = p->forward[0];
        if (p->key == key) return p->value;
        return tail->value;
      }
    
      bool count(const K &key) { return find(key) != tail->value; }
    };
    
    int main() {
      SkipList<int, int> L;
      map<int, int> M;
    
      clock_t s = clock();
    
      for (int i = 0; i < 1e5; ++i) {
        int key = rand(), value = rand();
        L[key] = value;
        M[key] = value;
      }
    
      for (int i = 0; i < 1e5; ++i) {
        int key = rand();
        if (i & 1) {
          L.erase(key);
          M.erase(key);
        } else {
          int r1 = L.count(key) ? L[key] : 0;
          int r2 = M.count(key) ? M[key] : 0;
          assert(r1 == r2);
        }
      }
    
      clock_t e = clock();
      cout << "Time elapsed: " << (double)(e - s) / CLOCKS_PER_SEC << endl;
      // about 0.2s
    
      return 0;
    }
    ```

## Optimizing random access in a skip list

Accessing the $k$-th node of a skip list is equivalent to accessing the $k$-th node of the original ordered linked list. Clearly, this takes $O(n)$ time, which is not good enough.

To optimize random access, maintain a length for every forward pointer. Suppose $A$ and $B$ are nodes in the skip list, with $A$ at position $a$ and $B$ at position $b$ $(a < b)$. If a forward pointer from $A$ points to $B$ on some level, its length is $b - a$.

To access the $k$-th node, start at the top level and traverse its list horizontally until the current node's position plus the length of its forward pointer on that level is at least $k$, then move down one level. Repeat until reaching the first level and no further operation is possible. The current node is then the $k$-th node of the skip list.

This allows fast access to the $k$-th element of a skip list. The operation can be proven to take $O(\log n)$ time.

## References

1.  [Skip Lists: A Probabilistic Alternative to Balanced Trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
2.  [Skip List](https://en.wikipedia.org/wiki/Skip_list)
3.  [A Skip List Cookbook](http://cglab.ca/~morin/teaching/5408/refs/p90b.pdf)
