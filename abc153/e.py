import io
import sys

# input here
_INPUT = """\
9999 10
540 7550
691 9680
700 9790
510 7150
415 5818
551 7712
587 8227
619 8671
588 8228
176 2461
"""
sys.stdin = io.StringIO(_INPUT)



H, N = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

INF = 10 ** 9
dp = [INF] * (H + max(A) + 1)
dp[0] = 0

