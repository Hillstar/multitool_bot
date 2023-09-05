import telegram

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
    )

TOKEN = None

generate_report_cmd = "Сгенерировать Отчет \U0001F385"
help_cmd = "Помощь \U00002753"

buttons = [[KeyboardButton(generate_report_cmd), KeyboardButton(help_cmd)]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "SALAM",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))

#TODO
#def generate_report(context: CallbackContext):

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_info = (update.message.chat_id, str(update.message.from_user.first_name), str(update.message.from_user.username))

    if update.message.text == generate_report_cmd:
        await update.message.reply_text("Отчет готов \U0001F60E")

    elif update.message.text == help_cmd:
        await update.message.reply_text(
            "Чтобы сгенерировать отчет, нажми кнопку сгенерировать (это так сложно понять?)",
            reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
    else:
        await update.message.reply_text(
            "Прости, я не понимаю. Пользуйся кнопками, плз", 
            reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
  
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

def main() -> None:
    # Read token from file
    with open("token.txt") as f:
        TOKEN = f.read().strip()

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, message_handler))

    # Filters out unknown commands
    application.add_handler(MessageHandler(filters.COMMAND, unknown))  

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()