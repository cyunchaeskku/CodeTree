string = list(input())

n = len(string)
ans = 0
for i in range(n-3):
    for j in range(i+2, n-1):
        if string[i] == '(' and string[i+1] == '(' and string[j] == ')' and string[j+1] == ')':
            ans += 1

print(ans)
        