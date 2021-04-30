import io
import sys

# input here
_INPUT = """\
2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = input()
s = []
for i in range(2*N):
    s.append(S[i])
Q = int(input())
TAB = [list(map(int, input().split())) for _ in range(Q)]

flip = False
for i in range(Q):
    if flip:
        if TAB[i][0] == 1:
            if TAB[i][1] - 1 < N:
                t = s[TAB[i][1] - 1 + N]
                if TAB[i][2] - 1 < N:
                    s[TAB[i][1] - 1 + N] = s[TAB[i][2] - 1 + N]
                    s[TAB[i][2] - 1 + N] = t
                else:
                    s[TAB[i][1] - 1 + N] = s[TAB[i][2] - 1 - N]
                    s[TAB[i][2] - 1 - N] = t
            else:
                t = s[TAB[i][1] - 1 - N]
                if TAB[i][2] - 1 < N:
                    s[TAB[i][1] - 1 - N] = s[TAB[i][2] - 1 + N]
                    s[TAB[i][2] - 1 + N] = t
                else:
                    s[TAB[i][1] - 1 - N] = s[TAB[i][2] - 1 - N]
                    s[TAB[i][2] - 1 - N] = t
        else:
            flip = False
    else:
        if TAB[i][0] == 1:
            t = s[TAB[i][1] - 1]
            s[TAB[i][1] - 1] = s[TAB[i][2] - 1]
            s[TAB[i][2] - 1] = t
        else:
            flip = True

if flip:
    for i in range(N):
        print(s[i+N], end='')
    for i in range(N):
        print(s[i], end='')
else:
    for i in range(2*N):
        print(s[i], end='')
