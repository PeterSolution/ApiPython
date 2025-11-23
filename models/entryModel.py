from models.SqlDB import db
import bcrypt

# db = SQLAlchemy()  # inicjalizacja bez powiązania z app (zrobimy to w app.py)

class EntryModel(db.Model):
    __tablename__ = 'Entries'
    id = db.Column(db.Integer, primary_key=True)
    person = db.Column(db.String(150))
    data = db.Column(db.String(50), unique=True)
    place = db.Column(db.String(150), nullable=False)

    def set_Entry(self, person,data,place):
        self.person = person
        self.data = data
        self.place = place

    def to_dict(self):
        return {
            "id": self.id,
            "person": self.person,
            "data": self.data,
            "place": self.place
        }