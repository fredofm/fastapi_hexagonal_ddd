from abc import ABC, abstractmethod
from typing import List
import uuid
from rhh.domain.models import Animatronic

class AnimatronicQueryUseCase(ABC):
    
    @abstractmethod
    def get_all_animatronics(self) -> List[Animatronic]:
        raise NotImplementedError


class AnimatronicQueryUseCaseImpl(AnimatronicQueryUseCase):
    
    def get_all_animatronics(self) -> Animatronic:
        animatronic_list = [
            Animatronic(uuid.uuid4(), "Animatronic 1", "Description"),
            Animatronic(uuid.uuid4(), "Animatronic 2", "Description")
        ]
        
        return animatronic_list