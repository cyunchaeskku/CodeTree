_a = [
    list(map(int,list(input().rstrip())))
    for _ in range(3)
]

a= []

for i in range(3):
    for j in range(3):
        a.append(_a[i][j])

'''
0 1 2
3 4 5
6 7 8
------
0 1 2
3 4 5
6 7 8
0 3 6
1 4 7
2 5 8
0 4 8
2 4 6
'''

win_combination_list = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]


ans = 0

for i in range(1,10):
    for j in range(i+1, 10):
        for k in range(len(win_combination_list)):
            success = True
            v = win_combination_list[k]

            temp = []
            for l in range(3):
                temp.append(a[v[l]])
            
            for it in range(1,10):
                if it == i or it == j:
                    continue
                else:
                    if it in temp:
                        success = False
            
            if temp.count(i) == 3:
                success = False
            if temp.count(j) == 3:
                success = False

            if success:
                ans += 1

print(ans)