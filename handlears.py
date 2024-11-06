from telegram import Update
from telegram.ext import CallbackContext
import db
from datetime import datetime
import keyboards

async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    if db.is_admin(user.id):
        await update.message.reply_text(
            text=f"""Assalomu aleykum {user.full_name}. Siz ushbu botda admin huqudiga egasiz. Mavjud ma'lumotnomalarni olish commandasi 👉 /results""",
        )
    else:
        await update.message.reply_text("Ma'lumotnomadan namuna olish 👉 /getnamuna")

async def get_obektivka(update: Update, context: CallbackContext):
    
    user = update.message.from_user
    if db.is_admin(user.id):
        await update.message.reply_document(
            document='BQACAgIAAxkBAAMVZyeqZ_Rnuj7WF9E6A25ByI0YgxMAAv8pAAKWMshKQXAQ5-IQH0c2BA', 
            caption="Bu siz yuklagan ma'lumotnoma namunasi")
    else:
        await update.message.reply_document(
            document='BQACAgIAAxkBAAMVZyeqZ_Rnuj7WF9E6A25ByI0YgxMAAv8pAAKWMshKQXAQ5-IQH0c2BA', 
            caption="Ushbu namuna kabi to'ldirishingiz kerak!")
    
async def save_doc_data(update: Update, context: CallbackContext):

    user = update.message.from_user
    file_id = update.message.document.file_id
    date_time = datetime.today().date()
    db.save_obektv(
        chat_id=user.id,
        username=user.username,
        file_id=file_id,
        date_time=date_time
        )
    await update.message.reply_text('✅ Sizning ma\'lumotingiz saqlandi!')
    
async def data_type_get(update: Update, context: CallbackContext):
    user = update.message.from_user
    if db.is_admin(user.id):
        await update.message.reply_text(text="Ma'lumotnomalarni olishning turini tanlang: ",
                                        reply_markup=keyboards.inline_keyboard)
    else:
         await update.message.reply_text(text="Siz admin emassiz. Bu admin uchun commanda!")
         
async def get_type_with_results(update: Update, context: CallbackContext):
    type_data = update.callback_query.data.split(':')[1]
    data = db.type_with_user_data(type=type_data)
    if data != []:
        for user in data:
            await update.callback_query.message.reply_document(
                document=user['file_id'],
                caption=f"👤 Username: @{user['username']}\n📅 Datetime: {user['date_time']}"
            )
    else:
        await update.callback_query.message.reply_text("Ushbu davrda yuborilgan ma'lumotnoma topilmadi!")
