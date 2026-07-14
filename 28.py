class Student :
    count = 0
    def __init__ (self,name,grade):
        self.name = name
        self.grade = grade
        Student.count +=1
    def __str__ (self) :
        return f'Student (name :{self.name}, grade : {self.grade})'
student2 = Student('mahta',20)
print (student2)
