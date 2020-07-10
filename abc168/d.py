import itertools
from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(M)]

ans = [-1] * N
ans[0] = 0
d = deque([1])
while any(i == -1 for i in ans) and any(i != [-1, -1] for i in AB):
    now = d[0]
    for i in itertools.product(range(M), range(2)):
        if AB[i[0]][i[1]] == now:
            if ans[AB[i[0]][1 - i[1]] - 1] == -1:
                ans[AB[i[0]][1 - i[1]] - 1] = now
                d.append(AB[i[0]][1 - i[1]])
            AB[i[0]] = [-1, -1]
    d.popleft()

if any(i == -1 for i in ans):
    print('No')
else:
    print('Yes')
    for i in ans[1:]:
        print(i)
