import io
import sys

# input here
_INPUT = """\
5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in itertools.permutations(range(1, N)):
    t = T[0][i[0]]
    for j in range(N - 2):
        t += T[i[j]][i[j + 1]]
    t += T[i[-1]][0]
    if t == K:
        ans += 1

print(ans)
