import io
import sys

# input here
_INPUT = """\
1
a

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = [input() for _ in range(N)]

dic = {}
for i in range(N):
    if S[i] in dic:
        dic[S[i]] += 1
    else:
        dic[S[i]] = 1

ans = ['', 0]
for name, value in dic.items():
    if value > ans[1]:
        ans[0] = name
        ans[1] = value

print(ans[0])
