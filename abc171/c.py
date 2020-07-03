N = int(input())

for i in range(11):
    if N <= 26 ** (i + 1):
        size = i + 1
        break
    N -= 26 ** (i + 1)

ans = [0] * size
N -= 1
for i in range(size):
    q = N // 26
    r = N % 26
    N = q
    ans[size - 1 - i] = r

ans_chr = ''
for i in range(size):
    ans_chr += chr(ans[i] + 97)

print(ans_chr)
