import numpy as np

H, W, M = map(int, list(input().split()))
hw = [list(map(int, list(input().split()))) for i in range(M)]
hw = np.array(hw) - 1

sh = [0] * H
sw = [0] * W
bomb = np.zeros((H, W), dtype=int)
for i in range(M):
    sh[hw[i, 0]] += 1
    sw[hw[i, 1]] += 1
    bomb[hw[i, 0], hw[i, 1]] = 1

h_list = [i for i, x in enumerate(sh) if x == max(sh)]
w_list = [i for i, x in enumerate(sw) if x == max(sw)]

m = 0
for h in h_list:
    for w in w_list:
        if bomb[h, w]:
            m = max(m, sh[h] + sw[w] - 1)
        else:
            m = max(m, sh[h] + sw[w])

print(m)
