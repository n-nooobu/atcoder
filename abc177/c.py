import io
import sys

# input here
_INPUT = """\
4
141421356 17320508 22360679 244949
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7
s = 0
for i in range(N):
    s += A[i]
    s %= mod

ans = 0
for i in range(N - 1):
    s -= A[i]
    ans += s * A[i]
    ans %= mod

print(ans)
