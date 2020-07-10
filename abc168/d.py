from collections import deque

N, M = map(int, input().split())
g = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    g[A-1].append(B)
    g[B-1].append(A)

ans = [-1] * N
ans[0] = 0
d = deque([1])
while len(d) != 0:
    now = d[0]
    d.popleft()
    for i in g[now-1]:
        if ans[i-1] != -1:
            continue
        ans[i-1] = now
        d.append(i)

if -1 in ans:
    print('No')
else:
    print('Yes')
    for i in ans[1:]:
        print(i)
