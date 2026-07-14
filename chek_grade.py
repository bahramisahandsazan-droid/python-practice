
def chek_grade(grade) :
    if grade>=18:
       return('aali')   
    elif grade <18 and grade >=14 :
        return ('khob')
    elif grade <14 and grade >=10 :
        return ('ghabol')
    else :
        return ('mardod')
student = []
while True :

    name = input('give me your name : ')
    if name == 'done':
        break
    grade = int(input('give me your number : '))  
   
    student.append((name , grade))
for (name , grade) in student :
    vaziat = chek_grade(grade)
    print(name , '--' ,grade , '--' ,vaziat)
        




    