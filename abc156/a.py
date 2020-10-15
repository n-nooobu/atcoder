import io
import sys

# input here
_INPUT = """\
2 2919


"""
sys.stdin = io.StringIO(_INPUT)



N, R = map(int, input().split())

if N >= 10:
    print(R)
else:
    print(R + 100 * (10 - N))
