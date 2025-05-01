# Access Modifiers: Public, Private, and Protected


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # This is Public
        self._salary = salary     # This is Protected
        self.__ssn = ssn          # This is Private

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")


emp = Employee("Ali", 50000, "123-45-6789")
print("Public:", emp.name)         
print("Protected:", emp._salary)   
print("Private (via name mangling):", emp._Employee__ssn)  
