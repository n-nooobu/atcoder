import io
import sys

# input here
_INPUT = """\
5
1000000000 0
1000000000 0
1000000000 0
1000000000 0
1000000000 4 1 2 3 4

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

N = int(input())
T = []
K = []
A = []
for _ in range(N):
    t = list(map(int, input().split()))
    T.append(t[0])
    K.append(t[1])
    A.append(t[2:])


ans = 0
used = [0] * N
dq = deque([N - 1])
while dq:
    u = dq.pop()
    ans += T[u]
    for v in A[u]:
        v -= 1
        if used[v]:
            continue
        used[v] = 1
        dq.append(v)

print(ans)
