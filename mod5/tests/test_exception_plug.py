import unittest
from mod5.exception_plug import BlockErrors


class TestRegistrationForm(unittest.TestCase):
    def test_BlockError_ignore(self):
        def wrapper():
            err_types = {ZeroDivisionError, TypeError}
            with BlockErrors(err_types):
                a = 1 / 0
            return 'Выполнено без ошибок'
        self.assertEqual(wrapper(), 'Выполнено без ошибок')

    def test_BlockError_upper(self):
        def wrapper():
            err_types = {ZeroDivisionError}
            with BlockErrors(err_types):
                a = 1 / '0'
            print('Выполнено без ошибок')
        self.assertRaises(TypeError, wrapper)

    def test_BlockError_two_blocks(self):
        def wrapper():
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
                return 'Внутренний блок: выполнено без ошибок'
            return 'Внешний блок: выполнено без ошибок'
        self.assertEqual(wrapper(), 'Внешний блок: выполнено без ошибок')

    def test_BlockError_children_exceptions_ignore(self):
        def wrapper():
            err_types = {Exception}
            with BlockErrors(err_types):
                a = 1 / '0'
            return 'Выполнено без ошибок'
        self.assertEqual(wrapper(), 'Выполнено без ошибок')
