import io
import sys

# input here
_INPUT = """\
7
firebox

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
s = input()

old0 = 'a'
old1 = 'b'
k = 0
while True:
    now = s[k]
    if old0 == 'f' and old1 == 'o' and now == 'x':
        old0 = s[k - 4]
        old1 = s[k - 3]
        s = s[:k - 2] + s[k + 1:]
        k -= 2
    else:
        old0 = old1
        old1 = now
        k += 1
    if k >= len(s):
        break

print(len(s))
