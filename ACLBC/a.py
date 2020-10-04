import io
import sys

# input here
_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)



K = int(input())

ans = ''
for i in range(K):
    ans += 'ACL'

print(ans)
