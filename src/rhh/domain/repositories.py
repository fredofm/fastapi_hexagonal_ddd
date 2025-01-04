from abc import ABC, abstractmethod
from typing import List

from rhh.domain.models import Animatronic

class AnimatronicRepository(ABC):
    
    @abstractmethod
    def insert_animatronic(animatronic: Animatronic):
        pass
    
    @abstractmethod
    def get_all_animatronics() -> List[Animatronic]:
        pass