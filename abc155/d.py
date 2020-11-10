import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))

for i in range(N):

