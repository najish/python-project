class Demo:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


    def __iter__(self):
        return iter(self.students)


    def __next__(self):
        return self.students



class Student:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __repr__(self):
        return f"Name : {self.name}, Age: {self.age}"
    


# a = Student("Hasnain", 28)
# b = Student("Zafer",27)
# c = Student("Afshan", 24)
# d = Student("Shifa",21)




# demo = Demo()

# demo.add_student(a)
# demo.add_student(b)
# demo.add_student(c)
# demo.add_student(d)


# for student in demo:
#     print(student)



class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    
    def __iter__(self):
        return self
    

    def __next__(self):

        if self.current > self.end:
            raise StopIteration
        
        current = self.current
        self.current += 1
        return current
    

counter = Counter(1,3)

for item in iter(counter):
    print(f"item : {item}")


