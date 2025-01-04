from abc import ABC, abstractmethod
import uuid

from fastapi import Depends
from rhh.domain.models import Animatronic
from rhh.domain.repositories import AnimatronicRepository
from rhh.infrastructure.db.repositories import AnimatronicSqlModelRepository  
from rhh.shared.logger import RHHLogger

logger = RHHLogger().get_logger(__name__)

class AnimatronicCommandUseCase(ABC):
    @abstractmethod
    def create_animatronic(self) -> Animatronic:
        raise NotImplementedError

class AnimatronicCommandUseCaseImpl(AnimatronicCommandUseCase):
    def __init__(self, repository: AnimatronicRepository = Depends(AnimatronicSqlModelRepository)):
        self._repository = repository
        super().__init__()

    def create_animatronic(self, item: Animatronic) -> Animatronic:
        logger.info(f"Creating animatronic {item.name}")
        animatronic = Animatronic(
            id=uuid.uuid4(), name=item.name, description=item.description
        )

        self._repository.insert_animatronic(animatronic)

        return animatronic
