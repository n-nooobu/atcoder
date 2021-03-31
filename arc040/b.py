import io
import sys

# input here
_INPUT = """\
4 4
oooo

"""
sys.stdin = io.StringIO(_INPUT)



N, R = map(int, input().split())
S = input()

end = 0
ans = 0
for i in reversed(range(N)):
    if S[i] == '.':
        end = max(0, i - (R - 1))
        ans = max(0, i - (R - 1))
        break

now = 0
while now < N:
    if S[now] == '.':
        ans += 1
        now += R
    else:
        now += 1

print(ans)
