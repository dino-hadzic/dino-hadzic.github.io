---
title: Stack
---

## Introduction

![](./images/stack.svg)

A stack is a linear data structure commonly used in competitive programming. This article discusses the stack data structure, not the system stack or stack space used during program execution.

Stack modification and access follow the last-in, first-out principle, so a stack is often called a last-in, first-out (LIFO) list.

??? warning "Warning"
    LIFO means that, among the elements **currently in the container**, the most recently inserted one is removed first.
    
    Consider a stack with these operations:
    
    ```text
    push(1)
    pop(1)
    push(2)
    pop(2)
    ```
    
    Viewed as a whole, 1 enters first and leaves first, while 2 enters last and leaves last. This would make it a FIFO list, which is clearly incorrect.
    
    Therefore, when deciding whether a data structure is LIFO or FIFO, consider the elements currently in the container.

## Implementing a stack with an array

An array can conveniently simulate a stack, as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        int st[N];
        // Here st[0] (that is, *st) stores the element count and the top index
        
        // Push:
        st[++*st] = var1;
        // Access the top:
        int u = st[*st];
        // Pop: check bounds; do not pop when *st == 0
        if (*st) --*st;
        // Clear the stack
        *st = 0;
        ```
    
    === "Python"
        ```python
        st = [0] * N
        # Here st[0] stores the element count and the top index
        
        # Push:
        st[st[0] + 1] = var1
        st[0] = st[0] + 1
        # Access the top:
        u = st[st[0]]
        # Pop: check bounds; do not pop when *st == 0
        if st[0]:
            st[0] = st[0] - 1
        # Clear the stack
        st[0] = 0
        ```

## Stacks in the C++ STL

The C++ STL provides the container `std::stack`. Include the `stack` header before using it.

???+ info "Definition of `stack` in the STL"
    ```cpp
    // clang-format off
    template<
        class T,
        class Container = std::deque<T>
    > class stack;
    ```
    
    `T` is the type of data stored in the stack.
    
    `Container` is the type of the underlying container used to store elements. It must provide the following functions with their usual semantics:
    
    -   `back()`
    -   `push_back()`
    -   `pop_back()`
    
    The STL containers `std::vector`, `std::deque`, and `std::list` satisfy these requirements. If not specified, the underlying container defaults to `std::deque`.

The STL `stack` container provides several member functions. Commonly used ones include:

-   Element access
    -   `st.top()` returns the top element
-   Modifiers
    -   `st.push()` inserts its argument at the top
    -   `st.pop()` removes the top element
-   Capacity
    -   `st.empty()` returns whether the stack is empty
    -   `st.size()` returns the number of elements

The container `std::stack` also provides several operators. One commonly used operator is assignment `=`, as in this example:

```cpp
// Create two stacks, st1 and st2
std::stack<int> st1, st2;

// Push 1 onto st1
st1.push(1);

// Assign st1 to st2
st2 = st1;

// Print the top element of st2
cout << st2.top() << endl;
// Output: 1
```

## Implementing a stack with a Python list

In Python, you can simulate a stack using a list:

???+ note "Implementation"
    ```python
    st = [5, 1, 4]
    
    # Use append() to add elements to the top
    st.append(2)
    st.append(3)
    # >>> st
    # [5, 1, 4, 2, 3]
    
    # Use pop to remove the top element
    st.pop()
    # >>> st
    # [5, 1, 4, 2]
    
    # Use clear to empty the stack
    st.clear()
    ```

## References

1.  [std::stack - zh.cppreference.com](https://zh.cppreference.com/w/cpp/container/stack)
