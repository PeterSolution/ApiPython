from models.entersInRowModel import EntersInRowModel
from models.SqlDB import db
from datetime import datetime

def handle(user_id: int):
    if EntersInRowModel.query.filter_by(userId=user_id).first() is not None:
        return None
    new_entry = EntersInRowModel(
        userId=user_id,
        EntersInRow=1,
        LastEdit=str(datetime.now().strftime("%Y-%m-%d"))
    )
    db.session.add(new_entry)
    db.session.commit()
    return new_entry.to_dict()