from uuid import uuid4

from rhh.domain.shared import Entity

class Animatronic(Entity):
    def __init__(self, id: uuid4, name: str, description: str):
        self.__id = id
        self.__name = name
        self.__description = "No description added"
        
        super().__init__()

    def same_identify_as(self, other_entity: Entity) -> bool:
        raise NotImplementedError
    
    @property
    def id(self) -> uuid4:
        return self.__id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def description(self) -> str:
        return self.__description

