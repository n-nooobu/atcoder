import io
import sys

# input here
_INPUT = """\
2
35
AT

"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()
X = input()

dp = [[False] * 7 for _ in range(N)]
dp[-1][0] = True
ten = 1
for i in range(N - 1, 0, -1):
    for j in range(7):
        if dp[i][j]:
            num = int(S[i])
            if X[i] == 'A':
                if num * ten % 7 == 0:
                    dp[i - 1][j] = True
            else:
                dp[i - 1][(j - num * ten) % 7] = True
                dp[i - 1][j] = True
    ten = (ten * 10) % 7

if sum(dp[0]) > 0:
    print('Takahashi')
else:
    print('Aoki')
