import io
import sys

# input here
_INPUT = """\
XXXX
200000

"""
sys.stdin = io.StringIO(_INPUT)



S = input()
K = int(input())

cnt = [0]
for i in range(len(S)):
    if S[i] == '.':
        cnt.append(cnt[-1] + 1)
    else:
        cnt.append(cnt[-1])

ans = 0
r = 0
for l in range(len((S))):
    while r < len(S) and cnt[r + 1] - cnt[l] <= K:
        r += 1
    ans = max(ans, r - l)

print(ans)
