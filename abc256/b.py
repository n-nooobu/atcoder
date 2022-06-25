import io
import sys

# input here
_INPUT = """\
10
2 2 4 1 1 1 4 2 2 1

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

ans = 0
masu = [0, 0, 0, 0]
for i in range(N):
    masu[0] = 1
    for j in range(3, -1, -1):
        if masu[j]:
            if j + A[i] >= 4:
                ans += 1
            else:
                masu[j + A[i]] = 1
            masu[j] = 0

print(ans)
