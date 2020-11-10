import io
import sys

# input here
_INPUT = """\
11 14
3 1 4 1 5 9 2 6 5 3 5
8 9 7 9 3 2 3 8 4 6 2

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
F = sorted(list(map(int, input().split())), reverse=True)

low = 0
high = 10 ** 12
mid = (high + low) // 2
while high - low > 1:
    syugyo = 0
    for i in range(N):
        syugyo += max(A[i] - mid // F[i], 0)
    if syugyo <= K:
        high = mid
    else:
        low = mid
    mid = (high + low) // 2

syugyo = 0
for i in range(N):
    syugyo += max(A[i] - low // F[i], 0)
if syugyo <= K:
    print(low)
else:
    print(high)
