import io
import sys

# input here
_INPUT = """\
3 4 4


"""
sys.stdin = io.StringIO(_INPUT)



R, X, Y = map(int, input().split())

D = (X ** 2 + Y ** 2) ** 0.5
if D < R:
    print(2)
else:
    if D % R == 0:
        print(int(D // R))
    else:
        print(int(D // R + 1))
