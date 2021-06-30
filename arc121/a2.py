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

house = []
for i in [0, 1, -2, -1]:
    house.append(X[i])
for i in [0, 1, -2, -1]:
    if not Y[i] in house:
        house.append(Y[i])

tyebi = []
for i in range(len(house)):
    for j in range(i + 1, len(house)):
        tyebi.append(max(abs(house[i][0] - house[j][0]), abs(house[i][1] - house[j][1])))
tyebi = sorted(tyebi)

print(tyebi[-2])
