from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def echo(bot, update):
    logger.info('New update from "%s"' % (update.message.from_user.name))

    bot.sendMessage(update.message.chat_id, text=update.message.text)


def hello(bot, update):
    logger.info('New update from "%s"' % (update.message.from_user.name))

    text = 'Hello {}!'.format(update.message.from_user.first_name)
    bot.sendMessage(update.message.chat_id, text)


def sayhito(bot, update, args):
    logger.info('New update from "%s"' % (update.message.from_user.name))

    text = 'Hello {}!'.format(args[0])
    bot.sendMessage(update.message.chat_id, text)


updater = Updater('257076271:AAEsldoAW_1puD9Sv7zAGRjQ1qBbkJsBb60')

updater.dispatcher.add_handler(MessageHandler([Filters.text], echo))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('sayhito', sayhito, pass_args=True))

updater.start_polling()
updater.idle()