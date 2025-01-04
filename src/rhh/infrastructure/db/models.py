from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel
    
class AnimatronicDB(SQLModel, table=True):
    __tablename__ = "animatronics"
    id: UUID = Field(default=uuid4, primary_key=True)
    name: str
    description: str