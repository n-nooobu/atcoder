import io
import sys

# input here
_INPUT = """\
100

"""
sys.stdin = io.StringIO(_INPUT)



X = int(input())

a = 0
while a < X:
    a += 100

print(a - X)
