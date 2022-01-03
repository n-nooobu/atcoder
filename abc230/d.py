import io
import sys

# input here
_INPUT = """\
5 2
1 100
1 1000000000
101 1000
9982 44353
1000000000 1000000000

"""
sys.stdin = io.StringIO(_INPUT)



N, D = map(int, input().split())
LR = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])

for i in range(N):
    LR[i][1] += D - 1

i = LR[0][1]
ans = 1
for j in range(1, N):
    if LR[j][0] <= i <= LR[j][1]:
        continue
    ans += 1
    i = LR[j][1]

print(ans)
