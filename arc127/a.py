import io
import sys

# input here
_INPUT = """\
120

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

l = [0]
for i in range(1, 16):
    s = 0
    for j in range(16):
        a = int('1' * i + '0' * j)
        b = int('1' * (i - 1) + '2' + '0' * j)
        if N < a: continue
        if N >= b:
            s += b - a
        else:
            s += N - a + 1
    l.append(s)

print(sum(l))
