from fastapi import Depends
from sqlmodel import Session

from rhh.infrastructure.db.database import get_session
from rhh.shared.exceptions import RavenHillHouseError

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Transaction:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # rollback and let the exception propagate
            self.session.rollback()
            return False

        try:
            self.session.commit()
        except Exception as e:
            # rollback and re-raise the exception
            self.session.rollback()
            raise RavenHillHouseError(f"Error committing transaction: {e}")
        return True

