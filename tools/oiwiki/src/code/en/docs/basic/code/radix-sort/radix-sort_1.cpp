#include <iostream>
#include <vector>
using namespace std;
// --8<-- [start:core]
constexpr unsigned MAXN = 1000;  // Number of numbers to sort
constexpr unsigned RADIX = 10;   // Radix
constexpr unsigned powRADIX[10] = {1,         10,        100,     1000,
                                   10000,     100000,    1000000, 10000000,
                                   100000000, 1000000000};  // Powers of RADIX

unsigned get_digit(unsigned value, int digit)  // Extract the digit at position digit
{
  return (value / powRADIX[digit]) % RADIX;
}

void MSD_radix_sort(unsigned* begin, unsigned* end, int digit)
// The elements in [begin,end) share (in base 10) their leading digits
// Only the last digit digits (positions digit-1 down to 0) still need sorting
// Example call: MSD_radix_sort(a,a+n,10)
{
  if (begin >= end)  // Empty range
  {
    return;
  }
  /** Counting sort (personal style, for reference only) **/
  static unsigned cnt[RADIX + 1],
      tmp[MAXN + 5];  // Different recursion levels never use cnt and tmp at the same time
                      // (the next level is called only after the current one is done), so static
                      // saves space
  vector<unsigned> beg;
  beg.resize(RADIX + 1);  // Accesses to beg could conflict, so use a local variable
  for (int i = 0; i <= RADIX; i++) {
    cnt[i] = beg[i] = 0;  // Clearing is a good habit
  }
  for (unsigned* it = begin; it != end; it++)  // Counting
  {
    int bitVal = get_digit(*it, digit - 1);
    cnt[bitVal] += 1;
  }
  beg[0] = 0;  // Compute the starting position (offset) of each digit value
  for (int i = 1; i <= RADIX; i++) {
    beg[i] = beg[i - 1] + cnt[i - 1];
  }
  // beg[RADIX] is computed additionally so that the range for i is simply [beg[i],beg[i+1])
  // without worrying that beg[i+1] goes out of bounds
  for (int i = 0; i < RADIX; i++) {
    cnt[i] = 0;
  }
  for (unsigned* it = begin; it != end; it++)  // Put the counting sort result into tmp
  {
    unsigned bitVal = get_digit(*it, digit - 1);  // Extract the digit at position digit - 1
    // Traversing in original order; this is the (cnt[bitVal]+1)-th element with digit bitVal at position digit-1
    tmp[beg[bitVal] + cnt[bitVal]] = *it;
    cnt[bitVal]++;
  }
  for (unsigned* it = begin; it != end; it++)  // Copy tmp back into the original array
  {
    *it = tmp[it - begin];
  }
  /** Recursively sort the next digit in each bucket **/
  if (digit == 1)  // Already at the lowest digit
  {
    return;
  }
  for (int i = 0; i < RADIX; i++)  // Recursively sort the next digit
  {
    MSD_radix_sort(begin + beg[i], begin + beg[i + 1], digit - 1);
  }
}

// --8<-- [end:core]
unsigned a[MAXN + 5];

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> a[i];
  MSD_radix_sort(a + 1, a + n + 1, 10);
  for (int i = 1; i <= n; i++) cout << a[i] << " \n"[i == n];
}
