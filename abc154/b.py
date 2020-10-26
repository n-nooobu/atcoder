import io
import sys

# input here
_INPUT = """\
sardine

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

ans = ''
for i in range(len(S)):
    ans = ans + 'x'

print(ans)
