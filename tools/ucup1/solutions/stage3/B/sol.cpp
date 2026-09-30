// UCup 1, Stage 3 (AMPPZ 2022), B. Bars
// Prihod = 2 * povrsina ispod izlomljene linije kroz odabrane tocke (i, p_i) uz
// obavezne krajeve 1 i n; maksimum daje gornja konveksna ljuska (monotoni stog).
#include <bits/stdc++.h>
using namespace std;

int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        int n;
        scanf("%d", &n);
        vector<long long> p(n + 1);
        for (int i = 1; i <= n; ++i) scanf("%lld", &p[i]);
        vector<int> st;                       // indeksi tocaka na gornjoj ljusci
        for (int i = 1; i <= n; ++i) {
            // izbaci srednju tocku ako nije strogo iznad spojnice susjeda
            while (st.size() >= 2) {
                int a = st[st.size() - 2], b = st.back();
                // vektorski produkt (b-a) x (i-a) >= 0 znaci da je b ispod ili na pravcu a-i
                long long cr = (long long)(b - a) * (p[i] - p[a]) - (p[b] - p[a]) * (long long)(i - a);
                if (cr >= 0) st.pop_back();
                else break;
            }
            st.push_back(i);
        }
        long long odg = 0;
        for (size_t j = 1; j < st.size(); ++j) {
            int a = st[j - 1], b = st[j];
            odg += (long long)(b - a) * (p[a] + p[b]);
        }
        printf("%lld\n", odg);
    }
    return 0;
}
