import unittest
from unittest.mock import Mock
from hogwarts_magic import Wizard, Student, Professor, House, Wand, Spell, Hogwarts

class TestWizard(unittest.TestCase):
    def setUp(self):
        self.wizard = Wizard("Albus Dumbledore", "Phoenix", 1881)

    def test_init_wizard(self):
        self.assertEqual(self.wizard.name, "Albus Dumbledore")
        self.assertEqual(self.wizard.patronus, "Phoenix")
        self.assertEqual(self.wizard.birth_year, 1881)
        self.assertIsNone(self.wizard.wand)
        self.assertEqual(self.wizard.skill, 0.2)

    def test_change_skill(self):
        self.wizard.change_skill(0.5)
        self.assertEqual(self.wizard.skill, 0.7)
        self.wizard.change_skill(0.4)  # This should cap the skill at 1.0
        self.assertEqual(self.wizard.skill, 1.0)



class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Harry Potter", "Stag", 1980)

    def test_student_assign_house(self):
        hogwarts = Hogwarts()
        self.student.assign_house_using_sorting_hat(hogwarts)
        self.assertIsNotNone(self.student.house)

    def test_take_exam(self):
        self.student.assign_subjects(["Defense Against the Dark Arts"])
        self.student.take_exam("Defense Against the Dark Arts", 85)
        self.assertEqual(self.student.subject_grades["Defense Against the Dark Arts"], 85)


class TestProfessor(unittest.TestCase):
    def setUp(self):
        self.professor = Professor("Minerva McGonagall", "Cat", 1935, "Transfiguration")
        self.student = Student("Hermione Granger", "Otter", 1979)
        self.student.assign_subjects(["Transfiguration"])

    def test_professor_assign_and_assess(self):
        self.professor.assign_wand(Wand("Birch", "Dragon heartstring", 9))
        self.professor.assess_student(self.student, 95)
        self.assertEqual(self.student.subject_grades["Transfiguration"], 95)


class TestHouse(unittest.TestCase):
    def setUp(self):
        self.house = House("Gryffindor", "Godric Gryffindor", ["red", "gold"], "lion")
        self.student = Student("Ron Weasley", "Dog", 1980)

    def test_add_member(self):
        self.house.add_member(self.student)
        self.assertIn(self.student, self.house.members)

    def test_remove_member(self):
        self.house.add_member(self.student)
        self.house.remove_member(self.student)
        self.assertNotIn(self.student, self.house.members)

    def test_add_member_twice(self):
        self.house.add_member(self.student)
        self.house.add_member(self.student)
        self.assertEqual(len(self.house.members), 1)  # Member should only be added once

class TestWand(unittest.TestCase):
    def setUp(self):
        self.wand = Wand("Holly", "Phoenix feather", 11, 0.9)

    def test_cast_spell(self):
        spell = Spell("Expelliarmus", "Disarming", 0.3)
        wizard = Wizard("Test Wizard", "None", 0.8)
        wizard.wand = self.wand
        result = spell.is_successful(self.wand, wizard)
        self.assertIsInstance(result, bool)  # Result should be a boolean

# Run the tests
if __name__ == '__main__':
    unittest.main()
