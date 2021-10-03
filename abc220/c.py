import io
import sys

# input here
_INPUT = """\
3
3 5 2
19


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))
X = int(input())

s = sum(A)
n = X // s
y = X % s

t = 0
for i in range(N):
    t += A[i]
    if t > y:
        print(N * n + i + 1)
        break
