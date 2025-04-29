# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"The name of the student is {self.name}")
        print(f"The marks of the student is {self.marks}")

student = Student("Moiz",90)
student.display()