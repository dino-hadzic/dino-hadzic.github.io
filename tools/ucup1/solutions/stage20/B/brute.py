# Brute force: za svaki element Dijkstra po vrijednostima 0..A_i (brid v -> floor(v/x) cijene cost[x]),
# zatim za svaki kandidat x = 0,1,... zbroj k+1 najjeftinijih "spustanja na <= x".
import sys, heapq
def main():
    data = sys.stdin.read().split(); p = 0
    t = int(data[p]); p += 1
    out = []
    for _ in range(t):
        n, m, K = int(data[p]), int(data[p+1]), int(data[p+2]); p += 3
        a = [int(x) for x in data[p:p+n]]; p += n
        cost = [0] + [int(x) for x in data[p:p+m]]; p += m
        best_le = []  # best_le[i][x] = min cijena da A_i postane <= x
        for v0 in a:
            dist = [float('inf')] * (v0 + 1); dist[v0] = 0
            pq = [(0, v0)]
            while pq:
                d, v = heapq.heappop(pq)
                if d > dist[v]: continue
                for x in range(1, m + 1):
                    w = v // x
                    if d + cost[x] < dist[w]:
                        dist[w] = d + cost[x]; heapq.heappush(pq, (dist[w], w))
            le = [0] * (v0 + 1); cur = float('inf')
            for x in range(v0 + 1):
                cur = min(cur, dist[x]); le[x] = cur
            best_le.append(le)
        k = n // 2
        x = 0
        while True:
            costs = sorted(le[x] if x < len(le) else 0 for le in best_le)
            if sum(costs[:k+1]) <= K: break
            x += 1
        out.append(str(x))
    print("\n".join(out))
main()
