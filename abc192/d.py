import io
import sys

# input here
_INPUT = """\
11
1500

"""
sys.stdin = io.StringIO(_INPUT)



X = input()
M = int(input())

nums = []
for s in X:
    nums.append(int(s))
d = max(nums) + 1

def shinsuu(X, n):
    t = 0
    for i, s in enumerate(X):
        t += int(s) * n ** (len(X) - 1 - i)
    return t

if len(X) == 1:
    if int(X) >= M:
        print(1)
    else:
        print(0)
elif len(X) > 4:
    a = set()
    while True:
        t = shinsuu(X, d)
        if t <= M:
            a.add(t)
            d += 1
        else:
            break
    print(len(a))
else:
    low = d
    high = 10 ** 18 + 10
    n = (high + low) // 2
    while high - low > 1:
        t = shinsuu(X, n)
        if t < M:
            low = n
        else:
            high = n
        n = (high + low) // 2
    t_high = shinsuu(X, high)
    t_low = shinsuu(X, low)
    if t_high == M:
        ans = high - d + 1
    elif t_low > M:
        ans = 0
    else:
        ans = high - d
    a = set()
    for i in range(d, d + ans):
        a.add(shinsuu(X, i))

    print(len(a))
