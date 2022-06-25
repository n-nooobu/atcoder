import io
import sys

# input here
_INPUT = """\
aaaabbbaa

"""
sys.stdin = io.StringIO(_INPUT)



import sys

S = input()

al, ar = 0, 0
l, r = 0, len(S) - 1
while l < len(S) and S[l] == 'a':
    l += 1
while r >= 0 and S[r] == 'a':
    r -= 1

if l == len(S) - 1:
    print('Yes')
elif l > len(S) - 1 - r:
    print('No')
else:
    while l < r:
        if S[l] != S[r]:
            print('No')
            sys.exit()
        l += 1
        r -= 1
    print('Yes')
