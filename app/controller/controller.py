from fastapi import FastAPI, Depends, HTTPException
from fastapi.param_functions import Query
from fastapi.encoders import jsonable_encoder
from app.models.user_model import UserModel
from app.models.login_model import UserLoginModel;
from uuid import uuid4 as uuid;

class Controller:
    def root(self):
        return {"message": "welcome to my api rest with fastapi"};

    def user(self, id:str):
        if not id or id == "unknown":
            raise HTTPException(status_code=422, detail="EL parametro id no puede estar vacio")
        response = ({"user": {"id": id,"name": "unknown"}});
        return jsonable_encoder(response);

    def create_user(self, user: UserModel):
        if not user:
            raise HTTPException(status_code=422, detail="Error al crear el usuario")
        user.id = uuid();
        return user.dict();

    def login(self, user: UserLoginModel):
        if not user:
            raise HTTPException(status_code=422, detail="Error al iniciar sesión")
        return jsonable_encoder(user);



controller = Controller();