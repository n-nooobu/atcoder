import io
import sys

# input here
_INPUT = """\
3
100000
30000
20000

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

if all(a[i] % 2 == 0 for i in range(N)):
    print('second')
else:
    print('first')
