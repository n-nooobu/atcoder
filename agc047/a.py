import math

N = int(input())
A = [float(input()) for i in range(N)]

A_decimal = []
is_int = [0] * N
for i in range(N):
    tmp = round(math.modf(A[i])[0], 9)
    if tmp == 0:
        is_int[i] += 1
    A_decimal.append(tmp)

