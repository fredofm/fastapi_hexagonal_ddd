from typing import List
from fastapi import APIRouter
from rhh.application.animatronic_command_use_cases import AnimatronicCommandUseCase, AnimatronicCommandUseCaseImpl
from rhh.application.animatronic_query_use_cases import AnimatronicQueryUseCase, AnimatronicQueryUseCaseImpl
from rhh.infrastructure.api.dtos.animatronics import AnimatronicMapper, AnimatronicOut, AnimatronicIn

router = APIRouter()
animatronic_query_use_case: AnimatronicQueryUseCase = AnimatronicQueryUseCaseImpl()
animatronic_command_use_case: AnimatronicCommandUseCase = AnimatronicCommandUseCaseImpl()

@router.get("/", response_model=List[AnimatronicOut])
def read_items() -> List[AnimatronicOut]:
    """
    Retrieve props.
    """
    
    animatronics = animatronic_query_use_case.get_all_animatronics()
    
    return map(AnimatronicMapper.fromDomain, animatronics)

@router.post("/", response_model=AnimatronicOut)
def read_items(item: AnimatronicIn) -> List[AnimatronicOut]:
    """
    Retrieve props.
    """
    
    return AnimatronicMapper.fromDomain(
        animatronic_command_use_case.create_animatronic(
            AnimatronicMapper.toDomain(item)
        )
    )