import io
import sys

# input here
_INPUT = """\
10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000


"""
sys.stdin = io.StringIO(_INPUT)



import heapq
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] *= -1

heapq.heapify(A)
for i in range(M):
    a = heapq.heappop(A)
    heapq.heappush(A, math.ceil(a / 2))

print(-sum(A))
