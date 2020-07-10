import numpy as np

A, B, H, M = map(int, input().split())

Aw = 2 * np.pi / 12 / 60
Bw = 2 * np.pi / 60
thetaA = Aw * (H * 60 + M)
thetaB = Bw * M

if thetaA > thetaB:
    ans = np.sqrt(A ** 2 + B ** 2 - 2 * A * B * np.cos(thetaA - thetaB))
elif thetaB > thetaA:
    ans = np.sqrt(A ** 2 + B ** 2 - 2 * A * B * np.cos(thetaB - thetaA))
else:
    ans = abs(A - B)

print(ans)
