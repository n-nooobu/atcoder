import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

dp = [[[0] * 3 for j in range(N)] for i in range(N)]


