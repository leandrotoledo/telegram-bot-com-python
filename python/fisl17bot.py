from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)


def hello(bot, update):
    text = 'Hello {}!'.format(update.message.from_user.first_name)
    bot.sendMessage(update.message.chat_id, text)


def sayhito(bot, update, args):
    text = 'Hello {}!'.format(args[0])
    bot.sendMessage(update.message.chat_id, text)


updater = Updater('257076271:AAEsldoAW_1puD9Sv7zAGRjQ1qBbkJsBb60')

updater.dispatcher.add_handler(MessageHandler([Filters.text], echo))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('sayhito', sayhito, pass_args=True))

updater.start_polling()
updater.idle()