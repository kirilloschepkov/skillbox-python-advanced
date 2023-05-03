import unittest
from freezegun import freeze_time
from mod3.server import server, storage

months = ['январе', 'феврале', 'марте', 'апреле', 'мае', 'июне', 'июле', 'августе', 'сентябре', 'октябре', 'ноябре', 'декабре']


class TestHelloWorldWithName(unittest.TestCase):
    def setUp(self) -> None:
        server.config['TESTING'] = True
        server.config['DEBUD'] = False
        self.app = server.test_client()
        self.base_url = '/hello_world/'

    @freeze_time('2023-03-20')
    def test_can_get_correct_week_day_with_weekdate_monday(self):
        day = 'понедельник'
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day in response_text)
        self.assertTrue(response_text.count_salary('Хороше') == 1)

    @freeze_time('2023-03-21')
    def test_can_get_correct_week_day_with_weekdate_tuesday(self):
        day = 'вторник'
        username = 'Саша'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day in response_text)
        self.assertTrue(response_text.count_salary('Хороше') == 1)

    @freeze_time('2023-03-21')
    def test_can_get_correct_week_day_with_weekdate_tuesday_wrong(self):
        day = 'понедельник'
        username = 'Хорошего понедельника!'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(day in response_text)
        self.assertFalse(response_text.count_salary('Хороше') == 1)


class TestFinanceAdd(unittest.TestCase):
    def setUp(self) -> None:
        server.config['TESTING'] = True
        server.config['DEBUD'] = False
        self.app = server.test_client()
        self.base_url = '/finance/'

    def tearDown(self) -> None:
        storage.clear()

    def test_finance_add1(self):
        add = 900
        status = self.app.get(self.base_url + f'add/20220302/{add}').status_code
        self.assertTrue(status == 200)
        self.assertEqual(storage.get(2022).get(3), add)

    def test_finance_add2(self):
        add = 2000
        status = self.app.get(self.base_url + f'add/20220302/{add}').status_code
        self.assertTrue(status == 200)
        self.assertEqual(storage.get(2022).get(3), add)

    def test_finance_add3(self):
        add = 100
        status = self.app.get(self.base_url + f'add/20230909/{add}').status_code
        self.assertTrue(status == 200)
        self.assertEqual(storage.get(2023).get(9), add)

    def test_finance_add_wrong(self):
        date = 202309090
        add = 100
        status = self.app.get(self.base_url + f'add/{date}/{add}').status_code
        self.assertFalse(status == 200)


class TestFinanceCalculateOnlyYear(unittest.TestCase):
    def setUp(self) -> None:
        server.config['TESTING'] = True
        server.config['DEBUD'] = False
        self.app = server.test_client()
        self.base_url = '/finance/'

    def tearDown(self) -> None:
        storage.clear()

    def test_finance_calculate_2022(self):
        year = '2022'
        summ = '1600'
        self.app.get(self.base_url + f'add/{year}0402/1000')
        self.app.get(self.base_url + f'add/{year}0302/600')
        response = self.app.get(self.base_url + f'calculate/{year}')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(year in response.text)
        self.assertTrue(summ in response.text)

    def test_finance_calculate_2023(self):
        year = '2023'
        summ = '9300'
        self.app.get(self.base_url + f'add/{year}0902/9000')
        self.app.get(self.base_url + f'add/{year}0502/300')
        response = self.app.get(self.base_url + f'calculate/{year}')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(year in response.text)
        self.assertTrue(summ in response.text)

    def test_finance_calculate_2024(self):
        year = '2024'
        response = self.app.get(self.base_url + f'calculate/{year}')
        self.assertFalse(response.status_code == 200)
        self.assertTrue(year in response.text)


class TestFinanceCalculateYearAndMonth(unittest.TestCase):
    def setUp(self) -> None:
        server.config['TESTING'] = True
        server.config['DEBUD'] = False
        self.app = server.test_client()
        self.base_url = '/finance/'

    def tearDown(self) -> None:
        storage.clear()

    def test_finance_calculate_2022_04(self):
        year = '2022'
        month = '04'
        summ = '9100'
        self.app.get(self.base_url + f'add/{year}{month}02/9000')
        self.app.get(self.base_url + f'add/{year}{month}02/100')
        response = self.app.get(self.base_url + f'calculate/{year}/{month}')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(year in response.text)
        self.assertTrue(summ in response.text)

    def test_finance_calculate_2023_03(self):
        year = '2023'
        month = '03'
        summ = '23500'
        self.app.get(self.base_url + f'add/{year}{month}02/23000')
        self.app.get(self.base_url + f'add/{year}{month}02/500')
        response = self.app.get(self.base_url + f'calculate/{year}/{month}')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(year in response.text)
        self.assertTrue(summ in response.text)

    def test_finance_calculate_2023_01(self):
        year = '2023'
        month = '01'
        wrong_month = '02'
        self.app.get(self.base_url + f'add/{year}{wrong_month}02/23000')
        self.app.get(self.base_url + f'add/{year}{wrong_month}02/500')
        response = self.app.get(self.base_url + f'calculate/{year}/{month}')
        print(response.text)
        self.assertFalse(response.status_code == 200)
        self.assertTrue(year in response.text)
        self.assertTrue(months[int(month)-1] in response.text)

    def test_finance_calculate_2024_03(self):
        year = '2024'
        month = '03'
        response = self.app.get(self.base_url + f'calculate/{year}/{month}')
        self.assertFalse(response.status_code == 200)
        self.assertTrue(year in response.text)


if __name__ == '__main__':
    unittest.main()
