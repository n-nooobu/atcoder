import io
import sys

# input here
_INPUT = """\
ABA

"""
sys.stdin = io.StringIO(_INPUT)



import sys

S = input()

kaisya = S[0]
for i in range(1, 3):
    if S[i] != kaisya:
        print('Yes')
        sys.exit()

print('No')
