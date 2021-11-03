import io
import sys

# input here
_INPUT = """\
7 14
1 6 3
1 4 1
1 5 2
1 2 7
1 3 5
3 2
3 4
3 6
2 3 5
2 4 1
1 1 5
3 2
3 4
3 6

"""
sys.stdin = io.StringIO(_INPUT)



N, Q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]

train = [[0, 0] for _ in range(N + 1)]
for i, q in enumerate(query):
    if q[0] == 1:
        train[q[1]][1] = q[2]
        train[q[2]][0] = q[1]
    elif q[0] == 2:
        train[q[1]][1] = 0
        train[q[2]][0] = 0
    else:
        now = q[1]
        t = train[now]
        while t[0] > 0:
            now = t[0]
            t = train[now]
        l = [1, now]
        while t[1] > 0:
            l[0] += 1
            now = t[1]
            l.append(now)
            t = train[now]
        print(*l, sep=' ')
