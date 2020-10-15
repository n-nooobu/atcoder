import io
import sys

# input here
_INPUT = """\
1000000000 141421 173205


"""
sys.stdin = io.StringIO(_INPUT)



n, a, b = map(int, input().split())

mod = 10 ** 9 + 7

two = pow(2, n, mod)

comb = 1
for i in range(a):
    comb = comb * (n - i) % mod
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

comb_a = comb_a * pow(A, mod - 2, mod) % mod
comb_b = comb_b * pow(B, mod - 2, mod) % mod

print((two - comb_a - comb_b - 1) % mod)
