import io
import sys

# input here
_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

N = int(input())

if N == 1:
    print('a')
    exit()

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
q = deque([])
q.append(['a', 1])
while q:
    t, s = q.popleft()
    for i in range(s + 1):
        t2 = t + alphabets[i]
        if i == s:
            s2 = s + 1
        else:
            s2 = s
        if len(t2) == N:
            print(t2)
        else:
            q.append([t2, s2])
