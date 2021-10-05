from pydantic import BaseModel
from typing import (
    List,
    Optional
)
class BaseUserPayload(BaseModel):
    """
    Model which all User objects will inherit from.
    """
    
    points : int
    id : int
    name : str
    username : str
    password : str
    timetable : List[List] # This will be a matrix containing classes in order, for each day of the week.

class BaseUserUpdatePayload(BaseModel):
    """
    Model which all Update payloads will inherit from.
    """
    id : int
    name : Optional[str]
    password : Optional[str]
    username : Optional[str]
    timetable : Optional[List[List]]

class UserDeletePayload(BaseModel):
    id : int