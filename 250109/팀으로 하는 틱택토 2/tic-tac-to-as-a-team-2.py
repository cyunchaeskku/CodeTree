import sys

a = []

for _ in range(3):
    temp = list(input().rstrip())
    for v in temp:
        a.append(int(v))

ans = 0


def judge_win (lis):
    win_combination = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    win = False
    for li in win_combination:
        if set(li).issubset(set(lis)):
            win = True

    return win


for i in range(1,10):
    for j in range(i+1,10):
        win = False
        a_copy = a.copy()
        for k in range(len(a_copy)):
            if a_copy[k] != i and a_copy[k] != j:
                a_copy[k] = 0
        
        left_list = []
        for k in range(len(a_copy)):
            if a_copy[k] > 0:
                left_list.append(k)

        if len(left_list) < 3:
            continue
            
        win = judge_win(left_list)

        if win:
            ans += 1
print(ans)

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