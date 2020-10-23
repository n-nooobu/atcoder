import io
import sys

# input here
_INPUT = """\
6 0

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
pS = [input().split() for _ in range(M)]

problem = [0] * (N + 1)
correct = 0
penalty = 0
for i in range(M):
    if problem[int(pS[i][0])] == -1:
        continue
    if pS[i][1] == 'WA':
        problem[int(pS[i][0])] += 1
    else:
        correct += 1
        penalty += problem[int(pS[i][0])]
        problem[int(pS[i][0])] = -1

print(correct, penalty)
