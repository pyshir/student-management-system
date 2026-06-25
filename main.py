from abc import ABC, abstractmethod
import sys

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show_details(self):
        pass

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.marks = []

    def add_marks(self, mark):
        self.marks.append(mark)

    def calculate_average(self): # Don't need to call from outside
        total = 0
        if not self.marks:
            return 0
        else:
            for i in self.marks:
                total += i
            avg = total / len(self.marks)
            return avg
    
    def show_details(self):
        print(f"""
Name: {self.name}
Age: {self.age}
Student ID: {self.student_id}
Marks: {self.marks}
Average: {self.calculate_average():.2f}
              """)
        

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_details(self):
        print(f"""
Name: {self.name}
Age: {self.age}
Subject: {self.subject}
              """)
        



if __name__ == '__main__':

    students = []
    teachers = []


    while True:
            print("""
        1. Add Student
        2. Add Teacher
        3. Show Everyone
        4. Exit
        """)
            
            choice = input('Enter choice')

            if choice == '1':
                name = input('Student name\n=')
                age = input('Student age\n=')
                st_id = input('Student Id\n=')

                student = Student(name, age, st_id)
                
                subjects = int(input('how many subjects\n='))
                for i in range(subjects):
                    mark = int(input(f'Enter mark {i+1}\n='))
                    student.add_marks(mark)
                students.append(student)

            elif choice == '2':
                name = input('Teacher name\n=')
                age = input('Teacher age\n=')
                subject = input('Subject\n=')
                teacher = Teacher(name, age, subject)
                teachers.append(teacher)

            elif choice == '3':

                if not students:
                    print('No student found')
                else:
                    print(f'*** Students ***\n')
                    for i in students:
                        i.show_details()
                    print('\n\n')
                if not teachers:
                    print('No teacher found')
                else:
                    print("*** Teachers ***\n")
                    for i in teachers:
                        i.show_details()
            
            elif choice == '4':
                sys.exit()
            
            



