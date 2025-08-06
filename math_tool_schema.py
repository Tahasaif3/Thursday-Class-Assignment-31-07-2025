from pydantic import BaseModel

class SubtractSchema(BaseModel):
    n1:int
    n2:int

class PlusSchema(BaseModel):
    n1:int
    n2:int

class MultilpicationSchema(BaseModel):
    n1:int
    n2:int

class DivisionSchema(BaseModel):
    n1:int
    n2:int


