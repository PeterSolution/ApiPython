from models.entryModel import EntryModel
from datetime import datetime
from models.dataHelpModel import DataHelpModel


def handle(user_id: int):
    data = DataHelpModel(99, 99, 99)

    # Pobierz wszystkie wpisy dla użytkownika
    entries = EntryModel.query.filter_by(id=user_id).all()
    if entries is None:
        return None
    # else:
    #     return [entry.to_dict() for entry in entries]

    entry = entries[0]
    for enters in entries:
        if str(enters.data[:10]) == str(datetime.now().strftime("%Y-%m-%d")):
            if data.hour > int(enters.data[11:13]):
                if data.min > int(enters.data[14:16]):
                    if data.sec > int(enters.data[17:19]):
                        data.setHour(int(enters.data[11:13]))
                        data.setMin(int(enters.data[14:16]))
                        data.setSec(int(enters.data[17:19]))
                        entry = enters
    return entry.to_dict()
