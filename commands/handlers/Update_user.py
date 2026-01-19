from models.user import User
from models.SqlDB import db

def handle(user_id, data):
    user = User.query.get_or_404(user_id)
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    if 'password' in data and data['password']:
        user.set_password(data['password'])
    if 'startWorkHour' in data:
        user.startWorkHour = data['startWorkHour']
    db.session.commit()
    return user.to_dict()