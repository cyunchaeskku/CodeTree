import sys

N, L = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True) # 내림차순

MAX_A = 100

def get_H_score(arr):
    ans = -sys.maxsize
    for v, idx in enumerate(arr):
        cnt = 0
        for j in range(len(arr)):
            if arr[j] >= v:
                cnt += 1
        if cnt >= v:
            ans = max(ans, v)
    return ans

ans = -sys.maxsize

for h in range(MAX_A + 1 + 1): # 최대 점수가 h일때
    possible = True
    ar = a.copy()

    '''
    가능하려면, ar를 순회했을때 h 이상인 원소 개수가 h 이상이어야 함
    1 100 2 3
    h가 4면, 이미 4 이상인 것을 제외 하고 제일 큰 순으로 1씩 더하면 될 듯. 이미 더한 건 idx 제외하고
    '''
    
    indicies = [False for _ in range(N)] # True면 더할 수 없다는 뜻.
    for i in range(N):
        if ar[i] >= h:
            indicies[i] = True
    
    L_count = 0
    for i in range(N):
        if ar[i] < h and indicies[i] == False:
            ar[i] += 1
            indicies[i] = True
            L_count += 1
        if L_count >= L:
            break
    
    ans = max(ans, get_H_score(ar))

print(ans)
