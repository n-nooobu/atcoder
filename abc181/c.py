import io
import sys

# input here
_INPUT = """\
9
8 2
2 3
1 3
3 7
1 0
8 8
5 6
9 7
0 1

"""
sys.stdin = io.StringIO(_INPUT)



import sys
import itertools

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

for i in itertools.combinations([_ for _ in range(N)], 3):
    if (xy[i[1]][0] - xy[i[0]][0]) * (xy[i[2]][1] - xy[i[0]][1]) == (xy[i[2]][0] - xy[i[0]][0]) * (xy[i[1]][1] - xy[i[0]][1]):
        print('Yes')
        sys.exit()

print('No')
