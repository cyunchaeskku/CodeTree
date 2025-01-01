import sys

'''
n개의 사람 m개의 치즈 먹음.
정확히 하나의 치즈만 상함...
'''

n, m, d, s = map(int, input().split())

eat_data = [
    tuple(map(int, input().split()))
    for _ in range(d)
]

cheese_list = [0 for _ in range(101)] # 1번부터 50번까지의 치즈. 값이 아픈 사람 수와 동일하면, 상한 치즈.
patients_list = [False for _ in range(101)] # 1번부터 50번 사람. True면 약 줘야 됨


sick_data = []
sick_people = []
sick_time = []
sick_dic = {}
for _ in range(s):
    sick_person, _sick_time = map(int, input().split())
    sick_people.append(sick_person)
    sick_time.append(_sick_time)
    sick_dic[sick_person] = _sick_time



for v in sick_data:
    sick_people.append(v[0])

for v in eat_data:
    person, cheese, time = v
    
    if person not in sick_people:
        continue
    else:
        if time < sick_dic[person]: # 치즈를 먹은 시각이, 아프게 된 시각보다 전이라면
            cheese_list[cheese] += 1
        if time >= sick_dic[person]:
            cheese_list[cheese] = -sys.maxsize
            
for v in eat_data:
    person, cheese, time = v

    if cheese_list[cheese] == s:
        patients_list[person] = True

ans =0
for i in range(len(patients_list)):
    if patients_list[i] == True:
        ans += 1
print(ans)
# print(cheese_list)
# print(patients_list)