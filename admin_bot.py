from telegram.ext import CommandHandler, MessageHandler, filters, Application, CallbackQueryHandler
import config
import handlears

def main():
    TOKEN = config.get_token()
    dp = Application.builder().token(TOKEN).build()

    dp.add_handler(CommandHandler('start', handlears.start))
    dp.add_handler(CommandHandler('getnamuna', handlears.get_obektivka))
    dp.add_handler(CommandHandler('results', handlears.data_type_get))
    
    dp.add_handler(CallbackQueryHandler(handlears.get_type_with_results, pattern='type:'))

    dp.add_handler(MessageHandler(filters=filters.Document.DOC | filters.Document.DOCX, callback=handlears.save_doc_data))
    dp.run_polling()

if __name__ == '__main__':
    main()

