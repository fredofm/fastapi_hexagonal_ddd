import logging

from rhh.shared.common import SingletonMeta

class RHHLogger(metaclass=SingletonMeta):

    def get_logger(self, name: str) -> logging.Logger:
        return logging.getLogger(name)