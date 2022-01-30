from pydantic import BaseModel
from defaults import STUDENT_ID


class StudentSerializer(BaseModel):
    student_id: str = STUDENT_ID
