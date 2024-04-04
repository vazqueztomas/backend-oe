from pydantic import BaseModel
import uuid

class User(BaseModel):
    name: str
    lastname: str
    city:str
    gender:str
    age: int