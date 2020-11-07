import io
import sys

# input here
_INPUT = """\
8
8 2 7 3 4 5 6 1


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

l = []
for i in range(N):
    l.append([A[i], i + 1])

l = sorted(l)
for i in range(N):
    print(l[i][1], end=' ')
