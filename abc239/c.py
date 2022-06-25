import io
import sys

# input here
_INPUT = """\
1000000000 1000000000 999999999 999999999

"""
sys.stdin = io.StringIO(_INPUT)



import sys

x1, y1, x2, y2 = map(int, input().split())

for dx in [-2, -1, 0, 1, 2]:
    for dy in [-2, -1, 0, 1, 2]:
        if abs(dx) * abs(dy) == 2 and abs(x2 - (x1 + dx)) * abs(y2 - (y1 + dy)) == 2:
            print('Yes')
            sys.exit()

print('No')
