import io
import sys

# input here
_INPUT = """\
5 896 483
228 59
529 310
339 60
78 266
659 391

"""
sys.stdin = io.StringIO(_INPUT)



N, D, H = map(int, input().split())
dh = [list(map(int, input().split())) for _ in range(N)]

ans = 1050
for i in range(N):
    flag = True
    for j in range(N):
        if (dh[j][1] - H) * (D - dh[i][0]) > (dh[j][0] - D) * (H - dh[i][1]):
            flag = False
    if flag:
        ans = min(ans, H - D * (H - dh[i][1]) / (D - dh[i][0]))

print(max(ans, 0))
