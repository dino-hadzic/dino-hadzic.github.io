from heapq import heappush, heapreplace

a = [tuple(map(int, input().split())) for _ in range(int(input()))]
a.sort(key=lambda job: job[0])  # sort by deadline in ascending order

ans = 0  # total profit
q = []  # min-heap keeps track of the minimum
for d, p in a:
    if d <= len(q):  # deadline exceeded
        if q[0] < p:  # regret – replace the worst choice
            ans += p - heapreplace(q, p)
    else:  # add to the queue directly
        ans += p
        heappush(q, p)
print(ans)
