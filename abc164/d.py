import io
import sys

# input here
_INPUT = """\
14282668646
"""
sys.stdin = io.StringIO(_INPUT)



S = input()

s = [0] * (len(S) + 1)
t = 1
for i in range(1, len(S) + 1):
    s[i] = (s[i - 1] + int(S[-i]) * t) % 2019
    t = t * 10 % 2019

ans = 0
l = [0] * 2019
for i in range(len(S) + 1):
    l[s[i]] += 1

for i in range(2019):
    ans += l[i] * (l[i] - 1) // 2

print(ans)
