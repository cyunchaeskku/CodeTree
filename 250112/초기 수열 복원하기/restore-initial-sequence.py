n = int(input())
arr = list(map(int, input().split()))

for i in range(1, max(arr)+1):
    possible_arr = []
    success = True
    possible_arr.append(i)
    for j in range(len(arr)):
        v = arr[j] - possible_arr[-1]
        if v in possible_arr:
            success = False
        elif v <= 0:
            success = False
        else:
            possible_arr.append(v)
    if success:        
        for v in possible_arr:
            print(v, end=' ')
        exit(0)