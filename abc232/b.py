import io
import sys

# input here
_INPUT = """\
atcoder
atcoder

"""
sys.stdin = io.StringIO(_INPUT)



import sys

S = input()
T = input()

if ord(T[0]) - ord(S[0]) >= 0:
    diff = ord(T[0]) - ord(S[0])
else:
    diff = ord(T[0]) - ord(S[0]) + 26

for i in range(1, len(S)):
    if ord(T[i]) - ord(S[i]) >= 0:
        diff2 = ord(T[i]) - ord(S[i])
    else:
        diff2 = ord(T[i]) - ord(S[i]) + 26
    if diff2 != diff:
        print('No')
        sys.exit()

print('Yes')
