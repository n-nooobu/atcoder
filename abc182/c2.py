import io
import sys

# input here
_INPUT = """\
6227384

"""
sys.stdin = io.StringIO(_INPUT)



N = input()

count = [0] * 3
for i in range(len(N)):
    count[int(N[i]) % 3] += 1
s = count[2] * 2 + count[1]

if s % 3 == 0:
    print(0)
elif sum(count) == 1:
    print(-1)
elif count[s % 3] > 0:
    print(1)
elif count[0] >= 1 and count[3 - s % 3] >= 2:
    print(2)
elif count[0] == 0 and count[3 - s % 3] >= 3:
    print(2)
else:
    print(-1)
