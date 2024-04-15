from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(default='correo@correo.com')
    password: str
