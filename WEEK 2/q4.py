class Employee:
    total_employees=0
    def __init__(self,name):
        self.name=name
        Employee.total_employees+=1
E1=Employee("asad")
E2=Employee("husain")
E3=Employee("faridi")
print(Employee.total_employees)