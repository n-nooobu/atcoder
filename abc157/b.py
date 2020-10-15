import io
import sys

# input here
_INPUT = """\
84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30


"""
sys.stdin = io.StringIO(_INPUT)



A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]

for i in range(3):
    for j in range(3):
        for k in range(N):
            if A[i][j] == b[k]:
                A[i][j] = 0

if (A[0][0] + A[0][1] + A[0][2] == 0) or (A[1][0] + A[1][1] + A[1][2] == 0) or (A[2][0] + A[2][1] + A[2][2] == 0) or (A[0][0] + A[1][0] + A[2][0] == 0) or (A[0][1] + A[1][1] + A[2][1] == 0) or (A[0][2] + A[1][2] + A[2][2] == 0) or (A[0][0] + A[1][1] + A[2][2] == 0) or (A[0][2] + A[1][1] + A[2][0] == 0):
    print('Yes')
else:
    print('No')
