
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.


class Person:
    def __init__(self, name):
        self.name = name
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  
        self.subject = subject

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")
t1 = Teacher("Mr. Hassan", "Mathematics")
t1.show_details()
