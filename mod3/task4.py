from datetime import datetime


class Person:
    def __init__(self, name, year_of_birth, address=''):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    @property
    def age(self):
        now = datetime.now()
        return now.year - datetime(*map(int, [self.yob[0:4], self.yob[5:7], self.yob[8:10]])).year

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def is_homeless(self):
        return self.address is None
