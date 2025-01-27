def is_3_basu(n):
    if n % 3 == 0:
        return True
    else:
        return False

def is_answer_number(n):
    if '3' in list(str(n)) or '6' in list(str(n)) or '9' in list(str(n)) or is_3_basu(n):
        return True
    else:
        return False

a, b = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    if is_answer_number(i):
        cnt += 1

print(cnt)