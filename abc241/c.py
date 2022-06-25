import io
import sys

# input here
_INPUT = """\
6
#..##.
.#....
......
......
....#.
.....#
"""
sys.stdin = io.StringIO(_INPUT)



import sys

N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i <= N - 6:
            cnt = 0
            for k in range(6):
                if S[i + k][j] == '#':
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                sys.exit()
        if j <= N - 6:
            cnt = 0
            for k in range(6):
                if S[i][j + k] == '#':
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                sys.exit()
        if i <= N - 6 and j <= N - 6:
            cnt = 0
            for k in range(6):
                if S[i + k][j + k] == '#':
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                sys.exit()
        if i >= 5 and j <= N - 6:
            cnt = 0
            for k in range(6):
                if S[i - k][j + k] == '#':
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                sys.exit()

print('No')
