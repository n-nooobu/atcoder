import io
import sys

# input here
_INPUT = """\
20
2 90
1 67
2 9
2 17
2 85
2 43
2 11
1 32
2 16
1 19
2 65
1 14
1 51
2 94
1 4
1 55
2 90
1 89
1 35
2 81
20
3 17
5 5
11 11
8 10
3 13
2 6
3 7
3 5
12 18
4 8
3 16
6 8
3 20
1 12
1 6
5 16
3 10
17 19
4 4
7 15


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
CP = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())

cum = [[0] * (N + 1) for _ in range(2)]
for i, (c, p) in enumerate(CP):
    cum[c - 1][i + 1] = p
for i in range(1, N + 1):
    for c in [0, 1]:
        cum[c][i] += cum[c][i - 1]
for i in range(Q):
    l, r = map(int, input().split())
    for c in [0, 1]:
        print(cum[c][r] - cum[c][l - 1], end=' ')
    print()
