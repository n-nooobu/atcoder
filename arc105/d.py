import io
import sys

# input here
_INPUT = """\
3
1
10
2
1 2
21
476523737 103976339 266993 706803678 802362985 892644371 953855359 196462821 817301757 409460796 773943961 488763959 405483423 616934516 710762957 239829390 55474813 818352359 312280585 185800870 255245162

"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter

T = int(input())
N = []
case = []
for _ in range(T):
    N.append(int(input()))
    case.append(list(map(int, input().split())))

for t in range(T):
    if N[t] % 2 == 1:
        print('Second')
    else:
        count = Counter(case[t])
        if all([i % 2 == 0 for i in count.values()]):
            print('Second')
        else:
            print('First')
