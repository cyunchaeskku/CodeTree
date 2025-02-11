import sys 

N, K, P, T = map(int, input().split())

input_string = []
for i in range(T):
    input_string.append(tuple(map(int, input().split())))

input_string.sort()

K_list = [K for _ in range(N+1)]
K_list[0] = 0

programmers = [0 for _ in range(N+1)]
programmers[P] = 1


for i in range(T):
    flag= False
    t,x,y = input_string[i]
    if programmers[x] == 1 and K_list[x] > 0: # x가 감염자일때
        if programmers[y] == 0:
            flag = True
        programmers[y] = 1
        K_list[x] -= 1
    if flag == False and programmers[y] == 1 and K_list[y] > 0:
        programmers[x] = 1
        K_list[y] -= 1





# ----- print answer ---------#
for i,v in enumerate(programmers):
    if i == 0:
        continue
    else:
        print(v,end='')