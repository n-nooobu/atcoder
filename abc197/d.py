import io
import sys

# input here
_INPUT = """\
4
1 1
2 2

"""
sys.stdin = io.StringIO(_INPUT)



import numpy as np

N = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

X = (x0 + xn2) / 2
Y = (y0 + yn2) / 2
theta = 2 * np.pi / N
z1 = ((x0 - X) + 1j * (y0 - Y)) * (np.cos(theta) + 1j * np.sin(theta)) + X + 1j * Y

print(z1.real, z1.imag)
