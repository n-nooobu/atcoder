import io
import sys

# input here
_INPUT = """\
314159265358979323846264338327950288419716939937551058209749445923078164062862089986280348253421170

"""
sys.stdin = io.StringIO(_INPUT)



N = input()

N = N[::-1] + '0'
INF = 10 ** 9
dp = [[INF] * 2 for _ in range(len(N) + 1)]

dp[0][0] = 0
for i in range(len(N)):
    for j in range(2):
        x = int(N[i])
        x += j
        for a in range(10):
            ni = i + 1
            nj = 0
            b = a - x
            if b < 0:
                nj = 1
                b += 10
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + a + b)

print(dp[len(N)][0])
