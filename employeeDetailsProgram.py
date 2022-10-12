#to print employee details using class

class Employee:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def display(self):
        print("Employee Id: ",self.id)
        print("Employee Name: ",self.name)

student1=Employee(4, "Kamaal")
student2=Employee(5, "Muzammil")
student1.display()
student2.display()
