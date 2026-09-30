# Brute force u točnoj aritmetici (Fraction): udaljenost točka-segment preko
# projekcije, segment-segment preko presjeka i 4 projekcije; pokretni krug se
# razbija na dijelove gibanja, relativno gibanje dvaju krugova također.
import sys
from fractions import Fraction as Fr

def d2(p, q): return (p[0]-q[0])**2 + (p[1]-q[1])**2
def pseg(p, a, b):
    ab = (b[0]-a[0], b[1]-a[1]); L = ab[0]**2 + ab[1]**2
    if L == 0: return d2(p, a)
    t = Fr((p[0]-a[0])*ab[0] + (p[1]-a[1])*ab[1], L)
    t = max(Fr(0), min(Fr(1), t))
    return d2(p, (a[0] + ab[0]*t, a[1] + ab[1]*t))
def cross(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
def inter(a, b, c, d):
    def sg(v): return (v > 0) - (v < 0)
    d1, d2_, d3, d4 = sg(cross(a, b, c)), sg(cross(a, b, d)), sg(cross(c, d, a)), sg(cross(c, d, b))
    if d1*d2_ < 0 and d3*d4 < 0: return True
    def on(p, a, b): return cross(a, b, p) == 0 and min(a[0],b[0]) <= p[0] <= max(a[0],b[0]) and min(a[1],b[1]) <= p[1] <= max(a[1],b[1])
    return on(c,a,b) or on(d,a,b) or on(a,c,d) or on(b,c,d)
def sseg(a, b, c, d):
    if inter(a, b, c, d): return Fr(0)
    return min(pseg(a,c,d), pseg(b,c,d), pseg(c,a,b), pseg(d,a,b))

data = sys.stdin.read().split()
n, r, d = int(data[0]), int(data[1]), int(data[2]); p = 3
objs = []
for _ in range(n):
    t = int(data[p]); p += 1
    if t == 1:
        cx, cy, tt = map(int, data[p:p+3]); p += 3
        objs.append(('C', (cx, cy), tt - d, tt + d))
    else:
        sx, sy, tx, ty, u, v = map(int, data[p:p+6]); p += 6
        objs.append(('F', (sx, sy), (tx, ty), u - d, v + d))
        objs.append(('M', (sx, sy), (tx, ty), u, v, u - d, v + d))

def pos(o, t):   # položaj pokretnog kruga u trenutku t
    _, S, T, u, v, lo, hi = o
    t = max(u, min(v, t))
    f = Fr(t - u, v - u)
    return (S[0] + (T[0]-S[0])*f, S[1] + (T[1]-S[1])*f)

def hit(a, b):
    lo = max(a[-2], b[-2]); hi = min(a[-1], b[-1])
    if lo > hi: return False
    R2 = (2*r)**2
    ta, tb = a[0], b[0]
    if ta == 'M' and tb != 'M': a, b = b, a; ta, tb = tb, ta
    if ta == 'C' and tb == 'C': return d2(a[1], b[1]) <= R2
    if ta == 'C' and tb == 'F': return pseg(a[1], b[1], b[2]) <= R2
    if ta == 'F' and tb == 'C': return pseg(b[1], a[1], a[2]) <= R2
    if ta == 'F' and tb == 'F': return sseg(a[1], a[2], b[1], b[2]) <= R2
    if tb == 'M' and ta != 'M':
        P1, P2 = pos(b, lo), pos(b, hi)
        if ta == 'C': return pseg(a[1], P1, P2) <= R2
        return sseg(P1, P2, a[1], a[2]) <= R2
    ts = sorted(set([lo, hi] + [t for t in (a[3], a[4], b[3], b[4]) if lo < t < hi]))
    for i in range(len(ts)):
        t0 = ts[i]; t1 = ts[i+1] if i + 1 < len(ts) else ts[i]
        q0 = pos(a, t0); q1 = pos(a, t1); s0 = pos(b, t0); s1 = pos(b, t1)
        rel0 = (q0[0]-s0[0], q0[1]-s0[1]); rel1 = (q1[0]-s1[0], q1[1]-s1[1])
        if pseg((0, 0), rel0, rel1) <= R2: return True
    return False

ans = 0
for i in range(len(objs)):
    for j in range(i+1, len(objs)):
        if hit(objs[i], objs[j]): ans += 1
print(ans)
