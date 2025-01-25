import sys

n = int(input())

hall_of_fame = ('A','B','C')
score = dict()
score['A'] = 0
score['B'] = 0
score['C'] = 0

cnt = 0

for _ in range(n):
    c, s = input().split()
    s = int(s)
    score[c] += s

    _hall_of_fame = tuple()

    if score['A'] == score['B'] and score['B'] == score['C']:
        _hall_of_fame = ('A','B','C')
    elif score['A'] == score['B'] and score['A'] > score['C']:
        _hall_of_fame = ('A','B')
    elif score['C'] == score['B'] and score['C'] > score['A']:
        _hall_of_fame = ('B','C')
    elif score['A'] == score['C'] and score['A'] > score['B']:
        _hall_of_fame = ('A','C')
    elif score['A'] > score['B'] and score['A'] > score['C']:
        _hall_of_fame = ('A')
    elif score['B'] > score['A'] and score['B'] > score['C']:
        _hall_of_fame = ('B')
    elif score['C'] > score['B'] and score['C'] > score['A']:
        _hall_of_fame = ('C')

    if hall_of_fame != _hall_of_fame:
        cnt += 1
    hall_of_fame = _hall_of_fame
print(cnt)