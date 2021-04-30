import io
import sys

# input here
_INPUT = """\
4 4
"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())

if H % 3 == 0 or W % 3 == 0:
    print(0)
    exit()

ans = 10 ** 5
for i in range(1, W):
    t = [i*H]
    if H % 2:
        t.append((W-i)*(H//2))
        t.append((W-i)*(H//2+1))
    else:
        t.append((W-i)*(H//2))
    ans = min(ans, max(t) - min(t))

    t = [i*H]
    if (W - i) % 2:
        t.append((W-i)//2 * H)
        t.append(((W-i)//2+1) * H)
    else:
        t.append((W-i)//2 * H)
    ans = min(ans, max(t) - min(t))

for i in range(1, H):
    t = [i*W]
    if W % 2:
        t.append((H-i)*(W//2))
        t.append((H-i)*(W//2+1))
    else:
        t.append((H-i)*(W//2))
    ans = min(ans, max(t) - min(t))

    t = [i*W]
    if (H - i) % 2:
        t.append((H-i)//2 * W)
        t.append(((H-i)//2+1) * W)
    else:
        t.append((H-i)//2 * W)
    ans = min(ans, max(t) - min(t))

print(ans)
