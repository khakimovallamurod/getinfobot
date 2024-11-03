from dotenv import load_dotenv
import os

load_dotenv()
def get_token():
    TOKEN = os.getenv('TOKEN')
    if TOKEN is None:
        raise ValueError("TOKEN not")
    return TOKEN

def get_adminID():
    adim_id = os.getenv('admin_id')
    if adim_id is None:
        raise ValueError('Admin ID not')
