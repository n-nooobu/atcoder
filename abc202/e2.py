import io
import sys

# input here
_INPUT = """\
7
1 1 2 2 4 2
4
1 2
7 2
4 1
5 5


"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N = int(input())
P = [0, 0] + list(map(int, input().split()))
Q = int(input())

G = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    a = i
    b = P[i]
    G[b].append(a)

def euler_tour(N, root=0):
    et_order = [None] * (2 * N)
    t_in, t_out = [None]*N, [None]*N
    depth = [[] for _ in range(N)]
    t = 0
    q = [[~root, 0], [root, 0]]
    while q:
        u, d = q.pop()
        if u >= 0:
            # 行きがけの処理
            # 記録
            et_order[t] = u
            t_in[u] = t
            depth[d].append(t)
            t += 1
            # 探索先を追加
            for v in G[u][::-1]:
                q.append([~v, d + 1])
                q.append([v, d + 1])
        else:
            # 帰りがけの処理
            # 記録
            et_order[t] = u
            t_out[~u] = t
            t += 1
    return et_order, t_in, t_out, depth

et_order, t_in, t_out, depth = euler_tour(N + 1, root=1)

for i in range(Q):
    U, D = map(int, input().split())
    low = bisect_left(depth[D], t_in[U])
    high = bisect_right(depth[D], t_out[U])
    print(high - low)
