import io
import sys

# input here
_INPUT = """\
20
407 361
167 433
756 388
-551 -47
306 -471
36 928
338 -355
911 852
288 70
-961 -769
-668 -386
-690 -378
182 -609
-677 401
-458 -112
184 -131
-243 888
-163 471
-11 997
119 544


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

XY = []
for i in range(N):
    x, y = map(int, input().split())
    XY.append([x, y, i])
X = sorted(XY, key=lambda a: a[0])
Y = sorted(XY, key=lambda a: a[1])

def cal_tyebi(x0, y0, x1, y1):
    return max(abs(x0 - x1), abs(y0 - y1))

ma = 0
ma_idx = [0, 0]
for x, y, i in XY:
    if cal_tyebi(x, y, X[0][0], X[0][1]) > cal_tyebi(x, y, X[-1][0], X[-1][1]):
        x_max = [cal_tyebi(x, y, X[0][0], X[0][1]), i, X[0][2]]
    else:
        x_max = [cal_tyebi(x, y, X[-1][0], X[-1][1]), i, X[-1][2]]
    if cal_tyebi(x, y, Y[0][0], Y[0][1]) > cal_tyebi(x, y, Y[-1][0], Y[-1][1]):
        y_max = [cal_tyebi(x, y, Y[0][0], Y[0][1]), i, Y[0][2]]
    else:
        y_max = [cal_tyebi(x, y, Y[-1][0], Y[-1][1]), i, Y[-1][2]]
    if x_max[0] > y_max[0]:
        if x_max[0] > ma:
            ma = x_max[0]
            ma_idx = [x_max[1], x_max[2]]
    else:
        if y_max[0] > ma:
            ma = y_max[0]
            ma_idx = [y_max[1], y_max[2]]

ma2 = 0
ma2_idx = [0, 0]
for x, y, i in XY:
    if cal_tyebi(x, y, X[0][0], X[0][1]) > cal_tyebi(x, y, X[-1][0], X[-1][1]):
        x_max = [cal_tyebi(x, y, X[0][0], X[0][1]), i, X[0][2]]
    else:
        x_max = [cal_tyebi(x, y, X[-1][0], X[-1][1]), i, X[-1][2]]
    if cal_tyebi(x, y, Y[0][0], Y[0][1]) > cal_tyebi(x, y, Y[-1][0], Y[-1][1]):
        y_max = [cal_tyebi(x, y, Y[0][0], Y[0][1]), i, Y[0][2]]
    else:
        y_max = [cal_tyebi(x, y, Y[-1][0], Y[-1][1]), i, Y[-1][2]]
    if x_max[0] > y_max[0]:
        if x_max[0] > ma2 and not ((x_max[1] == ma_idx[0] or x_max[1] == ma_idx[1]) and (x_max[2] == ma_idx[0] or x_max[2] == ma_idx[1])):
            ma2 = x_max[0]
            ma2_idx = [x_max[1], x_max[2]]
    else:
        if y_max[0] > ma2 and not ((y_max[1] == ma_idx[0] or y_max[1] == ma_idx[1]) and (y_max[2] == ma_idx[0] or y_max[2] == ma_idx[1])):
            ma2 = y_max[0]
            ma2_idx = [y_max[1], y_max[2]]

print(ma2)
