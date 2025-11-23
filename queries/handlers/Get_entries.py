# from flask import jsonify
from models.entryModel import EntryModel

def handle():
    users = EntryModel.query.all()
#     return jsonify([u.to_dict() for u in users])
    return [u.to_dict() for u in users]

