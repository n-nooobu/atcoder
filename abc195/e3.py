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

dp = [set() for _ in range(N + 1)]
dp[-1].add(0)
for i in range(N - 1, -1, -1):
    num = int(S[i])
    if X[i] == 'A':
        for k in range(7):
            if k * 10 % 7 in dp[i + 1] and (k * 10 + num) % 7 in dp[i + 1]:
                dp[i].add(k)
    else:
        for k in range(7):
            if k * 10 % 7 in dp[i + 1] or (k * 10 + num) % 7 in dp[i + 1]:
                dp[i].add(k)

if 0 in dp[0]:
    print('Takahashi')
else:
    print('Aoki')
