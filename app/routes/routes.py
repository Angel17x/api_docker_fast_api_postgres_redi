from fastapi import APIRouter;
from app.controller.controller import controller;
from app.models.user_model import UserModel;
from app.models.login_model import UserLoginModel;
from app.schemes.schemes import database;
router = APIRouter()

@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@router.get('/')
def read_root():
    return controller.root();

@router.get('/user')
def read_user(id: str = "unknown"):
    return controller.user(id=id);
    
@router.post('/create-user')
def create_user(user: UserModel):
    return controller.create_user(user=user);

@router.post('/login')
def login(user: UserLoginModel):
    return controller.login(user=user);

@router.post('/users')
async def users():
    query = database.select()
    return await database.fetch_all(query)