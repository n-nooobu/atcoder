import io
import sys

# input here
_INPUT = """\
200



"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

for i in range(40):
    if (i - 1) * 100 < N <= i * 100:
        print(i)
