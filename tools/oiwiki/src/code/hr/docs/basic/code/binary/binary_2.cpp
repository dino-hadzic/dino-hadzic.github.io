#include <iostream>
using namespace std;

int a[1000005];
int n, m;

bool check(int k) {  // provjera izvedivosti, k je visina pile
  long long sum = 0;
  for (int i = 1; i <= n; i++)       // provjeri svako stablo
    if (a[i] > k)                    // ako je stablo više od pile
      sum += (long long)(a[i] - k);  // zbroji duljinu odrezanog drva
  return sum >= m;                   // ako je dosegnuta najmanja duljina, izvedivo je
}

int find() {
  int l = 0, r = 1e9 + 1;   // interval je zatvoren slijeva i otvoren zdesna, pa 10^9 treba uvećati za 1
                            // održavamo check(l) istinito, a check(r) lažno
  while (l + 1 < r) {       // dok dvije točke nisu susjedne
    int mid = (l + r) / 2;  // uzmi sredinu
    if (check(mid))         // ako je izvedivo
      l = mid;              // podigni pilu
    else
      r = mid;  // inače spusti pilu
  }
  return l;  // vrati lijevu vrijednost
}

int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; i++) cin >> a[i];
  cout << find();
  return 0;
}
