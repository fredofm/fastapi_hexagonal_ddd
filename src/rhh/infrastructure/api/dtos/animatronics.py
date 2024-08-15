from pydantic import UUID4, BaseModel
from rhh.domain.models import Animatronic

class AnimatronicIn(BaseModel):
    name: str
    description: str
class AnimatronicOut(BaseModel):
    id: UUID4
    name: str
    description: str
    

class AnimatronicMapper():
    @staticmethod
    def toDomain(self) -> Animatronic:
        return Animatronic(
            id = None,
            name = self.name,
            description = self.description
        )
    
    @staticmethod
    def fromDomain(animatronic: Animatronic) -> AnimatronicOut:
        return AnimatronicOut(
            id = animatronic.id,
            name = animatronic.name,
            description = animatronic.description
        )