from .abc import * 
from typing import List

class Student(BaseUser):
    
    demerits : int
    timetable : List[List] # This will be a matrix containing classes in order, for each day of the week.