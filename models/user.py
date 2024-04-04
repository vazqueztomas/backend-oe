from pydantic import BaseModel

class User(BaseModel):
    name: str
    lastname: str
    city:str
    gender:str
    age: int