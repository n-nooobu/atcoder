import io
import sys

# input here
_INPUT = """\
8
1 2
2 3
2 4
2 5
4 7
5 6
6 8

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

n = int(input())

v = [[] for _ in range(n)]
e = []
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    v[a].append(b)
    e.append(b)

colors = [-1] * n
colors[0] = 0

queue = deque([0, ])

while queue:
    current = queue.popleft()
    now = 1
    for to in v[current]:
        if now == colors[current]:
            now += 1
        colors[to] = now
        now += 1
        queue.append(to)

print(max(colors))
for i in e:
    print(colors[i])
