from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.jwt_manager import create_token
from app.schemas.user import User
from app.services.user_service import UserService
from app.config.database import Session

user_router = APIRouter()
user_tag = "user"


def convert_str_to_dict(params: str) -> dict:
    """
    Convert a query string into a dictionary.
    """
    result = {}
    for param in params.split("&"):
        key, value = param.split("=")
        result[key] = value
    return result


# LOGIN
@user_router.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "correo@correo.com" and user.password == "1234":
        token = create_token(user.__dict__)
        return JSONResponse(content={"success": True, "token": token})
    return JSONResponse({"success": False})


@user_router.get("/users", tags=[user_tag])
async def get_all_users(params: str):
    db = Session()
    users = UserService(db).get_all_users(convert_str_to_dict(params))
    return JSONResponse(content={"success": True, "users": users})


@user_router.post("/users", tags=[user_tag])
async def create_user(user: User):
    db = Session()
    new_user = UserService(db).create_user(user)
    return {"success": True, "user": new_user}
