from abc import ABC, abstractmethod
from typing import List
import uuid
from rhh.domain.models import Animatronic

class AnimatronicCommandUseCase(ABC):
    
    @abstractmethod
    def create_animatronic(self) -> Animatronic:
        raise NotImplementedError


class AnimatronicCommandUseCaseImpl(AnimatronicCommandUseCase):
    
    def create_animatronic(self, item: Animatronic) -> Animatronic:
        animatronic = Animatronic(
            id = uuid.uuid4(),
            name = item.name,
            description = item.description
        )
        
        return animatronic