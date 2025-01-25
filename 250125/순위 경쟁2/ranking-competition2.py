import sys

n = int(input())
hall_of_fame = set()
hall_of_fame.add('A')
hall_of_fame.add('B')
score = dict()
score['A'] = 0
score['B'] = 0

cnt = 0

for _ in range(n):
    c, s = input().split()
    s = int(s)
    score[c] += s

    if score['A'] > score['B']:
        _hall_of_fame = ('A')
        if hall_of_fame != _hall_of_fame:
            cnt += 1
        hall_of_fame = _hall_of_fame
    elif score['A'] < score['B']:
        _hall_of_fame = ('B')
        if hall_of_fame != _hall_of_fame:
            cnt += 1
        hall_of_fame = _hall_of_fame
    elif score['A'] == score['B']:
        _hall_of_fame = ('A', 'B')
        if hall_of_fame != _hall_of_fame:
            cnt += 1
        hall_of_fame = _hall_of_fame
        
print(cnt)

