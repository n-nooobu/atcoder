N = str(input())

s = 0
for i in range(len(N)):
    s += int(N[i])

if s % 9 == 0:
    print('Yes')
else:
    print('No')