import sys

x, y = map(int, input().split())

def is_palindrome(k):
    k = str(k)
    flag = True
    for i in range(len(k)):
        if k[i] != k[len(k) -i -1]:
            flag = False
            break
    return flag

ans = 0
for k in range(x, y+1):
    if is_palindrome(k):
        ans += 1

print(ans)
