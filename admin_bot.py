from telegram.ext import CommandHandler, MessageHandler, filters, Application, CallbackQueryHandler, ConversationHandler
import config
import handlears

def main():
    TOKEN = config.get_token()
    dp = Application.builder().token(TOKEN).build()

    dp.add_handler(CommandHandler('start', handlears.start))
    dp.add_handler(CommandHandler('getnamuna', handlears.get_obektivka))
    dp.add_handler(CommandHandler('results', handlears.data_type_get))
    user_register = ConversationHandler(
        entry_points=[CommandHandler('newobektv', handlears.user_register)],
        states={
            handlears.obektvka_data[0]: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlears.ask_name)],
            handlears.obektvka_data[1]: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlears.ask_work)],
            handlears.obektvka_data[2]: [MessageHandler(filters.TEXT, handlears.ask_year)], 
            handlears.obektvka_data[3]: [MessageHandler(filters.TEXT, handlears.ask_loaction)], 
            handlears.obektvka_data[4]: [MessageHandler(filters.TEXT, handlears.ask_millati)], 
            handlears.obektvka_data[5]: [MessageHandler(filters.TEXT, handlears.ask_partiyaviyligi)], 
            handlears.obektvka_data[6]: [MessageHandler(filters.TEXT, handlears.ask_malumoti)], 
            handlears.obektvka_data[7]: [MessageHandler(filters.TEXT, handlears.ask_tamomlagan)], 
            handlears.obektvka_data[8]: [MessageHandler(filters.TEXT, handlears.ask_mutaxasis)], 
            handlears.obektvka_data[9]: [MessageHandler(filters.TEXT, handlears.ask_unvon)], 
            handlears.obektvka_data[10]: [MessageHandler(filters.TEXT, handlears.ask_rank)], 
            handlears.obektvka_data[11]: [MessageHandler(filters.TEXT, handlears.ask_harbiy_unvon)], 
            handlears.obektvka_data[12]: [MessageHandler(filters.TEXT, handlears.ask_chettili)], 
            handlears.obektvka_data[13]: [MessageHandler(filters.TEXT, handlears.ask_davlat_mukofot)], 
            handlears.obektvka_data[14]: [MessageHandler(filters.TEXT, handlears.ask_yuqori_mansab)], 
            handlears.obektvka_data[15]: [MessageHandler(filters.PHOTO | filters.TEXT, handlears.ask_image)], 
            handlears.obektvka_data[16]: [MessageHandler(filters.TEXT, handlears.mahnat_faoliyat)], 
            handlears.obektvka_data[17]: [MessageHandler(filters.TEXT, handlears.relyativ_data)], 
        },
        fallbacks=[CommandHandler('cancel', handlears.cancel)]
    )
    dp.add_handler(user_register)

    dp.add_handler(CallbackQueryHandler(handlears.get_type_with_results, pattern='type:'))
    
    dp.add_handler(MessageHandler(filters=filters.Document.DOC | filters.Document.DOCX, callback=handlears.save_doc_data))
    dp.run_polling()

if __name__ == '__main__':
    main()

