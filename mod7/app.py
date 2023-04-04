from utils import *
import logging.config
from dict_config import config_logging


AMOUNT, COMPOSITION, DEGREE = 1, 2, 3


# class FileHandlerByLevels(logging.Handler):
#     def __init__(self, mode='a'):
#         super().__init__()
#         self.mode = mode
#
#     def emit(self, record: logging.LogRecord) -> None:
#         message = self.format(record)
#         with open(f'calc_logs/calc_{record.levelname.lower()}.log', mode=self.mode) as f:
#             f.write(message + '\n')
#
#
# def config_logging():
#     formatter = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')
#
#     stream_handler = logging.StreamHandler(sys.stdout)
#     stream_handler.setFormatter(formatter)
#
#     file_handler = FileHandlerByLevels()
#     file_handler.setFormatter(formatter)
#
#     logging.basicConfig(level=logging.DEBUG, handlers=[stream_handler, file_handler])
#
# config_logging()
logging.config.dictConfig(config_logging)
logger = logging.getLogger('calculate_logger')


def calculate() -> None:
    logger.info('Start calculate')
    logger.debug('Data request')
    num1: int = get_number('Введите первое число: ')
    num2: int = get_number('Введите второе число: ')
    operation: int = get_operation('Выберете операцию:\n1. Сложение\n2. Произведение\n3. Возведение в степень\n')
    logger.debug('Data received')
    result: int = 0
    if operation == AMOUNT:
        result, operation = amount(num1, num2)
    elif operation == COMPOSITION:
        result, operation = composition(num1, num2)
    elif operation == DEGREE:
        result, operation = degree(num1, num2)
    logger.info(f'{num1} {operation} {num2} = {result}')
    logger.debug('Print result of operation')


if __name__ == '__main__':
    calculate()
