import io
import sys

# input here
_INPUT = """\
-9 99 -999 9999

"""
sys.stdin = io.StringIO(_INPUT)



Sx, Sy, Gx, Gy = map(int, input().split())

print(Sx + (Gx - Sx) * Sy / (Sy + Gy))
