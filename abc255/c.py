import io
import sys

# input here
_INPUT = """\
-555555555555555555 -1000000000000000000 1000000 1000000000000

"""
sys.stdin = io.StringIO(_INPUT)



import math

X, A, D, N = map(int, input().split())

if D == 0:
    print(abs(X - A))
elif (X - A) % D == 0 and 0 <= (X - A) // D < N:
    print(0)
elif D > 0 and X < A:
    print(abs(X - A))
elif D > 0 and X > A + (N - 1) * D:
    print(abs(X - A - (N - 1) * D))
elif D < 0 and X > A:
    print(abs(X - A))
elif D < 0 and X < A + (N - 1) * D:
    print(abs(X - A - (N - 1) * D))
elif D > 0:
    tmp = (X - A) / D
    small_i = math.floor(tmp)
    big_i = math.ceil(tmp)

    small_a = A + small_i * D
    big_a = A + big_i * D

    if abs(X - small_a) < abs(X - big_a):
        print(abs(X - small_a))
    else:
        print(abs(X - big_a))
else:
    tmp = (X - A) / D
    small_i = math.ceil(tmp)
    big_i = math.floor(tmp)

    small_a = A + small_i * D
    big_a = A + big_i * D

    if abs(X - small_a) < abs(X - big_a):
        print(abs(X - small_a))
    else:
        print(abs(X - big_a))
