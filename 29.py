class Student :
    count = 0
    def __init__ (self,name,grade):
        self.name = name
        self.grade = grade
        Student.count +=1
    def __str__ (self) :
        return f'Student (name :{self.name}, grade : {self.grade})'    
    @property
    def grade (self) :
        return self.__grade
    @grade.setter
    def grade (self,value) :
        if value <0 or value > 20 :
            print('نمره باید بین 0 و 20 باشه!')
        else :
            self.__grade = value
student2 = Student('mahta',20)
s1 = Student('ramin' , 14)
s1.grade = 18
print(s1)
print (student2)
