import io
import sys

# input here
_INPUT = """\
7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict
import itertools

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
G = defaultdict(set)
for i in range(M):
    A = ab[i][0] - 1
    B = ab[i][1] - 1
    G[A].add(B)
    G[B].add(A)

ans = 0
for i in itertools.permutations([i for i in range(1, N)]):
    v = 0
    flag = True
    for j in range(len(i)):
        if i[j] not in G[v]:
            flag = False
            break
        v = i[j]
    if flag:
        ans += 1

print(ans)
