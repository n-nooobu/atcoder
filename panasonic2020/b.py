import io
import sys

# input here
_INPUT = """\
1 5
"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())

if H == 1 or W == 1:
    print(1)
else:
    if H % 2 == 1 and W % 2 == 1:
        print(int(H * (W + 1) / 2) - H // 2)
    else:
        print(int(H * W / 2))
