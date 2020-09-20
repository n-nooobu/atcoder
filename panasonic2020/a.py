import io
import sys

# input here
_INPUT = """\
27
"""
sys.stdin = io.StringIO(_INPUT)



l = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
K = int(input())

print(l[K - 1])
