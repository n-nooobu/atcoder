import io
import sys

# input here
_INPUT = """\
1000000000

"""
sys.stdin = io.StringIO(_INPUT)



import itertools
from bisect import *

N = int(input())

two = [1]
for i in range(40):
    two.append(two[-1] * 2)

plus = []
minus = []
for i in itertools.product(range(2), repeat=16):
    t = 0
    s = ''
    for j, k in enumerate(range(0, 32, 2)):
        t += two[k] * i[j]
        s = str(i[j]) + s
    plus.append([t, s])

    t = 0
    s = ''
    for j, k in enumerate(range(1, 32, 2)):
        t += two[k] * i[j]
        s = str(i[j]) + s
    minus.append([t, s])
minus = sorted(minus)
m = []
for i in minus:
    m.append(i[0])

for p, t in plus:
    q = bisect_left(m, p - N)
    if q < len(m) and m[q] == p - N:
        a = minus[q][1]
        b = t
        break

flag = False
ans = ''
for i in range(16):
    if flag:
        ans += a[i]
    elif a[i] == '1':
        flag = True
        ans += a[i]
    if flag:
        ans += b[i]
    elif b[i] == '1':
        flag = True
        ans += b[i]

if ans:
    print(ans)
else:
    print(0)
