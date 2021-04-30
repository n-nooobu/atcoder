import io
import sys

# input here
_INPUT = """\
3


"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

N = int(input())
A = list(map(int, input().split()))

p, m, z = [], [], []
for i in range(N):
    if A[i] > 0:
        p.append(A[i])
    elif A[i] < 0:
        m.append(A[i])
    else:
        z.append(A[i])
p = sorted(p)
m = sorted(m)
p_que, m_que = deque(), deque()
for i in range(len(p)):
    p_que.append(p[i])
for i in range(len(m)):
    m_que.append(m[i])

ans = []

if not p_que and not m_que:
    print(0)
    for i in range(len(z) - 1):
        print(0, 0)
    exit()
elif not p_que:
    if z:
        for i in range(len(z)):
            p_que.append(z[i])
    else:
        m1 = m_que.pop()
        m2 = m_que.pop()
        if not m_que:
            print(m1 - m2)
            print(m1, m2)
            exit()
        else:
            p_que.append(m1 - m2)
            ans.append([m1, m2])
elif not m_que:
    if z:
        for i in range(len(z)):
            m_que.append(z[i])
    else:
        p1 = p_que.popleft()
        p2 = p_que.popleft()
        if not p_que:
            print(p2 - p1)
            print(p2, p1)
            exit()
        else:
            m_que.append(p1 - p2)
            ans.append([p1, p2])
else:
    if z:
        for i in range(len(z)):
            m_que.append(z[i])

while not (len(p_que) == 1 and not m_que):
    if len(p_que) == 1:
        p = p_que.popleft()
        m = m_que.popleft()
        p_que.append(p - m)
        ans.append([p, m])
    else:
        p = p_que.popleft()
        m = m_que.popleft()
        m_que.append(m - p)
        ans.append([m, p])

print(p_que.pop())
for x, y in ans:
    print(x, y)
