# Brute force: eksplicitno ažuriranje niza i redukcija stogom (konfluentnost).
import sys
data = sys.stdin.read().split()
n, q = int(data[0]), int(data[1])
s = [int(c) for c in data[2]]
p = 3
out = []
for _ in range(q):
    t, l, r = int(data[p]), int(data[p + 1]), int(data[p + 2]); p += 3
    if t == 1:
        for i in range(l - 1, r):
            s[i] = (s[i] + 1) % 3
    else:
        st = []
        for i in range(l - 1, r):
            if st and st[-1] == s[i]:
                st.pop()
            else:
                st.append(s[i])
        out.append("Yes" if not st else "No")
print("\n".join(out))
