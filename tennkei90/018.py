import io
import sys

# input here
_INPUT = """\
5121
312000000 4123 3314
6
123
12
445
4114
42
1233

"""
sys.stdin = io.StringIO(_INPUT)



from math import sin, cos, pi, sqrt, acos, atan

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

"""for i in range(Q):
    E = int(input())
    if E == 0:
        print(0)
    else:
        a = sqrt((-X) ** 2 + (-L / 2 * sin(E / T * 2 * pi) - Y) ** 2 + (-L / 2 * cos(E / T * 2 * pi) + L / 2) ** 2)
        b = sqrt((-X) ** 2 + (-L / 2 * sin(E / T * 2 * pi) - Y) ** 2)
        naiseki = (-X) ** 2 + (-L / 2 * sin(E / T * 2 * pi) - Y) ** 2
        costheta = naiseki / a / b
        theta = acos(costheta)
        print(theta * 180 / pi)"""

for i in range(Q):
    E = int(input())
    a = -L / 2 * cos(E / T * 2 * pi) + L / 2
    b = sqrt((-X) ** 2 + (- L / 2 * sin(E / T * 2 * pi) - Y) ** 2)
    tantheta = a / b
    theta = atan(tantheta)
    print(theta * 180 / pi)
