import io
import sys

# input here
_INPUT = """\
20 3
0 5 15
"""
sys.stdin = io.StringIO(_INPUT)



K, N = map(int, input().split())
A = list(map(int, input().split()))

ans = 10 ** 7
A = sorted(A)
for i in range(N):
    if i != 0:
        ans = min(ans, A[i - 1] + K - A[i])
    else:
        ans = min(ans, A[-1] - A[i])

print(ans)
