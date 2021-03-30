import io
import sys

# input here
_INPUT = """\
7 1 2
24 35 40 68 72 99 103

"""
sys.stdin = io.StringIO(_INPUT)



N, A, B = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    if X[i] - X[i-1] > B // A:
        ans += B
    else:
        ans += (X[i] - X[i-1]) * A

print(ans)
