import io
import sys

# input here
_INPUT = """\
100000 1 1 1

"""
sys.stdin = io.StringIO(_INPUT)



V, A, B, C = map(int, input().split())

while V >= 0:
    for a, b in [['F', A], ['M', B], ['T', C]]:
        V -= b
        if V < 0:
            print(a)
            break
