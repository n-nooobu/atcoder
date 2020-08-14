import numpy as np
import itertools

N = int(input())
XYP = np.array([list(map(int, list(input().split()))) for i in range(N)])

X = np.unique(XYP[:, 0])
Y = np.unique(XYP[:, 1])

ans = [None] * (N + 1)
for x in itertools.product([0, 1], repeat=len(X)):
    for y in itertools.product([0, 1], repeat=len(Y)):
        K = sum(x) + sum(y)
        if K > N:
            continue

        RX = [0]
        RY = [0]
        for x2 in range(len(x)):
            if x[x2]:
                RX.append(X[x2])
        for y2 in range(len(y)):
            if y[y2]:
                RY.append(Y[y2])

        s = 0
        for n in range(N):
            xm = np.abs(np.array(RX) - XYP[n][0]).min()
            ym = np.abs(np.array(RY) - XYP[n][1]).min()
            s += XYP[n][2] * min(xm, ym)

        if ans[K] is None or ans[K] > s:
            ans[K] = s

for k in range(len(ans)):
    print(ans[k])
