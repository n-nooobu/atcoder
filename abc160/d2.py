import io
import sys

# input here
_INPUT = """\
10 4 8

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

N, X, Y = map(int, input().split())

def push(v, l):
    if seen[v] >= 0:
        return
    seen[v] = l
    q.append(v)

ans = [0] * N
for i in range(1, N + 1):
    seen = [-1] * (N + 1)
    seen[i] = 0
    q = deque([])
    q.append(i)
    while q:
        t = q.popleft()
        l = seen[t]
        if t > 1:
            push(t - 1, l + 1)
        if t < N:
            push(t + 1, l + 1)
        if t == X:
            push(Y, l + 1)
        if t == Y:
            push(X, l + 1)
    for j in range(1, N + 1):
        ans[seen[j]] += 1

ans = [i // 2 for i in ans]
for i in range(1, N):
    print(ans[i])
