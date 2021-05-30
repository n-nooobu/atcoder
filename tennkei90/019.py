import io
import sys

# input here
_INPUT = """\
15
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

dp = [[10 ** 10] * 2 * N for _ in range(2 * N)]
for d in range(1, 2 * N, 2):
    for l in range(2 * N - 1):
        if d == 1:
            dp[l][l + d] = abs(A[l] - A[l + d])
            continue
        if l + d >= 2 * N:
            continue
        dp[l][l + d] = min(dp[l][l + d], dp[l + 1][l + d - 1] + abs(A[l] - A[l + d]))
        for k in range(l + 1, l + d, 2):
            dp[l][l + d] = min(dp[l][l + d], dp[l][k] + dp[k + 1][l + d])

print(dp[0][2 * N - 1])
