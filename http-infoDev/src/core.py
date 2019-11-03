from datetime import datetime
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, RegexHandler
from conf.settings import TELEGRAM_TOKEN
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


def start(bot, update):


    msg = "Bem vindo a infoDev empresa fictícia!"
    msg += "\nEu sou a Sami e estou aqui para ajudar você.\n"
    msg += "O que você quer fazer?\n"
    '''msg += "/suporte - Ajuda técnicas\n"
    msg += "/conhecer - Conhecer a infoDev\n"
    msg += "/opcoes - Ir para nosso site ou fazer login\n"
    msg += "/fotinha - Ver uma fotinha fofinha"'''

    bot.send_message(
        chat_id=update.message.chat_id,
        text=msg
    )
    print('Requerido por {name} as {time}'.format(name=update.effective_user.name,time=datetime.now().strftime('%d/%m/%Y, %H:%M:%S')))

    menu_keyboard = [[KeyboardButton('Suporte')], ['Quem somos'], [
        'Outras Opções'], ['Fotinha']]
    menu_markup = ReplyKeyboardMarkup(
        menu_keyboard, one_time_keyboard=True, resize_keyboard=True)

    bot.send_message(update.message.chat_id,
                     text="Escolha uma opção",  reply_markup=menu_markup)

     
def start_settings_select(bot, update, groups):

    chat_id = update.message.chat_id
    option = groups[0]
    
    if option == 'Sup':
        bot.send_message(
            chat_id=update.message.chat_id,
            text='Em construção...'
        )
    
    elif option == 'Que':
        msg = "Somos uma empresa fictícia desenvolvida apenas para dar sentido a este bot.\n"
        msg += "\nConheça outras opções\n"

        main_menu_keyboard = [[KeyboardButton('Nível 1')],
                              [KeyboardButton('Nível 2')],
                              [KeyboardButton('Nível 3')],
                              [KeyboardButton('Nível 4')],
                              [KeyboardButton('Nível 5')]
                              ]
        reply_kb_markup = ReplyKeyboardMarkup(main_menu_keyboard,
                                              resize_keyboard=True,
                                              one_time_keyboard=True)
        bot.send_message(chat_id=update.message.chat_id,
                         text=msg,
                         reply_markup=reply_kb_markup)
    elif option == 'Out':
        keyboard = []
        keyboard.append([InlineKeyboardButton(
            'Ir para site', 'https://motivaai.nandomoreira.me/', callback_data='1')])
        keyboard.append([InlineKeyboardButton(
            'Fazer Login', 'https://www.linkedin.com/', callback_data='2')])
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            'Escolha uma opção:',  reply_markup=reply_markup)
   
    elif option == 'Fot':
        bot.sendPhoto(
            chat_id=update.message.chat_id,
            photo="https://abrilmdemulher.files.wordpress.com/2016/10/meme-cc3a3o-feliz.jpg?quality=90&strip=info&w=600&h=886"
        )
    
    else:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Comando inválido"
        )

def quemSomos(bot, update):

    msg = "Somos uma empresa fictícia desenvolvida apenas para dar sentido a este bot.\n"
    msg += "\nConheça outras opções\n"

    main_menu_keyboard = [[KeyboardButton('Nível 1')],
                              [KeyboardButton('Nível 2')],
                              [KeyboardButton('Nível 3')],
                              [KeyboardButton('Nível 4')],
                              [KeyboardButton('Nível 5')]
                              ]
    reply_kb_markup = ReplyKeyboardMarkup(main_menu_keyboard,
                                          resize_keyboard=True,
                                          one_time_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)

def opcoes(bot, update):

    keyboard = []
    keyboard.append([InlineKeyboardButton(
        'Ir para site', 'https://motivaai.nandomoreira.me/', callback_data='1')])
    keyboard.append([InlineKeyboardButton(
        'Fazer Login', 'https://www.linkedin.com/', callback_data='2')])
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Escolha uma opção:',  reply_markup=reply_markup)

def enviaFoto(bot, update):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo="https://abrilmdemulher.files.wordpress.com/2016/10/meme-cc3a3o-feliz.jpg?quality=90&strip=info&w=600&h=886"
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('conhecer', quemSomos))
    dispatcher.add_handler(CommandHandler('foto', enviaFoto))
    dispatcher.add_handler(CommandHandler('opcoes', opcoes))

    get_option_start_handler = RegexHandler('^([A-Z]{1}[a-z]{2}).*',
                                            start_settings_select,
                                            pass_groups=True)

    dispatcher.add_handler(get_option_start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
