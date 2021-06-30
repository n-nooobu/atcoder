import io
import sys

# input here
_INPUT = """\
3
11 7
3 2
6 7

"""
sys.stdin = io.StringIO(_INPUT)



import math

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = math.inf
for i in range(N):
    for j in range(N):
        if i == j:
            time = AB[i][0] + AB[j][1]
        else:
            time = max(AB[i][0], AB[j][1])
        ans = min(ans, time)

print(ans)
