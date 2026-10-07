from heapq import heappush, heapreplace

a = [tuple(map(int, input().split())) for _ in range(int(input()))]
a.sort(key=lambda job: job[0])  # sortiraj uzlazno po roku

ans = 0  # ukupna zarada
q = []  # min-hrpa održava najmanju vrijednost
for d, p in a:
    if d <= len(q):  # rok je prekoračen
        if q[0] < p:  # „žaljenje” – zamijeni najlošiji izbor
            ans += p - heapreplace(q, p)
    else:  # izravno dodaj u red
        ans += p
        heappush(q, p)
print(ans)
