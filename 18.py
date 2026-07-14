
def sum_until_negative() :
    sum = 0
    while True :
        a = int(input('give me yor number : '))
        if a <0 : 
            break
        sum = sum + a
    return sum

result = sum_until_negative()
print(result)

