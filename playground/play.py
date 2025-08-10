from datetime import datetime
class student:
    def __init__(self,id, name, dob, grade, sex  ):
        self.id = id
        self.name = name
        self.dob = dob
        self.grade = grade
        self.sex = sex
    
    def age(self):
        year = datetime.now().year
        return year - self.dob
    
    def details(self):
        print(f"name : {self.name} , born : {self.dob}, grade : {self.grade} ")

student1 = student(2, "oyekan abdul-wahab", 19/1/1996, "year 1", "male" )

student1.details()