import io
import sys

# input here
_INPUT = """\
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
ooooxooooo
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx

"""
sys.stdin = io.StringIO(_INPUT)



import sys
from copy import deepcopy
from collections import deque

M = [list(input()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if M[i][j] == 'o':
            s = [i, j]
            break
    else:
        continue
    break

dh = [-1, 0, 0, 1]
dw = [0, 1, -1, 0]

for i in range(10):
    for j in range(10):
        q = deque()
        q.append(s)

        tM = deepcopy(M)
        tM[i][j] = 'o'
        while q:
            th, tw = q.pop()
            for k in range(4):
                nh = th + dh[k]
                nw = tw + dw[k]
                if nh < 0 or nh > 9 or nw < 0 or nw > 9:
                    continue
                if tM[nh][nw] == 'x':
                    continue
                tM[nh][nw] = 'x'
                q.append([nh, nw])

        flag = True
        for l in range(10):
            for m in range(10):
                if tM[l][m] == 'o':
                    flag = False
                    break
            else:
                continue
            break

        if flag:
            print('YES')
            sys.exit()

print('NO')
