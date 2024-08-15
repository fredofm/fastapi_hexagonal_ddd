from pydantic import UUID4, BaseModel
from rhh.domain.models import Animatronic

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