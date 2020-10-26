import io
import sys

# input here
_INPUT = """\
8
hmhmnknk uuuuuuuu

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S, T = input().split()

ans = ''
for i in range(N):
    ans += S[i] + T[i]

print(ans)
