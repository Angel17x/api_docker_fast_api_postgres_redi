from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi_jwt_auth.exceptions import JWTDecodeError, InvalidHeaderError
from fastapi_jwt_auth import AuthJWT
from datetime import datetime, timedelta
from app.config.config import SECRET_KEY, JWT_ALGORITHM, JWT_EXP_DELTA_SECONDS
from app.models.login_model import UserLoginModel
import jwt

security = HTTPBearer()


def generate_token(user: UserLoginModel) -> UserLoginModel:
    payload = {
        "sub": user,
        "exp": datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    }
    token = jwt.encode(payload, SECRET_KEY, JWT_ALGORITHM)
    return token
        

async def jwt_middleware(request: Request, call_next):
    auth = AuthJWT(secret_key=SECRET_KEY, algorithm='HS256')
    credentials: HTTPAuthorizationCredentials = await security.__call__(request)
    if not credentials:
        raise HTTPException(status_code=401, detail="Credenciales no presentes")
    try:
        auth.jwt_decode_token(credentials.credentials)
        response = await call_next(request)
        return response
    except (JWTDecodeError, InvalidHeaderError, TypeError):
        raise HTTPException(status_code=401, detail="Token inválido")
    