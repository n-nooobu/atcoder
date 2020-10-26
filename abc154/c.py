import io
import sys

# input here
_INPUT = """\
2
10000000 10000000

"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
if len(c) == N:
    print('YES')
else:
    print('NO')
