from models.user import  User
from models.SqlDB import db

def handle(data):
    IsUserNameExist = User.query.filter_by(name=data['name']).first()
    if IsUserNameExist:
        return Exception("User name already exists")
    user = User(name=data['name'], email=data['email'], startWorkHour=data['startWorkHour'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return user.to_dict()