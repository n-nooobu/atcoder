import io
import sys

# input here
_INPUT = """\
abracadabra

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

l = []
for i in range(len(S)):
    l.append(S[i:] + S[:i])

l = sorted(l)

print(l[0])
print(l[-1])
