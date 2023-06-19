from app.models.user_model import UserModel

class Querys:
    def users(): 
        return "select user_id, name, last_name, age, email, user_type from users"
    
    def userID(id:int):
        return f"select user_id, name, last_name, age, email, user_type from users where user_id = '{id}'"
    def create_user(user:UserModel):
        return "insert into users (user_id, name, last_name, age, email, password, user_type) values (%s, %s, %s, %s, %s, %s, %s)"