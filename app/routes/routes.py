from fastapi import APIRouter, Depends
from app.controller.controller import controller
from app.controller.user import User as userController
from app.models.user_model import UserModel
from app.models.login_model import UserLoginModel

router = APIRouter()

@router.get('/')
def read_root():
    return controller.root();

@router.get('/user')
def read_user(id: str = "unknown"):
    return userController.get_user(id=id);

@router.get('/users')
def read_users():
    users = userController.get_users();
    return users;
    

@router.post('/create-user')
def create_user(user: UserModel):
    return userController.create_user(user=user);

@router.post('/login')
def login(user: UserLoginModel):
    return controller.login(user=user);
