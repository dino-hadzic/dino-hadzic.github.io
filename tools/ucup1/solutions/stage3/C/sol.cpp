// UCup 1, Stage 3 (AMPPZ 2022), C. Ctrl+C Ctrl+V
// Pojave "ania" su intervali duljine 4; pohlepno mijenjamo posljednje slovo
// najranije zavrsavajuce pojave (pokrivanje intervala tockama).
#include <bits/stdc++.h>
using namespace std;

static char buf[1000005];

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        scanf("%s", buf);
        int l = strlen(buf), odg = 0;
        for (int i = 3; i < l; ++i) {
            if (buf[i - 3] == 'a' && buf[i - 2] == 'n' && buf[i - 1] == 'i' && buf[i] == 'a') {
                ++odg;
                buf[i] = '#';            // promijenjeno slovo vise ne moze biti dio "ania"
            }
        }
        printf("%d\n", odg);
    }
    return 0;
}
