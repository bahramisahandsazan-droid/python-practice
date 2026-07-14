a = []

while True :
    i = input('enter number : ')
    if i == 'done' :
        break
    a.append(int(i))
def find_max(a) :
    bigest = a[0]
    for num in a:
        if num > bigest :
            bigest = num
    return bigest
m = find_max(a)
print(a)
print('big number is : ',m)





