N = int(input())
S = [list(str(input())) for i in range(N)]

AC = 0
WA = 0
TLE = 0
RE = 0
for i in range(N):
    if S[i][0] == 'A':
        AC += 1
    elif S[i][0] == 'W':
        WA += 1
    elif S[i][0] == 'T':
        TLE += 1
    else:
        RE += 1

print('AC x ' + str(AC))
print('WA x ' + str(WA))
print('TLE x ' + str(TLE))
print('RE x ' + str(RE))