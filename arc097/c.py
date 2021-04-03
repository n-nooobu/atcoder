import io
import sys

# input here
_INPUT = """\
z
1

"""
sys.stdin = io.StringIO(_INPUT)



s = input()
K = int(input())

substring = set()
for i in range(len(s)):
    for j in range(1, 6):
        if i + j <= len(s):
            substring.add(s[i: i+j])

substring = sorted(substring)
print(substring[K - 1])
