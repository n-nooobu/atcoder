import numpy as np

N, D = map(int, input().split())
XY = [list(map(int, list(input().split()))) for i in range(N)]

ans = 0
for i in range(N):
    if np.sqrt(XY[i][0]**2 + XY[i][1]**2) <= D:
        ans += 1

print(ans)
