from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, HTTP_CATS_URL
from datetime import datetime

def start(bot, update):
    response_message = "=^._.^="
 
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )
    print('Requerido por {name} as {time}'.format(name=update.effective_user.name,time=datetime.now().strftime('%d/%m/%Y, %H:%M:%S')))

def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=HTTP_CATS_URL + args[0]
    )

def unknown(bot, update):
    response_message = "Meow? =^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN,use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('http', http_cats, pass_args=True)
    )
    
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    
    main()
