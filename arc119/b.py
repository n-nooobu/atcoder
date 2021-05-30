import io
import sys

# input here
_INPUT = """\
119
10101111011101001011111000111111101011110011010111111111111111010111111111111110111111110111110111101111111111110111011
11111111111111111111111111011111101011111011110111110010100101001110111011110111111111110010011111101111111101110111011

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = input()
T = input()

s, t = [], []
for i in range(N):
    if S[i] == '0':
        s.append(i)
    if T[i] == '0':
        t.append(i)

if len(s) != len(t):
    print(-1)
else:
    ans = len(s)
    for i, j in zip(s, t):
        if i == j:
            ans -= 1
    print(ans)
