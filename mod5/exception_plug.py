class BlockErrors:
    def __init__(self, exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type in self.exceptions or Exception in self.exceptions

err_types = {ZeroDivisionError, TypeError}
with BlockErrors(err_types):
    a = 1 / 0
print('Выполнено без ошибок')