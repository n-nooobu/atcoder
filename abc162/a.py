import io
import sys

# input here
_INPUT = """\
123
"""
sys.stdin = io.StringIO(_INPUT)



import sys

N = input()

for i in range(len(N)):
    if N[i] == '7':
        print('Yes')
        sys.exit()

print('No')
