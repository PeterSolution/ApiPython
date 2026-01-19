from models.user import User
from models.SqlDB import db

def handle(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {"message": f"User {user_id} deleted"}