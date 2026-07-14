
try :
    a = int(input('give mi your number :'))
    b = int(input('give mi your number :'))
    c = a/b
except ValueError :
    print(' not correct')
except ZeroDivisionError :
    print('no enetr 0')
else :
    print(c)