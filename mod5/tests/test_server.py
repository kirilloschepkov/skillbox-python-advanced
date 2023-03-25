import unittest
from mod5.server import server


class TestRegistrationForm(unittest.TestCase):
    def setUp(self) -> None:
        server.config['TESTING'] = True
        server.config['DEBUD'] = False
        server.config['WTF_CSRF_ENABLED'] = False
        self.app = server.test_client()
        self.base_url = '/code'

    def test_code(self):
        data = {
            'code': 'print(2**100)',
            'time': 0.1
        }
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.get_data().decode(), f'{2 ** 100}\n')

    def test_code_timeout_lower_than_work_time(self):
        data = {
            'code': 'print(2**100000)',
            'time': 0.01
        }
        responce = self.app.post(self.base_url, data=data)
        self.assertEqual(responce.get_data().decode(), 'Исполнение кода не уложилось в данное время')

    def test_code_invalid_data(self):
        data = {
            'code': 'print(2**100000)',
            'time': 'wrong'
        }
        response = self.app.post(self.base_url, data=data)
        print(response.get_data())
        self.assertEqual(response.status_code, 400)
