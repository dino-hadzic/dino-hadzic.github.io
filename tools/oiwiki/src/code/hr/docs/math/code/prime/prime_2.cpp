#include <iostream>

int p[16] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53};
unsigned long long n;
unsigned long long ans,
    ans_num;  // ans je najveći antiprost broj do n (stalno se ažurira), ans_sum je
              // broj djelitelja od ans.

// depth: redni broj prostog broja koji trenutno nabrajamo
// temp: vrijednost koja trenutno ima num djelitelja
// num: trenutni broj djelitelja
// up: eksponent prethodnog prostog broja, gornja granica trenutnog eksponenta
void dfs(int depth, unsigned long long temp, unsigned long long num, int up) {
  if (depth >= 16 || temp > n) return;
  if (num > ans_num) {  // ažuriraj odgovor
    ans = temp;
    ans_num = num;
  }
  if (num == ans_num && ans > temp) ans = temp;  // ažuriraj odgovor
  for (int i = 1; i <= up; i++) {
    if (temp * p[depth] > n)
      break;  // odsijecanje: ako je rezultat s još jednim ovim faktorom veći od ans, sigurno nije najbolje rješenje
    dfs(depth + 1, temp *= p[depth], num * (i + 1),
        i);  // uzmi jedan ovaj faktor i pretražuj dalje za sljedeći faktor
  }
  return;
}

using std::cin;
using std::cout;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  while (cin >> n) {
    ans_num = 0;
    dfs(0, 1, 1, 60);
    cout << ans << '\n';
  }
  return 0;
}
