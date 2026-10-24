#include <iostream>
#include <vector>
using namespace std;

// --8<-- [start:core]
pair<bool, vector<int>> findCycle(
    vector<int>
        nxt)  // nxt[i] je čvor na koji i pokazuje u jednostruko vezanoj listi (0-indeksirano), -1 znači da ne pokazuje ni na jedan čvor
{
  int fast = 0, slow = 0;
  do  // prvo provjeri postoji li ciklus
  {
    if (nxt[fast] == -1 || nxt[nxt[fast]] == -1) {
      return make_pair(false, vector<int>());  // nema ciklusa
    }
    fast = nxt[nxt[fast]];
    slow = nxt[slow];
  } while (fast != slow);
  slow = 0;
  while (slow != fast)  // zatim pronađi ulaz u ciklus
  {
    slow = nxt[slow];
    fast = nxt[fast];
  }
  vector<int> cycle;
  do  // na kraju pronađi cijeli ciklus
  {
    cycle.push_back(slow);
    slow = nxt[slow];
  } while (slow != fast);
  return make_pair(true, cycle);
}

// --8<-- [end:core]
int main() {
  int n;
  while (cin >> n) {
    vector<int> nxt;
    nxt.resize(n);
    for (int i = 0; i < n; i++) {
      cin >> nxt[i];
    }
    pair<bool, vector<int>> cycle = findCycle(nxt);
    if (cycle.first) {
      cout << "Cycle:";
      for (int i = 0; i < cycle.second.size(); i++) {
        cout << " " << cycle.second[i];
      }
      cout << endl;
    } else {
      cout << "No cycle.\n";
    }
  }
}
