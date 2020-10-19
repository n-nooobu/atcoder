import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N, A, B = map(int, input().split())

print(N - A + B)
