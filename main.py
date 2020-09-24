from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from keys import tk
from gitUser import git_api_user
from jokepon import jogar
from randomPics import getCats, getDogs, getFox, getGoats, getPoke
from comandos import listaComandos
bot = Bot(token=tk)


def get_user_git(update, context):
    if len(context.args) > 0:
        update.message.reply_text(git_api_user(context.args[0]))
    else:
        update.message.reply_text(
            "Para usar a função corretamente, envie seu nome de usuario\n ex: /git devgiordane")


def pedra(update, context):
    update.message.reply_text(jogar(1))


def papel(update, context):
    update.message.reply_text(jogar(2))


def tesoura(update, context):
    update.message.reply_text(jogar(3))


def add_group(update, context):
    for member in update.message.new_chat_members:
        update.message.reply_text(
            f"{update.message.from_user.first_name} seja muito bem vindo(a) ao nosso grupo! Eu sou o GioBot e estou aqui pra ajudar, você pode verificar o que eu faço digitando / \n \n \n Regras do grupo: \n Seja civilizado \n Respeite a dúvida do próximo \n")


def getDiscord(update, context):
    update.message.reply_text("Nosso discord: https://discord.gg/s8PEtvW")


def randomGoat(update, context):
    bot.send_photo(chat_id=update.message.chat_id, photo=getGoats())


def randomCat(update, context):
    bot.send_photo(chat_id=update.message.chat_id, photo=getCats())


def randomDog(update, context):
    bot.send_photo(chat_id=update.message.chat_id, photo=getDogs())


def randomFox(update, context):
    bot.send_photo(chat_id=update.message.chat_id, photo=getFox())


def randomPokemon(update, context):
    bot.send_photo(chat_id=update.message.chat_id, photo=getPoke())


def getComando(update, context):
    update.message.reply_text(listaComandos())


updater = Updater(tk, use_context=True)
updater.dispatcher.add_handler(CommandHandler('git', get_user_git))
updater.dispatcher.add_handler(CommandHandler('discord', getDiscord))
updater.dispatcher.add_handler(CommandHandler('pedra', pedra))
updater.dispatcher.add_handler(CommandHandler('papel', papel))
updater.dispatcher.add_handler(CommandHandler('tesoura', tesoura))
updater.dispatcher.add_handler(CommandHandler('goat', randomGoat))
updater.dispatcher.add_handler(CommandHandler('cat', randomCat))
updater.dispatcher.add_handler(CommandHandler('dog', randomDog))
updater.dispatcher.add_handler(CommandHandler('fox', randomFox))
updater.dispatcher.add_handler(CommandHandler('pokemon', randomPokemon))
updater.dispatcher.add_handler(CommandHandler('ajuda', getComando))
updater.dispatcher.add_handler(CommandHandler('help', getComando))
updater.dispatcher.add_handler(MessageHandler(
    Filters.status_update.new_chat_members, add_group))

updater.start_polling()
updater.idle()
