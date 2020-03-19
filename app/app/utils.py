from contextlib import ContextDecorator
from time import time


class timer(ContextDecorator):
    """Timer class to measure execution time in seconds."""

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time()
        self.elapsed = self.stop - self.start
        return False
