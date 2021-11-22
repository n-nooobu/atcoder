import io
import sys

# input here
_INPUT = """\
5
1 1
1 1
1 2
2 1 1
3 1 1 1

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
c = [input() for _ in range(N)]

a = set()
for i in range(N):
    a.add(c[i])

print(len(a))
