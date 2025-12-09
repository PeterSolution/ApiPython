from models.SqlDB import db

class EntersInRowModel(db.Model):
    __tablename__ = 'EntersInRow'
    userId = db.Column(db.Integer, primary_key=True, autoincrement=False)
    EntersInRow = db.Column(db.Integer)
    LastEdit = db.Column(db.String(50))

    def set_EntersInRow(self,userId, personid, LastEdit):
        self.userId = userId
        self.personId = personid
        self.LastEdit = LastEdit

    def to_dict(self):
        return {
            "userId": self.userId,
            "EntersInRow": self.EntersInRow,
            "LastEdit": self.LastEdit
        }