---
title: Dvostruki pokazivači
---

Ova stranica kratko predstavlja tehniku dvostrukih pokazivača (two pointers).

## Uvod

Dvostruki pokazivači jednostavna su, a opet fleksibilna tehnika i ideja: sami lako rješavaju neke specifične probleme, a u kombinaciji s drugim algoritmima imaju raznovrsne primjene.

Kao što ime kaže, dvostruki pokazivači znače istodobnu upotrebu dvaju pokazivača; u nizovima i vezanim listama pokazuju na položaje, a u stablima i grafovima na čvorove, te se pomiču u istom smjeru ili jedan prema drugome kako bi se održavale i prikupljale informacije.

Pogledajmo sada nekoliko konkretnih načina upotrebe dvostrukih pokazivača.

## Održavanje informacije o intervalu

Ako se ne kombiniraju s drugim strukturama podataka, najjednostavniji oblik održavanja informacije o intervalu dvostrukim pokazivačima jest održavanje informacije koja ima određenu monotonost i kod koje je dodavanje i uklanjanje jednog elementa lako obraditi, kao što su zbroj pozitivnih brojeva, umnožak pozitivnih cijelih brojeva itd.

### Primjer 1

???+ note "Primjer 1 [LeetCode 713. Podnizovi s umnoškom manjim od K](https://leetcode-cn.com/problems/subarray-product-less-than-k/)"
    Zadan je niz pozitivnih cijelih brojeva $\mathit{nums}$ duljine $n$ i cijeli broj $k$; odredite broj uzastopnih podnizova tog niza čiji je umnožak manji od $k$.
    
    Pri tome je $1 \leq n \leq 3 \times 10^4, 1 \leq nums[i] \leq 1000, 0 \leq k \leq 10^6$.

#### Postupak

Neka su dva pokazivača $l,r$, a dodatna varijabla $\mathit{tmp}$ pamti umnožak svih brojeva u $[l,r]$. Na početku su $l,r$ oba skroz lijevo; prvo pomičemo $r$ udesno dok prvi put ne otkrijemo $\mathit{tmp}\geq k$, tada fiksiramo $r$ i pomičemo $l$ udesno dok ne bude $\mathit{tmp}\lt k$. Tako je za svaki $r$ pokazivač $l$ lijeva granica do koje se može proširiti, a zbog monotonosti umnoška pozitivnih cijelih brojeva broj intervala s desnim krajem $r$ koji zadovoljavaju uvjet zadatka iznosi $r-l+1$.

#### Implementacija

```cpp
int numSubarrayProductLessThanK(vector<int>& nums, int k) {
  long long ji = 1ll, ans = 0;
  int l = 0;
  for (int i = 0; i < nums.size(); ++i) {
    ji *= nums[i];
    while (l <= i && ji >= k) ji /= nums[l++];
    ans += i - l + 1;
  }
  return ans;
}
```

Održavanje informacije o intervalu dvostrukim pokazivačima može se kombinirati i s drugim strukturama podataka, poput razlika (difference array), monotonog reda, segment treea, perzistentnog segment treea itd. Osim toga, tehniku dvostrukih pokazivača u algoritam ugrađuje i Mo algoritam: u Mo algoritmu se upiti offline sortiraju, a zatim se u pravilu dvama pokazivačima bilježi interval koji se trenutačno obrađuje te se informacija o intervalu postupno ažurira kako se pokazivači korak po korak pomiču.

### Primjer 2

Pogledajmo sada primjer upotrebe dvostrukih pokazivača na stablu u kombinaciji s razlikama na stablu:

???+ note "Primjer 2 [Luogu P3066 Running Away From the Barn G](https://www.luogu.com.cn/problem/P3066)"
    Zadano je korijensko stablo s $n$ čvorova, bridovi imaju težine, čvorovi su označeni brojevima od 1 do $n$, a čvor 1 je korijen stabla. Zadan je i parametar $t$; za svaki čvor $u$ stabla odredite koliko čvorova u podstablu čvora $u$ ima udaljenost do $u$ ne veću od $t$. Ograničenja: $1\leq n \leq 2\times 10^5,1 \leq t \leq 10^{18},1 \leq p_i \lt i,1 \leq w_i \leq 10^{12}$

#### Postupak

Od korijena DFS-om obilazimo cijelo stablo i stogom pamtimo lanac od korijena do trenutačnog čvora; jedan pokazivač $u$ pokazuje na trenutačni čvor, a drugi pokazivač $p$ na čvor najmanje dubine među čvorovima čija udaljenost do $u$ nije veća od $t$. Pamtimo udaljenosti do korijena i svaki put binarnim pretraživanjem određujemo $p$. Tada $u$ daje doprinos svakom čvoru na putu od $p$ do $u$, što se može zabilježiti razlikama na stablu.  
Pazite da se $p$ ne smije izravno pomicati grubom silom, jer bi se vremenska složenost mogla degradirati na $O(n^2)$.

### Zadaci za vježbu

[LeetCode 1438. Najdulji uzastopni podniz s apsolutnom razlikom ne većom od ograničenja](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

## Uparivanje podnizova

???+ note "Primjer 3 [LeetCode 524. Najdulja riječ iz rječnika dobivena brisanjem slova](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/)"
    Zadan je string $s$ i niz stringova $\mathit{dictionary}$ kao rječnik; pronađite i vratite najdulji string iz rječnika koji se može dobiti brisanjem nekih znakova iz $s$.

### Postupak

U ovoj vrsti problema treba usporediti stringove $s$ i $t$ i odrediti je li $t$ podniz (subsequence) stringa $s$. Za rješenje je dovoljno prvo postaviti dva pokazivača, jedan $i$ na početak $s$, a drugi $j$ na početak $t$. Ako je $s[i]=t[j]$, to znači da je za $j$-ti znak stringa $t$ pronađen prvi odgovarajući znak u $s$ i može se nastaviti provjeravati ostatak, pa se $i$ i $j$ istodobno uvećaju za jedan. Ako navedena jednakost ne vrijedi, $j$-ti znak stringa $t$ još nije uparen, pa se uvećava samo $i$ i traži se dalje u ostatku stringa $s$. Na kraju, ako je $j$ došao do položaja iza posljednjeg znaka, cijeli se string može upariti, tj. $t$ je podniz stringa $s$; inače nije.

### Implementacija

```cpp
string findLongestWord(string s, vector<string>& dictionary) {
  sort(dictionary.begin(), dictionary.end());
  int mx = 0, r = 0;
  string ans = "";
  for (int i = dictionary.size() - 1; i >= 0; i--) {
    r = 0;
    for (int j = 0; j < s.length(); ++j) {
      if (s[j] == dictionary[i][r]) r++;
    }
    if (r == dictionary[i].length()) {
      if (r >= mx) {
        mx = r;
        ans = dictionary[i];
      }
    }
  }
  return ans;
}
```

Ovaj način, u kojem dva pokazivača pokazuju na različite objekte koji se zatim postupno uspoređuju, može se primijeniti i u nekim DP-ovima.

## Iskorištavanje sortiranosti niza

Vrlo često dvostruki pokazivači na nizu ispravno postižu cilj upravo zbog nekih svojstava niza, a najčešće se iskorištava sortiranost niza.

???+ note "Primjer 4 [LeetCode 167. Zbroj dvaju brojeva II – ulazni niz je sortiran](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)"
    Zadan je niz cijelih brojeva `numbers` sortiran **uzlazno**; pronađite u njemu dva broja čiji je zbroj jednak ciljnom broju `target`.

### Postupak

I ovaj je problem klasična primjena dvostrukih pokazivača; iako je i binarno pretraživanje praktično, ono u vremenskoj složenosti ima dodatni faktor $\log{n}$, a kod nije dovoljno sažet.

Predstavimo pristup dvostrukim pokazivačima: budući da tražimo dva broja koji ne mogu biti na istom položaju, njihovi su položaji nužno jedan lijevo, a drugi desno. Budući da je zbroj dvaju brojeva fiksan, što je manji od njih veći, to je veći od njih manji. Uzimajući u obzir ta svojstva, možemo im se približavati s obaju krajeva.

Prvo pretpostavimo da je odgovor upravo 1 i n. Ako otkrijemo $num[1]+num[n]\gt \mathit{target}$, znači da jedan od elemenata treba smanjiti, a $\mathit{num}[1]$ se više ne može smanjiti, pa pokazivač koji pokazuje na $n$ umanjimo za jedan kako bi se veći broj smanjio.

Slično, ako otkrijemo $num[1]+num[n]\lt \mathit{target}$, znači da jedan od elemenata treba povećati, a $\mathit{num}[n]$ se više ne može povećati, pa pokazivač koji pokazuje na 1 uvećamo za jedan kako bi se manji broj povećao.

Poopćeno: ako dva pokazivača trenutačno pokazuju na $l,r$ i vrijedi $l\lt r$, onda ako je $num[l]+num[r]\gt \mathit{target}$, umanjimo $r$ za jedan, a ako je $num[l]+num[r]\lt \mathit{target}$, uvećamo $l$ za jedan. Tako se $l$ stalno pomiče udesno, $r$ stalno ulijevo i na kraju se oba približe odgovoru.

### Implementacija

```cpp
vector<int> twoSum(vector<int>& numbers, int target) {
  int r = numbers.size() - 1, l = 0;
  vector<int> ans;
  ans.clear();
  while (l < r) {
    if (numbers[l] + numbers[r] > target)
      r--;
    else if (numbers[l] + numbers[r] == target) {
      ans.push_back(l + 1), ans.push_back(r + 1);
      return ans;
    } else
      l++;
  }
  return ans;
}
```

I spajanje dvaju sortiranih nizova u vremenu $O(n+m)$ u merge sortu primjena je dvostrukih pokazivača pod uvjetom sortiranosti nizova.

### Zadaci za vježbu

[LeetCode 15. Zbroj triju brojeva](https://leetcode-cn.com/problems/3sum/)

## Pronalaženje ciklusa u jednostruko vezanoj listi

### Postupak

I za pronalaženje ciklusa u jednostruko vezanoj listi postoji više načina, ali metoda sporog i brzog pokazivača jedna je od najsažetijih; predstavljamo je u nastavku.

Najprije oba pokazivača pokazuju na glavu liste; jedan pokazivač pomiče se po jedan korak, a drugi po dva koraka. Ako se sretnu, dokazano je da ciklus postoji, inače ciklusa nema; vremenska složenost je $O(n)$.

Ako ciklus postoji, kako pronaći njegov početak?

Zapišimo jednadžbe i promotrimo ih. Neka je u trenutku susreta spori pokazivač napravio ukupno $k$ koraka, od toga $l$ koraka na ciklusu (kad se brzi i spori pokazivač sretnu na ciklusu, spori sigurno nije prošao cijeli krug). Brzi pokazivač napravio je $2k$ koraka; neka je duljina ciklusa $C$, tada vrijedi

$$
\begin{align}
& \ 2 k=n \times C+l+(k-l) \\
& \ k=n \times C \\
\end{align}
$$

Pri prvom susretu $n$ je najmanji pozitivni cijeli broj 1. Drugim riječima, $k=C$. Koristeći tu jednakost, nakon što se dva pokazivača sretnu možemo jedan od njih premjestiti na glavu liste i oba pomicati po jedan korak; mjesto na kojem se ponovno sretnu početak je ciklusa.

### Implementacija

```cpp
--8<-- "docs/misc/code/two-pointer/two-pointer_1.cpp:core"
```

Vremenska složenost je $O(n)$.
