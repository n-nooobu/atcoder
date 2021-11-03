import io
import sys

# input here
_INPUT = """\
1000000000 1000000000 1000000000000000000 1000000000000000000 1000000000000000000

"""
sys.stdin = io.StringIO(_INPUT)



X, Y, A, B, C = map(int, input().split())

def square3(x, y, a, b, c):
    for e0, e1 in [[x, y], [y, x]]:
        for s, S in [[a, [b, c]], [b, [a, c]], [c, [a, b]]]:
            if s % e0 == 0:
                ee1 = e1 - s // e0
            else:
                ee1 = e1 - s // e0 - 1
            if ee1 > 0:
                if square2(e0, ee1, S[0], S[1]):
                    return True

    return False

def square2(x, y, a, b):
    for e0, e1 in [[x, y], [y, x]]:
        if a % e0 == 0:
            e1 -= a // e0
        else:
            e1 -= a // e0 + 1
        if e1 * e0 >= b:
            return True

    return False

if square3(X, Y, A, B, C):
    print('Yes')
else:
    print('No')
