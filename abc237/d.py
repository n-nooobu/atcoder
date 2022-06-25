import io
import sys

# input here
_INPUT = """\
7
LLLLLLL

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

N = int(input())
S = input()

q = deque([len(S)])
for i in reversed(range(N)):
    if S[i] == 'L':
        q.append(i)
    else:
        q.appendleft(i)

for i in range(N + 1):
    print(q.popleft(), end=' ')
