// UCup 1, Stage 20 (India), L. (1,2) Nim
// Sprague vuce jedan potez, Grundy dva (drugi samo ako je ostalo kamenja).
// Neka je c = broj hrpa s vise od jednog kamena, a n = broj hrpa.
//  - c = 0: sve hrpe su jedinice; Sprague pobjeduje ako n % 3 == 1 (poslije njegova
//    poteza ostaje 3k hrpa i Grundy svaki krug smanjuje za 2, Sprague za 1).
//  - c = 1: Sprague tu hrpu smanji na 1 (ostaje n jedinica) ili 0 (ostaje n-1 jedinica);
//    Grundy na potezu gubi samo ako su sve hrpe jedinice i njihov broj je djeljiv s 3,
//    pa Sprague pobjeduje tocno kad n % 3 != 2.
//  - c >= 2: Sprague jednim potezom moze smanjiti c najvise za 1, pa Grundy uvijek
//    ima >= 1 veliku hrpu i moze (dva poteza) odgovoriti tako da c postane 0 s
//    pravim ostatkom -> Grundy pobjeduje.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        int velikih = 0;
        for (int i = 0; i < n; i++) {
            long long a;
            scanf("%lld", &a);
            if (a > 1) velikih++;
        }
        bool sprague;
        if (velikih == 0) sprague = (n % 3 == 1);
        else if (velikih == 1) sprague = (n % 3 != 2);
        else sprague = false;
        puts(sprague ? "Sprague" : "Grundy");
    }
    return 0;
}
