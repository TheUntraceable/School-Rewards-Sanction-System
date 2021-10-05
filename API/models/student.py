from .abc import BaseUserPayload, BaseUserUpdatePayload
from typing import (
    List
)

class Student(BaseUserPayload):
    """
    Student object.
    """

    demerits : int

class StudentUploadPayload(BaseUserUpdatePayload):
    """
    Update payload that will be used when updating a Student.
    """
    
    points : int
    demerits : int
    timetable : List[List]