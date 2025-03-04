from pydantic import BaseModel

class Signin(BaseModel):
    username:str
    password:str 