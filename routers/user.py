from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from jwt_manager import create_token
from schemas.user import User
user_router = APIRouter()

# LOGIN
@user_router.post('/login', tags=['auth'])
def login(user: User):    
    if user.email == "correo@correo.com" and user.password == "1234":
        token = create_token(user.__dict__)
        return JSONResponse(
            content={'success':True, 'token': token}
        )
    return JSONResponse({'success':False})