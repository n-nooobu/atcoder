import io
import sys

# input here
_INPUT = """\
8 5 22
100 3 7 5 3 1
164 4 5 2 7 8
334 7 2 7 2 9
234 4 7 2 8 2
541 5 4 3 3 6
235 4 8 6 9 7
394 3 6 1 6 2
872 8 4 3 7 2
"""
sys.stdin = io.StringIO(_INPUT)



import itertools
import numpy as np
import copy

N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]
CA = np.array(CA)

ans = 10 ** 7
for i in itertools.product([0, 1], repeat=N):
    tCA = copy.copy(CA)
    for j in range(N):
        if i[j] == 0:
            tCA[j] = np.zeros(CA.shape[1])
    s = np.sum(tCA, axis=0)
    l = sum(k >= X for k in s[1:])
    if s[0] < ans and l == M:
        ans = s[0]

if ans == 10 ** 7:
    print(-1)
else:
    print(ans)
