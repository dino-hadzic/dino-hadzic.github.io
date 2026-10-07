class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


fa = [0] * 1010  # polje roditelja (DSU)
g = []


def add(u, v, w):
    g.append(Edge(u, v, w))


# standardni DSU (union-find)
def findroot(x):
    if fa[x] == x:
        return x
    fa[x] = findroot(fa[x])
    return fa[x]


def Merge(x, y):
    x = findroot(x)
    y = findroot(y)
    fa[x] = y


# Kruskalov algoritam
def kruskal():
    tot = 0  # broj odabranih bridova
    ans = 0  # ukupni trošak
    for e in g:
        x = findroot(e.u)
        y = findroot(e.v)
        if x != y:  # ako su predstavnici različiti
            fa[x] = y  # spoji
            tot += 1  # još jedan brid
            ans += e.w  # dodaj trošak
            if tot == n - k:  # provjeri daje li broj odabranih bridova k šećernih vuna
                print(ans)
                return
    print("No Answer")  # ne može se povezati


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    if n == k:  # poseban rubni slučaj
        print("0")
        exit()
    for i in range(1, n + 1):  # inicijalizacija
        fa[i] = i
    for i in range(1, m + 1):
        u, v, w = map(int, input().split())
        add(u, v, w)  # dodaj brid
    g.sort(key=lambda edge: edge.w)  # prvo sortiraj po težini brida
    kruskal()
