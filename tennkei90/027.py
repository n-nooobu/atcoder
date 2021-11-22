import io
import sys

# input here
_INPUT = """\
5
e869120
atcoder
e869120
square1001
square1001

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = [input() for _ in range(N)]

user = {}
for i, s in enumerate(S):
    if s in user:
        continue
    user[s] = 1
    print(i + 1)
