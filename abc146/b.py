import io
import sys

# input here
_INPUT = """\
2
ABCXYZ

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = input()

ans = ''
for i in range(len(S)):
    if ord(S[i]) + N <= 90:
        ans += chr(ord(S[i]) + N)
    else:
        ans += chr(ord(S[i]) + N - 26)

print(ans)
