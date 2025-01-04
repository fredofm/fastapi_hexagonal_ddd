from abc import ABC, abstractmethod
from typing import List
from fastapi import Depends
from rhh.domain.models import Animatronic
from rhh.domain.repositories import AnimatronicRepository
from rhh.infrastructure.db.repositories import AnimatronicSqlModelRepository
from rhh.shared.logger import RHHLogger

logger = RHHLogger().get_logger(__name__)


class AnimatronicQueryUseCase(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_all_animatronics(self) -> List[Animatronic]:
        raise NotImplementedError


class AnimatronicQueryUseCaseImpl(AnimatronicQueryUseCase):
    def __init__(
        self, repository: AnimatronicRepository = Depends(AnimatronicSqlModelRepository)
    ):
        self._repository = repository
        super().__init__()

    def get_all_animatronics(self) -> Animatronic:
        logger.info("Getting all animatronics")
        return self._repository.get_all_animatronics()
