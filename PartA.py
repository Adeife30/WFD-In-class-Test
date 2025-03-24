

from datetime import date

class Staff:
    def __init__(self, name: str, DoB: str, sex: str, staffID: int, address: str):
        self.name = name
        self.DoB = DoB
        self.sex = sex
        self.staffID = staffID
        self.address = address

    def print_attributes(self):
        print(f"Name: {self.name}, DoB: {self.DoB}, Sex: {self.sex}, Staff ID: {self.staffID}, Address: {self.address}")

    def update_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            print("Invalid type for name")

    def update_DoB(self, DoB):
        if isinstance(DoB, str):
            self.DoB = DoB
        else:
            print("Invalid type for DoB")

    def update_sex(self, sex):
        if isinstance(sex, str):
            self.sex = sex
        else:
            print("Invalid type for sex")

    def update_staffID(self, staffID):
        if isinstance(staffID, int):
            self.staffID = staffID
        else:
            print("Invalid type for staffID")

    def update_address(self, address):
        if isinstance(address, str):
            self.address = address
        else:
            print("Invalid type for address")


# Child class: FullTimeStaff
class FullTimeStaff(Staff):
    def __init__(self, name, DoB, sex, staffID, address, salary: float, department: str):
        super().__init__(name, DoB, sex, staffID, address)
        self.salary = salary
        self.department = department

    def print_all_attributes(self):
        self.print_attributes()
        print(f"Salary: {self.salary}, Department: {self.department}")

    def update_salary(self, salary):
        if isinstance(salary, (int, float)):
            self.salary = salary
        else:
            print("Invalid type for salary")

    def update_department(self, department):
        if isinstance(department, str):
            self.department = department
        else:
            print("Invalid type for department")


#Instances
staff1 = Staff("Adeife Thomas", "09-12-2003", "Male", 4702, "123 Blanchardstown")
full_staff1 = FullTimeStaff("Chris Rock", "21-06-2003", "Male", 4703, "78 Castlecurragh Park, Blanchardstown", 55000.00, "IT")

#Print attributes
print("Staff1 attributes:")
staff1.print_attributes()
print("\nFullTimeStaff attributes:")
full_staff1.print_all_attributes()

# Update examples
print("\nUpdating Staff1's name and address...")
staff1.update_name("Adeife Thomas")
staff1.update_address( "123 Blanchardstown")
staff1.print_attributes()

print("\nUpdating FullTimeStaff's salary and department...")
full_staff1.update_salary(55000.00)
full_staff1.update_department("IT")
full_staff1.print_all_attributes()
