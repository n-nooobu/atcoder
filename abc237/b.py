import io
import sys

# input here
_INPUT = """\
2 2
1000000000 1000000000
1000000000 1000000000

"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for i in range(W):
    for j in range(H):
        print(A[j][i], end=' ')
    print()
