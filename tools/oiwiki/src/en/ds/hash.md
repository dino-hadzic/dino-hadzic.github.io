---
title: Hash table
---

## Introduction

![](images/hashtable.svg)

A hash table is a data structure that stores data in the form of "key-value" pairs. Storing data as "key-value" pairs means that every key corresponds uniquely to some location in memory. You only need to supply the key you are looking for to quickly find its corresponding value. A hash table can be thought of as an advanced array whose indices can be very large integers, floating-point numbers, strings or even structs.

## Hash function

To make a key correspond to a location in memory, we have to compute an index for the key, i.e. compute where this piece of data should be stored. The function that computes the index from the key is called the hash function. For example, if the key is a person's ID number, the hash function could be the last four digits of the number, or of course the first four digits. The "last digits of a phone number" commonly used in daily life are also a kind of hash function. In practical applications the keys may be more complex things, such as floating-point numbers, strings, structs and so on, in which case a suitable hash function has to be designed for the specific situation. A hash function should be easy to compute and should distribute the computed indices as uniformly as possible.

Once we can compute an index for a key, we know where the value corresponding to each key should be stored. Suppose we use an array a to store the data and the hash function is f; then the pair `(key, value)` should be stored at `a[f(key)]`. Whatever the type and range of the key, `f(key)` is an integer within an acceptable range and can be used as an array index.

In competitive programming the most common case is that the key is an integer. When the range of keys is small, the key can be used directly as the array index, but when the range is large, e.g. when the keys are integers up to $10^9$, a hash table is needed. Usually the key modulo a large prime is used as the index, i.e. the hash function is $f(x)=x \bmod M$.

Another common case is that the key is a string. Since strings cannot be used as array indices, and converting a string into a number also avoids repeated string comparisons, in competitive programming a string is generally not used as the key directly; instead, the hash of the string is computed first and then inserted into the hash table as the key. For string hashes we usually use the idea of positional notation and imagine the string as a number in base $127$. Then for every string $s$ of length $n$ we have:

$x = s_0 \cdot 127^0 + s_1 \cdot 127^1 + s_2 \cdot 127^2 + \dots + s_n \cdot 127^n$

We can take the resulting $x$ modulo $2^{64}$ (i.e. the maximum value of `unsigned long long`). Then the natural overflow of `unsigned long long` is equivalent to the modulo operation, which makes the operations more convenient.

Although this method is simple, it is not perfect. Data can be constructed that makes this method collide (i.e. two strings have the same $x$ modulo $2^{64}$).  
We can use double hashing: choose two large primes $a,b$. Two strings are considered equal if and only if their hash values are equal both modulo $a$ and modulo $b$. This greatly reduces the probability of a hash collision.

## Collisions

If the hash function produced a different index for every key, we would only have to put `(key, value)` at the position given by the index. In reality, however, it often happens that two different keys get the same index from the hash function. Then we need some method to handle collisions. In competitive programming the most common method is chaining.

### Chaining

Chaining is also called open hashing.

With chaining, a linked list is opened at every storage position; if several keys hash to the same position, they are all put into the linked list at that position. On a query the whole list at the corresponding position has to be scanned, comparing the key of each item with the queried key. If the indices range over $1\ldots M$ and the hash table has size $N$, one insertion/query needs an expected $O(\frac{N}{M})$ comparisons.

#### Implementation

=== "C++"
    ```cpp
    constexpr int SIZE = 1000000;
    constexpr int M = 999997;
    
    struct HashTable {
      struct Node {
        int next, value, key;
      } data[SIZE];
    
      int head[M], size;
    
      int f(int key) { return (key % M + M) % M; }
    
      int get(int key) {
        for (int p = head[f(key)]; p; p = data[p].next)
          if (data[p].key == key) return data[p].value;
        return -1;
      }
    
      int modify(int key, int value) {
        for (int p = head[f(key)]; p; p = data[p].next)
          if (data[p].key == key) return data[p].value = value;
      }
    
      int add(int key, int value) {
        if (get(key) != -1) return -1;
        data[++size] = Node{head[f(key)], value, key};
        head[f(key)] = size;
        return value;
      }
    };
    ```

=== "Python"
    ```python
    M = 999997
    SIZE = 1000000
    
    
    class Node:
        def __init__(self, next=None, value=None, key=None):
            self.next = next
            self.value = value
            self.key = key
    
    
    data = [Node() for _ in range(SIZE)]
    head = [0] * M
    size = 0
    
    
    def f(key):
        return key % M
    
    
    def get(key):
        p = head[f(key)]
        while p:
            if data[p].key == key:
                return data[p].value
            p = data[p].next
        return -1
    
    
    def modify(key, value):
        p = head[f(key)]
        while p:
            if data[p].key == key:
                data[p].value = value
                return data[p].value
            p = data[p].next
    
    
    def add(key, value):
        if get(key) != -1:
            return -1
        size = size + 1
        data[size] = Node(head[f(key)], value, key)
        head[f(key)] = size
        return value
    ```

Here is another encapsulated template that can be used like a map and is shorter:

```cpp
struct hash_map {  // hash table template

  struct data {
    long long u;
    int v, nex;
  };  // "forward star" structure (array-based adjacency lists)

  data e[SZ << 1];  // SZ is a const int giving the size
  int h[SZ], cnt;

  int hash(long long u) { return (u % SZ + SZ) % SZ; }

  // we use (u % SZ + SZ) % SZ instead of u % SZ here because
  // the % operator in C++ does not turn negative numbers into positive ones

  int& operator[](long long u) {
    int hu = hash(u);  // get the list head
    for (int i = h[hu]; i; i = e[i].nex)
      if (e[i].u == u) return e[i].v;
    return e[++cnt] = data{u, -1, h[hu]}, h[hu] = cnt, e[cnt].v;
  }

  hash_map() {
    cnt = 0;
    memset(h, 0, sizeof(h));
  }
};
```

Here the hash function is designed for the type of the key and returns a linked-list head used for lookup. In this template we wrote a hash table with key-value pairs of type `(long long, int)` that returns -1 when a nonexistent key is queried. The function `hash_map()` initializes the table at definition time.

### Closed hashing

Closed hashing stores all records directly in the hash table; if a collision occurs, probing continues according to some rule.

For example, linear probing: if a collision occurs at `d`, check `d + 1`, `d + 2`, ... in turn.

#### Implementation

```cpp
constexpr int N = 360007;  // N is the maximum number of elements that can be stored

class Hash {
 private:
  int keys[N];
  int values[N];

 public:
  Hash() { memset(values, 0, sizeof(values)); }

  int& operator[](int n) {
    // returns a reference to the corresponding Hash[Key]
    // set it to a nonzero value; 0 is treated as empty
    int idx = (n % N + N) % N, cnt = 1;
    while (keys[idx] != n && values[idx] != 0) {
      idx = (idx + cnt * cnt) % N;
      cnt += 1;
    }
    keys[idx] = n;
    return values[idx];
  }
};
```

## Example problem

["JLOI2011" Non-repeating Numbers](https://www.luogu.com.cn/problem/P4305)
