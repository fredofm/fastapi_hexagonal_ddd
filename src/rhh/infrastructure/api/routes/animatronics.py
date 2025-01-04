from typing import List
from fastapi import APIRouter, Depends
from rhh.application.animatronic_command_use_cases import (
    AnimatronicCommandUseCase,
    AnimatronicCommandUseCaseImpl,
)
from rhh.application.animatronic_query_use_cases import (
    AnimatronicQueryUseCase,
    AnimatronicQueryUseCaseImpl,
)
from rhh.infrastructure.api.dtos.animatronics import (
    AnimatronicMapper,
    AnimatronicOut,
    AnimatronicIn,
)
from rhh.shared.common import Transaction

router = APIRouter()

@router.get("/", response_model=List[AnimatronicOut])
async def read_items(
    use_case: AnimatronicQueryUseCase = Depends(AnimatronicQueryUseCaseImpl),
) -> List[AnimatronicOut]:
    """
    Retrieve props.
    """
    animatronics = use_case.get_all_animatronics()
    return list(map(AnimatronicMapper.fromDomain, animatronics))

@router.post("/", response_model=AnimatronicOut)
async def create_item(
    item: AnimatronicIn,
    use_case: AnimatronicCommandUseCase = Depends(AnimatronicCommandUseCaseImpl),
    tx: Transaction = Depends(Transaction),
) -> List[AnimatronicOut]:
    """
    Create props.
    """

    with tx:
        animatronic = use_case.create_animatronic(AnimatronicMapper.toDomain(item))

    return AnimatronicMapper.fromDomain(animatronic)