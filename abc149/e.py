import io
import sys

# input here
_INPUT = """\
5 3
10 14 19 34 33

"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

hlow, hhigh = A[0] * 2, A[-1] * 2
while hhigh - hlow > 1:
    hmid = (hhigh + hlow) // 2
    cnt = 0
    for a in A:
        cnt += N - bisect_left(A, hmid - a)
    if cnt >= M:
        hlow = hmid
    else:
        hhigh = hmid

CumA = [0] * (N + 1)
CumA[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    CumA[i] = CumA[i + 1] + A[i]

res = 0
cnt = 0
for a in A:
    _index = bisect_left(A, hlow - a)
    cnt += (N - _index)
    res += (N - _index) * a + CumA[_index]
res -= max(0, cnt - M) * hlow
print(res)
