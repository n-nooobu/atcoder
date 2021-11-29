import io
import sys

# input here
_INPUT = """\
...
200000
"""
sys.stdin = io.StringIO(_INPUT)



S = input()
K = int(input())

def is_ok(x):
    if x == 0:
        return True
    elif x > len(S):
        return False

    need = 0
    for i in range(x):
        if S[i] == '.':
            need += 1
    if need <= K:
        return True

    for j in range(x, len(S)):
        if S[j - x] == '.':
            need -= 1
        if S[j] == '.':
            need += 1
        if need <= K:
            return True

    return False

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(2 * 10 ** 5 + 1, 0))
