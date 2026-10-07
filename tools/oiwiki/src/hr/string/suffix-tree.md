---
title: Sufiksno stablo
---

Sufiksno stablo (suffix tree) struktura je podataka koja održava sve sufikse stringa.

## Oznake

Neka je $S$ string za koji gradimo sufiksno stablo, duljine $n$ i nad abecedom $\Sigma$.

Neka $S[i]$ označava znak stringa $S$ na poziciji $i$, pri čemu je $1 \le i \le n$.

Neka $S [l, r]$ označava string dobiven iz stringa $S$ uzimanjem znakova od $l$-tog do $r$-tog, koji zovemo podstringom stringa $S$.

Sa $S [i, n]$ označavamo sufiks stringa $S$ koji počinje na $i$, a sa $S [1, i]$ prefiks stringa $S$ koji završava na $i$.

## Definicija

**Sufiksni trie** stringa $S$ jest trie dobiven umetanjem svih sufiksa stringa S. U sufiksnom trieju čvoru x odgovara string dobiven spajanjem znakova na putu od korijena do x. Čvorove
sufiksnog trieja koji odgovaraju nekom sufiksu stringa $S$ zovemo sufiksnim čvorovima.

Lako je uočiti korisno svojstvo sufiksnog trieja: njegovi čvorovi osim korijena prihvaćaju točno sve različite neprazne podstringove stringa $S$. No za njegovu su izgradnju potrebni vrijeme i prostor $O(n^2)$, što je često neprihvatljivo. Zato uvodimo sufiksno stablo.

Označimo ključnima sve čvorove sufiksnog trieja s više od jednog djeteta i sve sufiksne čvorove. Komprimirani trie koji zadržava samo ključne čvorove, a lance ostalih čvorova sažima u jedan brid, zove se **sufiksno stablo (suffix tree)**. Ako ključnima označimo samo čvorove s više od jednog djeteta i listove, komprimirani trie koji zadržava samo te čvorove zove se **implicitno sufiksno stablo (implicit suffix tree)**. Očito se implicitno sufiksno stablo dobiva dodatnim sažimanjem sufiksnog stabla.

U sufiksnom i implicitnom sufiksnom stablu svaki brid odgovara jednom stringu. Svakom čvoru $x$ osim korijena odgovara skup stringova: string dobiven prolaskom od korijena do roditelja čvora $x$, označenog s $fa_x$, spajamo s bilo kojim nepraznim prefiksom stringa na bridu od $fa_x$ do $x$; taj skup označavamo sa $str_x$. U implicitnom sufiksnom stablu sufiks kojem ne odgovara nijedan čvor zovemo **implicitnim sufiksom**.

Slika slijeva nadesno prikazuje sufiksni trie, sufiksno stablo i implicitno sufiksno stablo za string $\texttt{cabab}$.

![suffix-tree\_cabab1.png](./images/suffix-tree1.png)

Promotrimo umetanje sufiksa stringa $S$ u sufiksni trie jednog po jednog. Od drugog umetanja nadalje svaki put dodajemo najviše jedan čvor s više od jednog djeteta i jedan sufiksni čvor. Zato sufiksno stablo ima najviše $2n$ čvorova, što je vrlo dobra ograda.

## Izgradnja sufiksnog stabla

### Dinamičko dodavanje znakova na početak

Stablo parent veza sufiksnog automata (SAM) izgrađenog za obrnuti string jest sufiksno stablo izvornog stringa. Zato je dovoljno dodavati znakove obrnutog stringa u SAM jedan po jedan.

???+ note "Referentna implementacija"
    ```cpp
    struct SuffixAutomaton {
      int tot, lst;
      int siz[N << 1];
      int buc[N], id[N << 1];
    
      struct Node {
        int len, link;
        int ch[26];
      } st[N << 1];
    
      SuffixAutomaton() : tot(1), lst(1) {}
    
      void extend(int ch) {
        int cur = ++tot, p = lst;
        lst = cur;
        siz[cur] = 1, st[cur].len = st[p].len + 1;
        for (; p && !st[p].ch[ch]; p = st[p].link) st[p].ch[ch] = cur;
        if (!p)
          st[cur].link = 1;
        else {
          int q = st[p].ch[ch];
          if (st[q].len == st[p].len + 1)
            st[cur].link = q;
          else {
            int pp = ++tot;
            st[pp] = st[q];
            st[pp].len = st[p].len + 1;
            st[cur].link = st[q].link = pp;
            for (; p && st[p].ch[ch] == q; p = st[p].link) st[p].ch[ch] = pp;
          }
        }
      }
    } SAM;
    ```

### Dinamičko dodavanje znakova na kraj

Ukkonenov algoritam algoritam je inkrementalne konstrukcije. Redom umećemo znakove stringa $S$ u stablo i nakon svakog umetanja ispravno održavamo trenutačno sufiksno stablo.

#### Naivni algoritam

Najprije predstavljamo izgradnju grubim pretraživanjem, a postupak ilustriramo stringom $\texttt {abbbc}$.

Na početku stvorimo korijen, čvor $0$. Za svaki brid održavamo interval $[l,r]$ koji označava da je string na njemu $S[l,r]$. Održavamo i broj dosad umetnutih znakova $m$, početno $0$.

Najprije umećemo znak $\texttt a$: iz čvora $0$ dodamo brid do novog čvora, označen s $[1,\infty]$. Ovdje je $\infty$ vrlo velika vrijednost koja predstavlja kraj stringa, pa taj brid automatski obuhvaća novoumetnute znakove.

![suffix-tree\_a.webp](./images/suffix-tree2.webp)

Zatim umećemo $\texttt b$ i ponovno dodajemo brid iz $0$, označen s $[2,\infty⁡]$. Značenje postojećeg brida $[1,\infty]$ automatski se mijenja: pomicanjem kraja stringa njegov string prelazi iz $\texttt a$ u $\texttt {ab}$. To je ispravno jer se svaki prethodni sufiks već pojavljuje kao list u stablu; dovoljno je na kraj svakog lista dodati trenutačni znak.

![suffix-tree\_ab.webp](./images/suffix-tree3.webp)

Sada umećemo još jedan $\texttt b$. No $\texttt b$ već je podstring dosad umetnutog stringa, pa stablo već sadrži $\texttt b$. Ne radimo ništa, nego bilježimo $k$ tako da je $S[k,m]$ trenutačno najdulji implicitni sufiks.

![suffix-tree\_abb.webp](./images/suffix-tree4.webp)

Zatim umećemo još jedan $\texttt b$. Budući da prethodni $\texttt b$ nije eksplicitno umetnut, vrijedi $k=3$, pa je sufiks koji treba umetnuti $\texttt {bb}$. Tražeći $\texttt {bb}$ od korijena prema dolje, vidimo da se i on već nalazi u stablu. Ponovno ne radimo ništa.

![suffix-tree\_abbb.webp](./images/suffix-tree5.webp)

Primijetimo da nismo obrađivali sufikse koji počinju nakon $k$. Ako je $S[k,m]$ implicitni sufiks, onda je za $l>k$ i $S[l,m]$ implicitni sufiks. Naime, budući da je $S[k,m]$ implicitan, postoji znak $c$ takav da je $S[k, m] + c$ podstring stringa $S$. Tada je i $S [ l, m] + c$ podstring stringa $S$, pa se prema definiciji implicitnog sufiksnog stabla ni $S[ l, m]$ ne pojavljuje kao list.

Zatim umećemo $\texttt c$. Budući da je $k=3$, od korijena tražimo $\texttt {bbc}$, kojeg nema u stablu. U čvoru koji predstavlja $\texttt {bb}$ treba dodati izlazni brid $[5,\infty]$. No taj čvor zapravo ne postoji: njegova je pozicija unutar brida. Zato razdvojimo brid i stvorimo novi čvor, a na njemu dodamo traženi izlazni brid. Umetanje je uspjelo, pa postavimo $k\to k+1$ jer $S[k,m]$ više nije implicitan sufiks.

![suffix-tree\_abbbc1.webp](./images/suffix-tree6.webp)

Budući da se $k$ promijenio, ponavljamo postupak dok se ponovno ne pojavi implicitni sufiks ili dok ne bude $k>m$ (u ovom primjeru događa se potonje).

![suffix-tree\_abbbc2.webp](./images/suffix-tree7.webp)

Izgradnja je završena.

Svako grubo traženje i umetanje od korijena u najgorem slučaju traje $O(n)$, pa ukupna složenost iznosi $O(n^2)$.

#### Sufiksne veze

Naivni je algoritam spor ponajprije zato što svaka operacija extend od korijena traži mjesto umetanja najduljeg implicitnog sufiksa. Umjesto toga zapamtimo tu poziciju. Parom $(now,rem)$ opisujemo trenutačno najdulji implicitno predstavljen sufiks $S[k,m]$. Od čvora $now$ krenemo njegovim izlaznim bridom koji počinje znakom $S[m-rem+1]$ i prijeđemo duljinu $rem$; dosegnuta pozicija jednoznačno predstavlja string. Pri umetanju novog znaka dovoljno je tražiti od pozicije opisane s $now$ i $rem$.

Sada pri $k\to k + 1$ trebamo samo ažurirati $(now,rem)$. Ako je $now=0$, postavimo $rem \to rem-1$ jer je duljina sljedećeg sufiksa jednaka duljini upravo umetnutog uz dodatak $-1$. Inače, neka $str_{now}$ odgovara podstringu $S[l,r]$. Pronađemo čvor $now'$ koji odgovara $S[l+1,r]$ i postavimo $now\to now'$.

Najprije lema: za svaki čvor $x$ implicitnog sufiksnog stabla koji nije ni list ni korijen postoji drugi čvor $y$ koji nije list, takav da se $str_y$ dobiva brisanjem prvog znaka podstringa koji odgovara $str_x$.

Dokaz. Neka je $s$ string dobiven brisanjem prvog znaka iz $str_x$. Prema definiciji implicitnog sufiksnog stabla postoje dva različita znaka $c_1,c_2$ takva da su $str_x + c1$ i $str_x + c_2$ podstringovi stringa $S$. Zato su i $s + c_1$ i $s + c_2$ podstringovi stringa $S$, pa $s$ u sufiksnom trieju također odgovara ključnom čvoru s grananjem. Dakle, u implicitnom sufiksnom trieju postoji $y$ takav da je $str_y=s$. Time je lema dokazana.

Na temelju te leme definiramo $\operatorname{Link}(x)=y$, što zovemo **sufiksnom vezom (suffix link)** čvora x. Dakle, $now'=\operatorname{Link}(now)$ uvijek postoji. Preostaje izračunati $\operatorname{Link}$ za svaki čvor implicitnog sufiksnog stabla koji nije ni korijen ni list.

#### Ukkonenov algoritam

Cjelokupan postupak Ukkonenova algoritma izgleda ovako:

Za izgradnju implicitnog sufiksnog stabla dodajemo znakove stringa $S$ slijeva nadesno. Pretpostavimo da je korijen $0$, da je implicitno sufiksno stablo stringa $S[1, m]$ već izgrađeno i da su njegove sufiksne veze održane. Najdulji implicitni sufiks stringa $S [1, m]$ jest $S [k, m]$, na poziciji $(now, rem)$ u stablu. Neka je $S [m + 1] = x$; sada treba dodati znak $x$. Svakom sufiksu stringa $S [1, m]$ treba na kraj dodati $x$. Svi eksplicitni sufiksi odgovaraju listovima čiji ulazni bridovi imaju desni kraj $\infty$, pa ih ne treba održavati. Dovoljno je razmotriti kako dodavanje znaka x na kraj implicitnih sufiksa mijenja stablo. Najprije promatramo $S [k, m]$. Postoje dva slučaja:

1.  Na poziciji $(now, rem)$ već postoji prijelaz znakom $x$. Oblik sufiksnog stabla ne mijenja se. Budući da se $S [k, m+1]$ već pojavljuje u sufiksnom stablu, za $l > k$ pojavljuje se i $S [ l, m + 1]$. Dovoljno je postaviti $rem\to rem + 1$, bez drugih izmjena.
2.  Na poziciji $(now, rem)$ ne postoji prijelaz znakom $x$. Ako je $(now, rem)$ čvor stabla, dodamo mu izlazni brid $x$; inače na toj poziciji razdvajanjem stvorimo novi čvor i dodamo mu izlazni brid $x$. Za $l > k$ još ne znamo kako $S [ l, m]$ utječe na oblik sufiksnog stabla, pa nastavljamo sa $S [k + 1, m]$. Poziciju $S [k + 1, m]$ u stablu pronalazimo ovako: ako $now$ nije $0$, slijedimo sufiksnu vezu postavljanjem $now = \operatorname{Link}(now)$; inače postavimo $rem\to rem − 1$. Na kraju postavimo $k\to k + 1$ i ponovimo postupak.

Svaki korak traje konstantno vrijeme, a algoritam završava nakon umetanja svih znakova, pa je vremenska složenost $O(n)$.

Ukkonenov algoritam konstruira samo implicitno sufiksno stablo stringa $S$, koje u nekim problemima može biti manje korisno od sufiksnog stabla. Kad je potrebno, na kraj stringa $S$ dodamo znak koji se još nije pojavio. Tada svi sufiksi stringa S bijektivno odgovaraju listovima stabla.

???+ note "Referentna implementacija"
    ```cpp
    struct SuffixTree {
      int ch[M + 5][RNG + 1], st[M + 5], len[M + 5], link[M + 5];
      int s[N + 5];
      int now{1}, rem{0}, n{0}, tot{1};
    
      SuffixTree() { len[0] = inf; }
    
      int new_node(int s, int le) {
        ++tot;
        st[tot] = s;
        len[tot] = le;
        return tot;
      }
    
      void extend(int x) {
        s[++n] = x;
        ++rem;
        for (int lst{1}; rem;) {
          while (rem > len[ch[now][s[n - rem + 1]]])
            rem -= len[now = ch[now][s[n - rem + 1]]];
          int &v{ch[now][s[n - rem + 1]]}, c{s[st[v] + rem - 1]};
          if (!v || x == c) {
            lst = link[lst] = now;
            if (!v)
              v = new_node(n, inf);
            else
              break;
          } else {
            int u{new_node(st[v], rem - 1)};
            ch[u][c] = v;
            ch[u][x] = new_node(n, inf);
            st[v] += rem - 1;
            len[v] -= rem - 1;
            lst = link[lst] = v = u;
          }
          if (now == 1)
            --rem;
          else
            now = link[now];
        }
      }
    } Tree;
    ```

## Primjene

Put između svakog čvora sufiksnog stabla i korijena predstavlja neprazan podstring stringa $S$, što je korisno u mnogim problemima sa stringovima.

DFS poredak sufiksnog stabla jest sufiksno polje. Zato svakom podstablu odgovara interval sufiksnog polja. Najdulji zajednički prefiks dvaju sufiksa jest LCA njihovih listova. Zato se svojstvo polja height sufiksnog polja može shvatiti ovako: LCA skupa čvorova u stablu jednak je LCA-u čvorova s najmanjim i najvećim DFS indeksom.

## Primjeri zadataka

### [Luogu P3804: Predložak za sufiksni automat (SAM)](https://www.luogu.com.cn/problem/P3804)

Opis zadatka:

Zadan je string $S$ sastavljen samo od malih slova.

Među svim podstringovima stringa $S$ čiji broj pojavljivanja nije $1$ pronađite najveći umnožak broja pojavljivanja i duljine podstringa.

??? note "Rješenje"
    Izgradimo implicitno sufiksno stablo nakon umetanja završnog znaka. Svaki put koji počinje u korijenu čini podstring. Broj pojavljivanja eksplicitnog sufiksa jednak je broju listova u podstablu odgovarajućeg čvora. Implicitne sufikse ne treba razmatrati: svaki ima jednak broj pojavljivanja kao eksplicitni sufiks koji odgovara prvom čvoru ispod njega, a nužno je kraći. Obiđemo cijelo stablo i za svaki čvor izračunamo broj listova u njegovu podstablu te duljinu puta do korijena. Ako je broj listova $>1$, ažuriramo odgovor. Složenost je $O(|S||\Sigma|)$.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/string/code/suffix-tree/suffix-tree_1.cpp"
    ```

### [CF235C Cyclical Quest](https://codeforces.com/problemset/problem/235/C)

Opis zadatka: zadan je glavni string $S$ od malih slova i $n$ upitnih stringova. Za svaki upitni string $x_i$ pronađite ukupan broj pojavljivanja svih njegovih cikličkih pomaka u glavnom stringu.

??? note "Rješenje"
    Izgradimo implicitno sufiksno stablo nakon umetanja završnog znaka.
    
    Prolazimo cikličkim pomacima i bilježimo duljinu prefiksa koji možemo pronaći u stablu.
    
    Ponavljamo postupak sličan Ukkonenovu algoritmu i pratimo trenutačno dosegnutu poziciju podudaranja $(now,rem)$. Svaki put pokušamo umetnuti sljedeći znak; ako uspijemo, nastavljamo, a inače izlazimo iz petlje.
    
    Ako smo uspješno podudarili cijeli trenutačni ciklički pomak i on se prije nije pojavio, ažuriramo odgovor.
    
    Pri prelasku na sljedeći ciklički pomak brišemo prvi znak trenutačno podudarenog podstringa. To točno odgovara postavljanju $now \to \operatorname{Link}(now)$. Ako je $now=1$, jednostavno postavimo $rem\to rem-1$.
    
    Složenost je $O(|S||\Sigma|+\sum|x_i|)$.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/string/code/suffix-tree/suffix-tree_2.cpp"
    ```

## Literatura

1.  Dai Chenxin, „Izgradnja sufiksnih stabala”, rad nacionalnog pripremnog tima iz 2021.
2.  [Čarolija sufiksnih stabala - blog EternalAlexandera](https://www.luogu.com.cn/blog/EternalAlexander/xuan-ku-hou-zhui-shu-mo-shu)
