import io
import sys

# input here
_INPUT = """\
4
aaaa
a
aaa
aa
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = [input() for _ in range(N)]

dic = {}
for i in range(N):
    dic[S[i]] = 0

print(len(dic.keys()))
