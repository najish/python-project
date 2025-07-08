class Student: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Demo:

    def __init__(self):
        self.students = []
        self.index = 0

    def addStudent(self, student):
        self.students.append(student)

    def __iter__(self):
          # Reset index for new iteration
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration

demo = Demo()

student1 = Student("Hasnain", 28)
student2 = Student("Zafer", 29)
student3 = Student("Shifa", 30)

demo.addStudent(student1)
demo.addStudent(student2)
demo.addStudent(student3)

for student in demo:
    print(student)

for student in demo:
    print(student)