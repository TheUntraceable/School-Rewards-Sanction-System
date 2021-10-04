from pydantic import BaseModel

class BaseUser(BaseModel):
    '''
    BaseModel that both Student and Teacher will inherit from.
    '''

    points : int
    id : int
    name : str
    password : str