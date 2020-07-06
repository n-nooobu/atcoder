N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 0 and temp != 1:
        arr.append([temp, 1])

    if not arr and n != 0 and n != 1:
        arr.append([n, 1])

    return arr

arr = factorization(N)
ans = 0
for i in range(len(arr)):
    for j in range(arr[i][1]):
        if j / 2 * (j + 3) + 1 <= arr[i][1] < (j + 1) / 2 * (j + 4) + 1:
            ans += j + 1
            break

print(ans)
