from models.entryModel import EntryModel
from models.SqlDB import db
from datetime import datetime

def handle(entry):
    entryData = EntryModel(personId=entry.get('personId'),
                           place=entry.get('place'),
                           data=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    db.session.add(entryData)
    db.session.commit()
    return entryData.to_dict()