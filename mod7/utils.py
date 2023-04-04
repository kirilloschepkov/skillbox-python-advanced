import logging.config
from dict_config import config_logging
# import logging_tree

# with open('logging_tree.txt', 'w') as file:
#     file.write(logging_tree.format.build_description())

# handler = logging.FileHandler('utils_logs.log')
# formatter = logging.Formatter(fmt='%(asctime)s, %(levelname)s, %(message)s', datefmt='%H:%M:%S')
# handler.setFormatter(formatter)
logging.config.dictConfig(config_logging)
logger = logging.getLogger('utils_logger')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(handler)


class InvalidIndexOperation(Exception):
    def __init__(self):
        self.message: str = 'Invalid operation index entered'

    def __str__(self) -> str:
        return self.message


def get_number(mes: str = '') -> int:
    logger.debug('Start function "get_number"')
    while True:
        try:
            logger.info(mes)
            number = int(input())
            logger.debug('Return result from a function "get_number"')
            return number
        except ValueError:
            logger.error('Invalid number')


def get_operation(mes: str = '') -> int:
    logger.debug('Start function "get_operation"')
    while True:
        try:
            logger.info(mes)
            index_operation = int(input())
            if 1 <= index_operation <= 3:
                logger.debug('Return result from a function "get_operation"')
                return index_operation
            raise InvalidIndexOperation()
        except ValueError:
            logger.error('Invalid number')
        except InvalidIndexOperation:
            logger.error('Invalid index operation')


def amount(n1: int, n2: int) -> (int, str):
    logger.debug('Start function "amount"')
    return n1 + n2, '+'


def composition(n1: int, n2: int) -> (int, str):
    logger.debug('Start function "composition"')
    return n1 * n2, '*'


def degree(n1: int, n2: int) -> (int, str):
    logger.debug('Start function "degree"')
    return n1 ** n2, '^'
