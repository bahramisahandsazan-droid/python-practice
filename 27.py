class Student :
    count = 0
    def __init__ (self,name,grade):
        self.name = name
        self.grade = grade
        Student.count +=1
    def display (self):
        print(f'name :{self.name} , grade : {self.grade}')
    def is_pass(self) :
        if self.grade >= 10 :
            return True
        else :
            return False
class GraduateStudent(Student) :
    def __init__(self,name,grade,thesis_topic) :
        super().__init__(name,grade)
        self.thesis_topic = thesis_topic
    def display(self) :
        print(f'name :{self.name} , grade : {self.grade} , thesis_topic : {self.thesis_topic}')
student1 = Student('ramin' , 18)
student2 = Student('mahta',20)
gs1 = GraduateStudent('amirreza' , 12 , 'drug')
student1.display()
student2.display()
gs1.display()
print(student1.is_pass())
print(student2.is_pass())
print(gs1.is_pass())
a = (Student.count)
print('number of stunent : ' , a)



