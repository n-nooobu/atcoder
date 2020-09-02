import io
import sys

# input here
_INPUT = """\
10 4
3 1
4 1
5 9
2 6
"""
sys.stdin = io.StringIO(_INPUT)



import numpy as np
from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(M)]

seen = [0] * N
visitm = [True] * M
listm = np.arange(M)
q = deque()
group = []

for i in range(N):
    if seen[i]:
        continue
    q.append(i)
    seen[i] = 1
    k = 1
    while q:
        t = q.popleft()
        for j in listm[visitm]:
            if AB[j][0] == i + 1 and seen[AB[j][1] - 1] != 1:
                q.append(AB[j][1])
                seen[AB[j][1] - 1] = 1
                k += 1
            if AB[j][1] == i + 1 and seen[AB[j][0] - 1] != 1:
                q.append(AB[j][0] - 1)
                seen[AB[j][0] - 1] = 1
                k += 1
            visitm[j] = False
    group.append(k)

print(max(group))
