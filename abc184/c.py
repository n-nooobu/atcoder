import io
import sys

# input here
_INPUT = """\
2 3
998244353 998244853

"""
sys.stdin = io.StringIO(_INPUT)



r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

if r1 == r2 and c1 == c2:
    print(0)
elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
    print(1)
elif abs(r2 - c2 - r1 + c1) <= 4 or abs(r2 + c2 - r1 - c1) <= 4:
    print(2)
elif (r1 + c1) % 2 == (r2 + c2) % 2:
    print(2)
else:
    print(3)
