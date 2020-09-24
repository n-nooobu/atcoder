import io
import sys

# input here
_INPUT = """\
1 1 0 0
AB
"""
sys.stdin = io.StringIO(_INPUT)



import sys

N, A, B, C = map(int, input().split())
s = [input() for _ in range(N)]

ans = []
for i in range(N):
    if s[i] == 'AB':
        if A >= B:
            A -= 1
            B += 1
            ans.append('B')
        else:
            B -= 1
            A += 1
            ans.append('A')
    elif s[i] == 'AC':
        if A >= C:
            A -= 1
            C += 1
            ans.append('C')
        else:
            C -= 1
            A += 1
            ans.append('A')
    else:
        if B >= C:
            B -= 1
            C += 1
            ans.append('C')
        else:
            C -= 1
            B += 1
            ans.append('B')
    if A < 0 or B < 0 or C < 0:
        print('No')
        sys.exit()

print('Yes')
for i in range(N):
    print(ans[i])
