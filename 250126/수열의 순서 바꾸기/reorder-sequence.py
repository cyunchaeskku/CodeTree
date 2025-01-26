import sys

n= int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def if_sorted(a):
    if sorted_a == a:
        return True
    else:
        return False

min_val = min(a)
max_val = max(a)
ans = 0

while if_sorted(a) == False:    
    target = a[0]
    a.remove(target)
    if target == min_val:
        a.insert(a.index(max(a)) + 1, target)
    elif target == max_val:
        a.insert(a.index(max(a)) + 1, target)
    else:
        for i in range(len(a)):
            if a[i] < target and a[(i+1)%3] > target:
                a.insert(i + 1, target)
                break
        

    ans += 1

print(ans)
    



