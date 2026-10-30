// --8<-- [start:mul]
int mulPowerOfTwo(int n, int m) {  // računa n*(2^m)
  return n << m;
}

int divPowerOfTwo(int n, int m) {  // računa n/(2^m)
  return n >> m;
}

// --8<-- [end:mul]
// --8<-- [start:abs]
int Abs(int n) {
  return (n ^ (n >> 31)) - (n >> 31);
  /* n>>31 daje predznak od n: ako je n pozitivan, n>>31 je 0, ako je n negativan, n>>31 je -1
    ako je n pozitivan, n^0=n, broj se ne mijenja; ako je n negativan, imamo n^(-1)
    treba uzeti dvojne komplemente od n i -1 i napraviti XOR,
    rezultat je n s promijenjenim predznakom, jednak apsolutnoj vrijednosti od n umanjenoj za 1; oduzimanjem -1 dobiva se apsolutna vrijednost */
}

// --8<-- [end:abs]
// --8<-- [start:minmax]
// ako je a >= b, (a - b) >> 31 je 0, inače je -1
int max(int a, int b) { return (b & ((a - b) >> 31)) | (a & (~(a - b) >> 31)); }

int min(int a, int b) { return (a & ((a - b) >> 31)) | (b & (~(a - b) >> 31)); }

// --8<-- [end:minmax]
// --8<-- [start:sgn]
bool isSameSign(int x, int y) {  // slučaj s 0 je iznimka
  return (x ^ y) >= 0;
}

// --8<-- [end:sgn]
// --8<-- [start:swap]
void swap(int& a, int& b) { a ^= b ^= a ^= b; }

// --8<-- [end:swap]
// --8<-- [start:get_bit]
// dohvaća b-ti bit od a, najniži bit ima indeks 0
int getBit(int a, int b) { return (a >> b) & 1; }

// --8<-- [end:get_bit]
// --8<-- [start:unset_bit]
// postavlja b-ti bit od a na 0, najniži bit ima indeks 0
int unsetBit(int a, int b) { return a & ~(1 << b); }

// --8<-- [end:unset_bit]
// --8<-- [start:set_bit]
// postavlja b-ti bit od a na 1, najniži bit ima indeks 0
int setBit(int a, int b) { return a | (1 << b); }

// --8<-- [end:set_bit]
// --8<-- [start:flap_bit]
// invertira b-ti bit od a, najniži bit ima indeks 0
int flapBit(int a, int b) { return a ^ (1 << b); }

// --8<-- [end:flap_bit]
namespace popcnt1 {
// --8<-- [start:popcnt1]
// računa Hammingovu težinu od x
int popcount(int x) {
  int cnt = 0;
  while (x) {
    cnt += x & 1;
    x >>= 1;
  }
  return cnt;
}

// --8<-- [end:popcnt1]
}  // namespace popcnt1

namespace popcnt2 {
// --8<-- [start:popcnt2]
// računa Hammingovu težinu od x
int popcount(int x) {
  int cnt = 0;
  while (x) {
    cnt++;
    x -= x & -x;
  }
  return cnt;
}

// --8<-- [end:popcnt2]
}  // namespace popcnt2

#include <cassert>
#include <iostream>
#if defined(_MSC_VER) && !defined(__clang__)
#include <immintrin.h>
#define __builtin_popcount __popcnt
#endif

int main() {
  int a, b;
  std::cin >> a >> b;

  for (int i = 0; i < 16; i++) {
    std::cout << mulPowerOfTwo(a, i) << ' ' << divPowerOfTwo(a, i) << std::endl;
  }

  assert(Abs(-a) == a);
  assert(Abs(a) == a);

  assert(max(a, b) == (a > b ? a : b));
  assert(min(a, b) == (a < b ? a : b));

  std::cout << isSameSign(a, b) << std::endl;

  int x = a, y = b;
  swap(x, y);
  assert(x == b && y == a);

  for (int i = 0; i < 32; i++)
    std::cout << getBit(a, i) << ' ' << unsetBit(a, i) << ' ' << setBit(a, i)
              << ' ' << flapBit(a, i) << std::endl;

  assert(popcnt1::popcount(a) == __builtin_popcount(a));
  assert(popcnt2::popcount(a) == __builtin_popcount(a));

  return 0;
}
