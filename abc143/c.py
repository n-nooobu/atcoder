import io
import sys

# input here
_INPUT = """\
20
xxzaffeeeeddfkkkkllq


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = input()

now = S[0]
count = 1
for i in range(1, N):
    if S[i] != now:
        count += 1
        now = S[i]

print(count)
