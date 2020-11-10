import io
import sys

# input here
_INPUT = """\
12 21 10

"""
sys.stdin = io.StringIO(_INPUT)



import math

a, b, x = map(int, input().split())

theta = math.atan(b / a)
y0 = 2 * b - 2 * x / a ** 2
theta0 = math.atan(y0 / a)
y1 = 2 * x / a / b
theta1 = math.atan(b / y1)
if theta0 <= theta:
    print(theta0 * 180 / math.pi)
elif theta1 > theta:
    print(theta1 * 180 / math.pi)
