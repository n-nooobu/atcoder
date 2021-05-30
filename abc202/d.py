import io
import sys

# input here
_INPUT = """\
30 30 118264581564861424


"""
sys.stdin = io.StringIO(_INPUT)



A, B, K = map(int, input().split())

l = [1]
for i in range(1, 61):
    l.append(l[-1] * i)

a = 1
for i in range(A + B):
    n = A + B - (i + 1)
    r = A - a
    comb = int(l[n] / (l[n - r] * l[r]))
    if K <= comb:
        print('a', end='')
        a += 1
    else:
        print('b', end='')
        K -= comb
