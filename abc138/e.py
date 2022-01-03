import io
import sys

# input here
_INPUT = """\
contest
sentence

"""
sys.stdin = io.StringIO(_INPUT)



import sys
from bisect import *

s = input()
t = input()

pos = [[] for _ in range(ord('z') - ord('a') + 1)]
for i in range(len(s)):
    pos[ord(s[i]) - ord('a')].append(i + 1)

ans = 0
now_pos = 0
for i in range(len(t)):
    l = pos[ord(t[i]) - ord('a')]
    if not l:
        print(-1)
        sys.exit()
    idx = bisect_right(l, now_pos)
    if idx == len(l):
        ans += len(s) - now_pos + l[0]
        now_pos = l[0]
    else:
        ans += l[idx] - now_pos
        now_pos = l[idx]

print(ans)
