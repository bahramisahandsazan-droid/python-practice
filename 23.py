def sum_average() :
    numbers =[]
    while True :
        a = int(input('give me your number :'))
        if a < 0 :
            break
        numbers.append(a)
    total = sum(numbers)
    count = len(numbers)
    try :
        average = total / count
        return total , average
    except ZeroDivisionError:
        print('no enter number!')
        return total , None
result_total , result_average = sum_average()
print('result_total :' ,result_total , 'result_average : ' ,result_average)


