import io
import sys

# input here
_INPUT = """\
helloAtZoner

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

ans = 0
for i in range(len(S) - 3):
    if S[i: i + 4] == 'ZONe':
        ans += 1

print(ans)
