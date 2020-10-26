import io
import sys

# input here
_INPUT = """\
85554

"""
sys.stdin = io.StringIO(_INPUT)



N = input()

five = [False] * len(N)
t = int(N[0])
for i in range(1, len(N)):
    if int(N[i]) == 5 and (t >= 6 or five[i - 1]):
        five[i] = True
    t = int(N[i])

old = False
ans = 0
sa = 0
for i in reversed(range(len(N))):
    if int(N[i]) >= 6:
        if old:
            sa += 9 - int(N[i])
        else:
            ans += 1
            sa += 10 - int(N[i])
            old = True
    elif int(N[i]) <= 4:
        ans += int(N[i])
        old = False
    else:
        if five[i] and not old:
            ans += 1
            sa += 10 - int(N[i])
            old = True
        elif old:
            sa += 9 - int(N[i])
        else:
            ans += int(N[i])

print(ans + sa)
