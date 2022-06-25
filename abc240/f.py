import io
import sys

# input here
_INPUT = """\
3
3 7
-1 2
2 3
-3 2
10 472
-4 12
1 29
2 77
-1 86
0 51
3 81
3 17
-2 31
-4 65
4 23
1 1000000000
4 1000000000

"""
sys.stdin = io.StringIO(_INPUT)



T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(N)]

    a = 0
    num = 0
    l = []
    for i in range(N):
        if a > 0 and a + xy[i][0] * xy[i][1] < 0:
            pass
        if a + xy[i][0] * xy[i][1] > 0:
            num += xy[i][1]
            l.append(num)

