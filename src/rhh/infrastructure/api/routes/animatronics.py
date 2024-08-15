from typing import List
from fastapi import APIRouter
from rhh.application.animatronic_use_cases import AnimatronicQueryUseCase, AnimatronicQueryUseCaseImpl
from rhh.infrastructure.api.dtos.animatronics import AnimatronicDTO
from rhh.shared.exceptions import RavenHillHouseError

router = APIRouter()
animatronic_query_use_case: AnimatronicQueryUseCase = AnimatronicQueryUseCaseImpl()

@router.get("/", response_model=List[AnimatronicDTO])
def read_items() -> List[AnimatronicDTO]:
    """
    Retrieve props.
    """
    
    animatronics = animatronic_query_use_case.get_all_animatronics()
    
    return map(AnimatronicDTO.fromDomain, animatronics)