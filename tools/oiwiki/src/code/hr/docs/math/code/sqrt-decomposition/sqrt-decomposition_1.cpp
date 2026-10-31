#include <iostream>

long long H(int n) {
  long long res = 0;  // pohranjuje rezultat
  int l = 1, r;       // lijevi i desni kraj bloka
  while (l <= n) {
    r = n / (n / l);  // izračunaj desni kraj trenutnog bloka
    // pribroji doprinos ovog bloka rezultatu; množenje s 1LL sprječava prelijevanje
    res += 1LL * (r - l + 1) * (n / l);
    l = r + 1;  // lijevi kraj pomakni na sljedeći blok
  }
  return res;
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int t, n;
  std::cin >> t;
  while (t--) {
    std::cin >> n;
    std::cout << H(n) << '\n';
  }
  return 0;
}
