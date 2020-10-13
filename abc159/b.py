import io
import sys

# input here
_INPUT = """\
atcoder

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

def kaibun(S):
    S_reverse = S[::-1]
    if S[:len(S) // 2] == S_reverse[:len(S) // 2]:
        return True
    else:
        return False

k1 = kaibun(S)
k2 = kaibun(S[:len(S) // 2])
k3 = kaibun(S[-len(S) // 2 + 1:])
if k1 and k2 and k3:
    print('Yes')
else:
    print('No')
