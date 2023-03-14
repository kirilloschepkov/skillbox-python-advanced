import unittest
from mod3.decrypt import decrypt


class TestDecryptWithOnePoint(unittest.TestCase):
    def test_decrypt_with_one_point_in_end(self):
        input = 'абра-кадабра.'
        output = 'абра-кадабра'
        self.assertTrue(decrypt(input) == output)

    def test_decrypt_with_only_one_point(self):
        input = '.'
        output = ''
        self.assertTrue(decrypt(input) == output)


class TestDecryptWithTwoPoint(unittest.TestCase):
    def test_decrypt_with_two_point_in_middle_before_dash(self):
        input = 'абраа..-кадабра'
        output = 'абра-кадабра'
        self.assertTrue(decrypt(input) == output)

    def test_decrypt_with_two_point_in_middle_after_double_dash(self):
        input = 'абра--..кадабра'
        output = 'абра-кадабра'
        self.assertTrue(decrypt(input) == output)

    def test_decrypt_with_two_point_in_begin(self):
        input = '1..2.3'
        output = '23'
        self.assertTrue(decrypt(input) == output)


class TestDecryptWithThreePoint(unittest.TestCase):
    def test_decrypt_with_three_point_in_middle_before_and_after_dash(self):
        input = 'абраа..-.кадабра'
        output = 'абра-кадабра'
        self.assertTrue(decrypt(input) == output)

    def test_decrypt_with_three_point_in_middle_before_dash(self):
        input = 'абрау...-кадабра'
        output = 'абра-кадабра'
        self.assertTrue(decrypt(input) == output)


class TestDecryptWithManyPoint(unittest.TestCase):
    def test_decrypt_with_many_point_in_end1(self):
        input = 'абра........'
        output = ''
        self.assertTrue(decrypt(input) == output)

    def test_decrypt_with_many_point_in_end2(self):
        input = '1.......................'
        output = ''
        self.assertTrue(decrypt(input) == output)

    def test_decrypt_with_many_point_in_middle(self):
        input = 'абр......a.'
        output = 'a'
        self.assertTrue(decrypt(input) == output)

