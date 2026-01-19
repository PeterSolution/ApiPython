from models.entersInRowModel import EntersInRowModel
from models.entryModel import EntryModel
from models.dataHelpModel import DataHelpModel
from models.user import User
from datetime import datetime
from models.SqlDB import db

def handle(user_id: int):
    entries_in_row = EntersInRowModel.query.filter_by(userId=user_id).first()
    
    if entries_in_row is None:
        return None
    else:
        if entries_in_row.LastEdit!=str(datetime.now().strftime("%Y-%m-%d")):
            u = User.query.get(user_id)
            u = u.to_dict()
            if entries_in_row.LastEdit is None:
                entries_in_row.EntersInRow=1
            # data = DataHelpModel(99, 99, 99)

            entries = EntryModel.query.filter_by(id=user_id).all()
            if entries is None:
                return None
            
            
            # else:
            #     return [entry.to_dict() for entry in entries]

            # for enters in entries:
            #     if str(enters.data[:10]) == str(datetime.now().strftime("%Y-%m-%d")):
            #         if data.hour > int(enters.data[11:13]):
            #             if data.min > int(enters.data[14:16]):
            #                 if data.sec > int(enters.data[17:19]):
            #                     data.setHour(int(enters.data[11:13]))
            #                     data.setMin(int(enters.data[14:16]))
            #                     data.setSec(int(enters.data[17:19]))
            # userhour,usermin = u.startWorkHour.split(":")
            # if data.hour<userhour and data.min<usermin:
            #     entries_in_row.EntersInRow+=1
            # else:
            #     entries_in_row.EntersInRow=0
            # entries_in_row.LastEdit=str(datetime.now().strftime("%Y-%m-%d"))
        today = datetime.now().date()

        # jeśli LastEdit istnieje → zamieniamy na date
        if entries_in_row.LastEdit:
            last_edit_date = datetime.strptime(entries_in_row.LastEdit, "%Y-%m-%d").date()
        else:
            last_edit_date = None

        # 1️⃣ LastEdit wcześniejszy niż dzisiaj (np. wczoraj)
        if last_edit_date and last_edit_date < today:
            entries_in_row.EntersInRow += 1

        # 2️⃣ LastEdit == dzisiaj
        elif last_edit_date == today:
            pass  # nic nie robimy z EntersInRow

        # 3️⃣ Inny przypadek (None albo przerwa)
        else:
            entries_in_row.EntersInRow = 1

        # zawsze aktualizujemy LastEdit
        entries_in_row.LastEdit = today.strftime("%Y-%m-%d")


        db.session.commit()
        return entries_in_row.to_dict()
