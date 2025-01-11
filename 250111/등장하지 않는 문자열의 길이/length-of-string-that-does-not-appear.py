n = int(input())
# s = [list(input().rstrip())]
s = input().rstrip()

'''
i + j = len(s)
i = 6
j = 1
'''
ans = 0

for i in range(1, len(s)+1): # 길이가 i 일때
    dictionary = set() # type은 set
    success = True
    for j in range(0, len(s) - 1): # 시작점
        if s[j:j+i] in dictionary :
            success = False
            break
        dictionary.add(s[j:j+i])
    if success == True:
        ans = i
        break
        
print(ans)
