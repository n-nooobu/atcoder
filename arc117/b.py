import io
import sys

# input here
_INPUT = """\
7
314 159 265 358 979 323 846

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7

ans = 1
pre = 0
for i in range(N):
    ans = ans * (A[i] - pre + 1) % mod
    pre = A[i]

print(ans)
