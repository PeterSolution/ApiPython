from models.entryModel import EntryModel

def handle(page: int = 1, page_size: int = 20):
    entries_query = EntryModel.query.order_by(EntryModel.id).paginate(page=page, per_page=page_size)
    entries = entries_query.items
    return [entry.to_dict() for entry in entries]