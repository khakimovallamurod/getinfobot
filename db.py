import config
from tinydb import TinyDB
from tinydb.database import Document
from datetime import datetime, timedelta

user_datas = TinyDB('datas.json', indent = 4)

user_data = user_datas.table('User_Datas')

def is_admin(chat_id):
    admin_id = config.get_adminID()
    if admin_id == str(chat_id):
        return True
    return False

def save_obektv(chat_id, username, file_id, date_time):
    user_data.insert({
        'username': username,
        'file_id': file_id,
        'date_time': str(date_time)
    })

def get_daily():
    date_time = datetime.today().date()
    datas_all = user_data.all()
    data = []
    for user in datas_all:
        date_obk = user['date_time']
        if date_obk == str(date_time):
            data.append(user)

    return data
def get_weekly():
    week_date = datetime.now().date() - timedelta(days=datetime.now().weekday())
    datas_all = user_data.all()
    data = []
    for user in datas_all:
        date_obk = datetime.fromisoformat(user['date_time'])
        if week_date <= date_obk.date() <= week_date + timedelta(days=7):
            data.append(user)
    return data
  
def get_monthly():
    monthly_date = datetime.now().date() - timedelta(days=datetime.now().day)
    datas_all = user_data.all()
    data = []
    for user in datas_all:
        date_obk = datetime.fromisoformat(user['date_time'])
        if monthly_date <= date_obk.date() <= monthly_date + timedelta(days=30):
            data.append(user)
    return data
def get_all():
    datas_all = user_data.all()
    data = []
    for user in datas_all:
        data.append(user)
    return data

def type_with_user_data(type):
    if type == 'daily':
        data = get_daily()
    elif type == 'weekly':
        data = get_weekly()
    elif data == 'monthly':
        data = get_monthly()
    else:
        data = get_all()
    return data
