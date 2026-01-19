from models.entersInRowModel import EntersInRowModel

def handle(user_id: int):
    entries_in_row = EntersInRowModel.query.filter_by(userId=user_id).all()
    if entries_in_row is None:
        return None
    else:
        return [entry.to_dict() for entry in entries_in_row]