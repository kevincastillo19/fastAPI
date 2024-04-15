from jwt import encode, decode

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"

def create_token(payload: dict) -> str:
    token: str = encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)
    return token

def validate_token(token: str) -> dict:
    token_data = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return token_data 