import unittest
from student_manager import Student, StudentManager

class Test(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager()
        self.manager.add_student(Student("Anna", 20))
        self.manager.add_student(Student("Tom", 22))

    def test_greet(self):
        student = self.manager.get_student("Anna")
        self.assertEqual(student.greet(), "Hallo, ich bin Anna!")

    def test_get_student(self):
        self.assertIsNotNone(self.manager.get_student("Anna"))
        self.assertIsNone(self.manager.get_student("Bob"))

    def test_remove_student(self):
        self.manager.remove_student("Tom")
        self.assertIsNone(self.manager.get_student("Tom"))
