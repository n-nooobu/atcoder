XY = list(map(int, input().split(' ')))

leg = XY[0] * 2
ans = 'No'
if leg == XY[1]:
    ans = 'Yes'
for i in range(XY[0]):
    leg += 2
    if leg == XY[1]:
        ans = 'Yes'

print(ans)