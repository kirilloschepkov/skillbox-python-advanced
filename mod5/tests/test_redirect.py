import sys
import unittest
from mod5.redirect import Redirect


class TestRedirect(unittest.TestCase):
    def test_redirect_stdout(self):
        name_file = 'stdout.txt'
        text = f'Hello {name_file}'
        with open(name_file, 'w') as file:
            with Redirect(file):
                print(text)
        with open(name_file, 'r') as file:
            self.assertTrue(text in file.read())

    def test_redirect_stderr(self):
        name_file = 'stderr.txt'
        text = f'Hello {name_file}'
        with open(name_file, 'w') as file:
            with Redirect(stderr=file):
                raise Exception(text)
        with open(name_file, 'r') as file:
            self.assertTrue(text in file.read())
