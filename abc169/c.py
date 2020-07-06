import math

A, B = input().split(' ')

A = int(A)
B = round(float(B) * 100)
print(math.floor(A * B // 100))