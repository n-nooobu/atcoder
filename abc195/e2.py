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

dp = [[False] * 7 for _ in range(N + 1)]
dp[-2][0] = True
for i in range(N - 1, -1, -1):
    for j in range(7):
        if dp[i][j]:
            num = int(S[i])
            if X[i] == 'A':
                for k in range(7):
                    if k * 10 % 7 == j and (k * 10 + num) % 7 == j:
                        dp[i - 1][k] = True
            else:
                for k in range(7):
                    if k * 10 % 7 == j or (k * 10 + num) % 7 == j:
                        dp[i - 1][k] = True

if X[-1][0]:
    print('Takahashi')
else:
    print('Aoki')
