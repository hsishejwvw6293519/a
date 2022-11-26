from telegram.ext import *



def st(u,c):
    u.message.reply_text("Welcome to this bot")

def up(u,c):
    f = str(c.bot.get_file(u.message.photo[-1]).download()))
    u.message.reply_text(f"Your File name is {f}")


up = Updater("5609178227:AAFukFJwF229CI9T0SetibLZBHpHx0T7Qh0", use_context=True)

up.dispatcher.add_handler(CommandHandler("start",st))
up.dispatcher.add_handler(MessageHandler(Filters.photo,up))


up.start_polling()
up.idle()
