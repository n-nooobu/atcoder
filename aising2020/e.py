T = int(input())
N = []
case = []
for i in range(T):
    N.append(int(input()))
    case.append([list(map(int, input().split())) for j in range(N[i])])

print(case)
print(case[0])
print(case[0][0])