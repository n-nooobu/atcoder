import io
import sys

# input here
_INPUT = """\
5 5
1 2
3 5
5 1
3 4
2 3

"""
sys.stdin = io.StringIO(_INPUT)



import sys

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

cnt = [0] * N
for i in range(M):
    cnt[ab[i][0] - 1] += 1
    cnt[ab[i][1] - 1] += 1

for i in range(N):
    if cnt[i] % 2:
        print('NO')
        sys.exit()

print('YES')
