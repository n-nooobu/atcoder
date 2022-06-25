import io
import sys

# input here
_INPUT = """\
5 3
89 62 15
44 36 17
4 24 24
25 98 99
66 33 57

"""
sys.stdin = io.StringIO(_INPUT)



import sys
import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

for i in itertools.product(range(K), repeat=N):
    xor = 0
    for j in range(N):
        xor ^= T[j][i[j]]
    if xor == 0:
        print('Found')
        sys.exit()

print('Nothing')
