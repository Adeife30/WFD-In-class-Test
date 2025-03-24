

import unittest
from PartA import Staff, FullTimeStaff

class TestStaffClasses(unittest.TestCase):

    def setUp(self):
        self.staff = Staff("Adeife Thomas", "09-12-2003", "Male", 4702, "123 Blanchardstown")
        self.full_staff = FullTimeStaff("Chris Rock", "21-06-2003", "Male", 4703, "78 Castlecurragh Park, Blanchardstown", 55000.00, "IT")

    #To Test if object is instance of class
    def test_instance_of_staff(self):
        self.assertIsInstance(self.staff, Staff)
        self.assertIsInstance(self.full_staff, FullTimeStaff)

    #Test if object is NOT instance of a class
    def test_not_instance(self):
        self.assertNotIsInstance(self.staff, FullTimeStaff)
        self.assertNotIsInstance(self.full_staff, dict)

    #Test if 2 objects are identical
    def test_object_identity(self):
        another_staff = self.staff
        self.assertIs(self.staff, another_staff)
        self.assertIsNot(self.staff, self.full_staff)

    #Update methods for Staff class
    def test_update_name(self):
        self.staff.update_name("Adeife Thomas")  
        self.assertEqual(self.staff.name, "Adeife Thomas")

    def test_update_DoB(self):
        self.staff.update_DoB("09-12-2003")
        self.assertEqual(self.staff.DoB, "09-12-2003")

    def test_update_sex(self):
        self.staff.update_sex("Male")
        self.assertEqual(self.staff.sex, "Male")

    def test_update_staffID(self):
        self.staff.update_staffID(9999)
        self.assertEqual(self.staff.staffID, 9999)


    def test_update_address(self):
        self.staff.update_address("123 Blanchardstown") 
        self.assertEqual(self.staff.address, "123 Blanchardstown")

    # Update methods for FullTimeStaff class
    def test_update_salary(self):
        self.full_staff.update_salary(55000.00)  
        self.assertEqual(self.full_staff.salary, 55000.00)

    def test_update_department(self):
        self.full_staff.update_department("IT")  
        self.assertEqual(self.full_staff.department, "IT")


#Run tests
if __name__ == '__main__':
    unittest.main()

