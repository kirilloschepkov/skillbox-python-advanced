import sys
import traceback


class Redirect:
    def __init__(self, stdout=sys.stdout, stderr=sys.stderr):
        self.prev_stdout = sys.stdout
        self.prev_stderr = sys.stderr
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        traceback.print_exc()
        sys.stdout = self.prev_stdout
        sys.stderr = self.prev_stderr
        return exc_type is Exception
