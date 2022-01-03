import io
import sys

# input here
_INPUT = """\
50

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

if N >= 42:
    print('AGC' + str(N + 1).zfill(3))
else:
    print('AGC' + str(N).zfill(3))
