import unittest
from mod4.server import server


class TestRegistrationForm(unittest.TestCase):
    def setUp(self) -> None:
        server.config['TESTING'] = True
        server.config['DEBUD'] = False
        server.config['WTF_CSRF_ENABLED'] = False
        self.app = server.test_client()
        self.base_url = '/registration'
        self.correct_data = {
            'email': 'test@example.com',
            'phone': 9922160000,
            'name': 'Kirill',
            'address': 'Perm',
            'index': 617000,
            'comment': 'empty'
        }

    def test_email(self):
        data = self.correct_data.copy()
        data['email'] = 'test@test.ru'
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_email_wrong(self):
        data = self.correct_data.copy()
        data['email'] = 'test'
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('email' in response.text)

    def test_phone(self):
        data = self.correct_data.copy()
        data['phone'] = '9003553535'
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_phone_wrong(self):
        data = self.correct_data.copy()
        data['phone'] = '90035535353'
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('phone' in response.text)

    def test_name(self):
        data = self.correct_data.copy()
        data['name'] = 'Karina'
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_name_wrong1(self):
        data = self.correct_data.copy()
        data['name'] = 'K'
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('name' in response.text)

    def test_name_wrong2(self):
        data = self.correct_data.copy()
        data['name'] = ''
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('name' in response.text)

    def test_address(self):
        data = self.correct_data.copy()
        data['address'] = 'Moscow'
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_address_wrong(self):
        data = self.correct_data.copy()
        data['address'] = ''
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('address' in response.text)

    def test_index(self):
        data = self.correct_data.copy()
        data['index'] = '666000'
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_index_wrong(self):
        data = self.correct_data.copy()
        data['index'] = '66600'
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('index' in response.text)

    def test_comment1(self):
        data = self.correct_data.copy()
        data['comment'] = 'Example'
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_comment2(self):
        data = self.correct_data.copy()
        data['comment'] = ''
        response = self.app.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
