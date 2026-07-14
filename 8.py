a= []

def search_name(a , name) :
    
    for i in a :
        if i == name:
            return(True)
    return(False)
while True :
    i = input('enter name : ')
    if i == 'done' :
        break
    a.append(i)    
name = input('search for : ')
result = search_name(a , name)
if result == True :
    print(name , 'found')
else :
    print(name , 'not found')

