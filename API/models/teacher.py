from .abc import (
    BaseUserPayload, 
    BaseUserUpdatePayload
)

class Teacher(BaseUserPayload):
    """
    Teacher object.
    """

    pass

class TeacherUploadPayload(BaseUserUpdatePayload):
    """
    Update payload that will be used when updating a Teacher.
    Nothing different from BaseUserUpdatePayload as there is nothing else that teachers have that can be updated that BaseUserUpdatePayload doesn't
    """

    pass