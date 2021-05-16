import io
import sys

# input here
_INPUT = """\
xxxxx?xxxo


"""
sys.stdin = io.StringIO(_INPUT)



S = input()

ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                t = [False] * 10
                for i in range(10):
                    if S[i] == 'o':
                        t[i] = True
                if S[a] == 'x' or S[b] == 'x' or S[c] == 'x' or S[d] == 'x':
                    continue
                t[a] = False
                t[b] = False
                t[c] = False
                t[d] = False
                if sum(t) != 0:
                    continue
                ans += 1

print(ans)
