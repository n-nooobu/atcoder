import io
import sys

# input here
_INPUT = """\
99992

"""
sys.stdin = io.StringIO(_INPUT)



X = int(input())

ans = 0
while ans == 0:
    prime = True
    for i in range(2, round(X ** 0.5) + 1):
        if X % i == 0:
            prime = False
            break
    if prime:
        ans = X
        print(ans)
    else:
        X += 1
