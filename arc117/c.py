import io
import sys

# input here
_INPUT = """\
21
BWBRRBBRWBRBBBRRBWWWR

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
c = input()
mod = 3

p = []
for i in c:
    if i == 'B':
        p.append(0)
    elif i == 'W':
        p.append(1)
    else:
        p.append(2)

if N % 2:
    ans = p[0] + p[-1]
    comb = N - 1
    for i in range(1, (N - 1) // 2):
        ans += comb * (p[i] + p[-(i+1)])
        comb = comb * (N - 1 - i) // (i + 1)
    ans += comb * p[(N - 1) // 2]
    ans %= 3
else:
    ans = p[0] + p[-1]
    comb = N - 1
    for i in range(1, N // 2):
        ans += comb * (p[i] + p[-(i + 1)])
        comb = comb * (N - 1 - i) // (i + 1)
    ans = -ans % 3

if ans == 0:
    print('B')
elif ans == 1:
    print('W')
else:
    print('R')
