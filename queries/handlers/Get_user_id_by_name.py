from models.user import User

def handle(user_name: str):
    u = User.query.filter_by(name=user_name).first()
    return u.id if u else None