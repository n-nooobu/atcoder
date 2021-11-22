import io
import sys

# input here
_INPUT = """\
?6?42???8??2??06243????9??3???7258??5??7???????774????4?1??17???9?5?70???76???

"""
sys.stdin = io.StringIO(_INPUT)



S = input()
mod = 10 ** 9 + 7

dp = [[0] * 13 for _ in range(len(S) + 1)]
dp[0][0] = 1

amari = [1]
for i in range(1, len(S)):
    amari.append((amari[-1] * 10) % 13)

for i in range(1, len(S) + 1):
    for j in range(13):
        if S[i - 1] != '?':
            idx = (j + int(S[i - 1]) * amari[-i]) % 13
            dp[i][idx] += dp[i - 1][j]
            dp[i][idx] %= mod
        else:
            for k in range(10):
                idx = (j + k * amari[-i]) % 13
                dp[i][idx] += dp[i - 1][j]
                dp[i][idx] %= mod

print(dp[-1][5])
