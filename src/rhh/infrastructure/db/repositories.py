from typing import List

from fastapi import Depends
from sqlmodel import Session, select
from rhh.domain.models import Animatronic
from rhh.domain.repositories import AnimatronicRepository
from rhh.infrastructure.db.database import get_session
from rhh.shared.exceptions import RavenHillHouseError
from .models import AnimatronicDB

class AnimatronicSqlModelRepository(AnimatronicRepository):
    def __init__(self, session: Session = Depends(get_session)):
        super().__init__()
        self._session = session
        
    def insert_animatronic(self, animatronic: Animatronic):
        animatronic = AnimatronicDB(
            id = animatronic.id,
            name = animatronic.name,
            description = animatronic.description
        )
    
        try:
            self._session.add(animatronic)
        except Exception as e:
            raise RavenHillHouseError(f"Error inserting animatronic: {e}")

    def get_all_animatronics(self) -> List[Animatronic]:
        statement = select(AnimatronicDB)
        result = self._session.exec(statement)
        return [Animatronic(
            id = animatronic.id,
            name = animatronic.name,
            description = animatronic.description
        ) for animatronic in result]
