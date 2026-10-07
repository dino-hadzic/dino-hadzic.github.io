---
title: Introduction to persistent data structures
---

author: morris821028

## Introduction

A persistent data structure preserves every historical version and supports immutability when performing operations.

## Types of persistence

### Partial persistence (Partially Persistent)

All versions can be accessed, but only the latest version can be modified.

### Full persistence (Fully Persistent)

All versions can be both accessed and modified.

If merging two historical versions is also supported, the structure is called confluently persistent.

## Applications

### Computational geometry

Computational geometry has many offline algorithms, such as sweep line algorithms that answer all queries in one pass with excellent time complexity. However, if queries must be processed online, sweeping once per query degrades the query complexity from logarithmic to linear time. Persistence offers another approach: use the sweep line's timeline as the basis for changes and make the relevant structures persistent. If queries can navigate this timeline in logarithmic time, the original problem can be solved dynamically.

### String processing

Persistence enables highly efficient merging and avoids performance degradation caused by creating many repeated strings, allowing various operations to take far less than linear time. For example, C++ rope is a persistent data structure. This is not limited to strings: persistence can be useful whenever the data being processed contains extensive repetition.

### Version rollback

In practice, this corresponds to redo/undo in most applications. If a database or state changes use complex structures for efficiency (unlike hash or set structures, where reversing an operation takes constant or logarithmic time), persistent structures reduce the cost of redo/undo to roll changes back quickly.

A database itself can roll back in constant time by recording only the changed parts. At the application layer, most implementations discard the cache and recompute a new structure. Sometimes a rollback changes m items but recomputing the structure costs n+m. If n and m differ greatly, repeated rollbacks feel very slow to the user.

### Functional programming

Functional programming requires specialized data structures that match the language's properties. Immutability is particularly important for parallel environments and debugging. For example, object-oriented Java introduced the stream class in Java 8, supporting functional-style syntax and features such as lazy evaluation and infinite value domains.

## References

-   <https://en.wikipedia.org/wiki/Persistent_data_structure>
-   MIT course <https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-854j-advanced-algorithms-fall-2005/lecture-notes/persistent.pdf>
