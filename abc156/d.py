import io
import sys

# input here
_INPUT = """\
1000000000 141421 173205


"""
sys.stdin = io.StringIO(_INPUT)



n, a, b = map(int, input().split())

mod = 10 ** 9 + 7

two = [1] * (10 ** 5 + 1)
for i in range(1, 10 ** 5 + 1):
    two[i] = two[i - 1] * 2 % mod
if n > 10 ** 5:
    two = two[10 ** 5] * two[n % (10 ** 5)] % mod
else:
    two = two[n]

comb = 1
for i in range(a):
    comb = comb * (n - i)
    comb = comb
comb_a = comb
for i in range(a, b):
    comb = comb * (n - i) % mod
comb_b = comb
t = 1
for i in range(a):
    t = t * (i + 1) % mod
A = t
for i in range(a, b):
    t = t * (i + 1) % mod
B = t


print((two - comb_a - comb_b - 1) % mod)
