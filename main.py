from telegram.ext import Updater, CommandHandler
from keys import tk
from gitUser import git_api_user
from jokepon import jogar

def get_user_git(update, context):
    update.message.reply_text(git_api_user(context.args[0]))

def pedra(update, context):
    update.message.reply_text(jogar(1))
def papel(update, context):
    update.message.reply_text(jogar(2))
def tesoura(update, context):
    update.message.reply_text(jogar(3))

updater = Updater(tk, use_context=True)
updater.dispatcher.add_handler(CommandHandler('git', get_user_git))
updater.dispatcher.add_handler(CommandHandler('pedra', pedra))
updater.dispatcher.add_handler(CommandHandler('papel', papel))
updater.dispatcher.add_handler(CommandHandler('tesoura', tesoura))

updater.start_polling()
updater.idle()