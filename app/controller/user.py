from fastapi import HTTPException
from app.models.user_model import UserModel
from uuid import uuid4 as uuid;
from app.config.conn import conn, redis_client
from app.querys.querys import Querys as querys;
from app.models.user_model import UserModel
import json

class User:
    def get_user(id:str):
        if not id or id == "unknown":
            raise HTTPException(status_code=422, detail="EL parametro id no puede estar vacio")
        
        # Verificar si el resultado ya está en Redis
        redis_key = f"user:{id}"
        redis_data = redis_client.get(redis_key)
        if redis_data:
            return redis_data.decode('utf-8')
        
        # Consultar la base de datos
        cur = conn.cursor()
        cur.execute(querys.userID(id=id))
        rows = cur.fetchall()
        users:list[UserModel] = []
        for row in rows:
            data = {
                "user_id":row[0],
                "name":row[1],
                "lastname":row[2],
                "age":row[3],
                "email":row[4],
                "password":None,
                "user_type":row[5]
            }
            user:UserModel = UserModel(**data)
            user_dict:list = user.dict(exclude_unset=True)
            users.append(user_dict)
        count = len(users);
        result:dict = {
            "status": 200,
            "count": count,
            "data": users,
            
        }
        
        # Almacenar los resultados en Redis
        redis_client.set(redis_key, json.dumps(result))
        return result

    def create_user(user: UserModel):
        if not user:
            raise HTTPException(status_code=422, detail="Error al crear el usuario")
        user.user_id = str(uuid());
        cur = conn.cursor()
        try:
            cur.execute("insert into users (user_id, name, last_name, age, email, password, user_type) values (%s, %s, %s, %s, %s, %s, %s)",
                       (user.user_id, user.name, user.lastname, user.age, user.email, user.password, user.user_type))
            conn.commit()
            return 
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error al crear usuario: " + str(e))

    def get_users():
        users = redis_client.get('users')
        if users:
            # Imprime un mensaje si los usuarios están en caché
            print('Este es Redis *////////*')
            users = json.loads(users)
            result = {
                "status": 200,
                "count": len(users),
                "data": users
            }
        else:
            # Consulta los usuarios en la base de datos si no están en caché
            cur = conn.cursor()
            cur.execute(querys.users())
            rows = cur.fetchall()
            users = []
            for row in rows:
                data = {
                    "user_id":row[0],
                    "name":row[1],
                    "lastname":row[2],
                    "age":row[3],
                    "email":row[4],
                    "password":None,
                    "user_type":row[5]
                }
                user = UserModel(**data)
                user_dict = user.dict(exclude_unset=True)
                users.append(user_dict)
            count = len(users)
            result = {
                "status": 200,
                "count": count,
                "data": users
            }
            # Almacena los usuarios en caché en Redis
            redis_client.set('users', json.dumps(users))
        return result