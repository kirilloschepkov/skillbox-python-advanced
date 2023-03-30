import json
import operator
import os
import re
from collections import Counter
from typing import List, Dict
from itertools import groupby

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skillbox_json_messages.log')) as data:
    logs: List[Dict[str, str]] = list(map(lambda log: json.loads(log), data.readlines()))


def count_levels():
    """1. Сколько было сообщений каждого уровня за сутки."""
    count_level_dict = dict()
    for level, logs_list in groupby(logs, key=lambda log: log['level']):
        count_level_dict[level] = count_level_dict.get(level, 0) + len(list(logs_list))
    for level, count in count_level_dict.items():
        print(f'{level} - {count}')


def max_count_logs_by_hour():
    """2. В какой час было больше всего логов."""
    count_logs_by_hours = dict()
    for hour, logs_list in groupby(logs, key=lambda log: log['time'][:2]):
        count_logs_by_hours[hour] = len(list(logs_list))
    print(f'Наибольшее количество логов было в {max(count_logs_by_hours.items(), key=operator.itemgetter(1))[0]} часа')


def count_critical_by_period():
    """3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00."""
    print(f'Логов уровня CRITICAL в период с 05:00:00 по 05:20:00 было: {len(list(filter(lambda log: log["level"] == "CRITICAL" and bool(re.search(r"05:[0-1]", log["time"])), logs)))}')


def count_logs_have_dogs():
    """4. Сколько сообщений содержат слово dog."""
    print(f'{len(list(filter(lambda log: "dog" in log["message"], logs)))} содержат слово "dog"')


def frequent_word_in_warning():
    """5. Какое слово чаще всего встречалось в сообщениях уровня WARNING."""
    words_list_from_warning = list()
    for log in filter(lambda log: log['level'] == 'WARNING', logs):
        words_list_from_warning += log['message'].split()
    print(f'Слово "{Counter(words_list_from_warning).most_common()[0][0]}" встречается чаще всего в WARNING')


count_levels()
max_count_logs_by_hour()
count_critical_by_period()
count_logs_have_dogs()
frequent_word_in_warning()
