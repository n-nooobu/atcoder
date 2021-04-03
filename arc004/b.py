import io
import sys

# input here
_INPUT = """\
10
1
2
3
4
5
6
7
8
9
10

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
d = []
for i in range(N):
    d.append(int(input()))

s = sum(d)
m = max(d)

print(s)

if s - m >= m:
    print(0)
else:
    print(m - (s - m))
