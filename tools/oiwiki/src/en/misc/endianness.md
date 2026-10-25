---
title: Endianness
---

This page briefly introduces the concept and the kinds of byte order (endianness).

## Introduction

Byte order is the storage rule for program objects that span multiple bytes; it describes how the bytes of an object are arranged.

## Kinds

There are two byte orders: little endian and big endian.

For convenience, in the following we take as an example a variable located at `0x100`, of type `int`, with hexadecimal value `0x01234567`. Here `0x01` is the most significant byte and `0x67` is the least significant byte.

### Little endian

Little endian means that the machine stores an object in memory in order from the **least** significant byte to the **most** significant byte.

The variable mentioned above is represented as follows:

| .... | 0x100 | 0x101 | 0x102 | 0x103 | .... |
| ---- | ----- | ----- | ----- | ----- | ---- |
| .... | 67    | 45    | 23    | 01    | .... |

### Big endian

Big endian means that the machine stores an object in memory in order from the **most** significant byte to the **least** significant byte.

The variable mentioned above is represented as follows:

| .... | 0x100 | 0x101 | 0x102 | 0x103 | .... |
| ---- | ----- | ----- | ----- | ----- | ---- |
| .... | 01    | 23    | 45    | 67    | .... |

### Difference between the two orders

In fact, neither of these two byte orders is better or worse than the other. Their names, "little endian" and "big endian", come from the book "Gulliver's Travels". In the book, two factions in Lilliput fight endlessly because they cannot agree on whether an egg should be cracked from the little end or the big end. Just like the argument about cracking eggs, the argument about which byte order to choose is non-technical.

Of course, inconsistent byte order causes binary data to be reversed when transferred between machines of different types. To avoid this, network applications have established a standard guaranteeing that the agreed network standard is used during transmission, rather than the internal representation of a particular machine.

## Conventional choices of order

-   Little endian: x86, ARM processors running Android, iOS, and Windows

-   Big endian: Sun, PPC Mac, Internet
