from abc import ABC, abstractmethod
import datetime
from typing import List
from uuid import UUID

class Entity(ABC):
    @abstractmethod
    def same_identify_as(self, other_entity: "Entity") -> bool:
        pass
    
class DomainEvent(ABC):
    __event_id: UUID
    __occured_on: datetime
    
    def __init__(self, event_id: UUID, occured_on: datetime):
        self.__event_id = event_id
        self.__occured_on = occured_on
    
    @property
    def event_id(self):
        return self.__event_id
    
    @property
    def occured_on(self):
        return self.__occured_on
    
class RootAggregate(ABC):
    __domain_events: List[DomainEvent]
    
    def __init__(self):
        self.__domain_events = {}
        
    def register_event(self, event: DomainEvent):
        self.__domain_events.append(event)
        
    def clear_domain_events(self):
        self.__domain_events.clear
    
    @property
    def domain_events(self) -> List[DomainEvent]:
        return self.__domain_events
    
class ValueObject(ABC):    
    @abstractmethod
    def same_value_as(self, other_value_object: "ValueObject") -> bool:
        pass