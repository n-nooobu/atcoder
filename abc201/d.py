import io
import sys

# input here
_INPUT = """\
3 3
---
+-+
+--

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
A = [input() for _ in range(H)]
a = [[1 if A[j][i] == '+' else -1 for i in range(W)] for j in range(H)]

dp = [[0] * W for _ in range(H)]

for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        if i < H - 1 and j < W - 1:
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1])
        elif i < H - 1:
            dp[i][j] = dp[i + 1][j]
        elif j < W - 1:
            dp[i][j] = dp[i][j + 1]
        if i != 0 or j != 0:
            if (i + j) % 2 == 0:
                dp[i][j] -= a[i][j]
            else:
                dp[i][j] += a[i][j]

if dp[0][0] > 0:
    print('Takahashi')
elif dp[0][0] < 0:
    print('Aoki')
else:
    print('Draw')
