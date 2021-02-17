import io
import sys

# input here
_INPUT = """\
100000

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

K = int(input())

if K < 10:
    print(K)
    exit()

q = deque([])
for i in range(1, 10):
    q.append(str(i))
k = 9
while q:
    t = q.popleft()

    if t[-1] == '0':
        l = ['0', '1']
    elif t[-1] == '9':
        l = ['8', '9']
    else:
        l = [str(int(t[-1]) - 1), t[-1], str(int(t[-1]) + 1)]

    for i in l:
        t2 = t + i
        q.append(t2)
        k += 1
        if k == K:
            print(t2)
            exit()
