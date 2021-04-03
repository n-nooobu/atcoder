import io
import sys

# input here
_INPUT = """\
3 4 5
700 198 700 198
198 700 198 700
700 198 700 198

"""
sys.stdin = io.StringIO(_INPUT)



R, C, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

ans = 0
for i in range(min(D + 1, R)):
    for j in range(min(D + 1 - i, C)):
        if (i + j) % 2 == D % 2:
            ans = max(ans, A[i][j])

print(ans)
