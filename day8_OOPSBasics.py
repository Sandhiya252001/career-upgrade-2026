class Student:
    School="Global"
    def __init__(self,firstname,lastname,marks):
        self.firstname=firstname
        self.lastname=lastname
        self.marks=marks
    def info(self):
        print(self.firstname, self.lastname, self.marks)
    @classmethod
    def details(cls):
        print(cls.School)
    @staticmethod
    def randomInfo():
        print("This is a Student class")
s1=Student("Sandhiya","Subramani",98)
s2=Student("Nandhini","Sivakumar",100)
s1.info()
s2.info()
Student.details()
Student.randomInfo()
    

