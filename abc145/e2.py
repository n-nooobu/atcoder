import io
import sys

# input here
_INPUT = """\
10 100
15 23
20 18
13 17
24 12
18 29
19 27
23 21
18 20
27 15
22 25

"""
sys.stdin = io.StringIO(_INPUT)



N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x: x[0])

dp = [0] * (T + 1)
for i in range(N):
    a, b = AB[i]
    for t in range(T - 1, -1, -1):
        idx = min(t + a, T)
        dp[idx] = max(dp[idx], dp[t] + b)

print(dp[-1])
