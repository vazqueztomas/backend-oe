from fastapi import FastAPI
from models.user import User

app = FastAPI()

fake_users = [
    User(name='Tomas', lastname="Vazquez", city="mercedes", gender="male", age=23),
    User(name='delfina', lastname="ensenat", city="mercedes", gender="female", age=26),
    User(name='juan', lastname="perez", city="lujan", gender="male", age=28),
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def get_users():
    return fake_users