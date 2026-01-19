from models.SqlDB import db
import bcrypt

# db = SQLAlchemy()  # inicjalizacja bez powiązania z app (zrobimy to w app.py)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(60), nullable=False)
    startWorkHour = db.Column(db.String(50))

    salt = b'$2b$12$KIX0QkZ0cZ5Z9v8fZxZ5uO'
    
    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), self.salt).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}