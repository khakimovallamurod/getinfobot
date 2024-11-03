import config

def is_admin(chat_id):
    admin_id = config.get_adminID()
    if admin_id == str(chat_id):
        return True
    return False

