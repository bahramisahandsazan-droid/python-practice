with open ('C:/Users/Dear User/Desktop/python/notes.txt' , 'w') as file :
    file.write('ramin\n')
    file.write('mahta\n')
    file.write('amirreza\n')
with open( 'C:/Users/Dear User/Desktop/python/notes.txt','r') as file:
    content = file.read()
    print(content)


