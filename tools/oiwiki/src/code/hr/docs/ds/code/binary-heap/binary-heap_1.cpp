#include <iostream>
#include <queue>
using namespace std;

int main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  int t, x;
  cin >> t;
  while (t--) {
    // max-heap, čuva prvu polovicu elemenata (manje vrijednosti)
    priority_queue<int, vector<int>, less<int>> a;
    // min-heap, čuva drugu polovicu elemenata (veće vrijednosti)
    priority_queue<int, vector<int>, greater<int>> b;
    while (cin >> x, x) {
      // ako je operacija upit s brisanjem, ispiši i izbriši vrh max-heapa
      // jer zadatak traži manji od dvaju medijana (za paran broj elemenata postoje dva kandidata)
      // to se malo razlikuje od gornjeg objašnjenja k-tog najvećeg, ali tko je razumio gornje, lako će se snaći
      if (x == -1) {
        cout << a.top() << '\n';
        a.pop();
      }
      // ako je operacija umetanje, prema vrhu max-heapa odaberi heap u koji se umeće
      else {
        if (a.empty() || x <= a.top())
          a.push(x);
        else
          b.push(x);
      }
      // uravnoteži dvostruki heap
      if (a.size() > (a.size() + b.size() + 1) / 2) {
        b.push(a.top());
        a.pop();
      } else if (a.size() < (a.size() + b.size() + 1) / 2) {
        a.push(b.top());
        b.pop();
      }
    }
  }
  return 0;
}
