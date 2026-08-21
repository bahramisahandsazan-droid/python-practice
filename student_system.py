class Student () :
    count = 0
    def __init__(self,name,grade) :
        self.name = name
        self.grade = grade
        Student.count +=1
    def __str__ (self) :
        return f'Student (name : {self.name} , grade : {self .grade})'
    @property 
    def grade (self) :
        return self.__grade
    @grade.setter
    def grade(self,value) :
        if value <0 or value >20 :
            print('not corect number !')
        else :
            self.__grade = value
students = []
def add_student () :
    name = input ('give me student name : ')
    grade = int(input ('give me student grade : '))
    new_student = Student (name,grade)
    students.append(new_student)
    print('new student inserted')
def show_student() :
    for student in students :
        print(student)
def average_grade() :
    if len(students )== 0 :
        print ('are not students !')
        return
    total = sum (student.grade for student in students)
    avrg = total / len(students)
    print(f'number average : {avrg}')
def failed_student() :
    failed = [student for student in students if student.grade < 10]
    if len(failed) == 0 :
        print ('no failed student')
    else :
        print ('failed students : ')
        for student in failed :
            print(student)
import json
def save_student() :
    data = [{'name' : student.name ,'grade' : student.grade} for student in students]
    with open ('student.json','w') as file :
        json.dump(data,file)
        print('saved') 
add_student()
add_student()
show_student()
average_grade()
failed_student()
save_student()





       



