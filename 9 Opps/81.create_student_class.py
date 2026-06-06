class Student:
    def __init__(self,name,roll_no,subject,marks):
        self.name = name
        self.roll_no = roll_no
        self.subject = subject
        self.marks = int(marks)
    
    def introduce(self):
        return f"Name of student: {self.name}\nRoll No:- {self.roll_no}\nSubject : {self.subject}\nMarks : {self.marks}"
    

student1 = Student("Ankit",2304327,'NN',76)
student2 = Student("Akash",2304324,'ML',56)

print(student1.introduce())