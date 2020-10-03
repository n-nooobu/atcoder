import io
import sys

# input here
_INPUT = """\
1000000000000000000 1
"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())

if N > K:
    N %= K

print(min(N, K - N))
