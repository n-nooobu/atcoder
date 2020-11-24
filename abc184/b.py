import io
import sys

# input here
_INPUT = """\
20 10
xxxxxxxxxxxxxxxxxxxx

"""
sys.stdin = io.StringIO(_INPUT)



N, X = map(int, input().split())
S = input()

for i in range(N):
    if S[i] == 'o':
        X += 1
    elif S[i] == 'x':
        X = max(0, X - 1)

print(X)
