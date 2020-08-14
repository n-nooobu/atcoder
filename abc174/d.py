N = int(input())
c = str(input())

Rcount = 0
Wcount = 0
for i in range(len(c)):
    if c[i] == 'R':
        Rcount += 1
for i in range(Rcount):
    if c[i] == 'W':
        Wcount += 1

print(Wcount)
