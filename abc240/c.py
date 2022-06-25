import io
import sys

# input here
_INPUT = """\
4 12
1 8
5 7
3 4
2 6

"""
sys.stdin = io.StringIO(_INPUT)



import copy

N, X = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (X + 1)
dp[0] = 1
for i in range(N):
    tmp = copy.deepcopy(dp)
    for j in range(X + 1):
        if tmp[j]:
            dp[j] = 0
    for j in range(X + 1):
        if tmp[j]:
            if j + ab[i][0] < X + 1:
                dp[j + ab[i][0]] = 1
            if j + ab[i][1] < X + 1:
                dp[j + ab[i][1]] = 1

if dp[X]:
    print('Yes')
else:
    print('No')
