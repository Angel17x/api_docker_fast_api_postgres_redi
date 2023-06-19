from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.models.login_model import UserLoginModel;
from app.querys.querys import Querys as querys;

class Controller:
    def root(self):
        return {"message": "welcome to my api rest with fastapi"};

    def login(self, user: UserLoginModel):
        if not user:
            raise HTTPException(status_code=422, detail="Error al iniciar sesión")
        return jsonable_encoder(user).dict();



controller = Controller();