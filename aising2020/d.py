import io
import sys

# input here
_INPUT = """\
3
001

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
X = input()

f = [0] * (2 * 10 ** 5)

for i in range(1, 2 * 10 ** 5):
    pc = i % bin(i).count('1')
    cnt = 1
    if pc == 0:
        f[i] = 1
    else:
        f[i] = f[pc] + 1

X10 = int(X, 2)
Xpc = X.count('1')
zeroflag = False
if Xpc - 1 != 0:
    Xm = X10 % (Xpc - 1)
else:
    zeroflag = True
Xp = X10 % (Xpc + 1)
for i in range(N):
    if X[i] == '0':
        x = (Xp + pow(2, len(X) - 1 - i, Xpc + 1)) % (Xpc + 1)
        print(f[x] + 1)
    else:
        if zeroflag:
            print(0)
        else:
            x = (Xm - pow(2, len(X) - 1 - i, Xpc - 1)) % (Xpc - 1)
            print(f[x] + 1)
