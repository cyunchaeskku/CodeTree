a, o, c = input().split()
a, c = int(a), int(c)

def f(a, o, c):
    if o == '+':
        return a + c
    elif o == '-':
        return a - c
    elif o == '*':
        return a * c
    elif o == '/':
        return a // c
    else:
        return False

if f(a, o, c) != False:
    print(a,o,c,'=',f(a,o,c))
else:
    print(f(a,o,c))

