import io
import sys

# input here
_INPUT = """\
TSSTTTSS

"""
sys.stdin = io.StringIO(_INPUT)



X = input()

ans = len(X)
stock = 0
for i in range(len(X)):
    if X[i] == 'S':
        stock += 1
    if X[i] == 'T' and stock > 0:
        ans -= 2
        stock -= 1

print(ans)
