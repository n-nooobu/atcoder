import io
import sys

# input here
_INPUT = """\
4
ushi
tapu
nichia
kun


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = [input() for _ in range(N)]

dict = {}
s = set()

for i in range(N):
    if S[i] in dict:
        dict[S[i]] += 1
    else:
        dict[S[i]] = 1

v = list(dict.values())
k = list(dict.keys())
m = max(v)
for i in range(len(dict)):
    if v[i] == m:
        s.add(k[i])

s_sort = sorted(list(s))
for i in range(len(s_sort)):
    print(s_sort[i])
