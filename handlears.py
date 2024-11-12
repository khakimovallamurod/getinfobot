from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
import db
from datetime import datetime
import keyboards
import py_to_doc

async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    if db.is_admin(user.id):
        await update.message.reply_text(
            text=f"""Assalomu aleykum {user.full_name}. Siz ushbu botda admin huqudiga egasiz. Mavjud ma'lumotnoma to'ldirish commandasi 👉 /newobektv""",
        )
    else:
        await update.message.reply_text(f"Assalomu aleykum {user.full_name}. Ma'lumotnoma to'ldirish commandasi 👉 /newobektv")

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
USER_DATA = {}
obektvka_data = list(range(19))
async def user_register(update: Update, context: CallbackContext):
    await update.message.reply_text("Familya, Ism va Otangizning ismi: ")
    return obektvka_data[0]

async def ask_name(update: Update, context: CallbackContext):
    USER_DATA["name"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Hozirgi vaqtda ish lavozimingiz va qachondan: """)
    return obektvka_data[1]
async def ask_work(update: Update, context: CallbackContext):
    USER_DATA["work"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Tu'gilgan yili (dd.mm.yy): """)
    return obektvka_data[2]

async def ask_year(update: Update, context: CallbackContext):
    USER_DATA["year"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Tug'ilgan joyi: """)
    return obektvka_data[3]

async def ask_loaction(update: Update, context: CallbackContext):
    USER_DATA["loaction"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Millati: """)
    return obektvka_data[4]

async def ask_millati(update: Update, context: CallbackContext):
    USER_DATA["millati"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Partiyaviyligi (Yo'q): """)
    return obektvka_data[5]

async def ask_partiyaviyligi(update: Update, context: CallbackContext):
    USER_DATA["partiyaviy"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Malumoti: """)
    return obektvka_data[6]

async def ask_malumoti(update: Update, context: CallbackContext):
    USER_DATA["malumoti"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Tamomlagan(To'liq): """)
    return obektvka_data[7]
async def ask_tamomlagan(update: Update, context: CallbackContext):
    USER_DATA["tamomlagan"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Ma'lumoti bo'yicha mutaxassisligi: """)
    return obektvka_data[8]
async def ask_mutaxasis(update: Update, context: CallbackContext):
    USER_DATA["mutaxasis"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Ilmiy unvoni (Yo'q): """)
    return obektvka_data[9]

async def ask_unvon(update: Update, context: CallbackContext):
    USER_DATA["unvon"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Ilmiy darajasi: """)
    return obektvka_data[10]

async def ask_rank(update: Update, context: CallbackContext):
    USER_DATA["rank"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Xarbiy (maxsus) unvoni (Yo'q): """)
    return obektvka_data[11]

async def ask_harbiy_unvon(update: Update, context: CallbackContext):
    USER_DATA["xunvon"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Qaysi chet tillarni biladi: """)
    return obektvka_data[12]

async def ask_chettili(update: Update, context: CallbackContext):
    USER_DATA["chettili"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Davlat mukofatlari bilan taqdirlanganmi (qanaqa): """)
    return obektvka_data[13]

async def ask_davlat_mukofot(update: Update, context: CallbackContext):
    USER_DATA["medal"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Xalq deputatlari, respublika, viloyat, shahar va tuman Kengashi deputatimi yoki boshqa saylangan organlarning azosimi (to'liq ko'rsatilishi lozim): """)
    return obektvka_data[14]

async def ask_yuqori_mansab(update: Update, context: CallbackContext):
    USER_DATA["yuqorimansab"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Rasm 3x4 formatda bo'lsin: """)
    return obektvka_data[15]

async def ask_image(update: Update, context: CallbackContext):
    if update.message.photo:
        file_id = update.message.photo[-1].file_id 
        file = await context.bot.get_file(file_id)

        image_path = 'downloaded_image.jpg'
        await file.download_to_drive(image_path)
        USER_DATA["image"] = image_path
        await update.message.reply_text(f"""MEHNAT FAOLIYAT ingizni kiriting va har birini yangi qator bilan yozing!\n.....\n..... """)
        return obektvka_data[16]
    else:
        await update.message.reply_text("""Iltimos rasm 3x4 formatda yuboring: """)
        return obektvka_data[15]

async def mahnat_faoliyat(update: Update, context: CallbackContext):
    USER_DATA["mehnatfaoliyat"] = update.message.text.strip().capitalize()
    await update.message.reply_text("""Yaqin qarindoshlaringizni Namunadek kiritishingiz shart!\nNamuna: Qarindoshligi : Familyasi, ismi va otasining ismi : Tug'ilgan yili va joyi : Ish joyi va lavozimi : Turar joyi\n Keyingilarini yangi qatordan yozing .....! """)
    return obektvka_data[17]

async def relyativ_data(update: Update, context: CallbackContext):
    text = update.message.text.strip().split('\n')
    total = 0
    for item in text:
        t = item.split(':')
        if len(t) == 5:
            total += 1
    if len(text)==total:
        USER_DATA["yaqinqarindosh"] = update.message.text.strip()

        full_name = USER_DATA['name']
        py_to_doc.control(USER_DATA)
        await update.message.reply_document(document=open(f'{full_name}.docx', 'rb'), caption="Sizning shaxsiy ma'lumotnomangiz")
        return ConversationHandler.END
    else:
        await update.message.reply_text("""❌Xato!\nNamuna: Qarindoshligi : Familyasi, ismi va otasining ismi : Tug'ilgan yili va joyi : Ish joyi va lavozimi : Turar joyi\n Keyingilarini yangi qatordan yozing .....! """)
        return obektvka_data[17]



async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text('Amalyot bajarilmadi!')
    return ConversationHandler.END
