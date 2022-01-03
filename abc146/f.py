import io
import sys

# input here
_INPUT = """\
5 4
011110

"""
sys.stdin = io.StringIO(_INPUT)



import sys

N, M = map(int, input().split())
S = input()[::-1]

if S[0] == '1' or S[-1] == '1':
    print(-1)
    sys.exit()

ok = 0
k = 0
ans = []
for i in range(1, N + 1):
    if S[i] == '0':
        ok = i
    k += 1
    if k == M:
        if i - ok >= M:
            print(-1)
            sys.exit()
        k = i - ok
        ans.append(M - k)

if k != 0:
    ans.append(k)

print(*ans[::-1], sep=' ')
