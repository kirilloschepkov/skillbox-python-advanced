from datetime import datetime
from mod3.task4 import Person
import unittest


class TestPersonInit(unittest.TestCase):
    def test_person_init(self):
        name = 'Bob'
        yob = '2022/02/20'
        address = 'America'
        person = Person(name, yob, address)
        self.assertEqual(person.name, name)
        self.assertEqual(person.yob, yob)
        self.assertEqual(person.address, address)

    def test_person_init_without_address(self):
        name = 'Bob'
        yob = '2022/02/20'
        person = Person(name, yob)
        self.assertEqual(person.name, name)
        self.assertEqual(person.yob, yob)


class TestPersonAge(unittest.TestCase):
    def test_person_age(self):
        name = 'Bob'
        yob = '2002/02/20'
        person = Person(name, yob)
        now = datetime.now()
        self.assertEqual(person.age, now.year - int(yob[:4]))


class TestPersonName(unittest.TestCase):
    def setUp(self) -> None:
        self.name = 'Bob'
        self.person = Person(self.name, '2002/02/20')

    def test_person_get_name(self):
        self.assertEqual(self.person.get_name(), self.name)

    def test_person_set_name(self):
        self.name = 'Alex'
        self.person.set_name(self.name)
        self.assertEqual(self.person.get_name(), self.name)


class TestPersonAddress(unittest.TestCase):
    def setUp(self) -> None:
        self.address = 'England'
        self.person = Person('Bob', '2002/02/20', self.address)

    def test_person_get_address(self):
        self.assertEqual(self.person.get_address(), self.address)

    def test_person_set_address(self):
        self.address = 'China'
        self.person.set_address(self.address)
        self.assertEqual(self.person.get_address(), self.address)

    def test_person_is_homeless(self):
        self.assertFalse(self.person.is_homeless())


if __name__ == '__main__':
    unittest.main()
