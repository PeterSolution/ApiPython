from models.SqlDB import db
import bcrypt

# db = SQLAlchemy()  # inicjalizacja bez powiązania z app (zrobimy to w app.py)

class EntryModel(db.Model):
    __tablename__ = 'Entries'
    id = db.Column(db.Integer, primary_key=True)
    personId = db.Column(db.Integer)
    data = db.Column(db.String(50), unique=True)
    place = db.Column(db.String(250), nullable=False)

    def set_Entry(self, personid,data,place):
        self.personId = personid
        self.data = data
        self.place = place

    def to_dict(self):
        return {
            "id": self.id,
            "personId": self.personId,
            "data": self.data,
            "place": self.place
        }