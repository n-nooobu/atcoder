import io
import sys

# input here
_INPUT = """\
1 0
"""
sys.stdin = io.StringIO(_INPUT)



import sys

N, M = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(M)]

if M == 0 and N == 1:
    print(0)
    sys.exit()

l = ['0'] * (N + 1)
for i in range(M):
    if sc[i][0] == 1 and sc[i][1] == 0:
        if N > 1:
            print(-1)
            sys.exit()
        else:
            print(0)
            sys.exit()
    elif l[sc[i][0]] == '0' or l[sc[i][0]] == str(sc[i][1]):
        l[sc[i][0]] = str(sc[i][1])
    else:
        print(-1)
        sys.exit()

if l[1] == '0':
    ans = '1'
else:
    ans = l[1]
for i in range(2, N + 1):
    ans = ans + l[i]

print(ans)
