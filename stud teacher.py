class student:
    def __init__(self):
        self.studentname=""
        self.studentid=""
        self.studentdepid=""
        self.studentsem=0
    def getvalue(self):
        self.name=input("enter the student name:")
        self.id=input("enter the student id:")
        self.depid=input("enter the student depid:")
        self.salary=input("enter the student salary:")
    def showvalue(self): 
        print("student name",self.name)
        print("student id",self.id)
        print("student depid",self.depid)
        print("student salary",self.salary)
class teacher:
    def __init__(self):
        self.teachername=""
        self.teacherid=""
        self.teacherdepid=""
        self.teachersalary=0
    def getvalue(self):
        self.name=input("enter the teacher name:")
        self.id=input("enter the teacher id:")
        self.depid=input("enter the teacher depid:")
        self.salary=input("enter the teacher salary:")
    def showvalue(self):
        print("teacher name",self.name)
        print("teacher id",self.id)
        print("teacher depid",self.depid)
        print("teacher salary",self.salary)
class subject:
    def __init__(self):
        self.subname=""
        self.subid=""
        
    def getvalue(self):
        self.name=input("enter the subject name:")
        self.code=input("enter the subject code:")
    def showvalue(self):
        print("subject name",self.name)
        print("subject code",self.code)
s1=student()
s1.getvalue()
s1.showvalue()
t1=teacher()
t1.getvalue()
t1.showvalue()
s2=subject()
s2.getvalue()
s2.showvalue()


        

        
