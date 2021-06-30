import io
import sys

# input here
_INPUT = """\
2 4
1 1
1 2
2 0
4 2

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict

N, M = map(int, input().split())
dict = defaultdict(list)
for i in range(M):
    x, y = map(int, input().split())
    y -= N
    if abs(y) > M + 5: continue
    dict[x].append(y)

dp = [0] * (2 * M + 10)
dp[0] = 1

for x in sorted(dict):
    ok = []
    for y in dict[x]:
        if dp[y - 1] or dp[y + 1]: ok.append(y)
    for y in dict[x]:
        dp[y] = 0
    for y in ok:
        dp[y] = 1

print(sum(dp))
