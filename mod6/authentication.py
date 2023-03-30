import getpass
import hashlib
import logging
import os
from typing import Dict, List
import re
import json


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        msg = json.dumps(msg, ensure_ascii=False)
        return msg, kwargs


logging.basicConfig(
    level=logging.INFO,
    filename='skillbox_json_messages.log',
    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
    datefmt='%H:%M:%S'
)
logger = JsonAdapter(logging.getLogger('password_checker'))
words: Dict[str, List[str]] = dict()
with open(os.path.join(os.sep, *'usr share dict words'.split())) as data:
    for word in data.read().split():
        if len(word) > 3:
            word = word.lower()
            first_letter: str = word[0]
            if first_letter not in words:
                words[first_letter]: List[str] = [word]
            else:
                words[first_letter].append(word)


def is_strong_password(pswd: str) -> bool:
    words_from_pswd = re.findall('[a-z]+', pswd)
    for word in words_from_pswd:
        first_letter = word[0]
        if word in words[first_letter]:
            return False
    return True


def input_and_check_password() -> bool:
    logger.debug('Начало input_and_check_password'.lower())
    password: str = getpass.getpass()
    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("latin-1"))
        if not is_strong_password(password.lower()):
            logger.warning('Содержит слово')
            return False
        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Некорректный символ", exc_info=ex)
    return False


if __name__ == "__main__":
    logger.info('Попытка войти')
    count_number: int = 3
    logger.info(f'У Вас есть {count_number} попытки.')
    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
    logger.error('Войти не удалось, пароль неверный')
    exit(1)
