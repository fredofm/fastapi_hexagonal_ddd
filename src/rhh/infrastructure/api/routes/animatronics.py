from typing import List

from fastapi import APIRouter
from pydantic import UUID4, BaseModel

from rhh.application.animatronic_use_cases import AnimatronicQueryUseCase, AnimatronicQueryUseCaseImpl
from rhh.domain.animatronic_model import Animatronic

router = APIRouter()
animatronic_query_use_case: AnimatronicQueryUseCase = AnimatronicQueryUseCaseImpl()

class AnimatronicDTO(BaseModel):
    id: UUID4
    name: str
    description: str
    
    @staticmethod
    def fromDomain(animatronic: Animatronic) -> "AnimatronicDTO":
        return AnimatronicDTO(
            id = animatronic.id,
            name = animatronic.name,
            description = animatronic.description
        )    

@router.get("/", response_model=List[AnimatronicDTO])
def read_items() -> List[AnimatronicDTO]:
    """
    Retrieve props.
    """
    
    animatronics = animatronic_query_use_case.get_all_animatronics()
    
    return map(AnimatronicDTO.fromDomain, animatronics)

    
