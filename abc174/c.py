import sys

K = int(input())

seven = 7
mod = 7 % K
for i in range(10**6):
    seven = seven % K
    if seven == 0:
        print(i+1)
        sys.exit()
    else:
        seven = seven * (10 % K) + mod

print(-1)
