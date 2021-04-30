import io
import sys

# input here
_INPUT = """\
abcd
efgh
ijkl


"""
sys.stdin = io.StringIO(_INPUT)



import itertools

S1 = input()
S2 = input()
S3 = input()

alpha = {chr(ord('a')+i): i for i in range(26)}
exist = [False] * 26
alpha_list = []
for S in [S1, S2, S3]:
    for s in S:
        if not exist[alpha[s]]:
            alpha_list.append(s)
            exist[alpha[s]] = True
if len(alpha_list) > 10:
    print('UNSOLVABLE')
    exit()

for p in itertools.permutations([i for i in range(10)]):
    dic = {alpha_list[i]: p[i] for i in range(len(alpha_list))}
    n1 = 0
    n2 = 0
    n3 = 0
    if dic[S1[0]] == 0 or dic[S2[0]] == 0 or dic[S3[0]] == 0:
        continue
    for i in range(len(S1)):
        n1 *= 10
        n1 += dic[S1[i]]
    for i in range(len(S2)):
        n2 *= 10
        n2 += dic[S2[i]]
    for i in range(len(S3)):
        n3 *= 10
        n3 += dic[S3[i]]
    if n1 + n2 == n3:
        print(n1)
        print(n2)
        print(n3)
        exit()

print('UNSOLVABLE')
