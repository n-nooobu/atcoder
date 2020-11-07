import io
import sys

# input here
_INPUT = """\
5


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

if N % 2 == 0:
    print(0.5)
else:
    print(1 - N // 2 / N)
