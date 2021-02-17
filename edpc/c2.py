import io
import sys

# input here
_INPUT = """\
7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
abc = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][0] = max(dp[i - 1][1] + abc[i - 1][0], dp[i - 1][2] + abc[i - 1][0])
    dp[i][1] = max(dp[i - 1][0] + abc[i - 1][1], dp[i - 1][2] + abc[i - 1][1])
    dp[i][2] = max(dp[i - 1][0] + abc[i - 1][2], dp[i - 1][1] + abc[i - 1][2])

print(max(dp[-1]))
