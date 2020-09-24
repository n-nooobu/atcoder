import io
import sys

# input here
_INPUT = """\
1333333333
"""
sys.stdin = io.StringIO(_INPUT)



X = int(input())

k = 0
y = 100
while y < X:
    k += 1
    r = y // 100
    y += r

print(k)
