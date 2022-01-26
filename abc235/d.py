import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



a, N = map(int, input().split())

dp = [[0] * 10 ** 6 for _ in range(20)]
dp[0][1] = 1

for i in range(19):
    for j in range(10 ** 6):
        if dp[i][j]:
            if dp[i][j] * a < 10 ** 6:
                dp[i + 1][dp[i][j] * a] = 1
            dp[i + 1][int(str(j)[-1] + str(j)[:-1])] = 1

for j in range(20):
    if dp[N][j]:
        print()
