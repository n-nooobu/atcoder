import io
import sys

# input here
_INPUT = """\
2 4
4 3 2 1
5 6 7 8

"""
sys.stdin = io.StringIO(_INPUT)



import sys

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for i1 in range(H):
    for j1 in range(W):
        for i2 in range(H):
            for j2 in range(W):
                if i1 >= i2 or j1 >= j2:
                    continue
                if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                    print('No')
                    sys.exit()

print('Yes')
