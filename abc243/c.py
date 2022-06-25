import io
import sys

# input here
_INPUT = """\
10
1 3
1 4
0 0
0 2
0 4
3 1
2 4
4 2
4 4
3 3
RLRRRLRLRR

"""
sys.stdin = io.StringIO(_INPUT)



import sys
from collections import OrderedDict

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
S = input()

od = OrderedDict()
for i in range(N):
    if XY[i][1] in od:
        od[XY[i][1]].append([i, XY[i][0]])
    else:
        od[XY[i][1]] = [[i, XY[i][0]]]

for i, l in od.items():
        flg = False
        l = sorted(l, key=lambda x: x[1])
        for j, _ in l:
            if not flg:
                if S[j] == 'R':
                    flg = True
            if flg:
                if S[j] == 'L':
                    print('Yes')
                    sys.exit()

print('No')
