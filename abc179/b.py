import io
import sys

# input here
_INPUT = """\
6
1 1
2 2
3 3
4 4
5 5
6 6
"""
sys.stdin = io.StringIO(_INPUT)



import sys

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

now = D[0]
zorome = 0
if now[0] == now[1]:
    zorome += 1
else:
    zorome = 0
for i in range(1, N):
    now = D[i]
    if now[0] == now[1]:
        zorome += 1
        if zorome == 3:
            print('Yes')
            sys.exit()
    else:
        zorome = 0
print('No')
