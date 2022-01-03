import io
import sys

# input here
_INPUT = """\
2
ABCCBA

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = input()

cnt = [[0] * (3 * N) for _ in range(3)]
if S[-1] == 'A':
    cnt[0][-1] = 1
elif S[-1] == 'B':
    cnt[1][-1] = 1
else:
    cnt[2][-1] = 1

alpha = ['A', 'B', 'C']
for i in range(3):
    for j in reversed(range(3 * N - 1)):
        cnt[i][j] = cnt[i][j + 1]
        if S[j] == alpha[i]:
            cnt[i][j] += 1

ans = [0] * (3 * N)

