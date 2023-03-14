import os
from datetime import datetime
from flask import Flask

server = Flask(__name__)


@server.route('/')
def home_page():
    return '<h1>Home page</h1>' \
           '<ol>' \
           '<li><a href="/hello_world">/hello_world</a></li>' \
           '<li><a href="/max_number">/max_number</a></li>' \
           '<li><a href="/preview">/preview</a></li>' \
           '<li><a href="/finance">/finance</a></li>' \
           '</ol>'


@server.route('/hello_world')
def hello_world() -> str:
    return '<a href="/">back</a>' \
           '<h2>Задача 4. Хорошего дня!</h2>' \
           '<ul>' \
           '<li><a href="/hello_world/Саша">Саша</a></li>' \
           '<li><a href="/hello_world/Даша">Даша</a></li>' \
           '<li><a href="/hello_world/Паша">Паша</a></li>' \
           '</ul>'


@server.route('/hello_world/<string:name>')
def hello_world_with_name(name: str) -> str:
    days = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')
    number_day = datetime.today().weekday()
    return '<a href="/hello_world">back</a>' \
           f'<h2>Привет, {name}. {"Хорошей" if number_day == 2 or number_day == 4 or number_day == 5 else "Хорошего"} {days[number_day]}!</h2>'


@server.route('/max_number')
def max_number() -> str:
    return '<a href="/">back</a>' \
           '<h2>Задача 5. Максимальное число</h2>' \
           '<ul>' \
           '<li><a href="/max_number/10/2/9/1">/max_number/10/2/9/1</a></li>' \
           '<li><a href="/max_number/1/1/1/1/1/1/1/2/">/max_number/1/1/1/1/1/1/1/2</a></li>' \
           '</ul>'


@server.route('/max_number/<path:numbers>')
def max_number_(numbers: str) -> str:
    return '<a href="/max_number">back</a>' \
           f'<h2>Максимальное число: {max(map(int, filter(lambda x: x.isdigit(), numbers.split("/"))))}</h2>'


@server.route('/preview')
def preview() -> str:
    return '<a href="/">back</a>' \
           '<h2>Задача 6. Превью файла</h2>' \
           '<ul>' \
           '<li><a href="/preview/8/docs/simple.txt">/preview/8/docs/simple.txt</a></li>' \
           '<li><a href="/preview/100/docs/simple.txt">/preview/100/docs/simple.txt</a></li>' \
           '</ul>'


@server.route('/preview/<int:length>/<path:path>')
def preview_file(length: int, path: str) -> str:
    abs_path = os.path.abspath(path)
    return '<a href="/preview">back</a>' \
           f'<p>{abs_path} {length}</p>' \
           f'<p>{open(abs_path, "r").read(length)}</p>'


@server.route('/finance')
def finance() -> str:
    return '<a href="/">back</a>' \
           '<h2>Задача 7. Учёт финансов</h2>' \
           '<ul>' \
           '<li><a href="/finance/add/20220424/1000">/add/20220424/1000</a></li>' \
           '<li><a href="/finance/add/20230101/800">/add/20230101/800</a></li>' \
           '<li><a href="/finance/add/20220430/5">/add/20220430/5</a></li>' \
           '<li><a href="/finance/calculate/2022/4">/calculate/2022/4</a></li>' \
           '<li><a href="/finance/calculate/2023/1">/calculate/2023/1</a></li>' \
           '<li><a href="/finance/calculate/2023/5">/calculate/2023/5</a></li>' \
           '<li><a href="/finance/calculate/2022/6">/calculate/2022/6</a></li>' \
           '<li><a href="/finance/calculate/2022">/calculate/2022</a></li>' \
           '<li><a href="/finance/calculate/2024">/calculate/2024</a></li>' \
           '</ul>'


storage = dict()


@server.route('/finance/add/<string:date>/<int:expense>')
def finance_add(date: str, expense: int) -> str:
    if len(date) != 8:
        return '<a href="/finance">back</a>'\
               '<h2>Неправильная дата</h2>', 400
    year, month, day = map(int, (date[0:4], date[4:6], date[6:8]))
    storage.setdefault(year, {}).setdefault(month, 0)
    storage[year][month] += expense
    return '<a href="/finance">back</a>' \
           '<h2>Добавление прошло успешно! Можно проверять дальше)</h2>', 200


@server.route('/finance/calculate/<int:year>')
def finance_year(year: int) -> str:
    if year in storage.keys():
        res = sum(storage.get(year).values())
        return f'Расход в {year} составил {res}', 200
    return f'В {year} расходов не было', 400


months = ['январе', 'феврале', 'марте', 'апреле', 'мае', 'июне', 'июле', 'августе', 'сентябре', 'октябре', 'ноябре', 'декабре']


@server.route('/finance/calculate/<path:date>')
def finance_year_and_month(date: str) -> str:
    year, month = map(int, date.split('/'))
    if year not in storage.keys():
        return finance_year(year)
    if month not in storage.get(year).keys():
        return f'В {months[month-1]} {year} расходов не было', 400
    return f'Расход в {months[month-1]} {year} составил {storage.get(year).get(month)}', 200


if __name__ == '__main__':
    server.run(debug=True)
