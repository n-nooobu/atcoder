import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
w = list(map(int, input().split()))
l = []
v = []
for _ in range(M):
    t = list(map(int, input().split()))
    l.append(t[0])
    v.append(t[1])


