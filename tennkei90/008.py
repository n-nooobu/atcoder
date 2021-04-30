import io
import sys

# input here
_INPUT = """\
140
aaaaaaaaaaaaaaaaaaaattttttttttttttttttttccccccccccccccccccccooooooooooooooooooooddddddddddddddddddddeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrr


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = input()
mod = 10 ** 9 + 7

a = {'atcoder'[i]: i for i in range(7)}
c = [0] * 7 + [1]
for i in range(N-1, -1, -1):
    if S[i] in a:
        c[a[S[i]]] = (c[a[S[i]]] + c[a[S[i]]+1]) % mod

print(c[0])
