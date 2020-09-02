import io
import sys

# input here
_INPUT = """\
codeforces
atcoder
"""
sys.stdin = io.StringIO(_INPUT)



S = input()
T = input()

counts = []
for i in range(len(S) - (len(T) - 1)):
    count = 0
    for j in range(len(T)):
        if S[i + j] == T[j]:
            count += 1
    counts.append(count)

print(len(T) - max(counts))
