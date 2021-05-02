import io
import sys

# input here
_INPUT = """\
hellospaceRhellospace

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

T = []
Tr = []
rev = False
for s in S:
    if s == 'R':
        if rev:
            rev = False
        else:
            rev = True
    else:
        if rev:
            if Tr and Tr[-1] == s:
                Tr.pop(-1)
            else:
                Tr.append(s)
        else:
            if T and T[-1] == s:
                T.pop(-1)
            else:
                T.append(s)

p = 0
while p < len(T) and p < len(Tr):
    if T[p] == Tr[p]:
        p += 1
    else:
        break
if rev:
    if p >= len(T) and p >= len(Tr):
        print('')
    elif p >= len(T):
        for i in range(p, len(Tr)):
            print(Tr[i], end='')
    elif p >= len(Tr):
        for i in range(len(T)-1, p-1, -1):
            print(T[i], end='')
    else:
        for i in range(len(T) - 1, p - 1, -1):
            print(T[i], end='')
        for i in range(p, len(Tr)):
            print(Tr[i], end='')
else:
    if p >= len(T) and p >= len(Tr):
        print('')
    elif p >= len(T):
        for i in range(len(Tr) - 1, p - 1, -1):
            print(Tr[i], end='')
    elif p >= len(Tr):
        for i in range(p, len(T)):
            print(T[i], end='')
    else:
        for i in range(len(Tr) - 1, p - 1, -1):
            print(Tr[i], end='')
        for i in range(p, len(T)):
            print(T[i], end='')
