#!/usr/bin/env python3
"""Konacne provjere na koje se oslanja dokaz za slucaj m = 2 (binarni nizovi) u detaljnom rjesenju.

  1. Za 3 <= n <= 14: minimalan broj palindromnih podsegmenata je 2n-2 i niz ga dostize
     ako i samo ako ne sadrzi nijedan uzorak iz F.
  2. Svaka pojava uzorka iz F ostavlja barem jedan palindrom "nepreuzet" u injekciji iz dokaza
     donje ograde (provjereno za sve kontekste do 6 znakova sa svake strane, ukljucujuci rubove),
     pa niz s takvim uzorkom ima >= 2n-1 palindroma.
  3. Nizova duljine 10 bez uzoraka iz F je tocno 12 (rotacije rijeci 001011 i komplementi), a svaki
     prozor od 5 znakova tih periodicnih rijeci ima jedinstven nastavak bez uzoraka iz F
     => indukcijom su za n >= 10 to jedini takvi nizovi.
  4. Ti nizovi imaju tocno 2n-2 palindroma: nemaju palindrome duljine >= 5, pa broj palindroma
     koji zavrsavaju na poziciji i ovisi samo o zadnja 4 znaka; kroz cijeli period iznosi 2.
Pokretanje: python3 provjera_leme.py  (traje nekoliko sekundi)
"""
from itertools import product

F = ["000", "111", "01010", "10101", "00100", "11011", "010010", "101101", "110011", "001100"]


def broj_palindroma(s):
    n = len(s)
    c = 0
    for i in range(n):
        for j in range(i, n):
            t = s[i:j + 1]
            if t == t[::-1]:
                c += 1
    return c


def izbjegava(s):
    return not any(f in s for f in F)


def palindromi(s):
    n = len(s)
    res = set()
    for i in range(n):
        for j in range(i + 1, n):
            t = s[i:j + 1]
            if t == t[::-1]:
                res.add((i, j))
    return res


def preuzeti(s, pozicije):
    """Injekcija iz dokaza: unutarnja pozicija i -> palindrom duljine >= 2 koji je sadrzi."""
    n = len(s)
    img = {}
    for i in pozicije:
        if i <= 0 or i >= n - 1:
            continue
        if s[i - 1] == s[i + 1]:
            img[i] = (i - 1, i + 1)
        elif s[i] == s[i - 1]:
            img[i] = (i - 1, i)
        else:
            img[i] = (i, i + 1)
    for i in list(img):
        if i + 1 in img and img[i] == img[i + 1] == (i, i + 1):
            assert s[i - 1] == s[i + 2]
            img[i + 1] = (i - 1, i + 2)
    return img


def main():
    # 1.
    for n in range(3, 15):
        svi = [''.join(t) for t in product('01', repeat=n)]
        vrijednosti = {s: broj_palindroma(s) for s in svi}
        assert min(vrijednosti.values()) == 2 * n - 2
        for s in svi:
            assert (vrijednosti[s] == 2 * n - 2) == izbjegava(s), s
    print("1. minimum 2n-2 i karakterizacija preko F: OK za n <= 14")

    # 2.
    C = 6
    for w in F:
        for l in range(C + 1):
            for r in range(C + 1):
                for L in product('01', repeat=l):
                    for R in product('01', repeat=r):
                        s = ''.join(L) + w + ''.join(R)
                        ws, we = l, l + len(w) - 1
                        n = len(s)
                        zlo, zhi = max(0, ws - 2), min(n - 1, we + 2)
                        plo, phi = max(1, ws - 4), min(n - 2, we + 4)
                        img = preuzeti(s, range(plo, phi + 1))
                        zona = {p for p in palindromi(s) if zlo <= p[0] and p[1] <= zhi}
                        assert zona - set(img.values()), (w, s)
    print("2. svaki uzorak iz F ostavlja nepreuzet palindrom: OK")

    # 3.
    baza = "001011"
    periodicne = set()
    for r in range(6):
        w = baza[r:] + baza[:r]
        periodicne.add(w)
        periodicne.add(''.join('1' if ch == '0' else '0' for ch in w))
    assert len(periodicne) == 12
    n = 10
    bezF = sorted(''.join(t) for t in product('01', repeat=n) if izbjegava(''.join(t)))
    assert bezF == sorted((w * 3)[:n] for w in periodicne)
    for w in periodicne:
        niz = w * 5
        for i in range(6):
            prozor = niz[i:i + 5]
            nastavci = [c for c in '01' if izbjegava(prozor + c)]
            assert nastavci == [niz[i + 5]], (prozor, nastavci)
    print("3. za n = 10 tocno 12 nizova bez F, nastavak jedinstven: OK")

    # 4.
    for w in periodicne:
        niz = w * 6
        for duljina in (5, 6):
            for i in range(len(niz) - duljina + 1):
                t = niz[i:i + duljina]
                assert t != t[::-1]
        for i in range(10, 30):
            s = niz[:i]
            zavrsavaju = 1 + (s[-1] == s[-2]) + (s[-1] == s[-3]) + (s[-1] == s[-4] and s[-2] == s[-3])
            assert zavrsavaju == 2, (w, i)
        assert broj_palindroma(niz[:10]) == 18
    print("4. periodicni nizovi: nema palindroma duljine >= 5, prirast po znaku je 2, P(10) = 18: OK")


if __name__ == '__main__':
    main()
