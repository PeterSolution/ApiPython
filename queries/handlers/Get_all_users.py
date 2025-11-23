# from flask import jsonify
# from models.user import User
from models.user import User

def handle():
    users = User.query.all()
#     return jsonify([u.to_dict() for u in users])
    return [u.to_dict() for u in users]

