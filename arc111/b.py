import io
import sys

# input here
_INPUT = """\
12
5 2
5 6
1 2
9 7
2 7
5 5
4 2
6 7
2 2
7 8
9 7
1 8

"""
sys.stdin = io.StringIO(_INPUT)



from collections import defaultdict
import sys
sys.setrecursionlimit(int(1e7))

N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]

G = defaultdict(set)
for i in range(N):
    A = ab[i][0] - 1
    B = ab[i][1] - 1
    G[A].add(B)
    G[B].add(A)

def dfs(u, p):
    global flag
    used[u] = 1
    preorder.append(u)
    for v in G[u]:
        if used[v]:
            if v != p:
                flag = True
            continue
        dfs(v, u)

used = [0] * (4 * 10 ** 5)
ans = 0
for i in range((4 * 10 ** 5)):
    if used[i]:
        continue
    preorder = []
    flag = False
    dfs(i, -1)
    if flag:
        ans += len(preorder)
    else:
        ans += len(preorder) - 1

print(ans)
