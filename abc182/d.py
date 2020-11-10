import io
import sys

# input here
_INPUT = """\
5
-1000 -1000 -1000 -1000 -1000

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

cum = [0] * N
cum[0] = A[0]
for i in range(1, N):
    cum[i] = cum[i - 1] + A[i]
cum2 = [0] * N
cum2[0] = cum[0]
for i in range(1, N):
    cum2[i] = cum2[i - 1] + cum[i]

ans = max(0, cum2[0])
cummax = cum2[0]
for i in range(N - 1):
    cummax = max(cummax, cum[i + 1])
    ans = max(ans, cum2[i] + cummax)

print(ans)
