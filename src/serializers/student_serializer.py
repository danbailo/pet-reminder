from pydantic import BaseModel


class StudentSerializer(BaseModel):
    id: str
