secret = 7
count = 0
while True :
    n = int(input('give me your guess :'))
    count +=1
    if n > secret :
        print('too high')
    elif n < secret :
        print('too low')
    else :
        print('correct! you did it in ' , count , 'tries')
        break

 

