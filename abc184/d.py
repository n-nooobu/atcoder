import io
import sys

# input here
_INPUT = """\
0 0 1


"""
sys.stdin = io.StringIO(_INPUT)



A, B, C = map(int, input().split())

dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
for i in reversed(range(100)):
    for j in reversed(range(100)):
        for k in reversed(range(100)):
            if i + j + k == 0:
                continue
            dp[i][j][k] = (dp[i + 1][j][k] + 1) * i / (i + j + k) + (dp[i][j + 1][k] + 1) * j / (i + j + k) + (dp[i][j][k + 1] + 1) * k / (i + j + k)

print(dp[A][B][C])
