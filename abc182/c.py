import io
import sys

# input here
_INPUT = """\
11

"""
sys.stdin = io.StringIO(_INPUT)



N = input()

n = []
c = [0] * 3
for i in range(len(N)):
    n.append(int(N[i]) % 3)
    c[int(N[i]) % 3] += 1
s = sum(n)

if s % 3 == 0:
    print(0)
elif len(n) == 1:
    print(-1)
else:
    if s % 3 == 1 and c[1] >= 1:
        print(1)
    elif s % 3 == 2 and c[2] >= 1:
        print(1)
    else:
        if c[1] == 0:
            if c[0] >= 1:
                for i in range(1, c[2] + 1):
                    s -= 2
                    if s % 3 == 0:
                        print(i)
                        exit()
            else:
                for i in range(1, c[2]):
                    s -= 2
                    if s % 3 == 0:
                        print(i)
                        exit()
        elif c[2] == 0:
            if c[0] >= 1:
                for i in range(1, c[1] + 1):
                    s -= 1
                    if s % 3 == 0:
                        print(i)
                        exit()
            else:
                for i in range(1, c[1]):
                    s -= 1
                    if s % 3 == 0:
                        print(i)
                        exit()
        print(-1)
