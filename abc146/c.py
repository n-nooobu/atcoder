import io
import sys

# input here
_INPUT = """\
1234 56789 314159265

"""
sys.stdin = io.StringIO(_INPUT)



A, B, X = map(int, input().split())

if 10 ** 9 * A + len(str(10 ** 9)) * B <= X:
    print(10 ** 9)
else:
    low = 0
    high = 10 ** 9
    C = 10 ** 9 // 2
    while high - low > 1:
        if C * A + len(str(C)) * B <= X:
            low = C
        else:
            high = C
        C = (high + low) // 2

    print(C)
