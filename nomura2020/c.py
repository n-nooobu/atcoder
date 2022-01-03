import io
import sys

# input here
_INPUT = """\
10
0 0 1 1 2 3 5 8 13 21 34

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

ans = 0
v = 1
As = sum(A)
for i in range(N + 1):
    ans += v
    As -= A[i]
    v = min((v - A[i]) * 2, As)

if v == 0:
    print(ans)
else:
    print(-1)
