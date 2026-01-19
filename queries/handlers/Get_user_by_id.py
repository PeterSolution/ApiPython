from models.user import User

def handle(user_id: int):
    u = User.query.get(user_id)
    # return u.to_dict() if u else None
    return u.to_dict() if u else None