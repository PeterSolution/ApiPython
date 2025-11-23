from models.user import  User
from models.SqlDB import db

def handle(data):
    user = User(name=data['name'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return user.to_dict()