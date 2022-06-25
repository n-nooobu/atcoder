import io
import sys

# input here
_INPUT = """\
333

"""
sys.stdin = io.StringIO(_INPUT)



H = int(input())

print((H * (12800000 + H)) ** 0.5)
