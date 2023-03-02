import datetime
import os
import re
from random import choice

from flask import Flask

server = Flask(__name__)


@server.route('/')
def home_page():
    return '<h1>Home page</h1>' \
           '<ol>' \
           '<li><a href="/hello_world">/hello_world</a></li>' \
           '<li><a href="/cars">/cars</a></li>' \
           '<li><a href="/cats">/cats</a></li>' \
           '<li><a href="/get_time">/get_time</a></li>' \
           '<li><a href="/get_random_word">/get_random_word</a></li>' \
           '<li><a href="/counter">/counter</a></li>' \
           '</ol>'


@server.route('/hello_world')
def hello_world():
    return '<a href="/">back</a>' \
           '<h2>Привет, мир!</h2>'


CARS = ['Chevrolet', 'Renault', 'Ford', 'Lada']


@server.route('/cars')
def cars():
    return f'<a href="/">back</a><ul><li>{"</li><li>".join(CARS)}</li></ul>'


CATS = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']


@server.route('/cats')
def cats():
    return '<a href="/">back</a>' \
          f'<h2>{choice(CATS)}</h2>'


@server.route('/get_time')
def time():
    return '<a href="/">back</a>' \
           '<ul>' \
           '<li><a href="/get_time/now">/now</a></li>' \
           '<li><a href="/get_time/future">/future</a></li>' \
           '</ul>'


@server.route('/get_time/now')
def now():
    return '<a href="/get_time">back</a>' \
          f'<h2>Точное время: {datetime.datetime.now().strftime("%H:%M:%S")}</h2>'


@server.route('/get_time/future')
def future():
    now_time = datetime.datetime.now().time()
    return '<a href="/get_time">back</a>' \
           f'<h2>{datetime.timedelta(hours=now_time.hour+1, minutes=now_time.minute, seconds=now_time.second)}</h2>'


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
with open(BOOK_FILE, 'r') as book:
    text = book.read()
    words = re.findall(r'(\b\w+\b)', book.read())


@server.route('/get_random_word')
def random_word():
    return '<a href="/">back</a>' \
           f'<h2>Случайное слово: {choice(words)}</h2>'


@server.route('/counter')
def counter():
    if not hasattr(counter, 'visits'):
        counter.visits = 0
    counter.visits += 1
    return '<a href="/">back</a>' \
           f'<h2>Счётчик: {counter.visits}</h2>'


server.run()
