class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


fa = [0] * 1010  # parent array (DSU)
g = []


def add(u, v, w):
    g.append(Edge(u, v, w))


# standard DSU (union-find)
def findroot(x):
    if fa[x] == x:
        return x
    fa[x] = findroot(fa[x])
    return fa[x]


def Merge(x, y):
    x = findroot(x)
    y = findroot(y)
    fa[x] = y


# Kruskal's algorithm
def kruskal():
    tot = 0  # number of edges chosen so far
    ans = 0  # total cost
    for e in g:
        x = findroot(e.u)
        y = findroot(e.v)
        if x != y:  # if the representatives differ
            fa[x] = y  # merge
            tot += 1  # one more edge
            ans += e.w  # add the cost
            if tot == n - k:  # check whether the chosen edges already give k cotton candies
                print(ans)
                return
    print("No Answer")  # cannot be connected


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    if n == k:  # special case at the boundary
        print("0")
        exit()
    for i in range(1, n + 1):  # initialization
        fa[i] = i
    for i in range(1, m + 1):
        u, v, w = map(int, input().split())
        add(u, v, w)  # add an edge
    g.sort(key=lambda edge: edge.w)  # sort by edge weight first
    kruskal()
