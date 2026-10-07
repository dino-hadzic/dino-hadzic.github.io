#include <iostream>
#include <vector>
using namespace std;
// --8<-- [start:core]
constexpr unsigned MAXN = 1000;  // Broj brojeva koje sortiramo
constexpr unsigned RADIX = 10;   // Baza
constexpr unsigned powRADIX[10] = {1,         10,        100,     1000,
                                   10000,     100000,    1000000, 10000000,
                                   100000000, 1000000000};  // Potencije od RADIX

unsigned get_digit(unsigned value, int digit)  // Izdvoji znamenku na mjestu digit
{
  return (value / powRADIX[digit]) % RADIX;
}

void MSD_radix_sort(unsigned* begin, unsigned* end, int digit)
// Elementi u [begin,end) imaju (u bazi 10) jednake vodeće znamenke
// Treba sortirati samo posljednjih digit znamenki (mjesta digit-1 do 0)
// Primjer poziva: MSD_radix_sort(a,a+n,10)
{
  if (begin >= end)  // Prazan interval
  {
    return;
  }
  /** Counting sort (osobni stil, samo kao primjer) **/
  static unsigned cnt[RADIX + 1],
      tmp[MAXN + 5];  // Različite razine rekurzije ne koriste cnt i tmp istodobno
                      // (sljedeća se razina poziva tek kad trenutna završi), pa static
                      // štedi prostor
  vector<unsigned> beg;
  beg.resize(RADIX + 1);  // Pristupi beg mogli bi se sukobiti, zato lokalna varijabla
  for (int i = 0; i <= RADIX; i++) {
    cnt[i] = beg[i] = 0;  // Čišćenje je dobra navika
  }
  for (unsigned* it = begin; it != end; it++)  // Brojanje
  {
    int bitVal = get_digit(*it, digit - 1);
    cnt[bitVal] += 1;
  }
  beg[0] = 0;  // Izračunaj početni položaj (pomak) za svaku znamenku
  for (int i = 1; i <= RADIX; i++) {
    beg[i] = beg[i - 1] + cnt[i - 1];
  }
  // beg[RADIX] računamo dodatno da bi raspon za i bio upravo [beg[i],beg[i+1])
  // bez brige da beg[i+1] izađe izvan granica
  for (int i = 0; i < RADIX; i++) {
    cnt[i] = 0;
  }
  for (unsigned* it = begin; it != end; it++)  // Rezultat counting sorta stavi u tmp
  {
    unsigned bitVal = get_digit(*it, digit - 1);  // Izdvoji znamenku na mjestu digit - 1
    // Prolazimo izvornim redom; ovo je (cnt[bitVal]+1)-ti element sa znamenkom bitVal na mjestu digit-1
    tmp[beg[bitVal] + cnt[bitVal]] = *it;
    cnt[bitVal]++;
  }
  for (unsigned* it = begin; it != end; it++)  // Kopiraj tmp natrag u izvorni niz
  {
    *it = tmp[it - begin];
  }
  /** Rekurzivno sortiraj sljedeću znamenku u svakoj košari **/
  if (digit == 1)  // Već smo na najnižoj znamenki
  {
    return;
  }
  for (int i = 0; i < RADIX; i++)  // Rekurzivno sortiraj sljedeću znamenku
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
