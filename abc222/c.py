import io
import sys

# input here
_INPUT = """\
2 2
GC
PG
CG
PP

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
A = [input() for _ in range(2 * N)]


def rcp(a, b):
    if a == 0 and b == 1: return 1
    if a == 1 and b == 2: return 1
    if a == 2 and b == 0: return 1
    return 0

rcp2num = {'G': 0, 'C': 1, 'P': 2}

rank = [[M, i + 1] for i in range(2 * N)]
for i in range(M):
    for j in range(0, 2 * N, 2):
        if rcp(rcp2num[A[rank[j][1] - 1][i]], rcp2num[A[rank[j + 1][1] - 1][i]]):
            rank[j][0] -= 1
        if rcp(rcp2num[A[rank[j + 1][1] - 1][i]], rcp2num[A[rank[j][1] - 1][i]]):
            rank[j + 1][0] -= 1
    rank = sorted(rank)

for i in range(2 * N):
    print(rank[i][1])
