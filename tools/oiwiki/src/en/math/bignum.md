---
title: Arbitrary-precision arithmetic (bignum)
---

> Too long, didn't read: grab the ready-made template at the end…

## Definition

Arbitrary-precision arithmetic, also called big integer (bignum) arithmetic, uses certain algorithmic structures to support operations on larger integers (numbers whose magnitude exceeds the language's built-in integer types).

## Introduction

Bignum problems contain many small details, and the implementation has many subtleties too.

So today let's implement a simple calculator together.

???+ note "Task"
    Input: an expression of the form `a <op> b`.
    
    -   `a` and `b` are non-negative decimal integers of length at most $1000$;
    -   `<op>` is a single character (`+`, `-`, `*` or `/`) denoting the operation.
    -   The integers and the operator are separated by a single space.
    
    Output: the result of the operation.
    
    -   For the operations `+`, `-` and `*`, output one line with the result;
    -   For the operation `/`, output two lines: the quotient and the remainder.
    -   It is guaranteed that all results are non-negative integers.

## Storage

In everyday implementations, big numbers are represented by strings, where each character represents one decimal digit. Therefore one can say that bignum arithmetic is really a special kind of string processing.

When the string is read in, the most significant digit is at the beginning of the string (at the position with the small index). However, by convention the position with the smallest index stores the **least significant** digit, i.e. the reversed string is stored. The reason is that the length of the number may change, but we want digits of the same weight to always stay aligned (for example, we want all the ones digits at index `[0]`, all the tens digits at index `[1]`…); at the same time, addition, subtraction and multiplication generally start from the ones digit (recall long arithmetic from elementary school), all of which gives ample justification for "reversed storage".

We will follow this convention from now on. Define a constant `LEN = 1004` as the maximum length the program can hold.

From this it is easy to write the code that reads a big number:

```cpp
void clear(int a[]) {
  for (int i = 0; i < LEN; ++i) a[i] = 0;
}

void read(int a[]) {
  static char s[LEN + 1];
  scanf("%s", s);

  clear(a);

  int len = strlen(s);
  // as described above, reverse
  for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
  // s[i] - '0' is exactly the digit that s[i] represents
  // some may find it more natural to think of it as ord(s[i]) - ord('0')
}
```

Output is also done in the reverse order of storage. Since we do not want to output leading zeros, here we search downward from the most significant digit for the first non-zero digit and start outputting from there; the stopping condition is `i >= 1` rather than `i >= 0` because when the whole number equals $0$ we still want to output a single character `0`.

```cpp
void print(int a[]) {
  int i;
  for (i = LEN - 1; i >= 1; --i)
    if (a[i] != 0) break;
  for (; i >= 0; --i) putchar(a[i] + '0');
  putchar('\n');
}
```

Put together, this is a complete "parrot" program that echoes its input.

??? note "`copycat.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    int main() {
      read(a);
      print(a);
    
      return 0;
    }
    ```

## The four basic operations

The four basic operations differ in difficulty. The simplest are bignum addition and subtraction, followed by bignum–single-precision (ordinary `int`) multiplication and bignum–bignum multiplication, and finally bignum–bignum division.

We will implement all the required functionality in this order.

### Addition

Bignum addition is really just long addition.

![](./images/plus.svg)

That is, starting from the least significant digit, add the digits of the two addends at the corresponding positions and check whether the sum reaches or exceeds $10$. If it does, handle the carry: increase the result at the next higher position by $1$ and decrease the result at the current position by $10$.

```cpp
void add(int a[], int b[], int c[]) {
  clear(c);

  // in bignum implementations, the maximum array length LEN is usually made a bit larger than the possible input
  // and the last few iterations of the loop are skipped; this saves a lot of handling of boundary cases
  // since the actual input does not exceed 1000 digits, looping up to LEN - 1 = 1003 here is sufficient
  for (int i = 0; i < LEN - 1; ++i) {
    // add the digits at the corresponding position
    c[i] += a[i] + b[i];
    if (c[i] >= 10) {
      // carry
      c[i + 1] += 1;
      c[i] -= 10;
    }
  }
}
```

Try combining this with the previous part and you get an addition calculator.

??? note "`adder.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN], b[LEN], c[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    void add(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] + b[i];
        if (c[i] >= 10) {
          c[i + 1] += 1;
          c[i] -= 10;
        }
      }
    }
    
    int main() {
      read(a);
      read(b);
    
      add(a, b, c);
      print(c);
    
      return 0;
    }
    ```

### Subtraction

Bignum subtraction is likewise just long subtraction.

![](./images/subtraction.svg)

Starting from the ones digit, subtract digit by digit, and when a negative value is encountered, borrow $1$ from the next higher position. The overall idea is exactly the same as for addition.

```cpp
void sub(int a[], int b[], int c[]) {
  clear(c);

  for (int i = 0; i < LEN - 1; ++i) {
    // subtract digit by digit
    c[i] += a[i] - b[i];
    if (c[i] < 0) {
      // borrow
      c[i + 1] -= 1;
      c[i] += 10;
    }
  }
}
```

Replace `add()` in the previous program with `sub()` and you have a subtraction calculator.

??? note "`subtractor.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN], b[LEN], c[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    void sub(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] - b[i];
        if (c[i] < 0) {
          c[i + 1] -= 1;
          c[i] += 10;
        }
      }
    }
    
    int main() {
      read(a);
      read(b);
    
      sub(a, b, c);
      print(c);
    
      return 0;
    }
    ```

Try it: input `1 2` – the output is `/9999999`. Hey, did **OI Wiki** just hand me fake code…

In fact, the code above can only handle the case where the minuend $a$ is greater than or equal to the subtrahend $b$. Handling the case where the minuend is smaller than the subtrahend, i.e. $a<b$, is simple.

$a-b=-(b-a)$

To compute $b-a$, since $b>a$, we can call the `sub` function from the code above as `sub(b,a,c)`. To obtain $a-b$, just put a minus sign in front of the result.

### Multiplication

#### Bignum – single precision

Bignum multiplication is really just long… wait, wait!

First consider a simple case: one of the factors is an ordinary `int`. Is there a simple way to handle this?

An intuitive idea is to directly multiply each digit of $a$ by $b$. Numerically this method is correct, but the result does not conform to decimal notation, so it needs to be rearranged into its normal form.

The rearrangement, too, proceeds from the ones digit upward, handling the carry digit by digit. But here the carry can be very large, even far larger than $9$, because each digit after multiplication may reach the order of magnitude of $9b$. So the carry here can no longer be handled by simply performing $-10$; instead it must be computed via the quotient and remainder of division by $10$. See the code comments for details, or refer to the figure below, which shows the process of multiplying the big number $1337$ by the single-precision number $42$.

![](./images/multiplication-short.png)

Of course, for this very reason, the method requires special attention to the range of the factor $b$. If it is of the same order of magnitude as $10^9$ (or the upper bound of the corresponding integer type), bignum–single-precision multiplication should be used with caution.

```cpp
void mul_short(int a[], int b, int c[]) {
  clear(c);

  for (int i = 0; i < LEN - 1; ++i) {
    // directly multiply the i-th digit of a by the factor and add it to the result
    c[i] += a[i] * b;

    if (c[i] >= 10) {
      // handle the carry
      // c[i] / 10, i.e. the quotient of the division, becomes the carry increment
      c[i + 1] += c[i] / 10;
      // and c[i] % 10, i.e. the remainder of the division, becomes the value left at the current position
      c[i] %= 10;
    }
  }
}
```

#### Bignum – bignum

If both factors are big numbers, long multiplication comes into its own again.

Recall that each step of long multiplication actually computes the sum of several terms $a \times b_i \times 10^i$. For example, computing $1337 \times 42$ computes $1337 \times 2 \times 10^0 + 1337 \times 4 \times 10^1$.

So we can decompose $b$ into all of its digits, each of which is a single-precision number, multiply each of them by $a$, then shift them left to their respective positions and add them up to obtain the answer. Of course, at the end the carries also need to be handled in the same way as in the previous example.

![](./images/multiplication-long.png)

Note that this process is not quite the same as long multiplication: our algorithm does not carry during each multiplication step but keeps all the results at their corresponding positions and handles the carries all at once at the end; this does not affect the result, however.

```cpp
void mul(int a[], int b[], int c[]) {
  clear(c);

  for (int i = 0; i < LEN - 1; ++i) {
    // here we directly compute the i-th digit of the result (from least significant) and handle the carry along the way
    // the i-th iteration adds to c[i] the sum of all products a[p] * b[q] with p + q = i
    // the effect is the same as performing the computation in the figure above and summing at the end, just a shorter implementation
    for (int j = 0; j <= i; ++j) c[i] += a[j] * b[i - j];

    if (c[i] >= 10) {
      c[i + 1] += c[i] / 10;
      c[i] %= 10;
    }
  }
}
```

### Division

One way to implement bignum division is long division.

![](./images/division.svg)

Long division can actually be viewed as a process of repeated subtraction. For example, the computation of the tens digit of the quotient in the figure above can be understood as follows: after subtracting $12$ from $45$ three times, the result becomes smaller than $12$ and no further subtraction is possible, so this digit is $3$.

To reduce redundant operations, we determine in advance the length $l_a$ of the dividend and the length $l_b$ of the divisor, and compute the quotient starting from index $l_a - l_b$, from the higher digits to the lower ones. This is the same as aligning the most significant digit of the first multiplication with the most significant digit of the dividend when computing by hand.

The reference program implements a function `greater_eq()` that checks whether the divisor can be subtracted once more from the dividend, with index `last_dg` as its least significant digit, while staying non-negative. Then, for each digit of the quotient, we repeatedly call `greater_eq()` and, when it holds, subtract the divisor from the remainder using bignum subtraction, thereby simulating the process of long division.

```cpp
// whether the divisor b can be subtracted once more from the dividend a, with index last_dg as its least significant digit, while staying non-negative
// len is the length of the divisor b, to avoid recomputing it
bool greater_eq(int a[], int b[], int last_dg, int len) {
  // the remaining part of the dividend may be longer than the divisor, but by at most 1 digit, so this check suffices
  if (a[last_dg + len] != 0) return true;
  // from the most significant digit to the least significant, compare digit by digit
  for (int i = len - 1; i >= 0; --i) {
    if (a[last_dg + i] > b[i]) return true;
    if (a[last_dg + i] < b[i]) return false;
  }
  // the equal case is also feasible
  return true;
}

void div(int a[], int b[], int c[], int d[]) {
  clear(c);
  clear(d);

  int la, lb;
  for (la = LEN - 1; la > 0; --la)
    if (a[la - 1] != 0) break;
  for (lb = LEN - 1; lb > 0; --lb)
    if (b[lb - 1] != 0) break;
  if (lb == 0) {  // the divisor must not be zero
    puts("> <");
    return;
  }

  // c is the quotient
  // d is the remaining part of the dividend, which naturally becomes the remainder when the algorithm ends
  for (int i = 0; i < la; ++i) d[i] = a[i];
  for (int i = la - lb; i >= 0; --i) {
    // compute the i-th digit of the quotient
    while (greater_eq(d, b, i, lb)) {
      // if we can subtract, subtract
      // this section is a bignum subtraction
      for (int j = 0; j < lb; ++j) {
        d[i + j] -= b[j];
        if (d[i + j] < 0) {
          d[i + j + 1] -= 1;
          d[i + j] += 10;
        }
      }
      // increase this digit of the quotient by 1
      c[i] += 1;
      // go back to the beginning of the loop and check again
    }
  }
}
```

## Beginner part complete!

Combining the implementations of the four basic operations introduced above, we can complete the calculator program mentioned at the beginning.

??? note "`calculator.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN], b[LEN], c[LEN], d[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    void add(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] + b[i];
        if (c[i] >= 10) {
          c[i + 1] += 1;
          c[i] -= 10;
        }
      }
    }
    
    void sub(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] - b[i];
        if (c[i] < 0) {
          c[i + 1] -= 1;
          c[i] += 10;
        }
      }
    }
    
    void mul(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        for (int j = 0; j <= i; ++j) c[i] += a[j] * b[i - j];
    
        if (c[i] >= 10) {
          c[i + 1] += c[i] / 10;
          c[i] %= 10;
        }
      }
    }
    
    bool greater_eq(int a[], int b[], int last_dg, int len) {
      if (a[last_dg + len] != 0) return true;
      for (int i = len - 1; i >= 0; --i) {
        if (a[last_dg + i] > b[i]) return true;
        if (a[last_dg + i] < b[i]) return false;
      }
      return true;
    }
    
    void div(int a[], int b[], int c[], int d[]) {
      clear(c);
      clear(d);
    
      int la, lb;
      for (la = LEN - 1; la > 0; --la)
        if (a[la - 1] != 0) break;
      for (lb = LEN - 1; lb > 0; --lb)
        if (b[lb - 1] != 0) break;
      if (lb == 0) {
        puts("> <");
        return;
      }
    
      for (int i = 0; i < la; ++i) d[i] = a[i];
      for (int i = la - lb; i >= 0; --i) {
        while (greater_eq(d, b, i, lb)) {
          for (int j = 0; j < lb; ++j) {
            d[i + j] -= b[j];
            if (d[i + j] < 0) {
              d[i + j + 1] -= 1;
              d[i + j] += 10;
            }
          }
          c[i] += 1;
        }
      }
    }
    
    int main() {
      read(a);
    
      char op[4];
      scanf("%s", op);
    
      read(b);
    
      switch (op[0]) {
        case '+':
          add(a, b, c);
          print(c);
          break;
        case '-':
          sub(a, b, c);
          print(c);
          break;
        case '*':
          mul(a, b, c);
          print(c);
          break;
        case '/':
          div(a, b, c, d);
          print(c);
          print(d);
          break;
        default:
          puts("> <");
      }
    
      return 0;
    }
    ```

## Digit packing

### Introduction

In ordinary bignum addition, subtraction and multiplication, we split the numbers taking part in the operation into individual digits and compute with them.

For example, when computing $8192\times 42$, if we follow the bignum–bignum multiplication procedure, what we actually compute is $(8000+100+90+2)\times(40+2)$.

When there are many digits, there are also many split-off pieces, and the efficiency of bignum arithmetic drops.

Is there any way to optimize this?

Note that the way the number is split does not affect the final result, so we can merge several digits together.

### Procedure

Take the example above again: if we split off two digits at a time, we can split it as $(8100+92)\times 42$.

Such a split does not affect the final result, but since there are fewer split-off numbers, the computation becomes more efficient.

Viewed from the perspective of [numeral systems](./numeral-sys/base.md), this process means computing in a larger base (splitting two digits at a time above can be regarded as computing in base $100$), thereby reducing the number of digits taking part in the computation and increasing efficiency.

This is the idea of **digit packing** (压位高精度, several digits per cell).

Below we give the code for bignum addition with digit packing to further illustrate how it is implemented:

??? note "Reference implementation of addition with digit packing"
    ```cpp
    // here the arrays a, b, c are numbers in base p
    // when finally outputting the answer, the number must be converted to decimal
    void add(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] + b[i];
        if (c[i] >= p) {  // in ordinary bignum arithmetic, p=10
          c[i + 1] += 1;
          c[i] -= p;
        }
      }
    }
    ```

### Efficient long division with digit packing

When using digit packing, if we still use the method described above to find each quotient digit by trial, the number of trials will be very large and the constant factor enormous. For example, in base 10000 each digit needs on average 5000 trials, which is an unacceptably large constant. So we need a more efficient way of estimating the quotient.

We can use a `double` as an intermediary. Suppose the dividend has 4 digits, $a_4,a_3,a_2,a_1$, and the divisor has 3 digits, $b_3,b_2,b_1$; then we only need to estimate one quotient digit: in base $base$, estimate the quotient with the expression $\dfrac{a_4 base + a_3}{b_3 + b_2 base^{-1} + (b_1+1)base^{-2}}$. For the multi-digit case, just wrap the single-digit version in a loop. Since the divisor takes part in the estimate with 3 digits of precision, it is guaranteed that the estimated quotient q' and the actual quotient q satisfy $q-1 \le q' \le q$, so each digit needs at most two trials even in the worst case. At the same time, however, $base^3$ must be within the effective precision of a `double`, i.e. $base^3 < 2^{53}$, so when applying this method it is recommended not to exceed base 32768; otherwise insufficient precision easily produces deviations that lead to errors.

Moreover, since the estimated quotient is always less than or equal to the actual quotient, there is room for further optimization. In the vast majority of cases each digit is estimated only once; then, when estimating the next digit, the quotient obtained may be greater than or equal to base due to the error in the previous digit, but that does not matter – it suffices to handle all the carries at once at the end. For example, suppose the base is 10 and we compute $395081/9876$; the trial steps are as follows:

1.  First, the trial gives $3950/988=3$, so $395081-(9876 \times 3 \times 10^1) = 98801$; an error appeared in this step, but we ignore it and continue with the next step.
2.  For the remainder 98801, the trial gives $9880/988=10$, so $98801-(9876 \times 10 \times 10^0) = 41$, which is the final remainder.
3.  Add up the results of the trials and handle the carry: $3 \times 10^1 + 10 \times 10^0 = 40$ is the exact quotient.

Although the method looks simple, it is easy to fall into pitfalls in the concrete implementation, so below we provide a thoroughly verified implementation with no known problems for reference; the details to watch out for are written in the comments.

??? note "Reference implementation of efficient long division with digit packing"
    ```cpp
    // full template and implementation: https://baobaobear.github.io/post/20210228-bigint1/
    // subtract b multiplied by mul and shifted left by offset from this number; serves division
    BigIntSimple &sub_mul(const BigIntSimple &b, int mul, int offset) {
      if (mul == 0) return *this;
      int borrow = 0;
      // unlike subtraction, borrow can be very large, so the subtraction style cannot be used
      for (size_t i = 0; i < b.v.size(); ++i) {
        borrow += v[i + offset] - b.v[i] * mul - BIGINT_BASE + 1;
        v[i + offset] = borrow % BIGINT_BASE + BIGINT_BASE - 1;
        borrow /= BIGINT_BASE;
      }
      // if there is still a borrow, keep processing
      for (size_t i = b.v.size(); borrow; ++i) {
        borrow += v[i + offset] - BIGINT_BASE + 1;
        v[i + offset] = borrow % BIGINT_BASE + BIGINT_BASE - 1;
        borrow /= BIGINT_BASE;
      }
      return *this;
    }
    
    BigIntSimple div_mod(const BigIntSimple &b, BigIntSimple &r) const {
      BigIntSimple d;
      r = *this;
      if (absless(b)) return d;
      d.v.resize(v.size() - b.v.size() + 1);
      // precompute the reciprocal of the divisor's top three digits + 1; if the top three digits are a3,a2,a1,
      // then db is the reciprocal of a3+a2/base+(a1+1)/base^2, and finally each quotient digit is estimated by multiplication
      // this method works within the int32 range when BIGINT_BASE<=32768
      // but even with int64 it is only usable for BIGINT_BASE<=131072 (limited by the precision of double)
      // it guarantees that the estimate q' and the actual result q satisfy q'<=q<=q'+1
      // so each digit needs only one trial on average, and the carries are handled all at once afterwards
      // if a larger base is to be used, a different trial scheme is needed
      double t = (b.get((unsigned)b.v.size() - 2) +
                  (b.get((unsigned)b.v.size() - 3) + 1.0) / BIGINT_BASE);
      double db = 1.0 / (b.v.back() + t / BIGINT_BASE);
      for (size_t i = v.size() - 1, j = d.v.size() - 1; j <= v.size();) {
        int rm = r.get(i + 1) * BIGINT_BASE + r.get(i);
        int m = std::max((int)(db * rm), r.get(i + 1));
        r.sub_mul(b, m, j);
        d.v[j] += m;
        if (!r.get(i + 1))  // check whether the top digit is already 0, to avoid extreme cases
          --i, --j;
      }
      r.trim();
      // fix the lowest digit of the result
      int carry = 0;
      while (!r.absless(b)) {
        r.subtract(b);
        ++carry;
      }
      // fix the carry of every digit
      for (size_t i = 0; i < d.v.size(); ++i) {
        carry += d.v[i];
        d.v[i] = carry % BIGINT_BASE;
        carry /= BIGINT_BASE;
      }
      d.trim();
      d.sign = sign * b.sign;
      return d;
    }
    
    BigIntSimple operator/(const BigIntSimple &b) const {
      BigIntSimple r;
      return div_mod(b, r);
    }
    
    BigIntSimple operator%(const BigIntSimple &b) const {
      BigIntSimple r;
      div_mod(b, r);
      return r;
    }
    ```

## Karatsuba multiplication

Let $n$ denote the number of digits of a big number; then bignum–bignum long multiplication takes $O(n^2)$ time. This section introduces an algorithm with better time complexity, proposed by the Soviet (Russian) mathematician Anatoly Karatsuba; it is a divide-and-conquer algorithm.

Consider two big decimal integers $x$ and $y$, both with $n$ digits (leading zeros allowed). Pick any $0 < m < n$ and write

$$
\begin{aligned}
x &= x_1 \cdot 10^m + x_0, \\
y &= y_1 \cdot 10^m + y_0, \\
x \cdot y &= z_2 \cdot 10^{2m} + z_1 \cdot 10^m + z_0,
\end{aligned}
$$

where $x_0, y_0, z_0, z_1 < 10^m$. We get

$$
\begin{aligned}
z_2 &= x_1 \cdot y_1, \\
z_1 &= x_1 \cdot y_0 + x_0 \cdot y_1, \\
z_0 &= x_0 \cdot y_0.
\end{aligned}
$$

Observe that

$$
z_1 = (x_1 + x_0) \cdot (y_1 + y_0) - z_2 - z_0,
$$

so to compute $z_1$ we only need to compute $(x_1 + x_0) \cdot (y_1 + y_0)$ and subtract $z_0$ and $z_2$ from it.

The formula above is in fact the core of Karatsuba's algorithm: it turns a multiplication problem of length $n$ into $3$ subproblems of smaller length. If we set $m = \left\lceil \dfrac n 2 \right\rceil$ and denote the time Karatsuba's algorithm takes to multiply two $n$-digit integers by $T(n)$, then $T(n) = 3 \cdot T \left(\left\lceil \dfrac n 2 \right\rceil\right) + O(n)$, and by the master theorem $T(n) = \Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})$.

The whole process can be implemented recursively. For clarity, the code below implements polynomial multiplication via Karatsuba's algorithm and handles all the carries at the end.

??? note "karatsuba_mulc.cpp"
    ```cpp
    int *karatsuba_polymul(int n, int *a, int *b) {
      if (n <= 32) {
        // for small sizes compute directly, to avoid the efficiency loss of further recursion
        int *r = new int[n * 2 + 1]();
        for (int i = 0; i <= n; ++i)
          for (int j = 0; j <= n; ++j) r[i + j] += a[i] * b[j];
        return r;
      }
    
      int m = n / 2 + 1;
      int *r = new int[m * 4 + 1]();
      int *z0, *z1, *z2;
    
      z0 = karatsuba_polymul(m - 1, a, b);
      z2 = karatsuba_polymul(n - m, a + m, b + m);
    
      // compute z1
      // temporary modification, restored after the computation
      for (int i = 0; i + m <= n; ++i) a[i] += a[i + m];
      for (int i = 0; i + m <= n; ++i) b[i] += b[i + m];
      z1 = karatsuba_polymul(m - 1, a, b);
      for (int i = 0; i + m <= n; ++i) a[i] -= a[i + m];
      for (int i = 0; i + m <= n; ++i) b[i] -= b[i + m];
      for (int i = 0; i <= (m - 1) * 2; ++i) z1[i] -= z0[i];
      for (int i = 0; i <= (n - m) * 2; ++i) z1[i] -= z2[i];
    
      // combine z0, z1, z2 to obtain the result
      for (int i = 0; i <= (m - 1) * 2; ++i) r[i] += z0[i];
      for (int i = 0; i <= (m - 1) * 2; ++i) r[i + m] += z1[i];
      for (int i = 0; i <= (n - m) * 2; ++i) r[i + m * 2] += z2[i];
    
      delete[] z0;
      delete[] z1;
      delete[] z2;
      return r;
    }
    
    void karatsuba_mul(int a[], int b[], int c[]) {
      int *r = karatsuba_polymul(LEN - 1, a, b);
      memcpy(c, r, sizeof(int) * LEN);
      for (int i = 0; i < LEN - 1; ++i)
        if (c[i] >= 10) {
          c[i + 1] += c[i] / 10;
          c[i] %= 10;
        }
      delete[] r;
    }
    ```

??? note "About `new` and `delete`"
    See [Memory pool](../contest/common-tricks.md#memory-pool).

However, such an implementation has a problem: in base $b$, every coefficient of the polynomial may reach the order of magnitude of $n \cdot b^2$, which may cause integer overflow in a digit-packed implementation; whereas if the carries are handled during the polynomial multiplication, the results of $x_1 + x_0$ and $y_1 + y_0$ may reach $2 \cdot b^m$, gaining one extra digit (and if the computation is done in the form $x_1 - x_0$, negative numbers have to be handled specially). Therefore the implementation approach must be chosen according to the actual application scenario.

## Efficient big integer multiplication based on polynomials

If the data size reaches $10^{10^5}$ or more, ordinary bignum multiplication may exceed the time limit. This section introduces how to optimize such multiplication using polynomials.

An $n$-digit decimal integer $a$ can be viewed as a polynomial $A=a_{0} 10^0+a_{1} 10^1+\cdots+a_{n-1} 10^{n-1}$ whose coefficients are all integers less than $10$. In this way we have turned the multiplication of two integers into the multiplication of two polynomials.

Ordinary polynomial multiplication still has time complexity $O(n^2)$, but it can be optimized with algorithms from the polynomial chapter such as the [fast Fourier transform](poly/fft.md) and the [number-theoretic transform](poly/ntt.md); after optimization the time complexity is $O(n\log n)$.

## Wrapper class

[Here](https://paste.ubuntu.com/p/7VKYzpC7dn/) is a ready-made big integer class, and [here](https://github.com/Baobaobear/MiniBigInteger/blob/main/bigint_tiny.h) is an ultra-mini implementation class supporting dynamic length and the four basic operations.

??? note "Here is another template"
    ```cpp
    constexpr int MAXN = 9999;
    // MAXN is the largest number in one cell
    constexpr int MAXSIZE = 10024;
    // MAXSIZE is the number of cells
    constexpr int DLEN = 4;
    
    // DLEN records how many digits are packed
    struct Big {
      int a[MAXSIZE], len;
      bool flag;  // marks the sign '-'
    
      Big() {
        len = 1;
        memset(a, 0, sizeof a);
        flag = false;
      }
    
      Big(const int);
      Big(const char*);
      Big(const Big&);
      Big& operator=(const Big&);
      Big operator+(const Big&) const;
      Big operator-(const Big&) const;
      Big operator*(const Big&) const;
      Big operator/(const int&) const;
      // TODO: Big / Big;
      Big operator^(const int&) const;
      // TODO: Big ^ Big;
    
      // TODO: bit operations on Big;
    
      int operator%(const int&) const;
      // TODO: Big ^ Big;
      bool operator<(const Big&) const;
      bool operator<(const int& t) const;
      void print() const;
    };
    
    Big::Big(const int b) {
      int c, d = b;
      len = 0;
      // memset(a,0,sizeof a);
      CLR(a);
      while (d > MAXN) {
        c = d - (d / (MAXN + 1) * (MAXN + 1));
        d = d / (MAXN + 1);
        a[len++] = c;
      }
      a[len++] = d;
    }
    
    Big::Big(const char* s) {
      int t, k, index, l;
      CLR(a);
      l = strlen(s);
      len = l / DLEN;
      if (l % DLEN) ++len;
      index = 0;
      for (int i = l - 1; i >= 0; i -= DLEN) {
        t = 0;
        k = i - DLEN + 1;
        if (k < 0) k = 0;
        g(j, k, i) t = t * 10 + s[j] - '0';
        a[index++] = t;
      }
    }
    
    Big::Big(const Big& T) : len(T.len) {
      CLR(a);
      f(i, 0, len) a[i] = T.a[i];
      // TODO: overload here?
    }
    
    Big& Big::operator=(const Big& T) {
      CLR(a);
      len = T.len;
      f(i, 0, len) a[i] = T.a[i];
      return *this;
    }
    
    Big Big::operator+(const Big& T) const {
      Big t(*this);
      int big = len;
      if (T.len > len) big = T.len;
      f(i, 0, big) {
        t.a[i] += T.a[i];
        if (t.a[i] > MAXN) {
          ++t.a[i + 1];
          t.a[i] -= MAXN + 1;
        }
      }
      if (t.a[big])
        t.len = big + 1;
      else
        t.len = big;
      return t;
    }
    
    Big Big::operator-(const Big& T) const {
      int big;
      bool ctf;
      Big t1, t2;
      if (*this < T) {
        t1 = T;
        t2 = *this;
        ctf = true;
      } else {
        t1 = *this;
        t2 = T;
        ctf = false;
      }
      big = t1.len;
      int j = 0;
      f(i, 0, big) {
        if (t1.a[i] < t2.a[i]) {
          j = i + 1;
          while (t1.a[j] == 0) ++j;
          --t1.a[j--];
          // WTF?
          while (j > i) t1.a[j--] += MAXN;
          t1.a[i] += MAXN + 1 - t2.a[i];
        } else
          t1.a[i] -= t2.a[i];
      }
      t1.len = big;
      while (t1.len > 1 && t1.a[t1.len - 1] == 0) {
        --t1.len;
        --big;
      }
      if (ctf) t1.a[big - 1] = -t1.a[big - 1];
      return t1;
    }
    
    Big Big::operator*(const Big& T) const {
      Big res;
      int up;
      int te, tee;
      f(i, 0, len) {
        up = 0;
        f(j, 0, T.len) {
          te = a[i] * T.a[j] + res.a[i + j] + up;
          if (te > MAXN) {
            tee = te - te / (MAXN + 1) * (MAXN + 1);
            up = te / (MAXN + 1);
            res.a[i + j] = tee;
          } else {
            up = 0;
            res.a[i + j] = te;
          }
        }
        if (up) res.a[i + T.len] = up;
      }
      res.len = len + T.len;
      while (res.len > 1 && res.a[res.len - 1] == 0) --res.len;
      return res;
    }
    
    Big Big::operator/(const int& b) const {
      Big res;
      int down = 0;
      gd(i, len - 1, 0) {
        res.a[i] = (a[i] + down * (MAXN + 1)) / b;
        down = a[i] + down * (MAXN + 1) - res.a[i] * b;
      }
      res.len = len;
      while (res.len > 1 && res.a[res.len - 1] == 0) --res.len;
      return res;
    }
    
    int Big::operator%(const int& b) const {
      int d = 0;
      gd(i, len - 1, 0) d = (d * (MAXN + 1) % b + a[i]) % b;
      return d;
    }
    
    Big Big::operator^(const int& n) const {
      Big t(*this), res(1);
      int y = n;
      while (y) {
        if (y & 1) res = res * t;
        t = t * t;
        y >>= 1;
      }
      return res;
    }
    
    bool Big::operator<(const Big& T) const {
      int ln;
      if (len < T.len) return true;
      if (len == T.len) {
        ln = len - 1;
        while (ln >= 0 && a[ln] == T.a[ln]) --ln;
        if (ln >= 0 && a[ln] < T.a[ln]) return true;
        return false;
      }
      return false;
    }
    
    bool Big::operator<(const int& t) const {
      Big tee(t);
      return *this < tee;
    }
    
    void Big::print() const {
      printf("%d", a[len - 1]);
      gd(i, len - 2, 0) { printf("%04d", a[i]); }
    }
    
    void print(const Big& s) {
      int len = s.len;
      printf("%d", s.a[len - 1]);
      gd(i, len - 2, 0) { printf("%04d", s.a[i]); }
    }
    
    char s[100024];
    ```

## Exercises

-   [NOIP 2012 国王游戏 (King's Game)](https://loj.ac/problem/2603)
-   [SPOJ - Fast Multiplication](http://www.spoj.com/problems/MUL/en/)
-   [SPOJ - GCD2](http://www.spoj.com/problems/GCD2/)
-   [UVa - Division](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1024)
-   [UVa - Fibonacci Freeze](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=436)
-   [Codeforces - Notepad](http://codeforces.com/contest/17/problem/D)

## References and links

1.  [Karatsuba algorithm - Wikipedia](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
