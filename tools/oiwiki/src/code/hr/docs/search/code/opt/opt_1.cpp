#include <iostream>
constexpr int N = 16;
int is_working[N] = {0};  // je li posao dodijeljen
int tm[N][N];             // vrijeme potrebno za posao
int cost_time_total_min;  // najmanji ukupni zbroj vremena za n poslova

// i je redni broj osobe, count je ukupni trošak poslova
void work(int i, int count, int n) {
  // Ako je i premašio najveći broj poslova koji se mogu dodijeliti, raspodjela je gotova; ako je count
  // manji od dosadašnjeg cost_time_total_min, ažuriraj cost_time_total_min
  if (i > n && count < cost_time_total_min) {
    cost_time_total_min = count;
    return;
  }
  // ideja backtrackinga
  if (count < cost_time_total_min) {
    // j je redni broj posla
    for (int j = 1; j <= n; j++) {
      // ako posao nije dodijeljen, is_working = 0
      if (is_working[j] == 0) {
        // dodijeli posao, is_working = 1
        is_working[j] = 1;
        // prijeđi na osobu i + 1
        work(i + 1, count + tm[i][j], n);
        // nakon završene iteracije vrati se na prethodnu osobu i ponovno raspodijeli ovaj posao
        // vrati is_working[j] na 0
        is_working[j] = 0;
      }
    }
  }
}

using std::cin;
using std::cout;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      cin >> tm[i][j];
    }
    cost_time_total_min += tm[i][i];
  }
  work(1, 0, n);
  cout << cost_time_total_min << '\n';
  return 0;
}
