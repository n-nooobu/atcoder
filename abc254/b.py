import io
import sys

# input here
_INPUT = """\
10

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

prev = []
for i in range(N):
    curr = []
    for j in range(i + 1):
        if (j == 0) or (j == i):
            curr.append(1)
        else:
            curr.append(prev[j - 1] + prev[j])
    print(*curr)
    prev = curr
