import io
import sys

# input here
_INPUT = """\
6
1 2 3 4 5 6
1 2 3 4 5 6

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
W = list(map(int, input().split()))
B = list(map(int, input().split()))

grundy = [[0] * 1326 for _ in range(51)]
for i in range(51):
    for j in range(1326):
        mex = [0] * 1326
        if i >= 1 and j + i < 1326:
            mex[grundy[i - 1][j + i]] = 1
        for k in range(1, j // 2 + 1):
            mex[grundy[i][j - k]] = 1
        for l in range(1326):
            if mex[l] == 0:
                grundy[i][j] = l
                break

ans = 0
for i in range(N):
    ans ^= grundy[W[i]][B[i]]

if ans:
    print('First')
else:
    print('Second')
