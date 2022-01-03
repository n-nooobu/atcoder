import io
import sys

# input here
_INPUT = """\
5 6
1 2
1 3
1 4
3 4
3 5
4 5
1 2
1 3
1 4
1 5
3 5
4 5

"""
sys.stdin = io.StringIO(_INPUT)



import sys
import copy
import itertools

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(M)]

matrix = [[0] * N for _ in range(N)]
for i in range(M):
    matrix[min(AB[i]) - 1][max(AB[i]) - 1] = 1

for i in itertools.permutations(range(N)):
    matrix2 = copy.deepcopy(matrix)
    for j in range(M):
        matrix2[min(i[CD[j][0] - 1], i[CD[j][1] - 1])][max(i[CD[j][0] - 1], i[CD[j][1] - 1])] -= 1
    flag = True
    for j in range(N):
        for k in range(N):
            if matrix2[j][k] != 0:
                flag = False
    if flag:
        print('Yes')
        sys.exit()

print('No')
