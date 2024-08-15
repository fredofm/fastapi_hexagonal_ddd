from abc import ABC, abstractmethod
from typing import List
import uuid
from rhh.domain.animatronic_model import Animatronic

class AnimatronicQueryUseCase(ABC):
    
    @abstractmethod
    def get_all_animatronics(self) -> List[Animatronic]:
        raise NotImplementedError


class AnimatronicQueryUseCaseImpl(AnimatronicQueryUseCase):
    
    def get_all_animatronics(self) -> List[Animatronic]:
        animatronic_list = [
            Animatronic(uuid.uuid4(), "Animatronic 1"),
            Animatronic(uuid.uuid4(), "Animatronic 2")
        ]
        
        return animatronic_list