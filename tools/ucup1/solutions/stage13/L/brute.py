# Brute force: dp[k] = bitmaska dostizivih zbrojeva T podnizovima duljine k (O(n^2 S)).
import sys
data = sys.stdin.read().split()
n, S = int(data[0]), int(data[1]); a = list(map(int, data[2:2 + n]))
dp = [0] * (n + 1); dp[0] = 1
for x in a:
    for k in range(n, 0, -1):
        dp[k] |= dp[k - 1] << x
print(sum(bin(m).count('1') for m in dp))
