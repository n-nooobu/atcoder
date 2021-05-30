import io
import sys

# input here
_INPUT = """\
3 3 100
1 1 1

"""
sys.stdin = io.StringIO(_INPUT)



from heapq import heappush, heappop

K, N, M = map(int, input().split())
A = list(map(int, input().split()))

b = [0] * K
B = [0] * K
s = 0
hq0 = []
hq1 = []
for i in range(K):
    b[i] = A[i] * M / N
    B[i] = round(b[i])
    heappush(hq0, [A[i] * (B[i] + 1 - b[i]), i])
    heappush(hq1, [A[i] * (b[i] - (B[i] - 1)), i])
    s += B[i]

while s < M:
    idx = heappop(hq0)
    B[idx[1]] += 1
    if B[idx[1]] > 0:
        heappush(hq0, [idx[0] + A[idx[1]], idx[1]])
    s += 1
while s > M:
    idx = heappop(hq1)
    B[idx[1]] -= 1
    if B[idx[1]] > 0:
        heappush(hq1, [idx[0] + A[idx[1]], idx[1]])
    s -= 1

for i in range(K):
    print(B[i], end=' ')