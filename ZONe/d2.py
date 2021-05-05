import io
import sys

# input here
_INPUT = """\
ozRnonnoe

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

S = input()

q = deque()
rev = False
for s in S:
    if s == 'R':
        rev = ~rev
    else:
        if rev:
            if q and q[0] == s:
                q.popleft()
            else:
                q.appendleft(s)
        else:
            if q and q[-1] == s:
                q.pop()
            else:
                q.append(s)

if rev:
    q.reverse()
print(''.join(q))
