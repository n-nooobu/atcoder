import io
import sys

# input here
_INPUT = """\
6
1 1 1 2 2 3
1 1 1 2 2 3
"""
sys.stdin = io.StringIO(_INPUT)



import sys
from collections import Counter

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
AB = [A, B]

cab = Counter(AB)
cab_mc = cab.most_common()
count_list = [[0] for _ in range(N + 1)]
for i in range(len(cab_mc)):
    count_list[cab_mc[i][0]] = cab_mc[i][1]

"""if cab.most_common()[0][1] > N:
    print('No')
    sys.exit()

for
"""