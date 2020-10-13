import io
import sys

# input here
_INPUT = """\
a
6
2 2 a
2 1 b
1
2 2 c
1
1

"""
sys.stdin = io.StringIO(_INPUT)



S = input()
Q = int(input())
Query = [input().split() for _ in range(Q)]

hanten = False
s_mae = ''
s_ushiro = ''
for i in range(Q):
    if Query[i][0] == '1':
        if hanten:
            hanten = False
        else:
            hanten = True
    elif Query[i][1] == '1':
        if hanten:
            s_ushiro = s_ushiro + Query[i][2]
        else:
            s_mae = Query[i][2] + s_mae
    else:
        if hanten:
            s_mae = Query[i][2] + s_mae
        else:
            s_ushiro = s_ushiro + Query[i][2]

ans = s_mae + S + s_ushiro
if hanten:
    print(ans[::-1])
else:
    print(ans)
