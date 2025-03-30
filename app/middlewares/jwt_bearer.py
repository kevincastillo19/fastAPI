from fastapi import Request, HTTPException
from app.jwt_manager import validate_token
from fastapi.security import HTTPBearer


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != "correo@correo.com":
            raise HTTPException(403, "Credenciales no válidas", data)
