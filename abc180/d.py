import io
import sys

# input here
_INPUT = """\
6 10 5 5

"""
sys.stdin = io.StringIO(_INPUT)



X, Y, A, B = map(int, input().split())

A_ = X
for kako in range(10000):
    if A_ * (A - 1) > B or A_ * A > Y:
        break
    A_ *= A

if (Y - A_) % B == 0:
    print(kako + (Y - A_) // B - 1)
else:
    print(kako + (Y - A_) // B)
