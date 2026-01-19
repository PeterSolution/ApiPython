from models.SqlDB import db

class ImageModel(db.Model):
    __tablename__ = 'Images'
    id = db.Column(db.Integer, primary_key=True)
    entryId = db.Column(db.Integer)
    imagePath = db.Column(db.String(250), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "entryId": self.entryId,
            "imagePath": self.imagePath
        }