from models.entryModel import EntryModel
from models.SqlDB import db
from datetime import date

def handle(entry):
    entryData = EntryModel(person=entry.get('username'),
                           place=entry.get('place'),
                           data=str(date.today()))
    db.session.add(entryData)
    db.session.commit()
    return entryData.to_dict()