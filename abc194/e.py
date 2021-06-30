import io
import sys

# input here
_INPUT = """\
7 7
0 1 2 3 4 5 6

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
A = list(map(int, input().split()))

pos = [[-1] for _ in range(N + 1)]

for i in range(N):
    pos[A[i]].append(i)
for i in range(N + 1):
    pos[i].append(N)

for i in range(N + 1):
    for j in range(len(pos[i]) - 1):
        if pos[i][j + 1] - pos[i][j] - 1 >= M:
            print(i)
            exit()
